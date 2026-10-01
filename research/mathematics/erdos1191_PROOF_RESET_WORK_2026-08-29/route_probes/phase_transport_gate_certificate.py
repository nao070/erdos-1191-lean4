#!/usr/bin/env python3
"""Exact certificate for the prefix/scale phase-transport gate.

The certificate has three deliberately limited jobs:

* verify the two-dimensional prefix/scale curl for centered box energies;
* verify finite scale Abel summation and finite epoch transport, including
  every initial and terminal boundary;
* prove and exercise the exact nonnegativity gate for the naive continuum
  coefficient profile.

It does not construct the common signed capacity map required by C058.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
from typing import Mapping, Sequence


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "phase_transport_gate_certificate.json"
SCHEMA = "erdos1191.phase_transport_gate.v1"


class CertificateError(RuntimeError):
    """Raised when an exact certificate check fails."""


def ftext(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def parse_fraction(value: str) -> F:
    numerator, denominator = value.split("/", 1)
    return F(int(numerator), int(denominator))


def power_two(exponent: int) -> F:
    if exponent >= 0:
        return F(1 << exponent)
    return F(1, 1 << (-exponent))


def positive_differences(points: Sequence[int]) -> tuple[int, ...]:
    return tuple(
        points[right] - points[left]
        for left in range(len(points))
        for right in range(left + 1, len(points))
    )


def centered_lowpass(points: Sequence[int], exponent: int) -> F:
    """Return C_(j,r) with the dyadic rational surrogate T=2^r."""
    width = power_two(exponent)
    return 2 * sum(
        (
            (width - F(difference)) / (width * width)
            for difference in positive_differences(points)
            if F(difference) < width
        ),
        F(0),
    )


def centered_band(points: Sequence[int], exponent: int) -> F:
    return centered_lowpass(points, exponent) - centered_lowpass(points, exponent + 1)


def prefix_state(
    prefixes: Mapping[int, Sequence[int]],
    first_epoch: int,
    last_epoch: int,
    first_scale: int,
    terminal_scale: int,
) -> tuple[dict[tuple[int, int], F], dict[tuple[int, int], F], dict[tuple[int, int], F]]:
    """Build exact C, O, Delta tables on one finite rectangle."""
    needed_epochs = range(first_epoch - 1, last_epoch + 1)
    needed_scales = range(first_scale, terminal_scale + 1)
    c_table = {
        (epoch, scale): centered_lowpass(prefixes[epoch], scale)
        for epoch in needed_epochs
        for scale in needed_scales
    }
    o_table = {
        (epoch, scale): c_table[epoch, scale] - c_table[epoch, scale + 1]
        for epoch in needed_epochs
        for scale in range(first_scale, terminal_scale)
    }
    delta_table = {
        (epoch, scale): c_table[epoch, scale] - c_table[epoch - 1, scale]
        for epoch in range(first_epoch, last_epoch + 1)
        for scale in needed_scales
    }
    return c_table, o_table, delta_table


def verify_curl(
    o_table: Mapping[tuple[int, int], F],
    delta_table: Mapping[tuple[int, int], F],
    first_epoch: int,
    last_epoch: int,
    first_scale: int,
    last_scale: int,
) -> tuple[dict[str, object], ...]:
    rows = []
    for epoch in range(first_epoch, last_epoch + 1):
        for scale in range(first_scale, last_scale + 1):
            prefix_difference = delta_table[epoch, scale] - delta_table[epoch, scale + 1]
            scale_difference = o_table[epoch, scale] - o_table[epoch - 1, scale]
            if prefix_difference != scale_difference:
                raise CertificateError("prefix/scale curl failed")
            rows.append(
                {
                    "epoch": epoch,
                    "scale": scale,
                    "delta_scale_difference": ftext(prefix_difference),
                    "band_prefix_difference": ftext(scale_difference),
                    "equal": True,
                }
            )
    return tuple(rows)


def cumulative_coefficients(coefficients: Mapping[int, F], first_scale: int, last_scale: int) -> dict[int, F]:
    running = F(0)
    result = {}
    for scale in range(first_scale, last_scale + 1):
        running += coefficients.get(scale, F(0))
        result[scale] = running
    return result


def verify_scale_abel(
    coefficients: Mapping[int, F],
    delta: Mapping[int, F],
    band_difference: Mapping[int, F],
    first_scale: int,
    last_scale: int,
) -> dict[str, object]:
    """Verify sum c Delta = sum s curl + the exact scale terminal."""
    cumulative = cumulative_coefficients(coefficients, first_scale, last_scale)
    lhs = sum(
        (coefficients.get(scale, F(0)) * delta[scale] for scale in range(first_scale, last_scale + 1)),
        F(0),
    )
    band_bulk = sum(
        (cumulative[scale] * band_difference[scale] for scale in range(first_scale, last_scale + 1)),
        F(0),
    )
    scale_terminal = cumulative[last_scale] * delta[last_scale + 1]
    if lhs != band_bulk + scale_terminal:
        raise CertificateError("finite scale Abel identity failed")
    return {
        "coefficients": {str(scale): ftext(coefficients.get(scale, F(0))) for scale in range(first_scale, last_scale + 1)},
        "cumulative": {str(scale): ftext(cumulative[scale]) for scale in range(first_scale, last_scale + 1)},
        "lhs": ftext(lhs),
        "band_bulk": ftext(band_bulk),
        "scale_terminal": ftext(scale_terminal),
        "rhs": ftext(band_bulk + scale_terminal),
        "identity_verified": True,
    }


def fejer_weight(epoch: int, horizon: int) -> F:
    if epoch > horizon:
        raise ValueError("epoch cannot exceed the Fejer horizon")
    return F((horizon + 1 - epoch) ** 2, (horizon + 1) ** 2)


def verify_epoch_transport(
    o_table: Mapping[tuple[int, int], F],
    delta_table: Mapping[tuple[int, int], F],
    coefficient_rows: Mapping[int, Mapping[int, F]],
    weights: Mapping[int, F],
    first_epoch: int,
    last_epoch: int,
    first_scale: int,
    last_scale: int,
) -> dict[str, object]:
    """Verify the exact finite rectangle transport and all four boundaries."""
    cumulative = {
        epoch: cumulative_coefficients(coefficient_rows[epoch], first_scale, last_scale)
        for epoch in range(first_epoch, last_epoch + 1)
    }
    lhs = sum(
        (
            weights[epoch]
            * coefficient_rows[epoch].get(scale, F(0))
            * delta_table[epoch, scale]
            for epoch in range(first_epoch, last_epoch + 1)
            for scale in range(first_scale, last_scale + 1)
        ),
        F(0),
    )

    initial_epoch_boundary = -sum(
        (
            weights[first_epoch]
            * cumulative[first_epoch][scale]
            * o_table[first_epoch - 1, scale]
            for scale in range(first_scale, last_scale + 1)
        ),
        F(0),
    )
    band_rows = []
    interior_band_bulk = F(0)
    for epoch in range(first_epoch, last_epoch):
        for scale in range(first_scale, last_scale + 1):
            band_coefficient = (
                weights[epoch] * cumulative[epoch][scale]
                - weights[epoch + 1] * cumulative[epoch + 1][scale]
            )
            contribution = band_coefficient * o_table[epoch, scale]
            interior_band_bulk += contribution
            band_rows.append(
                {
                    "epoch": epoch,
                    "scale": scale,
                    "b": ftext(band_coefficient),
                    "O": ftext(o_table[epoch, scale]),
                    "contribution": ftext(contribution),
                }
            )
    terminal_epoch_boundary = sum(
        (
            weights[last_epoch]
            * cumulative[last_epoch][scale]
            * o_table[last_epoch, scale]
            for scale in range(first_scale, last_scale + 1)
        ),
        F(0),
    )
    scale_terminal_boundary = sum(
        (
            weights[epoch]
            * cumulative[epoch][last_scale]
            * delta_table[epoch, last_scale + 1]
            for epoch in range(first_epoch, last_epoch + 1)
        ),
        F(0),
    )
    rhs = initial_epoch_boundary + interior_band_bulk + terminal_epoch_boundary + scale_terminal_boundary
    if lhs != rhs:
        raise CertificateError("finite epoch transport identity failed")
    return {
        "weights": {str(epoch): ftext(weights[epoch]) for epoch in range(first_epoch, last_epoch + 1)},
        "cumulative": {
            str(epoch): {str(scale): ftext(cumulative[epoch][scale]) for scale in range(first_scale, last_scale + 1)}
            for epoch in range(first_epoch, last_epoch + 1)
        },
        "band_rows": band_rows,
        "lhs": ftext(lhs),
        "initial_epoch_boundary": ftext(initial_epoch_boundary),
        "interior_band_bulk": ftext(interior_band_bulk),
        "terminal_epoch_boundary": ftext(terminal_epoch_boundary),
        "scale_terminal_boundary": ftext(scale_terminal_boundary),
        "rhs": ftext(rhs),
        "identity_verified": True,
    }


def naive_coefficient(mark_count: int, cutoff: int, scale: int) -> F:
    """c_(j,r)=2^r/(2 n_j^2) for r<=R_j, zero otherwise."""
    return power_two(scale) / (2 * mark_count * mark_count) if scale <= cutoff else F(0)


def naive_cumulative(mark_count: int, cutoff: int, scale: int) -> F:
    """The exact negative-infinite cumulative sum of naive_coefficient."""
    return power_two(min(scale, cutoff)) / (mark_count * mark_count)


def verify_naive_cumulative(mark_count: int, cutoff: int, scales: Sequence[int]) -> tuple[dict[str, object], ...]:
    rows = []
    for scale in scales:
        cumulative = naive_cumulative(mark_count, cutoff, scale)
        previous = naive_cumulative(mark_count, cutoff, scale - 1)
        coefficient = naive_coefficient(mark_count, cutoff, scale)
        if cumulative - previous != coefficient:
            raise CertificateError("naive cumulative geometric identity failed")
        rows.append(
            {
                "scale": scale,
                "c": ftext(coefficient),
                "s": ftext(cumulative),
                "s_previous": ftext(previous),
                "difference_verified": True,
            }
        )
    return tuple(rows)


def naive_band_coefficient(
    weight: F,
    next_weight: F,
    mark_count: int,
    next_mark_count: int,
    cutoff: int,
    next_cutoff: int,
    scale: int,
) -> F:
    return (
        weight * naive_cumulative(mark_count, cutoff, scale)
        - next_weight * naive_cumulative(next_mark_count, next_cutoff, scale)
    )


def naive_gate(
    weight: F,
    next_weight: F,
    mark_count: int,
    next_mark_count: int,
    cutoff: int,
    next_cutoff: int,
) -> dict[str, object]:
    """Return the exact iff gate for b_(j,r)>=0 at every dyadic phase."""
    if min(weight, next_weight) <= 0 or min(mark_count, next_mark_count) <= 0:
        raise ValueError("weights and mark counts must be positive")
    cutoff_jump = max(0, next_cutoff - cutoff)
    horizon_growth = power_two(cutoff_jump)
    mark_growth_square = F(next_mark_count * next_mark_count, mark_count * mark_count)
    lhs = next_weight * horizon_growth
    rhs = weight * mark_growth_square
    passes = lhs <= rhs
    threshold = mark_growth_square * weight / next_weight
    critical_scales = sorted({cutoff - 1, cutoff, cutoff + 1, next_cutoff - 1, next_cutoff, next_cutoff + 1})
    rows = []
    for scale in critical_scales:
        coefficient = naive_band_coefficient(
            weight,
            next_weight,
            mark_count,
            next_mark_count,
            cutoff,
            next_cutoff,
            scale,
        )
        rows.append({"scale": scale, "b": ftext(coefficient), "nonnegative": coefficient >= 0})
    if passes != all(row["nonnegative"] for row in rows):
        raise CertificateError("critical-scale replay disagrees with the naive iff gate")
    return {
        "weight": ftext(weight),
        "next_weight": ftext(next_weight),
        "mark_count": mark_count,
        "next_mark_count": next_mark_count,
        "cutoff": cutoff,
        "next_cutoff": next_cutoff,
        "cutoff_jump_positive_part": cutoff_jump,
        "horizon_growth": ftext(horizon_growth),
        "mark_growth_square": ftext(mark_growth_square),
        "threshold_for_horizon_growth": ftext(threshold),
        "gate_lhs_next_weight_times_horizon_growth": ftext(lhs),
        "gate_rhs_weight_times_mark_growth_square": ftext(rhs),
        "all_band_coefficients_nonnegative": passes,
        "critical_scale_rows": rows,
    }


def payload_hash(certificate: Mapping[str, object]) -> str:
    payload = {key: value for key, value in certificate.items() if key != "integrity"}
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def rendered_bytes(certificate: Mapping[str, object]) -> bytes:
    return (json.dumps(certificate, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def fixture_data() -> tuple[
    dict[int, tuple[int, ...]],
    int,
    int,
    int,
    int,
    dict[int, dict[int, F]],
    dict[int, F],
]:
    prefixes = {0: (0,), 1: (0, 1), 2: (0, 1, 4, 6)}
    first_epoch, last_epoch = 1, 2
    first_scale, last_scale = -1, 3
    coefficient_rows = {
        1: {-1: F(1, 7), 0: F(2, 9), 1: F(3, 11), 2: F(1, 5), 3: F(2, 13)},
        2: {-1: F(2, 11), 0: F(1, 6), 1: F(4, 15), 2: F(3, 14), 3: F(1, 8)},
    }
    weights = {1: fejer_weight(1, 3), 2: fejer_weight(2, 3)}
    return prefixes, first_epoch, last_epoch, first_scale, last_scale, coefficient_rows, weights


def build_certificate() -> dict[str, object]:
    (
        prefixes,
        first_epoch,
        last_epoch,
        first_scale,
        last_scale,
        coefficient_rows,
        weights,
    ) = fixture_data()
    c_table, o_table, delta_table = prefix_state(
        prefixes,
        first_epoch,
        last_epoch,
        first_scale,
        last_scale + 1,
    )
    curl_rows = verify_curl(
        o_table,
        delta_table,
        first_epoch,
        last_epoch,
        first_scale,
        last_scale,
    )
    scale_rows = []
    for epoch in range(first_epoch, last_epoch + 1):
        scale_rows.append(
            {
                "epoch": epoch,
                **verify_scale_abel(
                    coefficient_rows[epoch],
                    {scale: delta_table[epoch, scale] for scale in range(first_scale, last_scale + 2)},
                    {
                        scale: o_table[epoch, scale] - o_table[epoch - 1, scale]
                        for scale in range(first_scale, last_scale + 1)
                    },
                    first_scale,
                    last_scale,
                ),
            }
        )
    transport = verify_epoch_transport(
        o_table,
        delta_table,
        coefficient_rows,
        weights,
        first_epoch,
        last_epoch,
        first_scale,
        last_scale,
    )

    gate_weight = fejer_weight(1, 10)
    gate_next_weight = fejer_weight(2, 10)
    passing_gate = naive_gate(gate_weight, gate_next_weight, 2, 4, 2, 4)
    failing_gate = naive_gate(gate_weight, gate_next_weight, 2, 4, 2, 5)
    witness = next(row for row in failing_gate["critical_scale_rows"] if row["scale"] == 5)
    if parse_fraction(witness["b"]) != F(-62, 121):
        raise CertificateError("counterfixture negative coefficient changed")

    certificate: dict[str, object] = {
        "schema": SCHEMA,
        "purpose": "Certify the exact prefix/scale curl, finite-boundary transport identity, and the iff sign gate for the naive continuum-capacity coefficients.",
        "theorem_contract": {
            "curl": "Delta_(j,r)-Delta_(j,r+1)=O_(j,r)-O_(j-1,r)",
            "scale_abel": "sum_(r=L)^R c_(j,r)Delta_(j,r)=sum_(r=L)^R s_(j,r)(O_(j,r)-O_(j-1,r))+s_(j,R)Delta_(j,R+1)",
            "band_coefficient": "b_(j,r)=w_j*s_(j,r)-w_(j+1)*s_(j+1,r)",
            "naive_profile": "c_(j,r)=2^r/(2*n_j^2)*1_(r<=R_j), s_(j,r)=2^min(r,R_j)/n_j^2",
            "naive_gate_iff": "b_(j,r)>=0 for every integer r iff w_(j+1)*2^max(0,R_(j+1)-R_j)<=w_j*(n_(j+1)/n_j)^2",
        },
        "fixture": {
            "prefixes": {str(epoch): list(points) for epoch, points in prefixes.items()},
            "first_epoch": first_epoch,
            "last_epoch": last_epoch,
            "first_scale": first_scale,
            "last_scale": last_scale,
            "C": {f"{epoch},{scale}": ftext(value) for (epoch, scale), value in sorted(c_table.items())},
            "O": {f"{epoch},{scale}": ftext(value) for (epoch, scale), value in sorted(o_table.items())},
            "Delta": {f"{epoch},{scale}": ftext(value) for (epoch, scale), value in sorted(delta_table.items())},
        },
        "curl_rows": list(curl_rows),
        "scale_abel_rows": scale_rows,
        "finite_epoch_transport": transport,
        "naive_cumulative_rows": list(verify_naive_cumulative(4, 3, tuple(range(-4, 7)))),
        "naive_gate_passing_fixture": passing_gate,
        "naive_gate_counterfixture": {
            **failing_gate,
            "interior_epoch": 1,
            "fejer_horizon": 10,
            "negative_witness_scale": 5,
            "negative_witness_b": witness["b"],
            "interpretation": "The width-horizon factor 8 exceeds the exact threshold 400/81, so an interior band coefficient is negative.",
        },
        "scope": {
            "exact_prefix_scale_curl_certified": True,
            "finite_initial_and_terminal_boundaries_certified": True,
            "naive_nonnegative_gate_iff_certified": True,
            "naive_nonnegative_adjacent_epoch_realization_unconditional": False,
            "data_dependent_allocation_ruled_out": False,
            "signed_coefficients_ruled_out": False,
            "longer_transport_ruled_out": False,
            "c058_resolved": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "prize_claim_ready": False,
        },
    }
    certificate["integrity"] = {"payload_sha256": payload_hash(certificate)}
    return certificate


def validate_certificate(certificate: Mapping[str, object]) -> None:
    if certificate.get("schema") != SCHEMA:
        raise CertificateError("schema mismatch")
    integrity = certificate.get("integrity")
    if not isinstance(integrity, Mapping) or integrity.get("payload_sha256") != payload_hash(certificate):
        raise CertificateError("payload hash mismatch")
    expected_scope = build_certificate()["scope"]
    if certificate.get("scope") != expected_scope:
        raise CertificateError("scope boundary mismatch")
    expected = build_certificate()
    if certificate != expected:
        raise CertificateError("semantic replay mismatch")


def rehash(certificate: dict[str, object]) -> None:
    certificate["integrity"] = {"payload_sha256": payload_hash(certificate)}


def self_check(certificate: Mapping[str, object]) -> int:
    validate_certificate(certificate)
    mutations = []

    changed = copy.deepcopy(certificate)
    changed["naive_gate_counterfixture"]["negative_witness_b"] = "0/1"
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["theorem_contract"]["naive_gate_iff"] += " MUTATED"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["scope"]["c058_resolved"] = True
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["finite_epoch_transport"]["scale_terminal_boundary"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["curl_rows"][0]["equal"] = False
    rehash(changed)
    mutations.append(changed)

    rejected = 0
    for mutation in mutations:
        try:
            validate_certificate(mutation)
        except CertificateError:
            rejected += 1
    if rejected != len(mutations):
        raise CertificateError("a semantic mutation was not rejected")
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit", action="store_true", help="print the canonical certificate JSON")
    parser.add_argument("--verify", type=Path, help="verify an existing certificate")
    parser.add_argument("--self-check", action="store_true", help="run mutation rejection checks")
    args = parser.parse_args()

    if args.verify:
        certificate = json.loads(args.verify.read_text(encoding="utf-8"))
        validate_certificate(certificate)
    else:
        certificate = build_certificate()
    if args.self_check:
        self_check(certificate)
    if args.emit or not args.verify:
        print(rendered_bytes(certificate).decode("utf-8"), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
