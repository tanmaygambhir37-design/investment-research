# Verification — the check-cell discipline every model must carry

Two uses. **(A)** The discipline any *new* model you build must have: check cells that all read green, and a scenario switch that drives sensible Bear/Base/Bull outputs. **(B)** The two worked examples' expected outputs, so you know what "done" looks like and can confirm the reference `build.py` scripts reproduce the shipped workbooks. The workbooks ship with `fullCalcOnLoad`, so open them in Excel (or recompute with LibreOffice headless) to evaluate formulas; `openpyxl` alone reads formulas but does not calculate them. The shipped reference workbooks are in `../models/`.

## 1. Check cells — all must read `CHECK OK` / `OK`

**Technogym DCF**

| Cell | Passes when |
|---|---|
| `03 Assumptions!C3` | switch is 1, 2 or 3 |
| `03 Assumptions!A40` | 2025 segment bases (787.6 + 186.7 + 45) sum to reported 1,019.3 |
| `05 Revenue Build!A31` | 2025 revenue build ties to reported 1,019.3 |
| `06 Operating Model!A13` | margin path stays in a sane range (start >10%, 2035 <35%) |
| `10 WACC!A17` | WACC lands 6–10% |
| `11 DCF Valuation!A34` | WACC > g (Gordon valid) |
| `11 DCF Valuation!A35` | the two terminal-value methods are within 35% |
| `14 Charts & Dashboard!A40` | scenario weights sum to 100% |
| `00 Executive Summary!A32` | consensus-bridge attribution ties to the gap |

**Recordati LBO**

| Cell | Passes when |
|---|---|
| `03 Assumptions!C3` | switch is 1, 2 or 3 |
| `06 Sources & Uses!A21` | sources = uses |
| `07 Purchase Price!A13` | announced-basis entry multiple (`B14`) ≈ 12.9x |
| `09 Operating Model!A20` | 2026 EBITDA within guidance 995–1,030 |
| `08 Debt Schedule!A40` | year-1 interest coverage > 2.5x |
| `10 Returns!A21` | the MOIC bridge sums back to the headline MOIC |

If any cell reads `ERROR …` or a bare `CHECK …`, the model is broken. Fix before reporting done.

## 2. Expected headline outputs (flip `03 Assumptions!B3`)

**Technogym DCF — per-share fair value (Gordon)**

| `B3` | Scenario | Fair value | Note |
|---|---|---|---|
| 1 | Bear | **€8.82** | explicit 2027 cyclical downturn |
| 2 | Base | **€15.72** | +3.5% vs €15.19 spot → HOLD |
| 3 | Bull | **€24.05** | digital attach ramp + margin upside |

Other base anchors: exit-multiple cross-check ~€18.3; Gordon-implied exit ~9.4x; WACC 7.75%; TV ≈ 63% of EV; digital option (base → bull-digital) ~€3.3/share; illustrative probability-weighted value €14.63.

**Recordati LBO — sponsor IRR / MOIC**

| `B3` | Scenario | IRR | MOIC |
|---|---|---|---|
| 1 | Bear | **~4%** | ~1.2x |
| 2 | Base | **~15.0%** | ~2.01x |
| 3 | Bull | **~24%** | ~3.0x |

Other base anchors: no-BD conservative floor ~15.1%; sponsor-consistent (entry-flat 12.9x exit) ~18%; entry 12.6x close-date / 12.9x announced; exit leverage ~1.9x (BD-funded) / ~1.0x (no-BD); BD contribution ~0 to −0.1pt; exit-multiple contribution +2.9pt.

> Values are stated to the precision the model supports. Small differences (±0.1pt IRR, ±€0.05/share) from recompute-engine rounding are fine; a difference of a full point or more means a formula diverged — diff against `../models/`.

## 3. Confirm the reference build scripts are faithful

Running a `model-kit/*/build.py` and diffing its output against `../models/` yields exactly zero differences — that is the guarantee the reference reconstructions match the shipped workbooks. Use the same diff to check a new model against its own reference, or to confirm the scripts still round-trip:

```python
import openpyxl
def cells(p):
    wb = openpyxl.load_workbook(p)
    return {(ws.title, c.coordinate): c.value
            for ws in wb.worksheets for row in ws.iter_rows() for c in row if c.value is not None}, \
           [w.title for w in wb.worksheets]

mine, so_mine = cells("my_rebuild.xlsx")
ref,  so_ref  = cells("../models/Technogym_DCF_Model.xlsx")
assert so_mine == so_ref, "sheet order differs"
diffs = [k for k in ref if ref[k] != mine.get(k)] + [k for k in mine if k not in ref]
print("DIFFS:", len(diffs))
for k in diffs[:20]:
    print(k, "ref=", repr(ref.get(k))[:60], "mine=", repr(mine.get(k))[:60])
```

Expected: `DIFFS: 0`.
