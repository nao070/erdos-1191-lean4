"""Finite Wave 8 probes for survival-conditioned debt repayment.

The routines in this module use exact integer/Fraction arithmetic.  They
separate four finite questions which must not be confused with the missing
infinite theorem:

* how far a prefix survives in the explicitly capped ``C=1`` extension tree;
* how many differences are certified by the cheap-half rank-lag bound;
* how many actual non-adjacent differences lie below the same threshold; and
* whether either finite reservoir is large enough to dominate one exact
  adjoint innovation.

No bounded search is interpreted as evidence of infinite critical survival.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Iterable, Sequence
from dataclasses import asdict, dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import product
from pathlib import Path
from typing import Any

from gap_measure_dynamics import dyadic_gap_matrix_update
from innovation_budget import LYAPUNOV_MATRIX, frobenius_inner
from wave6_collision_bands import (
    antidiagonal_threshold,
    dyadic_shell_profile,
)
from wave6_hall_candidate_probe import (
    COUNTEREXAMPLE_64_POINTS,
    critical_modulus_cap,
)
from wave7_band_renewal_probe import (
    all_prefix_c1,
    compatible_adjacent_gap_swaps,
    dyadic_boundaries,
    enumerate_compatible_four_mark_rulers,
    is_golomb,
    load_authenticated_wave6_fixtures,
    positive_differences,
    threshold_activations,
)
from wave8_actual_adjacent_renewal import renewal_dichotomy

Pair = tuple[int, int]


def _validated_golomb(
    points: Sequence[int], *, require_c1: bool = False
) -> tuple[int, ...]:
    marks = tuple(points)
    if (
        len(marks) < 2
        or any(not isinstance(mark, int) for mark in marks)
        or marks[0] != 0
        or marks != tuple(sorted(set(marks)))
    ):
        raise ValueError("points must be normalized strictly increasing integers")
    if not is_golomb(marks):
        raise ValueError("points must be a Golomb ruler")
    if require_c1 and not all_prefix_c1(marks):
        raise ValueError("points must obey every C=1 prefix cap")
    return marks


def _incremental_children(points: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    used = frozenset(positive_differences(points))
    cap = critical_modulus_cap(len(points) + 1)
    rows: list[tuple[int, ...]] = []
    for mark in range(points[-1] + 1, cap):
        new_differences = tuple(mark - old for old in points)
        if len(new_differences) == len(set(new_differences)) and used.isdisjoint(
            new_differences
        ):
            rows.append((*points, mark))
    return tuple(rows)


def critical_children(points: Sequence[int]) -> tuple[tuple[int, ...], ...]:
    """Exhaust all one-mark children inside the exact next ``C=1`` cap."""
    marks = _validated_golomb(points, require_c1=True)
    return _incremental_children(marks)


@dataclass(frozen=True)
class CriticalSurvivalAudit:
    root: tuple[int, ...]
    requested_depth: int
    level_counts: tuple[int, ...]
    survives_requested_depth: bool
    first_leaf: tuple[int, ...] | None
    last_leaf: tuple[int, ...] | None


def critical_survival_audit(
    points: Sequence[int], *, depth: int
) -> CriticalSurvivalAudit:
    """Compute the exact finite-depth proxy ``surv_1(P)>=depth``.

    The returned predicate is only a finite tree statement.  In particular,
    ``True`` is never promoted to ``surv_1(P)=infinity``.
    """
    marks = _validated_golomb(points, require_c1=True)
    if not isinstance(depth, int) or depth < 0:
        raise ValueError("depth must be a nonnegative integer")
    frontier = (marks,)
    counts = [1]
    for _ in range(depth):
        frontier = tuple(
            child for parent in frontier for child in _incremental_children(parent)
        )
        counts.append(len(frontier))
        if not frontier:
            counts.extend(0 for _ in range(depth + 1 - len(counts)))
            break
    return CriticalSurvivalAudit(
        root=marks,
        requested_depth=depth,
        level_counts=tuple(counts),
        survives_requested_depth=bool(frontier) and len(counts) == depth + 1,
        first_leaf=frontier[0] if frontier else None,
        last_leaf=frontier[-1] if frontier else None,
    )


@dataclass(frozen=True)
class BoundedGolombExhaustion:
    mark_count: int
    maximum_last_mark: int
    ruler_count: int
    search_node_count: int
    first_ruler: tuple[int, ...]
    last_ruler: tuple[int, ...]
    rulers: tuple[tuple[int, ...], ...]


def bounded_golomb_exhaustion(
    *, mark_count: int, maximum_last_mark: int
) -> BoundedGolombExhaustion:
    """Exhaust normalized rulers with exactly ``mark_count`` marks and diameter cap."""
    if not isinstance(mark_count, int) or mark_count < 2:
        raise ValueError("mark_count must be an integer at least two")
    minimum_differences = mark_count * (mark_count - 1) // 2
    if (
        not isinstance(maximum_last_mark, int)
        or maximum_last_mark < minimum_differences
    ):
        raise ValueError("maximum_last_mark is below the counting lower bound")

    rulers: list[tuple[int, ...]] = []
    node_count = 0

    def extend(partial: tuple[int, ...], used: frozenset[int]) -> None:
        nonlocal node_count
        if len(partial) == mark_count:
            rulers.append(partial)
            return
        remaining = mark_count - len(partial)
        for mark in range(
            partial[-1] + 1,
            maximum_last_mark - remaining + 2,
        ):
            node_count += 1
            new_differences = tuple(mark - old for old in partial)
            if len(new_differences) == len(set(new_differences)) and used.isdisjoint(
                new_differences
            ):
                extend(partial + (mark,), used.union(new_differences))

    extend((0,), frozenset())
    if not rulers:
        raise ValueError("the bounded Golomb scope is empty")
    return BoundedGolombExhaustion(
        mark_count=mark_count,
        maximum_last_mark=maximum_last_mark,
        ruler_count=len(rulers),
        search_node_count=node_count,
        first_ruler=rulers[0],
        last_ruler=rulers[-1],
        rulers=tuple(rulers),
    )


@dataclass(frozen=True)
class HalfOption:
    epoch: int
    side: str
    lag_cutoff: int
    pairs: frozenset[Pair]


def _half_options(
    points: tuple[int, ...], epoch: int, threshold: Fraction
) -> tuple[HalfOption, ...]:
    if epoch == 1:
        return (HalfOption(epoch, "none", 0, frozenset()),)
    profile = dyadic_shell_profile(points, old_count=epoch)
    rows: list[HalfOption] = []
    for side, start, mean, discrepancy in (
        ("old", 0, profile.old_mean, profile.old_discrepancy),
        ("new", epoch, profile.shell_mean, profile.shell_discrepancy),
    ):
        raw_cutoff = (threshold - 2 * discrepancy) / mean
        lag_cutoff = min(
            epoch - 1,
            max(0, raw_cutoff.numerator // raw_cutoff.denominator),
        )
        if lag_cutoff < 1:
            continue
        pairs = frozenset(
            (left, left + lag)
            for lag in range(1, lag_cutoff + 1)
            for left in range(start, start + epoch - lag)
        )
        rows.append(HalfOption(epoch, side, lag_cutoff, pairs))
    if not rows:
        raise AssertionError("an active epoch has no cheap side at lag one")
    return tuple(rows)


def _wave6_pairs(
    points: tuple[int, ...], threshold: Fraction
) -> tuple[tuple[int, ...], frozenset[Pair]]:
    active: list[int] = []
    selected: set[Pair] = set()
    for epoch in dyadic_boundaries(len(points)):
        profile = dyadic_shell_profile(points, old_count=epoch)
        if antidiagonal_threshold(profile, 1) <= threshold:
            active.append(epoch)
        for antidiagonal in range(1, epoch + 1):
            if antidiagonal_threshold(profile, antidiagonal) > threshold:
                continue
            selected.update(
                (epoch - 1 - offset, epoch - 1 + antidiagonal - offset)
                for offset in range(antidiagonal)
            )
    return tuple(active), frozenset(selected)


@dataclass(frozen=True)
class _ConfigurationScore:
    orientations: tuple[str, ...]
    adjacent_new_count: int
    debt: int
    reservoir_count: int
    certified_total_count: int
    debt_margin: int


def _score_configuration(
    configuration: Sequence[HalfOption],
    wave6_pairs: frozenset[Pair],
    tax: int,
) -> _ConfigurationScore:
    certified = set().union(*(option.pairs for option in configuration))
    certified.difference_update(wave6_pairs)
    adjacent = {pair for pair in certified if pair[1] - pair[0] == 1}
    reservoir = certified.difference(adjacent)
    debt = tax - len(adjacent)
    return _ConfigurationScore(
        orientations=tuple(option.side for option in configuration),
        adjacent_new_count=len(adjacent),
        debt=debt,
        reservoir_count=len(reservoir),
        certified_total_count=len(certified),
        debt_margin=len(reservoir) - debt,
    )


def _best_configuration(
    option_rows: Sequence[Sequence[HalfOption]],
    wave6_pairs: frozenset[Pair],
    tax: int,
) -> _ConfigurationScore:
    scores = tuple(
        _score_configuration(configuration, wave6_pairs, tax)
        for configuration in product(*option_rows)
    )
    return min(
        scores,
        key=lambda row: (
            -row.debt_margin,
            -row.reservoir_count,
            -row.adjacent_new_count,
            row.orientations,
        ),
    )


def _maximum_adjacent_configuration(
    option_rows: Sequence[Sequence[HalfOption]],
    wave6_pairs: frozenset[Pair],
    tax: int,
) -> _ConfigurationScore:
    scores = tuple(
        _score_configuration(configuration, wave6_pairs, tax)
        for configuration in product(*option_rows)
    )
    return min(
        scores,
        key=lambda row: (
            -row.adjacent_new_count,
            row.orientations,
        ),
    )


def _new_preferred_configuration(
    option_rows: Sequence[Sequence[HalfOption]],
) -> tuple[HalfOption, ...]:
    selected: list[HalfOption] = []
    for options in option_rows:
        selected.append(
            min(
                options,
                key=lambda option: (
                    option.side != "new",
                    -option.lag_cutoff,
                    option.side,
                ),
            )
        )
    return tuple(selected)


def _greedy_configuration(
    option_rows: Sequence[Sequence[HalfOption]],
    wave6_pairs: frozenset[Pair],
) -> tuple[HalfOption, ...]:
    covered: set[Pair] = set()
    selected: list[HalfOption] = []
    for options in option_rows:
        option = min(
            options,
            key=lambda candidate: (
                -len(candidate.pairs.difference(wave6_pairs, covered)),
                candidate.side != "new",
                -candidate.lag_cutoff,
                candidate.side,
            ),
        )
        selected.append(option)
        covered.update(option.pairs)
    return tuple(selected)


@dataclass(frozen=True)
class RepaymentAudit:
    threshold: Fraction
    floor_threshold: int
    active_epochs: tuple[int, ...]
    option_signature: tuple[tuple[tuple[str, int], ...], ...]
    wave6_pair_count: int
    epoch_size_tax: int
    optimal_orientations: tuple[str, ...]
    optimal_adjacent_new_count: int
    optimal_adjacent_debt: int
    maximum_adjacent_new_count: int
    minimum_adjacent_debt: int
    certified_reservoir_count: int
    certified_total_new_count: int
    certified_debt_margin: int
    certified_tax_margin: int
    new_preferred_orientations: tuple[str, ...]
    new_preferred_debt_margin: int
    greedy_orientations: tuple[str, ...]
    greedy_debt_margin: int
    global_nonadjacent_reservoir_count: int
    global_nonadjacent_debt_margin: int
    latest_shell_nonadjacent_reservoir_count: int
    latest_shell_nonadjacent_debt_margin: int
    normalized_adjoint_innovation: Fraction
    certified_density_innovation_margin: Fraction
    global_density_innovation_margin: Fraction
    certified_density_to_innovation_ratio: Fraction
    global_density_to_innovation_ratio: Fraction


@dataclass(frozen=True)
class ActualRenewalComparison:
    epoch: int
    first_cross_threshold: Fraction
    actual_new_family_threshold: int
    ancestry_cleared: bool
    new_family_paid: bool
    outstanding_demand: int
    wave6_pair_count: int
    global_nonadjacent_reservoir_count: int
    global_debt_margin: int
    latest_shell_nonadjacent_reservoir_count: int
    latest_shell_debt_margin: int
    normalized_adjoint_innovation: Fraction
    global_density_innovation_margin: Fraction
    latest_density_innovation_margin: Fraction
    global_density_to_innovation_ratio: Fraction
    latest_density_to_innovation_ratio: Fraction


def actual_renewal_comparison(
    points: Sequence[int], *, old_count: int
) -> ActualRenewalComparison:
    """Compare non-adjacent capacity with the actual single-family renewal debt."""
    marks = _validated_golomb(points)
    if (
        not isinstance(old_count, int)
        or old_count < 2
        or old_count & (old_count - 1)
        or len(marks) < 2 * old_count
    ):
        raise ValueError("old_count must be a nontrivial complete dyadic epoch")
    prefix = marks[: 2 * old_count]
    event = renewal_dichotomy(prefix, old_count=old_count)
    threshold = event.first_cross_threshold
    integer_cutoff = threshold.numerator // threshold.denominator
    _, wave6_pairs = _wave6_pairs(prefix, threshold)
    history_pairs = {
        (left, right)
        for right in range(2 * old_count)
        for left in range(right - 1)
        if prefix[right] - prefix[left] <= integer_cutoff
    }
    latest_pairs = {
        (left, right)
        for right in range(old_count, 2 * old_count)
        for left in range(right - 1)
        if prefix[right] - prefix[left] <= integer_cutoff
    }
    global_reservoir = history_pairs.difference(wave6_pairs)
    latest_reservoir = latest_pairs.difference(wave6_pairs)
    outstanding = 0 if event.new_family_paid else old_count - 1

    update = dyadic_gap_matrix_update(prefix, old_count)
    innovation = (
        frobenius_inner(LYAPUNOV_MATRIX, update.innovation) / update.new_modulus
    )
    global_density = Fraction(len(global_reservoir), 1) / threshold
    latest_density = Fraction(len(latest_reservoir), 1) / threshold
    return ActualRenewalComparison(
        epoch=old_count,
        first_cross_threshold=threshold,
        actual_new_family_threshold=event.new_internal_maximum,
        ancestry_cleared=event.ancestry_cleared,
        new_family_paid=event.new_family_paid,
        outstanding_demand=outstanding,
        wave6_pair_count=len(wave6_pairs),
        global_nonadjacent_reservoir_count=len(global_reservoir),
        global_debt_margin=len(global_reservoir) - outstanding,
        latest_shell_nonadjacent_reservoir_count=len(latest_reservoir),
        latest_shell_debt_margin=len(latest_reservoir) - outstanding,
        normalized_adjoint_innovation=innovation,
        global_density_innovation_margin=global_density - innovation,
        latest_density_innovation_margin=latest_density - innovation,
        global_density_to_innovation_ratio=global_density / innovation,
        latest_density_to_innovation_ratio=latest_density / innovation,
    )


def repayment_audit(points: Sequence[int], threshold: Fraction | int) -> RepaymentAudit:
    """Score exact cheap-half, global, and innovation repayment candidates."""
    marks = _validated_golomb(points)
    cutoff = Fraction(threshold)
    if cutoff < 0:
        raise ValueError("threshold must be nonnegative")
    active, wave6_pairs = _wave6_pairs(marks, cutoff)
    if not active or max(active) < 2:
        raise ValueError("at least one nontrivial active dyadic epoch is required")
    option_rows = tuple(_half_options(marks, epoch, cutoff) for epoch in active)
    tax = sum(epoch - 1 for epoch in active)
    optimal = _best_configuration(option_rows, wave6_pairs, tax)
    maximum_adjacent = _maximum_adjacent_configuration(option_rows, wave6_pairs, tax)
    new_preferred = _score_configuration(
        _new_preferred_configuration(option_rows), wave6_pairs, tax
    )
    greedy = _score_configuration(
        _greedy_configuration(option_rows, wave6_pairs), wave6_pairs, tax
    )

    # The unrestricted comparison deliberately uses actual non-adjacent
    # differences, not the cheap-half upper bound.  Golomb uniqueness makes
    # pair cardinality equal numerical-difference cardinality.
    largest_epoch = max(active)
    integer_cutoff = cutoff.numerator // cutoff.denominator
    history_pairs = {
        (left, right)
        for right in range(2 * largest_epoch)
        for left in range(right - 1)
        if marks[right] - marks[left] <= integer_cutoff
    }
    latest_shell_pairs = {
        (left, right)
        for right in range(largest_epoch, 2 * largest_epoch)
        for left in range(right - 1)
        if marks[right] - marks[left] <= integer_cutoff
    }
    global_reservoir = history_pairs.difference(wave6_pairs)
    latest_reservoir = latest_shell_pairs.difference(wave6_pairs)

    update = dyadic_gap_matrix_update(marks[: 2 * largest_epoch], largest_epoch)
    innovation = (
        frobenius_inner(LYAPUNOV_MATRIX, update.innovation) / update.new_modulus
    )
    if innovation <= 0:
        raise AssertionError("the exact adjoint innovation must be positive")
    certified_density = Fraction(optimal.reservoir_count, 1) / cutoff
    global_density = Fraction(len(global_reservoir), 1) / cutoff

    return RepaymentAudit(
        threshold=cutoff,
        floor_threshold=integer_cutoff,
        active_epochs=active,
        option_signature=tuple(
            tuple((option.side, option.lag_cutoff) for option in options)
            for options in option_rows
        ),
        wave6_pair_count=len(wave6_pairs),
        epoch_size_tax=tax,
        optimal_orientations=optimal.orientations,
        optimal_adjacent_new_count=optimal.adjacent_new_count,
        optimal_adjacent_debt=optimal.debt,
        maximum_adjacent_new_count=maximum_adjacent.adjacent_new_count,
        minimum_adjacent_debt=maximum_adjacent.debt,
        certified_reservoir_count=optimal.reservoir_count,
        certified_total_new_count=optimal.certified_total_count,
        certified_debt_margin=optimal.debt_margin,
        certified_tax_margin=optimal.reservoir_count - tax,
        new_preferred_orientations=new_preferred.orientations,
        new_preferred_debt_margin=new_preferred.debt_margin,
        greedy_orientations=greedy.orientations,
        greedy_debt_margin=greedy.debt_margin,
        global_nonadjacent_reservoir_count=len(global_reservoir),
        global_nonadjacent_debt_margin=len(global_reservoir) - maximum_adjacent.debt,
        latest_shell_nonadjacent_reservoir_count=len(latest_reservoir),
        latest_shell_nonadjacent_debt_margin=(
            len(latest_reservoir) - maximum_adjacent.debt
        ),
        normalized_adjoint_innovation=innovation,
        certified_density_innovation_margin=certified_density - innovation,
        global_density_innovation_margin=global_density - innovation,
        certified_density_to_innovation_ratio=certified_density / innovation,
        global_density_to_innovation_ratio=global_density / innovation,
    )


_CANDIDATE_FIELDS = {
    "certified_rank_lag_debt": "certified_debt_margin",
    "certified_reservoir_pays_full_tax": "certified_tax_margin",
    "global_nonadjacent_debt": "global_nonadjacent_debt_margin",
    "latest_shell_nonadjacent_debt": "latest_shell_nonadjacent_debt_margin",
    "certified_density_innovation": "certified_density_innovation_margin",
    "global_density_innovation": "global_density_innovation_margin",
}

_ACTUAL_CANDIDATE_FIELDS = {
    "global_debt": "global_debt_margin",
    "latest_shell_debt": "latest_shell_debt_margin",
    "global_density_innovation": "global_density_innovation_margin",
    "latest_density_innovation": "latest_density_innovation_margin",
}


def _thresholds_with_active_count(
    points: tuple[int, ...], minimum_active_epochs: int
) -> tuple[Fraction, ...]:
    rows: list[Fraction] = []
    for threshold in sorted({row.threshold for row in threshold_activations(points)}):
        active, _ = _wave6_pairs(points, threshold)
        if len(active) >= minimum_active_epochs:
            rows.append(threshold)
    return tuple(rows)


def _audit_witness(
    points: tuple[int, ...], row: RepaymentAudit, field: str
) -> dict[str, Any]:
    return {
        "points": points,
        "threshold": row.threshold,
        "margin": getattr(row, field),
        "active_epochs": row.active_epochs,
        "wave6_pair_count": row.wave6_pair_count,
        "epoch_size_tax": row.epoch_size_tax,
        "optimal_orientations": row.optimal_orientations,
        "optimal_adjacent_debt": row.optimal_adjacent_debt,
        "maximum_adjacent_new_count": row.maximum_adjacent_new_count,
        "minimum_adjacent_debt": row.minimum_adjacent_debt,
        "certified_reservoir_count": row.certified_reservoir_count,
        "global_nonadjacent_reservoir_count": row.global_nonadjacent_reservoir_count,
        "latest_shell_nonadjacent_reservoir_count": (
            row.latest_shell_nonadjacent_reservoir_count
        ),
        "normalized_adjoint_innovation": row.normalized_adjoint_innovation,
    }


def audit_ruler_scope(
    rulers: Iterable[Sequence[int]], *, minimum_active_epochs: int
) -> dict[str, Any]:
    """Scan every activation threshold in an explicitly supplied finite scope."""
    if not isinstance(minimum_active_epochs, int) or minimum_active_epochs < 2:
        raise ValueError("minimum_active_epochs must be an integer at least two")
    normalized = tuple(_validated_golomb(points) for points in rulers)
    minima: dict[str, tuple[Any, ...] | None] = {
        name: None for name in _CANDIDATE_FIELDS
    }
    negative_counts = {name: 0 for name in _CANDIDATE_FIELDS}
    selection_suboptimal_counts = {"new_preferred": 0, "greedy": 0}
    selection_maximum_losses: dict[str, tuple[Any, ...] | None] = {
        "new_preferred": None,
        "greedy": None,
    }
    event_count = 0
    for points in normalized:
        for threshold in _thresholds_with_active_count(points, minimum_active_epochs):
            event_count += 1
            row = repayment_audit(points, threshold)
            for name, margin in (
                ("new_preferred", row.new_preferred_debt_margin),
                ("greedy", row.greedy_debt_margin),
            ):
                loss = row.certified_debt_margin - margin
                selection_suboptimal_counts[name] += loss > 0
                witness = (
                    loss,
                    points,
                    threshold,
                    row.optimal_orientations,
                    (
                        row.new_preferred_orientations
                        if name == "new_preferred"
                        else row.greedy_orientations
                    ),
                )
                current = selection_maximum_losses[name]
                if current is None or witness > current:
                    selection_maximum_losses[name] = witness
            for name, field in _CANDIDATE_FIELDS.items():
                margin = getattr(row, field)
                negative_counts[name] += margin < 0
                key = (margin, threshold, points)
                current = minima[name]
                if current is None or key < current[:3]:
                    minima[name] = (margin, threshold, points, row)
    if event_count == 0:
        raise ValueError("the supplied scope has no eligible activation event")
    results: dict[str, Any] = {}
    for name, field in _CANDIDATE_FIELDS.items():
        minimum = minima[name]
        if minimum is None:
            raise AssertionError("candidate minimum unexpectedly absent")
        results[name] = {
            "negative_count": negative_counts[name],
            "survives_stated_scope": negative_counts[name] == 0,
            "minimum_witness": _audit_witness(minimum[2], minimum[3], field),
        }
    return {
        "ruler_count": len(normalized),
        "activation_event_count": event_count,
        "minimum_active_epoch_count": minimum_active_epochs,
        "candidate_results": results,
        "selection_comparison": {
            name: {
                "suboptimal_event_count": selection_suboptimal_counts[name],
                "maximum_loss": selection_maximum_losses[name][0],
                "maximum_loss_points": selection_maximum_losses[name][1],
                "maximum_loss_threshold": selection_maximum_losses[name][2],
                "exact_orientations": selection_maximum_losses[name][3],
                "selected_orientations": selection_maximum_losses[name][4],
            }
            for name in selection_suboptimal_counts
        },
    }


def audit_actual_single_debt_scope(
    rulers: Iterable[Sequence[int]], *, old_count: int
) -> dict[str, Any]:
    """Audit the actual old-clear/new-pay debt at one fixed dyadic epoch."""
    normalized = tuple(_validated_golomb(points) for points in rulers)
    if (
        not isinstance(old_count, int)
        or old_count < 2
        or old_count & (old_count - 1)
        or any(len(points) < 2 * old_count for points in normalized)
    ):
        raise ValueError("old_count must be a complete nontrivial dyadic epoch")
    category_counts = {"old_clear_only": 0, "new_pay_only": 0, "both": 0}
    minima: dict[str, tuple[Any, ...] | None] = {
        name: None for name in _ACTUAL_CANDIDATE_FIELDS
    }
    negative_counts = {name: 0 for name in _ACTUAL_CANDIDATE_FIELDS}
    ratio_minima: dict[str, tuple[Any, ...] | None] = {
        "global": None,
        "latest": None,
    }
    for points in normalized:
        event = renewal_dichotomy(points[: 2 * old_count], old_count=old_count)
        if event.ancestry_cleared and event.new_family_paid:
            category_counts["both"] += 1
            continue
        if event.new_family_paid:
            category_counts["new_pay_only"] += 1
            continue
        category_counts["old_clear_only"] += 1
        row = actual_renewal_comparison(points, old_count=old_count)
        for name, ratio in (
            ("global", row.global_density_to_innovation_ratio),
            ("latest", row.latest_density_to_innovation_ratio),
        ):
            candidate = (ratio, points, row.first_cross_threshold, row)
            current = ratio_minima[name]
            if current is None or candidate < current:
                ratio_minima[name] = candidate
        for name, field in _ACTUAL_CANDIDATE_FIELDS.items():
            margin = getattr(row, field)
            negative_counts[name] += margin < 0
            key = (margin, points, row.first_cross_threshold)
            current = minima[name]
            if current is None or key < current[:3]:
                minima[name] = (margin, points, row.first_cross_threshold, row)

    if category_counts["old_clear_only"] == 0:
        candidate_results: dict[str, Any] = {
            name: {
                "negative_count": 0,
                "survives_stated_scope": True,
                "minimum_witness": None,
                "vacuous_no_old_clear_only_event": True,
            }
            for name in _ACTUAL_CANDIDATE_FIELDS
        }
    else:
        candidate_results = {}
        for name, field in _ACTUAL_CANDIDATE_FIELDS.items():
            minimum = minima[name]
            if minimum is None:
                raise AssertionError("actual candidate minimum unexpectedly absent")
            row = minimum[3]
            candidate_results[name] = {
                "negative_count": negative_counts[name],
                "survives_stated_scope": negative_counts[name] == 0,
                "minimum_witness": {
                    "points": minimum[1],
                    "epoch": old_count,
                    "threshold": row.first_cross_threshold,
                    "margin": getattr(row, field),
                    "outstanding_demand": row.outstanding_demand,
                    "global_nonadjacent_reservoir_count": (
                        row.global_nonadjacent_reservoir_count
                    ),
                    "latest_shell_nonadjacent_reservoir_count": (
                        row.latest_shell_nonadjacent_reservoir_count
                    ),
                    "normalized_adjoint_innovation": (
                        row.normalized_adjoint_innovation
                    ),
                },
                "vacuous_no_old_clear_only_event": False,
            }
    return {
        "ruler_count": len(normalized),
        "epoch": old_count,
        "old_clear_only_count": category_counts["old_clear_only"],
        "new_pay_only_count": category_counts["new_pay_only"],
        "both_count": category_counts["both"],
        "candidate_results": candidate_results,
        "density_ratio_calibration": {
            "global_minimum_ratio": (
                ratio_minima["global"][0] if ratio_minima["global"] else None
            ),
            "global_minimum_points": (
                ratio_minima["global"][1] if ratio_minima["global"] else None
            ),
            "global_minimum_threshold": (
                ratio_minima["global"][2] if ratio_minima["global"] else None
            ),
            "latest_minimum_ratio": (
                ratio_minima["latest"][0] if ratio_minima["latest"] else None
            ),
            "latest_minimum_points": (
                ratio_minima["latest"][1] if ratio_minima["latest"] else None
            ),
            "latest_minimum_threshold": (
                ratio_minima["latest"][2] if ratio_minima["latest"] else None
            ),
        },
    }


def _actual_renewal_category_counts(
    rulers: Iterable[Sequence[int]],
) -> dict[str, int]:
    counts = {"event_count": 0, "old_clear_only": 0, "new_pay_only": 0, "both": 0}
    for points in rulers:
        marks = _validated_golomb(points)
        for epoch in dyadic_boundaries(len(marks)):
            if epoch < 2:
                continue
            event = renewal_dichotomy(marks[: 2 * epoch], old_count=epoch)
            counts["event_count"] += 1
            if event.ancestry_cleared and event.new_family_paid:
                counts["both"] += 1
            elif event.new_family_paid:
                counts["new_pay_only"] += 1
            else:
                counts["old_clear_only"] += 1
    return counts


def _one_step_survival_scope(rulers: Iterable[Sequence[int]]) -> dict[str, Any]:
    normalized = tuple(_validated_golomb(points, require_c1=True) for points in rulers)
    rows = tuple((len(_incremental_children(points)), points) for points in normalized)
    return {
        "root_count": len(rows),
        "total_child_count": sum(count for count, _ in rows),
        "zero_child_root_count": sum(count == 0 for count, _ in rows),
        "minimum_child_count": min(rows),
        "maximum_child_count": max(rows),
        "scope_is_exhaustive": True,
        "infinite_survival_inferred": False,
    }


def _encode(value: Any) -> Any:
    if isinstance(value, Fraction):
        return f"{value.numerator}/{value.denominator}"
    if isinstance(value, tuple):
        return [_encode(item) for item in value]
    if isinstance(value, list):
        return [_encode(item) for item in value]
    if isinstance(value, dict):
        return {key: _encode(item) for key, item in value.items()}
    return value


def build_certificate(source_certificate: str | Path) -> dict[str, Any]:
    """Build the deterministic finite Wave 8 certificate."""
    source_path = Path(source_certificate)
    four_mark_rulers = tuple(enumerate_compatible_four_mark_rulers())
    bounded_eight = bounded_golomb_exhaustion(mark_count=8, maximum_last_mark=40)
    actual_bounded_eight = bounded_golomb_exhaustion(mark_count=8, maximum_last_mark=45)
    fixtures = load_authenticated_wave6_fixtures(source_path)
    transformed = tuple(
        variant.points
        for points in fixtures.sixty_four_mark_points
        for variant in compatible_adjacent_gap_swaps(points)
    )
    authenticated = (
        tuple(COUNTEREXAMPLE_64_POINTS),
        *fixtures.sixty_four_mark_points,
        fixtures.one_hundred_twenty_eight_mark_points,
        *transformed,
    )

    rank_lag_counterexample = (0, 4, 10, 13, 15, 27, 34, 35)
    global_counterexample = (0, 3, 7, 13, 21, 22, 33, 38)
    actual_single_debt_counterexample = (0, 2, 5, 6, 14, 25, 32, 42)
    rank_lag_survival = critical_survival_audit(rank_lag_counterexample, depth=2)
    global_survival = critical_survival_audit(global_counterexample, depth=2)
    actual_single_debt_survival = critical_survival_audit(
        actual_single_debt_counterexample, depth=2
    )
    unrestricted_base = (0, 8, 24, 56, 58, 314, 318, 319)
    unrestricted_scale = 100
    unrestricted_points = tuple(unrestricted_scale * mark for mark in unrestricted_base)
    unrestricted_comparison = actual_renewal_comparison(
        unrestricted_points, old_count=4
    )

    bounded_c1_rulers = tuple(
        points for points in bounded_eight.rulers if all_prefix_c1(points)
    )
    payload: dict[str, Any] = {
        "schema": "wave8_survival_debt_probe_v1",
        "research_date": "2026-08-28",
        "purpose": (
            "exact finite falsification of survival-conditioned non-adjacent "
            "debt-repayment candidates and calibration against adjoint innovation"
        ),
        "candidate_definitions": {
            "certified_rank_lag_debt": (
                "max over cheap-side choices of U_certified-(P-new_adjacent) >= 0"
            ),
            "certified_reservoir_pays_full_tax": (
                "max over cheap-side choices of U_certified-P >= 0"
            ),
            "global_nonadjacent_debt": (
                "all actual unused non-adjacent differences below floor(T) "
                "minus adjacent debt is nonnegative"
            ),
            "latest_shell_nonadjacent_debt": (
                "the same assertion restricted to pairs born in the latest active shell"
            ),
            "certified_density_innovation": ("U_certified/T >= <H,Q_m/N_(2m)>"),
            "global_density_innovation": ("U_global/T >= <H,Q_m/N_(2m)>"),
            "actual_single_debt": (
                "at an old-clear/new-unpaid event, compare the actual one-family "
                "demand m-1 with global and latest-shell non-adjacent reservoirs"
            ),
        },
        "four_mark_c1_scope": {
            "scope": (
                "all normalized four-mark Golomb rulers obeying every C=1 "
                "prefix cap; every threshold with both dyadic epochs active"
            ),
            "scope_is_exhaustive": True,
            **audit_ruler_scope(four_mark_rulers, minimum_active_epochs=2),
            "one_step_survival": _one_step_survival_scope(four_mark_rulers),
        },
        "bounded_eight_mark_scope": {
            "scope": (
                "all normalized eight-mark Golomb rulers with terminal mark "
                "at most 40; every threshold with all three dyadic epochs active"
            ),
            "scope_is_exhaustive": True,
            "ruler_count": bounded_eight.ruler_count,
            "search_node_count": bounded_eight.search_node_count,
            "first_ruler": bounded_eight.first_ruler,
            "last_ruler": bounded_eight.last_ruler,
            **audit_ruler_scope(bounded_eight.rulers, minimum_active_epochs=3),
            "c1_subscope_one_step_survival": _one_step_survival_scope(
                bounded_c1_rulers
            ),
        },
        "authenticated_and_gap_swap_scope": {
            "scope": (
                "Wave 6 Hall counterexample, six authenticated 64-mark rulers, "
                "one authenticated 128-mark ruler, and all 23 retained legal "
                "single adjacent-gap swaps; every threshold with at least "
                "three active epochs"
            ),
            "source_certificate_file_sha256": fixtures.certificate_file_sha256,
            "gap_swap_count": len(transformed),
            **audit_ruler_scope(authenticated, minimum_active_epochs=3),
        },
        "actual_single_debt_bounded_eight_scope": {
            "scope": (
                "all normalized eight-mark Golomb rulers with terminal mark "
                "at most 45, scored at the m=4 first-cross renewal event"
            ),
            "scope_is_exhaustive": True,
            "search_node_count": actual_bounded_eight.search_node_count,
            **audit_actual_single_debt_scope(actual_bounded_eight.rulers, old_count=4),
        },
        "authenticated_actual_renewal_scope": {
            "scope": (
                "the same 31 authenticated/transformed rulers, with every "
                "available nontrivial dyadic epoch scored separately"
            ),
            **_actual_renewal_category_counts(authenticated),
            "finding": (
                "every audited event pays both actual sides; the non-adjacent "
                "single-debt test is vacuous on this fixture scope"
            ),
        },
        "unrestricted_scaling_no_go": {
            "base_points": unrestricted_base,
            "scale": unrestricted_scale,
            "points": unrestricted_points,
            "obeys_all_prefix_c1": all_prefix_c1(unrestricted_points),
            "comparison": asdict(unrestricted_comparison),
            "conclusion": (
                "both U_global/T and U_latest/T fail to dominate the exact "
                "adjoint innovation; the density candidate is false without "
                "a critical-envelope or infinite-survival hypothesis"
            ),
        },
        "finite_survival_counterexamples": {
            "certified_rank_lag": {
                "repayment": asdict(
                    repayment_audit(rank_lag_counterexample, Fraction(25, 2))
                ),
                "survival_depth_two": asdict(rank_lag_survival),
            },
            "global_nonadjacent": {
                "repayment": asdict(
                    repayment_audit(global_counterexample, Fraction(51, 4))
                ),
                "survival_depth_two": asdict(global_survival),
            },
            "actual_single_debt": {
                "repayment": asdict(
                    actual_renewal_comparison(
                        actual_single_debt_counterexample, old_count=4
                    )
                ),
                "survival_depth_two": asdict(actual_single_debt_survival),
            },
        },
        "conclusions": {
            "certified_rank_lag_repayment": (
                "refuted by an exact eight-mark C=1 prefix that has 61,427 "
                "depth-two critical extensions"
            ),
            "global_nonadjacent_repayment": (
                "refuted by an exact eight-mark C=1 prefix that has 61,448 "
                "depth-two critical extensions"
            ),
            "actual_single_debt_repayment": (
                "refuted even after actual-adjacent renewal reduces history "
                "to one family: an exact eight-mark C=1 prefix has demand 3, "
                "only 2 global and 1 latest-shell unused non-adjacent "
                "differences, and 59,361 depth-two critical extensions"
            ),
            "actual_single_debt_density_innovation": (
                "U/T dominates the exact adjoint innovation at all 1,250 "
                "old-clear-only events in the exhaustive terminal<=45 scope; "
                "this is a finite observation, not an asymptotic theorem"
            ),
            "global_density_innovation": (
                "not refuted in the bounded eight-mark or authenticated/swap "
                "scopes, but refuted by an unrestricted scaled Golomb ruler; "
                "no unbounded critical-branch claim"
            ),
            "finite_survival_is_not_infinite_survival": True,
            "erdos_1191_resolved": False,
            "infinite_extension_claimed": False,
        },
    }
    encoded = _encode(payload)
    canonical = json.dumps(encoded, sort_keys=True, separators=(",", ":"))
    encoded["certificate_sha256"] = sha256(canonical.encode("utf-8")).hexdigest()
    return encoded


def main() -> None:
    directory = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-certificate",
        type=Path,
        default=directory / "wave6_arithmetic_mining_certificate_2026-08-28.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=directory / "wave8_survival_debt_certificate_2026-08-28.json",
    )
    arguments = parser.parse_args()
    certificate = build_certificate(arguments.source_certificate)
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(certificate, sort_keys=True))


if __name__ == "__main__":
    main()
