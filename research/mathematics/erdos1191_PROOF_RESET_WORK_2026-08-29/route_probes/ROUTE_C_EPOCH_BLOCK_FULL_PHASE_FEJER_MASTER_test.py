#!/usr/bin/env python3
"""Focused exact tests for the full-phase epoch-block Fejer master."""

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


MODULE = "ROUTE_C_EPOCH_BLOCK_FULL_PHASE_FEJER_MASTER_certificate"


class EpochBlockFullPhaseFejerMasterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cert = importlib.import_module(MODULE)
        cls.value = cls.cert.build_certificate()

    def test_exact_phase_fixture_has_108_gap_free_chambers(self) -> None:
        phase = self.value["full_phase_chamber_cover"]
        self.assertEqual(
            (
                phase["event_line_count"],
                phase["phase_endpoint_count"],
                phase["event_chamber_count"],
                phase["covered_chamber_count"],
                phase["uncovered_chamber_count"],
            ),
            (78, 109, 108, 108, 0),
        )
        self.assertEqual(phase["phase_endpoints"][0], "100/1")
        self.assertEqual(phase["phase_endpoints"][-1], "200/1")
        self.assertEqual(len(set(phase["phase_endpoints"])), 109)

        breakpoints = self.cert.phase_breakpoints()
        midpoint = (breakpoints[0] + breakpoints[1]) / 2
        self.assertEqual(len(self.cert._exact_cells(midpoint)), 77)

    def test_every_factor_is_an_exact_epoch_local_zero_sum_Gram_factor(self) -> None:
        phase = self.value["full_phase_chamber_cover"]
        manifest = phase["factor_manifest"]
        self.assertEqual(len(manifest["chambers"]), 108)
        self.assertEqual(
            phase["factor_manifest_raw_sha256"],
            "45060f68702057a81718ca452502c9f3cdd322edc07c9884583d802f5e18e49c",
        )
        past = set(self.cert._epoch_indices(4))
        current = set(self.cert._epoch_indices(8))
        total_columns = 0
        for chamber, factor in enumerate(manifest["chambers"]):
            with self.subTest(chamber=chamber):
                self.assertEqual(factor["chamber"], chamber)
                self.assertGreater(factor["denominator"], 0)
                self.assertEqual(
                    len(factor["columns"]), factor["rank4"] + factor["rank8"]
                )
                total_columns += len(factor["columns"])
                counts = {4: 0, 8: 0}
                for column in factor["columns"]:
                    self.assertEqual(len(column), 52)
                    self.assertEqual(sum(column), 0)
                    support = {index for index, entry in enumerate(column) if entry}
                    self.assertTrue(support)
                    if support <= past:
                        counts[4] += 1
                    elif support <= current:
                        counts[8] += 1
                    else:
                        self.fail("a Gram column crosses epoch blocks")
                self.assertEqual(counts, {4: factor["rank4"], 8: factor["rank8"]})
        self.assertEqual(total_columns, 2315)
        properties = phase["factor_properties"]
        self.assertEqual(properties["total_rational_Gram_columns"], 2315)
        self.assertEqual(properties["maximum_absolute_integer_entry"], 19791)
        self.assertTrue(properties["PSD_by_exact_rational_Gram_factor"])
        self.assertTrue(properties["every_factor_column_zero_sum"])
        self.assertTrue(properties["every_cross_epoch_Gram_block_zero"])

    def test_all_owner_rows_and_collapsed_endpoints_are_exact(self) -> None:
        rows = self.value["full_phase_chamber_cover"]["chamber_audits"]
        self.assertEqual(len(rows), 108)
        self.assertEqual(
            sum(row["generic_owner_endpoint_checks"] for row in rows),
            133056,
        )
        self.assertEqual(
            sum(
                row["collapsed_endpoint_owner_checks_with_ratio_replay"]
                for row in rows
            ),
            258560,
        )
        phase = self.value["full_phase_chamber_cover"]
        self.assertEqual(phase["total_open_chamber_owner_rows"], 66528)
        self.assertEqual(
            phase[
                "total_collapsed_endpoint_owner_rows_with_shared_endpoints_repeated"
            ],
            129280,
        )
        self.assertTrue(all(row["all_owner_rows_hold_on_closed_chamber"] for row in rows))

    def test_both_ratio_endpoints_and_every_intermediate_ratio_are_positive(self) -> None:
        phase = self.value["full_phase_chamber_cover"]
        self.assertEqual(phase["endpoint_ratio_range"], ["9/16", "1/1"])
        self.assertTrue(phase["r_9_over_16_audited_every_chamber"])
        self.assertTrue(phase["r_1_audited_every_chamber"])
        self.assertTrue(phase["every_r_in_closed_range_follows_by_affinity"])
        self.assertTrue(phase["every_endpoint_and_quadratic_vertex_positive"])
        for row in phase["chamber_audits"]:
            for ratio in ("9/16", "1/1"):
                audit = row["weighted_endpoint_ratio_audits"][ratio]
                self.assertGreater(self.cert.F(audit["minimum"]), 0)
                self.assertIn(
                    audit["minimizer_type"],
                    ("left_endpoint", "right_endpoint", "interior_vertex"),
                )
            self.assertTrue(
                row["all_ratios_9_over_16_through_1_positive_by_affinity"]
            )

    def test_global_exact_mu_and_normalized_log_phase_bound(self) -> None:
        phase = self.value["full_phase_chamber_cover"]
        self.assertEqual(
            phase["global_mu_min_t_times_Phi"],
            "255996752651/2560000000000",
        )
        self.assertEqual(
            phase["global_mu_at_r_9_over_16"],
            "255996752651/2560000000000",
        )
        self.assertEqual(phase["global_mu_at_r_1"], "54555211621/500000000000")
        self.assertEqual(
            phase["normalized_log_phase_lower_bound_mu_over_200"],
            "255996752651/512000000000000",
        )
        minimizer = phase["chamber_audits"][1]["weighted_endpoint_ratio_audits"]
        self.assertEqual(minimizer["9/16"]["minimizer_t"], "605/6")
        self.assertEqual(minimizer["9/16"]["minimizer_type"], "right_endpoint")

    def test_phase_scaled_whole_stencil_and_boundaries_are_exact(self) -> None:
        row = self.value["phase_scaled_whole_stencil_ledger"]
        self.assertEqual(row["primitive_count"], 24)
        self.assertEqual(row["four_corner_occurrence_count"], 96)
        self.assertEqual(row["distinct_nonzero_Gothic_row_count"], 42)
        self.assertEqual(row["mixed_sign_reused_row_count"], 28)
        self.assertEqual(row["lambda_equals_2M_rows_in_prerequisite"], 46)
        self.assertEqual(row["phase_sample_count_endpoints_plus_chamber_midpoints"], 217)
        self.assertEqual(row["primitive_Abel_identities_checked"], 5208)
        self.assertEqual(row["primitive_sum_equals_integrated_direct_demand_checks"], 217)
        self.assertTrue(row["upper_16t_terminal_zero_for_every_checked_primitive"])
        self.assertTrue(row["lower_t_boundary_retained_not_dropped"])
        self.assertGreater(row["samples_with_nonzero_lower_boundary"], 0)
        self.assertIs(row["primitive_owned_cover_claimed"], False)

    def test_scope_keeps_all_global_and_terminal_gates_false(self) -> None:
        scope = self.value["scope"]
        for key in (
            "primitive_owned_cover_constructed",
            "directed_epoch_flow_constructed",
            "m_3_m_2_m_1_terminal_closed",
            "global_birth_final_terminal_ledger_constructed",
            "arbitrary_horizon_or_history_proved",
            "C058_Q1_Q2_proved",
            "publication_novelty_or_prize_claimed",
        ):
            self.assertIs(scope[key], False)

    def test_mutations_boolean_hardening_and_cache_isolation(self) -> None:
        result = self.cert.self_check(self.value)
        self.assertEqual(result, {"mutations_attempted": 16, "mutations_rejected": 16})

        poisoned = self.cert.build_certificate()
        poisoned["scope"]["C058_Q1_Q2_proved"] = True
        self.assertIs(self.cert.build_certificate()["scope"]["C058_Q1_Q2_proved"], False)

        for path, replacement in (
            (("integrity", "canonical_json"), 1),
            (("scope", "C058_Q1_Q2_proved"), 0),
            (("fixture", "physical_coordinate_count"), True),
        ):
            with self.subTest(path=path):
                changed = copy.deepcopy(self.value)
                changed[path[0]][path[1]] = replacement
                changed["integrity"]["payload_sha256"] = self.cert.payload_hash(changed)
                with self.assertRaises(self.cert.CertificateError):
                    self.cert.verify_certificate(changed)

    def test_cli_canonical_bytes_nonobject_and_self_check(self) -> None:
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

    def test_committed_json_is_canonical_exact_replay(self) -> None:
        raw = self.cert.DEFAULT_CERTIFICATE.read_bytes()
        parsed = json.loads(raw.decode("utf-8"))
        self.assertEqual(raw, self.cert.rendered_bytes(parsed))
        self.assertEqual(parsed, self.value)
        self.cert.verify_certificate(parsed)


if __name__ == "__main__":
    unittest.main()
