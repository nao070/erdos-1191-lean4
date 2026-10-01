#!/usr/bin/env python3
"""Regression tests for the C128 common-phase pointwise no-go audit."""

from __future__ import annotations

from fractions import Fraction as F
import hashlib
import importlib
import json
from pathlib import Path
import tempfile
import unittest


MODULE = "ROUTE_C_C128_COMMON_PHASE_POINTWISE_NO_GO_certificate"


class C128CommonPhasePointwiseNoGoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cert = importlib.import_module(MODULE)
        cls.value = json.loads(cls.cert.DEFAULT_CERTIFICATE.read_text())
        cls.summary = cls.cert.verify_certificate(cls.value)

    def test_exact_local_dual_separation_set_is_frozen(self) -> None:
        self.assertEqual(self.summary["C120"]["separating_indices"], ())
        self.assertEqual(
            self.summary["C123"]["separating_indices"],
            tuple(range(22)),
        )
        self.assertEqual(
            self.summary["C123"]["first_separating_interval"],
            (F(82), F(493, 6)),
        )
        self.assertEqual(
            self.summary["C123"]["last_separating_interval"],
            (F(359, 4), F(90)),
        )

    def test_strongest_chamber_zero_has_exact_clean_bounds(self) -> None:
        chamber = self.summary["C123"]["strongest_chamber"]
        self.assertEqual(chamber["index"], 0)
        self.assertEqual(chamber["interval"], (F(82), F(493, 6)))
        self.assertGreater(chamber["target_lower"], F(9, 250))
        self.assertLess(chamber["combined_local_upper"], F(39, 2000))
        self.assertGreater(chamber["deficit_lower"], F(33, 2000))
        self.assertLess(chamber["epoch4_weighted_local_upper"], -F(13, 1000))
        self.assertLess(chamber["epoch8_weighted_local_upper"], F(33, 1000))

    def test_scope_preserves_every_unresolved_gate(self) -> None:
        scope = self.value["scope"]
        self.assertTrue(scope["fixed_C123_uniform_all_chambers_candidate_lower_refuted"])
        self.assertTrue(scope["fixed_C123_all_phase_pointwise_candidate_lower_refuted"])
        self.assertTrue(scope["phase_redistribution_is_load_bearing_for_this_candidate"])
        self.assertFalse(scope["integrated_primal_certificate_constructed"])
        self.assertFalse(scope["local_master_inequality_proved"])
        self.assertFalse(scope["global_phase_rule_admissible_proved"])
        self.assertFalse(scope["arbitrary_rank_proved"])
        self.assertFalse(scope["C058_resolved"])
        self.assertFalse(scope["Q1_Q2_resolved"])

    def test_canonical_payload_and_mutation_barrier(self) -> None:
        self.assertEqual(self.value, self.cert.expected_certificate())
        self.assertEqual(self.cert.self_check(self.value)["mutations_rejected"], 14)


class C128IntervalAndSourceHardeningTests(unittest.TestCase):
    def test_nonpositive_raw_piece_is_rejected_before_log_division(self) -> None:
        cert = importlib.import_module(MODULE)
        with self.assertRaisesRegex(cert.CertificateError, "raw piece is not strictly positive"):
            cert._positive_piece_average_interval(F(0), F(1), F(1), F(2))
        with self.assertRaisesRegex(cert.CertificateError, "raw piece is not strictly positive"):
            cert._positive_piece_average_interval(-F(1), F(1), F(1), F(2))

    def test_pinned_source_rejects_noncanonical_rendering(self) -> None:
        cert = importlib.import_module(MODULE)
        without_hash = {
            "schema": "erdos1191.c058_eta_negative_full_phase_dual.discovery.v1",
            "fixture": "controlled",
        }
        internal = cert._object_hash(without_hash)
        value = dict(without_hash)
        value["payload_sha256_without_hash"] = internal
        canonical = (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")
        noncanonical = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "source.json"
            path.write_bytes(canonical)
            loaded = cert._read_pinned_source(
                path,
                hashlib.sha256(canonical).hexdigest(),
                internal,
                "controlled",
            )
            self.assertEqual(loaded, value)
            path.write_bytes(noncanonical)
            with self.assertRaisesRegex(cert.CertificateError, "noncanonical rendering"):
                cert._read_pinned_source(
                    path,
                    hashlib.sha256(noncanonical).hexdigest(),
                    internal,
                    "controlled",
                )


if __name__ == "__main__":
    unittest.main()
