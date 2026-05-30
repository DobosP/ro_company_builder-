# Decision Log — Battery Energy Storage (Romania)

> Append-only; newest on top. [E#] → [sources](research/sources.md).

---

## 2026-05-29 — €100K small-start sizing: a few hundred kWh, so use it as dev seed (not an IPP)
- **How much storage?** At C&I turnkey LFP ~€170–280/kWh, €100K ≈ **~300–450 kWh** (one or two 100 kW/215 kWh cabinets); **~0.6–0.9 MWh** with second-life EV packs. [E58](research/sources.md#e58) [E61](research/sources.md#e61) [E62](research/sources.md#e62) Latest tech: LFP at record lows (stationary ~$70/kWh pack [E59](research/sources.md#e59)); sodium-ion arrived 2026 but not yet cheaper turnkey at this scale. [E60](research/sources.md#e60)
- **Reality:** a few-hundred-kWh battery is **sub-1 MW** → can't play wholesale/balancing markets; only **behind-the-meter** (peak-shaving/self-consumption) works. A €100K BTM pilot models IRR ~16%, ~5-yr payback — fine but small ([finsim-small-100k](finsim-small-100k-report.md)).
- **Decision:** **don't buy a small battery to chase the IPP dream.** Best use of €100K = **development seed capital** for the asset-light develop-and-sell model (control a Suceava grid node, sell ready-to-build). Alternative: a BTM pilot at the agri cold-store. See [small-start-100k.md](small-start-100k.md).

---

## 2026-05-29 — Reconsider the business model: asset-light "develop-and-sell" beats IPP
- **Trigger:** can we use EnergoBit's *schema* to profit? EnergoBit is **asset-light** (EPC/SCADA services, ~8–12% margin, no asset ownership). [E55](research/sources.md#e55) [E56](research/sources.md#e56)
- **Finding:** for a new entrant the strongest analogue is **asset-light development** — secure **grid connection + permits**, sell the **ready-to-build** project (live in RO: R.Power selling 200MW/400MWh, Repono buying 202MW/404MWh). [E57](research/sources.md#e57)
- **finsim:** develop-and-sell → **IRR ~127%, NPV +€7.1M on ~€1.2M equity** ([finsim-developer](finsim-developer-report.md)) vs IPP **−€4.7M NPV on €10M** ([finsim-suceava](finsim-suceava-report.md)). Monetises the scarce asset (grid) without €28M CAPEX or merchant risk.
- **Decision:** make **asset-light develop-and-sell the primary strategy** (with optionality to keep+co-build a node as IPP); use EnergoBit/Electrogrup as **EPC partners to the buyer**, not competitors. Full analysis: [business-model-options.md](business-model-options.md).
- **Next:** get ready-to-build **€/MW sale comps** from a RO BESS broker; re-run finsim-developer with real comps + ATR-guarantee development costs.

---

## 2026-05-29 — Add a Cluj EPC partner (EnergoBit / Electrogrup) to de-risk delivery
- **Decision:** integrate a **Cluj-Napoca smart-grid EPC** for the Suceava BESS — shortlist **EnergoBit** (substations/SCADA/grid; now VINCI Energies) and **Electrogrup** (PV+BESS+grid connection) for competitive budgetary quotes; keep trading/optimisation with a separate market optimiser. [E51](research/sources.md#e51) [E52](research/sources.md#e52) [E53](research/sources.md#e53)
- **Why:** fills the venture's weakest rubric dimension (team/execution); yields a **real CAPEX quote** (replacing the €280/kWh assumption) and a **credible delivery partner** for the grant application. See [partners.md](partners.md).
- **Workflow:** adds a reusable **"partners / ecosystem"** step to the venture method (template + hard-questions §7).
- **Next:** request EPC + grid-connection + SCADA quotes from both → feed [finsim-suceava.json](finsim-suceava.json) and the [funding-application.md](funding-application.md).

---

## 2026-05-29 — Arbitrage ("buy day / sell night") assessed: viable core, but stack balancing
- **Strategy:** charge midday (negative/cheap solar) → discharge evening peak (~€198/MWh) / morning. Romania's spread is huge, and **ANRE removed BESS double taxation (Jul 2025)** — energy stored→reinjected is exempt from transmission/distribution/system fees → arbitrage now pays. [E48](research/sources.md#e48) [E49](research/sources.md#e49)
- **Numbers:** arbitrage-only ~€3.0M/yr → **finsim IRR −7.9%, never pays back** vs the stacked +3.8% (pure arbitrage ~5–7% IRR is "unbankable alone"). [E50](research/sources.md#e50) See [arbitrage-strategy.md](arbitrage-strategy.md) + [finsim-suceava-arbitrage.json](finsim-suceava-arbitrage.json).
- **Decision:** make arbitrage the **core** of a **stacked** strategy (arbitrage + aFRR/FCR + intraday) via an **optimiser/tolling** with a revenue floor; don't rely on arbitrage alone. Green angle: charging midday = storing surplus renewables (no own-solar needed in weak-sun Suceava).
- **Next:** get an optimiser's stacked-revenue projection (incl. a floor) to replace the generic €4.5M assumption.

---

## 2026-05-29 — Site selected: Suceava / Ilișești (standalone battery)
- **Decision:** localize to **Suceava county / Ilișești** (DN17) as a **standalone battery** (drop solar — Bucovina sun is weak [E47](research/sources.md#e47)). Connect to the **reinforced Suceava 400/110 kV** node (Gădălin ring + Moldova interconnector) via **Delgaz Grid**; regional precedent = Premier Energy's 200 MW BESS near Iași. [E42](research/sources.md#e42) [E43](research/sources.md#e43) [E45](research/sources.md#e45)
- **Land:** ~1–2 ha cheap extravilan (~€2.5–8/m²) — trivial vs CAPEX; a willing single-owner plot near an MV line. [E44](research/sources.md#e44)
- **Economics:** [finsim-suceava.json](finsim-suceava.json) → IRR **3.8%**, NPV −€4.7M @10%, min DSCR 0.93x — **good site, marginal merchant economics**; hinges on a winning €/MWh bid + a tolling/floor + cheaper capital. Node-specific balancing value (reinforcement + Moldova flows) is upside to confirm.
- **Next:** Delgaz ATR/connection-cost request (real node headroom — O3/O4); parcel search; confirm Suceava station capacity with Transelectrica. See [site-suceava-ilisesti.md](site-suceava-ilisesti.md).

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
