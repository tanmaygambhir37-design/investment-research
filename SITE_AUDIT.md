# Site Audit — investment-research (July 2026)

> **Superseded in part.** A second, deeper pass ran on 31 July 2026 across all eight pages, covering
> responsive behaviour, accessibility, asset and link integrity, cross-page arithmetic, and a check
> for AI-generated writing. Findings and fixes: [`AUDIT_2026-07-31.md`](AUDIT_2026-07-31.md).
> Twelve defects were fixed there, including one P0 the first pass missed: the Dust memo rendered
> 816px wide inside a phone viewport. The open items from that pass are in
> [`IMPLEMENTATION_PLAN.md`](IMPLEMENTATION_PLAN.md).


Scope: all five pages (home, Dust memo, Technogym, Recordati, Red-Team), audited against the external AI review. Verdict up front: **the review's structural criticisms were mostly already addressed** — the homepage already has hero positioning, OG/meta tags, metric grids, tooltips, and conversational hooks; the summary pages already have 30-second reads, tables, red-team revision notes, and download CTAs. The real gaps were narrower than the review claimed.

## Confirmed issues (fixed in this pass)

| # | Severity | Page | Issue | Fix |
|---|----------|------|-------|-----|
| 1 | P0 | dust/ | "The 30-Second Read" body text was `#E0E5F0` (near-white) on the light `#E7EAEE` page — invisible | Recolored to `#334155` |
| 2 | P0 | dust/ | Only page with no meta description, OG tags, or twitter card | Added, matching the other pages |
| 3 | P1 | all | No favicon anywhere | Inline SVG "TG" data-URI favicon on all 5 pages |
| 4 | P1 | technogym/ | Text-only DCF page; no valuation visual | Added football-field SVG (bear–bull, WACC band, terminal-value methods, spot line) |
| 5 | P1 | recordati/ | Text-only LBO page; no returns visual | Added IRR-by-scenario SVG (bear / floor / sponsor-consistent / full-thesis vs 20% hurdle) |
| 6 | P1 | home | Process not shown | Added "How Each Piece Gets Made" strip: Idea → Research → Hypothesis → Model → Memo → Red-Team → Decision, with hover tooltips |
| 7 | P2 | summaries | Sections slightly dense | h2 top margin 34→46px (red-team 38→48px) |

## Review points deliberately NOT actioned (already covered or not worth it)

- **Hero rewrite** — the current hero already states CA / PwC / Bocconi × ESSEC positioning and a one-line mission. The review's suggested hero is generic buzzword stacking ("DCF • LBO • Business Quality"); the current prose version is stronger.
- **"Replace 40% of paragraphs with charts"** — the memos are the product; gutting them for visuals would dilute the thing recruiters actually praise. One decision-grade chart per model page is the right dose.
- **Search/filter, tags, citation system, keyboard shortcuts, PDF reader mode** — over-engineering for a 5-page site. Revisit if the site reaches ~10+ pieces.
- **Light/dark theme toggle** — the dark identity is deliberate and consistent; a toggle doubles CSS surface for zero recruiter value.
- **Sitemap/robots/RSS/schema.org** — GitHub Pages + 5 pages; negligible SEO effect. Add when content volume justifies it.
- **"Current Research / In Progress" progress bars** — becomes stale-looking the moment it isn't updated; a liability, not a feature.

## Recruiter journey (90 seconds)

Home loads → positioning is clear in one screen → the process strip answers "how do they work" → coverage cards give recommendation + numbers without a click → each model page now opens with recommendation + chart → red-team page is the differentiator and is linked from every page. No dead ends found; every page links back to home and across to the red-team.

## Remaining P2 backlog (see IMPLEMENTATION_PLAN.md)

Screenshots of the Excel models next to the download buttons; a Sources & Uses table on Recordati; six-month follow-up notes per piece (the "was I right?" scorecard).
