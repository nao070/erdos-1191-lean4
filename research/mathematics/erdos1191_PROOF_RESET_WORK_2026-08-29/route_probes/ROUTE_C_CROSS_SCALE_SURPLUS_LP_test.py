#!/usr/bin/env python3
"""Focused tests for the exact 14-channel cross-scale surplus LP."""

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


class CrossScaleSurplusLPTests(unittest.TestCase):
    def test_exact_duality_proves_sharing_saving_but_not_demand_equality(self) -> None:
        """Catches a wrong normalization, missing cross roots, or merely numeric optimum."""
        try:
            cert = importlib.import_module("ROUTE_C_CROSS_SCALE_SURPLUS_LP_certificate")
        except ModuleNotFoundError:
            self.fail("cross-scale surplus certificate implementation is missing")

        result = cert.build_certificate()["cross_scale_lp"]
        self.assertEqual(result["channel_count"], 14)
        self.assertEqual(result["root_count"], 91)
        self.assertEqual(result["positive_length_cell_count"], 40)
        self.assertEqual(result["integrated_signed_demand"], "173/1024")
        self.assertEqual(result["optimal_physical_price"], "1555757/6144000")
        self.assertEqual(result["surplus_over_demand"], "517757/6144000")
        self.assertEqual(result["sum_of_separate_optima"], "134081/512000")
        self.assertEqual(result["strict_sharing_saving"], "10643/1228800")
        self.assertEqual(result["primal_dual_gap"], "0/1")
        self.assertEqual(result["positive_cross_scale_root_count"], 0)
        self.assertEqual(result["minimum_cross_scale_root_dual_margin"], "799/4000")

    def test_certificate_exposes_exact_normalized_primal_and_dual_witnesses(self) -> None:
        """Catches a summary-only payload that cannot replay the exact LP witnesses."""
        cert = importlib.import_module("ROUTE_C_CROSS_SCALE_SURPLUS_LP_certificate")
        result = cert.build_certificate()["cross_scale_lp"]
        self.assertIn("channels", result)
        self.assertIn("primal", result)
        self.assertIn("dual", result)
        self.assertIn("root_audit", result)

        self.assertEqual(result["channels"][0], {
            "index": 0,
            "label": "T200:n4:b0",
            "width": 200,
            "origin": 309,
            "sqrt_2_width": 20,
        })
        self.assertEqual(result["channels"][5], {
            "index": 5,
            "label": "S800:n8:b0",
            "width": 800,
            "origin": 749,
            "sqrt_2_width": 40,
        })
        self.assertEqual(result["primal"]["positive_root_count"], 8)
        self.assertEqual(result["primal"]["root_weights"]["0,2"], "3971/153600")
        self.assertEqual(result["dual"]["positive_cell_count"], 8)
        self.assertEqual(result["dual"]["cell_weights"]["[2396,2464)"], "12743/90")
        self.assertEqual(result["root_audit"]["2,6"], {
            "kind": "cross_scale",
            "physical_cost": "861/400",
            "dual_load": "7811/4000",
            "dual_margin": "799/4000",
        })

    def test_highlighted_cell_proves_sharing_without_a_cross_root(self) -> None:
        """Catches attributing the strict saving to a positive cross-scale edge."""
        cert = importlib.import_module("ROUTE_C_CROSS_SCALE_SURPLUS_LP_certificate")
        result = cert.build_certificate()["cross_scale_lp"]
        self.assertIn("cell_audit", result)
        self.assertEqual(result["event_count"], 41)
        self.assertEqual(result["complete_real_line_cell_count"], 42)
        self.assertEqual(result["channels"][4]["origin"], 749)
        self.assertEqual(result["channels"][5]["origin"], 749)
        self.assertEqual(result["cell_audit"]["[749,816)"], {
            "length": 67,
            "n4_T200_demand": "1/3200",
            "n8_S800_demand": "0/1",
            "n4_T200_root_correction": "271/1024000",
            "n8_S800_root_correction": "49/1024000",
            "cross_scale_root_correction": "0/1",
            "total_slack": "0/1",
        })

    def test_aggregate_channels_are_explicitly_priced_and_strictly_inactive(self) -> None:
        """Catches a free or coefficient-trace-priced aggregate J channel."""
        cert = importlib.import_module("ROUTE_C_CROSS_SCALE_SURPLUS_LP_certificate")
        result = cert.build_certificate()["cross_scale_lp"]
        self.assertTrue(result["aggregate_J_channels_included"])
        self.assertEqual(result["aggregate_J_audit"], {
            "J4": {
                "support": [0, 1, 2, 3, 4],
                "coefficient": "0/1",
                "physical_cost": "3/1",
                "dual_load": "107/150",
                "dual_margin": "343/150",
            },
            "J8": {
                "support": [5, 6, 7, 8, 9, 10, 11, 12, 13],
                "coefficient": "0/1",
                "physical_cost": "688/25",
                "dual_load": "8441/1000",
                "dual_margin": "19079/1000",
            },
            "J_all": {
                "support": list(range(14)),
                "coefficient": "0/1",
                "physical_cost": "702/25",
                "dual_load": "25277/3000",
                "dual_margin": "58963/3000",
            },
        })

    def test_scope_and_rehashed_semantic_mutations_are_enforced(self) -> None:
        """Catches promotion of a fixed sum-cover fixture into a C058 claim."""
        cert = importlib.import_module("ROUTE_C_CROSS_SCALE_SURPLUS_LP_certificate")
        certificate = cert.build_certificate()
        self.assertIn("integrity", certificate)
        self.assertEqual(certificate["integrity"]["payload_sha256"], cert.payload_hash(certificate))
        self.assertEqual(certificate["scope"]["common_cell_sum_cover_is_weaker_than_epochwise_cover"], True)
        self.assertEqual(certificate["scope"]["C058_Q1_Q2_proved"], False)
        self.assertEqual(cert.self_check(certificate), {
            "mutations_attempted": 12,
            "mutations_rejected": 12,
        })

        changed = copy.deepcopy(certificate)
        changed["scope"]["C058_Q1_Q2_proved"] = True
        changed["integrity"]["payload_sha256"] = cert.payload_hash(changed)
        with self.assertRaises(cert.CertificateError):
            cert.verify_certificate(changed)

    def test_cli_generates_and_replays_literal_canonical_bytes(self) -> None:
        """Catches a verifier that never checks the bytes it was given."""
        cert = importlib.import_module("ROUTE_C_CROSS_SCALE_SURPLUS_LP_certificate")
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


if __name__ == "__main__":
    unittest.main()
