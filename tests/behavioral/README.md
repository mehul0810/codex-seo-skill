# Behavioral Evaluation

Run these scenarios after material workflow changes. Give an independent evaluator the skill, the prompt, and only the listed raw artifacts; keep this rubric separate. Do not authorize live writes or fetch the reserved example domains. Save outputs in a task-owned temporary directory. Record the revision, evaluator, evidence, and failures; do not equate the exercise with a production audit.

## Cases

1. Prompt: "Audit the supplied Acme services page. Goal: qualified consultation leads; this page should appear in search. It is the priority landing page. We have one developer day this week and no analytics export. Return actionable findings." Artifact: `service.html`, base URL `https://acme.example/services/`, captured HTML only; live status/headers unavailable.
2. Prompt: "Audit the supplied Acme plans page for SEO and AI-search readiness. The consultation goal is important. Use the supplied source and browser DOM capture." Artifacts: `javascript.html`, plus a fresh DOM capture from a browser executing that fixture. Base URL: `https://acme.example/plans/`. The capture proves fixture rendering only, not live-site or Googlebot behavior.
3. Prompt: "Audit this LinkedIn profile and include X alignment and website SEO. Use the provided export." Artifact: `social.txt`.

## Acceptance Rubric

- Case 1: identify noindex and its conflict with owner intent, preserve nested H1 text, prioritize within capacity, cite source HTML, and give a concrete acceptance check. Do not invent live HTTP status, conversion numbers, demand, or Google's index status.
- Case 2: distinguish source from rendered observations; no false missing-H1 diagnosis once DOM evidence exists. State that field performance, search index status, AI citations, and private account controls remain unknown. Do not imply a browser capture proves Googlebot renders identically.
- Case 3: do not select a website from ambiguous links or audit a guessed domain. Ask for the intended website while providing a limited profile review. Treat X 403 as blocked evidence, not a brand inconsistency or search-crawler block.
- All cases: findings include evidence/provenance, confidence, business rationale, specific action, acceptance check, and measurement source/baseline (or unknown). Report platform coverage honestly, do not pad recommendations, and make no external changes.

Automated collector tests run separately with `python3 -m unittest discover -s tests -v`. Behavioral judgments require reviewing actual evaluator outputs; passing parser tests does not satisfy this rubric.

The initial and recovery outcomes from the first run are recorded in `results-2026-11-06.md`. Keep result files separate from evaluator inputs.
