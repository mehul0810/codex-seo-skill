# Audit Delivery And Maintenance

## Collect Evidence

Choose a small representative sample: home, a conversion page, a content page, and relevant templates. Use links found on the site, supplied URLs, and declared sitemap URLs. Record which pages were sampled and why. Respect site policies and rate limits; do not bypass login, WAF challenges, or platform access restrictions.

From the skill directory, run the collector with explicit URLs:

```bash
python3 scripts/collect_evidence.py https://example.com/ https://example.com/robots.txt
python3 scripts/collect_evidence.py --html-file /path/to/page.html --base-url https://example.com/
```

Consult `--help` for limits. It writes JSON to stdout, follows bounded redirects, and fetches only supplied URLs and their redirects. Select discovered sitemap or page URLs in a subsequent bounded call; it does not recursively crawl. It uses standard-library Python and no account credentials. Public-network mode rejects targets resolving to non-public addresses, but this is a best-effort check, not a DNS-rebinding security boundary. Use only reviewed URLs; use offline HTML or an authorized browser for local/staging sites. Never paste signed/private URLs or credentials into public evidence reports.

When local retention is permitted and appropriate, retain collector JSON used for the audit in an approved task-owned artifact and reference it with the findings; avoid secrets and signed URLs, and keep raw evidence private unless sharing is authorized. Respect no-artifact instructions and storage restrictions; otherwise report the evidence-retention limit without writing. Do not rely only on a prose summary that drops relevant extracted values. The collector's timestamp is not the original capture time of saved HTML; irrelevant extracted fields need not be repeated in the narrative.

Interpret the record before assigning findings:

- Raw HTML extraction does not execute JavaScript. Inspect the rendered page separately if source content is incomplete; identify browser observations separately from server HTML.
- Check decoding warnings before quoting extracted text. Encoding detection is a limited helper, not a browser-equivalent parser; verify uncertain text against the source or browser.
- When rendering succeeds, recommend a rendering architecture change only with evidence of a relevant crawler, performance, or reliability problem. JavaScript dependence alone is an observation, not a reason to prescribe server rendering.
- Missing fields in truncated, failed, or unsupported responses are unknown. Even a complete raw response cannot establish the rendered DOM or Google's indexed version.
- A 403/429 or a transport failure describes this collector's access, not search-engine access. Report blocked evidence, not a confirmed crawl defect.
- Parse errors in JSON-LD are observations; valid JSON is not proof of valid schema or rich-result eligibility.
- Sitemap entries and links are candidates, not proof of indexing, a full page count, or orphan status. Verify a linked destination before reporting a broken link.
- Saved HTML has no verified live status, response headers, or redirect history. Preserve its user-supplied provenance and timestamp separately.
- The collector retains only the first source document title; it is not a duplicate-title detector or a streaming-metadata validator. Inspect the complete source and rendered DOM for those questions, using `delivery-diagnostics.md` only for the relevant stack.
- `meta_robots` contains generic robots meta tags, not every agent-specific tag. Inspect relevant platform-specific tags and directives in the complete response before determining effective policy.

## Finding Contract

Use a compact summary table and details keyed by stable IDs such as F01. Do not squeeze all evidence into a wide table.

| Field | Required content |
| --- | --- |
| ID and finding | Specific observed issue or explicit hypothesis; include category and relevant stage (delivery/crawl, index/canonical, retrieval/citation, referral, conversion) |
| Scope | Exact affected URL(s), sampled template, and known coverage limits |
| Evidence | Observation, source URL/artifact, capture time, method, and relevant header/tag/text; distinguish source HTML from rendered DOM |
| Status and confidence | Confirmed / hypothesis; high / medium / low with reason. Mark unavailable elements of an otherwise evidenced finding as unknown in the relevant fields; unavailable checks alone belong in coverage. Keep platform-policy evidence strength separate |
| Business rationale | Conversion goal, affected funnel stage, known importance/demand and source; label assumptions |
| Action | Concrete change or validation task, suggested owner, effort range, dependencies, and priority rationale |
| Acceptance | Observable pass condition and recheck method at the affected URL, not an SEO outcome promise |
| Measurement | Relevant baseline or unknown, primary KPI, data source, comparison period, and observation window; use the provenance contract in `measurement-and-experiments.md` for material metrics |

Shared provenance can be recorded once and referenced by finding IDs. If capture time, baseline, or measurement access is unavailable, explicitly mark it unknown rather than silently omitting it.

Example: F01 records a verified `noindex` on a lead page the owner wants searchable. Its action is to confirm the directive is accidental, then correct the responsible template. Acceptance is a fresh response and rendered check without the directive; URL Inspection is a separate follow-up. Lead growth remains an outcome to measure, not the acceptance test. An intentional noindex on a private or low-value page is not a defect.

For unavailable data, create a coverage note rather than a speculative fix or a finding ID. Put access requests and unperformed checks in a separate next-evidence list; labeling them "unknown" inside the findings table does not make them observed issues. Keep a validation task with findings only when an observation supports a specific testable hypothesis. A blocked LinkedIn profile cannot establish bio inconsistency; request public profile text or a user-provided export and continue with verified site-side links. For a social-only input, confirm the business website before auditing a similarly named domain.
If multiple linked domains have unclear ownership, explicitly ask which is the business website before recommending a primary link or a canonical domain. This is an intake question, not a finding: two links and missing context do not establish a wrong destination, inconsistent identity or visitor confusion. Recommend profile changes only after ownership and actual presentation reveal an issue. An empty findings table is preferable to classifying missing evidence as a defect to fix.

## Coverage Ledger

For each requested platform, record: platform, requested scope, status (observed / partial / blocked / not assessed), observed evidence, current documentation checked, and what remains unknown. When sampling results, record upstream provider when disclosed, locale, device, and personalization context. Shared providers do not make different surfaces independent confirmations. Separate public technical readiness from actual citations, identity-verified crawler requests, account settings, and analytics; a user-agent string alone is not verified identity.

For public-HTML or local-fixture SEO/AI-readiness audits, explicitly distinguish rendered evidence, field performance, engine index status, actual AI citations, and private account controls in coverage notes. Mark each relevant class unknown or not assessed when unavailable; a broad "limited audit" disclaimer alone does not identify these missing checks. Public source or a local browser capture cannot establish engine/account state or field performance.

Select relevant sources from `search-platforms.md` and recheck current primary documentation. If unavailable, report generic content observations only and leave platform-specific eligibility unknown. Never transfer one provider's bot rules or metrics to another. Do not use a readiness checklist as proof of citations.

## Source Maintenance

During each audit, reverify rules that materially affect the recommendation: crawl/index/snippet controls, rich-result availability, bot purposes, reporting definitions, and regional/account feature access. A recent check date is not permission to assume an unchanged critical rule.

When maintaining the skill, recheck volatile reference claims after 90 days or sooner when an official changelog, redirect, contradiction, or deprecation appears. This is a maintenance trigger, not an automatic scheduled job. Keep verified dates per source/claim; do not update dates for unread pages.

Record source URL, title, checked date, supported claim, and relevant limits. Verify destination content, not merely HTTP 200: a documentation URL may redirect to an unrelated index. Prefer official documentation over announcements, distinguish announced features from available property data, and label experiments explicitly. If verification fails, retain the last-known date and mark the affected claim unverified for the current run.

For a material contradiction, record both statements with source, publication/update date when available, checked date, scope/version, and the basis for the chosen interpretation. Prefer current feature-specific primary guidance for that feature, without silently deleting a contradictory overview. If the conflict remains unresolved, qualify or defer the affected recommendation. Vendor documentation defines its own product, not another engine's ranking rules. Record original research design and commercial affiliation using `measurement-and-experiments.md`; repeated summaries and common ownership are not independent corroboration.

When maintaining the source checkout, validate frontmatter, links to bundled resources, the collector tests, and affected behavioral scenarios under the repository's `tests/` directory. Tests are development resources, not part of the installed runtime bundle. Record observed outcomes and revision. Structural validation alone does not establish audit quality.
