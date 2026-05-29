# Hard Questions — Battery Energy Storage (Romania)

> Answers to [`../../framework/hard-questions.md`](../../framework/hard-questions.md). Evidence in [research notes](research/research-notes.md); [E#] → [sources](research/sources.md). Verified 2026-05.

## 1. Problem & need
Romania's fast solar/wind growth outpaces grid flexibility → **congestion, curtailment, negative prices**. [E20](research/sources.md#e20) [E21](research/sources.md#e21) Storage shifts energy and sells fast balancing, which the system increasingly needs. **Why now:** generous Modernisation Fund support + strong 2025 spreads (DAM avg €110/MWh, daily spread €168/MWh). [E12](research/sources.md#e12) [E2](research/sources.md#e2)

## 2. Market & demand
- **Who pays:** Transelectrica (balancing) and the wholesale market (arbitrage); offtake often via an optimiser/trader. [E11](research/sources.md#e11)
- **Size:** national target ~1,200 MW by 2030 (talk of ~2,000 MW by end-2026); ~241 MW operational mid-2026 → large headroom. [E1](research/sources.md#e1) [E5](research/sources.md#e5)
- **Competition:** crowded with well-funded players — Nova Power (200 MW/400 MWh), Aukera (250 MW/500 MWh), Toki, R.Power, Electrica, Hidroelectrica. [E7](research/sources.md#e7) [E8](research/sources.md#e8) [E9](research/sources.md#e9) [E19](research/sources.md#e19)
- **Switching/edge:** the binding constraint isn't customers, it's **grid-connection rights + land** and **speed** — see §8.

## 3. Legal structure
- **SRL** (limited liability; capital-intensive asset-co). The **micro 1%** regime is irrelevant (turnover/asset scale) → **CIT 16%** with depreciation. [taxation](../../knowledge/taxation.md)
- Likely a **project SPV per site** for financing/grant ring-fencing.
- **CAEN:** storage operators are "assimilated to producers" [E15](research/sources.md#e15) → likely **3511** + **3514**; *[TODO: verify Rev. 3 code]*.

## 4. Regulation, permits & licensing
- **ANRE establishment authorization** required > **1 MW**. [E13](research/sources.md#e13)
- **Grid connection (ATR)** under **Order 20/2025**: operational limitation + financial guarantees + prioritization. [E14](research/sources.md#e14)
- Guarantee stack ≈ **€20k/MW + €30k/MW + 20% of connection tariff**. [E13](research/sources.md#e13)
- Path: **ATR → ANRE establishment authorization → building permit → ANRE operating licence** (+ environmental). [E13](research/sources.md#e13)
- Storage classified by **Order 27/2025**; capacity allocation by **Order 79/2025**. [E15](research/sources.md#e15)
- See [compliance-checklist.md](compliance-checklist.md).

## 5. Capital & funding
- **Capital-heavy:** a 50 MW / 100 MWh project ≈ **€25–35M** CAPEX (see [financial-model.md](financial-model.md)). Not bootstrappable.
- **Grant:** the **live €150M standalone Modernisation Fund scheme** (EC-approved Mar 2026, CISAF, competitive €/MWh bidding, aid to 2030, newly established entities eligible). [E2](research/sources.md#e2) Co-located route also exists (≤100% eligible cost, max €10M/enterprise, ≥75% absorption rule). [E3](research/sources.md#e3)
- **Mix:** equity + project debt + grant. **PNRR is legacy** (closes Aug 2026). [E4](research/sources.md#e4)
- Defensible asset the money buys: **a connected, permitted, sited MW** — scarce and valuable even if later sold.

## 6. Financial viability
- **Revenue:** balancing 60–70% (aFRR €80–150/MW/day, mFRR €30–60, FCR €40–80) + arbitrage 20–30% (DAM/IDM spreads). [E11](research/sources.md#e11) [E12](research/sources.md#e12)
- **Tax/VAT:** CIT 16%; VAT 21% recoverable on CAPEX (cash-flow timing). [taxation](../../knowledge/taxation.md)
- **Sensitivity:** the model lives or dies on **balancing-price decay** and **cycles/day**; grant intensity and debt terms swing the equity IRR. See [financial-model.md](financial-model.md).

## 7. Team & operations
- Need: development (permitting/grid), engineering/EPC management, and trading/optimisation (likely **outsourced** to an optimiser initially). [E9](research/sources.md#e9)
- O&M can be contracted to the BESS supplier/EPC.
- Week-1 reality is **development & paperwork**, not operations.

## 8. Location & strategic fit
- **The whole game.** Pick nodes with **grid headroom** near RES clusters; the ATR + operational-limitation regime rewards sites with real evacuation capacity. [E13](research/sources.md#e13) [E14](research/sources.md#e14)
- Land control (lease/option) + a clean connection study = the core asset.

## 9. Risks & mitigations
Top risks (full table in [risk-register.md](risk-register.md)):
- **Grid connection denied/limited** → scout multiple nodes early; post guarantees only on the best.
- **Balancing-price saturation** → sign an optimisation/tolling contract; diversify revenue. [E11](research/sources.md#e11)
- **Grant not won** (competitive €/MWh) → have a merchant case that works without grant, or co-located route. [E2](research/sources.md#e2)
- **CAPEX/financing** → fix EPC price; secure debt term sheet before bidding.
- **Crowding/first-mover loss** → speed on site control; or pivot asset-light (sell development rights).

## 10. Impact & theory of change
Not a mission venture, but real system benefit: **less curtailment, fewer negative-price hours, more renewables integrated, grid stability**. [E20](research/sources.md#e20) Worth stating for ESG-linked finance.

## 11. Timeline & milestones
1. Site + grid headroom shortlist (2–3 nodes) — *months 0–3*.
2. Land options + connection solution study + guarantees — *months 2–6*. [E13](research/sources.md#e13)
3. Standalone-scheme bid (when call opens) — *track 2026 date*. [E2](research/sources.md#e2)
4. ANRE establishment authorization + building permit — *months 6–12*.
5. EPC + financing close — *months 9–15*.
6. Build + grid energisation — *months 12–24*.
7. Commercial operation + optimisation contract live.
- **Smallest real step:** secure ONE connection point with a valid solution study — that alone is a sellable asset.
