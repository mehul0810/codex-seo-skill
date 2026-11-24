# Acme services: focused SEO audit

## Mode and summary

**Audit mode:** a focused review of the supplied priority landing page for qualified consultation leads. The most important issue is a `noindex` directive in the captured HTML, which conflicts with the stated goal that the page appear in search. Verify the current served response first, then correct the directive if it remains present and the page is intended to be public. With one developer day, reserve capacity for this and its verification before expanding the page.

The page also provides almost no information about the migration service or the consultation. Accurate, owner-confirmed detail could help visitors decide whether they are a fit, but no traffic or lead uplift can be forecast from this single capture.

## Evidence and coverage

- Sample: `https://acme.example/services/`, the supplied priority landing page and base URL. The complete supplied `service.html` was inspected and parsed offline; its original capture date is unknown. [Retained evidence](service-evidence.json) was extracted on 2026-11-24 UTC, which is analysis time, not capture time.
- Captured HTML has `<meta name="robots" content="noindex, follow">`, title `Book an Acme consultation`, description `Book an Acme migration consultation.`, an H1 `Book a migration consultation`, and one `Contact the team` link to `/contact/`. The declared canonical matches the supplied base URL. Its live response and Google's selected canonical are unknown.
- The saved capture does not establish current HTTP status, redirects, response headers including `X-Robots-Tag`, robots.txt, sitemap, rendering, crawler access, actual index status, search performance, contact destination, or successful lead submission. `/contact/` was not fetched and is not asserted broken. Field performance, other pages, social profiles, actual AI citations and account controls were not assessed. No live fixture-domain request was made.
- The consultation goal and priority status come from the request. Market, language targeting, customer segment, migration type, demand, qualification criteria, and baseline conversions are unknown. Do not infer sitewide coverage or performance from this page.

## Priority actions

| ID | Issue and stage | Impact | Effort | Dependency / owner | Timing |
| --- | --- | --- | --- | --- | --- |
| F01 | Captured `noindex` conflicts with intended search visibility; indexing | High potential on the stated priority page; actual live and index state unknown | Up to one developer day including checks, subject to cause | Current served response and configuration access; developer / SEO owner | Now, first |
| F02 | Migration offer and next-step detail are sparse; retrieval and conversion | Potentially meaningful for qualified leads; effect unknown | Content input plus a small page edit, time unknown | Verified offer and qualification details; service owner / content owner, then developer | Next, or use remaining day only if F01 is resolved |

Priority is qualitative: impact is tied to the explicitly identified priority landing page, while search demand and actual conversion rates are unavailable. No numerical ranking or revenue forecast is implied.

### F01: Verify and remove the conflicting indexing directive

**Evidence and confidence:** Confirmed in the supplied HTML, high confidence for this capture; whether it exists live is unknown. The generic robots tag contains `noindex, follow`. The supplied page is supposed to appear in search. According to [Google's noindex documentation](https://developers.google.com/search/docs/crawling-indexing/block-indexing), checked 2026-11-24, Google can exclude a page when it crawls and reads this rule. A robots.txt block can prevent Google from seeing it, so this capture alone neither proves current exclusion nor proves access. Removing it does not guarantee indexing or ranking.

**Action:** Obtain a fresh authorized response for the actual route, recording status, redirects, complete HTML, and `X-Robots-Tag`; inspect effective robots.txt and any CMS, template, or edge setting responsible. If the directive remains and the owner confirms the page is public and intended for indexing, remove the unintended `noindex` at its source without weakening unrelated rules. Check for any other applicable indexing directives. If already absent, do not change it; document the discrepancy and proceed with inspection. Do not alter crawler training choices or block/unblock unrelated paths.

**Acceptance:** A fresh served response at the intended canonical URL has the expected successful status and no unintended applicable `noindex` in HTML or headers, and the relevant crawler can access it under the observed robots rules. Verify the rendered page separately. If authorized Google Search Console access exists, inspect the URL and request recrawl where appropriate; record Google's reported status and canonical separately. A request is not proof of indexing, and outcomes may take time.

**Measurement:** Technical baseline is the supplied capture only; live baseline unknown. Primary outcome: qualified consultation completions from organic landings on this URL, once an agreed event and qualification definition and analytics access exist. Secondary: URL-level organic clicks and impressions in Search Console, if available. Record date, country/device, query grouping, comparison period, and concurrent changes. These measures are unavailable now; do not treat missing data as zero or promise a change.

### F02: Explain the service and consultation clearly

**Evidence and confidence:** Confirmed for the captured page: beyond a migration consultation heading, the only body copy says `Speak with our team about your project.` No migration type, audience, scope, qualification criteria, or consultation process is supplied. The title promises booking while the visible link says `Contact the team`; its destination and whether it actually books a consultation were not inspected. This is an observed information gap, not proof that visitors are confused or that the link fails.

**Action:** Ask the service owner for the actual migration type, suitable customers/projects, relevant scope, and what happens after contact. Add concise, accurate details that help a prospect decide whether to proceed. Inspect the contact destination and align the title and CTA to the real action; do not promise direct booking if it is only an enquiry. Avoid inventing prices, results, expertise, or guarantees. If the one developer day is exhausted by F01, prepare the copy for the next sprint rather than compromising the indexing check.

**Acceptance:** Owner-approved information appears visibly on the real page, identifies the service and audience accurately, and matches the destination's actual next step. Test the link, keyboard operation and consultation submission/confirmation in the authorized environment; separately record any unavailable tests. Do not count a click as a confirmed qualified lead.

**Measurement:** Primary and secondary outcomes use F01's definitions. Baseline is unknown; use comparable periods and segment by landing page, country, device and relevant query groups when data is available. Changes to content and indexing may overlap, so a before/after result alone will not isolate cause.

## AI-search readiness

The captured `noindex` is relevant to search readiness, but the evidence does not establish whether any AI answer cites the page. For Googlebot, Bingbot and OAI-SearchBot, current robots rules, infrastructure access, actual rendering, indexing and citations are unknown. Training crawler policy is separate and not assessed. The page identifies Acme and a migration consultation but lacks enough verified service detail for a reader to evaluate the offer. Add genuine detail under F02 rather than invented evidence or special AI markup. A bounded future citation sample can record exact questions, platform, locale, date, valid answers and cited URL, checking whether citations support their associated claims; failed captures should be reported separately. Such a sample is not a market-wide visibility estimate.

## 30/60/90-day checkpoints

- **30 days:** Verify the live directive and complete the corrective check if applicable. Establish a baseline for qualified organic consultations and URL-level Search Console data if access becomes available. Confirm the offer and contact flow.
- **60 days:** Review comparable organic clicks, impressions and qualified consultations with country/device and query segments where available. Investigate changes without assuming causation.
- **90 days:** Reassess the same measures and indexing evidence, then prioritize further work based on actual demand and conversion evidence. The checkpoints are not outcome deadlines or guarantees.

**Next evidence needed:** a current authorized page response and headers, robots.txt, access to relevant configuration and URL Inspection, verified offer and qualification details, and a working contact-flow test. An analytics export was not supplied, so all outcome baselines remain unknown.
