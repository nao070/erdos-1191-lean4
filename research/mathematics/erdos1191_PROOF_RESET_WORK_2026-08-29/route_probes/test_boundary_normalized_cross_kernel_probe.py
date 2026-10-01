"""Exact tests for normalized Route C; Q1 and Q2 remain unresolved."""

from __future__ import annotations

import copy
import json
import unittest
from fractions import Fraction
from pathlib import Path

import boundary_normalized_cross_kernel_probe as probe

HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE / "boundary_normalized_cross_kernel_certificate.json"


class BoundaryNormalizedCrossKernelTests(unittest.TestCase):
    def setUp(self) -> None:
        self.kernels = (
            (Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)),
            (Fraction(3, 8), Fraction(1, 4), Fraction(3, 8)),
        )
        self.matrix = probe.matrix_b(Fraction(-1, 5))
        self.gamma = (Fraction(1, 2), Fraction(1, 2))

    def test_pd_gamma_and_leading_normalization(self) -> None:
        parameters = probe.normalized_parameters(self.kernels, self.matrix, self.gamma)
        self.assertEqual(parameters["beta"], Fraction(5, 8))
        self.assertEqual(parameters["s"], Fraction(8, 5))
        self.assertEqual(parameters["delta"], Fraction(1))
        self.assertEqual(probe.equality_gamma(self.matrix), self.gamma)

    def test_equality_gamma_requires_coordinatewise_attainability(self) -> None:
        positive_definite_with_bad_image = (
            (Fraction(1), Fraction(-2)),
            (Fraction(-2), Fraction(5)),
        )
        with self.assertRaises(probe.CertificateError):
            probe.equality_gamma(positive_definite_with_bad_image)

    def test_discrete_gate_and_block_lift_formula(self) -> None:
        expected = [Fraction(19, 32), Fraction(27, 80), Fraction(53, 320)]
        observed = [
            probe.discrete_cross_correlation(self.kernels, self.matrix, shift)
            for shift in range(3)
        ]
        self.assertEqual(observed, expected)
        self.assertTrue(probe.shift_gate(self.kernels, self.matrix))
        self.assertEqual(
            probe.block_lift_correlation(self.kernels, self.matrix, 4, 5),
            (3 * expected[1] + expected[2]) / 16,
        )

    def test_exact_cross_qp_and_supplied_values(self) -> None:
        problem = probe.boundary_problem(self.kernels, self.matrix, self.gamma, 2)
        certificate = probe.solve_boundary_qp(problem)
        probe.validate_qp_certificate(problem, certificate)
        metrics = probe.complete_metrics(problem, certificate)
        self.assertEqual(metrics["Phi"], Fraction(629198090085, 175479603614))
        self.assertEqual(metrics["a"], Fraction(57, 32))
        self.assertEqual(metrics["bH"], Fraction(361764546455, 701918414456))
        self.assertEqual(
            metrics["product"], Fraction(20620579147935, 22461389262592)
        )

    def test_same_kernel_baseline_and_exact_improvement(self) -> None:
        cross_problem = probe.boundary_problem(self.kernels, self.matrix, self.gamma, 2)
        cross = probe.complete_metrics(cross_problem, probe.solve_boundary_qp(cross_problem))
        base_problem = probe.boundary_problem(
            self.kernels, probe.matrix_b(Fraction(0)), self.gamma, 2
        )
        base = probe.complete_metrics(base_problem, probe.solve_boundary_qp(base_problem))
        self.assertEqual(base["Phi"], Fraction(82462667, 28528330))
        self.assertEqual(base["a"], Fraction(69, 32))
        self.assertEqual(base["bH"], Fraction(36547849, 85584990))
        self.assertEqual(base["product"], Fraction(840600527, 912906560))
        ratio = cross["product"] / base["product"]
        self.assertEqual(
            ratio, Fraction(1190831349642527325, 1194398763365825948)
        )
        self.assertLess(ratio, 1)

    def test_master_domain_and_correct_general_coefficient(self) -> None:
        problem = probe.boundary_problem(self.kernels, self.matrix, self.gamma, 2)
        metrics = probe.complete_metrics(problem, probe.solve_boundary_qp(problem))
        self.assertGreater(probe.master_bound(10, 400, 100, 2, metrics), 0)
        with self.assertRaises(probe.CertificateError):
            probe.master_bound(10, 399, 100, 2, metrics)
        payload = probe.build_payload()
        self.assertEqual(
            payload["general_theorem"]["secondary_coefficient"],
            "delta^(1/4)*sqrt(a*bH)",
        )

    def test_zero_gamma_coordinate_is_deleted_and_not_free(self) -> None:
        problem = probe.boundary_problem(
            self.kernels,
            probe.matrix_b(Fraction(0)),
            (Fraction(1), Fraction(0)),
            1,
        )
        self.assertEqual(problem["active_coordinates"], (0,))
        self.assertEqual(problem["variable_count"], problem["n"])
        certificate = probe.solve_boundary_qp(problem)
        mutated = copy.deepcopy(certificate)
        mutated["q"] = mutated["q"] + (Fraction(0),)
        with self.assertRaises(probe.CertificateError):
            probe.validate_qp_certificate(problem, mutated)

    def test_bounded_exhaustive_scope_counts_and_winners(self) -> None:
        result = probe.exhaustive_search()
        self.assertEqual(len(result["scope"]["negative_b_values"]), 21)
        self.assertEqual(result["cross_counts"]["m3_L2"]["kernel_count"], 5)
        self.assertEqual(result["cross_counts"]["m5_L2"]["kernel_count"], 15)
        self.assertEqual(result["cross_counts"]["m3_L2"]["exact_kkt_certified"], 121)
        self.assertEqual(result["cross_counts"]["m5_L2"]["exact_kkt_certified"], 834)
        self.assertEqual(
            result["best_cross_product"], "20620579147935/22461389262592"
        )
        self.assertEqual(
            result["best_diagonal_product"],
            "20720894357613941/23062969911203072",
        )
        self.assertEqual(result["best_diagonal_location"]["lambda"], "1/8")

    def test_diagonal_winner_exact_values(self) -> None:
        payload = probe.build_payload()
        metrics = payload["bounded_grid_diagonal_winner"]["metrics"]
        self.assertEqual(metrics["Phi"], "6624259711621393/720717809725096")
        self.assertEqual(metrics["a"], "85/64")
        self.assertEqual(metrics["bH"], "1218876138683173/1801794524312740")
        self.assertEqual(metrics["product"], "20720894357613941/23062969911203072")

    def test_all_adversarial_mutations_are_rejected(self) -> None:
        probe.mutation_checks()

    def test_semantic_hash_and_deterministic_byte_replay(self) -> None:
        probe.verify_certificate(CERTIFICATE)
        observed = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
        expected = probe.build_certificate()
        self.assertEqual(observed, expected)
        self.assertEqual(CERTIFICATE.read_bytes(), probe.render_certificate().encode("utf-8"))
        self.assertEqual(len(observed["canonical_payload_sha256"]), 64)


if __name__ == "__main__":
    unittest.main()
