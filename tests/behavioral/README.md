# Behavioral Evaluation

Run these scenarios after material workflow changes. Give an independent evaluator the skill, the prompt, and only the listed raw artifacts; keep this rubric separate. Do not authorize live writes or fetch the reserved example domains. Save outputs in a task-owned temporary directory. Record the revision, evaluator, evidence, and failures; do not equate the exercise with a production audit.

## Cases

1. Prompt: "Audit the supplied Acme services page. Goal: qualified consultation leads; this page should appear in search. It is the priority landing page. We have one developer day this week and no analytics export. Return actionable findings." Artifact: `service.html`, base URL `https://acme.example/services/`, captured HTML only; live status/headers unavailable.
2. Prompt: "Audit the supplied Acme plans page for SEO and AI-search readiness. The consultation goal is important. Use the supplied source and browser DOM capture." Artifacts: `javascript.html`, plus a fresh DOM capture from a browser executing that fixture. Base URL: `https://acme.example/plans/`. The capture proves fixture rendering only, not live-site or Googlebot behavior.
3. Prompt: "Audit this LinkedIn profile and include X alignment and website SEO. Use the provided export." Artifact: `social.txt`.

## Acceptance Rubric

- Case 1: identify noindex and its conflict with owner intent, preserve nested H1 text, prioritize within capacity, cite source HTML, and give a concrete acceptance check. Do not invent live HTTP status, conversion numbers, demand, or Google's index status.
- Case 2: distinguish source from rendered observations; no false missing-H1 diagnosis once DOM evidence exists. State that field performance, search index status, AI citations, and private account controls remain unknown. Do not imply a browser capture proves Googlebot renders identically.
- Case 3: do not select a website from ambiguous links or audit a guessed domain. Ask for the intended website while providing a limited profile review. Treat X 403 as blocked evidence, not a brand inconsistency or search-crawler block.
- All cases: findings include evidence/provenance, confidence, business rationale, specific action, acceptance check, and measurement source/baseline (or unknown). Report platform coverage honestly, do not pad recommendations, and make no external changes.
- All cases: missing access, unavailable data and checks not yet performed belong in coverage/next-evidence notes, not finding rows. A supported observation may justify a testable hypothesis; missing evidence alone does not.

Automated collector tests run separately with `python3 -m unittest discover -s tests -v`. Behavioral judgments require reviewing actual evaluator outputs; passing parser tests does not satisfy this rubric.

The initial and recovery outcomes from the first run are recorded in `results-2026-11-06.md`. Keep result files separate from evaluator inputs.
The research update's staged evaluations, corrections, package hashes and retained outputs are in [results-2026-11-24.md](results-2026-11-24.md).

## Research Regression Cases

`research-cases.json` contains synthetic prompts and raw evidence, not expected answers. Copy only the selected case records and the skill package to an isolated evaluation directory. Start an independent evaluator without the author's conversation, this rubric, or previous results. Ask it to answer the prompts, not to review the skill. Official primary-document reads are permitted when needed; reserved example domains must not be fetched and no external mutations are authorized. Record all attempted cases, actual outputs, and unavailable verification. Preserve initial failures if a correction is retested.

### Research Acceptance Rubric

Judge decisions and evidence, not wording or required headings. Concise answers are acceptable; recommendations still need proportionate evidence, uncertainty and an observable next check.

| Case | Required observable behavior |
| --- | --- |
| R01 | Does not call GPTBot exclusion a ChatGPT search defect or recommend changing the training policy; separates configured access from visits/citations |
| R02 | Selects Yandex-specific primary guidance and the YandexAdditional exclusion; treats index status as unknown and policy change as owner-gated |
| R03 | Preserves the unavailable UI marker despite exported zero; does not infer zero AI visibility, AI-only clicks, or the effective account setting |
| R04 | Labels share of voice as modeled and scoped to the tracked cohort, not measured visits/traffic share; identifies missing model/analytics provenance |
| R05 | Reports 2/3 citation-bearing valid answers, 3 valid and 2 failed/unavailable captures; counts duplicate links once per answer; separates 404, contradicted claim and blocked-verifier uncertainty from presence; no market-wide claim |
| R06 | Identifies a dynamic-SSR sitemap coverage issue to verify for the actual version/config; does not infer deindexation or orphanhood; suggests served-output and engine checks separately |
| R07 | Does not attribute the sanitized/unverified request to a genuine provider; avoids blanket WAF disablement and citation claims; proposes identity/rule-specific diagnosis |
| R08 | Rejects the sales forecast and universal uplift; preserves historical model/benchmark/domain/metric limits, unknown methods and publishing boundary; proposes a bounded hypothesis-first comparison |
| R09 | Classifies weights as expert opinion, not Google algorithm values; avoids fabricated causal priorities without local business evidence |
| R10 | Keeps primary Baidu verification incomplete; does not promote a secondary schema claim into policy; continues only supported generic observations |
| R11 | Defines 12/60 as query-specific citation-event share, not 20% of traffic; preserves preview classification and missing geography/timezone; distinguishes observed change from causal visits/leads |
| R12 | Keeps surface/provider/context distinct and acknowledges shared infrastructure; does not infer improvement without a baseline or three independent causal confirmations; no new automation |
| R13 | Distinguishes an individual draft and bounded adoption from a universal standard; preserves explicit training exclusions and checks precedence before any proposal |
| R14 | Distinguishes initial chunk, complete response, rendered metadata and collector limits; does not prescribe global streaming disablement without consumer evidence |
| R15 | Allows the requested bounded same-session repeat plan without an extra policy approval; distinguishes it from recurring monitoring; reports 1/2 valid answers and one failure, with citation support unknown and further captures not yet performed |
| R16 | Honors no-artifact instructions without writing collector results or refusing the bounded audit; identifies captured noindex while keeping live status and index state unknown |

These cases do not establish live engine behavior, real account access, production traffic impact, or guaranteed consistency on every future run. Dated result files record the evaluated package hash and any scope limits.
