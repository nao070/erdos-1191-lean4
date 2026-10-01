from __future__ import annotations

from fractions import Fraction
import random
import unittest

from sidon_block_variance import (
    direct_diameter_variance,
    dyadic_functional_via_birth_kernel,
    dyadic_positive_functional,
    dyadic_shell_upper_bound,
    erdos_turan_ruler,
    is_golomb_ruler,
    positive_birth_kernel,
    positive_gap_variance,
    sidon_block_variance_witness,
    three_rank_lift,
)


class SidonBlockVarianceTests(unittest.TestCase):
    def test_positive_gap_identity_on_random_arbitrary_sets(self) -> None:
        generator = random.Random(1191)
        for mark_count in range(2, 11):
            for _ in range(40):
                points = tuple(sorted(generator.sample(range(0, 80), mark_count)))
                self.assertEqual(positive_gap_variance(points), direct_diameter_variance(points))

    def test_block_theorem_on_dense_sidon_ruler(self) -> None:
        points = erdos_turan_ruler(16, 17)
        witness = sidon_block_variance_witness(points)
        self.assertTrue(is_golomb_ruler(points))
        self.assertGreaterEqual(witness.exact_variance, witness.block_lower_bound)
        self.assertGreaterEqual(witness.block_lower_bound, witness.simplified_lower_bound)
        self.assertGreaterEqual(witness.heavy_mass * 8, witness.diameter)
        self.assertGreaterEqual(witness.minimum_level_separation, 3 * witness.q**2)

    def test_positive_birth_kernel_expansion(self) -> None:
        points = erdos_turan_ruler(16, 17)
        direct = dyadic_positive_functional(points, 2, 4)
        exchanged = dyadic_functional_via_birth_kernel(points, 2, 4)
        self.assertEqual(direct, exchanged)
        for left in range(16):
            for right in range(left + 1, 16):
                self.assertGreaterEqual(positive_birth_kernel(points, left, right, 2, 4), 0)

    def test_unconditional_shell_upper_bound(self) -> None:
        points = erdos_turan_ruler(32, 37)
        self.assertLessEqual(
            dyadic_positive_functional(points, 2, 5),
            dyadic_shell_upper_bound(points, 2, 5),
        )

    def test_three_rank_lift_has_constant_one_shell_energy(self) -> None:
        base = erdos_turan_ruler(16, 17)
        lifted = three_rank_lift(base)
        self.assertTrue(is_golomb_ruler(lifted))
        self.assertGreaterEqual(
            positive_gap_variance(lifted) / len(lifted) ** 4,
            Fraction(1, 2304),
        )

    def test_theorem_rejects_non_sidon_and_wrong_size(self) -> None:
        with self.assertRaises(ValueError):
            sidon_block_variance_witness(range(16))
        with self.assertRaises(ValueError):
            sidon_block_variance_witness(erdos_turan_ruler(8, 11))


if __name__ == "__main__":
    unittest.main()
