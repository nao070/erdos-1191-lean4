#!/usr/bin/env python3
"""Regression tests for the C131 complete fixed-C120 phase primal."""

from __future__ import annotations

import importlib
import importlib.util
from fractions import Fraction as F
import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest import mock


MODULE = "ROUTE_C_C131_COMPLETE_C120_PHASE_PRIMAL_certificate"


class C131ModuleContractTests(unittest.TestCase):
    def test_certificate_module_exists(self) -> None:
        """Catches omission of the executable exact-replay verifier."""
        self.assertIsNotNone(importlib.util.find_spec(MODULE))

    def test_certificate_module_exposes_exact_replay_api(self) -> None:
        """Catches a non-executable placeholder in place of the verifier."""
        cert = importlib.import_module(MODULE)
        for name in (
            "DEFAULT_CERTIFICATE",
            "verify_certificate",
            "self_check",
            "payload_hash",
            "_object_hash",
            "_load",
        ):
            with self.subTest(name=name):
                self.assertTrue(hasattr(cert, name), name)

    def test_canonical_certificate_payload_exists(self) -> None:
        """Catches omission of the immutable accepted tail factor payload."""
        cert = importlib.import_module(MODULE)
        self.assertTrue(cert.DEFAULT_CERTIFICATE.is_file())

    def test_complete_bank_replays_exact_clean_integrated_margin(self) -> None:
        """Catches an incomplete bank or a nonpositive integrated C120 margin."""
        cert = importlib.import_module(MODULE)
        value = json.loads(cert.DEFAULT_CERTIFICATE.read_text())
        summary = cert.verify_certificate(value)
        self.assertIn("complete_C120", summary)
        complete = summary["complete_C120"]
        self.assertEqual((complete["chambers"], complete["factors"]), (147, 294))
        self.assertGreater(complete["raw_margin_lower"], F(21, 1000))
        self.assertGreater(complete["normalized_margin_lower"], F(3, 100))
        self.assertLess(complete["normalized_margin_upper"], F(31, 1000))
        self.assertLess(
            complete["raw_margin_upper"] - complete["raw_margin_lower"],
            F(1, 10**26),
        )

    def test_exact_geometry_rank_owner_and_objective_census_is_frozen(self) -> None:
        """Catches dropped owner contexts, cross-epoch cancellation, or lost rank."""
        cert = importlib.import_module(MODULE)
        value = json.loads(cert.DEFAULT_CERTIFICATE.read_text())
        summary = cert.verify_certificate(value)
        self.assertIn("complete_C120", summary)
        complete = summary["complete_C120"]
        self.assertEqual((complete["rank_min"], complete["rank_max"]), (4, 31))
        self.assertEqual(complete["rank_sum"], 3205)
        self.assertEqual(complete["generic_owner_rows"], 53312)
        self.assertEqual(complete["generic_owner_endpoint_checks"], 106624)
        self.assertEqual(complete["structural_zero_generic_rows"], 37240)
        self.assertEqual(complete["collapsed_endpoint_owner_rows"], 104080)
        self.assertEqual(complete["structural_zero_collapsed_endpoint_rows"], 73440)
        self.assertEqual(complete["interior_owner_rows"], 53312)
        self.assertEqual(complete["structural_zero_interior_rows"], 37240)
        self.assertEqual(complete["owner_recovery_unique_state_evaluations"], 11319)
        self.assertEqual(complete["per_epoch_owner_recovery_checks"], 22638)
        self.assertEqual(complete["owner_recovery_context_references"], 44828)
        self.assertEqual(complete["per_epoch_owner_recovery_context_references"], 89656)
        self.assertEqual(complete["endpoint_epoch_objective_checks"], 588)
        self.assertEqual(complete["endpoint_weighted_objective_checks"], 294)
        self.assertEqual(complete["interior_epoch_objective_checks"], 294)
        self.assertEqual(complete["interior_weighted_objective_checks"], 147)
        self.assertEqual(
            complete["minimum_owner_margin"], F(305733, 87500000000000)
        )
        self.assertEqual(complete["positive_piece_indices"], tuple(range(147)))
        self.assertEqual(complete["negative_piece_indices"], ())

    def test_normal_payload_factor_and_endpoint_barriers(self) -> None:
        """Catches acceptance of any required canonical mutation class."""
        cert = importlib.import_module(MODULE)
        value = json.loads(cert.DEFAULT_CERTIFICATE.read_text())
        result = cert.self_check(value)
        self.assertEqual(
            result.get("cases"),
            ("normal", "payload", "factor", "endpoint", "scope"),
        )
        self.assertEqual(result.get("normal_verified"), 1)
        self.assertEqual(result.get("mutations_attempted"), 4)
        self.assertEqual(result.get("mutations_rejected"), 4)

    def test_cached_replay_still_rechecks_pinned_provenance(self) -> None:
        """Catches a cache hit that bypasses missing or changed dependencies."""
        cert = importlib.import_module(MODULE)
        value = json.loads(cert.DEFAULT_CERTIFICATE.read_text())
        cert.verify_certificate(value)
        missing = Path(cert.HERE) / "__missing_c126_dependency_for_cache_test__.py"
        self.assertFalse(missing.exists())
        with mock.patch.object(cert, "C126_VERIFIER", missing):
            with self.assertRaises((cert.CertificateError, FileNotFoundError)):
                cert.verify_certificate(value)

    def test_command_line_verifier_reports_exact_success(self) -> None:
        """Catches a verifier artifact that cannot be executed independently."""
        cert = importlib.import_module(MODULE)
        completed = subprocess.run(
            [sys.executable, str(cert.__file__), "--verify", str(cert.DEFAULT_CERTIFICATE)],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("VERIFY_OK row=C120", completed.stdout)
        self.assertIn("chambers=147", completed.stdout)
        self.assertIn("C058_open", completed.stdout)


if __name__ == "__main__":
    unittest.main()
