"""Exact integer-band audits for dyadic newborn shells.

The functions in this module use only integer arithmetic and
``fractions.Fraction``.  They do not search for rulers and do not assert an
asymptotic consequence: their purpose is to make the endpoints and rounding
in the cross-epoch packing lemmas independently reproducible.
"""
from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from fractions import Fraction
from math import ceil, floor
from typing import Protocol


def _validated_points(points: Sequence[int], old_count: int) -> tuple[int, ...]:
    marks = tuple(points)
    if (
        any(not isinstance(mark, int) for mark in marks)
        or len(marks) < 2 * old_count
        or marks != tuple(sorted(set(marks)))
    ):
        raise ValueError(
            "points must be strictly increasing integers with at least "
            "2*old_count entries"
        )
    if not isinstance(old_count, int) or old_count < 1:
        raise ValueError("old_count must be a positive integer")
    return marks


def _prefix_modulus(points: tuple[int, ...], count: int) -> int:
    if count == 0:
        return 0
    return points[count - 1] - points[0] + 1


def integer_band_capacity(lower: Fraction | int, upper: Fraction | int) -> int:
    """Number of integers in the closed real interval ``[lower, upper]``."""
    left = ceil(Fraction(lower))
    right = floor(Fraction(upper))
    return max(0, right - left + 1)


def positive_integer_band_capacity(
    lower: Fraction | int, upper: Fraction | int
) -> int:
    """Number of positive integers in the closed interval."""
    left = max(1, ceil(Fraction(lower)))
    right = floor(Fraction(upper))
    return max(0, right - left + 1)


@dataclass(frozen=True)
class DyadicShellProfile:
    old_count: int
    old_modulus: int
    new_modulus: int
    shell_total: int
    old_mean: Fraction
    shell_mean: Fraction
    old_discrepancy: Fraction
    shell_discrepancy: Fraction
    normalized_shell_discrepancy: Fraction
    endpoint_error: Fraction
    shell_gaps: tuple[int, ...]


def dyadic_shell_profile(
    points: Sequence[int], *, old_count: int
) -> DyadicShellProfile:
    """Return exact old-prefix and newborn-shell linear discrepancies."""
    marks = _validated_points(points, old_count)
    m = old_count
    old_modulus = _prefix_modulus(marks, m)
    new_modulus = _prefix_modulus(marks, 2 * m)
    shell_total = new_modulus - old_modulus
    old_mean = Fraction(old_modulus, m)
    shell_mean = Fraction(shell_total, m)

    old_discrepancy = max(
        (
            abs(Fraction(_prefix_modulus(marks, rank)) - rank * old_mean)
            for rank in range(m + 1)
        ),
        default=Fraction(0),
    )
    shell_gaps = tuple(marks[index] - marks[index - 1] for index in range(m, 2 * m))
    partial = 0
    shell_discrepancy = Fraction(0)
    for rank, gap in enumerate(shell_gaps, start=1):
        partial += gap
        shell_discrepancy = max(
            shell_discrepancy,
            abs(Fraction(partial) - rank * shell_mean),
        )

    return DyadicShellProfile(
        old_count=m,
        old_modulus=old_modulus,
        new_modulus=new_modulus,
        shell_total=shell_total,
        old_mean=old_mean,
        shell_mean=shell_mean,
        old_discrepancy=old_discrepancy,
        shell_discrepancy=shell_discrepancy,
        normalized_shell_discrepancy=Fraction(shell_discrepancy, shell_total),
        endpoint_error=Fraction(old_modulus, new_modulus) - Fraction(1, 2),
        shell_gaps=shell_gaps,
    )


def antidiagonal_threshold(
    profile: DyadicShellProfile, antidiagonal: int
) -> Fraction:
    """Return ``H_m + k*M_m``, the exact Theorem-C activation threshold."""
    if not isinstance(antidiagonal, int) or not 1 <= antidiagonal <= profile.old_count:
        raise ValueError("antidiagonal must be between one and old_count")
    discrepancy = profile.old_discrepancy + profile.shell_discrepancy
    maximum_mean = max(profile.old_mean, profile.shell_mean)
    return discrepancy + antidiagonal * maximum_mean


def low_band_cutoff(
    profile: DyadicShellProfile, threshold: Fraction | int
) -> int:
    """Return the exact cutoff ``R_m(T)`` from the cumulative band ledger."""
    value = Fraction(threshold)
    discrepancy = profile.old_discrepancy + profile.shell_discrepancy
    maximum_mean = max(profile.old_mean, profile.shell_mean)
    cutoff = floor((value - discrepancy) / maximum_mean)
    return min(profile.old_count, max(0, cutoff))


def threshold_count(
    profiles: Sequence[DyadicShellProfile], threshold: Fraction | int
) -> int:
    """Return ``sum_m sum_{k<=R_m(T)} k`` exactly."""
    return sum(
        (cutoff := low_band_cutoff(profile, threshold)) * (cutoff + 1) // 2
        for profile in profiles
    )


def truncated_harmonic_threshold_sum(
    profiles: Sequence[DyadicShellProfile], maximum: Fraction | int
) -> Fraction:
    """Return ``sum_{tau_(m,k)<=X} k/tau_(m,k)`` exactly."""
    upper = Fraction(maximum)
    if upper < 1:
        raise ValueError("maximum must be at least one")
    return sum(
        (
            Fraction(antidiagonal, antidiagonal_threshold(profile, antidiagonal))
            for profile in profiles
            for antidiagonal in range(1, profile.old_count + 1)
            if antidiagonal_threshold(profile, antidiagonal) <= upper
        ),
        Fraction(0),
    )


def fractional_threshold_sum(
    profiles: Sequence[DyadicShellProfile], *, epsilon: int
) -> Fraction:
    """Exact integer-epsilon audit of the fractional Carleson sum.

    The analytic theorem allows every real ``epsilon > 0``.  This verifier
    accepts positive integers so every power and returned value stay rational.
    """
    if not isinstance(epsilon, int) or epsilon < 1:
        raise ValueError("epsilon must be a positive integer for exact auditing")
    return sum(
        (
            Fraction(antidiagonal, 1)
            / antidiagonal_threshold(profile, antidiagonal) ** (1 + epsilon)
            for profile in profiles
            for antidiagonal in range(1, profile.old_count + 1)
        ),
        Fraction(0),
    )


class DifferenceBand(Protocol):
    lower: Fraction
    upper: Fraction
    difference_count: int
    differences: tuple[int, ...]


@dataclass(frozen=True)
class ShellLengthBand:
    old_count: int
    length: int
    lower: Fraction
    upper: Fraction
    difference_count: int
    integer_capacity: int
    differences: tuple[int, ...]
    all_differences_distinct: bool
    all_differences_inside_band: bool


def dyadic_shell_length_band(
    points: Sequence[int], *, old_count: int, length: int
) -> ShellLengthBand:
    """Band containing every newborn-shell interval sum of one rank length."""
    marks = _validated_points(points, old_count)
    m = old_count
    if not isinstance(length, int) or not 1 <= length <= m:
        raise ValueError("length must be an integer between one and old_count")
    profile = dyadic_shell_profile(marks, old_count=m)
    radius = 2 * profile.shell_discrepancy
    center = length * profile.shell_mean
    lower = center - radius
    upper = center + radius
    differences = tuple(
        marks[start + length - 1] - marks[start - 1]
        for start in range(m, 2 * m - length + 1)
    )
    return ShellLengthBand(
        old_count=m,
        length=length,
        lower=lower,
        upper=upper,
        difference_count=m - length + 1,
        integer_capacity=positive_integer_band_capacity(lower, upper),
        differences=differences,
        all_differences_distinct=len(differences) == len(set(differences)),
        all_differences_inside_band=all(lower <= value <= upper for value in differences),
    )


@dataclass(frozen=True)
class AntidiagonalBand:
    old_count: int
    antidiagonal: int
    lower: Fraction
    upper: Fraction
    difference_count: int
    integer_capacity: int
    differences: tuple[int, ...]
    all_differences_distinct: bool
    all_differences_inside_band: bool


def dyadic_antidiagonal_band(
    points: Sequence[int], *, old_count: int, antidiagonal: int
) -> AntidiagonalBand:
    """Band for the first-half/second-half cross pairs ``t+s=k``.

    For ``0 <= t < k`` put ``s=k-t``.  The associated endpoint pair is
    ``(m-1-t, m-1+s)``.  Restricting ``1 <= k <= m`` keeps its right endpoint
    in the newborn mark block, so different dyadic epochs use disjoint pairs.
    """
    marks = _validated_points(points, old_count)
    m = old_count
    if not isinstance(antidiagonal, int) or not 1 <= antidiagonal <= m:
        raise ValueError("antidiagonal must be an integer between one and old_count")
    k = antidiagonal
    profile = dyadic_shell_profile(marks, old_count=m)
    first_center = k * profile.shell_mean
    last_center = (k - 1) * profile.old_mean + profile.shell_mean
    radius = profile.old_discrepancy + profile.shell_discrepancy
    lower = min(first_center, last_center) - radius
    upper = max(first_center, last_center) + radius
    differences = tuple(
        marks[m - 1 + (k - t)] - marks[m - 1 - t] for t in range(k)
    )
    return AntidiagonalBand(
        old_count=m,
        antidiagonal=k,
        lower=lower,
        upper=upper,
        difference_count=k,
        integer_capacity=positive_integer_band_capacity(lower, upper),
        differences=differences,
        all_differences_distinct=len(differences) == len(set(differences)),
        all_differences_inside_band=all(lower <= value <= upper for value in differences),
    )


@dataclass(frozen=True)
class BandCollectionAudit:
    lower: Fraction
    upper: Fraction
    selected_count: int
    distinct_count: int
    integer_capacity: int
    all_differences_distinct: bool
    all_differences_inside_envelope: bool


def audit_band_collection(bands: Sequence[DifferenceBand]) -> BandCollectionAudit:
    """Audit the common-envelope packing count for a nonempty band family."""
    selected = tuple(bands)
    if not selected:
        raise ValueError("bands must be nonempty")
    lower = min(band.lower for band in selected)
    upper = max(band.upper for band in selected)
    differences = tuple(value for band in selected for value in band.differences)
    selected_count = sum(band.difference_count for band in selected)
    if selected_count != len(differences):
        raise ValueError("a band difference_count does not match its values")
    return BandCollectionAudit(
        lower=lower,
        upper=upper,
        selected_count=selected_count,
        distinct_count=len(set(differences)),
        integer_capacity=positive_integer_band_capacity(lower, upper),
        all_differences_distinct=len(differences) == len(set(differences)),
        all_differences_inside_envelope=all(
            lower <= value <= upper for value in differences
        ),
    )
