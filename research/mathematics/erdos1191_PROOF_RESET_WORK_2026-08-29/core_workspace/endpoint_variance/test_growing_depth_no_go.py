from __future__ import annotations

from fractions import Fraction
import unittest

from growing_depth_no_go import (
    erdos_turan_points_without_quadratic_check,
    growing_depth_erdos_turan_witness,
    logarithmic_window_depth,
    logarithmic_window_sufficient_condition,
    normalized_gap_innovation_00,
)
from gap_measure_dynamics import dyadic_gap_matrix_update
from sidon_block_variance import is_golomb_ruler


class GrowingDepthNoGoTests(unittest.TestCase):
    def test_logarithmic_depth_and_exact_critical_condition(self) -> None:
        self.assertEqual(logarithmic_window_depth(8), 1)
        self.assertEqual(logarithmic_window_depth(16), 2)
        self.assertEqual(logarithmic_window_depth(32), 3)
        for scale_index in range(8, 10_001):
            depth = logarithmic_window_depth(scale_index)
            self.assertTrue(
                all(
                    logarithmic_window_sufficient_condition(scale_index, offset)
                    for offset in range(depth + 1)
                )
            )

    def test_fast_erdos_turan_constructor_matches_golomb_oracle(self) -> None:
        for count, prime in ((8, 11), (16, 17), (32, 37)):
            points = erdos_turan_points_without_quadratic_check(count, prime)
            self.assertTrue(is_golomb_ruler(points))
        points = erdos_turan_points_without_quadratic_check(32, 37)
        update = dyadic_gap_matrix_update(points, 16)
        self.assertEqual(
            normalized_gap_innovation_00(points, 16),
            update.innovation[0][0] / update.new_modulus,
        )

    def test_window_statistics_and_exact_sums(self) -> None:
        witness = growing_depth_erdos_turan_witness(16)
        self.assertEqual(witness.depth, 2)
        self.assertEqual(
            tuple(record.mark_count for record in witness.scales),
            (16_384, 32_768, 65_536),
        )
        self.assertEqual(
            witness.variance_sum,
            sum((record.normalized_variance for record in witness.scales), Fraction(0)),
        )
        self.assertEqual(
            witness.innovation_00_sum,
            sum(
                (record.normalized_innovation_00 for record in witness.transitions),
                Fraction(0),
            ),
        )
        self.assertEqual(
            witness.same_modulus_birth_shell_sum,
            sum(
                (record.same_modulus_birth_shell for record in witness.transitions),
                Fraction(0),
            ),
        )
        for record in witness.scales:
            self.assertLessEqual(
                record.kolmogorov_discrepancy,
                Fraction(4, record.mark_count),
            )
            self.assertLess(
                abs(record.normalized_variance - Fraction(1, 180)),
                Fraction(1, 1000),
            )
        for record in witness.transitions:
            self.assertLess(
                abs(record.normalized_innovation_00 - Fraction(1, 360)),
                Fraction(1, 1000),
            )
            self.assertLess(
                abs(record.same_modulus_birth_shell - Fraction(19, 3840)),
                Fraction(1, 1000),
            )


if __name__ == "__main__":
    unittest.main()
