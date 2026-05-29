# Decision Log — Agriculture / Irrigation (Romania)

> Append-only; newest on top. [A#] → [sources](research/sources.md).

---

## 2026-05-29 — Funding-first update: grant €2.8M → integrated IRR 10.5%; processing-first is the bankable path
- **Integrated** (corrected grant €2.8M = DR-23 65% €2.6M + sM4.1 €0.2M): project IRR **10.5%**, NPV **+€94k** @10%, payback 2034 — clears the hurdle, **but min DSCR still 0.56x** → over-levered (more equity / less debt needed).
- **Processing-first** (leased, contracted supply, 48% margin, €1.5M equity): IRR **52%**, NPV **+€3.3M**, **min DSCR 2.43x**, payback 2030 — **bankable**. ⚠️ The high IRR is **grant-dependent** (DR-23 covers 65% of CAPEX → small net outlay) and **margin-sensitive** (48% variable-cost assumption). See [finsim-processing-first-report.md](finsim-processing-first-report.md).
- **Lesson:** **margin + capitalization, not scope, are the levers** — a thin-margin/low-equity build fails DSCR; a lean, well-margined, well-capitalised one is strong.
- **Added** [funding-application.md](funding-application.md) — full AFIR DR-23 mockup (€2.6M, 65%, scoring). Confirms the **processing-first** entry.

---

## 2026-05-29 — finsim run: thin and under-capitalised as configured (IRR ~8%, DSCR 0.56x)
- **Result:** project **IRR ~8.0%**, **NPV −€377k** @10%, **payback 2034**, P&L break-even 2030, **min DSCR 0.56x**, **min cash −€130k** (financing gap) — at €6.3M CAPEX / €2.3M grant / €2.5M debt / €1.5M equity. See [finsim-report.md](finsim-report.md) (`python tools/finsim/run.py ventures/agriculture-irrigation/finsim.json`).
- **Read:** below the 10% hurdle, and **debt is not serviceable in the ramp** (DSCR 0.56x ≪ a bankable ~1.3x). The deal is **over-levered / under-capitalised** at these assumptions and very sensitive to the **45% variable-cost (margin)** assumption.
- **Levers:** **lease land** (cut €1.7M CAPEX), **more equity / less debt**, a **bigger AFIR grant**, and **higher processing margins** (offtake at a premium). → reinforces phasing.
- **Action:** model a **processing-first, leased-land** variant; treat crop+processing margin (O7) and grant intensity (O8) as make-or-break; re-run finsim. [A5](research/sources.md#a5)

---

## 2026-05-29 — Initial rubric score: 80/115 ("promising")
Using [`../../framework/evaluation-rubric.md`](../../framework/evaluation-rubric.md):

| Dim (weight) | Rating | Score | Why |
|---|:-:|:-:|---|
| Problem intensity (3) | 5 | 15 | import dependency + drought + food security [A6](research/sources.md#a6) |
| Market size & demand (3) | 5 | 15 | >80% fruit/veg imported [A7](research/sources.md#a7) |
| Financial viability (3) | 2 | 6 | finsim: IRR 8% < hurdle, DSCR 0.56x, thin margins |
| Fundability (2) | 5 | 10 | CAP €15.83B + AFIR DR-23 + APIA [A3](research/sources.md#a3) [A5](research/sources.md#a5) |
| Regulatory feasibility (2) | 3 | 6 | many authorities but well-trodden |
| Team/execution (3) | 2 | 6 | farming **and** processing competence needed |
| Defensibility (2) | 3 | 6 | land + water rights + processing + contracts |
| Impact (2) | 4 | 8 | food security, jobs, water efficiency |
| Location fit (1) | 4 | 4 | fertile irrigable south |
| Risk profile (2) | 2 | 4 | drought is severe and partly uncontrollable |
| **Total** | | **80** | promising, but fix capital structure + prove margins |

Financial viability (2) is the drag — the finsim run is why. **Action:** re-shape (phase + lease + margin) before committing.

---

## 2026-05-29 — Strategic entry: processing-first, leased land, contracted supply
- **Decision:** enter via **Phase 1 = processing + cold storage** (AFIR **DR-23** grant, clear import gap) sourcing from **contracted local growers**, then **Phase 2 = own ~200 ha irrigated production** once water + offtake are proven.
- **Options:** (A) production-only; (B) processing-only; (C) integrated now; (D) irrigation/OUAI services. Chose **C, phased** — captures the value-add margin and the richest grant stack while deferring land/irrigation CAPEX (the finsim shows full integration up-front is under-capitalised).
- **Reasoning:** the scarce, valuable assets are **reliable water on fertile land** + **offtake at a margin**; processing-first de-risks both before heavy CAPEX. [A1](research/sources.md#a1) [A7](research/sources.md#a7)
- **Follow-ups:** land/water + ANIF/OUAI scouting; DR-23 product + grant intensity; offtake LOIs; crop-margin model.

---

## Template entry (copy above)
