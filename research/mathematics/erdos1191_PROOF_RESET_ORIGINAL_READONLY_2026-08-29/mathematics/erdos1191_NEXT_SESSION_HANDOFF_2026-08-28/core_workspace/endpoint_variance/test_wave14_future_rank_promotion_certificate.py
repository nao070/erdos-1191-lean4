from __future__ import annotations

import json
import unittest
from fractions import Fraction
from hashlib import sha256

from wave14_future_rank_promotion_certificate import (
    DEFAULT_OUTPUT,
    build_certificate,
    coefficient_identity_row,
    finite_spatial_bin_fixture,
    next_lower_shell_weight,
    residual_weight,
    terminal_suffix_weight,
)


class Wave14FutureRankPromotionCertificateTests(unittest.TestCase):
    def test_finite_spatial_bin_fixture_replays_exactly(self) -> None:
        fixture = finite_spatial_bin_fixture()
        self.assertEqual(fixture["threshold"], 7935)
        self.assertEqual(fixture["future_mark_count"], 98)
        self.assertEqual(fixture["occupied_bin_count"], 7)
        self.assertEqual(fixture["same_bin_pair_count"], 696)
        self.assertEqual(fixture["cauchy_pair_lower"], "637/1")
        self.assertEqual(fixture["documented_cauchy_expression"], "4459/7")
        self.assertTrue(fixture["documented_cauchy_expression_verified"])
        self.assertEqual(fixture["old_rank"], 120)
        self.assertEqual(fixture["observed_promotion"], 1468)
        self.assertTrue(fixture["exact_expected_values_replayed"])
        self.assertTrue(fixture["exact_inequality_chain_verified"])
        self.assertFalse(fixture["infinite_branch_inferred"])

    def test_termwise_coefficient_and_endpoint_identities(self) -> None:
        for epoch in range(4, 257):
            endpoint = 2 * epoch - 2
            for left in range(2, endpoint + 1):
                with self.subTest(epoch=epoch, left=left):
                    self.assertEqual(
                        terminal_suffix_weight(epoch, left),
                        next_lower_shell_weight(epoch, left)
                        + residual_weight(epoch, left),
                    )
                    self.assertGreater(residual_weight(epoch, left), 0)
            self.assertEqual(
                residual_weight(epoch, endpoint),
                Fraction(3, 8 * epoch * epoch),
            )

    def test_macroscopic_mass_identities(self) -> None:
        for epoch in range(4, 257):
            with self.subTest(epoch=epoch):
                row = coefficient_identity_row(epoch)
                self.assertTrue(row["u_mass_formula_verified"])
                self.assertTrue(row["v_mass_formula_verified"])
                self.assertTrue(row["residual_mass_formula_verified"])
                self.assertTrue(row["macro_mass_split_verified"])
                self.assertTrue(row["termwise_macro_residual_formula_verified"])
                self.assertTrue(row["termwise_u_equals_v_plus_residual_verified"])
                self.assertTrue(row["macro_residual_coefficients_positive"])
                self.assertTrue(row["endpoint_residual_formula_verified"])
                if epoch >= 20:
                    self.assertTrue(row["u_macro_mass_at_least_one_half"])

    def test_certificate_is_deterministic_self_hashed_and_committed(self) -> None:
        first = build_certificate()
        second = build_certificate()
        self.assertEqual(first, second)

        internal_hash = first["certificate_sha256"]
        unhashed = dict(first)
        del unhashed["certificate_sha256"]
        canonical = json.dumps(unhashed, sort_keys=True, separators=(",", ":"))
        self.assertEqual(internal_hash, sha256(canonical.encode("utf-8")).hexdigest())

        boundary = first["claim_boundary"]
        self.assertEqual(
            first["scope_flags"],
            {
                "infinite_branch": False,
                "signed_allocation": False,
                "problem_unresolved": True,
            },
        )
        self.assertFalse(boundary["infinite_eventually_critical_branch_certified"])
        self.assertFalse(boundary["signed_cross_epoch_allocation_certified"])
        self.assertTrue(boundary["erdos_1191_unresolved"])
        self.assertFalse(boundary["erdos_1191_resolved"])
        self.assertFalse(boundary["prize_claim_ready"])

        committed = json.loads(DEFAULT_OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(committed, first)


if __name__ == "__main__":
    unittest.main()
