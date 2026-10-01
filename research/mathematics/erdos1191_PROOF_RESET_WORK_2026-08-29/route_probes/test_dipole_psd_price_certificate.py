#!/usr/bin/env python3
"""Regression tests for the active dipole PSD-price certificate."""
from __future__ import annotations

import copy
from fractions import Fraction as F
import json
from pathlib import Path
import unittest

import dipole_psd_price_certificate as probe


FIXTURE = Path(__file__).resolve().with_name("dipole_psd_price_certificate.json")


class DipolePSDPriceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_01_weighted_completion_primal_dual(self) -> None:
        row = probe.completion_fixture()
        self.assertEqual(F(row["primal_weighted_diagonal_cost"]), F(12416, 1155))
        self.assertEqual(F(row["primal_weighted_diagonal_cost"]), F(row["rank_one_dual_value"]))
        self.assertTrue(row["strong_duality_verified"])

    def test_02_rank_one_edge_blocks_are_psd(self) -> None:
        for row in probe.completion_fixture()["edge_blocks"]:
            self.assertGreater(F(row["upper_left"]), 0)
            self.assertGreater(F(row["lower_right"]), 0)
            self.assertEqual(F(row["determinant"]), 0)

    def test_03_pointwise_price_dominates_twice_tent(self) -> None:
        for row in probe.pointwise_price_rows():
            self.assertGreaterEqual(F(row["psi"]), 0)
            self.assertGreaterEqual(F(row["g_product_minus_4psi_squared"]), 0)

    def test_04_golomb_fixture_has_28_differences(self) -> None:
        row = probe.golomb_obstruction_fixture()
        self.assertEqual(row["difference_count"], 28)
        self.assertEqual(len(set(row["positive_differences"])), 28)

    def test_05_exact_logarithmic_separation(self) -> None:
        row = probe.golomb_obstruction_fixture()
        self.assertGreater(F(row["two_wave_lower_minus_gothic_upper"]), 0)
        self.assertTrue(row["strict_separation_verified"])

    def test_06_direct_sign_fixture_is_bipartite(self) -> None:
        row = probe.golomb_obstruction_fixture()
        colors = {int(vertex): color for vertex, color in row["bipartition"].items()}
        for left, right in row["complete_wave_edges"]:
            self.assertNotEqual(colors[left], colors[right])
        self.assertTrue(row["direct_sign_fixture_is_bipartite"])

    def test_07_nonlocalized_price_diverges(self) -> None:
        row = probe.golomb_obstruction_fixture()
        self.assertEqual(F(row["nonlocalized_price_coefficient_over_T"]), F(17, 32))
        self.assertTrue(row["nonlocalized_integral_diverges_at_zero"])

    def test_08_certificate_semantic_and_byte_replay(self) -> None:
        generated = probe.build_certificate()
        self.assertEqual(generated, self.fixture)
        self.assertEqual(FIXTURE.read_bytes(), probe.rendered_bytes(self.fixture))
        probe.validate_certificate(self.fixture)

    def test_09_mutations_are_rejected(self) -> None:
        self.assertEqual(probe.self_check(self.fixture), 8)
        changed = copy.deepcopy(self.fixture)
        changed["scope"]["question_1_resolved"] = True
        probe.rehash(changed)
        with self.assertRaises(probe.CertificateError):
            probe.validate_certificate(changed)

    def test_10_scope_preserves_surviving_routes(self) -> None:
        scope = self.fixture["scope"]
        self.assertTrue(scope["weighted_coefficient_psd_price_exact"])
        self.assertFalse(scope["gram_restricted_route_ruled_out"])
        self.assertFalse(scope["signed_cancellation_ruled_out"])
        self.assertFalse(scope["cross_epoch_payment_ruled_out"])
        self.assertFalse(scope["larger_psd_master_ruled_out"])
        self.assertFalse(scope["c058_resolved"])
        self.assertFalse(scope["question_1_resolved"])
        self.assertFalse(scope["question_2_resolved"])
        self.assertFalse(scope["prize_claim_ready"])


if __name__ == "__main__":
    unittest.main()
