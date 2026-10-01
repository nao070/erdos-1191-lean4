from __future__ import annotations

from fractions import Fraction
import unittest

from fixed_depth_no_go import (
    erdos_turan_fixed_depth_witness,
    is_prime,
    least_prime_at_least,
)


class FixedDepthNoGoTests(unittest.TestCase):
    def test_prime_helpers(self) -> None:
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(21))
        self.assertEqual(least_prime_at_least(32), 37)

    def test_exact_shell_decomposition(self) -> None:
        for count in (16, 32, 64):
            witness = erdos_turan_fixed_depth_witness(count)
            self.assertEqual(
                witness.normalized_birth_shell,
                witness.normalized_birth_diagonal
                + witness.normalized_birth_off_diagonal,
            )
            self.assertGreater(witness.normalized_birth_off_diagonal, 0)

    def test_asymptotic_constants_on_large_structured_witness(self) -> None:
        witness = erdos_turan_fixed_depth_witness(512)
        self.assertLess(
            abs(witness.full_normalized_variance - Fraction(1, 180)),
            Fraction(1, 2000),
        )
        self.assertLess(
            abs(witness.normalized_matrix_innovation_00 - Fraction(1, 360)),
            Fraction(1, 2000),
        )
        self.assertLess(
            abs(witness.normalized_birth_shell - Fraction(19, 3840)),
            Fraction(1, 1000),
        )
        self.assertLess(witness.normalized_birth_diagonal, Fraction(1, 512**2))


if __name__ == "__main__":
    unittest.main()
