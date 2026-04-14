# codex-seo-skill

SEO skill for Codex that improves website search positioning from a website URL and optional social profile URLs.

## Skill

- Name: `seo-positioning-optimizer`
- Path: `seo-positioning-optimizer/SKILL.md`

## What It Does

- Runs a practical SEO workflow and produces a prioritized implementation plan.
- Supports two modes:
  - `audit`: fast SEO audit with quick wins.
  - `deep`: detailed SEO analysis (technical, content, internal links, competitors, authority/trust).
- Asks essential clarifying questions when required context is missing.

## Typical Inputs

- Primary website URL (required)
- Social profile URLs (optional)
- Target geography/language (optional)
- Business goals and key pages (optional)
- Competitors (optional, recommended)

## Output Structure

1. Mode used and why
2. Executive summary
3. Assumptions and missing data
4. Priority action table
5. Page-level recommendations
6. Competitor insights (`deep` mode)
7. Social alignment recommendations
8. 30/60/90-day KPI plan

## Repository Structure

- `seo-positioning-optimizer/SKILL.md`
- `seo-positioning-optimizer/agents/openai.yaml`
- `seo-positioning-optimizer/references/seo-audit-framework.md`
