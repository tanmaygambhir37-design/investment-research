# Recordati LBO — Build Specification

**Object:** independent leveraged-buyout underwrite of the €10.7bn CVC IX / GBL take-private of Recordati S.p.A. (Milan: REC), a two-part pharma (mature Specialty & Primary Care funding high-growth Rare Diseases). 14 sheets, 605 live formulas. The model underwrites the deal *blind* at the announced price, then reconciles against the actual announced economics.

**Headline (base):** **~15.0% IRR / ~2.01x MOIC**. No-BD conservative floor ~15.1%; sponsor-consistent read (entry-flat 12.9x exit) ~18%; full thesis ~24%. Bear ~4% / Bull ~24%. → **PARTICIPATE selectively (6/10).**

**How to use this spec:** it's a **reference architecture to adapt to a new buyout / take-private**, not a script to re-run for Recordati (that's done — see `../../recordati/`). The S&U, three-tranche debt schedule with sweep, the returns/MOIC-bridge logic and the check-cell discipline all transfer unchanged; you swap the segment build, deal terms and financing for your target. `build.py` reconstructs the exact Recordati workbook — read it for the literal formula in any cell, then adapt it. Shipped workbook: `../../models/Recordati_LBO_Model.xlsx`. Finished hosted analysis: `../../recordati/index.html`.

---

## Sheet map (build in this order)

| # | Sheet | Purpose |
|---|---|---|
| 01 | Cover | Title, disclaimer, legend. |
| 02 | Sources | Reported vs derived vs judgment. |
| 03 | Assumptions | **Scenario switch (`B3`) + every input**, incl. the close-date net-debt bridge. |
| 04 | Historical Financials | 2021–25 actuals. |
| 05 | Transaction Overview | The announced deal facts (offer, premium, structure, co-investors). |
| 07 | Purchase Price | Entry EV and multiples (close-date basis + announced-basis reference). |
| 06 | Sources & Uses | Uses (equity + refinanced debt + fees + min cash) = Sources (debt tranches + sponsor equity plug). |
| 09 | Operating Model | RD / SPC segment build; organic EBITDA + BD-acquired EBITDA. |
| 08 | Debt Schedule | 3-tranche debt, mandatory amort + 100% cash sweep, interest, FCF, leverage/coverage. |
| 10 | Returns | IRR / MOIC, the MOIC bridge, and IRR by exit year. |
| 11 | Sensitivities | IRR across exit multiple × EBITDA growth × leverage. |
| 12 | Charts | Visual outputs. |
| 13 | Dashboard | Independent model vs actual announced deal; the value-creation decomposition. |
| 00 | Executive Summary | Answer, drivers, risks, glossary. Written last. |

## `03 Assumptions` — the control sheet

`B3` = scenario switch (1/2/3), check at `C3`. Scenario rows use `=CHOOSE($B$3, …)`:

| Row | Input | Bear | Base | Bull |
|---|---|---|---|---|
| 6/7 | Rare Diseases growth 2027–29 → 2030–31 | 8%→5% | 14%→9% | 19%→12% |
| 8 | Specialty & Primary Care growth p.a. | −1% | 2% | 3.5% |
| 9 | EBITDA margin endpoint by 2029 | 36.0% | 37.75% | 39.0% |
| 10 | Entry leverage (× FY25 EBITDA €991.1m) | 5.0x | 5.5x | 6.0x |
| 11 | Exit EV/EBITDA multiple | 10.0x | 11.5x | 12.9x |
| 13 | BD / in-licensing spend per year 2027–31 (€m) | 0 | 400 | 600 |

Fixed inputs: FY25 EBITDA €991.1m, revenue €2,618.4m (RD €1,081.4m / SPC €1,537m), offer €51.29/sh × 209.125m shares = €10,726m equity, advisory fee 1.25% of EV, OID 2.5% of debt, blended debt cost inputs (Euribor 2.1% + TLB spread 3.75%, USD TLB 7.25% all-in, notes 6.75%), tax 24%, maintenance capex 1.5% of revenue, ΔNWC 15% of revenue change, tranche split (TLB-EUR 55% / TLB-USD 18% / notes remainder), 1% mandatory amort, min operating cash €250m, ATAD interest-deduction cap 30% of EBITDA, hold 5 years.

**Close-date net-debt bridge (rows 49–52, the v3 correction):** the net debt refinanced at close is **not** the FY25 reported €2,037.3m but a bridged estimate: `€2,037.3m − €550m 2026 FCF + €280m 2026 dividends ≈ €1,767m` (cell `B52`), and `B23` points to it. This lowers uses, the equity cheque, and entry EV. The FY25 gross figure is retained at `B49` for the announced-basis multiple reference.

## `07 Purchase Price` — two entry multiples

- `B8` = EV / FY25 EBITDA on **close-date** net debt ≈ **12.6x** (the independent basis).
- `B14` = EV / FY25 EBITDA on **FY25 gross** net debt ≈ **12.9x** (the announced-deal basis). The check at `A13` ties `B14` to the announced 12.9x — so the model reconciles to the real deal while underwriting on a cleaner close-date basis.

## `06 Sources & Uses`

Uses = equity purchase (€10,726m) + refinanced net debt (`03!B23`, close-date) + advisory fees (1.25% × EV) + OID (2.5% × new debt) + min cash (€250m). Sources = total new debt (leverage × €991.1m, split into TLB-EUR / TLB-USD / Senior Secured Notes) + sponsor equity **plug**. Balance check at `A21` (sources = uses). Sponsor equity falls out as the residual.

## `09 Operating Model` — segment build + BD engine

- **RD revenue** grows at the scenario RD rate (higher for years 1–3, stepping down 4–5); **SPC** at its flat rate. Total revenue → EBITDA at a margin that ramps to the endpoint (`03!F9`).
- **BD-acquired EBITDA (row 17):** each €400m/yr of business development buys `spend / 9.0x` of EBITDA, **credited from the year *after* spend** (an acquisition made in year *t* contributes from *t+1*). Cumulative into row 17; total EBITDA (row 18) = organic + acquired.
- **The exit-year bug fix (v3):** BD spend in the final hold year (2031) is set to €0 in the debt schedule, because EBITDA it would buy only lands in 2032 — after exit. Cumulative modeled BD is therefore €1.6bn (2027–2030), at a true 9.0x effective, not €2.0bn. Guidance check at `A20` (2026 EBITDA within €995–1,030m).

## `08 Debt Schedule` — waterfall, sweep, and the tax cap

Three tranches: **TLB-EUR** (Euribor + spread), **TLB-USD** (all-in; a natural hedge against US rare-disease revenue), **Senior Secured Notes** (fixed bullet). Mechanics per year:
- 1% mandatory amortisation, then a **100% cash sweep** of remaining FCF, applied **TLB-EUR first, then TLB-USD**, with residual cash accumulating once TLBs are repaid (notes are a bullet).
- Interest on **beginning** balances (avoids circularity; slightly conservative).
- **Cash taxes** apply the **ATAD 30%-of-EBITDA interest-deductibility cap** — interest above 30% of EBITDA is not deductible (carryforward ignored, conservative).
- FCF before debt service = EBITDA − capex − ΔNWC − cash tax − cash interest − BD spend.
- Leverage, interest coverage and DSCR reported; coverage check at `A40` (year-1 coverage > 2.5x).

Because BD is funded pre-sweep, the base case exits at ~1.9x leverage (the €1.6bn BD came out of the sweep); the **no-BD floor** deleverages to ~1.0x.

## `10 Returns` — IRR, MOIC, and the bridge that must tie

- Exit equity = exit-year EBITDA × exit multiple − net debt at exit. MOIC = exit equity / entry equity; IRR = `MOIC^(1/hold) − 1` (single-flow; conservative vs recap optionality).
- **MOIC bridge:** entry (1.00x) + EBITDA growth at entry multiple + multiple change + deleveraging + fees residual. Check at `A21` forces the bridge to sum back to the headline MOIC — if it doesn't, the model is wrong.
- IRR / MOIC by exit year (2029/30/31) shown live.

## `13 Dashboard` — the decomposition (the model's punchline)

Independent model vs the actual announced deal, and the **BD value-creation decomposition**: no-BD floor ~15% → funding BD €400m/yr adds ~0 to −0.1pt (the 9x-in / 11.5x-out arbitrage is offset by interest drag on un-swept cash + forfeited deleveraging) → exit at entry-flat 12.9x adds **+2.9pt**. Conclusion: the exit multiple is ~100% of the sponsor's return case; BD grows MOIC *dollars*, not the *rate*. This is the finding that separates this model from a naive "bolt-ons make pharma LBOs work" narrative.

## Rebuild checklist specific to this model

- Net debt refinanced uses the **close-date bridge** (`03!B23 = B52 ≈ €1,767m`), not FY25 gross — but the announced-basis multiple (`07!B14`) must still tie to 12.9x (`07!A13`).
- BD 2031 (exit-year) spend = €0; BD-acquired EBITDA credits from the year after spend.
- Sources = Uses (`06!A21`); MOIC bridge ties (`10!A21`); year-1 coverage > 2.5x (`08!A40`); 2026 EBITDA in guidance (`09!A20`).
- Interest on beginning balances; ATAD 30% cap applied to cash taxes.
- Flip `03!B3` to 1/2/3 → ~4% / ~15% / ~24% IRR (see `../../VERIFICATION.md`).
