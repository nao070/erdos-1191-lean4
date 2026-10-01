from __future__ import annotations

from fractions import Fraction
import unittest

from prefix_monotonicity import (
    direct_same_modulus_prefix_variance,
    doubled_prefix_comparison,
    four_mark_full_variance_lower_bound,
    prefix_monotonicity_counterfamily,
    same_modulus_prefix_variance,
)
from sidon_block_variance import is_golomb_ruler


class PrefixMonotonicityTests(unittest.TestCase):
    def test_exact_minimal_sidon_counterexample(self) -> None:
        points = (0, 20, 21, 39)
        comparison = doubled_prefix_comparison(points, 2, 40)
        self.assertTrue(is_golomb_ruler(points))
        self.assertEqual(comparison.prefix_variance, Fraction(1, 4))
        self.assertEqual(comparison.full_variance, Fraction(99, 400))
        self.assertEqual(comparison.change, Fraction(-1, 400))

    def test_counterfamily_exact_formulas(self) -> None:
        for modulus in range(40, 101):
            points = prefix_monotonicity_counterfamily(modulus)
            comparison = doubled_prefix_comparison(points, 2, modulus)
            self.assertEqual(
                comparison.prefix_variance,
                Fraction(modulus * modulus // 4, modulus * modulus),
            )
            self.assertEqual(
                comparison.full_variance,
                Fraction(10 * modulus - 4, modulus * modulus),
            )
            self.assertLess(comparison.full_variance, comparison.prefix_variance)

    def test_same_modulus_formula_matches_literal_oracle(self) -> None:
        for modulus in range(40, 51):
            points = prefix_monotonicity_counterfamily(modulus)
            for prefix_count in (2, 4):
                self.assertEqual(
                    same_modulus_prefix_variance(points, prefix_count, modulus),
                    direct_same_modulus_prefix_variance(points, prefix_count, modulus),
                )

    def test_sharp_four_mark_lower_bound(self) -> None:
        for modulus in range(4, 60):
            equality_points = (0, 1, 2, modulus - 1)
            self.assertEqual(
                same_modulus_prefix_variance(equality_points, 4, modulus),
                four_mark_full_variance_lower_bound(modulus),
            )


if __name__ == "__main__":
    unittest.main()
