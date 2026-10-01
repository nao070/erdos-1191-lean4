#!/usr/bin/env python3
"""Regression tests for the C130 complete fixed-C123 phase primal."""

from __future__ import annotations

import copy
from fractions import Fraction as F
import importlib
import json
from pathlib import Path
import tempfile
import unittest


MODULE = "ROUTE_C_C130_COMPLETE_C123_PHASE_PRIMAL_certificate"


class C130CompleteC123PhasePrimalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cert = importlib.import_module(MODULE)
        cls.value = json.loads(cls.cert.DEFAULT_CERTIFICATE.read_text())
        cls.summary = cls.cert.verify_certificate(cls.value)

    def test_complete_bank_has_exact_clean_integrated_margin(self) -> None:
        complete = self.summary["complete_C123"]
        self.assertEqual((complete["chambers"], complete["factors"]), (135, 270))
        self.assertGreater(complete["raw_margin_lower"], F(1, 400))
        self.assertGreater(complete["normalized_margin_lower"], F(91, 25_000))

    def test_exact_gram_owner_rank_and_objective_census_is_frozen(self) -> None:
        complete = self.summary["complete_C123"]
        self.assertEqual(complete["generic_owner_rows"], 51_355)
        self.assertEqual(complete["generic_owner_endpoint_checks"], 102_710)
        self.assertEqual(complete["collapsed_endpoint_owner_rows"], 100_183)
        self.assertEqual(complete["structural_zero_generic_rows"], 31_805)
        self.assertEqual(complete["structural_zero_collapsed_endpoint_rows"], 62_713)
        self.assertEqual(complete["owner_recovery_state_evaluations"], 10_395)
        self.assertEqual(complete["per_epoch_owner_recovery_checks"], 20_790)
        self.assertEqual(complete["endpoint_epoch_objective_checks"], 540)
        self.assertEqual(complete["endpoint_weighted_objective_checks"], 270)
        self.assertEqual(complete["interior_owner_rows"], 51_355)
        self.assertEqual(complete["structural_zero_interior_rows"], 31_805)
        self.assertEqual(complete["interior_epoch_objective_checks"], 270)
        self.assertEqual(complete["interior_weighted_objective_checks"], 135)
        self.assertEqual((complete["rank_min"], complete["rank_max"]), (9, 25))
        self.assertEqual(complete["rank_sum"], 4_288)
        self.assertEqual(complete["denominators"], (100_000_000,))
        self.assertTrue(complete["all_factor_columns_independent"])
        self.assertTrue(complete["all_embedded_columns_zero_sum"])
        self.assertTrue(complete["all_gram_matrices_psd"])
        self.assertTrue(complete["all_owner_rows_strictly_positive"])
        self.assertTrue(complete["all_epoch_objectives_reconstructed"])
        self.assertEqual(
            complete["minimum_owner_margin"],
            F(1_137_298_595_103, 235_750_000_000_000_000),
        )
        self.assertEqual(len(complete["negative_piece_indices"]), 37)
        self.assertEqual(len(complete["positive_piece_indices"]), 98)

    def test_bank_is_ordered_complete_and_float_free(self) -> None:
        records = self.value["factor_bank"]["records"]
        self.assertEqual([record["index"] for record in records], list(range(135)))
        rendered = json.dumps(self.value, sort_keys=True, separators=(",", ":"))
        for forbidden in (
            "solver_status", "numeric_", "optimal", "inaccurate",
            "clipped_negative_eigenvalue", "matrix",
        ):
            self.assertNotIn(forbidden, rendered)

    def test_scope_preserves_every_unresolved_gate(self) -> None:
        scope = self.value["scope"]
        self.assertTrue(scope["complete_fixed_C123_common_phase_primal_constructed"])
        self.assertTrue(scope["all_135_C123_phase_chambers_exactified"])
        self.assertFalse(scope["C120_phase_primal_constructed"])
        self.assertFalse(scope["C103_phase_rule_admissible_proved"])
        self.assertFalse(scope["C103_Abel_boundary_terminal_ledger_constructed"])
        self.assertFalse(scope["global_phase_rule_admissible_proved"])
        self.assertFalse(scope["local_master_inequality_proved"])
        self.assertFalse(scope["arbitrary_rank_proved"])
        self.assertFalse(scope["global_owner_stitching_proved"])
        self.assertFalse(scope["C058_resolved"])
        self.assertFalse(scope["Q1_Q2_resolved"])
        self.assertFalse(scope["publication_novelty_or_prize_claimed"])

    def test_factor_mutation_is_rejected_even_after_rehash(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["factor_bank"]["records"][0]["n4"]["columns"][0][0] += 1
        changed["integrity"]["factor_bank_sha256"] = self.cert._object_hash(
            changed["factor_bank"]
        )
        changed["integrity"]["payload_sha256"] = self.cert.payload_hash(changed)
        with self.assertRaisesRegex(self.cert.CertificateError, "factor bank hash changed"):
            self.cert.verify_certificate(changed)

    def test_rehashed_float_and_integer_bool_confusions_are_rejected(self) -> None:
        changed_float = copy.deepcopy(self.value)
        changed_float["results"]["factor_bank_chambers"] = 135.0
        changed_float["integrity"]["payload_sha256"] = self.cert.payload_hash(changed_float)
        with self.assertRaisesRegex(self.cert.CertificateError, "floating value forbidden"):
            self.cert.verify_certificate(changed_float)

        changed_bool = copy.deepcopy(self.value)
        changed_bool["scope"]["C058_resolved"] = 0
        changed_bool["integrity"]["payload_sha256"] = self.cert.payload_hash(changed_bool)
        with self.assertRaisesRegex(self.cert.CertificateError, "exact value type changed"):
            self.cert.verify_certificate(changed_bool)

    def test_separate_interior_objective_mismatch_is_rejected(self) -> None:
        actual4, actual8 = F(2), F(3)
        expected4, expected8 = F(1), F(43, 9)
        self.assertEqual(
            actual4 + self.cert.RHO * actual8,
            expected4 + self.cert.RHO * expected8,
        )
        with self.assertRaisesRegex(
            self.cert.CertificateError, "epoch-4 interior objective mismatch"
        ):
            self.cert._check_interior_objectives(
                index=0,
                actual4=actual4,
                actual8=actual8,
                expected4=expected4,
                expected8=expected8,
            )

    def test_canonical_payload_and_mutation_barrier(self) -> None:
        self.assertEqual(self.cert._load(self.cert.DEFAULT_CERTIFICATE), self.value)
        mutation_summary = self.cert.self_check(self.value)
        self.assertEqual(mutation_summary["mutations_rejected"], 28)


class C130CanonicalRenderingTests(unittest.TestCase):
    def test_noncanonical_certificate_rendering_is_rejected(self) -> None:
        cert = importlib.import_module(MODULE)
        value = json.loads(cert.DEFAULT_CERTIFICATE.read_text())
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "certificate.json"
            path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
            with self.assertRaisesRegex(cert.CertificateError, "canonical rendering"):
                cert._load(path)


if __name__ == "__main__":
    unittest.main()
