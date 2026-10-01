#!/usr/bin/env python3
"""Exact certificate for the ordered-dipole marginal transport price.

The general strip decomposition and LP theorem are proved in the companion
memo.  This certificate locks the local overlap identities, the five exact
LP stages for the eight-mark fixture, and the rational separation between
the integrated marginal price and the positive same-epoch Gothic budget.

It does not rule out use of the exact intersection coupling, signed or
cross-epoch cancellation, a larger master, or Erdős Problem #1191.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
from typing import Mapping, Sequence


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "gram_marginal_transport_certificate.json"
SCHEMA = "erdos1191.gram_marginal_transport.v1"
STATUS = "EXACT_ORDERED_STRIP_AND_MARGINAL_PRICE_ONLY_EXACT_GRAM_MASTER_OPEN"
GOL0MB = (0, 101, 204, 309, 416, 525, 636, 749)
N = 4


class CertificateError(RuntimeError):
    """Raised when an exact replay or scope check fails."""


def ftext(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def interval_length(left: tuple[int, int], right: tuple[int, int]) -> int:
    return max(0, min(left[1], right[1]) - max(left[0], right[0]))


def strips(left_mark: int, right_mark: int, width: int) -> tuple[tuple[int, int], tuple[int, int]]:
    if right_mark <= left_mark or width <= 0:
        raise ValueError("positive gap and width required")
    gap = right_mark - left_mark
    retained = min(gap, width)
    left_strip = (left_mark, left_mark + retained)
    right_strip = (right_mark + width - retained, right_mark + width)
    return left_strip, right_strip


def tent_numerator(middle: int, left_gap: int, right_gap: int, width: int) -> int:
    positive = lambda value: max(value, 0)
    return (
        positive(width - middle)
        + positive(width - middle - left_gap - right_gap)
        - positive(width - middle - left_gap)
        - positive(width - middle - right_gap)
    )


def local_strip_audit() -> dict[str, object]:
    checked = 0
    positive = 0
    for middle in range(1, 7):
        for left_gap in range(1, 7):
            for right_gap in range(1, 7):
                marks = (-left_gap, 0, middle, middle + right_gap)
                for width in range(1, middle + left_gap + right_gap + 3):
                    left_i, right_i = strips(marks[0], marks[1], width)
                    left_j, right_j = strips(marks[2], marks[3], width)
                    if interval_length(left_i, left_j) or interval_length(right_i, right_j):
                        raise CertificateError("same-sign strip families overlap")
                    if interval_length(left_i, right_j):
                        raise CertificateError("reverse ordered strip overlap is nonzero")
                    overlap = interval_length(right_i, left_j)
                    if overlap != tent_numerator(middle, left_gap, right_gap, width):
                        raise CertificateError("strip overlap/tent identity failed")
                    checked += 1
                    positive += overlap > 0
    return {
        "parameter_box": "1<=M,u,v<=6; 1<=T<=M+u+v+2",
        "rows_checked": checked,
        "positive_overlap_rows": positive,
        "same_sign_and_reverse_order_disjoint": True,
        "overlap_equals_tent_numerator": True,
    }


def positive_differences(points: Sequence[int]) -> tuple[int, ...]:
    values = tuple(
        points[right] - points[left]
        for left in range(len(points))
        for right in range(left + 1, len(points))
    )
    if len(values) != len(set(values)):
        raise CertificateError("fixture is not a Golomb ruler")
    return tuple(sorted(values))


def current_gaps(points: Sequence[int]) -> dict[int, int]:
    return {index: points[index] - points[index - 1] for index in range(N, 2 * N)}


def wave_edges(points: Sequence[int]) -> tuple[dict[str, object], ...]:
    rows = []
    for right in range(N + 2, 2 * N):
        for left in range(N, right - 1):
            middle = points[right - 1] - points[left]
            terminal = points[right] - points[left - 1]
            alpha = F((right - left) ** 2, 4 * N * N)
            rows.append(
                {
                    "left": left,
                    "right": right,
                    "middle": middle,
                    "terminal": terminal,
                    "alpha": ftext(alpha),
                }
            )
    expected = (
        {"left": 4, "right": 6, "middle": 109, "terminal": 327, "alpha": "1/16"},
        {"left": 4, "right": 7, "middle": 220, "terminal": 440, "alpha": "9/64"},
        {"left": 5, "right": 7, "middle": 111, "terminal": 333, "alpha": "1/16"},
    )
    if tuple(rows) != expected:
        raise CertificateError("fixture Wave edge table changed")
    return tuple(rows)


def stage(
    lower: int,
    upper: int,
    active_edges: tuple[tuple[int, int, F], ...],
    p: Mapping[int, F],
    q: Mapping[int, F],
    y_scaled: Mapping[tuple[int, int], F],
) -> dict[str, object]:
    gaps = current_gaps(GOL0MB)
    if any(value and gaps[index] > lower for index, value in (*p.items(), *q.items())):
        raise CertificateError("a positive cover potential has a nonsaturated strip mass")
    for left, right, alpha in active_edges:
        if p.get(left, F(0)) + q.get(right, F(0)) < alpha:
            raise CertificateError("vertex-cover primal constraint failed")
    for left in {edge[0] for edge in active_edges}:
        if sum((y_scaled.get((i, j), F(0)) for i, j, _ in active_edges if i == left), F(0)) > gaps[left]:
            raise CertificateError("transport row capacity failed")
    for right in {edge[1] for edge in active_edges}:
        # Every positive dual load below is constant and lies below min(h,T)
        # throughout the stated open interval.
        load = sum((y_scaled.get((i, j), F(0)) for i, j, _ in active_edges if j == right), F(0))
        if load > min(gaps[right], lower):
            raise CertificateError("transport column capacity failed")
    primal_scaled = sum((F(gaps[i]) * value for i, value in p.items()), F(0)) + sum(
        (F(gaps[j]) * value for j, value in q.items()), F(0)
    )
    dual_scaled = sum(
        (alpha * y_scaled.get((left, right), F(0)) for left, right, alpha in active_edges),
        F(0),
    )
    if primal_scaled != dual_scaled:
        raise CertificateError("stage primal/dual values disagree")
    return {
        "open_interval": [lower, upper],
        "active_edges": [[left, right, ftext(alpha)] for left, right, alpha in active_edges],
        "vertex_cover_p": {str(key): ftext(value) for key, value in sorted(p.items())},
        "vertex_cover_q": {str(key): ftext(value) for key, value in sorted(q.items())},
        "transport_y_scaled_by_T_squared": {
            f"{left},{right}": ftext(value) for (left, right), value in sorted(y_scaled.items())
        },
        "price_coefficient_over_T_squared": ftext(primal_scaled),
        "strong_duality_verified": True,
    }


def marginal_price_fixture() -> dict[str, object]:
    e46 = (4, 6, F(1, 16))
    e47 = (4, 7, F(9, 64))
    e57 = (5, 7, F(1, 16))
    stages = (
        stage(109, 111, (e46,), {4: F(1, 16)}, {6: F(0)}, {(4, 6): F(107)}),
        stage(
            111,
            220,
            (e46, e57),
            {4: F(1, 16), 5: F(1, 16)},
            {6: F(0), 7: F(0)},
            {(4, 6): F(107), (5, 7): F(109)},
        ),
        stage(
            220,
            327,
            (e46, e47, e57),
            {4: F(5, 64), 5: F(0)},
            {6: F(0), 7: F(1, 16)},
            {(4, 6): F(0), (4, 7): F(107), (5, 7): F(6)},
        ),
        stage(
            327,
            333,
            (e47, e57),
            {4: F(5, 64), 5: F(0)},
            {7: F(1, 16)},
            {(4, 7): F(107), (5, 7): F(6)},
        ),
        stage(
            333,
            440,
            (e47,),
            {4: F(9, 64)},
            {7: F(0)},
            {(4, 7): F(107)},
        ),
    )
    integrated = sum(
        (
            F(row["price_coefficient_over_T_squared"])
            * (F(1, row["open_interval"][0]) - F(1, row["open_interval"][1]))
            for row in stages
        ),
        F(0),
    )
    expected = F(32755417, 340707840)
    if integrated != expected:
        raise CertificateError("integrated marginal price changed")
    return {
        "stages": list(stages),
        "integrated_marginal_price": ftext(integrated),
        "zero_outside_open_interval": [109, 440],
    }


def log_bounds(ratio: F) -> tuple[F, F]:
    if ratio <= 1:
        raise ValueError("ratio must exceed one")
    z = (ratio - 1) / (ratio + 1)
    lower = 2 * z
    upper = 2 * (z + z**3 / (3 * (1 - z * z)))
    return lower, upper


def gothic_separation_fixture(integrated_price: F) -> dict[str, object]:
    gothic_rows = (
        (F(1, 16), F(440, 109), F(109, 440) - 1),
        (F(1, 64), F(2), F(1, 2) - 1),
        (F(1, 16), F(440, 111), F(111, 440) - 1),
    )
    gothic_upper = sum(
        (weight * (log_bounds(ratio)[1] + affine) for weight, ratio, affine in gothic_rows),
        F(0),
    )
    expected_upper = F(81908500355, 936943462656)
    margin = integrated_price - gothic_upper
    expected_margin = F(898545848033, 103063780892160)
    if gothic_upper != expected_upper or margin != expected_margin or margin <= 0:
        raise CertificateError("marginal-price/Gothic separation changed")
    return {
        "positive_gothic_upper": ftext(gothic_upper),
        "integrated_marginal_price": ftext(integrated_price),
        "price_minus_gothic_upper": ftext(margin),
        "strict_separation_verified": True,
    }


def payload_hash(certificate: Mapping[str, object]) -> str:
    payload = {key: value for key, value in certificate.items() if key != "integrity"}
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def rendered_bytes(certificate: Mapping[str, object]) -> bytes:
    return (json.dumps(certificate, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def build_certificate() -> dict[str, object]:
    differences = positive_differences(GOL0MB)
    if len(differences) != 28:
        raise CertificateError("unexpected Golomb difference count")
    marginal = marginal_price_fixture()
    value = F(marginal["integrated_marginal_price"])
    certificate: dict[str, object] = {
        "schema": SCHEMA,
        "status": STATUS,
        "scope": {
            "proved": [
                "ordered dipole strip decomposition",
                "marginal vertex-cover/transport price theorem",
                "exact n=4 marginal-price counterfixture",
            ],
            "not_proved": [
                "no-go for the exact intersection coupling",
                "no-go for signed or cross-epoch masters",
                "C058",
                "Erdos Problem 1191",
                "publication novelty or prize eligibility",
            ],
        },
        "local_strip_audit": local_strip_audit(),
        "golomb_fixture": {
            "points": list(GOL0MB),
            "difference_count": len(differences),
            "current_gaps": {str(key): value for key, value in current_gaps(GOL0MB).items()},
            "wave_edges": list(wave_edges(GOL0MB)),
        },
        "marginal_price": marginal,
        "gothic_separation": gothic_separation_fixture(value),
    }
    certificate["integrity"] = {
        "payload_sha256": payload_hash(certificate),
        "canonical_json": True,
    }
    return certificate


def validate_certificate(certificate: Mapping[str, object]) -> None:
    expected = build_certificate()
    if certificate.get("schema") != SCHEMA or certificate.get("status") != STATUS:
        raise CertificateError("schema or status mismatch")
    if certificate.get("integrity", {}).get("payload_sha256") != payload_hash(certificate):
        raise CertificateError("payload hash mismatch")
    if certificate != expected:
        raise CertificateError("semantic replay mismatch")


def rehash(certificate: dict[str, object]) -> None:
    certificate.setdefault("integrity", {})["payload_sha256"] = payload_hash(certificate)


def self_check(certificate: Mapping[str, object]) -> int:
    mutations: list[dict[str, object]] = []

    changed = copy.deepcopy(certificate)
    changed["status"] = "ERDOS_1191_SOLVED"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["scope"]["not_proved"] = []
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["marginal_price"]["stages"].pop()
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["marginal_price"]["integrated_marginal_price"] = "1/10"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["gothic_separation"]["positive_gothic_upper"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["gothic_separation"]["price_minus_gothic_upper"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["local_strip_audit"]["same_sign_and_reverse_order_disjoint"] = False
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["integrity"]["payload_sha256"] = "0" * 64
    mutations.append(changed)

    rejected = 0
    for mutation in mutations:
        try:
            validate_certificate(mutation)
        except CertificateError:
            rejected += 1
    if rejected != len(mutations):
        raise CertificateError("a semantic or hash mutation was accepted")
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--verify", type=Path, help="verify an existing certificate")
    parser.add_argument("--self-check", action="store_true", help="run semantic mutation checks")
    args = parser.parse_args()

    certificate = build_certificate()
    if args.verify:
        loaded = json.loads(args.verify.read_text(encoding="utf-8"))
        validate_certificate(loaded)
        if rendered_bytes(loaded) != rendered_bytes(certificate):
            raise CertificateError("byte replay mismatch")
    if args.self_check:
        self_check(certificate)
    if not args.verify:
        args.output.write_bytes(rendered_bytes(certificate))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
