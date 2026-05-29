# Taxation in Romania (2026)

> ⚠️ **Not tax advice. Verified 2026-05; rates change frequently (major 2025–2026 reforms) — confirm with ANAF/an accountant.** Sources: [`sources.md`](sources.md).

## Company income tax — two regimes

### Micro-enterprise regime (1% on revenue)
- **1%** tax on revenue. [[S6]](sources.md#s6) [[S9]](sources.md#s9)
- Eligibility: turnover **≤ €100,000** (lowered from €250,000), **at least 1 employee**, and **sector restrictions removed** for 2026 (any activity may qualify if the other conditions are met). [[S6]](sources.md#s6) [[S9]](sources.md#s9)
- Cross €100,000 → switch to **CIT 16%** from the quarter in which the threshold is exceeded. [[S9]](sources.md#s9)

### Corporate income tax (CIT)
- **16%** on profit. [[S8]](sources.md#s8) [[S9]](sources.md#s9)
- **IMCA** minimum turnover tax for very large companies (turnover > €50M): **0.5%** in 2026 (down from 1%), **abolished in 2027**. [[S6]](sources.md#s6)

> **Choosing:** micro is simpler and often cheaper at healthy margins (tax on revenue, not profit); CIT can be better at thin/negative margins or once you pass the threshold. Model both in [`../templates/financial-model.md`](../templates/financial-model.md).

## VAT (TVA)
- Standard rate **21%** (raised from 19% in mid-2025). [[S6]](sources.md#s6) [[S9]](sources.md#s9)
- Reduced rates apply to certain categories (e.g. some food, medicines, books) — *[TODO: verify current reduced-rate values for 2026]*.
- Registration status (and the option to register voluntarily) affects pricing and cash flow — see the reporting stack in [regulatory-compliance.md](regulatory-compliance.md).

## Dividend tax
- **16%** on dividends from 1 Jan 2026 (up from 10% in 2025), for individuals and legal entities. [[S6]](sources.md#s6) [[S7]](sources.md#s7)

## Payroll & social contributions (2026)
Burden on salaries:

| Contribution | Romanian | Rate | Paid by |
|--------------|----------|------|---------|
| Pension | CAS | **25%** of gross | Employee (withheld) [[S15]](sources.md#s15) |
| Health | CASS | **10%** of gross | Employee (withheld) [[S15]](sources.md#s15) |
| Income tax | impozit pe venit | **10%** (on gross after CAS+CASS) | Employee (withheld) [[S15]](sources.md#s15) |
| Work insurance | CAM | **2.25%** of gross | **Employer** [[S15]](sources.md#s15) |

- An employee's gross splits roughly **65% net / 35% contributions**, before income tax; the **employer adds ~2.25%** on top. [[S15]](sources.md#s15)
- **CAS** is capped at a ceiling of 24× the minimum wage; **CASS** has no ceiling on employment income. [[S15]](sources.md#s15)
- **Minimum gross wage 2026:** **RON 4,050/month** until June, **RON 4,325** from July 2026; construction sector **RON 4,582**. [[S16]](sources.md#s16)

> **Hard-questions tie-in:** §6 (financial viability) — model the gross→net and gross→employer-cost gaps, and pick the right regime.
