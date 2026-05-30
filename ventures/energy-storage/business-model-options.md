# Business-Model Options — can an EnergoBit-style "schema" make this more profitable?

> Your question: *could I use a model like theirs (EnergoBit) to profit from my energy venture?* **Yes — and the analysis says an asset-light model beats owning the battery for a new entrant.** Verified 2026-05; [E#] → [sources](research/sources.md). finsim runs are illustrative — replace with real quotes/sale comps.

## What EnergoBit's "schema" actually is
EnergoBit is **asset-light**: it **engineers, builds and services** energy infrastructure (substations, T&D lines, SCADA, grid automation, MV switchgear) **for** DSOs/TSOs and private clients — it **earns execution margins (~8–12%)**, it does **not own** the generation/storage asset or take merchant/price risk. [E55](research/sources.md#e55) [E56](research/sources.md#e56) (That's why VINCI bought it — a scalable, capital-light services franchise.)

Our Suceava plan, by contrast, is **IPP** (asset-heavy): own the €28M battery, earn arbitrage+balancing, carry all the market risk → **IRR ~3.8%** ([finsim-suceava](finsim-suceava-report.md)). High EBITDA margin (80%+) but huge capital and thin returns. [E56](research/sources.md#e56)

## The four ways to make money from this venture
| Model | What you do | Capital | Return profile | finsim |
|-------|-------------|---------|----------------|--------|
| **A. IPP (own asset)** | own + operate the battery | **very high** (~€28M) | low IRR (~3.8%), recurring | [finsim-suceava](finsim-suceava-report.md) |
| **B. Asset-light developer** ⭐ | secure **grid connection + permits + land**, sell the **ready-to-build** project | **low** (~€1–2M) | **very high IRR**, lumpy | [finsim-developer](finsim-developer-report.md) |
| **C. EPC / services** (EnergoBit's own model) | build/integrate/SCADA **for** owners | low–med (working capital) | ~8–12% margin, recurring [E56](research/sources.md#e56) | — |
| **D. Optimisation / O&M-as-a-service** | trade & maintain others' batteries for a fee | low | fee per MW + uplift share | — |

## ⭐ The winner for a new entrant: B (develop-and-sell)
This is a **live, proven market in Romania right now**: R.Power is **selling a ready-to-build 200 MW/400 MWh** BESS; Repono **bought 202 MW/404 MWh** in Argeș. Projects with **secured grid connection + permits** command strong investor demand. [E57](research/sources.md#e57) It monetises **exactly the scarce asset we identified all along — the grid connection** — *without* the €28M CAPEX or merchant risk.

finsim ([finsim-developer.json](finsim-developer.json) → [report](finsim-developer-report.md)):
**IRR ~127%, NPV +€7.1M @12%, payback 2028, on ~€1.2M equity** (sell ready-to-build rights as you secure each node). vs IPP's **−€4.7M NPV on €10M equity**. *(Sale value per MW is an assumption — confirm with broker comps; the −€316k yr-1 dip = working capital before the first sale.)*

## Why this fits *you* specifically
- It plays to the real bottleneck (grid headroom at the reinforced **Suceava 400/110** node + Delgaz [E42](research/sources.md#e42)) — securing an **ATR + permits** is the value, and you can sell it.
- **Low capital, fast cash, repeatable** across multiple Suceava/NE nodes.
- Uses **EnergoBit/Electrogrup as EPC partners** (you sell to an investor; they build it) rather than competing with them. [E51](research/sources.md#e51) [E53](research/sources.md#e53)
- It's the **asset-light fallback** we flagged in the very first energy decision — the data now says make it the **primary** strategy.

## Recommended schema (hybrid of B + optionality)
1. **Develop** connection rights + permits + land at 1–3 Suceava/NE nodes (the [site work](site-suceava-ilisesti.md)).
2. **Apply for the Modernisation Fund grant** in the SPV (a grant-awarded, permitted project is worth more). [funding-application.md](funding-application.md)
3. **Then choose per project:** **sell ready-to-build** (bank the IRR now, model B) **or** keep one and co-build with an EPC partner + optimiser if you want recurring IPP income (model A). You're not locked in.
4. Optionally add **C/D** later (offer development/optimisation services to other owners) — that *is* the EnergoBit playbook applied to BESS.

## Caveats (be honest)
- Model B income is **lumpy** (per-sale), needs **working capital** to carry development before the first exit, and depends on **sale comps** that vary — verify with a broker.
- You must still **win the grid connection** (Order 20/2025 guarantees) — that's the real work and the real risk.
- EPC/services (C) means competing with EnergoBit/Electrogrup/VINCI — hard for a newcomer; **partner, don't compete**.

## Next actions
- [ ] Get **ready-to-build sale comps** (€/MW) from a RO BESS broker/M&A advisor to firm up model B revenue. [E57](research/sources.md#e57)
- [ ] Re-run [finsim-developer.json](finsim-developer.json) with real comps + development cost (ATR guarantees ~€20k+€30k/MW). [E13](research/sources.md#e13)
- [ ] Decide the **default exit** (sell vs hold) per node before committing development capital.
