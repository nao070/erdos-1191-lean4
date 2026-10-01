#!/usr/bin/env python3
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import sys
import unittest


HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import ROUTE_C_C132_COMPOSITE32_NAIVE_PASTE_NO_GO_certificate as cert


class C132Composite32NaivePasteNoGoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.value = cert.build_certificate()

    def test_01_explicit_composite_is_exact_golomb(self) -> None:
        row = self.value["composite"]
        self.assertEqual(row["mark_count"], 32)
        self.assertEqual(row["span"], 7084)
        self.assertEqual(row["positive_differences"], 496)
        self.assertEqual(row["distinct_positive_differences"], 496)

    def test_02_finite_C2_cap_scope_is_exact(self) -> None:
        row = self.value["composite"]
        self.assertEqual((row["finite_cap_onset"], row["finite_cap_last_prefix"]), (4, 32))
        self.assertEqual(row["finite_cap_rows_checked"], 29)
        self.assertEqual(row["worst_required_C_prefix"], 8)
        self.assertEqual(row["worst_required_C_inside"], ["1931/1000", "483/250"])

    def test_03_cross_half_residual_is_not_silently_lost(self) -> None:
        row = self.value["cross_half_residual"]
        self.assertEqual(row["omitted_cross_half_source_count"], 63)
        self.assertEqual(row["omitted_cross_half_alpha_mass"], "4767/1024")
        self.assertTrue(row["mixed_sign_and_indefinite"])
        self.assertTrue(row["zero_diagonal"])
        self.assertTrue(row["zero_row_sums"])

    def test_04_natural_epoch16_owner_counterexample(self) -> None:
        row = self.value["natural_owner_counterexample"]
        self.assertEqual(row["natural_epoch16_owner_rows_checked"], 692)
        self.assertEqual(row["strictly_negative_natural_owner_rows"], 152)
        self.assertEqual(row["strongest"]["natural_demand"], "9/512")
        self.assertEqual(
            row["strongest"]["margin"],
            "-175791028451541/10006250000000000",
        )

    def test_05_exact_phase_alignment_family_is_not_Golomb(self) -> None:
        row = self.value["phase_alignment_no_go"]
        self.assertTrue(row["all_positive_integer_q_fail_Golomb"])
        self.assertEqual(row["q5_repeated_difference"], 2135)

    def test_06_scope_does_not_upgrade_C058(self) -> None:
        scope = self.value["scope"]
        self.assertTrue(scope["naive_affine_local_bank_paste_refuted"])
        self.assertFalse(scope["fresh_joint_epoch8_16_master_refuted"])
        self.assertFalse(scope["arbitrary_rank_proved"])
        self.assertFalse(scope["C058_resolved"])
        self.assertFalse(scope["Q1_Q2_resolved"])

    def test_07_mutations_are_rejected(self) -> None:
        bad = deepcopy(self.value)
        bad["scope"]["C058_resolved"] = True
        with self.assertRaises(cert.CertificateError):
            cert.validate(bad, self.value)
        self.assertEqual(cert.mutation_self_check(self.value), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
