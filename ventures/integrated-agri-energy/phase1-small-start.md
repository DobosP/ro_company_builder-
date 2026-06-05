# Phase 1 — Small Start (own land, low labour, free engineer)

> Your concrete starting point: **own land**, a **small greenhouse + irrigation**, a **pond growing algae/protein-plant → biofertiliser** for the greenhouse, **small solar + second-hand batteries**, a **free electrical engineer**, minimal labour, and a high-margin crop. This is the realistic Phase-1 entry to the [integrated system](research/system-design.md). Verified 2026-05; [I#] → [sources](research/sources.md).

## 🎯 The grant that fits "start small": AFIR DR-14 (small farms)
- **Up to €75,000 per project** (raised from €50k), **85% non-refundable** — you fund only ~15% + ineligible costs. **€108M** budget, sessions from **27 Feb 2026**. [I9](research/sources.md#i9)
- Why it's right for you: small scale, **flat-rate/lump-sum** style, light on co-financing and admin — **manageable solo**. Covers farm modernisation incl. greenhouse, irrigation, equipment, and on-farm renewables.
- **Other small options to stack later** (not all at once): **DR-12** young farmers (€200k, 80%) if you qualify; **AFIR sM4.1** irrigation (50%, ≤€200k); a small **Modernisation Fund / national PV** scheme for the solar. Keep Phase 1 to **one clean DR-14 application**. See [funding-stack.md](funding-stack.md).

## The "protein plant" you're thinking of
Two pond options — they do different jobs:
| Plant | Best for | Reality |
|-------|----------|---------|
| **Spirulina** (cyanobacteria) | **protein** (sells high; **20× protein/ha vs soy**) [I10](research/sources.md#i10) | needs **warm water + pH/temperature control** → hard outdoors in a RO winter; better *inside* the heated greenhouse in tanks; manual farms rarely profit. [I10](research/sources.md#i10) |
| **Duckweed (Lemna)** ⭐ | **biofertiliser + animal feed** | **hardy**, grows on diluted effluent, ~27–40% protein, up to **28.5 g/m²/day**, doubles in days — the **easy pond plant** for your fertiliser loop. [I11](research/sources.md#i11) |

**Recommendation:** start the **outdoor pond with duckweed** (robust, low-effort) for the **biofertiliser loop** [I12](research/sources.md#i12); add **spirulina in tanks inside the greenhouse** later if you want a protein cash crop (it likes the warmth you're already paying for).

## ⚠️ Heating the greenhouse through a Romanian winter — honest math
This is the hard part, and electricity alone won't do it cheaply:
- A mid-size greenhouse needs **~15–30 kWh/day** of heat in winter; 2–3 days autonomy = a **30–80 kWh battery**. [I14](research/sources.md#i14) That's a *lot* of second-hand battery and solar (winter sun is weak).
- **So don't rely on electric heat.** Use **passive solar + thermal mass** as the primary defence: **black water barrels** in the sun path, an **insulated north wall**, double glazing, and the **pond itself as thermal mass**. This holds **+15–20°F (≈ +8–11°C) overnight** for ~zero running cost. [I13](research/sources.md#i13)
- Use **solar + second-hand batteries** for **frost protection + circulation pumps + snow-melt on the roof + lights**, not bulk heating. Size the battery to the *frost-protection* load, not full heating.
- **Net:** treat winter as **season-extension** (grow into late autumn / early spring, protect from frost) rather than tropical year-round — far cheaper and matches "manageable with less effort."

## High-margin crop (for the solar-heated space)
Best €/m² for a small grower (low labour, premium price): **specialty herbs** (Thai/purple basil), **microgreens**, **leafy greens** (21–30-day cycles → fast cash), or **tomatoes** (up to 55 kg/m²). [I15](research/sources.md#i15) **Microgreens/herbs** give the most value per m² and per hour of effort — ideal to start. Spirulina (if added) is a second premium line.

## "Cheaper / second-hand / new-tech" levers (you asked)
- **Solar:** second-hand/EoL panels (reuse) — see [circular variant](../energy-storage/circular-economy-variant.md); **MPPT controllers >99%** efficient. [I6](research/sources.md#i6)
- **Batteries:** **second-life EV/C&I packs** (~€65–110/kWh) — your engineer can integrate the BMS for free. [E61](../energy-storage/research/sources.md#e61)
- **Heat:** thermal mass (barrels/pond) = free; **passive first**. [I13](research/sources.md#i13)
- **Fertiliser:** duckweed/algae from the pond → cuts bought fertiliser. [I12](research/sources.md#i12)
- **Greenhouse:** start as an **insulated polytunnel**, automate later.

## Low-labour design (no full employee at first)
- **Automate the fiddly bits:** drip irrigation on a timer, sensors/thermostat for the fans/frost heater, automatic vents. Capital (grant-funded) replaces labour.
- **Choose low-touch crops** (herbs/greens/duckweed) over labour-intensive ones (saffron, fish).
- **Defer fish** (aquaculture is the highest-effort, highest-regulation layer — EMFAF phase later).
- Your **free electrical engineer** covers the solar/battery/controls build — a real cost saving; log it as in-kind.

## Indicative Phase-1 budget (own land, ~€80–120k project)
| Item | Indicative | Note |
|------|-----------|------|
| Polytunnel/greenhouse (~500–1,000 m²) + thermal mass | €25–45k | passive-solar design [I13](research/sources.md#i13) |
| Drip irrigation + controls (automation) | €8–15k | low-labour |
| Pond (duckweed) + liner + circulation | €5–12k | biofertiliser loop |
| Small solar (~10–20 kWp) + second-hand batteries | €15–30k | engineer = free labour |
| Frost heater + snow-melt + sensors | €5–10k | size to frost, not bulk heat |
| Spirulina tanks (optional, indoor) | €5–15k | protein cash crop, later |
| **Total** | **~€80–120k** | **~85% via DR-14 → your cash ~€12–30k** [I9](research/sources.md#i9) |

→ Run it: [finsim-phase1-small.json](finsim-phase1-small.json) → [report](finsim-phase1-small-report.md). Headline (micro 1% regime, ~€100k project / €75k grant / €30k cash): **IRR ~25%, payback 2032, break-even 2029** — a viable small business.

> ⚠️ **Grant cash-flow timing:** DR-14 (like most grants) **reimburses *after* you spend** — finsim shows a **−€54k mid-point dip**, i.e. you must **bridge ~€50–55k** (your cash or a short bridge loan) between paying suppliers and receiving the grant. Budget this; it's the #1 practical trap for small grant projects.

> 💡 **Tax regime:** stay on **micro (1% on revenue)** while turnover ≤ €100k with ≥1 employee — cheaper than CIT here (NPV €93k vs €81k). You're below the **VAT threshold (RON 395k)** too, so VAT-exempt is simplest at the start. [taxation](../../knowledge/taxation.md)

## Permits (small scale — lighter, but check)
- **APIA** registration; **DR-14** application. [I9](research/sources.md#i9)
- **Pond + water:** small ponds may need an **Apele Române** notification/permit; deep borehole abstraction does. [A9](../agriculture-irrigation/research/sources.md#a9)
- **Solar <1 MW:** licence-exempt (self-consumption). [E26](../energy-storage/research/sources.md#e26)
- **Spirulina/algae for sale as food/feed:** ANSVSA + Novel Food rules (fine as biofertiliser/own-use). [I5](research/sources.md#i5)

## Next actions
- [ ] Confirm **DR-14** eligibility + the Feb 2026 session guide (exact eligible costs). [I9](research/sources.md#i9)
- [ ] Pick the **crop** (herbs/microgreens to start) + **pond plant** (duckweed first).
- [ ] Have your engineer spec the **frost-protection** load → size solar + second-hand battery to *that*.
- [ ] Design the greenhouse **passive-solar** (orientation, thermal mass, insulated north wall). [I13](research/sources.md#i13)
