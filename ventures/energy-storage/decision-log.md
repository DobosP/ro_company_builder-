# Decision Log — Battery Energy Storage (Romania)

> Append-only; newest on top. [E#] → [sources](research/sources.md).

---

## 2026-05-29 — Grant corrected to €6.0M (scheme cap) → IRR 4.1%; + funding-application mockup
- **Correction:** the earlier €8M grant exceeded the scheme cap. The Modernisation Fund pays **≤€69k/MWh** → a 100 MWh battery maxes at ~€6.9M; a competitive **€60k/MWh bid = €6.0M**. [E41](research/sources.md#e41)
- **Updated finsim:** IRR **4.1%**, NPV **−€5.8M** @10%, payback 2036, min DSCR 1.00x — **clearly sub-hurdle**. Leans even harder on a keener **€/MWh bid**, a **revenue floor (tolling)** and **cheaper debt**.
- **Added** [funding-application.md](funding-application.md) — full Modernisation Fund standalone-storage mockup. (Supersedes the 5.7% figure below, which used the too-high €8M grant.)

---

## 2026-05-29 — finsim run: hybrid is marginal at base assumptions (IRR ~5.7%)
- **Result:** project **IRR ~5.7%**, **NPV −€3.9M** at a 10% hurdle, **payback 2035**, **min DSCR 1.00x** (tight), at the illustrative €34.4M CAPEX / €8M grant / €15M debt. See [finsim-report.md](finsim-report.md) (`python tools/finsim/run.py ventures/energy-storage/finsim.json`).
- **Read:** below a 10% equity hurdle → the deal needs a **bigger grant** (the scheme allows up to €69k/MWh, cap €15M), **cheaper debt**, or a **revenue floor** (tolling) so balancing income doesn't decay. Min DSCR 1.00x means the debt is sized to the limit.
- **Action:** treat grant size + a contracted revenue floor as make-or-break; re-run finsim per scenario. [E30](research/sources.md#e30) [E37](research/sources.md#e37)

---

## 2026-05-29 — Extend to hybrid: add ~10 MWp co-located solar (rubric 85 → 88/115)
- **Decision:** evolve from standalone BESS to a **hybrid** — 50 MW/100 MWh battery + ~10 MWp co-located solar sharing one grid connection (AC-coupled).
- **Why:** the market is shifting to hybrids; co-location improves capture price, gives the battery cheap midday/negative-price charging, and **shares the scarce grid connection** across two revenue streams, easing financing. [E23](research/sources.md#e23) [E24](research/sources.md#e24) [E28](research/sources.md#e28)
- **Grant nuance (open):** the battery can bid the **standalone** scheme *or* go **co-located behind-the-meter** (≤100% eligible cost, €10M cap, ≥75% solar-absorption) — likely **not both** for the same asset; verify before bidding. [E2](research/sources.md#e2) [E3](research/sources.md#e3)
- **Rubric impact:** financial viability 3→4 (de-risked, shared connection) → **total 88/115**.
- **Follow-ups:** land scouting (avoid Class I–III; <50 ha Class III–V skips PUZ); hybrid EPC quote (AC vs DC coupling); confirm grant route. [E27](research/sources.md#e27)

---

## 2026-05-29 — Initial rubric score: 85/115 ("promising→strong")
Using [`../../framework/evaluation-rubric.md`](../../framework/evaluation-rubric.md):

| Dim (weight) | Rating | Score | Why |
|---|:-:|:-:|---|
| Problem intensity (3) | 5 | 15 | RES congestion/negative prices, clear why-now [E20](research/sources.md#e20) |
| Market size & demand (3) | 5 | 15 | 1,200–2,000 MW target, ~241 MW live [E1](research/sources.md#e1) |
| Financial viability (3) | 3 | 9 | works but merchant + saturation risk [E11](research/sources.md#e11) |
| Fundability (2) | 5 | 10 | live €150M standalone scheme [E2](research/sources.md#e2) |
| Regulatory feasibility (2) | 3 | 6 | clear but demanding ATR/guarantees [E13](research/sources.md#e13) |
| Team/execution fit (3) | 2 | 6 | **weak spot** — capital + dev expertise needed |
| Defensibility (2) | 4 | 8 | connection rights + site = real moat |
| Impact (2) | 3 | 6 | genuine system benefit, not mission |
| Location fit (1) | 4 | 4 | strong if node chosen well |
| Risk profile (2) | 3 | 6 | several material risks |
| **Total** | | **85** | proceed to model + secure a site |

No dimension scores 1 (no fatal cap). **Action:** close the team/execution gap (partner with a developer/optimiser; line up capital).

---

## 2026-05-29 — Strategic entry: pursue a connection-advantaged mid-size project, keep an asset-light fallback
- **Decision:** target one **50 MW/100 MWh** site with grid headroom and bid the **standalone Modernisation Fund** scheme; if sites/capital are scarce, pivot **asset-light** (secure connection + land + permits, then sell/partner the development rights).
- **Options considered:** (A) utility-scale IPP — high capital, crowded; (B) C&I/behind-the-meter — less capital, smaller; (C) asset-light development rights — lowest capital, sells the scarce asset.
- **Reasoning:** the scarce, valuable asset is a **connected, permitted, sited MW** [E13](research/sources.md#e13) [E14](research/sources.md#e14); pursuing it works for both A and C, so it's the no-regret first move.
- **Follow-ups:** node scouting; 2026 call terms [E2](research/sources.md#e2); optimiser conversations [E9](research/sources.md#e9); EPC + debt indications.

---

## Template entry (copy above)
