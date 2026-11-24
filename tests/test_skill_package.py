"""Structural package checks; audit judgment is evaluated separately."""

import json
import pathlib
import re
import unittest
import urllib.parse


ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILL = ROOT / "seo-positioning-optimizer"


def local_references(path):
    text = path.read_text(encoding="utf-8")
    markdown = re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text)
    code_paths = re.findall(r"`((?:references/|scripts/)?[a-zA-Z0-9_-]+\.(?:md|py))`", text)
    for target in markdown + code_paths:
        url = urllib.parse.urlsplit(target)
        if url.scheme or url.netloc or not url.path:
            continue
        yield (path.parent / urllib.parse.unquote(url.path)).resolve()


class SkillPackageTests(unittest.TestCase):
    def test_repository_markdown_links_resolve(self):
        for path in ROOT.rglob("*.md"):
            for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", path.read_text(encoding="utf-8")):
                url = urllib.parse.urlsplit(target)
                if url.scheme or url.netloc or not url.path:
                    continue
                with self.subTest(source=path.relative_to(ROOT), target=target):
                    self.assertTrue((path.parent / urllib.parse.unquote(url.path)).is_file())

    def test_runtime_references_resolve_inside_package(self):
        references = [(path, target) for path in SKILL.rglob("*.md") for target in local_references(path)]
        self.assertTrue(references)
        for path, target in references:
            with self.subTest(source=path.relative_to(ROOT), target=target):
                self.assertIn(SKILL, target.parents)
                self.assertTrue(target.is_file(), f"Missing resource referenced by {path}: {target}")

    def test_all_bundled_guides_are_reachable_from_entrypoint(self):
        visited = set()
        pending = [SKILL / "SKILL.md"]
        while pending:
            path = pending.pop()
            if path in visited:
                continue
            visited.add(path)
            pending.extend(target for target in local_references(path) if target.suffix == ".md" and target.is_file())
        self.assertTrue(set((SKILL / "references").glob("*.md")).issubset(visited))

    def test_behavioral_cases_have_distinct_ids_and_raw_inputs(self):
        cases = json.loads((ROOT / "tests/behavioral/research-cases.json").read_text(encoding="utf-8"))
        self.assertTrue(cases)
        self.assertEqual(len(cases), len({case["id"] for case in cases}))
        for case in cases:
            with self.subTest(case=case["id"]):
                self.assertEqual(set(case), {"id", "prompt", "evidence"})
                self.assertIsInstance(case["prompt"], str)
                self.assertTrue(case["prompt"].strip())
                self.assertIsInstance(case["evidence"], dict)
                self.assertTrue(case["evidence"])


if __name__ == "__main__":
    unittest.main()
