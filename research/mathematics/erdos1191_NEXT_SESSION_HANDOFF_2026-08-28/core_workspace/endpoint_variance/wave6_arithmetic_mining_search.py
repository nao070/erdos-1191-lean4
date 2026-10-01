"""Exact arithmetic mining across dyadic birth epochs of nested rulers."""
from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from fractions import Fraction

from wave4_nested_search import independent_difference_audit


@dataclass(frozen=True)
class LagFamilyAudit:
    epoch: int
    category: str
    lag: int
    pairs: tuple[tuple[int, int], ...]
    differences: tuple[int, ...]
    demand: int
    distinct_count: int
    collision_deficit: int
    lower: int
    upper: int
    width: int


@dataclass(frozen=True)
class HallPressureAudit:
    lower: int
    upper: int
    width: int
    demand: int
    ratio: Fraction
    represented_epochs: tuple[int, ...]
    families: tuple[LagFamilyAudit, ...]


@dataclass(frozen=True)
class CategorySpectrumAudit:
    category: str
    pairs: tuple[tuple[int, int], ...]
    differences: tuple[int, ...]
    pair_count: int
    distinct_count: int
    collision_deficit: int
    lower: int
    upper: int
    width: int
    collisions: tuple[tuple[int, tuple[tuple[int, int], ...]], ...]


@dataclass(frozen=True)
class TransitionPackingAudit:
    old_count: int
    new_count: int
    old_new: CategorySpectrumAudit
    new_new: CategorySpectrumAudit
    overlap_lower: int | None
    overlap_upper: int | None
    overlap_width: int
    old_new_occupied_in_overlap: tuple[int, ...]
    new_new_occupied_in_overlap: tuple[int, ...]
    cross_collision_values: tuple[int, ...]


@dataclass(frozen=True)
class AdjacentHallPressureAudit:
    epochs: tuple[int, int]
    pressure: HallPressureAudit


@dataclass(frozen=True)
class ArithmeticWitnessAudit:
    points: tuple[int, ...]
    pair_count: int
    sorted_differences: tuple[int, ...]
    difference_collisions: tuple[
        tuple[int, tuple[tuple[int, int], ...]], ...
    ]
    is_golomb: bool
    families: tuple[LagFamilyAudit, ...]
    transitions: tuple[TransitionPackingAudit, ...]
    adjacent_nn_pressures: tuple[AdjacentHallPressureAudit, ...]
    all_epoch_nn_pressure: HallPressureAudit | None


def _validated_power_two_points(points: Sequence[int]) -> tuple[int, ...]:
    marks = tuple(points)
    if any(not isinstance(mark, int) for mark in marks):
        raise TypeError("points must be integers")
    if len(marks) < 2 or len(marks) & (len(marks) - 1):
        raise ValueError("the number of points must be a power of two at least two")
    if marks != tuple(sorted(set(marks))):
        raise ValueError("points must be strictly increasing")
    return marks


def birth_lag_families(points: Sequence[int]) -> tuple[LagFamilyAudit, ...]:
    """Partition every rank pair by birth epoch, category, and rank lag."""
    marks = _validated_power_two_points(points)
    grouped: dict[tuple[int, str, int], list[tuple[int, int, int]]] = {}
    for right in range(1, len(marks)):
        epoch = 1 << right.bit_length()
        boundary = epoch // 2
        for left in range(right):
            category = "ON" if left < boundary else "NN"
            grouped.setdefault((epoch, category, right - left), []).append(
                (left, right, marks[right] - marks[left])
            )

    keys = sorted(
        grouped,
        key=lambda key: (key[0], 0 if key[1] == "ON" else 1, key[2]),
    )
    rows: list[LagFamilyAudit] = []
    covered_pairs: list[tuple[int, int]] = []
    for epoch, category, lag in keys:
        entries = grouped[(epoch, category, lag)]
        pairs = tuple((left, right) for left, right, _ in entries)
        differences = tuple(difference for _, _, difference in entries)
        distinct_count = len(set(differences))
        rows.append(
            LagFamilyAudit(
                epoch=epoch,
                category=category,
                lag=lag,
                pairs=pairs,
                differences=differences,
                demand=len(entries),
                distinct_count=distinct_count,
                collision_deficit=len(entries) - distinct_count,
                lower=min(differences),
                upper=max(differences),
                width=max(differences) - min(differences) + 1,
            )
        )
        covered_pairs.extend(pairs)

    expected_count = len(marks) * (len(marks) - 1) // 2
    if len(covered_pairs) != expected_count or len(set(covered_pairs)) != expected_count:
        raise AssertionError("birth-lag families did not partition all rank pairs")
    return tuple(rows)


def _hall_rank(audit: HallPressureAudit) -> tuple[Fraction, int, int, int, int]:
    return (
        audit.ratio,
        audit.demand,
        -audit.width,
        -audit.lower,
        -audit.upper,
    )


def hall_pressure(
    families: Sequence[LagFamilyAudit],
    *,
    categories: Sequence[str] = ("ON", "NN"),
    epochs: Sequence[int] | None = None,
    min_family_demand: int = 2,
    min_epoch_count: int = 2,
) -> HallPressureAudit | None:
    """Maximize contained family demand divided by integer interval width."""
    allowed_categories = frozenset(categories)
    if not allowed_categories or not allowed_categories <= {"ON", "NN"}:
        raise ValueError("categories must be a nonempty subset of ON and NN")
    if not isinstance(min_family_demand, int) or min_family_demand < 1:
        raise ValueError("min_family_demand must be a positive integer")
    if not isinstance(min_epoch_count, int) or min_epoch_count < 1:
        raise ValueError("min_epoch_count must be a positive integer")
    allowed_epochs = None if epochs is None else frozenset(epochs)
    eligible = tuple(
        family
        for family in families
        if family.category in allowed_categories
        and (allowed_epochs is None or family.epoch in allowed_epochs)
        and family.demand >= min_family_demand
    )
    if not eligible:
        return None
    endpoints = tuple(
        sorted(
            {family.lower for family in eligible}
            | {family.upper for family in eligible}
        )
    )
    best: HallPressureAudit | None = None
    for lower in endpoints:
        for upper in endpoints:
            if upper < lower:
                continue
            contained = tuple(
                family
                for family in eligible
                if lower <= family.lower and family.upper <= upper
            )
            represented_epochs = tuple(
                sorted({family.epoch for family in contained})
            )
            if len(represented_epochs) < min_epoch_count:
                continue
            demand = sum(family.demand for family in contained)
            width = upper - lower + 1
            candidate = HallPressureAudit(
                lower=lower,
                upper=upper,
                width=width,
                demand=demand,
                ratio=Fraction(demand, width),
                represented_epochs=represented_epochs,
                families=contained,
            )
            if best is None or _hall_rank(candidate) > _hall_rank(best):
                best = candidate
    return best


def _category_spectrum(
    marks: tuple[int, ...],
    category: str,
    pairs: tuple[tuple[int, int], ...],
) -> CategorySpectrumAudit:
    by_difference: dict[int, list[tuple[int, int]]] = {}
    for left, right in pairs:
        by_difference.setdefault(marks[right] - marks[left], []).append(
            (left, right)
        )
    differences = tuple(sorted(by_difference))
    if not differences:
        raise ValueError("a transition category must contain at least one pair")
    collisions = tuple(
        (difference, tuple(by_difference[difference]))
        for difference in differences
        if len(by_difference[difference]) > 1
    )
    return CategorySpectrumAudit(
        category=category,
        pairs=pairs,
        differences=differences,
        pair_count=len(pairs),
        distinct_count=len(differences),
        collision_deficit=len(pairs) - len(differences),
        lower=differences[0],
        upper=differences[-1],
        width=differences[-1] - differences[0] + 1,
        collisions=collisions,
    )


def transition_packing(
    points: Sequence[int], *, new_count: int
) -> TransitionPackingAudit:
    """Audit whole old-new and new-new spectra for one dyadic transition."""
    marks = _validated_power_two_points(points)
    if (
        not isinstance(new_count, int)
        or new_count < 4
        or new_count > len(marks)
        or new_count & (new_count - 1)
    ):
        raise ValueError(
            "new_count must be a power of two from four through len(points)"
        )
    prefix = marks[:new_count]
    old_count = new_count // 2
    old_new_pairs = tuple(
        (left, right)
        for left in range(old_count)
        for right in range(old_count, new_count)
    )
    new_new_pairs = tuple(
        (left, right)
        for left in range(old_count, new_count)
        for right in range(left + 1, new_count)
    )
    old_new = _category_spectrum(prefix, "ON", old_new_pairs)
    new_new = _category_spectrum(prefix, "NN", new_new_pairs)
    overlap_lower = max(old_new.lower, new_new.lower)
    overlap_upper = min(old_new.upper, new_new.upper)
    if overlap_upper < overlap_lower:
        stored_lower: int | None = None
        stored_upper: int | None = None
        overlap_width = 0
        old_new_occupied: tuple[int, ...] = ()
        new_new_occupied: tuple[int, ...] = ()
    else:
        stored_lower = overlap_lower
        stored_upper = overlap_upper
        overlap_width = overlap_upper - overlap_lower + 1
        old_new_occupied = tuple(
            value
            for value in old_new.differences
            if overlap_lower <= value <= overlap_upper
        )
        new_new_occupied = tuple(
            value
            for value in new_new.differences
            if overlap_lower <= value <= overlap_upper
        )
    cross_collision_values = tuple(
        sorted(set(old_new.differences) & set(new_new.differences))
    )
    return TransitionPackingAudit(
        old_count=old_count,
        new_count=new_count,
        old_new=old_new,
        new_new=new_new,
        overlap_lower=stored_lower,
        overlap_upper=stored_upper,
        overlap_width=overlap_width,
        old_new_occupied_in_overlap=old_new_occupied,
        new_new_occupied_in_overlap=new_new_occupied,
        cross_collision_values=cross_collision_values,
    )


def audit_arithmetic_witness(
    points: Sequence[int], *, require_golomb: bool = True
) -> ArithmeticWitnessAudit:
    """Recompute all differences, birth-lag rows, and packing statistics."""
    marks = _validated_power_two_points(points)
    difference_audit = independent_difference_audit(marks)
    if require_golomb and not difference_audit.is_golomb:
        raise ValueError("the arithmetic witness is not a Golomb ruler")
    families = birth_lag_families(marks)
    pair_differences = {
        pair: difference
        for family in families
        for pair, difference in zip(family.pairs, family.differences)
    }
    expected_pair_count = len(marks) * (len(marks) - 1) // 2
    if len(pair_differences) != expected_pair_count:
        raise AssertionError("birth-lag rows did not retain every pair")
    for (left, right), difference in pair_differences.items():
        if difference != marks[right] - marks[left]:
            raise AssertionError("a stored family difference is inconsistent")

    sizes: list[int] = []
    size = 4
    while size <= len(marks):
        sizes.append(size)
        size *= 2
    transitions = tuple(
        transition_packing(marks, new_count=new_count)
        for new_count in sizes
    )
    adjacent_pressures: list[AdjacentHallPressureAudit] = []
    for older_epoch, newer_epoch in zip(sizes[1:], sizes[2:]):
        pressure = hall_pressure(
            families,
            categories=("NN",),
            epochs=(older_epoch, newer_epoch),
            min_family_demand=2,
            min_epoch_count=2,
        )
        if pressure is None:
            raise AssertionError("an adjacent NN pressure was unexpectedly empty")
        adjacent_pressures.append(
            AdjacentHallPressureAudit(
                epochs=(older_epoch, newer_epoch), pressure=pressure
            )
        )
    all_epoch_pressure = hall_pressure(
        families,
        categories=("NN",),
        min_family_demand=2,
        min_epoch_count=2,
    )
    if difference_audit.is_golomb:
        pressures = [row.pressure for row in adjacent_pressures]
        if all_epoch_pressure is not None:
            pressures.append(all_epoch_pressure)
        if any(pressure.ratio > 1 for pressure in pressures):
            raise AssertionError("a Golomb ruler violated the Hall packing bound")
        if any(family.collision_deficit for family in families):
            raise AssertionError("a Golomb family contained a repeated difference")
    return ArithmeticWitnessAudit(
        points=marks,
        pair_count=difference_audit.pair_count,
        sorted_differences=difference_audit.sorted_differences,
        difference_collisions=difference_audit.collisions,
        is_golomb=difference_audit.is_golomb,
        families=families,
        transitions=transitions,
        adjacent_nn_pressures=tuple(adjacent_pressures),
        all_epoch_nn_pressure=all_epoch_pressure,
    )
