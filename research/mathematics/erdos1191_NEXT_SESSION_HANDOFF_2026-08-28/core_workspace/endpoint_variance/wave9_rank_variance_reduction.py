"""Exact scalar rank-variance reduction of the Wave 8 birth budget.

The fixed Lyapunov kernel satisfies

    <H, K_ij^(L)> = ((j-i)/L)^2 q(1-(i+j)/L),

where 16/147 <= q <= 36/35 on every birth pair.  Removing the bounded
factor leaves a scalar positive birth budget.  That scalar budget telescopes
exactly to the sum of the weighted rank variances of the dyadic gap measures.

This is an algebraic reduction.  It does not prove the required
sublogarithmic upper bound and does not infer an infinite extension from a
finite ruler.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from fractions import Fraction

from innovation_budget import LYAPUNOV_MATRIX
from wave8_pair_telescope import pair_kernel

Q_MIN = Fraction(16, 147)
Q_MAX = Fraction(36, 35)


def _validated_marks(points: Sequence[int]) -> tuple[int, ...]:
    marks = tuple(points)
    if (
        len(marks) < 2
        or marks[0] != 0
        or marks != tuple(sorted(set(marks)))
        or any(not isinstance(mark, int) for mark in marks)
    ):
        raise ValueError("points must be normalized strictly increasing integers")
    return marks


def _is_power_of_two(value: int) -> bool:
    return value >= 1 and value & (value - 1) == 0


def _gap_weights(marks: tuple[int, ...]) -> tuple[int, ...]:
    return (1, *(marks[index] - marks[index - 1] for index in range(1, len(marks))))


def _modulus(marks: tuple[int, ...], count: int) -> int:
    return marks[count - 1] + 1


def weighted_rank_variance(points: Sequence[int], *, count: int) -> Fraction:
    """Return Var_nu(i/count) for the first ``count`` weighted gaps."""
    marks = _validated_marks(points)
    if not isinstance(count, int) or not 1 <= count <= len(marks):
        raise ValueError("count must index a nonempty prefix")
    weights = _gap_weights(marks)
    modulus = _modulus(marks, count)
    mean = sum(
        (Fraction(weights[index] * index, modulus * count) for index in range(count)),
        Fraction(0),
    )
    second_moment = sum(
        (
            Fraction(weights[index] * index * index, modulus * count * count)
            for index in range(count)
        ),
        Fraction(0),
    )
    return second_moment - mean * mean


@dataclass(frozen=True)
class ScalarBirthStep:
    old_count: int
    new_count: int
    old_modulus: int
    new_modulus: int
    modulus_ratio: Fraction
    old_rank_variance: Fraction
    new_rank_variance: Fraction
    direct_scalar_birth: Fraction
    telescoped_scalar_birth: Fraction
    fixed_h_birth: Fraction
    q_ratio: Fraction


@dataclass(frozen=True)
class DistinctGapVarianceAudit:
    count: int
    modulus: int
    actual_rank_variance: Fraction
    universal_lower_bound: Fraction


def distinct_gap_rank_variance_lower_bound(
    points: Sequence[int], *, count: int
) -> DistinctGapVarianceAudit:
    """Audit ``Var_nu(u) >= count^2/(512 N_count)`` for ``count>=8``.

    Only the genuine adjacent gaps ``h_1,...,h_(count-1)`` need be distinct.
    This is automatic for a Golomb ruler.  The artificial mass ``h_0=1`` is
    deliberately excluded from the distinctness assertion because it may
    equal a genuine unit gap.
    """
    marks = _validated_marks(points)
    if not isinstance(count, int) or not 8 <= count <= len(marks):
        raise ValueError("count must be an integer between 8 and the horizon")
    weights = _gap_weights(marks)
    if len(set(weights[1:count])) != count - 1:
        raise ValueError("the genuine adjacent gaps must be distinct")
    modulus = _modulus(marks, count)
    actual = weighted_rank_variance(marks, count=count)
    lower = Fraction(count * count, 512 * modulus)
    if actual < lower:
        raise AssertionError("the distinct-gap rank-variance bound failed")
    return DistinctGapVarianceAudit(
        count=count,
        modulus=modulus,
        actual_rank_variance=actual,
        universal_lower_bound=lower,
    )


def scalar_birth_step(points: Sequence[int], *, old_count: int) -> ScalarBirthStep:
    """Audit one dyadic scalar birth identity and the exact H-kernel ratio."""
    marks = _validated_marks(points)
    if (
        not isinstance(old_count, int)
        or not _is_power_of_two(old_count)
        or 2 * old_count > len(marks)
    ):
        raise ValueError("old_count must specify a complete dyadic update")
    new_count = 2 * old_count
    weights = _gap_weights(marks)
    old_modulus = _modulus(marks, old_count)
    new_modulus = _modulus(marks, new_count)
    ratio = Fraction(old_modulus, new_modulus)

    scalar = sum(
        (
            weights[left] * weights[right] * Fraction((right - left) ** 2, new_count**2)
            for right in range(old_count, new_count)
            for left in range(right)
        ),
        Fraction(0),
    ) / (new_modulus * new_modulus)
    fixed_h = sum(
        (
            weights[left]
            * weights[right]
            * pair_kernel(
                LYAPUNOV_MATRIX,
                left,
                right,
                count=new_count,
            )
            for right in range(old_count, new_count)
            for left in range(right)
        ),
        Fraction(0),
    ) / (new_modulus * new_modulus)

    old_variance = weighted_rank_variance(marks, count=old_count)
    new_variance = weighted_rank_variance(marks, count=new_count)
    telescoped = new_variance - ratio * ratio * old_variance / 4
    if scalar != telescoped:
        raise AssertionError("the scalar birth/rank-variance identity failed")
    if scalar <= 0:
        raise AssertionError("a nontrivial scalar birth increment must be positive")
    if not Q_MIN * scalar <= fixed_h <= Q_MAX * scalar:
        raise AssertionError("the fixed-H birth charge escaped the q bounds")

    return ScalarBirthStep(
        old_count=old_count,
        new_count=new_count,
        old_modulus=old_modulus,
        new_modulus=new_modulus,
        modulus_ratio=ratio,
        old_rank_variance=old_variance,
        new_rank_variance=new_variance,
        direct_scalar_birth=scalar,
        telescoped_scalar_birth=telescoped,
        fixed_h_birth=fixed_h,
        q_ratio=fixed_h / scalar,
    )


@dataclass(frozen=True)
class RankVarianceReductionAudit:
    mark_count: int
    update_count: int
    state_counts: tuple[int, ...]
    rank_variances: tuple[Fraction, ...]
    scalar_birth_sum: Fraction
    telescoped_scalar_sum: Fraction
    fixed_h_birth_sum: Fraction
    variance_sum: Fraction
    scalar_to_variance_ratio: Fraction
    h_to_variance_ratio: Fraction
    universal_h_lower_bound: Fraction
    universal_h_upper_bound: Fraction


def audit_rank_variance_reduction(points: Sequence[int]) -> RankVarianceReductionAudit:
    """Audit the global scalarization through a power-of-two horizon.

    If ``V_k`` is the rank variance at ``2^k`` marks and ``R_k`` the scalar
    birth increment, then

        R_k = V_(k+1) - (rho_k^2/4) V_k.

    Since 0 < rho_k < 1, summing gives

        (3/4) sum_{k=1}^{J+1} V_k <= sum_{k=0}^J R_k
        <= sum_{k=1}^{J+1} V_k.

    Combining this with the q bounds gives

        (4/49) sum V_k <= B_H <= (36/35) sum V_k.
    """
    marks = _validated_marks(points)
    if not _is_power_of_two(len(marks)):
        raise ValueError("the terminal mark count must be a power of two")

    counts = [1]
    while counts[-1] < len(marks):
        counts.append(2 * counts[-1])
    steps = tuple(scalar_birth_step(marks, old_count=count) for count in counts[:-1])
    variances = tuple(weighted_rank_variance(marks, count=count) for count in counts)
    scalar_sum = sum((step.direct_scalar_birth for step in steps), Fraction(0))
    telescoped_sum = sum((step.telescoped_scalar_birth for step in steps), Fraction(0))
    fixed_h_sum = sum((step.fixed_h_birth for step in steps), Fraction(0))
    variance_sum = sum(variances[1:], Fraction(0))

    if scalar_sum != telescoped_sum:
        raise AssertionError("the global scalar telescope failed")
    if not Fraction(3, 4) * variance_sum <= scalar_sum <= variance_sum:
        raise AssertionError("the scalar/variance global comparison failed")
    lower = Fraction(4, 49) * variance_sum
    upper = Q_MAX * variance_sum
    if not lower <= fixed_h_sum <= upper:
        raise AssertionError("the global H/variance comparison failed")

    return RankVarianceReductionAudit(
        mark_count=len(marks),
        update_count=len(steps),
        state_counts=tuple(counts),
        rank_variances=variances,
        scalar_birth_sum=scalar_sum,
        telescoped_scalar_sum=telescoped_sum,
        fixed_h_birth_sum=fixed_h_sum,
        variance_sum=variance_sum,
        scalar_to_variance_ratio=scalar_sum / variance_sum,
        h_to_variance_ratio=fixed_h_sum / variance_sum,
        universal_h_lower_bound=lower,
        universal_h_upper_bound=upper,
    )
