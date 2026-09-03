# Implementation Plan — remaining work

P0 items from SITE_AUDIT.md are done. This is the backlog, in priority order. Each item is independent; do them one commit at a time.

## 1. Model screenshots next to download buttons (P1, ~1h)
- **Problem:** nobody downloads an .xlsx cold; they want one glance at the build quality first.
- **Do:** open each model, screenshot the DCF output tab and the LBO returns tab, export as compressed PNG (~150 KB), place in `technogym/` and `recordati/`, add an `<img>` (with `loading="lazy"`, max-width 100%, border + radius matching the chart cards) directly above the `.btns` block.
- **Accept:** page still loads fast; screenshot legible at 780px width.

## 2. Six-month scorecard blocks (P1, both triggers have now landed)
- **Problem:** the strongest long-term differentiator is "was I right?" — nobody does it.
- **Do:** Technogym H1-26 results (30 Jul 2026) and the Recordati CONSOB offer document (31 Aug 2026) are both out. Add a dated "Scorecard" section to each page: what the model predicted, what happened, what moved. Rebuild Recordati's Sources & Uses against the disclosed offer-document financing structure before writing the scorecard — verify figures against the primary CONSOB document, not a secondhand summary.
- **Accept:** written even (especially) where the call was wrong. Numbers cited to the primary source.

## 4. New research pieces (ongoing)
Per the strategic advice: one piece a quarter, varied formats (company research, sector map, framework). Add a simple "Research" index grouping by type only once there are ≥6 pieces — no tags/search before then.

## Explicitly rejected (do not build)
Search, tag filters, theme toggle, RSS, schema.org, keyboard shortcuts, reading-progress bars, "in progress" trackers. Reasons in SITE_AUDIT.md — all are maintenance liabilities at current site size.
