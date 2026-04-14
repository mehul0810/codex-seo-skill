---
name: seo-positioning-optimizer
description: Improve search visibility for a website using audits and prioritized SEO actions. Use when the user asks to improve rankings, diagnose traffic drops, audit SEO, compare with competitors, optimize metadata/content/internal links, or align website and social profile signals (website URL, social URLs, or both).
---

# SEO Positioning Optimizer

Execute a practical SEO workflow from a website URL and optional social profile URLs. Produce a prioritized plan that balances impact, effort, and implementation speed.

## Inputs

Collect these inputs first:
- Required: primary website URL.
- Optional: social profile URLs (LinkedIn, X, Instagram, YouTube, Facebook, Pinterest), target country/city, target language, business type, main conversion goal.
- Optional: 2-4 direct competitors and any recent traffic/ranking decline window.

If critical context is missing, ask concise questions before deep analysis:
1. What is the primary conversion action (purchase, lead form, booking, call, newsletter)?
2. Which geography and language should ranking improvements target?
3. Which products/services or pages matter most right now?
4. Who are 2-4 competitors in search results for your core terms?

If the user cannot provide all details, proceed with explicit assumptions and label them as assumptions.

## Workflow

1. Confirm scope.
- Confirm whether to audit website only or website + social profile alignment.
- Confirm priority pages (homepage, core service pages, product/category pages, blog hub).

2. Perform baseline assessment.
- Check indexability signals (robots, sitemap availability, canonical consistency, obvious crawl blockers).
- Check information architecture and internal linking depth for priority pages.
- Check title/meta quality, heading structure, duplicate/thin content patterns, and intent mismatch.
- Check entity consistency across site and social profiles: brand name, NAP/contact data, about messaging, and primary link consistency.

3. Build issue inventory.
- Group findings into: technical SEO, on-page/content, internal links/architecture, authority/off-page, local/entity/social alignment.
- For each issue include: evidence, affected pages, expected impact, effort, dependency, and owner suggestion (content/dev/marketing).

4. Prioritize with scoring.
- Use the scoring rubric in `references/seo-audit-framework.md`.
- Prioritize quick wins (high impact, low effort, low dependency) first.
- Highlight foundational blockers that must be fixed before content scaling.

5. Produce implementation plan.
- Split into now (0-2 weeks), next (2-6 weeks), later (6-12 weeks).
- Include concrete tasks, acceptance criteria, and suggested measurement KPI.
- Include social profile actions only when they influence SEO entity trust and click-through behavior.

## Output Format

Return results in this order:
1. Executive summary (current state + biggest ranking constraints).
2. Assumptions and missing data.
3. Priority action table: issue, impact, effort, owner, timeline.
4. Page-level recommendations for top priority URLs.
5. Social-URL alignment recommendations (if provided).
6. KPI tracking plan for next 30/60/90 days.

Use direct language, avoid generic advice, and tie each recommendation to expected ranking or CTR outcomes.

## Guardrails

- Do not promise specific ranking positions.
- Do not invent analytics values.
- Mark uncertain conclusions as hypothesis and state required validation.
- Prefer the smallest set of changes that can improve measurable outcomes quickly.

## References

- For scoring, timelines, and KPI mapping, use `references/seo-audit-framework.md`.
