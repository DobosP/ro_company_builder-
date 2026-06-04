# Hard Questions — Integrated Agri-Energy System (Romania)

> Answers to [`../../framework/hard-questions.md`](../../framework/hard-questions.md). Evidence in [system design](research/system-design.md); [I#] → [sources](research/sources.md). Verified 2026-05.

## 1. Problem & need
A conventional farm pays for **energy, water, fertiliser and feed** — all costly, often imported, volatile. This system **produces its own** and sells the surplus, cutting exposure on all four while substituting imports. **Why now:** each loop has a live grant + RO enables agrivoltaics/aquaculture. [I1](research/sources.md#i1) [I7](research/sources.md#i7)

## 2. Market & demand
- **Self-consumption first** (internal savings), then sell veg/fruit (import substitution [A7](../agriculture-irrigation/research/sources.md#a7)), fish, algae products, processed goods, surplus power.
- Fish + greenhouse veg + algae biofertiliser all have RO/EU demand; revenue is **dominated by plant/produce sales** in aquaponics. [I2](research/sources.md#i2)

## 3. Legal structure
- **HoldCo SRL + per-module SPVs** to stack funding cleanly (see [funding-stack.md](funding-stack.md)).
- CAEN spans farming/aquaculture/energy/processing — *[TODO: verify Rev. 3]*. CIT regime at scale.

## 4. Regulation, permits & licensing
- **AFIR/APIA** (farm + greenhouse + irrigation), **EMFAF** authority (aquaculture), **Apele Române** (deep-water abstraction — sustainability check), **ANSVSA** (fish + food processing), **ANRE/Delgaz** (solar+storage grid), **Environmental** permits for lakes/earthworks. [A9](../agriculture-irrigation/research/sources.md#a9) [A10](../agriculture-irrigation/research/sources.md#a10) [I7](research/sources.md#i7)

## 5. Capital & funding ⭐
- Multi-million system, but **stack 4–6 funds** (AFIR, EMFAF ≤70%, Modernisation Fund, agrivoltaics, LIFE) → majority grant-funded, **~€2–4M equity** on a €5–10M build. The funding-stacking is the whole point. [funding-stack.md](funding-stack.md)
- **Cheaper/secondhand/new-tech levers:** floating PV + **second-life panels/batteries** [E61](../energy-storage/research/sources.md#e61); **MPPT solar pumps** (>99% eff.) [I6](research/sources.md#i6); **flat-panel photobioreactors** (3–4× cheaper algae) [I5](research/sources.md#i5); start greenhouses as **polytunnels** then automate. [I4](research/sources.md#i4)

## 6. Financial viability
- Each module must **stand on its own** post-grant; the loops add savings + resilience on top.
- ⚠️ Aquaponics profitable typically **>1,000 m²**, ~2 yrs to profit [I2](research/sources.md#i2); "free" fertiliser costs **7–88× inorganic** per nutrient — supplement, don't fully replace. [I3](research/sources.md#i3)
- Run the phased model: [finsim.json](finsim.json) → [finsim-report.md](finsim-report.md).

## 7. Team & operations
- **The hardest part.** Solar+storage, pumping, aquaculture, algae, greenhouses, processing each need expertise → **phase it**, hire/partner per layer, automate (smart sensors). Add a **grant manager** for 6 SPVs × grants.

## 8. Location & strategic fit
- One site that has it all: **fertile irrigable land + groundwater + high sun + grid node** → southern/SE plain (overlaps [agri](../agriculture-irrigation/) siting). Lakes enable floating PV + aquavoltaics. [I7](research/sources.md#i7) [I8](research/sources.md#i8)

## 9. Risks & mitigations
- **Complexity** → strict **phasing** (energy/water → greenhouse → fish/algae → processing).
- **Groundwater over-abstraction** → hydrogeology study + Apele Române limits. [A9](../agriculture-irrigation/research/sources.md#a9)
- **Grant timing mismatch / double-funding** → per-SPV call calendar + consultant. [funding-stack.md](funding-stack.md)
- **Aquaponics underperformance** → start small, prove the loop before scaling.

## 10. Impact & theory of change
Strong: food + energy + water self-sufficiency, import substitution, circular nutrients, renewable power, rural jobs — excellent ESG/grant narrative (and it's *why* the funds exist).

## 11. Timeline & milestones (phased)
1. **Phase 1** solar + storage + solar pumps + first lake (self-consumption base) — Modernisation Fund + agrivoltaic.
2. **Phase 2** smart greenhouse + irrigation — AFIR.
3. **Phase 3** fish + algae + nutrient loop — EMFAF + LIFE.
4. **Phase 4** processing + circular reuse — AFIR DR-23 + LIFE.
- **Smallest real step:** Phase 1 energy+water base on one plot — already useful and grant-funded.
