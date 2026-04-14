---
name: seo-positioning-optimizer
description: "Improve search visibility for a website using two modes: fast SEO audit and deep SEO analysis. Use when the user asks to improve rankings, diagnose traffic drops, perform technical/on-page/content/internal-link analysis, evaluate competitors, align social profile signals, or request a prioritized SEO roadmap from a website URL and optional social URLs."
---

# SEO Positioning Optimizer

Run a practical SEO workflow from a website URL and optional social profile URLs. Support two modes so the user can choose speed or depth.

## Mode Selection

Select a mode at the start of every run:
- `audit`: Fast assessment with prioritized actions and quick wins.
- `deep`: Detailed analysis with technical, content, internal link, competitor, and authority diagnostics.

If the user does not pick a mode, ask once:
- "Do you want a fast audit or deep SEO analysis?"

Default to `audit` only when the user does not answer and time-to-output is more important than completeness.

## Inputs

Collect these inputs first:
- Required: primary website URL.
- Optional: social profile URLs (LinkedIn, X, Instagram, YouTube, Facebook, Pinterest).
- Optional: target country/city, target language, business type, conversion goal.
- Optional: 2-5 direct competitors and traffic/ranking decline window.
- Optional for deep mode: key service/product pages, existing keyword targets, CMS/platform, recent redesign/migration date.

If critical context is missing, ask concise questions before deep analysis:
1. What is the primary conversion action (purchase, lead form, booking, call, newsletter)?
2. Which geography and language should ranking improvements target?
3. Which products/services or pages matter most right now?
4. Who are 2-5 competitors in search results for your core terms?
5. Which CMS/platform do you use, and was there a recent migration or redesign?

If the user cannot provide all details, proceed with explicit assumptions and label them clearly.

## Shared Workflow

1. Confirm scope.
- Confirm website-only vs website + social signal alignment.
- Confirm priority page groups (homepage, service/category/product, blog/resource hub).

2. Build issue inventory.
- Group findings into: technical, on-page/content, architecture/internal links, authority/off-page, entity/social alignment.
- For each issue include: evidence, affected pages, expected impact, effort, dependency, and suggested owner.

3. Prioritize actions.
- Use scoring from `references/seo-audit-framework.md`.
- Prioritize quick wins and foundational blockers first.

4. Produce an implementation roadmap.
- Split into now (0-2 weeks), next (2-6 weeks), later (6-12 weeks).
- Define acceptance criteria and KPI mapping for each high-priority action.

## Audit Mode (`audit`)

Use when the user needs a fast, actionable plan.

Required checks:
- Indexability basics (robots, sitemap presence, canonical consistency, obvious crawl blockers).
- Core template quality (title/meta, heading hierarchy, thin/duplicate content signals).
- Internal linking basics (orphan risk, weak contextual anchors, deep click depth to priority pages).
- Entity consistency across website and social URLs (brand name, contact details, profile links).

Output focus:
- Quick wins with high impact and low effort.
- Maximum 10-15 prioritized recommendations.

## Deep Analysis Mode (`deep`)

Use when the user requests detailed SEO analysis, large ranking gains, or root-cause diagnosis.

Run all audit checks plus:

1. Technical depth
- Index coverage patterns, canonical clusters, redirect chain/cycle risk, parameter/indexation risk.
- Template-level rendering/indexation hypotheses for JS-heavy pages.
- Core Web Vitals risk by template and likely causes (LCP/CLS/INP hypotheses).

2. Content and intent depth
- Query intent mapping for key page groups.
- Content gap analysis for missing subtopics and weak topical depth.
- Cannibalization risks across pages targeting similar intent.
- Snippet competitiveness (title/meta angle, clarity, CTR hooks).

3. Architecture and internal link depth
- Topic cluster quality and pillar-support relationships.
- Anchor text diversity and contextual link relevance.
- Link equity flow toward conversion pages.

4. Competitor depth
- Compare content breadth, likely query coverage, and SERP positioning patterns.
- Identify areas where competitors are winning (topic completeness, authority, freshness, UX).
- Recommend counter-strategy by page cluster.

5. Authority and trust depth
- Evaluate off-page trust signals and E-E-A-T gaps.
- Recommend trust-building assets (author pages, editorial policy, case studies, citations, trust pages).

Output focus:
- Root-cause hypotheses, validation steps, and sequencing dependencies.
- 15-30 recommendations grouped by theme with explicit implementation order.

## Output Format

Return results in this order:
1. Mode used (`audit` or `deep`) and why.
2. Executive summary (current state + biggest ranking constraints).
3. Assumptions and missing data.
4. Priority action table: issue, impact, effort, dependency, owner, timeline.
5. Page-level recommendations for top priority URLs.
6. Competitor insight section (required for `deep`, optional for `audit`).
7. Social-URL alignment recommendations (if provided).
8. KPI tracking plan for 30/60/90 days.

Use direct language, avoid generic advice, and tie each recommendation to expected ranking, CTR, or conversion impact.

## Guardrails

- Do not promise specific ranking positions.
- Do not invent analytics or crawl data.
- Mark uncertain conclusions as hypotheses and provide validation steps.
- Prefer smallest high-leverage changes first, then scale.

## References

- Use `references/seo-audit-framework.md` for scoring, effort tiers, deep-analysis checklist, and KPI mapping.
