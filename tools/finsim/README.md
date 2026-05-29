# finsim — venture financial simulator

A small, **dependency-free** (pure Python 3.8+ stdlib) financial projection engine for any venture in this repo. One generic engine; each venture supplies a **JSON config**. Romanian tax/payroll rules are baked in and mirror [`../../knowledge/taxation.md`](../../knowledge/taxation.md).

> Planning aid, **not** accounting or tax advice. Re-verify rates against [`../../knowledge/open-questions.md`](../../knowledge/open-questions.md) before relying on output.

## Run it
```bash
# console summary
python tools/finsim/run.py ventures/energy-storage/finsim.json

# write a Markdown report next to the venture
python tools/finsim/run.py ventures/energy-storage/finsim.json --out ventures/energy-storage/finsim-report.md

# examples for the other venture types
python tools/finsim/run.py tools/finsim/configs/saas-app.example.json
python tools/finsim/run.py tools/finsim/configs/ngo-app.example.json

# override the tax regime, or export CSV
python tools/finsim/run.py <config> --regime cit --csv /tmp/proj.csv

# tests
python tools/finsim/test_finsim.py
```

## What it computes
Per year over the horizon: **Revenue → OPEX → EBITDA → Depreciation → Interest → Tax → Net profit**, plus **project free cash flow**, **cash balance**, and **DSCR**. Headline metrics: **NPV, IRR, payback, P&L break-even, min cash, min DSCR**, and optional **net dividends**.

- **Tax regime** `auto` compares **micro (1% of revenue)** vs **CIT (16% of profit)** and picks the cheaper *eligible* one (micro needs every year ≤ €100k turnover **and** ≥1 employee). `ngo` → no profit tax. Force with `tax_regime` or `--regime`.
- **CIT** uses simple **loss carry-forward**; **grants** reduce the depreciation base pro-rata (per-grant toggle); **debt** supports annuity / linear / bullet.

## Config schema (JSON)
| Key | Type | Notes |
|-----|------|-------|
| `name`, `currency` | str | label + currency code (display only) |
| `eur_rate` | num | currency units per **1 EUR** (1.0 if EUR) — used for the micro €100k test |
| `start_year`, `horizon_years` | int | projection window |
| `legal_form` | str | `srl` \| `sa` \| `pfa` \| `ngo` |
| `tax_regime` | str | `auto` \| `micro` \| `cit` \| `none` |
| `discount_rate` | num | for NPV/IRR (e.g. 0.10) |
| `revenue` | list | each: `{name, amounts_by_year:[...]}` **or** `{name, base, growth}` |
| `costs.fixed_opex` | num/list/obj | a [series](#series) |
| `costs.variable_pct_of_revenue` | num | e.g. 0.15 |
| `costs.payroll` | list | each: `{role, count, gross_monthly}` (employer cost adds CAM 2.25%) |
| `capex` | list | each: `{name, amount, year, depreciation_years}` |
| `grants` | list | each: `{name, amount, year, reduces_depreciation_base?}` |
| `financing.equity` | num | injected in `start_year` |
| `financing.debt` | list | each: `{amount, rate, term_years, type, draw_year}` |
| `dividend_payout` | num | fraction of net profit distributed (for take-home) |

<a id="series"></a>**Series** values accept a number (constant), a list (by year, last value carried forward), `{amounts_by_year:[...]}`, or `{base, growth}`.

## Deliberate simplifications (honest caveats)
- **VAT** is treated as pass-through (amounts are net of VAT); CAPEX VAT is recoverable with a timing lag not modelled here.
- Payroll uses CAS 25% + CASS 10% + 10% income tax (employee) and CAM 2.25% (employer); **minimum-wage tax reliefs** and **CASS-on-dividends** are not modelled (see [taxation.md](../../knowledge/taxation.md)).
- No working-capital, inflation indexation, or terminal value. `auto` regime is a whole-horizon choice (a company-level decision), not switched mid-life.
- **Local/property tax** (asset-heavy ventures) is not automatic — add it to `fixed_opex`.

## Files
- `finsim.py` — engine (series, debt schedule, projection, NPV/IRR)
- `tax_ro.py` — Romanian rates & payroll (mirrors the knowledge base)
- `report.py` — Markdown / CSV / console renderers
- `run.py` — CLI · `test_finsim.py` — unit tests · `configs/` — example configs

**When tax rates change:** update [`../../knowledge/taxation.md`](../../knowledge/taxation.md) **and** `tax_ro.py` together, then re-run.
