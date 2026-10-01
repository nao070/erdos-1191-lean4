#!/usr/bin/env python3
"""Exact actual-cell LP certificate for an SDDM repair of direct ordered B.

The one-epoch fixture is the n=4, T=200 block from C079--C083.  The
correction is restricted to a nonnegative sum of complete-graph roots,

    C = sum_(i<j) w_ij (e_i-e_j)(e_i-e_j)^T,  w_ij >= 0,

and the only aggregate channel is kappa*J.  Two finite LPs are certified by
exact rational primal and dual feasible points with zero gap.  A second,
explicit n=4/n=8 consecutive-epoch fixture is also certified for the
total-trace objective.  Every semantic check uses ``fractions.Fraction``;
SciPy was used only to discover candidate active sets and is not a runtime
dependency of this file.

This is a bounded actual-cell result.  It does not solve the cross-scale
common-ledger problem, C058, Q1/Q2, or Erdos Problem #1191.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
from itertools import combinations
import json
from pathlib import Path
from typing import Mapping, Sequence


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "direct_b_membership_sddm_lp_certificate.json"
SCHEMA = "erdos1191.direct_b_membership_sddm_lp.v1"
STATUS = "EXACT_BOUNDED_ACTUAL_CELL_SDDM_LP_ONLY_GLOBAL_LEDGER_OPEN"

N = 4
T = 200
ONE_EPOCH_POINTS = (309, 416, 525, 636, 749)
FULL_TWO_EPOCH_POINTS = (
    0,
    101,
    204,
    309,
    416,
    525,
    636,
    749,
    864,
    981,
    1100,
    1221,
    1344,
    1469,
    1596,
    1725,
)
TWO_EPOCH_UNION_POINTS = FULL_TWO_EPOCH_POINTS[3:]


class CertificateError(RuntimeError):
    """Raised when an exact identity, LP constraint, or scope gate fails."""


def ftext(value: F | int) -> str:
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def matrix_text(matrix: Sequence[Sequence[F | int]]) -> list[list[str]]:
    return [[ftext(value) for value in row] for row in matrix]


def quadratic(matrix: Sequence[Sequence[F | int]], vector: Sequence[int]) -> F:
    if len(matrix) != len(vector) or any(len(row) != len(vector) for row in matrix):
        raise ValueError("quadratic-form dimensions do not match")
    return sum(
        (
            F(vector[i]) * F(matrix[i][j]) * F(vector[j])
            for i in range(len(vector))
            for j in range(len(vector))
        ),
        F(0),
    )


def wave_b_matrix(n: int) -> list[list[F]]:
    if n < 2:
        raise ValueError("n must be at least two")
    return [
        [
            F(0)
            if i == j or abs(i - j) == 1
            else -F((j - i) ** 2, 8 * n * n)
            for j in range(n)
        ]
        for i in range(n)
    ]


def incidence_matrix(n: int) -> list[list[F]]:
    return [[F((k == i) - (k == i + 1)) for k in range(n + 1)] for i in range(n)]


def point_m_matrix(n: int) -> list[list[F]]:
    """Return M=D^T B D without any floating arithmetic."""
    b = wave_b_matrix(n)
    d = incidence_matrix(n)
    return [
        [
            sum(
                (d[a][i] * b[a][c] * d[c][j] for a in range(n) for c in range(n)),
                F(0),
            )
            for j in range(n + 1)
        ]
        for i in range(n + 1)
    ]


def positive_differences(points: Sequence[int]) -> tuple[int, ...]:
    if any(points[i] >= points[i + 1] for i in range(len(points) - 1)):
        raise CertificateError("points are not strictly increasing")
    values = tuple(
        points[j] - points[i]
        for i in range(len(points))
        for j in range(i + 1, len(points))
    )
    if len(values) != len(set(values)):
        raise CertificateError("fixture is not a Golomb ruler")
    return tuple(sorted(values))


def scaled_haar_value(x: int, point: int, width: int) -> int:
    """Return 2T*(K_T-K_(2T))(x-point), using half-open boxes."""
    displacement = x - point
    return 2 * int(0 <= displacement < width) - int(0 <= displacement < 2 * width)


def interval_id(left: int | None, right: int | None) -> str:
    left_text = "-inf" if left is None else str(left)
    right_text = "+inf" if right is None else str(right)
    return f"[{left_text},{right_text})"


def atomic_cells(points: Sequence[int], width: int) -> list[dict[str, object]]:
    """Enumerate the complete real-line partition, including zero exteriors."""
    if width <= 0 or not points:
        raise ValueError("positive width and nonempty point list required")
    events = sorted({point + shift for point in points for shift in (0, width, 2 * width)})
    bounds: list[tuple[int | None, int | None]] = [(None, events[0])]
    bounds.extend(zip(events, events[1:]))
    bounds.append((events[-1], None))
    rows: list[dict[str, object]] = []
    for left, right in bounds:
        sample = events[0] - 1 if left is None else left
        state = tuple(scaled_haar_value(sample, point, width) for point in points)
        rows.append(
            {
                "id": interval_id(left, right),
                "left": "-inf" if left is None else left,
                "right": "+inf" if right is None else right,
                "length": "infinite" if left is None or right is None else right - left,
                "state": state,
            }
        )
    if rows[0]["state"] != (0,) * len(points) or rows[-1]["state"] != (0,) * len(points):
        raise CertificateError("exterior Haar state is not zero")
    if any(rows[i]["state"] == rows[i + 1]["state"] for i in range(len(rows) - 1)):
        raise CertificateError("a listed atomic endpoint does not change the vector state")
    return rows


def root_matrix(size: int, weights: Mapping[tuple[int, int], F]) -> list[list[F]]:
    matrix = [[F(0) for _ in range(size)] for _ in range(size)]
    for (i, j), weight in weights.items():
        if not (0 <= i < j < size) or weight < 0:
            raise CertificateError("invalid root weight")
        matrix[i][i] += weight
        matrix[j][j] += weight
        matrix[i][j] -= weight
        matrix[j][i] -= weight
    if any(sum(row, F(0)) for row in matrix):
        raise CertificateError("root correction does not annihilate one")
    return matrix


def embed_matrix(target: list[list[F]], source: Sequence[Sequence[F]], offset: int) -> None:
    for i in range(len(source)):
        for j in range(len(source)):
            target[offset + i][offset + j] += source[i][j]


def cell_rows(
    cells: Sequence[Mapping[str, object]],
    matrix: Sequence[Sequence[F]],
    supports: Sequence[Sequence[int]],
) -> list[dict[str, object]]:
    rows = []
    for cell in cells:
        state = tuple(int(value) for value in cell["state"])
        rows.append(
            {
                "id": cell["id"],
                "left": cell["left"],
                "right": cell["right"],
                "length": cell["length"],
                "state": list(state),
                "aggregate_sums": [sum(state[i] for i in support) for support in supports],
                "M_rhs": ftext(quadratic(matrix, state)),
            }
        )
    return rows


def verify_lp_solution(
    *,
    label: str,
    cells: Sequence[Mapping[str, object]],
    matrix: Sequence[Sequence[F]],
    supports: Sequence[Sequence[int]],
    root_weights: Mapping[tuple[int, int], F],
    kappas: Sequence[F],
    kappa_costs: Sequence[F],
    dual_weights: Mapping[str, F],
    expected: F,
) -> dict[str, object]:
    """Verify primal/dual feasibility and equality for min c*x, A*x>=b."""
    size = len(matrix)
    pairs = tuple(combinations(range(size), 2))
    if len(kappas) != len(supports) or len(kappa_costs) != len(supports):
        raise ValueError("aggregate channel dimensions do not match")
    if any(value < 0 for value in (*root_weights.values(), *kappas, *dual_weights.values())):
        raise CertificateError("LP variables and dual cell weights must be nonnegative")
    unknown_cells = set(dual_weights) - {str(cell["id"]) for cell in cells}
    if unknown_cells:
        raise CertificateError(f"dual refers to unknown cells: {sorted(unknown_cells)}")

    correction = root_matrix(size, root_weights)
    primal_rows: list[dict[str, object]] = []
    slack_by_id: dict[str, F] = {}
    for cell in cells:
        state = tuple(int(value) for value in cell["state"])
        root_energy = sum(
            (root_weights.get((i, j), F(0)) * (state[i] - state[j]) ** 2 for i, j in pairs),
            F(0),
        )
        aggregate_energies = tuple(
            kappas[k] * sum(state[i] for i in support) ** 2
            for k, support in enumerate(supports)
        )
        rhs = quadratic(matrix, state)
        lhs = root_energy + sum(aggregate_energies, F(0))
        slack = lhs - rhs
        if slack < 0:
            raise CertificateError(f"{label}: primal cell constraint failed at {cell['id']}")
        slack_by_id[str(cell["id"])] = slack
        primal_rows.append(
            {
                "id": cell["id"],
                "root_energy": ftext(root_energy),
                "aggregate_energies": [ftext(value) for value in aggregate_energies],
                "rhs": ftext(rhs),
                "slack": ftext(slack),
            }
        )

    primal_objective = 2 * sum(root_weights.values(), F(0)) + sum(
        (kappa_costs[k] * kappas[k] for k in range(len(kappas))), F(0)
    )
    edge_loads: dict[tuple[int, int], F] = {}
    for i, j in pairs:
        edge_loads[(i, j)] = sum(
            (
                dual_weights.get(str(cell["id"]), F(0))
                * (int(cell["state"][i]) - int(cell["state"][j])) ** 2
                for cell in cells
            ),
            F(0),
        )
        if edge_loads[(i, j)] > 2:
            raise CertificateError(f"{label}: dual edge constraint failed at {(i, j)}")
    aggregate_loads = []
    for k, support in enumerate(supports):
        load = sum(
            (
                dual_weights.get(str(cell["id"]), F(0))
                * sum(int(cell["state"][i]) for i in support) ** 2
                for cell in cells
            ),
            F(0),
        )
        if load > kappa_costs[k]:
            raise CertificateError(f"{label}: dual aggregate constraint failed")
        aggregate_loads.append(load)
    dual_objective = sum(
        (
            dual_weights.get(str(cell["id"]), F(0))
            * quadratic(matrix, tuple(int(value) for value in cell["state"]))
            for cell in cells
        ),
        F(0),
    )
    if primal_objective != dual_objective or primal_objective != expected:
        raise CertificateError(f"{label}: nonzero primal/dual gap or changed optimum")
    for edge, weight in root_weights.items():
        if weight and edge_loads[edge] != 2:
            raise CertificateError(f"{label}: positive root violates complementary slackness")
    for k, value in enumerate(kappas):
        if value and aggregate_loads[k] != kappa_costs[k]:
            raise CertificateError(f"{label}: positive kappa violates complementary slackness")
    for cell_id, weight in dual_weights.items():
        if weight and slack_by_id[cell_id] != 0:
            raise CertificateError(f"{label}: positive dual row violates complementary slackness")

    return {
        "label": label,
        "primal": {
            "root_weights": {f"{i},{j}": ftext(value) for (i, j), value in sorted(root_weights.items())},
            "kappas": [ftext(value) for value in kappas],
            "C_matrix": matrix_text(correction),
            "C_is_nonnegative_root_sum_hence_PSD_SDDM": True,
            "C_times_one_is_zero": True,
            "trace_C": ftext(2 * sum(root_weights.values(), F(0))),
            "objective": ftext(primal_objective),
            "cell_rows": primal_rows,
        },
        "dual": {
            "cell_weights": {key: ftext(value) for key, value in sorted(dual_weights.items())},
            "edge_loads": {f"{i},{j}": ftext(value) for (i, j), value in edge_loads.items()},
            "edge_capacity": "2/1",
            "aggregate_loads": [ftext(value) for value in aggregate_loads],
            "aggregate_capacities": [ftext(value) for value in kappa_costs],
            "objective": ftext(dual_objective),
        },
        "zero_duality_gap": True,
        "optimal_value": ftext(expected),
    }


def one_epoch_audit() -> dict[str, object]:
    matrix = point_m_matrix(N)
    cells = atomic_cells(ONE_EPOCH_POINTS, T)
    supports = (tuple(range(N + 1)),)
    if len(cells) != 16:
        raise CertificateError("one-epoch complete atomic-cell count changed")
    rows = cell_rows(cells, matrix, supports)
    expected_events = (309, 416, 509, 525, 616, 636, 709, 725, 749, 816, 836, 925, 949, 1036, 1149)
    actual_events = tuple(int(row["left"]) for row in cells[1:])
    if actual_events != expected_events:
        raise CertificateError("one-epoch event list changed")
    zero_sum_positive = [
        row for row in rows if row["aggregate_sums"] == [0] and F(row["M_rhs"]) > 0
    ]
    if [(row["id"], row["M_rhs"]) for row in zero_sum_positive] != [
        ("[636,709)", "1/8"),
        ("[749,816)", "1/8"),
    ]:
        raise CertificateError("zero-sum positive cells changed")

    lp_a = verify_lp_solution(
        label="A_minimize_trace_C_kappa_free_in_objective",
        cells=cells,
        matrix=matrix,
        supports=supports,
        root_weights={(1, 3): F(1, 32)},
        kappas=(F(3, 32),),
        kappa_costs=(F(0),),
        dual_weights={"[749,816)": F(1, 2)},
        expected=F(1, 16),
    )
    lp_b = verify_lp_solution(
        label="B_minimize_trace_C_plus_kappa_J",
        cells=cells,
        matrix=matrix,
        supports=supports,
        root_weights={(0, 2): F(1, 40), (2, 4): F(1, 40)},
        kappas=(F(0),),
        kappa_costs=(F(N + 1),),
        dual_weights={"[525,616)": F(2, 5), "[836,925)": F(2, 5)},
        expected=F(1, 10),
    )
    return {
        "n": N,
        "T": T,
        "mu": "1/1",
        "points": list(ONE_EPOCH_POINTS),
        "box_convention": "K_T=T^-1*1_[0,T); h_T=K_T-K_(2T); v=2T*h_T",
        "M": matrix_text(matrix),
        "event_count": len(expected_events),
        "complete_real_line_atomic_cell_count": len(cells),
        "finite_active_cell_count": len(cells) - 2,
        "atomic_cells": rows,
        "zero_sum_positive_M_cells": zero_sum_positive,
        "LP_A": lp_a,
        "LP_A_zero_sum_cells_force_positive_exact_correction": True,
        "LP_A_minimum_trace_C": "1/16",
        "LP_B": lp_b,
        "LP_B_minimum_trace_C_plus_kappa_J": "1/10",
    }


def two_epoch_matrix() -> tuple[list[list[F]], tuple[int, ...], tuple[int, ...]]:
    size = len(TWO_EPOCH_UNION_POINTS)
    matrix = [[F(0) for _ in range(size)] for _ in range(size)]
    first_support = tuple(range(0, 5))
    second_support = tuple(range(4, 13))
    embed_matrix(matrix, point_m_matrix(4), 0)
    embed_matrix(matrix, point_m_matrix(8), 4)
    return matrix, first_support, second_support


def nonzero_pair_support(matrix: Sequence[Sequence[F]], offset: int = 0) -> set[tuple[int, int]]:
    return {
        (offset + i, offset + j)
        for i in range(len(matrix))
        for j in range(i + 1, len(matrix))
        if matrix[i][j]
    }


def two_epoch_audit() -> dict[str, object]:
    differences = positive_differences(FULL_TWO_EPOCH_POINTS)
    if len(differences) != 120:
        raise CertificateError("two-epoch fixture difference count changed")
    matrix, first_support, second_support = two_epoch_matrix()
    first_pairs = nonzero_pair_support(point_m_matrix(4), 0)
    second_pairs = nonzero_pair_support(point_m_matrix(8), 4)
    if first_pairs & second_pairs:
        raise CertificateError("consecutive direct-M physical pair ownership overlaps")
    if set(first_support) & set(second_support) != {4}:
        raise CertificateError("consecutive blocks do not share exactly one endpoint")
    cells = atomic_cells(TWO_EPOCH_UNION_POINTS, T)
    if len(cells) != 40:
        raise CertificateError("two-epoch complete atomic-cell count changed")
    supports = (first_support, second_support)
    first_matrix = point_m_matrix(4)
    second_matrix = point_m_matrix(8)
    component_rows = []
    for cell in cells:
        state = tuple(int(value) for value in cell["state"])
        first_rhs = quadratic(first_matrix, state[:5])
        second_rhs = quadratic(second_matrix, state[4:])
        combined_rhs = quadratic(matrix, state)
        if first_rhs + second_rhs != combined_rhs:
            raise CertificateError("embedded epoch demands do not add to combined M")
        component_rows.append(
            {
                "id": cell["id"],
                "n4_M_rhs": ftext(first_rhs),
                "n8_M_rhs": ftext(second_rhs),
                "combined_M_rhs": ftext(combined_rhs),
            }
        )
    first_nonzero = sum(F(row["n4_M_rhs"]) != 0 for row in component_rows)
    first_positive = sum(F(row["n4_M_rhs"]) > 0 for row in component_rows)
    second_nonzero = sum(F(row["n8_M_rhs"]) != 0 for row in component_rows)
    second_positive = sum(F(row["n8_M_rhs"]) > 0 for row in component_rows)
    if (first_nonzero, first_positive, second_nonzero, second_positive) != (7, 5, 15, 5):
        raise CertificateError("two-epoch component activity counts changed")
    integrated_first = sum(
        (
            F(cell["length"])
            * F(component_rows[index]["n4_M_rhs"])
            / F((2 * T) ** 2)
            for index, cell in enumerate(cells)
            if cell["length"] != "infinite"
        ),
        F(0),
    )
    integrated_second = sum(
        (
            F(cell["length"])
            * F(component_rows[index]["n8_M_rhs"])
            / F((2 * T) ** 2)
            for index, cell in enumerate(cells)
            if cell["length"] != "infinite"
        ),
        F(0),
    )
    integrated_combined = integrated_first + integrated_second
    if (integrated_first, integrated_second, integrated_combined) != (
        F(63, 256000),
        F(169, 5120000),
        F(1429, 5120000),
    ):
        raise CertificateError("two-epoch integrated Haar-band demands changed")
    solution = verify_lp_solution(
        label="two_epoch_B_total_trace_common_scale",
        cells=cells,
        matrix=matrix,
        supports=supports,
        root_weights={
            (0, 2): F(45, 1792),
            (2, 4): F(11, 448),
            (4, 6): F(3, 1792),
            (10, 12): F(1, 128),
        },
        kappas=(F(0), F(0)),
        kappa_costs=(F(5), F(9)),
        dual_weights={
            "[636,709)": F(3, 7),
            "[836,864)": F(2, 7),
            "[1100,1149)": F(3, 7),
            "[1725,1744)": F(1, 2),
        },
        expected=F(53, 448),
    )
    correction = root_matrix(
        len(TWO_EPOCH_UNION_POINTS),
        {
            (0, 2): F(45, 1792),
            (2, 4): F(11, 448),
            (4, 6): F(3, 1792),
            (10, 12): F(1, 128),
        },
    )
    if correction[4][4] != F(47, 1792):
        raise CertificateError("shared endpoint correction diagonal changed")
    if any(F(value) for value in solution["primal"]["kappas"]):
        raise CertificateError("two-epoch aggregate baselines unexpectedly became active")
    first_dual_share = F(3, 7) * F(1, 8) + F(2, 7) * F(1, 8)
    second_dual_share = F(3, 7) * F(1, 32) + F(1, 2) * F(1, 32)
    if (first_dual_share, second_dual_share, first_dual_share + second_dual_share) != (
        F(40, 448),
        F(13, 448),
        F(53, 448),
    ):
        raise CertificateError("two-epoch dual objective split changed")
    return {
        "full_16_mark_Golomb_fixture": list(FULL_TWO_EPOCH_POINTS),
        "positive_difference_count": len(differences),
        "common_T": T,
        "epochs": [
            {"n": 4, "global_mark_indices": [3, 7], "union_coordinate_support": list(first_support)},
            {"n": 8, "global_mark_indices": [7, 15], "union_coordinate_support": list(second_support)},
        ],
        "union_points": list(TWO_EPOCH_UNION_POINTS),
        "shared_physical_point": 749,
        "shared_union_coordinate": 4,
        "direct_M_pair_supports_disjoint": True,
        "combined_M": matrix_text(matrix),
        "complete_real_line_atomic_cell_count": len(cells),
        "atomic_cells": cell_rows(cells, matrix, supports),
        "per_epoch_cell_demands": component_rows,
        "epoch_activity": {
            "n4_nonzero_cell_constraints": first_nonzero,
            "n4_positive_cell_constraints": first_positive,
            "n8_nonzero_cell_constraints": second_nonzero,
            "n8_positive_cell_constraints": second_positive,
            "n4_integrated_signed_Haar_band": ftext(integrated_first),
            "n8_integrated_signed_Haar_band": ftext(integrated_second),
            "combined_integrated_signed_Haar_band": ftext(integrated_combined),
            "n4_dual_objective_share": ftext(first_dual_share),
            "n8_dual_objective_share": ftext(second_dual_share),
            "both_epochs_are_substantively_active_at_common_T": True,
        },
        "LP_B": solution,
        "shared_endpoint_ownership": {
            "aggregate_kappas_are_zero": True,
            "no_double_owned_J_diagonal_is_used": True,
            "shared_diagonal_accounting": "recorded once in the single global correction matrix C; this is not an external paid-capacity owner",
            "budget_owner_supplied": False,
            "C_shared_endpoint_diagonal": "47/1792",
            "C_shared_endpoint_diagonal_trace_multiplicity": 1,
            "direct_M_diagonals_are_zero": True,
        },
    }


def payload_hash(certificate: Mapping[str, object]) -> str:
    payload = {key: value for key, value in certificate.items() if key != "integrity"}
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def rendered_bytes(certificate: Mapping[str, object]) -> bytes:
    return (json.dumps(certificate, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def build_certificate() -> dict[str, object]:
    one = one_epoch_audit()
    two = two_epoch_audit()
    certificate: dict[str, object] = {
        "schema": SCHEMA,
        "status": STATUS,
        "scope": {
            "proved": [
                "exact complete actual-cell enumeration for the n=4 T=200 fixture",
                "exact coefficient-trace primal-dual optima within the root-SDDM-plus-J class for the two stated one-epoch objectives at mu=1",
                "exact coefficient-total-trace optimum in the same class for one stated n=4/n=8 consecutive-epoch common-T fixture",
            ],
            "not_proved": [
                "a uniform bound over all Golomb/Sidon fixtures",
                "a simultaneous theorem over all dyadic scales or phases",
                "an integrated-energy optimum or a lower bound for arbitrary PSD, indefinite, or signed repairs",
                "payment by an already-owned disjoint capacity",
                "a Gothic rewrite, cross-scale ownership theorem, or external budget owner",
                "C058 or Q1 or Q2",
                "Erdos Problem 1191",
                "publication novelty or prize eligibility",
            ],
        },
        "LP_convention": {
            "mu": "1/1",
            "correction": "C=sum_(i<j) w_ij*(e_i-e_j)*(e_i-e_j)^T with w_ij>=0",
            "cell_constraint": "sum w_ij*(v_i-v_j)^2+sum kappa_s*(sum_(i in block_s) v_i)^2>=v^T M_total v",
            "dual": "max sum_c y_c*(v_c^T M_total v_c), y_c>=0; edge loads <=2 and aggregate loads <= their trace costs",
            "dual_cell_weights_are_abstract_LP_multipliers_not_lengths_or_measures": True,
        },
        "one_epoch": one,
        "two_consecutive_epochs": two,
    }
    certificate["integrity"] = {"payload_sha256": payload_hash(certificate), "canonical_json": True}
    return certificate


def validate_certificate(certificate: Mapping[str, object]) -> None:
    expected = build_certificate()
    if certificate.get("schema") != SCHEMA or certificate.get("status") != STATUS:
        raise CertificateError("schema or status mismatch")
    if certificate.get("integrity", {}).get("payload_sha256") != payload_hash(certificate):
        raise CertificateError("payload hash mismatch")
    if certificate != expected:
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
    changed["one_epoch"]["LP_A"]["optimal_value"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["one_epoch"]["LP_A"]["dual"]["cell_weights"]["[749,816)"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["one_epoch"]["LP_B"]["primal"]["root_weights"]["0,2"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["one_epoch"]["atomic_cells"][6]["M_rhs"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["one_epoch"]["complete_real_line_atomic_cell_count"] = 15
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["two_consecutive_epochs"]["LP_B"]["optimal_value"] = "1/9"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["two_consecutive_epochs"]["shared_endpoint_ownership"]["no_double_owned_J_diagonal_is_used"] = False
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["two_consecutive_epochs"]["full_16_mark_Golomb_fixture"][-1] = 815
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["LP_convention"]["mu"] = "2/1"
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
    parser.add_argument("--output", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--verify", type=Path, help="verify an existing certificate")
    parser.add_argument("--self-check", action="store_true", help="run semantic mutation checks")
    args = parser.parse_args()

    certificate = build_certificate()
    if args.verify:
        raw = args.verify.read_bytes()
        loaded = json.loads(raw.decode("utf-8"))
        validate_certificate(loaded)
        if raw != rendered_bytes(certificate):
            raise CertificateError("byte replay mismatch")
    if args.self_check:
        self_check(certificate)
    if not args.verify:
        args.output.write_bytes(rendered_bytes(certificate))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
