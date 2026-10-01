from __future__ import annotations

from fractions import Fraction as F
import importlib
import json
import unittest


MODULE_NAME = "ROUTE_C_MIXED_SCALE_HAAR_ENERGY_certificate"


class MixedScaleHaarEnergyTests(unittest.TestCase):
    def test_mixed_inner_product_has_asymmetric_shift_value(self) -> None:
        """Catches dropping the orientation of the shift when T differs from S."""
        try:
            certificate = importlib.import_module(MODULE_NAME)
        except ModuleNotFoundError:
            self.fail(f"{MODULE_NAME}.py has not been implemented")

        self.assertEqual(certificate.mixed_haar_inner(F(2), F(4), F(-1)), F(2))
        self.assertEqual(certificate.mixed_haar_inner(F(2), F(4), F(1)), F(-1))

    def test_half_open_union_cells_reproduce_the_inner_product(self) -> None:
        """Catches a closed-endpoint state or a missing mixed-scale breakpoint."""
        certificate = importlib.import_module(MODULE_NAME)
        if not hasattr(certificate, "mixed_atomic_cells"):
            self.fail("mixed_atomic_cells has not been implemented")

        cells = certificate.mixed_atomic_cells(F(2), F(4), F(-1))
        finite = [cell for cell in cells if cell["length"] != "infinite"]
        self.assertEqual(
            [(cell["left"], cell["right"], tuple(cell["state"])) for cell in finite],
            [
                (F(-1), F(0), (0, 1)),
                (F(0), F(2), (1, 1)),
                (F(2), F(3), (-1, 1)),
                (F(3), F(4), (-1, -1)),
                (F(4), F(7), (0, -1)),
            ],
        )
        self.assertEqual(
            sum((cell["length"] * cell["state"][0] * cell["state"][1] for cell in finite), F(0)),
            F(2),
        )

    def test_mixed_linear_energy_keeps_both_scale_norms(self) -> None:
        """Catches using the same-scale 2T normalization for both channels."""
        certificate = importlib.import_module(MODULE_NAME)
        if not hasattr(certificate, "mixed_linear_energy"):
            self.fail("mixed_linear_energy has not been implemented")

        self.assertEqual(
            certificate.mixed_linear_energy(F(2), F(4), F(-1), F(3, 2), F(-2, 3)),
            F(77, 9),
        )
        self.assertEqual(certificate.mixed_haar_inner(F(4), F(2), F(1)), F(2))
        self.assertEqual(certificate.mixed_haar_inner(F(4), F(4), F(4)), F(-4))
        self.assertEqual(certificate.mixed_haar_inner(F(8), F(4), F(2)), F(4))

    def test_price_lowering_cross_term_fails_an_actual_cell(self) -> None:
        """Catches treating a negative integrated cross term as a legal free saving."""
        certificate = importlib.import_module(MODULE_NAME)
        if not hasattr(certificate, "two_scale_cross_block_audit"):
            self.fail("two_scale_cross_block_audit has not been implemented")

        audit = certificate.two_scale_cross_block_audit()
        self.assertEqual(F(audit["canonical_same_scale_demand"]), F(2))
        self.assertEqual(F(audit["price_lowering_attempt"]["physical_price"]), F(7, 4))
        self.assertEqual(audit["price_lowering_attempt"]["violating_cell"], "[0,2)")
        self.assertEqual(F(audit["price_lowering_attempt"]["violating_slack"]), F(-1, 8))
        self.assertEqual(F(audit["actual_cell_feasible_cross_block"]["physical_price"]), F(9, 4))
        self.assertEqual(F(audit["actual_cell_feasible_cross_block"]["excess_over_demand"]), F(1, 4))

    def test_actual_cell_grid_has_no_below_demand_cross_block(self) -> None:
        """Catches a mixed block that passes cells but violates integrated weak duality."""
        certificate = importlib.import_module(MODULE_NAME)
        if not hasattr(certificate, "cross_block_grid_audit"):
            self.fail("cross_block_grid_audit has not been implemented")

        audit = certificate.cross_block_grid_audit()
        self.assertGreater(audit["actual_cell_feasible_count"], 0)
        self.assertEqual(audit["feasible_negative_excess_count"], 0)
        self.assertEqual(F(audit["minimum_feasible_excess"]), F(0))
        self.assertTrue(audit["zero_excess_only_at_zero_added_block"])
        self.assertEqual(F(audit["minimum_feasible_excess_with_nonzero_cross"]), F(1, 4))

    def test_dyadic_formula_audit_covers_both_orientations_and_breakpoints(self) -> None:
        """Catches a formula valid only for T=S, d>=0, or away from a knot."""
        certificate = importlib.import_module(MODULE_NAME)
        if not hasattr(certificate, "mixed_formula_audit"):
            self.fail("mixed_formula_audit has not been implemented")

        audit = certificate.mixed_formula_audit()
        self.assertGreaterEqual(audit["exact_dyadic_rows_checked"], 1000)
        self.assertTrue(audit["cell_sum_equals_hinge_formula_everywhere"])
        self.assertTrue(audit["orientation_symmetry_everywhere"])
        self.assertTrue(audit["common_dilation_everywhere"])
        self.assertEqual(audit["same_scale_T4_samples"], {
            "d=0": "8/1",
            "d=1": "5/1",
            "d=4": "-4/1",
            "d=8": "0/1",
        })

    def test_certificate_states_the_exact_no_go_scope(self) -> None:
        """Catches promotion of the physical lower bound into a paid Route-C ledger."""
        certificate = importlib.import_module(MODULE_NAME)
        if not hasattr(certificate, "build_certificate"):
            self.fail("build_certificate has not been implemented")

        value = certificate.build_certificate()
        self.assertEqual(value["status"], "EXACT_MIXED_SCALE_PHYSICAL_DUAL_NO_GO_ONLY")
        self.assertTrue(value["cell_length_dual_theorem"]["arbitrary_finite_scale_family"])
        self.assertTrue(value["cell_length_dual_theorem"]["cross_blocks_cannot_beat_integrated_demand"])
        self.assertIn("continuum-phase paid ledger", value["scope"]["not_proved"])
        self.assertIn("C058, Q1, or Q2", value["scope"]["not_proved"])
        self.assertEqual(value["integrity"]["payload_sha256"], certificate.payload_hash(value))

    def test_committed_json_replays_literal_bytes(self) -> None:
        """Catches stale generated evidence after the exact code changes."""
        certificate = importlib.import_module(MODULE_NAME)
        if not hasattr(certificate, "DEFAULT_CERTIFICATE"):
            self.fail("DEFAULT_CERTIFICATE has not been implemented")
        if not certificate.DEFAULT_CERTIFICATE.exists():
            self.fail("committed mixed-scale JSON has not been generated")

        raw = certificate.DEFAULT_CERTIFICATE.read_bytes()
        loaded = json.loads(raw.decode("utf-8"))
        certificate.validate_certificate(loaded)
        self.assertEqual(raw, certificate.rendered_bytes(certificate.build_certificate()))

    def test_self_check_rejects_formula_dual_scope_and_hash_mutations(self) -> None:
        """Catches a hash-valid semantic promotion or corrupted exact formula."""
        certificate = importlib.import_module(MODULE_NAME)
        if not hasattr(certificate, "self_check"):
            self.fail("self_check has not been implemented")
        self.assertEqual(certificate.self_check(certificate.build_certificate()), 8)


if __name__ == "__main__":
    unittest.main()
