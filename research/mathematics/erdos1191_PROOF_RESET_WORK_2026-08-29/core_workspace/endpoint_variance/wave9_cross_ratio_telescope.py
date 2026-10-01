"""Formal and numerical audit of the weighted gap cross-ratio telescope.

For genuine nonadjacent gaps ``h_i`` and ``h_j``, put

    M = a_(j-1) - a_i,
    D = a_j - a_(i-1),

and

    C_(i,j) = log(((M+h_i)(M+h_j))/(M D)).

The ratio is ``1 + h_i h_j/(M D)``.  Therefore

    h_i h_j / D^2 <= C_(i,j).

With the quadratic rank weight ``((j-i)/n)^2``, the sum of these positive
cross-ratios has an exact summation-by-parts formula whose interior
coefficients are all nonpositive.  This module audits the coefficient
identity independently of floating-point logarithms and checks the analytic
inequalities numerically on concrete rulers.

The resulting ``O(log diameter)`` one-prefix bound does *not* prove P15.
In particular, it supplies no sublogarithmic cross-epoch estimate by itself.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping, Sequence
from fractions import Fraction
from math import comb, fsum, gcd, lgamma, log

Interval = tuple[int, int]


def _validated_marks(points: Sequence[int]) -> tuple[int, ...]:
    marks = tuple(points)
    if (
        len(marks) < 4
        or marks[0] != 0
        or marks != tuple(sorted(set(marks)))
        or any(not isinstance(mark, int) for mark in marks)
    ):
        raise ValueError(
            "points must be at least four normalized strictly increasing integers"
        )
    return marks


def formal_cross_ratio_coefficients(count: int) -> dict[Interval, int]:
    """Return ``count^2`` times every formal log-difference coefficient.

    The returned dictionary represents

        sum_(i+2<=j) (j-i)^2 log(
            (a_(j-1)-a_(i-1))(a_j-a_i)
            / ((a_(j-1)-a_i)(a_j-a_(i-1)))
        ).

    It is computed directly from the four terms of each cross-ratio and is
    deliberately independent of the closed coefficient formula below.
    """
    if not isinstance(count, int) or count < 4:
        raise ValueError("count must be an integer at least four")
    coefficients: defaultdict[Interval, int] = defaultdict(int)
    for left_gap in range(1, count - 2):
        for right_gap in range(left_gap + 2, count):
            weight = (right_gap - left_gap) ** 2
            coefficients[left_gap - 1, right_gap - 1] += weight
            coefficients[left_gap, right_gap] += weight
            coefficients[left_gap, right_gap - 1] -= weight
            coefficients[left_gap - 1, right_gap] -= weight
    return {interval: value for interval, value in coefficients.items() if value}


def closed_cross_ratio_coefficients(count: int) -> dict[Interval, int]:
    """Return the closed boundary/interior coefficient formula.

    Positive coefficients occur only on the left and right boundaries.
    The full-span and every strict-interior coefficient are negative.
    """
    if not isinstance(count, int) or count < 4:
        raise ValueError("count must be an integer at least four")
    coefficients: defaultdict[Interval, int] = defaultdict(int)

    coefficients[0, 2] += 4
    for right in range(3, count - 1):
        coefficients[0, right] += 2 * right - 1

    coefficients[count - 3, count - 1] += 4
    for left in range(1, count - 3):
        lag = count - 1 - left
        coefficients[left, count - 1] += 2 * lag - 1

    coefficients[0, count - 1] -= (count - 2) ** 2
    for left in range(1, count - 2):
        coefficients[left, left + 1] -= 4
    for left in range(1, count - 3):
        coefficients[left, left + 2] -= 1
    for left in range(1, count - 4):
        for right in range(left + 3, count - 1):
            coefficients[left, right] -= 2

    return {interval: value for interval, value in coefficients.items() if value}


def coefficient_sign_mass(
    coefficients: Mapping[Interval, int],
) -> tuple[int, int]:
    """Return the total positive and absolute negative coefficient mass."""
    positive = sum(value for value in coefficients.values() if value > 0)
    negative = -sum(value for value in coefficients.values() if value < 0)
    return positive, negative


def cross_ratio_argument(
    points: Sequence[int], *, left_gap: int, right_gap: int
) -> Fraction:
    """Return the exact rational argument of one positive cross-ratio."""
    marks = _validated_marks(points)
    if not 1 <= left_gap < right_gap - 1 < len(marks) - 1:
        raise ValueError("the two genuine gap indices must be nonadjacent")
    middle = marks[right_gap - 1] - marks[left_gap]
    outer = marks[right_gap] - marks[left_gap - 1]
    left_outer = marks[right_gap - 1] - marks[left_gap - 1]
    right_outer = marks[right_gap] - marks[left_gap]
    return Fraction(left_outer * right_outer, middle * outer)


def exact_pair_lower_ratio(
    points: Sequence[int], *, left_gap: int, right_gap: int
) -> Fraction:
    """Return ``h_i h_j / D^2``, the exact lower target for ``log CR``."""
    marks = _validated_marks(points)
    if not 1 <= left_gap < right_gap - 1 < len(marks) - 1:
        raise ValueError("the two genuine gap indices must be nonadjacent")
    left_weight = marks[left_gap] - marks[left_gap - 1]
    right_weight = marks[right_gap] - marks[right_gap - 1]
    outer = marks[right_gap] - marks[left_gap - 1]
    return Fraction(left_weight * right_weight, outer * outer)


def weighted_cross_ratio_sum(points: Sequence[int]) -> float:
    """Evaluate the positive weighted cross-ratio sum using real logs."""
    marks = _validated_marks(points)
    count = len(marks)
    return fsum(
        ((right - left) / count) ** 2
        * log(float(cross_ratio_argument(marks, left_gap=left, right_gap=right)))
        for left in range(1, count - 2)
        for right in range(left + 2, count)
    )


def coefficient_expansion_sum(points: Sequence[int]) -> float:
    """Evaluate the independently expanded formal log-difference sum."""
    marks = _validated_marks(points)
    count = len(marks)
    coefficients = closed_cross_ratio_coefficients(count)
    return fsum(
        coefficient * log(marks[right] - marks[left]) / (count * count)
        for (left, right), coefficient in coefficients.items()
    )


def weighted_cross_ratio_boundary_bound(points: Sequence[int]) -> float:
    """Return ``((n-2)/n)^2 log(a_(n-1))``.

    This upper bound keeps the negative full-span term, bounds both positive
    boundary fans by the full span, and drops every other negative term.
    """
    marks = _validated_marks(points)
    count = len(marks)
    return ((count - 2) / count) ** 2 * log(marks[-1])


def _has_distinct_positive_differences(marks: tuple[int, ...]) -> bool:
    differences = {
        marks[right] - marks[left]
        for right in range(1, len(marks))
        for left in range(right)
    }
    return len(differences) == comb(len(marks), 2)


def golomb_distinctness_cross_ratio_bound(points: Sequence[int]) -> float:
    """Sharpen the boundary bound using every strict-interior difference.

    Let ``delta`` be the gcd of the strict-interior one-gap differences
    ``h_2,...,h_(n-2)`` and put ``K=binom(n-2, 2)``.  After division by
    ``delta``, all strict-interior interval differences remain distinct positive
    integers.  The negative interior part of the formal
    telescope assigns coefficient 4 to ``A=n-3`` adjacent intervals,
    coefficient 1 to ``B=n-4`` lag-two intervals, and coefficient 2 to all
    other strict-interior intervals.  Since their ``K`` differences are
    distinct positive integers, the rearrangement inequality gives the exact
    spectrum-only minimum

        I_min = 2 log(A!) + log((K-B)!) + log(K!).

    Consequently

        S_n <= ((n-2)/n)^2 log(D/delta) - I_min/n^2.

    As ``n`` tends to infinity this is

        log(D/(delta n^2)) + 1 + log(2) + o(1).

    Thus a critical diameter ``D=O(n^2 log n)`` gives ``S_n=O(log log n)``.
    This one-prefix estimate still does not sum to P15 across dyadic epochs.
    """
    marks = _validated_marks(points)
    if not _has_distinct_positive_differences(marks):
        raise ValueError("points must form a Golomb ruler")
    count = len(marks)
    strict_interior_gap_gcd = 0
    for index in range(2, count - 1):
        strict_interior_gap_gcd = gcd(
            strict_interior_gap_gcd,
            marks[index] - marks[index - 1],
        )
    strict_interior_count = comb(count - 2, 2)
    adjacent_count = count - 3
    lag_two_count = count - 4
    interior_minimum = (
        2 * lgamma(adjacent_count + 1)
        + lgamma(strict_interior_count - lag_two_count + 1)
        + lgamma(strict_interior_count + 1)
    )
    return ((count - 2) / count) ** 2 * log(
        marks[-1] / strict_interior_gap_gcd
    ) - interior_minimum / (count * count)


def genuine_nonadjacent_scalar_energy(points: Sequence[int]) -> Fraction:
    """Return the full-prefix nonadjacent scalar rank energy.

    The normalization matches the project convention ``N=a_(n-1)+1``.
    This contains all genuine nonadjacent pairs, rather than one birth shell,
    and is bounded above by ``weighted_cross_ratio_sum``.
    """
    marks = _validated_marks(points)
    count = len(marks)
    modulus = marks[-1] + 1
    gaps = tuple(marks[index] - marks[index - 1] for index in range(1, count))
    return sum(
        (
            Fraction(
                gaps[left - 1] * gaps[right - 1] * (right - left) ** 2,
                modulus * modulus * count * count,
            )
            for left in range(1, count - 2)
            for right in range(left + 2, count)
        ),
        Fraction(0),
    )


def audit_cross_ratio_telescope(points: Sequence[int]) -> dict[str, float | int]:
    """Run the complete formal and numerical audit for one point list."""
    marks = _validated_marks(points)
    count = len(marks)
    formal = formal_cross_ratio_coefficients(count)
    closed = closed_cross_ratio_coefficients(count)
    if formal != closed:
        raise AssertionError("the formal and closed coefficient formulas disagree")
    positive, negative = coefficient_sign_mass(closed)
    if positive != negative or positive != 2 * (count - 2) ** 2:
        raise AssertionError("unexpected coefficient sign mass")

    direct = weighted_cross_ratio_sum(marks)
    expanded = coefficient_expansion_sum(marks)
    boundary = weighted_cross_ratio_boundary_bound(marks)
    distinctness_bound = (
        golomb_distinctness_cross_ratio_bound(marks)
        if _has_distinct_positive_differences(marks)
        else None
    )
    scalar = float(genuine_nonadjacent_scalar_energy(marks))
    tolerance = 1e-12 * max(1.0, abs(direct), abs(expanded), abs(boundary))
    if abs(direct - expanded) > tolerance:
        raise AssertionError("the numerical cross-ratio telescope failed")
    if scalar > direct + tolerance:
        raise AssertionError("the scalar energy escaped its cross-ratio majorant")
    if direct > boundary + tolerance:
        raise AssertionError("the boundary upper bound failed")
    if distinctness_bound is not None and direct > distinctness_bound + tolerance:
        raise AssertionError("the Golomb distinctness upper bound failed")

    return {
        "count": count,
        "nonzero_coefficients": len(closed),
        "positive_coefficient_mass": positive,
        "negative_coefficient_mass": negative,
        "scalar_energy": scalar,
        "weighted_cross_ratio_sum": direct,
        "coefficient_expansion_sum": expanded,
        "boundary_upper_bound": boundary,
        "golomb_distinctness_upper_bound": distinctness_bound,
    }
