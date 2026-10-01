#!/usr/bin/env python3
"""Exact certificate for the direct ordered-B interval/Haar bridge.

The certificate moves the indefinite Wave matrix B from full-gap dipole
coordinates to the n+1 physical point coordinates by M=D^T B D.  It checks
the exact interval-state theorem, the Gothic mixed-difference normalization,
the finite dyadic Abel endpoint signs, two signed Haar-band fixtures, one
actual zero-aggregate Haar cell, and the precise price/ownership gates that
remain before a common multiscale carrier is available.

All arithmetic used by the semantic payload is exact ``fractions.Fraction``.
The SHA-256 hash covers every top-level field except ``integrity``; source
hashes are deliberately excluded to avoid a source/hash self-reference.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys
from typing import Mapping, Sequence


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "direct_ordered_b_interval_haar_certificate.json"
SCHEMA = "erdos1191.direct_ordered_b_interval_haar.v1"
STATUS = "EXACT_DIRECT_B_INTERVAL_HAAR_BRIDGE_ONLY_COMMON_LEDGER_OPEN"

NEGATIVE_POINTS = (0, 1, 3, 7, 12, 20)
POSITIVE_POINTS = (0, 101, 204, 309, 416, 525, 636, 749)


class CertificateError(RuntimeError):
    """Raised when an exact identity, scope gate, or replay check fails."""


def ftext(value: F | int) -> str:
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def matrix_text(matrix: Sequence[Sequence[F | int]]) -> list[list[str]]:
    return [[ftext(value) for value in row] for row in matrix]


def transpose(matrix: Sequence[Sequence[F | int]]) -> list[list[F]]:
    if not matrix:
        return []
    return [[F(matrix[i][j]) for i in range(len(matrix))] for j in range(len(matrix[0]))]


def matmul(
    left: Sequence[Sequence[F | int]], right: Sequence[Sequence[F | int]]
) -> list[list[F]]:
    if not left or not right or len(left[0]) != len(right):
        raise ValueError("incompatible matrix dimensions")
    return [
        [
            sum((F(left[i][k]) * F(right[k][j]) for k in range(len(right))), F(0))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def quadratic(matrix: Sequence[Sequence[F | int]], vector: Sequence[F | int]) -> F:
    if len(matrix) != len(vector) or any(len(row) != len(vector) for row in matrix):
        raise ValueError("quadratic form dimensions do not match")
    return sum(
        (
            F(vector[i]) * F(matrix[i][j]) * F(vector[j])
            for i in range(len(vector))
            for j in range(len(vector))
        ),
        F(0),
    )


def frobenius(
    left: Sequence[Sequence[F | int]], right: Sequence[Sequence[F | int]]
) -> F:
    if len(left) != len(right) or any(len(left[i]) != len(right[i]) for i in range(len(left))):
        raise ValueError("Frobenius dimensions do not match")
    return sum(
        (F(left[i][j]) * F(right[i][j]) for i in range(len(left)) for j in range(len(left[i]))),
        F(0),
    )


def identity(size: int) -> list[list[F]]:
    return [[F(i == j) for j in range(size)] for i in range(size)]


def incidence_matrix(n: int) -> list[list[F]]:
    """D is n by n+1 and (D u)_i=u_i-u_{i+1}."""
    if n < 2:
        raise ValueError("the Wave block needs n>=2")
    return [[F((k == i) - (k == i + 1)) for k in range(n + 1)] for i in range(n)]


def wave_b_matrix(n: int) -> list[list[F]]:
    """Exact local Wave matrix, including the Frobenius factor 1/2."""
    if n < 2:
        raise ValueError("the Wave block needs n>=2")
    return [
        [
            F(0)
            if i == j or abs(i - j) == 1
            else -F((j - i) ** 2, 8 * n * n)
            for j in range(n)
        ]
        for i in range(n)
    ]


def point_m_matrix(n: int) -> list[list[F]]:
    d = incidence_matrix(n)
    return matmul(matmul(transpose(d), wave_b_matrix(n)), d)


def r_kernel(width: F | int, distance: F | int) -> F:
    width = F(width)
    distance = abs(F(distance))
    if width <= 0:
        raise ValueError("T must be positive")
    return max(F(0), width - distance) / (width * width)


def point_gram(block_points: Sequence[int], width: F | int) -> list[list[F]]:
    return [[r_kernel(width, left - right) for right in block_points] for left in block_points]


def wave_gram(block_points: Sequence[int], width: F | int) -> list[list[F]]:
    n = len(block_points) - 1
    d = incidence_matrix(n)
    return matmul(matmul(d, point_gram(block_points, width)), transpose(d))


def q_density(block_points: Sequence[int], width: F | int) -> F:
    n = len(block_points) - 1
    return frobenius(wave_b_matrix(n), wave_gram(block_points, width))


def alpha_global(n: int, left_gap: int, right_gap: int) -> F:
    if n <= left_gap <= right_gap - 2 and n + 2 <= right_gap <= 2 * n - 1:
        return F((right_gap - left_gap) ** 2, 4 * n * n)
    return F(0)


def gothic_lambda(n: int, point_left: int, point_right: int) -> F:
    """Mixed difference for D_(p,q)=a_q-a_(p-1)."""
    return (
        alpha_global(n, point_left, point_right)
        + alpha_global(n, point_left - 1, point_right + 1)
        - alpha_global(n, point_left, point_right + 1)
        - alpha_global(n, point_left - 1, point_right)
    )


def interval_vector(n: int, left: int, right: int) -> tuple[int, ...]:
    if not (0 <= left <= right <= n):
        raise ValueError("invalid local inclusive interval")
    return tuple(int(left <= k <= right) for k in range(n + 1))


def positive_differences(points: Sequence[int]) -> tuple[int, ...]:
    if any(points[i] >= points[i + 1] for i in range(len(points) - 1)):
        raise CertificateError("points are not strictly increasing")
    differences = tuple(
        points[right] - points[left]
        for left in range(len(points))
        for right in range(left + 1, len(points))
    )
    if len(differences) != len(set(differences)):
        raise CertificateError("fixture is not a Golomb ruler")
    return tuple(sorted(differences))


def interval_and_lambda_audit() -> dict[str, object]:
    interval_rows = 0
    lambda_rows = 0
    for n in range(2, 10):
        m_matrix = point_m_matrix(n)
        if any(m_matrix[i][i] for i in range(n + 1)):
            raise CertificateError("diag(M) is not zero")
        if any(sum(row, F(0)) for row in m_matrix):
            raise CertificateError("M*1 is not zero")
        for left in range(n + 1):
            for right in range(left, n + 1):
                vector = interval_vector(n, left, right)
                membership = right - left + 1
                expected = (
                    F(membership * membership, 4 * n * n)
                    if 0 < left <= right < n and membership >= 2
                    else F(0)
                )
                value = quadratic(m_matrix, vector)
                if value != expected:
                    raise CertificateError("interval-state formula failed")
                if value < 0 or value > F(sum(vector) ** 2, 4 * n * n):
                    raise CertificateError("membership-count domination failed")
                interval_rows += 1
        for p in range(n, 2 * n):
            for q in range(p, 2 * n):
                local_left = p - n
                local_right = q - n + 1
                if 2 * m_matrix[local_left][local_right] != gothic_lambda(n, p, q):
                    raise CertificateError("2M=lambda normalization failed")
                lambda_rows += 1

    n = 4
    m4 = point_m_matrix(n)
    expected_m4 = (
        (F(0), F(0), F(-1, 32), F(-5, 128), F(9, 128)),
        (F(0), F(0), F(1, 32), F(1, 128), F(-5, 128)),
        (F(-1, 32), F(1, 32), F(0), F(1, 32), F(-1, 32)),
        (F(-5, 128), F(1, 128), F(1, 32), F(0), F(0)),
        (F(9, 128), F(-5, 128), F(-1, 32), F(0), F(0)),
    )
    if tuple(map(tuple, m4)) != expected_m4:
        raise CertificateError("n=4 point matrix changed")
    witness = interval_vector(3, 1, 2)
    witness_value = quadratic(point_m_matrix(3), witness)
    if witness_value != F(1, 9):
        raise CertificateError("sharp interval witness changed")

    lambda_table = []
    for p in range(n, 2 * n):
        for q in range(p, 2 * n):
            k, ell = p - n, q - n + 1
            lambda_table.append(
                {
                    "global_interval": [p, q],
                    "local_physical_pair": [k, ell],
                    "M_entry": ftext(m4[k][ell]),
                    "lambda": ftext(2 * m4[k][ell]),
                }
            )
    return {
        "n_range_exhausted": [2, 9],
        "interval_states_checked": interval_rows,
        "mixed_difference_rows_checked": lambda_rows,
        "M_has_zero_diagonal": True,
        "M_times_one_is_zero": True,
        "interval_formula": "u_[p,q]^T M u_[p,q]=m^2/(4*n^2) iff 0<p<=q<n and m=q-p+1>=2; otherwise 0",
        "membership_count_domination": "0<=u^T M u<=(1^T u)^2/(4*n^2) on every binary interval state",
        "sharp_for_n_at_least_3": True,
        "sharp_witness": {"n": 3, "local_interval": [1, 2], "value": ftext(witness_value)},
        "n4_M": matrix_text(m4),
        "n4_global_lambda_rows": lambda_table,
        "global_local_rule": "for n<=p<=q<=2n-1, k=p-n and l=q-n+1, 2*M[k,l]=lambda[p,q]",
    }


def synthetic_abel_audit() -> dict[str, object]:
    widths = (5, 10, 20, 40)
    values = (F(2, 3), F(3, 5), F(5, 7), F(7, 11))
    lhs = sum((F(widths[i]) * values[i] for i in range(3)), F(0))
    band_sum = sum(
        (F(2 * widths[i]) * (values[i] - values[i + 1]) for i in range(3)), F(0)
    )
    lower_endpoint = -F(widths[0]) * values[0]
    upper_endpoint = F(widths[3]) * values[3]
    if (lhs, band_sum, lower_endpoint, upper_endpoint) != (
        F(496, 21),
        F(346, 231),
        F(-10, 3),
        F(280, 11),
    ):
        raise CertificateError("general Abel endpoint audit changed")
    if lhs != band_sum + lower_endpoint + upper_endpoint:
        raise CertificateError("general Abel identity failed")
    return {
        "widths": list(widths),
        "Q_rows": [ftext(value) for value in values],
        "left_sum": ftext(lhs),
        "twice_width_band_sum": ftext(band_sum),
        "lower_endpoint_row": ftext(lower_endpoint),
        "upper_endpoint_row": ftext(upper_endpoint),
        "right_sum": ftext(band_sum + lower_endpoint + upper_endpoint),
        "endpoint_signs": {"lower": "negative", "upper": "positive"},
    }


def active_abel_audit() -> dict[str, object]:
    n = 3
    block = NEGATIVE_POINTS[n - 1 :]
    widths = (4, 8, 16, 32)
    values = tuple(q_density(block, width) for width in widths)
    expected = (F(0), F(1, 192), F(1, 2304), F(0))
    if values != expected:
        raise CertificateError("active Abel Q rows changed")
    left_sum = sum((F(widths[i]) * values[i] for i in range(3)), F(0))
    band_rows = tuple(F(2 * widths[i]) * (values[i] - values[i + 1]) for i in range(3))
    if left_sum != F(7, 144) or sum(band_rows, F(0)) != left_sum:
        raise CertificateError("terminal-free active Abel replay failed")
    gaps = tuple(NEGATIVE_POINTS[i] - NEGATIVE_POINTS[i - 1] for i in range(n, 2 * n))
    minimum_middle_gap = min(gaps[1:-1])
    horizon = NEGATIVE_POINTS[2 * n - 1] - NEGATIVE_POINTS[n - 1]
    if (gaps, minimum_middle_gap, horizon) != ((4, 5, 8), 5, 17):
        raise CertificateError("active endpoint gate changed")
    return {
        "points": list(NEGATIVE_POINTS),
        "local_block_points": list(block),
        "current_gaps": list(gaps),
        "m_star": minimum_middle_gap,
        "horizon_H": horizon,
        "chosen_widths": list(widths),
        "Q_rows": [ftext(value) for value in values],
        "lower_boundary_TQ": ftext(F(widths[0]) * values[0]),
        "upper_boundary_TQ": ftext(F(widths[-1]) * values[-1]),
        "twice_width_band_rows": [ftext(value) for value in band_rows],
        "terminal_free_sum": ftext(left_sum),
        "both_endpoint_rows_vanish": True,
    }


def signed_band_fixtures() -> dict[str, object]:
    negative_n = 3
    negative_block = NEGATIVE_POINTS[negative_n - 1 :]
    b3 = wave_b_matrix(negative_n)
    g3 = wave_gram(negative_block, 3)
    g6 = wave_gram(negative_block, 6)
    delta_negative = [
        [g3[i][j] - g6[i][j] for j in range(negative_n)] for i in range(negative_n)
    ]
    q3 = frobenius(b3, g3)
    q6 = frobenius(b3, g6)
    if q3 != 0 or q6 != F(1, 324) or frobenius(b3, delta_negative) != F(-1, 324):
        raise CertificateError("negative signed-band fixture changed")

    positive_n = 4
    positive_block = POSITIVE_POINTS[positive_n - 1 :]
    b4 = wave_b_matrix(positive_n)
    g200 = wave_gram(positive_block, 200)
    g400 = wave_gram(positive_block, 400)
    q200 = frobenius(b4, g200)
    q400 = frobenius(b4, g400)
    delta_positive = [
        [g200[i][j] - g400[i][j] for j in range(positive_n)] for i in range(positive_n)
    ]
    if q200 != F(9, 32000) or q400 != F(9, 256000):
        raise CertificateError("positive signed-band Q rows changed")
    if frobenius(b4, delta_positive) != F(63, 256000):
        raise CertificateError("positive signed-band difference changed")
    return {
        "negative": {
            "points": list(NEGATIVE_POINTS),
            "difference_count": len(positive_differences(NEGATIVE_POINTS)),
            "n": negative_n,
            "T": 3,
            "B": matrix_text(b3),
            "G_T": matrix_text(g3),
            "G_2T": matrix_text(g6),
            "G_T_minus_G_2T": matrix_text(delta_negative),
            "Q_T": ftext(q3),
            "Q_2T": ftext(q6),
            "signed_band_contraction": ftext(q3 - q6),
            "twice_T_weighted_Abel_row": ftext(F(6) * (q3 - q6)),
        },
        "positive": {
            "points": list(POSITIVE_POINTS),
            "difference_count": len(positive_differences(POSITIVE_POINTS)),
            "n": positive_n,
            "T": 200,
            "B": matrix_text(b4),
            "M": matrix_text(point_m_matrix(positive_n)),
            "G_T": matrix_text(g200),
            "G_2T": matrix_text(g400),
            "G_T_minus_G_2T": matrix_text(delta_positive),
            "Q_T": ftext(q200),
            "Q_2T": ftext(q400),
            "signed_band_contraction": ftext(q200 - q400),
            "twice_T_weighted_Abel_row": ftext(F(400) * (q200 - q400)),
        },
    }


def scaled_haar_value(x: int, point: int, width: int) -> int:
    """Return 2T*(K_T-K_(2T))(x-point), with half-open boxes."""
    displacement = x - point
    return 2 * int(0 <= displacement < width) - int(0 <= displacement < 2 * width)


def haar_cell_fixture() -> dict[str, object]:
    points = POSITIVE_POINTS
    n = 4
    width = 200
    block = points[n - 1 :]
    all_events = sorted({point + shift for point in points for shift in (0, width, 2 * width)})
    cell_left = 636
    cell_right = min(event for event in all_events if event > cell_left)
    state_all = tuple(scaled_haar_value(cell_left, point, width) for point in points)
    state_local = state_all[n - 1 :]
    d_state = tuple(state_local[i] - state_local[i + 1] for i in range(n))
    m_value = quadratic(point_m_matrix(n), state_local)
    density = m_value / F((2 * width) ** 2)
    if (
        cell_right != 709
        or state_all != (0, 0, 0, -1, -1, 1, 1, 0)
        or state_local != (-1, -1, 1, 1, 0)
        or d_state != (0, -2, 0, 1)
        or sum(state_local) != 0
        or m_value != F(1, 8)
        or density != F(1, 1280000)
    ):
        raise CertificateError("actual Haar cell fixture changed")
    # Verify constancy on every integer point in the half-open cell and the
    # state change at its excluded right endpoint.
    if any(tuple(scaled_haar_value(x, point, width) for point in points) != state_all for x in range(cell_left, cell_right)):
        raise CertificateError("Haar state is not constant on its certified cell")
    if tuple(scaled_haar_value(cell_right, point, width) for point in points) == state_all:
        raise CertificateError("right half-open cell endpoint did not change state")
    return {
        "points": list(points),
        "T": width,
        "box_convention": "K_T=T^-1*1_[0,T); Haar h_T=K_T-K_(2T)",
        "scaled_state_convention": "v=2T*(h_T(x-a_p))",
        "maximal_atomic_cell": [cell_left, cell_right],
        "cell_is_left_closed_right_open": True,
        "cell_length": cell_right - cell_left,
        "scaled_state_all_eight_marks": list(state_all),
        "local_block_points": list(block),
        "scaled_local_state_v": list(state_local),
        "D_v": list(d_state),
        "one_transpose_v": sum(state_local),
        "v_transpose_M_v": ftext(m_value),
        "pointwise_h_transpose_M_h": ftext(density),
        "cell_contribution_to_M_Haar_Gram": ftext(F(cell_right - cell_left) * density),
        "v_transpose_J_v": ftext(F(sum(state_local) ** 2)),
        "kappa_J_minus_mu_M_on_v": "-mu/8 for every kappa and every mu>0",
        "C_equal_zero_cellwise_repair_feasible_for_positive_mu": False,
    }


def cover_and_schur_obstructions() -> dict[str, object]:
    n = 4
    m_matrix = point_m_matrix(n)
    singleton_values = [quadratic(m_matrix, tuple(int(k == i) for k in range(n + 1))) for i in range(n + 1)]
    if singleton_values != [F(0)] * (n + 1):
        raise CertificateError("singleton interval slack changed")
    b = wave_b_matrix(n)
    x_column = (F(1), F(0), F(0), F(0))
    extended = [row[:] + [x_column[i]] for i, row in enumerate(b)]
    extended.append(list(x_column) + [F(1)])
    witness = (F(1), F(0), F(0), F(0), F(-1))
    witness_value = quadratic(extended, witness)
    if witness_value != F(-1):
        raise CertificateError("Schur zero-slack witness changed")
    return {
        "singleton_M_values": [ftext(value) for value in singleton_values],
        "rank_one_cover_hypothesis": "(c^T u)^2<=C*u^T M u on every binary interval state",
        "singleton_consequence": "testing u=e_k forces c_k=0 for every k, hence c=0",
        "nonzero_scalar_interval_cover_exists": False,
        "Schur_root_restricted_block": "evaluate [[B,X],[X^T,D_ext]], D_ext positive definite, only on (t*e_i,y) for every t,y and each singleton root e_i",
        "Schur_root_residual": "e_i^T(B-X*D_ext^-1*X^T)e_i=-e_i^T X D_ext^-1 X^T e_i",
        "zero_slack_consequence": "nonnegativity on every root-restricted pair (t*e_i,y), not whole coefficient-block PSD, forces X^T e_i=0 for every i, hence X=0",
        "nonzero_zero_price_Schur_cross_coupling_exists": False,
        "exact_Schur_counterfixture": {
            "D_ext": "1/1",
            "X_column": [ftext(value) for value in x_column],
            "witness": [ftext(value) for value in witness],
            "quadratic_value": ftext(witness_value),
        },
    }


def affine_golomb_audit() -> dict[str, object]:
    symbolic_points = ((0, 0), (0, 2), (0, 5), (0, 16), (1, 16), (1, 17), (1, 25), (3, 25))
    differences: list[tuple[int, int, int, int]] = []
    for left in range(len(symbolic_points)):
        for right in range(left + 1, len(symbolic_points)):
            differences.append(
                (
                    symbolic_points[right][0] - symbolic_points[left][0],
                    symbolic_points[right][1] - symbolic_points[left][1],
                    left,
                    right,
                )
            )
    for i, first in enumerate(differences):
        for second in differences[i + 1 :]:
            if first[:2] == second[:2]:
                raise CertificateError("affine difference forms coincide identically")
    positive_integral_collisions: set[int] = set()
    for i, first in enumerate(differences):
        for second in differences[i + 1 :]:
            slope_delta = first[0] - second[0]
            constant_delta = second[1] - first[1]
            if slope_delta:
                candidate = F(constant_delta, slope_delta)
                if candidate > 0 and candidate.denominator == 1:
                    positive_integral_collisions.add(candidate.numerator)
    if max(positive_integral_collisions) != 25:
        raise CertificateError("affine Golomb collision threshold changed")
    constants_by_slope: dict[str, list[int]] = {}
    for slope in sorted({row[0] for row in differences}):
        constants = sorted(row[1] for row in differences if row[0] == slope)
        if len(constants) != len(set(constants)):
            raise CertificateError("same-slope affine differences collide")
        constants_by_slope[str(slope)] = constants
    return {
        "family": "A_L=(0,2,5,16,L+16,L+17,L+25,3L+25)",
        "integer_parameter_domain": "L>=26",
        "difference_count": len(differences),
        "difference_constants_by_slope": constants_by_slope,
        "maximum_positive_integral_collision_parameter": max(positive_integral_collisions),
        "Golomb_for_every_integer_L_at_least_26": True,
    }


def count_baseline_family() -> dict[str, object]:
    affine = affine_golomb_audit()
    n = 4
    sample_checks = 0
    for length in (26, 31, 64, 101):
        points = (0, 2, 5, 16, length + 16, length + 17, length + 25, 3 * length + 25)
        positive_differences(points)
        block = points[n - 1 :]
        for twice_width in range(19, 2 * length, 7):
            width = F(twice_width, 2)
            if not F(9) < width < F(length):
                continue
            point_sum_energy = sum((value for row in point_gram(block, width) for value in row), F(0))
            expected_point_sum = F(11, 1) / width - F(36, 1) / (width * width)
            q_value = q_density(block, width)
            expected_q = F(9, 64) / width - F(45, 64) / (width * width)
            if point_sum_energy != expected_point_sum or q_value != expected_q:
                raise CertificateError("A_L count-baseline density formula failed")
            sample_checks += 1
    if sample_checks < 20:
        raise CertificateError("too few A_L exact sample checks")
    baseline_log = F(11, 64)
    gothic_log = F(9, 64)
    if baseline_log - gothic_log != F(1, 32):
        raise CertificateError("A_L logarithmic price gap changed")
    finite_length = 2**24
    finite_horizon = 3 * finite_length + 9
    # Exact elementary finite witness.  The exact difference is
    #
    # 64(B-G)=11 log L-9 log H-10 log 9+4 log 8+5+36/L-45/H.
    #
    # Since H<=4L, log L=24 log 2, log 4=2 log 2 and
    # log 8=3 log 2, its logarithmic part is bounded below by
    # 42 log 2-10 log 9.  The atanh series gives log 2>2/3 from
    # its first positive term.  For z=4/5 the first term plus the
    # geometric tail is 344/135<3, hence log 9<3.  Dropping 36/L
    # and using 45/H<1 gives the strict lower bound 64(B-G)>2.
    log2_lower = F(2, 3)
    z9 = F(4, 5)
    log9_upper = 2 * z9 + 2 * z9**3 / (F(3) * (1 - z9**2))
    coarse_64_gap_lower = 42 * log2_lower - 10 * F(3) + 5 - 1
    if (
        finite_horizon > 4 * finite_length
        or log9_upper != F(344, 135)
        or not log9_upper < 3
        or coarse_64_gap_lower != 2
        or not F(45, finite_horizon) < 1
    ):
        raise CertificateError("finite A_L count/Gothic witness changed")
    return {
        **affine,
        "current_block_points": ["16", "L+16", "L+17", "L+25", "3L+25"],
        "scale_interval": "9<T<L",
        "exact_Fraction_sample_rows_checked": sample_checks,
        "point_sum_energy": "||sum_(k=0)^4 delta_(b_k)*K_T||_2^2=11/T-36/T^2",
        "sharp_count_baseline_density": "(1/64)||sum q_k||_2^2=11/(64*T)-9/(16*T^2)",
        "wave_density_Q": "9/(64*T)-45/(64*T^2)",
        "baseline_minus_Q": "1/(32*T)+9/(64*T^2)",
        "integrated_count_baseline_9_to_L": "(11/64)log(L/9)-1/16+9/(16L)",
        "positive_same_epoch_Gothic_capacity": "(9*log(H)-log(9)-4*log(8)-9+45/H)/64, H=3L+9",
        "exact_64_times_baseline_minus_Gothic": "11*log(L)-9*log(H)-10*log(9)+4*log(8)+5+36/L-45/H",
        "count_baseline_log_L_coefficient": ftext(baseline_log),
        "positive_same_epoch_Gothic_log_L_coefficient": ftext(gothic_log),
        "baseline_minus_positive_Gothic_log_L_coefficient": ftext(baseline_log - gothic_log),
        "positive_Gothic_alone_uniformly_pays_count_baseline": False,
        "finite_separation_witness": {
            "L": finite_length,
            "H": finite_horizon,
            "log_2_strict_lower": ftext(log2_lower),
            "log_9_strict_upper": ftext(log9_upper),
            "coarse_strict_lower_for_64_times_gap": ftext(coarse_64_gap_lower),
            "count_baseline_minus_positive_Gothic_strictly_greater_than": ftext(F(1, 32)),
        },
    }


def epoch_pair_ownership_audit() -> dict[str, object]:
    checked = 0
    for n in range(2, 13):
        current_points = tuple(range(n - 1, 2 * n))
        next_points = tuple(range(2 * n - 1, 4 * n))
        if set(current_points) & set(next_points) != {2 * n - 1}:
            raise CertificateError("consecutive epoch blocks do not share exactly one point")
        current_m = point_m_matrix(n)
        next_m = point_m_matrix(2 * n)
        current_pairs = {
            frozenset((current_points[i], current_points[j]))
            for i in range(n + 1)
            for j in range(i + 1, n + 1)
            if current_m[i][j]
        }
        next_pairs = {
            frozenset((next_points[i], next_points[j]))
            for i in range(2 * n + 1)
            for j in range(i + 1, 2 * n + 1)
            if next_m[i][j]
        }
        if current_pairs & next_pairs:
            raise CertificateError("direct physical M-pair ownership overlaps")
        checked += len(current_pairs) + len(next_pairs)
    return {
        "epoch_sizes_exhausted": [2, 12],
        "nonzero_physical_pair_rows_checked": checked,
        "current_point_block": "{a_(n-1),...,a_(2n-1)}",
        "next_point_block": "{a_(2n-1),...,a_(4n-1)}",
        "shared_physical_points": 1,
        "direct_M_pair_supports_disjoint": True,
        "reason": "diag(M)=0, and two consecutive point blocks share only a_(2n-1)",
        "positive_J_baseline_shared_endpoint_diagonal_multiplicity": 2,
        "positive_block_count_baseline_requires_explicit_endpoint_owner": True,
    }


def sdp_schema() -> dict[str, object]:
    return {
        "single_epoch_fixed_scale": {
            "atomic_endpoints": "sort the distinct a_p, a_p+T, a_p+2T; use every half-open cell between consecutive endpoints",
            "state": "v_c=(2T*(K_T-K_(2T))(x_c-a_p))_p for any x_c in cell c",
            "variables": [
                "C=C^T positive semidefinite on the n+1 physical point coordinates",
                "C*1=0",
                "kappa>=0",
                "mu>0",
            ],
            "cell_constraints": "v_c^T(kappa*J+C-mu*M)v_c>=0 for every atomic Haar cell c",
            "stronger_ordinary_Cauchy_constraint": "kappa*J+C-mu*M is positive semidefinite",
            "diagonal_energy_objective": "minimize trace(C)/(2T)",
        },
        "finite_multi_epoch_extension": {
            "physical_coordinates": "deduplicate the union of all epoch point blocks before embedding each M_s and J_s",
            "fixed_common_T_constraint": "v_c^T(C+sum_s kappa_s*J_s-sum_s mu_s*M_s)v_c>=0 on every union endpoint cell",
            "multiwidth_constraint": "concatenate the states indexed by (epoch,scale), use one block PSD C, and partition by every a_p, a_p+T_r, a_p+2T_r endpoint",
            "objective": "minimize sum_r trace(C_rr)/(2T_r)",
            "falsifiable_output": "exact rational primal matrix, exact rational dual cell weights, and zero duality gap",
        },
        "positive_fixture_gate": {
            "C_equal_zero_constraint_value": "-mu/8 on the certified [636,709) state for every kappa",
            "C_equal_zero_feasible_for_mu_positive": False,
            "PSD_C_and_zero_diagonal_force_C_equal_zero": True,
            "nontrivial_repair_has_positive_diagonal_price": True,
        },
    }


def payload_hash(certificate: Mapping[str, object]) -> str:
    payload = {key: value for key, value in certificate.items() if key != "integrity"}
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def rendered_bytes(certificate: Mapping[str, object]) -> bytes:
    return (json.dumps(certificate, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def build_certificate() -> dict[str, object]:
    certificate: dict[str, object] = {
        "schema": SCHEMA,
        "status": STATUS,
        "purpose": "Certify the exact direct indefinite-B point-coordinate interval/Haar bridge, its signed dyadic rows, and the remaining common-carrier price gates.",
        "theorem_contract": {
            "coordinates": "b_k=a_(n-1+k), 0<=k<=n; q_k=delta_(b_k)*K_T; (D u)_i=u_i-u_(i+1)",
            "Wave_matrix": "B_ii=0; B_ij=0 for |i-j|=1; B_ij=-(j-i)^2/(8*n^2) for |i-j|>=2",
            "point_matrix": "M=D^T*B*D; G_T=D*P_T*D^T; Q_n(T)=<B,G_T>_F=<M,P_T>_F",
            "interval_theorem": "for binary consecutive membership u_[p,q], u^T M u=m^2/(4*n^2) exactly for an internal interval of length m>=2, and is zero otherwise",
            "sharp_domination": "q(x)^T M q(x)<=(sum_k q_k(x))^2/(4*n^2) pointwise; integration gives Q_n(T)<=||sum_k q_k||_2^2/(4*n^2)",
            "Gothic_identity": "2*M[p-n,q-n+1]=lambda_(p,q) for n<=p<=q<=2n-1; the 2 is the symmetric Frobenius pair",
            "Abel_identity": "sum_(r=L)^U T_r Q_r=sum 2*T_r*(Q_r-Q_(r+1))-T_L*Q_L+T_(U+1)*Q_(U+1)",
            "Haar_identity": "G_T-G_(2T)=Gram((delta_(b_i)-delta_(b_(i+1)))*(K_T-K_(2T)))",
            "active_support": "for n>=3 (canonical use n>=4), Q_n(T)=0 for T<=m_*=min(h_(n+1),...,h_(2n-2)) and for T>=H=a_(2n-1)-a_(n-1); a Haar band can be active only inside (m_*/2,H)",
        },
        "interval_and_lambda_audit": interval_and_lambda_audit(),
        "general_Abel_endpoint_audit": synthetic_abel_audit(),
        "terminal_free_active_Abel_audit": active_abel_audit(),
        "signed_band_fixtures": signed_band_fixtures(),
        "actual_Haar_cell_fixture": haar_cell_fixture(),
        "cover_and_Schur_obstructions": cover_and_schur_obstructions(),
        "A_L_count_baseline_family": count_baseline_family(),
        "epoch_pair_ownership_audit": epoch_pair_ownership_audit(),
        "falsifiable_SDP_schema": sdp_schema(),
        "scope": {
            "direct_B_interval_state_theorem_exact": True,
            "direct_B_Gothic_physical_pair_map_exact": True,
            "dyadic_Abel_with_both_endpoint_signs_exact": True,
            "terminal_free_active_scale_choice_exists": True,
            "signed_Haar_band_contraction_has_fixed_sign": False,
            "scalar_interval_cover_nontrivial": False,
            "zero_price_PSD_Schur_cross_coupling_nontrivial": False,
            "positive_same_epoch_Gothic_alone_pays_sharp_count_baseline": False,
            "multi_epoch_endpoint_diagonal_owner_supplied": False,
            "finite_multi_epoch_SDP_solved": False,
            "direct_pair_disjointness_creates_new_capacity_beyond_the_same_epoch_Gothic_rewrite": False,
            "common_opposite_sign_capacity_ledger_closed": False,
            "C058_closed": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "publication_novelty_claimed": False,
            "prize_claim_ready": False,
        },
    }
    certificate["integrity"] = {
        "payload_sha256": payload_hash(certificate),
        "hash_domain": "all top-level fields except integrity",
        "source_hash_embedded": False,
        "canonical_json": True,
    }
    return certificate


def validate_certificate(certificate: Mapping[str, object]) -> None:
    if certificate.get("schema") != SCHEMA or certificate.get("status") != STATUS:
        raise CertificateError("schema or status mismatch")
    integrity = certificate.get("integrity")
    if not isinstance(integrity, Mapping) or integrity.get("payload_sha256") != payload_hash(certificate):
        raise CertificateError("payload hash mismatch")
    if integrity.get("source_hash_embedded") is not False:
        raise CertificateError("source/hash self-reference gate changed")
    if certificate != build_certificate():
        raise CertificateError("semantic replay mismatch")


def rehash(certificate: dict[str, object]) -> None:
    certificate.setdefault("integrity", {})["payload_sha256"] = payload_hash(certificate)


def self_check(certificate: Mapping[str, object]) -> int:
    validate_certificate(certificate)
    mutations: list[dict[str, object]] = []

    changed = copy.deepcopy(certificate)
    changed["integrity"]["payload_sha256"] = "0" * 64
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["theorem_contract"]["Wave_matrix"] = "B_ij=-(j-i)^2/(4*n^2)"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["interval_and_lambda_audit"]["n4_M"][0][2] = "-1/16"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["interval_and_lambda_audit"]["sharp_witness"]["value"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["general_Abel_endpoint_audit"]["endpoint_signs"]["lower"] = "positive"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["terminal_free_active_Abel_audit"]["both_endpoint_rows_vanish"] = False
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["signed_band_fixtures"]["negative"]["signed_band_contraction"] = "1/324"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["signed_band_fixtures"]["positive"]["signed_band_contraction"] = "-63/256000"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["actual_Haar_cell_fixture"]["maximal_atomic_cell"] = [636, 708]
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["actual_Haar_cell_fixture"]["one_transpose_v"] = 1
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["cover_and_Schur_obstructions"]["nonzero_scalar_interval_cover_exists"] = True
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["cover_and_Schur_obstructions"]["nonzero_zero_price_Schur_cross_coupling_exists"] = True
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["A_L_count_baseline_family"]["baseline_minus_positive_Gothic_log_L_coefficient"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["epoch_pair_ownership_audit"]["positive_J_baseline_shared_endpoint_diagonal_multiplicity"] = 1
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["scope"]["C058_closed"] = True
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["scope"]["prize_claim_ready"] = True
    rehash(changed)
    mutations.append(changed)

    rejected = 0
    for mutation in mutations:
        try:
            validate_certificate(mutation)
        except CertificateError:
            rejected += 1
    if rejected != len(mutations):
        raise CertificateError("a semantic or hash mutation was accepted")
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit", action="store_true", help="emit canonical JSON")
    parser.add_argument("--verify", type=Path, help="verify a committed certificate")
    parser.add_argument("--self-check", action="store_true", help="run mutation rejection checks")
    args = parser.parse_args()

    built = build_certificate()
    if args.verify:
        raw = args.verify.read_bytes()
        loaded = json.loads(raw.decode("utf-8"))
        validate_certificate(loaded)
        if raw != rendered_bytes(loaded) or raw != rendered_bytes(built):
            raise CertificateError("byte replay mismatch")
    if args.self_check:
        self_check(built)
    if args.emit:
        sys.stdout.buffer.write(rendered_bytes(built))
    elif not args.verify and not args.self_check:
        print(built["integrity"]["payload_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
