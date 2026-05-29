"""Generic multi-year financial projection engine for Romanian ventures.

Config-driven (JSON): the *same* engine serves any venture — capital-heavy
(energy, agri), SaaS (apps), or non-profit (NGO) — by toggling optional config
sections. It produces a per-year P&L + cash flow and headline metrics
(NPV, IRR, payback, DSCR, break-even).

A planning aid, not accounting. Romanian tax rules live in tax_ro.py
(mirrored from ../../knowledge/taxation.md). See README.md for the config schema
and the deliberate simplifications.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import tax_ro


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def expand_series(spec: Any, horizon: int) -> list[float]:
    """Expand a flexible spec into a per-year list of length `horizon`.

    spec may be:
      - a number                     -> constant every year
      - a list of numbers            -> used by index; last value carried forward
      - {"amounts_by_year": [...]}   -> same as a list
      - {"base": x, "growth": g}     -> x * (1+g)**t
    """
    if spec is None:
        return [0.0] * horizon
    if isinstance(spec, (int, float)):
        return [float(spec)] * horizon
    if isinstance(spec, list):
        if not spec:
            return [0.0] * horizon
        return [float(spec[min(t, len(spec) - 1)]) for t in range(horizon)]
    if isinstance(spec, dict):
        if "amounts_by_year" in spec:
            return expand_series(spec["amounts_by_year"], horizon)
        base = float(spec.get("base", 0.0))
        growth = float(spec.get("growth", 0.0))
        return [base * ((1 + growth) ** t) for t in range(horizon)]
    raise ValueError(f"Unsupported series spec: {spec!r}")


def npv(rate: float, flows: list[float]) -> float:
    """Net present value of year-end `flows` (flows[0] at t=0, undiscounted)."""
    return sum(cf / ((1 + rate) ** t) for t, cf in enumerate(flows))


def irr(flows: list[float]) -> float | None:
    """Internal rate of return via bisection; None if there is no sign change."""
    if not flows or all(f >= 0 for f in flows) or all(f <= 0 for f in flows):
        return None
    lo, hi = -0.9999, 10.0
    f_lo, f_hi = npv(lo, flows), npv(hi, flows)
    if f_lo * f_hi > 0:
        return None
    for _ in range(200):
        mid = (lo + hi) / 2
        f_mid = npv(mid, flows)
        if abs(f_mid) < 1e-6:
            return mid
        if f_lo * f_mid < 0:
            hi, f_hi = mid, f_mid
        else:
            lo, f_lo = mid, f_mid
    return (lo + hi) / 2


def debt_schedule(debts: list[dict], start_year: int, horizon: int):
    """Per-year (interest, principal, draw) arrays for a list of loans.

    Each loan: {amount, rate, term_years, type: annuity|linear|bullet, draw_year}.
    Draw lands in draw_year; repayment runs over the following `term_years`.
    """
    interest = [0.0] * horizon
    principal = [0.0] * horizon
    draw = [0.0] * horizon
    for d in debts:
        amount = float(d["amount"])
        r = float(d.get("rate", 0.0))
        term = int(d.get("term_years", 1))
        kind = d.get("type", "annuity")
        di = int(d.get("draw_year", start_year)) - start_year
        if 0 <= di < horizon:
            draw[di] += amount
        annuity_pay = amount * r / (1 - (1 + r) ** (-term)) if (kind == "annuity" and r > 0) else amount / term
        bal = amount
        for k in range(1, term + 1):
            t = di + k
            if t >= horizon or bal <= 0:
                break
            intr = bal * r
            if kind == "bullet":
                pr = amount if k == term else 0.0
            elif kind == "annuity":
                pr = annuity_pay - intr
            else:  # linear
                pr = amount / term
            pr = min(pr, bal)
            interest[t] += intr
            principal[t] += pr
            bal -= pr
    return interest, principal, draw


# --------------------------------------------------------------------------
# results
# --------------------------------------------------------------------------
@dataclass
class Results:
    years: list[int]
    revenue: list[float]
    opex: list[float]
    ebitda: list[float]
    depreciation: list[float]
    interest: list[float]
    principal: list[float]
    tax: list[float]
    net_profit: list[float]
    project_fcf: list[float]
    cash_balance: list[float]
    dscr: list[float | None]
    dividends_net: list[float]
    meta: dict = field(default_factory=dict)


# --------------------------------------------------------------------------
# engine
# --------------------------------------------------------------------------
def project(cfg: dict) -> Results:
    """Run the projection for a parsed config dict and return Results."""
    start = int(cfg.get("start_year", 2026))
    H = int(cfg.get("horizon_years", 10))
    eur_rate = float(cfg.get("eur_rate", 1.0))          # currency units per 1 EUR
    disc = float(cfg.get("discount_rate", 0.10))
    legal = cfg.get("legal_form", "srl").lower()
    regime_cfg = cfg.get("tax_regime", "auto").lower()
    years = [start + t for t in range(H)]

    # --- revenue ---
    revenue = [0.0] * H
    for stream in cfg.get("revenue", []):
        ser = expand_series(stream, H)
        revenue = [a + b for a, b in zip(revenue, ser)]

    # --- costs (fixed, variable, payroll) ---
    costs = cfg.get("costs", {})
    fixed = expand_series(costs.get("fixed_opex"), H)
    var_pct = float(costs.get("variable_pct_of_revenue", 0.0))
    payroll_roles = costs.get("payroll", [])
    annual_payroll = sum(
        float(r.get("count", 0)) * float(r.get("gross_monthly", 0)) * 12 * (1 + tax_ro.CAM)
        for r in payroll_roles
    )
    has_employee = any(int(r.get("count", 0)) >= 1 for r in payroll_roles)
    opex = [fixed[t] + var_pct * revenue[t] + annual_payroll for t in range(H)]
    ebitda = [revenue[t] - opex[t] for t in range(H)]

    # --- capex, grants, depreciation ---
    capex_items = cfg.get("capex", [])
    total_capex = sum(float(c["amount"]) for c in capex_items)
    capex_cash = [0.0] * H
    for c in capex_items:
        i = int(c.get("year", start)) - start
        if 0 <= i < H:
            capex_cash[i] += float(c["amount"])

    grant_cash = [0.0] * H
    grants_reducing_base = 0.0
    for g in cfg.get("grants", []):
        i = int(g.get("year", start)) - start
        if 0 <= i < H:
            grant_cash[i] += float(g["amount"])
        if g.get("reduces_depreciation_base", True):
            grants_reducing_base += float(g["amount"])

    base_factor = max(0.0, 1 - grants_reducing_base / total_capex) if total_capex > 0 else 1.0
    depreciation = [0.0] * H
    for c in capex_items:
        i = int(c.get("year", start)) - start
        yrs = int(c.get("depreciation_years", 10))
        if yrs <= 0:
            continue
        annual = float(c["amount"]) * base_factor / yrs
        for k in range(yrs):
            t = i + k
            if 0 <= t < H:
                depreciation[t] += annual

    # --- financing ---
    fin = cfg.get("financing", {})
    equity = float(fin.get("equity", 0.0))
    interest, principal, draw = debt_schedule(fin.get("debt", []), start, H)

    # --- tax regime selection ---
    revenue_eur = [revenue[t] / eur_rate for t in range(H)]

    def tax_for(regime: str) -> list[float]:
        out = [0.0] * H
        loss_pool = 0.0
        for t in range(H):
            ebit = ebitda[t] - depreciation[t]
            pretax = ebit - interest[t]
            if regime == "cit":
                if pretax < 0:
                    loss_pool += -pretax
                    out[t] = 0.0
                else:
                    used = min(loss_pool, pretax)
                    loss_pool -= used
                    out[t] = tax_ro.CIT_RATE * (pretax - used)
            elif regime == "micro":
                out[t] = tax_ro.MICRO_RATE * max(0.0, revenue[t])
            else:  # none
                out[t] = 0.0
        return out

    micro_ok = (
        legal not in ("ngo", "pfa")
        and has_employee
        and all(revenue_eur[t] <= tax_ro.MICRO_TURNOVER_CAP_EUR for t in range(H))
    )
    if regime_cfg == "auto":
        if legal == "ngo":
            regime = "none"
        elif micro_ok:
            regime = "micro" if npv(disc, tax_for("micro")) <= npv(disc, tax_for("cit")) else "cit"
        else:
            regime = "cit"
    else:
        regime = regime_cfg
    tax = tax_for(regime)

    # --- P&L, cash flow, balances ---
    net_profit = [(ebitda[t] - depreciation[t] - interest[t]) - tax[t] for t in range(H)]
    project_fcf = [ebitda[t] - tax[t] - capex_cash[t] + grant_cash[t] for t in range(H)]

    cash_balance: list[float] = []
    cash = 0.0
    for t in range(H):
        flow = (ebitda[t] - tax[t] - interest[t] - principal[t]
                - capex_cash[t] + grant_cash[t] + draw[t])
        if t == 0:
            flow += equity
        cash += flow
        cash_balance.append(cash)

    dscr: list[float | None] = []
    for t in range(H):
        service = interest[t] + principal[t]
        dscr.append((ebitda[t] - tax[t]) / service if service > 1e-9 else None)

    payout = float(cfg.get("dividend_payout", 0.0))
    dividends_net = [payout * max(0.0, net_profit[t]) * (1 - tax_ro.DIVIDEND_TAX) for t in range(H)]

    # --- metrics ---
    cum = 0.0
    payback_year = None
    for t in range(H):
        cum += project_fcf[t]
        if payback_year is None and cum >= 0:
            payback_year = start + t
    dscr_vals = [d for d in dscr if d is not None]
    meta = {
        "name": cfg.get("name", "Venture"),
        "currency": cfg.get("currency", "EUR"),
        "legal_form": legal,
        "regime": regime,
        "regime_auto": regime_cfg == "auto",
        "discount_rate": disc,
        "npv": npv(disc, project_fcf),
        "irr": irr(project_fcf),
        "payback_year": payback_year,
        "pl_breakeven_year": next((start + t for t in range(H) if net_profit[t] > 0), None),
        "min_cash": min(cash_balance) if cash_balance else 0.0,
        "min_dscr": min(dscr_vals) if dscr_vals else None,
        "total_capex": total_capex,
        "total_grant": sum(grant_cash),
        "equity": equity,
        "horizon_years": H,
    }

    return Results(years, revenue, opex, ebitda, depreciation, interest, principal,
                   tax, net_profit, project_fcf, cash_balance, dscr, dividends_net, meta)


def load_config(path: str) -> dict:
    import json
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)
