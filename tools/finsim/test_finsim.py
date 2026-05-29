"""Unit tests for finsim. Run: python tools/finsim/test_finsim.py"""
from __future__ import annotations

import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import finsim  # noqa: E402
import tax_ro  # noqa: E402


class TaxTests(unittest.TestCase):
    def test_net_salary(self):
        # gross 10,000: CAS 2,500 + CASS 1,000 -> base 6,500; income tax 650 -> net 5,850
        self.assertAlmostEqual(tax_ro.net_salary(10_000), 5_850.0, places=2)

    def test_employer_cost(self):
        self.assertAlmostEqual(tax_ro.employer_cost(10_000), 10_225.0, places=2)

    def test_micro_eligibility(self):
        self.assertTrue(tax_ro.micro_eligible(80_000, True))
        self.assertFalse(tax_ro.micro_eligible(120_000, True))   # over EUR 100k
        self.assertFalse(tax_ro.micro_eligible(80_000, False))   # no employee

    def test_company_tax(self):
        self.assertAlmostEqual(tax_ro.company_tax("micro", 50_000, 10_000), 500.0)
        self.assertAlmostEqual(tax_ro.company_tax("cit", 50_000, 10_000), 1_600.0)
        self.assertEqual(tax_ro.company_tax("none", 50_000, 10_000), 0.0)
        self.assertEqual(tax_ro.company_tax("cit", 50_000, -5_000), 0.0)  # no tax on a loss


class EngineTests(unittest.TestCase):
    def test_series_forms(self):
        self.assertEqual(finsim.expand_series(5, 3), [5, 5, 5])
        self.assertEqual(finsim.expand_series([1, 2], 4), [1, 2, 2, 2])  # carry forward
        grown = finsim.expand_series({"base": 100, "growth": 0.1}, 2)
        self.assertAlmostEqual(grown[0], 100.0)
        self.assertAlmostEqual(grown[1], 110.0)

    def test_npv_irr(self):
        self.assertAlmostEqual(finsim.npv(0.10, [-100, 110]), 0.0, places=6)
        self.assertAlmostEqual(finsim.irr([-100, 110]), 0.10, places=4)
        self.assertIsNone(finsim.irr([1, 2, 3]))  # no sign change -> no IRR

    def test_debt_annuity(self):
        intr, prin, draw = finsim.debt_schedule(
            [{"amount": 1000, "rate": 0.10, "term_years": 2, "type": "annuity", "draw_year": 2026}],
            2026, 4)
        self.assertAlmostEqual(draw[0], 1000.0)
        self.assertAlmostEqual(sum(prin), 1000.0, places=2)   # principal fully repaid
        self.assertAlmostEqual(intr[1], 100.0, places=2)      # yr-1 interest = 10% of 1000

    def test_auto_regime_picks_micro_when_cheaper(self):
        cfg = {
            "start_year": 2026, "horizon_years": 1, "legal_form": "srl", "tax_regime": "auto",
            "revenue": [{"name": "sales", "amounts_by_year": [50_000]}],
            "costs": {"payroll": [{"role": "founder", "count": 1, "gross_monthly": 1000}]},
        }
        self.assertEqual(finsim.project(cfg).meta["regime"], "micro")

    def test_auto_regime_forces_cit_over_threshold(self):
        cfg = {
            "start_year": 2026, "horizon_years": 1, "legal_form": "srl", "tax_regime": "auto",
            "revenue": [{"name": "sales", "amounts_by_year": [500_000]}],
            "costs": {"payroll": [{"role": "founder", "count": 1, "gross_monthly": 1000}]},
        }
        self.assertEqual(finsim.project(cfg).meta["regime"], "cit")  # over EUR 100k

    def test_ngo_pays_no_tax(self):
        cfg = {"start_year": 2026, "horizon_years": 2, "legal_form": "ngo", "tax_regime": "auto",
               "revenue": [{"name": "grants", "amounts_by_year": [100_000, 100_000]}],
               "costs": {"fixed_opex": 50_000}}
        r = finsim.project(cfg)
        self.assertEqual(r.meta["regime"], "none")
        self.assertEqual(sum(r.tax), 0.0)

    def test_break_even_detection(self):
        cfg = {"start_year": 2026, "horizon_years": 5, "legal_form": "srl", "tax_regime": "cit",
               "revenue": [{"name": "s", "amounts_by_year": [60, 60, 60, 60, 60]}],
               "costs": {"fixed_opex": 10},
               "capex": [{"name": "kit", "amount": 100, "year": 2026, "depreciation_years": 5}]}
        self.assertIsNotNone(finsim.project(cfg).meta["payback_year"])

    def test_grant_reduces_depreciation_base(self):
        # 100 capex, 50 grant reducing base, 10y dep -> annual dep = 100*0.5/10 = 5
        cfg = {"start_year": 2026, "horizon_years": 1, "legal_form": "srl", "tax_regime": "cit",
               "revenue": [{"name": "s", "amounts_by_year": [0]}],
               "capex": [{"name": "k", "amount": 100, "year": 2026, "depreciation_years": 10}],
               "grants": [{"name": "g", "amount": 50, "year": 2026, "reduces_depreciation_base": True}]}
        self.assertAlmostEqual(finsim.project(cfg).depreciation[0], 5.0, places=6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
