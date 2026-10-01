from fractions import Fraction
import unittest

from endpoint_variance import (
    crossing_loads,
    diameter_required_levels_lower_bound,
    variance,
)


class RequiredLevelsBoundTests(unittest.TestCase):
    def test_bound_is_exact_for_consecutive_points_at_minimal_modulus(self) -> None:
        for size in range(1, 15):
            points = list(range(size))
            modulus = max(2, size)
            self.assertEqual(
                variance(crossing_loads(points, modulus)),
                diameter_required_levels_lower_bound(size, modulus),
            )

    def test_bound_holds_for_arbitrary_diameter_regime_sets(self) -> None:
        cases = [
            ([0, 1, 4, 10, 12, 17], 18),
            ([0, 1, 8, 11, 13, 17], 18),
            ([-10, -3, 2, 20], 31),
            ([0, 100], 101),
            ([], 7),
        ]
        for points, modulus in cases:
            self.assertGreaterEqual(
                variance(crossing_loads(points, modulus)),
                diameter_required_levels_lower_bound(len(points), modulus),
            )

    def test_closed_form(self) -> None:
        self.assertEqual(diameter_required_levels_lower_bound(6, 18), Fraction(329, 108))
        self.assertEqual(diameter_required_levels_lower_bound(0, 7), Fraction(0, 1))
        with self.assertRaises(ValueError):
            diameter_required_levels_lower_bound(-1, 10)


if __name__ == '__main__':
    unittest.main()
