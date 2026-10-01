"""Finite audit of the Wave 15 local promotion-to-bulk allocation.

For a source epoch ``m`` this module compares the macroscopic suffix
thresholds at prefix ``2m`` with the newly born differences at prefix
``4m-1``.  It performs three separate checks:

* the promotion logarithm is expanded into an exact finite layer cake;
* every selected new difference is authenticated as a literal atom of the
  next negative bulk ``B_(2m)`` with its exact rational coefficient; and
* an equal-share attempt to repay the much larger raw ``u*log(d)`` fan is
  recorded as a failure.

All logarithmic expressions are stored as rational linear forms in logarithms
of positive integers.  The aggregate inequalities are signed exactly by
clearing denominators and comparing integer products.  Floating values and
atomwise deficit counts are explicitly labelled finite projections.  No row
implies an infinite eventually critical branch or an all-epoch allocation.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from collections.abc import Sequence
from dataclasses import dataclass
from fractions import Fraction
from functools import cache
from hashlib import sha256
from itertools import pairwise
from pathlib import Path
from typing import Any

from complete_birth_ledger import erdos_turan_ruler
from wave6_hall_candidate_probe import COUNTEREXAMPLE_64_POINTS
from wave11_abel_repayment_probe import ExactLogForm

DIRECTORY = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    DIRECTORY / "wave15_local_promotion_allocation_certificate_2026-08-29.json"
)


def _canonical_hash(payload: dict[str, Any]) -> str:
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return sha256(canonical.encode("utf-8")).hexdigest()


def _points_sha256(points: Sequence[int]) -> str:
    encoded = ",".join(str(point) for point in points).encode("ascii")
    return sha256(encoded).hexdigest()


def _form_summary(form: ExactLogForm) -> dict[str, Any]:
    return {
        "term_count": len(form.terms),
        "formal_sha256": form.digest(),
        "float_projection": format(form.evaluate(), ".17g"),
    }


def _sum_forms(forms: Sequence[ExactLogForm]) -> ExactLogForm:
    return ExactLogForm.from_terms(term for form in forms for term in form.terms)


def terminal_suffix_weight(epoch: int, left: int) -> Fraction:
    """Return ``u_(m,p)`` on the Wave 15 macroscopic subfan."""
    if epoch < 4:
        raise ValueError("epoch must be at least four")
    if not 2 <= left <= epoch:
        raise ValueError("left must satisfy 2 <= p <= m")
    return Fraction(12 * epoch - 5 - 6 * left, 16 * epoch * epoch)


def literal_next_bulk_coefficient(
    source_epoch: int, left_mark: int, right_mark: int
) -> Fraction:
    """Coefficient of ``a_j-a_i`` in the literal next bulk ``B_(2m)``.

    ``left_mark`` and ``right_mark`` are zero-based mark indices.  The left
    index must be positive because ``B_(2m)`` contains ``D_(i+1,j)`` only for
    ``i+1 >= 2``.
    """
    if source_epoch < 4:
        raise ValueError("source_epoch must be at least four")
    target_epoch = 2 * source_epoch
    if not 1 <= left_mark < right_mark:
        raise ValueError("mark indices must satisfy 1 <= i < j")
    if not target_epoch <= right_mark <= 2 * target_epoch - 2:
        raise ValueError("right mark is outside the next bulk")
    separation = right_mark - left_mark
    if separation == 1:
        return Fraction(1, 4 * source_epoch * source_epoch)
    if separation == 2:
        return Fraction(1, 16 * source_epoch * source_epoch)
    return Fraction(1, 8 * source_epoch * source_epoch)


def _validated_prefix(points: Sequence[int], epoch: int) -> tuple[int, ...]:
    if epoch < 4:
        raise ValueError("epoch must be at least four")
    required = 4 * epoch - 1
    marks = tuple(points[:required])
    if (
        len(marks) != required
        or marks[0] != 0
        or marks != tuple(sorted(set(marks)))
        or any(not isinstance(mark, int) for mark in marks)
    ):
        raise ValueError("points must supply a normalized increasing 4m-1 prefix")
    differences = tuple(
        marks[right] - marks[left]
        for left in range(required)
        for right in range(left + 1, required)
    )
    if len(differences) != len(set(differences)):
        raise ValueError("the 4m-1 prefix must be a Golomb ruler")
    return marks


@dataclass(frozen=True)
class PromotionThresholdRow:
    left: int
    threshold: int
    weight: Fraction
    old_rank: int
    new_rank_increment: int
    future_future_count: int


@dataclass(frozen=True)
class LocalPromotionAudit:
    epoch: int
    point_count: int
    points_sha256: str
    threshold_rows: tuple[PromotionThresholdRow, ...]
    thresholds_strictly_decreasing: bool
    selected_difference_count: int
    all_selected_differences_are_new: bool
    all_selected_differences_are_literal_next_bulk_atoms: bool
    minimum_literal_bulk_coefficient: Fraction
    delta_form: ExactLogForm
    layer_cake_form: ExactLogForm
    layer_cake_identity_exact: bool
    selected_bulk_capacity_form: ExactLogForm
    capacity_minus_delta_exact_sign: int
    raw_frontier_form: ExactLogForm
    raw_equal_share_form: ExactLogForm
    raw_equal_share_identity_exact: bool
    capacity_minus_raw_exact_sign: int
    layer_atom_projection_deficit_count: int
    raw_equal_share_projection_failure_count: int
    minimum_layer_atom_margin_projection: float
    maximum_raw_equal_share_deficit_projection: float


@cache
def _local_promotion_audit_cached(
    points: tuple[int, ...], epoch: int
) -> LocalPromotionAudit:
    marks = _validated_prefix(points, epoch)
    old_mark_count = 2 * epoch
    extended_mark_count = 4 * epoch - 1

    difference_pairs: dict[int, tuple[int, int]] = {}
    for left in range(extended_mark_count):
        for right in range(left + 1, extended_mark_count):
            difference = marks[right] - marks[left]
            if difference in difference_pairs:
                raise AssertionError("Golomb validation failed to ensure uniqueness")
            difference_pairs[difference] = (left, right)

    old_differences = {
        marks[right] - marks[left]
        for left in range(old_mark_count)
        for right in range(left + 1, old_mark_count)
    }
    new_differences = {
        difference: pair
        for difference, pair in difference_pairs.items()
        if pair[1] >= old_mark_count
    }

    delta_terms: list[tuple[int, Fraction]] = []
    raw_frontier_terms: list[tuple[int, Fraction]] = []
    layer_loads: defaultdict[int, ExactLogForm] = defaultdict(ExactLogForm.zero)
    raw_equal_share_loads: defaultdict[int, ExactLogForm] = defaultdict(
        ExactLogForm.zero
    )
    threshold_rows: list[PromotionThresholdRow] = []

    for left in range(2, epoch + 1):
        threshold = marks[2 * epoch - 1] - marks[left - 1]
        weight = terminal_suffix_weight(epoch, left)
        old_rank = sum(value <= threshold for value in old_differences)
        eligible = tuple(
            sorted(value for value in new_differences if value <= threshold)
        )
        increment = len(eligible)
        if not increment:
            raise ValueError("the finite audit requires a positive rank increment")

        delta_terms.extend(((old_rank + increment, weight), (old_rank, -weight)))
        raw_frontier_terms.append((threshold, weight))
        equal_share = weight / increment
        for rank_increment, difference in enumerate(eligible, start=1):
            layer_loads[difference] = layer_loads[difference] + ExactLogForm.from_terms(
                (
                    (old_rank + rank_increment, weight),
                    (old_rank + rank_increment - 1, -weight),
                )
            )
            raw_equal_share_loads[difference] = raw_equal_share_loads[
                difference
            ] + ExactLogForm.from_terms(((threshold, equal_share),))

        future_future_count = sum(
            marks[right] - marks[future_left] < threshold
            for future_left in range(old_mark_count, extended_mark_count)
            for right in range(future_left + 1, extended_mark_count)
        )
        threshold_rows.append(
            PromotionThresholdRow(
                left=left,
                threshold=threshold,
                weight=weight,
                old_rank=old_rank,
                new_rank_increment=increment,
                future_future_count=future_future_count,
            )
        )

    selected = tuple(sorted(layer_loads))
    literal_coefficients: dict[int, Fraction] = {}
    literal_flags: list[bool] = []
    for difference in selected:
        left_mark, right_mark = new_differences[difference]
        literal = (
            left_mark >= 1 and old_mark_count <= right_mark <= extended_mark_count - 1
        )
        literal_flags.append(literal)
        if not literal:
            raise AssertionError(
                "a selected difference is not a literal next-bulk atom"
            )
        literal_coefficients[difference] = literal_next_bulk_coefficient(
            epoch, left_mark, right_mark
        )

    delta_form = ExactLogForm.from_terms(delta_terms)
    layer_cake_form = _sum_forms(tuple(layer_loads.values()))
    selected_capacity_form = ExactLogForm.from_terms(
        (difference, literal_coefficients[difference]) for difference in selected
    )
    raw_frontier_form = ExactLogForm.from_terms(raw_frontier_terms)
    raw_equal_share_form = _sum_forms(tuple(raw_equal_share_loads.values()))

    layer_margins = tuple(
        ExactLogForm.from_terms(
            ((difference, literal_coefficients[difference]),)
        ).evaluate()
        - layer_loads[difference].evaluate()
        for difference in selected
    )
    raw_deficits = tuple(
        raw_equal_share_loads[difference].evaluate()
        - ExactLogForm.from_terms(
            ((difference, literal_coefficients[difference]),)
        ).evaluate()
        for difference in selected
    )

    return LocalPromotionAudit(
        epoch=epoch,
        point_count=len(marks),
        points_sha256=_points_sha256(marks),
        threshold_rows=tuple(threshold_rows),
        thresholds_strictly_decreasing=all(
            left.threshold > right.threshold for left, right in pairwise(threshold_rows)
        ),
        selected_difference_count=len(selected),
        all_selected_differences_are_new=old_differences.isdisjoint(selected),
        all_selected_differences_are_literal_next_bulk_atoms=all(literal_flags),
        minimum_literal_bulk_coefficient=min(literal_coefficients.values()),
        delta_form=delta_form,
        layer_cake_form=layer_cake_form,
        layer_cake_identity_exact=(delta_form == layer_cake_form),
        selected_bulk_capacity_form=selected_capacity_form,
        capacity_minus_delta_exact_sign=(
            selected_capacity_form - delta_form
        ).exact_sign(maximum_exponent_mass=2_000_000),
        raw_frontier_form=raw_frontier_form,
        raw_equal_share_form=raw_equal_share_form,
        raw_equal_share_identity_exact=(raw_frontier_form == raw_equal_share_form),
        capacity_minus_raw_exact_sign=(
            selected_capacity_form - raw_frontier_form
        ).exact_sign(maximum_exponent_mass=2_000_000),
        layer_atom_projection_deficit_count=sum(margin < 0 for margin in layer_margins),
        raw_equal_share_projection_failure_count=sum(
            deficit > 0 for deficit in raw_deficits
        ),
        minimum_layer_atom_margin_projection=min(layer_margins),
        maximum_raw_equal_share_deficit_projection=max(raw_deficits),
    )


def local_promotion_audit(points: Sequence[int], epoch: int) -> LocalPromotionAudit:
    """Return the cached exact finite audit for one fixture and epoch."""
    return _local_promotion_audit_cached(tuple(points), epoch)


def _audit_summary(
    fixture: str, audit: LocalPromotionAudit, expected: tuple[int, str, str]
) -> dict[str, Any]:
    expected_future_count, expected_delta, expected_capacity = expected
    minimum_future_count = min(row.future_future_count for row in audit.threshold_rows)
    delta_six = format(audit.delta_form.evaluate(), ".6f")
    capacity_six = format(audit.selected_bulk_capacity_form.evaluate(), ".6f")
    return {
        "fixture": fixture,
        "epoch": audit.epoch,
        "point_count": audit.point_count,
        "points_sha256": audit.points_sha256,
        "threshold_rows": [
            {
                "left": row.left,
                "threshold": row.threshold,
                "weight": str(row.weight),
                "old_rank": row.old_rank,
                "new_rank_increment": row.new_rank_increment,
                "future_future_count": row.future_future_count,
            }
            for row in audit.threshold_rows
        ],
        "thresholds_strictly_decreasing": audit.thresholds_strictly_decreasing,
        "minimum_future_future_count": minimum_future_count,
        "selected_difference_count": audit.selected_difference_count,
        "all_selected_differences_are_new": audit.all_selected_differences_are_new,
        "all_selected_differences_are_literal_next_bulk_atoms": (
            audit.all_selected_differences_are_literal_next_bulk_atoms
        ),
        "minimum_literal_bulk_coefficient": str(audit.minimum_literal_bulk_coefficient),
        "minimum_coefficient_formula_verified": (
            audit.minimum_literal_bulk_coefficient
            == Fraction(1, 16 * audit.epoch * audit.epoch)
        ),
        "delta": _form_summary(audit.delta_form),
        "layer_cake": _form_summary(audit.layer_cake_form),
        "layer_cake_identity_exact": audit.layer_cake_identity_exact,
        "selected_literal_bulk_capacity": _form_summary(
            audit.selected_bulk_capacity_form
        ),
        "capacity_minus_delta_exact_sign": audit.capacity_minus_delta_exact_sign,
        "delta_at_most_selected_capacity_exact": (
            audit.capacity_minus_delta_exact_sign >= 0
        ),
        "layer_atom_projection_deficit_count": (
            audit.layer_atom_projection_deficit_count
        ),
        "minimum_layer_atom_margin_projection": format(
            audit.minimum_layer_atom_margin_projection, ".17g"
        ),
        "raw_frontier": _form_summary(audit.raw_frontier_form),
        "raw_equal_share": _form_summary(audit.raw_equal_share_form),
        "raw_equal_share_identity_exact": audit.raw_equal_share_identity_exact,
        "capacity_minus_raw_exact_sign": audit.capacity_minus_raw_exact_sign,
        "raw_total_exceeds_selected_capacity_exact": (
            audit.capacity_minus_raw_exact_sign < 0
        ),
        "raw_equal_share_failure_forced_exactly": (
            audit.raw_equal_share_identity_exact
            and audit.capacity_minus_raw_exact_sign < 0
        ),
        "raw_equal_share_projection_failure_count": (
            audit.raw_equal_share_projection_failure_count
        ),
        "maximum_raw_equal_share_deficit_projection": format(
            audit.maximum_raw_equal_share_deficit_projection, ".17g"
        ),
        "reported_calibration": {
            "minimum_future_future_count": expected_future_count,
            "delta_six_decimal": expected_delta,
            "selected_capacity_six_decimal": expected_capacity,
        },
        "reported_calibration_matches": (
            minimum_future_count == expected_future_count
            and delta_six == expected_delta
            and capacity_six == expected_capacity
        ),
        "finite_only": True,
        "asymptotic_inference": False,
    }


@cache
def build_certificate() -> dict[str, Any]:
    """Build the deterministic Wave 15 finite certificate."""
    hall = tuple(COUNTEREXAMPLE_64_POINTS)
    et = tuple(erdos_turan_ruler(128, 257))
    specifications = (
        ("wave6_hall_counterexample_64", hall, 4, (6, "0.116177", "0.685518")),
        ("wave6_hall_counterexample_64", hall, 8, (39, "0.173403", "0.877240")),
        (
            "wave6_hall_counterexample_64",
            hall,
            16,
            (222, "0.265625", "1.476791"),
        ),
        ("erdos_turan_128_p257", et, 4, (15, "0.223784", "2.131468")),
        ("erdos_turan_128_p257", et, 8, (84, "0.387305", "3.358074")),
        ("erdos_turan_128_p257", et, 16, (351, "0.464170", "3.996318")),
        (
            "erdos_turan_128_p257",
            et,
            32,
            (1465, "0.504070", "4.498849"),
        ),
    )
    rows = [
        _audit_summary(fixture, local_promotion_audit(points, epoch), expected)
        for fixture, points, epoch, expected in specifications
    ]
    payload: dict[str, Any] = {
        "schema": "erdos1191.wave15.local-promotion-allocation.v1",
        "research_date": "2026-08-29",
        "purpose": (
            "Certify the finite Delta_m layer cake, authenticate its selected "
            "differences as literal B_(2m) atoms, and retain the raw-log-d "
            "equal-share failure as a separate finite no-go."
        ),
        "fixture_rows": rows,
        "exact_contract": {
            "delta": "sum_(p=2)^m u_(m,p) log(1+K_p/r_p)",
            "layer_increment": "u_(m,p) log((r_p+k)/(r_p+k-1))",
            "literal_bulk_coefficient_gap_1": "1/(4m^2)",
            "literal_bulk_coefficient_gap_2": "1/(16m^2)",
            "literal_bulk_coefficient_gap_at_least_3": "1/(8m^2)",
            "selected_capacity": "sum_x beta_(2m)(x) log(x)",
            "raw_equal_share": "each p assigns u_(m,p) log(d_p)/K_p to each eligible x",
            "logarithm": "natural",
        },
        "scope_flags": {
            "finite_fixture_only": True,
            "eventual_cap_inferred": False,
            "infinite_branch": False,
            "all_epoch_signed_allocation": False,
            "problem_unresolved": True,
        },
        "claim_boundary": {
            "finite_layer_cake_certified": True,
            "literal_next_bulk_membership_certified": True,
            "finite_delta_at_most_selected_capacity_certified": True,
            "raw_log_d_equal_share_repayment_certified": False,
            "raw_log_d_equal_share_failure_recorded": True,
            "asymptotic_local_promotion_lemma_certified_by_fixtures": False,
            "infinite_eventually_critical_branch_certified": False,
            "p19_proved": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "erdos_1191_resolved": False,
            "prize_claim_ready": False,
        },
        "conclusions": [
            "Every finite fixture has an exact layer-cake identity for Delta_m.",
            "The selected new differences are literal next-bulk atoms, and their total capacity exceeds Delta_m exactly.",
            "The raw u*log(d) equal-share load exceeds the same selected capacity in every calibration row.",
            "These bounded rows do not imply an infinite branch or solve the all-epoch terminal allocation.",
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
