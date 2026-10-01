#!/usr/bin/env python3
"""Regression tests for the exact ET fixed-prefix no-go certificate."""
from __future__ import annotations

import copy
from fractions import Fraction as F
import json
from pathlib import Path
import unittest

import et_fixed_prefix_no_go_certificate as probe


FIXTURE = Path(__file__).resolve().with_name("et_fixed_prefix_no_go_certificate.json")


class ETFixedPrefixNoGoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_01_least_prime_and_index_contract(self) -> None:
        expected = {8: 11, 16: 17, 32: 37, 64: 67, 128: 131, 256: 257, 512: 521}
        self.assertEqual({k: probe.least_prime_strictly_above(k) for k in probe.DYADIC_K}, expected)
        for k, p in expected.items():
            self.assertTrue(probe.is_prime(p))
            self.assertLess(k, p)
            self.assertLess(p, 2 * k)

    def test_02_et_sets_are_exact_sidon_rulers(self) -> None:
        for k in probe.DYADIC_K:
            p = probe.least_prime_strictly_above(k)
            points = probe.et_points(k, p)
            self.assertEqual(len(points), k)
            self.assertEqual(points[0], 0)
            self.assertTrue(all(left < right for left, right in zip(points, points[1:])))
            self.assertTrue(probe.is_sidon(points))
            self.assertLess(points[-1] + 1, 4 * k * k)
            gaps = probe.adjacent_gaps(points)
            self.assertTrue(all(p + 1 <= gap <= 3 * p - 1 for gap in gaps))

    def test_03_exact_log2_interval_and_schedule(self) -> None:
        lower, upper = probe.log_two_interval()
        self.assertLess(lower, upper)
        self.assertLess(upper - lower, F(1, 10**25))
        for k in probe.DYADIC_K:
            row = probe.schedule_record(k)
            self.assertEqual(row["T"], k * row["q"])
            self.assertIn(row["T_next"] // row["T"], (2, 4))
            self.assertEqual(row["q"], probe.ceil_power_of_two(F(row["threshold_upper"])))
            self.assertEqual(row["q_next"], probe.ceil_power_of_two(F(row["threshold_next_upper"])))

    def test_04_exact_centered_lowpass_and_analytic_bound(self) -> None:
        for k in probe.DYADIC_K:
            record = probe.fixture_record(k)
            points = probe.et_points(k, record["p"])
            for width_key, value_key, bound_key in (
                ("T", "C_T", "error_bound_T"),
                ("T_next", "C_T_next", "error_bound_T_next"),
            ):
                width = record[width_key]
                exact = probe.centered_lowpass(points, width)
                self.assertEqual(exact, F(record[value_key]))
                error = abs(exact - F(k, 2 * record["p"]))
                self.assertLessEqual(error, F(record[bound_key]))
                self.assertEqual(F(record[bound_key]), probe.approximation_error_bound(k, record["p"], width))
            self.assertEqual(F(record["X"]), F(record["C_T"]) - F(record["C_T_next"]))
            self.assertLessEqual(abs(F(record["X"])), F(record["X_error_bound"]))

    def test_05_formal_W_and_rational_lower(self) -> None:
        for k in probe.DYADIC_K:
            record = probe.fixture_record(k)
            points = probe.et_points(k, record["p"])
            audit = probe.formal_w_audit(points, k // 2)
            self.assertEqual(audit["formal_log_sha256"], record["W_formal_log_sha256"])
            self.assertEqual(audit["cells"], record["W_cells"])
            self.assertGreaterEqual(F(record["layered_rational_lower"]), F(record["simple_rational_lower"]))
            self.assertEqual(F(record["simple_rational_lower"]), F((k // 2 - 2) * (k // 2 - 1), 162 * (k // 2) ** 2))

    def test_06_fixed_prefix_no_go_contract(self) -> None:
        theorem = self.fixture["theorem_contract"]
        self.assertIn("for every fixed C>0 and K<infinity", theorem["quantifiers"])
        self.assertIn("changing finite family", theorem["boundary"])
        self.assertIn("does not construct one nested infinite branch", theorem["boundary"])
        self.assertTrue(theorem["refutes_single_prefix_uniform_comparison"])
        self.assertFalse(theorem["refutes_fixed_infinite_branch_history_theorem"])

    def test_07_scope_flags_are_all_conservative(self) -> None:
        scope = self.fixture["scope"]
        self.assertTrue(scope["finite_fixed_prefix_no_go"])
        for key in (
            "infinite_counterexample",
            "q1_resolved",
            "q2_resolved",
            "publication_ready_proof_of_1191",
            "prize_claim_ready",
            "novelty_claim",
        ):
            self.assertFalse(scope[key])

    def test_08_certificate_semantic_and_byte_replay(self) -> None:
        generated = probe.build_certificate()
        self.assertEqual(generated, self.fixture)
        self.assertEqual(FIXTURE.read_bytes(), probe.rendered_bytes(self.fixture))
        probe.validate_certificate(self.fixture)

    def test_09_hash_and_semantic_mutations_rejected(self) -> None:
        self.assertGreaterEqual(probe.self_check(self.fixture), 14)
        changed = copy.deepcopy(self.fixture)
        changed["scope"]["infinite_counterexample"] = True
        probe.rehash(changed)
        with self.assertRaises(probe.CertificateError):
            probe.validate_certificate(changed)

    def test_10_invalid_parameters_rejected(self) -> None:
        with self.assertRaises(ValueError):
            probe.et_points(7, 11)
        with self.assertRaises(ValueError):
            probe.et_points(8, 7)
        with self.assertRaises(ValueError):
            probe.centered_lowpass((0, 1), 0)
        with self.assertRaises(ValueError):
            probe.fixture_record(12)

    def test_11_every_embedded_record_replays(self) -> None:
        records = self.fixture["finite_fixtures"]
        self.assertEqual([row["k"] for row in records], list(probe.DYADIC_K))
        self.assertEqual(records, [probe.fixture_record(k) for k in probe.DYADIC_K])

    def test_12_proof_contract_contains_exact_bounds(self) -> None:
        proof = self.fixture["analytic_proof_contract"]
        self.assertIn("2k/S+4pk/S^2+S/(4p^2)+1/(2p)", proof["C_S_approximation"])
        self.assertIn("(n-2)(n-1)/(162n^2)", proof["W_lower"])
        self.assertIn("B/N tends to 1", proof["normalized_gain"])


if __name__ == "__main__":
    unittest.main()
