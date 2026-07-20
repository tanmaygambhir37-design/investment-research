# Implementation Plan — remaining work

P0 items from SITE_AUDIT.md are done. This is the backlog, in priority order. Each item is independent; do them one commit at a time.

## 1. Model screenshots next to download buttons (P1, ~1h)
- **Problem:** nobody downloads an .xlsx cold; they want one glance at the build quality first.
- **Do:** open each model, screenshot the DCF output tab and the LBO returns tab, export as compressed PNG (~150 KB), place in `technogym/` and `recordati/`, add an `<img>` (with `loading="lazy"`, max-width 100%, border + radius matching the chart cards) directly above the `.btns` block.
- **Accept:** page still loads fast; screenshot legible at 780px width.

## 2. Sources & Uses table on Recordati (P1, ~30min)
- **Problem:** an LBO page without Sources & Uses is missing the one table every PE reader expects.
- **Do:** add a two-column table (Sources: TLB €/$ tranches, SSN, sponsor equity; Uses: equity purchase, refinanced net debt, fees) under "Model Economics", numbers from the model.
- **Accept:** totals tie to €12.49bn EV.

## 3. Six-month scorecard blocks (P2, revisit January 2027)
- **Problem:** the strongest long-term differentiator is "was I right?" — nobody does it.
- **Do:** when H1-26 Technogym results (30 July 2026) and the Recordati CONSOB offer document land, add a dated "Scorecard" section to each page: what the model predicted, what happened, what moved.
- **Accept:** written even (especially) where the call was wrong.

## 4. New research pieces (ongoing)
Per the strategic advice: one piece a quarter, varied formats (company research, sector map, framework). Add a simple "Research" index grouping by type only once there are ≥6 pieces — no tags/search before then.

## Explicitly rejected (do not build)
Search, tag filters, theme toggle, RSS, schema.org, keyboard shortcuts, reading-progress bars, "in progress" trackers. Reasons in SITE_AUDIT.md — all are maintenance liabilities at current site size.
