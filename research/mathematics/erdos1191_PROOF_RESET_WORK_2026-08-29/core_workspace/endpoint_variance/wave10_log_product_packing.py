"""Hereditary log-product packing for dyadic cross-ratio birth shells.

Every positive difference of a Golomb ruler is a distinct positive integer.
Consequently any selected family of ``M`` differences has product at least
``M!``.  More generally, if the selected differences carry nonnegative
rational weights, the rearrangement inequality gives an exact weighted
product floor after the denominators are cleared.

This module aligns that elementary but global fact with the exact Abel
coefficients of the genuine cross-ratio birth shell.  It is a proof audit and
finite falsification aid; it does not prove P15 or Erdős Problem #1191.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping, Sequence
from fractions import Fraction
from functools import reduce
from math import factorial, fsum, gcd, log

GapInterval = tuple[int, int]


def _validated_marks(
    points: Sequence[int], *, minimum_count: int = 4
) -> tuple[int, ...]:
    marks = tuple(points)
    if (
        len(marks) < minimum_count
        or marks[0] != 0
        or marks != tuple(sorted(set(marks)))
        or any(not isinstance(mark, int) for mark in marks)
    ):
        raise ValueError("points must be normalized strictly increasing integers")
    return marks


def is_golomb(points: Sequence[int]) -> bool:
    """Return whether all positive differences are distinct."""
    marks = _validated_marks(points)
    differences = {
        marks[right] - marks[left]
        for right in range(1, len(marks))
        for left in range(right)
    }
    return len(differences) == len(marks) * (len(marks) - 1) // 2


def formal_birth_shell_coefficients(count: int) -> dict[GapInterval, int]:
    """Return ``count**2`` times the direct four-origin shell coefficients.

    Gap interval ``(p,q)`` represents ``D_(p,q)=a_q-a_(p-1)``.  The shell is
    the dyadic update ``m=count/2 -> count``.
    """
    if not isinstance(count, int) or count < 8 or count % 2:
        raise ValueError("count must be an even integer at least eight")
    shell_start = count // 2
    coefficients: defaultdict[GapInterval, int] = defaultdict(int)
    for left_gap in range(1, count - 2):
        for right_gap in range(max(shell_start, left_gap + 2), count):
            weight = (right_gap - left_gap) ** 2
            coefficients[left_gap, right_gap - 1] += weight
            coefficients[left_gap + 1, right_gap] += weight
            coefficients[left_gap + 1, right_gap - 1] -= weight
            coefficients[left_gap, right_gap] -= weight
    return {interval: value for interval, value in coefficients.items() if value}


def closed_birth_shell_coefficients(count: int) -> dict[GapInterval, int]:
    """Return the closed sign-classified dyadic shell coefficients."""
    if not isinstance(count, int) or count < 8 or count % 2:
        raise ValueError("count must be an even integer at least eight")
    m = count // 2
    final_gap = count - 1
    coefficients: defaultdict[GapInterval, int] = defaultdict(int)

    # Positive left-prefix boundary.
    coefficients[1, m - 1] += (m - 1) ** 2
    for right in range(m, final_gap):
        coefficients[1, right] += 2 * right - 1

    # Positive terminal-suffix boundary.
    coefficients[final_gap - 1, final_gap] += 4
    for length in range(3, final_gap):
        left = final_gap - length + 1
        coefficients[left, final_gap] += 2 * length - 1

    # Negative full span.
    coefficients[1, final_gap] -= (count - 2) ** 2

    # Negative lower boundary ending immediately before the newborn shell.
    for left in range(2, m):
        length = m - left
        coefficients[left, m - 1] -= 4 if length == 1 else 2 * length + 1

    # Negative bulk with right endpoint inside, but not at the end of, shell.
    for right in range(m, final_gap):
        for left in range(2, right + 1):
            length = right - left + 1
            magnitude = 4 if length == 1 else 1 if length == 2 else 2
            coefficients[left, right] -= magnitude

    return {interval: value for interval, value in coefficients.items() if value}


def coefficient_sign_mass(
    coefficients: Mapping[GapInterval, int],
) -> tuple[int, int]:
    """Return positive and absolute negative coefficient masses."""
    positive = sum(value for value in coefficients.values() if value > 0)
    negative = -sum(value for value in coefficients.values() if value < 0)
    return positive, negative


def negative_bulk_coefficients(count: int) -> dict[GapInterval, int]:
    """Return positive magnitudes of all negative non-full-span coefficients."""
    coefficients = closed_birth_shell_coefficients(count)
    full_span = (1, count - 1)
    return {
        interval: -value
        for interval, value in coefficients.items()
        if value < 0 and interval != full_span
    }


def negative_bulk_profile(m: int) -> dict[str, int]:
    """Return the exact coefficient-multiset counts for ``m -> 2m``.

    The coefficients here are scaled by ``(2m)**2``.
    """
    if not isinstance(m, int) or m < 4:
        raise ValueError("m must be an integer at least four")
    return {
        "ramp_count": m - 3,
        "weight_four_count": m,
        "weight_two_count": (m - 1) * (3 * m - 8) // 2,
        "weight_one_count": m - 1,
        "interval_count": m * (3 * m - 5) // 2,
        "scaled_mass": 4 * (m - 1) ** 2,
    }


def single_shell_rearrangement_floor(m: int) -> float:
    """Return the exact coefficient-multiset log floor for one shell."""
    count = 2 * m
    weights = sorted(negative_bulk_coefficients(count).values(), reverse=True)
    return fsum(
        Fraction(weight, count * count) * log(rank)
        for rank, weight in enumerate(weights, 1)
    )


def relaxed_critical_shell_envelope(m: int, *, constant: float = 1.0) -> float:
    """Return the crude critical-cap envelope after the log-product floor.

    This is only a calibration of the relaxation

        Y_m <= alpha_m log(D_(1,2m-1)) - L_m,

    with ``D<=C(2m)^2 log(4m)``.  It is not an upper bound on an infinite
    sum and it does not certify a Golomb construction attaining the envelope.
    """
    if constant <= 0:
        raise ValueError("constant must be positive")
    count = 2 * m
    alpha = Fraction((count - 2) ** 2, count * count)
    diameter_cap = constant * count * count * log(2 * count)
    return float(alpha) * log(diameter_cap) - single_shell_rearrangement_floor(m)


def interval_difference(points: Sequence[int], interval: GapInterval) -> int:
    """Return ``D_(p,q)=a_q-a_(p-1)``."""
    marks = tuple(points)
    left, right = interval
    if not 1 <= left <= right < len(marks):
        raise ValueError("invalid gap interval")
    return marks[right] - marks[left - 1]


def selected_rank_lag_differences(
    points: Sequence[int], epoch_lags: Mapping[int, int]
) -> tuple[int, ...]:
    """Return the W9-RLP/W10-HLP selected birth differences.

    At epoch ``m`` this selects ``a_j-a_(j-s)`` for ``m<=j<2m`` and
    ``1<=s<=q_m``.
    """
    marks = _validated_marks(points)
    selected_pairs: set[tuple[int, int]] = set()
    values: list[int] = []
    for m, lag_cutoff in sorted(epoch_lags.items()):
        if (
            not isinstance(m, int)
            or m < 1
            or m & (m - 1)
            or not isinstance(lag_cutoff, int)
            or not 1 <= lag_cutoff <= m
            or 2 * m > len(marks)
        ):
            raise ValueError("epochs must be available powers of two with 1<=q_m<=m")
        for lag in range(1, lag_cutoff + 1):
            for right in range(m, 2 * m):
                pair = (right - lag, right)
                if pair in selected_pairs:
                    raise AssertionError("selected mark pairs must be disjoint")
                selected_pairs.add(pair)
                values.append(marks[right] - marks[right - lag])
    return tuple(values)


def hereditary_log_product_check(
    points: Sequence[int], epoch_lags: Mapping[int, int]
) -> tuple[int, int]:
    """Return the exact selected product and its factorial floor."""
    marks = _validated_marks(points)
    if not is_golomb(marks):
        raise ValueError("points must form a Golomb ruler")
    values = selected_rank_lag_differences(marks, epoch_lags)
    if len(set(values)) != len(values):
        raise AssertionError("Golomb uniqueness failed on the selected family")
    product = reduce(int.__mul__, values, 1)
    floor = factorial(len(values))
    if product < floor:
        raise AssertionError("the hereditary factorial floor failed")
    return product, floor


def _lcm(left: int, right: int) -> int:
    return left // gcd(left, right) * right


def exact_weighted_rearrangement_products(
    values: Sequence[int], weights: Sequence[Fraction]
) -> tuple[int, int, int]:
    """Clear denominators and return both sides of the weighted product floor.

    For distinct positive integers ``d_t`` and nonnegative rational weights
    ``lambda_t``, rearrangement gives

        product d_t**lambda_t >= product r**lambda_r^downarrow.

    The returned common denominator makes every exponent integral.
    """
    integer_values = tuple(values)
    rational_weights = tuple(weights)
    if (
        len(integer_values) != len(rational_weights)
        or len(set(integer_values)) != len(integer_values)
        or any(value <= 0 for value in integer_values)
        or any(weight < 0 for weight in rational_weights)
    ):
        raise ValueError(
            "values must be distinct positive integers with matching weights"
        )
    common_denominator = 1
    for weight in rational_weights:
        common_denominator = _lcm(common_denominator, weight.denominator)
    lhs = reduce(
        int.__mul__,
        (
            value ** (weight.numerator * (common_denominator // weight.denominator))
            for value, weight in zip(integer_values, rational_weights, strict=True)
        ),
        1,
    )
    sorted_exponents = sorted(
        (
            weight.numerator * (common_denominator // weight.denominator)
            for weight in rational_weights
        ),
        reverse=True,
    )
    rhs = reduce(
        int.__mul__,
        (rank**exponent for rank, exponent in enumerate(sorted_exponents, 1)),
        1,
    )
    if lhs < rhs:
        raise AssertionError("the exact weighted rearrangement floor failed")
    return lhs, rhs, common_denominator


def dyadic_bulk_values_and_weights(
    points: Sequence[int], epochs: Sequence[int]
) -> tuple[tuple[int, ...], tuple[Fraction, ...]]:
    """Collect globally distinct negative-bulk differences and Abel weights."""
    marks = _validated_marks(points)
    values: list[int] = []
    weights: list[Fraction] = []
    seen_intervals: set[GapInterval] = set()
    for m in sorted(epochs):
        if not isinstance(m, int) or m < 4 or m & (m - 1) or 2 * m > len(marks):
            raise ValueError("epochs must be available powers of two")
        count = 2 * m
        for interval, scaled_weight in negative_bulk_coefficients(count).items():
            if interval in seen_intervals:
                raise AssertionError("dyadic negative-bulk intervals must be disjoint")
            seen_intervals.add(interval)
            values.append(interval_difference(marks, interval))
            weights.append(Fraction(scaled_weight, count * count))
    if len(set(values)) != len(values):
        raise ValueError("the selected bulk differences are not globally distinct")
    return tuple(values), tuple(weights)


def birth_shell_cross_ratio_sum(points: Sequence[int], m: int) -> float:
    """Evaluate the genuine unretained cross-ratio shell directly."""
    marks = _validated_marks(points)
    if 2 * m > len(marks) or m < 4:
        raise ValueError("the requested dyadic shell is unavailable")
    count = 2 * m
    prefix = marks[:count]
    return fsum(
        ((right - left) / count) ** 2
        * log(
            (prefix[right - 1] - prefix[left - 1])
            * (prefix[right] - prefix[left])
            / ((prefix[right - 1] - prefix[left]) * (prefix[right] - prefix[left - 1]))
        )
        for left in range(1, count - 2)
        for right in range(max(m, left + 2), count)
    )


def birth_shell_abel_sum(points: Sequence[int], m: int) -> float:
    """Evaluate the exact shell coefficient expansion."""
    marks = _validated_marks(points)
    if 2 * m > len(marks) or m < 4:
        raise ValueError("the requested dyadic shell is unavailable")
    count = 2 * m
    prefix = marks[:count]
    return fsum(
        coefficient * log(interval_difference(prefix, interval)) / (count * count)
        for interval, coefficient in closed_birth_shell_coefficients(count).items()
    )


def hereditary_bulk_log_floor(points: Sequence[int], epochs: Sequence[int]) -> float:
    """Return the global weighted rearrangement floor in logarithmic form."""
    _values, weights = dyadic_bulk_values_and_weights(points, epochs)
    sorted_weights = sorted(weights, reverse=True)
    return fsum(
        float(weight) * log(rank) for rank, weight in enumerate(sorted_weights, 1)
    )


def bulk_actual_log_mass(points: Sequence[int], epochs: Sequence[int]) -> float:
    """Return the actual negative-bulk weighted log mass."""
    values, weights = dyadic_bulk_values_and_weights(points, epochs)
    return fsum(
        float(weight) * log(value)
        for value, weight in zip(values, weights, strict=True)
    )
