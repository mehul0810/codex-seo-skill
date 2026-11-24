# Conditional Delivery Diagnostics

Use only when the actual stack or an observed response discrepancy makes a check relevant. Establish CMS/framework/plugin versions, route type, deployment mode, and edge involvement first. Do not turn these examples into a universal checklist or a reason to rebuild a working JavaScript site.

Capture complete raw response and headers, final URL/status, rendered DOM when needed, served robots/sitemap output, timestamp, and request context. A configuration value or build artifact does not prove the served response. A generic collector is not a particular crawler; do not spoof bot identity or bypass challenges. Use authorized inspection or identity-verified logs where necessary.

Sources and scoped claims checked 2026-11-24:

| Relevant stack/symptom | Evidence and smallest useful check | Limit |
| --- | --- | --- |
| WordPress + Rank Math robots changes do not appear | [Rank Math robots settings](https://rankmath.com/kb/general-settings/): its editor writes a virtual file; an existing physical robots.txt can take precedence. Compare served output with authorized filesystem/plugin evidence and cache state | Do not infer a physical file from a screenshot alone, delete a file blindly, or disable unrelated security rules |
| Astro dynamic SSR routes absent from a generated sitemap | [Astro sitemap integration](https://docs.astro.build/en/guides/integrations-guide/sitemap/): dynamic SSR entries are not automatically generated. Compare known intended canonical routes, configured custom entries, and served child sitemaps | Missing sitemap coverage is not proof of missing indexation or orphan status; check internal discovery and authorized engine evidence separately |
| Next.js initial response appears to lack metadata | [generateMetadata](https://nextjs.org/docs/app/api-reference/functions/generate-metadata): metadata can stream later, and HTML-limited bot handling differs. Check complete response, rendered DOM, actual version/config, and relevant consumer evidence | Do not infer missing metadata from an initial chunk or the collector's first-title field. Do not disable streaming globally without a reproduced consumer problem and performance assessment |
| React duplicate document titles | [React title reference](https://react.dev/reference/react-dom/components/title): multiple title components can produce multiple document titles. Inspect all document-head titles and component ownership in the rendered output | SVG titles are not document titles; a source collector that returns one title cannot prove uniqueness |
| Edge and origin observations disagree | Compare authorized origin evidence with public edge status/body/cache headers at known times and relevant verified requests | A stale response or blocked request is a hypothesis until reproduced. Fix the narrow cache/policy owner; do not disable the WAF broadly or expose private content |

After an authorized change, verify the served route and affected templates again; inspect cache propagation separately when relevant. Report local/build, browser, engine-inspection, and deployed evidence as distinct. Successful rendering or sitemap generation alone does not establish indexing, citations, or conversions.
