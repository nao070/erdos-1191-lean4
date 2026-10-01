from fractions import Fraction
import unittest

from endpoint_variance import (
    crossing_loads,
    diameter_regime_profile,
    diameter_regime_variance,
    endpoint_imbalance,
    rank_imbalance_square_sum,
    variance,
)


class DiameterRegimeTests(unittest.TestCase):
    def test_gap_profile_reconstructs_crossing_load_multiset(self) -> None:
        points = [0, 1, 4, 10, 12, 17]
        modulus = 18
        profile = diameter_regime_profile(points, modulus)
        expected = [0] * profile.outside_gap
        for gap, level in zip(profile.internal_gaps, profile.crossing_levels):
            expected.extend([level] * gap)
        self.assertEqual(sorted(expected), sorted(crossing_loads(points, modulus)))
        self.assertEqual(len(expected), modulus)

    def test_exact_gap_moment_formula(self) -> None:
        for points, modulus in [
            ([0, 1, 4, 10, 12, 17], 18),
            ([-3, 0, 8], 20),
            ([5], 7),
            ([], 11),
        ]:
            self.assertEqual(
                diameter_regime_variance(points, modulus),
                variance(crossing_loads(points, modulus)),
            )

    def test_rank_imbalance_is_cubic(self) -> None:
        for size in range(0, 15):
            points = [3 * j * j + j for j in range(size)]
            diameter = points[-1] - points[0] if size else 0
            modulus = max(2, diameter + 1)
            delta = endpoint_imbalance(points, modulus)
            self.assertEqual(sum(entry * entry for entry in delta), rank_imbalance_square_sum(size))
            self.assertEqual(rank_imbalance_square_sum(size), size * (size * size - 1) // 3)

    def test_diameter_hypothesis_is_checked(self) -> None:
        with self.assertRaises(ValueError):
            diameter_regime_profile([0, 5], 5)


if __name__ == '__main__':
    unittest.main()
