# Research Notes — Battery Energy Storage in Romania

> Evidence base for this venture. Verified **2026-05**; not investment/legal advice — the market and ANRE rules change fast. Citations [E#] → [`sources.md`](sources.md); reusable Romania facts → [`../../../knowledge/`](../../../knowledge/).

## 1. Why storage, why Romania, why now
- Romania is one of Europe's most active BESS markets in 2025–26. Roughly **240.7 MW / 404.9 MWh** was operational by mid-May 2026, with a national **2030 target of ~1,200 MW** (NIESC/NECP) and government talk of **~2,000 MW by end-2026**. [E1](sources.md#e1) [E5](sources.md#e5)
- Driver: a fast solar/wind build-out is creating **grid congestion, curtailment, and negative prices** — exactly the conditions that make storage (shifting energy and selling flexibility) valuable. [E20](sources.md#e20) [E21](sources.md#e21)
- 2025 wholesale signal: OPCOM **day-ahead average ≈ €110/MWh**, **max daily spread ≈ €168/MWh**, intraday spreads **200–300 €/MWh** — strong arbitrage and balancing economics. [E12](sources.md#e12)

## 2. Funding — a major tailwind (and the live opportunity)
- **Modernisation Fund** is the engine: ~**€300M** earmarked for BESS across two €150M tranches. [E1](sources.md#e1)
  - **Co-located** (behind existing RES), Nov 2024: €150M, up to **100% of eligible cost**, **max €10M per enterprise**, storage must absorb **≥75%** of the connected plant's energy; bids closed 17 Jan 2025. [E3](sources.md#e3)
  - **Standalone**, ranked solely on **requested aid in €/MWh** (lowest wins). [E4](sources.md#e4)
- **⭐ Live now:** in **March 2026** the EC approved a **€150M standalone** scheme for **≥2,174 MWh**, financed by the Modernisation Fund under the **CISAF** state-aid framework, **competitive bidding**, aid disbursed **before 31 Dec 2030**. Eligible: micro/SME/large companies **including newly established EU entities** registered with **ONRC** before the first aid payment. *(No call-opening date published yet — monitor the Ministry of Energy / MIPE.)* [E2](sources.md#e2)
- **PNRR** also funded storage (~€80M → ~1.8 GW targeted; e.g. €30M for 791.48 MWh across 5 projects) — but **PNRR closes Aug 2026**, so treat it as legacy, not a new-applicant route. [E4](sources.md#e4)
- A separate **€150M municipal** program (Nov 2025) adds ~385 MW. [E18](sources.md#e18)

## 3. Regulation & licensing (ANRE) — the gating path
- **ANRE establishment authorization** (*autorizație de înființare*) is required for projects with export capacity **> 1 MW**. [E13](sources.md#e13)
- **Grid connection (ATR — *aviz tehnic de racordare*)** is the bottleneck. **Order 20/2025** (from **1 June 2025**) introduced:
  - **"Operational limitation"** baked into the ATR — the operator can temporarily curtail evacuation to protect the grid. [E14](sources.md#e14)
  - **Financial guarantee** required within ~2 months of the solution study, or the request lapses; **project prioritization** by complete-file registration date — explicitly to kill speculative reservations. [E14](sources.md#e14)
- Guarantee stack (indicative): **€20,000/MW** capacity-allocation + **€30,000/MW** establishment-authorization + **20% of the connection tariff**. [E13](sources.md#e13)
- **Order 27/2025**: standalone storage operators are **"assimilated to producers."** **Order 79/2025**: revised capacity-allocation methodology/auctions. [E15](sources.md#e15)
- End-to-end permits: **grid connection (ATR/ATR certificate) → ANRE establishment authorization → building permit → ANRE operating licence**, plus environmental sign-off. [E13](sources.md#e13)

## 4. Revenue stack
- **Balancing services ≈ 60–70%** of BESS revenue (procured by **Transelectrica** to hold 50 Hz): **aFRR €80–150/MW/day**, **mFRR €30–60/MW/day**, **FCR €40–80/MW/day** (capacity + activated energy). [E11](sources.md#e11)
- **Energy arbitrage ≈ 20–30%** on **OPCOM DAM** (hourly, gate closure 12:00) and **IDM** (continuous, to 5 min before delivery; volatile, larger spreads). [E11](sources.md#e11) [E12](sources.md#e12)
- Route-to-market matters: developers commonly sign **optimisation/tolling agreements** with traders (e.g. GEN-I optimising R.Power's Scornicești). This converts merchant risk into contracted revenue. [E9](sources.md#e9)
- ⚠️ **Saturation risk:** balancing markets are finite — as GW of BESS arrive, aFRR/FCR prices compress. Today's revenue assumptions will erode; model conservatively.

## 5. Competitive landscape (crowded, well-capitalised)
- **Nova Power & Gas** — **200 MW / 400 MWh** operational (Florești, Cluj), largest to date. [E8](sources.md#e8)
- **Aukera (BE)** — **250 MW / 500 MWh** (Gura Ialomiței), online ~mid-2026, biggest announced. [E7](sources.md#e7)
- **Toki Power (Renalfa, AT)** — **150 MW / 300 MWh** standalone. [E19](sources.md#e19)
- **R.Power** Scornicești — **127 MW / 254 MWh** (GEN-I optimised). [E9](sources.md#e9)
- **Electrica** — 15 BESS ~**1 GWh** by 2030; **Hidroelectrica** — storage across hydro/wind (Crucea Nord 36 MW/72 MWh, Porțile de Fier II 64 MW/256 MWh). [E6](sources.md#e6) [E19](sources.md#e19)
- Implication: utilities and international IPPs are moving fast. A new entrant's scarce assets are **grid-connection rights + sited land**, plus speed and a financing/route-to-market edge.

## 6. Economics (orders of magnitude)
- Turnkey BESS ~**$117/kWh** globally in 2025 (−31% YoY); 4h packs outside China/US ≈ **$125/kWh** ($75 equipment + $50 install/connection). [E16](sources.md#e16)
- **Europe 4h LFP ≈ $180–260/kWh installed**; shorter-duration (2h) systems cost **more per kWh** (power electronics spread over fewer kWh). [E17](sources.md#e17)
- **LCOS** for well-sited 4h LFP ~**$65–150/MWh**. [E16](sources.md#e16)
- See [`../financial-model.md`](../financial-model.md) for an illustrative 50 MW / 100 MWh case.

## 7. Open research tasks
- [ ] Exact **CAEN Rev. 3** code(s) for energy storage operation/trading.
- [ ] Current **ANRE licence** thresholds & fees for storage operation (vs the >1 MW establishment-authorization trigger).
- [ ] The **2026 standalone scheme** call-opening date, per-project aid cap, and scoring details (CISAF). [E2](sources.md#e2)
- [ ] Grid-connection availability by node (Transelectrica/DSO capacity maps) — where is headroom?
- [ ] Realistic 2026–2030 **balancing-price decay** curve as capacity scales.
