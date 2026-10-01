#!/usr/bin/env python3
"""Exact physical-Haar-energy LP certificate for the direct ordered-B repair.

This certificate reuses the exact fixtures and actual half-open cell
enumerator from ``direct_b_membership_sddm_lp_certificate`` but replaces the
coefficient-trace objective by

    sum_c |c|/(2T) * [v_c^T C v_c + sum_s kappa_s s_(c,s)^2].

All accepted primal and dual solutions are rational and are checked with
``fractions.Fraction``.  A floating LP solver was used only to discover
candidate active sets; it is not a runtime dependency.
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

import direct_b_membership_sddm_lp_certificate as membership


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "direct_b_physical_energy_lp_certificate.json"
SCHEMA = "erdos1191.direct_b_physical_energy_lp.v1"
STATUS = "EXACT_FIXED_FIXTURE_PHYSICAL_HAAR_LP_ONLY_UNIVERSAL_PAYMENT_OPEN"
T = membership.T
THREE_EPOCH_T = 2000
THREE_EPOCH_COUNTER_T = 2500
THREE_EPOCH_FULL_POINTS = tuple(k * (k + 1000) for k in range(32))
THREE_EPOCH_UNION_POINTS = THREE_EPOCH_FULL_POINTS[3:]


class CertificateError(RuntimeError):
    """Raised when an exact cost, LP constraint, or scope gate fails."""


def ftext(value: F | int) -> str:
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def cell_weight(cell: Mapping[str, object], width: int) -> F:
    length = cell["length"]
    return F(0) if length == "infinite" else F(int(length), 2 * width)


def physical_root_cost(distance: int | F, width: int | F) -> F:
    """Return chi_T(d)=2T*||h_T-h_T(.-d)||_2^2 exactly."""
    distance = abs(F(distance))
    width = F(width)
    if width <= 0:
        raise ValueError("width must be positive")
    if distance <= width:
        return 3 * distance / width
    if distance <= 2 * width:
        return 4 - distance / width
    return F(2)


def root_cost_from_cells(distance: int, width: int) -> F:
    cells = membership.atomic_cells((0, distance), width)
    return sum(
        (
            cell_weight(cell, width)
            * (int(cell["state"][0]) - int(cell["state"][1])) ** 2
            for cell in cells
        ),
        F(0),
    )


def root_cost_audit() -> dict[str, object]:
    checked = 0
    for width in range(1, 17):
        for distance in range(0, 3 * width + 3):
            if root_cost_from_cells(distance, width) != physical_root_cost(distance, width):
                raise CertificateError("piecewise physical root cost failed")
            checked += 1
    breakpoints = {
        "d=0": ftext(physical_root_cost(0, T)),
        "d=T": ftext(physical_root_cost(T, T)),
        "d=2T": ftext(physical_root_cost(2 * T, T)),
        "d=3T": ftext(physical_root_cost(3 * T, T)),
    }
    if breakpoints != {"d=0": "0/1", "d=T": "3/1", "d=2T": "2/1", "d=3T": "2/1"}:
        raise CertificateError("root cost breakpoints changed")
    return {
        "scaled_Haar_profile": "g_T=2T*h_T=1_[0,T)-1_[T,2T)",
        "autocorrelation": "A_T(d)=2T-3d for 0<=d<=T; d-2T for T<=d<=2T; 0 for d>=2T",
        "piecewise_root_cost": "chi_T(d)=3d/T for 0<=d<=T; 4-d/T for T<=d<=2T; 2 for d>=2T",
        "interpretation": "chi_T(d)=(1/(2T))*integral (g_T(x)-g_T(x-d))^2 dx",
        "exact_integer_parameter_rows_checked": checked,
        "breakpoints": breakpoints,
    }


def physical_costs(
    points: Sequence[int],
    cells: Sequence[Mapping[str, object]],
    supports: Sequence[Sequence[int]],
    width: int,
) -> tuple[dict[tuple[int, int], F], tuple[F, ...]]:
    pairs = tuple(combinations(range(len(points)), 2))
    edge_costs: dict[tuple[int, int], F] = {}
    for i, j in pairs:
        value = sum(
            (
                cell_weight(cell, width)
                * (int(cell["state"][i]) - int(cell["state"][j])) ** 2
                for cell in cells
            ),
            F(0),
        )
        expected = physical_root_cost(points[j] - points[i], width)
        if value != expected:
            raise CertificateError(f"cell/root physical cost mismatch at {(i, j)}")
        edge_costs[(i, j)] = value
    aggregate_costs = tuple(
        sum(
            (
                cell_weight(cell, width)
                * sum(int(cell["state"][i]) for i in support) ** 2
                for cell in cells
            ),
            F(0),
        )
        for support in supports
    )
    return edge_costs, aggregate_costs


def base_cell_rows(
    cells: Sequence[Mapping[str, object]],
    matrix: Sequence[Sequence[F]],
    supports: Sequence[Sequence[int]],
    width: int,
) -> list[dict[str, object]]:
    rows = []
    for cell in cells:
        state = tuple(int(value) for value in cell["state"])
        rhs = membership.quadratic(matrix, state)
        weight = cell_weight(cell, width)
        rows.append(
            {
                "id": cell["id"],
                "left": cell["left"],
                "right": cell["right"],
                "length": cell["length"],
                "state": list(state),
                "aggregate_sums": [sum(state[i] for i in support) for support in supports],
                "M_rhs": ftext(rhs),
                "physical_weight_length_over_2T": ftext(weight),
                "weighted_signed_demand": ftext(weight * rhs),
            }
        )
    return rows


def verify_physical_solution(
    *,
    label: str,
    width: int,
    points: Sequence[int],
    cells: Sequence[Mapping[str, object]],
    matrix: Sequence[Sequence[F]],
    supports: Sequence[Sequence[int]],
    root_weights: Mapping[tuple[int, int], F],
    kappas: Sequence[F],
    dual_weights: Mapping[str, F],
    expected: F,
) -> dict[str, object]:
    size = len(points)
    pairs = tuple(combinations(range(size), 2))
    edge_costs, aggregate_costs = physical_costs(points, cells, supports, width)
    if len(kappas) != len(supports):
        raise ValueError("kappa/support dimensions do not match")
    if any(value < 0 for value in (*root_weights.values(), *kappas, *dual_weights.values())):
        raise CertificateError(f"{label}: negative primal or dual variable")
    cell_ids = {str(cell["id"]) for cell in cells}
    if set(dual_weights) - cell_ids:
        raise CertificateError(f"{label}: dual uses an unknown cell")

    correction = membership.root_matrix(size, root_weights)
    primal_rows = []
    slack_by_id: dict[str, F] = {}
    objective_from_cells = F(0)
    signed_demand = F(0)
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
        lhs = root_energy + sum(aggregate_energies, F(0))
        rhs = membership.quadratic(matrix, state)
        slack = lhs - rhs
        if slack < 0:
            raise CertificateError(f"{label}: primal constraint failed at {cell['id']}")
        weight = cell_weight(cell, width)
        objective_from_cells += weight * lhs
        signed_demand += weight * rhs
        slack_by_id[str(cell["id"])] = slack
        primal_rows.append(
            {
                "id": cell["id"],
                "root_energy": ftext(root_energy),
                "aggregate_energies": [ftext(value) for value in aggregate_energies],
                "rhs": ftext(rhs),
                "slack": ftext(slack),
                "weighted_correction_energy": ftext(weight * lhs),
                "weighted_signed_demand": ftext(weight * rhs),
            }
        )

    primal_objective = sum(
        (edge_costs[edge] * root_weights.get(edge, F(0)) for edge in pairs), F(0)
    ) + sum(
        (aggregate_costs[k] * kappas[k] for k in range(len(kappas))), F(0)
    )
    if primal_objective != objective_from_cells:
        raise CertificateError(f"{label}: root-cost and cell-sum objectives disagree")

    edge_loads: dict[tuple[int, int], F] = {}
    for i, j in pairs:
        load = sum(
            (
                dual_weights.get(str(cell["id"]), F(0))
                * (int(cell["state"][i]) - int(cell["state"][j])) ** 2
                for cell in cells
            ),
            F(0),
        )
        if load > edge_costs[(i, j)]:
            raise CertificateError(f"{label}: dual root constraint failed at {(i, j)}")
        edge_loads[(i, j)] = load
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
        if load > aggregate_costs[k]:
            raise CertificateError(f"{label}: dual aggregate constraint failed")
        aggregate_loads.append(load)
    dual_objective = sum(
        (
            dual_weights.get(str(cell["id"]), F(0))
            * membership.quadratic(matrix, tuple(int(value) for value in cell["state"]))
            for cell in cells
        ),
        F(0),
    )
    if primal_objective != dual_objective or primal_objective != expected:
        raise CertificateError(f"{label}: nonzero duality gap or changed optimum")
    for edge, value in root_weights.items():
        if value and edge_loads[edge] != edge_costs[edge]:
            raise CertificateError(f"{label}: positive root violates complementary slackness")
    for k, value in enumerate(kappas):
        if value and aggregate_loads[k] != aggregate_costs[k]:
            raise CertificateError(f"{label}: positive kappa violates complementary slackness")
    for cell_id, value in dual_weights.items():
        if value and slack_by_id[cell_id] != 0:
            raise CertificateError(f"{label}: positive dual cell violates complementary slackness")

    # The physical cell-length measure is itself a canonical dual feasible
    # point: by definition it saturates every root and aggregate cost column.
    measure_weights = {str(cell["id"]): cell_weight(cell, width) for cell in cells}
    for i, j in pairs:
        measure_load = sum(
            (
                measure_weights[str(cell["id"])]
                * (int(cell["state"][i]) - int(cell["state"][j])) ** 2
                for cell in cells
            ),
            F(0),
        )
        if measure_load != edge_costs[(i, j)]:
            raise CertificateError(f"{label}: cell-length dual misses root cost at {(i, j)}")
    for k, support in enumerate(supports):
        measure_load = sum(
            (
                measure_weights[str(cell["id"])]
                * sum(int(cell["state"][i]) for i in support) ** 2
                for cell in cells
            ),
            F(0),
        )
        if measure_load != aggregate_costs[k]:
            raise CertificateError(f"{label}: cell-length dual misses aggregate cost")
    measure_objective = sum(
        (
            measure_weights[str(cell["id"])]
            * membership.quadratic(matrix, tuple(int(value) for value in cell["state"]))
            for cell in cells
        ),
        F(0),
    )
    if measure_objective != signed_demand:
        raise CertificateError(f"{label}: cell-length dual demand mismatch")

    return {
        "label": label,
        "objective_definition": "sum_c |cell|/(2T) * [v_c^T C v_c + sum_s kappa_s*s_(c,s)^2]",
        "primal": {
            "root_weights": {f"{i},{j}": ftext(value) for (i, j), value in sorted(root_weights.items())},
            "kappas": [ftext(value) for value in kappas],
            "C_matrix": membership.matrix_text(correction),
            "C_is_singular_PSD_graph_Laplacian": True,
            "C_times_one_is_zero": True,
            "objective_from_root_and_aggregate_costs": ftext(primal_objective),
            "objective_from_complete_cell_sum": ftext(objective_from_cells),
            "cell_rows": primal_rows,
        },
        "costs": {
            "root_costs": {f"{i},{j}": ftext(value) for (i, j), value in edge_costs.items()},
            "aggregate_costs": [ftext(value) for value in aggregate_costs],
        },
        "dual": {
            "cell_weights": {key: ftext(value) for key, value in sorted(dual_weights.items())},
            "cell_weights_are_abstract_LP_multipliers_not_lengths": True,
            "root_loads": {f"{i},{j}": ftext(value) for (i, j), value in edge_loads.items()},
            "tight_root_constraints": [
                f"{i},{j}" for i, j in pairs if edge_loads[(i, j)] == edge_costs[(i, j)]
            ],
            "inactive_but_tight_root_constraints": [
                f"{i},{j}"
                for i, j in pairs
                if edge_loads[(i, j)] == edge_costs[(i, j)]
                and root_weights.get((i, j), F(0)) == 0
            ],
            "aggregate_loads": [ftext(value) for value in aggregate_loads],
            "objective": ftext(dual_objective),
        },
        "canonical_cell_length_dual": {
            "weights": {key: ftext(value) for key, value in measure_weights.items()},
            "weights_are_exact_cell_length_over_2T_not_optimized_multipliers": True,
            "every_root_and_aggregate_cost_column_is_saturated": True,
            "objective_equals_weighted_signed_direct_B_demand": ftext(measure_objective),
            "dual_feasible_lower_bound": True,
        },
        "weighted_signed_direct_B_demand": ftext(signed_demand),
        "physical_correction_surplus_over_signed_demand": ftext(primal_objective - signed_demand),
        "zero_duality_gap": True,
        "optimal_value": ftext(expected),
    }


def fixture_audits() -> tuple[dict[str, object], dict[str, object], dict[str, object]]:
    # One n=4 epoch.
    points4 = membership.ONE_EPOCH_POINTS
    cells4 = membership.atomic_cells(points4, T)
    matrix4 = membership.point_m_matrix(4)
    support4 = (tuple(range(5)),)
    solution4 = verify_physical_solution(
        label="separate_n4_physical_energy_LP",
        width=T,
        points=points4,
        cells=cells4,
        matrix=matrix4,
        supports=support4,
        root_weights={(0, 2): F(1, 40), (2, 4): F(1, 40)},
        kappas=(F(0),),
        dual_weights={
            "[525,616)": F(349, 1000),
            "[636,709)": F(713, 3000),
            "[749,816)": F(209, 1000),
            "[836,925)": F(1093, 3000),
        },
        expected=F(29, 200),
    )
    if solution4["costs"]["aggregate_costs"] != ["3/1"]:
        raise CertificateError("n=4 aggregate physical cost changed")

    # Separate n=8 epoch from the substantive quadratic Golomb fixture.
    points8 = membership.FULL_TWO_EPOCH_POINTS[7:]
    cells8 = membership.atomic_cells(points8, T)
    matrix8 = membership.point_m_matrix(8)
    support8 = (tuple(range(9)),)
    solution8 = verify_physical_solution(
        label="separate_n8_physical_energy_LP",
        width=T,
        points=points8,
        cells=cells8,
        matrix=matrix8,
        supports=support8,
        root_weights={(0, 2): F(1, 128), (6, 8): F(1, 128)},
        kappas=(F(0),),
        dual_weights={
            "[981,1064)": F(217, 800),
            "[1100,1149)": F(351, 800),
            "[1725,1744)": F(157, 800),
            "[1796,1869)": F(387, 800),
        },
        expected=F(139, 3200),
    )
    if solution8["costs"]["aggregate_costs"] != ["97/25"]:
        raise CertificateError("n=8 aggregate physical cost changed")

    # Joint n=4/n=8 common-scale problem on the 13-point union.
    points_joint = membership.TWO_EPOCH_UNION_POINTS
    cells_joint = membership.atomic_cells(points_joint, T)
    matrix_joint, first_support, second_support = membership.two_epoch_matrix()
    solution_joint = verify_physical_solution(
        label="joint_n4_n8_common_scale_physical_energy_LP",
        width=T,
        points=points_joint,
        cells=cells_joint,
        matrix=matrix_joint,
        supports=(first_support, second_support),
        root_weights={
            (0, 2): F(45, 1792),
            (2, 4): F(11, 448),
            (4, 6): F(3, 1792),
            (10, 12): F(1, 128),
        },
        kappas=(F(0), F(0)),
        dual_weights={
            "[525,616)": F(5297, 15400),
            "[636,709)": F(623, 2200),
            "[749,816)": F(3529, 15400),
            "[836,864)": F(401, 2200),
            "[981,1036)": F(1249, 3850),
            "[1036,1064)": F(7, 1760),
            "[1100,1149)": F(223, 800),
            "[1725,1744)": F(283, 600),
            "[1796,1869)": F(5, 24),
        },
        expected=F(3809, 22400),
    )
    if solution_joint["costs"]["aggregate_costs"] != ["3/1", "97/25"]:
        raise CertificateError("joint aggregate physical costs changed")
    joint_dual = {
        key: F(value)
        for key, value in solution_joint["dual"]["cell_weights"].items()
    }
    n4_dual_share = F(0)
    n8_dual_share = F(0)
    for cell in cells_joint:
        multiplier = joint_dual.get(str(cell["id"]), F(0))
        state = tuple(int(value) for value in cell["state"])
        n4_dual_share += multiplier * membership.quadratic(matrix4, state[:5])
        n8_dual_share += multiplier * membership.quadratic(matrix8, state[4:])
    if (n4_dual_share, n8_dual_share, n4_dual_share + n8_dual_share) != (
        F(727, 5600),
        F(901, 22400),
        F(3809, 22400),
    ):
        raise CertificateError("joint physical dual epoch split changed")

    return (
        {
            "n": 4,
            "T": T,
            "mu": "1/1",
            "points": list(points4),
            "complete_real_line_atomic_cell_count": len(cells4),
            "atomic_cells": base_cell_rows(cells4, matrix4, support4, T),
            "LP": solution4,
        },
        {
            "n": 8,
            "T": T,
            "mu": "1/1",
            "points": list(points8),
            "complete_real_line_atomic_cell_count": len(cells8),
            "atomic_cells": base_cell_rows(cells8, matrix8, support8, T),
            "LP": solution8,
        },
        {
            "epochs": [4, 8],
            "T": T,
            "mu_each": "1/1",
            "points": list(points_joint),
            "supports": [list(first_support), list(second_support)],
            "shared_physical_point": 749,
            "complete_real_line_atomic_cell_count": len(cells_joint),
            "atomic_cells": base_cell_rows(cells_joint, matrix_joint, (first_support, second_support), T),
            "LP": solution_joint,
            "dual_objective_epoch_split": {
                "n4": ftext(n4_dual_share),
                "n8": ftext(n8_dual_share),
                "both_strictly_positive": True,
            },
            "budget_owner_supplied": False,
        },
    )


def verify_embedded_separate_primal(joint: Mapping[str, object]) -> dict[str, object]:
    points = membership.TWO_EPOCH_UNION_POINTS
    cells = membership.atomic_cells(points, T)
    matrix, first_support, second_support = membership.two_epoch_matrix()
    weights = {
        (0, 2): F(1, 40),
        (2, 4): F(1, 40),
        (4, 6): F(1, 128),
        (10, 12): F(1, 128),
    }
    edge_costs, aggregate_costs = physical_costs(points, cells, (first_support, second_support), T)
    for cell in cells:
        state = tuple(int(value) for value in cell["state"])
        lhs = sum((value * (state[i] - state[j]) ** 2 for (i, j), value in weights.items()), F(0))
        rhs = membership.quadratic(matrix, state)
        if lhs < rhs:
            raise CertificateError("embedded separate physical primal is not jointly feasible")
    objective = sum((edge_costs[edge] * value for edge, value in weights.items()), F(0))
    separate_sum = F(29, 200) + F(139, 3200)
    joint_value = F(joint["LP"]["optimal_value"])
    saving = separate_sum - joint_value
    if (objective, separate_sum, joint_value, saving) != (
        F(603, 3200),
        F(603, 3200),
        F(3809, 22400),
        F(103, 5600),
    ) or saving <= 0:
        raise CertificateError("separate/joint physical comparison changed")
    return {
        "embedded_separate_root_weights": {
            f"{i},{j}": ftext(value) for (i, j), value in sorted(weights.items())
        },
        "embedded_separate_is_jointly_feasible": True,
        "sum_of_separate_optima": ftext(separate_sum),
        "joint_optimum": ftext(joint_value),
        "joint_strictly_less_than_sum_of_separate": True,
        "exact_joint_saving": ftext(saving),
        "reason": "the joint LP dominates only the signed sum M4+M8 on union cells, so one global root correction can serve both epochs and exploit their signed cell alignment; it is not required to dominate each epoch separately",
        "not_a_paid_ledger_reason": "the LP supplies no disjoint Gothic, birth, phase, cross-scale, or external reserve budget that pays the physical correction objective",
    }


def three_epoch_matrix() -> tuple[list[list[F]], tuple[tuple[int, ...], ...]]:
    """Embed n=4,8,16 direct matrices on the 29-point shared union."""
    size = len(THREE_EPOCH_UNION_POINTS)
    matrix = [[F(0) for _ in range(size)] for _ in range(size)]
    specifications = ((4, 0), (8, 4), (16, 12))
    supports = []
    pair_supports = []
    for n, offset in specifications:
        source = membership.point_m_matrix(n)
        membership.embed_matrix(matrix, source, offset)
        supports.append(tuple(range(offset, offset + n + 1)))
        pair_supports.append(membership.nonzero_pair_support(source, offset))
    if any(pair_supports[i] & pair_supports[j] for i in range(3) for j in range(i + 1, 3)):
        raise CertificateError("three-epoch direct-M pair ownership overlaps")
    if set(supports[0]) & set(supports[1]) != {4}:
        raise CertificateError("n=4/n=8 shared endpoint changed")
    if set(supports[1]) & set(supports[2]) != {12}:
        raise CertificateError("n=8/n=16 shared endpoint changed")
    if set(supports[0]) & set(supports[2]):
        raise CertificateError("nonconsecutive epoch supports overlap")
    return matrix, tuple(supports)


def three_epoch_component_audit(
    cells: Sequence[Mapping[str, object]], supports: Sequence[Sequence[int]]
) -> tuple[list[dict[str, object]], tuple[F, F, F]]:
    matrices = (
        membership.point_m_matrix(4),
        membership.point_m_matrix(8),
        membership.point_m_matrix(16),
    )
    rows = []
    demands = [F(0), F(0), F(0)]
    nonzero = [0, 0, 0]
    positive = [0, 0, 0]
    negative = [0, 0, 0]
    for cell in cells:
        state = tuple(int(value) for value in cell["state"])
        values = []
        for k, support in enumerate(supports):
            local = tuple(state[i] for i in support)
            value = membership.quadratic(matrices[k], local)
            values.append(value)
            demands[k] += cell_weight(cell, THREE_EPOCH_T) * value
            nonzero[k] += value != 0
            positive[k] += value > 0
            negative[k] += value < 0
        rows.append(
            {
                "id": cell["id"],
                "n4_M_rhs": ftext(values[0]),
                "n8_M_rhs": ftext(values[1]),
                "n16_M_rhs": ftext(values[2]),
                "combined_M_rhs": ftext(sum(values, F(0))),
            }
        )
    if (tuple(nonzero), tuple(positive), tuple(negative), tuple(demands)) != (
        (7, 16, 31),
        (5, 6, 5),
        (2, 10, 26),
        (F(783, 6400), F(3769, 128000), F(3333, 512000)),
    ):
        raise CertificateError("three-epoch component activity changed")
    return rows, tuple(demands)  # type: ignore[return-value]


def three_epoch_audit() -> dict[str, object]:
    if len(membership.positive_differences(THREE_EPOCH_FULL_POINTS)) != 496:
        raise CertificateError("32-mark quadratic fixture is not the certified Golomb ruler")
    matrix_joint, supports = three_epoch_matrix()
    cells_joint = membership.atomic_cells(THREE_EPOCH_UNION_POINTS, THREE_EPOCH_T)
    if len(cells_joint) != 88:
        raise CertificateError("three-epoch joint cell count changed")
    component_rows, component_demands = three_epoch_component_audit(cells_joint, supports)

    points4 = THREE_EPOCH_FULL_POINTS[3:8]
    cells4 = membership.atomic_cells(points4, THREE_EPOCH_T)
    matrix4 = membership.point_m_matrix(4)
    separate4 = verify_physical_solution(
        label="three_epoch_fixture_separate_n4_physical_LP",
        width=THREE_EPOCH_T,
        points=points4,
        cells=cells4,
        matrix=matrix4,
        supports=(tuple(range(5)),),
        root_weights={(0, 2): F(1, 40), (2, 4): F(1, 40)},
        kappas=(F(0),),
        dual_weights={
            "[5025,6016)": F(3049, 10000),
            "[6036,7009)": F(8813, 30000),
            "[7049,8016)": F(2909, 10000),
            "[8036,9025)": F(9193, 30000),
        },
        expected=F(299, 2000),
    )

    points8 = THREE_EPOCH_FULL_POINTS[7:16]
    cells8 = membership.atomic_cells(points8, THREE_EPOCH_T)
    matrix8 = membership.point_m_matrix(8)
    separate8 = verify_physical_solution(
        label="three_epoch_fixture_separate_n8_physical_LP",
        width=THREE_EPOCH_T,
        points=points8,
        cells=cells8,
        matrix=matrix8,
        supports=(tuple(range(9)),),
        root_weights={(0, 2): F(1, 128), (6, 8): F(1, 128)},
        kappas=(F(0),),
        dual_weights={
            "[9081,10064)": F(2917, 8000),
            "[10100,11049)": F(3051, 8000),
            "[15225,16144)": F(2857, 8000),
            "[16196,17169)": F(3087, 8000),
        },
        expected=F(1489, 32000),
    )

    points16 = THREE_EPOCH_FULL_POINTS[15:32]
    cells16 = membership.atomic_cells(points16, THREE_EPOCH_T)
    matrix16 = membership.point_m_matrix(16)
    separate16 = verify_physical_solution(
        label="three_epoch_fixture_separate_n16_physical_LP",
        width=THREE_EPOCH_T,
        points=points16,
        cells=cells16,
        matrix=matrix16,
        supports=(tuple(range(17)),),
        root_weights={(0, 2): F(1, 512), (14, 16): F(1, 512)},
        kappas=(F(0),),
        dual_weights={
            "[17289,18256)": F(2837, 8000),
            "[18324,19225)": F(3099, 8000),
            "[31961,32784)": F(2697, 8000),
            "[32900,33841)": F(3183, 8000),
        },
        expected=F(1477, 128000),
    )

    joint_dual_weights = {
        "[5025,6016)": F(270559, 840000),
        "[6036,7009)": F(38303, 120000),
        "[7049,8016)": F(23323, 105000),
        "[8036,8064)": F(3071, 15000),
        "[9081,10036)": F(14443, 56000),
        "[10100,11049)": F(3051, 8000),
        "[15225,16144)": F(3081, 8000),
        "[16196,16256)": F(49547, 168000),
        "[18324,19225)": F(661, 2625),
        "[31961,32784)": F(3177, 8000),
        "[32900,33841)": F(2703, 8000),
    }
    joint_root_weights = {
        (0, 2): F(45, 1792),
        (2, 4): F(11, 448),
        (4, 6): F(3, 1792),
        (10, 12): F(1, 128),
        (26, 28): F(1, 512),
    }
    joint = verify_physical_solution(
        label="joint_n4_n8_n16_common_scale_physical_LP",
        width=THREE_EPOCH_T,
        points=THREE_EPOCH_UNION_POINTS,
        cells=cells_joint,
        matrix=matrix_joint,
        supports=supports,
        root_weights=joint_root_weights,
        kappas=(F(0), F(0), F(0)),
        dual_weights=joint_dual_weights,
        expected=F(163481, 896000),
    )
    if joint["costs"]["aggregate_costs"] != ["3/1", "386/125", "444/125"]:
        raise CertificateError("three-epoch aggregate physical costs changed")
    if joint["dual"]["aggregate_loads"] != ["162947/84000", "2463/2000", "171011/168000"]:
        raise CertificateError("three-epoch aggregate dual loads changed")

    matrices = (matrix4, matrix8, matrix16)
    dual_shares = [F(0), F(0), F(0)]
    for cell in cells_joint:
        multiplier = joint_dual_weights.get(str(cell["id"]), F(0))
        state = tuple(int(value) for value in cell["state"])
        for k, support in enumerate(supports):
            dual_shares[k] += multiplier * membership.quadratic(
                matrices[k], tuple(state[i] for i in support)
            )
    if tuple(dual_shares) != (F(7477, 56000), F(1979, 48000), F(20723, 2688000)):
        raise CertificateError("three-epoch joint dual split changed")
    if sum(dual_shares, F(0)) != F(163481, 896000):
        raise CertificateError("three-epoch dual shares do not sum to optimum")

    # Embed all three separate optima into the union and check the strict gain.
    embedded_weights = {
        (0, 2): F(1, 40),
        (2, 4): F(1, 40),
        (4, 6): F(1, 128),
        (10, 12): F(1, 128),
        (12, 14): F(1, 512),
        (26, 28): F(1, 512),
    }
    edge_costs, _ = physical_costs(
        THREE_EPOCH_UNION_POINTS, cells_joint, supports, THREE_EPOCH_T
    )
    for cell in cells_joint:
        state = tuple(int(value) for value in cell["state"])
        lhs = sum(
            (value * (state[i] - state[j]) ** 2 for (i, j), value in embedded_weights.items()),
            F(0),
        )
        if lhs < membership.quadratic(matrix_joint, state):
            raise CertificateError("embedded three-separate correction is not jointly feasible")
    embedded_objective = sum(
        (edge_costs[edge] * value for edge, value in embedded_weights.items()), F(0)
    )
    separate_sum = F(299, 2000) + F(1489, 32000) + F(1477, 128000)
    saving = separate_sum - F(163481, 896000)
    if (embedded_objective, separate_sum, saving) != (
        F(26569, 128000),
        F(26569, 128000),
        F(11251, 448000),
    ):
        raise CertificateError("three-epoch joint/separate comparison changed")

    # The exact sparse optimum at T=2000 is not scale-universal.
    counter_cells = membership.atomic_cells(THREE_EPOCH_UNION_POINTS, THREE_EPOCH_COUNTER_T)
    counter_cell = next(
        (cell for cell in counter_cells if cell["id"] == "[6036,6516)"), None
    )
    if counter_cell is None:
        raise CertificateError("T=2500 countercheck cell disappeared")
    counter_state = tuple(int(value) for value in counter_cell["state"])
    counter_lhs = sum(
        (
            value * (counter_state[i] - counter_state[j]) ** 2
            for (i, j), value in joint_root_weights.items()
        ),
        F(0),
    )
    counter_rhs = membership.quadratic(matrix_joint, counter_state)
    counter_slack = counter_lhs - counter_rhs
    if (counter_lhs, counter_rhs, counter_slack) != (F(1, 8), F(9, 32), -F(5, 32)):
        raise CertificateError("T=2500 sparse-recurrence countercheck changed")

    total_demand = sum(component_demands, F(0))
    if total_demand != F(81049, 512000):
        raise CertificateError("three-epoch total weighted demand changed")
    if F(joint["physical_correction_surplus_over_signed_demand"]) != F(86581, 3584000):
        raise CertificateError("three-epoch joint physical surplus changed")

    return {
        "fixture": {
            "formula": "a_k=k*(k+1000), 0<=k<=31",
            "points": list(THREE_EPOCH_FULL_POINTS),
            "positive_difference_count": 496,
            "all_positive_differences_distinct": True,
            "T": THREE_EPOCH_T,
            "union_points": list(THREE_EPOCH_UNION_POINTS),
            "epochs": [
                {"n": 4, "global_mark_indices": [3, 7], "union_support": list(supports[0])},
                {"n": 8, "global_mark_indices": [7, 15], "union_support": list(supports[1])},
                {"n": 16, "global_mark_indices": [15, 31], "union_support": list(supports[2])},
            ],
            "direct_M_pair_supports_are_disjoint": True,
        },
        "separate": {
            "n4": {
                "points": list(points4),
                "complete_real_line_atomic_cell_count": len(cells4),
                "atomic_cells": base_cell_rows(cells4, matrix4, (tuple(range(5)),), THREE_EPOCH_T),
                "LP": separate4,
            },
            "n8": {
                "points": list(points8),
                "complete_real_line_atomic_cell_count": len(cells8),
                "atomic_cells": base_cell_rows(cells8, matrix8, (tuple(range(9)),), THREE_EPOCH_T),
                "LP": separate8,
            },
            "n16": {
                "points": list(points16),
                "complete_real_line_atomic_cell_count": len(cells16),
                "atomic_cells": base_cell_rows(cells16, matrix16, (tuple(range(17)),), THREE_EPOCH_T),
                "LP": separate16,
            },
            "sum_of_separate_optima": ftext(separate_sum),
        },
        "joint": {
            "complete_real_line_atomic_cell_count": len(cells_joint),
            "atomic_cells": base_cell_rows(cells_joint, matrix_joint, supports, THREE_EPOCH_T),
            "per_epoch_cell_demands": component_rows,
            "per_epoch_weighted_signed_demands": {
                "n4": ftext(component_demands[0]),
                "n8": ftext(component_demands[1]),
                "n16": ftext(component_demands[2]),
                "total": ftext(total_demand),
            },
            "dual_objective_epoch_split": {
                "n4": ftext(dual_shares[0]),
                "n8": ftext(dual_shares[1]),
                "n16": ftext(dual_shares[2]),
                "all_strictly_positive": True,
            },
            "LP": joint,
            "budget_owner_supplied": False,
        },
        "joint_vs_separate": {
            "embedded_separate_root_weights": {
                f"{i},{j}": ftext(value) for (i, j), value in sorted(embedded_weights.items())
            },
            "embedded_separate_is_jointly_feasible": True,
            "sum_of_separate_optima": ftext(separate_sum),
            "joint_optimum": joint["optimal_value"],
            "joint_strictly_less_than_sum_of_three_separate_optima": True,
            "exact_joint_saving": ftext(saving),
        },
        "same_sparse_weights_T2500_countercheck": {
            "T": THREE_EPOCH_COUNTER_T,
            "cell": counter_cell["id"],
            "state": list(counter_state),
            "lhs_correction": ftext(counter_lhs),
            "rhs_direct_M_demand": ftext(counter_rhs),
            "slack": ftext(counter_slack),
            "same_T2000_sparse_correction_is_feasible_at_T2500": False,
            "scope": "refutes only reuse of these fixed sparse weights at T=2500; it does not refute a different correction or a scale-dependent recurrence",
        },
    }


def payload_hash(certificate: Mapping[str, object]) -> str:
    payload = {key: value for key, value in certificate.items() if key != "integrity"}
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def rendered_bytes(certificate: Mapping[str, object]) -> bytes:
    return (json.dumps(certificate, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def build_certificate() -> dict[str, object]:
    n4, n8, joint = fixture_audits()
    comparison = verify_embedded_separate_primal(joint)
    three_epoch = three_epoch_audit()
    certificate: dict[str, object] = {
        "schema": SCHEMA,
        "status": STATUS,
        "scope": {
            "proved": [
                "the exact piecewise physical Haar root cost",
                "exact physical-objective primal-dual optima in the root-SDDM-plus-J class for the stated n=4 and n=8 fixtures at T=200 and mu=1",
                "an exact joint optimum and strict saving for the stated consecutive n=4/n=8 common-scale fixture",
                "exact separate and joint n=4/n=8/n=16 physical optima and strict joint saving for the stated T=2000 fixture",
                "the fixed T=2000 sparse three-epoch weights fail on one exact cell at T=2500",
            ],
            "not_proved": [
                "a uniform theorem over arbitrary Golomb/Sidon fixtures",
                "a simultaneous correction over all scales, phases, or epochs",
                "a scale-universal recurrence for the sparse roots found at T=2000",
                "payment by an already-owned Gothic, birth, cross-scale, phase, or external reserve budget",
                "optimality among arbitrary PSD, indefinite, signed, or nonlinear repairs outside the stated root-SDDM-plus-J LP",
                "C058, Q1, Q2, or Erdos Problem 1191",
                "publication novelty or prize eligibility",
            ],
        },
        "objective": {
            "formula": "sum_c |cell|/(2T) * [v_c^T C v_c + sum_s kappa_s*s_(c,s)^2]",
            "physical_meaning": "2T times the integrated Haar correction energy",
            "not_the_coefficient_trace_objective": True,
        },
        "root_cost_theorem": root_cost_audit(),
        "separate_n4": n4,
        "separate_n8": n8,
        "joint_n4_n8": joint,
        "joint_vs_separate": comparison,
        "three_epoch_n4_n8_n16": three_epoch,
    }
    certificate["integrity"] = {"payload_sha256": payload_hash(certificate), "canonical_json": True}
    return certificate


def _validate_against(
    certificate: Mapping[str, object], expected: Mapping[str, object]
) -> None:
    if certificate.get("schema") != SCHEMA or certificate.get("status") != STATUS:
        raise CertificateError("schema or status mismatch")
    if certificate.get("integrity", {}).get("payload_sha256") != payload_hash(certificate):
        raise CertificateError("payload hash mismatch")
    if certificate != expected:
        raise CertificateError("semantic replay mismatch")


def validate_certificate(certificate: Mapping[str, object]) -> None:
    _validate_against(certificate, build_certificate())


def rehash(certificate: dict[str, object]) -> None:
    certificate.setdefault("integrity", {})["payload_sha256"] = payload_hash(certificate)


def self_check(certificate: Mapping[str, object]) -> int:
    expected = build_certificate()
    _validate_against(certificate, expected)
    mutations: list[dict[str, object]] = []

    changed = copy.deepcopy(certificate)
    changed["status"] = "PRIZE_READY"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["scope"]["not_proved"] = []
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["root_cost_theorem"]["piecewise_root_cost"] = "chi=2"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["separate_n4"]["LP"]["optimal_value"] = "1/10"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["separate_n4"]["LP"]["costs"]["aggregate_costs"] = ["2/1"]
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["separate_n8"]["LP"]["dual"]["cell_weights"]["[981,1064)"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["joint_n4_n8"]["LP"]["primal"]["root_weights"]["4,6"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["joint_n4_n8"]["budget_owner_supplied"] = True
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["joint_vs_separate"]["exact_joint_saving"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["objective"]["not_the_coefficient_trace_objective"] = False
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["joint_n4_n8"]["complete_real_line_atomic_cell_count"] = 39
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["three_epoch_n4_n8_n16"]["joint"]["LP"]["optimal_value"] = "1/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["three_epoch_n4_n8_n16"]["joint_vs_separate"]["exact_joint_saving"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["three_epoch_n4_n8_n16"]["same_sparse_weights_T2500_countercheck"]["slack"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["three_epoch_n4_n8_n16"]["fixture"]["positive_difference_count"] = 495
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["integrity"]["payload_sha256"] = "0" * 64
    mutations.append(changed)

    rejected = 0
    for mutation in mutations:
        try:
            _validate_against(mutation, expected)
        except (CertificateError, membership.CertificateError):
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
        _validate_against(loaded, certificate)
        if raw != rendered_bytes(certificate):
            raise CertificateError("literal raw-byte replay mismatch")
    if args.self_check:
        self_check(certificate)
    if not args.verify:
        args.output.write_bytes(rendered_bytes(certificate))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
