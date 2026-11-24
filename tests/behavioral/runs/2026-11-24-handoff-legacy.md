# L01. Acme services page

## Mode and summary
**Audit**, limited to the supplied priority landing-page HTML. The captured page explicitly says `noindex`, contrary to the owner's stated goal. If the live response still contains that directive, it is the first issue to address within the one developer day. The page also gives prospective consultation leads very little information to judge fit. Neither the live state nor current indexing is established by this capture.

## Scope and evidence
Reviewed `service.html` and `evidence-service.json` on 2026-11-24. Original capture time, live HTTP status, response headers, redirects, and rendering are unknown; the base URL is `https://acme.example/services/`. The HTML has a self-referencing canonical, title, description, H1 and contact link. A canonical declaration is not proof of Google's selected canonical. Target geography, language beyond HTML `en`, demand, CMS, lead baseline and search performance are unknown. No analytics export was provided. This is one page, not a sitewide crawl.

## Priority actions
| ID | Issue and stage | Impact | Effort | Dependency / owner | Timing |
| --- | --- | --- | --- | --- | --- |
| S01 | Captured `noindex` conflicts with desired search eligibility; indexing | High for this priority page if live | < half day to diagnose and correct, subject to CMS | Confirm live directive and intended visibility; developer | Now, first |
| S02 | Consultation offer lacks details needed to assess fit; retrieval and conversion | Potentially meaningful, unquantified | 0.5–2 days, subject to approved facts | Owner supplies accurate service details; content owner, developer | Next, after S01; draft within capacity |

**S01: captured indexing directive.** The saved source has `<meta name="robots" content="noindex, follow">`. Confidence is high for the captured HTML, unknown for the live response and current index. Google says a crawlable `noindex` page is removed from Google Search when the directive is processed; robots blocking can prevent it being seen. [Google: Block Search indexing with noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing), checked 2026-11-24. Verify the live HTML, rendered DOM and `X-Robots-Tag`, then confirm that no exclusion is intentional and remove the responsible directive if it remains. Check robots access separately. **Acceptance:** a fresh live response and rendered DOM for the intended canonical have no conflicting `noindex`, including relevant headers and agent-specific tags; record final URL and status. Authorized Search Console URL Inspection can separately check Google's indexed state and selected canonical; removal is not proof of indexing. Primary KPI: non-brand organic clicks to this URL; secondary: qualified organic consultation leads. Baseline unavailable. Compare matched periods after sufficient data, segmented by country/device and query where possible; initial review at 30/60/90 days, not a guarantee.

**S02: sparse offer context.** The entire visible body consists of a migration-consultation heading, “Speak with our team about your project,” and a contact link. Confidence high for this captured page, not for an unknown live version; whether more context improves leads is a hypothesis. Confirm who the consultation serves, scope, process and next step with the owner. Add only accurate, useful details that answer those questions and retain a clear contact action. **Acceptance:** render the actual page and confirm approved, specific offer and next-step information is readable and the contact destination works; no invented claims. Primary KPI: qualified consultation leads from organic landing sessions; secondary: organic landing-to-lead conversion rate (qualified leads divided by organic landing sessions). Baseline unknown; define qualification and attribution before comparing matched periods at 60/90 days. Capture and implementation require owner-supplied facts.

## Page and AI visibility
The priority URL should first pass S01, then S02. The contact link is present in the capture; its destination was not fetched and is not called broken. Incoming links, depth, sitemap and orphan status are unknown. No social profiles, authority evidence, competitor data, or actual AI answers were supplied. No `llms.txt` or special AI schema is required as a fix here. Google says its ordinary SEO guidance applies to AI Overviews and AI Mode; no special AI optimization is necessary. [Google: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features), checked 2026-11-24. Actual citations and eligibility remain unverified.

| Crawler / purpose | Captured policy | Infrastructure / action |
| --- | --- | --- |
| Googlebot / Search | `noindex` in saved HTML; robots.txt unknown | Live delivery, account controls and verified visits unknown; perform S01 |
| OAI-SearchBot / ChatGPT search | robots and actual access unknown | Inspect policy and delivery only with authorized access; don't infer citations |
| GPTBot / potential training | unknown | Separate owner policy choice, not a search fix |

OpenAI documents search and training crawlers separately: [OpenAI crawlers](https://developers.openai.com/api/docs/bots), checked 2026-11-24. No crawler policy change is implied or authorized.

**Next evidence and checkpoints:** obtain live response, robots.txt and declared sitemap, URL Inspection, contact-path test, country/language and lead definition. At 30 days record technical acceptance and available Search Console page/query impressions and clicks; at 60 days compare organic clicks and qualified leads against a comparable baseline; at 90 days reassess the offer and conversion rate with sufficient sample. Record dates, property, URL, device and geography; unknown or unavailable is not zero. Search Console Web data is not AI-only traffic.

# L02. Acme plans page

## Mode and summary
**Audit**, focused on the supplied source and browser DOM. The local fixture demonstrates that JavaScript populated its heading, text, contact link and description in the provided Chrome capture. It does not establish a live delivery or search-crawler failure, so a server-rendering rewrite is not justified on this evidence. The rendered page promises a plan choice without giving any plan details, an observable gap in the captured experience.

## Scope and evidence
`javascript.html`, `javascript-rendered.html`, `evidence-plans-source.json`, and `evidence-plans-rendered.json` were inspected 2026-11-24 for `https://acme.example/plans/`. Source is synthetic, capture time unknown. The supplied DOM was produced from this fixture in isolated headless Chrome 158.0.8127.37 on 2026-11-24, not from a live site or Googlebot. Collector parsing of saved DOM is not a new browser run. Source has title and canonical, an empty `#app`, and script constructing content and description. DOM has H1 “Acme plans,” “Choose a consultation plan,” contact link and “Compare Acme consultation plans” description. No source or DOM robots meta is observed; headers and other live directives remain unknown. No status, redirect history, robots.txt, sitemap, analytics or selected canonical is available. Country, demand and plan facts are unknown.

## Priority actions
| ID | Issue and stage | Impact | Effort | Dependency / owner | Timing |
| --- | --- | --- | --- | --- | --- |
| P01 | Rendered promise of plan choice lacks comparison details; retrieval and consultation conversion | Potentially meaningful, not quantified | 0.5–2 days subject to facts | Confirm actual offerings; owner/content editor | Now / next |

**P01: plan choice cannot be evaluated from the captured page.** The rendered body offers only the heading, one sentence and “Contact us”; it provides no plan differences or selection criteria. Confidence high for the local fixture, not for live content or actual visitor outcomes. Have the owner confirm whether distinct plans exist and supply accurate scope, eligibility and next steps; add a concise comparison only if true, or correct the page's promise if it is not. Keep a clear consultation route. **Acceptance:** render the actual page, confirm it accurately explains available options and how to proceed, and test the contact destination; do not invent plans, prices or commitments. Primary KPI: qualified organic consultation leads; secondary: conversion rate from organic sessions landing on this URL, qualified leads / eligible organic sessions. Baseline and definition are unavailable; review comparable periods at 60/90 days, segmented by geography and device where possible. Content changes need owner-approved facts and normal publishing authorization.

## Page and AI visibility
The local source/DOM difference is a **delivery observation**, not an established crawler or performance defect. Verify the live final response, DOM and error paths; if a specific search rendering or reliability failure is observed, diagnose that failure before choosing a remedy. Google Search's processing and other crawlers' behavior are not established by this Chrome fixture. The contact destination is untested; no broken-link or orphan claim is supported. There is no evidence of actual AI citations or external authority. The lack of plan facts limits useful answer coverage in this fixture; no special AI schema is required. [Google AI features guidance](https://developers.google.com/search/docs/appearance/ai-features), checked 2026-11-24.

| Crawler / purpose | Policy in evidence | Infrastructure / next check |
| --- | --- | --- |
| Googlebot / Search | Source and DOM show no generic robots meta; live headers and robots unknown | Inspect live directives, rendering and URL Inspection with authorization |
| OAI-SearchBot / ChatGPT search | Unknown | Inspect robots and delivery; do not infer access or citation |
| GPTBot / training | Unknown | Separate policy choice; no change proposed |

[OpenAI crawler documentation](https://developers.openai.com/api/docs/bots), checked 2026-11-24, distinguishes search from training. No bot setting has been inspected or changed.

**Next evidence and checkpoints:** establish geography, service facts and conversion definition; inspect live response, headers, robots, declared sitemap, canonical and contact flow. At 30 days establish technical and measurement baselines; at 60 and 90 days compare the page's organic clicks and qualified leads with matched prior periods, noting concurrent changes and incomplete data. Search Console Web reporting is not an AI-only click measure. A bounded manual citation sample may be designed from real customer questions once available, recording valid answers, failures, cited URLs and claim support separately; no citation baseline exists.

# L03. LinkedIn, X and website alignment

## Mode and summary
**Audit**, limited social-profile review. The supplied LinkedIn text identifies “Acme Example” and describes migration advice and consulting. It lists two domains without designating a primary website. Neither ownership nor the correct primary destination can be inferred from that alone. The export reports an X fetch returning HTTP 403 to the auditing client; this is not proof that the profile is unavailable to users or search crawlers. There is insufficient evidence for an actionable defect or a website SEO audit.

## Scope and coverage
Reviewed `social.txt` on 2026-11-24. The user-supplied synthetic public-profile text has no live capture time or authenticated account access. LinkedIn: **partial**, display name, bio and two links observed in export; current presentation and designated website field unknown. X: **blocked in supplied evidence**, 403 reported for that client; no profile content was provided and no new fetch was attempted. Website: **not assessed**; no HTML, response, ownership confirmation, analytics or account settings supplied. No live requests were made to either reserved domain or social profiles.

## Priority actions
No supported defect findings or scored actions. Confirm which of `https://acme.example/` and `https://acme-partners.example/` is the business website, and what relationship the other has, before proposing profile or canonical changes. Ask for the public X bio and link text or a fresh export. Then inspect the confirmed site's home and priority consultation pages, declared sitemap and robots policies, and compare actual entity and contact information with the profiles. Do not change a link merely because two links exist.

## Page, social and AI-search notes
A page-level SEO recommendation is not possible without a confirmed site and page evidence. Social name consistency, destination correctness, crawler access, structured data, citation quality and actual AI mentions are **unknown**, not failures. Crawler matrix: Googlebot/Search, OAI-SearchBot/ChatGPT search, and GPTBot/training all have unknown robots policy and infrastructure access; no policy change is recommended. [OpenAI crawler documentation](https://developers.openai.com/api/docs/bots), checked 2026-11-24, distinguishes search and training. Google describes ordinary Search practices as relevant to its AI features, not a special schema requirement: [Google AI features](https://developers.google.com/search/docs/appearance/ai-features), checked 2026-11-24.

**30/60/90-day measurement:** after ownership confirmation and appropriate access, establish a dated baseline for branded/non-brand Search Console clicks and impressions for the confirmed site and qualified consultation leads where tracked. At 60 and 90 days compare the same URL/query cohort, country, device and comparable periods, documenting attribution and missing values. Citation sampling, if later useful, requires a fixed question set and valid-answer denominator; failed captures are reported separately. No baseline or outcome has been observed and no recurring monitoring is authorized.
