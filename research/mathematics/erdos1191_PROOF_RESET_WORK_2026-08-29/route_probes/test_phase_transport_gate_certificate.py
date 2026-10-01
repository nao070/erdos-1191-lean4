#!/usr/bin/env python3
"""Exact regression tests for the phase-transport gate certificate."""
from __future__ import annotations

import copy
from fractions import Fraction as F
import json
from pathlib import Path
import unittest

import phase_transport_gate_certificate as probe


FIXTURE = Path(__file__).resolve().with_name("phase_transport_gate_certificate.json")


class PhaseTransportGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_01_rational_dyadic_phase(self) -> None:
        self.assertEqual(probe.power_two(-3), F(1, 8))
        self.assertEqual(probe.power_two(0), F(1))
        self.assertEqual(probe.power_two(5), F(32))

    def test_02_exact_prefix_scale_curl(self) -> None:
        certificate = probe.build_certificate()
        self.assertTrue(certificate["curl_rows"])
        self.assertTrue(all(row["equal"] for row in certificate["curl_rows"]))
        self.assertTrue(
            all(
                F(row["delta_scale_difference"]) == F(row["band_prefix_difference"])
                for row in certificate["curl_rows"]
            )
        )

    def test_03_scale_abel_has_explicit_terminal(self) -> None:
        certificate = probe.build_certificate()
        for row in certificate["scale_abel_rows"]:
            self.assertEqual(F(row["lhs"]), F(row["band_bulk"]) + F(row["scale_terminal"]))
            self.assertTrue(row["identity_verified"])

    def test_04_epoch_transport_all_boundaries(self) -> None:
        row = probe.build_certificate()["finite_epoch_transport"]
        rhs = (
            F(row["initial_epoch_boundary"])
            + F(row["interior_band_bulk"])
            + F(row["terminal_epoch_boundary"])
            + F(row["scale_terminal_boundary"])
        )
        self.assertEqual(F(row["lhs"]), rhs)
        self.assertEqual(F(row["rhs"]), rhs)
        self.assertTrue(row["identity_verified"])

    def test_05_naive_negative_infinite_geometric_cumulative(self) -> None:
        for scale in range(-12, 12):
            self.assertEqual(
                probe.naive_cumulative(8, 3, scale) - probe.naive_cumulative(8, 3, scale - 1),
                probe.naive_coefficient(8, 3, scale),
            )

    def test_06_naive_gate_is_exact_iff(self) -> None:
        weight = probe.fejer_weight(1, 10)
        next_weight = probe.fejer_weight(2, 10)
        passing = probe.naive_gate(weight, next_weight, 2, 4, 2, 4)
        failing = probe.naive_gate(weight, next_weight, 2, 4, 2, 5)
        self.assertEqual(F(passing["threshold_for_horizon_growth"]), F(400, 81))
        self.assertEqual(F(passing["horizon_growth"]), F(4))
        self.assertTrue(passing["all_band_coefficients_nonnegative"])
        self.assertEqual(F(failing["horizon_growth"]), F(8))
        self.assertFalse(failing["all_band_coefficients_nonnegative"])

    def test_07_small_interior_negative_counterfixture(self) -> None:
        row = probe.build_certificate()["naive_gate_counterfixture"]
        self.assertEqual(row["interior_epoch"], 1)
        self.assertEqual(row["fejer_horizon"], 10)
        self.assertEqual(row["negative_witness_scale"], 5)
        self.assertEqual(F(row["negative_witness_b"]), F(-62, 121))

    def test_08_certificate_semantic_and_byte_replay(self) -> None:
        generated = probe.build_certificate()
        self.assertEqual(generated, self.fixture)
        self.assertEqual(FIXTURE.read_bytes(), probe.rendered_bytes(self.fixture))
        probe.validate_certificate(self.fixture)

    def test_09_hash_and_scope_mutations_rejected(self) -> None:
        self.assertEqual(probe.self_check(self.fixture), 5)
        changed = copy.deepcopy(self.fixture)
        changed["scope"]["question_1_resolved"] = True
        probe.rehash(changed)
        with self.assertRaises(probe.CertificateError):
            probe.validate_certificate(changed)


if __name__ == "__main__":
    unittest.main()
