"""Exact verifier for the Wave 8 arithmetic innovation atom identities.

This module is intentionally self-contained apart from the established
constants.  It checks the matrix pair decompositions, Abel fan, signed
contiguous-square expansion, sign classification, positive atom envelope,
and the two finite no-go witnesses with ``Fraction`` arithmetic.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from fractions import Fraction

Vector2 = tuple[Fraction, Fraction]
Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]
H_MATRIX: Matrix2 = (
    (Fraction(16, 15), Fraction(8, 105)),
    (Fraction(8, 105), Fraction(4, 35)),
)


def _validated_gaps(gaps: Sequence[int], *, old_count: int) -> tuple[int, ...]:
    weights = tuple(gaps)
    if (
        not isinstance(old_count, int)
        or old_count < 2
        or len(weights) != 2 * old_count
        or weights[0] != 1
        or any(not isinstance(weight, int) or weight < 1 for weight in weights)
    ):
        raise ValueError(
            "gaps must be 2*old_count positive integers with artificial h_0=1"
        )
    return weights


def points_from_gap_weights(gaps: Sequence[int]) -> tuple[int, ...]:
    """Recover marks from ``(h_0=1,h_1,...,h_(L-1))``."""
    weights = tuple(gaps)
    if (
        len(weights) < 2
        or weights[0] != 1
        or any(not isinstance(weight, int) or weight < 1 for weight in weights)
    ):
        raise ValueError("gap weights must be positive integers with h_0=1")
    points = [0]
    for weight in weights[1:]:
        points.append(points[-1] + weight)
    return tuple(points)


def is_golomb_from_gap_weights(gaps: Sequence[int]) -> bool:
    points = points_from_gap_weights(gaps)
    differences = tuple(
        points[right] - points[left]
        for right in range(1, len(points))
        for left in range(right)
    )
    return len(differences) == len(set(differences))


def _z(index: int, length: int) -> Vector2:
    u = Fraction(index, length)
    return (u * (1 - u), u)


def _vector_subtract(left: Vector2, right: Vector2) -> Vector2:
    return (left[0] - right[0], left[1] - right[1])


def _vector_scale(scale: Fraction | int, vector: Vector2) -> Vector2:
    exact = Fraction(scale)
    return (exact * vector[0], exact * vector[1])


def _vector_add(*vectors: Vector2) -> Vector2:
    return (
        sum((vector[0] for vector in vectors), Fraction(0)),
        sum((vector[1] for vector in vectors), Fraction(0)),
    )


def _outer(vector: Vector2) -> Matrix2:
    return (
        (vector[0] ** 2, vector[0] * vector[1]),
        (vector[0] * vector[1], vector[1] ** 2),
    )


def _matrix_add(*matrices: Matrix2) -> Matrix2:
    return tuple(
        tuple(
            sum((matrix[row][column] for matrix in matrices), Fraction(0))
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def _matrix_scale(scale: Fraction | int, matrix: Matrix2) -> Matrix2:
    exact = Fraction(scale)
    return tuple(
        tuple(exact * matrix[row][column] for column in range(2)) for row in range(2)
    )  # type: ignore[return-value]


def _weighted_mean(vectors: Sequence[Vector2], weights: Sequence[int]) -> Vector2:
    total = sum(weights)
    return (
        sum(
            (weight * vector[0] for weight, vector in zip(weights, vectors)),
            Fraction(0),
        )
        / total,
        sum(
            (weight * vector[1] for weight, vector in zip(weights, vectors)),
            Fraction(0),
        )
        / total,
    )


def _weighted_covariance(vectors: Sequence[Vector2], weights: Sequence[int]) -> Matrix2:
    mean = _weighted_mean(vectors, weights)
    total = sum(weights)
    deltas = tuple(_vector_subtract(vector, mean) for vector in vectors)
    return tuple(
        tuple(
            sum(
                (
                    weight * delta[row] * delta[column]
                    for weight, delta in zip(weights, deltas)
                ),
                Fraction(0),
            )
            / total
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def _h_inner(matrix: Matrix2) -> Fraction:
    return sum(
        (
            H_MATRIX[row][column] * matrix[row][column]
            for row in range(2)
            for column in range(2)
        ),
        Fraction(0),
    )


def kernel_phi(index: int, other: int, *, length: int) -> Fraction:
    """Return the exact adjoint secant kernel ``Phi_(index,other)``."""
    if (
        not isinstance(length, int)
        or length < 2
        or not isinstance(index, int)
        or not isinstance(other, int)
        or not 0 <= index < other < length
    ):
        raise ValueError("require integer indices 0 <= index < other < length")
    lag = other - index
    coordinate = 1 - Fraction(index + other, length)
    polynomial = (
        Fraction(16, 15) * coordinate**2
        + Fraction(16, 105) * coordinate
        + Fraction(4, 35)
    )
    formula = Fraction(lag * lag, length * length) * polynomial
    direct = _h_inner(_outer(_vector_subtract(_z(other, length), _z(index, length))))
    if formula != direct:
        raise AssertionError("the adjoint secant kernel formula failed")
    return formula


def shell_kappa(start: int, end: int, *, old_count: int) -> Fraction:
    """Return the zero-extended mixed difference ``kappa_(start,end)``."""
    if (
        not isinstance(old_count, int)
        or old_count < 2
        or not old_count <= start <= end < 2 * old_count
    ):
        raise ValueError("require old_count <= start <= end < 2*old_count")
    length = 2 * old_count

    def extended(first: int, second: int) -> Fraction:
        if old_count <= first < second < length:
            return kernel_phi(first, second, length=length)
        return Fraction(0)

    return (
        extended(start, end)
        - extended(start - 1, end)
        - extended(start, end + 1)
        + extended(start - 1, end + 1)
    )


def contiguous_gap_sum(gaps: Sequence[int], start: int, end: int) -> int:
    weights = tuple(gaps)
    if not 0 <= start <= end < len(weights):
        raise ValueError("require 0 <= start <= end < len(gaps)")
    return sum(weights[start : end + 1])


@dataclass(frozen=True)
class QAtomAudit:
    old_count: int
    old_mass: int
    shell_mass: int
    full_mass: int
    shell_h_energy: Fraction
    rank_one_h_energy: Fraction
    normalized_q_charge: Fraction
    positive_envelope: Fraction
    negative_kappa_count: int
    positive_kappa_count: int
    adjacent_negative_debt: Fraction
    adjacent_debt_bound: Fraction


def audit_q_atom_identities(gaps: Sequence[int], *, old_count: int) -> QAtomAudit:
    """Recompute every central Wave 8 identity on one exact gap vector."""
    weights = _validated_gaps(gaps, old_count=old_count)
    m = old_count
    length = 2 * m
    old_indices = tuple(range(m))
    shell_indices = tuple(range(m, length))
    vectors = tuple(_z(index, length) for index in range(length))
    old_mass = sum(weights[:m])
    shell_mass = sum(weights[m:])
    full_mass = old_mass + shell_mass

    old_mean = _weighted_mean(
        tuple(vectors[index] for index in old_indices),
        weights[:m],
    )
    shell_mean = _weighted_mean(
        tuple(vectors[index] for index in shell_indices),
        weights[m:],
    )
    mean_difference = _vector_subtract(old_mean, shell_mean)
    shell_matrix = _matrix_scale(
        shell_mass,
        _weighted_covariance(
            tuple(vectors[index] for index in shell_indices),
            weights[m:],
        ),
    )
    rank_one_matrix = _matrix_scale(
        Fraction(old_mass * shell_mass, full_mass),
        _outer(mean_difference),
    )

    def pair_matrix(
        indices_left: Sequence[int], indices_right: Sequence[int]
    ) -> Matrix2:
        rows: list[Matrix2] = []
        same = indices_left is indices_right
        for first in indices_left:
            for second in indices_right:
                if same and first >= second:
                    continue
                delta = _vector_subtract(vectors[second], vectors[first])
                rows.append(
                    _matrix_scale(weights[first] * weights[second], _outer(delta))
                )
        zero: Matrix2 = ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(0)))
        return _matrix_add(*rows) if rows else zero

    old_pairs = pair_matrix(old_indices, old_indices)
    shell_pairs = pair_matrix(shell_indices, shell_indices)
    cross_pairs = pair_matrix(old_indices, shell_indices)
    if shell_matrix != _matrix_scale(Fraction(1, shell_mass), shell_pairs):
        raise AssertionError("newborn covariance pair identity failed")
    rank_pair_form = _matrix_add(
        _matrix_scale(Fraction(1, full_mass), cross_pairs),
        _matrix_scale(
            -Fraction(shell_mass, old_mass * full_mass),
            old_pairs,
        ),
        _matrix_scale(
            -Fraction(old_mass, shell_mass * full_mass),
            shell_pairs,
        ),
    )
    if rank_one_matrix != rank_pair_form:
        raise AssertionError("rank-one two-sample pair identity failed")

    q_matrix = _matrix_add(shell_matrix, rank_one_matrix)
    short_q_form = _matrix_add(
        _matrix_scale(
            Fraction(1, full_mass),
            _matrix_add(cross_pairs, shell_pairs),
        ),
        _matrix_scale(
            -Fraction(shell_mass, old_mass * full_mass),
            old_pairs,
        ),
    )
    if q_matrix != short_q_form:
        raise AssertionError("short signed Q pair identity failed")

    prefix_masses = tuple(sum(weights[:rank]) for rank in range(1, m))
    suffix_masses = tuple(sum(weights[m + rank :]) for rank in range(1, m))
    abel_terms = (
        tuple(
            _vector_scale(
                Fraction(prefix_masses[rank - 1], old_mass),
                _vector_subtract(vectors[rank], vectors[rank - 1]),
            )
            for rank in range(1, m)
        )
        + (_vector_subtract(vectors[m], vectors[m - 1]),)
        + tuple(
            _vector_scale(
                Fraction(suffix_masses[rank - 1], shell_mass),
                _vector_subtract(vectors[m + rank], vectors[m + rank - 1]),
            )
            for rank in range(1, m)
        )
    )
    abel_difference = _vector_scale(-1, _vector_add(*abel_terms))
    if mean_difference != abel_difference:
        raise AssertionError("rank-one Abel boundary-fan identity failed")

    shell_energy = _h_inner(shell_matrix)
    square_energy = sum(
        (
            shell_kappa(start, end, old_count=m)
            * contiguous_gap_sum(weights, start, end) ** 2
            for start in shell_indices
            for end in range(start, length)
        ),
        Fraction(0),
    ) / (2 * shell_mass)
    if shell_energy != square_energy:
        raise AssertionError("signed contiguous-square expansion failed")

    negative = 0
    positive = 0
    for start in shell_indices:
        for end in range(start, length):
            coefficient = shell_kappa(start, end, old_count=m)
            expected_negative = (start == m and end < length - 1) or (
                end == length - 1 and start > m
            )
            if coefficient == 0 or (coefficient < 0) != expected_negative:
                raise AssertionError("complete kappa sign classification failed")
            negative += coefficient < 0
            positive += coefficient > 0

    normalized_q = _h_inner(q_matrix) / full_mass
    shell_envelope = sum(
        (
            kernel_phi(first, second, length=length)
            * contiguous_gap_sum(weights, first, second) ** 2
            for first in shell_indices
            for second in range(first + 1, length)
        ),
        Fraction(0),
    ) / (4 * shell_mass * full_mass)
    cross_envelope = sum(
        (
            kernel_phi(first, second, length=length)
            * contiguous_gap_sum(weights, first, second) ** 2
            for first in range(1, m)
            for second in shell_indices
        ),
        Fraction(0),
    ) / (4 * full_mass * full_mass)
    artificial_boundary = Fraction(23 * shell_mass, 105 * full_mass * full_mass)
    envelope = shell_envelope + cross_envelope + artificial_boundary
    if not 0 <= normalized_q <= envelope:
        raise AssertionError("positive non-adjacent atom envelope failed")

    last = length - 1
    adjacent_debt = (
        -shell_kappa(m, m, old_count=m) * weights[m] ** 2
        - shell_kappa(last, last, old_count=m) * weights[last] ** 2
    )
    tau_upper = Fraction(3 * full_mass, 2)
    delta_upper = Fraction(full_mass)
    adjacent_bound = Fraction(36, 35 * length * length) * (
        tau_upper**2 + delta_upper**2
    )
    if adjacent_debt > adjacent_bound:
        raise AssertionError("adjacent kappa-debt bound failed")

    return QAtomAudit(
        old_count=m,
        old_mass=old_mass,
        shell_mass=shell_mass,
        full_mass=full_mass,
        shell_h_energy=shell_energy,
        rank_one_h_energy=_h_inner(rank_one_matrix),
        normalized_q_charge=normalized_q,
        positive_envelope=envelope,
        negative_kappa_count=negative,
        positive_kappa_count=positive,
        adjacent_negative_debt=adjacent_debt,
        adjacent_debt_bound=adjacent_bound,
    )


@dataclass(frozen=True)
class NonAdjacentNecessityAudit:
    points: tuple[int, ...]
    boundary_debt: Fraction
    corner_asset: Fraction
    adjacent_asset: Fraction
    nonadjacent_asset: Fraction
    deficit_without_nonadjacent: Fraction
    surplus_with_nonadjacent: Fraction
    shell_h_energy: Fraction


def nonadjacent_necessity_audit() -> NonAdjacentNecessityAudit:
    """Rebuild the exact eight-mark bulk-nonadjacent no-go table."""
    gaps = (1, 8, 16, 32, 2, 256, 4, 1)
    points = points_from_gap_weights(gaps)
    if not is_golomb_from_gap_weights(gaps):
        raise AssertionError("the eight-mark no-go fixture is not Golomb")
    m = 4
    length = 8
    signed = {
        (start, end): shell_kappa(start, end, old_count=m)
        * contiguous_gap_sum(gaps, start, end) ** 2
        for start in range(m, length)
        for end in range(start, length)
    }
    boundary = -sum((value for value in signed.values() if value < 0), Fraction(0))
    corner = signed[(m, length - 1)]
    adjacent = sum(
        (signed[(index, index)] for index in range(m + 1, length - 1)),
        Fraction(0),
    )
    nonadjacent = sum(
        (
            signed[(start, end)]
            for start in range(m + 1, length - 1)
            for end in range(start + 1, length - 1)
        ),
        Fraction(0),
    )
    deficit = boundary - corner - adjacent
    surplus = corner + adjacent + nonadjacent - boundary
    shell_energy = sum(signed.values(), Fraction(0)) / (2 * sum(gaps[m:]))
    if not deficit > 0 or not surplus > 0:
        raise AssertionError("the non-adjacent necessity margins have wrong signs")
    return NonAdjacentNecessityAudit(
        points=points,
        boundary_debt=boundary,
        corner_asset=corner,
        adjacent_asset=adjacent,
        nonadjacent_asset=nonadjacent,
        deficit_without_nonadjacent=deficit,
        surplus_with_nonadjacent=surplus,
        shell_h_energy=shell_energy,
    )


def rank_one_to_shell_ratio(parameter: int) -> Fraction:
    """Return the exact ratio for ``(0,D,3D,3D+1)`` at ``m=2``."""
    if not isinstance(parameter, int) or parameter < 2:
        raise ValueError("parameter must be an integer at least two")
    gaps = (1, parameter, 2 * parameter, 1)
    audit = audit_q_atom_identities(gaps, old_count=2)
    return audit.rank_one_h_energy / audit.shell_h_energy
