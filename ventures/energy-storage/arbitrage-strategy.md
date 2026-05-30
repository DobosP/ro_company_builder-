# Buy-Day / Sell-Night — Arbitrage Strategy

> Your question: *"buy during the day, sell at night/morning when prices are higher — can that be profitable?"* Short answer: **yes, it's real and Romania is ideal for it — but make it the core of a *stacked* strategy, not the only revenue.** Verified 2026-05; [E#] → [sources](research/sources.md).

## 1. The opportunity is huge in Romania
The daily price shape is exactly what arbitrage wants:
- **Midday (11:00–16:00): negative / very low** prices — solar floods the grid (DAM has gone to **−€6.18/MWh**). [E48](research/sources.md#e48)
- **Evening peak (20:00–21:00): ~€198/MWh** — sun gone, demand high. [E48](research/sources.md#e48)
- 2025 DAM avg €110/MWh, **max daily spread €168/MWh**, intraday spreads 200–300 €/MWh. [E12](research/sources.md#e12)

So: **charge midday (cheap, even paid to take it), discharge into the evening — and the morning ramp.**

## 2. 🔑 The rule change that makes it pay (July 2025)
Until mid-2025 you'd pay grid fees **twice** (charging *and* discharging), which killed arbitrage. **ANRE ended that double taxation:** energy drawn → stored → reinjected is now **exempt from transmission (extraction), distribution and system-service fees**, with **no green-certificate** purchase. Only the **round-trip losses** (~10–15%) pay normal tariffs. [E49](research/sources.md#e49) This is the single biggest reason your plan is now viable.

## 3. "Green production" — you don't need your own panels here
Charging **midday** *is* buying **surplus renewable** power (the grid is solar-saturated and cheap/negative then), and releasing it at the evening peak. That's genuinely green **time-shifting** — the core climate value of storage. In Suceava the **sun is weak** [E47](research/sources.md#e47), so own-solar is marginal; **buying cheap midday green power is the better route** (and exactly your idea).

## 4. The mechanics & economics
- **Round-trip efficiency** ~85–90% → you sell back ~85% of what you store. [E50](research/sources.md#e50)
- **Cycles** ~**1.4/day** (1,500–1,800 full-cycle hours/yr) for a 2-hour battery. [E50](research/sources.md#e50)
- **Net captured spread** ~**€60/MWh** long-run average → ~**€70k/MW** from arbitrage. [E50](research/sources.md#e50)
- For our 50 MW / 100 MWh: ~**€3.0M/yr** of pure arbitrage (declining as more batteries compete). [E37](research/sources.md#e37)

## 5. ⚠️ The honest catch — arbitrage *alone* is thin
Pure arbitrage yields only ~**5–7% IRR**; standalone-arbitrage projects are "**unbankable**" on their own in 2025. [E50](research/sources.md#e50) The profitable batteries **stack** revenue:
**day-ahead arbitrage + intraday + aFRR + FCR + mFRR + capacity** — via an optimiser/trader. Balancing is ~60–70% of revenue today. [E11](research/sources.md#e11) By **2030**, arbitrage's share is expected to **grow** (frequency markets saturate) — so your instinct is where the market is heading, but **today you need the stack**. [E50](research/sources.md#e50)

## 6. Numbers (finsim)
| Scenario | Battery revenue (yr 1) | Result |
|----------|------------------------|--------|
| **Arbitrage-only** ([config](finsim-suceava-arbitrage.json) → [report](finsim-suceava-arbitrage-report.md)) | ~€3.0M | **IRR −7.9%, never pays back** (unviable alone) |
| **Stacked** (arbitrage + balancing) ([report](finsim-suceava-report.md)) | ~€4.5M | IRR ~3.8% — still marginal |

→ Even *stacked* is marginal at today's battery CAPEX; **arbitrage-only is clearly insufficient by itself.** The strategy is right; the revenue mix and capital cost decide profitability.

## 7. How to actually make it profitable
1. **Stack balancing on top of arbitrage** — sign an **optimiser/tolling** deal (the GEN-I/R.Power model) so a trader maximises arbitrage + aFRR/FCR and ideally gives a **revenue floor**. [E9](research/sources.md#e9)
2. **Bank the tax exemption** — charge cheap midday under the no-double-tax rule. [E49](research/sources.md#e49)
3. **Bid keenly for the grant** — a winning €/MWh Modernisation Fund bid cuts net CAPEX. [E41](research/sources.md#e41)
4. **Ride the tailwinds** — 15-min settlement (+~14% arbitrage) and widening spreads as solar grows. [E50](research/sources.md#e50)
5. **Cheaper CAPEX/capital** — battery prices keep falling (~−31% in 2025); a 4-hour system captures more spread. [E16](research/sources.md#e16)

**Bottom line:** buy-day/sell-night is the right core idea and Romania just removed the rule that blocked it — but design it as a **stacked** strategy (arbitrage + balancing, an optimiser, the grant), or the economics stay marginal.
