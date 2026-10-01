#!/usr/bin/env python3
"""Regression tests for the exact C125 ordered-suffix outer bank."""

from __future__ import annotations

from fractions import Fraction as F
import importlib
import json
from pathlib import Path
import unittest


MODULE = "ROUTE_C_C125_ORDERED_SUFFIX_FIVE_ROW_BANK_certificate"
HERE = Path(__file__).resolve().parent


class C125OrderedSuffixFiveRowBankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cert = importlib.import_module(MODULE)
        cls.value = json.loads(cls.cert.DEFAULT_CERTIFICATE.read_text())
        cls.summary = cls.cert.verify_certificate(cls.value)

    def test_frozen_schema_status_and_scope(self) -> None:
        self.assertEqual(self.value["schema"], self.cert.SCHEMA)
        self.assertEqual(self.value["status"], self.cert.STATUS)
        self.assertFalse(self.value["scope"]["C058_resolved"])
        self.assertFalse(self.value["scope"]["outer_bank_infeasible"])
        self.assertTrue(self.value["scope"]["five_fixed_16_mark_rows_only"])

    def test_two_new_full_phase_sources_replay_exactly(self) -> None:
        rows = self.summary["new_rows"]
        self.assertEqual(rows["index12"]["phase_chambers"], 149)
        self.assertEqual(rows["index12"]["epoch_duals"], 298)
        self.assertEqual(rows["index12"]["dual_weights"], 91784)
        self.assertEqual(rows["index12"]["endpoint_pd_checks"], 596)
        self.assertEqual(rows["index3"]["phase_chambers"], 155)
        self.assertEqual(rows["index3"]["epoch_duals"], 310)
        self.assertEqual(rows["index3"]["dual_weights"], 95480)
        self.assertEqual(rows["index3"]["endpoint_pd_checks"], 620)

    def test_exact_rational_candidate_survives_all_five_outer_rows(self) -> None:
        self.assertEqual(self.summary["candidate_B"], F(1, 2))
        self.assertEqual(self.summary["candidate_C"], F(1, 10))
        self.assertEqual(set(self.summary["strict_margins"]), {
            "C118", "C120", "C123", "index12", "index3"
        })
        self.assertTrue(all(x > 0 for x in self.summary["strict_margins"].values()))
        self.assertFalse(self.summary["outer_bank_infeasible"])

    def test_self_check_rejects_all_mutations(self) -> None:
        result = self.cert.self_check(self.value)
        self.assertEqual(result["mutations_rejected"], 12)


if __name__ == "__main__":
    unittest.main()
