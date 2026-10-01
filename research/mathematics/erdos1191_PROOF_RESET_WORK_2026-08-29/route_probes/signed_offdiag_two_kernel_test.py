"""Deterministic exact tests; Questions 1 and 2 remain unresolved."""

from __future__ import annotations

import json
import unittest
from fractions import Fraction
from pathlib import Path

from signed_offdiag_two_kernel_probe import (
    build_certificate,
    combined_correlation,
    correlation_table,
    direct_energy,
    energy_from_correlation,
    filled_shift_value,
    gram,
    point_mass,
    positive_part_value,
    psd_2x2,
    render_certificate,
    search_unit_diagonal,
    verify_certificate,
)

HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE / "signed_offdiag_two_kernel_certificate.json"


class SignedOffDiagonalTwoKernelTests(unittest.TestCase):
    def setUp(self) -> None:
        self.kernels = (point_mass(0), point_mass(1))

    def test_exact_psd_constraints_reject_bad_matrices(self) -> None:
        self.assertTrue(psd_2x2(gram(Fraction(1), Fraction(-1, 2), Fraction(1)), definite=True))
        self.assertTrue(psd_2x2(gram(Fraction(1), Fraction(-1), Fraction(1))))
        self.assertFalse(psd_2x2(gram(Fraction(1), Fraction(-1), Fraction(1)), definite=True))
        self.assertFalse(psd_2x2(gram(Fraction(1), Fraction(-2), Fraction(1))))
        nonsymmetric = ((Fraction(1), Fraction(1, 2)), (Fraction(1, 3), Fraction(1)))
        self.assertFalse(psd_2x2(nonsymmetric))

    def test_correlation_is_computed_from_definition(self) -> None:
        matrix = gram(Fraction(1), Fraction(-1, 2), Fraction(1))
        self.assertEqual(
            correlation_table(self.kernels, matrix),
            {-1: Fraction(-1, 2), 0: Fraction(2), 1: Fraction(-1, 2)},
        )

    def test_minimal_sidonic_avoidance_witness(self) -> None:
        matrix = gram(Fraction(1), Fraction(-1, 2), Fraction(1))
        witness = (0, 2)
        actual = direct_energy(witness, self.kernels, matrix)
        self.assertEqual(actual, Fraction(4))
        self.assertEqual(energy_from_correlation(witness, self.kernels, matrix), actual)
        self.assertEqual(filled_shift_value(2, self.kernels, matrix), Fraction(3))
        self.assertEqual(positive_part_value(2, self.kernels, matrix), Fraction(4))

    def test_represented_negative_shift_does_not_create_same_violation(self) -> None:
        matrix = gram(Fraction(1), Fraction(-1, 2), Fraction(1))
        represented = (0, 1)
        self.assertEqual(direct_energy(represented, self.kernels, matrix), Fraction(3))
        self.assertEqual(filled_shift_value(2, self.kernels, matrix), Fraction(3))

    def test_exact_search_has_no_feasible_signed_gain(self) -> None:
        result = search_unit_diagonal(12)
        self.assertEqual(result["positive_definite_candidates_checked"], 91)
        self.assertEqual(result["negative_cross_candidates_checked"], 45)
        self.assertEqual(result["feasible_strict_gain_count"], 0)
        self.assertEqual(result["minimal_obstruction_parameter"], "-1/2")

    def test_certificate_is_deterministic_hashed_and_replays(self) -> None:
        verify_certificate(CERTIFICATE)
        observed = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
        self.assertEqual(observed, build_certificate())
        self.assertEqual(CERTIFICATE.read_bytes(), render_certificate().encode("utf-8"))
        self.assertEqual(len(observed["canonical_payload_sha256"]), 64)
        self.assertIn("Questions 1 and 2 remain unresolved", observed["payload"]["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
