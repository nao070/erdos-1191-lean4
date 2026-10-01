"""Deterministic exact finite certificate for multiscale arc identities.

This script checks finite instances only.  It deliberately distinguishes the
literal-set and direct-variance oracles from the formulas in
``multiscale_variance.py``.  Passing this certificate is not an asymptotic
result and does not resolve Erdos Problem #1191.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from fractions import Fraction
from itertools import combinations
from pathlib import Path

from endpoint_variance import (
    crossing_loads,
    endpoint_imbalance,
    short_pair_edges,
    variance,
)
from multiscale_variance import (
    cyclic_arc_covariance,
    cyclic_arc_covariance_via_resistance,
    cyclic_arc_overlap,
    pair_pair_covariance_sum,
)

CERTIFICATE_DATE = "2026-08-28"
DEFAULT_OUTPUT = "multiscale_variance_certificate_2026-08-28.json"


def _fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _literal_cyclic_arc(start: int, length: int, modulus: int) -> set[int]:
    """Independent literal realization of ``{start+1,...,start+length}``."""
    return {(start + step) % modulus for step in range(1, length + 1)}


def _positive_differences(points: tuple[int, ...]) -> list[int]:
    return sorted(
        right - left
        for index, left in enumerate(points)
        for right in points[index + 1 :]
    )


def _arc_kernel_checks() -> tuple[dict[str, object], dict[str, object]]:
    overlap_checks = 0
    resistance_checks = 0
    for modulus in range(2, 13):
        for left_start in range(modulus):
            for right_start in range(modulus):
                for left_length in range(1, modulus):
                    left_arc = _literal_cyclic_arc(
                        left_start,
                        left_length,
                        modulus,
                    )
                    for right_length in range(1, modulus):
                        right_arc = _literal_cyclic_arc(
                            right_start,
                            right_length,
                            modulus,
                        )
                        literal_overlap = len(left_arc & right_arc)
                        formula_overlap = cyclic_arc_overlap(
                            left_start,
                            left_length,
                            right_start,
                            right_length,
                            modulus,
                        )
                        if formula_overlap != literal_overlap:
                            raise AssertionError(
                                "cyclic arc overlap disagreed with literal sets"
                            )
                        overlap_checks += 1

                        literal_covariance = Fraction(literal_overlap) - Fraction(
                            left_length * right_length,
                            modulus,
                        )
                        resistance_covariance = (
                            cyclic_arc_covariance_via_resistance(
                                left_start,
                                left_length,
                                right_start,
                                right_length,
                                modulus,
                            )
                        )
                        if resistance_covariance != literal_covariance:
                            raise AssertionError(
                                "resistance polarization disagreed with literal covariance"
                            )
                        resistance_checks += 1

    expected_count = 49_192
    if overlap_checks != expected_count or resistance_checks != expected_count:
        raise AssertionError("unexpected exhaustive arc-kernel case count")
    return (
        {
            "check_count": overlap_checks,
            "mismatch_count": 0,
            "modulus_range_inclusive": [2, 12],
            "start_ranges": "both starts exhaust all residues 0,...,N-1",
            "length_ranges": "both lengths exhaust 1,...,N-1",
            "oracle": "literal Python sets of cyclic integer residues",
        },
        {
            "check_count": resistance_checks,
            "mismatch_count": 0,
            "modulus_range_inclusive": [2, 12],
            "comparison": (
                "four-endpoint cycle-resistance polarization equals literal "
                "overlap minus LM/N"
            ),
        },
    )


def _ordered_pair_pair_checks() -> dict[str, object]:
    checks = 0
    ordered_kernel_terms = 0
    universe = tuple(range(7))
    for size in range(len(universe) + 1):
        for points in combinations(universe, size):
            for modulus in range(2, 11):
                kernel_sum = pair_pair_covariance_sum(points, modulus)
                direct = Fraction(modulus) * variance(
                    crossing_loads(points, modulus)
                )
                if kernel_sum != direct:
                    raise AssertionError(
                        "ordered pair-pair expansion disagreed with direct variance"
                    )
                edge_count = len(short_pair_edges(points, modulus))
                ordered_kernel_terms += edge_count * edge_count
                checks += 1
    if checks != 1_152:
        raise AssertionError("unexpected ordered pair-pair case count")
    return {
        "check_count": checks,
        "mismatch_count": 0,
        "point_sets": "all 128 subsets of {0,1,2,3,4,5,6}",
        "modulus_range_inclusive": [2, 10],
        "ordered_kernel_terms_evaluated": ordered_kernel_terms,
        "oracle": "N times Fraction-valued variance of direct crossing_loads",
    }


def _sidon_three_cycle_check() -> dict[str, object]:
    points = (0, 3, 7, 12)
    modulus = 6
    differences = _positive_differences(points)
    if len(differences) != 6 or len(set(differences)) != 6:
        raise AssertionError("three-cycle fixture is not a Sidon ruler")

    edges = short_pair_edges(points, modulus)
    short_distances = [edge.distance for edge in edges]
    edge_residues = [[edge.tail, edge.head] for edge in edges]
    if short_distances != [3, 4, 5] or edge_residues != [
        [0, 3],
        [3, 1],
        [1, 0],
    ]:
        raise AssertionError("short edges no longer form the certified 3-cycle")

    loads = crossing_loads(points, modulus)
    direct_variance = variance(loads)
    if direct_variance != 0:
        raise AssertionError("certified Sidon 3-cycle lost zero variance")
    imbalance = endpoint_imbalance(points, modulus)
    if imbalance != [0] * modulus:
        raise AssertionError("certified Sidon 3-cycle lost endpoint balance")

    return {
        "check_count": 4,
        "mismatch_count": 0,
        "points": list(points),
        "modulus": modulus,
        "positive_differences": differences,
        "short_edge_distances": short_distances,
        "short_edge_tail_head_residues": edge_residues,
        "crossing_loads": loads,
        "endpoint_imbalance": imbalance,
        "variance": _fraction_text(direct_variance),
    }


def _covariance_sign_flip_check() -> dict[str, object]:
    covariance_8 = cyclic_arc_covariance(0, 3, 1, 6, 8)
    covariance_16 = cyclic_arc_covariance(0, 3, 1, 6, 16)
    if covariance_8 != Fraction(-1, 4):
        raise AssertionError("N=8 covariance changed from -1/4")
    if covariance_16 != Fraction(7, 8):
        raise AssertionError("N=16 covariance changed from 7/8")
    if not covariance_8 < 0 < covariance_16:
        raise AssertionError("certified covariance sign flip disappeared")
    return {
        "check_count": 3,
        "mismatch_count": 0,
        "point_fixture": [0, 1, 3, 7],
        "left_pair": [0, 3],
        "right_pair": [1, 7],
        "left_arc_start_length": [0, 3],
        "right_arc_start_length": [1, 6],
        "modulus_8_covariance": _fraction_text(covariance_8),
        "modulus_16_covariance": _fraction_text(covariance_16),
    }


def _dominant_gap_family_checks() -> dict[str, object]:
    instances: list[dict[str, object]] = []
    sidon_checks = 0
    formula_checks = 0
    pair_expansion_checks = 0
    for gap_parameter in range(3, 201):
        points = (0, 1, gap_parameter + 1, gap_parameter + 3)
        modulus = gap_parameter + 4
        differences = _positive_differences(points)
        if len(differences) != 6 or len(set(differences)) != 6:
            raise AssertionError("dominant-gap fixture ceased to be Sidon")
        sidon_checks += 1

        expected = Fraction(
            19 * gap_parameter + 27,
            (gap_parameter + 4) ** 2,
        )
        direct = variance(crossing_loads(points, modulus))
        if direct != expected:
            raise AssertionError("dominant-gap direct variance formula failed")
        formula_checks += 1

        pair_sum = pair_pair_covariance_sum(points, modulus)
        if pair_sum != modulus * expected:
            raise AssertionError("dominant-gap pair-pair expansion failed")
        pair_expansion_checks += 1

        instances.append(
            {
                "G": gap_parameter,
                "modulus": modulus,
                "points": list(points),
                "variance": _fraction_text(expected),
            }
        )

    if len(instances) != 198:
        raise AssertionError("unexpected dominant-gap instance count")
    return {
        "check_count": sidon_checks + formula_checks + pair_expansion_checks,
        "mismatch_count": 0,
        "G_range_inclusive": [3, 200],
        "instance_count": len(instances),
        "sidon_uniqueness_checks": sidon_checks,
        "direct_variance_formula_checks": formula_checks,
        "pair_pair_expansion_checks": pair_expansion_checks,
        "family": "A_G={0,1,G+1,G+3}, N=G+4",
        "finite_formula_tested": "Var(C_N)=(19G+27)/(G+4)^2",
        "ordered_instance_records_sha256": hashlib.sha256(
            _canonical_bytes(instances)
        ).hexdigest(),
        "first_instance": instances[0],
        "last_instance": instances[-1],
    }


def build_certificate() -> dict[str, object]:
    """Run every exact check and return the self-hashed certificate payload."""
    overlap, resistance = _arc_kernel_checks()
    ordered_expansion = _ordered_pair_pair_checks()
    zero_mode = _sidon_three_cycle_check()
    sign_flip = _covariance_sign_flip_check()
    dominant_gap = _dominant_gap_family_checks()

    check_records = {
        "covariance_sign_flip": sign_flip,
        "cyclic_arc_overlap": overlap,
        "dominant_gap_family": dominant_gap,
        "ordered_pair_pair_expansion": ordered_expansion,
        "resistance_polarization": resistance,
        "sidon_three_cycle_zero_mode": zero_mode,
    }
    exact_check_count = sum(
        int(record["check_count"]) for record in check_records.values()
    )
    if exact_check_count != 100_137:
        raise AssertionError("unexpected grand total of exact checks")

    source_directory = Path(__file__).resolve().parent
    payload: dict[str, object] = {
        "certificate_date": CERTIFICATE_DATE,
        "evidence_label": "[COMPUTATIONAL — CERTIFIED FINITE]",
        "evidence_scope": (
            "Certified exact finite evidence only; no asymptotic theorem and no "
            "resolution of Erdos Problem #1191 is claimed."
        ),
        "formulas_checked": {
            "arc_overlap": (
                "(L-x)_+-(L-x-M)_+ +(x+M-N)_+-(x+M-N-L)_+, "
                "x=(c-a) mod N"
            ),
            "arc_covariance": "K_N(B,B')=|B intersect B'|-LM/N",
            "cycle_resistance": "Phi_N(t)=r(N-r)/N, r=t mod N",
            "resistance_polarization": (
                "K_N=1/2[Phi(a-d)+Phi(b-c)-Phi(a-c)-Phi(b-d)]"
            ),
            "ordered_pair_pair_expansion": (
                "N Var(C_N)=sum over ordered short-pair pairs (p,q) of K_N(p,q)"
            ),
            "dominant_gap_finite_family": (
                "A_G={0,1,G+1,G+3}, N=G+4, "
                "Var(C_N)=(19G+27)/(G+4)^2"
            ),
        },
        "checks": check_records,
        "environment": {
            "machine": platform.machine(),
            "platform": platform.platform(),
            "python_implementation": platform.python_implementation(),
            "python_version": platform.python_version(),
            "release": platform.release(),
            "system": platform.system(),
        },
        "source_sha256": {
            "certificate_script": _sha256(Path(__file__).resolve()),
            "endpoint_variance.py": _sha256(
                source_directory / "endpoint_variance.py"
            ),
            "multiscale_variance.py": _sha256(
                source_directory / "multiscale_variance.py"
            ),
        },
        "summary": {
            "all_checks_passed": True,
            "exact_check_count": exact_check_count,
            "mismatch_count": 0,
        },
    }
    payload["canonical_payload_sha256"] = hashlib.sha256(
        _canonical_bytes(payload)
    ).hexdigest()
    return payload


def serialize_certificate(certificate: dict[str, object]) -> bytes:
    """Return sorted, UTF-8, newline-terminated deterministic JSON bytes."""
    return (
        json.dumps(
            certificate,
            sort_keys=True,
            indent=2,
            ensure_ascii=False,
        )
        + "\n"
    ).encode("utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent / DEFAULT_OUTPUT,
        help="deterministic JSON output path",
    )
    arguments = parser.parse_args(argv)
    certificate = build_certificate()
    output_bytes = serialize_certificate(certificate)
    arguments.output.write_bytes(output_bytes)
    summary = {
        "canonical_payload_sha256": certificate["canonical_payload_sha256"],
        "exact_check_count": certificate["summary"]["exact_check_count"],
        "json_file_sha256": hashlib.sha256(output_bytes).hexdigest(),
        "output_name": arguments.output.name,
    }
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
