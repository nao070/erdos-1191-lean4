from __future__ import annotations

import json
import unittest
from fractions import Fraction
from hashlib import sha256

from wave16_multiscale_future_rank import (
    DEFAULT_OUTPUT,
    build_certificate,
    cap_side_condition,
    theoretical_inequality_audit,
    theoretical_max_scale,
    theoretical_single_block_lower,
    theoretical_total_lower,
)


class Wave16MultiscaleFutureRankTests(unittest.TestCase):
    def test_exact_scale_range_without_floating_point(self) -> None:
        expected = {
            2: 0,
            3: 0,
            4: 1,
            8: 1,
            15: 1,
            16: 2,
            32: 2,
            63: 2,
            64: 3,
            2**24: 12,
        }
        for length, scale in expected.items():
            with self.subTest(length=length):
                self.assertEqual(theoretical_max_scale(length), scale)
                self.assertLessEqual(4**scale, length)
                self.assertGreater(4 ** (scale + 1), length)

    def test_decimal_side_condition_and_constant_chain(self) -> None:
        self.assertFalse(cap_side_condition(16, Fraction(1)))
        self.assertTrue(cap_side_condition(2**24, Fraction(1)))

        length = 2**24
        difference = length * length // 8
        audit = theoretical_inequality_audit(length, difference, Fraction(1))
        self.assertTrue(audit["eight_d_at_least_L_squared"])
        self.assertTrue(audit["side_condition"])
        self.assertTrue(audit["block_count_converts_single_to_total"])
        self.assertTrue(audit["all_constant_chain_checks"])
        self.assertEqual(audit["theoretical_max_scale"], 12)
        self.assertEqual(audit["theoretical_block_count"], 13)
        self.assertTrue(
            all(row["M_at_least_twice_bin_upper"] for row in audit["block_rows"])
        )

        single = theoretical_single_block_lower(length, difference, Fraction(1))
        total = theoretical_total_lower(difference, Fraction(1))
        self.assertGreater(13 * single, total)

        failed_hypothesis = theoretical_inequality_audit(16, 10**9, Fraction(1))
        self.assertFalse(failed_hypothesis["side_condition"])
        self.assertFalse(failed_hypothesis["all_constant_chain_checks"])

    def test_finite_block_counts_and_rank_increments(self) -> None:
        rows = build_certificate()["fixture_rows"]
        self.assertEqual(
            [row["selected_old_difference"] for row in rows],
            [218, 1002, 3647, 7935, 16124],
        )
        self.assertEqual(
            [
                [block["same_bin_pair_count"] for block in row["block_rows"]]
                for row in rows
            ],
            [[4, 0], [24, 22], [16, 41], [105, 211, 427], [465, 932]],
        )
        self.assertEqual(
            [
                [block["exact_rank_increment"] for block in row["block_rows"]]
                for row in rows
            ],
            [[17, 1], [69, 64], [48, 107], [239, 480, 959], [990, 1984]],
        )
        self.assertEqual(
            [row["aggregate_witness_difference_count"] for row in rows],
            [4, 46, 57, 743, 1397],
        )
        self.assertEqual(
            [row["exact_total_rank_increment"] for row in rows],
            [18, 133, 155, 1678, 2974],
        )
        self.assertTrue(all(row["reported_values_match"] for row in rows))

    def test_finite_disjointness_and_scope_are_explicit(self) -> None:
        rows = build_certificate()["fixture_rows"]
        self.assertEqual(
            [row["full_theoretical_scale_range_observed"] for row in rows],
            [True, False, True, True, False],
        )
        self.assertEqual(
            [row["fixture_range_truncated"] for row in rows],
            [False, True, False, False, True],
        )
        for row in rows:
            with self.subTest(
                fixture=row["fixture"], old_mark_count=row["old_mark_count"]
            ):
                self.assertTrue(row["global_golomb_prefix_verified"])
                self.assertTrue(row["selected_difference_is_old"])
                self.assertTrue(row["eight_d_at_least_L_squared"])
                self.assertTrue(row["aggregate_witnesses_distinct"])
                self.assertTrue(row["aggregate_witnesses_disjoint_from_old_prefix"])
                self.assertTrue(row["rho_increment_dominates_aggregate_witness"])
                self.assertFalse(row["cap_side_condition_C1"])
                self.assertFalse(row["asymptotic_block_lower_applied"])
                for block in row["block_rows"]:
                    self.assertTrue(block["same_bin_count_dominates_cauchy"])
                    self.assertTrue(block["all_witness_differences_strictly_below_d"])
                    self.assertTrue(block["witness_differences_distinct_within_block"])
                    self.assertTrue(
                        block["witness_differences_disjoint_from_old_prefix"]
                    )
                    self.assertTrue(
                        block["witness_differences_disjoint_from_earlier_blocks"]
                    )
                    self.assertTrue(block["rank_increment_dominates_block_witness"])

    def test_certificate_is_deterministic_self_hashed_and_unresolved(self) -> None:
        first = build_certificate()
        second = build_certificate()
        self.assertEqual(first, second)

        unhashed = dict(first)
        internal_hash = unhashed.pop("certificate_sha256")
        canonical = json.dumps(unhashed, sort_keys=True, separators=(",", ":"))
        self.assertEqual(internal_hash, sha256(canonical.encode("utf-8")).hexdigest())

        self.assertEqual(
            first["scope_flags"],
            {
                "finite_fixture_only": True,
                "eventual_cap_branch_inferred": False,
                "asymptotic_theorem_inferred_from_fixtures": False,
                "all_epoch_signed_allocation": False,
                "problem_unresolved": True,
            },
        )
        boundary = first["claim_boundary"]
        self.assertTrue(
            boundary["conditional_constant_chain_checked_at_80_decimal_digits"]
        )
        self.assertFalse(boundary["infinite_eventually_critical_branch_certified"])
        self.assertFalse(boundary["p19_proved"])
        self.assertFalse(boundary["question_1_resolved"])
        self.assertFalse(boundary["erdos_1191_resolved"])
        self.assertFalse(boundary["prize_claim_ready"])

        committed = json.loads(DEFAULT_OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(committed, first)


if __name__ == "__main__":
    unittest.main()
