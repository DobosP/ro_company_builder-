# Financial Model (illustrative) — 50 MW / 100 MWh BESS

> ⚠️ **Orders of magnitude, not a pro forma.** Every figure is an **ASSUMPTION to verify** with an EPC quote, an optimiser's revenue stack, and a debt term sheet. Verified market inputs 2026-05; [E#] → [sources](research/sources.md). Romanian tax from [taxation](../../knowledge/taxation.md).

## Configuration
- **50 MW / 100 MWh** (2-hour) standalone LFP, single SPV (SRL).

## CAPEX
| Item | Basis | Estimate |
|------|-------|----------|
| Installed system cost | Europe 4h LFP ~$180–260/kWh; 2h costs more per kWh → assume **~€280/kWh** | **~€28M** |
| Range | sensitivity | **€25–35M** |

Sources for unit cost: [E16](research/sources.md#e16) [E17](research/sources.md#e17). *(2h vs 4h, grid works, and land swing this materially — verify.)*

## Funding stack (illustrative)
| Source | Assumption | Amount |
|--------|-----------|--------|
| Modernisation Fund grant | competitive €/MWh; assume offsets ~30% (cap/▼ vs co-located max €10M) | **~€8M** [E2](research/sources.md#e2) [E3](research/sources.md#e3) |
| Project debt | ~60% of net CAPEX | **~€12M** |
| Equity | balance | **~€8M** |

> Grant intensity is **the key swing** and is competitive — model a **no-grant** case too. [E2](research/sources.md#e2)

## Revenue (gross, per year)
| Stream | Share | Basis |
|--------|-------|-------|
| Balancing (aFRR/mFRR/FCR) | 60–70% | aFRR €80–150/MW/day etc. [E11](research/sources.md#e11) |
| Arbitrage (DAM/IDM) | 20–30% | 2025 spread €168/MWh; IDM 200–300 [E12](research/sources.md#e12) |

- Illustrative blended **€80–120k/MW/year** in 2026 → **€4–6M/yr** for 50 MW. **ASSUMPTION.**
- ⚠️ **Decay:** assume this **falls over time** as GW of BESS saturate balancing markets. Model a declining curve, not a flat line. [E11](research/sources.md#e11)

## OPEX (per year)
O&M + insurance + augmentation reserve + **optimiser fee (~10–20% of revenue)** + grid charges → **~€0.8–1.5M/yr**. **ASSUMPTION.**

## Tax
- **CIT 16%** on profit (micro 1% not applicable at this scale). [taxation](../../knowledge/taxation.md)
- **VAT 21%** recoverable on CAPEX — but creates a **cash-flow timing** gap to manage.
- Depreciation of the asset shields early profits.

## Headline (rough)
- Net CAPEX after grant ≈ **€20M**; equity ≈ **€8M**.
- EBITDA ≈ revenue − OPEX ≈ **€3–5M/yr** (year 1, pre-decay).
- → simple payback on **total** net CAPEX ~5–7 yrs; equity returns depend on debt terms + grant + revenue decay. **Verify with a real model.**

## Must-verify before committing
- [ ] EPC turnkey quote (€/kWh) for 2h vs 4h at the chosen site.
- [ ] Optimiser revenue projection + fee, ideally a **floor/tolling** offer. [E9](research/sources.md#e9)
- [ ] Grant clearing €/MWh and per-project cap (2026 call). [E2](research/sources.md#e2)
- [ ] Debt term sheet (gearing, rate, tenor).
- [ ] Balancing-price decay curve 2026–2032.
