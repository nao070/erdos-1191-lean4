#!/usr/bin/env python3
"""Exact C136 scratch certificate for a fresh 32-mark joint graph master.

The accepted result has two deliberately separated layers.

1.  At the single common physical phase t=17745/32, a fresh 57-root global
    graph-Laplacian matrix is an exact positive-semidefinite, zero-row-sum
    capacity satisfying all 1,192 direct epoch-8/16 owner-cell inequalities.
    Its exact physical margin 2D-P is positive.  The matrix is not a pasted
    C130/C131 factor.
2.  On the same fixture and phase, the complete C133 fourteen-row identity is
    instantiated pointwise for a one-sided box-pair carrier, with all
    initial/shared/final/upper-terminal rows nonzero and unique pair birth
    accounting checked.  An exact countercell proves that this carrier is not
    the potential generating the direct M8/M16 demand.

No theorem currently identifies the arbitrary graph-root price with payment
of those fourteen physical rows.  Consequently the full fourteen-row joint
payment status is UNKNOWN, not feasible or infeasible.  This file proves no
phase interval, nonanticipating rule, global C103 ledger, arbitrary rank,
C058, Q1, or Q2 statement.
"""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_C136_JOINT_GRAPH_MASTER_certificate.json"
SCHEMA = "erdos1191.c136.joint_epoch8_16_single_phase_graph_master_unlinked_carrier.v1"
STATUS = (
    "EXACT_SINGLE_PHASE_DIRECT_OWNER_GRAPH_FEASIBLE_"
    "C133_FIXTURE_PHASE_BOX_CARRIER_INSTANTIATED_UNLINKED_PAYMENT_UNKNOWN_C058_OPEN"
)

POINTS = (
    0, 22, 60, 83, 102, 173, 303, 513,
    616, 727, 772, 881, 972, 1041, 1103, 1169,
    1239, 1349, 1539, 1654, 2009, 2659, 3709, 3804,
    4114, 4339, 4794, 5124, 5639, 6184, 6739, 7084,
)
MULTIPLIERS = (1, 2, 4, 8)
PHASE_LOWER = F(5915, 16)
PHASE_UPPER = F(5915, 8)
PHASE = F(17745, 32)
WEIGHTS = {8: F(1), 16: F(9, 16)}
ACTIVE_SCALE_COEFFICIENTS = {s: F(2**s, 128) for s in range(4)}

CHANNELS = tuple(
    (rank, multiplier, POINTS[rank])
    for multiplier in MULTIPLIERS
    for rank in range(7, 32)
)
CHANNEL_INDEX = {(rank, multiplier): i for i, (rank, multiplier, _) in enumerate(CHANNELS)}
ROOTS = tuple((i, j) for i in range(len(CHANNELS)) for j in range(i + 1, len(CHANNELS)))
DIRECT_OWNERS = tuple((epoch, multiplier) for multiplier in MULTIPLIERS for epoch in (8, 16))

# Exact y=t*w graph-root coefficients recovered from the HiGHS basic support
# by a 57 by 57 rational solve.  Root labels are (rank,multiplier).
SUPPORT = (
    ((7, 1), (8, 1), F(21, 16384)),
    ((13, 1), (15, 1), F(15, 65536)),
    ((14, 1), (15, 1), F(13, 65536)),
    ((15, 1), (16, 1), F(271211, 2611937280)),
    ((16, 1), (17, 1), F(191501, 7835811840)),
    ((16, 1), (16, 2), F(24307, 7835811840)),
    ((17, 1), (18, 1), F(191501, 7835811840)),
    ((18, 1), (19, 1), F(47629, 15671623680)),
    ((18, 1), (18, 2), F(24307, 2611937280)),
    ((18, 1), (26, 4), F(14563, 5223874560)),
    ((19, 1), (24, 4), F(430631, 15671623680)),
    ((22, 1), (16, 4), F(6273709, 150447587328)),
    ((22, 1), (19, 4), F(623467, 150447587328)),
    ((23, 1), (26, 2), F(6395, 9402974208)),
    ((24, 1), (22, 2), F(89257, 12537298944)),
    ((24, 1), (25, 2), F(89257, 12537298944)),
    ((29, 1), (28, 2), F(1, 49152)),
    ((15, 2), (16, 2), F(947761, 2611937280)),
    ((16, 2), (17, 2), F(1031411, 15671623680)),
    ((16, 2), (18, 2), F(380047, 7835811840)),
    ((17, 2), (20, 2), F(24307, 1958952960)),
    ((18, 2), (19, 2), F(5, 131072)),
    ((21, 2), (26, 4), F(23519, 391790592)),
    ((22, 2), (23, 2), F(36703, 12537298944)),
    ((23, 2), (20, 4), F(307535, 9402974208)),
    ((25, 2), (20, 4), F(12497, 2089549824)),
    ((25, 2), (22, 4), F(12497, 2089549824)),
    ((26, 2), (22, 4), F(7, 196608)),
    ((28, 2), (27, 4), F(1, 24576)),
    ((29, 2), (27, 4), F(11, 98304)),
    ((30, 2), (31, 2), F(5, 131072)),
    ((31, 2), (26, 4), F(5, 294912)),
    ((15, 4), (16, 4), F(32680223, 37611896832)),
    ((16, 4), (17, 4), F(9, 65536)),
    ((16, 4), (19, 4), F(9723743, 75223793664)),
    ((16, 4), (22, 4), F(1120543, 9402974208)),
    ((16, 4), (24, 4), F(7221529, 62686494720)),
    ((16, 4), (26, 4), F(2938007, 20895498240)),
    ((18, 4), (19, 4), F(307535, 18805948416)),
    ((20, 4), (21, 4), F(39421, 1175371776)),
    ((24, 4), (31, 4), F(11047609, 62686494720)),
    ((25, 4), (31, 4), F(19937, 195895296)),
    ((26, 4), (31, 4), F(7581901, 62686494720)),
    ((27, 4), (28, 4), F(230725, 4701487104)),
    ((28, 4), (29, 4), F(33365, 146921472)),
    ((29, 4), (31, 4), F(83369, 2786066432)),
    ((30, 4), (31, 4), F(19937, 261193728)),
    ((15, 8), (16, 8), F(219, 16384)),
    ((15, 8), (17, 8), F(69, 16384)),
    ((16, 8), (18, 8), F(127, 81920)),
    ((17, 8), (18, 8), F(23, 16384)),
    ((18, 8), (21, 8), F(379, 163840)),
    ((19, 8), (20, 8), F(21, 163840)),
    ((20, 8), (21, 8), F(21, 163840)),
    ((28, 8), (29, 8), F(21, 40960)),
    ((28, 8), (30, 8), F(5, 2048)),
    ((30, 8), (31, 8), F(5, 2048)),
)


class CertificateError(RuntimeError):
    pass


def ftext(value: F | int) -> str:
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def fixture_audit() -> dict[str, Any]:
    if len(POINTS) != 32 or POINTS[0] != 0 or any(a >= b for a, b in zip(POINTS, POINTS[1:])):
        raise CertificateError("32-mark fixture ordering changed")
    differences = [POINTS[j] - POINTS[i] for i in range(32) for j in range(i + 1, 32)]
    if len(differences) != 496 or len(set(differences)) != 496:
        raise CertificateError("32-mark fixture is not Golomb/Sidon-valid")
    return {
        "marks": len(POINTS),
        "span": POINTS[-1] - POINTS[0],
        "positive_differences": len(differences),
        "distinct_positive_differences": len(set(differences)),
        "Golomb_Sidon_valid": True,
    }


def haar_sign(x: F, origin: int, width: F) -> int:
    displacement = x - origin
    return int(0 <= displacement < width) - int(width <= displacement < 2 * width)


def active_state(x: F) -> tuple[int, ...]:
    return tuple(
        (8 // multiplier) * haar_sign(x, origin, multiplier * PHASE)
        for _, multiplier, origin in CHANNELS
    )


def active_geometry() -> tuple[tuple[F, ...], tuple[tuple[F, F, tuple[int, ...]], ...]]:
    events = tuple(sorted({
        F(origin) + shift * multiplier * PHASE
        for _, multiplier, origin in CHANNELS
        for shift in (0, 1, 2)
    }))
    cells = tuple(
        (left, right, active_state((left + right) / 2))
        for left, right in zip(events, events[1:])
    )
    if (len(events), len(cells), events[0], events[-1]) != (150, 149, F(513), F(31913, 2)):
        raise CertificateError("active event/cell geometry changed")
    return events, cells


def point_matrix(n: int) -> tuple[tuple[F, ...], ...]:
    b = tuple(tuple(
        F(0) if i == j or abs(i - j) == 1 else -F((j - i) ** 2, 8 * n * n)
        for j in range(n)
    ) for i in range(n))
    d = tuple(tuple(F((k == i) - (k == i + 1)) for k in range(n + 1)) for i in range(n))
    return tuple(tuple(
        sum((d[a][i] * b[a][c] * d[c][j] for a in range(n) for c in range(n)), F(0))
        for j in range(n + 1)
    ) for i in range(n + 1))


POINT_MATRICES = {8: point_matrix(8), 16: point_matrix(16)}


def quadratic(matrix: Sequence[Sequence[F]], vector: Sequence[int]) -> F:
    return sum((
        F(vector[i]) * matrix[i][j] * vector[j]
        for i in range(len(vector))
        for j in range(len(vector))
    ), F(0))


def direct_full_indices(owner: tuple[int, int]) -> tuple[int, ...]:
    epoch, multiplier = owner
    ranks = range(7, 16) if epoch == 8 else range(15, 32)
    return tuple(CHANNEL_INDEX[rank, multiplier] for rank in ranks)


def direct_group_indices(owner: tuple[int, int]) -> tuple[int, ...]:
    epoch, multiplier = owner
    ranks = range(8, 16) if epoch == 8 else range(16, 32)
    return tuple(CHANNEL_INDEX[rank, multiplier] for rank in ranks)


def direct_demand(owner: tuple[int, int], state: Sequence[int]) -> F:
    epoch, multiplier = owner
    local = tuple(state[i] for i in direct_full_indices(owner))
    return F(multiplier, 128) * quadratic(POINT_MATRICES[epoch], local)


def support_indices() -> tuple[tuple[int, int, F], ...]:
    rows = []
    seen: set[tuple[int, int]] = set()
    for left, right, coefficient in SUPPORT:
        i, j = CHANNEL_INDEX[left], CHANNEL_INDEX[right]
        if i > j:
            i, j = j, i
        if i == j or (i, j) in seen or coefficient <= 0:
            raise CertificateError("invalid exact support root")
        seen.add((i, j))
        rows.append((i, j, coefficient))
    if len(rows) != 57:
        raise CertificateError("support size changed")
    return tuple(rows)


def graph_owner_share(
    state: Sequence[int], group: set[int], support: Sequence[tuple[int, int, F]]
) -> F:
    return sum((
        coefficient
        * ((state[i] if i in group else 0) - (state[j] if j in group else 0))
        * (state[i] - state[j])
        for i, j, coefficient in support
    ), F(0))


def graph_energy(state: Sequence[int], support: Sequence[tuple[int, int, F]]) -> F:
    return sum((coefficient * (state[i] - state[j]) ** 2 for i, j, coefficient in support), F(0))


def coordinate_owner(rank: int) -> str:
    if rank == 7:
        return "past_epoch4"
    if 8 <= rank <= 15:
        return "epoch8"
    if 16 <= rank <= 31:
        return "epoch16"
    raise CertificateError("rank outside the C133 owner union")


def graph_rank(support: Sequence[tuple[int, int, F]]) -> int:
    parent = list(range(len(CHANNELS)))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(i: int, j: int) -> None:
        a, b = find(i), find(j)
        if a != b:
            parent[b] = a

    for i, j, coefficient in support:
        if coefficient <= 0:
            raise CertificateError("nonpositive graph coefficient")
        union(i, j)
    components = len({find(i) for i in range(len(CHANNELS))})
    return len(CHANNELS) - components


def exact_support_basis_audit(
    cells: Sequence[tuple[F, F, tuple[int, ...]]],
    support: Sequence[tuple[int, int, F]],
) -> dict[str, Any]:
    """Recover the stored 57 coefficients from 57 exact tight owner rows.

    A modular rank calculation selects a nonsingular integer row subsystem.
    Full rank modulo the displayed prime implies full rank over Q.  A separate
    Fraction Gauss-Jordan solve then reconstructs every coefficient.
    """
    prime = 1_000_003
    modular_basis: dict[int, list[int]] = {}
    selected: list[tuple[list[int], F, tuple[int, int, int]]] = []
    stored = tuple(coefficient for _, _, coefficient in support)

    for cell_index, (_, _, state) in enumerate(cells):
        for owner in DIRECT_OWNERS:
            group = set(direct_group_indices(owner))
            row = [
                ((state[i] if i in group else 0) - (state[j] if j in group else 0))
                * (state[i] - state[j])
                for i, j, _ in support
            ]
            rhs = direct_demand(owner, state)
            if sum((F(value) * coefficient for value, coefficient in zip(row, stored)), F(0)) != rhs:
                continue
            reduced = [value % prime for value in row]
            for pivot in sorted(modular_basis):
                factor = reduced[pivot]
                if factor:
                    basis_row = modular_basis[pivot]
                    reduced = [(a - factor * b) % prime for a, b in zip(reduced, basis_row)]
            pivot = next((i for i, value in enumerate(reduced) if value), None)
            if pivot is None:
                continue
            inverse = pow(reduced[pivot], prime - 2, prime)
            modular_basis[pivot] = [(value * inverse) % prime for value in reduced]
            selected.append((row, rhs, (cell_index, owner[0], owner[1])))
            if len(selected) == len(support):
                break
        if len(selected) == len(support):
            break

    if len(selected) != 57 or len(modular_basis) != 57:
        raise CertificateError("57-root tight subsystem lost full rational rank")

    augmented = [[F(value) for value in row] + [rhs] for row, rhs, _ in selected]
    n = len(support)
    for column in range(n):
        pivot_row = next((row for row in range(column, n) if augmented[row][column]), None)
        if pivot_row is None:
            raise CertificateError("exact support subsystem is singular")
        augmented[column], augmented[pivot_row] = augmented[pivot_row], augmented[column]
        divisor = augmented[column][column]
        augmented[column] = [value / divisor for value in augmented[column]]
        for row in range(n):
            if row == column or augmented[row][column] == 0:
                continue
            factor = augmented[row][column]
            augmented[row] = [
                value - factor * pivot_value
                for value, pivot_value in zip(augmented[row], augmented[column])
            ]
    recovered = tuple(augmented[row][-1] for row in range(n))
    if recovered != stored or any(value <= 0 for value in recovered):
        raise CertificateError("exact support coefficient recovery changed")
    return {
        "tight_rows_used_for_exactification": len(selected),
        "modular_full_rank_prime": prime,
        "modular_rank": len(modular_basis),
        "unique_Fraction_Gauss_solution_matches_stored_support": True,
        "selected_row_keys_cell_epoch_multiplier": [list(key) for _, _, key in selected],
    }


def cross_half_residual_audit() -> dict[str, Any]:
    m8, m16 = POINT_MATRICES[8], POINT_MATRICES[16]
    halves = [[F(0) for _ in range(17)] for _ in range(17)]
    for i in range(9):
        for j in range(9):
            halves[i][j] += m8[i][j] / 4
            halves[i + 8][j + 8] += m8[i][j] / 4
    residual = tuple(tuple(m16[i][j] - halves[i][j] for j in range(17)) for i in range(17))
    sources = tuple((i, j) for i in range(8) for j in range(8, 16) if j >= i + 2)
    mass = sum((F((j - i) ** 2, 1024) for i, j in sources), F(0))
    gamma8 = tuple((i, j) for j in range(10, 16) for i in range(8, j - 1))
    gamma16 = tuple((i, j) for j in range(18, 32) for i in range(16, j - 1))
    gamma8_mass = sum((F((j - i) ** 2, 4 * 8 * 8) for i, j in gamma8), F(0))
    gamma16_mass = sum((F((j - i) ** 2, 4 * 16 * 16) for i, j in gamma16), F(0))
    ordered_nonzero_offdiagonal = sum(
        residual[i][j] != 0 for i in range(17) for j in range(17) if i != j
    )
    nonzero_values = [residual[i][j] for i in range(17) for j in range(i + 1, 17) if residual[i][j]]
    negative_witness = 2 * residual[0][8]
    positive_witness = 2 * residual[1][8]
    if (
        len(sources) != 63
        or mass != F(4767, 1024)
        or (len(gamma8), gamma8_mass) != (21, F(329, 256))
        or (len(gamma16), gamma16_mass) != (105, F(5425, 1024))
        or ordered_nonzero_offdiagonal != 160
        or len(nonzero_values) != 80
        or not (min(nonzero_values) < 0 < max(nonzero_values))
        or negative_witness != -F(1, 16)
        or positive_witness != F(15, 1024)
        or any(residual[i][i] for i in range(17))
        or residual[0][8] != -F(1, 32)
        or residual[1][8] != F(15, 2048)
        or residual[1][9] != F(1, 1024)
        or any(sum(row, F(0)) for row in residual)
    ):
        raise CertificateError("full M16 residual audit changed")
    return {
        "M8_primitive_sources": len(gamma8),
        "M8_primitive_alpha_mass": ftext(gamma8_mass),
        "M16_primitive_sources": len(gamma16),
        "M16_primitive_alpha_mass": ftext(gamma16_mass),
        "M16_used_in_every_epoch16_direct_row": True,
        "quarter_scaled_two_M8_replacement_used": False,
        "cross_half_source_count": 63,
        "cross_half_alpha_mass": ftext(mass),
        "R16_ordered_nonzero_offdiagonal_entries": ordered_nonzero_offdiagonal,
        "R16_unordered_nonzero_offdiagonal_entries": len(nonzero_values),
        "R16_zero_diagonal": True,
        "R16_zero_row_sums": True,
        "R16_mixed_sign": True,
        "R16_indefinite_exact_witness_values": [ftext(negative_witness), ftext(positive_witness)],
        "R16_signed_residual_not_used_as_PSD_capacity": True,
        "sample_R16_entries": [ftext(residual[0][8]), ftext(residual[1][8]), ftext(residual[1][9])],
    }


def exact_graph_audit() -> dict[str, Any]:
    events, cells = active_geometry()
    support = support_indices()
    slacks: list[F] = []
    demands: list[F] = []
    capacities: list[F] = []
    epoch_row_counts = {8: 0, 16: 0}
    owner_partition_checks = 0

    fiber_indices = {
        owner: {
            i for i, (rank, _, _) in enumerate(CHANNELS) if coordinate_owner(rank) == owner
        }
        for owner in ("past_epoch4", "epoch8", "epoch16")
    }
    if {owner: len(indices) for owner, indices in fiber_indices.items()} != {
        "past_epoch4": 4,
        "epoch8": 32,
        "epoch16": 64,
    }:
        raise CertificateError("C133 coordinate owner fibers changed")

    physical_price = F(0)
    integrated_demand = F(0)
    for left, right, state in cells:
        length = right - left
        energy = graph_energy(state, support)
        physical_price += length * energy
        shares = {
            owner: graph_owner_share(state, group, support)
            for owner, group in fiber_indices.items()
        }
        if sum(shares.values(), F(0)) != energy:
            raise CertificateError("coordinate owner fibers lost physical energy")
        owner_partition_checks += 1

        for owner in DIRECT_OWNERS:
            demand = direct_demand(owner, state)
            group = set(direct_group_indices(owner))
            owned = graph_owner_share(state, group, support)
            slack = owned - demand
            if owned < 0 or slack < 0:
                raise CertificateError(f"negative direct owner slack at {owner} on {(left, right)}")
            demands.append(demand)
            capacities.append(owned)
            slacks.append(slack)
            integrated_demand += length * demand
            epoch_row_counts[owner[0]] += 1

    positive_slacks = tuple(value for value in slacks if value > 0)
    if (
        len(slacks) != 1192
        or epoch_row_counts != {8: 596, 16: 596}
        or len(capacities) != 1192
        or any(value < 0 for value in capacities)
        or sum(value == 0 for value in capacities) != 807
        or sum(value > 0 for value in capacities) != 385
        or sum(value < 0 for value in demands) != 40
        or sum(value == 0 for value in demands) != 971
        or sum(value > 0 for value in demands) != 181
        or sum(value == 0 for value in slacks) != 884
        or len(positive_slacks) != 308
        or integrated_demand != F(457, 4)
        or physical_price != F(1878008419901, 9402974208)
    ):
        raise CertificateError("exact graph census/objective changed")
    margin = 2 * integrated_demand - physical_price
    if margin != F(270571186627, 9402974208) or margin <= 0:
        raise CertificateError("exact positive direct-owner margin changed")

    matrix = [[F(0) for _ in CHANNELS] for _ in CHANNELS]
    for i, j, coefficient in support:
        matrix[i][i] += coefficient
        matrix[j][j] += coefficient
        matrix[i][j] -= coefficient
        matrix[j][i] -= coefficient
    if any(sum(row, F(0)) for row in matrix):
        raise CertificateError("graph matrix lost zero row sums")
    rank = graph_rank(support)
    if rank != 51:
        raise CertificateError("graph PSD rank changed")
    support_basis = exact_support_basis_audit(cells, support)

    return {
        "classification": "EXACT_FEASIBLE_IN_STATED_GRAPH_ROOT_SUBCONE",
        "phase": ftext(PHASE),
        "phase_is_exact_midpoint": PHASE == (PHASE_LOWER + PHASE_UPPER) / 2,
        "channels": len(CHANNELS),
        "candidate_graph_roots": len(ROOTS),
        "positive_support_roots": len(support),
        "graph_matrix_rank": rank,
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
        "negative_zero_positive_demand_rows": [
            sum(value < 0 for value in demands),
            sum(value == 0 for value in demands),
            sum(value > 0 for value in demands),
        ],
        "tight_direct_owner_rows": sum(value == 0 for value in slacks),
        "strict_direct_owner_rows": len(positive_slacks),
        "minimum_positive_direct_owner_slack": ftext(min(positive_slacks)),
        "owner_fiber_counts": {owner: len(group) for owner, group in fiber_indices.items()},
        "rank15_owner": "epoch8",
        "owner_partition_state_checks": owner_partition_checks,
        "integrated_direct_demand_D": ftext(integrated_demand),
        "physical_price_P": ftext(physical_price),
        "positive_2D_minus_P_margin": ftext(margin),
        "support": [
            {
                "left": [CHANNELS[i][0], CHANNELS[i][1]],
                "right": [CHANNELS[j][0], CHANNELS[j][1]],
                "coefficient_y_equals_t_times_w": ftext(coefficient),
            }
            for i, j, coefficient in support
        ],
        "exact_support_recovery": support_basis,
    }


def prefix_carrier_integral(prefix: int, width: F) -> F:
    points = POINTS[:prefix]
    return 2 * sum((
        F(width - (points[j] - points[i]), width * width)
        for i in range(prefix)
        for j in range(i + 1, prefix)
        if points[j] - points[i] < width
    ), F(0))


def carrier_density(prefix: int, scale: int, x: F) -> F:
    width = (2**scale) * PHASE
    active = sum(int(F(point) <= x < F(point) + width) for point in POINTS[:prefix])
    return F(active * active - active, width * width)


def c133_row_values(C: Mapping[tuple[int, int], F]) -> tuple[F, dict[str, F]]:
    scale_prefix: dict[int, F] = {}
    running = F(0)
    for scale in range(4):
        running += ACTIVE_SCALE_COEFFICIENTS[scale]
        scale_prefix[scale] = running
    rows: dict[str, F] = {}
    for scale in range(4):
        o8 = C[8, scale] - C[8, scale + 1]
        o16 = C[16, scale] - C[16, scale + 1]
        o32 = C[32, scale] - C[32, scale + 1]
        rows[f"band:A8:s{scale}"] = -WEIGHTS[8] * scale_prefix[scale] * o8
        rows[f"band:A16:s{scale}"] = (
            WEIGHTS[8] * scale_prefix[scale] - WEIGHTS[16] * scale_prefix[scale]
        ) * o16
        rows[f"band:A32:s{scale}"] = WEIGHTS[16] * scale_prefix[scale] * o32
    rows["terminal:e8:s4"] = (
        WEIGHTS[8] * scale_prefix[3] * (C[16, 4] - C[8, 4])
    )
    rows["terminal:e16:s4"] = (
        WEIGHTS[16] * scale_prefix[3] * (C[32, 4] - C[16, 4])
    )
    lhs = sum((
        WEIGHTS[8] * ACTIVE_SCALE_COEFFICIENTS[scale] * (C[16, scale] - C[8, scale])
        + WEIGHTS[16] * ACTIVE_SCALE_COEFFICIENTS[scale] * (C[32, scale] - C[16, scale])
        for scale in range(4)
    ), F(0))
    if len(rows) != 14 or lhs != sum(rows.values(), F(0)):
        raise CertificateError("C133 fourteen-row identity failed")
    return lhs, rows


def c133_box_carrier_ledger_audit() -> dict[str, Any]:
    events = tuple(sorted({
        F(point) + endpoint * (2**scale) * PHASE
        for point in POINTS
        for scale in range(5)
        for endpoint in (0, 1)
    }))
    cells = tuple(zip(events, events[1:]))
    if (len(events), len(cells), events[0], events[-1]) != (192, 191, F(0), F(31913, 2)):
        raise CertificateError("C133 box-carrier geometry changed")

    integrated_rows: dict[str, F] = {}
    integrated_lhs = F(0)
    pointwise_checks = 0
    birth_checks = 0
    for left, right in cells:
        midpoint = (left + right) / 2
        C = {
            (prefix, scale): carrier_density(prefix, scale, midpoint)
            for prefix in (8, 16, 32)
            for scale in range(5)
        }
        lhs, rows = c133_row_values(C)
        length = right - left
        integrated_lhs += length * lhs
        for key, value in rows.items():
            integrated_rows[key] = integrated_rows.get(key, F(0)) + length * value
        pointwise_checks += 1

        # Unique pair-birth decomposition: delta8 contains exactly pairs not
        # both in A8; delta16 contains exactly pairs with a new rank >=16.
        for prefix, old in ((16, 8), (32, 16)):
            for scale in range(5):
                width = (2**scale) * PHASE
                direct = C[prefix, scale] - C[old, scale]
                born = F(0)
                for i in range(prefix):
                    for j in range(i + 1, prefix):
                        if j < old:
                            continue
                        gi = int(F(POINTS[i]) <= midpoint < F(POINTS[i]) + width)
                        gj = int(F(POINTS[j]) <= midpoint < F(POINTS[j]) + width)
                        born += F(2 * gi * gj, width * width)
                if direct != born:
                    raise CertificateError("box-carrier unique-birth decomposition failed")
                birth_checks += 1

    scalar_C = {
        (prefix, scale): prefix_carrier_integral(prefix, (2**scale) * PHASE)
        for prefix in (8, 16, 32)
        for scale in range(5)
    }
    scalar_lhs, scalar_rows = c133_row_values(scalar_C)
    if integrated_lhs != scalar_lhs or integrated_rows != scalar_rows:
        raise CertificateError("pointwise and pair-overlap C133 integrals differ")
    if scalar_lhs != F(10229179, 1007632080) or any(value == 0 for value in scalar_rows.values()):
        raise CertificateError("C133 box-carrier ledger values changed")

    return {
        "classification": "EXACT_SAME_FIXTURE_PHASE_BOX_CARRIER_INSTANTIATION_UNLINKED_TO_DIRECT_DEMAND",
        "same_phase_as_graph_master": ftext(PHASE),
        "weights": {"w8": ftext(WEIGHTS[8]), "w16": ftext(WEIGHTS[16])},
        "active_coefficients": {f"c_s{scale}": ftext(value) for scale, value in ACTIVE_SCALE_COEFFICIENTS.items()},
        "carrier_events_including_scale4_terminal": len(events),
        "carrier_cells": len(cells),
        "pointwise_14_row_identities_checked": pointwise_checks,
        "unique_pair_birth_checks": birth_checks,
        "epoch8_new_pair_atoms": 92,
        "epoch16_new_pair_atoms": 376,
        "raw_separate_occurrences": 18,
        "unique_stitched_keys": 14,
        "shared_A16_premerge_multiplicity": [2, 2, 2, 2],
        "shared_A16_postmerge_multiplicity": [1, 1, 1, 1],
        "initial_rows": 4,
        "shared_rows": 4,
        "final_rows": 4,
        "upper_terminal_rows": 2,
        "all_14_integrated_rows_nonzero": True,
        "integrated_lhs_equals_rhs": ftext(scalar_lhs),
        "integrated_rows": {key: ftext(value) for key, value in scalar_rows.items()},
        "row_owners": {
            **{f"band:A8:s{s}": "past_epoch4" for s in range(4)},
            **{f"band:A16:s{s}": "epoch8" for s in range(4)},
            **{f"band:A32:s{s}": "epoch16" for s in range(4)},
            "terminal:e8:s4": "epoch8",
            "terminal:e16:s4": "epoch16",
        },
    }


def direct_demand_box_carrier_unlink_audit(ledger: Mapping[str, Any]) -> dict[str, Any]:
    left, right = F(44701, 4), F(46081, 4)
    midpoint = (left + right) / 2
    graph_events, _ = active_geometry()
    carrier_events = {
        F(point) + endpoint * (2**scale) * PHASE
        for point in POINTS
        for scale in range(5)
        for endpoint in (0, 1)
    }
    joint_events = sorted(set(graph_events) | carrier_events)
    index = joint_events.index(left)
    if index + 1 >= len(joint_events) or joint_events[index + 1] != right:
        raise CertificateError("direct/carrier countercell is not a joint endpoint cell")

    C = {
        (prefix, scale): carrier_density(prefix, scale, midpoint)
        for prefix in (8, 16, 32)
        for scale in range(5)
    }
    carrier_lhs, carrier_rows = c133_row_values(C)
    state = active_state(midpoint)
    components = {
        (epoch, multiplier): direct_demand((epoch, multiplier), state)
        for epoch in (8, 16)
        for multiplier in MULTIPLIERS
    }
    weighted_direct = sum((
        WEIGHTS[epoch] * components[epoch, multiplier]
        for epoch in (8, 16)
        for multiplier in MULTIPLIERS
    ), F(0))
    nonzero_components = {key: value for key, value in components.items() if value}
    nonzero_carrier_rows = {key: value for key, value in carrier_rows.items() if value}
    integrated_rows = ledger.get("integrated_rows")
    if not isinstance(integrated_rows, Mapping):
        raise CertificateError("box-carrier integrated rows missing")
    terminal_values = [integrated_rows.get("terminal:e8:s4"), integrated_rows.get("terminal:e16:s4")]
    if (
        midpoint != F(45391, 4)
        or carrier_lhs != 0
        or weighted_direct != F(225, 32768)
        or nonzero_components != {(16, 8): F(25, 2048)}
        or set(nonzero_carrier_rows) != {"band:A32:s3", "terminal:e16:s4"}
        or sum(nonzero_carrier_rows.values(), F(0)) != 0
        or terminal_values != ["253807/111959120", "6604809/1791345920"]
        or 16 in MULTIPLIERS
    ):
        raise CertificateError("direct-demand/box-carrier unlink gate changed")
    return {
        "classification": "EXACT_COUNTEREXAMPLE_TO_IDENTIFYING_BOX_CARRIER_WITH_DIRECT_DEMAND_POTENTIAL",
        "joint_endpoint_cell": [ftext(left), ftext(right)],
        "midpoint": ftext(midpoint),
        "box_carrier_C133_lhs_density": ftext(carrier_lhs),
        "weighted_direct_M8_M16_demand_density": ftext(weighted_direct),
        "only_nonzero_direct_component": {
            "owner": [16, 8],
            "unweighted_demand": ftext(components[16, 8]),
            "weight": ftext(WEIGHTS[16]),
        },
        "nonzero_box_carrier_rows_cancel_on_cell": {
            key: ftext(value) for key, value in nonzero_carrier_rows.items()
        },
        "graph_multipliers": list(MULTIPLIERS),
        "scale4_multiplier16_terminal_channel_present": False,
        "nonzero_integrated_upper_terminal_values": terminal_values,
        "box_carrier_is_direct_demand_potential": False,
    }


def _scope() -> dict[str, bool]:
    return {
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


def assert_scope(scope: Mapping[str, object]) -> None:
    expected = _scope()
    if dict(scope) != expected:
        raise CertificateError("scope changed or was upgraded")


def build_certificate() -> dict[str, Any]:
    fixture = fixture_audit()
    graph = exact_graph_audit()
    residual = cross_half_residual_audit()
    ledger = c133_box_carrier_ledger_audit()
    unlink = direct_demand_box_carrier_unlink_audit(ledger)
    scope = _scope()
    assert_scope(scope)
    certificate: dict[str, Any] = {
        "schema": SCHEMA,
        "status": STATUS,
        "overall_full_14_row_joint_classification": "UNKNOWN_UNLINKED_GRAPH_PRICE_TO_C133_PAYMENT",
        "solver_role": {
            "HiGHS_status_used_only_for_discovery": True,
            "accepted_evidence_is_exact_Fraction_replay": True,
            "optimality_claimed": False,
            "optimal_inaccurate_accepted_as_evidence": False,
        },
        "fixture": {
            "points": list(POINTS),
            "phase_interval": [ftext(PHASE_LOWER), ftext(PHASE_UPPER)],
            "phase_midpoint": ftext(PHASE),
            "multipliers": list(MULTIPLIERS),
            "channel_rank_range": [7, 31],
            "mandatory_natural_epoch16_state_ranks": [15, 31],
            "exact_fixture_audit": fixture,
        },
        "direct_owner_graph_master": graph,
        "full_M16_residual_gate": residual,
        "C133_same_fixture_phase_box_carrier_14_row_contract": ledger,
        "direct_demand_vs_box_carrier_unlink_gate": unlink,
        "missing_link": (
            "The exact graph-root price is an arbitrary cross-rank/cross-width PSD energy. "
            "The audited box carrier is not the potential generating the direct M8/M16 demand, "
            "as witnessed by an exact countercell, and the graph has no multiplier-16 terminal "
            "channel.  No proved charge map assigns the graph price to the fourteen signed C133 "
            "box-carrier rows.  Therefore direct-owner feasibility does not equal full "
            "fourteen-row payment."
        ),
        "scope": scope,
    }
    certificate["integrity"] = {"payload_sha256": canonical_hash(certificate)}
    return certificate


def validate_certificate(value: Mapping[str, Any]) -> dict[str, Any]:
    if type(value) is not dict:
        raise CertificateError("certificate must be a dictionary")
    integrity = value.get("integrity")
    if type(integrity) is not dict:
        raise CertificateError("integrity missing")
    payload = {key: item for key, item in value.items() if key != "integrity"}
    if integrity.get("payload_sha256") != canonical_hash(payload):
        raise CertificateError("payload hash mismatch")
    if value.get("schema") != SCHEMA or value.get("status") != STATUS:
        raise CertificateError("schema/status changed")
    scope = value.get("scope")
    if not isinstance(scope, Mapping):
        raise CertificateError("scope missing")
    assert_scope(scope)
    expected = build_certificate()
    if dict(value) != expected:
        raise CertificateError("certificate differs from exact reconstruction")
    return expected


def mutation_self_check(certificate: Mapping[str, Any]) -> dict[str, Any]:
    mutations = []
    for name, path, changed_value in (
        ("false_full_payment", ("scope", "C133_all_14_box_carrier_rows_paid_by_graph_master"), True),
        ("false_carrier_potential", ("scope", "box_carrier_is_direct_M8_M16_demand_potential"), True),
        ("false_terminal_channel", ("scope", "scale4_multiplier16_terminal_channel_present"), True),
        ("false_phase_interval", ("scope", "phase_interval_feasible"), True),
        ("false_C058", ("scope", "C058_Q1_Q2_proved"), True),
        ("drop_terminal", ("C133_same_fixture_phase_box_carrier_14_row_contract", "upper_terminal_rows"), 0),
        ("erase_countercell_direct", ("direct_demand_vs_box_carrier_unlink_gate", "weighted_direct_M8_M16_demand_density"), "0/1"),
        ("invent_multiplier16_channel", ("direct_demand_vs_box_carrier_unlink_gate", "scale4_multiplier16_terminal_channel_present"), True),
        ("drop_residual", ("full_M16_residual_gate", "cross_half_source_count"), 0),
        ("bad_margin", ("direct_owner_graph_master", "positive_2D_minus_P_margin"), "0/1"),
    ):
        changed = copy.deepcopy(certificate)
        changed[path[0]][path[1]] = changed_value
        changed["integrity"] = {
            "payload_sha256": canonical_hash({key: value for key, value in changed.items() if key != "integrity"})
        }
        mutations.append((name, changed))
    rejected = []
    for name, changed in mutations:
        try:
            validate_certificate(changed)
        except CertificateError:
            rejected.append(name)
        else:
            raise CertificateError(f"mutation accepted: {name}")
    return {"attempted": len(mutations), "rejected": len(rejected), "cases": rejected}


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if type(value) is not dict:
        raise CertificateError("JSON root is not a dictionary")
    return value


def write(path: Path, value: Mapping[str, Any]) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()

    certificate = build_certificate()
    if args.write:
        write(args.certificate, certificate)
    else:
        certificate = load(args.certificate)
    checked = validate_certificate(certificate)
    if args.self_check:
        mutations = mutation_self_check(checked)
        print(f"MUTATION_OK rejected={mutations['rejected']}/{mutations['attempted']}")
    graph = checked["direct_owner_graph_master"]
    print(
        "C136_EXACT_PARTIAL_OK "
        f"phase={graph['phase']} channels={graph['channels']} roots={graph['positive_support_roots']} "
        f"owner_rows={graph['direct_owner_cell_rows']} tight={graph['tight_direct_owner_rows']} "
        f"margin={graph['positive_2D_minus_P_margin']} C133_rows=14 "
        "full_14row_payment=UNKNOWN C058_open"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
