# Technogym DCF — Build Specification

**Object:** 10-year unlevered DCF of Technogym S.p.A. (Milan: TGYM), a premium B2B fitness-equipment maker with an embryonic connected-software layer. 15 sheets, 825 live formulas.

**Headline (base):** fair value **€15.72** (Gordon) / ~€18.3 (exit-multiple cross-check) vs €15.19 spot → **HOLD**. Bear €8.82 / Bull €24.05. WACC 7.75%.

**How to use this spec:** it's a **reference architecture to adapt to a new listed equity**, not a script to re-run for Technogym (that's done — see `../../technogym/`). The sheet order, scenario switch, driver-based revenue, two-method terminal cross-check and check-cell discipline all transfer unchanged; you swap the revenue drivers and inputs for your company. `build.py` in this folder reconstructs the exact Technogym workbook — read it when you need the literal formula in any cell, then adapt it. Shipped workbook: `../../models/Technogym_DCF_Model.xlsx`. Finished hosted analysis (thesis, inputs narrative, football field): `../../technogym/index.html`.

---

## Sheet map (build in this order)

| # | Sheet | Purpose |
|---|---|---|
| 01 | Cover | Title, disclaimer, colour-code legend. |
| 02 | Sources | Reported vs consensus vs judgment labels; source list. |
| 03 | Assumptions | **The scenario switch (`B3`) and every input.** All blue cells live here. |
| 04 | Historical Financials | 2021–25 actuals (revenue, margin, FCF) for anchoring. |
| 05 | Revenue Build | Driver-based revenue: BtoB, BtoC, and the **digital estimation block**. |
| 06 | Operating Model | EBITDA (hardware + digital isolated), EBIT, NOPAT. |
| 07 | Working Capital | NWC on DSO/DIO/DPO days, with bear-case stress. |
| 08 | Capex & Depreciation | Capex % of revenue; D&A. |
| 09 | Free Cash Flow | FCFF build, incl. IFRS-16 lease-principal charge. |
| 10 | WACC | Bottom-up cost of equity; net-cash company → WACC ≈ Ke. |
| 11 | DCF Valuation | PV of FCFF + terminal value (two methods), EV→equity bridge, per share. |
| 12 | Sensitivity Analysis | WACC × g and WACC × exit-multiple grids (recompute off the live FCFF row). |
| 13 | Scenarios | Lists all three assumption sets; ACTIVE column shows full-model output. |
| 14 | Charts & Dashboard | Headline outputs + illustrative probability-weighted value. |
| 00 | Executive Summary | Answer, drivers, football field, glossary. Written last, links upward. |

## `03 Assumptions` — the control sheet

`B3` = scenario switch (1/2/3), guarded by a check at `C3`. Scenario-driven rows use `=CHOOSE($B$3, C, D, E)` where columns C/D/E = Bear/Base/Bull and F = ACTIVE. The scenario inputs:

| Row | Input | Bear | Base | Bull |
|---|---|---|---|---|
| 6/7 | BtoB growth 2026 → fade-to-2035 | 4%→2% | 9%→2.5% | 13%→3% |
| 8/9 | BtoC growth 2026 → 2035 | 0%→1% | 5%→2% | 9%→2.5% |
| 10/11 | Digital attach endpoint (B2B / consumer) | 20% / 15% | 30% / 20% | 40% / 30% |
| 12 | Digital ARPU growth p.a. | 0% | 3% | 5% |
| **13** | **Hardware EBITDA margin endpoint by 2032** | 19.5% | **20.75%** | 22.2% |
| 14 | Capex % revenue | 5.5% | 5.0% | 5.0% |
| 16 | Terminal growth g | 1.5% | 2.25% | 2.75% |
| 17 | Exit EV/EBITDA (cross-check) | 10x | 12x | 14x |
| **18** | **Digital EBITDA margin** | 50% | 60% | 75% |

Fixed inputs (rows 21–36): tax 27.4%, D&A 5.1% of revenue, shares 199.3m ex-treasury, net cash €156m, NFP ex-IFRS16 €209.6m (used in the equity bridge), 2025 segment bases (BtoB €787.6m, BtoC €186.7m, digital est. €45m), installed base 100k sites / 500k homes, ARPU €1,800/site and €120/user. A check at `A40` enforces that the three 2025 segment bases sum to reported €1,019.3m.

## `05 Revenue Build` — driver-based, digital carved out

Three revenue streams, each grown from its own driver, then summed:
- **BtoB (ex-digital):** base/bull grow on a linear fade from the 2026 rate to the 2035 rate; **bear** follows an explicit cyclical path (row 32: a 2027 downturn of −10%, recovery from 2029) rather than a smooth fade — this is what a real capex cycle looks like.
- **BtoC (ex-digital):** linear fade.
- **Digital estimation block (rows 14–25):** `installed sites × attach rate × ARPU` for B2B, plus `connected homes × attach × ARPU` for consumer. Attach ramps to its endpoint by 2030; ARPU compounds. This block is **entirely L-confidence and editable** — it exists because Technogym discloses no digital KPI.

A check at `A31` ties the 2025 build back to reported €1,019.3m.

## `06 Operating Model` — the signature design: isolate the digital P&L

This is the model's defining decision. Rather than applying one blended EBITDA margin to all revenue (which silently lets software economics inflate the hardware margin), the two businesses are valued on **separate margins that sum to total EBITDA**:

- **Hardware margin (row 23)** starts at a *derived* 2025 level (~19.8%, = `(reported €220.1m EBITDA − digital EBITDA) / hardware revenue`, cell `B22`) and expands on its own operating leverage to the endpoint in `03!F13`.
- **Digital EBITDA (row 25)** = digital revenue × its own margin (`03!F18`, ~60%).
- **Total EBITDA (row 26)** = hardware + digital. For base/bull this feeds row 6; the **bear** case keeps the explicit cyclical total-margin path from `05!row33`.

The **base hardware endpoint (20.75%) is chosen so total base margin holds at the defensible ~23.5%** — the restructure is margin-neutral at base, so isolating digital *redistributes* value rather than inflating it. Consequence: the digital option is worth ~€3.3/share (base → bull-digital) instead of ~€0.6 when blended — but it sits in the bull case, and the base stays a HOLD. Margin-sanity check at `A13`.

## `09 Free Cash Flow` — IFRS-16 handled consistently

FCFF = NOPAT + D&A − capex − ΔNWC − **lease principal repayment** (IFRS-16, ~1.5% of revenue, row 8). Because lease principal is charged in FCFF, the EV→equity bridge on sheet 11 uses **NFP *excluding* IFRS-16 lease liabilities** (`03!B44` = €209.6m). Charging leases here rather than ignoring them was a v2 correction that lowered fair value ~€1.6/share — do not drop it.

## `10 WACC` — bottom-up, net-cash company

`Ke = rf + β·ERP + weighted CRP` = German Bund 3.13% + 0.95 × 4.23% mature-market ERP + 0.6% revenue-weighted country-risk premium ≈ **7.75%**. Deliberately does **not** use the Italian BTP yield as risk-free *and* add a CRP (that double-counts). Technogym is net cash, so debt weight = 0 and WACC ≈ Ke. Beta is triangulated across providers (0.86–0.94), flagged M-confidence. Range check at `A17`.

## `11 DCF Valuation` — two terminal methods, cross-checked

- PV of explicit FCFF 2026–35 at the WACC discount factor.
- **Terminal value, Method 1 (primary):** Gordon growth, `FCFF₂₀₃₅ × (1+g) / (WACC − g)`, PV'd. Reports the implied exit multiple (~9.4x — below today's ~13x, the honest signal).
- **Method 2 (cross-check):** 2035 EBITDA × exit multiple.
- EV → equity: `EV + NFP(ex-IFRS16)`, ÷ 199.3m shares → per-share value. A 5-year horizon cross-check is also shown.
- Checks: `A34` (WACC > g, else Gordon invalid) and `A35` (two TV methods within 35%).

## `12`–`14` — sensitivities, scenarios, dashboard

Grids on sheet 12 recompute per-share value off the **live FCFF row**, so they auto-update when any driver changes (they key off the WACC and terminal inputs, not a repurposed cell). Sheet 14 adds an **illustrative probability-weighted fair value** (40% Bear / 40% Base / 20% Bull → €14.63), explicitly labelled subjective and non-headline, with a weights-sum check at `A40`.

## Rebuild checklist specific to this model

- 2025 segment bases sum to €1,019.3m (`03!A40`, `05!A31`).
- Hardware 2025 margin is **derived to tie** reported €220.1m EBITDA — do not hardcode it; it must move if the digital margin input moves.
- Bear case uses the explicit cyclical paths (`05!row32/33`), not a linear fade.
- WACC lands 6–10% (`10!A17`); WACC > g (`11!A34`); TV methods within 35% (`11!A35`).
- Flip `03!B3` to 1/2/3 → €8.82 / €15.72 / €24.05 (see `../../VERIFICATION.md`).
