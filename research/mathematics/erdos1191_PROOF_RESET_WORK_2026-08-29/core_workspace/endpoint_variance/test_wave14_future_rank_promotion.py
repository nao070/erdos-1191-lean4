from __future__ import annotations

import unittest
from fractions import Fraction

from complete_birth_ledger import erdos_turan_ruler
from wave14_future_rank_promotion import (
    difference_rank,
    future_rank_promotion_audit,
    logarithmic_block_size,
    macroscopic_suffix_weight,
)


class Wave14FutureRankPromotionTests(unittest.TestCase):
    def test_exact_future_bin_promotion_on_erdos_turan_fixture(self) -> None:
        points = erdos_turan_ruler(128, 257)
        old_mark_count = 16
        threshold = points[old_mark_count - 1]
        self.assertEqual(threshold, 7935)
        self.assertEqual(logarithmic_block_size(threshold), 98)

        audit = future_rank_promotion_audit(points, old_mark_count, threshold)
        self.assertEqual(audit.future_mark_count, 98)
        self.assertEqual(audit.occupied_bin_count, 7)
        self.assertEqual(audit.same_bin_pair_count, 696)
        self.assertEqual(audit.cauchy_pair_lower, Fraction(4459, 7))
        self.assertEqual(audit.old_rank, 120)
        self.assertEqual(audit.observed_promotion, 1468)
        self.assertTrue(audit.same_bin_differences_are_distinct)
        self.assertTrue(audit.same_bin_differences_are_new)
        self.assertTrue(audit.same_bin_differences_are_strictly_below_threshold)
        self.assertTrue(audit.observed_promotion_dominates_same_bin_pairs)
        self.assertTrue(audit.same_bin_pairs_dominate_cauchy_lower)

    def test_rank_count_obeys_integer_spacing_bound(self) -> None:
        points = erdos_turan_ruler(64, 257)
        for mark_count in (4, 8, 16, 32):
            threshold = points[mark_count - 1]
            with self.subTest(mark_count=mark_count):
                rank = difference_rank(points, mark_count, threshold)
                self.assertEqual(rank, mark_count * (mark_count - 1) // 2)
                self.assertLessEqual(rank, threshold)

    def test_macroscopic_suffix_weight_formula_and_half_mass(self) -> None:
        for epoch in (4, 8, 16, 20, 32, 64, 128):
            direct = sum(
                (
                    Fraction(12 * epoch - 5 - 6 * left, 16 * epoch * epoch)
                    for left in range(2, epoch + 1)
                ),
                Fraction(0),
            )
            with self.subTest(epoch=epoch):
                self.assertEqual(macroscopic_suffix_weight(epoch), direct)
                if epoch >= 20:
                    self.assertGreaterEqual(direct, Fraction(1, 2))


if __name__ == "__main__":
    unittest.main()
