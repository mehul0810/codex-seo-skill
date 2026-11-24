# R05

**Mode: audit**, limited to the supplied answer and URL-check snapshots. Acme appeared as a cited source in **2 of 3 valid answers (66.7%)** to this one prompt. Two of five attempts failed or were unavailable and are excluded from that denominator. A3 mentions Acme without a citation. This is a small, synthetic sample, not a market-wide visibility rate.

The five attempts were captured on 24 November 2026 at 00:00 UTC for “Which tools export invoices?” in Example Assistant with search enabled, en-GB, UK, signed out. The model and upstream provider were not disclosed. No example domain was browsed.

| Answer | Presence and accuracy |
| --- | --- |
| A1 | Acme cited once. The cited `/old-invoices/` returned 404 in the supplied check, so it counts for presence, but the destination is broken and cannot substantiate the claim from this evidence. |
| A2 | Acme cited twice, but counted once for answer presence. The claim of unlimited free exports contradicts the supplied `/plans/` text, updated 20 November: free users can view only; Pro can export up to 100 invoices per month. The `/help/exports/` check returned a tool-blocked 403, so its content and support are unknown, not necessarily false or inaccessible to the assistant. |
| A3 | Mentions Acme but provides no citation. Its general suggestion is not evidence of a verified export entitlement. |

**Citation quality:** Of three cited URL instances across two citation-bearing answers, one was broken, one resolved but contradicted the associated claim, and one was unverified because the audit tool was blocked. None was verified as supporting the associated claim. These counts describe the supplied checks, not all citations or actual customer access.

**Next action, product owner:** First confirm the current export entitlements against the authoritative product configuration and identify the appropriate current replacement for the old invoice URL. If the old URL was permanently moved, have the web owner evaluate a relevant redirect or restore useful content; do not redirect blindly. Review the plans and help copy for consistent, explicit limits. Separately inspect the help page through an authorized normal route; do not bypass the 403. Acceptance: a fresh check of the old URL shows the intended relevant destination, and the current plans/help text matches confirmed entitlements. Retain the snapshots and recheck the same prompt only as a bounded follow-up; a corrected page does not guarantee an assistant will cite it or describe it accurately. No site changes are authorized by this assessment.

# R12

**Mode: audit**, based on one supplied snapshot per surface. **No: these are three observed surface appearances, not three independent confirmations of an improvement.** There is no earlier comparable snapshot, so even one improvement has not been established.

| Surface | Observed position | Provider evidence |
| --- | --- | --- |
| Bing | 5 | Bing surface |
| DuckDuckGo | 4 | Provider for this particular result not disclosed |
| Ecosia | 5 | Supplied footer identifies Bing |

The synthetic captures are dated 24 November 2026 at 00:00 UTC for “invoice export tools,” UK desktop, signed out. Ecosia and Bing share a disclosed provider in this sample, so their results are not independent corroboration. DuckDuckGo says its traditional links primarily come from Bing and other sources, but that does not identify the provider for this particular result. Ecosia says its provider may vary by context and search; preserve the actual disclosed provider for each capture rather than assigning one globally. [DuckDuckGo sources](https://duckduckgo.com/duckduckgo-help-pages/results/sources); [Ecosia search providers](https://support.ecosia.org/article/579-search-results-providers).

**One-off recheck:** At a later agreed point, manually run the exact query once on each surface under the same UK, desktop and signed-out conditions. Record timestamp, locale, settings, result URL, organic position and counting method, screenshot, and provider when disclosed; record unavailable results or changed context rather than forcing a comparison. Compare each surface to its own original snapshot and label provider overlap. This can show a difference between two snapshots, not establish a durable trend or its cause. For business impact, separately consult available search click and qualified-lead data over comparable periods; neither position nor a result appearance is a visit or a lead. No recurring monitoring or automation is proposed or started.

# R15

**Mode: audit**, limited to the supplied one-off answer sample. Acme is cited in **1 of 2 valid answers (50%)**: B1 cites its homepage, and B2 neither mentions nor cites it. B3 timed out and is excluded; report it as **1 failed capture out of 3 attempts**. The homepage destination, claim support and current accuracy have not been checked, so citation presence is not verified citation quality. This is not a population-wide visibility estimate.

The supplied snapshots are from 24 November 2026 at 00:00 UTC for “Which invoice tools serve UK small businesses?” in Example Assistant, search enabled, en-GB, UK, signed out. Model and upstream provider are undisclosed.

**Bounded evidence-gathering plan:** Use the existing authorized free access to run exactly two further attempts in the same session, with the identical prompt and settings. This is public read-only evidence collection within the one-off audit, not a purchase, new account, site change or recurring monitoring. No live assistant tool is available in this fixture, so these two captures **have not been executed** and no results can be claimed. If the session or settings cannot be matched, record that limitation rather than calling the attempts comparable.

For each additional attempt, record its timestamp, exact prompt, surface, search setting, locale, sign-in/session context, model and provider if displayed, full answer snapshot, Acme mention, exact cited URLs, and success or failure. Preserve timeouts and unavailable answers separately. If a cited public destination can be checked within the same access boundary, record status, final URL, publisher, relevant passage and whether it supports the associated claim; otherwise mark accuracy unverified.

Afterward, calculate citation-bearing answer rate as **(1 + number of new valid answers citing Acme) / (2 + number of new valid answers)**. Count each valid answer once even if it has several Acme links; exclude failed captures and state their count out of five total attempts. If both new attempts fail, the rate remains 1/2, with three failed attempts out of five. Record mentions without citations and citation accuracy separately. The result remains a small, variable sample of this prompt and session, not proof of ranking, referral traffic or leads.
