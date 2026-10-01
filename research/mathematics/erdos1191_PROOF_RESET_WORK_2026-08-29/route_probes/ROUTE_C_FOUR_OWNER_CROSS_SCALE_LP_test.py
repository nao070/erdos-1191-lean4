#!/usr/bin/env python3
"""Focused tests for the exact 26-channel four-owner cross-scale LP."""

from __future__ import annotations

import copy
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


MODULE = "ROUTE_C_FOUR_OWNER_CROSS_SCALE_LP_certificate"


def load_certificate_module():
    """Load the real certificate or return ``None`` for the initial RED run."""

    try:
        return importlib.import_module(MODULE)
    except ModuleNotFoundError:
        return None


class FourOwnerCrossScaleLPTests(unittest.TestCase):
    def test_exact_physical_channel_and_cell_census(self) -> None:
        """Catches duplicate shared channels, a missing event, or a fake 63-cell grid."""

        cert = load_certificate_module()
        self.assertIsNotNone(cert, "four-owner certificate implementation is missing")
        result = cert.build_certificate()["four_owner_lp"]
        self.assertEqual(result["raw_owner_channel_occurrence_count"], 28)
        self.assertEqual(result["physical_channel_count"], 26)
        self.assertEqual(result["deduplicated_owner_channel_count"], 2)
        self.assertEqual(result["finite_event_count"], 64)
        self.assertEqual(result["positive_length_cell_count"], 63)
        self.assertEqual(result["complete_real_line_cell_count"], 65)
        self.assertEqual(result["event_collisions"], {
            "2125": ["a5+1600", "a15+400"],
        })
        self.assertEqual(result["shared_channel_indices"], {
            "n4_T200_last_equals_n8_T200_first": 4,
            "n4_T800_last_equals_n8_T800_first": 17,
        })

    def test_all_root_prices_have_two_independent_exact_replays(self) -> None:
        """Catches trace pricing or a same-scale surrogate for an unequal-width root."""

        cert = load_certificate_module()
        self.assertIsNotNone(cert)
        result = cert.build_certificate()["four_owner_lp"]
        self.assertEqual(result["physical_root_count"], 325)
        self.assertEqual(result["same_scale_root_count"], 156)
        self.assertEqual(result["cross_scale_root_count"], 169)
        self.assertEqual(result["cell_sum_root_price_check_count"], 325)
        self.assertEqual(result["C091_oriented_formula_check_count"], 325)
        self.assertEqual(result["root_price_audit"]["0,13"], {
            "kind": "cross_scale",
            "physical_cost": "2/1",
        })
        self.assertEqual(result["root_price_audit"]["9,17"], {
            "kind": "cross_scale",
            "physical_cost": "41/40",
        })

    def test_full_and_no_cross_lp_have_the_same_exact_optimum(self) -> None:
        """Catches a numerical-only solve or an artificial cross-scale saving."""

        cert = load_certificate_module()
        self.assertIsNotNone(cert)
        result = cert.build_certificate()["four_owner_lp"]
        self.assertEqual(result["owner_count"], 4)
        self.assertEqual(result["owner_cell_constraint_count"], 252)
        self.assertEqual(result["full_owner_root_variable_count"], 1300)
        self.assertEqual(result["full_dual_column_check_count"], 1300)
        self.assertEqual(result["no_cross_owner_root_variable_count"], 624)
        self.assertEqual(result["integrated_signed_demand"], "4663/25600")
        self.assertEqual(result["full_optimum"], "156321/512000")
        self.assertEqual(result["no_cross_scale_optimum"], "156321/512000")
        self.assertEqual(result["full_minus_no_cross_gap"], "0/1")
        self.assertEqual(result["surplus_over_integrated_demand"], "63061/512000")
        self.assertEqual(result["full_primal_dual_gap"], "0/1")

    def test_each_owner_has_an_exact_primal_dual_witness(self) -> None:
        """Catches pooled demand rows or a witness that omits one owner."""

        cert = load_certificate_module()
        self.assertIsNotNone(cert)
        owners = cert.build_certificate()["four_owner_lp"]["owners"]
        self.assertEqual(owners["n4_T200"], {
            "channel_indices": [0, 1, 2, 3, 4],
            "integrated_demand": "63/640",
            "full_optimum": "29/200",
            "no_cross_optimum": "29/200",
            "primal_root_weights": {"0,2": "1/40", "2,4": "1/40"},
            "dual_cell_weights": {
                "[525,616)": "698/5",
                "[636,709)": "1426/15",
                "[749,816)": "418/5",
                "[836,864)": "2186/15",
            },
            "minimum_cross_margin": "161/300",
            "minimum_cross_roots": ["0,13"],
            "positive_cross_root_count": 0,
        })
        self.assertEqual(owners["n8_T200"], {
            "channel_indices": list(range(4, 13)),
            "integrated_demand": "169/12800",
            "full_optimum": "139/3200",
            "no_cross_optimum": "139/3200",
            "primal_root_weights": {"4,6": "1/128", "10,12": "1/128"},
            "dual_cell_weights": {
                "[981,1036)": "247/2",
                "[1109,1149)": "321/2",
                "[1725,1744)": "351/2",
                "[1796,1869)": "193/2",
            },
            "minimum_cross_margin": "21/100",
            "minimum_cross_roots": ["6,13"],
            "positive_cross_root_count": 0,
        })
        self.assertEqual(owners["n4_T800"], {
            "channel_indices": [13, 14, 15, 16, 17],
            "integrated_demand": "0/1",
            "full_optimum": "0/1",
            "no_cross_optimum": "0/1",
            "primal_root_weights": {},
            "dual_cell_weights": {},
            "minimum_cross_margin": "41/40",
            "minimum_cross_roots": ["9,17", "10,18"],
            "positive_cross_root_count": 0,
        })
        self.assertEqual(owners["n8_T800"], {
            "channel_indices": list(range(17, 26)),
            "integrated_demand": "361/5120",
            "full_optimum": "59841/512000",
            "no_cross_optimum": "59841/512000",
            "primal_root_weights": {
                "17,18": "13/512",
                "17,19": "131/2560",
                "23,24": "131/2560",
                "24,25": "49/640",
            },
            "dual_cell_weights": {
                "[1596,1621)": "933/10",
                "[1669,1725)": "351/2",
                "[2349,2396)": "381/2",
                "[2396,2464)": "1263/10",
            },
            "minimum_cross_margin": "29/100",
            "minimum_cross_roots": ["9,19", "9,20", "9,21", "9,22"],
            "positive_cross_root_count": 0,
        })

    def test_cross_mass_secondary_face_is_zero_and_strictly_excluded(self) -> None:
        """Catches claiming nonessentiality from one sparse primal alone."""

        cert = load_certificate_module()
        self.assertIsNotNone(cert)
        face = cert.build_certificate()["four_owner_lp"]["optimal_face_cross_mass"]
        self.assertEqual(face, {
            "objective_definition": "sum of all owner-labelled cross-scale root coefficients",
            "minimum_cross_root_mass": "0/1",
            "minimum_cross_physical_price_contribution": "0/1",
            "cross_free_optimal_witness_present": True,
            "all_676_owner_cross_columns_have_strict_dual_margin": True,
            "cross_roots_forced_zero_on_exposed_optimal_face": True,
        })

    def test_physical_price_is_paid_once_and_owner_rows_are_separate(self) -> None:
        """Catches crediting one root to several demands while pricing it once."""

        cert = load_certificate_module()
        self.assertIsNotNone(cert)
        ledger = cert.build_certificate()["four_owner_lp"]["ownership_ledger"]
        self.assertEqual(ledger, {
            "root_coefficient_identity": "q_e=sum_o x_(o,e)",
            "owner_correction_identity": "P_(o,c)=sum_e R_(c,e)*x_(o,e)",
            "pointwise_sum_identity": "sum_o P_(o,c)=sum_e R_(c,e)*q_e",
            "physical_price_identity": "sum_o,e p_e*x_(o,e)=sum_e p_e*q_e",
            "one_root_unit_credited_to_multiple_owners_for_one_price": False,
            "owner_demands_pooled_before_cover": False,
            "exact_pointwise_identity_check_count": 63,
            "exact_objective_identity_verified": True,
        })

    def test_inactive_owner_and_scope_caveats_are_machine_visible(self) -> None:
        """Catches promotion of a three-active finite fixture into C058."""

        cert = load_certificate_module()
        self.assertIsNotNone(cert)
        certificate = cert.build_certificate()
        result = certificate["four_owner_lp"]
        self.assertEqual(result["inactive_owner_caveat"], {
            "owner": "n4_T800",
            "zero_demand_cell_count": 63,
            "nonzero_demand_cell_count": 0,
            "block_span": 440,
            "width": 800,
            "four_active_owner_fixture": False,
        })
        self.assertEqual(certificate["scope"], {
            "fixed_16_mark_four_owner_fixture_only": True,
            "four_active_owner_fixture": False,
            "nonnegative_globally_owner_labelled_roots_only": True,
            "cell_dependent_owner_reassignment_allowed": False,
            "signed_coordinate_row_split_included": False,
            "aggregate_J_or_indefinite_cross_blocks_included": False,
            "signed_source_to_sink_owner_flow_included": False,
            "direct_M_Gothic_one_for_one_payment_proved": False,
            "birth_gate_final_terminal_ownership_proved": False,
            "active_current_to_past_payment_proved": False,
            "positive_net_Phi_proved": False,
            "other_scale_ratios_or_histories_proved": False,
            "continuum_phase_or_common_history_ledger_proved": False,
            "C058_Q1_Q2_proved": False,
            "publication_novelty_or_prize_claimed": False,
        })

    def test_rehashed_semantic_mutations_and_scope_promotions_are_rejected(self) -> None:
        """Catches a hash-only verifier or a rehashed false C058 promotion."""

        cert = load_certificate_module()
        self.assertIsNotNone(cert)
        certificate = cert.build_certificate()
        self.assertEqual(
            certificate["integrity"]["payload_sha256"], cert.payload_hash(certificate)
        )
        self.assertEqual(cert.self_check(certificate), {
            "mutations_attempted": 18,
            "mutations_rejected": 18,
        })

        changed = copy.deepcopy(certificate)
        changed["scope"]["C058_Q1_Q2_proved"] = True
        changed["integrity"]["payload_sha256"] = cert.payload_hash(changed)
        with self.assertRaises(cert.CertificateError):
            cert.verify_certificate(changed)

    def test_integrity_canonical_json_flag_must_be_a_boolean(self) -> None:
        """Catches Python's equality between True and the integer one."""

        cert = load_certificate_module()
        self.assertIsNotNone(cert)
        certificate = cert.build_certificate()
        certificate["integrity"]["canonical_json"] = 1
        with self.assertRaises(cert.CertificateError):
            cert.verify_certificate(certificate)

    def test_cli_generates_and_replays_literal_canonical_bytes(self) -> None:
        """Catches a verifier that validates parsed data but ignores supplied bytes."""

        cert = load_certificate_module()
        self.assertIsNotNone(cert)
        script = Path(cert.__file__).resolve()
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory) / "certificate.json"
            generated = subprocess.run(
                [sys.executable, str(script), "--output", str(output)],
                check=False,
                capture_output=True,
                text=True,
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            )
            self.assertEqual(generated.returncode, 0, generated.stderr)
            raw = output.read_bytes()
            parsed = json.loads(raw.decode("utf-8"))
            self.assertEqual(raw, cert.rendered_bytes(parsed))

            replay = subprocess.run(
                [sys.executable, str(script), "--verify", str(output), "--self-check"],
                check=False,
                capture_output=True,
                text=True,
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            )
            self.assertEqual(replay.returncode, 0, replay.stderr)
            self.assertIn("mutations_attempted=18", replay.stdout)
            self.assertIn("mutations_rejected=18", replay.stdout)

    def test_cli_rejects_a_nonobject_json_root_without_traceback(self) -> None:
        """Catches an uncaught AttributeError on syntactically valid JSON arrays."""

        cert = load_certificate_module()
        self.assertIsNotNone(cert)
        with tempfile.TemporaryDirectory() as temporary_directory:
            malformed = Path(temporary_directory) / "array.json"
            malformed.write_text("[]\n", encoding="utf-8")
            replay = subprocess.run(
                [
                    sys.executable,
                    str(Path(cert.__file__).resolve()),
                    "--verify",
                    str(malformed),
                ],
                check=False,
                capture_output=True,
                text=True,
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            )
            self.assertEqual(replay.returncode, 1)
            self.assertIn("ERROR: certificate root must be an object", replay.stderr)
            self.assertNotIn("Traceback", replay.stderr)

    def test_committed_json_is_the_literal_semantic_replay(self) -> None:
        """Catches a stale, pretty-printed, or hand-edited committed certificate."""

        cert = load_certificate_module()
        self.assertIsNotNone(cert)
        raw = cert.DEFAULT_CERTIFICATE.read_bytes()
        parsed = json.loads(raw.decode("utf-8"))
        self.assertEqual(raw, cert.rendered_bytes(parsed))
        self.assertEqual(parsed, cert.build_certificate())
        cert.verify_certificate(parsed)


if __name__ == "__main__":
    unittest.main()
