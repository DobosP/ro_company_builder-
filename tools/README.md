# Tools (roadmap — deferred)

This project is **docs-first**. Software tools are deferred; this file records the intent so it isn't lost. Nothing here is built yet.

## Planned tools

| Tool | What it does | Likely inputs → outputs |
|------|--------------|--------------------------|
| **Financial simulator** | Micro-vs-CIT comparison, gross→net & employer-cost payroll, break-even, VAT cash-flow | model assumptions → P&L, charts |
| **Report generator** | Assemble a venture's markdown (brief + plan + financials) into a shareable dossier | `ventures/<slug>/` → PDF/HTML |
| **Venture evaluator** | Apply the [rubric](../framework/evaluation-rubric.md) programmatically; rank ventures | scores → comparison table |
| **Funding matcher** | Match a venture profile to live calls on `oportunitati-ue.gov.ro` | venture profile → eligible calls |
| **Data ingest** | Support for venture #5 (Romania data repo) — pull & normalize open data | sources → datasets |

## Principles when a tool is started
- Keep facts/rates sourced from [`../knowledge/`](../knowledge/) — don't hardcode duplicates that can drift.
- Store generated artifacts under the relevant `ventures/<slug>/`.
- Add the chosen stack's ignores to the root [`.gitignore`](../.gitignore).
- Pick the stack when the first tool starts (Python for simulation/data is the likely default); record the choice here.
