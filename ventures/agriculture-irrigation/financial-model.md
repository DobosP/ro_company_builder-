# Financial Model (illustrative) — Integrated 200 ha + Processing

> ⚠️ **Orders of magnitude, not a pro forma.** Every figure is an **ASSUMPTION to verify** (crop margins, grant intensity, water/energy cost, offtake prices). Inputs verified 2026-05; [A#] → [sources](research/sources.md). RO tax from [taxation](../../knowledge/taxation.md).

▶ **Run the numbers:** `python tools/finsim/run.py ventures/agriculture-irrigation/finsim.json` → [finsim-report.md](finsim-report.md).

## Configuration
- **~200 ha** irrigated production + a **processing line + cold storage**; phased (processing first).

## CAPEX (illustrative)
| Item | Basis | Estimate |
|------|-------|----------|
| Irrigation (200 ha, drip + pumping) | ~€3,000/ha (subsidised) [A8](research/sources.md#a8) | €0.6M |
| Processing line + cold storage | mid-size unit | €4.0M |
| Land (200 ha @ ~€8.5k) | [A8](research/sources.md#a8); R14 | €1.7M |
| **Total** | | **~€6.3M** |

## Funding stack (illustrative)
| Source | Assumption | Amount |
|--------|-----------|--------|
| AFIR DR-23 processing grant | competitive; ~part of €164.9M call | **~€2.0M** [A5](research/sources.md#a5) |
| AFIR irrigation subsidy | up to ~$540k/farm | **~€0.3M** [A2](research/sources.md#a2) |
| Project debt | annuity, 7%, 8y | **~€2.5M** |
| Equity | balance | **~€1.5M** |

## Revenue (illustrative, per year)
| Stream | Basis | Year 1 |
|--------|-------|--------|
| Processed products | import substitution; ramps | €2.0M (+8%/yr) |
| Fresh / raw sales | surplus crop | €0.6M (+3%/yr) |
| **APIA** direct payments | ~€250/ha × 200 ha | **€50k** (stable floor) [A4](research/sources.md#a4) |

## Costs
Variable ≈ **45% of revenue** (seeds, inputs, packaging, raw material); fixed ~€0.5M (energy, water, maintenance, logistics); payroll (farm + plant + management). Margins are thin — the model leans on **grants + APIA + processing value-add**.

## Tax
- **CIT 16%** (turnover ≫ €100k → micro ineligible). VAT: **food is 11%** reduced band. [taxation](../../knowledge/taxation.md)
- Local/property tax on the processing building (ANEVAR value) — add to opex. [taxation](../../knowledge/taxation.md)

## Headline
See the generated [finsim-report.md](finsim-report.md). Expect a **grant-dependent, thin-margin** profile where APIA + AFIR shift the payback materially — the decision hinges on **crop margins, water reliability and grant intensity**.

## Must-verify before committing
- [ ] Crop + processing **gross margins** (the 45% variable assumption).
- [ ] **AFIR grant intensity / cap** (drives the funding stack).
- [ ] **Water** reliability + abstraction cost under drought. [A9](research/sources.md#a9)
- [ ] Offtake prices / contracts; energy cost for cold storage.
- [ ] Land **buy vs lease** (lease cuts CAPEX sharply).
