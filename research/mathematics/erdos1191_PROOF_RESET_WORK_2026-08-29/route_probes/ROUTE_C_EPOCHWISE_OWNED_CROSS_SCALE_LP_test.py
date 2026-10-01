#!/usr/bin/env python3
"""Focused tests for the exact epochwise-owned cross-scale LP."""

from __future__ import annotations

import importlib
import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


class EpochwiseOwnedCrossScaleLPTests(unittest.TestCase):
    def test_nonnegative_owned_columns_do_not_improve_either_epoch(self) -> None:
        """Catches cross-scale saving manufactured by sharing one column twice."""
        try:
            cert = importlib.import_module(
                "ROUTE_C_EPOCHWISE_OWNED_CROSS_SCALE_LP_certificate"
            )
        except ModuleNotFoundError:
            self.fail("epochwise-owned cross-scale certificate implementation is missing")

        result = cert.build_certificate()["epochwise_owned_lp"]
        self.assertEqual(result["common_cell_count"], 40)
        self.assertEqual(result["owned_demand_row_count"], 80)
        self.assertEqual(result["physical_root_identity_count"], 91)
        self.assertEqual(result["owner_root_variable_count"], 182)
        self.assertEqual(result["small_epoch_optimum"], "29/200")
        self.assertEqual(result["large_epoch_optimum"], "59841/512000")
        self.assertEqual(result["total_epochwise_owned_optimum"], "134081/512000")
        self.assertEqual(result["saving_against_same_scale_separate_optima"], "0/1")
        self.assertEqual(result["gap_above_weaker_sum_cover_optimum"], "10643/1228800")
        self.assertEqual(result["positive_cross_scale_owner_variable_count"], 0)
        self.assertEqual(result["small_owner_minimum_cross_root_margin"], "169/300")
        self.assertEqual(result["large_owner_minimum_cross_root_margin"], "817/500")

    def test_exact_owner_witnesses_strictly_exclude_every_foreign_column(self) -> None:
        """Catches a numerical optimum or an unpriced off-scale correction."""
        cert = importlib.import_module(
            "ROUTE_C_EPOCHWISE_OWNED_CROSS_SCALE_LP_certificate"
        )
        result = cert.build_certificate()["epochwise_owned_lp"]

        self.assertIn("small_owner", result)
        self.assertIn("large_owner", result)
        self.assertEqual(result["small_owner"], {
            "objective": "29/200",
            "primal_root_weights": {"0,2": "1/40", "2,4": "1/40"},
            "dual_cell_weights": {
                "[525,616)": "698/5",
                "[636,709)": "1426/15",
                "[749,816)": "418/5",
                "[836,864)": "2186/15",
            },
            "minimum_cross_root": "2,5",
            "minimum_cross_root_margin": "169/300",
            "minimum_foreign_same_scale_root": "5,6",
            "minimum_foreign_same_scale_root_margin": "691/2400",
        })
        self.assertEqual(result["large_owner"], {
            "objective": "59841/512000",
            "primal_root_weights": {
                "5,6": "13/512",
                "5,7": "131/2560",
                "11,13": "131/2560",
                "12,13": "13/512",
            },
            "dual_cell_weights": {
                "[1596,1664)": "933/10",
                "[1664,1725)": "351/2",
                "[2349,2396)": "381/2",
                "[2396,2464)": "1263/10",
            },
            "minimum_cross_root": "0,6",
            "minimum_cross_root_margin": "817/500",
            "minimum_foreign_same_scale_root": "0,1",
            "minimum_foreign_same_scale_root_margin": "321/200",
        })

    def test_every_owned_aggregate_column_is_fully_priced_and_inactive(self) -> None:
        """Catches a free J column or reuse of one aggregate price by two owners."""
        cert = importlib.import_module(
            "ROUTE_C_EPOCHWISE_OWNED_CROSS_SCALE_LP_certificate"
        )
        result = cert.build_certificate()["epochwise_owned_lp"]
        self.assertIn("owned_aggregate_audit", result)
        self.assertEqual(result["aggregate_column_identity_count"], 3)
        self.assertEqual(result["owner_aggregate_variable_count"], 6)
        self.assertEqual(result["total_nonnegative_owner_variable_count"], 188)
        self.assertEqual(result["owned_aggregate_audit"], {
            "small_owner": {
                "J4": {"coefficient": "0/1", "physical_cost": "3/1", "dual_margin": "343/150"},
                "J8": {"coefficient": "0/1", "physical_cost": "688/25", "dual_margin": "8213/300"},
                "J_all": {"coefficient": "0/1", "physical_cost": "702/25", "dual_margin": "82763/3000"},
            },
            "large_owner": {
                "J4": {"coefficient": "0/1", "physical_cost": "3/1", "dual_margin": "3/1"},
                "J8": {"coefficient": "0/1", "physical_cost": "688/25", "dual_margin": "18919/1000"},
                "J_all": {"coefficient": "0/1", "physical_cost": "702/25", "dual_margin": "19479/1000"},
            },
        })

    def test_legacy_sum_cover_tight_row_fails_epochwise_ownership(self) -> None:
        """Catches silently retaining the weaker C097 combined inequality."""
        cert = importlib.import_module(
            "ROUTE_C_EPOCHWISE_OWNED_CROSS_SCALE_LP_certificate"
        )
        certificate = cert.build_certificate()
        result = certificate["epochwise_owned_lp"]
        self.assertIn("legacy_sum_cover_highlight", result)
        self.assertEqual(result["legacy_sum_cover_highlight"], {
            "cell": "[749,816)",
            "small_demand": "1/3200",
            "small_owned_correction": "271/1024000",
            "small_owned_slack": "-49/1024000",
            "large_demand": "0/1",
            "large_owned_correction": "49/1024000",
            "large_owned_slack": "49/1024000",
            "summed_slack": "0/1",
        })
        self.assertIn("scope", certificate)
        self.assertEqual(certificate["scope"], {
            "fixed_14_channel_two_demand_fixture_only": True,
            "nonnegative_global_partition_relaxation": True,
            "each_owner_copy_pays_full_physical_price": True,
            "one_physical_column_credited_twice_for_one_price": False,
            "canonical_signed_coordinate_row_split_audited": True,
            "arbitrary_signed_owned_splits_audited": False,
            "four_owner_26_channel_model_audited": False,
            "signed_cross_term_cancellation_payment_proved": False,
            "direct_M_Gothic_one_for_one_payment_proved": False,
            "birth_gate_final_terminal_ownership_proved": False,
            "active_current_to_past_payment_proved": False,
            "other_scale_ratios_or_histories_proved": False,
            "C058_Q1_Q2_proved": False,
            "publication_novelty_or_prize_claimed": False,
        })

    def test_rehashed_semantic_mutations_cannot_promote_the_scope(self) -> None:
        """Catches a hash-only verifier or a mutation that upgrades C058."""
        cert = importlib.import_module(
            "ROUTE_C_EPOCHWISE_OWNED_CROSS_SCALE_LP_certificate"
        )
        certificate = cert.build_certificate()
        self.assertIn("integrity", certificate)
        self.assertEqual(
            certificate["integrity"]["payload_sha256"], cert.payload_hash(certificate)
        )
        self.assertEqual(cert.self_check(certificate), {
            "mutations_attempted": 12,
            "mutations_rejected": 12,
        })

        changed = copy.deepcopy(certificate)
        changed["scope"]["C058_Q1_Q2_proved"] = True
        changed["integrity"]["payload_sha256"] = cert.payload_hash(changed)
        with self.assertRaises(cert.CertificateError):
            cert.verify_certificate(changed)

    def test_canonical_signed_coordinate_row_split_also_has_no_saving(self) -> None:
        """Catches a noncanonical split or an unowned signed cross-term debit."""
        cert = importlib.import_module(
            "ROUTE_C_EPOCHWISE_OWNED_CROSS_SCALE_LP_certificate"
        )
        result = cert.build_certificate()["epochwise_owned_lp"]
        self.assertIn("coordinate_row_split", result)
        self.assertEqual(result["coordinate_row_split"], {
            "small_share_formula": "z_i*(z_i-z_j)",
            "large_share_formula": "z_j*(z_j-z_i)",
            "pointwise_share_sum_equals_physical_root_square": True,
            "signed_negative_cross_cell_entry_count": 9,
            "signed_example": {
                "root": "3,5",
                "cell": "[749,816)",
                "small_share": "1/800",
                "large_share": "-1/1600",
                "physical_sum": "1/1600",
            },
            "optimal_physical_price": "134081/512000",
            "primal_dual_gap": "0/1",
            "positive_cross_scale_root_count": 0,
            "minimum_cross_scale_root": "2,7",
            "minimum_cross_scale_root_dual_margin": "237/500",
            "primal_root_weights": {
                "0,2": "1/40",
                "2,4": "1/40",
                "5,6": "13/512",
                "5,7": "131/2560",
                "11,13": "131/2560",
                "12,13": "13/512",
            },
            "small_dual_cell_weights": {
                "[525,616)": "1934/15",
                "[636,709)": "1586/15",
                "[749,816)": "1894/15",
                "[836,864)": "1546/15",
            },
            "large_dual_cell_weights": {
                "[1596,1664)": "933/10",
                "[1664,1725)": "351/2",
                "[2349,2396)": "381/2",
                "[2396,2464)": "1263/10",
            },
            "aggregate_dual_margins": {
                "J4": "121/50",
                "J8": "18919/1000",
                "J_all": "114167/6000",
            },
        })

    def test_cli_generates_and_replays_literal_canonical_bytes(self) -> None:
        """Catches a verifier that trusts parsed summaries instead of raw bytes."""
        cert = importlib.import_module(
            "ROUTE_C_EPOCHWISE_OWNED_CROSS_SCALE_LP_certificate"
        )
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
            self.assertTrue(output.is_file())
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
            self.assertIn("mutations_rejected=12", replay.stdout)

    def test_default_stdout_is_only_canonical_json(self) -> None:
        """Catches status text appended to the default machine-readable stream."""
        cert = importlib.import_module(
            "ROUTE_C_EPOCHWISE_OWNED_CROSS_SCALE_LP_certificate"
        )
        generated = subprocess.run(
            [sys.executable, str(Path(cert.__file__).resolve())],
            check=False,
            capture_output=True,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )
        self.assertEqual(generated.returncode, 0, generated.stderr.decode())
        certificate = json.loads(generated.stdout.decode("utf-8"))
        self.assertEqual(generated.stdout, cert.rendered_bytes(certificate))

    def test_integrity_canonical_json_flag_must_be_a_boolean(self) -> None:
        """Catches Python's equality between True and the integer one."""
        cert = importlib.import_module(
            "ROUTE_C_EPOCHWISE_OWNED_CROSS_SCALE_LP_certificate"
        )
        certificate = cert.build_certificate()
        certificate["integrity"]["canonical_json"] = 1
        with self.assertRaises(cert.CertificateError):
            cert.verify_certificate(certificate)

    def test_scope_booleans_cannot_be_replaced_by_equal_integers(self) -> None:
        """Catches Python's True/1 and False/0 equality in semantic replay."""
        cert = importlib.import_module(
            "ROUTE_C_EPOCHWISE_OWNED_CROSS_SCALE_LP_certificate"
        )
        for key, integer in (
            ("fixed_14_channel_two_demand_fixture_only", 1),
            ("C058_Q1_Q2_proved", 0),
        ):
            with self.subTest(key=key):
                certificate = cert.build_certificate()
                certificate["scope"][key] = integer
                certificate["integrity"]["payload_sha256"] = cert.payload_hash(
                    certificate
                )
                with self.assertRaises(cert.CertificateError):
                    cert.verify_certificate(certificate)

    def test_committed_certificate_is_the_exact_canonical_replay(self) -> None:
        """Catches a stale or hand-edited committed JSON certificate."""
        cert = importlib.import_module(
            "ROUTE_C_EPOCHWISE_OWNED_CROSS_SCALE_LP_certificate"
        )
        self.assertTrue(cert.DEFAULT_CERTIFICATE.is_file())
        raw = cert.DEFAULT_CERTIFICATE.read_bytes()
        certificate = json.loads(raw.decode("utf-8"))
        self.assertEqual(raw, cert.rendered_bytes(certificate))
        self.assertEqual(certificate, cert.build_certificate())
        cert.verify_certificate(certificate)


if __name__ == "__main__":
    unittest.main()
