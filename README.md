# ro_company_builder

A reusable **"Romania company builder"** — a knowledge base and methodology for starting and running ventures in Romania. It exists to **ask the hard questions** and to capture the **common information** an AI or a founder needs to go from idea → registered company → operating venture in Romania.

> ⚠️ **Not legal, tax, or financial advice.** Everything here is a research aid. Romanian fiscal and corporate law changes frequently (major reforms landed in 2025–2026). Every fact is dated and sourced in [`knowledge/sources.md`](knowledge/sources.md) — **re-verify with ONRC/ANAF or a licensed professional before acting.**

## Why this exists

Starting a company involves the same recurring questions and the same body of country-specific knowledge, regardless of the idea. This repo separates the two:

- **The reusable methodology** — the questions every venture must answer, the lifecycle every venture passes through, and a rubric to compare ventures. → [`framework/`](framework/)
- **The reusable Romania knowledge** — how companies are formed, taxed, funded, and regulated here. → [`knowledge/`](knowledge/)

Each concrete venture then becomes: *copy a template, answer the hard questions, fill in the venture-specific research.*

## Repository map

| Path | What's inside |
|------|---------------|
| [`framework/`](framework/) | The methodology: [hard questions](framework/hard-questions.md), [venture lifecycle](framework/venture-lifecycle.md), [evaluation rubric](framework/evaluation-rubric.md) |
| [`knowledge/`](knowledge/) | Verified Romania facts: [formation](knowledge/company-formation.md), [taxation](knowledge/taxation.md), [funding](knowledge/funding-landscape.md), [compliance](knowledge/regulatory-compliance.md), [institutions](knowledge/institutions.md), [glossary](knowledge/glossary.md), [open questions](knowledge/open-questions.md), [sources](knowledge/sources.md) |
| [`templates/`](templates/) | Fill-in artifacts: venture brief, business plan, financial model, market analysis, compliance checklist, risk register, decision log |
| [`ventures/`](ventures/) | One folder per venture (scaffold + [`_template/`](ventures/_template/)). Ventures are added in later sessions. |
| [`tools/`](tools/) | Roadmap/placeholder for future software (simulators, report generators, evaluators). |

## How to use it

1. Read [`framework/hard-questions.md`](framework/hard-questions.md) — this is the heart of the project.
2. Skim the [`knowledge/`](knowledge/) docs for the Romanian context.
3. To work a new idea: copy [`ventures/_template/`](ventures/_template/) to `ventures/<name>/` and work through the hard questions using the [`templates/`](templates/).

## Planned ventures (deep research in later sessions)

This pass builds only the framework. The ventures queued for research:

1. **Energy storage / batteries** in strategic locations in Romania *(flagged #1)*
2. **Agriculture** — irrigation systems & infrastructure to produce/process agri products
3. **Children's social app** — nonprofit, child-safety-first
4. **Dyslexia learning app** for children
5. **Romania data / knowledge repository** — open-ended end product

## Status

- ✅ Framework + Romania knowledge base (v1, verified 2026-05)
- ⬜ Venture deep-dives
- ⬜ Software tools (see [`tools/README.md`](tools/README.md))

See [`CLAUDE.md`](CLAUDE.md) for conventions and how to extend this repo.
