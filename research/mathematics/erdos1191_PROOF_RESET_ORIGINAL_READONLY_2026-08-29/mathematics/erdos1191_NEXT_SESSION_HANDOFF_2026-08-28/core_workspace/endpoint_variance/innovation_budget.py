"""Exact adjoint-Lyapunov accounting for the gap covariance recursion."""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from gap_measure_dynamics import B_MATRIX, Matrix2, is_positive_semidefinite


E_MATRIX: Matrix2 = (
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(0)),
)
ZERO_MATRIX: Matrix2 = (
    (Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0)),
)
LYAPUNOV_MATRIX: Matrix2 = (
    (Fraction(16, 15), Fraction(8, 105)),
    (Fraction(8, 105), Fraction(4, 35)),
)
ABSTRACT_COVARIANCE: Matrix2 = (
    (Fraction(1, 72), Fraction(0)),
    (Fraction(0), Fraction(1, 6)),
)


def matrix_add(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (left[0][0] + right[0][0], left[0][1] + right[0][1]),
        (left[1][0] + right[1][0], left[1][1] + right[1][1]),
    )


def matrix_subtract(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (left[0][0] - right[0][0], left[0][1] - right[0][1]),
        (left[1][0] - right[1][0], left[1][1] - right[1][1]),
    )


def matrix_scale(scale: int | Fraction, matrix: Matrix2) -> Matrix2:
    exact = Fraction(scale)
    return (
        (exact * matrix[0][0], exact * matrix[0][1]),
        (exact * matrix[1][0], exact * matrix[1][1]),
    )


def matrix_multiply(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def transpose(matrix: Matrix2) -> Matrix2:
    return ((matrix[0][0], matrix[1][0]), (matrix[0][1], matrix[1][1]))


def frobenius_inner(left: Matrix2, right: Matrix2) -> Fraction:
    return sum(
        (left[row][column] * right[row][column] for row in range(2) for column in range(2)),
        Fraction(0),
    )


def determinant(matrix: Matrix2) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def transported(matrix: Matrix2) -> Matrix2:
    """Return ``B matrix B^T`` exactly."""
    return matrix_multiply(matrix_multiply(B_MATRIX, matrix), transpose(B_MATRIX))


def adjoint_transport(matrix: Matrix2) -> Matrix2:
    """Return ``B^T matrix B`` exactly."""
    return matrix_multiply(matrix_multiply(transpose(B_MATRIX), matrix), B_MATRIX)


def verify_infinite_horizon_lyapunov_matrix() -> bool:
    """Check ``H-B^T H B=E`` and positive definiteness exactly."""
    residual = matrix_subtract(LYAPUNOV_MATRIX, adjoint_transport(LYAPUNOV_MATRIX))
    return (
        residual == E_MATRIX
        and is_positive_semidefinite(LYAPUNOV_MATRIX)
        and determinant(LYAPUNOV_MATRIX) > 0
    )


def adjoint_weights(moduli: tuple[int, ...]) -> tuple[Matrix2, ...]:
    """Return ``H_1,...,H_{J+1}`` for positive ``N_1,...,N_{J+1}``."""
    if len(moduli) < 2 or any(not isinstance(value, int) or value <= 0 for value in moduli):
        raise ValueError("moduli must contain at least two positive integers")
    if any(left > right for left, right in zip(moduli, moduli[1:])):
        raise ValueError("moduli must be nondecreasing")
    weights = [ZERO_MATRIX for _ in moduli]
    for index in range(len(moduli) - 2, -1, -1):
        rho = Fraction(moduli[index], moduli[index + 1])
        weights[index] = matrix_add(
            E_MATRIX,
            matrix_scale(rho, adjoint_transport(weights[index + 1])),
        )
    return tuple(weights)


def three_point_covariance() -> Matrix2:
    """Covariance of ``z=(u(1-u),u)`` for uniform ``u in {0,1/2,1}``."""
    support = (Fraction(0), Fraction(1, 2), Fraction(1))
    values = tuple((u * (1 - u), u) for u in support)
    mean = tuple(sum(value[index] for value in values) / 3 for index in range(2))
    return (
        (
            sum((value[0] - mean[0]) ** 2 for value in values) / 3,
            sum((value[0] - mean[0]) * (value[1] - mean[1]) for value in values) / 3,
        ),
        (
            sum((value[1] - mean[1]) * (value[0] - mean[0]) for value in values) / 3,
            sum((value[1] - mean[1]) ** 2 for value in values) / 3,
        ),
    )


def abstract_modulus(index: int, scale: int = 3) -> int:
    """Return the critical abstract modulus ``scale*4^index*index``."""
    if not isinstance(index, int) or index < 1:
        raise ValueError("index must be a positive integer")
    if not isinstance(scale, int) or scale < 1:
        raise ValueError("scale must be a positive integer")
    return scale * 4**index * index


def abstract_raw_innovation(index: int, scale: int = 3) -> Matrix2:
    """Return ``Q_j=N_(j+1)R-N_j B R B^T`` for the abstract no-go orbit."""
    current = abstract_modulus(index, scale)
    following = abstract_modulus(index + 1, scale)
    return matrix_subtract(
        matrix_scale(following, ABSTRACT_COVARIANCE),
        matrix_scale(current, transported(ABSTRACT_COVARIANCE)),
    )


@dataclass(frozen=True)
class AbstractOrbitAudit:
    horizon: int
    scale: int
    functional_sum: Fraction
    boundary_term: Fraction
    innovation_sum: Fraction
    minimum_innovation_determinant: Fraction


def audit_abstract_orbit(horizon: int, scale: int = 3) -> AbstractOrbitAudit:
    """Verify the adjoint identity on the linear-growth PSD-innovation orbit."""
    if not isinstance(horizon, int) or horizon < 1:
        raise ValueError("horizon must be a positive integer")
    moduli = tuple(abstract_modulus(index, scale) for index in range(1, horizon + 2))
    weights = adjoint_weights(moduli)
    minimum_determinant: Fraction | None = None
    innovation_sum = Fraction(0)
    for offset, index in enumerate(range(1, horizon + 1)):
        raw = abstract_raw_innovation(index, scale)
        if not is_positive_semidefinite(raw):
            raise AssertionError("abstract innovation was not positive semidefinite")
        raw_determinant = determinant(raw)
        if minimum_determinant is None or raw_determinant < minimum_determinant:
            minimum_determinant = raw_determinant
        normalized = matrix_scale(Fraction(1, moduli[offset + 1]), raw)
        innovation_sum += frobenius_inner(weights[offset + 1], normalized)
    functional_sum = Fraction(horizon, 72)
    boundary_term = frobenius_inner(weights[0], ABSTRACT_COVARIANCE)
    if functional_sum != boundary_term + innovation_sum:
        raise AssertionError("adjoint-Lyapunov telescoping identity failed")
    if minimum_determinant is None:
        raise AssertionError("empty abstract orbit audit")
    return AbstractOrbitAudit(
        horizon=horizon,
        scale=scale,
        functional_sum=functional_sum,
        boundary_term=boundary_term,
        innovation_sum=innovation_sum,
        minimum_innovation_determinant=minimum_determinant,
    )
