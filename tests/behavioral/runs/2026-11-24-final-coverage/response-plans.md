# Acme plans: SEO and AI-search audit

## Mode and summary

**Audit mode**, limited to the supplied plans-page source and browser DOM. The consultation goal is important; the target geography, audience, offer details, search demand, and actual conversion performance are unknown.

The rendered page says “Choose a consultation plan” and links to contact, but provides no plan details to compare. That is the strongest actionable issue: visitors and answer systems lack the information needed to understand the offer before taking the next step. The page's content and description are injected by JavaScript, but the supplied local browser capture shows them rendered. That difference warrants a targeted delivery check, not a conclusion that Google or another engine cannot see the page or that server rendering is required.

## Scope and evidence

- Sample: `https://acme.example/plans/` only, a synthetic fixture and supplied base URL, not a live-site request. Source: `javascript.html`, original capture time unknown. Rendered DOM: `javascript-rendered.html`, generated from the fixture in isolated headless Chrome 158.0.8127.37 on 2026-11-24. This is local fixture rendering, not evidence of live or search-engine rendering.
- Offline extraction, 2026-11-24 UTC: [source evidence](source-evidence.json) and [rendered evidence](rendered-evidence.json). Both complete files were also inspected directly. Extractor timestamps are analysis times, not original capture times.
- Source contains title `Acme plans`, a canonical pointing to the supplied base URL, an empty `main#app`, and a script that injects the H1, text, contact link, and meta description. Rendered DOM contains those elements, including description `Compare Acme consultation plans.` and `/contact/` link. There are no robots meta tags or JSON-LD in either supplied artifact; response headers are unavailable. Absence of structured data alone is not a defect.
- HTTP status, actual final URL and redirects, `X-Robots-Tag`, robots.txt, sitemaps, other templates, contact destination and form, live browser behavior, field Core Web Vitals, indexing and selected canonical, rankings, backlinks, and actual AI answers/citations are **not assessed**. The contact link is not reported broken: its destination was not fetched. No social profiles were supplied.
- Search demand, country/language, business capacity, analytics, consultation completions, and whether this is a top-converting page are unknown. English is observed in the artifact; target market is not inferred from it. This is not a sitewide audit.

## Priority actions

| ID | Issue and stage | Expected impact | Effort | Dependency and owner | Timing |
| --- | --- | --- | --- | --- | --- |
| F01 | Plan comparison information missing; content / retrieval and conversion | High potential relevance to a consultation decision, but traffic and conversion effect unknown | 0.5-2 days provisionally | Confirm actual offers and permitted claims; product/content owner with developer | Now, 0-2 weeks |
| F02 | Source-to-DOM dependency; delivery / crawl hypothesis | Unknown until a relevant consumer or reliability problem is reproduced | < half day for initial checks; remediation effort unknown | Authorized live or staging response and inspection access; developer/SEO owner | Now, after access |

Priorities are qualitative: a numeric score would imply knowledge of demand, implementation capacity, and conversion performance that is not available. F01 is first because it affects the stated consultation goal in the one observed page. F02 is validation first, not a mandated architecture change.

### F01: Give visitors the information needed to choose

**Observed, high confidence for this fixture only.** The complete rendered main contains one heading, a single sentence, and `Contact us`; it contains no plan names, differences, inclusions, prices or pricing approach, eligibility, or explanation of what happens next. The description promises a comparison that the visible page does not supply. Source and DOM evidence are the supplied artifacts above. This does not establish that the real offer has multiple plans or that specific prices exist.

**Action:** Confirm with the offer owner what is actually sold and whether there are distinct plans. If there are, add accurate, visible comparisons of the distinctions customers need, such as scope, duration, pricing or how pricing is determined, and the consultation process, only where confirmed. If there is no comparison to make, revise the page's promise and description to match the actual offer. Keep a clear consultation/contact route; verify its destination and wording against the real next step before changing the CTA. This is a content and conversion improvement, not a guaranteed ranking or citation improvement.

**Acceptance:** Reinspect the actual affected page in source and rendered view: the stated plan/comparison promise matches visible, owner-approved details and the consultation link leads to the intended working next step. Test keyboard access and form/confirmation behavior if the destination is in scope. Record the deployed revision separately from the local fixture.

**Measurement:** Baseline unavailable. Primary: qualified consultation completions attributable to organic landings on this URL, from consented analytics/CRM with an agreed event and qualification definition. Secondary: organic search clicks to this URL, if Search Console access exists. Compare comparable pre/post windows, segment country, device, branded/non-branded query where available, and record concurrent changes and incomplete data. Review at 30/60/90 days; traffic changes alone cannot establish causality. If the fixture is not a real deployment, these metrics do not apply until a real page is identified.

### F02: Validate the JavaScript-dependent delivery path

**Observed difference; delivery problem is a hypothesis, low confidence.** The source has an empty main and injects the page content and description through inline JavaScript; the supplied Chrome DOM includes them. This is evidence of successful local browser execution, not proof of successful or failed search-engine rendering, live reliability, or an SEO blocker.

**Action:** When an authorized real environment exists, capture the complete served response, headers, status, final URL and rendered DOM for this route; compare with the intended content and use authorized search-engine URL inspection where available. Check failures in the actual delivery path if those checks expose missing content. Only investigate a targeted rendering, script, or caching fix if a relevant failure is reproduced; do not rebuild or add server rendering on the basis of this fixture alone.

**Acceptance:** A documented fresh capture shows the intended page content and contact path in the relevant browser and the available engine inspection, with statuses and limitations recorded. If an engine inspection is unavailable, report that gap rather than claiming engine success. No policy or training-crawler changes are implied.

**Measurement:** Baseline and affected population unknown. Primary is the proportion of specifically tested, successful relevant captures showing the intended content, with failed or unavailable captures reported separately; this is a technical diagnostic, not a traffic metric. Secondary is qualified organic consultation completions as defined under F01. Review after any confirmed fix and at the next 30-day checkpoint; do not infer causal impact from this small sample.

## Page-level and AI-search readiness

- **Plans page:** Resolve F01 before optimizing snippets around a comparison. Preserve the existing canonical as an observed declaration only; its live redirect consistency and engine-selected canonical remain unknown. The rendered title, H1 and description identify Acme and plans, but do not identify the service beyond consultation. Improve specificity only from verified offer details.
- **Citation and entity readiness:** The fixture supplies only the name Acme and a generic consultation description. Confirm the organization's identity and add accurate service detail and substantiation where relevant. No specific unsupported factual claims were observed, and no citation presence or absence was measured. Do not invent an author, proof, prices, schema, or claims. No special AI markup is proposed.
- **Crawler coverage:** Google Search/AI features, Bing/Copilot and ChatGPT search were not directly requested by name and were not tested. For Googlebot, Bingbot and OAI-SearchBot, robots rules, infrastructure access, verified requests, engine rendering/indexing and citations are all **unknown**. GPTBot training controls are a separate owner choice and also unknown. No crawler-policy change is recommended based on these artifacts. Search Console/account inclusion controls are likewise not assessed.
- **Experiment, not a platform requirement:** After verified content is available, optionally compare a fixed, small set of genuine consultation questions before and after the improvement. Record exact prompts, surface/model, locale, dates, valid answers, linked URLs and whether each cited claim is supported. Report valid answers citing the page divided by valid captured answers, and failed captures separately; a small sample is not market-wide visibility. Control for concurrent page and platform changes where feasible. Do not imply that citation frequency proves conversions.

## 30/60/90-day tracking and next evidence

- **30 days:** Confirm the real offer and target geography, capture the real baseline and access where authorized, complete F01, and perform F02's bounded delivery checks. Record technical acceptance independently from business outcomes.
- **60 days:** Review qualified organic consultation completions and page-level organic clicks against a comparable baseline; inspect the contact funnel and segmentation if instrumentation permits. Note small samples, seasonality and other releases.
- **90 days:** Reassess the same metrics and any bounded citation sample. Iterate only on observed gaps; no uplift or ranking outcome is promised.

To refine priorities, provide the real page or authorized captures, target market and audience, confirmed plan details, the intended consultation conversion and contact flow, and any available Search Console and analytics baselines. Robots/sitemap, HTTP headers, index status, field performance, other pages and social alignment remain unassessed until relevant evidence is provided. No network requests to the fixture domain were made.
