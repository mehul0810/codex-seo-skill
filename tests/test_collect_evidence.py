import pathlib
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(pathlib.Path(__file__).parents[1] / "seo-positioning-optimizer" / "scripts"))
import collect_evidence


class Response:
    def __init__(self, status=200, body=b"", headers=None):
        self.status = status
        self._body = body
        self.headers = headers or {}
        self.closed = False

    def read(self, size=-1):
        return self._body[:size]

    def close(self):
        self.closed = True


class ReadFailure(Response):
    def read(self, size=-1):
        raise TimeoutError("read timed out")


class Opener:
    def __init__(self, responses):
        self.responses = iter(responses)
        self.calls = []

    def open(self, request, timeout):
        self.calls.append((request.full_url, timeout))
        response = next(self.responses)
        if isinstance(response, Exception):
            raise response
        return response


class CollectorTests(unittest.TestCase):
    URL = "https://example.test/page"

    def test_html_metadata_heading_base_link_and_jsonld(self):
        source = b'''<html><head><base href="/docs/"><title> Sample\n Title </title>
        <meta name="description" content="first"><meta name="description" content="second">
        <meta name="robots" content="noindex"><link rel="canonical" href="canonical">
        <script type="application/ld+json">{"@type":"Thing"}</script>
        <script type="application/ld+json">{broken}</script></head>
        <body><h1>Outer <em>nested</em>\n heading</h1><a href="child">See <b>more</b></a></body></html>'''
        evidence = collect_positioning(source)
        self.assertEqual(evidence["title"], "Sample Title")
        self.assertEqual(evidence["meta_descriptions"], ["first", "second"])
        self.assertEqual(evidence["canonicals"], ["https://example.test/docs/canonical"])
        self.assertEqual(evidence["headings"], [{"level": "1", "text": "Outer nested heading"}])
        self.assertEqual(evidence["links"], [{"href": "https://example.test/docs/child", "text": "See more"}])
        self.assertEqual(evidence["json_ld"][0]["data"], {"@type": "Thing"})
        self.assertIsNotNone(evidence["json_ld"][1]["error"])

    def test_document_title_is_not_overwritten_by_svg_or_body_titles(self):
        source = b'''<html><head><title>AI features and your website</title>
        <title>Duplicate head title</title></head><body>
        <svg role="img"><title>Google</title><path d="M0 0"/></svg>
        <title>Body title</title><h1>AI features</h1></body></html>'''
        evidence = collect_positioning(source)
        self.assertEqual(evidence["title"], "AI features and your website")
        self.assertEqual(evidence["headings"], [{"level": "1", "text": "AI features"}])

    def test_svg_and_body_titles_are_not_document_titles(self):
        for source in (
            b'<html><head></head><body><svg><title>Logo</title></svg></body></html>',
            b'<html><body><title>Body title</title></body></html>',
            b'<svg><title>Logo</title></svg>',
        ):
            with self.subTest(source=source):
                self.assertIsNone(collect_positioning(source)["title"])

    def test_headless_fragment_retains_first_non_foreign_title(self):
        source = b'<svg><title>Logo</title></svg><title>Document</title><title>Later</title>'
        self.assertEqual(collect_positioning(source)["title"], "Document")

    def test_base_after_canonical_applies_globally_and_empty_canonical_is_retained(self):
        evidence = collect_positioning(b'<link rel="canonical" href="canonical"><base href="/base/"><link rel="canonical">')
        self.assertEqual(evidence["canonicals"], ["https://example.test/base/canonical", ""])

    def test_offline_does_not_claim_js_shell_has_rendered_headings(self):
        result = collect_evidence.collect([self.URL], offline_html=b'<div id="app"></div><script>render()</script>')
        self.assertFalse(result["raw_html_rendered"])
        self.assertEqual(result["results"][0]["evidence"]["headings"], [])

    def test_truncated_document_fields_are_unknown(self):
        opener = Opener([Response(body=b"<title>Too large</title>", headers={"Content-Type": "text/html"})])
        with patch.object(collect_evidence, "public_target"):
            result = collect_evidence.collect([self.URL], opener=opener, max_body=5)
        self.assertTrue(result["results"][0]["truncated"])
        self.assertIsNone(result["results"][0]["evidence"]["title"])

    def test_offline_windows_1252_meta_charset_is_honored(self):
        source = '<meta charset="windows-1252"><title>caf\xe9</title>'.encode("cp1252")
        result = collect_evidence.collect([self.URL], offline_html=source)
        evidence = result["results"][0]["evidence"]
        self.assertEqual(evidence["title"], "caf\u00e9")
        self.assertEqual(evidence["decoding"]["encoding"], "cp1252")
        self.assertEqual(evidence["decoding"]["source"], "html_declaration")
        self.assertEqual(evidence["decoding"]["warnings"], [])

    def test_offline_http_equiv_charset_is_honored(self):
        source = '<meta http-equiv="Content-Type" content="text/html; charset=windows-1252"><h1>caf\xe9</h1>'.encode("cp1252")
        result = collect_evidence.collect([self.URL], offline_html=source)
        evidence = result["results"][0]["evidence"]
        self.assertEqual(evidence["headings"][0]["text"], "caf\u00e9")
        self.assertEqual(evidence["decoding"]["source"], "html_declaration")

    def test_network_http_charset_and_bom_precedence(self):
        response = Response(body=b"<title>caf\xe9</title>", headers={"Content-Type": "text/html; charset=windows-1252"})
        with patch.object(collect_evidence, "public_target"):
            item = collect_evidence.collect([self.URL], opener=Opener([response]))["results"][0]
        self.assertEqual(item["evidence"]["title"], "caf\u00e9")
        self.assertEqual(item["evidence"]["decoding"]["source"], "http_content_type")

        bom_response = Response(body=b"\xef\xbb\xbf<title>caf\xc3\xa9</title>", headers={"Content-Type": "text/html; charset=windows-1252"})
        with patch.object(collect_evidence, "public_target"):
            item = collect_evidence.collect([self.URL], opener=Opener([bom_response]))["results"][0]
        self.assertEqual(item["evidence"]["title"], "caf\u00e9")
        self.assertEqual(item["evidence"]["decoding"]["source"], "byte_order_mark")

    def test_invalid_charset_uses_utf8_fallback_with_warning(self):
        evidence = collect_evidence.parse_html(b'<meta charset="x-not-real"><title>caf\xc3\xa9</title>', self.URL)
        self.assertEqual(evidence["title"], "caf\u00e9")
        self.assertEqual(evidence["decoding"]["encoding"], "utf-8")
        self.assertEqual(evidence["decoding"]["source"], "utf-8_fallback")
        self.assertTrue(any("charset" in warning.lower() for warning in evidence["decoding"]["warnings"]))

        lossy = collect_evidence.parse_html(b"<meta charset=utf-8><title>bad: \xff</title>", self.URL)
        self.assertIn("\ufffd", lossy["title"])
        self.assertTrue(any("replacement characters" in warning for warning in lossy["decoding"]["warnings"]))

    def test_non_text_and_problematic_registered_codecs_do_not_abort_batch(self):
        labels = ("rot_13", "base64_codec", "hex_codec", "punycode", "undefined", "x-not-real", "utf-7", "unicode_escape", "idna")
        responses = [
            Response(200, b"<title>OK</title>", {"Content-Type": f"text/html; charset={label}"})
            for label in labels
        ]
        urls = [f"https://example.test/{index}" for index in range(len(labels))]
        with patch.object(collect_evidence, "public_target"):
            result = collect_evidence.collect(urls, opener=Opener(responses))
        self.assertEqual(len(result["results"]), len(labels))
        for item in result["results"]:
            self.assertIsNone(item["error"])
            self.assertEqual(item["evidence"]["title"], "OK")
            self.assertEqual(item["evidence"]["decoding"]["encoding"], "utf-8")
            self.assertEqual(item["evidence"]["decoding"]["source"], "utf-8_fallback")
            self.assertTrue(any("Unsupported or non-text charset" in warning for warning in item["evidence"]["decoding"]["warnings"]))

    def test_unsupported_meta_charsets_preserve_utf8_content(self):
        for label in ("punycode", "rot_13", "utf-7", "unicode_escape", "idna"):
            with self.subTest(label=label):
                source = f'<meta charset="{label}"><title>caf\u00e9</title>'.encode("utf-8")
                evidence = collect_positioning(source)
                self.assertEqual(evidence["title"], "caf\u00e9")
                self.assertEqual(evidence["decoding"]["encoding"], "utf-8")
                self.assertEqual(evidence["decoding"]["source"], "utf-8_fallback")
                self.assertTrue(evidence["decoding"]["warnings"])

    def test_supported_text_encoding_aliases_preserve_titles(self):
        for label, title in (("UTF8", "caf\u00e9"), ("latin-1", "caf\u00e9"), ("Shift-JIS", "\u65e5\u672c"), ("GB18030", "\u4e2d\u6587")):
            with self.subTest(label=label):
                source = f'<meta charset="{label}"><title>{title}</title>'.encode(label)
                evidence = collect_positioning(source)
                self.assertEqual(evidence["title"], title)
                self.assertEqual(evidence["decoding"]["source"], "html_declaration")
                self.assertEqual(evidence["decoding"]["warnings"], [])

    def test_redirect_limit_is_reported_without_following_sixth_redirect(self):
        responses = [Response(302, headers={"Location": f"/step-{index}"}) for index in range(1, 7)]
        opener = Opener(responses)
        with patch.object(collect_evidence, "public_target"):
            record = collect_evidence.fetch(self.URL, opener=opener)
        self.assertIn("redirect limit exceeded", record["error"])
        self.assertEqual(len(opener.calls), collect_evidence.MAX_REDIRECTS + 1)
        self.assertTrue(all(response.closed for response in responses))

    def test_redirect_chain_and_final_headers(self):
        first = Response(302, headers={"Location": "/final"})
        second = Response(200, b"ok", {"Content-Type": "text/plain", "X-Robots-Tag": "noindex"})
        opener = Opener([first, second])
        with patch.object(collect_evidence, "public_target"):
            record = collect_evidence.fetch(self.URL, opener=opener)
        self.assertEqual(record["redirect_chain"], ["https://example.test/final"])
        self.assertEqual(record["final_url"], "https://example.test/final")
        self.assertEqual(record["x_robots_tag"], "noindex")
        self.assertTrue(first.closed)
        self.assertTrue(second.closed)

    def test_private_redirect_is_rejected_without_requesting_target(self):
        opener = Opener([Response(302, headers={"Location": "http://127.0.0.1/internal"})])
        with patch.object(collect_evidence, "public_target", side_effect=[None, ValueError("private target")]) as guard:
            record = collect_evidence.fetch(self.URL, opener=opener)
        self.assertIn("private target", record["error"])
        self.assertEqual(len(opener.calls), 1)
        self.assertEqual(guard.call_count, 2)

    def test_read_failure_is_recorded_and_batch_continues(self):
        opener = Opener([ReadFailure(headers={"Content-Type": "text/html"}), Response(200, b"ok", {"Content-Type": "text/plain"})])
        with patch.object(collect_evidence, "public_target"):
            result = collect_evidence.collect([self.URL, "https://example.test/second"], opener=opener)
        self.assertIn("response read failed: read timed out", result["results"][0]["error"])
        self.assertTrue(opener.responses is not None)
        self.assertEqual(result["results"][1]["status"], 200)
        self.assertEqual(len(opener.calls), 2)

    def test_unsupported_type_and_malformed_xml_are_not_interpreted_as_pages(self):
        opener = Opener([
            Response(200, b"binary", {"Content-Type": "application/octet-stream"}),
            Response(200, b"<sitemapindex>", {"Content-Type": "application/xml"}),
            Response(200, b"<html><h1>X</h1></html>", {"Content-Type": "application/xhtml+xml"}),
        ])
        with patch.object(collect_evidence, "public_target"):
            result = collect_evidence.collect(["https://example.test/a", "https://example.test/b.xml", "https://example.test/c"], opener=opener)
        self.assertIsNone(result["results"][0]["sitemaps"])
        self.assertEqual(result["results"][1]["sitemaps"]["kind"], None)
        self.assertEqual(result["results"][2]["evidence"]["headings"], [{"level": "1", "text": "X"}])

    def test_http_error_statuses_are_reported_not_parsed_as_success(self):
        for status in (403, 404):
            opener = Opener([Response(status, b"blocked", {"Content-Type": "text/html"})])
            with patch.object(collect_evidence, "public_target"):
                item = collect_evidence.collect([self.URL], opener=opener)["results"][0]
            self.assertEqual(item["status"], status)
            self.assertIsNone(item["evidence"]["title"])

    def test_sitemap_html_masquerade_is_not_parsed_as_xml(self):
        opener = Opener([Response(body=b"<html><body>not sitemap</body></html>", headers={"Content-Type": "text/html"})])
        with patch.object(collect_evidence, "public_target"):
            item = collect_evidence.collect(["https://example.test/sitemap.xml"], opener=opener)["results"][0]
        self.assertEqual(item["evidence"]["title"], None)
        self.assertIsNone(item["sitemaps"])

    def test_robots_declarations_and_xml_index_entries(self):
        self.assertEqual(collect_evidence.parse_robots(b"User-agent: *\nSitemap: https://example.test/sitemap.xml\n"), ["https://example.test/sitemap.xml"])
        parsed = collect_evidence.parse_sitemap(b'<sitemapindex><sitemap><loc>https://example.test/a.xml</loc></sitemap></sitemapindex>')
        self.assertEqual(parsed["kind"], "sitemapindex")
        self.assertEqual(parsed["entries"], ["https://example.test/a.xml"])
        rejected = collect_evidence.parse_sitemap(b'<!DOCTYPE x [<!ENTITY y "z">]><urlset/>')
        self.assertIn("not allowed", rejected["xml_error"])
        urlset = collect_evidence.parse_sitemap(b'<urlset xmlns:image="urn:image"><url><loc>https://example.test/a&amp;b</loc><image:loc>https://example.test/image</image:loc></url></urlset>')
        self.assertEqual(urlset["entries"], ["https://example.test/a&b"])

    def test_rejects_unsafe_or_credentialed_urls_and_more_than_ten(self):
        for url in ("file:///etc/passwd", "https://u:p@example.test/"):
            with self.assertRaises(ValueError):
                collect_evidence.validate_url(url)
        with patch.object(collect_evidence.socket, "getaddrinfo", return_value=[(None, None, None, None, ("127.0.0.1", 0))]):
            with self.assertRaises(ValueError):
                collect_evidence.public_target(self.URL)
        with self.assertRaises(ValueError):
            collect_evidence.collect([self.URL] * 11)


def collect_positioning(source):
    return collect_evidence.parse_html(source, "https://example.test/page")


if __name__ == "__main__":
    unittest.main()
