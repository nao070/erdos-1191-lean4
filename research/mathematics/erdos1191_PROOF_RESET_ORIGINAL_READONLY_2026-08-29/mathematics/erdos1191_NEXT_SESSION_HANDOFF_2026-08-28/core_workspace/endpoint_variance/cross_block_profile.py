"""Exact cross-block packing data for Sidon diameter profiles.

The accompanying proof note derives the asymptotic consequences.  This module
keeps the finite identities and packing inequalities in exact integer and
``Fraction`` arithmetic.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from sidon_block_variance import is_golomb_ruler


def _validated_sidon_points(points: tuple[int, ...]) -> tuple[int, ...]:
    marks = tuple(points)
    if len(marks) < 2:
        raise ValueError("at least two marks are required")
    if any(not isinstance(mark, int) for mark in marks):
        raise TypeError("marks must be integers")
    if tuple(sorted(marks)) != marks or len(set(marks)) != len(marks):
        raise ValueError("marks must be strictly increasing")
    if not is_golomb_ruler(marks):
        raise ValueError("the cross-block packing lemmas require a Sidon ruler")
    return marks


def prefix_moduli(points: tuple[int, ...]) -> tuple[int, ...]:
    """Return ``N_0=0`` and ``N_r=a[r-1]-a[0]+1`` for every prefix."""
    marks = _validated_sidon_points(points)
    return (0,) + tuple(mark - marks[0] + 1 for mark in marks)


def diameter_profile_discrepancy(points: tuple[int, ...]) -> Fraction:
    """Return ``max_r |N_r/N_M-r/M|`` exactly.

    If ``Delta`` is the exact Kolmogorov discrepancy of the diameter-gap
    measure, then ``epsilon <= Delta <= epsilon + 1/M``.
    """
    marks = _validated_sidon_points(points)
    moduli = prefix_moduli(marks)
    count = len(marks)
    modulus = moduli[-1]
    return max(
        abs(Fraction(moduli[index], modulus) - Fraction(index, count))
        for index in range(count + 1)
    )


@dataclass(frozen=True)
class CrossBandWitness:
    left_start: int
    left_stop: int
    right_start: int
    right_stop: int
    difference_count: int
    minimum_difference: int
    maximum_difference: int
    band_length: int
    span_sum_plus_one: int


def cross_band_witness(
    points: tuple[int, ...],
    left_start: int,
    left_stop: int,
    right_start: int,
    right_stop: int,
) -> CrossBandWitness:
    """Audit one ordered rank rectangle and its exact containing band."""
    marks = _validated_sidon_points(points)
    indices = (left_start, left_stop, right_start, right_stop)
    if any(not isinstance(index, int) for index in indices):
        raise TypeError("rank endpoints must be integers")
    if not (
        0 <= left_start < left_stop <= right_start < right_stop <= len(marks)
    ):
        raise ValueError("require two nonempty ordered disjoint rank intervals")

    differences = tuple(
        marks[right] - marks[left]
        for left in range(left_start, left_stop)
        for right in range(right_start, right_stop)
    )
    expected_count = (left_stop - left_start) * (right_stop - right_start)
    if len(differences) != expected_count or len(set(differences)) != expected_count:
        raise AssertionError("Sidon cross-spectrum cardinality failed")

    minimum = marks[right_start] - marks[left_stop - 1]
    maximum = marks[right_stop - 1] - marks[left_start]
    band_length = maximum - minimum + 1
    span_sum_plus_one = (
        marks[left_stop - 1]
        - marks[left_start]
        + marks[right_stop - 1]
        - marks[right_start]
        + 1
    )
    if min(differences) != minimum or max(differences) != maximum:
        raise AssertionError("literal cross-spectrum endpoints failed")
    if band_length != span_sum_plus_one or expected_count > band_length:
        raise AssertionError("cross-band packing inequality failed")
    return CrossBandWitness(
        left_start=left_start,
        left_stop=left_stop,
        right_start=right_start,
        right_stop=right_stop,
        difference_count=expected_count,
        minimum_difference=minimum,
        maximum_difference=maximum,
        band_length=band_length,
        span_sum_plus_one=span_sum_plus_one,
    )


@dataclass(frozen=True)
class SameLagPackingWitness:
    mark_count: int
    block_count: int
    block_size: int
    lag: int
    difference_count: int
    exact_global_band_length: int
    exact_error_formula_band_length: Fraction
    discrepancy: Fraction
    discrepancy_band_upper_bound: Fraction
    bands: tuple[CrossBandWitness, ...]


def same_lag_packing_witness(
    points: tuple[int, ...], block_count: int, lag: int
) -> SameLagPackingWitness:
    """Return the exact common-band audit for all block pairs of one lag."""
    marks = _validated_sidon_points(points)
    count = len(marks)
    if not isinstance(block_count, int) or not isinstance(lag, int):
        raise TypeError("block_count and lag must be integers")
    if block_count < 2 or count % block_count:
        raise ValueError("block_count must divide the number of marks")
    if not 1 <= lag < block_count:
        raise ValueError("require 1 <= lag < block_count")

    block_size = count // block_count
    moduli = prefix_moduli(marks)
    modulus = moduli[-1]
    errors = tuple(
        Fraction(moduli[index], modulus) - Fraction(index, count)
        for index in range(count + 1)
    )
    discrepancy = max(abs(error) for error in errors)

    bands = []
    lower_errors = []
    upper_errors = []
    all_differences: set[int] = set()
    for block in range(block_count - lag):
        left_start = block * block_size
        left_stop = (block + 1) * block_size
        right_start = (block + lag) * block_size
        right_stop = (block + lag + 1) * block_size
        band = cross_band_witness(
            marks,
            left_start,
            left_stop,
            right_start,
            right_stop,
        )
        bands.append(band)

        lower_error = errors[right_start + 1] - errors[left_stop]
        upper_error = errors[right_stop] - errors[left_start + 1]
        lower_errors.append(lower_error)
        upper_errors.append(upper_error)
        formula_minimum = modulus * (
            Fraction(lag - 1, block_count)
            + Fraction(1, count)
            + lower_error
        )
        formula_maximum = modulus * (
            Fraction(lag + 1, block_count)
            - Fraction(1, count)
            + upper_error
        )
        if formula_minimum != band.minimum_difference:
            raise AssertionError("same-lag minimum endpoint formula failed")
        if formula_maximum != band.maximum_difference:
            raise AssertionError("same-lag maximum endpoint formula failed")

        for left in range(left_start, left_stop):
            for right in range(right_start, right_stop):
                difference = marks[right] - marks[left]
                if difference in all_differences:
                    raise AssertionError("same-lag spectra were not disjoint")
                all_differences.add(difference)

    exact_global_band_length = (
        max(band.maximum_difference for band in bands)
        - min(band.minimum_difference for band in bands)
        + 1
    )
    exact_formula = modulus * (
        Fraction(2, block_count)
        - Fraction(2, count)
        + max(upper_errors)
        - min(lower_errors)
    ) + 1
    coarse_upper = modulus * (
        Fraction(2, block_count)
        - Fraction(2, count)
        + 4 * discrepancy
    ) + 1
    expected_count = (block_count - lag) * block_size * block_size
    if len(all_differences) != expected_count:
        raise AssertionError("same-lag difference count failed")
    if exact_formula != exact_global_band_length:
        raise AssertionError("exact same-lag global band formula failed")
    if expected_count > exact_global_band_length or exact_formula > coarse_upper:
        raise AssertionError("same-lag common-band packing failed")

    return SameLagPackingWitness(
        mark_count=count,
        block_count=block_count,
        block_size=block_size,
        lag=lag,
        difference_count=expected_count,
        exact_global_band_length=exact_global_band_length,
        exact_error_formula_band_length=exact_formula,
        discrepancy=discrepancy,
        discrepancy_band_upper_bound=coarse_upper,
        bands=tuple(bands),
    )


@dataclass(frozen=True)
class DyadicTreeNode:
    start: int
    stop: int
    child_size: int
    cross_difference_count: int
    span: int
    running_count: int


@dataclass(frozen=True)
class DyadicTreeCarlesonWitness:
    mark_count: int
    total_cross_differences: int
    weighted_span_sum: Fraction
    running_count_upper_sum: Fraction
    nodes: tuple[DyadicTreeNode, ...]


def dyadic_tree_carleson_witness(
    points: tuple[int, ...],
) -> DyadicTreeCarlesonWitness:
    """Audit the dyadic child-spectrum partition and rational packing chain."""
    marks = _validated_sidon_points(points)
    count = len(marks)
    if count & (count - 1):
        raise ValueError("the dyadic tree requires a power-of-two mark count")

    raw_nodes: list[tuple[int, int, int, int, int]] = []

    def visit(start: int, stop: int) -> None:
        length = stop - start
        if length == 1:
            return
        middle = start + length // 2
        child_size = length // 2
        cross_count = child_size * child_size
        span = marks[stop - 1] - marks[start]
        raw_nodes.append((start, stop, child_size, cross_count, span))
        visit(start, middle)
        visit(middle, stop)

    visit(0, count)
    raw_nodes.sort(key=lambda record: record[-1])
    running = 0
    nodes = []
    weighted_span_sum = Fraction(0)
    running_count_upper_sum = Fraction(0)
    for start, stop, child_size, cross_count, span in raw_nodes:
        running += cross_count
        if span < running:
            raise AssertionError("ordered cross-spectrum packing failed")
        weighted_span_sum += Fraction(cross_count, span)
        running_count_upper_sum += Fraction(cross_count, running)
        nodes.append(
            DyadicTreeNode(
                start=start,
                stop=stop,
                child_size=child_size,
                cross_difference_count=cross_count,
                span=span,
                running_count=running,
            )
        )

    expected_total = count * (count - 1) // 2
    if running != expected_total or len(nodes) != count - 1:
        raise AssertionError("dyadic spectra did not partition all rank pairs")
    if weighted_span_sum > running_count_upper_sum:
        raise AssertionError("dyadic rational Carleson chain failed")
    return DyadicTreeCarlesonWitness(
        mark_count=count,
        total_cross_differences=running,
        weighted_span_sum=weighted_span_sum,
        running_count_upper_sum=running_count_upper_sum,
        nodes=tuple(nodes),
    )


def profile_discrepancy_lower_bound(
    total_count: int,
    block_count: int,
    old_prefix_upper_bound: int,
) -> Fraction:
    """Return the exact lower bound from cross-block packing and an old bound.

    If ``M=qm`` and ``N_m <= old_prefix_upper_bound``, Sidon uniqueness gives

    ``epsilon_M >= 1/q - old_bound/(binom(q,2)*m**2+1)``.
    """
    values = (total_count, block_count, old_prefix_upper_bound)
    if any(not isinstance(value, int) for value in values):
        raise TypeError("all inputs must be integers")
    if total_count < 2 or block_count < 2 or total_count % block_count:
        raise ValueError("block_count must divide total_count")
    if old_prefix_upper_bound < 1:
        raise ValueError("old_prefix_upper_bound must be positive")
    block_size = total_count // block_count
    cross_count = block_count * (block_count - 1) // 2 * block_size**2
    return Fraction(1, block_count) - Fraction(
        old_prefix_upper_bound,
        cross_count + 1,
    )
