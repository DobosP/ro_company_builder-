# Site Assessment — Suceava / Ilișești (standalone BESS)

> A concrete siting option for the energy venture: a **standalone battery** near Suceava's grid, on cheap extravilan land. Verified 2026-05; [E#] → [sources](research/sources.md). Grid headroom and specific parcels need **local verification** (flagged below).

## Why standalone storage here (not the hybrid)
North Romania (Bucovina) has **weak solar** (~1,000–1,300 kWh/m²/yr vs ~1,650 in the SE) [E47](research/sources.md#e47), so co-located solar makes little sense in Suceava. A **standalone battery** is **resource-agnostic**, has a **tiny footprint** (~1–2 ha), and is exactly what the **Modernisation Fund standalone scheme** funds — so localizing here cleanly simplifies the venture to storage-only. See [funding-application.md](funding-application.md).

## Grid — the binding asset (strong here)
- **Transelectrica "Suceava" 400/220/110/20 kV substation** (TTB Bacău) is the county's high-capacity node. [E42](research/sources.md#e42)
- It's being **reinforced**: the **400 kV Gădălin–Suceava** ring line + **Suceava–Bălți** (Moldova interconnector) + a **2nd 400/110 kV transformer** + reactive compensation. [E42](research/sources.md#e42) A battery rides this reinforcement and the new cross-border balancing flows.
- **DSO = Delgaz Grid** (E.ON) for Suceava; connect at **110 kV / MV** via Delgaz (ATR, Order ANRE 59/2013; online request + cost estimator). [E43](research/sources.md#e43)
- **Regional precedent:** Premier Energy is building a **200 MW BESS near Iași** (~€75M) in the same NE/Delgaz region — proving large BESS connects and finances here. [E45](research/sources.md#e45)
- ⚠️ **Verify per-node headroom** (register O3/O4): the spare MW at the Suceava 400/110 station and at Delgaz MV nodes near Ilișești must be confirmed with a **connection request** — the #1 next action.

## Location options
| Option | Pros | Cons |
|--------|------|------|
| **At/near the Suceava 400/110 node** (E, toward Suceava city) | strongest tie, highest capacity | land nearer the city slightly dearer |
| **Ilișești commune** (DN17, ~20 km W of Suceava) [E46](research/sources.md#e46) | cheap fields, DN17 access, equidistant Suceava/Gura Humorului | ~20 km from the big station → connect via local Delgaz MV/110 (check capacity) |

## Land — cheap, small footprint, easy to buy
- A 50 MW/100 MWh battery needs only **~1–2 ha**. Suceava **extravilan** land is cheap (~€2.5–8/m²; lower for plain arable) → **~€0.05–0.15M** total — trivial vs ~€28M CAPEX. [E44](research/sources.md#e44)
- Target: **flat extravilan outside the village**, near an MV line, good road access; a willing **single owner** of a low-value plot ("easy to budge"). Avoid forest/intravilan; lower land classes ease change-of-use.

## Access & connectivity
On **DN17 (E58)**, recently rehabilitated Suceava–Gura Humorului; fixed + wireless internet present (SCADA/telemetry feasible). [E46](research/sources.md#e46)

## Permitting path (this site)
1. **Delgaz connection request → ATR** (110 kV/MV) + financial guarantees (Order 20/2025). [E43](research/sources.md#e43)
2. **ANRE establishment authorization** (>1 MW) + operating licence.
3. **Building permit** via **Primăria Ilișești** (or the relevant commune) + environmental screening.
4. Land option/purchase; OCPI registration.

## Numbers (this site)
Standalone Suceava config (no solar, cheap land) — [finsim-suceava.json](finsim-suceava.json) → [finsim-suceava-report.md](finsim-suceava-report.md):
**IRR ~3.8%, NPV −€4.7M @10%, payback 2036, min DSCR 0.93x** (€28.1M CAPEX / €6.0M grant / €10M equity).
→ **Good site, marginal merchant economics** at a 10% hurdle (same project-level reality as the hybrid). Levers: a **winning €/MWh grant bid**, a **tolling/floor** for balancing revenue, and **cheaper capital**. Node-specific balancing value (reinforced Suceava + Moldova flows) is **upside** to confirm with an optimiser.

## Next actions (local verification — beyond desk research)
- [ ] **Delgaz connection cost-estimator + formal ATR request** for a node near Ilișești/Suceava → real MW headroom + connection cost. [E43](research/sources.md#e43)
- [ ] **Parcel search** (OCPI / local agents) for ~1–2 ha flat extravilan near an MV line. [E44](research/sources.md#e44)
- [ ] Confirm **Suceava 400/110 station** spare capacity with Transelectrica (TTB Bacău). [E42](research/sources.md#e42)
