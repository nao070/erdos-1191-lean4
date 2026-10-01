#!/usr/bin/env python3
"""Focused exact tests for the C133 adjacent epoch ledger verifier."""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import subprocess
import sys
import unittest


HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import ROUTE_C_C133_ADJACENT_EPOCH_LEDGER_verifier as cert


class C133AdjacentEpochLedgerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.value = cert.build_certificate()

    def test_01_exact_14_row_identity_and_nonzero_minimality_fixture(self) -> None:
        row = self.value["ledger_audit"]
        self.assertEqual(F(row["fixture_lhs"]), F(1707, 1372))
        self.assertEqual(F(row["fixture_rhs"]), F(1707, 1372))
        self.assertEqual(row["unique_stitched_rows"], 14)
        self.assertEqual(len(row["fixture_rows"]), 14)
        self.assertTrue(row["every_fixture_row_nonzero"])
        self.assertTrue(all(F(value) != 0 for value in row["fixture_rows"].values()))

    def test_02_exact_18_to_14_A16_stitch(self) -> None:
        row = self.value["ledger_audit"]
        self.assertEqual(row["raw_one_edge_occurrences"], 18)
        self.assertEqual(row["shared_A16_premerge_multiplicity"], [2, 2, 2, 2])
        self.assertEqual(row["shared_A16_postmerge_multiplicity"], [1, 1, 1, 1])
        self.assertEqual(row["shared_A16_rows"], 4)
        for scale in cert.SCALES:
            self.assertEqual(row["fixture_row_owners"][f"band:A16:s{scale}"], "epoch8")

    def test_03_C103_specialization_retains_every_boundary_and_terminal(self) -> None:
        theorem = self.value["theorem_contract"]
        row = self.value["ledger_audit"]
        self.assertEqual(
            theorem["C103_specialization"],
            "L=0,m=1,n=4; edges 8,16; prefixes A8,A16,A32",
        )
        self.assertEqual(theorem["shared_A16_coefficient"], "w8*S8,s-w16*S16,s")
        self.assertEqual(
            (row["initial_A8_rows"], row["shared_A16_rows"], row["final_A32_rows"]),
            (4, 4, 4),
        )
        self.assertEqual(row["upper_terminal_rows"], 2)
        self.assertEqual(row["upper_terminal_width"], "16t")

    def test_04_100_coordinate_partition_and_live_rank15(self) -> None:
        row = self.value["coordinate_owner_audit"]
        self.assertEqual(row["coordinate_count"], 100)
        self.assertEqual(
            row["fiber_counts"],
            {"past_epoch4": 4, "epoch8": 32, "epoch16": 64},
        )
        self.assertEqual(row["shared_rank15_owner"], "epoch8")
        self.assertEqual(row["shared_rank15_scale_count"], 4)
        self.assertEqual(F(row["rank15_example_coordinate_row"]), F(-1))
        self.assertFalse(row["right_zero_used"])
        self.assertEqual(F(row["example_energy"]), F(17))
        self.assertEqual(
            sum((F(value) for value in row["example_owner_shares"].values()), F(0)),
            F(row["example_energy"]),
        )

    def test_05_unique_birth_cases_keep_prebirth_final_and_terminal_rows(self) -> None:
        row = self.value["birth_audit"]
        birth8 = row["epoch8"]
        birth16 = row["epoch16"]
        self.assertEqual(birth8["active_band"], "A16_shared_birth")
        self.assertEqual(birth16["active_band"], "A32_final_birth")
        self.assertTrue(birth8["initial_A8_zero"])
        self.assertIsNone(birth8["prebirth_A16_zero"])
        self.assertTrue(birth16["initial_A8_zero"])
        self.assertTrue(birth16["prebirth_A16_zero"])
        self.assertNotEqual(F(birth8["upper_terminal"]), 0)
        self.assertNotEqual(F(birth16["upper_terminal"]), 0)
        self.assertTrue(row["unique_birth_hypothesis_required"])
        self.assertTrue(row["birth_supported_coefficients_required"])
        self.assertFalse(row["aggregate_C130_C131_decomposition_proved"])

    def test_06_deterministic_random_fraction_replay(self) -> None:
        row = self.value["ledger_audit"]
        self.assertEqual(row["random_fraction_fixtures"], 512)
        self.assertEqual(row["random_seed"], 1191132)
        cert.random_fixture_audit(32, 20260831)

    def test_07_scope_is_C103_specialization_only_and_C058_open(self) -> None:
        scope = self.value["scope"]
        self.assertTrue(scope["finite_C103_specialization_only"])
        self.assertTrue(scope["exact_14_row_identity_verified"])
        self.assertTrue(scope["exact_18_to_14_stitch_verified"])
        self.assertFalse(scope["rank15_right_zero_used"])
        self.assertFalse(scope["sign_or_capacity_claimed"])
        self.assertFalse(scope["nonanticipating_phase_rule_proved"])
        self.assertFalse(scope["PSD_master_inequality_proved"])
        self.assertFalse(scope["C130_C131_global_compatibility_proved"])
        self.assertFalse(scope["fresh_epoch16_factor_constructed"])
        self.assertFalse(scope["arbitrary_history_proved"])
        self.assertFalse(scope["arbitrary_rank_proved"])
        self.assertFalse(scope["C058_resolved"])
        self.assertFalse(scope["Q1_Q2_resolved"])
        self.assertFalse(scope["prize_claim_ready"])

    def test_08_semantic_replay_and_mutation_barrier(self) -> None:
        summary = cert.validate_certificate(self.value)
        self.assertEqual(summary["unique_rows"], 14)
        self.assertTrue(summary["C058_open"])
        mutations = cert.mutation_self_check(self.value)
        self.assertEqual(mutations["normal_verified"], 1)
        self.assertEqual(mutations["mutations_attempted"], 8)
        self.assertEqual(mutations["mutations_rejected"], 8)
        self.assertEqual(
            mutations["cases"],
            [
                "scope_upgrade",
                "row_count",
                "A16_double_owner",
                "rank15_owner_or_right_zero",
                "upper_terminal_drop",
                "birth_prestate",
                "fixture_identity",
                "exact_type",
            ],
        )

    def test_09_command_line_verifier(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(Path(cert.__file__)), "--self-check"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("MUTATION_OK rejected=8/8", completed.stdout)
        self.assertIn("VERIFY_OK C133 rows=14 raw=18 random=512", completed.stdout)
        self.assertIn("rank15_owner=epoch8", completed.stdout)
        self.assertIn("C103_specialization_only C058_open", completed.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
