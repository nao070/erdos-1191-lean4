"""Deterministic finite audit for the Wave 16 multiscale rank mechanism.

The analytic helper records the constants in the following conditional
statement.  Let ``d`` be an old difference in a normalized integer Golomb
prefix of ``L`` marks, with ``8d >= L^2``.  For

``M_t = 2^t L, 0 <= t <= floor((log_2 L)/2)``,

put the marks with indices ``M_t,...,2M_t-1`` into half-open bins of width
``d``.  Under the eventual cap and the explicit square-root side condition,
the Cauchy same-bin count is strictly larger than
``d/(64 C log L)`` in every block.  The blocks are disjoint, and global
Golomb uniqueness makes all witnessed differences new and mutually distinct.

The packaged certificate is deliberately finite.  It audits only the block
ranges present in the Hall64 and Erdos--Turan128 fixtures.  Truncated fixture
ranges are labelled as such and are never promoted to an asymptotic branch.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from decimal import Decimal, localcontext
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from typing import Any

from complete_birth_ledger import erdos_turan_ruler
from wave6_hall_candidate_probe import COUNTEREXAMPLE_64_POINTS

DIRECTORY = Path(__file__).resolve().parent
DEFAULT_OUTPUT = DIRECTORY / "wave16_multiscale_future_rank_certificate_2026-08-29.json"
DECIMAL_PRECISION = 80


def _canonical_hash(payload: dict[str, Any]) -> str:
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return sha256(canonical.encode("utf-8")).hexdigest()


def _points_sha256(points: Sequence[int]) -> str:
    encoded = ",".join(str(point) for point in points).encode("ascii")
    return sha256(encoded).hexdigest()


def _fraction(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def _decimal(value: Decimal) -> str:
    return format(value, ".50g")


def _positive_fraction(value: Fraction | int) -> Fraction:
    result = value if isinstance(value, Fraction) else Fraction(value)
    if result <= 0:
        raise ValueError("the cap constant must be positive")
    return result


def _fraction_decimal(value: Fraction) -> Decimal:
    return Decimal(value.numerator) / Decimal(value.denominator)


def theoretical_max_scale(old_mark_count: int) -> int:
    """Return ``floor((log_2 L)/2)`` without floating point arithmetic."""
    if old_mark_count < 2:
        raise ValueError("old_mark_count must be at least two")
    scale = 0
    while 4 ** (scale + 1) <= old_mark_count:
        scale += 1
    return scale


def cap_side_condition(old_mark_count: int, cap_constant: Fraction | int) -> bool:
    """Check ``sqrt(L) >= 128 C log(4 L^(3/2))`` at high precision."""
    if old_mark_count < 2:
        raise ValueError("old_mark_count must be at least two")
    constant = _positive_fraction(cap_constant)
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        length = Decimal(old_mark_count)
        square_root = length.sqrt()
        logarithm = (Decimal(4) * length * square_root).ln()
        return square_root >= Decimal(128) * _fraction_decimal(constant) * logarithm


def theoretical_single_block_lower(
    old_mark_count: int, old_difference: int, cap_constant: Fraction | int
) -> Decimal:
    """Return the claimed strict per-block lower ``d/(64 C log L)``."""
    if old_mark_count < 2 or old_difference <= 0:
        raise ValueError("L must be at least two and d must be positive")
    constant = _positive_fraction(cap_constant)
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        return Decimal(old_difference) / (
            Decimal(64) * _fraction_decimal(constant) * Decimal(old_mark_count).ln()
        )


def theoretical_total_lower(
    old_difference: int, cap_constant: Fraction | int
) -> Decimal:
    """Return the claimed strict total lower ``d/(128 C log 2)``."""
    if old_difference <= 0:
        raise ValueError("d must be positive")
    constant = _positive_fraction(cap_constant)
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        return Decimal(old_difference) / (
            Decimal(128) * _fraction_decimal(constant) * Decimal(2).ln()
        )


def theoretical_inequality_audit(
    old_mark_count: int,
    old_difference: int,
    cap_constant: Fraction | int = Fraction(1),
) -> dict[str, Any]:
    """Audit every numerical implication in the Wave 16 constant chain.

    This function does not assert that a Golomb branch satisfying the cap
    exists.  It only verifies the displayed implications after their stated
    hypotheses are supplied.
    """
    if old_mark_count < 16:
        raise ValueError("the logarithmic comparison requires L >= 16")
    if old_difference <= 0:
        raise ValueError("old_difference must be positive")
    constant = _positive_fraction(cap_constant)
    scale_max = theoretical_max_scale(old_mark_count)

    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        length = Decimal(old_mark_count)
        difference = Decimal(old_difference)
        constant_decimal = _fraction_decimal(constant)
        logarithm_length = length.ln()
        single_lower = difference / (Decimal(64) * constant_decimal * logarithm_length)
        total_lower = difference / (Decimal(128) * constant_decimal * Decimal(2).ln())
        block_rows: list[dict[str, Any]] = []
        for scale in range(scale_max + 1):
            block_size = (2**scale) * old_mark_count
            block_decimal = Decimal(block_size)
            logarithm_block = (Decimal(4) * block_decimal).ln()
            bin_upper = (
                Decimal(8)
                * constant_decimal
                * block_decimal
                * block_decimal
                * logarithm_block
                / difference
            )
            cauchy_lower = difference / (
                Decimal(32) * constant_decimal * logarithm_block
            )
            block_rows.append(
                {
                    "scale": scale,
                    "block_size": block_size,
                    "block_within_L_to_three_halves": (
                        block_size * block_size <= old_mark_count**3
                    ),
                    "log_4M_at_most_2_log_L": (
                        logarithm_block <= Decimal(2) * logarithm_length
                    ),
                    "bin_count_strict_upper": _decimal(bin_upper),
                    "M_at_least_twice_bin_upper": (
                        block_decimal >= Decimal(2) * bin_upper
                    ),
                    "cauchy_derived_lower": _decimal(cauchy_lower),
                    "cauchy_lower_dominates_claimed_single_lower": (
                        cauchy_lower >= single_lower
                    ),
                }
            )

        block_count = scale_max + 1
        summed_single_lower = Decimal(block_count) * single_lower
        return {
            "old_mark_count": old_mark_count,
            "old_difference": old_difference,
            "cap_constant": _fraction(constant),
            "eight_d_at_least_L_squared": (
                8 * old_difference >= old_mark_count * old_mark_count
            ),
            "side_condition": cap_side_condition(old_mark_count, constant),
            "theoretical_max_scale": scale_max,
            "theoretical_block_count": block_count,
            "single_block_strict_lower": _decimal(single_lower),
            "summed_single_block_lower": _decimal(summed_single_lower),
            "total_strict_lower": _decimal(total_lower),
            "block_count_converts_single_to_total": (summed_single_lower > total_lower),
            "block_rows": block_rows,
            "all_constant_chain_checks": (
                8 * old_difference >= old_mark_count * old_mark_count
                and cap_side_condition(old_mark_count, constant)
                and summed_single_lower > total_lower
                and all(
                    row["block_within_L_to_three_halves"]
                    and row["log_4M_at_most_2_log_L"]
                    and row["M_at_least_twice_bin_upper"]
                    and row["cauchy_lower_dominates_claimed_single_lower"]
                    for row in block_rows
                )
            ),
        }


def _validated_marks(points: Sequence[int], required: int) -> tuple[int, ...]:
    marks = tuple(points[:required])
    if (
        required < 2
        or len(marks) != required
        or marks[0] != 0
        or marks != tuple(sorted(set(marks)))
        or any(not isinstance(mark, int) for mark in marks)
    ):
        raise ValueError("a normalized increasing integer prefix is required")
    seen: set[int] = set()
    for left in range(required):
        for right in range(left + 1, required):
            difference = marks[right] - marks[left]
            if difference in seen:
                raise ValueError("the supplied prefix is not Golomb")
            seen.add(difference)
    return marks


def _prefix_differences(marks: Sequence[int], mark_count: int) -> set[int]:
    return {
        marks[right] - marks[left]
        for left in range(mark_count)
        for right in range(left + 1, mark_count)
    }


def finite_multiscale_audit(
    points: Sequence[int], old_mark_count: int
) -> dict[str, Any]:
    """Audit every theoretical block available inside one finite fixture."""
    if old_mark_count < 2:
        raise ValueError("old_mark_count must be at least two")
    scale_max = theoretical_max_scale(old_mark_count)
    available_scales = tuple(
        scale
        for scale in range(scale_max + 1)
        if 2 * (2**scale) * old_mark_count <= len(points)
    )
    if not available_scales or available_scales != tuple(range(len(available_scales))):
        raise ValueError("the fixture must contain an initial run of dyadic blocks")

    final_block_size = (2 ** available_scales[-1]) * old_mark_count
    required = 2 * final_block_size
    marks = _validated_marks(points, required)
    threshold = marks[old_mark_count - 1] - marks[0]
    old_differences = _prefix_differences(marks, old_mark_count)
    if threshold not in old_differences:
        raise AssertionError("the selected diameter must be an old difference")

    witness_values: set[int] = set()
    block_rows: list[dict[str, Any]] = []
    for scale in available_scales:
        block_size = (2**scale) * old_mark_count
        block_indices = tuple(range(block_size, 2 * block_size))
        bins: dict[int, list[int]] = {}
        for index in block_indices:
            bins.setdefault(marks[index] // threshold, []).append(index)

        witnessed: list[int] = []
        for indices in bins.values():
            for left, right in combinations(indices, 2):
                witnessed.append(marks[right] - marks[left])

        witnessed_set = set(witnessed)
        if len(witnessed_set) != len(witnessed):
            raise AssertionError("Golomb uniqueness failed inside a block")
        before_overlap = witness_values.intersection(witnessed_set)
        old_overlap = old_differences.intersection(witnessed_set)
        rank_before = sum(
            value <= threshold for value in _prefix_differences(marks, block_size)
        )
        rank_after = sum(
            value <= threshold for value in _prefix_differences(marks, 2 * block_size)
        )
        occupied = len(bins)
        cauchy_lower = Fraction(block_size * block_size, occupied)
        cauchy_lower = (cauchy_lower - block_size) / 2
        block_rows.append(
            {
                "scale": scale,
                "block_size": block_size,
                "index_range_inclusive": [block_size, 2 * block_size - 1],
                "mark_count": block_size,
                "occupied_half_open_bin_count": occupied,
                "same_bin_pair_count": len(witnessed),
                "cauchy_pair_lower": _fraction(cauchy_lower),
                "same_bin_count_dominates_cauchy": (
                    Fraction(len(witnessed)) >= cauchy_lower
                ),
                "minimum_witness_difference": min(witnessed, default=None),
                "maximum_witness_difference": max(witnessed, default=None),
                "all_witness_differences_strictly_below_d": all(
                    value < threshold for value in witnessed
                ),
                "witness_differences_distinct_within_block": (
                    len(witnessed_set) == len(witnessed)
                ),
                "witness_differences_disjoint_from_old_prefix": not old_overlap,
                "witness_differences_disjoint_from_earlier_blocks": (
                    not before_overlap
                ),
                "rank_before": rank_before,
                "rank_after": rank_after,
                "exact_rank_increment": rank_after - rank_before,
                "rank_increment_dominates_block_witness": (
                    rank_after - rank_before >= len(witnessed)
                ),
            }
        )
        witness_values.update(witnessed_set)

    old_rank = sum(value <= threshold for value in old_differences)
    final_differences = _prefix_differences(marks, required)
    final_rank = sum(value <= threshold for value in final_differences)
    full_range = available_scales[-1] == scale_max
    return {
        "old_mark_count": old_mark_count,
        "selected_old_difference": threshold,
        "selected_difference_pair": [0, old_mark_count - 1],
        "selected_difference_is_old": threshold in old_differences,
        "eight_d_at_least_L_squared": (
            8 * threshold >= old_mark_count * old_mark_count
        ),
        "theoretical_max_scale": scale_max,
        "theoretical_block_count": scale_max + 1,
        "available_scales": list(available_scales),
        "available_block_count": len(available_scales),
        "full_theoretical_scale_range_observed": full_range,
        "fixture_range_truncated": not full_range,
        "used_prefix_mark_count": required,
        "used_prefix_sha256": _points_sha256(marks),
        "global_golomb_prefix_verified": True,
        "old_rank": old_rank,
        "block_rows": block_rows,
        "aggregate_witness_difference_count": len(witness_values),
        "aggregate_witnesses_distinct": (
            len(witness_values) == sum(row["same_bin_pair_count"] for row in block_rows)
        ),
        "aggregate_witnesses_disjoint_from_old_prefix": (
            not old_differences.intersection(witness_values)
        ),
        "final_rank": final_rank,
        "exact_total_rank_increment": final_rank - old_rank,
        "rho_increment_dominates_aggregate_witness": (
            final_rank - old_rank >= len(witness_values)
        ),
        "cap_side_condition_C1": cap_side_condition(old_mark_count, Fraction(1)),
        "asymptotic_block_lower_applied": False,
    }


def _fixture_summary(
    fixture: str,
    points: Sequence[int],
    old_mark_count: int,
    expected_counts: tuple[int, ...],
    expected_rank_increments: tuple[int, ...],
) -> dict[str, Any]:
    audit = finite_multiscale_audit(points, old_mark_count)
    counts = tuple(row["same_bin_pair_count"] for row in audit["block_rows"])
    increments = tuple(row["exact_rank_increment"] for row in audit["block_rows"])
    audit.update(
        {
            "fixture": fixture,
            "fixture_mark_count": len(points),
            "fixture_sha256": _points_sha256(points),
            "reported_same_bin_counts": list(expected_counts),
            "reported_rank_increments": list(expected_rank_increments),
            "reported_values_match": (
                counts == expected_counts and increments == expected_rank_increments
            ),
        }
    )
    return audit


def build_certificate() -> dict[str, Any]:
    """Build the deterministic Wave 16 finite certificate."""
    hall = tuple(COUNTEREXAMPLE_64_POINTS)
    et = tuple(erdos_turan_ruler(128, 257))
    rows = [
        _fixture_summary("wave6_hall_counterexample_64", hall, 8, (4, 0), (17, 1)),
        _fixture_summary("wave6_hall_counterexample_64", hall, 16, (24, 22), (69, 64)),
        _fixture_summary("erdos_turan_128_p257", et, 8, (16, 41), (48, 107)),
        _fixture_summary(
            "erdos_turan_128_p257", et, 16, (105, 211, 427), (239, 480, 959)
        ),
        _fixture_summary("erdos_turan_128_p257", et, 32, (465, 932), (990, 1984)),
    ]
    theory_witness = theoretical_inequality_audit(2**24, (2**24) ** 2 // 8, Fraction(1))
    payload: dict[str, Any] = {
        "schema": "erdos1191.wave16.multiscale-future-rank.v1",
        "research_date": "2026-08-29",
        "purpose": (
            "Certify finite disjoint next-block bin witnesses and separately "
            "audit the constants in the conditional multiscale theorem."
        ),
        "analytic_contract": {
            "scales": "M_t=2^t L, 0<=t<=floor((log_2 L)/2)",
            "old_difference_floor": "d>=L^2/8",
            "bins": "half-open [kd,(k+1)d)",
            "side_condition": "sqrt(L)>=128 C log(4 L^(3/2))",
            "single_block_strict_lower": "S_t>d/(64 C log L)",
            "aggregate_strict_lower": "sum_t S_t>d/(128 C log 2)",
            "logarithm": "natural",
        },
        "theory_constant_chain_witness": theory_witness,
        "fixture_rows": rows,
        "scope_flags": {
            "finite_fixture_only": True,
            "eventual_cap_branch_inferred": False,
            "asymptotic_theorem_inferred_from_fixtures": False,
            "all_epoch_signed_allocation": False,
            "problem_unresolved": True,
        },
        "claim_boundary": {
            "finite_block_counts_certified": True,
            "finite_block_disjointness_certified": True,
            "finite_rank_increment_witness_certified": True,
            "conditional_constant_chain_checked_at_80_decimal_digits": True,
            "infinite_eventually_critical_branch_certified": False,
            "p19_proved": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "erdos_1191_resolved": False,
            "prize_claim_ready": False,
        },
        "conclusions": [
            "Same-bin pairs in different dyadic future blocks give mutually distinct differences below the old threshold.",
            "Every finite row has an exact rank increment at least as large as its authenticated witness set.",
            "Hall L=16 and Erdos--Turan L=32 are explicitly truncated at the fixture boundary.",
            "The finite rows do not satisfy or infer the asymptotic cap side condition.",
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
