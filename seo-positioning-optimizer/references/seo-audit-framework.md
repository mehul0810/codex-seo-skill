# SEO Audit Framework

## Priority Scoring

Score each issue from 1-5 for:
- Impact
- Effort
- Confidence

Compute:
- Base priority = Impact x (6 - Effort)
- Adjust +2 when Confidence >= 4
- Adjust -2 when blocked by external dependency
- Adjust +1 when issue affects top-converting pages
- Clamp the result to 1-28. Record dependencies as named blockers rather than an unused numeric score. Treat scores as planning estimates, not measured SEO effects.
- Override arithmetic for confirmed sitewide availability/indexing failures. Sequence prerequisite fixes before dependent tasks. Low-confidence hypotheses should become validation tasks first.

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

## Evidence And Technical Checks

- Fetch declared sitemap URLs and check final status, XML content, and representative child sitemaps. A missing sitemap can impair discovery but does not prove pages are unindexed.
- Separate crawl permission, index eligibility, canonical selection, and snippet eligibility. robots.txt blocking is not a reliable removal method and can prevent a crawler from seeing noindex. Inspect both HTML robots and X-Robots-Tag headers.
- Compare canonical targets with redirects and sitemap URLs. Use Search Console URL Inspection when authorized to verify Google's selected canonical and index status.
- Parse complete HTML for headings and metadata; use rendered DOM inspection when necessary. JavaScript alone is not an SEO defect. Do not diagnose missing content from a line-based regex or truncated response.
- Assess headings for clear structure; missing H1s are not automatically high-impact ranking blockers. Meta descriptions influence presentation but may be rewritten. Avoid fixed character-count or word-count pass/fail rules.
- Measure Core Web Vitals using field data where available: good thresholds at the 75th percentile are LCP <= 2.5 seconds, INP <= 200 ms, CLS <= 0.1. Record device, period, URL versus origin scope, and distinguish laboratory diagnostics from field results. Missing field data means unknown, not failure.
- Validate schema semantics separately from Google rich-result eligibility. Use the current feature gallery and Rich Results Test for supported features; valid schema alone guarantees neither rankings nor rich results. FAQ rich results ended in Google Search on May 7, 2026; do not recommend FAQ markup for that benefit.
- Check Organization sameAs against confirmed company profiles; do not attach company identities to a fictional Person author. Social engagement counts and share images are not direct ranking guarantees. If profiles block access, request public text or a user-provided export and label the review incomplete.
- For commerce, local, multilingual, or migrations, selectively inspect product/feed consistency, Business Profile details, hreflang reciprocity, or redirect maps. Avoid applying niche checklists universally.

## Measurement Integrity

Use comparable periods and segment by query intent, brand/non-brand, page, country, and device when data permits. Account for seasonality, migrations, tracking changes, and incomplete recent data before attributing a traffic change. Treat average position as contextual. Define denominators for ratios and distinguish technical acceptance checks from business outcomes. Do not promise improvements within 30/60/90 days.

Sources checked 2026-09-06:
- https://developers.google.com/search/updates
- https://developers.google.com/search/docs/crawling-indexing/robots/intro
- https://web.dev/articles/vitals

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

6. AI Discovery and Citation Readiness
- Search-crawler access, entity clarity, answer coverage, source attribution, evidence quality, freshness, and measurable citation/referral visibility.

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

### AI-search depth
- Use `ai-search-optimization.md` to inspect crawler controls, citation readiness, related-question coverage, AI-answer competitors, and measurement.
- Classify every AI-specific recommendation as a platform requirement, established practice, research-backed hypothesis, or experiment.

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
- Qualified conversions from AI referrals

Secondary KPI options:
- Indexed page quality ratio
- Internal link count to priority pages
- Branded query growth
- Returning visitor rate from organic
- Conversion rate from organic landing pages
- Observed citation rate across a stable query sample

## Clarifying Questions Template

Ask only what is required to make decisions:
1. Which pages drive revenue or leads today?
2. Which country/language is the primary SEO target?
3. What CMS/platform is used?
4. Which competitors currently outrank you for target terms?
5. Were there recent redesigns, migrations, or URL-structure changes?
6. Do you want a fast audit or deep SEO analysis?

If answers are unavailable, proceed with assumptions and call them out explicitly.
