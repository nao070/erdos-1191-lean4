"""Behavioral checks for the deterministic finite multiscale certificate."""
from __future__ import annotations

import hashlib
import json

from multiscale_variance_certificate_2026_08_28 import (
    build_certificate,
    serialize_certificate,
)


def test_certificate_covers_every_requested_exact_finite_check() -> None:
    certificate = build_certificate()

    assert certificate["evidence_scope"] == (
        "Certified exact finite evidence only; no asymptotic theorem and no "
        "resolution of Erdos Problem #1191 is claimed."
    )
    assert certificate["summary"]["all_checks_passed"] is True
    assert certificate["summary"]["exact_check_count"] == 100_137

    checks = certificate["checks"]
    assert checks["cyclic_arc_overlap"]["check_count"] == 49_192
    assert checks["resistance_polarization"]["check_count"] == 49_192
    assert checks["ordered_pair_pair_expansion"]["check_count"] == 1_152

    zero = checks["sidon_three_cycle_zero_mode"]
    assert zero["points"] == [0, 3, 7, 12]
    assert zero["modulus"] == 6
    assert zero["positive_differences"] == [3, 4, 5, 7, 9, 12]
    assert zero["short_edge_distances"] == [3, 4, 5]
    assert zero["crossing_loads"] == [2, 2, 2, 2, 2, 2]
    assert zero["variance"] == "0"

    sign_flip = checks["covariance_sign_flip"]
    assert sign_flip["modulus_8_covariance"] == "-1/4"
    assert sign_flip["modulus_16_covariance"] == "7/8"

    dominant = checks["dominant_gap_family"]
    assert dominant["G_range_inclusive"] == [3, 200]
    assert dominant["instance_count"] == 198
    assert dominant["first_instance"]["variance"] == "12/7"
    assert dominant["last_instance"]["variance"] == "3827/41616"


def test_certificate_serialization_is_sorted_deterministic_and_self_hashed() -> None:
    first = build_certificate()
    second = build_certificate()
    first_bytes = serialize_certificate(first)
    second_bytes = serialize_certificate(second)

    assert first_bytes == second_bytes
    assert first_bytes.endswith(b"\n")
    decoded = json.loads(first_bytes)
    assert decoded == first

    payload_without_hash = dict(first)
    claimed = payload_without_hash.pop("canonical_payload_sha256")
    canonical = json.dumps(
        payload_without_hash,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    assert claimed == hashlib.sha256(canonical).hexdigest()

