"""Exact cross-epoch identities and a reset-amortization counterprofile.

The counterprofile is an increasing integer gap sequence satisfying the
scalar Sidon diameter lower bound and the dyadic ``C=1`` critical upper
bound.  Every newborn shell is exactly rank-uniform.  It is deliberately not
a Golomb ruler: its role is to show exactly where a diameter/profile-only
reset argument stops seeing Sidon arithmetic.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from gap_measure_dynamics import dyadic_gap_matrix_update


Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def q_step_transport_matrix(q: int) -> Matrix2:
    """Return the matrix carrying ``(f(u),u)`` under ``u -> u/q``."""
    if not isinstance(q, int) or q < 2:
        raise ValueError("q must be an integer at least two")
    return (
        (Fraction(1, q * q), Fraction(q - 1, q * q)),
        (Fraction(0), Fraction(1, q)),
    )


def uniform_upper_half_f_variance(count: int) -> Fraction:
    """Return ``Var(u(1-u))`` on ``{k/(2m): m <= k < 2m}``."""
    if not isinstance(count, int) or count < 2:
        raise ValueError("count must be an integer at least two")
    m = count
    return Fraction(
        (m - 1) * (2 * m - 1) * (8 * m * m - 3 * m - 11),
        2880 * m**4,
    )


def _validated_points(points: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    marks = tuple(points)
    if (
        len(marks) < 2
        or any(not isinstance(mark, int) for mark in marks)
        or marks != tuple(sorted(set(marks)))
    ):
        raise ValueError("points must be strictly increasing integers")
    return marks


def _prefix_modulus(points: tuple[int, ...], count: int) -> int:
    return points[count - 1] - points[0] + 1


def grid_profile_errors(
    points: tuple[int, ...] | list[int], count: int
) -> tuple[Fraction, ...]:
    """Return ``N_r/N_count-r/count`` for every ``0 <= r <= count``."""
    marks = _validated_points(points)
    if not isinstance(count, int) or not 2 <= count <= len(marks):
        raise ValueError("count must be between two and the number of points")
    modulus = _prefix_modulus(marks, count)
    return (Fraction(0),) + tuple(
        Fraction(_prefix_modulus(marks, rank), modulus) - Fraction(rank, count)
        for rank in range(1, count + 1)
    )


@dataclass(frozen=True)
class ProfilePersistenceRow:
    old_count: int
    final_count: int
    rank: int
    old_mass: Fraction
    old_error: Fraction
    final_error: Fraction
    chord_error: Fraction
    residual: Fraction
    transported_old_error: Fraction


def profile_persistence_row(
    points: tuple[int, ...] | list[int],
    *,
    old_count: int,
    final_count: int,
    rank: int,
) -> ProfilePersistenceRow:
    """Evaluate the exact old-profile/chord decomposition at one rank."""
    marks = _validated_points(points)
    if not 1 <= rank <= old_count < final_count <= len(marks):
        raise ValueError("require 1 <= rank <= old_count < final_count")
    old_modulus = _prefix_modulus(marks, old_count)
    final_modulus = _prefix_modulus(marks, final_count)
    rank_modulus = _prefix_modulus(marks, rank)
    old_mass = Fraction(old_modulus, final_modulus)
    old_error = Fraction(rank_modulus, old_modulus) - Fraction(rank, old_count)
    final_error = Fraction(rank_modulus, final_modulus) - Fraction(rank, final_count)
    endpoint_error = old_mass - Fraction(old_count, final_count)
    chord_error = Fraction(rank, old_count) * endpoint_error
    residual = final_error - chord_error
    transported = old_mass * old_error
    if residual != transported:
        raise AssertionError("cross-epoch profile persistence identity failed")
    return ProfilePersistenceRow(
        old_count=old_count,
        final_count=final_count,
        rank=rank,
        old_mass=old_mass,
        old_error=old_error,
        final_error=final_error,
        chord_error=chord_error,
        residual=residual,
        transported_old_error=transported,
    )


def sawtooth_multipliers(last_exponent: int) -> tuple[int, ...]:
    """Return the exact normalized-diameter reset/halving orbit."""
    if not isinstance(last_exponent, int) or last_exponent < 1:
        raise ValueError("last_exponent must be a positive integer")
    values = [1]
    for exponent in range(2, last_exponent + 1):
        previous = values[-1]
        if previous > 1:
            values.append(previous // 2)
        else:
            values.append(1 << (exponent.bit_length() - 1))
    return tuple(values)


@dataclass(frozen=True)
class SawtoothLevel:
    exponent: int
    mark_count: int
    multiplier: int
    modulus: int
    scalar_sidon_lower_bound: bool
    critical_c1_dyadic_bound: bool


@dataclass(frozen=True)
class SawtoothTransition:
    old_exponent: int
    old_count: int
    new_count: int
    old_to_new_modulus_ratio: Fraction
    flat_half_mass_step: bool
    innovation_q00_per_new_modulus: Fraction


@dataclass(frozen=True)
class SawtoothGapProfile:
    points: tuple[int, ...]
    dyadic_moduli: tuple[int, ...]
    levels: tuple[SawtoothLevel, ...]
    transitions: tuple[SawtoothTransition, ...]
    smallest_repeated_difference: int | None


def _points_from_gaps(gaps: list[int]) -> tuple[int, ...]:
    cumulative = 0
    points = []
    for gap in gaps:
        cumulative += gap
        points.append(cumulative - 1)
    return tuple(points)


def _smallest_repeated_difference(points: tuple[int, ...]) -> int | None:
    """Return the numerically smallest repeated positive difference, if any."""
    seen: set[int] = set()
    collisions: set[int] = set()
    for left in range(len(points)):
        for right in range(left + 1, len(points)):
            difference = points[right] - points[left]
            if difference in seen:
                collisions.add(difference)
            seen.add(difference)
    return min(collisions) if collisions else None


def build_sawtooth_gap_profile(last_exponent: int) -> SawtoothGapProfile:
    """Build the nested integer gap counterprofile through ``2**J`` marks."""
    multipliers = sawtooth_multipliers(last_exponent)
    gaps = [1, 4 * multipliers[0] - 1]
    for new_exponent in range(2, last_exponent + 1):
        old_count = 1 << (new_exponent - 1)
        new_modulus = 4**new_exponent * multipliers[new_exponent - 1]
        growth = new_modulus - sum(gaps)
        shell_weight, remainder = divmod(growth, old_count)
        if remainder or shell_weight < 1:
            raise AssertionError("new shell cannot be exactly rank-uniform")
        shell = [shell_weight] * old_count
        gaps.extend(shell)

    points = _points_from_gaps(gaps)
    levels = []
    moduli = []
    for exponent, multiplier in enumerate(multipliers, start=1):
        mark_count = 1 << exponent
        modulus = _prefix_modulus(points, mark_count)
        expected = 4**exponent * multiplier
        if modulus != expected:
            raise AssertionError("constructed dyadic modulus is incorrect")
        sidon_scalar_floor = mark_count * (mark_count - 1) // 2 + 1
        levels.append(
            SawtoothLevel(
                exponent=exponent,
                mark_count=mark_count,
                multiplier=multiplier,
                modulus=modulus,
                scalar_sidon_lower_bound=modulus >= sidon_scalar_floor,
                # multiplier <= exponent and log(2) > 1/2 imply
                # N <= 2*m^2*log(m), with no floating-point decision.
                critical_c1_dyadic_bound=multiplier <= exponent,
            )
        )
        moduli.append(modulus)

    transitions = []
    for old_exponent in range(1, last_exponent):
        old_count = 1 << old_exponent
        new_count = 2 * old_count
        prefix = points[:new_count]
        update = dyadic_gap_matrix_update(prefix, old_count)
        ratio = Fraction(update.old_modulus, update.new_modulus)
        transitions.append(
            SawtoothTransition(
                old_exponent=old_exponent,
                old_count=old_count,
                new_count=new_count,
                old_to_new_modulus_ratio=ratio,
                flat_half_mass_step=ratio == Fraction(1, 2),
                innovation_q00_per_new_modulus=Fraction(
                    update.innovation[0][0], update.new_modulus
                ),
            )
        )

    return SawtoothGapProfile(
        points=points,
        dyadic_moduli=tuple(moduli),
        levels=tuple(levels),
        transitions=tuple(transitions),
        smallest_repeated_difference=_smallest_repeated_difference(points),
    )
