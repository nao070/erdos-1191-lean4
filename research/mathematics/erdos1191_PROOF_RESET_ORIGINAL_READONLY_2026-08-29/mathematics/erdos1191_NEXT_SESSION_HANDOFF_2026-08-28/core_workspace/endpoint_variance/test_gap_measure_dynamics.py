from __future__ import annotations

from fractions import Fraction
import random
import unittest

from gap_measure_dynamics import (
    diameter_compensated_gap_matrix,
    dyadic_gap_matrix_update,
    gap_rank_variance,
    normalized_gap_function_variance,
    two_step_distinct_gap_witness,
)
from sidon_block_variance import erdos_turan_ruler


class GapMeasureDynamicsTests(unittest.TestCase):
    def test_exact_matrix_update_on_random_increasing_sets(self) -> None:
        generator = random.Random(1191)
        for old_count in range(2, 10):
            for _ in range(30):
                points = tuple(sorted(generator.sample(range(0, 200), 2 * old_count)))
                update = dyadic_gap_matrix_update(points, old_count)
                self.assertEqual(update.new_matrix, diameter_compensated_gap_matrix(points))

    def test_optimized_two_step_bound(self) -> None:
        for count, prime in ((16, 17), (32, 37), (64, 67)):
            witness = two_step_distinct_gap_witness(erdos_turan_ruler(count, prime))
            self.assertGreaterEqual(witness.old_rank_variance, witness.old_rank_lower_bound)
            self.assertGreaterEqual(
                witness.final_normalized_variance,
                witness.distinct_gap_lower_bound,
            )

    def test_two_step_bound_only_needs_old_prefix_to_be_golomb(self) -> None:
        points = (0, 1, 4, 6, *range(7, 19))
        witness = two_step_distinct_gap_witness(points)
        self.assertGreaterEqual(
            witness.final_normalized_variance,
            witness.distinct_gap_lower_bound,
        )

    def test_one_step_scalar_aging_can_move_both_directions(self) -> None:
        decreasing = (0, 1, 4, 6)
        increasing = (0, 1, 3, 7)
        self.assertEqual(normalized_gap_function_variance(decreasing), Fraction(3, 448))
        self.assertEqual(
            normalized_gap_function_variance(decreasing, 2),
            Fraction(297, 50176),
        )
        self.assertLess(
            normalized_gap_function_variance(decreasing, 2),
            normalized_gap_function_variance(decreasing),
        )
        self.assertEqual(normalized_gap_function_variance(increasing), Fraction(87, 16384))
        self.assertEqual(
            normalized_gap_function_variance(increasing, 2),
            Fraction(1615, 262144),
        )
        self.assertGreater(
            normalized_gap_function_variance(increasing, 2),
            normalized_gap_function_variance(increasing),
        )

    def test_gap_rank_variance_is_nonnegative(self) -> None:
        self.assertGreaterEqual(gap_rank_variance((0, 2, 7, 11)), 0)


if __name__ == "__main__":
    unittest.main()
