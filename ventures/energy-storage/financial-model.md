# Financial Model (illustrative) — Hybrid: 50 MW / 100 MWh BESS + 10 MWp solar

> ⚠️ **Orders of magnitude, not a pro forma.** Every figure is an **ASSUMPTION to verify** with EPC quotes, an optimiser's revenue stack, and a debt term sheet. Market inputs verified 2026-05; [E#] → [sources](research/sources.md). Romanian tax from [taxation](../../knowledge/taxation.md).

▶ **Run the numbers:** `python tools/finsim/run.py ventures/energy-storage/finsim.json` → [finsim-report.md](finsim-report.md). Headline (illustrative): **IRR ~5.7%, NPV −€3.9M @10%, payback 2035, min DSCR 1.00x** — **marginal**, highly sensitive to grant size, debt terms and revenue decay.

## Configuration
- **Battery:** 50 MW / 100 MWh (2-hour) LFP.
- **Solar:** ~10 MWp co-located, **AC-coupled**, sharing one grid connection. [E28](research/sources.md#e28)

## CAPEX
| Item | Basis | Estimate |
|------|-------|----------|
| Battery system | Europe 4h LFP ~$180–260/kWh; 2h higher per kWh → ~€280/kWh | **~€28M** [E16](research/sources.md#e16) [E17](research/sources.md#e17) |
| Solar park (10 MWp) | RO ~€637/kWp (Scatec 190 MW) | **~€6.4M** [E33](research/sources.md#e33) |
| Shared connection saving | one connection/substation vs two | **−€0.5–1M** [E28](research/sources.md#e28) |
| **Combined** | range €30–42M | **~€34M** |

## Funding stack (illustrative)
| Source | Assumption | Amount |
|--------|-----------|--------|
| Modernisation Fund grant | competitive €/MWh; **standalone** route caps **€15M/project**, up to **€69k/MWh** | **~€8M** [E30](research/sources.md#e30) |
| Project debt | ~60% of net CAPEX | **~€15M** |
| Equity | balance | **~€10M** |

> The **grant route choice** is strategic: co-located = ≤100% eligible cost but ≥75% solar-absorption rule + €10M cap (constrains arbitrage); standalone = battery free (cap €15M/project, ≤€69k/MWh), solar separate. **Model both; verify eligibility.** [E30](research/sources.md#e30) [E3](research/sources.md#e3)

## Revenue (gross, per year — year 1, pre-decay)
| Stream | Basis | Estimate |
|--------|-------|----------|
| Battery — balancing (aFRR/mFRR/FCR) | 60–70%; aFRR €80–150/MW/day | part of €4–6M [E11](research/sources.md#e11) |
| Battery — arbitrage (DAM/IDM) | 20–30%; 2025 spread €168/MWh | part of €4–6M [E12](research/sources.md#e12) |
| **Battery subtotal** | ~€80–120k/MW/yr (declining) | **€4–6M** |
| Solar generation | ~13 GWh/yr × captured ~€60–90/MWh | **€0.8–1.2M** [E22](research/sources.md#e22) |
| **Combined** | | **~€5–7M** |

⚠️ **Decay:** model balancing **and** solar-capture prices **falling** over time as capacity scales; the battery partly offsets solar cannibalization (charges cheap midday, sells peak). [E11](research/sources.md#e11) [E23](research/sources.md#e23)

## OPEX (per year)
O&M + insurance + augmentation reserve + **optimiser fee (~10–20% of battery revenue)** + grid charges + minimal solar O&M → **~€1.0–1.8M/yr**. **ASSUMPTION.**

## Tax
- **CIT 16%** on profit (micro 1% not applicable at this scale). [taxation](../../knowledge/taxation.md)
- **VAT 21%** recoverable on CAPEX — manage the cash-flow timing gap.
- Asset depreciation shields early profits.

## Headline (rough)
- Net CAPEX after grant ≈ **€25M**; equity ≈ **€10M**.
- EBITDA ≈ revenue − OPEX ≈ **€3.5–5.5M/yr** (year 1).
- → simple payback on **total** net CAPEX ~5–7 yrs; equity returns depend on grant route, debt terms and price decay. **Verify with a real model.**
- **Hybrid upside vs standalone:** cheaper charging, capture-price uplift, shared-connection savings, lower merchant risk → easier financing. [E23](research/sources.md#e23) [E24](research/sources.md#e24)

## Must-verify before committing
- [ ] Hybrid EPC quote (AC vs DC coupling) for battery + 10 MWp solar. [E28](research/sources.md#e28)
- [ ] Grant route decision + eligibility (standalone vs co-located, new-build solar). [E2](research/sources.md#e2) [E3](research/sources.md#e3)
- [ ] Optimiser revenue projection + fee + any floor/tolling. [E9](research/sources.md#e9)
- [ ] Debt term sheet (gearing, rate, tenor).
- [ ] Balancing-price decay + solar capture-price curves 2026–2032.
- [ ] Solar **land cost €/ha** + lease terms (CAPEX ~€637/kWp now confirmed). [E33](research/sources.md#e33)
