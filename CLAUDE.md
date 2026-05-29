# CLAUDE.md — working in this repo

This file orients an AI (or human) contributor. Read it before extending the repo.

## What this is

`ro_company_builder` is a **docs-first knowledge base + methodology** for creating and running ventures in **Romania**. It is not (yet) a software project — software tools are deferred and tracked in [`tools/README.md`](tools/README.md).

Two reusable pillars + per-venture workspaces:
- [`framework/`](framework/) — the methodology ("ask the hard questions") + the **[EU funding playbook](framework/eu-funding-playbook.md)** (the project's core funding lens).
- [`knowledge/`](knowledge/) — verified Romania-specific facts ("common info").
- [`templates/`](templates/) — fill-in artifacts reused by every venture.
- [`ventures/`](ventures/) — one folder per concrete venture (copy [`_template/`](ventures/_template/)).
- [`tools/`](tools/) — roadmap for deferred software.

## Conventions

- **Language:** English prose; keep Romanian official terms verbatim (SRL, ONRC, ANAF, CAEN, TVA, CUI, PNRR) and decode them in [`knowledge/glossary.md`](knowledge/glossary.md).
- **Every fact is sourced and dated.** When you state a number (a rate, a threshold, a deadline), add an inline citation and a matching entry in [`knowledge/sources.md`](knowledge/sources.md) with the URL and a `verified YYYY-MM` date.
- **Disclaimers stay.** Every `knowledge/` doc carries the "not legal/tax advice — re-verify" banner. Romanian fiscal law changes fast; do not delete the banner.
- **Markdown only** for content. Tables for structured facts, checklists for questions.
- **Relative links** between docs; keep them resolving.

## How to add a venture

1. Copy [`ventures/_template/`](ventures/_template/) to `ventures/<slug>/`.
2. Work through [`framework/hard-questions.md`](framework/hard-questions.md), capturing answers.
3. Use the [`templates/`](templates/) for the brief, business plan, financials, etc.
4. Pull venture-specific research (sector regulator, subsidies, market) — cite sources.
5. Score it with [`framework/evaluation-rubric.md`](framework/evaluation-rubric.md).

## How to add a tool

The first tool — [`tools/finsim/`](tools/finsim/), a config-driven financial simulator (pure-stdlib Python) — is built; its Romanian rates **mirror** [`knowledge/taxation.md`](knowledge/taxation.md), so update both together. When starting another tool, see [`tools/README.md`](tools/README.md), add a `.gitignore` entry if needed, and keep generated docs/reports under the relevant venture folder.

## Guardrails

- This repo **informs**; it does not replace ONRC/ANAF guidance or a licensed lawyer/accountant.
- Don't invent legal/tax figures. If unverified, mark `[TODO: verify]` rather than guessing, and log it in [`knowledge/open-questions.md`](knowledge/open-questions.md). When you resolve a question, update the doc + [`knowledge/sources.md`](knowledge/sources.md) and move the row to "Resolved" in that register.
- Keep mission-driven and children-focused ventures' safeguarding considerations explicit.
