"""Exact verifier for the complete dyadic birth-spectrum ledger.

This module independently rebuilds the Wave 7 full-rhombus and newborn-
internal families. It deliberately does not call the Wave 6 band helpers.
All algebra is integer or fractions.Fraction based.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from fractions import Fraction
from math import floor


@dataclass(frozen=True)
class BirthFamily:
    """One equal-rank-lag family born at a dyadic boundary."""

    epoch: int
    kind: str
    lag: int
    demand: int
    lower: Fraction
    upper: Fraction
    pairs: tuple[tuple[int, int], ...]
    differences: tuple[int, ...]


@dataclass(frozen=True)
class CompleteLedgerAudit:
    """Exact endpoint audit of Theorems 1--4."""

    mark_count: int
    family_count: int
    pair_count: int
    distinct_difference_count: int
    threshold_count: int
    wedge_check_count: int
    w2: Fraction
    w2_square_at_most_128: bool


@dataclass(frozen=True)
class ErdosTuranBridgeAudit:
    """Exact p=1423 counterexample data."""

    prime: int
    old_count: int
    mark_count: int
    pair_count: int
    old_modulus: int
    new_modulus: int
    compatible_prefix_count: int
    minimum_cap_slack: int
    innovation_q00_per_modulus: Fraction
    w2: Fraction
    w2_upper_bound: Fraction
    comparison_cross_product: int


def _validated_marks(points: Sequence[int], *, minimum: int = 2) -> tuple[int, ...]:
    marks = tuple(points)
    if len(marks) < minimum:
        raise ValueError(f"at least {minimum} marks are required")
    if any(not isinstance(mark, int) for mark in marks):
        raise TypeError("marks must be integers")
    if marks != tuple(sorted(set(marks))):
        raise ValueError("marks must be strictly increasing")
    return marks


def _prefix_modulus(marks: tuple[int, ...], count: int) -> int:
    if count == 0:
        return 0
    return marks[count - 1] - marks[0] + 1


def _profile(
    marks: tuple[int, ...], old_count: int
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    m = old_count
    old_modulus = _prefix_modulus(marks, m)
    full_modulus = _prefix_modulus(marks, 2 * m)
    old_mean = Fraction(old_modulus, m)
    shell_mean = Fraction(full_modulus - old_modulus, m)
    old_discrepancy = max(
        abs(Fraction(_prefix_modulus(marks, rank)) - rank * old_mean)
        for rank in range(m + 1)
    )
    shell_discrepancy = max(
        abs(
            Fraction(_prefix_modulus(marks, m + rank) - old_modulus) - rank * shell_mean
        )
        for rank in range(m + 1)
    )
    return old_mean, shell_mean, old_discrepancy, shell_discrepancy


def epoch_birth_families(
    points: Sequence[int], *, old_count: int
) -> tuple[BirthFamily, ...]:
    """Return every pair family born in the block [m, 2m)."""
    marks = _validated_marks(points)
    if not isinstance(old_count, int) or old_count < 1 or len(marks) < 2 * old_count:
        raise ValueError("old_count must be positive and 2*old_count marks must exist")
    m = old_count
    old_mean, shell_mean, old_discrepancy, shell_discrepancy = _profile(marks, m)
    history_radius = old_discrepancy + shell_discrepancy
    families: list[BirthFamily] = []

    for lag in range(1, 2 * m):
        first_t = max(0, lag - m)
        last_t = min(m - 1, lag - 1)
        first_center = first_t * old_mean + (lag - first_t) * shell_mean
        last_center = last_t * old_mean + (lag - last_t) * shell_mean
        lower = min(first_center, last_center) - history_radius
        upper = max(first_center, last_center) + history_radius
        pairs = tuple(
            (m - 1 - offset, m - 1 + lag - offset)
            for offset in range(first_t, last_t + 1)
        )
        differences = tuple(marks[right] - marks[left] for left, right in pairs)
        family = BirthFamily(
            epoch=m,
            kind="cross",
            lag=lag,
            demand=min(lag, 2 * m - lag),
            lower=lower,
            upper=upper,
            pairs=pairs,
            differences=differences,
        )
        _assert_family(family)
        families.append(family)

    for lag in range(1, m):
        lower = lag * shell_mean - 2 * shell_discrepancy
        upper = lag * shell_mean + 2 * shell_discrepancy
        pairs = tuple(
            (m + offset - 1, m + offset + lag - 1) for offset in range(1, m - lag + 1)
        )
        differences = tuple(marks[right] - marks[left] for left, right in pairs)
        family = BirthFamily(
            epoch=m,
            kind="internal",
            lag=lag,
            demand=m - lag,
            lower=lower,
            upper=upper,
            pairs=pairs,
            differences=differences,
        )
        _assert_family(family)
        families.append(family)

    return tuple(families)


def _assert_family(family: BirthFamily) -> None:
    if family.demand != len(family.pairs) or family.demand != len(family.differences):
        raise AssertionError("family demand does not equal its pair count")
    if len(family.pairs) != len(set(family.pairs)):
        raise AssertionError("a family repeats an endpoint pair")
    if any(
        difference < 1 or not family.lower <= difference <= family.upper
        for difference in family.differences
    ):
        raise AssertionError("a family difference lies outside its exact band")


def complete_birth_families(points: Sequence[int]) -> tuple[BirthFamily, ...]:
    """Partition all pairs of a power-of-two prefix by dyadic birth block."""
    marks = _validated_marks(points)
    if len(marks) & (len(marks) - 1):
        raise ValueError("the terminal mark count must be a power of two")
    families: list[BirthFamily] = []
    epoch = 1
    while 2 * epoch <= len(marks):
        families.extend(epoch_birth_families(marks, old_count=epoch))
        epoch *= 2
    return tuple(families)


def complete_w2(families: Sequence[BirthFamily]) -> Fraction:
    """Return sum demand*lag/upper^2 exactly."""
    selected = tuple(families)
    if not selected:
        raise ValueError("at least one family is required")
    if any(family.upper < 1 for family in selected):
        raise ValueError("every upper threshold must be at least one")
    return sum(
        (
            Fraction(family.demand * family.lag, 1) / family.upper**2
            for family in selected
        ),
        Fraction(0),
    )


def audit_complete_birth_ledger(points: Sequence[int]) -> CompleteLedgerAudit:
    """Check full partition, every activation endpoint, and every wedge K."""
    marks = _validated_marks(points)
    families = complete_birth_families(marks)
    family_pairs = tuple(pair for family in families for pair in family.pairs)
    expected_pairs = tuple(
        (left, right) for right in range(1, len(marks)) for left in range(right)
    )
    if len(family_pairs) != len(set(family_pairs)):
        raise AssertionError("the complete birth partition repeats a pair")
    if set(family_pairs) != set(expected_pairs):
        raise AssertionError("the complete birth partition omits a pair")

    differences = tuple(
        difference for family in families for difference in family.differences
    )
    if len(differences) != len(set(differences)):
        raise AssertionError("the supplied ruler is not Golomb")

    grouped: dict[Fraction, list[BirthFamily]] = {}
    for family in families:
        grouped.setdefault(family.upper, []).append(family)
    demand_by_lag = [0] * len(marks)
    total_demand = 0
    wedge_checks = 0
    for threshold in sorted(grouped):
        for family in grouped[threshold]:
            demand_by_lag[family.lag] += family.demand
            total_demand += family.demand
        integer_cutoff = floor(threshold)
        if total_demand > integer_cutoff:
            raise AssertionError("complete threshold ledger failed")
        tail_demand = 0
        for minimum_lag in range(len(marks) - 1, 0, -1):
            tail_demand += demand_by_lag[minimum_lag]
            rank_floor = minimum_lag * (minimum_lag + 1) // 2
            capacity = max(0, integer_cutoff - rank_floor + 1)
            if tail_demand > capacity:
                raise AssertionError("two-parameter wedge ledger failed")
            wedge_checks += 1

    w2 = complete_w2(families)
    return CompleteLedgerAudit(
        mark_count=len(marks),
        family_count=len(families),
        pair_count=len(family_pairs),
        distinct_difference_count=len(set(differences)),
        threshold_count=len(grouped),
        wedge_check_count=wedge_checks,
        w2=w2,
        w2_square_at_most_128=w2 * w2 <= 128,
    )


def _log_ratio_interval(
    numerator: int, denominator: int, terms: int
) -> tuple[Fraction, Fraction]:
    """Rigorous atanh-series enclosure for log(numerator/denominator)."""
    if not (numerator >= denominator >= 1 and terms >= 1):
        raise ValueError("require numerator >= denominator >= 1 and terms >= 1")
    z = Fraction(numerator - denominator, numerator + denominator)
    lower = 2 * sum(
        (z ** (2 * index + 1) / (2 * index + 1) for index in range(terms)),
        Fraction(0),
    )
    tail = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return lower, lower + tail


def log_integer_interval(value: int, terms: int) -> tuple[Fraction, Fraction]:
    """Fast rigorous enclosure of log(value) by binary range reduction."""
    if not isinstance(value, int) or value < 2:
        raise ValueError("value must be an integer at least two")
    exponent = value.bit_length() - 1
    power = 1 << exponent
    log_two_lower, log_two_upper = _log_ratio_interval(2, 1, terms)
    ratio_lower, ratio_upper = _log_ratio_interval(value, power, terms)
    return (
        exponent * log_two_lower + ratio_lower,
        exponent * log_two_upper + ratio_upper,
    )


def critical_modulus_cap(mark_count: int) -> int:
    """Certify floor(2*n^2*log(n)) using only rational bounds."""
    if not isinstance(mark_count, int) or mark_count < 2:
        raise ValueError("mark_count must be an integer at least two")
    factor = 2 * mark_count * mark_count
    terms = 4
    while True:
        lower, upper = log_integer_interval(mark_count, terms)
        lower_floor = floor(factor * lower)
        upper_floor = floor(factor * upper)
        if lower_floor == upper_floor:
            return lower_floor
        terms *= 2
        if terms > 4096:
            raise ArithmeticError("log enclosure did not determine the cap")


def _prime_by_trial_division(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def erdos_turan_ruler(mark_count: int, prime: int) -> tuple[int, ...]:
    """Return the classical integer Erdos--Turan ruler."""
    if (
        not isinstance(mark_count, int)
        or not isinstance(prime, int)
        or not 2 <= mark_count <= prime
        or not _prime_by_trial_division(prime)
    ):
        raise ValueError("require 2 <= mark_count <= prime with prime prime")
    return tuple(
        2 * prime * index + (index * index % prime) for index in range(mark_count)
    )


def _compensated_covariance(points: tuple[int, ...]) -> tuple[Fraction, ...]:
    """Return (M00,M01,M11,N) without project covariance helpers."""
    count = len(points)
    modulus = points[-1] - points[0] + 1
    gaps = (
        1,
        *(points[index] - points[index - 1] for index in range(1, count)),
    )
    ranks = tuple(Fraction(index, count) for index in range(count))
    functions = tuple(rank * (1 - rank) for rank in ranks)
    mean_function = (
        sum((gap * value for gap, value in zip(gaps, functions)), Fraction(0)) / modulus
    )
    mean_rank = (
        sum((gap * rank for gap, rank in zip(gaps, ranks)), Fraction(0)) / modulus
    )
    matrix_00 = sum(
        (gap * (value - mean_function) ** 2 for gap, value in zip(gaps, functions)),
        Fraction(0),
    )
    matrix_01 = sum(
        (
            gap * (value - mean_function) * (rank - mean_rank)
            for gap, value, rank in zip(gaps, functions, ranks)
        ),
        Fraction(0),
    )
    matrix_11 = sum(
        (gap * (rank - mean_rank) ** 2 for gap, rank in zip(gaps, ranks)),
        Fraction(0),
    )
    return matrix_00, matrix_01, matrix_11, Fraction(modulus)


def normalized_innovation_q00(points: Sequence[int], *, old_count: int) -> Fraction:
    """Independently evaluate Q00/N_(2m) for one exact dyadic update."""
    marks = _validated_marks(points)
    if len(marks) != 2 * old_count or old_count < 2:
        raise ValueError("the ruler must contain exactly 2*old_count marks")
    old_matrix = _compensated_covariance(marks[:old_count])
    full_matrix = _compensated_covariance(marks)
    transported_00 = (old_matrix[0] + 2 * old_matrix[1] + old_matrix[2]) / 16
    return (full_matrix[0] - transported_00) / full_matrix[3]


def audit_erdos_turan_1423() -> ErdosTuranBridgeAudit:
    """Recompute the exact 512-mark finite bridge counterexample."""
    prime = 1423
    old_count = 256
    points = erdos_turan_ruler(2 * old_count, prime)
    differences = tuple(
        points[right] - points[left]
        for right in range(1, len(points))
        for left in range(right)
    )
    if len(differences) != len(set(differences)):
        raise AssertionError("the p=1423 ruler failed the Golomb audit")

    cap_slacks = tuple(
        critical_modulus_cap(count) - _prefix_modulus(points, count)
        for count in range(old_count, 2 * old_count + 1)
    )
    if min(cap_slacks) < 0:
        raise AssertionError("a p=1423 prefix failed its C=1 critical cap")

    families = epoch_birth_families(points, old_count=old_count)
    family_pairs = tuple(pair for family in families for pair in family.pairs)
    expected_pairs = tuple(
        (left, right)
        for right in range(old_count, 2 * old_count)
        for left in range(right)
    )
    if set(family_pairs) != set(expected_pairs) or len(family_pairs) != len(
        expected_pairs
    ):
        raise AssertionError("the p=1423 epoch birth partition failed")

    w2 = complete_w2(families)
    w2_upper_bound = Fraction(2304, prime * prime)
    innovation = normalized_innovation_q00(points, old_count=old_count)
    cross_product = (
        innovation.numerator * w2_upper_bound.denominator
        - w2_upper_bound.numerator * innovation.denominator
    )
    if not w2 < w2_upper_bound < innovation:
        raise AssertionError("the exact p=1423 bridge comparison failed")

    return ErdosTuranBridgeAudit(
        prime=prime,
        old_count=old_count,
        mark_count=len(points),
        pair_count=len(differences),
        old_modulus=_prefix_modulus(points, old_count),
        new_modulus=_prefix_modulus(points, 2 * old_count),
        compatible_prefix_count=len(cap_slacks),
        minimum_cap_slack=min(cap_slacks),
        innovation_q00_per_modulus=innovation,
        w2=w2,
        w2_upper_bound=w2_upper_bound,
        comparison_cross_product=cross_product,
    )
