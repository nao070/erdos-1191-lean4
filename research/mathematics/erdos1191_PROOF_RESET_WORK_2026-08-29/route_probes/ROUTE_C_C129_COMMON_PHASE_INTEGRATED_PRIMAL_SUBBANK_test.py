#!/usr/bin/env python3
"""Regression tests for the C129 exact integrated primal sub-bank."""

from __future__ import annotations

import copy
from fractions import Fraction as F
import importlib
import json
from pathlib import Path
import tempfile
import unittest


MODULE = "ROUTE_C_C129_COMMON_PHASE_INTEGRATED_PRIMAL_SUBBANK_certificate"


class C129IntegratedPrimalSubBankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cert = importlib.import_module(MODULE)
        cls.value = json.loads(cls.cert.DEFAULT_CERTIFICATE.read_text())
        cls.summary = cls.cert.verify_certificate(cls.value)

    def test_sparse_seven_exactly_crosses_after_top_six(self) -> None:
        self.assertEqual(
            self.summary["minimal_sparse7"]["surplus_indices"],
            (88, 120, 122, 126, 132, 133, 134),
        )
        self.assertLess(self.summary["top6"]["raw_margin_upper"], F(0))
        self.assertGreater(
            self.summary["minimal_sparse7"]["raw_margin_lower"], F(1, 15_000)
        )
        self.assertGreater(
            self.summary["minimal_sparse7"]["normalized_margin_lower"],
            F(99, 1_000_000),
        )

    def test_robust_ten_has_exact_clean_integrated_margin(self) -> None:
        robust = self.summary["robust10"]
        self.assertEqual(
            robust["surplus_indices"],
            (43, 88, 119, 120, 122, 124, 126, 132, 133, 134),
        )
        self.assertGreater(robust["raw_margin_lower"], F(143, 400_000))
        self.assertGreater(robust["normalized_margin_lower"], F(103, 200_000))
        self.assertEqual(robust["chambers"], 32)

    def test_exact_gram_owner_and_rank_census_is_frozen(self) -> None:
        robust = self.summary["robust10"]
        sparse = self.summary["minimal_sparse7"]
        self.assertEqual(robust["factors"], 64)
        self.assertEqual(robust["generic_owner_rows"], 12_140)
        self.assertEqual(robust["generic_owner_endpoint_checks"], 24_280)
        self.assertEqual(robust["collapsed_endpoint_owner_rows"], 23_745)
        self.assertEqual((robust["rank_min"], robust["rank_max"]), (9, 24))
        self.assertEqual(robust["rank_sum"], 1004)
        self.assertEqual(sparse["factors"], 58)
        self.assertEqual(sparse["generic_owner_rows"], 10_987)
        self.assertEqual(sparse["generic_owner_endpoint_checks"], 21_974)
        self.assertEqual(sparse["collapsed_endpoint_owner_rows"], 21_500)
        self.assertEqual(sparse["rank_sum"], 910)
        self.assertTrue(robust["all_owner_rows_strictly_positive"])
        self.assertTrue(robust["all_factor_columns_independent"])
        self.assertEqual(robust["denominators"], (100_000_000,))

    def test_scope_preserves_every_unresolved_gate(self) -> None:
        scope = self.value["scope"]
        self.assertTrue(scope["exact_selected_29_chamber_integrated_subbank_constructed"])
        self.assertTrue(scope["exact_selected_32_chamber_integrated_subbank_constructed"])
        self.assertFalse(scope["complete_C123_phase_primal_witness_constructed"])
        self.assertFalse(scope["remaining_103_chambers_exactified"])
        self.assertFalse(scope["global_phase_rule_admissible_proved"])
        self.assertFalse(scope["local_master_inequality_proved"])
        self.assertFalse(scope["arbitrary_rank_proved"])
        self.assertFalse(scope["C058_resolved"])
        self.assertFalse(scope["Q1_Q2_resolved"])

    def test_factor_mutation_is_rejected_even_after_rehash(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["factor_bank"]["records"][0]["n4"]["columns"][0][0] += 1
        changed["integrity"]["factor_bank_sha256"] = self.cert._object_hash(
            changed["factor_bank"]
        )
        changed["integrity"]["payload_sha256"] = self.cert.payload_hash(changed)
        with self.assertRaisesRegex(self.cert.CertificateError, "factor bank hash changed"):
            self.cert.verify_certificate(changed)

    def test_canonical_payload_and_mutation_barrier(self) -> None:
        self.assertEqual(self.cert._load(self.cert.DEFAULT_CERTIFICATE), self.value)
        mutation_summary = self.cert.self_check(self.value)
        self.assertEqual(mutation_summary["mutations_rejected"], 21)

    def test_epoch_objective_mismatch_is_rejected_despite_weighted_cancellation(self) -> None:
        endpoint4, endpoint8 = F(2), F(3)
        expected4, expected8 = F(1), F(43, 9)
        self.assertEqual(
            endpoint4 + self.cert.RHO * endpoint8,
            expected4 + self.cert.RHO * expected8,
        )
        with self.assertRaisesRegex(
            self.cert.CertificateError, "epoch-4 collapsed objective mismatch"
        ):
            self.cert._check_collapsed_objectives(
                index=0,
                endpoint_phi4=endpoint4,
                endpoint_phi8=endpoint8,
                expected_phi4=expected4,
                expected_phi8=expected8,
            )

    def test_epoch_owner_recovery_mismatch_is_rejected_despite_total_cancellation(self) -> None:
        physical = {4: F(1), 8: F(4)}
        owners = ((4, 1), (8, 1))
        owned = (F(2), F(3))
        self.assertEqual(sum(owned, F()), physical[4] + physical[8])
        with self.assertRaisesRegex(
            self.cert.CertificateError,
            "epoch-4 owner shares do not recover physical energy",
        ):
            self.cert._check_epoch_owner_recovery(
                physical=physical,
                owned=owned,
                owners=owners,
            )

    def test_structural_zero_row_rejects_nonzero_owner_share_even_for_negative_demand(self) -> None:
        with self.assertRaisesRegex(
            self.cert.CertificateError,
            "structural-zero owner share is nonzero",
        ):
            self.cert._check_structural_zero_owner(
                index=0,
                context="generic",
                owner_value=-F(1),
                demand=-F(1),
            )


class C129CanonicalRenderingTests(unittest.TestCase):
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
