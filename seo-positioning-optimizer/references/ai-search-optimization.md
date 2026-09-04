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
- For Google AI Overviews and AI Mode, apply normal Google Search eligibility and SEO practices. Google states that no special AI schema or additional technical requirement is needed.
- Audit `Googlebot` access for Google Search. Discuss `Google-Extended` separately because it is not the control for inclusion in Google Search AI features.
- Audit `OAI-SearchBot` for ChatGPT search visibility. Treat `GPTBot` as a separate model-training control.
- Audit `Bingbot`, sitemap freshness, and IndexNow when Bing/Copilot matters. IndexNow notifies participating engines about changed URLs; it does not guarantee indexing or ranking.
- Check CDN, WAF, bot-management, and server-log behavior in addition to robots.txt. A crawler allowed in robots.txt may still be blocked elsewhere.
- Report user-agent policy in a matrix: crawler, purpose, robots rule, infrastructure access, evidence, recommended action.

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
- use structured data that is valid, supported by Google, and consistent with visible page content.

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
- Bing Webmaster Tools: AI Performance citations and cited URLs when the feature is available to the property.
- Analytics: referrals from AI assistants, landing pages, engaged sessions, assisted conversions, and conversion rate.
- Entity demand: branded queries, direct traffic, mentions, and qualified backlinks.
- Citation sampling: repeat a stable, documented prompt/query set on a schedule; record whether the site is cited, the cited URL, context, and competitors.

Do not add platform citations and referral sessions together as if they were the same metric.

## Experiments

Run bounded tests with a baseline, changed pages, control pages where possible, and a 30-90 day observation window:

- improve first-party evidence and source citations;
- clarify entity/about/author information;
- consolidate cannibalizing pages;
- add or correct supported structured data;
- improve answer completeness for a defined question set;
- allow a target search crawler through robots.txt and infrastructure;
- optionally publish `llms.txt`, but measure it separately and state that major search platforms do not require it for search eligibility.

## Primary Sources

Verified 2026-09-04:

- Google Search Central, AI features and your website: https://developers.google.com/search/docs/appearance/ai-features
- Google Search Central, creating helpful, reliable, people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Google Search Central, structured data introduction: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- Google Search Central, spam policies: https://developers.google.com/search/docs/essentials/spam-policies
- OpenAI crawler documentation: https://platform.openai.com/docs/bots
- Bing Webmaster Blog, AI Performance public preview: https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview
- IndexNow protocol documentation: https://www.indexnow.org/documentation
- Aggarwal et al., "GEO: Generative Engine Optimization": https://arxiv.org/abs/2311.09735

The GEO paper reports experimental visibility gains in its benchmark and emphasizes domain-dependent results. Treat its tactics as research-backed hypotheses, not universal production guarantees.
