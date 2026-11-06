#!/usr/bin/env python3
"""Collect bounded, raw-HTML SEO evidence without scoring or recommendations."""

from __future__ import annotations

import argparse
import codecs
import datetime as dt
import ipaddress
import json
import re
import socket
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from typing import Any

MAX_URLS = 10
MAX_BODY = 2_000_000
TIMEOUT = 10
MAX_REDIRECTS = 5
USER_AGENT = "SEO-Evidence-Collector/1.0"
# Deliberately bounded text encodings, not every transform in Python's registry.
HTML_TEXT_ENCODINGS = {
    "ascii", "utf-8", "utf-8-sig", "utf-16", "utf-16-le", "utf-16-be",
    "utf-32", "utf-32-le", "utf-32-be", "cp874", "koi8-r", "koi8-u",
    "mac-roman", "mac-cyrillic", "shift_jis", "cp932", "euc_jp",
    "iso2022_jp", "euc_kr", "cp949", "gb2312", "gbk", "gb18030",
    "big5", "big5hkscs",
} | {f"cp{number}" for number in range(1250, 1259)} | {
    f"iso8859-{number}" for number in (*range(1, 12), *range(13, 17))
}


def validate_url(url: str) -> urllib.parse.SplitResult:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme.lower() not in {"http", "https"} or not parsed.hostname:
        raise ValueError("URL must use HTTP or HTTPS and include a hostname")
    if parsed.username is not None or parsed.password is not None:
        raise ValueError("URL credentials are not allowed")
    return parsed


def public_target(url: str) -> None:
    """Best-effort network-target guard; DNS can change between check and connect."""
    parsed = validate_url(url)
    host = parsed.hostname or ""
    try:
        addresses = [ipaddress.ip_address(host.split("%", 1)[0])]
    except ValueError:
        try:
            addresses = [ipaddress.ip_address(item[4][0]) for item in socket.getaddrinfo(host, parsed.port or (443 if parsed.scheme == "https" else 80), type=socket.SOCK_STREAM)]
        except OSError as exc:
            raise ValueError(f"host lookup failed: {exc}") from exc
    if not addresses or any(not address.is_global for address in addresses):
        raise ValueError("private, loopback, link-local, or otherwise non-public targets are not allowed")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def fetch(url: str, *, opener: Any = None, timeout: int = TIMEOUT, max_body: int = MAX_BODY) -> dict[str, Any]:
    chain: list[str] = []
    current = url
    # Do not inherit ambient proxy configuration or credentials from the environment.
    opener = opener or urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    for _ in range(MAX_REDIRECTS + 1):
        try:
            public_target(current)
            request = urllib.request.Request(current, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml,application/xml,text/plain,*/*;q=0.1"})
            response = opener.open(request, timeout=timeout)
        except urllib.error.HTTPError as exc:
            response = exc
        except Exception as exc:
            return {"requested_url": url, "final_url": current, "status": None, "redirect_chain": chain, "content_type": None, "x_robots_tag": None, "error": str(exc), "truncated": False, "body": b""}
        status = getattr(response, "status", None)
        if status is None:
            status = response.getcode()
        headers = response.headers
        location = headers.get("Location")
        if status in {301, 302, 303, 307, 308} and location:
            next_url = urllib.parse.urljoin(current, location)
            try:
                if len(chain) >= MAX_REDIRECTS:
                    return {"requested_url": url, "final_url": current, "status": status, "redirect_chain": chain + [next_url], "content_type": headers.get("Content-Type"), "x_robots_tag": headers.get("X-Robots-Tag"), "error": "redirect limit exceeded", "truncated": False, "body": b""}
                public_target(next_url)
                current = next_url
                chain.append(current)
            except Exception as exc:
                return {"requested_url": url, "final_url": current, "status": status, "redirect_chain": chain + [next_url], "content_type": headers.get("Content-Type"), "x_robots_tag": headers.get("X-Robots-Tag"), "error": str(exc), "truncated": False, "body": b""}
            finally:
                close = getattr(response, "close", None)
                if close:
                    close()
            continue
        try:
            body = response.read(max_body + 1)
        except Exception as exc:
            return {"requested_url": url, "final_url": current, "status": status, "redirect_chain": chain, "content_type": headers.get("Content-Type"), "x_robots_tag": headers.get("X-Robots-Tag"), "error": f"response read failed: {exc}", "truncated": False, "body": b""}
        finally:
            close = getattr(response, "close", None)
            if close:
                close()
        truncated = len(body) > max_body
        body = body[:max_body]
        return {"requested_url": url, "final_url": current, "status": status, "redirect_chain": chain, "content_type": headers.get("Content-Type"), "x_robots_tag": headers.get("X-Robots-Tag"), "error": None, "truncated": truncated, "body": body}
    raise AssertionError("unreachable")


class PageParser(HTMLParser):
    def __init__(self, base_url: str):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.base_seen = False
        self.title: list[str] | None = None
        self.title_value: str | None = None
        self.head_finished = False
        self.foreign_depth = 0
        self.headings: list[dict[str, str]] = []
        self.active_heading: dict[str, str] | None = None
        self.meta: dict[str, list[str]] = {"description": [], "canonical": [], "robots": []}
        self.links: list[dict[str, str]] = []
        self.active_link: dict[str, str] | None = None
        self.jsonld: list[dict[str, Any]] = []
        self.jsonld_buf: list[str] | None = None
        self.jsonld_type: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_map = {k.lower(): (v or "") for k, v in attrs}
        tag = tag.lower()
        if tag == "body":
            self.head_finished = True
        if tag in {"svg", "math"}:
            self.foreign_depth += 1
        if tag == "base" and not self.base_seen and attrs_map.get("href"):
            self.base_url = urllib.parse.urljoin(self.base_url, attrs_map["href"])
            self.base_seen = True
        # Accept a headless title fragment, but never a body or SVG/MathML title.
        if tag == "title" and self.title is None and self.title_value is None and not self.head_finished and not self.foreign_depth:
            self.title = []
        if tag in {f"h{i}" for i in range(1, 7)}:
            self.active_heading = {"level": tag[1], "text": ""}
        if tag == "meta":
            name = attrs_map.get("name", "").lower()
            if name == "description":
                self.meta["description"].append(attrs_map.get("content", ""))
            elif name == "robots":
                self.meta["robots"].append(attrs_map.get("content", ""))
        if tag == "link" and "canonical" in attrs_map.get("rel", "").lower().split():
            self.meta["canonical"].append(attrs_map.get("href", ""))
        if tag == "a" and attrs_map.get("href"):
            self.active_link = {"href": urllib.parse.urljoin(self.base_url, attrs_map["href"]), "text": ""}
        if tag == "script" and attrs_map.get("type", "").lower().split(";")[0].strip() == "application/ld+json":
            self.jsonld_buf = []
            self.jsonld_type = attrs_map.get("type")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "head":
            self.head_finished = True
        if tag in {"svg", "math"} and self.foreign_depth:
            self.foreign_depth -= 1
        if tag == "title" and self.title is not None:
            self.title_value = " ".join("".join(self.title).split())
            self.title = None
        if tag in {f"h{i}" for i in range(1, 7)} and self.active_heading is not None:
            self.active_heading["text"] = " ".join(self.active_heading["text"].split())
            self.headings.append(self.active_heading)
            self.active_heading = None
        if tag == "script" and self.jsonld_buf is not None:
            raw = "".join(self.jsonld_buf).strip()
            try:
                parsed = json.loads(raw)
                error = None
            except (json.JSONDecodeError, ValueError) as exc:
                parsed = None
                error = str(exc)
            self.jsonld.append({"raw": raw, "data": parsed, "error": error})
            self.jsonld_buf = None
        if tag == "a" and self.active_link is not None:
            self.active_link["text"] = " ".join(self.active_link["text"].split())
            self.links.append(self.active_link)
            self.active_link = None

    def handle_data(self, data: str) -> None:
        if self.title is not None:
            self.title.append(data)
        if self.active_heading is not None:
            self.active_heading["text"] += data
        if self.active_link is not None:
            self.active_link["text"] += data
        if self.jsonld_buf is not None:
            self.jsonld_buf.append(data)


def _html_declared_charset(body: bytes) -> str | None:
    head = body[:8192].decode("ascii", errors="ignore")
    for match in re.finditer(r"<meta\b[^>]*>", head, re.IGNORECASE):
        tag = match.group(0)
        charset = re.search(r"\bcharset\s*=\s*['\"]?\s*([^\s;/'\">]+)", tag, re.IGNORECASE)
        if charset:
            return charset.group(1)
        if re.search(r"\bhttp-equiv\s*=\s*['\"]?content-type", tag, re.IGNORECASE):
            content = re.search(r"\bcontent\s*=\s*(['\"])(.*?)\1", tag, re.IGNORECASE)
            if content:
                declared = re.search(r"\bcharset\s*=\s*([^\s;]+)", content.group(2), re.IGNORECASE)
                if declared:
                    return declared.group(1).strip("'\"")
    return None


def decode_html(body: bytes, content_type: str | None = None) -> tuple[str, dict[str, Any]]:
    warnings: list[str] = []
    candidates: list[tuple[str, str]] = []
    for marker, encoding in ((codecs.BOM_UTF32_LE, "utf-32"), (codecs.BOM_UTF32_BE, "utf-32"), (codecs.BOM_UTF8, "utf-8-sig"), (codecs.BOM_UTF16_LE, "utf-16"), (codecs.BOM_UTF16_BE, "utf-16")):
        if body.startswith(marker):
            candidates.append((encoding, "byte_order_mark"))
            break
    if not candidates and content_type:
        charset = re.search(r"(?:^|;)\s*charset\s*=\s*(?:\"([^\"]+)\"|'([^']+)'|([^;\s]+))", content_type, re.IGNORECASE)
        if charset:
            candidates.append((next(group for group in charset.groups() if group), "http_content_type"))
    if not candidates:
        declared = _html_declared_charset(body)
        if declared:
            candidates.append((declared, "html_declaration"))
    if not candidates:
        candidates.append(("utf-8", "utf-8_fallback"))

    requested, source = candidates[0]
    try:
        codec = codecs.lookup(requested)
        canonical = codec.name
        if canonical not in HTML_TEXT_ENCODINGS:
            raise LookupError("charset is outside the supported HTML text encodings")
    except (LookupError, TypeError, ValueError, UnicodeError):
        warnings.append(f"Unsupported or non-text charset {requested!r}; decoded with UTF-8 fallback.")
        requested, source, canonical = "utf-8", "utf-8_fallback", "utf-8"
    try:
        decoded = body.decode(requested, errors="strict")
    except (LookupError, TypeError, ValueError, UnicodeError):
        warnings.append(f"Bytes could not be decoded strictly as {canonical}; replacement characters may be present.")
        try:
            decoded = body.decode(requested, errors="replace")
        except (LookupError, TypeError, ValueError, UnicodeError):
            warnings.append(f"Replacement decoding failed for {canonical}; UTF-8 replacement fallback was used.")
            decoded = body.decode("utf-8", errors="replace")
            requested, source, canonical = "utf-8", "utf-8_fallback", "utf-8"
    return decoded, {"encoding": canonical, "source": source, "warnings": warnings}


def parse_html(body: bytes, final_url: str, content_type: str | None = None) -> dict[str, Any]:
    text, decoding = decode_html(body, content_type)
    parser = PageParser(final_url)
    parser.feed(text)
    parser.close()
    canonicals = [urllib.parse.urljoin(parser.base_url, href) if href else "" for href in parser.meta["canonical"]]
    return {"title": parser.title_value, "meta_descriptions": parser.meta["description"], "canonicals": canonicals, "meta_robots": parser.meta["robots"], "headings": parser.headings, "json_ld": parser.jsonld, "links": parser.links, "decoding": decoding}


def parse_robots(body: bytes) -> list[str]:
    return [line.split(":", 1)[1].strip() for line in body.decode("utf-8", "replace").splitlines() if line.lower().startswith("sitemap:")]


def parse_sitemap(body: bytes) -> dict[str, Any]:
    if b"<!doctype" in body.lower() or b"<!entity" in body.lower():
        return {"kind": None, "entries": [], "xml_error": "DTD and entity declarations are not allowed"}
    try:
        root = ET.fromstring(body)
    except ET.ParseError as exc:
        return {"kind": None, "entries": [], "xml_error": str(exc)}
    kind = root.tag.rsplit("}", 1)[-1]
    namespace = root.tag[:-len(kind)] if "}" in root.tag else ""
    entries = []
    expected_child = "url" if kind == "urlset" else "sitemap" if kind == "sitemapindex" else None
    if expected_child:
        for record in root:
            if record.tag.rsplit("}", 1)[-1] != expected_child or (record.tag[:-len(expected_child)] if "}" in record.tag else "") != namespace:
                continue
            for loc in record:
                loc_namespace = loc.tag[:-3] if "}" in loc.tag else ""
                if loc.tag.rsplit("}", 1)[-1] == "loc" and loc_namespace == namespace and loc.text:
                    entries.append(loc.text.strip())
    return {"kind": kind, "entries": entries, "xml_error": None}


def collect(urls: list[str], *, offline_html: bytes | None = None, opener: Any = None, max_body: int = MAX_BODY) -> dict[str, Any]:
    if len(urls) > MAX_URLS:
        raise ValueError(f"at most {MAX_URLS} URLs are allowed")
    timestamp = dt.datetime.now(dt.timezone.utc).isoformat()
    results = []
    for url in urls:
        validate_url(url)
        item = {"requested_url": url, "final_url": url, "status": None, "redirect_chain": [], "content_type": None, "x_robots_tag": None, "error": None, "truncated": False, "raw_html_rendered": False, "evidence": {"title": None, "meta_descriptions": None, "canonicals": None, "meta_robots": None, "headings": None, "json_ld": None, "links": None}, "sitemaps": None}
        if offline_html is not None:
            fetched = {"requested_url": url, "final_url": url, "status": None, "redirect_chain": [], "content_type": "text/html (offline fixture)", "x_robots_tag": None, "error": None, "truncated": len(offline_html) > max_body, "body": offline_html[:max_body]}
        else:
            fetched = fetch(url, opener=opener, max_body=max_body)
        for key in ("final_url", "status", "redirect_chain", "content_type", "x_robots_tag", "error", "truncated"):
            item[key] = fetched[key]
        body = fetched["body"]
        ctype = (fetched.get("content_type") or "").lower()
        is_success = offline_html is not None or fetched["status"] is not None and 200 <= fetched["status"] < 300
        if fetched["error"] is None and is_success:
            if fetched["truncated"]:
                item["evidence"] = {key: None for key in item["evidence"]}
            elif (urllib.parse.urlsplit(fetched["final_url"]).path.rstrip("/").endswith("robots.txt") and "html" not in ctype) or ("text/plain" in ctype and b"sitemap:" in body.lower()):
                item["sitemaps"] = {"kind": "robots", "declared_sitemaps": parse_robots(body)}
            elif "html" in ctype or "xhtml" in ctype:
                item["evidence"] = parse_html(body, fetched["final_url"], None if offline_html is not None else fetched.get("content_type"))
            elif "xml" in ctype or body.lstrip().startswith(b"<?xml"):
                item["sitemaps"] = parse_sitemap(body)
        results.append(item)
    return {"collected_at": timestamp, "source_mode": "offline_html" if offline_html is not None else "network", "raw_html_rendered": False, "results": results}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=f"{__doc__} Bounds: 10 URLs, {MAX_REDIRECTS} redirects, {MAX_BODY} response bytes, {TIMEOUT}s per-socket timeout (not a total request deadline).")
    parser.add_argument("urls", nargs="*", help="Explicit HTTP(S) URLs; at most 10")
    parser.add_argument("--html-file", help="Parse a local HTML file without network access")
    parser.add_argument("--base-url", help="Base URL required with --html-file")
    args = parser.parse_args(argv)
    try:
        if bool(args.html_file) != bool(args.base_url):
            raise ValueError("--html-file and --base-url must be provided together")
        if args.html_file:
            if args.urls:
                raise ValueError("explicit URLs cannot be combined with --html-file")
            validate_url(args.base_url)
            with open(args.html_file, "rb") as source:
                result = collect([args.base_url], offline_html=source.read(MAX_BODY + 1))
        else:
            if not args.urls:
                raise ValueError("provide one or more explicit URLs")
            result = collect(args.urls)
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
