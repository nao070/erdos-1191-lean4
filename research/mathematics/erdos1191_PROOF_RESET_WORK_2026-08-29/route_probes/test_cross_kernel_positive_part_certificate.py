"""Exact tests for the Route-C positive-part/zero-mass no-go."""

from __future__ import annotations

import json
import unittest
from fractions import Fraction
from pathlib import Path

from cross_kernel_positive_part_certificate import (
    build_certificate,
    combined_correlation,
    correlation_table,
    direct_energy,
    exact_completion_slack,
    expansion_energy,
    gram_matrix,
    is_sidon,
    kernel_masses,
    mass_form_upper,
    point_mass,
    positive_negative_mass,
    positive_part_upper,
    quadratic,
    render_certificate,
    transformed_kernels,
    validate_model,
    verify_certificate,
)

HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE / "cross_kernel_positive_part_certificate.json"


class CrossKernelPositivePartTests(unittest.TestCase):
    def test_general_exact_completion_and_mass_identity(self) -> None:
        kernels = (
            {0: Fraction(1, 2), 1: Fraction(1, 2)},
            {0: Fraction(1, 3), 2: Fraction(2, 3)},
            {-1: Fraction(1, 4), 0: Fraction(1, 2), 2: Fraction(1, 4)},
        )
        factor = (
            (Fraction(1), Fraction(-1, 2), Fraction(2, 3)),
            (Fraction(0), Fraction(3, 4), Fraction(-1, 3)),
        )
        matrix = gram_matrix(factor)
        marks = (0, 1, 4, 6)
        self.assertTrue(is_sidon(marks))
        table = correlation_table(kernels, matrix)
        direct = direct_energy(marks, kernels, matrix)
        expansion = expansion_energy(marks, table)
        upper = positive_part_upper(len(marks), table)
        self.assertEqual(direct, expansion)
        self.assertEqual(upper - direct, exact_completion_slack(marks, table))
        self.assertGreaterEqual(upper, direct)
        self.assertEqual(upper, mass_form_upper(len(marks), kernels, matrix, table))
        positive, negative = positive_negative_mass(table)
        self.assertEqual(
            quadratic(kernel_masses(kernels), matrix),
            table[0] + 2 * (positive - negative),
        )

    def test_zero_mass_contrast_requires_negative_shift(self) -> None:
        kernels = (point_mass(0), point_mass(1))
        factor = ((Fraction(1), Fraction(-1)),)
        matrix = gram_matrix(factor)
        table = correlation_table(kernels, matrix)
        self.assertEqual(quadratic(kernel_masses(kernels), matrix), 0)
        self.assertEqual(table, {-1: Fraction(-1), 0: Fraction(2), 1: Fraction(-1)})
        positive, negative = positive_negative_mass(table)
        self.assertEqual(2 * negative, table[0] + 2 * positive)
        self.assertGreaterEqual(2 * negative, table[0])

    def test_psd_factorization_preserves_energy(self) -> None:
        kernels = (
            {0: Fraction(2, 3), 1: Fraction(1, 3)},
            {0: Fraction(1, 4), 2: Fraction(3, 4)},
        )
        factor = (
            (Fraction(1), Fraction(-2, 5)),
            (Fraction(1, 3), Fraction(4, 5)),
        )
        matrix = gram_matrix(factor)
        marks = (0, 1, 4, 6)
        effective = transformed_kernels(kernels, factor)
        transformed_energy = sum(
            (
                direct_energy(marks, (kernel,), ((Fraction(1),),))
                for kernel in effective
            ),
            Fraction(0),
        )
        self.assertEqual(direct_energy(marks, kernels, matrix), transformed_energy)

    def test_all_distinct_point_masses_cannot_beat_diagonal_baseline(self) -> None:
        locations = (0, 1, 4, 10, 12)
        kernels = tuple(point_mass(location) for location in locations)
        factor = (
            (Fraction(1), Fraction(-1), Fraction(1, 2), Fraction(0), Fraction(2, 3)),
            (Fraction(0), Fraction(1, 3), Fraction(-2, 5), Fraction(1), Fraction(-1, 4)),
        )
        matrix = gram_matrix(factor)
        table = correlation_table(kernels, matrix)
        trace = sum((matrix[index][index] for index in range(len(matrix))), Fraction(0))
        self.assertEqual(table[0], trace)
        positive, _ = positive_negative_mass(table)
        upper = positive_part_upper(7, table)
        self.assertEqual(upper, 7 * trace + 2 * positive)
        self.assertGreaterEqual(upper, 7 * trace)

    def test_mutations_and_invalid_models_are_rejected(self) -> None:
        kernels = (point_mass(0), point_mass(1))
        with self.assertRaises(ValueError):
            validate_model(kernels, ((Fraction(1),),))
        with self.assertRaises(ValueError):
            validate_model(
                kernels,
                ((Fraction(1), Fraction(1, 2)), (Fraction(1, 3), Fraction(1))),
            )
        matrix = ((Fraction(1), Fraction(-1)), (Fraction(-1), Fraction(1)))
        self.assertEqual(combined_correlation(kernels, matrix, 1), Fraction(-1))
        # Mutating the sign would make the explicit zero-mass identity fail.
        mutated = dict(correlation_table(kernels, matrix))
        mutated[1] = Fraction(1)
        positive, negative = positive_negative_mass(mutated)
        self.assertNotEqual(0, mutated[0] + 2 * (positive - negative))

    def test_empty_set_and_zero_kernel_degeneracies(self) -> None:
        kernels = ({},)
        matrix = ((Fraction(1),),)
        table = correlation_table(kernels, matrix)
        self.assertEqual(table, {0: Fraction(0)})
        self.assertTrue(is_sidon(()))
        self.assertEqual(direct_energy((), kernels, matrix), Fraction(0))
        self.assertEqual(expansion_energy((), table), Fraction(0))
        self.assertEqual(direct_energy((0, 2), kernels, matrix), Fraction(0))
        self.assertEqual(expansion_energy((0, 2), table), Fraction(0))

    def test_certificate_replays_byte_for_byte(self) -> None:
        verify_certificate(CERTIFICATE)
        observed = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
        self.assertEqual(observed, build_certificate())
        self.assertEqual(CERTIFICATE.read_bytes(), render_certificate().encode("utf-8"))
        self.assertEqual(len(observed["canonical_payload_sha256"]), 64)
        self.assertIn("Questions 1 and 2 remain unresolved", observed["payload"]["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
