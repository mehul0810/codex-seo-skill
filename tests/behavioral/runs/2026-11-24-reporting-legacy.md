# L01. Acme services page

**Mode: audit.** This is a focused review of one priority landing-page capture, not a sitewide audit. The goal is qualified consultation leads; market, language beyond the English HTML, search demand, and historical performance are unknown.

## Executive summary and coverage

The supplied page explicitly says `noindex, follow`, conflicting with the owner's stated intent for it to appear in search. This is the first issue to investigate within the one developer day. The capture also gives a visitor little information for deciding whether the consultation fits their migration. A self-referencing canonical and a contact link are present, but neither proves that the page is indexed or that the contact destination works.

Evidence: complete supplied `service.html`, base `https://acme.example/services/`, inspected directly and with the offline collector on 2026-11-24. Original capture time, live status, final URL, headers, redirects, rendered page, robots.txt, sitemap, Search Console, analytics, rankings, competitors, and contact destination are unavailable. No live request was made. Google and other search/AI surfaces, crawler access, selected canonical, and actual citations are not assessed. No analytics baseline is available.

## Priority actions

| ID | Issue and stage | Impact / confidence | Effort, owner, dependency | When |
|---|---|---|---|---|
| S1 | `noindex` conflicts with intended search inclusion; indexing | High potential on this priority URL; high confidence in captured tag, unknown live state | Developer, under half a day if template setting is straightforward; confirm served response and intended policy first | Now, first |
| S2 | Consultation offer is underspecified; retrieval and conversion | Potentially meaningful; high confidence in captured content, effect on leads unknown | Content owner with developer, under half a day for a focused revision; verified offer details | Now if S1 leaves capacity, otherwise next |

**S1. Search eligibility.** The captured head contains `<meta name="robots" content="noindex, follow">`. Confirm that this is not an intentionally protected or excluded version, then remove the unintended directive at its source for this public priority page, without changing exclusions elsewhere. First inspect the current complete response, rendered head, `X-Robots-Tag`, robots rules and redirects in an authorized environment. A `noindex` in an old capture alone does not prove today's live setting or actual index status. Acceptance: a fresh served response and rendered head for the intended final URL contain no unintended `noindex`, headers do not introduce it, and the intended crawler can fetch the page. Separately use authorized URL Inspection to check Google's selected canonical and index state; reinspection is not a guarantee of inclusion. Business rationale: removing an unintended eligibility conflict addresses the owner's stated goal before content polish. Primary KPI: search impressions for this exact URL in Search Console Web; secondary: qualified organic consultation leads, if attribution exists. Baselines unknown; compare comparable 28-day periods after allowing processing time, segmented by country and device where available.

**S2. Explain the offer.** The source has the heading “Book a migration consultation,” one general sentence, and “Contact the team.” Work with the owner to add truthful specifics: who the consultation is for, what migration topics it covers, what happens after contact, and any genuinely applicable prerequisites or geography. Do not invent scope, outcomes, pricing or guarantees. Make the contact label describe its actual destination and verify the linked `/contact/` flow before claiming it works. Acceptance: the served page visibly answers those questions using approved facts and its contact link leads to the intended functioning form or contact method. Primary KPI: qualified leads from this landing page, if instrumented; secondary: organic clicks to this URL, using the same cohort and comparable periods. This is a user-value improvement, not a promised ranking or conversion lift.

**One-day sequence:** reserve the morning for S1 diagnosis, targeted correction if confirmed, and response/header verification. Use remaining time to gather verified offer details and implement S2 only if feasible. No site or policy changes are made by this audit.

## AI-search readiness and measurement

| Crawler / surface | Captured policy | Infrastructure and actual access | Status |
|---|---|---|---|
| Google Search / AI features | Generic `noindex` in saved HTML | Unknown | Partial source evidence only |
| Bing and ChatGPT search | Generic `noindex` in saved HTML | Unknown | Partial source evidence only; engine-specific behavior not verified |
| Training crawlers | No policy evidence | Unknown | Not assessed; separate owner decision |

The page names the offer but provides limited answer and evidence detail. Add only verifiable specifics and a clear publisher identity where useful; citation presence and accuracy were not sampled. Do not change training permissions or create speculative AI markup. At 30 days check served eligibility and establish Search Console and lead baselines; at 60 days compare URL-level impressions, clicks and qualified leads with a comparable baseline; at 90 days review query mix and lead quality before further content investment. If measurement access remains unavailable, record results as unavailable, not zero. These are checkpoints, not outcome promises.

# L02. Acme plans page

**Mode: audit.** Scope is the supplied plans source and local browser DOM for consultation intent. Geography, target audience, plan details, live behavior, actual search demand and conversion baselines are unknown.

## Executive summary and coverage

The source ships an empty `main`, then JavaScript supplies the heading, description, contact link and meta description. The supplied local Chrome DOM shows those elements after execution. This establishes fixture rendering only, not a live or search-crawler failure; do not rebuild the page merely because it uses JavaScript. More directly, the rendered copy says “Choose a consultation plan” but supplies no comparison or plan information, leaving a gap for both a prospective client and a system trying to describe the offer.

Evidence reviewed on 2026-11-24: `javascript.html` and `javascript-rendered.html`, base `https://acme.example/plans/`, directly and with offline extraction. The source capture time is unknown; supplied DOM was generated from the fixture in isolated headless Chrome 158.0.8127.37 on 2026-11-24. The DOM contains `Acme plans`, “Choose a consultation plan,” a `/contact/` link and the description “Compare Acme consultation plans.” Source has title and self-canonical but no initial content or description. HTTP status, headers, redirects, live rendering, contact destination, sitemap, robots rules, engine rendering/index status, analytics, competitors and citations are unavailable. No live requests were made.

## Priority actions

| ID | Issue and stage | Impact / confidence | Effort, owner, dependency | When |
|---|---|---|---|---|
| P1 | Comparison promise lacks plan details; retrieval and conversion | Meaningful potential; high confidence in captured DOM, unknown commercial effect | Content/product owner and developer, under half a day for a small verified comparison; approved plan facts | Now |
| P2 | Important page content depends on script execution; delivery/retrieval hypothesis | Unknown impact; high confidence in fixture dependency, low confidence of a real crawler problem | Developer, under half a day for targeted investigation; access to actual served route and authorized inspection | Next, or now if delivery evidence is available |

**P1. Supply useful plan information.** The rendered text asks visitors to choose but contains no actual plan names, differences, eligibility, scope or decision guidance. Confirm whether plans exist and add only approved, current comparison details, including pricing or availability only if the owner confirms them. If it is not genuinely a comparison page, revise the title, description and copy to describe the real consultation instead. Acceptance: in the actual rendered page, a visitor can understand the verified options and their relevant differences, or sees accurately relabeled consultation content; the contact path leads to the intended working destination. Primary KPI: qualified consultation leads from this page; secondary: organic clicks to the page. Both baselines and tracking are unknown; compare equivalent 28-day cohorts after instrumentation rather than forecast uplift.

**P2. Test actual delivery before prescribing a rendering change.** The source `<main id="app"></main>` has no initial page copy or link, while the supplied DOM has all three after script execution. The meta description is also appended by script. This may matter for consumers that do not execute the script or if script delivery fails, but the fixture's successful local rendering is not evidence of a crawler failure. Inspect the actual response and rendered output, browser console and network errors, and authorized Google URL Inspection rendered output for this exact URL. Check relevant crawler access, response headers and index status separately. If a reproducible consumer cannot access material content, fix the narrow delivery problem and consider server-rendering or pre-rendering that content only after evaluating the cause. Acceptance: the relevant observed failure is reproduced, addressed and rechecked for affected consumers without breaking the interactive page; successful inspection alone does not prove indexing or ranking. Developer owns investigation. Primary measure: whether the identified consumer receives the required text and link; secondary outcome: URL-level organic impressions over a comparable period. Baseline unknown.

## AI-search and checks

| Surface or crawler | Policy / content evidence | Access and citations | Status |
|---|---|---|---|
| Google Search and AI features | Local DOM contains the basic offer, source depends on script | robots, infrastructure, indexing, account controls and actual citations unknown | Partial |
| Bing / Copilot | Same local source and DOM only | Engine-specific access, rendering and citations unknown | Not assessed |
| ChatGPT search | Same local source and DOM only | Search-crawler access and citations unknown | Not assessed |
| Model training | No relevant policy evidence | Unknown | Not assessed, separate from search |

Citation readiness is limited by the absence of actual plan details; no citation absence is inferred. Add accurate entity and offer details that users need, not fabricated evidence or special AI schema. Any future citation sampling should preserve exact prompts, date, locale and valid-answer counts; record failed captures separately and verify whether cited pages support associated claims.

At 30 days establish real delivery/index and analytics baselines; at 60 days compare exact-page impressions, clicks and qualified leads across matched periods where data exists; at 90 days review query intent and lead quality. Metrics are unknown until measured; search impressions and leads are distinct, and no AI-only traffic is inferred from general search reports. No changes were applied.

# L03. LinkedIn, X and website

**Mode: audit, limited profile review.** The supplied export is the only observed material. It identifies `https://www.linkedin.com/company/acme-example/` as “Acme Example,” with bio “Migration advice and consulting” and links to `https://acme.example/` and `https://acme-partners.example/`. It does not identify a designated website field. The X profile fetch in the supplied export returned HTTP 403 to that auditing client; the profile's contents are not available. There is no site HTML. Capture date, conversion goal, audience, location, ownership of either domain and the relationship between them are unknown.

## Executive summary and coverage

The profile states a coherent high-level service, but the two linked domains have no stated relationship in the export. Confirm ownership and intended destination before treating either as the canonical business website. X alignment and website SEO cannot be assessed from a blocked X fetch and absent site evidence. The 403 is an observation about the auditing client, not proof that the profile is unavailable to others. No live profiles or fixture domains were fetched.

| Requested scope | Status | Evidence / limit |
|---|---|---|
| LinkedIn | Partial | Supplied public text only, no capture time or authenticated fields; no live verification |
| X | Blocked in supplied evidence | Client received HTTP 403; no bio, name or link available for comparison |
| Website SEO | Not assessed | Two domains mentioned, ownership unclear, no site source, crawl or analytics |
| Search and AI surfaces | Not assessed | No robots, headers, indexing, citation or account evidence |

## Priority action

| ID | Issue and stage | Impact / confidence | Effort, owner, dependency | When |
|---|---|---|---|---|
| E1 | Two unexplained profile links make the intended business destination unclear in the supplied text; entity/referral | Potential navigation confusion; high confidence in the export, unknown actual profile presentation and user impact | Business owner, under half a day; verify both domain relationships and actual profile layout | Now |

**E1. Confirm and clarify the destinations.** Ask which domain is the business's primary website, what the other domain represents, and whether each link is intended for prospects. Then, if the actual profile does not already clarify this, label or order links to reflect their verified purposes and ensure the primary website field points to the intended destination. Do not change a canonical domain or remove a link based on the export alone. Acceptance: owner confirms both relationships; an authorized review of the actual public profile shows accurate names and destinations, and each verified link reaches its intended page. Business rationale: a clear next step can reduce ambiguity for prospects, but its effect is unmeasured. Primary metric: qualified referrals or leads from the profile, if attribution exists; secondary: profile link clicks, if available. Baselines, cohort and reporting periods are unknown; compare equivalent periods once access is available.

## Next evidence and AI readiness

1. Which domain is the primary business website, what is the relationship of the other, and what action should a prospect take? What geography and language matter?
2. Provide the X profile URL and a current public text export or screenshot, plus the designated LinkedIn website field and a current capture. Compare name, service description and destination only after obtaining these; do not infer mismatch from the 403.
3. Provide an authorized crawl or saved HTML for the confirmed site's homepage and priority consultation page, including capture time, status, response headers, robots.txt and sitemap, plus Search Console access or exports if available. Then inspect indexing, canonical and content rather than assuming a problem.

Crawler matrix: Googlebot, Bingbot and search-specific AI crawlers all have **unknown** robots and infrastructure access; model-training crawler policy is also **unknown and separate**. No citation, structured-data, backlink or ranking claims can be established here. At 30 days establish confirmed identities, destinations and any available referral baseline; at 60 days compare matched profile clicks and qualified leads; at 90 days assess whether the verified site and profile information remain consistent. Record unavailable data as unavailable. This audit made no account, profile or website changes.
