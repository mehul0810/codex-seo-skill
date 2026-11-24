# L01: Services page audit

**Mode: audit**, focused on the priority consultation landing page and the one developer day available. The most important issue is a `noindex` directive in the supplied capture, which conflicts with your stated intention for the page to appear in search. Confirm that the capture reflects the current response before changing anything. The captured page also gives prospective clients little detail to assess the service, but demand and conversion effects are unknown.

## Evidence and coverage

On 2026-11-24 I inspected the complete supplied `service.html` offline with the evidence collector and directly. It represents `https://acme.example/services/`; its original capture time, live status, response headers and redirect history are unknown. The capture has a self-referencing canonical, a title, description, H1 and a link to `/contact/`. The link destination was not fetched, so its health is unknown. This is one page, not a site crawl. Country, language target beyond the English capture, CMS, keyword demand and analytics are unknown. Google Search, other search engines, AI citations, robots.txt, sitemap, actual indexing, page rendering and social profiles were not assessed. The fixture domain was not fetched.

| ID | Issue and stage | Expected impact | Effort / owner | Dependency / timing |
| --- | --- | --- | --- | --- |
| S1 | Captured `noindex` conflicts with search intent; indexing | High for eligibility if also served live; no traffic guarantee | < half day, developer | Verify current response and confirm intent; first this week |
| S2 | Service and consultation details are sparse; retrieval and conversion | Potentially meaningful for qualified leads, uncertain without customer/query evidence | < half day for a scoped draft, content owner; developer as needed | Confirm accurate offer details; after S1 |

**S1. Captured indexing directive.** Confirmed in the saved HTML, high confidence for that artifact only: `<meta name="robots" content="noindex, follow">`. Current live state and Google index status are unknown. Google documents that a crawler-accessible `noindex` prevents inclusion when Google encounters it; a robots.txt block can prevent Google from seeing the directive. [Google: Block Search indexing with noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing) (checked 2026-11-24). This is a material risk for the owner's priority lead page, not proof of its present index status.

Action: inspect the current full response and headers, redirects, rendered DOM, robots.txt, and relevant agent-specific directives. If `noindex` is currently served and unintended, remove it at its source without changing unrelated crawler or privacy policies. **Acceptance:** a fresh response and DOM at the intended final URL contain no conflicting `noindex`, including `X-Robots-Tag`; verify that the relevant search crawler can access it. Separately use authorized Google URL Inspection to check its indexed state and selected canonical. Indexing may take time and is not the technical acceptance criterion. Owner: developer. Baseline: captured directive present; live baseline unknown. KPI: non-brand organic clicks to the page from Search Console, compared with a comparable pre-change period over 30/60/90 days, segmented by country/device and query where available; qualified organic consultation leads are secondary, if tracking exists.

**S2. Make the offer easier to evaluate.** Confirmed limited copy in the capture: “Speak with our team about your project” and a contact link, with no visible explanation of consultation scope or outcome. Confidence is high for the capture, low for the effect on leads. Ask the service owner for verified audience, migration scope, what happens in a consultation, and next steps; add only accurate details and a descriptive consultation CTA if appropriate. Do not invent prices, guarantees or expertise. **Acceptance:** the current page visibly explains the confirmed offer and next step, and the CTA reaches the intended contact flow in a functional test. Baseline and primary KPI: qualified consultation leads originating from this page, currently unknown; record source and qualification definition before comparing equivalent periods. Secondary: relevant Search Console query impressions/clicks. No uplift is assumed.

## Plan and measurement

- **Now, 0–2 weeks:** Reserve the developer day for S1 verification, correction if needed, and recheck; use any remaining time to ship the small, owner-approved S2 content update. No deployment is implied by this audit.
- **Next, 2–6 weeks:** With access, check the page's indexing and canonical, discovery through actual internal links and sitemap, and contact-flow completion. Review queries and lead quality before further content expansion.
- **Later, 6–12 weeks:** Reassess based on observed queries and qualified leads; investigate other pages only when sample evidence supports it.
- **30/60/90 days:** Establish available baselines first, then compare the same page, query groups, geography and devices over comparable periods. Search Console clicks/impressions are not qualified leads; track lead source and qualification separately. No analytics export was supplied, so no baseline or forecast is asserted.

**AI-search coverage:** Googlebot, Bingbot and OAI-SearchBot robots rules and infrastructure access are unknown; actual AI answers/citations and training policy are not assessed. Do not change crawler policies on this evidence. Google says its usual Search practices apply to AI features, without a special AI schema requirement: [Google AI features guidance](https://developers.google.com/search/docs/appearance/ai-features), checked 2026-11-24. The page's sparse offer explanation is an opportunity to improve clarity for people, not proof of a citation deficit.

# L02: Plans page audit

**Mode: audit.** The local fixture renders a heading, short description, contact link and meta description in Chrome. The source relies on JavaScript for those elements, but that alone is not a demonstrated search defect and does not justify a rendering rebuild. The more concrete opportunity is that the supplied rendered page says “plans” without providing plan details to help a visitor decide whether to consult.

## Evidence and coverage

Inspected `javascript.html` and `javascript-rendered.html` offline on 2026-11-24 with the collector and direct reading. Base URL: `https://acme.example/plans/`. The source is synthetic, original capture time unknown; the supplied DOM was generated from it in isolated headless Chrome 158.0.8127.37 on 2026-11-24. This proves local fixture rendering only, not live behavior, performance or Googlebot rendering. Source contains title and self-canonical, an empty `main`, and a script that inserts the H1, paragraph, contact link and meta description. The supplied DOM contains those elements. The link target was not fetched. Live status, headers, redirects, robots.txt, sitemap, selected canonical, index status, analytics, real customer demand, geography and actual AI citations are unknown. The fixture domain was not fetched.

| ID | Issue and stage | Expected impact | Effort / owner | Dependency / timing |
| --- | --- | --- | --- | --- |
| P1 | Rendered plan page lacks plan comparison information; retrieval / conversion | Potentially meaningful for consultation intent; effect unmeasured | < half day to draft, content owner; developer as needed | Confirm actual offer; now |
| P2 | Client-rendered core content creates a testable delivery risk, not a proven defect; delivery / retrieval | Unknown until relevant live consumer evidence | < half day to inspect, developer | Access to live response and authorized inspection; next |

**P1. Explain actual plans.** The supplied DOM consists of “Acme plans,” “Choose a consultation plan,” and “Contact us”; it does not state what the plans include, who each serves, or how to choose. Confirmed in this fixture with high confidence; live scope and conversion impact unknown. Ask the offer owner for accurate plan distinctions and consultation next steps, then present the confirmed information in visible, readable text and make the CTA accurately describe its destination. Do not invent prices or promises. **Acceptance:** a fresh rendered page shows approved plan details and a working contact route; any metadata accurately reflects the visible content. Owner: content owner and developer. Primary KPI: qualified organic consultations landing on the page, baseline unknown; secondary: relevant page-level organic clicks. Compare equivalent periods after measurement is available, at 30/60/90-day checkpoints.

**P2. Validate the specific rendering hypothesis before changing architecture.** The empty source `main` contrasts with the locally rendered DOM. This supports a hypothesis that a particular consumer might not receive core content, not a finding that Google or any AI crawler fails. Confidence in the difference is high; confidence in live impact is low. Check the current complete response, rendered DOM and relevant authorized URL Inspection or verified crawler evidence, including any execution errors and final response. **Acceptance:** the priority content and working link are observable in the actual user experience and the relevant inspected search rendering; if a specific failure is reproduced, fix its narrow cause and repeat those checks. Do not mandate SSR, prerendering or a framework migration based on this fixture. Owner: developer; baseline unknown. Technical pass is separate from organic click and lead outcomes.

## AI discovery and next evidence

| Crawler / purpose | Policy and infrastructure | Evidence / action |
| --- | --- | --- |
| Googlebot, Search | Unknown | Check served robots, response and authorized inspection; no live access evidence supplied |
| Bingbot, Search | Unknown | Check only if Bing is a target; no crawler evidence supplied |
| OAI-SearchBot, ChatGPT search | Unknown | Check separately if targeted; no verified visits or citations supplied |
| GPTBot, potential model training | Unknown | Separate policy decision, not interchangeable with search access |

OpenAI distinguishes search from training crawlers in its [crawler documentation](https://developers.openai.com/api/docs/bots), checked 2026-11-24. Do not alter either policy as part of this audit. Google states that no special AI markup is required for its AI features: [Google AI features guidance](https://developers.google.com/search/docs/appearance/ai-features), checked 2026-11-24. No structured data appears in the supplied fixture; absence alone is not a defect. No AI answers were sampled, so citation presence, accuracy and competing sources are unknown. Clarify the organization and actual offers in visible copy rather than manufacture claims or schema.

**Roadmap:** now, establish accurate plan details and review P1; next (2–6 weeks), perform P2 and check current robots, sitemap, canonical and indexing; later (6–12 weeks), use actual search queries and lead quality to decide whether further pages or content are worthwhile. At 30/60/90 days compare the same page, geography, device and query cohorts against a recorded baseline; track search clicks and qualified leads as separate units. No baseline, ranking or impact is inferred. No social URLs were supplied.

# L03: LinkedIn, X and website alignment

**Mode: audit, limited to the supplied profile export.** Do not choose a primary website or change profile links yet. The export lists two domains but does not establish which is the business website or their relationship. The X request returned a client-side 403 in the supplied evidence; that is not evidence of an X profile problem. Website SEO cannot be audited without an established website and page evidence.

## Coverage

On 2026-11-24 I read `social.txt`, a user-supplied synthetic public-profile text export with no live capture time. The LinkedIn text identifies “Acme Example,” bio “Migration advice and consulting,” and links to `https://acme.example/` and `https://acme-partners.example/`; no designated website field is included. This is partial LinkedIn coverage, not a live profile or authenticated account inspection. X coverage is blocked in the supplied export by HTTP 403 from the auditing client, with no profile content observed. Website, search engines, crawler policies, index status, analytics, structured data and AI citations are not assessed. Neither fixture domain nor social profile was fetched.

**Question:** Which of the two domains is Acme Example's primary business website, and what is the relationship of the other domain? Please also provide the X profile URL and a current public text export or screenshot, plus the primary target geography and consultation goal if relevant. Until ownership is confirmed, neither domain should be treated as canonical or as an erroneous link.

| ID | Issue / stage | Expected impact | Effort / owner | Dependency / timing |
| --- | --- | --- | --- | --- |
| L3-1 | Two linked domains have an unclear relationship in the supplied text; entity / referral clarity | Potential confusion for visitors; actual confusion and impact unverified | < half day, business owner | Confirm ownership and intended destinations first; now |

**L3-1. Verify the linked identities before editing.** Confirmed only that both links occur in the export, not that the live profile lacks a designated website or that either link is wrong. Medium confidence for the export, low for any user impact. Once ownership and intent are established, check each current link's destination and whether its label or surrounding context accurately describes its purpose. If genuine confusion is observed, clarify the profile wording or destination with approved facts; do not remove a valid partner link simply because there are two. **Acceptance:** a fresh profile view presents the owner-confirmed primary site and any partner destination with accurate, distinguishable context, and each tested link reaches its intended destination. Owner: business/profile owner. Primary metric, if available: qualified referrals from LinkedIn to the intended landing page, baseline unknown; secondary: link clicks where available. Compare same periods and attribution rules, not search rankings as a proxy for profile quality.

## Next evidence and roadmap

- **Now, 0–2 weeks:** Resolve the domain question; obtain current profile and site evidence. No site or account changes are authorized by this audit.
- **Next, 2–6 weeks:** Once the website is confirmed, inspect its homepage and priority service page, navigation and declared sitemap, current response and canonical/robots directives; compare its name and links against both supplied profile texts. Check link destinations without interpreting a blocked fetch as a site defect.
- **Later, 6–12 weeks:** Based on observed site and query evidence, prioritize any supported content and internal-link changes. Do not infer backlinks, rankings or brand inconsistency from this export.
- **30/60/90 days:** If measurement exists, record LinkedIn referral sessions and qualified leads separately, with source, landing page, geography, comparison period and attribution limits. Search Console page/query clicks and impressions are separate metrics. No baseline or expected uplift is available.

**AI-search and crawler matrix:** Googlebot, Bingbot, OAI-SearchBot and GPTBot rules, infrastructure access, identity-verified visits and citations are all unknown for both domains. First confirm the business domain and target surfaces; preserve existing search and training policies. No platform-specific eligibility or citation claim can be made from the profile text alone.
