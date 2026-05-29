# Open Questions — Verification Register

> This project is **data-driven**: every figure should be sourced and dated. This register tracks what's **verified** and what's still **open**, so gaps stay visible and nothing is silently assumed. When you resolve an item, update the relevant doc + [`sources.md`](sources.md), then move it to "Resolved."

> ⚠️ Re-verify before acting — Romanian law changes fast. "Verified 2026-05" means checked that month.

## Resolved this pass (2026-05)

| # | Question | Answer | Where | Source |
|---|----------|--------|-------|--------|
| R1 | SA minimum share capital 2026? | **RON 90,000** (unchanged; ≥2 shareholders; ≥30% paid at incorporation) | [company-formation](company-formation.md) | [S24](sources.md#s24) |
| R2 | VAT reduced rate(s) 2026? | **Single 11%** (from 1 Aug 2025; replaced 5%/9%); temp **9%** on new homes to 31 Jul 2026 | [taxation](taxation.md) | [S20](sources.md#s20) |
| R3 | VAT registration threshold 2026? | **RON 395,000** (~€80k); small-enterprise exemption below it | [taxation](taxation.md) | [S21](sources.md#s21) |
| R4 | Micro regime — is the 3% tier gone? | **Yes** — single **1%**; ≥1 **full-time** employee; sector limits removed | [taxation](taxation.md) | [S22](sources.md#s22) |
| R5 | CASS on dividends 2026? | Due if non-salary income > **6 min wages (~RON 24,300)**; **10%** of 6/12/24-wage ceiling | [taxation](taxation.md) | [S23](sources.md#s23) |
| R6 | CAEN Rev. 3 for storage / trading? | **3516** storage, **3514** trading, **3511** production (renewable sub-code TBC → O1) | [energy venture](../ventures/energy-storage/) | [E31](../ventures/energy-storage/research/sources.md#e31) |
| R7 | 2026 standalone BESS scheme terms? | Call **Q2 2026**; **€/MWh** bid; cap **€15M/project**; up to **€69k/MWh**; 2,174 MWh; ≤100% eligible | [energy venture](../ventures/energy-storage/) | [E30](../ventures/energy-storage/research/sources.md#e30) |
| R8 | Romania utility solar CAPEX? | **~€600–640/kWp** (Scatec 190 MW ≈ €637/kWp) | [energy venture](../ventures/energy-storage/) | [E33](../ventures/energy-storage/research/sources.md#e33) |
| R9 | ANRE fees for production/storage? | Annual contribution **0.1%** of turnover; modification fee 2,500 lei + 0.1% of investment; full schedule in **Order 93/2024** | [energy venture](../ventures/energy-storage/) | [E32](../ventures/energy-storage/research/sources.md#e32) |

## Still open / newly found

| # | Question | Why it matters | Where to get it |
|---|----------|----------------|-----------------|
| O1 | Exact CAEN Rev. 3 **renewable-production** code (3511 is non-renewable) | correct company object for solar | ONRC CAEN Rev. 3 full structure |
| O2 | ANRE **licence-grant** tariff (exact € for a production/storage licence) | budgeting formation cost | Order 93/2024 table (Monitorul Oficial 1315/2024) |
| O3 | Does a battery beside **new** solar count as standalone or co-located for the grant? | decides grant route (mutually exclusive) | Ministry of Energy scheme guide / ANRE |
| O4 | **Grid-connection headroom by node** (Transelectrica/DSO) | site selection (~60 GW requested vs ~19.6 GW installed → scarce) | Transelectrica capacity maps |
| O5 | **Balancing-price decay** + **solar capture** curves 2026–2032 | revenue realism (60–70% of BESS income) | market analysts / optimisers |
| O6 | Solar **land cost €/ha** + lease terms in target counties | CAPEX/opex input | local land brokers |
| O7 | 2026 **property / local tax** changes | opex for asset-heavy ventures | ANAF / local councils |
| O8 | Min-wage **tax exemption** (was RON 300/200) status in 2026 | payroll modeling | ANAF / payroll guides |
| O9 | Names & live calls of EU **operational programmes** (SME, energy, digital) | funding routes per venture | oportunitati-ue.gov.ro |

> Venture-specific open items also live in each venture's `decision-log.md` and research notes (e.g. [energy storage](../ventures/energy-storage/research/research-notes.md)).
