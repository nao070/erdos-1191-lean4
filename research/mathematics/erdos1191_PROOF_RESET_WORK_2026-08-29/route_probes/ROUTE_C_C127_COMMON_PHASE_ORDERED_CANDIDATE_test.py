#!/usr/bin/env python3
"""Regression tests for the C127 common-phase ordered candidate audit."""

from __future__ import annotations

from fractions import Fraction as F
import importlib
import json
import unittest


MODULE = "ROUTE_C_C127_COMMON_PHASE_ORDERED_CANDIDATE_certificate"


class C127CommonPhaseOrderedCandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cert = importlib.import_module(MODULE)
        cls.value = json.loads(cls.cert.DEFAULT_CERTIFICATE.read_text())
        cls.summary = cls.cert.verify_certificate(cls.value)

    def test_common_phase_dependencies_replay_with_frozen_counts(self) -> None:
        self.assertEqual(self.summary["common_phase"], (F(82), F(164)))
        self.assertEqual(self.summary["C120"]["phase_chambers"], 147)
        self.assertEqual(self.summary["C120"]["epoch_duals"], 294)
        self.assertEqual(self.summary["C120"]["dual_weights"], 90_552)
        self.assertEqual(self.summary["C120"]["endpoint_pd_checks"], 588)
        self.assertEqual(self.summary["C123"]["phase_chambers"], 135)
        self.assertEqual(self.summary["C123"]["epoch_duals"], 270)
        self.assertEqual(self.summary["C123"]["dual_weights"], 83_160)
        self.assertEqual(self.summary["C123"]["endpoint_pd_checks"], 540)

    def test_exact_dual_upper_minus_target_margins_exceed_clean_fences(self) -> None:
        c120_margin = self.summary["C120"]["certified_margin_lower"]
        c123_margin = self.summary["C123"]["certified_margin_lower"]
        self.assertGreater(c120_margin, F(21, 500))
        self.assertGreater(c123_margin, F(7, 1000))
        self.assertGreater(c120_margin, F(1, 10_000))
        self.assertGreater(c123_margin, F(1, 10_000))
        self.assertFalse(self.summary["stored_dual_upper_checks_separate_candidate"])

    def test_candidate_and_scope_are_exactly_frozen(self) -> None:
        self.assertEqual(self.summary["candidate"]["epsilon"], F(1, 1000))
        self.assertEqual(self.summary["candidate"]["A"], F(1, 1000))
        self.assertEqual(self.summary["candidate"]["B"], F(1, 2))
        self.assertEqual(self.summary["candidate"]["C_ordered_suffix"], F(1, 10))
        self.assertEqual(self.summary["candidate"]["e2"], F(0))
        self.assertTrue(self.value["scope"]["failure_of_two_necessary_side_dual_checks_only"])
        self.assertFalse(self.value["scope"]["primal_phase_witness_constructed"])
        self.assertFalse(self.value["scope"]["local_master_inequality_proved"])
        self.assertFalse(self.value["scope"]["global_phase_rule_admissible_proved"])
        self.assertFalse(self.value["scope"]["arbitrary_rank_proved"])
        self.assertFalse(self.value["scope"]["C058_resolved"])
        self.assertFalse(self.value["scope"]["Q1_Q2_resolved"])

    def test_canonical_payload_and_mutation_barrier(self) -> None:
        self.assertEqual(self.value, self.cert.expected_certificate())
        self.assertEqual(self.cert.self_check(self.value)["mutations_rejected"], 13)


class C127NeutralMarginFailureTests(unittest.TestCase):
    def test_missing_positive_margin_does_not_claim_separation(self) -> None:
        cert = importlib.import_module(MODULE)
        dependency_row = {
            "phase_chambers": 1,
            "epoch_duals": 2,
            "dual_weights": 616,
            "endpoint_pd_checks": 4,
            "normalized_lower": F(0),
            "normalized_upper": F(0),
        }
        with self.assertRaisesRegex(
            cert.CertificateError,
            "certified positive stored-dual margin is missing",
        ):
            cert._candidate_row(
                dependency_row,
                F(0),
                F(1, 1000),
                "test-row",
                F(0),
                F(0),
            )


if __name__ == "__main__":
    unittest.main()
