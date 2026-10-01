#!/usr/bin/env python3
"""Focused tests for the signed coordinate-owner graph/PSD master."""

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


MODULE = "ROUTE_C_SIGNED_COORDINATE_OWNER_MASTER_LP_certificate"


class SignedCoordinateOwnerMasterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cert = importlib.import_module(MODULE)
        cls.value = cls.cert.build_certificate()

    def test_exact_fixture_census_and_owner_partition(self) -> None:
        row = self.value["fixture"]
        self.assertEqual(
            (
                row["physical_coordinate_count"],
                row["finite_event_count"],
                row["positive_length_cell_count"],
                row["owner_count"],
                row["owner_cell_row_count"],
                row["physical_root_count"],
            ),
            (52, 77, 76, 8, 608, 1326),
        )
        self.assertTrue(row["coordinate_groups_partition_all_coordinates"])
        self.assertTrue(row["shared_a7_endpoint_owned_once_by_past_epoch"])
        self.assertEqual(row["pointwise_owner_root_identities_checked"], 100776)
        self.assertEqual(row["direct_M_Gothic_lambda_equals_2M_rows_checked"], 46)
        self.assertEqual(row["integrated_signed_demand"], "2069/10240")

    def test_exact_graph_root_primal_and_dual_bounds(self) -> None:
        row = self.value["graph_root_master"]
        self.assertEqual(row["feasible_primal"]["positive_root_count"], 20)
        self.assertEqual(row["feasible_primal"]["physical_price"], "99062067/179732480")
        self.assertEqual(row["feasible_primal"]["cross_epoch_positive_root_count"], 6)
        self.assertEqual(row["no_cross_epoch_dual"]["support_count"], 28)
        self.assertEqual(row["no_cross_epoch_dual"]["lower_bound"], "611554977/1024000000")
        self.assertEqual(
            row["cross_epoch_essentiality_gap"],
            "51737891019/1123328000000",
        )
        self.assertEqual(row["full_dual"]["support_count"], 30)
        self.assertEqual(row["full_dual"]["lower_bound"], "55874798199/102400000000")
        self.assertEqual(row["twice_integrated_demand"], "2069/5120")
        self.assertEqual(
            row["conditional_Phi_strict_negative_margin"],
            "14494798199/102400000000",
        )

    def test_exact_rational_psd_witness_reopens_larger_cone_only(self) -> None:
        row = self.value["psd_reopening_witness"]
        self.assertEqual(row["factor_shape"], [52, 13])
        self.assertEqual(row["factor_common_denominator"], 5200000)
        self.assertEqual(row["owner_rows_checked"], 608)
        self.assertTrue(row["all_owner_rows_feasible_exactly"])
        self.assertTrue(row["zero_row_sum_exact"])
        self.assertTrue(row["PSD_by_rational_Gram_factor"])
        self.assertEqual(row["physical_price"], "19511959/50000000")
        self.assertEqual(row["below_twice_demand_margin"], "5544953/400000000")
        self.assertTrue(row["cross_epoch_block_nonzero"])
        self.assertFalse(row["cross_epoch_essential_in_PSD_cone_proved"])

    def test_exact_psd_dual_closes_the_zero_row_sum_cone_for_this_ledger(self) -> None:
        row = self.value["zero_row_sum_PSD_dual"]
        self.assertEqual(row["support_count"], 227)
        self.assertEqual(row["lower_bound"], "64678786029/204800000000")
        self.assertEqual(row["projected_dimension"], 51)
        self.assertEqual(row["strictly_positive_LDL_pivot_count"], 51)
        self.assertTrue(row["projected_slack_positive_definite_exactly"])
        self.assertEqual(
            row["gap_above_twice_maximum_Goff"],
            "89607170277983/1807769600000000",
        )

    def test_pair_ledger_sign_is_exact_and_still_negative(self) -> None:
        row = self.value["pair_owner_Abel_ledger"]
        self.assertEqual(row["proportional"]["Goff_plus_terminal"], "2069/10240")
        self.assertEqual(
            row["proportional"]["Phi_at_PSD_witness_price"],
            "-2768860635551669/19535540800000000",
        )
        self.assertEqual(
            row["optimal_finite_pair_allocation"]["minimum_terminal"],
            "124605023/1807769600",
        )
        self.assertEqual(
            row["optimal_finite_pair_allocation"]["maximum_Goff"],
            "240656237/1807769600",
        )
        self.assertEqual(
            row["optimal_finite_pair_allocation"]["maximum_Phi_at_PSD_witness_price"],
            "-1751172283851/14123200000000",
        )

    def test_scope_keeps_the_missing_directed_source_map_explicit(self) -> None:
        scope = self.value["scope"]
        self.assertTrue(scope["fixed_fixture_graph_root_theorem"])
        self.assertTrue(scope["one_exact_rational_PSD_feasible_witness"])
        self.assertTrue(scope["zero_row_sum_PSD_coordinate_owner_cone_no_go"])
        self.assertTrue(scope["C067_finite_pair_allocation_convention_frozen"])
        for key in (
            "exact_graph_root_optimum_known",
            "exact_PSD_optimum_known",
            "directed_current_to_past_source_map_constructed",
            "cross_epoch_essential_in_PSD_cone_proved",
            "indefinite_or_other_owner_split_theorem",
            "other_pair_allocation_or_terminal_conventions",
            "birth_final_terminal_global_ledger_constructed",
            "C058_Q1_Q2_proved",
            "publication_novelty_or_prize_claimed",
        ):
            self.assertIs(scope[key], False)

    def test_rehashed_semantic_mutations_are_rejected(self) -> None:
        cert = self.cert
        value = self.value
        self.assertEqual(cert.self_check(value), {
            "mutations_attempted": 12,
            "mutations_rejected": 12,
        })
        changed = copy.deepcopy(value)
        changed["scope"]["C058_Q1_Q2_proved"] = True
        changed["integrity"]["payload_sha256"] = cert.payload_hash(changed)
        with self.assertRaises(cert.CertificateError):
            cert.verify_certificate(changed)

        poisoned = cert.build_certificate()
        poisoned["scope"]["C058_Q1_Q2_proved"] = True
        self.assertIs(cert.build_certificate()["scope"]["C058_Q1_Q2_proved"], False)

    def test_canonical_bytes_cli_and_nonobject_rejection(self) -> None:
        cert = self.cert
        script = Path(cert.__file__).resolve()
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
            self.assertEqual(raw, cert.rendered_bytes(parsed))
            replay = subprocess.run(
                [sys.executable, str(script), "--verify", str(output), "--self-check"],
                capture_output=True,
                check=False,
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            )
            self.assertEqual(replay.returncode, 0, replay.stderr.decode())
            self.assertIn(b"mutations_rejected=12", replay.stdout)

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

    def test_default_stdout_and_boolean_type_hardening(self) -> None:
        cert = self.cert
        generated = subprocess.run(
            [sys.executable, str(Path(cert.__file__).resolve())],
            capture_output=True,
            check=False,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )
        self.assertEqual(generated.returncode, 0, generated.stderr.decode())
        parsed = json.loads(generated.stdout.decode("utf-8"))
        self.assertEqual(generated.stdout, cert.rendered_bytes(parsed))

        for path, integer in (
            (("integrity", "canonical_json"), 1),
            (("scope", "fixed_fixture_graph_root_theorem"), 1),
            (("scope", "C058_Q1_Q2_proved"), 0),
        ):
            with self.subTest(path=path):
                changed = copy.deepcopy(self.value)
                changed[path[0]][path[1]] = integer
                changed["integrity"]["payload_sha256"] = cert.payload_hash(changed)
                with self.assertRaises(cert.CertificateError):
                    cert.verify_certificate(changed)

    def test_committed_json_is_exact_replay(self) -> None:
        cert = self.cert
        raw = cert.DEFAULT_CERTIFICATE.read_bytes()
        parsed = json.loads(raw.decode("utf-8"))
        self.assertEqual(raw, cert.rendered_bytes(parsed))
        self.assertEqual(parsed, self.value)
        cert.verify_certificate(parsed)


if __name__ == "__main__":
    unittest.main()
