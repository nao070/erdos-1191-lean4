#!/usr/bin/env python3
"""Exact finite certificate for the ordered-Gram ramp master.

The companion memo proves the general fixed-scale root-cone decomposition.
This replay locks its signs and factors on exact Golomb fixtures, checks the
rank-one ramp surplus and optimal-shift Schur complement, and records the
scope gates that prevent the fixed-scale statement from being mistaken for a
closed signed/cross-epoch proof of Erdős Problem #1191.

The JSON integrity hash covers the semantic payload only (all top-level
fields except ``integrity``).  It deliberately contains no source-file hash,
so there is no source/hash self-reference.
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
DEFAULT_CERTIFICATE = HERE / "ordered_gram_ramp_master_certificate.json"
SCHEMA = "erdos1191.ordered_gram_ramp_master.v1"
STATUS = "EXACT_FIXED_SCALE_ORDERED_GRAM_RAMP_ONLY_COMMON_PAYMENT_OPEN"

N4_POINTS = (0, 101, 204, 309, 416, 525, 636, 749)
N5_TRIANGLE_POINTS = (0, 6, 14, 29, 53, 153, 154, 257, 259, 366)
SIGNED_BAND_POINTS = (0, 1, 3, 7, 12, 20)


class CertificateError(RuntimeError):
    """Raised when an exact replay or a scope gate fails."""


def ftext(value: F | int) -> str:
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def interval_length(left: tuple[int, int], right: tuple[int, int]) -> int:
    return max(0, min(left[1], right[1]) - max(left[0], right[0]))


def positive_differences(points: Sequence[int]) -> tuple[int, ...]:
    if any(points[i] >= points[i + 1] for i in range(len(points) - 1)):
        raise CertificateError("points are not strictly increasing")
    values = tuple(
        points[right] - points[left]
        for left in range(len(points))
        for right in range(left + 1, len(points))
    )
    if len(values) != len(set(values)):
        raise CertificateError("fixture is not a Golomb ruler")
    return tuple(sorted(values))


def tent_numerator(middle: int, left_gap: int, right_gap: int, width: int) -> int:
    positive = lambda value: max(value, 0)
    return (
        positive(width - middle)
        + positive(width - middle - left_gap - right_gap)
        - positive(width - middle - left_gap)
        - positive(width - middle - right_gap)
    )


def local_root_cone_audit() -> dict[str, object]:
    """Exhaust the local full-gap/shifted-gap overlap identity in a box."""
    checked = 0
    positive_rows = 0
    for middle in range(1, 7):
        for left_gap in range(1, 7):
            for right_gap in range(1, 7):
                left_v = (0, left_gap)
                right_v = (left_gap + middle, left_gap + middle + right_gap)
                for width in range(1, middle + left_gap + right_gap + 3):
                    left_u = (width, left_gap + width)
                    right_u = (
                        left_gap + middle + width,
                        left_gap + middle + right_gap + width,
                    )
                    if interval_length(left_v, right_v) or interval_length(left_u, right_u):
                        raise CertificateError("a same-sign interval family overlaps")
                    if interval_length(right_u, left_v):
                        raise CertificateError("a reverse ordered cross overlap is nonzero")
                    overlap = interval_length(left_u, right_v)
                    if overlap != tent_numerator(middle, left_gap, right_gap, width):
                        raise CertificateError("full-gap overlap/tent identity failed")
                    checked += 1
                    positive_rows += overlap > 0
    return {
        "parameter_box": "1<=M,u,v<=6; 1<=T<=M+u+v+2",
        "rows_checked": checked,
        "positive_overlap_rows": positive_rows,
        "same_sign_and_reverse_order_disjoint": True,
        "overlap_equals_tent_numerator": True,
        "pointwise_vectors": ["0", "+e_i", "-e_i", "e_j-e_i (i<j)"],
    }


def root_cone_data(
    points: Sequence[int], n: int, width: int
) -> tuple[list[list[int]], dict[tuple[int, int], int], dict[int, int]]:
    """Return T^2 G, T^2 psi, and T^2 rho for I={n,...,2n-1}."""
    if len(points) < 2 * n or n < 2 or width <= 0:
        raise ValueError("need 2n ordered marks, n>=2, and T>0")
    if any(points[i] >= points[i + 1] for i in range(2 * n - 1)):
        raise ValueError("marks must be strictly increasing")
    indices = tuple(range(n, 2 * n))
    gaps = {i: points[i] - points[i - 1] for i in indices}
    v = {i: (points[i - 1], points[i]) for i in indices}
    u = {i: (points[i - 1] + width, points[i] + width) for i in indices}
    overlap = {
        (i, j): interval_length(u[i], v[j])
        for i in indices
        for j in indices
        if i < j
    }
    matrix = [[0 for _ in indices] for _ in indices]
    for i in indices:
        matrix[i - n][i - n] = 2 * min(gaps[i], width)
    for (i, j), value in overlap.items():
        matrix[i - n][j - n] = matrix[j - n][i - n] = -value
    rho = {
        i: matrix[i - n][i - n]
        - sum(value for edge, value in overlap.items() if i in edge)
        for i in indices
    }
    if min(rho.values()) < 0:
        raise CertificateError("root-cone residual became negative")
    return matrix, overlap, rho


def determinant(matrix: Sequence[Sequence[F | int]]) -> F:
    work = [[F(value) for value in row] for row in matrix]
    size = len(work)
    if any(len(row) != size for row in work):
        raise ValueError("determinant needs a square matrix")
    result = F(1)
    for column in range(size):
        pivot_row = next((row for row in range(column, size) if work[row][column]), None)
        if pivot_row is None:
            return F(0)
        if pivot_row != column:
            work[pivot_row], work[column] = work[column], work[pivot_row]
            result = -result
        pivot = work[column][column]
        result *= pivot
        for row in range(column + 1, size):
            multiplier = work[row][column] / pivot
            for entry in range(column + 1, size):
                work[row][entry] -= multiplier * work[column][entry]
    return result


def quadratic(matrix: Sequence[Sequence[F | int]], vector: Sequence[F | int]) -> F:
    return sum(
        (F(vector[i]) * F(matrix[i][j]) * F(vector[j]) for i in range(len(vector)) for j in range(len(vector))),
        F(0),
    )


def bilinear(
    left: Sequence[F | int], matrix: Sequence[Sequence[F | int]], right: Sequence[F | int]
) -> F:
    return sum(
        (F(left[i]) * F(matrix[i][j]) * F(right[j]) for i in range(len(left)) for j in range(len(right))),
        F(0),
    )


def alpha(n: int, left: int, right: int) -> F:
    return F((right - left) ** 2, 4 * n * n)


def wave_b_matrix(n: int) -> list[list[F]]:
    indices = tuple(range(n, 2 * n))
    result = [[F(0) for _ in indices] for _ in indices]
    for left in indices:
        for right in range(left + 2, 2 * n):
            result[left - n][right - n] = result[right - n][left - n] = -alpha(n, left, right) / 2
    return result


def connected_nonadjacent_graph(n: int) -> bool:
    vertices = set(range(n, 2 * n))
    seen = {n}
    frontier = [n]
    while frontier:
        left = frontier.pop()
        neighbours = {right for right in vertices if abs(right - left) >= 2}
        new = neighbours - seen
        seen |= new
        frontier.extend(sorted(new))
    return seen == vertices


def n4_ramp_fixture() -> dict[str, object]:
    points = N4_POINTS
    n = 4
    width = 221
    differences = positive_differences(points)
    matrix, overlap, rho = root_cone_data(points, n, width)
    expected_matrix = (
        (214, 0, -106, -1),
        (0, 218, 0, -109),
        (-106, 0, 222, -3),
        (-1, -109, -3, 226),
    )
    expected_overlap = {(4, 5): 0, (4, 6): 106, (4, 7): 1, (5, 6): 0, (5, 7): 109, (6, 7): 3}
    expected_rho = {4: 107, 5: 109, 6: 113, 7: 113}
    if tuple(map(tuple, matrix)) != expected_matrix or overlap != expected_overlap or rho != expected_rho:
        raise CertificateError("n=4 Gram/root-cone fixture changed")

    indices = tuple(range(n, 2 * n))
    q_scaled = sum(
        (alpha(n, left, right) * overlap[left, right] for left in indices for right in range(left + 2, 2 * n)),
        F(0),
    )
    midpoint = F(3 * n - 1, 2)
    eta = tuple(F(i - midpoint, 2 * n) for i in indices)
    energy_scaled = quadratic(matrix, eta)
    adjacent_scaled = sum(F(overlap[i, i + 1], 4 * n * n) for i in range(n, 2 * n - 1))
    residual_scaled = sum(F(rho[i]) * eta[i - n] ** 2 for i in indices)
    if (
        q_scaled != F(869, 64)
        or energy_scaled != F(2845, 128)
        or energy_scaled - q_scaled != F(1107, 128)
        or residual_scaled != F(1101, 128)
        or adjacent_scaled != F(3, 64)
        or energy_scaled - q_scaled != residual_scaled + adjacent_scaled
    ):
        raise CertificateError("n=4 midpoint ramp identity changed")

    ones = (1, 1, 1, 1)
    ranks = indices
    one_g_one = bilinear(ones, matrix, ones)
    rank_g_one = bilinear(ranks, matrix, ones)
    rank_g_rank = bilinear(ranks, matrix, ranks)
    c_star = rank_g_one / one_g_one
    schur_energy = F(1, 4 * n * n) * (rank_g_rank - rank_g_one**2 / one_g_one)
    residual_variance = sum(F(rho[i]) * (i - c_star) ** 2 for i in indices)
    optimal_surplus = F(1, 4 * n * n) * (
        sum(F(overlap[i, i + 1]) for i in range(n, 2 * n - 1)) + residual_variance
    )
    if (
        (rank_g_rank, rank_g_one, one_g_one) != (F(14914), F(2442), F(442))
        or c_star != F(1221, 221)
        or schur_energy != F(39289, 1768)
        or residual_variance != F(121600, 221)
        or schur_energy - q_scaled != F(122263, 14144)
        or optimal_surplus != schur_energy - q_scaled
    ):
        raise CertificateError("n=4 optimal-shift Schur identity changed")

    leading_minors = tuple(determinant([row[:size] for row in matrix[:size]]) for size in range(1, n + 1))
    if leading_minors != (F(214), F(46652), F(7907296), F(1355494352)):
        raise CertificateError("n=4 Gram principal minors changed")

    b_matrix = wave_b_matrix(n)
    b_det = determinant(b_matrix)
    b_trace = sum(b_matrix[i][i] for i in range(n))
    cross_block_det = determinant(((b_matrix[0][2], b_matrix[0][3]), (b_matrix[1][2], b_matrix[1][3])))
    if b_det != F(1, 1048576) or b_trace or cross_block_det != F(1, 1024):
        raise CertificateError("n=4 Wave coefficient inertia witness changed")

    c_matrix = [[eta[i] * eta[j] - b_matrix[i][j] for j in range(n)] for i in range(n)]
    root_slacks: dict[str, str] = {}
    for left in indices:
        for right in range(left + 1, 2 * n):
            root = [F(0)] * n
            root[left - n] = -1
            root[right - n] = 1
            value = quadratic(c_matrix, root)
            expected = F(0) if right >= left + 2 else F(1, 4 * n * n)
            if value != expected:
                raise CertificateError("H-B root slack changed")
            root_slacks[f"{left},{right}"] = ftext(value)
    if not connected_nonadjacent_graph(n):
        raise CertificateError("n=4 nonadjacent graph ceased to be connected")
    cross_rows = (0, 1, 2, 3)
    witness_edge = (4, 6)
    schur_root_value = -F((cross_rows[witness_edge[1] - n] - cross_rows[witness_edge[0] - n]) ** 2)
    if schur_root_value != -4:
        raise CertificateError("zero-slack cross-coupling witness changed")

    return {
        "points": list(points),
        "difference_count": len(differences),
        "n": n,
        "T": width,
        "T_squared_G": matrix,
        "T_squared_psi": {f"{i},{j}": value for (i, j), value in sorted(overlap.items())},
        "T_squared_rho": {str(i): value for i, value in sorted(rho.items())},
        "leading_principal_minors_of_T_squared_G": [ftext(value) for value in leading_minors],
        "wave": {
            "T_squared_Q": ftext(q_scaled),
            "B_determinant": ftext(b_det),
            "B_trace": ftext(b_trace),
            "bipartite_cross_block_determinant": ftext(cross_block_det),
            "B_inertia_from_invertible_bipartite_block": [2, 2, 0],
        },
        "midpoint_ramp": {
            "c": ftext(midpoint),
            "eta": [ftext(value) for value in eta],
            "T_squared_energy": ftext(energy_scaled),
            "T_squared_surplus": ftext(energy_scaled - q_scaled),
            "T_squared_residual_surplus": ftext(residual_scaled),
            "T_squared_adjacent_surplus": ftext(adjacent_scaled),
            "root_slacks_of_H_minus_B": root_slacks,
        },
        "optimal_shift": {
            "rank_G_rank": ftext(rank_g_rank),
            "rank_G_one": ftext(rank_g_one),
            "one_G_one": ftext(one_g_one),
            "c_star": ftext(c_star),
            "T_squared_optimal_energy": ftext(schur_energy),
            "T_squared_optimal_surplus": ftext(schur_energy - q_scaled),
            "T_squared_residual_variance_before_1_over_4n_squared": ftext(residual_variance),
        },
        "zero_slack_cross_coupling": {
            "nonadjacent_graph_connected": True,
            "forced_condition": "X^T(e_j-e_i)=0 on every nonadjacent Wave edge",
            "consequence": "all rows of X are equal for n>=4",
            "nonconstant_scalar_rows": list(cross_rows),
            "witness_edge": list(witness_edge),
            "Schur_root_value_with_D_equal_1": ftext(schur_root_value),
        },
    }


def n5_triangle_fixture() -> dict[str, object]:
    points = N5_TRIANGLE_POINTS
    n = 5
    width = 107
    differences = positive_differences(points)
    _, overlap, _ = root_cone_data(points, n, width)
    triangle = ((5, 7), (7, 9), (5, 9))
    expected = {(5, 7): 97, (7, 9): 103, (5, 9): 1}
    if {edge: overlap[tuple(sorted(edge))] for edge in triangle} != expected:
        raise CertificateError("n=5 active triangle overlaps changed")
    rows = []
    for left, right in triangle:
        middle = points[right - 1] - points[left]
        terminal = points[right] - points[left - 1]
        numerator = overlap[tuple(sorted((left, right)))]
        if not (middle < width < terminal) or numerator <= 0:
            raise CertificateError("n=5 triangle edge is no longer active")
        rows.append(
            {
                "edge": [left, right],
                "M": middle,
                "D": terminal,
                "alpha": ftext(alpha(n, left, right)),
                "T_squared_psi": numerator,
                "psi": ftext(F(numerator, width * width)),
            }
        )
    return {
        "points": list(points),
        "n": n,
        "T": width,
        "difference_count": len(differences),
        "active_triangle_vertices": [5, 7, 9],
        "edges": rows,
        "odd_cycle_blocks_universal_bipartite_sign_switch": True,
    }


def small_scale_divergence_fixture() -> dict[str, object]:
    n = 4
    width = 1
    matrix, overlap, _ = root_cone_data(N4_POINTS, n, width)
    expected_matrix = ((2, -1, 0, 0), (-1, 2, -1, 0), (0, -1, 2, -1), (0, 0, -1, 2))
    if tuple(map(tuple, matrix)) != expected_matrix:
        raise CertificateError("small-scale adjacent Gram matrix changed")
    midpoint = F(3 * n - 1, 2)
    eta = tuple(F(i - midpoint, 2 * n) for i in range(n, 2 * n))
    q_scaled = sum(
        (alpha(n, left, right) * overlap[left, right] for left in range(n, 2 * n) for right in range(left + 2, 2 * n)),
        F(0),
    )
    energy = quadratic(matrix, eta) / (width * width)
    coefficient = F(n * n - 1, 8 * n * n)
    if q_scaled or energy != coefficient or coefficient != F(15, 128):
        raise CertificateError("small-scale divergence fixture changed")
    gaps = [N4_POINTS[i] - N4_POINTS[i - 1] for i in range(n, 2 * n)]
    lower_gate = min(gaps[1:-1])
    upper_gate = sum(gaps)
    if (lower_gate, upper_gate) != (109, 440):
        raise CertificateError("n=4 active localization gate changed")
    return {
        "n": n,
        "T": width,
        "minimum_block_gap": min(gaps),
        "T_squared_G": matrix,
        "Q": ftext(F(0)),
        "midpoint_ramp_energy": ftext(energy),
        "general_unlocalized_energy": "(n^2-1)/(8*n^2*T) for 0<T<min_i h_i",
        "log_divergence_coefficient_for_n_4": ftext(coefficient),
        "active_Q_scale_gate_for_n4": {"strict_lower": lower_gate, "strict_upper": upper_gate},
    }


def signed_band_cone_loss_fixture() -> dict[str, object]:
    points = SIGNED_BAND_POINTS
    n = 3
    width = 3
    differences = positive_differences(points)
    g_small, _, _ = root_cone_data(points, n, width)
    g_large, _, _ = root_cone_data(points, n, 2 * width)
    signed = [
        [F(g_small[i][j], width * width) - F(g_large[i][j], 4 * width * width) for j in range(n)]
        for i in range(n)
    ]
    expected = (
        (F(4, 9), F(-1, 4), F(1, 36)),
        (F(-1, 4), F(7, 18), F(-7, 36)),
        (F(1, 36), F(-7, 36), F(1, 3)),
    )
    if tuple(map(tuple, signed)) != expected:
        raise CertificateError("signed-band cone-loss fixture changed")
    b = wave_b_matrix(n)
    sum_zero = (1, -2, 1)
    b_value = quadratic(b, sum_zero)
    if b_value != F(-1, 9):
        raise CertificateError("coefficient-mixing counterfixture changed")
    return {
        "points": list(points),
        "difference_count": len(differences),
        "n": n,
        "T": width,
        "G_T_minus_G_2T": [[ftext(value) for value in row] for row in signed],
        "positive_offdiagonal_witness": {"entry": [0, 2], "value": ftext(signed[0][2])},
        "SDDM_root_cone_preserved": False,
        "sum_zero_coefficient_mixing_witness": {
            "vector": list(sum_zero),
            "quadratic_value_for_Wave_B": ftext(b_value),
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
        "theorem_contract": {
            "full_gap_identity": "T f_i = 1_{V_i} - 1_{U_i}, V_i=[a_{i-1},a_i), U_i=V_i+T",
            "root_cone": "G=diag(rho)+sum_{i<j} psi_ij (e_i-e_j)(e_i-e_j)^T, rho_i>=0",
            "dual": "<C,G>=sum_i rho_i C_ii+sum_{i<j} psi_ij(C_ii+C_jj-2C_ij)",
            "wave_B": "B_ii=0, B_ij=-alpha_ij/2 for j>=i+2, and <B,G>=Q_n(T)",
            "cellwise_SOS": "Q_n(T)=sum_{j>=i+2} alpha_ij ||T^{-1}1_{U_i intersect V_j}||_2^2",
            "rank_one_H": "eta_i=(i-c)/(2n), H=eta eta^T",
            "surplus": "eta^T G eta-Q=sum_i rho_i eta_i^2+(1/(4n^2))sum_i psi_{i,i+1}",
            "optimal_shift": "c_*=(r^T G 1)/(1^T G 1)=sum_i i rho_i/sum_i rho_i",
            "Schur_complement": "min_c eta^T G eta=(r^T G r-(r^T G 1)^2/(1^T G 1))/(4n^2)",
            "ramp_channel": "sum_i eta_i f_i=[(n-c)q_{a_{n-1}}+sum_{p=n}^{2n-2}q_{a_p}-(2n-1-c)q_{a_{2n-1}}]/(2n)",
        },
        "scope": {
            "proved": [
                "fixed-T actual ordered-box Gram root-cone factorization",
                "fixed-T Wave dual contraction and disjoint-cell SOS",
                "rank-one ramp domination with exact surplus",
                "optimal-c Schur complement",
                "exact n=4 ramp fixture and n=5 active-triangle fixture",
                "explicit signed-band cone-loss fixture",
            ],
            "not_proved": [
                "an ungated integral of the ramp energy down to T=0",
                "preservation under signed band differences or arbitrary cross-scale mixing",
                "nonconstant zero-slack Schur cross-coupling to external channels",
                "diagonal plus terminal payment in a legal common master",
                "signed or cross-epoch or larger-master closure",
                "Route C or C058",
                "either question in Erdos Problem 1191",
                "publication novelty, prize eligibility, or a complete proof",
            ],
        },
        "scope_gates": {
            "fixed_scale_actual_ordered_gram_only": True,
            "nonnegative_scale_mixtures_preserve_root_cone": True,
            "signed_band_differences_preserve_root_cone": False,
            "active_scale_localization_required_for_integrated_ramp_use": True,
            "zero_slack_supports_nonconstant_rank_cross_coupling": False,
            "common_master_diagonal_and_terminal_payment_closed": False,
            "route_c_closed": False,
            "C058_closed": False,
            "erdos_1191_solved": False,
        },
        "local_root_cone_audit": local_root_cone_audit(),
        "n4_ramp_fixture": n4_ramp_fixture(),
        "n5_triangle_fixture": n5_triangle_fixture(),
        "small_scale_divergence_fixture": small_scale_divergence_fixture(),
        "signed_band_cone_loss_fixture": signed_band_cone_loss_fixture(),
        "marginal_transport_reconciliation": {
            "statement": "Q<=V<=P_PSD/2 is a row/column-marginal relaxation and does not contradict the exact cellwise SOS or ramp master",
            "universal_order_between_V_and_ramp_energy_claimed": False,
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
    integrity = certificate.get("integrity", {})
    if not isinstance(integrity, Mapping) or integrity.get("payload_sha256") != payload_hash(certificate):
        raise CertificateError("payload hash mismatch")
    if integrity.get("source_hash_embedded") is not False:
        raise CertificateError("source/hash self-reference gate changed")
    if certificate != build_certificate():
        raise CertificateError("semantic replay mismatch")


def rehash(certificate: dict[str, object]) -> None:
    certificate.setdefault("integrity", {})["payload_sha256"] = payload_hash(certificate)


def self_check(certificate: Mapping[str, object]) -> int:
    mutations: list[dict[str, object]] = []

    changed = copy.deepcopy(certificate)
    changed["status"] = "ERDOS_1191_SOLVED"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["scope"]["not_proved"] = []
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["scope_gates"]["route_c_closed"] = True
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["theorem_contract"]["wave_B"] = "B is coefficient PSD"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["n4_ramp_fixture"]["T_squared_G"][0][2] = -105
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["n4_ramp_fixture"]["T_squared_rho"]["4"] = 108
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["n4_ramp_fixture"]["wave"]["T_squared_Q"] = "1/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["n4_ramp_fixture"]["optimal_shift"]["c_star"] = "11/2"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["n5_triangle_fixture"]["edges"][0]["psi"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["small_scale_divergence_fixture"]["Q"] = "1/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["signed_band_cone_loss_fixture"]["SDDM_root_cone_preserved"] = True
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["integrity"]["payload_sha256"] = "0" * 64
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
    parser.add_argument("--emit", action="store_true", help="emit canonical JSON to stdout")
    parser.add_argument("--verify", type=Path, help="verify an existing certificate")
    parser.add_argument("--self-check", action="store_true", help="run semantic mutation rejection")
    args = parser.parse_args()

    certificate = build_certificate()
    if args.verify:
        loaded = json.loads(args.verify.read_text(encoding="utf-8"))
        validate_certificate(loaded)
        if rendered_bytes(loaded) != rendered_bytes(certificate):
            raise CertificateError("byte replay mismatch")
    if args.self_check:
        self_check(certificate)
    if args.emit:
        sys.stdout.buffer.write(rendered_bytes(certificate))
    elif not args.verify and not args.self_check:
        print(certificate["integrity"]["payload_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
