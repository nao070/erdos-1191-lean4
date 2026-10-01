from __future__ import annotations

from fractions import Fraction
import unittest

from cross_block_profile import (
    cross_band_witness,
    diameter_profile_discrepancy,
    dyadic_tree_carleson_witness,
    profile_discrepancy_lower_bound,
    same_lag_packing_witness,
)
from growing_depth_no_go import (
    erdos_turan_points_without_quadratic_check,
    gap_measure_kolmogorov_discrepancy,
)
from gap_measure_dynamics import (
    dyadic_gap_matrix_update,
    normalized_gap_function_variance,
)


class CrossBlockProfileTests(unittest.TestCase):
    def setUp(self) -> None:
        self.points = erdos_turan_points_without_quadratic_check(32, 37)

    def test_profile_brackets_kolmogorov_with_one_grid_step(self) -> None:
        profile = diameter_profile_discrepancy(self.points)
        kolmogorov = gap_measure_kolmogorov_discrepancy(self.points)
        self.assertGreaterEqual(kolmogorov, profile)
        self.assertLessEqual(
            kolmogorov,
            profile + Fraction(1, len(self.points)),
        )

    def test_cross_band_and_same_lag_formulas_are_literal(self) -> None:
        band = cross_band_witness(self.points, 0, 8, 16, 24)
        literal = {
            self.points[right] - self.points[left]
            for left in range(0, 8)
            for right in range(16, 24)
        }
        self.assertEqual(band.difference_count, 64)
        self.assertEqual(band.minimum_difference, min(literal))
        self.assertEqual(band.maximum_difference, max(literal))
        self.assertEqual(band.band_length, max(literal) - min(literal) + 1)

        for lag in (1, 2, 3):
            witness = same_lag_packing_witness(self.points, block_count=4, lag=lag)
            self.assertEqual(witness.difference_count, (4 - lag) * 8 * 8)
            self.assertLessEqual(
                witness.difference_count,
                witness.exact_global_band_length,
            )
            self.assertLessEqual(
                witness.exact_global_band_length,
                witness.discrepancy_band_upper_bound,
            )

    def test_dyadic_cross_spectra_partition_and_pack(self) -> None:
        witness = dyadic_tree_carleson_witness(self.points)
        self.assertEqual(witness.total_cross_differences, 32 * 31 // 2)
        self.assertEqual(len(witness.nodes), 31)
        self.assertLessEqual(
            witness.weighted_span_sum,
            witness.running_count_upper_sum,
        )
        self.assertTrue(all(node.span >= node.running_count for node in witness.nodes))

    def test_exact_profile_lower_bound_from_an_old_critical_block(self) -> None:
        block_count = 4
        block_size = len(self.points) // block_count
        old_modulus = self.points[block_size - 1] - self.points[0] + 1
        lower = profile_discrepancy_lower_bound(
            total_count=len(self.points),
            block_count=block_count,
            old_prefix_upper_bound=old_modulus,
        )
        self.assertGreaterEqual(diameter_profile_discrepancy(self.points), lower)

    def test_scalar_discrepancy_does_not_determine_variance_or_innovation(self) -> None:
        for height in (2, 10, 100):
            points = (0, height, height + 1, 2 * height + 3)
            self.assertEqual(diameter_profile_discrepancy(points), Fraction(1, 4))
            self.assertEqual(
                gap_measure_kolmogorov_discrepancy(points),
                Fraction(1, 4),
            )
            self.assertEqual(
                normalized_gap_function_variance(points),
                Fraction(5 * height + 9, 256 * (height + 2) ** 2),
            )

        first = dyadic_gap_matrix_update((0, 1, 3, 7), 2)
        second = dyadic_gap_matrix_update((0, 1, 5, 7), 2)
        self.assertEqual(first.old_modulus, second.old_modulus)
        self.assertEqual(first.new_modulus, second.new_modulus)
        self.assertEqual(
            tuple(
                tuple(entry / first.new_modulus for entry in row)
                for row in first.innovation
            ),
            (
                (Fraction(51, 16384), Fraction(37, 4096)),
                (Fraction(37, 4096), Fraction(67, 1024)),
            ),
        )
        self.assertEqual(
            tuple(
                tuple(entry / second.new_modulus for entry in row)
                for row in second.innovation
            ),
            (
                (Fraction(67, 16384), Fraction(37, 4096)),
                (Fraction(37, 4096), Fraction(51, 1024)),
            ),
        )


if __name__ == "__main__":
    unittest.main()
