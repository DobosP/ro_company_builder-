# Open Questions — Verification Register

> This project is **data-driven**: every figure should be sourced and dated. This register tracks what's **verified** and what's still **open**, so gaps stay visible and nothing is silently assumed. When you resolve an item, update the relevant doc + [`sources.md`](sources.md), then move it here to "Resolved."

> ⚠️ Re-verify before acting — Romanian law changes fast. "Verified 2026-05" means checked that month. `[S#]` → [`sources.md`](sources.md); `[E#]` → the [energy venture sources](../ventures/energy-storage/research/sources.md).

## Resolved (verified 2026-05)

| # | Question | Answer | Where | Source |
|---|----------|--------|-------|--------|
| R1 | SA minimum share capital? | **RON 90,000** (unchanged; ≥2 shareholders; ≥30% paid at incorporation) | [company-formation](company-formation.md) | [S24](sources.md#s24) |
| R2 | VAT reduced rate(s)? | **Single 11%** (from 1 Aug 2025; replaced 5%/9%); temp **9%** on new homes to 31 Jul 2026 | [taxation](taxation.md) | [S20](sources.md#s20) |
| R3 | VAT registration threshold? | **RON 395,000** (~€80k); small-enterprise exemption below it | [taxation](taxation.md) | [S21](sources.md#s21) |
| R4 | Micro regime — 3% tier gone? | **Yes** — single **1%**; ≥1 **full-time** employee; sector limits removed | [taxation](taxation.md) | [S22](sources.md#s22) |
| R5 | CASS on dividends? | Due if non-salary income > **6 min wages (~RON 24,300)**; **10%** of 6/12/24-wage ceiling | [taxation](taxation.md) | [S23](sources.md#s23) |
| R6 | CAEN Rev. 3 energy codes? | Group 351: **3511** non-ren prod, **3512** renewable prod, **3513** transmission, **3514** distribution, **3515** trading, **3516** storage → venture uses **3512 + 3516 + 3515** | [energy venture](../ventures/energy-storage/) | [E35](../ventures/energy-storage/research/sources.md#e35) |
| R7 | 2026 standalone BESS scheme terms? | Call **Q2 2026**; **€/MWh** bid; cap **€15M/project**; up to **€69k/MWh**; 2,174 MWh; ≤100% eligible | [energy venture](../ventures/energy-storage/) | [E30](../ventures/energy-storage/research/sources.md#e30) |
| R8 | Romania utility solar CAPEX? | **~€637/kWp** (Scatec 190 MW) | [energy venture](../ventures/energy-storage/) | [E33](../ventures/energy-storage/research/sources.md#e33) |
| R9 | ANRE fees (production/storage)? | Annual **0.1%** of turnover; **7,500 lei/yr** contribution for a new licence; grant tariffs in **Order 93/2024** Table 1 | [energy venture](../ventures/energy-storage/) | [E32](../ventures/energy-storage/research/sources.md#e32) |
| R10 | Min-wage tax exemption 2026? | **Reduced, not removed:** RON **300** (H1) → **200** (H2) exempt | [taxation](taxation.md) | [S26](sources.md#s26) |
| R11 | Property/local tax changes 2026? | Non-residential building tax **0.2–1.3%** on **ANEVAR market value**; broad increase (EO 7/2026) | [taxation](taxation.md) | [S25](sources.md#s25) |
| R12 | EU operational programmes? | **POCIDIF** ~€2.14B, **PODD** ~€13.62B, **POTJ** ~€1.77B, **POR** regional; ~€100B total incl. CAP | [funding-landscape](funding-landscape.md) | [S27](sources.md#s27) [S28](sources.md#s28) |
| R13 | Grid-connection headroom? | Transelectrica **interactive map**, 10 zones A–J; ~**10,530 MW** available 2025 → 11,500 MW 2030 (aggregate, not per-substation) | [energy venture](../ventures/energy-storage/) | [E36](../ventures/energy-storage/research/sources.md#e36) |
| R14 | Solar/agri land cost? | Buy **~€8,000–9,000/ha** (2025); lease below DE's €2.7–4.4k/ha/yr | [energy venture](../ventures/energy-storage/) | [E40](../ventures/energy-storage/research/sources.md#e40) |
| R15 | BESS revenue & decay? | ~**€140/kW/yr** now; **+4 GW** by 2030 will compress aFRR/FCR; solar cannibalization risk **~30% by 2030** in saturated markets | [energy venture](../ventures/energy-storage/) | [E37](../ventures/energy-storage/research/sources.md#e37) [E39](../ventures/energy-storage/research/sources.md#e39) |
| R16 | CAP / APIA / AFIR funding (venture #2)? | **CAP PNS 2023–27 €15.83B**; APIA ~€250/ha; **AFIR DR-23 processing €164.9M** (Dec 2025), DR-12 €169.5M; irrigation up to ~$540k/farm | [funding-landscape](funding-landscape.md), [agri venture](../ventures/agriculture-irrigation/) | [A3](../ventures/agriculture-irrigation/research/sources.md#a3) [A5](../ventures/agriculture-irrigation/research/sources.md#a5) |
| R17 | AFIR grant intensity & caps? | **DR-23 65%, ≤€3M** (≤€10M bakery); **sM4.1 irrigation 50%, ≤€200k**; **DR-12 80%/65%, ≤€200k** | [funding playbook](../framework/eu-funding-playbook.md) | [S32](sources.md#s32) |
| R18 | Modernisation Fund storage grant cap? | **≤100% of CAPEX**, **≤€69k/MWh**, **≤€10M/company**; select on €/MWh (an earlier draft said €15M/project) | [funding playbook](../framework/eu-funding-playbook.md) | [S31](sources.md#s31) |

## Still open / newly found

| # | Question | Why it matters | Where to get it |
|---|----------|----------------|-----------------|
| O1 | Exact **one-off ANRE licence-grant tariff** (Order 93/2024 Table 1) | precise formation cost | Order 93/2024 full table (Monitorul Oficial 1315/2024) |
| O2 | Definitive **standalone vs co-located** treatment of a battery beside *new* solar | decides the (mutually exclusive) grant route | Ministry of Energy scheme **applicant guide** |
| O3 | **Per-substation** grid headroom (not just the 10 aggregate zones) | precise siting | Transelectrica node query / DSO |
| O4 | **Year-by-year** balancing-price decay + solar capture curve 2026–2032 | revenue realism | paid analyst model (Modo / Aurora / Clean Horizon) |
| O5 | Exact Romania **solar lease €/ha/yr** | opex input | local land brokers / MADR Order 13/2025 |
| O6 | **Property-tax revaluation** impact modelled per venture | asset-heavy opex | ANEVAR valuer + local council rate |
| O7 | Crop + processing **gross margins** (irrigated veg vs cereals) | agri venture viability (drives finsim) | farm-management data / USAMV studies |
| O8 | **Water availability / abstraction terms** under drought | the binding enabler for irrigation | Apele Române / ANIF, per county |

> Venture-specific open items also live in each venture's `decision-log.md` and research notes.
