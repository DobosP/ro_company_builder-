# Financial Model (spec) — <Venture Name>

> Markdown spec of the model. The spreadsheet/calculator becomes a tool later (see [`../tools/README.md`](../tools/README.md)). Use real Romanian rates from [taxation.md](../knowledge/taxation.md).

## Inputs (assumptions)
| Input | Value | Note |
|-------|-------|------|
| Price per unit / customer | | |
| Units / customers (monthly ramp) | | |
| Variable cost per unit | | |
| Fixed monthly costs | | |
| Headcount & gross salaries | | payroll model below |
| Starting capital | | min RON 500 for SRL |
| Funding (grant/debt) | | co-financing %, timing |

## Tax regime comparison _(decide explicitly)_
| | Micro (1% revenue) | CIT (16% profit) |
|---|---|---|
| Eligible? | turnover ≤ €100k + ≥1 employee | always |
| Tax on… | revenue | profit |
| Better when… | healthy margins | thin/negative margins or > €100k |

## Payroll (per employee, RON/month)
| Line | Formula |
|------|---------|
| Gross | input |
| − CAS (25%) | gross × 0.25 |
| − CASS (10%) | gross × 0.10 |
| − Income tax (10%) | (gross − CAS − CASS) × 0.10 |
| **= Net** | take-home |
| **Employer cost** | gross × 1.0225 (CAM 2.25%) |

_(Min gross wage 2026: RON 4,050 → 4,325 from July — see [taxation.md](../knowledge/taxation.md).)_

## Outputs
- Monthly P&L (revenue − COGS − opex − tax)
- VAT (21%) cash-flow impact, if registered
- Break-even month
- Cash runway / financing need
- Sensitivity: ±20% price, ±20% volume, slower ramp

## Open assumptions to validate
- [ ]
- [ ]
