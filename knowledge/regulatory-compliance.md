# Regulatory & Compliance — Romania

> ⚠️ **Not legal advice. Verified 2026-05 — re-verify with the relevant authority before acting.** Sources: [`sources.md`](sources.md).

## Data protection (GDPR)
- Supervisory authority: **ANSPDCP** (see [institutions.md](institutions.md)).
- **Children's data** carries heightened protection. Under GDPR Art. 8, Romania sets the **digital-consent age at 16** — below it, parental/guardian consent is required. Critical for the planned **children's social app** and the **dyslexia learning app**: age assurance, parental-consent flows, data minimization, and safeguarding by design.
- Appoint a **DPO** where required (large-scale or sensitive processing); keep a record of processing activities (RoPA); run a DPIA for high-risk processing.

## Mandatory e-invoicing & tax reporting
Romania has one of the EU's most demanding digital-reporting stacks — budget for it from day one.

| System | What it is | Key requirement |
|--------|-----------|-----------------|
| **RO e-Factura** | Mandatory e-invoicing | B2B mandatory since Jan 2024 (EU derogation through end-2026), B2C in scope; XML per **EN 16931 + RO-CIUS**; submit within **5 working days**. [[S17]](sources.md#s17) |
| **SAF-T (D406)** | Standard Audit File for Tax | ANAF Order 1783/2021; **390+ data elements** (ledgers, customers, suppliers, stock…). [[S18]](sources.md#s18) |
| **RO e-TVA** | Pre-filled VAT return | Draft VAT return built from e-Factura/e-Transport/SAF-T data, available by the **20th** of the following month. [[S19]](sources.md#s19) |
| **RO e-Transport** | Goods-movement reporting | Declare transport of high-risk goods **3 days** before shipment. [[S17]](sources.md#s17) |

- Penalties for late/missing invoice data range **RON 1,000–10,000** by taxpayer size. [[S17]](sources.md#s17)

## Employment
- Register employment contracts in the national register (**REGES**, formerly Revisal) before the employee starts.
- Respect minimum-wage, working-time, and health-and-safety rules. Payroll contributions → [taxation.md](taxation.md).

## Accounting
- Double-entry bookkeeping and annual financial statements; most SMEs use a licensed accountant (*expert contabil*).
- Align the chart of accounts with **SAF-T D406** from the start to avoid rework.

## Sector-specific permits (pointer)
Depending on the CAEN activity, expect authorizations from sector regulators — e.g. **ANRE** (energy), **ANSVSA** + **APIA/AFIR** (food/agri), **ANCOM** (communications). Map yours via [institutions.md](institutions.md) and §4 of [`../framework/hard-questions.md`](../framework/hard-questions.md).
