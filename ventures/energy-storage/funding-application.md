# Funding Application (mockup) — Energy Storage → Modernisation Fund (standalone)

> A **full "funds project" mockup** for the battery, via the Modernisation Fund **standalone storage** scheme. Planning aid, not a submission — fill against the official Applicant Guide. Method: [`../../framework/eu-funding-playbook.md`](../../framework/eu-funding-playbook.md). [E#] → [sources](research/sources.md). Verified 2026-05.

> **Grant-route note:** this scheme funds the **standalone battery only**; the co-located **solar is financed separately** (merchant/PPA). This is the "standalone" branch of the [grant-route decision](decision-log.md).

## 1. Applicant & instrument
| Field | Value |
|-------|-------|
| Applicant | RO Grid Storage SRL *(SPV, working name)* |
| CUI / J-number | *[TBD at incorporation]* |
| Legal form & size | SRL; SME (newly established) |
| Instrument | **Modernisation Fund — standalone battery storage** (CISAF state-aid) [E41](research/sources.md#e41) |
| Call reference | Ministry of Energy €150M call (EC-approved Mar 2026); window **Q2 2026** [E30](research/sources.md#e30) |
| Platform | **MySMIS2021** (energie.gov.ro for guide/timeline) [E41](research/sources.md#e41) |

## 2. Executive summary
A **50 MW / 100 MWh** standalone lithium battery at a grid-strategic node, delivering balancing services + arbitrage. Eligible CAPEX **€28M**; **grant requested €6.0M** (a **€60,000/MWh** bid, under the €69k cap); **co-financing €22M** (equity + debt). Adds **100 MWh** of flexible capacity to a congested grid.

## 3. Alignment with objectives & priorities
Directly serves the scheme's aim — **storage to integrate renewables and stabilise the grid** [E41](research/sources.md#e41) — amid ~60 GW of connection requests vs ~10.5 GW headroom. [E34](research/sources.md#e34) [E36](research/sources.md#e36)

## 4. Eligibility self-check
| Criterion | Requirement | Us | ✓ |
|-----------|-------------|----|---|
| Entity | micro→large, incl. new EU entities | SRL SPV | ✓ |
| Asset | **standalone** electricity storage | 100 MWh standalone | ✓ |
| ONRC before first aid payment | yes | will incorporate pre-award | ✓ |
| Not double-funded | yes | solar funded separately, no overlap | ✓ |

## 5. Project description
100 MWh / 50 MW LFP system (2h), CAEN **3516** (storage); grid connection (ATR) at a high-headroom substation; ANRE establishment authorization (>1 MW) + operating licence. [E35](research/sources.md#e35) [E13](research/sources.md#e13) **Candidate site:** the reinforced **Suceava 400/110 kV** node (DSO **Delgaz Grid**), near **Ilișești / DN17** — see [site-suceava-ilisesti.md](site-suceava-ilisesti.md). [E42](research/sources.md#e42) [E43](research/sources.md#e43)

## 6. Budget & eligible costs
| Item | Total | Eligible? | Notes |
|------|------:|:---------:|-------|
| Battery system (100 MWh) | €28.0M | ✓ | investment cost; operating excluded |
| Grid connection works | (in CAPEX) | ✓ | per ATR |
| **Total eligible** | **€28.0M** | | VAT excluded (recovered via ANAF) |
| **Grant requested** | **€6.0M** | | bid €60k/MWh (≤€69k cap; ≤€10M/company; ≤100%) [E41](research/sources.md#e41) |
| **Co-financing** | **€22.0M** | | equity + project debt |

## 7. Selection — the €/MWh bid
Single criterion = **requested aid €/MWh**; lowest ranks highest. [E30](research/sources.md#e30) **Our bid: €60,000/MWh** (€6.0M / 100 MWh) — under the €69k ceiling, but the rank depends on rivals. Trade-off modelled in finsim: a lower bid improves rank but cuts the grant and the IRR.

## 8. Implementation plan & milestones
| Milestone | Date | Done when |
|-----------|------|-----------|
| ATR + ANRE establishment auth. | 2027 H1 | permits issued |
| Grant award + financing close | 2027 H2 | contracts signed |
| Build + energisation | 2028 | COD |
| Aid fully disbursed | **≤ 31 Dec 2030** | scheme deadline [E30](research/sources.md#e30) |

## 9. Indicators / outputs
**100 MWh / 50 MW** new storage; renewable MWh shifted; CO₂ avoided; negative-price hours absorbed; balancing availability.

## 10. Financial viability
See [finsim-report.md](finsim-report.md) (`tools/finsim/run.py … finsim.json`). With the corrected **€6.0M** grant the project is **marginal** at a 10% hurdle — reinforcing the need for a low-but-viable bid, a revenue floor (tolling), and cheap debt. See [financial-model.md](financial-model.md).

## 11. Risk & compliance
Not winning the bid (rank) → have a fallback bid/scenario; clawback if milestones missed → realistic schedule; procurement/audit rules → clean trail; state-aid cumulation → no overlap with solar funding.

## 12. Annexes checklist
- [ ] ONRC registration
- [ ] ATR (grid connection) + ANRE establishment authorization
- [ ] Building permit; technical design
- [ ] Proof of co-financing (equity + debt term sheet)
- [ ] finsim projection ([finsim-report.md](finsim-report.md))

## 13. Sources
Scheme: [E30](research/sources.md#e30) [E41](research/sources.md#e41); grid: [E34](research/sources.md#e34) [E36](research/sources.md#e36); CAEN/permits: [E35](research/sources.md#e35) [E13](research/sources.md#e13). Re-verify against the official Applicant Guide.
