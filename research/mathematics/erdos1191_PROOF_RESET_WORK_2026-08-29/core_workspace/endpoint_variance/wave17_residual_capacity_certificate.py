"""Deterministic finite/algebra audit of the Wave 17 residual-capacity lemma.

The accompanying analytic derivation proves the following local statement.
For the Wave 15 promotion ``Delta_m`` and the Wave 11 interior triangular
floor,

``B_(2m) >= K_(2m)^int + c_0 Delta_m - E_m``,

where ``c_0 = log(3/2)/12`` and
``E_m = 2146 log(3/2)/(16 m^2)``.  The proof uses only three inputs:

* ten layers of near differences in any consecutive Golomb interval;
* the exact coefficient classes of a literal next-Gothic-bulk atom; and
* the exact rational Wave 15 layer-load upper bound ``3/(4m^2)``.

This module checks the integer and rational parts of that derivation and
audits its atom ownership on finite Hall and Erdos--Turan fixtures.  Decimal
logarithms are 80-digit display projections only.  The certificate does not
construct an infinite branch or prove P19 or either Erdos question.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import cache
from hashlib import sha256
from pathlib import Path
from typing import Any

from complete_birth_ledger import erdos_turan_ruler
from wave6_hall_candidate_probe import COUNTEREXAMPLE_64_POINTS

DIRECTORY = Path(__file__).resolve().parent
DEFAULT_OUTPUT = DIRECTORY / "wave17_residual_capacity_certificate_2026-08-29.json"

NEAR_DEPTH = 10
LONG_INTERVAL_MARK_THRESHOLD = 55
LARGE_DIFFERENCE_CUTOFF = 2147
SMALL_DIFFERENCE_COUNT = LARGE_DIFFERENCE_CUTOFF - 1
DECIMAL_PRECISION = 80


def _canonical_hash(payload: dict[str, Any]) -> str:
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return sha256(canonical.encode("utf-8")).hexdigest()


def _points_sha256(points: Sequence[int]) -> str:
    encoded = ",".join(str(point) for point in points).encode("ascii")
    return sha256(encoded).hexdigest()


def _fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def _decimal_text(value: Decimal) -> str:
    return format(value, ".70g")


def _require_plain_integer(value: int, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    return value


def triangular_floor(separation: int) -> int:
    """Return ``binom(separation+1, 2)`` for a positive gap length."""
    separation = _require_plain_integer(separation, "separation")
    if separation < 1:
        raise ValueError("separation must be positive")
    return separation * (separation + 1) // 2


def near_difference_count(mark_count: int, depth: int = NEAR_DEPTH) -> int:
    """Count pairs whose index separation is at most ``depth``."""
    mark_count = _require_plain_integer(mark_count, "mark_count")
    depth = _require_plain_integer(depth, "depth")
    if depth < 1 or mark_count <= depth:
        raise ValueError("require 1 <= depth < mark_count")
    return depth * mark_count - depth * (depth + 1) // 2


def near_difference_diameter_lower(
    mark_count: int, depth: int = NEAR_DEPTH
) -> Fraction:
    """Return the exact lower bound ``N(N+1)/(h(h+1))`` for the diameter."""
    count = near_difference_count(mark_count, depth)
    return Fraction(count * (count + 1), depth * (depth + 1))


def threshold_polynomial_twice(mark_count: int) -> int:
    """Return twice the h=10 margin over ``(3/4)n(n-1)``.

    For ``N=10n-55``, this is

    ``2*N*(N+1)-165*n*(n-1) = 35*n^2-2015*n+5940``.
    """
    mark_count = _require_plain_integer(mark_count, "mark_count")
    if mark_count <= NEAR_DEPTH:
        raise ValueError("the ten-layer argument needs at least eleven marks")
    return 35 * mark_count * mark_count - 2015 * mark_count + 5940


def threshold_audit(mark_count: int) -> dict[str, Any]:
    """Audit the exact h=10 diameter comparison at one mark count."""
    count = near_difference_count(mark_count)
    lower = near_difference_diameter_lower(mark_count)
    target = Fraction(3 * mark_count * (mark_count - 1), 4)
    polynomial = threshold_polynomial_twice(mark_count)
    direct_margin = lower - target
    return {
        "mark_count": mark_count,
        "separation": mark_count - 1,
        "near_depth": NEAR_DEPTH,
        "near_difference_count": count,
        "near_difference_count_formula_matches": count == 10 * mark_count - 55,
        "diameter_lower": _fraction_text(lower),
        "three_halves_triangular_target": _fraction_text(target),
        "diameter_margin": _fraction_text(direct_margin),
        "twice_cleared_polynomial_margin": polynomial,
        "polynomial_formula_matches_direct_margin": (
            direct_margin == Fraction(polynomial, 220)
        ),
        "threshold_claim_applies": mark_count >= LONG_INTERVAL_MARK_THRESHOLD,
        "diameter_lower_at_least_three_halves_triangular": lower >= target,
    }


def literal_coefficient(source_epoch: int, separation: int) -> Fraction:
    """Return the selected atom coefficient in ``B_(2m)``."""
    source_epoch = _require_plain_integer(source_epoch, "source_epoch")
    separation = _require_plain_integer(separation, "separation")
    if source_epoch < 4:
        raise ValueError("source_epoch must be at least four")
    if separation < 1:
        raise ValueError("separation must be positive")
    denominator = source_epoch * source_epoch
    if separation == 1:
        return Fraction(1, 4 * denominator)
    if separation == 2:
        return Fraction(1, 16 * denominator)
    return Fraction(1, 8 * denominator)


def layer_load_cap(source_epoch: int) -> Fraction:
    """Return the conservative exact load cap ``3/(4m^2)``."""
    source_epoch = _require_plain_integer(source_epoch, "source_epoch")
    if source_epoch < 4:
        raise ValueError("source_epoch must be at least four")
    return Fraction(3, 4 * source_epoch * source_epoch)


def minimum_residual_log_coefficient(source_epoch: int) -> Fraction:
    """Coefficient of ``log(3/2)`` left after the triangular floor."""
    source_epoch = _require_plain_integer(source_epoch, "source_epoch")
    if source_epoch < 4:
        raise ValueError("source_epoch must be at least four")
    return Fraction(1, 16 * source_epoch * source_epoch)


def small_value_error_log_coefficient(source_epoch: int) -> Fraction:
    """Coefficient of ``log(3/2)`` in the discarded-small-value error."""
    return SMALL_DIFFERENCE_COUNT * minimum_residual_log_coefficient(source_epoch)


def cutoff_ratio_audit(separation: int) -> dict[str, Any]:
    """Audit the cutoff argument for a short interval length."""
    floor = triangular_floor(separation)
    return {
        "separation": separation,
        "triangular_floor": floor,
        "cutoff": LARGE_DIFFERENCE_CUTOFF,
        "twice_cutoff_minus_three_floors": (2 * LARGE_DIFFERENCE_CUTOFF - 3 * floor),
        "cutoff_ratio_at_least_three_halves": (
            2 * LARGE_DIFFERENCE_CUTOFF >= 3 * floor
        ),
    }


def coefficient_class_audit(source_epoch: int, separation: int) -> dict[str, Any]:
    """Audit exact coefficient ownership and the conservative minimum."""
    coefficient = literal_coefficient(source_epoch, separation)
    minimum = minimum_residual_log_coefficient(source_epoch)
    return {
        "source_epoch": source_epoch,
        "separation": separation,
        "coefficient_class": (
            "gap_1" if separation == 1 else "gap_2" if separation == 2 else "gap_ge_3"
        ),
        "literal_coefficient": _fraction_text(coefficient),
        "minimum_coefficient": _fraction_text(minimum),
        "literal_coefficient_dominates_minimum": coefficient >= minimum,
        "twelve_times_minimum_equals_layer_load_cap": (
            12 * minimum == layer_load_cap(source_epoch)
        ),
    }


def _validated_fixture_prefix(points: Sequence[int], epoch: int) -> tuple[int, ...]:
    epoch = _require_plain_integer(epoch, "epoch")
    if epoch < 4:
        raise ValueError("epoch must be at least four")
    required = 4 * epoch - 1
    marks = tuple(points[:required])
    if (
        len(marks) != required
        or marks[0] != 0
        or marks != tuple(sorted(set(marks)))
        or any(isinstance(mark, bool) or not isinstance(mark, int) for mark in marks)
    ):
        raise ValueError("a normalized increasing 4m-1 prefix is required")
    seen: set[int] = set()
    for left in range(required):
        for right in range(left + 1, required):
            difference = marks[right] - marks[left]
            if difference in seen:
                raise ValueError("the supplied prefix is not Golomb")
            seen.add(difference)
    return marks


def _decimal_from_fraction(value: Fraction) -> Decimal:
    return Decimal(value.numerator) / Decimal(value.denominator)


def finite_fixture_audit(
    fixture: str, points: Sequence[int], epoch: int
) -> dict[str, Any]:
    """Independently audit selected atom ownership and rational load caps."""
    marks = _validated_fixture_prefix(points, epoch)
    old_count = 2 * epoch
    full_count = 4 * epoch - 1

    difference_pairs: dict[int, tuple[int, int]] = {}
    for left in range(full_count):
        for right in range(left + 1, full_count):
            difference = marks[right] - marks[left]
            if difference in difference_pairs:
                raise AssertionError("Golomb validation failed")
            difference_pairs[difference] = (left, right)

    old_differences = {
        marks[right] - marks[left]
        for left in range(old_count)
        for right in range(left + 1, old_count)
    }
    new_differences = {
        value: pair for value, pair in difference_pairs.items() if pair[1] >= old_count
    }

    selected_load_uppers: dict[int, Fraction] = {}
    threshold_rows: list[dict[str, Any]] = []
    delta_terms: list[tuple[Fraction, int, int]] = []
    for left in range(2, epoch + 1):
        threshold = marks[2 * epoch - 1] - marks[left - 1]
        weight = Fraction(12 * epoch - 5 - 6 * left, 16 * epoch * epoch)
        old_rank = sum(value <= threshold for value in old_differences)
        eligible = tuple(
            sorted(value for value in new_differences if value <= threshold)
        )
        increment = len(eligible)
        if increment:
            delta_terms.append((weight, old_rank, increment))
        for value in eligible:
            selected_load_uppers[value] = (
                selected_load_uppers.get(value, Fraction()) + weight / old_rank
            )
        threshold_rows.append(
            {
                "left": left,
                "threshold": threshold,
                "weight": _fraction_text(weight),
                "old_rank": old_rank,
                "new_rank_increment": increment,
            }
        )

    cap = layer_load_cap(epoch)
    selected_rows: list[dict[str, Any]] = []
    for value in sorted(selected_load_uppers):
        left_mark, right_mark = new_differences[value]
        separation = right_mark - left_mark
        coefficient = literal_coefficient(epoch, separation)
        floor = triangular_floor(separation)
        is_large = value >= LARGE_DIFFERENCE_CUTOFF
        selected_rows.append(
            {
                "difference": value,
                "left_mark": left_mark,
                "right_mark": right_mark,
                "separation": separation,
                "triangular_floor": floor,
                "literal_coefficient": _fraction_text(coefficient),
                "load_upper": _fraction_text(selected_load_uppers[value]),
                "load_upper_below_cap": selected_load_uppers[value] < cap,
                "left_index_authenticates_gothic_membership": left_mark >= 1,
                "right_index_authenticates_gothic_membership": (
                    old_count <= right_mark <= full_count - 1
                ),
                "triangular_floor_holds": value >= floor,
                "above_cutoff": is_large,
                "large_atom_ratio_at_least_three_halves": (
                    not is_large or 2 * value >= 3 * floor
                ),
                "coefficient_dominates_minimum": (
                    coefficient >= minimum_residual_log_coefficient(epoch)
                ),
            }
        )

    small_rows = [row for row in selected_rows if not row["above_cutoff"]]
    large_rows = [row for row in selected_rows if row["above_cutoff"]]
    coefficient_class_counts = {
        label: sum(
            row["separation"] == separation
            if separation in (1, 2)
            else row["separation"] >= 3
            for row in selected_rows
        )
        for label, separation in (("gap_1", 1), ("gap_2", 2), ("gap_ge_3", 3))
    }
    sample_candidates = selected_rows[:2] + large_rows[:2] + selected_rows[-2:]
    selected_sample = list(
        {row["difference"]: row for row in sample_candidates}.values()
    )

    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        log_three_halves = (Decimal(3) / Decimal(2)).ln()
        c_zero = log_three_halves / Decimal(12)
        delta = sum(
            (
                _decimal_from_fraction(weight)
                * (Decimal(old_rank + increment) / Decimal(old_rank)).ln()
                for weight, old_rank, increment in delta_terms
            ),
            Decimal(0),
        )
        residual = Decimal(0)
        for right in range(2 * epoch, 4 * epoch - 1):
            for left_gap in range(2, right + 1):
                separation = right - left_gap + 1
                value = marks[right] - marks[left_gap - 1]
                floor = triangular_floor(separation)
                coefficient = literal_coefficient(epoch, separation)
                residual += (
                    _decimal_from_fraction(coefficient)
                    * (Decimal(value) / Decimal(floor)).ln()
                )
        error = (
            Decimal(SMALL_DIFFERENCE_COUNT)
            * log_three_halves
            / Decimal(16 * epoch * epoch)
        )
        projected_rhs = c_zero * delta - error

    return {
        "fixture": fixture,
        "epoch": epoch,
        "used_mark_count": len(marks),
        "used_prefix_sha256": _points_sha256(marks),
        "global_golomb_prefix_verified": True,
        "threshold_rows": threshold_rows,
        "selected_atom_count": len(selected_rows),
        "selected_small_atom_count": len(small_rows),
        "selected_large_atom_count": len(large_rows),
        "small_atom_count_at_most_global_cutoff_count": (
            len(small_rows) <= SMALL_DIFFERENCE_COUNT
        ),
        "maximum_exact_load_upper": _fraction_text(
            max(selected_load_uppers.values(), default=Fraction())
        ),
        "conservative_layer_load_cap": _fraction_text(cap),
        "all_load_uppers_below_cap": all(
            row["load_upper_below_cap"] for row in selected_rows
        ),
        "all_selected_atoms_are_literal_next_gothic_atoms": all(
            row["left_index_authenticates_gothic_membership"]
            and row["right_index_authenticates_gothic_membership"]
            for row in selected_rows
        ),
        "all_selected_atoms_satisfy_triangular_floor": all(
            row["triangular_floor_holds"] for row in selected_rows
        ),
        "all_large_atoms_have_three_halves_residual_ratio": all(
            row["large_atom_ratio_at_least_three_halves"] for row in large_rows
        ),
        "all_coefficients_dominate_conservative_minimum": all(
            row["coefficient_dominates_minimum"] for row in selected_rows
        ),
        "coefficient_class_counts": coefficient_class_counts,
        "minimum_large_ratio_cleared_margin": min(
            (2 * row["difference"] - 3 * row["triangular_floor"] for row in large_rows),
            default=None,
        ),
        "selected_atom_rows_sha256": _canonical_hash({"rows": selected_rows}),
        "selected_atom_sample": selected_sample,
        "decimal_projection_precision": DECIMAL_PRECISION,
        "delta_decimal_projection": _decimal_text(delta),
        "full_interior_residual_decimal_projection": _decimal_text(residual),
        "c0_delta_minus_error_decimal_projection": _decimal_text(projected_rhs),
        "projected_local_inequality_holds": residual >= projected_rhs,
        "transcendental_projection_only": True,
    }


@cache
def build_certificate() -> dict[str, Any]:
    """Build the deterministic Wave 17 certificate."""
    hall = tuple(COUNTEREXAMPLE_64_POINTS)
    et = tuple(erdos_turan_ruler(128, 257))
    fixture_specs = (
        ("wave6_hall_counterexample_64", hall, 4),
        ("wave6_hall_counterexample_64", hall, 8),
        ("wave6_hall_counterexample_64", hall, 16),
        ("erdos_turan_128_p257", et, 4),
        ("erdos_turan_128_p257", et, 8),
        ("erdos_turan_128_p257", et, 16),
        ("erdos_turan_128_p257", et, 32),
    )
    threshold_rows = [threshold_audit(n) for n in (54, 55, 56, 64, 128, 512)]
    cutoff_rows = [cutoff_ratio_audit(s) for s in (1, 2, 3, 4, 10, 53)]
    coefficient_rows = [
        coefficient_class_audit(32, separation) for separation in (1, 2, 3, 54)
    ]
    fixture_rows = [
        finite_fixture_audit(fixture, points, epoch)
        for fixture, points, epoch in fixture_specs
    ]

    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        log_three_halves = (Decimal(3) / Decimal(2)).ln()
        c_zero = log_three_halves / Decimal(12)

    payload: dict[str, Any] = {
        "schema": "erdos1191.wave17.residual-capacity.v1",
        "research_date": "2026-08-29",
        "arithmetic": {
            "integer_and_rational_checks": "exact",
            "transcendental_projections": "decimal.Context precision 80; display only",
        },
        "purpose": (
            "Audit the exact finite and algebraic inputs of the conservative "
            "Wave 17 disjoint residual-capacity theorem."
        ),
        "analytic_contract": {
            "near_depth": NEAR_DEPTH,
            "near_difference_count": "N=10n-55",
            "diameter_lower": "x>=N(N+1)/110",
            "cleared_threshold_polynomial": ("2N(N+1)-165n(n-1)=35n^2-2015n+5940"),
            "long_interval_threshold": LONG_INTERVAL_MARK_THRESHOLD,
            "long_interval_ratio": "x/binom(s+1,2)>=3/2 for s=n-1>=54",
            "short_interval_cutoff": LARGE_DIFFERENCE_CUTOFF,
            "small_positive_integer_count": SMALL_DIFFERENCE_COUNT,
            "literal_coefficient_gap_1": "1/(4m^2)",
            "literal_coefficient_gap_2": "1/(16m^2)",
            "literal_coefficient_gap_at_least_3": "1/(8m^2)",
            "minimum_literal_coefficient": "1/(16m^2)",
            "layer_load_cap": "lambda_m(x)<3/(4m^2)",
            "conservative_c0": "log(3/2)/12",
            "small_value_error": "2146 log(3/2)/(16m^2)",
            "conclusion": ("B_(2m)>=K_(2m)^int+c0 Delta_m-2146 log(3/2)/(16m^2)"),
            "logarithm": "natural",
        },
        "decimal_display": {
            "precision": DECIMAL_PRECISION,
            "log_three_halves": _decimal_text(log_three_halves),
            "conservative_c0": _decimal_text(c_zero),
            "projection_only": True,
        },
        "threshold_rows": threshold_rows,
        "short_interval_cutoff_rows": cutoff_rows,
        "coefficient_class_rows": coefficient_rows,
        "fixture_rows": fixture_rows,
        "all_exact_checks_pass": (
            all(
                row["near_difference_count_formula_matches"]
                and row["polynomial_formula_matches_direct_margin"]
                and (
                    not row["threshold_claim_applies"]
                    or row["diameter_lower_at_least_three_halves_triangular"]
                )
                for row in threshold_rows
            )
            and all(row["cutoff_ratio_at_least_three_halves"] for row in cutoff_rows)
            and all(
                row["literal_coefficient_dominates_minimum"]
                and row["twelve_times_minimum_equals_layer_load_cap"]
                for row in coefficient_rows
            )
            and all(
                row["global_golomb_prefix_verified"]
                and row["small_atom_count_at_most_global_cutoff_count"]
                and row["all_load_uppers_below_cap"]
                and row["all_selected_atoms_are_literal_next_gothic_atoms"]
                and row["all_selected_atoms_satisfy_triangular_floor"]
                and row["all_large_atoms_have_three_halves_residual_ratio"]
                and row["all_coefficients_dominate_conservative_minimum"]
                for row in fixture_rows
            )
        ),
        "scope_flags": {
            "certificate_finite_and_algebraic_only": True,
            "local_p21_inequality_proved_analytically_by_accompanying_derivation": True,
            "finite_fixtures_promoted_to_infinite_branch": False,
            "p19_proved": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "erdos_1191_resolved": False,
            "prize_claim_ready": False,
            "problem_unresolved": True,
        },
        "conclusions": [
            "The h=10 near-difference diameter threshold is checked exactly.",
            "The selected next-bulk atoms retain at least 1/(16m^2) times log(3/2) after the triangular floor above the fixed cutoff.",
            "Twelve times that minimum residual coefficient equals the conservative 3/(4m^2) layer-load cap.",
            "At most 2146 small positive integer differences are discarded, producing a dyadically summable error.",
            "The finite fixtures authenticate ownership and rational load bounds but do not prove an infinite branch or P19.",
        ],
    }
    payload["certificate_sha256"] = _canonical_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    arguments = parser.parse_args()
    certificate = build_certificate()
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(certificate["certificate_sha256"])


if __name__ == "__main__":
    main()
