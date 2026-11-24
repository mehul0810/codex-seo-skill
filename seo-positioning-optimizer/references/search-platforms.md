# Search Platforms And Controls

Read only the rows relevant to the audience and requested surfaces. This is a routing matrix, not evidence that any site is eligible, indexed, cited, or configured correctly. Recheck each material rule in current primary documentation before recommending changes. Do not apply Google's rules to another provider.

## Purpose And Access Matrix

For each relevant agent or control record: purpose, effective robots/header/account policy, verified request identity and response, edge/WAF evidence, documentation date, unknowns, and proposed action. Search, potential training, and user-directed retrieval can have different rules. Separate agent names do not guarantee independent effective policies; check fallback and precedence. Preserve owner choices, and do not change policies merely to run an audit.

Primary pages below were checked on 2026-11-24. Existing Google/Bing reporting details and source-specific older dates remain in `ai-search-optimization.md`.

| Surface | Primary source and specific check | Interpretation limit |
| --- | --- | --- |
| Google Search / AI Overviews / AI Mode | [Search generative AI control](https://support.google.com/webmasters/answer/16908024): inspect the effective property setting, parent inheritance and overrides, alongside index/snippet eligibility | Public HTML does not establish account state. This is separate from ordinary Search inclusion and training permission |
| Bing / Copilot | [AI Performance additions](https://blogs.bing.com/search/2026/6/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare/): check available account reports and their definitions | Preview availability and classifications need verification; citations are not traffic |
| Yandex AI | [Yandex AI guidance](https://yandex.com/support/webmaster/en/yandex-ai): check Yandex indexing evidence and `YandexAdditional` / `YandexAdditionalBot` directives | AI answers use Yandex-indexed pages; exclusions take effect after recrawl. Google state does not establish Yandex state |
| ChatGPT search | [OpenAI crawlers](https://developers.openai.com/api/docs/bots): `OAI-SearchBot` for search, `GPTBot` for potential training, `ChatGPT-User` for user-directed retrieval | Blocking training is not a search defect. User-directed fetch rules may differ; use the documented identity checks |
| Claude | [Anthropic crawlers](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler): distinguish `Claude-SearchBot`, `ClaudeBot`, and `Claude-User` | Search, potential training, and user retrieval differ; verify precedence and rollout for additional preference signals |
| Perplexity | [Perplexity crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers): distinguish `PerplexityBot` search crawling from `Perplexity-User` retrieval | User-directed requests generally differ in robots behavior. Match published IP information and agent before attributing requests; logs do not prove answer use |
| DuckDuckGo AI answers | [DuckAssistBot](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot): check the AI-answer fetch policy separately from organic search | Provider says this opt-out does not affect ordinary result appearance/ranking; do not treat it as a general search opt-out |
| Naver | [Search Advisor guide](https://searchadvisor.naver.com/guide/seo-basic-intro): Yeti, host ownership, crawlable links, sitemap/RSS discovery | The guide contains legacy wording; verify the applicable procedure. Submission is not indexing proof |
| Amazon / Alexa | [Amazon agents](https://developer.amazon.com/docs/amazonbot/amazonbot): `Amazonbot` may support training, `Amzn-SearchBot` search, `Amzn-User` user retrieval | Check documented search-agent fallbacks when no explicit rule exists. Do not recommend blanket AI-bot access |

For other regional engines, find their current primary guidance first. If official Baidu documentation or another provider's page cannot be opened, record primary verification as incomplete; secondary advice can guide investigation but cannot become verified platform policy.

## Surface Versus Provider

Sources checked 2026-11-24:

- [DuckDuckGo sources](https://duckduckgo.com/duckduckgo-help-pages/results/sources): traditional links/images largely come from Bing, alongside other sources. This does not imply identical results.
- [Ecosia providers](https://support.ecosia.org/article/579-search-results-providers): provider choice can depend on market, device, and permissions. Capture the provider disclosed for the actual sample rather than assigning one globally.
- [Kagi sources](https://help.kagi.com/kagi/search-details/search-sources.html): own indexes and external sources combine with personalization/lenses. Record exposed context; do not infer a hidden provider or treat personalized samples as market-wide results.

Use distinct surface records even when providers overlap, but do not count shared infrastructure as independent evidence for a causal claim.

## Emerging Preference Signals

Track only when relevant to a named consumer. Record version/status, known adoption, rollout, precedence against existing rules, and current primary evidence. The [training preference signal](https://datatracker.ietf.org/doc/draft-kelley-aipref-training-preference-signal/) was an individual Internet-Draft, not an endorsed standard, when checked on 2026-11-24. Recheck status before use. A proposal or one consumer's implementation is not universal support, an access-control boundary, or permission to change the owner's training policy.
