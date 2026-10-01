#!/usr/bin/env python3
"""Independent exact oracle for the scratch C136 joint-master certificate.

This verifier is intentionally stdlib-only.  It imports neither
``ROUTE_C_C136_JOINT_GRAPH_MASTER_certificate.py`` nor any other canonical
Erdős-1191 module.  Its only input is the JSON certificate.  From frozen
mathematical definitions it rebuilds

* the common phase, 100 Haar channels, 150 events, and 149 active cells;
* the full M8/M16 direct-owner problem and all 1,192 exact inequalities;
* the JSON graph support, its Laplacian Gram form, rank, price, and margin;
* the complete 63-source cross-half residual identity;
* rank-15 ownership and the three-fibre energy partition; and
* the same-fixture/phase box-carrier C133 identity on all 191 carrier cells,
  including all fourteen rows and all unique pair births; and
* an exact countercell separating that carrier from the direct M8/M16 demand.

The graph feasibility and the box-carrier ledger are separate verified finite
facts.  The carrier is not the potential generating the direct demand, the
graph has no multiplier-16 terminal channel, and no charge identity is proved.
Thus full fourteen-row payment remains UNKNOWN and C058 remains open.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import re
from typing import Any, Iterable, Mapping, Sequence


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_C136_JOINT_GRAPH_MASTER_certificate.json"

SCHEMA = "erdos1191.c136.joint_epoch8_16_single_phase_graph_master_unlinked_carrier.v1"
STATUS = (
    "EXACT_SINGLE_PHASE_DIRECT_OWNER_GRAPH_FEASIBLE_"
    "C133_FIXTURE_PHASE_BOX_CARRIER_INSTANTIATED_"
    "UNLINKED_PAYMENT_UNKNOWN_C058_OPEN"
)
OVERALL = "UNKNOWN_UNLINKED_GRAPH_PRICE_TO_C133_PAYMENT"

POINTS = (
    0, 22, 60, 83, 102, 173, 303, 513,
    616, 727, 772, 881, 972, 1041, 1103, 1169,
    1239, 1349, 1539, 1654, 2009, 2659, 3709, 3804,
    4114, 4339, 4794, 5124, 5639, 6184, 6739, 7084,
)
MULTIPLIERS = (1, 2, 4, 8)
PHASE_LOWER = Q(5915, 16)
PHASE_UPPER = Q(5915, 8)
PHASE = Q(17745, 32)
WEIGHTS = {8: Q(1), 16: Q(9, 16)}
ACTIVE_COEFFICIENTS = {scale: Q(2**scale, 128) for scale in range(4)}

# The ordering is reconstructed independently and is used only internally.
# Certificate support endpoints are semantic (rank,multiplier) labels.
CHANNELS = tuple(
    (rank, multiplier, POINTS[rank])
    for multiplier in MULTIPLIERS
    for rank in range(7, 32)
)
CHANNEL_INDEX = {
    (rank, multiplier): index
    for index, (rank, multiplier, _origin) in enumerate(CHANNELS)
}
DIRECT_OWNERS = tuple(
    (epoch, multiplier)
    for multiplier in MULTIPLIERS
    for epoch in (8, 16)
)

EXPECTED_SCOPE = {
    "single_explicit_32_mark_fixture_only": True,
    "single_common_physical_phase_midpoint_only": True,
    "fresh_global_graph_root_capacity_not_C130_C131_paste": True,
    "exact_direct_owner_graph_subcone_feasible": True,
    "full_ranks15_through31_present": True,
    "full_M16_with_all_63_cross_half_sources_present": True,
    "rank15_owned_once_by_epoch8": True,
    "C133_all_14_same_fixture_phase_box_carrier_rows_instantiated": True,
    "C133_initial_shared_final_terminal_rows_retained": True,
    "C133_unique_pair_birth_decomposition_checked": True,
    "direct_demand_box_carrier_unlink_counterexample_checked": True,
    "box_carrier_is_direct_M8_M16_demand_potential": False,
    "scale4_multiplier16_terminal_channel_present": False,
    "C133_all_14_box_carrier_rows_paid_by_graph_master": False,
    "graph_price_to_C133_box_carrier_row_charge_identity_proved": False,
    "phase_interval_feasible": False,
    "phase_integrated_master_constructed": False,
    "nonanticipating_phase_rule_proved": False,
    "global_C103_owner_boundary_ledger_constructed": False,
    "arbitrary_history_proved": False,
    "arbitrary_rank_proved": False,
    "full_joint_problem_infeasible": False,
    "C058_Q1_Q2_proved": False,
    "publication_novelty_or_prize_claimed": False,
}


class OracleFailure(RuntimeError):
    """Raised when any exact replay gate fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OracleFailure(message)


def ratio(value: Q | int) -> str:
    value = Q(value)
    return f"{value.numerator}/{value.denominator}"


def parse_ratio(value: object, label: str) -> Q:
    require(type(value) is str, f"{label}: rational is not a string")
    require(re.fullmatch(r"-?[0-9]+/[1-9][0-9]*", value) is not None,
            f"{label}: rational is not canonical n/d text")
    numerator, denominator = (int(part) for part in value.split("/"))
    result = Q(numerator, denominator)
    require(value == ratio(result), f"{label}: rational is not reduced/canonical")
    return result


def canonical_hash(value: object) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def dictionary(value: object, label: str) -> dict[str, Any]:
    require(type(value) is dict, f"{label}: expected dictionary")
    return value


def exact_fields(stored: Mapping[str, object], expected: Mapping[str, object], label: str) -> None:
    """Check an exact set of scalar/structural fields."""
    for key, value in expected.items():
        require(key in stored, f"{label}: missing {key}")
        require(stored[key] == value, f"{label}: bad {key}: {stored[key]!r} != {value!r}")


def load_and_authenticate(path: Path) -> dict[str, Any]:
    try:
        cert = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise OracleFailure(f"cannot load certificate: {exc}") from exc
    cert = dictionary(cert, "certificate")
    expected_top = {
        "C133_same_fixture_phase_box_carrier_14_row_contract",
        "direct_owner_graph_master",
        "direct_demand_vs_box_carrier_unlink_gate",
        "fixture",
        "full_M16_residual_gate",
        "integrity",
        "missing_link",
        "overall_full_14_row_joint_classification",
        "schema",
        "scope",
        "solver_role",
        "status",
    }
    require(set(cert) == expected_top, "unexpected or missing top-level key")
    integrity = dictionary(cert["integrity"], "integrity")
    require(set(integrity) == {"payload_sha256"}, "integrity shape")
    payload = {key: value for key, value in cert.items() if key != "integrity"}
    require(
        integrity["payload_sha256"] == canonical_hash(payload),
        "payload SHA-256 mismatch",
    )
    require(cert["schema"] == SCHEMA, "schema mismatch")
    require(cert["status"] == STATUS, "status mismatch")
    require(cert["overall_full_14_row_joint_classification"] == OVERALL,
            "overall classification was upgraded")
    require(type(cert["missing_link"]) is str and len(cert["missing_link"]) > 100,
            "missing-link explanation absent")
    return cert


def audit_scope_and_solver(cert: Mapping[str, Any]) -> None:
    scope = dictionary(cert["scope"], "scope")
    require(scope == EXPECTED_SCOPE, "scope flags differ or were upgraded")
    solver = dictionary(cert["solver_role"], "solver_role")
    require(
        solver == {
            "HiGHS_status_used_only_for_discovery": True,
            "accepted_evidence_is_exact_Fraction_replay": True,
            "optimality_claimed": False,
            "optimal_inaccurate_accepted_as_evidence": False,
        },
        "solver/evidence role changed",
    )


def audit_fixture(cert: Mapping[str, Any]) -> None:
    fixture = dictionary(cert["fixture"], "fixture")
    differences = [
        POINTS[j] - POINTS[i]
        for i in range(len(POINTS))
        for j in range(i + 1, len(POINTS))
    ]
    fixture_audit = {
        "marks": 32,
        "span": 7084,
        "positive_differences": 496,
        "distinct_positive_differences": len(set(differences)),
        "Golomb_Sidon_valid": len(differences) == len(set(differences)) == 496,
    }
    require(all(left < right for left, right in zip(POINTS, POINTS[1:])),
            "fixture is not strictly increasing")
    require(fixture_audit["Golomb_Sidon_valid"], "fixture is not Golomb/Sidon-valid")
    require(
        fixture == {
            "points": list(POINTS),
            "phase_interval": [ratio(PHASE_LOWER), ratio(PHASE_UPPER)],
            "phase_midpoint": ratio(PHASE),
            "multipliers": list(MULTIPLIERS),
            "channel_rank_range": [7, 31],
            "mandatory_natural_epoch16_state_ranks": [15, 31],
            "exact_fixture_audit": fixture_audit,
        },
        "fixture or phase contract mismatch",
    )
    require(PHASE == (PHASE_LOWER + PHASE_UPPER) / 2, "phase is not midpoint")
    require(PHASE_LOWER < PHASE < PHASE_UPPER, "phase is outside interval")


def haar_sign(x: Q, origin: int, width: Q) -> int:
    displacement = x - origin
    if Q(0) <= displacement < width:
        return 1
    if width <= displacement < 2 * width:
        return -1
    return 0


def haar_state(x: Q) -> tuple[int, ...]:
    return tuple(
        (8 // multiplier) * haar_sign(x, origin, multiplier * PHASE)
        for _rank, multiplier, origin in CHANNELS
    )


def active_geometry() -> tuple[tuple[Q, ...], tuple[tuple[Q, Q, tuple[int, ...]], ...]]:
    events = tuple(sorted({
        Q(origin) + endpoint * multiplier * PHASE
        for _rank, multiplier, origin in CHANNELS
        for endpoint in (0, 1, 2)
    }))
    cells = tuple(
        (left, right, haar_state((left + right) / 2))
        for left, right in zip(events, events[1:])
    )
    require(
        (len(events), len(cells), events[0], events[-1])
        == (150, 149, Q(513), Q(31913, 2)),
        "active Haar cell geometry mismatch",
    )
    require(all(left < right for left, right, _state in cells), "degenerate active cell")
    return events, cells


def zero_matrix(size: int) -> list[list[Q]]:
    return [[Q(0) for _ in range(size)] for _ in range(size)]


def add_matrices(*matrices: Sequence[Sequence[Q]]) -> list[list[Q]]:
    require(bool(matrices), "matrix sum needs an operand")
    size = len(matrices[0])
    return [
        [sum((matrix[i][j] for matrix in matrices), Q(0)) for j in range(size)]
        for i in range(size)
    ]


def scale_matrix(scale: Q, matrix: Sequence[Sequence[Q]]) -> list[list[Q]]:
    return [[scale * value for value in row] for row in matrix]


def difference_matrix(
    left: Sequence[Sequence[Q]], right: Sequence[Sequence[Q]]
) -> list[list[Q]]:
    return add_matrices(left, scale_matrix(Q(-1), right))


def point_matrix(n: int) -> list[list[Q]]:
    """Independently form M_n = D^T B_n D on n+1 point coordinates."""
    band = [
        [
            Q(0) if i == j or abs(i - j) == 1
            else -Q((j - i) ** 2, 8 * n * n)
            for j in range(n)
        ]
        for i in range(n)
    ]
    difference = [[Q(0) for _ in range(n + 1)] for _ in range(n)]
    for i in range(n):
        difference[i][i] = Q(1)
        difference[i][i + 1] = Q(-1)
    return [
        [
            sum(
                (
                    difference[a][i] * band[a][b] * difference[b][j]
                    for a in range(n)
                    for b in range(n)
                ),
                Q(0),
            )
            for j in range(n + 1)
        ]
        for i in range(n + 1)
    ]


M8 = point_matrix(8)
M16 = point_matrix(16)


def quadratic(matrix: Sequence[Sequence[Q]], vector: Sequence[int]) -> Q:
    require(len(matrix) == len(vector), "quadratic dimension")
    return sum(
        (
            Q(vector[i]) * matrix[i][j] * vector[j]
            for i in range(len(vector))
            for j in range(len(vector))
        ),
        Q(0),
    )


def full_owner_indices(owner: tuple[int, int]) -> tuple[int, ...]:
    epoch, multiplier = owner
    ranks: Iterable[int] = range(7, 16) if epoch == 8 else range(15, 32)
    return tuple(CHANNEL_INDEX[(rank, multiplier)] for rank in ranks)


def owned_group_indices(owner: tuple[int, int]) -> frozenset[int]:
    epoch, multiplier = owner
    ranks: Iterable[int] = range(8, 16) if epoch == 8 else range(16, 32)
    return frozenset(CHANNEL_INDEX[(rank, multiplier)] for rank in ranks)


def owner_demand(owner: tuple[int, int], state: Sequence[int]) -> Q:
    epoch, multiplier = owner
    local_state = tuple(state[index] for index in full_owner_indices(owner))
    expected_length = 9 if epoch == 8 else 17
    require(len(local_state) == expected_length, "owner state lost a rank")
    matrix = M8 if epoch == 8 else M16
    return Q(multiplier, 128) * quadratic(matrix, local_state)


def coordinate_owner(rank: int) -> str:
    if rank == 7:
        return "past_epoch4"
    if 8 <= rank <= 15:
        return "epoch8"
    if 16 <= rank <= 31:
        return "epoch16"
    raise OracleFailure(f"unowned channel rank {rank}")


def read_support(graph: Mapping[str, Any]) -> tuple[tuple[int, int, Q], ...]:
    raw_support = graph.get("support")
    require(type(raw_support) is list, "support is not a list")
    support: list[tuple[int, int, Q]] = []
    seen: set[tuple[int, int]] = set()
    for number, raw in enumerate(raw_support):
        item = dictionary(raw, f"support[{number}]")
        require(
            set(item) == {"left", "right", "coefficient_y_equals_t_times_w"},
            f"support[{number}] shape",
        )
        endpoints: list[tuple[int, int]] = []
        for side in ("left", "right"):
            endpoint = item[side]
            require(
                type(endpoint) is list
                and len(endpoint) == 2
                and all(type(value) is int for value in endpoint),
                f"support[{number}] {side} label",
            )
            label = (endpoint[0], endpoint[1])
            require(label in CHANNEL_INDEX, f"support[{number}] unknown {side} channel")
            endpoints.append(label)
        i, j = (CHANNEL_INDEX[label] for label in endpoints)
        require(i != j, f"support[{number}] self root")
        if i > j:
            i, j = j, i
        require((i, j) not in seen, f"support[{number}] duplicate root")
        seen.add((i, j))
        coefficient = parse_ratio(
            item["coefficient_y_equals_t_times_w"], f"support[{number}] coefficient"
        )
        require(coefficient > 0, f"support[{number}] nonpositive coefficient")
        support.append((i, j, coefficient))
    require(len(support) == 57, "support does not have 57 positive roots")
    return tuple(support)


def graph_energy(state: Sequence[int], support: Sequence[tuple[int, int, Q]]) -> Q:
    return sum(
        (coefficient * (state[i] - state[j]) ** 2 for i, j, coefficient in support),
        Q(0),
    )


def projected_graph_share(
    state: Sequence[int], group: frozenset[int], support: Sequence[tuple[int, int, Q]]
) -> Q:
    # This is q_group^T L q, the exact coordinate-row owner share.
    return sum(
        (
            coefficient
            * ((state[i] if i in group else 0) - (state[j] if j in group else 0))
            * (state[i] - state[j])
            for i, j, coefficient in support
        ),
        Q(0),
    )


def graph_component_rank(
    size: int, support: Sequence[tuple[int, int, Q]]
) -> tuple[int, int]:
    parent = list(range(size))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(i: int, j: int) -> None:
        left, right = find(i), find(j)
        if left != right:
            parent[right] = left

    for i, j, coefficient in support:
        require(coefficient > 0, "PSD Gram root coefficient is not positive")
        union(i, j)
    components = len({find(i) for i in range(size)})
    # For a positive weighted graph Laplacian, ker L is exactly the vectors
    # constant on each connected component, hence rank = |V|-components.
    return size - components, components


def exact_support_recovery(
    cells: Sequence[tuple[Q, Q, tuple[int, ...]]],
    support: Sequence[tuple[int, int, Q]],
) -> dict[str, Any]:
    """Independently recover all 57 support weights from tight owner rows.

    The modular elimination selects rows without consulting the stored row-key
    list.  Full rank modulo 1,000,003 proves full rank over Q; a second exact
    Gauss-Jordan solve checks the unique rational solution itself.
    """
    prime = 1_000_003
    modular_basis: dict[int, list[int]] = {}
    selected: list[tuple[list[int], Q, tuple[int, int, int]]] = []
    stored_coefficients = tuple(coefficient for _i, _j, coefficient in support)

    for cell_index, (_left, _right, state) in enumerate(cells):
        for owner in DIRECT_OWNERS:
            group = owned_group_indices(owner)
            row = [
                ((state[i] if i in group else 0) - (state[j] if j in group else 0))
                * (state[i] - state[j])
                for i, j, _coefficient in support
            ]
            rhs = owner_demand(owner, state)
            value = sum(
                (Q(entry) * coefficient for entry, coefficient in zip(row, stored_coefficients)),
                Q(0),
            )
            if value != rhs:
                continue

            reduced = [entry % prime for entry in row]
            for pivot in sorted(modular_basis):
                factor = reduced[pivot]
                if factor:
                    basis_row = modular_basis[pivot]
                    reduced = [
                        (left - factor * right) % prime
                        for left, right in zip(reduced, basis_row)
                    ]
            pivot = next((index for index, entry in enumerate(reduced) if entry), None)
            if pivot is None:
                continue
            inverse = pow(reduced[pivot], prime - 2, prime)
            modular_basis[pivot] = [(entry * inverse) % prime for entry in reduced]
            selected.append((row, rhs, (cell_index, owner[0], owner[1])))
            if len(selected) == len(support):
                break
        if len(selected) == len(support):
            break

    require(len(selected) == len(support) == 57, "tight support subsystem size")
    require(len(modular_basis) == 57, "tight support subsystem modular rank")
    augmented = [
        [Q(entry) for entry in row] + [rhs]
        for row, rhs, _key in selected
    ]
    n = len(support)
    for column in range(n):
        pivot = next(
            (row for row in range(column, n) if augmented[row][column] != 0),
            None,
        )
        require(pivot is not None, "exact support subsystem singular over Q")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        divisor = augmented[column][column]
        augmented[column] = [entry / divisor for entry in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [
                    entry - factor * pivot_entry
                    for entry, pivot_entry in zip(augmented[row], augmented[column])
                ]
    recovered = tuple(augmented[row][-1] for row in range(n))
    require(recovered == stored_coefficients, "unique exact solution differs from support")
    require(all(coefficient > 0 for coefficient in recovered),
            "recovered support contains a nonpositive weight")
    return {
        "tight_rows_used_for_exactification": 57,
        "modular_full_rank_prime": prime,
        "modular_rank": 57,
        "unique_Fraction_Gauss_solution_matches_stored_support": True,
        "selected_row_keys_cell_epoch_multiplier": [
            list(key) for _row, _rhs, key in selected
        ],
    }


def audit_graph_master(cert: Mapping[str, Any]) -> dict[str, Any]:
    graph = dictionary(cert["direct_owner_graph_master"], "direct_owner_graph_master")
    events, cells = active_geometry()
    support = read_support(graph)

    laplacian = zero_matrix(len(CHANNELS))
    for i, j, coefficient in support:
        laplacian[i][i] += coefficient
        laplacian[j][j] += coefficient
        laplacian[i][j] -= coefficient
        laplacian[j][i] -= coefficient
    require(
        all(sum(row, Q(0)) == 0 for row in laplacian),
        "graph Laplacian lost zero row sums",
    )
    require(
        all(laplacian[i][j] == laplacian[j][i]
            for i in range(len(CHANNELS)) for j in range(len(CHANNELS))),
        "graph Laplacian is not symmetric",
    )
    graph_rank, components = graph_component_rank(len(CHANNELS), support)
    require(graph_rank == 51 and components == 49, "graph Laplacian rank/components")

    fibre_groups = {
        owner: frozenset(
            index
            for index, (rank, _multiplier, _origin) in enumerate(CHANNELS)
            if coordinate_owner(rank) == owner
        )
        for owner in ("past_epoch4", "epoch8", "epoch16")
    }
    require(
        {key: len(value) for key, value in fibre_groups.items()}
        == {"past_epoch4": 4, "epoch8": 32, "epoch16": 64},
        "coordinate-owner fibre census",
    )
    require(
        set().union(*fibre_groups.values()) == set(range(len(CHANNELS)))
        and sum(len(group) for group in fibre_groups.values()) == len(CHANNELS),
        "coordinate-owner fibres do not partition all channels",
    )
    require(coordinate_owner(15) == "epoch8", "rank 15 ownership")
    for multiplier in MULTIPLIERS:
        require(
            CHANNEL_INDEX[(15, multiplier)] in fibre_groups["epoch8"]
            and CHANNEL_INDEX[(15, multiplier)] not in fibre_groups["epoch16"],
            "rank 15 was not owned exactly once by epoch 8",
        )
    require(
        {CHANNELS[index][0] for index in full_owner_indices((16, 1))}
        == set(range(15, 32)),
        "natural epoch-16 state is missing ranks 15..31",
    )

    slacks: list[Q] = []
    demands: list[Q] = []
    capacities: list[Q] = []
    epoch_row_counts = {8: 0, 16: 0}
    integrated_demand = Q(0)
    physical_price = Q(0)
    partition_checks = 0
    for left, right, state in cells:
        cell_length = right - left
        energy = graph_energy(state, support)
        physical_price += cell_length * energy
        shares = {
            owner: projected_graph_share(state, group, support)
            for owner, group in fibre_groups.items()
        }
        require(sum(shares.values(), Q(0)) == energy,
                "owner fibres do not sum to graph energy")
        partition_checks += 1
        for owner in DIRECT_OWNERS:
            demand = owner_demand(owner, state)
            owned = projected_graph_share(state, owned_group_indices(owner), support)
            slack = owned - demand
            require(owned >= 0, f"negative owned capacity at cell {(left, right)}, {owner}")
            require(slack >= 0, f"negative direct-owner slack at cell {(left, right)}, {owner}")
            demands.append(demand)
            capacities.append(owned)
            slacks.append(slack)
            integrated_demand += cell_length * demand
            epoch_row_counts[owner[0]] += 1

    positive_slacks = [slack for slack in slacks if slack > 0]
    tight = sum(slack == 0 for slack in slacks)
    margin = 2 * integrated_demand - physical_price
    require(len(slacks) == 1192, "direct-owner row census")
    require(epoch_row_counts == {8: 596, 16: 596}, "per-epoch row census")
    require(sum(value == 0 for value in capacities) == 807, "zero capacity census")
    require(sum(value > 0 for value in capacities) == 385, "positive capacity census")
    demand_signs = [
        sum(value < 0 for value in demands),
        sum(value == 0 for value in demands),
        sum(value > 0 for value in demands),
    ]
    require(demand_signs == [40, 971, 181], "demand sign census")
    require(tight == 884 and len(positive_slacks) == 308, "tight/strict row census")
    require(min(positive_slacks) == Q(5, 36864), "minimum positive slack")
    require(integrated_demand == Q(457, 4), "integrated direct demand")
    require(physical_price == Q(1878008419901, 9402974208), "physical graph price")
    require(margin == Q(270571186627, 9402974208) and margin > 0,
            "2D-P margin")
    support_recovery = exact_support_recovery(cells, support)

    expected_graph_fields = {
        "classification": "EXACT_FEASIBLE_IN_STATED_GRAPH_ROOT_SUBCONE",
        "phase": ratio(PHASE),
        "phase_is_exact_midpoint": True,
        "channels": 100,
        "candidate_graph_roots": 4950,
        "positive_support_roots": 57,
        "graph_matrix_rank": graph_rank,
        "PSD_by_nonnegative_graph_root_sum": True,
        "zero_row_sums": True,
        "active_events": len(events),
        "active_cells": len(cells),
        "direct_owners": len(DIRECT_OWNERS),
        "direct_owner_cell_rows": len(slacks),
        "epoch8_M8_direct_rows": epoch_row_counts[8],
        "epoch16_full_M16_direct_rows": epoch_row_counts[16],
        "M8_state_dimension": 9,
        "M16_state_dimension": 17,
        "nonnegative_owned_capacity_rows": len(capacities),
        "zero_owned_capacity_rows": sum(value == 0 for value in capacities),
        "strict_positive_owned_capacity_rows": sum(value > 0 for value in capacities),
        "negative_zero_positive_demand_rows": demand_signs,
        "tight_direct_owner_rows": tight,
        "strict_direct_owner_rows": len(positive_slacks),
        "minimum_positive_direct_owner_slack": ratio(min(positive_slacks)),
        "owner_fiber_counts": {key: len(value) for key, value in fibre_groups.items()},
        "rank15_owner": "epoch8",
        "owner_partition_state_checks": partition_checks,
        "integrated_direct_demand_D": ratio(integrated_demand),
        "physical_price_P": ratio(physical_price),
        "positive_2D_minus_P_margin": ratio(margin),
        "exact_support_recovery": support_recovery,
    }
    exact_fields(graph, expected_graph_fields, "direct_owner_graph_master")
    require(set(graph) == set(expected_graph_fields) | {"support"},
            "unexpected graph-master field")
    return {
        "events": len(events),
        "cells": len(cells),
        "roots": len(support),
        "rank": graph_rank,
        "rows": len(slacks),
        "tight": tight,
        "strict": len(positive_slacks),
        "D": integrated_demand,
        "P": physical_price,
        "margin": margin,
    }


def embed_m8(offset: int) -> list[list[Q]]:
    result = zero_matrix(17)
    for i in range(9):
        for j in range(9):
            result[offset + i][offset + j] = M8[i][j]
    return result


def gap_vector(gap: int) -> list[Q]:
    vector = [Q(0) for _ in range(17)]
    vector[gap] = Q(1)
    vector[gap + 1] = Q(-1)
    return vector


def outer(left: Sequence[Q], right: Sequence[Q]) -> list[list[Q]]:
    return [[x * y for y in right] for x in left]


def residual_source(i: int, j: int) -> list[list[Q]]:
    alpha = Q((j - i) ** 2, 1024)
    left, right = gap_vector(i), gap_vector(j)
    return scale_matrix(
        -alpha / 2,
        add_matrices(outer(left, right), outer(right, left)),
    )


def audit_full_residual(cert: Mapping[str, Any]) -> dict[str, Any]:
    stored = dictionary(cert["full_M16_residual_gate"], "full_M16_residual_gate")
    sources = tuple(
        (i, j)
        for i in range(8)
        for j in range(8, 16)
        if j >= i + 2
    )
    require(len(sources) == 63 and (7, 8) not in sources, "cross-half source census")
    primitive_sum = add_matrices(*(residual_source(i, j) for i, j in sources))
    half_replacement = scale_matrix(
        Q(1, 4), add_matrices(embed_m8(0), embed_m8(8))
    )
    full_residual = difference_matrix(M16, half_replacement)
    require(primitive_sum == full_residual,
            "63-source primitive sum differs from full M16 residual")
    require(all(sum(row, Q(0)) == 0 for row in full_residual),
            "M16 residual row sums")
    require(all(full_residual[i][i] == 0 for i in range(17)),
            "M16 residual diagonal")
    unordered_nonzero = sum(
        full_residual[i][j] != 0 for i in range(17) for j in range(i + 1, 17)
    )
    require(unordered_nonzero == 80, "M16 residual nonzero census")
    mass = sum((Q((j - i) ** 2, 1024) for i, j in sources), Q(0))
    gamma8 = tuple(
        (i, j) for j in range(10, 16) for i in range(8, j - 1)
    )
    gamma16 = tuple(
        (i, j) for j in range(18, 32) for i in range(16, j - 1)
    )
    gamma8_mass = sum((Q((j - i) ** 2, 4 * 8 * 8) for i, j in gamma8), Q(0))
    gamma16_mass = sum((Q((j - i) ** 2, 4 * 16 * 16) for i, j in gamma16), Q(0))
    samples = (full_residual[0][8], full_residual[1][8], full_residual[1][9])
    require(mass == Q(4767, 1024), "cross-half alpha mass")
    require((len(gamma8), gamma8_mass) == (21, Q(329, 256)),
            "M8 primitive census/mass")
    require((len(gamma16), gamma16_mass) == (105, Q(5425, 1024)),
            "M16 primitive census/mass")
    require(samples == (-Q(1, 32), Q(15, 2048), Q(1, 1024)),
            "M16 residual sample entries")
    nonzero_values = [
        full_residual[i][j]
        for i in range(17)
        for j in range(i + 1, 17)
        if full_residual[i][j] != 0
    ]
    require(min(nonzero_values) < 0 < max(nonzero_values), "R16 is not mixed-sign")
    witnesses = [2 * full_residual[0][8], 2 * full_residual[1][8]]
    require(witnesses == [-Q(1, 16), Q(15, 1024)], "R16 exact witnesses")
    require(
        stored == {
            "M8_primitive_sources": len(gamma8),
            "M8_primitive_alpha_mass": ratio(gamma8_mass),
            "M16_primitive_sources": len(gamma16),
            "M16_primitive_alpha_mass": ratio(gamma16_mass),
            "M16_used_in_every_epoch16_direct_row": True,
            "quarter_scaled_two_M8_replacement_used": False,
            "cross_half_source_count": 63,
            "cross_half_alpha_mass": ratio(mass),
            "R16_ordered_nonzero_offdiagonal_entries": 2 * unordered_nonzero,
            "R16_unordered_nonzero_offdiagonal_entries": unordered_nonzero,
            "R16_zero_diagonal": True,
            "R16_zero_row_sums": True,
            "R16_mixed_sign": True,
            "R16_indefinite_exact_witness_values": [ratio(value) for value in witnesses],
            "R16_signed_residual_not_used_as_PSD_capacity": True,
            "sample_R16_entries": [ratio(value) for value in samples],
        },
        "stored full-M16 residual gate mismatch",
    )
    return {"sources": len(sources), "mass": mass, "nonzero_pairs": unordered_nonzero}


def carrier_density(prefix: int, scale: int, x: Q) -> Q:
    width = (2**scale) * PHASE
    active = sum(
        Q(point) <= x < Q(point) + width
        for point in POINTS[:prefix]
    )
    return Q(active * active - active) / (width * width)


def carrier_integral(prefix: int, scale: int) -> Q:
    width = (2**scale) * PHASE
    overlap = Q(0)
    for i in range(prefix):
        for j in range(i + 1, prefix):
            gap = POINTS[j] - POINTS[i]
            if gap < width:
                overlap += 2 * (width - gap) / (width * width)
    return overlap


def c133_rows(carriers: Mapping[tuple[int, int], Q]) -> tuple[Q, dict[str, Q]]:
    prefix_coefficients: dict[int, Q] = {}
    running = Q(0)
    for scale in range(4):
        running += ACTIVE_COEFFICIENTS[scale]
        prefix_coefficients[scale] = running

    rows: dict[str, Q] = {}
    for scale in range(4):
        coefficient = prefix_coefficients[scale]
        o8 = carriers[(8, scale)] - carriers[(8, scale + 1)]
        o16 = carriers[(16, scale)] - carriers[(16, scale + 1)]
        o32 = carriers[(32, scale)] - carriers[(32, scale + 1)]
        rows[f"band:A8:s{scale}"] = -WEIGHTS[8] * coefficient * o8
        rows[f"band:A16:s{scale}"] = (
            WEIGHTS[8] * coefficient - WEIGHTS[16] * coefficient
        ) * o16
        rows[f"band:A32:s{scale}"] = WEIGHTS[16] * coefficient * o32
    rows["terminal:e8:s4"] = (
        WEIGHTS[8]
        * prefix_coefficients[3]
        * (carriers[(16, 4)] - carriers[(8, 4)])
    )
    rows["terminal:e16:s4"] = (
        WEIGHTS[16]
        * prefix_coefficients[3]
        * (carriers[(32, 4)] - carriers[(16, 4)])
    )

    lhs = sum(
        (
            WEIGHTS[8]
            * ACTIVE_COEFFICIENTS[scale]
            * (carriers[(16, scale)] - carriers[(8, scale)])
            + WEIGHTS[16]
            * ACTIVE_COEFFICIENTS[scale]
            * (carriers[(32, scale)] - carriers[(16, scale)])
            for scale in range(4)
        ),
        Q(0),
    )
    require(len(rows) == 14, "C133 row-key census")
    require(lhs == sum(rows.values(), Q(0)), "C133 fourteen-row Abel identity")
    return lhs, rows


def audit_c133_box_carrier_ledger(cert: Mapping[str, Any]) -> dict[str, Any]:
    stored = dictionary(
        cert["C133_same_fixture_phase_box_carrier_14_row_contract"],
        "C133_same_fixture_phase_box_carrier_14_row_contract",
    )
    events = tuple(sorted({
        Q(point) + endpoint * (2**scale) * PHASE
        for point in POINTS
        for scale in range(5)
        for endpoint in (0, 1)
    }))
    cells = tuple(zip(events, events[1:]))
    require(
        (len(events), len(cells), events[0], events[-1])
        == (192, 191, Q(0), Q(31913, 2)),
        "C133 carrier-cell geometry",
    )

    integrated_lhs = Q(0)
    integrated_rows: dict[str, Q] = {}
    pointwise_checks = 0
    birth_checks = 0
    for left, right in cells:
        midpoint = (left + right) / 2
        carriers = {
            (prefix, scale): carrier_density(prefix, scale, midpoint)
            for prefix in (8, 16, 32)
            for scale in range(5)
        }
        lhs, rows = c133_rows(carriers)
        length = right - left
        integrated_lhs += length * lhs
        for key, value in rows.items():
            integrated_rows[key] = integrated_rows.get(key, Q(0)) + length * value
        pointwise_checks += 1

        # A_P density counts ordered pairs.  When a prefix grows, every pair
        # is charged exactly once to the epoch containing its larger index.
        for prefix, old_prefix in ((16, 8), (32, 16)):
            for scale in range(5):
                width = (2**scale) * PHASE
                born_density = Q(0)
                for i in range(prefix):
                    for j in range(max(i + 1, old_prefix), prefix):
                        active_i = int(Q(POINTS[i]) <= midpoint < Q(POINTS[i]) + width)
                        active_j = int(Q(POINTS[j]) <= midpoint < Q(POINTS[j]) + width)
                        born_density += Q(2 * active_i * active_j) / (width * width)
                require(
                    carriers[(prefix, scale)] - carriers[(old_prefix, scale)]
                    == born_density,
                    "unique pair-birth decomposition",
                )
                birth_checks += 1

    scalar_carriers = {
        (prefix, scale): carrier_integral(prefix, scale)
        for prefix in (8, 16, 32)
        for scale in range(5)
    }
    scalar_lhs, scalar_rows = c133_rows(scalar_carriers)
    require(integrated_lhs == scalar_lhs, "pointwise/scalar C133 LHS mismatch")
    require(integrated_rows == scalar_rows, "pointwise/scalar C133 rows mismatch")
    require(scalar_lhs == Q(10229179, 1007632080), "C133 integrated scalar")
    require(all(value != 0 for value in scalar_rows.values()),
            "a retained C133 integrated row vanished")

    epoch8_pair_atoms = 16 * 15 // 2 - 8 * 7 // 2
    epoch16_pair_atoms = 32 * 31 // 2 - 16 * 15 // 2
    require((epoch8_pair_atoms, epoch16_pair_atoms) == (92, 376),
            "pair-birth atom census")
    row_owners = {
        **{f"band:A8:s{scale}": "past_epoch4" for scale in range(4)},
        **{f"band:A16:s{scale}": "epoch8" for scale in range(4)},
        **{f"band:A32:s{scale}": "epoch16" for scale in range(4)},
        "terminal:e8:s4": "epoch8",
        "terminal:e16:s4": "epoch16",
    }
    expected_stored = {
        "classification": "EXACT_SAME_FIXTURE_PHASE_BOX_CARRIER_INSTANTIATION_UNLINKED_TO_DIRECT_DEMAND",
        "same_phase_as_graph_master": ratio(PHASE),
        "weights": {"w8": ratio(WEIGHTS[8]), "w16": ratio(WEIGHTS[16])},
        "active_coefficients": {
            f"c_s{scale}": ratio(value)
            for scale, value in ACTIVE_COEFFICIENTS.items()
        },
        "carrier_events_including_scale4_terminal": len(events),
        "carrier_cells": len(cells),
        "pointwise_14_row_identities_checked": pointwise_checks,
        "unique_pair_birth_checks": birth_checks,
        "epoch8_new_pair_atoms": epoch8_pair_atoms,
        "epoch16_new_pair_atoms": epoch16_pair_atoms,
        "raw_separate_occurrences": 18,
        "unique_stitched_keys": 14,
        "shared_A16_premerge_multiplicity": [2, 2, 2, 2],
        "shared_A16_postmerge_multiplicity": [1, 1, 1, 1],
        "initial_rows": 4,
        "shared_rows": 4,
        "final_rows": 4,
        "upper_terminal_rows": 2,
        "all_14_integrated_rows_nonzero": True,
        "integrated_lhs_equals_rhs": ratio(scalar_lhs),
        "integrated_rows": {key: ratio(value) for key, value in scalar_rows.items()},
        "row_owners": row_owners,
    }
    require(stored == expected_stored, "stored C133 fourteen-row ledger mismatch")
    require(birth_checks == 1910, "unique pair-birth check census")
    return {
        "events": len(events),
        "cells": len(cells),
        "pointwise": pointwise_checks,
        "birth_checks": birth_checks,
        "rows": len(scalar_rows),
        "lhs": scalar_lhs,
        "integrated_rows": scalar_rows,
    }


def audit_direct_demand_carrier_unlink(
    cert: Mapping[str, Any], ledger_result: Mapping[str, Any]
) -> dict[str, Any]:
    """Recompute the exact cell proving the two finite layers are unlinked."""
    stored = dictionary(
        cert["direct_demand_vs_box_carrier_unlink_gate"],
        "direct_demand_vs_box_carrier_unlink_gate",
    )
    left, right = Q(44701, 4), Q(46081, 4)
    midpoint = (left + right) / 2
    graph_events, _graph_cells = active_geometry()
    carrier_events = tuple(sorted({
        Q(point) + endpoint * (2**scale) * PHASE
        for point in POINTS
        for scale in range(5)
        for endpoint in (0, 1)
    }))

    def consecutive(events: Sequence[Q]) -> bool:
        try:
            index = events.index(left)
        except ValueError:
            return False
        return index + 1 < len(events) and events[index + 1] == right

    joint_events = tuple(sorted(set(graph_events) | set(carrier_events)))
    require(consecutive(graph_events), "countercell is not one graph Haar cell")
    require(consecutive(carrier_events), "countercell is not one box-carrier cell")
    require(consecutive(joint_events), "countercell is not one joint endpoint cell")
    require(midpoint == Q(45391, 4), "countercell midpoint")

    carriers = {
        (prefix, scale): carrier_density(prefix, scale, midpoint)
        for prefix in (8, 16, 32)
        for scale in range(5)
    }
    carrier_lhs, carrier_rows = c133_rows(carriers)
    nonzero_carrier_rows = {
        key: value for key, value in carrier_rows.items() if value != 0
    }
    require(carrier_lhs == 0, "countercell box-carrier LHS is nonzero")
    require(
        nonzero_carrier_rows == {
            "band:A32:s3": -Q(33, 358269184),
            "terminal:e16:s4": Q(33, 358269184),
        },
        "countercell nonzero carrier rows",
    )
    require(sum(nonzero_carrier_rows.values(), Q(0)) == 0,
            "countercell carrier rows do not cancel")

    state = haar_state(midpoint)
    components = {
        owner: owner_demand(owner, state) for owner in DIRECT_OWNERS
    }
    nonzero_components = {
        owner: value for owner, value in components.items() if value != 0
    }
    require(nonzero_components == {(16, 8): Q(25, 2048)},
            "countercell direct-demand component census")
    weighted_direct = sum(
        (WEIGHTS[epoch] * value for (epoch, _multiplier), value in components.items()),
        Q(0),
    )
    require(weighted_direct == Q(225, 32768), "countercell weighted direct demand")
    require(weighted_direct != carrier_lhs,
            "countercell failed to separate direct demand and carrier")

    integrated_rows = ledger_result["integrated_rows"]
    terminal_values_exact = [
        integrated_rows["terminal:e8:s4"],
        integrated_rows["terminal:e16:s4"],
    ]
    require(
        terminal_values_exact == [Q(253807, 111959120), Q(6604809, 1791345920)]
        and all(value != 0 for value in terminal_values_exact),
        "integrated upper-terminal values",
    )
    terminal_values = [ratio(value) for value in terminal_values_exact]
    require(16 not in MULTIPLIERS and set(MULTIPLIERS) == {1, 2, 4, 8},
            "graph unexpectedly has multiplier-16 terminal channel")
    require(ledger_result["rows"] == 14, "box-carrier ledger missing rows")
    expected = {
        "classification": "EXACT_COUNTEREXAMPLE_TO_IDENTIFYING_BOX_CARRIER_WITH_DIRECT_DEMAND_POTENTIAL",
        "joint_endpoint_cell": [ratio(left), ratio(right)],
        "midpoint": ratio(midpoint),
        "box_carrier_C133_lhs_density": ratio(carrier_lhs),
        "weighted_direct_M8_M16_demand_density": ratio(weighted_direct),
        "only_nonzero_direct_component": {
            "owner": [16, 8],
            "unweighted_demand": ratio(components[(16, 8)]),
            "weight": ratio(WEIGHTS[16]),
        },
        "nonzero_box_carrier_rows_cancel_on_cell": {
            key: ratio(value) for key, value in nonzero_carrier_rows.items()
        },
        "graph_multipliers": list(MULTIPLIERS),
        "scale4_multiplier16_terminal_channel_present": False,
        "nonzero_integrated_upper_terminal_values": terminal_values,
        "box_carrier_is_direct_demand_potential": False,
    }
    require(stored == expected, "stored direct-demand/box-carrier unlink gate mismatch")
    return {
        "left": left,
        "right": right,
        "midpoint": midpoint,
        "carrier_lhs": carrier_lhs,
        "weighted_direct": weighted_direct,
        "only_direct": nonzero_components,
    }


def audit(path: Path) -> dict[str, Any]:
    cert = load_and_authenticate(path)
    audit_scope_and_solver(cert)
    audit_fixture(cert)
    graph = audit_graph_master(cert)
    residual = audit_full_residual(cert)
    c133 = audit_c133_box_carrier_ledger(cert)
    unlink = audit_direct_demand_carrier_unlink(cert, c133)
    return {"graph": graph, "residual": residual, "c133": c133, "unlink": unlink}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate_path", nargs="?", type=Path)
    parser.add_argument("--certificate", dest="certificate_option", type=Path)
    args = parser.parse_args()
    require(
        args.certificate_path is None or args.certificate_option is None,
        "pass the certificate either positionally or with --certificate, not both",
    )
    certificate_path = args.certificate_option or args.certificate_path or DEFAULT_CERTIFICATE
    try:
        result = audit(certificate_path)
    except OracleFailure as exc:
        print(f"INDEPENDENT_C136_FAIL {exc}")
        return 1
    graph = result["graph"]
    residual = result["residual"]
    c133 = result["c133"]
    print(
        "INDEPENDENT_C136_PARTIAL_OK "
        f"phase={ratio(PHASE)} channels={len(CHANNELS)} roots={graph['roots']} "
        f"graph_rank={graph['rank']} owner_rows={graph['rows']} tight={graph['tight']} "
        f"margin={ratio(graph['margin'])} residual_sources={residual['sources']} "
        f"C133_box_rows={c133['rows']} pointwise={c133['pointwise']} "
        f"countercell_direct={ratio(result['unlink']['weighted_direct'])} "
        "full14=UNKNOWN C058_open"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
