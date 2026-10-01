#!/usr/bin/env python3
"""Focused adversarial tests for the physical-cover transfer certificate."""
from __future__ import annotations

from fractions import Fraction as F
import json
import unittest

import ROUTE_C_PHYSICAL_COVER_TRANSFER_certificate as probe


class PhysicalCoverTransferTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.built = probe.build_certificate()
        cls.raw = probe.DEFAULT_CERTIFICATE.read_bytes()
        cls.stored = json.loads(cls.raw.decode("utf-8"))

    def test_01_semantic_replay(self) -> None:
        probe.validate_certificate(self.stored)

    def test_02_raw_byte_replay(self) -> None:
        self.assertEqual(self.raw, probe.rendered_bytes(self.built))

    def test_03_payload_hash(self) -> None:
        self.assertEqual(
            self.stored["integrity"]["payload_sha256"],
            probe.payload_hash(self.stored),
        )

    def test_04_general_interface_formula(self) -> None:
        formula = self.stored["transfer_formula"]
        self.assertEqual(formula["rows_checked"], 208)
        self.assertEqual(formula["one_sided_slack"], "(4-m^2)/(8*n^2)")

    def test_05_m2_is_exact_threshold(self) -> None:
        row = self.stored["transfer_formula"]["selected_rows"]["n4_m2"]
        self.assertEqual(row["combined_demand"], "1/32")
        self.assertEqual(row["one_sided_slack"], "0/1")

    def test_06_m3_is_first_failure(self) -> None:
        row = self.stored["transfer_formula"]["selected_rows"]["n4_m3"]
        self.assertEqual(row["one_sided_slack"], "-5/128")
        self.assertEqual(row["two_sided_slack"], "-1/128")
        self.assertEqual(
            row["minimum_extra_successor_root_weight_after_one_sided"], "5/512"
        )

    def test_07_boundary_only_actual_cell_no_go(self) -> None:
        row = self.stored["T200_exact_pass_and_boundary_only_no_go"][
            "highlighted_actual_cell"
        ]
        self.assertEqual(row["state"]["id"], "[981,1036)")
        self.assertEqual(row["boundary_only"]["slack"], "-1/32")

    def test_08_T200_one_sided_complete_pass(self) -> None:
        correction = self.stored["T200_exact_pass_and_boundary_only_no_go"][
            "corrections"
        ]["one_sided"]
        self.assertTrue(correction["feasible_on_all_actual_cells"])
        self.assertEqual(correction["negative_cell_count"], 0)
        self.assertEqual(correction["physical_price_from_root_costs"], "81/400")

    def test_09_T250_actual_m3_failure(self) -> None:
        fixture = self.stored["T250_exact_one_sided_transfer_no_go"]
        row = fixture["highlighted_actual_cell"]
        self.assertEqual(row["state"]["id"], "[1100,1114)")
        self.assertEqual(row["state"]["combined_demand"], "9/128")
        self.assertEqual(row["one_sided"]["slack"], "-5/128")
        self.assertFalse(
            fixture["corrections"]["one_sided"]["feasible_on_all_actual_cells"]
        )

    def test_10_canonical_dual_and_physical_price(self) -> None:
        for key in (
            "T200_exact_pass_and_boundary_only_no_go",
            "T250_exact_one_sided_transfer_no_go",
        ):
            dual = self.stored[key]["canonical_cell_length_dual"]
            self.assertEqual(dual["root_columns_saturated"], 78)
            self.assertTrue(dual["lower_bound_for_every_feasible_nonnegative_root_cover"])
        price = self.stored["physical_internal_price"]
        self.assertEqual(
            price["T200_predecessor_interface_root"]["physical_price"], "9/100"
        )
        self.assertEqual(
            price["T250_highlighted_row_minimum_successor_add_on"]
            ["minimum_physical_price_for_this_add_on"],
            "87/3200",
        )

    def test_11_ownership_gates(self) -> None:
        ownership = self.stored["ownership"]
        self.assertTrue(ownership["gothic_rows_replaced_one_for_one"])
        self.assertTrue(ownership["direct_M_pair_supports_disjoint"])
        self.assertFalse(ownership["external_payment_owner_supplied"])
        self.assertFalse(ownership["shared_endpoint_diagonal_owner_created"])

    def test_12_all_adversarial_mutations_rejected(self) -> None:
        self.assertEqual(probe.self_check(self.stored), 12)


if __name__ == "__main__":
    unittest.main()
