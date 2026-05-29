"""Romanian tax & payroll rules (2026), mirrored from ../../knowledge/taxation.md.

Single source of truth for the rates the simulator uses. When the knowledge base
changes, update these constants too (and the citations in README.md).

Not tax advice — a planning aid. Rates verified 2026-05.
"""
from __future__ import annotations

# --- Company income tax ---------------------------------------------------
CIT_RATE = 0.16                    # corporate income tax, on profit
MICRO_RATE = 0.01                  # micro-enterprise tax, on revenue
MICRO_TURNOVER_CAP_EUR = 100_000   # micro eligibility ceiling (annual turnover)
# micro also requires >= 1 full-time employee; sector restrictions removed in 2026

# --- VAT (TVA) ------------------------------------------------------------
VAT_STANDARD = 0.21
VAT_REDUCED = 0.11

# --- Payroll: employee (withheld from gross) ------------------------------
CAS = 0.25                         # pension social insurance
CASS = 0.10                        # health insurance
INCOME_TAX = 0.10                  # on (gross - CAS - CASS)
# --- Payroll: employer (on top of gross) ----------------------------------
CAM = 0.0225                       # work-insurance contribution

# --- Distributions --------------------------------------------------------
DIVIDEND_TAX = 0.16                # since 2026 (was 10%); CASS may also apply (see README)


def net_salary(gross_monthly: float) -> float:
    """Monthly net take-home from a monthly gross salary (CAS + CASS + income tax)."""
    after_social = gross_monthly * (1 - CAS - CASS)
    return after_social * (1 - INCOME_TAX)


def employer_cost(gross_monthly: float) -> float:
    """Total monthly employer cost for a monthly gross salary (gross + CAM)."""
    return gross_monthly * (1 + CAM)


def micro_eligible(annual_revenue_eur: float, has_employee: bool) -> bool:
    """Whether the micro-enterprise (1% on revenue) regime can apply this year."""
    return has_employee and annual_revenue_eur <= MICRO_TURNOVER_CAP_EUR


def company_tax(regime: str, revenue: float, taxable_profit: float) -> float:
    """Company income tax for one year, in the model currency.

    regime: 'micro' (1% of revenue) | 'cit' (16% of positive profit) | 'none' (e.g. NGO).
    """
    if regime == "none":
        return 0.0
    if regime == "micro":
        return MICRO_RATE * max(0.0, revenue)
    return CIT_RATE * max(0.0, taxable_profit)  # 'cit'
