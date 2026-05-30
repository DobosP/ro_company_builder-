# Small Start — what €100K buys (latest tech, 2026)

> Your question: *start small with €100K — how much energy can I store at most with the latest innovations?* Verified 2026-05; [E#] → [sources](research/sources.md). finsim figures illustrative.

## The headline number
At **€100K total budget**, in the C&I ("all-in-one cabinet") class:

| Chemistry / route | Installed €/kWh (2026) | **kWh for ~€100K** | Notes |
|---|---|---|---|
| **LFP turnkey** (battery+PCS+cooling+BMS+fire) | ~€170–280/kWh [E58](research/sources.md#e58) | **~360–580 kWh** of kit | the safe default |
| LFP, after ~€20–30k for siting/connection/install | — | **~300–450 kWh** usable project | realistic all-in |
| **Second-life EV** batteries | ~€65–110/kWh [E61](research/sources.md#e61) | **~600–900 kWh** | cheapest kWh, higher integration/warranty risk |
| **Sodium-ion** (newest) | ~near LFP at small scale in 2026 [E60](research/sources.md#e60) | similar to LFP | longer life/safety; not yet cheaper turnkey small |

**Practical answer: ~300–450 kWh** of new LFP as a turnkey project (e.g. **one or two 100 kW / 215–233 kWh cabinets** [E62](research/sources.md#e62)), or **up to ~0.6–0.9 MWh** if you go second-life. So think **a few hundred kWh**, not MWh.

## Why these numbers (the latest innovations)
- **Battery prices hit record lows in 2025:** LFP packs **$81/kWh**, stationary-storage LFP **~$70/kWh** (cheapest cells/packs $36/$50). [E59](research/sources.md#e59) That's *cells/packs* — your **turnkey** cost is higher (PCS, cooling, fire, EMS, install) → ~€170–280/kWh. [E58](research/sources.md#e58)
- **Sodium-ion** arrived commercially in 2026 (CATL Naxtra etc.) at near-LFP cost with very long life — great for the *future*, but **not yet meaningfully cheaper than LFP at €100K scale**. [E60](research/sources.md#e60)
- **Second-life EV** packs are the cheapest €/kWh today (30–70% off) — the way to maximise raw kWh on a tight budget, at the cost of more integration work and shorter/uncertain warranty. [E61](research/sources.md#e61)

## ⚠️ The strategic reality at this scale
A few-hundred-kWh battery **cannot play the wholesale/balancing markets** (those need ~1 MW+ and an ANRE licence; sub-1 MW is licence-exempt — see [E26](research/sources.md#e26)). So the €100K profit model is **different from the utility plan**:
- ❌ Not: grid arbitrage / aFRR (too small).
- ✅ **Behind-the-meter for a business** (peak-shaving, demand-charge reduction, solar self-consumption, backup) — for your own site or a host's.
- ✅ A **pilot / proof-of-concept** to build a track record before scaling.

## How €100K actually makes money (pick one)
1. **Behind-the-meter at a commercial host** — install at a factory/farm/cold-store with high power bills; earn from **peak-shaving + self-consumption** (and resilience). Pair with the **agri venture's cold storage** (a natural host!). 
2. **Seed capital for the asset-light developer** — €100K comfortably funds **early development** (land options, a connection study, ANRE guarantees for *one* node) → then **sell the ready-to-build project** (see [business-model-options.md](business-model-options.md), finsim IRR ~127%). **This is the best use of €100K** — it doesn't buy a meaningful battery, but it *controls* a grid connection worth far more.
3. **Small commercial pilot** to learn the tech + permitting, then raise/grant-fund the big one.

## finsim — a €100K behind-the-meter pilot
[finsim-small-100k.json](finsim-small-100k.json) → [report](finsim-small-100k-report.md): a ~**400 kWh** LFP cabinet doing peak-shaving/self-consumption for a commercial host. Returns are modest and **depend entirely on the host's tariff & peak charges** — it's a **learning/asset play**, not a wealth engine at this size.

## Recommendation
**Don't spend €100K on a small battery to chase the IPP dream — it's too small to play the markets.** Two better moves:
- **Best:** use the €100K as **development seed capital** for the **asset-light develop-and-sell** model (control a Suceava grid node, sell it on). [business-model-options.md](business-model-options.md)
- **Or:** a **behind-the-meter pilot** at a real commercial host (ideally your own agri cold-store) to prove the tech and economics cheaply.

## Next actions
- [ ] Decide: **development seed** (asset-light) vs **behind-the-meter pilot**.
- [ ] If pilot: find a host site with high **peak demand charges**; get a turnkey 100 kW/215 kWh cabinet quote. [E62](research/sources.md#e62)
- [ ] If seed: scope the cheapest path to *one* secured connection + permit at the Suceava node. [site-suceava-ilisesti.md](site-suceava-ilisesti.md)
