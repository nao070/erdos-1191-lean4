"""Exact tests for the finite probe; Q1 and Q2 remain unresolved."""

from __future__ import annotations

import copy
import unittest
from fractions import Fraction
from pathlib import Path

from overlapping_kernel_probe import (
    MissingBoundaryFunctionalError,
    build_payload,
    canonical_pd_coefficient,
    combined_correlation,
    enumerate_grid,
    gate_criterion,
    gated_energy_formula,
    is_pd_parameter,
    is_psd_parameter,
    mutation_checks,
    positive_part_energy,
    pure_energy_difference_formula,
    render_certificate,
    shift_gate_passes,
    t_family,
    validate_boundary_claim,
    verify_certificate,
)

HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE / "overlapping_kernel_certificate.json"


class OverlappingKernelProbeTests(unittest.TestCase):
    def test_psd_and_pd_ranges_are_exact(self) -> None:
        self.assertTrue(is_psd_parameter(Fraction(-1)))
        self.assertFalse(is_pd_parameter(Fraction(-1)))
        self.assertTrue(is_pd_parameter(Fraction(-1, 2)))
        self.assertFalse(is_psd_parameter(Fraction(-3, 2)))

    def test_no_positive_B_case_is_not_encoded_as_zero_rho(self) -> None:
        point = (Fraction(1),)
        result = gate_criterion(point, point)
        self.assertIsNone(result["rho"])
        self.assertFalse(result["has_positive_cross_shift"])
        self.assertTrue(result["negative_feasible"])
        self.assertTrue(shift_gate_passes(point, point, Fraction(-1, 2)))
        self.assertTrue(shift_gate_passes(point, point, Fraction(-1)))
        self.assertFalse(is_pd_parameter(Fraction(-1)))
        self.assertEqual(canonical_pd_coefficient(point, point), Fraction(-1, 2))

    def test_rho_one_psd_endpoint_and_pd_infimum(self) -> None:
        identical = (Fraction(1, 2), Fraction(1, 2))
        result = gate_criterion(identical, identical)
        self.assertEqual(result["rho"], Fraction(1))
        self.assertTrue(shift_gate_passes(identical, identical, Fraction(-1)))
        self.assertTrue(is_psd_parameter(Fraction(-1)))
        self.assertFalse(is_pd_parameter(Fraction(-1)))
        self.assertEqual(positive_part_energy(identical, identical, Fraction(-1), 3), 0)
        energies = [
            positive_part_energy(identical, identical, Fraction(-1) + epsilon, 3)
            for epsilon in (Fraction(1, 2), Fraction(1, 4), Fraction(1, 8))
        ]
        self.assertTrue(all(energy > 0 for energy in energies))
        self.assertGreater(energies[0], energies[1])
        self.assertGreater(energies[1], energies[2])

    def test_minimal_half_grid_witness(self) -> None:
        first = (Fraction(1), Fraction(0))
        second = (Fraction(1, 2), Fraction(1, 2))
        coefficient = Fraction(-1, 2)
        self.assertEqual(combined_correlation(first, second, coefficient, 0), Fraction(1))
        self.assertEqual(combined_correlation(first, second, coefficient, 1), Fraction(0))
        self.assertTrue(shift_gate_passes(first, second, coefficient))
        self.assertEqual(positive_part_energy(first, second, coefficient, 2), Fraction(2))
        self.assertEqual(gated_energy_formula(first, second, coefficient, 2), Fraction(2))
        self.assertEqual(pure_energy_difference_formula(first, second, coefficient, 2), Fraction(-3, 2))

    def test_full_support_denominator_four_witness(self) -> None:
        first = (Fraction(1, 4), Fraction(1, 4), Fraction(1, 2))
        second = (Fraction(1, 4), Fraction(1, 2), Fraction(1, 4))
        coefficient = Fraction(-7, 8)
        self.assertEqual(combined_correlation(first, second, coefficient, 0), Fraction(13, 64))
        self.assertEqual(combined_correlation(first, second, coefficient, 1), Fraction(0))
        self.assertEqual(combined_correlation(first, second, coefficient, 2), Fraction(3, 128))
        self.assertEqual(positive_part_energy(first, second, coefficient, 2), Fraction(29, 64))

    def test_exact_grid_enumerations(self) -> None:
        half = enumerate_grid(2)
        self.assertEqual(half["kernel_count"], 6)
        self.assertEqual(half["distinct_overlapping_pair_count"], 9)
        self.assertEqual(half["feasible_strict_gain_count"], 8)
        self.assertEqual(half["best_ratio"], Fraction(4, 7))

        full = enumerate_grid(4, full_support=True)
        self.assertEqual(full["kernel_count"], 3)
        self.assertEqual(full["distinct_overlapping_pair_count"], 3)
        self.assertEqual(full["feasible_strict_gain_count"], 3)
        self.assertEqual(full["best_ratio"], Fraction(29, 176))

    def test_rational_family_and_degenerating_normalization(self) -> None:
        ratios = []
        for t_value in (Fraction(1, 3), Fraction(1, 6), Fraction(1, 12)):
            record = t_family(t_value)
            expected_b = -1 + 2 * t_value * t_value
            expected_c0 = 4 * t_value * t_value
            expected_ratio = (8 * t_value * t_value) / (3 + 2 * t_value * t_value)
            self.assertEqual(Fraction(record["b"]), expected_b)
            self.assertEqual(Fraction(record["C0"]), expected_c0)
            self.assertEqual(Fraction(record["total_mass"]), expected_c0)
            self.assertEqual(Fraction(record["small_eigenvalue"]), 2 * t_value * t_value)
            self.assertEqual(Fraction(record["ratio"]), expected_ratio)
            ratios.append(Fraction(record["ratio"]))
        self.assertGreater(ratios[0], ratios[1])
        self.assertGreater(ratios[1], ratios[2])

    def test_pure_gain_identity_on_multiple_kernels_and_cardinalities(self) -> None:
        fixtures = (
            (
                (Fraction(1), Fraction(0)),
                (Fraction(1, 2), Fraction(1, 2)),
                Fraction(-1, 2),
            ),
            (
                (Fraction(1, 4), Fraction(1, 4), Fraction(1, 2)),
                (Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)),
                Fraction(-7, 8),
            ),
            (
                (Fraction(1, 3), Fraction(2, 3)),
                (Fraction(1, 2), Fraction(1, 2)),
                Fraction(-17, 18),
            ),
        )
        for first, second, coefficient in fixtures:
            for cardinality in (1, 2, 5, 9):
                actual = positive_part_energy(first, second, coefficient, cardinality)
                baseline = positive_part_energy(first, second, Fraction(0), cardinality)
                formula = pure_energy_difference_formula(
                    first, second, coefficient, cardinality
                )
                self.assertEqual(actual - baseline, formula)

    def test_mutations_reject_sign_psd_and_boundary_overclaim(self) -> None:
        mutation_checks()
        mutated = copy.deepcopy(build_payload())
        boundary = mutated["hou_zhao_boundary_cover"]
        boundary["useful_sidon_inequality_claimed"] = True
        with self.assertRaises(MissingBoundaryFunctionalError):
            validate_boundary_claim(mutated)

    def test_certificate_replay_is_byte_exact(self) -> None:
        verify_certificate(CERTIFICATE)
        self.assertEqual(CERTIFICATE.read_bytes(), render_certificate().encode("utf-8"))


if __name__ == "__main__":
    unittest.main()
