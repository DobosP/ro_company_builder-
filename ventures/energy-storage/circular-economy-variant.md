# Circular-Economy Variant — reuse + recycle as the core

> Your question: *how much money to develop/implement a project where **second-life batteries + end-of-life solar panels are reused and recycled** as the core business?* Verified 2026-05; [E#] → [sources](research/sources.md). finsim illustrative. **This is a different venture from the storage IPP** — circular-economy manufacturing/recycling — so it gets its own sizing here and may deserve its own `ventures/` folder later.

## What "the core is reuse + recycle" actually means
Three distinct activities — decide which you do (they have very different capital needs):
1. **Reuse / repurpose** — collect retired EV/industrial batteries → **test, grade (SoH), repackage, add a BMS** → resell as cheap stationary storage. [E67](research/sources.md#e67)
2. **Recycle** — shred/process **end-of-life solar panels** (and dead battery cells) → recover glass, aluminium, silicon, copper, lithium. [E64](research/sources.md#e64)
3. **Both** (a "circular hub") — reuse what still works, recycle what doesn't.

Reuse is **light assembly/electronics**; recycling is **heavy industrial processing**. Money needed differs ~10×.

## How much money — three realistic tiers

| Tier | Scope | Indicative all-in CAPEX | What it is |
|------|-------|--------------------------|------------|
| **A. Micro workshop** (reuse only) | diagnostic/testing gear, BMS integration, repackaging, small premises | **~€150k–500k** | a battery-refurb workshop; buy retired packs, grade, rebuild, resell [E63](research/sources.md#e63) [E67](research/sources.md#e67) |
| **B. SME reuse line + light panel handling** | semi-automated test/repack line, collection logistics, WEEE compliance, larger unit | **~€1–4M** | a real repurposing factory (Voltfang-class started ~€15M to reach 1 GWh) [E63](research/sources.md#e63) |
| **C. Industrial recycling plant** (panels and/or cells) | shredding/delamination/recovery line, 5–10k t/yr, permits | **~€10–25M+** | ROSI raised **>€20M** for 10,000 t/yr; PRISM 8,400 t/yr [E64](research/sources.md#e64) |

**Direct answer:**
- To **start small (reuse core):** **~€150k–500k** gets a working battery-refurbishment workshop. Your **€100K is just below comfortable** — feasible as a bare-bones micro-pilot if you host in existing premises and buy testing gear second-hand, but ~€250k+ is more realistic.
- To run a **real reuse SME:** **~€1–4M**.
- To run a **recycling plant:** **~€10–25M+** (grant/investor territory).

## Operating economics (the reuse model)
- Repurposing cost ~**$12/kWh at pack level, $25–49/kWh at module level**. [E63](research/sources.md#e63)
- It's **profitable when your repurposed cost is < ~60% of a new battery**, break-even < ~80%. [E67](research/sources.md#e67) With new LFP turnkey ~€170–280/kWh, your **target sell price ~€100–170/kWh** with input packs cheap/free — achievable, but margins hinge on **cheap input supply + low grading/BMS cost**.
- Biggest risks: **input sourcing** (retired packs), **grading accuracy/safety**, **a fit-for-purpose BMS**, and **warranty/liability** on used cells. [E67](research/sources.md#e67)

## ⚠️ Romania regulatory layer (WEEE / EPR) — new cost & opportunity
Recycling/handling EoL panels & batteries pulls you into **WEEE/EPR**:
- EPR schemes **relicensed from 1 Jan 2025**, **min 5% market share**, certified by the **Environmental Fund**. [E66](research/sources.md#e66)
- Producers placing PV/batteries must **finance their collection & recycling**; missing targets = **RON 2/kg (~€0.4/kg)** penalty. [E66](research/sources.md#e66)
- **Opportunity:** those obligations mean producers/importers will **pay you** to take and recycle their EoL panels/batteries — a built-in revenue stream (gate fees + recovered materials + EPR compliance services).
- **ANSPDCP not relevant; key authorities = Environmental Fund Administration, ANPM (environmental permits), ANSVSA n/a.**

## Funding — this is the strong part (very grant-friendly)
Circular economy + clean-tech is squarely in the EU's priorities:
- **LIFE 2025 — Circular Economy** sub-programme (battery collection/recycling). [E65](research/sources.md#e65)
- **Innovation Fund** (had a €1B battery call) — for innovative recycling/manufacturing. [E65](research/sources.md#e65)
- **Cohesion POCIDIF / PODD** (SME, green) + national de-minimis — see [funding playbook](../../framework/eu-funding-playbook.md).
- These often fund **40–70%** → a €1–4M reuse line could need only **~€0.5–2M equity/debt** after grant.

## finsim — a Tier-A reuse micro-workshop (~€350K CAPEX)
[finsim-circular.json](finsim-circular.json) → [report](finsim-circular-report.md): buy retired packs, refurbish, resell + EPR/gate-fee income, ~50% grant. With a **realistic 3-year sales ramp** and adequate equity: **IRR ~30.7%, NPV +€573k @12%, payback 2030** — a viable small business. ⚠️ But an earlier, under-funded run showed a **−€417k financing gap**: a refurb business is **working-capital-hungry** (you buy inventory before you sell), so budget **CAPEX (~€350k) + working capital (~€150–300k)**. Returns hinge on **cheap input packs, throughput ramp, and resale price** — it's an **operating business**, not a passive asset.

## How this relates to your other ventures (synergy)
- **Cheap storage feedstock:** refurbished packs can supply the **behind-the-meter / agri cold-store** battery cheaply.
- **Closes the loop** on the energy + solar ventures (their EoL panels/batteries become your input).
- Strong **ESG / impact** story for grants and partners.

## Recommendation
- If you want **reuse as the core** and to **start small:** plan for **~€250k–500k** (not €100K) for a credible Tier-A workshop; **lead with a LIFE/POCIDIF grant application** to cover 40–70%.
- **Recycling** (panels) is a **€10M+ industrial** play — pursue only with serious grant/investor backing (and it pairs with EPR contracts).
- **Best first step:** a **reuse workshop** (Tier A) that *also* signs **EPR take-back contracts** — low capital, grant-eligible, and feeds your storage ventures.

## Next actions
- [ ] Decide scope: **reuse-only (A/B)** vs **recycling (C)**.
- [ ] Confirm **retired-pack supply** (EV dealers, fleets, importers) and **EPR take-back** demand. [E66](research/sources.md#e66)
- [ ] Map the live **LIFE / POCIDIF / Innovation Fund** call + intensity. [E65](research/sources.md#e65)
- [ ] If serious, spin up a dedicated `ventures/circular-batteries-solar/` workspace.
