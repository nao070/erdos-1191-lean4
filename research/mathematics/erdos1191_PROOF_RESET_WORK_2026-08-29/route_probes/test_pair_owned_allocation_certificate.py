#!/usr/bin/env python3
"""Regression tests for the exact pair-owned allocation certificate."""
from __future__ import annotations

import copy
from fractions import Fraction as F
import json
from pathlib import Path
import unittest

import pair_owned_allocation_certificate as probe


FIXTURE = Path(__file__).resolve().with_name("pair_owned_allocation_certificate.json")


class PairOwnedAllocationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_01_nested_prefixes_are_exact_sidon(self) -> None:
        self.assertEqual(len(probe.require_sidon(probe.OLD_PREFIX)), 28)
        self.assertEqual(len(probe.require_sidon(probe.NEW_PREFIX)), 120)
        self.assertEqual(len(probe.first_use_differences(probe.OLD_PREFIX, probe.NEW_PREFIX)), 92)

    def test_02_first_use_supremum_is_exact(self) -> None:
        row = probe.scalar_no_go_fixture()["first_use_supremum"]
        self.assertEqual(F(row["value"]), F(18, 385))
        self.assertEqual(row["active_count"], 12)
        self.assertEqual(F(row["width"]), F(770, 3))

    def test_03_proportional_pair_lp_replays(self) -> None:
        rows = probe.proportional_allocation_rows(probe.OLD_PREFIX, 4, tuple(range(0, 6)))
        self.assertTrue(rows)
        for row in rows:
            self.assertEqual(F(row["allocated_total"]), F(row["demand"]))
            self.assertGreaterEqual(F(row["P"]), F(row["Q"]))

    def test_04_owner_lift_zeroes_prebirth_negative_row(self) -> None:
        row = probe.owner_lift_fixture()
        self.assertTrue(row["prebirth_bands_all_zero"])
        self.assertEqual(F(row["formal_negative_prebirth_contribution"]), 0)
        self.assertEqual(
            F(row["lhs"]),
            F(row["positive_birth_bulk"]) + F(row["scale_terminal"]),
        )

    def test_05_diagonal_price_and_terminal_are_exact(self) -> None:
        row = probe.owner_lift_fixture()
        self.assertEqual(
            F(row["band_diagonal_price"]) + F(row["tail_diagonal_price"]),
            F(row["swapped_diagonal_price"]),
        )
        self.assertTrue(row["diagonal_price_identity_verified"])

    def test_06_scalar_fractional_no_go_has_strict_gap(self) -> None:
        row = probe.scalar_no_go_fixture()
        self.assertEqual(F(row["scalar_phase_integral_upper"]), F(185, 1386))
        self.assertEqual(F(row["comparison_sum"]), F(494, 5175))
        self.assertEqual(F(row["strict_rational_gap"]), F(461, 227700))
        self.assertTrue(row["contradiction_verified"])

    def test_07_strict_interior_beta_sum(self) -> None:
        owners = probe.positive_owners(probe.OLD_PREFIX, 4)
        self.assertEqual(sum((row[3] for row in owners), F(0)), F(9, 64))

    def test_08_certificate_semantic_and_byte_replay(self) -> None:
        generated = probe.build_certificate()
        self.assertEqual(generated, self.fixture)
        self.assertEqual(FIXTURE.read_bytes(), probe.rendered_bytes(self.fixture))
        probe.validate_certificate(self.fixture)

    def test_09_mutations_are_rejected(self) -> None:
        self.assertEqual(probe.self_check(self.fixture), 7)
        changed = copy.deepcopy(self.fixture)
        changed["scope"]["prize_claim_ready"] = True
        probe.rehash(changed)
        with self.assertRaises(probe.CertificateError):
            probe.validate_certificate(changed)

    def test_10_scope_preserves_open_problem(self) -> None:
        scope = self.fixture["scope"]
        self.assertTrue(scope["positive_potential_pair_lp_solved"])
        self.assertTrue(scope["owner_lift_adjacent_sign_gate_removed"])
        self.assertFalse(scope["psd_diagonal_price_paid"])
        self.assertFalse(scope["gothic_ledger_rewritten"])
        self.assertFalse(scope["c058_resolved"])
        self.assertFalse(scope["question_1_resolved"])
        self.assertFalse(scope["question_2_resolved"])
        self.assertFalse(scope["prize_claim_ready"])


if __name__ == "__main__":
    unittest.main()
