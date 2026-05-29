# EU Funding Playbook — the project's core lens

> Many Romanian ventures are only viable **with non-dilutive EU grants**. This project therefore treats **funding as a first-class design driver**, not an afterthought: you scan the instruments, match a venture to one, and **design the project to score** — then build the application with [`../templates/funding-application.md`](../templates/funding-application.md) and model the co-financing in [`../tools/finsim/`](../tools/finsim/).

> ⚠️ Not legal/financial advice. Figures verified 2026-05 — **always re-confirm against the official Applicant Guide** for the live call. Sources in [`../knowledge/sources.md`](../knowledge/sources.md) and each venture's research.

## Funding-first method (8 steps)
1. **Scan** instruments (catalog below) for ones whose objectives match the venture.
2. **Match** eligibility (entity type, size, sector, location) — be honest.
3. **Time it** — when does the call open/close? (windows are short and often once-a-year).
4. **Design to score** — read the selection criteria and shape the project to win points.
5. **Build the application** — [`funding-application.md`](../templates/funding-application.md).
6. **Model** — put the intensity, cap and co-financing into [finsim](../tools/finsim/) to check it still works.
7. **Submit** on the right platform (MySMIS2021 / AFIR portal / ministry site).
8. **Implement & report** — milestones, indicators, audit trail (grants are reimbursed against eligible, evidenced cost).

## Instrument catalog (Romania, 2026)
| Instrument | Funds | Intensity / cap | Who | Apply via |
|-----------|-------|-----------------|-----|-----------|
| **Modernisation Fund — standalone storage** | battery storage CAPEX | **up to 100%**; **≤€10M/company**; **≤€69k/MWh**; select on **€/MWh** | micro→large, incl. new EU entities | MySMIS2021 / energie.gov.ro [[S31]](../knowledge/sources.md#s31) |
| **CAP–AFIR DR-23** (processing) | agri-product processing & marketing | **65%**; **≤€3M** (≤€10M bakery); €164.9M pot; 15 Dec 2025–16 Feb 2026 | micro→large, co-ops, PFA | AFIR portal [[S32]](../knowledge/sources.md#s32) |
| **CAP–AFIR sM4.1** (irrigation) | on-farm irrigation equipment | **50%** (+20% top-up, ≤90%); **≤€200k** | farms | AFIR portal [[S32]](../knowledge/sources.md#s32) |
| **CAP–AFIR DR-12** (young farmers) | farm setup/development | **80%** (≤40y) / 65%; **≤€200k**; €169.5M | young farmers | AFIR portal [[S32]](../knowledge/sources.md#s32) |
| **CAP–APIA** (direct payments) | per-hectare income support | ~**€250/ha** combined (annual) | active farmers | APIA single application [[S29]](../knowledge/sources.md#s29) |
| **Cohesion 2021–27** (POCIDIF/PODD/POTJ/POR) | SME, R&I, digital, green, regional | varies (often 40–70%) | SMEs, etc. | MySMIS2021 [[S27]](../knowledge/sources.md#s27) |
| **PNRR** | legacy (closing Aug 2026) | — | — | — [[S10]](../knowledge/sources.md#s10) |
| **Horizon Europe / Innovation Fund** | R&I, clean-tech | 60–70% | consortia | EU portals |

(Full funding landscape: [`../knowledge/funding-landscape.md`](../knowledge/funding-landscape.md).)

## Two grant mechanics — don't confuse them
- **Capital/investment grants** (Modernisation Fund, AFIR): reimburse a **% of eligible CAPEX up to a cap** (often paid against invoices). This is what our ventures mostly use.
- **Cost-reimbursement grants** (Horizon-style): reimburse **eligible costs incurred** — equipment enters via **depreciation during the project**, plus a flat-rate **indirect cost** (e.g. 25%). [[S30]](../knowledge/sources.md#s30)

## Design-to-score (the winning move)
- **Modernisation Fund storage:** the *only* criterion is **€/MWh requested** — bid **low to rank**, but not so low the project breaks. Model the trade-off in finsim. [[S31]](../knowledge/sources.md#s31)
- **AFIR DR-23:** points for **priority sector** (trade-balance/food-security), **environment ≤25** (energy efficiency ≤12 + digital ≤13), **co-ops +5** — so bake in efficient cold storage, solar/heat recovery and digital management. [[S32]](../knowledge/sources.md#s32)

## Co-financing, state aid & eligibility rules
- **Co-financing:** you fund the non-grant share (e.g. 35% for AFIR DR-23, 0–any for 100% Modernisation Fund) from equity/debt — size it in finsim.
- **No double funding:** the same cost can't be covered by two EU sources; respect **cumulation** caps (CISAF / GBER / de minimis).
- **VAT** is usually **ineligible** (recover it via ANAF instead); **operating costs** often ineligible in capital grants.
- **Entity must exist** (ONRC-registered) before the first aid payment; keep a clean **audit trail**.

## Common pitfalls
- Missing the **call window**; under-reading the **Applicant Guide**; assuming VAT/operating costs are eligible; bidding an unwinnable €/MWh; ignoring **state-aid cumulation**; weak **indicators**; no proof of **co-financing**.

## Worked mockups ("full funds projects")
- Energy: [`../ventures/energy-storage/funding-application.md`](../ventures/energy-storage/funding-application.md) — Modernisation Fund standalone storage.
- Agriculture: [`../ventures/agriculture-irrigation/funding-application.md`](../ventures/agriculture-irrigation/funding-application.md) — AFIR DR-23 processing (+ sM4.1 irrigation).
