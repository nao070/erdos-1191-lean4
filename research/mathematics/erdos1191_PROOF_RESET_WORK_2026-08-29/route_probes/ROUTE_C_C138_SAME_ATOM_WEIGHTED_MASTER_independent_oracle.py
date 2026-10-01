#!/usr/bin/env python3
"""Stdlib-only independent exact oracle for canonical C138.

This file deliberately does not import C136 or the discovery/exactification
programs.  It reconstructs the fixture, matrices, graph cone, weighted owner
rows, and same-atom C133 ledger from first principles.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
from pathlib import Path
import json


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_C138_SAME_ATOM_WEIGHTED_MASTER_certificate.json"
POINTS = (
    0, 22, 60, 83, 102, 173, 303, 513,
    616, 727, 772, 881, 972, 1041, 1103, 1169,
    1239, 1349, 1539, 1654, 2009, 2659, 3709, 3804,
    4114, 4339, 4794, 5124, 5639, 6184, 6739, 7084,
)
T = Q(17745, 32)
MULTIPLIERS = (1, 2, 4, 8)
CHANNELS = tuple((rank, multiplier, POINTS[rank]) for multiplier in MULTIPLIERS for rank in range(7, 32))
INDEX = {(rank, multiplier): i for i, (rank, multiplier, _) in enumerate(CHANNELS)}
ROOTS = tuple((i, j) for i in range(100) for j in range(i + 1, 100))
OWNERS = tuple((epoch, multiplier) for multiplier in MULTIPLIERS for epoch in (8, 16))
WEIGHTS = {8: Q(1), 16: Q(9, 16)}
ACTIVE_C = {s: Q(2**s, 128) for s in range(4)}


def canonical_hash(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def need(condition, message):
    if not condition:
        raise RuntimeError(message)


def fraction(text):
    need(type(text) is str and text.count("/") == 1, "noncanonical fraction field")
    a, b = text.split("/")
    value = Q(int(a), int(b))
    need(f"{value.numerator}/{value.denominator}" == text, "unreduced fraction")
    return value


def point_matrix(n):
    b = tuple(tuple(
        Q(0) if i == j or abs(i - j) == 1 else -Q((j - i) ** 2, 8 * n * n)
        for j in range(n)
    ) for i in range(n))
    d = tuple(tuple(Q((k == i) - (k == i + 1)) for k in range(n + 1)) for i in range(n))
    return tuple(tuple(
        sum((d[a][i] * b[a][c] * d[c][j] for a in range(n) for c in range(n)), Q(0))
        for j in range(n + 1)
    ) for i in range(n + 1))


M = {n: point_matrix(n) for n in (4, 8, 16)}


def quadratic(matrix, vector):
    return sum((vector[i] * matrix[i][j] * vector[j] for i in range(len(vector)) for j in range(len(vector))), Q(0))


def haar(x, origin, width):
    d = x - origin
    return int(0 <= d < width) - int(width <= d < 2 * width)


def global_state(x):
    return tuple(Q(8, multiplier) * haar(x, origin, multiplier * T) for _, multiplier, origin in CHANNELS)


def global_cells():
    events = tuple(sorted({Q(origin) + shift * multiplier * T for _, multiplier, origin in CHANNELS for shift in (0, 1, 2)}))
    need((len(events), events[0], events[-1]) == (150, Q(513), Q(31913, 2)), "global geometry")
    return tuple((a, b, global_state((a + b) / 2)) for a, b in zip(events, events[1:]))


def direct_group(epoch, multiplier):
    return {INDEX[rank, multiplier] for rank in range(epoch, 2 * epoch)}


def direct_demand(epoch, multiplier, state):
    local = tuple(state[INDEX[rank, multiplier]] for rank in range(epoch - 1, 2 * epoch))
    return Q(multiplier, 128) * quadratic(M[epoch], local)


def owner_share(state, group, support):
    return sum((
        coefficient
        * ((state[i] if i in group else 0) - (state[j] if j in group else 0))
        * (state[i] - state[j])
        for i, j, coefficient in support
    ), Q(0))


def graph_energy(state, support):
    return sum((coefficient * (state[i] - state[j]) ** 2 for i, j, coefficient in support), Q(0))


def graph_rank(support):
    parent = list(range(100))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i, j, coefficient in support:
        need(coefficient > 0, "positive graph root")
        a, b = find(i), find(j)
        if a != b:
            parent[b] = a
    return 100 - len({find(i) for i in range(100)})


def local_u(epoch, scale, x):
    multiplier = 2**scale
    width = multiplier * T
    vector = tuple(Q(8, multiplier) * haar(x, POINTS[rank], width) for rank in range(epoch - 1, 2 * epoch))
    return quadratic(M[epoch], vector)


def potential(x):
    u = {(epoch, scale): local_u(epoch, scale, x) for epoch in (4, 8, 16) for scale in range(5)}
    C = {}
    for scale in range(5):
        C[8, scale] = u[4, scale]
        C[16, scale] = u[4, scale] + u[8, scale]
        C[32, scale] = u[4, scale] + u[8, scale] + u[16, scale]
    return u, C


def ledger(C):
    prefix = {}
    running = Q(0)
    for scale in range(4):
        running += ACTIVE_C[scale]
        prefix[scale] = running
    rows = {}
    for scale in range(4):
        rows[f"band:A8:s{scale}"] = -WEIGHTS[8] * prefix[scale] * (C[8, scale] - C[8, scale + 1])
        rows[f"band:A16:s{scale}"] = (WEIGHTS[8] - WEIGHTS[16]) * prefix[scale] * (C[16, scale] - C[16, scale + 1])
        rows[f"band:A32:s{scale}"] = WEIGHTS[16] * prefix[scale] * (C[32, scale] - C[32, scale + 1])
    rows["terminal:e8:s4"] = WEIGHTS[8] * prefix[3] * (C[16, 4] - C[8, 4])
    rows["terminal:e16:s4"] = WEIGHTS[16] * prefix[3] * (C[32, 4] - C[16, 4])
    lhs = sum((
        WEIGHTS[8] * ACTIVE_C[s] * (C[16, s] - C[8, s])
        + WEIGHTS[16] * ACTIVE_C[s] * (C[32, s] - C[16, s])
        for s in range(4)
    ), Q(0))
    return lhs, rows


def verify(certificate: Path = DEFAULT_CERTIFICATE):
    data = json.loads(certificate.read_text())
    need(data["schema"] == "erdos1191.c138.weighted_same_atom_exact_support.v1", "schema")
    need(data["classification"] == "EXACT_FIXED_PHASE_SAME_ATOM_WEIGHTED_GRAPH_FEASIBLE_C058_OPEN", "classification")
    need(
        data["integrity"]["payload_sha256"]
        == canonical_hash({key: value for key, value in data.items() if key != "integrity"}),
        "payload hash",
    )
    need(data["phase"] == "17745/32", "phase metadata")
    need(fraction(data["objective"]["weighted_direct_demand_D"]) == Q(1305537, 16384), "D metadata")
    need(fraction(data["objective"]["physical_graph_price_P"]) == Q(2367807877181, 16716398592), "P metadata")
    need(fraction(data["objective"]["two_D_minus_P"]) == Q(296239592131, 16716398592), "margin metadata")
    need(data["objective"]["positive"] is True and data["scope"]["C058"] is False, "scope metadata")
    need(data["owner_audit"]["pre8_rank7_owner_rows"] == 149, "pre8 row metadata")
    need(data["owner_audit"]["pre8_rank7_zero_rows"] == 145, "pre8 zero metadata")
    need(data["owner_audit"]["pre8_rank7_positive_rows"] == 4, "pre8 positive metadata")
    need(fraction(data["owner_audit"]["pre8_rank7_integral"]) == Q(6489, 256), "pre8 integral metadata")
    need(data["owner_audit"]["weights_apply_only_to_owner_RHS_and_D"] is True, "weight placement")
    need(data["owner_audit"]["past_pre8_included_in_physical_price"] is True, "pre8 price")
    need(data["owner_audit"]["unweighted_integrated_demand_by_epoch"] == {"8": "36087/1024", "16": "80905/1024"}, "epoch demand metadata")
    need(data["owner_audit"]["direct_demand_sign_census"] == {"negative": 40, "zero": 971, "positive": 181}, "demand sign metadata")
    need(data["objective"]["price_is_single_unweighted_physical_energy"] is True, "physical price")
    need(data["objective"]["normalization_valid_because_same_M_terminals_zero"] is True, "terminal normalization")
    need(len(data["support"]) == 57, "support count")
    support = []
    seen = set()
    for item in data["support"]:
        k = item["root_index"]
        need(type(k) is int and k not in seen and 0 <= k < len(ROOTS), "root key")
        seen.add(k)
        i, j = ROOTS[k]
        need(item["left"] == list(CHANNELS[i][:2]), "left label")
        need(item["right"] == list(CHANNELS[j][:2]), "right label")
        support.append((i, j, fraction(item["coefficient"])))

    cells = global_cells()
    D = Q(0)
    P = Q(0)
    tight = strict = zero = positive = 0
    pre8_zero = pre8_positive = 0
    pre8_integral = Q(0)
    demand_by_epoch = {8: Q(0), 16: Q(0)}
    demand_signs = {"negative": 0, "zero": 0, "positive": 0}
    fibers = {
        "past": {i for i, (rank, _, _) in enumerate(CHANNELS) if rank == 7},
        "e8": {i for i, (rank, _, _) in enumerate(CHANNELS) if 8 <= rank <= 15},
        "e16": {i for i, (rank, _, _) in enumerate(CHANNELS) if 16 <= rank <= 31},
    }
    need(tuple(map(len, fibers.values())) == (4, 32, 64), "owner fibers")
    for left, right, state in cells:
        length = right - left
        energy = graph_energy(state, support)
        P += length * energy
        need(sum((owner_share(state, group, support) for group in fibers.values()), Q(0)) == energy, "owner recovery")
        pre8 = owner_share(state, fibers["past"], support)
        need(pre8 >= 0, "negative pre8 owner share")
        pre8_zero += int(pre8 == 0)
        pre8_positive += int(pre8 > 0)
        pre8_integral += length * pre8
        for epoch, multiplier in OWNERS:
            capacity = owner_share(state, direct_group(epoch, multiplier), support)
            unweighted_demand = direct_demand(epoch, multiplier, state)
            demand = WEIGHTS[epoch] * unweighted_demand
            need(capacity >= 0 and capacity >= demand, "owner row")
            tight += int(capacity == demand)
            strict += int(capacity > demand)
            zero += int(capacity == 0)
            positive += int(capacity > 0)
            D += length * demand
            demand_by_epoch[epoch] += length * unweighted_demand
            demand_signs["negative"] += int(unweighted_demand < 0)
            demand_signs["zero"] += int(unweighted_demand == 0)
            demand_signs["positive"] += int(unweighted_demand > 0)
    need((tight, strict, zero, positive) == (884, 308, 807, 385), "owner census")
    need((pre8_zero, pre8_positive, pre8_integral) == (145, 4, Q(6489, 256)), "pre8 census")
    need(demand_by_epoch == {8: Q(36087, 1024), 16: Q(80905, 1024)}, "epoch demand census")
    need(demand_signs == {"negative": 40, "zero": 971, "positive": 181}, "demand sign census")
    need(D == Q(1305537, 16384), "D")
    need(P == Q(2367807877181, 16716398592), "P")
    need(2 * D - P == Q(296239592131, 16716398592), "margin")
    rank = graph_rank(support)
    need(rank == 51, "graph rank")

    events = tuple(sorted({
        Q(POINTS[r]) + endpoint * (2**scale) * T
        for epoch in (4, 8, 16)
        for r in range(epoch - 1, 2 * epoch)
        for scale in range(5)
        for endpoint in (0, 1, 2)
    }))
    need(len(events) == 203, "ledger events")
    integrated = {}
    total = Q(0)
    terminal_checks = 0
    increment_checks = 0
    for left, right in zip(events, events[1:]):
        x = (left + right) / 2
        u, C = potential(x)
        for scale in range(5):
            need(C[16, scale] - C[8, scale] == u[8, scale], "Delta8")
            need(C[32, scale] - C[16, scale] == u[16, scale], "Delta16")
            increment_checks += 2
        need(u[4, 4] == u[8, 4] == u[16, 4] == 0, "terminal state")
        terminal_checks += 3
        lhs, rows = ledger(C)
        direct = sum((
            WEIGHTS[8] * ACTIVE_C[s] * u[8, s]
            + WEIGHTS[16] * ACTIVE_C[s] * u[16, s]
            for s in range(4)
        ), Q(0))
        need(lhs == direct == sum(rows.values(), Q(0)), "C133 identity")
        length = right - left
        total += length * lhs
        for key, value in rows.items():
            integrated[key] = integrated.get(key, Q(0)) + length * value
    need(total == D and len(integrated) == 14, "integrated C133")
    expected_rows = {
        "band:A8:s0": Q(0), "band:A8:s1": Q(0), "band:A8:s2": Q(0), "band:A8:s3": Q(0),
        "band:A16:s0": Q(252609, 16384), "band:A16:s1": Q(0), "band:A16:s2": Q(0), "band:A16:s3": Q(0),
        "band:A32:s0": Q(19452807, 1048576), "band:A32:s1": -Q(12662595, 2097152),
        "band:A32:s2": Q(804195, 65536), "band:A32:s3": Q(82797525, 2097152),
        "terminal:e8:s4": Q(0), "terminal:e16:s4": Q(0),
    }
    need(integrated == expected_rows, "integrated row values")
    same_atom = data["same_atom_C133"]
    need(same_atom["formal_rows"] == 14 and same_atom["nonzero_integrated_rows"] == 5, "row metadata")
    need(same_atom["joint_cells"] == 202 and same_atom["prefix_increment_checks"] == 2020, "cell metadata")
    need(same_atom["terminal_state_checks"] == 606, "terminal metadata")
    need({key: fraction(value) for key, value in same_atom["integrated_rows"].items()} == expected_rows, "stored rows")
    need(data["scope"]["formal_14_rows_retained_but_only_5_nonzero"] is True, "row scope")
    for key in ("C058", "Q1_Q2", "phase_interval", "nonanticipating_phase_rule", "global_C103_owner_boundary_ledger"):
        need(data["scope"][key] is False, f"scope upgrade {key}")
    print(
        "INDEPENDENT_C138_OK "
        f"roots=57 rank={rank} rows={tight+strict} D={D} P={P} margin={2*D-P} "
        f"ledger_cells={len(events)-1} increment_checks={increment_checks} "
        f"terminal_checks={terminal_checks} formal_rows=14 C058_open"
    )
    return {
        "roots": len(support), "rank": rank, "owner_rows": tight + strict,
        "D": D, "P": P, "margin": 2 * D - P, "formal_rows": len(integrated),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    args = parser.parse_args()
    verify(args.certificate)


if __name__ == "__main__":
    main()
