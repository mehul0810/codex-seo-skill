# Audit Delivery And Maintenance

## Collect Evidence

Choose a small representative sample: home, a conversion page, a content page, and relevant templates. Use links found on the site, supplied URLs, and declared sitemap URLs. Record which pages were sampled and why. Respect site policies and rate limits; do not bypass login, WAF challenges, or platform access restrictions.

From the skill directory, run the collector with explicit URLs:

```bash
python3 scripts/collect_evidence.py https://example.com/ https://example.com/robots.txt
python3 scripts/collect_evidence.py --html-file /path/to/page.html --base-url https://example.com/
```

Consult `--help` for limits. It writes JSON to stdout, follows bounded redirects, and fetches only supplied URLs and their redirects. Select discovered sitemap or page URLs in a subsequent bounded call; it does not recursively crawl. It uses standard-library Python and no account credentials. Public-network mode rejects targets resolving to non-public addresses, but this is a best-effort check, not a DNS-rebinding security boundary. Use only reviewed URLs; use offline HTML or an authorized browser for local/staging sites. Never paste signed/private URLs or credentials into public evidence reports.

Interpret the record before assigning findings:

- Raw HTML extraction does not execute JavaScript. Inspect the rendered page separately if source content is incomplete; identify browser observations separately from server HTML.
- Check decoding warnings before quoting extracted text. Encoding detection is a limited helper, not a browser-equivalent parser; verify uncertain text against the source or browser.
- When rendering succeeds, recommend a rendering architecture change only with evidence of a relevant crawler, performance, or reliability problem. JavaScript dependence alone is an observation, not a reason to prescribe server rendering.
- Missing fields in truncated, failed, or unsupported responses are unknown. Even a complete raw response cannot establish the rendered DOM or Google's indexed version.
- A 403/429 or a transport failure describes this collector's access, not search-engine access. Report blocked evidence, not a confirmed crawl defect.
- Parse errors in JSON-LD are observations; valid JSON is not proof of valid schema or rich-result eligibility.
- Sitemap entries and links are candidates, not proof of indexing, a full page count, or orphan status. Verify a linked destination before reporting a broken link.
- Saved HTML has no verified live status, response headers, or redirect history. Preserve its user-supplied provenance and timestamp separately.

## Finding Contract

Use a compact summary table and details keyed by stable IDs such as F01. Do not squeeze all evidence into a wide table.

| Field | Required content |
| --- | --- |
| ID and finding | Specific observed issue or explicit hypothesis; include category |
| Scope | Exact affected URL(s), sampled template, and known coverage limits |
| Evidence | Observation, source URL/artifact, capture time, method, and relevant header/tag/text; distinguish source HTML from rendered DOM |
| Status and confidence | Confirmed / hypothesis / unavailable; high / medium / low with reason. Keep platform-policy evidence strength separate |
| Business rationale | Conversion goal, affected funnel stage, known importance/demand and source; label assumptions |
| Action | Concrete change or validation task, suggested owner, effort range, dependencies, and priority rationale |
| Acceptance | Observable pass condition and recheck method at the affected URL, not an SEO outcome promise |
| Measurement | Relevant baseline or unknown, primary KPI, data source, comparison period, and observation window |

Shared provenance can be recorded once and referenced by finding IDs. If capture time, baseline, or measurement access is unavailable, explicitly mark it unknown rather than silently omitting it.

Example: F01 records a verified `noindex` on a lead page the owner wants searchable. Its action is to confirm the directive is accidental, then correct the responsible template. Acceptance is a fresh response and rendered check without the directive; URL Inspection is a separate follow-up. Lead growth remains an outcome to measure, not the acceptance test. An intentional noindex on a private or low-value page is not a defect.

For unavailable data, create a coverage note rather than a speculative fix. A blocked LinkedIn profile cannot establish bio inconsistency; request public profile text or a user-provided export and continue with verified site-side links. For a social-only input, confirm the business website before auditing a similarly named domain.
If multiple linked domains have unclear ownership, explicitly ask which is the business website before recommending a primary link or a canonical domain. Do not classify missing evidence as a defect to fix.

## Coverage Ledger

For each requested platform, record: platform, requested scope, status (observed / partial / blocked / not assessed), observed evidence, current documentation checked, and what remains unknown. Separate public technical readiness from actual citations, logged crawler requests, account settings, and analytics.

Google, Bing/Copilot, and ChatGPT have source references in `ai-search-optimization.md`. For Perplexity or any other service, first read that service's current primary documentation. If unavailable, report generic content observations only and leave platform-specific eligibility unknown. Never transfer one provider's bot rules or metrics to another. Do not use a readiness checklist as proof of citations.

## Source Maintenance

During each audit, reverify rules that materially affect the recommendation: crawl/index/snippet controls, rich-result availability, bot purposes, reporting definitions, and regional/account feature access. A recent check date is not permission to assume an unchanged critical rule.

When maintaining the skill, recheck volatile reference claims after 90 days or sooner when an official changelog, redirect, contradiction, or deprecation appears. This is a maintenance trigger, not an automatic scheduled job. Keep verified dates per source/claim; do not update dates for unread pages.

Record source URL, title, checked date, supported claim, and relevant limits. Verify destination content, not merely HTTP 200: a documentation URL may redirect to an unrelated index. Prefer official documentation over announcements, distinguish announced features from available property data, and label experiments explicitly. If verification fails, retain the last-known date and mark the affected claim unverified for the current run.

When maintaining the source checkout, validate frontmatter, links to bundled resources, the collector tests, and affected behavioral scenarios under the repository's `tests/` directory. Tests are development resources, not part of the installed runtime bundle. Record observed outcomes and revision. Structural validation alone does not establish audit quality.
