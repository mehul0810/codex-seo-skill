# SEO Audit Framework

## Priority Scoring

Score each issue from 1-5 for:
- Impact
- Effort
- Dependency risk
- Confidence

Compute:
- Base priority = Impact x (6 - Effort)
- Adjust +2 when Confidence >= 4
- Adjust -2 when blocked by external dependency
- Adjust +1 when issue affects top-converting pages

Interpretation:
- 20-28: Immediate quick win or critical blocker
- 14-19: Prioritize in next sprint
- 8-13: Plan after core fixes
- 1-7: Backlog

## Effort Tiers

Map effort consistently:
- 1: < half day
- 2: 0.5-2 days
- 3: 3-5 days
- 4: 1-2 weeks
- 5: >2 weeks or multi-team dependency

## Issue Buckets

1. Technical
- Crawl/index blockers, canonical conflicts, redirect waste, broken internal links, weak CWV by template.

2. On-page and Content
- Intent mismatch, weak titles/meta descriptions, thin pages, weak heading structure, schema gaps.

3. Internal Linking and Architecture
- Orphan pages, weak clusters, poor anchor relevance, low link flow to money pages.

4. Authority and Trust
- Weak backlinks vs competitors, trust-page gaps, weak E-E-A-T signals.

5. Entity and Social Alignment
- Inconsistent brand/contact details across website and social profiles.
- Weak connection between social bios and canonical website pages.

## Deep Analysis Checklist

Use this checklist only in `deep` mode.

### Technical depth
- Check likely index coverage risks by template or page type.
- Check canonicalization patterns and conflict clusters.
- Check redirect chain/cycle risks and URL normalization consistency.
- Check JS-rendering/indexation risk for key templates.
- Check LCP/CLS/INP risk signals and likely causes.

### Content depth
- Map pages to user intent classes (transactional/commercial/informational/navigational).
- Identify topic gaps and missing supporting subtopics.
- Identify cannibalization risks between similar-intent pages.
- Evaluate snippet competitiveness for CTR.

### Architecture depth
- Evaluate pillar/cluster completeness and internal link pathways.
- Evaluate anchor text quality and distribution.
- Evaluate crawl depth and discoverability of conversion pages.

### Competitor depth
- Compare topic breadth and page-pattern coverage.
- Compare perceived freshness and trust cues.
- Identify competitor advantages and map counter-actions.

### Authority depth
- Identify trust and credibility assets to add or improve.
- Identify citation/reputation gaps relevant to the niche.

## KPI Mapping

Map each recommendation to:
- 1 primary KPI
- 1 secondary KPI
- 1 validation window (30, 60, or 90 days)

Primary KPI options:
- Non-brand organic clicks
- Impressions for target query clusters
- Average position of priority URLs
- CTR on ranking pages
- Qualified organic conversions

Secondary KPI options:
- Indexed page quality ratio
- Internal link count to priority pages
- Branded query growth
- Returning visitor rate from organic
- Conversion rate from organic landing pages

## Clarifying Questions Template

Ask only what is required to make decisions:
1. Which pages drive revenue or leads today?
2. Which country/language is the primary SEO target?
3. What CMS/platform is used?
4. Which competitors currently outrank you for target terms?
5. Were there recent redesigns, migrations, or URL-structure changes?
6. Do you want a fast audit or deep SEO analysis?

If answers are unavailable, proceed with assumptions and call them out explicitly.
