"""Exact dyadic dynamics of diameter-gap probability measures."""
from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from fractions import Fraction

from sidon_block_variance import diameter_gap_profile, is_golomb_ruler, positive_gap_variance


Vector2 = tuple[Fraction, Fraction]
Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]
B_MATRIX: Matrix2 = (
    (Fraction(1, 4), Fraction(1, 4)),
    (Fraction(0), Fraction(1, 2)),
)


def _validated_points(points: Iterable[int]) -> tuple[int, ...]:
    marks = tuple(points)
    if any(not isinstance(mark, int) for mark in marks):
        raise TypeError("points must be integers")
    if len(marks) < 2 or tuple(sorted(marks)) != marks or len(set(marks)) != len(marks):
        raise ValueError("points must be a strictly increasing sequence of length at least two")
    return marks


def _weighted_mean(values: tuple[Vector2, ...], weights: tuple[int, ...]) -> Vector2:
    total = sum(weights)
    return (
        sum(weight * value[0] for weight, value in zip(weights, values)) / total,
        sum(weight * value[1] for weight, value in zip(weights, values)) / total,
    )


def _weighted_covariance(values: tuple[Vector2, ...], weights: tuple[int, ...]) -> Matrix2:
    mean = _weighted_mean(values, weights)
    total = sum(weights)
    covariance_00 = sum(
        weight * (value[0] - mean[0]) ** 2 for weight, value in zip(weights, values)
    ) / total
    covariance_01 = sum(
        weight * (value[0] - mean[0]) * (value[1] - mean[1])
        for weight, value in zip(weights, values)
    ) / total
    covariance_11 = sum(
        weight * (value[1] - mean[1]) ** 2 for weight, value in zip(weights, values)
    ) / total
    return ((covariance_00, covariance_01), (covariance_01, covariance_11))


def _matrix_add(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def _matrix_subtract(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(left[row][column] - right[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def _matrix_scale(scale: Fraction | int, matrix: Matrix2) -> Matrix2:
    exact_scale = Fraction(scale)
    return tuple(
        tuple(exact_scale * matrix[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def _matrix_multiply(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(
            sum((left[row][index] * right[index][column] for index in range(2)), Fraction(0))
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def _transpose(matrix: Matrix2) -> Matrix2:
    return ((matrix[0][0], matrix[1][0]), (matrix[0][1], matrix[1][1]))


def _matrix_vector(matrix: Matrix2, vector: Vector2) -> Vector2:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    )


def _outer(vector: Vector2) -> Matrix2:
    return (
        (vector[0] * vector[0], vector[0] * vector[1]),
        (vector[1] * vector[0], vector[1] * vector[1]),
    )


def is_positive_semidefinite(matrix: Matrix2) -> bool:
    """Exact 2-by-2 positive-semidefinite test for a symmetric matrix."""
    if matrix[0][1] != matrix[1][0]:
        return False
    return (
        matrix[0][0] >= 0
        and matrix[1][1] >= 0
        and matrix[0][0] * matrix[1][1] - matrix[0][1] ** 2 >= 0
    )


def gap_measure_data(points: Iterable[int]) -> tuple[int, tuple[int, ...], tuple[Fraction, ...]]:
    """Return modulus, integer gap weights, and normalized rank locations."""
    marks = _validated_points(points)
    modulus, gaps, _ = diameter_gap_profile(marks)
    count = len(marks)
    locations = tuple(Fraction(index, count) for index in range(count))
    return modulus, gaps, locations


def gap_rank_variance(points: Iterable[int]) -> Fraction:
    """Return ``Var_nu(U)`` for the diameter-gap probability measure."""
    modulus, gaps, locations = gap_measure_data(points)
    mean = sum(gap * location for gap, location in zip(gaps, locations)) / modulus
    return sum(
        gap * (location - mean) ** 2 for gap, location in zip(gaps, locations)
    ) / modulus


def normalized_gap_function_variance(points: Iterable[int], dilation: int = 1) -> Fraction:
    """Return ``Var_nu(f(U/dilation))`` for ``f(u)=u(1-u)``."""
    if not isinstance(dilation, int) or dilation < 1:
        raise ValueError("dilation must be a positive integer")
    modulus, gaps, locations = gap_measure_data(points)
    values = tuple(
        (location / dilation) * (1 - location / dilation) for location in locations
    )
    mean = sum(gap * value for gap, value in zip(gaps, values)) / modulus
    return sum(gap * (value - mean) ** 2 for gap, value in zip(gaps, values)) / modulus


def gap_covariance_matrix(points: Iterable[int]) -> Matrix2:
    """Return ``Cov_nu((f(U),U))`` exactly."""
    _, gaps, locations = gap_measure_data(points)
    values = tuple((location * (1 - location), location) for location in locations)
    return _weighted_covariance(values, gaps)


def diameter_compensated_gap_matrix(points: Iterable[int]) -> Matrix2:
    """Return ``N*Cov_nu((f(U),U))``."""
    modulus, _, _ = gap_measure_data(points)
    return _matrix_scale(modulus, gap_covariance_matrix(points))


@dataclass(frozen=True)
class DyadicGapUpdate:
    old_count: int
    old_modulus: int
    new_modulus: int
    old_term: Matrix2
    innovation: Matrix2
    new_matrix: Matrix2


def dyadic_gap_matrix_update(points: Iterable[int], old_count: int) -> DyadicGapUpdate:
    """Certify ``M_2m = B M_m B^T + Q`` with ``Q`` positive semidefinite."""
    marks = _validated_points(points)
    if not isinstance(old_count, int) or old_count < 2 or len(marks) != 2 * old_count:
        raise ValueError("the full set must have exactly 2*old_count marks")
    old = marks[:old_count]
    old_modulus, old_gaps, old_locations = gap_measure_data(old)
    new_modulus, full_gaps, _ = gap_measure_data(marks)
    growth = new_modulus - old_modulus
    if growth <= 0:
        raise AssertionError("diameter modulus did not grow")

    old_values = tuple((u * (1 - u), u) for u in old_locations)
    old_mean = _weighted_mean(old_values, old_gaps)
    new_shell_weights = tuple(full_gaps[index] for index in range(old_count, 2 * old_count))
    new_shell_locations = tuple(
        Fraction(index, 2 * old_count) for index in range(old_count, 2 * old_count)
    )
    new_shell_values = tuple((u * (1 - u), u) for u in new_shell_locations)
    shell_mean = _weighted_mean(new_shell_values, new_shell_weights)
    shell_covariance = _weighted_covariance(new_shell_values, new_shell_weights)

    old_matrix = diameter_compensated_gap_matrix(old)
    old_term = _matrix_multiply(_matrix_multiply(B_MATRIX, old_matrix), _transpose(B_MATRIX))
    transformed_mean = _matrix_vector(B_MATRIX, old_mean)
    mean_difference = (
        transformed_mean[0] - shell_mean[0],
        transformed_mean[1] - shell_mean[1],
    )
    innovation = _matrix_add(
        _matrix_scale(growth, shell_covariance),
        _matrix_scale(Fraction(old_modulus * growth, new_modulus), _outer(mean_difference)),
    )
    new_matrix = diameter_compensated_gap_matrix(marks)
    if new_matrix != _matrix_add(old_term, innovation):
        raise AssertionError("exact dyadic covariance update failed")
    if not is_positive_semidefinite(innovation):
        raise AssertionError("dyadic gap innovation was not positive semidefinite")
    if not is_positive_semidefinite(_matrix_subtract(new_matrix, old_term)):
        raise AssertionError("diameter-compensated matrix inequality failed")
    return DyadicGapUpdate(
        old_count=old_count,
        old_modulus=old_modulus,
        new_modulus=new_modulus,
        old_term=old_term,
        innovation=innovation,
        new_matrix=new_matrix,
    )


@dataclass(frozen=True)
class TwoStepGapAgingWitness:
    old_count: int
    final_count: int
    old_modulus: int
    final_modulus: int
    old_rank_variance: Fraction
    old_rank_lower_bound: Fraction
    final_normalized_variance: Fraction
    aged_component_lower_bound: Fraction
    distinct_gap_lower_bound: Fraction


def two_step_distinct_gap_witness(points: Iterable[int]) -> TwoStepGapAgingWitness:
    """Certify the optimized two-step distinct-adjacent-gap lower bound."""
    marks = _validated_points(points)
    final_count = len(marks)
    if final_count < 16 or final_count % 16:
        raise ValueError("the theorem requires final_count=4m with 4|m and m>=4")
    old_count = final_count // 4
    old = marks[:old_count]
    if not is_golomb_ruler(old):
        raise ValueError("the theorem requires the first m marks to form a Sidon/Golomb ruler")
    old_modulus, _, _ = gap_measure_data(old)
    final_modulus, _, _ = gap_measure_data(marks)
    old_rank_variance = gap_rank_variance(old)
    old_rank_lower_bound = Fraction(9 * old_count**2 - 16, 1024 * old_modulus)
    final_normalized_variance = positive_gap_variance(marks) / final_count**4
    aged_component_lower_bound = (
        Fraction(old_modulus, final_modulus)
        * Fraction(1, 64)
        * old_rank_variance
    )
    distinct_gap_lower_bound = Fraction(
        9 * final_count**2 - 256,
        1_048_576 * final_modulus,
    )
    if old_rank_variance < old_rank_lower_bound:
        raise AssertionError("optimized distinct-adjacent-gap rank bound failed")
    if final_normalized_variance < aged_component_lower_bound:
        raise AssertionError("two-step old-component persistence failed")
    if aged_component_lower_bound < distinct_gap_lower_bound:
        raise AssertionError("two-step distinct-gap constant chain failed")
    return TwoStepGapAgingWitness(
        old_count=old_count,
        final_count=final_count,
        old_modulus=old_modulus,
        final_modulus=final_modulus,
        old_rank_variance=old_rank_variance,
        old_rank_lower_bound=old_rank_lower_bound,
        final_normalized_variance=final_normalized_variance,
        aged_component_lower_bound=aged_component_lower_bound,
        distinct_gap_lower_bound=distinct_gap_lower_bound,
    )
