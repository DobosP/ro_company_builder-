# Risk Register — Hybrid Solar-plus-Storage (Romania)

> L (likelihood) and I (impact): 1–5. Score = L × I. Verified 2026-05. [E#] → [sources](research/sources.md).

| # | Risk | Category | L | I | Score | Early-warning signal | Mitigation |
|---|------|----------|:-:|:-:|:-----:|----------------------|------------|
| 1 | Grid connection denied or heavily **operationally limited** | regulatory | 4 | 5 | 20 | low headroom in node study; ATR caveats [E14](research/sources.md#e14) | scout 2–3 nodes; guarantees only on the best; favour high-capacity substations |
| 2 | **Balancing-price saturation** erodes 60–70% of battery revenue | market | 4 | 4 | 16 | falling aFRR/FCR clearing prices [E11](research/sources.md#e11) | optimisation/tolling floor; diversify; conservative decay curve |
| 3 | **Grant-route misfit** (standalone vs co-located eligibility) | financing | 3 | 4 | 12 | scheme rules exclude new-build solar co-location [E2](research/sources.md#e2) [E3](research/sources.md#e3) | model both routes early; confirm eligibility before posting guarantees |
| 4 | **CAPEX / financing** overrun or no debt | financing | 3 | 4 | 12 | EPC quote > model; tight credit | fix hybrid EPC price; debt term sheet before bidding |
| 5 | **Crowding** — best sites taken first | execution | 4 | 3 | 12 | rivals announcing same counties [E7](research/sources.md#e7) [E24](research/sources.md#e24) | speed on land+connection; or pivot **asset-light** (sell development rights) |
| 6 | **Solar capture-price cannibalization** | market | 4 | 2 | 8 | rising midday solar, more negative hours [E23](research/sources.md#e23) | battery shifts solar to peak; PPA for part of output |
| 7 | **Solar land / agri-permitting** blocked | regulatory | 3 | 3 | 9 | only Class I–III land available; PUZ needed [E27](research/sources.md#e27) | target Class III–V, <50 ha (no PUZ); agrivoltaic grassland option |
| 8 | Permitting/build **delay** | execution | 3 | 3 | 9 | slow ANRE/building permit | experienced local developer/lawyer; realistic schedule |
| 9 | Tech **degradation/augmentation** cost | technology | 2 | 3 | 6 | capacity fade > warranty | supplier warranty; augmentation reserve in OPEX |

> **Net effect of going hybrid:** adds land/permit + solar-cannibalization risks (#6, #7) but **reduces** overall merchant risk and improves financeability vs standalone. [E23](research/sources.md#e23) [E24](research/sources.md#e24)

## Single biggest assumption
We can **secure a connection-advantaged site with suitable land**, pick the **right grant route**, and **balancing + solar-capture revenue holds** long enough to repay the asset.

## Kill criteria
- [ ] No node with real evacuation headroom + viable land after scouting → stop or go asset-light.
- [ ] Neither grant route fits the hybrid, **and** the no-grant case is below hurdle.
- [ ] No optimiser willing to offer a revenue floor.
