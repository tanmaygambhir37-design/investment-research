# Implementation Plan — remaining work

Backlog in priority order. Each item is independent; do them one commit at a time.

P0 items from `SITE_AUDIT.md` are done. The twelve UI, accessibility and asset defects found in the
31 July pass are also done (see `AUDIT_2026-07-31.md` §1). What follows is what that pass left open,
plus the research pipeline.

## 1. Reconcile the sector map's numbers (P0, ~1h)
- **Problem:** `$725B` hyperscaler capex carries the whole page (used 10 times, called "the single
  most important number in semis"), but the Stage 8 component breakdown sums to `$600–640B`. Two
  numbers for the same quantity, unreconciled, on the same page. Two more: the "~$240B run-rate"
  Nvidia figure matches none of the three revenue figures elsewhere on the page, and Carl Zeiss
  Meditec is described as a proxy for the EUV optics business, which it is not.
- **Do:** go back to the source for each, fix or relabel. Full detail in `AUDIT_2026-07-31.md` §3.
- **Accept:** no two figures on the page describe the same quantity differently without a stated
  reconciliation.

## 2. Citations on the five uncited pages (P0, ~3h)
- **Problem:** `README.md` promises "Every number is cited to a public source. No exceptions." Only
  the Dust memo delivers it (19 links). Technogym, Recordati, all three red-team pages and the sector
  map carry zero. The claim is checkable and currently overstated.
- **Do:** table-level or inline citations in the Dust memo's pattern, primary sources first.
- **Accept:** every material figure on every research page traces to a link.

## 3. Technogym scorecard — do this now, not in January (P0, ~2h)
- **Problem:** the page conditions its whole rating on an event that has already happened. "A BUY
  rating requires the upcoming H1-2026 earnings report (due 30 July) to confirm that the Americas
  growth slowdown has stabilized." H1-2026 printed 30 July 2026. Until it is written up, the site's
  most prominent rating is visibly stale against a catalyst it named itself.
- **Do:** a dated Scorecard section: what the model predicted, what printed, what moved, and whether
  the rating changes. Then the same for Recordati when the CONSOB offer document lands.
- **Accept:** written even (especially) where the call was wrong. This is the strongest differentiator
  on the site and nobody else does it.

## 4. Red-team the Dust memo (P1, ~2h)
- **Problem:** `README.md` says every piece carries a red-team page. Dust, the flagship and the first
  thing the homepage sends visitors to, has none and links to none. Neither does the sector map.
- **Do:** a `red-team/dust/` page in the existing "challenges that land / don't land / revised
  judgment" format. The obvious attacks are already inside the memo: ARR is company-reported and
  undated within "early 2026"; the $350–500M post is an internal estimate that drives the entire
  sizing recommendation; MuleSoft / Segment / Looker is three hand-picked outcomes presented as a
  base rate.
- **Accept:** linked from the Dust memo, the red-team index and the homepage card.

## 5. Sector map: house style, or unlist it (P1, ~4h)
- **Problem:** three separate issues on one page. It shares nothing with the house design system but
  the favicon (light theme, Georgia serif, blue accent, its own nav). Its prose is the only writing
  on the site that reads as AI-generated, against the site's own rule in `MEMO_PLAYBOOK.md` §4 (108
  em dashes; every one of 20 sections closes on an aphorism). And it is badged "WORKING DRAFT",
  which `SITE_AUDIT.md` already established is a liability on a portfolio.
- **Do:** either rebuild it in the house system with a voice pass and citations, or unlist it from
  the homepage until that is done. Evidence in `AUDIT_2026-07-31.md` §2 and §4.
- **Accept:** no draft badge, no separate design system, em dash density in line with the other pages.

## 6. `404.html` (P2, ~15min)
- **Problem:** GitHub Pages serves its own error page, which breaks the identity and dead-ends the
  visitor.
- **Do:** twelve lines in the house style, linking home and to the coverage list.

## 7. Fifth research piece (P2)
There is a fork here, and it depends on the recruiting target:
- **Venture / growth track:** a second VC memo. Both current valuations are Milan-listed mid-caps,
  which reads narrow, and the memo is the format the work actually gets tested on.
- **IB / PE track:** a merger model with accretion/dilution. The kit has a DCF and an LBO but no M&A
  model, `MODEL_PLAYBOOK.md` is built to be adapted, and it is the third model every banking
  interview expects.

Default if unstated: the merger model, because it closes a visible hole in the modelling kit rather
than repeating a format the site already demonstrates.

## Explicitly rejected (do not build)
Search, tag filters, theme toggle, RSS, schema.org, keyboard shortcuts, reading-progress bars,
"in progress" trackers. Reasons in `SITE_AUDIT.md` — all are maintenance liabilities at current site
size. Still the right call at four pieces. Revisit at roughly 10+.
