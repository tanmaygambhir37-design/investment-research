# How to Build the Financial Model — Playbook

Companion to `MEMO_PLAYBOOK.md`. That one is for pieces that are mostly writing (the Dust memo).
**This one is for pieces that need a real valuation** — a DCF or an LBO, built as a live Excel
workbook and shipped as a full site analysis like `technogym/` and `recordati/`.

It exists so a new session can build a model for **a company we haven't covered yet** — a different
industry, a different deal — without relearning the method by trial and error. The two workbooks in
`models/` and their pages under `technogym/` and `recordati/` are the canonical examples. When in
doubt, open one and match it.

**You are not here to rebuild Technogym or Recordati.** Those are done. You are here to produce the
*next* one — pick a company, decide DCF or LBO, build it to the same standard, red-team it, and ship
the finished page to the site. The examples are the template; the deliverable is a new, hosted piece.

---

## Where the pieces live

- `MODEL_PLAYBOOK.md` — this file: the method and the modeling rules.
- `model-kit/technogym_dcf/` and `model-kit/recordati_lbo/` — a `BUILD_SPEC.md` (sheet-by-sheet
  architecture, the transferable one) and a `build.py` (a deterministic reconstruction of the exact
  workbook — read it when you need the literal formula in any cell, adapt it for a new company).
- `model-kit/VERIFICATION.md` — the check-cell discipline every model must carry, plus the two
  examples' expected Bear/Base/Bull outputs as a reference for what "done" looks like.
- `models/*.xlsx` — the two shipped workbooks (diff a rebuild against these).
- `technogym/`, `recordati/`, `red-team/` — the finished, hosted pages. Your new piece copies these.

## The method (four phases — same for any company)

1. **Research.** Build the dossier from public sources, then an **Assumptions Register**: every input
   as a row — *value · source · date · confidence (H/M/L)*. H = reported, M = derived, L = judgment.
   Nothing enters the model that isn't on the register with a grade. This is the memo-side discipline
   from `MEMO_PLAYBOOK.md`, applied to model inputs.
2. **Thesis, written first.** Before building, write down where you expect the model to land *and
   why*, and commit to it. The rule: the model is built blind to that number, not toward it. If it
   lands outside your range, you attribute the gap to a named assumption before touching anything.
   This is what stops you tuning inputs until the model agrees with what you already believed.
3. **Build the model** (rules below).
4. **Red-team it.** Attack your own load-bearing assumptions. Where a challenge lands, change the
   model and record what moved. Where it doesn't, record the defence. Both example conclusions moved
   *against* the starting thesis — that's the sign it worked, and it's the whole reason the red-team
   page is the most differentiating thing on the site.

## Modeling rules (extracted from building Technogym and Recordati)

These are the corrections that actually got made, not generic advice.

- **One scenario switch drives everything.** `03 Assumptions!B3` = 1/2/3 (Bear/Base/Bull). Every
  scenario input is `=CHOOSE($B$3, bear, base, bull)` on the Assumptions sheet; downstream sheets
  read the single ACTIVE column. Flip the switch, the whole model moves. Don't scatter scenario logic
  across sheets.
- **Driver-based, never a single growth row.** Revenue is built from its economics (segment growth;
  installed base × attach × ARPU), so every assumption is inspectable. A lone "revenue grows 8%" row
  is not a model, it's a guess with extra steps.
- **No invented data — build an estimation block instead.** Where a number isn't disclosed (Technogym
  digital revenue; Recordati segment EBITDA), make the drivers visible, editable, and labelled L, and
  force them to reconcile to a reported total. Never hardcode a fabricated "reported" figure. This is
  the model-side version of the memo rule "undisclosed metrics are shown as Not Disclosed, not
  estimated into existence."
- **Isolate the thing you're actually valuing, or the assumption smuggles itself in.** Technogym's
  whole point was the software option. Blending digital into one group margin let the software
  economics inflate the hardware margin invisibly. Splitting the P&L — hardware on its own margin,
  digital on its own ~60% margin, summed — is what made the option worth ~€3.3/share honestly instead
  of ~€0.6 by accident. If a model exists to answer one question, that question needs its own line.
- **Cross-check every terminal / exit value two ways.** DCF: Gordon growth vs exit multiple, and flag
  if they diverge (`11!A35`). LBO: a MOIC bridge that must sum back to the headline MOIC (`10!A21`).
  If the two methods don't agree, you don't have a valuation, you have one number and a hope.
- **Check cells everywhere, and they must be green.** Reconciliation `=IF(...,"CHECK OK","ERROR:...")`
  cells: 2025 build ties to reported revenue; sources = uses; bridge ties; WACC > g. A model with a
  red check is not to be trusted — fix before shipping. Full list in `model-kit/VERIFICATION.md`.
- **Don't double-count risk in the discount rate.** WACC used the German Bund as risk-free plus a
  revenue-weighted country-risk premium — *not* the Italian BTP yield *and* a CRP, which counts Italy
  risk twice. Net-cash company → debt weight 0 → WACC ≈ cost of equity.
- **Model the tax and structure reality, not the textbook.** The LBO applies the ATAD 30%-of-EBITDA
  interest-deductibility cap to cash taxes; uses a close-date net-debt estimate (not the stale
  year-end figure) so the entry multiple and equity cheque are right; and decomposes returns to show
  the bolt-on machine is ~IRR-neutral and the exit multiple is the whole bet. Those specifics won't
  all transfer, but the habit — model what actually governs the cash — does.
- **Ship without cached values** (`wb.calculation.fullCalcOnLoad = True`) so the workbook recomputes on
  open and can never show a stale headline.
- **Colour code = audit trail:** blue = input, black = formula, green = cross-sheet link, red = check,
  yellow = the primary levers.

## Adapting the kit to a new company

1. **DCF or LBO?** A listed equity you're valuing on its own cash flows → DCF (mirror
   `model-kit/technogym_dcf/`). A buyout / take-private you're underwriting with leverage → LBO
   (mirror `model-kit/recordati_lbo/`). Some companies warrant both.
2. **Keep the architecture, swap the drivers.** The sheet order, the scenario switch, the check-cell
   discipline, the two-method terminal cross-check, the FCFF/returns build — all transfer unchanged.
   What changes is the *revenue drivers* and the *company-specific realities* (a SaaS business isn't
   installed-base × ARPU; a bank isn't FCFF at all). Read the relevant `BUILD_SPEC.md` for the
   architecture and `build.py` for the exact formula patterns, then rebuild with the new company's
   drivers and inputs.
3. **Re-run the four phases for the new name** — new register, new pre-model thesis, new red-team.
   Don't inherit the old company's numbers.

## Shipping the piece to the site (this is what makes it a finished product)

A model isn't done when the workbook is; it's done when it's a hosted analysis matching the house
pattern. The five-stage skeleton from `MEMO_PLAYBOOK.md`, for a model piece:

**30-Second Read → full analysis → Sources & Uses (LBO) or football-field (DCF) → Red-Team page → Sources.**

Concretely, for a new company `<co>`:

1. **Create `<co>/index.html`** by copying `recordati/index.html` (LBO) or `technogym/index.html`
   (DCF) and replacing the content. Keep every structural element: the sticky top nav, the gold
   **THE 30-SECOND READ** box directly under the verdict badge, the section order, the "Last updated"
   line, the OG tags (`og:title`, `og:description`, `og:image` → the site `og.png`, `og:url`), and
   the Investment Summary (PDF) as the primary button with the model `.xlsx` secondary.
2. **Put the workbook in `models/`** and link it from the page's download button.
3. **Add a deal card to the landing page** (`index.html`, the `Financial Modeling` grid): copy an
   existing card block, swap the title, one-line context, the four stat tiles (with hover-tooltip
   definitions), the "In short:" verdict line, the plain-language key finding, tags, and the two
   buttons (`Investment summary →` primary, `⤓ Model (.xlsx)` secondary).
4. **Extend the red-team page** (`red-team/`) with a Part for the new model, or give it its own, in
   the same "challenges that land / don't land / revised judgment" format.
5. **Voice and integrity rules from `MEMO_PLAYBOOK.md` apply verbatim** — no em dashes, spell out
   abbreviations on first use, one number per fact, and **every number on the page must reconcile to
   the live workbook.** If the card says 15% and the model computes 14%, the model wins and the card
   is wrong. Grep the whole piece for each headline figure before calling it shipped.

## What "done" looks like

A new `.xlsx` in `models/` whose scenario switch drives sensible Bear/Base/Bull outputs with every
check cell green; a `<co>/index.html` live on the site in the house style with a 30-Second Read on
top; a deal card on the landing page; a red-team section; and not a single number anywhere in the
prose that disagrees with the workbook. That is a finished piece — the same bar as `recordati/` and
`technogym/`, applied to a company we hadn't covered before.
