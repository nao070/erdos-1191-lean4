from __future__ import annotations

from fractions import Fraction
import unittest

from endpoint_variance import (
    crossing_loads,
    endpoint_imbalance,
    forward_difference,
    homometric_distance_spectrum,
    offset_energies,
    poincare_lower_bound,
    short_pair_edges,
    variance,
    variance_from_imbalance,
    zero_variance_cycle_decomposition,
)


class EndpointVarianceTests(unittest.TestCase):
    def test_all_offset_boundary_arc_identity(self) -> None:
        points = [0, 1, 4, 10]
        modulus = 8
        edges = short_pair_edges(points, modulus)
        loads = crossing_loads(points, modulus)
        energies = offset_energies(points, modulus)
        self.assertEqual(sum(loads), sum(edge.distance for edge in edges))
        self.assertEqual(
            sum(energies),
            sum(modulus - edge.distance for edge in edges),
        )
        self.assertEqual(
            [loads[r] + energies[r] for r in range(modulus)],
            [len(edges)] * modulus,
        )

    def test_forward_difference_is_endpoint_imbalance(self) -> None:
        points = [0, 1, 4, 10, 12, 17]
        modulus = 14
        self.assertEqual(
            forward_difference(crossing_loads(points, modulus)),
            endpoint_imbalance(points, modulus),
        )

    def test_variance_reconstructed_exactly_from_imbalance(self) -> None:
        points = [0, 2, 7, 11]
        modulus = 9
        direct = variance(crossing_loads(points, modulus))
        reconstructed = variance_from_imbalance(endpoint_imbalance(points, modulus))
        self.assertEqual(direct, reconstructed)
        self.assertEqual(direct, variance(offset_energies(points, modulus)))

    def test_zero_variance_eulerian_two_cycle(self) -> None:
        modulus = 11
        points = [0, 1, modulus]
        self.assertEqual(endpoint_imbalance(points, modulus), [0] * modulus)
        self.assertEqual(variance(crossing_loads(points, modulus)), Fraction(0, 1))
        cycles = zero_variance_cycle_decomposition(points, modulus)
        self.assertEqual(len(cycles), 1)
        self.assertEqual(len(cycles[0]), 2)
        self.assertEqual(
            sorted(edge.distance for edge in cycles[0]),
            [1, modulus - 1],
        )

    def test_non_eulerian_graph_has_positive_variance(self) -> None:
        points = [0, 1, 4]
        modulus = 5
        self.assertNotEqual(endpoint_imbalance(points, modulus), [0] * modulus)
        self.assertGreater(variance(crossing_loads(points, modulus)), 0)
        with self.assertRaises(ValueError):
            zero_variance_cycle_decomposition(points, modulus)

    def test_homometric_sidon_rulers_have_different_variance(self) -> None:
        left = [0, 1, 4, 10, 12, 17]
        right = [0, 1, 8, 11, 13, 17]
        self.assertTrue(homometric_distance_spectrum(left, right))
        self.assertEqual(len(set(b - a for i, a in enumerate(left) for b in left[i + 1 :])), 15)
        self.assertEqual(len(set(b - a for i, a in enumerate(right) for b in right[i + 1 :])), 15)
        self.assertEqual(variance(crossing_loads(left, 14)), Fraction(79, 28))
        self.assertEqual(variance(crossing_loads(right, 14)), Fraction(55, 28))
        self.assertEqual(
            variance(crossing_loads(left, 14)) - variance(crossing_loads(right, 14)),
            Fraction(6, 7),
        )

    def test_poincare_lower_bound(self) -> None:
        for points, modulus in [
            ([0, 1, 4], 5),
            ([0, 1, 4, 10, 12, 17], 14),
            ([0, 1, 8, 11, 13, 17], 14),
            ([0, 3, 9, 18], 10),
        ]:
            delta = endpoint_imbalance(points, modulus)
            self.assertGreaterEqual(
                variance_from_imbalance(delta),
                poincare_lower_bound(delta),
            )

    def test_input_validation(self) -> None:
        with self.assertRaises(ValueError):
            short_pair_edges([0, 0, 1], 4)
        with self.assertRaises(ValueError):
            crossing_loads([0, 1], 1)
        with self.assertRaises(ValueError):
            variance_from_imbalance([1, 0])


if __name__ == '__main__':
    unittest.main()
