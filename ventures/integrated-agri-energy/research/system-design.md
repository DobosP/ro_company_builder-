# Integrated Agri-Energy System — design & funding map

> The concept: **multiple interlocking projects** that feed each other (solar → storage → pumps → lakes → fish + algae → natural fertiliser → smart greenhouses), **self-consumption first**, where **each module draws its own EU/RO funding stream**. Verified 2026-05; [I#] → [sources](sources.md), [E#]/[A#] → energy/agri venture sources.

## The circular flow (each arrow is a value loop)
```
            ┌──────────────── SOLAR PV (agrivoltaic + floating) ───────────────┐
            │                         │ electricity                            │
            ▼                         ▼                                         │
      BATTERY STORAGE  ──power──►  SOLAR BOREHOLE PUMPS  ──deep water──►  LAKES / PONDS
            │ (self-consume,            │                                  │   │
            │  arbitrage surplus)       │ irrigation                       │   │ water + nutrients
            ▼                          ▼                                   ▼   ▼
       SMART GREENHOUSES ◄──natural fertiliser (fish effluent + algae)── FISH + ALGAE
            │ veg/fruit                                                    │ feed/biomass
            └──────────────────── PRODUCE + PROCESSING (sell) ◄────────────┘
```
**Self-consumption first:** the system powers and feeds itself (own electricity, own water, own fertiliser), then sells the surplus (produce, fish, processed goods, and excess power).

## The modules, their economics, and "cheaper/secondhand/new-tech" options
| Module | What it does | Indicative cost | Cheaper / efficiency option |
|--------|--------------|-----------------|------------------------------|
| **Solar PV** (agrivoltaic + floating on lakes) | generates the system's electricity | ~€637/kWp [E33](../../energy-storage/research/sources.md#e33) | **floating PV** on the lakes (no extra land, cuts evaporation [I8](sources.md#i8)); **second-hand/EoL panels reused** ([circular variant](../../energy-storage/circular-economy-variant.md)) |
| **Battery storage** | stores solar for night/pumps; arbitrage surplus | C&I ~€170–280/kWh [E58](../../energy-storage/research/sources.md#e58) | **second-life EV packs** (~€65–110/kWh) [E61](../../energy-storage/research/sources.md#e61) |
| **Solar borehole pumps** | pump deep groundwater to lakes/irrigation | a few €k–€20k/pump | **MPPT solar pumps >99% eff.**, no diesel/grid [I6](sources.md#i6) |
| **Lakes / ponds** | water storage + fish + algae habitat | earthworks-driven | dual-use **aquavoltaics** (solar over water) [I8](sources.md#i8) |
| **Fish (aquaculture)** | protein revenue + nutrient-rich effluent | part of aquaponics capex | RAS/IMTA; start with hardy species |
| **Algae** | biofertiliser + fish feed + biomass | ~€1.4–2.25/kg [I5](sources.md#i5) | **flat-panel photobioreactors** (3–4× cheaper than raceway) [I5](sources.md#i5) |
| **Smart greenhouses** | high-value veg/fruit, climate-controlled | ~€0.7–1.2M/ha [I4](sources.md#i4) | start with **polytunnels** (Romania-proven, cheap) then automate [I4](sources.md#i4) |
| **Natural fertiliser loop** | fish effluent + algae → greenhouse nutrients | (loop, not a buy) | real value, **but feed-N/P is costly** — supplement, don't fully replace [I3](sources.md#i3) |
| **Processing** | turn produce/fish into shelf-stable goods | ~€4M (see agri) [A13](../../agriculture-irrigation/research/sources.md#a13) | reuse the [agri venture](../../agriculture-irrigation/) design |

## ⭐ The funding insight: one system, many funds (stack them via SPVs)
Each module is eligible for a **different** pot — so structure as a **holding company + per-module SPVs**, each applying separately. This is legitimate (different assets, different objectives) **as long as no single cost is double-funded** (state-aid cumulation rules).

| Module | Funding stream | Intensity | Source |
|--------|----------------|-----------|--------|
| Smart greenhouse + irrigation | **AFIR** (CAP) — incl. €100M irrigation budget | 50–65% | [A13](../../agriculture-irrigation/research/sources.md#a13) [I4](sources.md#i4) |
| Processing | **AFIR DR-23** | 65%, ≤€3M | [A13](../../agriculture-irrigation/research/sources.md#a13) |
| **Fish / aquaculture / lakes** | **EMFAF** (fisheries fund, >€6B) | **≤70%** | [I1](sources.md#i1) |
| Battery storage | **Modernisation Fund** standalone | ≤100%, ≤€69k/MWh | [E41](../../energy-storage/research/sources.md#e41) |
| Solar PV (agrivoltaic/floating) | agrivoltaics law 254/2022; CfD/PNRR-legacy; self-finance | — | [I7](sources.md#i7) |
| Algae / circular / innovation | **LIFE / Horizon / POCIDIF** | 40–70% | [E65](../../energy-storage/research/sources.md#e65) |
| Young-farmer setup | **AFIR DR-12** | 80%, ≤€200k | [A15](../../agriculture-irrigation/research/sources.md#a15) |

→ A multi-million-euro system could be **majority grant-funded** by stacking 4–6 streams, each on its own module. This is the core advantage of the integrated approach.

## Honest reality checks (don't over-promise)
- **Aquaponics is hard & capital-heavy:** profitable typically only **>1,000 m²**, ~2 yrs to profit, revenue **dominated by plant sales** (fish is secondary). [I2](sources.md#i2) Start with the greenhouse+fish loop modest; scale once proven.
- **"Free" natural fertiliser isn't free:** fish-feed nutrients cost **7–88× inorganic** per unit N/P — the loop *reduces* and *greens* fertiliser but won't fully replace it cheaply. [I3](sources.md#i3)
- **Complexity risk:** running solar + storage + pumps + aquaculture + algae + greenhouses + processing at once is **operationally extreme**. **Phase it** (below), don't build all at once.
- **Deep-water pumping** needs an **Apele Române abstraction permit** + sustainability check (over-abstraction risk). [A9](../../agriculture-irrigation/research/sources.md#a9)
- **Grant timing mismatch:** AFIR, EMFAF, Modernisation Fund calls open at different times — sequencing matters.

## Recommended phasing (de-risk + match funding windows)
1. **Phase 1 — Energy + water base:** solar PV (agrivoltaic/floating) + battery + solar borehole pumps + first lake. *Self-consumption foundation.* Funds: Modernisation Fund (battery), self/agrivoltaic (solar).
2. **Phase 2 — Grow:** smart greenhouse (start polytunnel) + irrigation from the lake. Funds: **AFIR**.
3. **Phase 3 — Aquaculture loop:** fish in the lakes + algae + nutrient loop to greenhouse. Funds: **EMFAF** + LIFE/Horizon (algae/innovation).
4. **Phase 4 — Processing + circular:** process produce/fish; optionally reuse/recycle panels & batteries. Funds: **AFIR DR-23** + LIFE.

## Synergy with the existing ventures
This **combines** [energy-storage](../../energy-storage/) (solar+storage, the circular reuse of panels/batteries) and [agriculture-irrigation](../../agriculture-irrigation/) (greenhouse, irrigation, processing) and adds the **fish + algae + funding-stacking** layer. Reuse their research, finsim configs and grant mockups.

## Open research tasks
- [ ] EMFAF Romania managing authority + live aquaculture call terms/intensity. [I1](sources.md#i1)
- [ ] Borehole hydrogeology + Apele Române abstraction limits at the chosen site.
- [ ] Aquaponics species + greenhouse crop mix with the best RO margins.
- [ ] Detailed energy balance (kWp / kWh / pump load) for true self-sufficiency.
- [ ] State-aid cumulation check across the stacked funds (no double-funding).
