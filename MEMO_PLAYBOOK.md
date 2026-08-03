# How to Make a Good Investment Memo — Playbook

This is the accumulated set of rules from building the Dust memo (`dust/`) and the site around it.
It exists so a new session doesn't relearn these the slow way — by making the mistake, getting
corrected, and fixing it after the fact. Read this before starting a new piece. When in doubt,
open `dust/index.html` and match its patterns; it is the canonical example everything below was
extracted from.

**Author's own words matter here.** The rules below are written the way Tanmay actually corrected
them, not softened into generic advice. If a new session paraphrases these back into something
blander, it has missed the point.

## 1. Structure

- **Recommendation goes on page 3, not page 20.** A partner reads the conclusion before the
  reasoning. Original draft buried it at the end; the fix moved "Invest — Small Follow-On" plus
  sizing, entry math, and next steps to right after the TOC.
- **Cut filler ruthlessly.** A radial "ecosystem" diagram restating numbers already on the
  previous page got deleted outright, not trimmed. If a page doesn't add a new fact or a new
  argument, it doesn't belong. Original Dust draft was 22 pages of which ~2 were pure filler —
  cut first, add real content second, net length stayed disciplined.
- **One-page structure per section:** headline claim → the numbers → the "why it matters" callout.
  Don't make the reader assemble the point themselves.
- **The site's five-stage skeleton per piece:** 30-Second Read → full memo/model → Sources & Uses
  (LBO) or football-field (DCF) → Red-Team page → Sources. Every new piece should ship all five,
  not just the memo.
- **Every piece links back to the homepage and sideways to its own red-team page.** No dead ends.

## 2. Data integrity — this is where most of the actual correction happened

- **Scores must match the source, or be labeled as your own addition.** Early scorecard showed
  Moat 4.5 when the source research scored it 5.0 (Financials 5.0 vs. source 6.0). This is the
  single most credibility-damaging category of mistake: a partner who checks one number and finds
  it wrong distrusts everything else in the document. If you invent a category the source doesn't
  have (e.g., a "Risk" score), label it explicitly as analyst-added.
- **One number per fact, used consistently everywhere.** Original draft used two different
  headcounts (~66 in one place, ~100–140 in another) and used them to compute a per-employee
  metric with one and display the other elsewhere. Pick the number, cite where it came from, and
  grep the whole document for every other place that fact appears before calling it done.
- **Never let two numbers on the same page contradict each other without addressing it.** "0%
  gross churn" sitting next to "240% NRR" in the same dashboard is not a caveat, it's a red flag —
  fix by sourcing precisely or removing the claim, not by hoping nobody notices.
- **Confidence tiers on every material figure:** High / Medium / Low / Not Disclosed. Undisclosed
  metrics (margin, runway, CAC/LTV) are shown as "Not Disclosed," not estimated into existence.
  Company-reported numbers are "directionally credible," never treated as audited fact.
- **Do the arithmetic a reader will do in their head.** 3,000+ customers against $20M ARR implies
  a mid-single-digit-thousand average ACV — call that out yourself (revenue concentration risk)
  before the reader has to point it out to you.
- **Reconcile contradictions between sections.** Porter's "switching is a project, not a crisis"
  (i.e., weak lock-in) can't sit unaddressed next to a recommendation claiming "real usage
  lock-in." Pick one position or explicitly explain how both are true.
- **If a metric like NRR looks implausibly strong, say so in the same sentence you report it**
  (240% read against Bessemer's 120% "best-in-class" ceiling reads as a small-cohort artifact, not
  durable retention). Don't just report the number and move on.

## 3. Sourcing

- **Every claim traces to a numbered citation.** No exceptions for things that "everyone knows."
- **Real quotes only, with attribution and date.** Founder quotes, customer quotes (G2, case
  studies, interviews) must be actual sourced text, never paraphrased and presented as a quote.
  When research turned up genuine Qonto/Sequoia/founder-interview material, it went in with exact
  attribution; nothing was invented to fill a gap.
- **Distinguish primary from vendor-published from independent.** A company's own case study is
  weaker evidence than an independent G2 review, which is weaker than an unaffiliated journalist.
  Say which kind each source is when it matters (Customer Voice page explicitly flags that public
  feedback "skews vendor-published" and is thin — 19 G2 reviews — as an honest caveat, not hidden).
- **Cite the exact source for market-sizing figures on the page itself**, not just in an appendix
  — a partner shouldn't have to flip pages to check a TAM number.

## 4. Language and voice — the most frequently corrected category

- **No filler version-labels or draft-signaling.** "Version 1.0 — Institutional Research" on a
  cover reads as unfinished work, not a finished product. Remove entirely.
- **No em dashes used as a crutch — they read as AI-generated.** Prefer periods, commas, or a
  colon. This was flagged explicitly and repeatedly.
- **Cut insider jargon that makes the reader stop and decode.** "MuleSoft-shaped base case" was
  rewritten to "our base case is a strategic infrastructure acquisition (as happened to MuleSoft,
  Segment, Looker)." If a sentence needs the reader to already know your internal shorthand,
  simplify it. The rule as given: "whenever a sentence makes the reader pause to decode it,
  simplify."
- **Don't sound like you're performing intelligence.** Externally-facing prose should read like
  plain, direct thinking, not like it's trying to prove how clever the analyst is.
- **Personal bio copy should sound like an actual person, not a positioning statement.** First
  draft of the homepage bio ("I write institutional-grade investment memos... every figure is
  tiered by confidence...") was rejected as "too AI." Rewritten to plain first-person: "I'm a
  Master in Management student exploring venture capital by doing the work." State credentials
  and process in ordinary sentences, not marketing language.
- **Consistent terminology throughout — pick one term per concept and stick to it.** "Follow-on"
  (the position), "secondary" (the mechanism), "Series C path" (the future entry) are three
  different things; don't let them blur into each other across pages.
- **Reduce paragraph length where density creeps in**, and leave more whitespace in numbers-heavy
  sections (Business Model, Financial Dashboard) — dense text pages get flagged first in review.

## 5. What a partner (or recruiter) actually wants, that first drafts tend to skip

- **Explicit sizing and entry math**, not "small follow-on." State the dollar range, the price
  ceiling it's conditioned on, and what percentage that buys at a reference valuation.
- **A concrete path to entry**, not just "if access opens." Name the actual mechanism (secondary
  vs. Series C relationship) and what happens in parallel.
- **A "Next Steps" section** — what specifically is being asked of the reader (founder meeting,
  CFO call, price discovery, a tracked metric ahead of the next decision point).
- **Explicit, separated "we get more bullish if / we get more bearish if" triggers** — not just a
  bull/base/bear scenario table. State the falsifiable thing that would change the recommendation
  in each direction, and make sure the bear triggers are as specific as the bull triggers.
- **Analyst-assigned probabilities on scenarios**, labeled as your own assignment, not the
  company's — and justify the weighting in one sentence.
- **A sensitivity view beyond bull/base/bear**: named shocks (a competitor ships a feature, a
  metric reverts, budgets slow) mapped to their actual mechanism and effect on the valuation range.
- **Qualitative evidence, not just metrics** — a Customer Voice page with real quotes and named
  pain points is what separates a "researched" memo from a "described" one. Include the pain
  points and adoption friction, not only the wins.
- **A one-page summary that stands alone.** Busy readers won't open the full document first. Build
  the 1-pager as its own artifact (own file, own layout, print-tested to exactly one page), not a
  truncated copy-paste of the full memo's intro.
- **A red-team pass is not optional polish — it's a distinct required stage.** The site's process
  is Idea → Research → Hypothesis → Model → Memo → Red-Team → Decision. The red-team step is
  explicitly adversarial: attack your own assumptions, and where a challenge lands, move the
  number. Both directions of Dust's follow-on work went through this and the estimates moved as a
  result — that's the point of the stage, not a failure of the first draft.

## 6. Process discipline for the site itself (applies to every new piece added)

- Match the existing five pages' visual system exactly (navy `#0F172A` / gold `#D4AF37` palette,
  Manrope headings, Inter body, JetBrains Mono for labels/numbers) — don't introduce a new style
  per piece.
- Every new piece needs: a 30-Second Read block, the full memo, a decision-grade chart (football
  field for a DCF, IRR-by-scenario for an LBO — not a decorative visual), a downloadable model
  file, a red-team page, and a homepage coverage card.
- Don't over-build the site chassis for its own sake. Search, tag filters, theme toggles, RSS,
  schema.org, and progress-bar trackers were all explicitly rejected as premature at five pieces —
  see `SITE_AUDIT.md` for the reasoning. Revisit only once there are roughly 10+ pieces.
- Before adding new pages, check `IMPLEMENTATION_PLAN.md` and `SITE_AUDIT.md` for what's already
  decided and already rejected, so the same debate doesn't happen twice.

## 7. Fastest way to onboard a new session

Tell it to:
1. Open `dust/index.html` and read it fully — it is the reference example for structure, tone,
   sourcing, and what a finished page looks like.
2. Read this file end to end before writing anything.
3. Check `SITE_AUDIT.md` and `IMPLEMENTATION_PLAN.md` for current site state and backlog.
4. Match the existing five-page visual and structural system for any new piece, and run every
   claim through the sourcing and data-integrity rules above before it ships.

## 8. Market Signals — a second content type, same visual system

`markets/` is a different kind of piece from the memos: a recurring, monthly, single-author
macro/rates publication (first edition: `markets/uk-rates-aug-2026/`), not a one-off company
analysis. It still uses the exact same dark navy `#0F172A` / gold `#D4AF37` / JetBrains Mono
system as everything else — the only genuinely new component is a **sticky sub-nav** (`.subnav`,
directly below `.topnav`) for in-page jump links, because this piece is long enough (~22 min read,
~6,700 words in the source report) to need one and nothing else on the site is. Two things worth
knowing before extending it:

- **The sub-nav goes `position:static` below 760px** (`@media(max-width:760px){.subnav{position:static}}`).
  The shared `.topnav` already wraps to two lines at mobile widths — that's pre-existing site
  behavior, not a bug — and a second sticky bar stacked under a two-line nav will get clipped.
  Don't re-enable sticky on mobile without also solving that.
- **IA decision:** `markets/` has its own landing page (`markets/index.html`), unlike Coverage or
  Industry Intelligence, which are just homepage anchors. The reason is real, not a stylistic
  choice: this section is designed from day one to accumulate ~12 editions a year, so it needs a
  real index of editions the way a single Dust memo or single sector map does not. If Industry
  Intelligence grows past a handful of pieces, give it the same treatment rather than overloading
  the homepage anchor.
- **Every research note still needs its own homepage card** (mirrors the Coverage/Industry
  pattern) **and its own nav link** (`Market Signals`, after `Industry`, before `Contact`, on every
  page that carries the shared `.topnav`). `dust/` and `industry/ai-semiconductor-supply-chain/`
  don't carry the shared topnav at all (they're self-contained documents with just a back-link) —
  don't add the nav item there.
- **Chart curation, not chart dumping.** The source project shipped 12 charts; the web page uses 7.
  Pick the ones that carry the argument (the hero chart, the two or three that prove the report's
  contrarian findings, one that shows quantitative range beyond the obvious). Point to the full PDF
  for the rest. This is the same "cut filler ruthlessly" rule as Section 1, applied to figures.
- **A monthly series needs an honest "edition 1" posture.** Don't fabricate a scorecard history —
  ship the running-scorecard table with exactly one open row and say plainly that this is the first
  edition. The credibility is in the mechanism (state what changed, what was wrong, before restating
  the view) being visibly ready to hold future editions accountable, not in pretending there's a
  track record yet.
