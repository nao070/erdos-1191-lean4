"""Exact normalized Route-C cross-kernel probe; Q1/Q2 remain unresolved.

Standard-library floating point is used only to discover a candidate dual
active set.  Every accepted boundary QP is then independently replayed with
Fraction arithmetic and must satisfy the complete primal/dual KKT system
exactly.  No NumPy/SciPy runtime is required.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
import math
from functools import lru_cache
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Sequence

Vector = tuple[Fraction, ...]
Matrix = tuple[tuple[Fraction, ...], ...]
KernelPair = tuple[Vector, Vector]


class CertificateError(ValueError):
    """Raised when an exact mathematical or claim-boundary check fails."""


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def dot(left: Sequence[Fraction], right: Sequence[Fraction]) -> Fraction:
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


def matvec(matrix: Sequence[Sequence[Fraction]], vector: Sequence[Fraction]) -> list[Fraction]:
    return [dot(row, vector) for row in matrix]


def transpose(matrix: Sequence[Sequence[Fraction]]) -> list[list[Fraction]]:
    if not matrix:
        return []
    return [list(column) for column in zip(*matrix)]


def matmul(
    left: Sequence[Sequence[Fraction]], right: Sequence[Sequence[Fraction]]
) -> list[list[Fraction]]:
    right_t = transpose(right)
    return [[dot(row, column) for column in right_t] for row in left]


def identity(size: int) -> list[list[Fraction]]:
    return [[Fraction(int(i == j)) for j in range(size)] for i in range(size)]


def solve_linear(
    matrix: Sequence[Sequence[Fraction]], rhs: Sequence[Fraction]
) -> list[Fraction]:
    size = len(matrix)
    if size == 0:
        return []
    augmented = [list(row) + [value] for row, value in zip(matrix, rhs)]
    for column in range(size):
        pivot = next((row for row in range(column, size) if augmented[row][column]), None)
        if pivot is None:
            raise CertificateError("singular exact active-set system")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(size):
            if row == column or augmented[row][column] == 0:
                continue
            scale = augmented[row][column]
            augmented[row] = [
                value - scale * pivot_value
                for value, pivot_value in zip(augmented[row], augmented[column])
            ]
    return [augmented[row][-1] for row in range(size)]


def inverse_matrix(matrix: Matrix) -> Matrix:
    size = len(matrix)
    columns = [solve_linear(matrix, row) for row in identity(size)]
    return tuple(tuple(columns[column][row] for column in range(size)) for row in range(size))


def determinant(matrix: Matrix) -> Fraction:
    size = len(matrix)
    work = [list(row) for row in matrix]
    result = Fraction(1)
    sign = 1
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign *= -1
        pivot_value = work[column][column]
        result *= pivot_value
        for row in range(column + 1, size):
            scale = work[row][column] / pivot_value
            for index in range(column, size):
                work[row][index] -= scale * work[column][index]
    return sign * result


def validate_pd(matrix: Matrix) -> None:
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise CertificateError("H must be a nonempty square matrix")
    if any(matrix[i][j] != matrix[j][i] for i in range(size) for j in range(size)):
        raise CertificateError("H must be symmetric")
    for leading in range(1, size + 1):
        minor = tuple(tuple(matrix[i][j] for j in range(leading)) for i in range(leading))
        if determinant(minor) <= 0:
            raise CertificateError("H is not positive definite")


def validate_gamma(gamma: Vector, dimension: int) -> None:
    if len(gamma) != dimension or any(value < 0 for value in gamma):
        raise CertificateError("gamma must be coordinatewise nonnegative")
    if sum(gamma, Fraction(0)) != 1:
        raise CertificateError("gamma must lie in the simplex")


def validate_kernel(kernel: Vector) -> None:
    if not kernel or any(value < 0 for value in kernel):
        raise CertificateError("kernel must be nonnegative and nonempty")
    if sum(kernel, Fraction(0)) != 1:
        raise CertificateError("kernel must have exact mass one")
    if kernel != tuple(reversed(kernel)):
        raise CertificateError("kernel must be symmetric")


def discrete_cross_correlation(
    kernels: KernelPair, matrix: Matrix, shift: int
) -> Fraction:
    size = len(kernels[0])
    if shift < 0:
        shift = -shift
    if shift >= size:
        return Fraction(0)
    return sum(
        (
            matrix[r][s]
            * sum(
                (kernels[r][index] * kernels[s][index + shift] for index in range(size - shift)),
                Fraction(0),
            )
            for r in range(2)
            for s in range(2)
        ),
        Fraction(0),
    )


def shift_gate(kernels: KernelPair, matrix: Matrix) -> bool:
    return all(
        discrete_cross_correlation(kernels, matrix, shift) >= 0
        for shift in range(1, len(kernels[0]))
    )


def block_lift_correlation(
    kernels: KernelPair, matrix: Matrix, block_length: int, shift: int
) -> Fraction:
    """Exact lift for shift=q*h+t: ((h-t)C(q)+tC(q+1))/h^2."""

    if block_length < 1 or shift < 0:
        raise ValueError("block length must be positive and shift nonnegative")
    quotient, remainder = divmod(shift, block_length)
    return (
        (block_length - remainder) * discrete_cross_correlation(kernels, matrix, quotient)
        + remainder * discrete_cross_correlation(kernels, matrix, quotient + 1)
    ) / (block_length * block_length)


def quadratic(vector: Vector, matrix: Matrix) -> Fraction:
    return dot(vector, matvec(matrix, vector))


def normalized_parameters(
    kernels: KernelPair, matrix: Matrix, gamma: Vector
) -> dict[str, Fraction]:
    validate_pd(matrix)
    validate_gamma(gamma, len(matrix))
    for kernel in kernels:
        validate_kernel(kernel)
    inverse = inverse_matrix(matrix)
    ones = tuple(Fraction(1) for _ in matrix)
    beta = quadratic(gamma, inverse)
    s_value = quadratic(ones, matrix)
    a_value = len(kernels[0]) * discrete_cross_correlation(kernels, matrix, 0)
    return {"beta": beta, "s": s_value, "delta": beta * s_value, "a": a_value}


def equality_gamma(matrix: Matrix) -> Vector:
    validate_pd(matrix)
    ones = tuple(Fraction(1) for _ in matrix)
    image = tuple(matvec(matrix, ones))
    s_value = sum(image, Fraction(0))
    candidate = tuple(value / s_value for value in image)
    if any(value < 0 for value in candidate):
        raise CertificateError("equality gamma=H1/s is not coordinatewise nonnegative")
    return candidate


def boundary_problem(
    kernels: KernelPair, matrix: Matrix, gamma: Vector, level: int
) -> dict[str, object]:
    params = normalized_parameters(kernels, matrix, gamma)
    if level < 1:
        raise ValueError("L must be positive")
    inverse = inverse_matrix(matrix)
    active_coordinates = tuple(index for index, value in enumerate(gamma) if value > 0)
    if not active_coordinates:
        raise CertificateError("at least one gamma coordinate must be positive")
    # q=gamma*w, so gamma-zero coordinates are identically zero and deleted.
    block_d = tuple(
        tuple(inverse[r][s] for s in active_coordinates) for r in active_coordinates
    )
    block_d_inverse = inverse_matrix(block_d)
    m_value = len(kernels[0])
    n_value = level * m_value
    coordinate_count = len(active_coordinates)
    variable_count = n_value * coordinate_count
    cover: list[list[Fraction]] = [
        [Fraction(0) for _ in range(variable_count)] for _ in range(n_value)
    ]
    rhs: list[Fraction] = []
    for row in range(n_value):
        tail = Fraction(0)
        for r, kernel in enumerate(kernels):
            for i, weight in enumerate(kernel):
                target = row + i
                if target < n_value and r in active_coordinates:
                    local = active_coordinates.index(r)
                    cover[row][target * coordinate_count + local] += weight
                elif target >= n_value:
                    tail += gamma[r] * weight
        rhs.append(1 - tail)
    return {
        "kernels": kernels,
        "matrix": matrix,
        "gamma": gamma,
        "L": level,
        "m": m_value,
        "n": n_value,
        "active_coordinates": active_coordinates,
        "coordinate_count": coordinate_count,
        "variable_count": variable_count,
        "D_block": block_d,
        "D_inverse_block": block_d_inverse,
        "A": cover,
        "c": rhs,
        **params,
    }


def block_apply(block: Matrix, vector: Sequence[Fraction], block_count: int) -> list[Fraction]:
    width = len(block)
    result: list[Fraction] = []
    for index in range(block_count):
        start = index * width
        result.extend(matvec(block, vector[start : start + width]))
    return result


def solve_linear_float(
    matrix: Sequence[Sequence[float]], rhs: Sequence[float], tolerance: float = 1e-12
) -> list[float]:
    """Partial-pivot float solve used only for active-set discovery."""

    size = len(matrix)
    work = [list(row) + [value] for row, value in zip(matrix, rhs)]
    for column in range(size):
        pivot = max(range(column, size), key=lambda row: abs(work[row][column]))
        if abs(work[pivot][column]) <= tolerance:
            raise CertificateError("singular floating active-set system")
        work[column], work[pivot] = work[pivot], work[column]
        pivot_value = work[column][column]
        for row in range(column + 1, size):
            scale = work[row][column] / pivot_value
            if scale == 0.0:
                continue
            for index in range(column, size + 1):
                work[row][index] -= scale * work[column][index]
    result = [0.0 for _ in range(size)]
    for row in range(size - 1, -1, -1):
        tail = sum(work[row][column] * result[column] for column in range(row + 1, size))
        result[row] = (work[row][-1] - tail) / work[row][row]
    return result


def discover_active_set(problem: Mapping[str, object]) -> tuple[int, ...]:
    """Deterministic Lawson--Hanson-style discovery for the dual QP.

    For G=A D^{-1} A^T, the exact dual KKT equations are
    y>=0, (G y)/2-c>=0, and y_j((G y)/2-c)_j=0.  This routine uses floats
    only to guess the positive coordinates of y.  ``exact_active_solution``
    recomputes that candidate from rational input and accepts it only after
    exact primal/dual/KKT verification.
    """

    cover = problem["A"]
    rhs = problem["c"]
    assert isinstance(cover, list) and isinstance(rhs, list)
    n_value = int(problem["n"])
    d_inverse_block = problem["D_inverse_block"]
    assert isinstance(d_inverse_block, tuple)
    transformed = [block_apply(d_inverse_block, row, n_value) for row in cover]
    gram = [
        [float(dot(left, right)) for right in transformed]
        for left in cover
    ]
    target = [2.0 * float(value) for value in rhs]

    tolerance = 1e-10
    dual = [0.0 for _ in range(n_value)]
    passive: list[int] = []
    iteration_limit = 20 * n_value * n_value + 1
    for _ in range(iteration_limit):
        residual = [
            target[row] - sum(gram[row][column] * dual[column] for column in range(n_value))
            for row in range(n_value)
        ]
        entering = [
            row for row in range(n_value) if row not in passive and residual[row] > tolerance
        ]
        if not entering:
            return tuple(passive)
        # Largest dual-gradient violation, with the row index as a stable tie-break.
        chosen = min(entering, key=lambda row: (-residual[row], row))
        passive.append(chosen)
        passive.sort()

        while True:
            submatrix = [[gram[row][column] for column in passive] for row in passive]
            subtarget = [target[row] for row in passive]
            candidate_values = solve_linear_float(submatrix, subtarget)
            if all(value > tolerance for value in candidate_values):
                dual = [0.0 for _ in range(n_value)]
                for row, value in zip(passive, candidate_values):
                    dual[row] = value
                break

            candidate = [0.0 for _ in range(n_value)]
            for row, value in zip(passive, candidate_values):
                candidate[row] = value
            ratios = [
                dual[row] / (dual[row] - candidate[row])
                for row in passive
                if candidate[row] <= tolerance and dual[row] - candidate[row] > tolerance
            ]
            alpha = min(ratios, default=0.0)
            dual = [
                old + alpha * (new - old) for old, new in zip(dual, candidate)
            ]
            passive = [row for row in passive if dual[row] > tolerance]
    raise CertificateError("deterministic floating active-set discovery did not converge")


def exact_active_solution(
    problem: Mapping[str, object], active_rows: Sequence[int]
) -> dict[str, object]:
    cover = problem["A"]
    rhs = problem["c"]
    assert isinstance(cover, list) and isinstance(rhs, list)
    n_value = int(problem["n"])
    variable_count = int(problem["variable_count"])
    d_block = problem["D_block"]
    d_inverse_block = problem["D_inverse_block"]
    assert isinstance(d_block, tuple) and isinstance(d_inverse_block, tuple)
    active = tuple(active_rows)
    selected = [cover[index] for index in active]
    selected_rhs = [rhs[index] for index in active]

    def d_inverse_apply(vector: Sequence[Fraction]) -> list[Fraction]:
        return block_apply(d_inverse_block, vector, n_value)

    if active:
        gram = [
            [dot(row, d_inverse_apply(other)) for other in selected] for row in selected
        ]
        dual_active = solve_linear(gram, [2 * value for value in selected_rhs])
        at_dual = [
            sum((selected[row][column] * dual_active[row] for row in range(len(active))), Fraction(0))
            for column in range(variable_count)
        ]
        primal = [value / 2 for value in d_inverse_apply(at_dual)]
    else:
        dual_active = []
        primal = [Fraction(0) for _ in range(variable_count)]
    dual = [Fraction(0) for _ in range(n_value)]
    for row, value in zip(active, dual_active):
        dual[row] = value
    slack = [value - bound for value, bound in zip(matvec(cover, primal), rhs)]
    d_primal = block_apply(d_block, primal, n_value)
    at_dual_full = matvec(transpose(cover), dual)
    stationarity = [2 * left - right for left, right in zip(d_primal, at_dual_full)]
    complementarity = [value * gap for value, gap in zip(dual, slack)]
    phi = dot(primal, d_primal)
    gram_dual = dot(dual, matvec(cover, block_apply(d_inverse_block, at_dual_full, n_value)))
    dual_value = dot(rhs, dual) - gram_dual / 4
    certificate = {
        "active_rows": active,
        "q": tuple(primal),
        "y": tuple(dual),
        "slack": tuple(slack),
        "stationarity": tuple(stationarity),
        "complementarity": tuple(complementarity),
        "Phi": phi,
        "dual_value": dual_value,
    }
    validate_qp_certificate(problem, certificate)
    return certificate


def validate_qp_certificate(
    problem: Mapping[str, object], certificate: Mapping[str, object]
) -> None:
    q_value = certificate["q"]
    y_value = certificate["y"]
    if not isinstance(q_value, tuple) or len(q_value) != int(problem["variable_count"]):
        raise CertificateError("q layout includes a free/deleted coordinate or has wrong length")
    if not isinstance(y_value, tuple) or len(y_value) != int(problem["n"]):
        raise CertificateError("dual length mismatch")
    if any(value < 0 for value in certificate["slack"]):
        raise CertificateError("cover constraint failure")
    if any(value < 0 for value in y_value):
        raise CertificateError("dual feasibility failure")
    if any(certificate["stationarity"]):
        raise CertificateError("stationarity failure")
    if any(certificate["complementarity"]):
        raise CertificateError("complementarity failure")
    if certificate["Phi"] != certificate["dual_value"]:
        raise CertificateError("primal-dual value mismatch")


def solve_boundary_qp(problem: Mapping[str, object]) -> dict[str, object]:
    active = discover_active_set(problem)
    try:
        return exact_active_solution(problem, active)
    except CertificateError as first_error:
        for size in range(len(active), -1, -1):
            for subset in itertools.combinations(active, size):
                if subset == active:
                    continue
                try:
                    return exact_active_solution(problem, subset)
                except CertificateError:
                    continue
        raise CertificateError(f"no exact KKT subset found after discovery: {first_error}")


def complete_metrics(
    problem: Mapping[str, object], certificate: Mapping[str, object]
) -> dict[str, Fraction]:
    beta = problem["beta"]
    s_value = problem["s"]
    a_value = problem["a"]
    assert isinstance(beta, Fraction) and isinstance(s_value, Fraction) and isinstance(a_value, Fraction)
    phi = certificate["Phi"]
    assert isinstance(phi, Fraction)
    m_value = int(problem["m"])
    level = int(problem["L"])
    b_h = beta + 2 * (phi / m_value - level * beta)
    return {
        "beta": beta,
        "s": s_value,
        "delta": beta * s_value,
        "a": a_value,
        "Phi": phi,
        "bH": b_h,
        "product": a_value * b_h,
    }


def master_bound(
    cardinality: int,
    ambient_size: int,
    scale: int,
    level: int,
    metrics: Mapping[str, Fraction],
) -> Fraction:
    if ambient_size < 2 * level * scale:
        raise CertificateError("master inequality requires N>=2*L*T")
    if metrics["bH"] <= 0:
        raise CertificateError("master inequality optimization requires bH>0")
    beta = metrics["beta"]
    return (beta * ambient_size + metrics["bH"] * scale - beta) * (
        metrics["s"] + metrics["a"] * (cardinality - 1) / scale
    )


def symmetric_grid(m_value: int, denominator: int = 8) -> list[Vector]:
    if m_value == 3:
        return [
            (Fraction(i, denominator), Fraction(denominator - 2 * i, denominator), Fraction(i, denominator))
            for i in range(denominator // 2 + 1)
        ]
    if m_value == 5:
        values: set[Vector] = set()
        for i in range(denominator // 2 + 1):
            for j in range(denominator // 2 - i + 1):
                center = denominator - 2 * i - 2 * j
                values.add(
                    (
                        Fraction(i, denominator),
                        Fraction(j, denominator),
                        Fraction(center, denominator),
                        Fraction(j, denominator),
                        Fraction(i, denominator),
                    )
                )
        return sorted(values)
    raise ValueError("bounded grid supports only m=3 or m=5")


def negative_b_grid(max_denominator: int = 8) -> list[Fraction]:
    return sorted(
        {
            Fraction(numerator, denominator)
            for denominator in range(2, max_denominator + 1)
            for numerator in range(-denominator + 1, 0)
            if math.gcd(abs(numerator), denominator) == 1
        }
    )


def matrix_b(coefficient: Fraction) -> Matrix:
    return ((Fraction(1), coefficient), (coefficient, Fraction(1)))


def joint_support_is_minimal(kernels: KernelPair) -> bool:
    """Reject an m=5 pair that is merely a common zero-padding of m=3.

    The scale parameter m is the joint block-support length.  Counting a
    common-zero-padded m=3 pair again at m=5 changes a=m*C(0) without changing
    the kernels and is therefore a normalization artifact, not a new grid
    candidate.  m=3 is the smallest audited grid and is retained as-is.
    """

    return len(kernels[0]) <= 3 or any(kernel[0] > 0 for kernel in kernels)


def serialize_qp(certificate: Mapping[str, object]) -> dict[str, object]:
    return {
        "active_rows": list(certificate["active_rows"]),
        "q": [ftext(value) for value in certificate["q"]],
        "y": [ftext(value) for value in certificate["y"]],
        "slack": [ftext(value) for value in certificate["slack"]],
        "Phi": ftext(certificate["Phi"]),
        "dual_value": ftext(certificate["dual_value"]),
    }


def serialize_metrics(metrics: Mapping[str, Fraction]) -> dict[str, str]:
    return {key: ftext(value) for key, value in metrics.items()}


def candidate_record(
    kernels: KernelPair, matrix: Matrix, gamma: Vector, level: int
) -> tuple[dict[str, object], dict[str, Fraction], dict[str, object]]:
    if not shift_gate(kernels, matrix):
        raise CertificateError("every-discrete-shift gate fails")
    problem = boundary_problem(kernels, matrix, gamma, level)
    certificate = solve_boundary_qp(problem)
    metrics = complete_metrics(problem, certificate)
    if metrics["bH"] <= 0:
        raise CertificateError("bH is not positive")
    record = {
        "m": len(kernels[0]),
        "L": level,
        "kernels": [[ftext(value) for value in kernel] for kernel in kernels],
        "H": [[ftext(value) for value in row] for row in matrix],
        "gamma": [ftext(value) for value in gamma],
        "correlations": [
            ftext(discrete_cross_correlation(kernels, matrix, shift))
            for shift in range(len(kernels[0]))
        ],
        "metrics": serialize_metrics(metrics),
        "qp": serialize_qp(certificate),
    }
    return record, metrics, certificate


@lru_cache(maxsize=1)
def exhaustive_search() -> dict[str, object]:
    gamma_half = (Fraction(1, 2), Fraction(1, 2))
    b_values = negative_b_grid(8)
    cross_counts: dict[str, dict[str, int]] = {}
    best_cross: tuple[Fraction, KernelPair, Fraction, int, dict[str, Fraction]] | None = None
    best_same_ratio: tuple[Fraction, KernelPair, Fraction, int] | None = None
    diagonal_counts: dict[str, dict[str, int]] = {}
    best_diagonal: tuple[Fraction, KernelPair, Fraction, int, dict[str, Fraction]] | None = None

    for m_value in (3, 5):
        kernels = symmetric_grid(m_value, 8)
        for level in (1, 2):
            key = f"m{m_value}_L{level}"
            cross_total = 0
            common_padding_skipped = 0
            gate_count = 0
            exact_count = 0
            positive_bh_count = 0
            baseline_cache: dict[KernelPair, Fraction] = {}
            for pair in itertools.combinations(kernels, 2):
                for coefficient in b_values:
                    cross_total += 1
                    if not joint_support_is_minimal(pair):
                        common_padding_skipped += 1
                        continue
                    matrix = matrix_b(coefficient)
                    if not shift_gate(pair, matrix):
                        continue
                    gate_count += 1
                    problem = boundary_problem(pair, matrix, gamma_half, level)
                    certificate = solve_boundary_qp(problem)
                    exact_count += 1
                    metrics = complete_metrics(problem, certificate)
                    if metrics["bH"] <= 0:
                        continue
                    positive_bh_count += 1
                    product = metrics["product"]
                    if best_cross is None or product < best_cross[0]:
                        best_cross = (product, pair, coefficient, level, metrics)
                    if pair not in baseline_cache:
                        baseline_problem = boundary_problem(pair, matrix_b(Fraction(0)), gamma_half, level)
                        baseline_certificate = solve_boundary_qp(baseline_problem)
                        baseline_cache[pair] = complete_metrics(
                            baseline_problem, baseline_certificate
                        )["product"]
                    ratio = product / baseline_cache[pair]
                    if best_same_ratio is None or ratio < best_same_ratio[0]:
                        best_same_ratio = (ratio, pair, coefficient, level)
            cross_counts[key] = {
                "kernel_count": len(kernels),
                "pair_count": len(list(itertools.combinations(kernels, 2))),
                "b_count": len(b_values),
                "total_candidates": cross_total,
                "common_zero_padding_skipped": common_padding_skipped,
                "normalized_candidates": cross_total - common_padding_skipped,
                "shift_gate_pass": gate_count,
                "exact_kkt_certified": exact_count,
                "positive_bH": positive_bh_count,
            }

            diagonal_total = 0
            diagonal_padding_skipped = 0
            diagonal_exact = 0
            diagonal_positive = 0
            for pair in itertools.combinations_with_replacement(kernels, 2):
                for numerator in range(1, 8):
                    diagonal_total += 1
                    if not joint_support_is_minimal(pair):
                        diagonal_padding_skipped += 1
                        continue
                    mixing = Fraction(numerator, 8)
                    matrix = ((mixing, Fraction(0)), (Fraction(0), 1 - mixing))
                    gamma = (mixing, 1 - mixing)
                    problem = boundary_problem(pair, matrix, gamma, level)
                    certificate = solve_boundary_qp(problem)
                    diagonal_exact += 1
                    metrics = complete_metrics(problem, certificate)
                    if metrics["bH"] <= 0:
                        continue
                    diagonal_positive += 1
                    product = metrics["product"]
                    if best_diagonal is None or product < best_diagonal[0]:
                        best_diagonal = (product, pair, mixing, level, metrics)
            diagonal_counts[key] = {
                "kernel_count": len(kernels),
                "pair_with_replacement_count": len(
                    list(itertools.combinations_with_replacement(kernels, 2))
                ),
                "lambda_count": 7,
                "total_candidates": diagonal_total,
                "common_zero_padding_skipped": diagonal_padding_skipped,
                "normalized_candidates": diagonal_total - diagonal_padding_skipped,
                "exact_kkt_certified": diagonal_exact,
                "positive_bH": diagonal_positive,
            }

    if best_cross is None or best_diagonal is None or best_same_ratio is None:
        raise AssertionError("bounded exhaustive search produced no candidates")
    return {
        "scope": {
            "denominator": 8,
            "m_values": [3, 5],
            "L_values": [1, 2],
            "negative_b_values": [ftext(value) for value in b_values],
            "diagonal_lambdas": [f"{value}/8" for value in range(1, 8)],
        },
        "cross_counts": cross_counts,
        "diagonal_counts": diagonal_counts,
        "best_cross_product": ftext(best_cross[0]),
        "best_cross_location": {
            "m": len(best_cross[1][0]),
            "L": best_cross[3],
            "b": ftext(best_cross[2]),
            "kernels": [[ftext(value) for value in kernel] for kernel in best_cross[1]],
        },
        "best_same_kernel_product_ratio": ftext(best_same_ratio[0]),
        "best_diagonal_product": ftext(best_diagonal[0]),
        "best_diagonal_location": {
            "m": len(best_diagonal[1][0]),
            "L": best_diagonal[3],
            "lambda": ftext(best_diagonal[2]),
            "kernels": [[ftext(value) for value in kernel] for kernel in best_diagonal[1]],
        },
    }


def build_payload() -> dict[str, object]:
    gamma_half = (Fraction(1, 2), Fraction(1, 2))
    cross_kernels = (
        (Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)),
        (Fraction(3, 8), Fraction(1, 4), Fraction(3, 8)),
    )
    cross_record, cross_metrics, _ = candidate_record(
        cross_kernels, matrix_b(Fraction(-1, 5)), gamma_half, 2
    )
    baseline_record, baseline_metrics, _ = candidate_record(
        cross_kernels, matrix_b(Fraction(0)), gamma_half, 2
    )
    ratio = cross_metrics["product"] / baseline_metrics["product"]

    diagonal_kernels = (
        (Fraction(0), Fraction(1, 8), Fraction(3, 4), Fraction(1, 8), Fraction(0)),
        (
            Fraction(1, 8),
            Fraction(1, 4),
            Fraction(1, 4),
            Fraction(1, 4),
            Fraction(1, 8),
        ),
    )
    mixing = Fraction(1, 8)
    diagonal_matrix = ((mixing, Fraction(0)), (Fraction(0), 1 - mixing))
    diagonal_record, diagonal_metrics, _ = candidate_record(
        diagonal_kernels, diagonal_matrix, (mixing, 1 - mixing), 2
    )

    expected = {
        "cross_phi": Fraction(629198090085, 175479603614),
        "cross_a": Fraction(57, 32),
        "cross_bh": Fraction(361764546455, 701918414456),
        "cross_product": Fraction(20620579147935, 22461389262592),
        "baseline_phi": Fraction(82462667, 28528330),
        "baseline_a": Fraction(69, 32),
        "baseline_bh": Fraction(36547849, 85584990),
        "baseline_product": Fraction(840600527, 912906560),
        "ratio": Fraction(1190831349642527325, 1194398763365825948),
        "diagonal_phi": Fraction(6624259711621393, 720717809725096),
        "diagonal_a": Fraction(85, 64),
        "diagonal_bh": Fraction(1218876138683173, 1801794524312740),
        "diagonal_product": Fraction(20720894357613941, 23062969911203072),
    }
    observed = {
        "cross_phi": cross_metrics["Phi"],
        "cross_a": cross_metrics["a"],
        "cross_bh": cross_metrics["bH"],
        "cross_product": cross_metrics["product"],
        "baseline_phi": baseline_metrics["Phi"],
        "baseline_a": baseline_metrics["a"],
        "baseline_bh": baseline_metrics["bH"],
        "baseline_product": baseline_metrics["product"],
        "ratio": ratio,
        "diagonal_phi": diagonal_metrics["Phi"],
        "diagonal_a": diagonal_metrics["a"],
        "diagonal_bh": diagonal_metrics["bH"],
        "diagonal_product": diagonal_metrics["product"],
    }
    if observed != expected:
        raise AssertionError(f"exact supplied witness drift: {observed}")

    payload: dict[str, object] = {
        "global_status": "UNRESOLVED_AT_HARD_LIMIT",
        "extension_status": "PROJECT_INTERNAL_PD_CROSS_EXTENSION",
        "claim_boundary": {
            "global_optimality_claimed": False,
            "current_best_claimed": False,
            "q1_resolved": False,
            "q2_resolved": False,
            "compatible_history_theorem": False,
        },
        "general_theorem": {
            "master_inequality": (
                "k^2 <= (beta*N+bH*T-beta)*(s+a*(k-1)/T), for N>=2*L*T and bH>0"
            ),
            "delta": "beta*s>=1",
            "equality": "gamma=H*1/s, only if coordinatewise nonnegative",
            "leading_term": "sqrt(delta)*N^(1/2)",
            "secondary_coefficient": "delta^(1/4)*sqrt(a*bH)",
            "equality_case_secondary": "sqrt(a*bH)",
            "qp_layout": "q variables are j-major; D=I_n tensor H^(-1)",
            "zero_gamma_rule": "q coordinates with gamma_r=0 are fixed to zero and deleted",
            "block_lift": "C(q*h+t)=((h-t)*C_discrete(q)+t*C_discrete(q+1))/h^2",
        },
        "same_kernel_cross_candidate": cross_record,
        "same_kernel_diagonal_baseline": baseline_record,
        "same_kernel_product_ratio": ftext(ratio),
        "same_kernel_coefficient_ratio_approx": math.sqrt(float(ratio)),
        "bounded_grid_diagonal_winner": diagonal_record,
        "cross_over_diagonal_winner_product_ratio": ftext(
            cross_metrics["product"] / diagonal_metrics["product"]
        ),
        "cross_over_diagonal_winner_coefficient_ratio_approx": math.sqrt(
            float(cross_metrics["product"] / diagonal_metrics["product"])
        ),
        "exhaustive_search": exhaustive_search(),
        "non_claims": [
            "The PD cross extension is project-internal, not a theorem attributed to Hou-Zhao.",
            "The same-kernel normalized hit is not a global improvement.",
            "The bounded grid does not establish current-best or global optimality.",
            "Compatible history, Question 1, and Question 2 remain open.",
        ],
    }
    validate_payload_semantics(payload)
    return payload


def validate_payload_semantics(payload: Mapping[str, object]) -> None:
    theorem = payload["general_theorem"]
    claims = payload["claim_boundary"]
    if not isinstance(theorem, Mapping) or not isinstance(claims, Mapping):
        raise CertificateError("semantic sections missing")
    if theorem.get("secondary_coefficient") != "delta^(1/4)*sqrt(a*bH)":
        raise CertificateError("wrong general asymptotic coefficient")
    forbidden = (
        "global_optimality_claimed",
        "current_best_claimed",
        "q1_resolved",
        "q2_resolved",
        "compatible_history_theorem",
    )
    if any(claims.get(key) is not False for key in forbidden):
        raise CertificateError("unsupported global/current-best/Q1/Q2/history claim")
    ratio = Fraction(payload["same_kernel_product_ratio"])
    if ratio >= 1:
        raise CertificateError("same-kernel strict improvement missing")


def canonical_payload_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode(
        "utf-8"
    )


def build_certificate() -> dict[str, object]:
    payload = build_payload()
    return {
        "canonical_payload_sha256": hashlib.sha256(canonical_payload_bytes(payload)).hexdigest(),
        "payload": payload,
    }


def render_certificate() -> str:
    return json.dumps(build_certificate(), indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def verify_certificate(path: Path) -> None:
    expected = render_certificate().encode("utf-8")
    observed = path.read_bytes()
    if observed != expected:
        raise CertificateError("byte-exact certificate replay mismatch")
    parsed = json.loads(observed)
    digest = hashlib.sha256(canonical_payload_bytes(parsed["payload"])).hexdigest()
    if digest != parsed["canonical_payload_sha256"]:
        raise CertificateError("canonical payload hash mismatch")
    validate_payload_semantics(parsed["payload"])


def mutation_checks() -> None:
    kernels = (
        (Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)),
        (Fraction(3, 8), Fraction(1, 4), Fraction(3, 8)),
    )
    try:
        candidate_record(kernels, matrix_b(Fraction(-9, 10)), (Fraction(1, 2), Fraction(1, 2)), 2)
    except CertificateError:
        pass
    else:
        raise AssertionError("sign-gate mutation accepted")
    try:
        boundary_problem(kernels, matrix_b(Fraction(-1)), (Fraction(1, 2), Fraction(1, 2)), 2)
    except CertificateError:
        pass
    else:
        raise AssertionError("non-PD mutation accepted")

    problem = boundary_problem(kernels, matrix_b(Fraction(-1, 5)), (Fraction(1, 2), Fraction(1, 2)), 2)
    certificate = solve_boundary_qp(problem)
    cover_mutation = copy.deepcopy(certificate)
    cover_mutation["slack"] = (Fraction(-1),) + cover_mutation["slack"][1:]
    try:
        validate_qp_certificate(problem, cover_mutation)
    except CertificateError:
        pass
    else:
        raise AssertionError("cover mutation accepted")
    stationarity_mutation = copy.deepcopy(certificate)
    stationarity_mutation["stationarity"] = (Fraction(1),) + stationarity_mutation[
        "stationarity"
    ][1:]
    try:
        validate_qp_certificate(problem, stationarity_mutation)
    except CertificateError:
        pass
    else:
        raise AssertionError("stationarity mutation accepted")
    complementarity_mutation = copy.deepcopy(certificate)
    complementarity_mutation["complementarity"] = (Fraction(1),) + complementarity_mutation[
        "complementarity"
    ][1:]
    try:
        validate_qp_certificate(problem, complementarity_mutation)
    except CertificateError:
        pass
    else:
        raise AssertionError("complementarity mutation accepted")

    zero_problem = boundary_problem(
        kernels, matrix_b(Fraction(0)), (Fraction(1), Fraction(0)), 1
    )
    if zero_problem["variable_count"] != zero_problem["n"]:
        raise AssertionError("zero-gamma coordinate was not deleted")
    zero_certificate = solve_boundary_qp(zero_problem)
    layout_mutation = copy.deepcopy(zero_certificate)
    layout_mutation["q"] = layout_mutation["q"] + (Fraction(0),)
    try:
        validate_qp_certificate(zero_problem, layout_mutation)
    except CertificateError:
        pass
    else:
        raise AssertionError("zero-gamma free-coordinate mutation accepted")

    payload = build_payload()
    coefficient_mutation = copy.deepcopy(payload)
    coefficient_mutation["general_theorem"]["secondary_coefficient"] = "sqrt(delta*a*bH)"
    try:
        validate_payload_semantics(coefficient_mutation)
    except CertificateError:
        pass
    else:
        raise AssertionError("wrong coefficient mutation accepted")
    claim_mutation = copy.deepcopy(payload)
    claim_mutation["claim_boundary"]["current_best_claimed"] = True
    try:
        validate_payload_semantics(claim_mutation)
    except CertificateError:
        pass
    else:
        raise AssertionError("unsupported claim mutation accepted")


def self_check() -> None:
    build_payload()
    mutation_checks()


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--emit", action="store_true")
    parser.add_argument("--verify", type=Path)
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--exhaustive", action="store_true")
    args = parser.parse_args(list(argv) if argv is not None else None)
    if args.self_check:
        self_check()
        print("self-check and adversarial mutations: PASS; Q1/Q2 remain unresolved")
    if args.exhaustive:
        print(json.dumps(exhaustive_search(), indent=2, sort_keys=True))
    if args.verify:
        verify_certificate(args.verify)
        print(f"byte-exact certificate replay: PASS ({args.verify})")
    if args.emit:
        print(render_certificate(), end="")
    if not (args.self_check or args.exhaustive or args.verify or args.emit):
        payload = build_payload()
        print(
            json.dumps(
                {
                    "payload_hash": build_certificate()["canonical_payload_sha256"],
                    "same_kernel_ratio": payload["same_kernel_product_ratio"],
                    "status": payload["global_status"],
                },
                sort_keys=True,
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
