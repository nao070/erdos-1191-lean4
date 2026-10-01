#!/usr/bin/env python3
"""Exact consecutive-epoch physical-cover transfer certificate.

This probe tests a narrow shared-endpoint ansatz for the direct ordered-B
repair.  It proves an exact interface-state formula, checks the natural
one-sided predecessor-root transfer on the existing 16-mark Golomb fixture,
and records the first membership-count failure at a nearby width.

All semantic arithmetic is exact ``fractions.Fraction``.  A numerical LP
solver is neither imported nor used.
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
import direct_ordered_b_interval_haar_certificate as bridge


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_PHYSICAL_COVER_TRANSFER_certificate.json"
SCHEMA = "erdos1191.route_c_physical_cover_transfer.v1"
STATUS = "EXACT_INTERFACE_TRANSFER_THRESHOLD_AND_FIXED_FIXTURE_NO_GO_ONLY"

N = 4
T_PASS = 200
T_FAIL = 250
FULL_POINTS = tuple(k * (k + 100) for k in range(16))
UNION_POINTS = FULL_POINTS[3:]
SHARED = N

FIRST_ROOT = (0, 2)
PREDECESSOR_INTERFACE_ROOT = (SHARED - 2, SHARED)
SUCCESSOR_INTERFACE_ROOT = (SHARED, SHARED + 2)
LAST_ROOT = (len(UNION_POINTS) - 3, len(UNION_POINTS) - 1)

FIRST_WEIGHT = F(1, 2 * N * N)
PREDECESSOR_WEIGHT = F(1, 2 * N * N)
SUCCESSOR_STANDARD_WEIGHT = F(1, 2 * (2 * N) ** 2)
LAST_WEIGHT = F(1, 2 * (2 * N) ** 2)


class CertificateError(RuntimeError):
    """Raised when an exact identity, fixture row, or scope gate changes."""


def ftext(value: F | int) -> str:
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def embed_matrix(
    target: list[list[F]], source: Sequence[Sequence[F | int]], offset: int
) -> None:
    for i, row in enumerate(source):
        for j, value in enumerate(row):
            target[offset + i][offset + j] += F(value)


def two_epoch_matrix(n: int) -> list[list[F]]:
    size = 3 * n + 1
    matrix = [[F(0) for _ in range(size)] for _ in range(size)]
    embed_matrix(matrix, bridge.point_m_matrix(n), 0)
    embed_matrix(matrix, bridge.point_m_matrix(2 * n), n)
    return matrix


def interface_state(n: int, positive_run: int) -> tuple[int, ...]:
    """Return 0*,(-1,-1),+1^m,0* across an n/2n interface."""
    if n < 4 or not (2 <= positive_run <= 2 * n - 3):
        raise ValueError("need n>=4 and 2<=m<=2n-3")
    vector = [0] * (3 * n + 1)
    vector[n - 1] = -1
    vector[n] = -1
    for index in range(n + 1, n + positive_run + 1):
        vector[index] = 1
    return tuple(vector)


def edge_energy(vector: Sequence[int], edge: tuple[int, int], weight: F) -> F:
    i, j = edge
    return weight * (vector[i] - vector[j]) ** 2


def physical_root_cost(distance: int | F, width: int | F) -> F:
    distance = abs(F(distance))
    width = F(width)
    if width <= 0:
        raise ValueError("width must be positive")
    if distance <= width:
        return 3 * distance / width
    if distance <= 2 * width:
        return 4 - distance / width
    return F(2)


def cell_weight(cell: Mapping[str, object], width: int) -> F:
    length = cell["length"]
    return F(0) if length == "infinite" else F(int(length), 2 * width)


def transfer_formula_audit() -> dict[str, object]:
    rows_checked = 0
    selected: dict[str, object] = {}
    for n in range(4, 17):
        combined = two_epoch_matrix(n)
        first_matrix = bridge.point_m_matrix(n)
        second_matrix = bridge.point_m_matrix(2 * n)
        first = (0, 2)
        predecessor = (n - 2, n)
        successor = (n, n + 2)
        last = (3 * n - 2, 3 * n)
        for positive_run in range(2, 2 * n - 2):
            vector = interface_state(n, positive_run)
            first_demand = bridge.quadratic(first_matrix, vector[: n + 1])
            second_demand = bridge.quadratic(second_matrix, vector[n:])
            combined_demand = bridge.quadratic(combined, vector)
            expected = F(positive_run * positive_run, 8 * n * n)
            if first_demand != 0 or second_demand != expected or combined_demand != expected:
                raise CertificateError("interface direct-M formula changed")

            first_energy = edge_energy(vector, first, F(1, 2 * n * n))
            predecessor_energy = edge_energy(
                vector, predecessor, F(1, 2 * n * n)
            )
            successor_energy = edge_energy(
                vector, successor, F(1, 8 * n * n)
            )
            last_energy = edge_energy(vector, last, F(1, 8 * n * n))
            if (
                first_energy,
                predecessor_energy,
                successor_energy,
                last_energy,
            ) != (F(0), F(1, 2 * n * n), F(1, 2 * n * n), F(0)):
                raise CertificateError("interface root-energy formula changed")

            one_sided_slack = predecessor_energy - combined_demand
            two_sided_slack = predecessor_energy + successor_energy - combined_demand
            if one_sided_slack != F(4 - positive_run**2, 8 * n * n):
                raise CertificateError("one-sided transfer slack formula changed")
            if two_sided_slack != F(8 - positive_run**2, 8 * n * n):
                raise CertificateError("two-sided transfer slack formula changed")
            rows_checked += 1

            if n == 4 and positive_run in (2, 3):
                selected[f"n4_m{positive_run}"] = {
                    "state": list(vector),
                    "first_epoch_demand": ftext(first_demand),
                    "second_epoch_demand": ftext(second_demand),
                    "combined_demand": ftext(combined_demand),
                    "first_outer_root_energy": ftext(first_energy),
                    "predecessor_interface_root_energy": ftext(predecessor_energy),
                    "successor_standard_root_energy": ftext(successor_energy),
                    "last_outer_root_energy": ftext(last_energy),
                    "one_sided_slack": ftext(one_sided_slack),
                    "two_sided_slack": ftext(two_sided_slack),
                    "minimum_extra_successor_root_weight_after_one_sided": ftext(
                        max(F(0), -one_sided_slack / 4)
                    ),
                }

    if rows_checked != 208:
        raise CertificateError("interface formula exhaustion count changed")
    if selected["n4_m2"]["one_sided_slack"] != "0/1":
        raise CertificateError("m=2 is no longer the sharp accepted row")
    if selected["n4_m3"]["one_sided_slack"] != "-5/128":
        raise CertificateError("m=3 is no longer the first one-sided failure")
    if selected["n4_m3"]["two_sided_slack"] != "-1/128":
        raise CertificateError("standard two-sided m=3 failure changed")

    return {
        "n_range_exhausted": [4, 16],
        "positive_run_range": "2<=m<=2n-3",
        "rows_checked": rows_checked,
        "state_definition": "global state is zero except v[n-1]=v[n]=-1 and v[n+1..n+m]=+1",
        "exact_direct_M_identity": "M_n(v[0..n])=0 and M_2n(v[n..3n])=m^2/(8*n^2)",
        "outer_boundary_root_energies": "both zero",
        "predecessor_interface_root_energy_at_weight_1/(2n^2)": "1/(2*n^2)",
        "successor_interface_root_energy_at_weight_1/(8n^2)": "1/(2*n^2)",
        "one_sided_slack": "(4-m^2)/(8*n^2)",
        "two_sided_standard_slack": "(8-m^2)/(8*n^2)",
        "sharp_membership_threshold": "one-sided predecessor transfer accepts m=2 exactly and first fails at m=3",
        "selected_rows": selected,
    }


def ownership_audit() -> dict[str, object]:
    rows = 0
    pair_supports = []
    for n, offset in ((N, 0), (2 * N, N)):
        local = bridge.point_m_matrix(n)
        if local != membership.point_m_matrix(n):
            raise CertificateError("direct-M implementations disagree")
        support = set()
        for p in range(n, 2 * n):
            for q in range(p, 2 * n):
                left = p - n
                right = q - n + 1
                if 2 * local[left][right] != bridge.gothic_lambda(n, p, q):
                    raise CertificateError("2M=lambda ownership row changed")
                if local[left][right] != 0:
                    support.add((offset + left, offset + right))
                rows += 1
        pair_supports.append(support)
    if rows != 46 or pair_supports[0] & pair_supports[1]:
        raise CertificateError("consecutive direct-pair ownership changed")
    if set(range(0, N + 1)) & set(range(N, 3 * N + 1)) != {N}:
        raise CertificateError("shared endpoint changed")
    return {
        "mixed_difference_rows_checked": rows,
        "literal_identity": "2*M[p-n,q-n+1]=lambda[p,q] in each epoch",
        "direct_M_pair_supports_disjoint": True,
        "blocks_share_only_union_coordinate_4_point_749": True,
        "direct_M_diagonals_zero": True,
        "gothic_rows_replaced_one_for_one": True,
        "gothic_rows_may_not_be_counted_as_additional_capacity": True,
        "shared_endpoint_diagonal_owner_created": False,
        "external_payment_owner_supplied": False,
    }


def correction_weights(kind: str) -> dict[tuple[int, int], F]:
    weights = {FIRST_ROOT: FIRST_WEIGHT, LAST_ROOT: LAST_WEIGHT}
    if kind in ("one_sided", "two_sided"):
        weights[PREDECESSOR_INTERFACE_ROOT] = PREDECESSOR_WEIGHT
    if kind == "two_sided":
        weights[SUCCESSOR_INTERFACE_ROOT] = SUCCESSOR_STANDARD_WEIGHT
    if kind not in ("boundary_only", "one_sided", "two_sided"):
        raise ValueError("unknown correction kind")
    return weights


def physical_price(
    cells: Sequence[Mapping[str, object]], width: int, weights: Mapping[tuple[int, int], F]
) -> tuple[F, F]:
    root_sum = sum(
        (
            weight * physical_root_cost(UNION_POINTS[j] - UNION_POINTS[i], width)
            for (i, j), weight in weights.items()
        ),
        F(0),
    )
    cell_sum = F(0)
    for cell in cells:
        vector = tuple(int(value) for value in cell["state"])
        energy = sum(
            (edge_energy(vector, edge, weight) for edge, weight in weights.items()),
            F(0),
        )
        cell_sum += cell_weight(cell, width) * energy
    if root_sum != cell_sum:
        raise CertificateError("root-cost and complete-cell physical prices disagree")
    return root_sum, cell_sum


def fixture_width_audit(width: int, highlighted_cell: str) -> dict[str, object]:
    combined, first_support, second_support = membership.two_epoch_matrix()
    cells = membership.atomic_cells(UNION_POINTS, width)
    if len(cells) != 40:
        raise CertificateError("complete two-epoch cell count changed")

    # The canonical cell-length dual saturates every root column exactly.
    saturation_rows = 0
    for i, j in combinations(range(len(UNION_POINTS)), 2):
        load = sum(
            (
                cell_weight(cell, width)
                * (int(cell["state"][i]) - int(cell["state"][j])) ** 2
                for cell in cells
            ),
            F(0),
        )
        cost = physical_root_cost(UNION_POINTS[j] - UNION_POINTS[i], width)
        if load != cost:
            raise CertificateError("canonical cell-length dual missed a root cost")
        saturation_rows += 1

    weighted_demand = F(0)
    row_data: dict[str, dict[str, object]] = {}
    summaries: dict[str, dict[str, object]] = {}
    for kind in ("boundary_only", "one_sided", "two_sided"):
        weights = correction_weights(kind)
        negative = 0
        tight = 0
        minimum_slack: F | None = None
        price, price_from_cells = physical_price(cells, width, weights)
        for cell in cells:
            vector = tuple(int(value) for value in cell["state"])
            first_demand = membership.quadratic(
                membership.point_m_matrix(N), vector[: N + 1]
            )
            second_demand = membership.quadratic(
                membership.point_m_matrix(2 * N), vector[N:]
            )
            demand = membership.quadratic(combined, vector)
            if demand != first_demand + second_demand:
                raise CertificateError("embedded epoch demand split changed")
            energy = sum(
                (edge_energy(vector, edge, value) for edge, value in weights.items()),
                F(0),
            )
            slack = energy - demand
            negative += slack < 0
            tight += slack == 0
            minimum_slack = slack if minimum_slack is None else min(minimum_slack, slack)
            if kind == "boundary_only":
                weighted_demand += cell_weight(cell, width) * demand
            if str(cell["id"]) == highlighted_cell:
                row_data[kind] = {
                    "correction_energy": ftext(energy),
                    "slack": ftext(slack),
                }
                row_data.setdefault("state", {})
                row_data["state"] = {
                    "id": cell["id"],
                    "length": cell["length"],
                    "vector": list(vector),
                    "first_epoch_demand": ftext(first_demand),
                    "second_epoch_demand": ftext(second_demand),
                    "combined_demand": ftext(demand),
                    "canonical_dual_weight_length_over_2T": ftext(cell_weight(cell, width)),
                    "canonical_dual_objective_contribution": ftext(
                        cell_weight(cell, width) * demand
                    ),
                }
        summaries[kind] = {
            "root_weights": {
                f"{i},{j}": ftext(value) for (i, j), value in sorted(weights.items())
            },
            "physical_price_from_root_costs": ftext(price),
            "physical_price_from_complete_cell_sum": ftext(price_from_cells),
            "negative_cell_count": negative,
            "tight_cell_count": tight,
            "minimum_slack": ftext(minimum_slack or F(0)),
            "feasible_on_all_actual_cells": negative == 0,
        }

    if saturation_rows != 78:
        raise CertificateError("canonical root-column audit count changed")
    expected = {
        T_PASS: {
            "demand": F(1429, 12800),
            "boundary_price": F(9, 80),
            "one_price": F(81, 400),
            "two_price": F(719, 3200),
            "boundary_neg": 6,
            "one_neg": 0,
            "two_neg": 0,
            "cell_state": (0, 0, 0, -1, -1, 1, 1, 0, 0, 0, 0, 0, 0),
            "cell_demand": F(1, 32),
            "boundary_slack": -F(1, 32),
            "one_slack": F(0),
        },
        T_FAIL: {
            "demand": F(2347, 16000),
            "boundary_price": F(417, 4000),
            "one_price": F(753, 4000),
            "two_price": F(21, 100),
            "boundary_neg": 14,
            "one_neg": 6,
            "two_neg": 4,
            "cell_state": (0, 0, 0, -1, -1, 1, 1, 1, 0, 0, 0, 0, 0),
            "cell_demand": F(9, 128),
            "boundary_slack": -F(9, 128),
            "one_slack": -F(5, 128),
        },
    }[width]
    state_row = row_data["state"]
    if (
        weighted_demand != expected["demand"]
        or F(summaries["boundary_only"]["physical_price_from_root_costs"])
        != expected["boundary_price"]
        or F(summaries["one_sided"]["physical_price_from_root_costs"])
        != expected["one_price"]
        or F(summaries["two_sided"]["physical_price_from_root_costs"])
        != expected["two_price"]
        or summaries["boundary_only"]["negative_cell_count"] != expected["boundary_neg"]
        or summaries["one_sided"]["negative_cell_count"] != expected["one_neg"]
        or summaries["two_sided"]["negative_cell_count"] != expected["two_neg"]
        or tuple(state_row["vector"]) != expected["cell_state"]
        or F(state_row["combined_demand"]) != expected["cell_demand"]
        or F(row_data["boundary_only"]["slack"]) != expected["boundary_slack"]
        or F(row_data["one_sided"]["slack"]) != expected["one_slack"]
    ):
        raise CertificateError("fixed transfer fixture changed")

    if width == T_PASS and not summaries["one_sided"]["feasible_on_all_actual_cells"]:
        raise CertificateError("T=200 one-sided transfer lost feasibility")
    if width == T_FAIL and summaries["one_sided"]["feasible_on_all_actual_cells"]:
        raise CertificateError("T=250 one-sided transfer no-go disappeared")

    return {
        "T": width,
        "points": list(UNION_POINTS),
        "supports": [list(first_support), list(second_support)],
        "shared_union_coordinate": SHARED,
        "shared_physical_point": UNION_POINTS[SHARED],
        "complete_real_line_atomic_cell_count": len(cells),
        "canonical_cell_length_dual": {
            "formula": "y_c=|c|/(2T) on finite cells and zero on the two exteriors",
            "root_columns_saturated": saturation_rows,
            "weighted_signed_direct_M_demand": ftext(weighted_demand),
            "lower_bound_for_every_feasible_nonnegative_root_cover": True,
        },
        "corrections": summaries,
        "highlighted_actual_cell": row_data,
    }


def physical_internal_price_audit(pass_fixture: Mapping[str, object], fail_fixture: Mapping[str, object]) -> dict[str, object]:
    pass_internal_distance = UNION_POINTS[SHARED] - UNION_POINTS[SHARED - 2]
    fail_successor_distance = UNION_POINTS[SHARED + 2] - UNION_POINTS[SHARED]
    pass_internal_cost = PREDECESSOR_WEIGHT * physical_root_cost(
        pass_internal_distance, T_PASS
    )
    minimum_extra_weight = F(5, 512)
    fail_minimum_extra_cost = minimum_extra_weight * physical_root_cost(
        fail_successor_distance, T_FAIL
    )
    if (
        pass_internal_distance,
        pass_internal_cost,
        fail_successor_distance,
        physical_root_cost(fail_successor_distance, T_FAIL),
        fail_minimum_extra_cost,
    ) != (224, F(9, 100), 232, F(348, 125), F(87, 3200)):
        raise CertificateError("physical interface-root price changed")
    if F(pass_fixture["corrections"]["one_sided"]["physical_price_from_root_costs"]) <= F(
        pass_fixture["canonical_cell_length_dual"]["weighted_signed_direct_M_demand"]
    ):
        raise CertificateError("T=200 cover no longer lies strictly above canonical demand")
    if F(fail_fixture["corrections"]["one_sided"]["physical_price_from_root_costs"]) <= F(
        fail_fixture["canonical_cell_length_dual"]["weighted_signed_direct_M_demand"]
    ):
        raise CertificateError("T=250 infeasible cover no longer exceeds total demand")
    return {
        "root_price_identity": "E_T(sum w_ij r_ij r_ij^T)=sum w_ij*chi_T(|b_i-b_j|)",
        "chi_T": "3d/T for d<=T; 4-d/T for T<=d<=2T; 2 for d>=2T",
        "strict_positivity": "chi_T(d)>0 for every distinct-point root d>0",
        "consequence": "nonnegative internal root weights cannot telescope out of physical price; eliminating their price forces their weights to vanish",
        "T200_predecessor_interface_root": {
            "distance": pass_internal_distance,
            "weight": ftext(PREDECESSOR_WEIGHT),
            "chi": ftext(physical_root_cost(pass_internal_distance, T_PASS)),
            "physical_price": ftext(pass_internal_cost),
        },
        "T250_highlighted_row_minimum_successor_add_on": {
            "distance": fail_successor_distance,
            "minimum_weight_to_repair_this_row_after_one_sided_root": ftext(
                minimum_extra_weight
            ),
            "chi": ftext(physical_root_cost(fail_successor_distance, T_FAIL)),
            "minimum_physical_price_for_this_add_on": ftext(fail_minimum_extra_cost),
            "repairs_entire_T250_fixture": False,
        },
        "canonical_dual_warning": "total physical price above weighted signed demand does not imply actual-cell feasibility",
    }


def payload_hash(certificate: Mapping[str, object]) -> str:
    payload = {key: value for key, value in certificate.items() if key != "integrity"}
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def rendered_bytes(certificate: Mapping[str, object]) -> bytes:
    return (
        json.dumps(certificate, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        + "\n"
    ).encode("utf-8")


def build_certificate() -> dict[str, object]:
    if len(membership.positive_differences(FULL_POINTS)) != 120:
        raise CertificateError("16-mark fixture is not the certified Golomb ruler")
    if UNION_POINTS != membership.TWO_EPOCH_UNION_POINTS:
        raise CertificateError("two-epoch union fixture changed")

    transfer_formula = transfer_formula_audit()
    ownership = ownership_audit()
    pass_fixture = fixture_width_audit(T_PASS, "[981,1036)")
    fail_fixture = fixture_width_audit(T_FAIL, "[1100,1114)")
    physical_price = physical_internal_price_audit(pass_fixture, fail_fixture)
    certificate: dict[str, object] = {
        "schema": SCHEMA,
        "status": STATUS,
        "scope": {
            "proved": [
                "the exact interface-state demand and transfer-slack formulas for n=4..16 and every audited membership count",
                "the natural one-sided predecessor-root transfer covers all actual T=200 cells of the stated n=4/n=8 Golomb fixture",
                "a boundary-only first/last root cover already fails on the actual T=200 m=2 interface cell",
                "the same one-sided transfer fails first at membership m=3 and the stated T=250 fixture realizes the exact deficit -5/128",
                "the canonical cell-length dual saturates every physical root column at both widths",
                "the literal 2M=lambda ownership rewrite and disjoint consecutive direct-pair supports",
            ],
            "not_proved": [
                "a no-go for arbitrary scale-adaptive weights, wider root supports, signed cross-scale corrections, or nonlinear covers",
                "a complete transfer theorem on arbitrary compatible Sidon towers",
                "a legal owner for the full correction price or its excess over the Gothic demand",
                "a continuum log-phase or exact mixed-scale energy theorem",
                "C058, Q1, Q2, Erdos Problem 1191, publication novelty, or prize eligibility",
            ],
        },
        "fixture": {
            "formula": "a_k=k*(k+100), 0<=k<=15",
            "full_points": list(FULL_POINTS),
            "positive_difference_count": 120,
            "all_positive_differences_distinct": True,
            "epochs": [
                {"n": 4, "global_mark_indices": [3, 7], "union_support": [0, 4]},
                {"n": 8, "global_mark_indices": [7, 15], "union_support": [4, 12]},
            ],
        },
        "transfer_formula": transfer_formula,
        "ownership": ownership,
        "T200_exact_pass_and_boundary_only_no_go": pass_fixture,
        "T250_exact_one_sided_transfer_no_go": fail_fixture,
        "physical_internal_price": physical_price,
        "strict_conclusion": {
            "endpoint_only_telescope": "false even at T=200 because the actual m=2 interface cell has zero first/last root energy and demand 1/32",
            "one_sided_predecessor_transfer": "fixture-feasible at T=200 but false at T=250; highlighted actual m=3 cell has slack -5/128",
            "standard_two_sided_boundary_weights": "also fail on the highlighted m=3 row with slack -1/128",
            "surviving_target": "scale-adaptive actual-cell transfer with membership-sensitive weights or wider supports, exact physical prices, explicit one-for-one 2M=lambda cancellation, and a singly owned finite-horizon ledger",
        },
    }
    certificate["integrity"] = {
        "payload_sha256": payload_hash(certificate),
        "canonical_json": True,
    }
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
    changed["transfer_formula"]["one_sided_slack"] = "0"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["transfer_formula"]["selected_rows"]["n4_m3"]["one_sided_slack"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["T200_exact_pass_and_boundary_only_no_go"]["corrections"]["one_sided"]["feasible_on_all_actual_cells"] = False
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["T250_exact_one_sided_transfer_no_go"]["corrections"]["one_sided"]["feasible_on_all_actual_cells"] = True
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["T250_exact_one_sided_transfer_no_go"]["highlighted_actual_cell"]["one_sided"]["slack"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["physical_internal_price"]["T200_predecessor_interface_root"]["physical_price"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["ownership"]["gothic_rows_replaced_one_for_one"] = False
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["ownership"]["external_payment_owner_supplied"] = True
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["fixture"]["positive_difference_count"] = 119
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["integrity"]["payload_sha256"] = "0" * 64
    mutations.append(changed)

    rejected = 0
    for mutation in mutations:
        try:
            _validate_against(mutation, expected)
        except CertificateError:
            rejected += 1
    if rejected != len(mutations):
        raise CertificateError("a semantic or integrity mutation was accepted")
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--verify", type=Path, help="verify an existing certificate")
    parser.add_argument("--self-check", action="store_true")
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
