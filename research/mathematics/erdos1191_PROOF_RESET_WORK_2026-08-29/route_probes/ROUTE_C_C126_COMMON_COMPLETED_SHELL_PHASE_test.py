#!/usr/bin/env python3
"""Regression tests for the C126 common completed-shell phase audit."""

from __future__ import annotations

from fractions import Fraction as F
import importlib
import json
import unittest


MODULE = "ROUTE_C_C126_COMMON_COMPLETED_SHELL_PHASE_certificate"


class C126CommonCompletedShellPhaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cert = importlib.import_module(MODULE)
        cls.value = json.loads(cls.cert.DEFAULT_CERTIFICATE.read_text())
        cls.summary = cls.cert.verify_certificate(cls.value)

    def test_frozen_scope_retains_global_phase_gate(self) -> None:
        self.assertEqual(self.value["schema"], self.cert.SCHEMA)
        self.assertFalse(self.value["scope"]["global_C103_phase_rule_admissible_proved"])
        self.assertFalse(self.value["scope"]["C058_resolved"])
        self.assertTrue(self.value["scope"]["common_phase_for_C120_C123_proved"])

    def test_both_common_phase_duals_replay_exactly(self) -> None:
        self.assertEqual(self.summary["C120"]["phase_chambers"], 147)
        self.assertEqual(self.summary["C120"]["epoch_duals"], 294)
        self.assertEqual(self.summary["C120"]["dual_weights"], 90552)
        self.assertEqual(self.summary["C120"]["endpoint_pd_checks"], 588)
        self.assertEqual(self.summary["C123"]["phase_chambers"], 135)
        self.assertEqual(self.summary["C123"]["epoch_duals"], 270)
        self.assertEqual(self.summary["C123"]["dual_weights"], 83160)
        self.assertEqual(self.summary["C123"]["endpoint_pd_checks"], 540)

    def test_clean_scalar_interval_is_nonempty(self) -> None:
        self.assertEqual(self.summary["clean_B_lower"], F(1341, 4000))
        self.assertEqual(self.summary["clean_B_upper"], F(1133, 2000))
        self.assertEqual(self.summary["clean_width"], F(37, 160))
        self.assertFalse(self.summary["barriers_contradict"])

    def test_exact_scalar_interval_has_a_rational_witness(self) -> None:
        self.assertTrue(self.summary["exact_common_phase_interval_nonempty"])
        self.assertEqual(self.summary["exact_B_witness"], F(1, 2))
        self.assertLess(self.summary["exact_C121_B_lower"], F(1, 2))
        self.assertLess(F(1, 2), self.summary["C120"]["exact_B_upper"])
        self.assertLess(F(1, 2), self.summary["C123"]["exact_B_upper"])

    def test_self_check_rejects_all_mutations(self) -> None:
        self.assertEqual(self.cert.self_check(self.value)["mutations_rejected"], 12)


if __name__ == "__main__":
    unittest.main()
