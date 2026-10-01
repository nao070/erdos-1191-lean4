from __future__ import annotations

from fractions import Fraction
import random
import unittest

from cover_martingale import (
    cover_variance_identity,
    edge_coordinate_budget,
    frozen_cover_variance_identity,
    old_birth_dichotomy,
    pair_arc_loads,
    vector_cover_increment_trace,
    vector_discounted_cover_trace,
)
from endpoint_variance import crossing_loads, variance


class CoverMartingaleTests(unittest.TestCase):
    def test_exact_cover_identity_on_random_pair_multisets(self) -> None:
        generator = random.Random(1191)
        for modulus in range(2, 10):
            for cover in range(2, 5):
                for _ in range(30):
                    pairs = []
                    for _ in range(generator.randrange(0, 12)):
                        left = generator.randrange(-20, 21)
                        distance = generator.randrange(1, cover * modulus)
                        pairs.append((left, left + distance))
                    identity = cover_variance_identity(pairs, modulus, cover)
                    self.assertEqual(
                        identity.scaled_fine_variance,
                        identity.residual_variance + identity.innovation,
                    )
                    self.assertGreaterEqual(identity.innovation, 0)

    def test_frozen_q2_square_identity(self) -> None:
        pairs = ((0, 1), (0, 3), (1, 7), (3, 7))
        result = frozen_cover_variance_identity(pairs, 8, 2)
        coarse = pair_arc_loads(pairs, 8)
        fine = pair_arc_loads(pairs, 16)
        square = Fraction(
            sum((fine[r] - fine[r + 8]) ** 2 for r in range(8)),
            8,
        )
        self.assertEqual(4 * variance(fine), variance(coarse) + square)
        self.assertEqual(result.innovation, square)

    def test_minimal_birth_obstruction(self) -> None:
        points = (0, 1, 4)
        self.assertEqual(variance(crossing_loads(points, 2)), Fraction(1, 4))
        self.assertEqual(variance(crossing_loads(points, 4)), 0)
        left, right = old_birth_dichotomy(((0, 1),), ((1, 4),), 2, 2)
        self.assertEqual(left, Fraction(1, 8))
        self.assertGreaterEqual(right, left)

    def test_general_birth_complement(self) -> None:
        for modulus in range(2, 10):
            for cover in range(2, 5):
                points = (0, 1, cover * modulus)
                self.assertEqual(
                    variance(crossing_loads(points, modulus)),
                    Fraction(modulus - 1, modulus**2),
                )
                self.assertEqual(variance(crossing_loads(points, cover * modulus)), 0)

    def test_three_cycle_can_have_zero_frozen_innovation(self) -> None:
        pairs = ((0, 3), (3, 7), (7, 12))
        result = frozen_cover_variance_identity(pairs, 6, 2)
        self.assertEqual(result.residual_variance, 0)
        self.assertEqual(result.fine_variance, 0)
        self.assertEqual(result.innovation, 0)

    def test_edge_coordinate_trace_examples(self) -> None:
        self.assertEqual(edge_coordinate_budget((3, 4, 5), 6).trace, Fraction(11, 18))
        self.assertEqual(
            vector_cover_increment_trace((3, 4, 5), 6, 2),
            2,
        )
        self.assertEqual(
            edge_coordinate_budget((1, 2, 3, 4, 6, 7), 8).trace,
            Fraction(69, 64),
        )
        self.assertEqual(
            vector_cover_increment_trace((1, 2, 3, 4, 6, 7), 8, 2),
            Fraction(23, 8),
        )
        self.assertEqual(edge_coordinate_budget((1, 3), 4).trace, Fraction(3, 8))

    def test_weighted_coordinate_budget_cannot_beat_universal_bound(self) -> None:
        result = edge_coordinate_budget(
            (1, 3, 4, 8, 10, 11),
            13,
            (Fraction(1, 3), 2, Fraction(5, 7), 11, Fraction(9, 2), 3),
        )
        self.assertGreaterEqual(result.product, result.universal_lower_bound)

    def test_discounted_vector_trace_is_exact_geometric_sum(self) -> None:
        differences = (1, 3, 7)
        modulus = 10
        cover = 3
        finite = sum(
            Fraction(1, cover ** (2 * level))
            * vector_cover_increment_trace(differences, modulus, cover, level)
            for level in range(12)
        )
        infinite = vector_discounted_cover_trace(differences, modulus, cover)
        self.assertLess(finite, infinite)
        self.assertEqual(
            infinite - finite,
            Fraction(sum(differences), modulus * cover**11),
        )


if __name__ == "__main__":
    unittest.main()
