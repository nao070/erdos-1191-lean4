#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import unittest

import ROUTE_C_PARAMETRIC_PHYSICAL_COVER_CHAMBERS_certificate as cert


HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE / "ROUTE_C_PARAMETRIC_PHYSICAL_COVER_CHAMBERS_certificate.json"


class ParametricPhysicalCoverChambersTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.built = cert.build_certificate()
        cls.raw = CERTIFICATE.read_bytes()
        cls.loaded = json.loads(cls.raw)

    def test_01_certificate_validates(self) -> None:
        cert.validate_certificate(self.loaded, self.built)

    def test_02_committed_json_has_literal_raw_byte_replay(self) -> None:
        self.assertEqual(self.raw, cert.rendered_bytes(self.built))

    def test_03_one_fixed_golomb_history(self) -> None:
        fixture = self.built["fixture"]
        self.assertEqual(fixture["full_points"], [k * (k + 100) for k in range(16)])
        self.assertTrue(fixture["all_120_positive_differences_distinct"])
        self.assertTrue(fixture["not_a_changing_family"])

    def test_04_exact_event_breakpoints(self) -> None:
        theorem = self.built["chamber_theorem"]
        self.assertEqual(theorem["open_event_chamber_count"], 22)
        self.assertEqual(theorem["open_optimality_chamber_count"], 30)
        self.assertEqual(
            theorem["event_breakpoints"],
            [cert.ftext(value) for value in cert.exact_breakpoints()],
        )

    def test_05_every_generic_event_chamber_has_complete_cells(self) -> None:
        events = self.built["chamber_theorem"]["event_chambers"]
        self.assertEqual(len(events), 22)
        self.assertTrue(all(event["generic_complete_real_line_cell_count"] == 40 for event in events))
        self.assertTrue(
            all(
                event["canonical_cell_length_dual"]["all_80_cost_columns_saturated"]
                for event in events
            )
        )

    def test_06_all_piecewise_primal_dual_gaps_are_zero(self) -> None:
        pieces = self.built["chamber_theorem"]["optimality_chambers"]
        self.assertEqual(len(pieces), 30)
        self.assertTrue(all(piece["zero_gap_for_every_T_in_open_piece"] for piece in pieces))
        self.assertTrue(
            all(
                piece["left_limiting_dual"]["objective"]
                == cert.ftext(
                    F(piece["optimal_value_formula"]["alpha"])
                    + F(piece["optimal_value_formula"]["beta"])
                    / F(piece["T_interval"]["lower"])
                )
                for piece in pieces
            )
        )

    def test_07_local_cross_chamber_primal_transport(self) -> None:
        transport = self.built["transport"]
        self.assertTrue(transport["same_primal_is_optimal_on_both_adjacent_open_event_chambers"])
        self.assertEqual(transport["open_chambers"], ["(381/2,216)", "(216,220)"])
        self.assertEqual([row["T"] for row in transport["actual_breakpoints"]], ["216/1", "220/1"])
        self.assertTrue(all(row["zero_gap"] for row in transport["actual_breakpoints"]))

    def test_08_fixed_primal_fails_at_T_221(self) -> None:
        failure = self.built["transport"]["literal_fixed_primal_fails_beyond_transport_window"]
        self.assertEqual(
            (failure["T"], failure["cell"], failure["lhs"], failure["rhs"], failure["slack"]),
            ("221/1", "[636,637)", "1/8", "9/32", "-5/32"),
        )

    def test_09_exact_positive_phase_obstruction(self) -> None:
        phase = self.built["phase_integrated_cover_excess"]
        obstruction = phase["certified_positive_subinterval"]
        self.assertEqual(obstruction["excess_formula"], "-479/1792+4169/(64T)")
        self.assertEqual(obstruction["minimum_excess"], "3317/96768")
        self.assertEqual(obstruction["rational_lower_bound"], "56389/13934592")
        self.assertGreater(F(phase["full_phase_integrated_cover_excess_at_least"]), 0)
        self.assertTrue(phase["zero_telescoping_on_this_fixture_is_impossible"])

    def test_10_isolated_breakpoint_scope_is_explicit(self) -> None:
        theorem = self.built["chamber_theorem"]
        self.assertTrue(theorem["breakpoint_values_have_measure_zero_in_phase_integration"])
        self.assertTrue(theorem["actual_breakpoint_optima_certified_separately_only_at_T_216_and_T_220"])
        self.assertIn(
            "the isolated actual LP optima at event breakpoints other than the separately checked T=216 and T=220",
            self.built["scope"]["not_proved"],
        )

    def test_11_scope_and_budget_owner_gates(self) -> None:
        scope = self.built["scope"]
        self.assertFalse(scope["budget_owner_supplied"])
        self.assertTrue(scope["root_SDDM_plus_two_J_class_only"])
        self.assertTrue(scope["same_scale_only"])
        self.assertIn(
            "C058, Q1, Q2, Erdos Problem 1191, novelty, publication, or prize eligibility",
            scope["not_proved"],
        )

    def test_12_payload_hash_and_mutations(self) -> None:
        self.assertEqual(self.built["integrity"]["payload_sha256"], cert.payload_hash(self.built))
        self.assertEqual(cert.self_check(), 12)
        self.assertEqual(
            hashlib.sha256(self.raw).hexdigest(),
            hashlib.sha256(cert.rendered_bytes(self.built)).hexdigest(),
        )


if __name__ == "__main__":
    unittest.main()
