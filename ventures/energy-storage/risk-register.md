# Risk Register — Battery Energy Storage (Romania)

> L (likelihood) and I (impact): 1–5. Score = L × I. Verified 2026-05. [E#] → [sources](research/sources.md).

| # | Risk | Category | L | I | Score | Early-warning signal | Mitigation |
|---|------|----------|:-:|:-:|:-----:|----------------------|------------|
| 1 | Grid connection denied or heavily **operationally limited** | regulatory | 4 | 5 | 20 | low headroom in node study; ATR caveats [E14](research/sources.md#e14) | scout 2–3 nodes; commit guarantees only on the best; favour high-capacity substations |
| 2 | **Balancing-price saturation** erodes 60–70% of revenue | market | 4 | 4 | 16 | falling aFRR/FCR clearing prices [E11](research/sources.md#e11) | optimisation/tolling floor; diversify to arbitrage; conservative decay curve |
| 3 | **Grant not won** (competitive €/MWh) | financing | 3 | 4 | 12 | aggressive rival bids [E2](research/sources.md#e2) | viable no-grant case; co-located route; phase project |
| 4 | **CAPEX / financing** overrun or no debt | financing | 3 | 4 | 12 | EPC quote > model; tight credit | fix EPC price; debt term sheet before bidding |
| 5 | **Crowding** — best sites taken first | execution | 4 | 3 | 12 | competitors announcing same counties [E7](research/sources.md#e7) [E8](research/sources.md#e8) | speed on land+connection; or pivot **asset-light** (sell development rights) |
| 6 | Permitting/build **delay** | execution | 3 | 3 | 9 | slow ANRE/building permit | experienced local developer/lawyer; realistic schedule |
| 7 | Tech **degradation/augmentation** cost | technology | 2 | 3 | 6 | capacity fade > warranty | supplier warranty; augmentation reserve in OPEX |

## Single biggest assumption
We can **secure a connection-advantaged site** and that **balancing revenue holds** long enough to repay the asset.

## Kill criteria
- [ ] No node with real evacuation headroom after scouting → stop or go asset-light.
- [ ] No-grant case IRR below hurdle **and** grant not won.
- [ ] No optimiser willing to offer a revenue floor.
