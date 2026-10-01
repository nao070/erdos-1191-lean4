"""Deterministic exhaustive certificate for Target D (2026-08-28).

The primary engine extends ``endpoint_variance.py``.  A deliberately separate
oracle enumerates positive gap compositions and computes offset variance from
translated blocks, without calling the primary Golomb filter or gap formula.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import random
from collections.abc import Iterable, Iterator
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

from endpoint_variance import (
    canonical_reflection_ruler,
    crossing_loads,
    diameter_regime_variance,
    endpoint_imbalance,
    golomb_variance_minimum,
    has_distinct_contiguous_gap_sums,
    homometric_distance_spectrum,
    iter_normalized_golomb_rulers,
    normalized_ruler_candidate_count,
    variance,
    zero_variance_cycle_decomposition,
)

CERTIFICATE_DATE = "2026-08-28"
DEFAULT_OUTPUT = "golomb_variance_certificate_2026-08-28.json"
RANDOM_SEED = 1191


def _fraction_text(value: Fraction | None) -> str | None:
    if value is None:
        return None
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _ordered_json_sha256(value: object) -> str:
    canonical = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode()
    return hashlib.sha256(canonical).hexdigest()


def _gaps(points: Iterable[int]) -> tuple[int, ...]:
    marks = tuple(points)
    return tuple(marks[index + 1] - marks[index] for index in range(len(marks) - 1))


def _oracle_compositions(total: int, parts: int) -> Iterator[tuple[int, ...]]:
    """Enumerate positive compositions recursively (independent of mark subsets)."""
    if parts == 1:
        yield (total,)
        return
    for first in range(1, total - parts + 2):
        for suffix in _oracle_compositions(total - first, parts - 1):
            yield (first, *suffix)


def _oracle_rulers(mark_count: int, diameter: int) -> tuple[tuple[int, ...], ...]:
    rulers: list[tuple[int, ...]] = []
    for gaps in _oracle_compositions(diameter, mark_count - 1):
        contiguous_sums = []
        for start in range(len(gaps)):
            running_sum = 0
            for stop in range(start, len(gaps)):
                running_sum += gaps[stop]
                contiguous_sums.append(running_sum)
        if len(contiguous_sums) != len(set(contiguous_sums)):
            continue
        marks = [0]
        for gap in gaps:
            marks.append(marks[-1] + gap)
        rulers.append(tuple(marks))
    return tuple(rulers)


def _oracle_variance(points: tuple[int, ...], modulus: int) -> Fraction:
    """Direct translated-block oracle, independent of the gap-moment formula."""
    crossing_counts = []
    for boundary in range(modulus):
        cut_pairs = 0
        for index, left in enumerate(points):
            left_block = (left - boundary) // modulus
            for right in points[index + 1 :]:
                if left_block != (right - boundary) // modulus:
                    cut_pairs += 1
        crossing_counts.append(cut_pairs)
    mean = Fraction(sum(crossing_counts), modulus)
    return sum((Fraction(value) - mean) ** 2 for value in crossing_counts) / modulus


def _minimum_record(result) -> dict[str, object]:
    return {
        "modulus": result.modulus,
        "minimum_variance": _fraction_text(result.minimum_variance),
        "minimizer_count_oriented": len(result.minimizers),
        "minimizers": [list(ruler) for ruler in result.minimizers],
        "minimizer_gap_vectors": [list(_gaps(ruler)) for ruler in result.minimizers],
        "minimizer_reflection_class_count": len(result.reflection_classes),
        "minimizer_reflection_representatives": [
            list(ruler) for ruler in result.reflection_classes
        ],
    }


def _exhaustive_records(
    max_marks: int,
    max_diameter: int,
    modulus_offsets: tuple[int, ...],
) -> tuple[list[dict[str, object]], dict[str, int]]:
    records: list[dict[str, object]] = []
    candidate_subsets = 0
    golomb_rulers = 0
    variance_evaluations = 0
    for mark_count in range(2, max_marks + 1):
        for diameter in range(mark_count - 1, max_diameter + 1):
            candidates = normalized_ruler_candidate_count(mark_count, diameter)
            rulers = tuple(iter_normalized_golomb_rulers(mark_count, diameter))
            reflection_classes = {
                canonical_reflection_ruler(ruler) for ruler in rulers
            }
            minima = [
                golomb_variance_minimum(
                    mark_count,
                    diameter,
                    diameter + offset,
                )
                for offset in modulus_offsets
            ]
            if any(result.candidate_count != candidates for result in minima):
                raise AssertionError("candidate count changed between modulus searches")
            if any(result.golomb_ruler_count != len(rulers) for result in minima):
                raise AssertionError("Golomb ruler count changed between modulus searches")
            records.append(
                {
                    "mark_count": mark_count,
                    "diameter": diameter,
                    "candidate_internal_mark_subsets": candidates,
                    "golomb_ruler_count_oriented": len(rulers),
                    "golomb_reflection_class_count": len(reflection_classes),
                    "ordered_ruler_list_sha256": _ordered_json_sha256(rulers),
                    "modulus_results": [_minimum_record(result) for result in minima],
                }
            )
            candidate_subsets += candidates
            golomb_rulers += len(rulers)
            variance_evaluations += len(rulers) * len(modulus_offsets)
    return records, {
        "parameter_pairs": len(records),
        "candidate_internal_mark_subsets": candidate_subsets,
        "golomb_rulers_oriented": golomb_rulers,
        "exact_variance_evaluations": variance_evaluations,
    }


def _oracle_records(
    max_marks: int,
    max_diameter: int,
    modulus_offsets: tuple[int, ...],
) -> tuple[list[dict[str, object]], int, int]:
    records: list[dict[str, object]] = []
    mismatches = 0
    exact_checks = 0
    for mark_count in range(2, max_marks + 1):
        for diameter in range(mark_count - 1, max_diameter + 1):
            oracle_rulers = _oracle_rulers(mark_count, diameter)
            primary_rulers = tuple(
                iter_normalized_golomb_rulers(mark_count, diameter)
            )
            enumeration_match = oracle_rulers == primary_rulers
            exact_checks += 1
            if not enumeration_match:
                mismatches += 1

            modulus_records = []
            for offset in modulus_offsets:
                modulus = diameter + offset
                values = [
                    _oracle_variance(ruler, modulus) for ruler in oracle_rulers
                ]
                oracle_minimum = min(values, default=None)
                oracle_minimizers = tuple(
                    ruler
                    for ruler, value in zip(oracle_rulers, values)
                    if value == oracle_minimum
                )
                primary = golomb_variance_minimum(
                    mark_count,
                    diameter,
                    modulus,
                )
                minimum_match = primary.minimum_variance == oracle_minimum
                minimizers_match = primary.minimizers == oracle_minimizers
                exact_checks += 2
                if not minimum_match:
                    mismatches += 1
                if not minimizers_match:
                    mismatches += 1
                modulus_records.append(
                    {
                        "modulus": modulus,
                        "oracle_minimum_variance": _fraction_text(oracle_minimum),
                        "minimum_match": minimum_match,
                        "minimizers_match": minimizers_match,
                    }
                )
            records.append(
                {
                    "mark_count": mark_count,
                    "diameter": diameter,
                    "composition_count": normalized_ruler_candidate_count(
                        mark_count,
                        diameter,
                    ),
                    "oracle_golomb_ruler_count": len(oracle_rulers),
                    "enumeration_match": enumeration_match,
                    "ordered_oracle_ruler_list_sha256": _ordered_json_sha256(
                        oracle_rulers
                    ),
                    "modulus_results": modulus_records,
                }
            )
    return records, mismatches, exact_checks


def _greedy_mian_chowla(mark_count: int) -> tuple[int, ...]:
    marks = [0]
    differences: set[int] = set()
    while len(marks) < mark_count:
        candidate = marks[-1] + 1
        while any(candidate - mark in differences for mark in marks):
            candidate += 1
        differences.update(candidate - mark for mark in marks)
        marks.append(candidate)
    return tuple(marks)


def _random_golomb_rulers(
    *,
    mark_count: int,
    diameter: int,
    sample_count: int,
    seed: int,
) -> tuple[tuple[tuple[int, ...], ...], int]:
    generator = random.Random(seed)
    rulers: set[tuple[int, ...]] = set()
    attempts = 0
    while len(rulers) < sample_count and attempts < 100_000:
        attempts += 1
        internal = sorted(
            generator.sample(range(1, diameter), mark_count - 2)
        )
        ruler = (0, *internal, diameter)
        if has_distinct_contiguous_gap_sums(_gaps(ruler)):
            rulers.add(ruler)
    if len(rulers) != sample_count:
        raise AssertionError("deterministic random sampler did not reach target")
    return tuple(sorted(rulers)), attempts


def _variance_instance(points: tuple[int, ...], modulus: int) -> dict[str, object]:
    return {
        "points": list(points),
        "gaps": list(_gaps(points)),
        "diameter": points[-1] - points[0],
        "modulus": modulus,
        "variance": _fraction_text(diameter_regime_variance(points, modulus)),
        "reflection_representative": list(canonical_reflection_ruler(points)),
    }


def _mandatory_instances() -> dict[str, object]:
    zero_modulus = 11
    zero_points = (0, 1, zero_modulus)
    zero_cycles = zero_variance_cycle_decomposition(zero_points, zero_modulus)

    union_points = (0, 1, 11, 36, 38, 47)
    union_cycles = zero_variance_cycle_decomposition(union_points, 11)

    homometric_left = (0, 1, 4, 10, 12, 17)
    homometric_right = (0, 1, 8, 11, 13, 17)
    if not homometric_distance_spectrum(homometric_left, homometric_right):
        raise AssertionError("certified homometric pair lost its common spectrum")

    greedy = _greedy_mian_chowla(10)
    if not has_distinct_contiguous_gap_sums(_gaps(greedy)):
        raise AssertionError("greedy Mian-Chowla prefix is not Golomb")

    random_rulers, random_attempts = _random_golomb_rulers(
        mark_count=6,
        diameter=30,
        sample_count=12,
        seed=RANDOM_SEED,
    )

    dominant = (0, 1, 50, 54, 60)
    if not has_distinct_contiguous_gap_sums(_gaps(dominant)):
        raise AssertionError("dominant-gap fixture is not Golomb")

    near_critical = (0, 1, 4, 10, 18, 23, 25)
    with localcontext() as context:
        context.prec = 60
        constant = Decimal(2)
        envelope_checks = []
        for index, mark in enumerate(near_critical[1:], 1):
            bound = constant * index * index * Decimal(2 * index).ln()
            envelope_checks.append(
                {
                    "index": index,
                    "mark": mark,
                    "bound_C_k2_log_2k": str(bound),
                    "satisfies": Decimal(mark) <= bound,
                }
            )
    if not all(check["satisfies"] for check in envelope_checks):
        raise AssertionError("near-critical fixture failed its coordinate envelope")

    return {
        "zero_mode": {
            "conjecture_tested": "Eulerian two-cycle has zero offset variance",
            "points": list(zero_points),
            "modulus": zero_modulus,
            "variance": _fraction_text(variance(crossing_loads(zero_points, zero_modulus))),
            "endpoint_imbalance": endpoint_imbalance(zero_points, zero_modulus),
            "cycle_edge_distances": [
                [edge.distance for edge in cycle] for cycle in zero_cycles
            ],
        },
        "modular_cycle_union": {
            "conjecture_tested": "Separated modular cycles can remain an exact zero mode",
            "points": list(union_points),
            "modulus": 11,
            "variance": _fraction_text(variance(crossing_loads(union_points, 11))),
            "cycle_count": len(union_cycles),
            "cycle_edge_distances": [
                [edge.distance for edge in cycle] for cycle in union_cycles
            ],
        },
        "homometric_pair": {
            "conjecture_tested": "Equal difference spectra need not give equal endpoint variance",
            "points": [list(homometric_left), list(homometric_right)],
            "modulus_14_variances": [
                _fraction_text(variance(crossing_loads(points, 14)))
                for points in (homometric_left, homometric_right)
            ],
            "diameter_regime_modulus_18": [
                _variance_instance(points, 18)
                for points in (homometric_left, homometric_right)
            ],
        },
        "greedy_mian_chowla_prefix": {
            "conjecture_tested": "Greedy prefix is a valid deterministic Golomb stress case",
            **_variance_instance(greedy, greedy[-1] + 1),
        },
        "random_sidon_rulers": {
            "conjecture_tested": "Exact gap variance handles non-extremal random rulers",
            "seed": RANDOM_SEED,
            "sampling_method": "uniform internal-mark subsets with rejection",
            "mark_count": 6,
            "diameter": 30,
            "attempts": random_attempts,
            "requested_samples": 12,
            "samples": [
                _variance_instance(ruler, 31) for ruler in random_rulers
            ],
        },
        "dominant_central_gap": {
            "conjecture_tested": "A ruler with one dominant central gap is included",
            "dominant_gap_index_one_based": 2,
            **_variance_instance(dominant, 61),
        },
        "near_critical_coordinate_envelope": {
            "conjecture_tested": "A finite ruler satisfies b_k <= C k^2 log(2k)",
            "C": "2",
            "logarithm": "natural",
            **_variance_instance(near_critical, 26),
            "coordinate_checks": envelope_checks,
        },
        "singer_bose_chowla": {
            "status": "not_run",
            "reason": (
                "No validated Singer/Bose-Chowla construction code is present in "
                "the canonical handoff; the protocol makes this case conditional on "
                "reliable construction code, so no unverified implementation is claimed."
            ),
        },
    }


def build_certificate(
    *,
    max_marks: int,
    max_diameter: int,
    modulus_offsets: tuple[int, ...],
    oracle_max_marks: int,
    oracle_max_diameter: int,
) -> dict[str, object]:
    records, totals = _exhaustive_records(
        max_marks,
        max_diameter,
        modulus_offsets,
    )
    oracle_records, mismatch_count, oracle_checks = _oracle_records(
        oracle_max_marks,
        oracle_max_diameter,
        modulus_offsets,
    )
    if mismatch_count:
        raise AssertionError(f"independent oracle found {mismatch_count} mismatches")

    directory = Path(__file__).resolve().parent
    source_files = {
        "certificate_script": Path(__file__).resolve(),
        "extended_verifier": directory / "endpoint_variance.py",
        "tests": directory / "test_golomb_variance.py",
    }
    payload: dict[str, object] = {
        "schema": "erdos1191-target-d-golomb-variance-certificate-v1",
        "certificate_date": CERTIFICATE_DATE,
        "evidence_label": "[PROJECT-INTERNAL EXACT FINITE THEOREM]",
        "claim_scope": (
            "Exact finite exhaustive minima only; no asymptotic Sidon bound and "
            "no resolution of Erdos Problem #1191 is claimed."
        ),
        "conjecture_tested": (
            "For fixed m,D,N with D<N, minimize the exact diameter-regime "
            "endpoint variance over normalized Golomb rulers."
        ),
        "engine": {
            "python_implementation": platform.python_implementation(),
            "python_version": platform.python_version(),
            "primary_enumeration": (
                "all C(D-1,m-2) internal-mark subsets, lexicographic, then all "
                "positive differences checked for uniqueness"
            ),
            "primary_variance": "Fraction-valued diameter gap-moment formula",
            "independent_oracle_enumeration": (
                "recursive positive gap compositions, distinct contiguous sums"
            ),
            "independent_oracle_variance": (
                "direct translated half-open block membership at every offset"
            ),
            "source_sha256": {
                name: _sha256(path) for name, path in source_files.items()
            },
            "source_paths": {
                name: path.name for name, path in source_files.items()
            },
        },
        "completeness": {
            "mark_count_range_inclusive": [2, max_marks],
            "diameter_rule": f"m-1 <= D <= {max_diameter}",
            "modulus_offsets_N_minus_D": list(modulus_offsets),
            "normalization": "first mark 0 and final mark D",
            "orientation_policy": (
                "both orientations enumerated; reflection quotient reported only "
                "after exhaustive filtering"
            ),
            "search_denominator_per_case": "binomial(D-1,m-2)",
            "totals": totals,
        },
        "exhaustive_cases": records,
        "oracle": {
            "mark_count_range_inclusive": [2, oracle_max_marks],
            "diameter_rule": f"m-1 <= D <= {oracle_max_diameter}",
            "exact_checks": oracle_checks,
            "mismatch_count": mismatch_count,
            "cases": oracle_records,
        },
        "mandatory_instances": _mandatory_instances(),
        "limitations": [
            "Finite minima do not imply a uniform asymptotic strengthening.",
            "A stronger one-prefix lower bound still lacks the required cross-prefix upper budget.",
            "Singer/Bose-Chowla cases were not synthesized without validated construction code.",
        ],
    }
    canonical = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode()
    payload["certificate_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def _parse_offsets(raw: str) -> tuple[int, ...]:
    offsets = tuple(int(value) for value in raw.split(",") if value)
    if not offsets or any(offset < 1 for offset in offsets):
        raise argparse.ArgumentTypeError("offsets must be comma-separated positive integers")
    if len(set(offsets)) != len(offsets):
        raise argparse.ArgumentTypeError("offsets must be distinct")
    return offsets


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(DEFAULT_OUTPUT))
    parser.add_argument("--max-marks", type=int, default=7)
    parser.add_argument("--max-diameter", type=int, default=25)
    parser.add_argument("--modulus-offsets", type=_parse_offsets, default=(1, 2, 3))
    parser.add_argument("--oracle-max-marks", type=int, default=5)
    parser.add_argument("--oracle-max-diameter", type=int, default=12)
    arguments = parser.parse_args()
    if arguments.max_marks < 2 or arguments.max_diameter < 1:
        parser.error("primary bounds must be positive and max-marks must be at least 2")
    if arguments.oracle_max_marks < 2 or arguments.oracle_max_diameter < 1:
        parser.error("oracle bounds must be positive and max-marks must be at least 2")

    payload = build_certificate(
        max_marks=arguments.max_marks,
        max_diameter=arguments.max_diameter,
        modulus_offsets=arguments.modulus_offsets,
        oracle_max_marks=arguments.oracle_max_marks,
        oracle_max_diameter=arguments.oracle_max_diameter,
    )
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    )
    totals = payload["completeness"]["totals"]
    print(
        json.dumps(
            {
                "output": str(arguments.output),
                "certificate_sha256": payload["certificate_sha256"],
                "parameter_pairs": totals["parameter_pairs"],
                "candidate_internal_mark_subsets": totals[
                    "candidate_internal_mark_subsets"
                ],
                "golomb_rulers_oriented": totals["golomb_rulers_oriented"],
                "exact_variance_evaluations": totals["exact_variance_evaluations"],
                "oracle_exact_checks": payload["oracle"]["exact_checks"],
                "oracle_mismatches": payload["oracle"]["mismatch_count"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
