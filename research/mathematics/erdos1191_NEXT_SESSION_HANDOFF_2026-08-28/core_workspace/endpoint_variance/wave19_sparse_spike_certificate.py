"""Exact finite certificate for the Wave 19 sparse-spike witnesses.

All point, difference, separation, and prefix-cap decisions are integer or
``fractions.Fraction`` checks.  The descendant-jump functional contains
transcendental logarithms; it is therefore reported as a high-precision
``Decimal`` projection and is never used to decide Golomb uniqueness or a
prefix cap.

The finite 255/256-mark continuations are exact witnesses after replay, but
their greedy discovery is not a globally exhaustive search and proves no
infinite extension or asymptotic claim.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from dataclasses import asdict
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import cache
from hashlib import sha256
from itertools import pairwise
from math import comb
from pathlib import Path
from typing import Any

DIRECTORY = Path(__file__).resolve().parent
DEFAULT_OUTPUT = DIRECTORY / "wave19_sparse_spike_certificate_2026-08-29.json"
DECIMAL_PRECISION = 80
ENVELOPE_CONSTANT = 32
CAP_MULTIPLIER = 2 * ENVELOPE_CONSTANT

A32 = (
    0,
    15,
    32,
    44,
    58,
    74,
    85,
    200,
    202,
    205,
    223,
    224,
    233,
    269,
    273,
    1418,
    1425,
    1431,
    1479,
    1514,
    1534,
    1571,
    1657,
    1696,
    1790,
    1798,
    1850,
    1912,
    1984,
    2047,
    2072,
    7096,
)

ET_PRIME = 173
ET_QUADRATIC_COEFFICIENT = 63
ET_SCALE = 7
ET_COUNT = 95
ET95 = tuple(
    ET_SCALE
    * (2 * ET_PRIME * index + (ET_QUADRATIC_COEFFICIENT * index * index) % ET_PRIME)
    for index in range(ET_COUNT)
)
ET95_WIDTH = 228557
TRANSLATION = 235654
SEPARATED_UNION = A32 + tuple(TRANSLATION + point for point in ET95)
PRIMARY_TERMINAL = 5087721
RESERVE_TERMINAL = 1271930
PRIMARY_WITNESS = SEPARATED_UNION + (PRIMARY_TERMINAL,)
RESERVE_WITNESS = SEPARATED_UNION + (RESERVE_TERMINAL,)

REPORTED_PRIMARY_J = {
    4: 0.002078576661344486,
    8: 0.06999594179639168,
    16: 0.02824820609231238,
    32: 0.0,
    64: 0.31393714841781556,
}
REPORTED_RESERVE_J64 = 0.06891061854425407


def _require_plain_integer(value: int, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    return value


def _validated_points(points: Sequence[int]) -> tuple[int, ...]:
    marks = tuple(points)
    if len(marks) < 2:
        raise ValueError("at least two points are required")
    if any(isinstance(mark, bool) or not isinstance(mark, int) for mark in marks):
        raise TypeError("points must be integers")
    if any(left >= right for left, right in pairwise(marks)):
        raise ValueError("points must be strictly increasing")
    return marks


def csv_sha256(values: Sequence[int]) -> str:
    """SHA-256 of comma-separated base-ten integers, with no final newline."""
    if any(isinstance(value, bool) or not isinstance(value, int) for value in values):
        raise TypeError("CSV hash values must be integers")
    return sha256(",".join(map(str, values)).encode("ascii")).hexdigest()


def positive_differences(points: Sequence[int]) -> tuple[int, ...]:
    """Return every positive pair difference, sorted and retaining collisions."""
    marks = _validated_points(points)
    return tuple(
        sorted(
            marks[right] - marks[left]
            for right in range(1, len(marks))
            for left in range(right)
        )
    )


def _atanh_log_interval(value: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    """Rational enclosure for log(value), for 1 <= value <= 2."""
    if not isinstance(value, Fraction):
        raise TypeError("value must be a Fraction")
    if not Fraction(1) <= value <= Fraction(2):
        raise ValueError("value must lie in [1, 2]")
    terms = _require_plain_integer(terms, "terms")
    if terms < 1:
        raise ValueError("terms must be positive")
    z = (value - 1) / (value + 1)
    if z == 0:
        return Fraction(), Fraction()
    z_squared = z * z
    power = z
    partial = Fraction()
    for index in range(terms):
        partial += power / (2 * index + 1)
        power *= z_squared
    lower = 2 * partial
    first_tail_power = z ** (2 * terms + 1)
    tail_upper = 2 * first_tail_power / ((2 * terms + 1) * (1 - z_squared))
    return lower, lower + tail_upper


@cache
def _log_integer_interval(value: int, terms: int) -> tuple[Fraction, Fraction]:
    """Rational enclosure for natural log(value) using binary range reduction."""
    value = _require_plain_integer(value, "value")
    if value < 2:
        raise ValueError("value must be at least two")
    terms = _require_plain_integer(terms, "terms")
    power = value.bit_length() - 1
    reduced = Fraction(value, 1 << power)
    log_two_lower, log_two_upper = _atanh_log_interval(Fraction(2), terms)
    reduced_lower, reduced_upper = _atanh_log_interval(reduced, terms)
    return (
        power * log_two_lower + reduced_lower,
        power * log_two_upper + reduced_upper,
    )


def critical_cap_audit(mark_count: int) -> dict[str, Any]:
    """Certify floor(64*m^2*log(m)) with exact rational bounds."""
    mark_count = _require_plain_integer(mark_count, "mark_count")
    if mark_count < 2:
        raise ValueError("mark_count must be at least two")
    selected: tuple[int, Fraction, Fraction, int, int] | None = None
    for terms in (12, 16, 24, 32, 48, 64, 96, 128):
        log_lower, log_upper = _log_integer_interval(mark_count, terms)
        scale = CAP_MULTIPLIER * mark_count * mark_count
        lower = scale * log_lower
        upper = scale * log_upper
        lower_floor = lower.numerator // lower.denominator
        upper_floor = upper.numerator // upper.denominator
        if lower_floor == upper_floor:
            selected = (terms, lower, upper, lower_floor, upper_floor)
            break
    if selected is None:
        raise ArithmeticError("rational logarithm enclosure did not determine the cap")
    terms, lower, upper, lower_floor, upper_floor = selected
    return {
        "mark_count": mark_count,
        "envelope_constant": ENVELOPE_CONSTANT,
        "cap_multiplier": CAP_MULTIPLIER,
        "series_terms": terms,
        "lower_bound": f"{lower.numerator}/{lower.denominator}",
        "upper_bound": f"{upper.numerator}/{upper.denominator}",
        "lower_floor": lower_floor,
        "upper_floor": upper_floor,
        "certified_cap": lower_floor,
        "floor_uniquely_certified": lower_floor == upper_floor,
        "arithmetic": "exact fractions.Fraction enclosure",
    }


@cache
def critical_cap(mark_count: int) -> int:
    return int(critical_cap_audit(mark_count)["certified_cap"])


def prefix_cap_audit(points: Sequence[int]) -> tuple[dict[str, Any], ...]:
    """Audit a_(m-1)+1 <= floor(64*m^2*log(m)) for every m >= 2."""
    marks = _validated_points(points)
    rows: list[dict[str, Any]] = []
    for mark_count in range(2, len(marks) + 1):
        cap = critical_cap(mark_count)
        terminal_plus_one = marks[mark_count - 1] + 1
        rows.append(
            {
                "mark_count": mark_count,
                "terminal": marks[mark_count - 1],
                "terminal_plus_one": terminal_plus_one,
                "certified_cap": cap,
                "integer_slack": cap - terminal_plus_one,
                "passes": terminal_plus_one <= cap,
            }
        )
    return tuple(rows)


def _fraction_decimal(value: Fraction) -> Decimal:
    return Decimal(value.numerator) / Decimal(value.denominator)


def _beta(epoch: int, source: int, target: int) -> Fraction:
    denominator = epoch * epoch
    if source == target:
        return Fraction(1, denominator)
    if source == target - 1:
        return Fraction(1, 4 * denominator)
    return Fraction(1, 2 * denominator)


def _residual(epoch: int, source: int) -> Fraction:
    return Fraction(4 * epoch - 2 * source - 3, 8 * epoch * epoch)


def descendant_jump_value(
    points: Sequence[int],
    epoch: int,
    h: Fraction = Fraction(5, 2),
    *,
    precision: int = DECIMAL_PRECISION,
) -> Decimal:
    """Project the exact Wave 18 J_n^(h) indexing at Decimal precision."""
    marks = _validated_points(points)
    epoch = _require_plain_integer(epoch, "epoch")
    if epoch < 3:
        raise ValueError("epoch must be at least three")
    if 2 * epoch > len(marks):
        raise ValueError("points do not contain the required 2*epoch prefix")
    if not isinstance(h, Fraction):
        raise TypeError("h must be a Fraction")
    if h <= 0:
        raise ValueError("h must be positive")
    precision = _require_plain_integer(precision, "precision")
    if precision < 20:
        raise ValueError("precision must be at least 20")

    with localcontext() as context:
        context.prec = precision
        exponential = _fraction_decimal(h).exp()
        atom_count = Decimal((epoch - 1) * (3 * epoch - 4)) / Decimal(2)
        total = Decimal()
        for source in range(2, epoch + 1):
            residual = _residual(epoch, source)
            weights = tuple(
                _beta(epoch, source, target) for target in range(epoch, 2 * epoch - 1)
            )
            source_mass = sum(weights, Fraction())
            suffix = marks[2 * epoch - 1] - marks[source - 1]
            rank_floor = comb(2 * epoch - source + 1, 2)
            row = Decimal()
            for target, weight in zip(range(epoch, 2 * epoch - 1), weights):
                descendant = marks[target] - marks[source - 1]
                ratio = (
                    Decimal(suffix)
                    * atom_count
                    / (exponential * Decimal(rank_floor) * Decimal(descendant))
                )
                if ratio > 1:
                    row += _fraction_decimal(weight) * ratio.ln()
            total += _fraction_decimal(residual / source_mass) * row
        return +total


def _descendant_active_term_count(
    points: Sequence[int], epoch: int, h: Fraction = Fraction(5, 2)
) -> int:
    marks = _validated_points(points)
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        exponential = _fraction_decimal(h).exp()
        atom_count = Decimal((epoch - 1) * (3 * epoch - 4)) / Decimal(2)
        count = 0
        for source in range(2, epoch + 1):
            suffix = marks[2 * epoch - 1] - marks[source - 1]
            rank_floor = comb(2 * epoch - source + 1, 2)
            for target in range(epoch, 2 * epoch - 1):
                descendant = marks[target] - marks[source - 1]
                ratio = (
                    Decimal(suffix)
                    * atom_count
                    / (exponential * Decimal(rank_floor) * Decimal(descendant))
                )
                count += ratio > 1
        return count


def descendant_jump_audit(
    points: Sequence[int], epoch: int, reported_binary64: float
) -> dict[str, Any]:
    if isinstance(reported_binary64, bool) or not isinstance(
        reported_binary64, (int, float)
    ):
        raise TypeError("reported_binary64 must be numeric")
    row = descendant_jump_projection_audit(points, epoch)
    projected_binary64 = row["projected_binary64"]
    error = abs(projected_binary64 - float(reported_binary64))
    return {
        **row,
        "reported_binary64": float(reported_binary64),
        "absolute_binary64_error": error,
        "match_tolerance": 1e-15,
        "reported_value_matches_projection": error < 1e-15,
    }


def descendant_jump_projection_audit(
    points: Sequence[int], epoch: int
) -> dict[str, Any]:
    projected = descendant_jump_value(points, epoch)
    return {
        "epoch": epoch,
        "h": "5/2",
        "decimal_precision": DECIMAL_PRECISION,
        "projected_decimal": format(projected, "f"),
        "projected_binary64": float(projected),
        "active_log_plus_term_count": _descendant_active_term_count(points, epoch),
        "transcendental_projection_only": True,
    }


@cache
def separated_union_audit() -> dict[str, Any]:
    root_differences = positive_differences(A32)
    block_differences = positive_differences(ET95)
    cross_differences = tuple(
        sorted(TRANSLATION + block - root for root in A32 for block in ET95)
    )
    all_differences = positive_differences(SEPARATED_UNION)
    root_set = set(root_differences)
    block_set = set(block_differences)
    cross_set = set(cross_differences)
    checks = {
        "translation_is_width_separating": TRANSLATION == A32[-1] + ET95[-1] + 1,
        "root_internal_unique": len(root_set) == comb(len(A32), 2),
        "block_internal_unique": len(block_set) == comb(len(ET95), 2),
        "internal_spectra_disjoint": root_set.isdisjoint(block_set),
        "cross_differences_unique": len(cross_set) == len(A32) * len(ET95),
        "cross_above_internal_spectra": min(cross_set) > max(root_set | block_set),
        "partition_reconstructs_all_differences": sorted(
            root_differences + block_differences + cross_differences
        )
        == list(all_differences),
        "union_is_golomb": len(set(all_differences)) == comb(127, 2),
    }
    return {
        "root_internal_count": len(root_differences),
        "block_internal_count": len(block_differences),
        "cross_count": len(cross_differences),
        "total_difference_count": len(all_differences),
        "distinct_difference_count": len(set(all_differences)),
        "largest_internal_difference": max(root_set | block_set),
        "smallest_cross_difference": min(cross_set),
        "difference_sha256": csv_sha256(all_differences),
        **checks,
        "all_partition_checks_pass": all(checks.values()),
    }


def _witness_audit(
    points: Sequence[int], *, include_all_differences: bool
) -> dict[str, Any]:
    marks = _validated_points(points)
    differences = positive_differences(marks)
    cap_rows = prefix_cap_audit(marks)
    result: dict[str, Any] = {
        "points": list(marks),
        "point_count": len(marks),
        "terminal": marks[-1],
        "marks_csv_sha256": csv_sha256(marks),
        "difference_count": len(differences),
        "expected_difference_count": comb(len(marks), 2),
        "distinct_difference_count": len(set(differences)),
        "difference_csv_sha256": csv_sha256(differences),
        "is_golomb": len(set(differences)) == comb(len(marks), 2),
        "all_prefix_cap_rows": list(cap_rows),
        "all_prefix_caps_pass": all(row["passes"] for row in cap_rows),
    }
    if include_all_differences:
        result["all_positive_differences"] = list(differences)
    return result


def _extension_audit(result: Any) -> dict[str, Any]:
    points = result.points
    differences_255 = positive_differences(points[:255])
    differences_256 = positive_differences(points)
    cap_rows = prefix_cap_audit(points)
    return {
        "points": list(points),
        "point_count": len(points),
        "terminal_255": points[254],
        "terminal_256": points[255],
        "marks_255_csv_sha256": csv_sha256(points[:255]),
        "marks_256_csv_sha256": csv_sha256(points),
        "difference_255_count": len(differences_255),
        "difference_255_distinct_count": len(set(differences_255)),
        "difference_255_csv_sha256": csv_sha256(differences_255),
        "difference_256_count": len(differences_256),
        "difference_256_distinct_count": len(set(differences_256)),
        "difference_256_csv_sha256": csv_sha256(differences_256),
        "all_prefix_caps_pass": all(row["passes"] for row in cap_rows),
        "prefix_cap_rows_128_through_256": list(cap_rows[126:]),
        "stage_candidate_counts": list(result.stage_candidate_counts),
        "total_candidates_tested": result.total_candidates_tested,
        "maximum_stage_candidate_count": max(result.stage_candidate_counts),
        "maximum_stage_mark_count": result.stage_candidate_counts.index(
            max(result.stage_candidate_counts)
        )
        + 129,
        "completed": result.completed,
        "global_search_exhaustive": result.global_search_exhaustive,
        "each_step_first_legal_is_exhaustive": (
            result.each_step_first_legal_is_exhaustive
        ),
        "scope": result.scope,
        "exact_255_witness_verified": len(set(differences_255)) == comb(255, 2),
        "exact_256_witness_verified": len(set(differences_256)) == comb(256, 2),
    }


def _maximized_terminal_audit(result: Any, *, jump_epoch: int) -> dict[str, Any]:
    points = result.points
    differences = positive_differences(points)
    cap_rows = prefix_cap_audit(points)
    payload = asdict(result)
    payload["points"] = list(points)
    payload.update(
        {
            "marks_csv_sha256": csv_sha256(points),
            "difference_count": len(differences),
            "expected_difference_count": comb(len(points), 2),
            "distinct_difference_count": len(set(differences)),
            "difference_csv_sha256": csv_sha256(differences),
            "all_prefix_caps_pass": all(row["passes"] for row in cap_rows),
            "terminal_prefix_cap_row": cap_rows[-1],
            "descendant_jump": descendant_jump_projection_audit(points, jump_epoch),
            "fixed_witness_exactly_verified": len(set(differences))
            == comb(len(points), 2),
        }
    )
    return payload


def _cooldown_audit(result: Any) -> dict[str, Any]:
    points = result.points
    differences = positive_differences(points)
    cap_rows = prefix_cap_audit(points)
    return {
        "points": list(points),
        "point_count": len(points),
        "terminal": points[-1],
        "marks_csv_sha256": csv_sha256(points),
        "difference_count": len(differences),
        "expected_difference_count": comb(len(points), 2),
        "distinct_difference_count": len(set(differences)),
        "difference_csv_sha256": csv_sha256(differences),
        "all_prefix_caps_pass": all(row["passes"] for row in cap_rows),
        "prefix_cap_rows_256_through_511": list(cap_rows[254:]),
        "stage_candidate_counts": list(result.stage_candidate_counts),
        "total_candidates_tested": result.total_candidates_tested,
        "maximum_stage_candidate_count": max(result.stage_candidate_counts),
        "maximum_stage_mark_count": result.stage_candidate_counts.index(
            max(result.stage_candidate_counts)
        )
        + 257,
        "completed": result.completed,
        "global_search_exhaustive": result.global_search_exhaustive,
        "each_step_first_legal_is_exhaustive": (
            result.each_step_first_legal_is_exhaustive
        ),
        "scope": result.scope,
        "fixed_511_witness_exactly_verified": len(set(differences)) == comb(511, 2),
    }


@cache
def build_certificate() -> dict[str, Any]:
    """Build the deterministic, self-hashed certificate."""
    import wave19_sparse_spike_search as search

    union_audit = separated_union_audit()
    primary = _witness_audit(PRIMARY_WITNESS, include_all_differences=True)
    reserve = _witness_audit(RESERVE_WITNESS, include_all_differences=True)
    primary_j = [
        descendant_jump_audit(PRIMARY_WITNESS, epoch, reported)
        for epoch, reported in REPORTED_PRIMARY_J.items()
    ]
    reserve_j = descendant_jump_audit(RESERVE_WITNESS, 64, REPORTED_RESERVE_J64)
    primary_scan = search.exhaustive_next_mark_scan(PRIMARY_WITNESS)
    reserve_scan = search.exhaustive_next_mark_scan(RESERVE_WITNESS)
    primary_greedy = search.greedy_extend(PRIMARY_WITNESS, 256)
    reserve_greedy = search.greedy_extend(RESERVE_WITNESS, 256)
    primary_extension = _extension_audit(primary_greedy)
    reserve_extension = _extension_audit(reserve_greedy)
    primary_maximum_result = search.maximize_next_terminal(primary_greedy.points[:255])
    reserve_maximum_result = search.maximize_next_terminal(reserve_greedy.points[:255])
    primary_maximum = _maximized_terminal_audit(primary_maximum_result, jump_epoch=128)
    reserve_maximum = _maximized_terminal_audit(reserve_maximum_result, jump_epoch=128)
    cooldown_result = search.greedy_extend(reserve_maximum_result.points, 511)
    cooldown = _cooldown_audit(cooldown_result)
    maximum_512_result = search.maximize_next_terminal(cooldown_result.points)
    maximum_512 = _maximized_terminal_audit(maximum_512_result, jump_epoch=256)

    exact_checks = {
        "root_is_golomb": len(set(positive_differences(A32))) == comb(32, 2),
        "scaled_et_block_is_golomb": len(set(positive_differences(ET95)))
        == comb(95, 2),
        "separated_union_partition_verified": union_audit["all_partition_checks_pass"],
        "primary_128_is_golomb": primary["is_golomb"],
        "primary_128_all_prefix_caps_pass": primary["all_prefix_caps_pass"],
        "reserve_128_is_golomb": reserve["is_golomb"],
        "reserve_128_all_prefix_caps_pass": reserve["all_prefix_caps_pass"],
        "reserve_next_prefix_slack_is_3903885": critical_cap(129)
        - (RESERVE_TERMINAL + 1)
        == 3903885,
        "primary_one_step_scan_exhaustive": primary_scan.exhaustive_for_fixed_prefix_and_cap,
        "reserve_one_step_scan_exhaustive": reserve_scan.exhaustive_for_fixed_prefix_and_cap,
        "primary_255_and_256_exact": primary_extension["exact_255_witness_verified"]
        and primary_extension["exact_256_witness_verified"]
        and primary_extension["all_prefix_caps_pass"],
        "reserve_255_and_256_exact": reserve_extension["exact_255_witness_verified"]
        and reserve_extension["exact_256_witness_verified"]
        and reserve_extension["all_prefix_caps_pass"],
        "primary_stage_256_cap_maximum_exact": primary_maximum[
            "fixed_witness_exactly_verified"
        ]
        and primary_maximum["all_prefix_caps_pass"]
        and primary_maximum["cap_maximum_selected"]
        and primary_maximum["selection_exhaustive_for_maximum"],
        "reserve_stage_256_cap_maximum_exact": reserve_maximum[
            "fixed_witness_exactly_verified"
        ]
        and reserve_maximum["all_prefix_caps_pass"]
        and reserve_maximum["cap_maximum_selected"]
        and reserve_maximum["selection_exhaustive_for_maximum"],
        "reserve_cooldown_511_exact": cooldown["completed"]
        and cooldown["fixed_511_witness_exactly_verified"]
        and cooldown["all_prefix_caps_pass"],
        "stage_512_cap_maximum_exact": maximum_512["fixed_witness_exactly_verified"]
        and maximum_512["all_prefix_caps_pass"]
        and maximum_512["cap_maximum_selected"]
        and maximum_512["selection_exhaustive_for_maximum"],
    }
    projection_checks = {
        "all_reported_primary_J_values_match": all(
            row["reported_value_matches_projection"] for row in primary_j
        ),
        "reported_reserve_J64_matches": reserve_j["reported_value_matches_projection"],
    }

    payload: dict[str, Any] = {
        "schema": "erdos1191.wave19.sparse-spike.v1",
        "research_date": "2026-08-29",
        "purpose": (
            "Independently replay the sparse-spike 32+95+1 construction, "
            "its reserve terminal, and deterministic finite continuations."
        ),
        "arithmetic": {
            "points_differences_and_separation": "exact integers",
            "prefix_cap": (
                "exact Fraction lower/upper enclosures certify floor(64*m^2*log(m))"
            ),
            "descendant_jump_J": (
                "Decimal precision 80 projection of transcendental logs; "
                "not used in combinatorial decisions"
            ),
            "marks_and_difference_hash": (
                "SHA-256 of comma-separated base-ten integers without newline"
            ),
        },
        "construction": {
            "root_32": list(A32),
            "et_parameters": {
                "prime": ET_PRIME,
                "quadratic_coefficient": ET_QUADRATIC_COEFFICIENT,
                "scale": ET_SCALE,
                "retained_mark_count": ET_COUNT,
                "formula": "7*(346*j + ((63*j*j) mod 173)), 0<=j<95",
            },
            "scaled_et_95": list(ET95),
            "scaled_et_width": ET95_WIDTH,
            "translation": TRANSLATION,
            "separated_union": list(SEPARATED_UNION),
            "primary_terminal": PRIMARY_TERMINAL,
            "reserve_terminal": RESERVE_TERMINAL,
        },
        "separated_union_audit": union_audit,
        "primary_128_audit": primary,
        "reserve_128_audit": reserve,
        "primary_descendant_jump_rows": primary_j,
        "reserve_descendant_jump_row": reserve_j,
        "reserve_first_next_prefix": {
            "mark_count": 129,
            "certified_cap": critical_cap(129),
            "largest_legal_terminal": critical_cap(129) - 1,
            "terminal_plus_one": RESERVE_TERMINAL + 1,
            "integer_slack": critical_cap(129) - (RESERVE_TERMINAL + 1),
        },
        "one_step_exhaustive_discriminators": {
            "primary": asdict(primary_scan),
            "reserve": asdict(reserve_scan),
            "logical_scope": (
                "Exhaustive only for one appended mark over the complete "
                "C=32 legal integer domain of each fixed 128-mark prefix."
            ),
        },
        "deterministic_greedy_extensions": {
            "primary": primary_extension,
            "reserve": reserve_extension,
            "search_scope": (
                "The first legal mark is selected after a complete ascending "
                "scan at each fixed prefix. Alternative branches are not "
                "explored, so the global search is not exhaustive or optimal."
            ),
        },
        "stage_256_terminal_maximization": {
            "primary": primary_maximum,
            "reserve": reserve_maximum,
            "selection_scope": (
                "For each fixed 255-mark core, the C=32 cap maximum itself "
                "lies above max(A)+max(Delta(A)); maximality is exhaustive. "
                "The lower candidate domain was not classified because no "
                "lower candidate can improve the cap maximum."
            ),
        },
        "preferred_256_for_cooldown": {
            "label": "reserve",
            "criterion": "larger Decimal-80 J_128^(5/2) projection",
            "primary_J128_decimal": primary_maximum["descendant_jump"][
                "projected_decimal"
            ],
            "reserve_J128_decimal": reserve_maximum["descendant_jump"][
                "projected_decimal"
            ],
            "choice_is_transcendental_projection_only": True,
        },
        "reserve_256_to_511_cooldown": {
            **cooldown,
            "search_scope": (
                "Deterministic first-legal continuation. Each local chosen "
                "mark is minimal for its fixed prefix, but alternative "
                "branches were not explored."
            ),
        },
        "stage_512_terminal_maximization": {
            **maximum_512,
            "selection_scope": (
                "For the fixed 511-mark cooldown core, the C=32 cap maximum "
                "exceeds max(A)+max(Delta(A)); terminal maximality is exact, "
                "while the preceding cooldown branch is heuristic."
            ),
        },
        "exact_checks": exact_checks,
        "projection_checks": projection_checks,
        "scope_flags": {
            "finite_witnesses_exactly_verified": True,
            "one_step_scan_exhaustive_for_each_fixed_prefix": True,
            "greedy_extension_global_search_exhaustive": False,
            "greedy_255_and_256_witnesses_exactly_verified": True,
            "stage_256_terminal_maximization_exhaustive": True,
            "cooldown_to_511_global_search_exhaustive": False,
            "stage_512_terminal_maximization_exhaustive": True,
            "optimized_512_witness_exactly_verified": True,
            "optimality_claimed": False,
            "infinite_extension_claimed": False,
            "p23_refuted": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "erdos_1191_resolved": False,
        },
        "all_required_checks_pass": all(exact_checks.values())
        and all(projection_checks.values()),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )
    payload["certificate_sha256"] = sha256(canonical).hexdigest()
    return payload


def write_certificate(path: Path = DEFAULT_OUTPUT) -> dict[str, Any]:
    payload = build_certificate()
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    arguments = parser.parse_args()
    payload = write_certificate(arguments.output)
    print(
        json.dumps(
            {
                "output": str(arguments.output),
                "certificate_sha256": payload["certificate_sha256"],
                "all_required_checks_pass": payload["all_required_checks_pass"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
