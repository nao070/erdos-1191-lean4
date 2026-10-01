from __future__ import annotations

import unittest
from fractions import Fraction
from itertools import combinations

from endpoint_variance import crossing_loads, endpoint_imbalance, variance
from multiscale_variance import (
    cycle_resistance,
    cyclic_arc_covariance,
    cyclic_arc_covariance_via_resistance,
    cyclic_arc_overlap,
    fixed_modulus_prefix_load_second_difference,
    pair_pair_covariance_sum,
)


def brute_arc(start: int, length: int, modulus: int) -> set[int]:
    return {(start + step) % modulus for step in range(1, length + 1)}


class MultiscaleVarianceTests(unittest.TestCase):
    def test_closed_overlap_matches_exhaustive_set_oracle(self) -> None:
        for modulus in range(2, 13):
            for left_start in range(modulus):
                for right_start in range(modulus):
                    for left_length in range(1, modulus):
                        for right_length in range(1, modulus):
                            expected = len(
                                brute_arc(left_start, left_length, modulus)
                                & brute_arc(right_start, right_length, modulus)
                            )
                            self.assertEqual(
                                cyclic_arc_overlap(
                                    left_start,
                                    left_length,
                                    right_start,
                                    right_length,
                                    modulus,
                                ),
                                expected,
                            )

    def test_resistance_representation_matches_overlap_covariance(self) -> None:
        for modulus in range(2, 18):
            for left_start in range(modulus):
                for right_start in range(modulus):
                    for left_length in range(1, modulus):
                        for right_length in range(1, modulus):
                            direct = cyclic_arc_covariance(
                                left_start,
                                left_length,
                                right_start,
                                right_length,
                                modulus,
                            )
                            resistance = cyclic_arc_covariance_via_resistance(
                                left_start,
                                left_length,
                                right_start,
                                right_length,
                                modulus,
                            )
                            self.assertEqual(direct, resistance)

    def test_resistance_kernel_is_symmetric_and_zero_at_origin(self) -> None:
        for modulus in range(2, 30):
            self.assertEqual(cycle_resistance(0, modulus), 0)
            for position in range(-2 * modulus, 2 * modulus + 1):
                self.assertEqual(
                    cycle_resistance(position, modulus),
                    cycle_resistance(-position, modulus),
                )

    def test_pair_pair_expansion_equals_n_times_variance(self) -> None:
        for ambient_size in range(2, 10):
            for mark_count in range(2, min(6, ambient_size + 1)):
                for points in combinations(range(ambient_size), mark_count):
                    for modulus in range(2, 10):
                        self.assertEqual(
                            pair_pair_covariance_sum(points, modulus),
                            modulus * variance(crossing_loads(points, modulus)),
                        )

    def test_covariance_sign_examples(self) -> None:
        modulus = 17
        # (2, 6] is nested in (0, 10].
        self.assertGreater(cyclic_arc_covariance(0, 10, 2, 4, modulus), 0)
        # (0, 3] and (7, 12] are disjoint.
        self.assertLess(cyclic_arc_covariance(0, 3, 7, 5, modulus), 0)
        # These two arcs cover the circle and neither contains the other.
        self.assertLess(cyclic_arc_covariance(0, 10, 8, 9, modulus), 0)
        # Partial crossing can have either sign.
        self.assertGreater(cyclic_arc_covariance(0, 9, 6, 4, modulus), 0)
        self.assertLess(cyclic_arc_covariance(0, 6, 5, 6, modulus), 0)

    def test_prefix_second_difference_is_one_adjacent_gap(self) -> None:
        cases = [
            ((0, 1, 4, 10, 12, 17), 19),
            ((5, 8, 14, 23), 21),
            ((0, 2, 9), 12),
        ]
        for points, modulus in cases:
            for mark_count in range(2, len(points) + 1):
                expected = [0] * modulus
                left = points[mark_count - 2]
                right = points[mark_count - 1]
                for step in range(1, right - left + 1):
                    expected[(left + step) % modulus] = mark_count - 1
                self.assertEqual(
                    fixed_modulus_prefix_load_second_difference(
                        points, modulus, mark_count
                    ),
                    expected,
                )

    def test_three_cycle_sidon_zero_mode(self) -> None:
        points = (0, 3, 7, 12)
        modulus = 6
        differences = {
            points[j] - points[i]
            for i in range(len(points))
            for j in range(i + 1, len(points))
        }
        self.assertEqual(len(differences), 6)
        self.assertEqual(endpoint_imbalance(points, modulus), [0] * modulus)
        self.assertEqual(variance(crossing_loads(points, modulus)), Fraction(0, 1))

    def test_validation_rejects_full_or_empty_arcs(self) -> None:
        with self.assertRaises(ValueError):
            cyclic_arc_overlap(0, 0, 1, 1, 5)
        with self.assertRaises(ValueError):
            cyclic_arc_overlap(0, 5, 1, 1, 5)
        with self.assertRaises(ValueError):
            fixed_modulus_prefix_load_second_difference((0, 4, 9), 9, 3)


if __name__ == "__main__":
    unittest.main()
