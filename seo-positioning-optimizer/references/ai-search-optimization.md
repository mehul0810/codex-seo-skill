# AI Search Optimization Reference

Use this reference for AEO, GEO, AI Overviews, AI Mode, ChatGPT search, and Bing/Copilot visibility. Verify platform-specific details against current primary documentation because crawler names, controls, and reporting can change.

## Evidence Hierarchy

Label recommendations by evidence strength:

1. `platform requirement`: stated in current official documentation.
2. `established SEO practice`: supported by search-engine guidance and observable crawl/index behavior.
3. `research-backed hypothesis`: supported by published research but not guaranteed by a platform.
4. `experiment`: plausible but unverified; define a test and success metric.

Never convert a hypothesis or experiment into a claimed ranking factor.

## Eligibility And Crawler Controls

- Start with indexability, crawl access, canonical consistency, accessible HTML, internal links, and sitemap health.
- For Google AI Overviews and AI Mode, apply normal Google Search eligibility and SEO practices; no special AI schema is needed. Also verify the Search Console inclusion control below instead of relying solely on older eligibility summaries.
- Audit `Googlebot` access for Google Search. Discuss `Google-Extended` separately because it is not the control for inclusion in Google Search AI features.
- Audit `OAI-SearchBot` for ChatGPT search visibility. Treat `GPTBot` as a separate model-training control.
- Audit `Bingbot`, sitemap freshness, and IndexNow when Bing/Copilot matters. IndexNow notifies participating engines about changed URLs; it does not guarantee indexing or ranking.
- Check CDN, WAF, bot-management, and server-log behavior in addition to robots.txt. A crawler allowed in robots.txt may still be blocked elsewhere.
- Report user-agent policy in a matrix: crawler, purpose, robots rule, infrastructure access, evidence, recommended action.
- Check the current Search Console Search generative AI control when relevant and authorized, including parent-property inheritance and child overrides. It manages inclusion in supported Search/Discover AI features, not model training or ordinary Search ranking. Public HTML cannot reveal the account setting. Preserve it unless the owner authorizes a change. Do not describe robots and snippet directives as the only available controls.

## Content And Citation Readiness

Evaluate whether priority pages:

- answer the primary question directly before expanding into detail;
- cover related subquestions without mixing incompatible search intents;
- name the organization, product, author, and relevant entities consistently;
- support factual claims with original data, methodology, primary sources, or reputable citations;
- expose author/reviewer identity, publication date, update date, and correction policy when relevant;
- use descriptive headings, lists, tables, definitions, and concise passages where these improve human comprehension;
- provide genuinely differentiated information such as research, benchmarks, examples, templates, tools, datasets, or expert experience;
- keep important facts in crawlable text rather than only images, video, or client-side interactions;
- use semantically valid structured data consistent with visible content; check Google support separately when recommending rich results.

Do not optimize prose merely to create quotable fragments. Clarity, accuracy, completeness, and original value come first.

## Query And Competitor Analysis

In `deep` mode:

1. Define the core user task and primary query intent.
2. Build a bounded set of related questions, comparisons, constraints, and follow-up queries.
3. Map each question to the best existing or proposed canonical page.
4. Sample search results and AI answers where accessible; record cited domains and exact source URLs.
5. Compare source quality, entity clarity, evidence, freshness, and answer completeness.
6. Recommend consolidation when multiple pages compete for the same intent; recommend expansion only when a distinct user need exists.

Treat the query-fan-out model as a useful analysis technique, not a promise about the exact internal queries a system uses.

## Measurement

Use multiple signals because no single platform provides a complete AI-visibility metric:

- Google Search Console: clicks, impressions, CTR, positions, query/page groups, and conversions joined from analytics. Google reports AI-feature traffic within Search Console's Web search reporting.
- Use the separate Generative AI performance report (Search) when available to the property. Current documentation describes AI Overviews/AI Mode impressions, with page/country/date/device breakdowns, not AI-only clicks or conversions. Absence may mean insufficient impressions, not zero visibility. Exported unavailable values can become zero; preserve that distinction and report aggregation/period limits.
- Bing Webmaster Tools: AI Performance citations and cited URLs when the feature is available to the property.
- If Bing Topics Portfolio is available, use its approximate topic sizes and opportunity ranges as planning inputs only. Classification can be imperfect, competitor-branded queries can appear, and insufficient data can hide topics. It is not exact search volume or assured opportunity.
- Analytics: referrals from AI assistants, landing pages, engaged sessions, assisted conversions, and conversion rate.
- Entity demand: branded queries, direct traffic, mentions, and qualified backlinks.
- Citation sampling: repeat a stable, documented prompt/query set on a schedule; record whether the site is cited, the cited URL, context, and competitors.

Record platform/model when exposed, date, locale, search mode, exact prompts, repeat count, and citations for every sample. Define citation rate as responses citing the site divided by observed responses, disclose the denominator, and distinguish mentions from linked citations. Sampling is variable and is not a market-wide visibility estimate. Do not infer an AI-only Google traffic total from aggregated Web data or equate Bing citations with rank, endorsement, clicks, or conversions.

Do not add platform citations and referral sessions together as if they were the same metric.

## Experiments

Run bounded tests with a baseline, changed pages, control pages where possible, and a 30-90 day observation window:

- improve first-party evidence and source citations;
- clarify entity/about/author information;
- consolidate cannibalizing pages;
- add or correct supported structured data;
- improve answer completeness for a defined question set;
- allow a target search crawler through robots.txt and infrastructure;
- consider `llms.txt` only for an identified downstream consumer. Google's June 2026 clarification says it does not affect Google visibility or rankings; do not prioritize it as a Google SEO experiment. Verify other platforms individually.

Inspect snippet controls (`nosnippet`, `max-snippet`, `data-nosnippet`, `noindex`) when relevant: Google supporting-link eligibility requires indexing and snippet eligibility. Explain visibility tradeoffs before changing controls. Preserve the owner's separate choices for search access and model training.

## Primary Sources

Focused verification on 2026-11-06 (other historical source dates below remain unchanged):

| Source | Claim checked | Limit |
| --- | --- | --- |
| [Google AI features](https://developers.google.com/search/docs/appearance/ai-features) | Search eligibility and aggregated Web reporting | No citation or indexing guarantee |
| [Google AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | Original useful content; avoid artificial chunking and inauthentic mentions | Not a citation formula |
| [Google content controls](https://developers.google.com/search/docs/crawling-indexing/control-what-you-share) | Search generative AI control exists in Search Console | Account state needs separate inspection |
| [Search generative AI control](https://support.google.com/webmasters/answer/16908024) | Inclusion, inheritance, and distinction from training/ordinary Search | Read the effective property setting; do not assume defaults |
| [Generative AI performance report](https://support.google.com/webmasters/answer/16984139) | Separate impressions report and export/aggregation limits | Property visibility depends on sufficient impressions; no AI-only conversion metric |
| [OpenAI bots](https://developers.openai.com/api/docs/bots) | Independent search and training crawler purposes | No inference about actual visits from robots.txt |
| [Bing AI Performance](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/) | Citations do not establish placement or authority | Aggregated surfaces and sampled queries |
| [Bing Topics Portfolio](https://blogs.bing.com/webmaster/2026/10/introducing-topics-portfolio-beta-in-ai-performance/) | Approximate opportunity data and beta limitations | Only when available to the property |

Use the coverage ledger and revalidation triggers in `audit-delivery.md`; do not claim all named platforms were assessed.

Verified 2026-09-04:

Additional review 2026-09-06: checked Google AI eligibility and documentation changelog, OpenAI crawler documentation, and Bing AI Performance. Recheck individual sources before making new platform claims.

- Google Search documentation changelog: https://developers.google.com/search/updates

- Google Search Central, AI features and your website: https://developers.google.com/search/docs/appearance/ai-features
- Google Search Central, creating helpful, reliable, people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Google Search Central, structured data introduction: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- Google Search Central, spam policies: https://developers.google.com/search/docs/essentials/spam-policies
- OpenAI crawler documentation: https://platform.openai.com/docs/bots
- Bing Webmaster Blog, AI Performance public preview: https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview
- IndexNow protocol documentation: https://www.indexnow.org/documentation
- Aggarwal et al., "GEO: Generative Engine Optimization": https://arxiv.org/abs/2311.09735

The GEO paper reports experimental visibility gains in its benchmark and emphasizes domain-dependent results. Treat its tactics as research-backed hypotheses, not universal production guarantees.
