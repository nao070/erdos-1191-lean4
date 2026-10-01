#!/usr/bin/env python3
"""Focused exact tests for the whole-stencil cross-width master."""

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


MODULE = "ROUTE_C_WHOLE_STENCIL_CROSS_WIDTH_MASTER_certificate"


class WholeStencilCrossWidthMasterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cert = importlib.import_module(MODULE)
        cls.value = cls.cert.build_certificate()

    def test_exact_epoch_block_witness_and_cross_width_dual(self) -> None:
        witness = self.value["epoch_block_cross_width_witness"]
        self.assertEqual(witness["owner_rows_checked"], 608)
        self.assertEqual(witness["strictly_positive_LDL_pivot_counts"], {"n4": 19, "n8": 31})
        self.assertTrue(witness["PSD_by_exact_epoch_block_LDL"])
        self.assertTrue(witness["zero_row_sum_exact"])
        self.assertTrue(witness["epoch_cross_block_zero_exact"])
        self.assertGreater(witness["cross_width_nonzero_entry_count_upper_triangle"], 0)
        self.assertEqual(witness["zero_owner_slack_count"], 254)
        self.assertEqual(
            witness["minimum_positive_owner_slack"],
            "41304919/12500000000000",
        )
        self.assertEqual(
            witness["physical_price"],
            "3900000000091/10000000000000",
        )
        self.assertEqual(
            witness["Phi"],
            "141015624909/10000000000000",
        )
        dual = self.value["no_cross_width_dual"]
        self.assertEqual(dual["support_count"], 380)
        self.assertEqual(dual["strictly_positive_LDL_pivot_count"], 48)
        self.assertEqual(
            dual["gap_above_twice_demand"],
            "16069938599/2048000000000",
        )

    def test_exact_whole_stencil_census_factors_and_bands(self) -> None:
        row = self.value["whole_stencil_Abel_Gothic_ledger"]
        self.assertEqual(
            (
                row["primitive_count"],
                row["four_corner_occurrence_count"],
                row["distinct_nonzero_Gothic_row_count"],
                row["mixed_sign_reused_row_count"],
                row["lambda_equals_2M_rows_checked"],
            ),
            (24, 96, 42, 28, 46),
        )
        self.assertTrue(row["no_extra_quadratic_factor"])
        self.assertTrue(row["lower_width_100_boundary_zero_for_every_primitive"])
        self.assertTrue(row["upper_width_1600_terminal_zero_for_every_primitive"])
        self.assertEqual(row["epoch_capacity_totals"], {"n4": "9/128", "n8": "1349/10240"})
        self.assertEqual(row["integrated_signed_demand"], "2069/10240")
        self.assertEqual(
            [band["band_equals_2f_minus_f_next"] for band in row["owner_band_ledger"]],
            [
                "-9/160",
                "-117/3200",
                "63/640",
                "169/12800",
                "9/320",
                "4331/51200",
                "0/1",
                "361/5120",
            ],
        )

    def test_exact_epoch_price_split_and_Fejer_gate(self) -> None:
        row = self.value["epoch_block_cross_width_witness"]
        self.assertEqual(
            row["epoch_price_and_Phi"]["n4"]["Phi"],
            "-290502965603/25000000000000",
        )
        self.assertEqual(
            row["epoch_price_and_Phi"]["n8"]["Phi"],
            "1286084055751/50000000000000",
        )
        gate = row["Fejer_weight_gate"]
        self.assertEqual(
            gate["positive_iff_w8_over_w4_exceeds"],
            "581005931206/1286084055751",
        )
        self.assertEqual(gate["Phi_at_m_4"], "2278661602463/800000000000000")
        self.assertEqual(gate["Phi_at_m_3"], "-1694343157/9000000000000")
        self.assertEqual(
            gate["Phi_at_81_over_100"],
            "46072215395231/5000000000000000",
        )
        self.assertTrue(gate["all_m_at_least_4_positive_on_this_fixture"])
        self.assertTrue(gate["m_3_negative_on_this_fixture"])

    def test_no_cross_width_dual_is_exact_and_strict(self) -> None:
        row = self.value["no_cross_width_dual"]
        self.assertEqual(row["support_by_width"], {"100": 0, "200": 152, "400": 152, "800": 76})
        self.assertEqual(row["lower_bound"], "843669938599/2048000000000")
        self.assertTrue(row["projected_dual_slacks_positive_definite_exactly"])
        self.assertTrue(row["cross_width_coupling_essential_in_this_fixed_cone"])

    def test_primitive_countercell_and_fixed_X_cascade_are_exact(self) -> None:
        row = self.value["primitive_and_directed_RED_gates"]
        counter = row["primitive_countercell"]
        self.assertEqual(
            (
                counter["positive_primitive_(5,7)"],
                counter["negative_primitive_(4,7)"],
                counter["aggregate_demand"],
                counter["old_PSD_owner_share"],
            ),
            (
                "1/3200",
                "-9/25600",
                "-1/25600",
                "-49528467/1690000000000",
            ),
        )
        self.assertEqual(counter["aggregate_slack"], "8243579/845000000000")
        self.assertEqual(
            counter["primitive_(5,7)_residual"],
            "-577653467/1690000000000",
        )
        self.assertTrue(counter["aggregate_covered_but_positive_primitive_not_covered"])
        cascade = row["fixed_old_X_left_edge_cascade"]
        self.assertEqual(len(cascade["tight_rows"]), 5)
        self.assertEqual(cascade["zero_sampled_capacity_source"], "(8,8,13)")
        self.assertTrue(
            cascade["all_positive_capacity_tau_for_j10_j11_j12_j14_j15_forced_zero"]
        )

    def test_scope_keeps_every_global_gate_false(self) -> None:
        scope = self.value["scope"]
        self.assertTrue(scope["exact_epoch_block_cross_width_PSD_witness"])
        self.assertTrue(scope["cross_width_essential_in_fixed_no_cross_width_cone"])
        for key in (
            "primitive_owned_cover_constructed",
            "directed_current_to_past_source_map_constructed",
            "joint_reoptimized_flow_SDP_no_go_proved",
            "continuum_phase_integrated",
            "m_3_m_2_m_1_terminal_closed",
            "global_birth_final_terminal_ledger_constructed",
            "arbitrary_history_or_uniform_epoch_template_proved",
            "C058_Q1_Q2_proved",
            "publication_novelty_or_prize_claimed",
        ):
            self.assertIs(scope[key], False)

    def test_rehashed_mutations_and_cached_object_poisoning_are_rejected(self) -> None:
        result = self.cert.self_check(self.value)
        self.assertEqual(result, {"mutations_attempted": 16, "mutations_rejected": 16})
        changed = copy.deepcopy(self.value)
        changed["scope"]["C058_Q1_Q2_proved"] = True
        changed["integrity"]["payload_sha256"] = self.cert.payload_hash(changed)
        with self.assertRaises(self.cert.CertificateError):
            self.cert.verify_certificate(changed)

        poisoned = self.cert.build_certificate()
        poisoned["scope"]["C058_Q1_Q2_proved"] = True
        self.assertIs(self.cert.build_certificate()["scope"]["C058_Q1_Q2_proved"], False)

    def test_canonical_cli_nonobject_and_boolean_hardening(self) -> None:
        script = Path(self.cert.__file__).resolve()
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "certificate.json"
            generated = subprocess.run(
                [sys.executable, str(script), "--output", str(output)],
                capture_output=True,
                check=False,
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            )
            self.assertEqual(generated.returncode, 0, generated.stderr.decode())
            raw = output.read_bytes()
            parsed = json.loads(raw.decode("utf-8"))
            self.assertEqual(raw, self.cert.rendered_bytes(parsed))
            replay = subprocess.run(
                [sys.executable, str(script), "--verify", str(output), "--self-check"],
                capture_output=True,
                check=False,
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            )
            self.assertEqual(replay.returncode, 0, replay.stderr.decode())
            self.assertIn(b"mutations_rejected=16", replay.stdout)

            nonobject = Path(directory) / "nonobject.json"
            nonobject.write_text("[]\n", encoding="utf-8")
            rejected = subprocess.run(
                [sys.executable, str(script), "--verify", str(nonobject)],
                capture_output=True,
                check=False,
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            )
            self.assertNotEqual(rejected.returncode, 0)
            self.assertIn(b"JSON root must be an object", rejected.stderr)
            self.assertNotIn(b"Traceback", rejected.stderr)

        for path, integer in (
            (("integrity", "canonical_json"), 1),
            (("scope", "fixed_two_epoch_one_phase_fixture_only"), 1),
            (("scope", "C058_Q1_Q2_proved"), 0),
        ):
            with self.subTest(path=path):
                changed = copy.deepcopy(self.value)
                changed[path[0]][path[1]] = integer
                changed["integrity"]["payload_sha256"] = self.cert.payload_hash(changed)
                with self.assertRaises(self.cert.CertificateError):
                    self.cert.verify_certificate(changed)

    def test_committed_json_is_canonical_exact_replay(self) -> None:
        raw = self.cert.DEFAULT_CERTIFICATE.read_bytes()
        parsed = json.loads(raw.decode("utf-8"))
        self.assertEqual(raw, self.cert.rendered_bytes(parsed))
        self.assertEqual(parsed, self.value)
        self.cert.verify_certificate(parsed)


if __name__ == "__main__":
    unittest.main()
