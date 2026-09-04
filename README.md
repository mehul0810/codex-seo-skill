# codex-seo-skill

SEO skill for Codex that improves traditional search positioning and AI-search citation visibility from a website URL and optional social profile URLs.

## Skill

- Name: `seo-positioning-optimizer`
- Path: `seo-positioning-optimizer/SKILL.md`

## How To Use In Codex

1. Open Codex in a workspace where this skill is available.
2. Invoke the skill in your prompt:
   - `Use $seo-positioning-optimizer to analyze https://yourdomain.com`
3. Choose a mode when asked:
   - `audit` for quick wins
   - `deep` for detailed SEO and AI-search analysis
4. Provide required inputs:
   - Website URL (required)
   - Social profile URLs, target location/language, top pages, and competitors (optional but recommended)
5. Answer clarifying questions from Codex so recommendations are more accurate.
6. Review the prioritized roadmap and execute the 0-2 week actions first.

## Example Prompts

- `Use $seo-positioning-optimizer to run an audit on https://example.com and include LinkedIn + Instagram profile alignment.`
- `Use $seo-positioning-optimizer in deep mode for https://example.com targeting US-English. Competitors: competitor1.com, competitor2.com.`

## What It Does

- Runs a practical SEO workflow and produces a prioritized implementation plan.
- Audits AI Overviews/AI Mode, ChatGPT search, and Bing/Copilot readiness without treating speculative tactics as ranking facts.
- Supports two modes:
  - `audit`: fast SEO audit with quick wins.
  - `deep`: detailed SEO analysis (technical, content, internal links, competitors, authority/trust, crawler controls, entities, and citation readiness).
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
8. AI-search crawler, citation, entity, and measurement findings
9. 30/60/90-day KPI plan

## Repository Structure

- `seo-positioning-optimizer/SKILL.md`
- `seo-positioning-optimizer/agents/openai.yaml`
- `seo-positioning-optimizer/references/seo-audit-framework.md`
- `seo-positioning-optimizer/references/ai-search-optimization.md`
