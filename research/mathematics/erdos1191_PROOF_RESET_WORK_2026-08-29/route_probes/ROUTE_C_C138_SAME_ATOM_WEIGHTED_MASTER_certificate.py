#!/usr/bin/env python3
"""Exact C138 same-atom weighted master certificate replay.

This is a fixed-fixture, fixed-phase finite certificate only. It does not
prove a phase interval, arbitrary history/rank, C058, Q1, or Q2.
"""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
from pathlib import Path
import json
import sys


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_C138_SAME_ATOM_WEIGHTED_MASTER_certificate.json"
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import ROUTE_C_C136_JOINT_GRAPH_MASTER_certificate as c136


WEIGHTS = {8: F(1), 16: F(9, 16)}
ACTIVE_C = {s: F(2**s, 128) for s in range(4)}
EXPECTED_D = F(1_305_537, 16_384)
EXPECTED_P = F(2_367_807_877_181, 16_716_398_592)
EXPECTED_MARGIN = F(296_239_592_131, 16_716_398_592)
DIRECT_MATRICES = {epoch: c136.point_matrix(epoch) for epoch in (4, 8, 16)}
EXPECTED_ROWS = {
    "band:A8:s0": F(0), "band:A8:s1": F(0), "band:A8:s2": F(0), "band:A8:s3": F(0),
    "band:A16:s0": F(252609, 16384), "band:A16:s1": F(0),
    "band:A16:s2": F(0), "band:A16:s3": F(0),
    "band:A32:s0": F(19452807, 1048576), "band:A32:s1": -F(12662595, 2097152),
    "band:A32:s2": F(804195, 65536), "band:A32:s3": F(82797525, 2097152),
    "terminal:e8:s4": F(0), "terminal:e16:s4": F(0),
}


class CertificateError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CertificateError(message)


def canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def parse_fraction(value) -> F:
    require(type(value) is str and "/" in value, "fraction must be canonical string")
    numerator, denominator = value.split("/", 1)
    parsed = F(int(numerator), int(denominator))
    require(f"{parsed.numerator}/{parsed.denominator}" == value, "fraction string not canonical")
    return parsed


def graph_rank(support) -> int:
    parent = list(range(len(c136.CHANNELS)))

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
        require(coefficient > 0, "nonpositive graph root")
        union(i, j)
    return len(c136.CHANNELS) - len({find(i) for i in range(len(c136.CHANNELS))})


def exact_square_solution(rows, rhs):
    n = len(rows)
    augmented = [[F(value) for value in row] + [value] for row, value in zip(rows, rhs)]
    for column in range(n):
        pivot = next((r for r in range(column, n) if augmented[r][column]), None)
        require(pivot is not None, "stored tight subsystem singular")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        divisor = augmented[column][column]
        augmented[column] = [value / divisor for value in augmented[column]]
        for r in range(n):
            if r == column or not augmented[r][column]:
                continue
            factor = augmented[r][column]
            augmented[r] = [
                value - factor * pivot_value
                for value, pivot_value in zip(augmented[r], augmented[column])
            ]
    return tuple(augmented[r][-1] for r in range(n))


def direct_u(epoch: int, scale: int, x: F) -> F:
    multiplier = 2**scale
    width = multiplier * c136.PHASE
    q = tuple(
        F(8, multiplier) * c136.haar_sign(x, c136.POINTS[rank], width)
        for rank in range(epoch - 1, 2 * epoch)
    )
    return c136.quadratic(DIRECT_MATRICES[epoch], q)


def same_atom_potential(x: F):
    u = {(epoch, scale): direct_u(epoch, scale, x) for epoch in (4, 8, 16) for scale in range(5)}
    C = {}
    for scale in range(5):
        C[8, scale] = u[4, scale]
        C[16, scale] = u[4, scale] + u[8, scale]
        C[32, scale] = u[4, scale] + u[8, scale] + u[16, scale]
    return u, C


def c133_rows(C):
    prefix = {}
    running = F(0)
    for scale in range(4):
        running += ACTIVE_C[scale]
        prefix[scale] = running
    rows = {}
    for scale in range(4):
        rows[f"band:A8:s{scale}"] = -WEIGHTS[8] * prefix[scale] * (C[8, scale] - C[8, scale + 1])
        rows[f"band:A16:s{scale}"] = (
            WEIGHTS[8] * prefix[scale] - WEIGHTS[16] * prefix[scale]
        ) * (C[16, scale] - C[16, scale + 1])
        rows[f"band:A32:s{scale}"] = WEIGHTS[16] * prefix[scale] * (C[32, scale] - C[32, scale + 1])
    rows["terminal:e8:s4"] = WEIGHTS[8] * prefix[3] * (C[16, 4] - C[8, 4])
    rows["terminal:e16:s4"] = WEIGHTS[16] * prefix[3] * (C[32, 4] - C[16, 4])
    lhs = sum((
        WEIGHTS[8] * ACTIVE_C[s] * (C[16, s] - C[8, s])
        + WEIGHTS[16] * ACTIVE_C[s] * (C[32, s] - C[16, s])
        for s in range(4)
    ), F(0))
    return lhs, rows


def validate_certificate(data: dict) -> dict:
    require(type(data) is dict, "certificate root")
    require(data["schema"] == "erdos1191.c138.weighted_same_atom_exact_support.v1", "schema")
    require(
        data["classification"] == "EXACT_FIXED_PHASE_SAME_ATOM_WEIGHTED_GRAPH_FEASIBLE_C058_OPEN",
        "classification",
    )
    integrity = data.get("integrity")
    require(type(integrity) is dict and integrity.get("canonical_json") is True, "integrity metadata")
    require(
        integrity.get("payload_sha256")
        == canonical_hash({key: value for key, value in data.items() if key != "integrity"}),
        "payload hash",
    )
    require(data["phase"] == "17745/32", "phase metadata")
    require(data["owner_audit"]["rows"] == 1192, "owner row metadata")
    require(data["owner_audit"]["tight"] == 884 and data["owner_audit"]["strict"] == 308, "slack metadata")
    require(data["owner_audit"]["zero_capacity_rows"] == 807, "zero capacity metadata")
    require(data["owner_audit"]["positive_capacity_rows"] == 385, "positive capacity metadata")
    require(data["owner_audit"]["pre8_rank7_owner_rows"] == 149, "pre8 row metadata")
    require(data["owner_audit"]["pre8_rank7_zero_rows"] == 145, "pre8 zero metadata")
    require(data["owner_audit"]["pre8_rank7_positive_rows"] == 4, "pre8 positive metadata")
    require(parse_fraction(data["owner_audit"]["pre8_rank7_integral"]) == F(6489, 256), "pre8 integral metadata")
    require(data["owner_audit"]["unweighted_integrated_demand_by_epoch"] == {"8": "36087/1024", "16": "80905/1024"}, "epoch demand metadata")
    require(data["owner_audit"]["direct_demand_sign_census"] == {"negative": 40, "zero": 971, "positive": 181}, "demand sign metadata")
    require(data["owner_audit"]["weights_apply_only_to_owner_RHS_and_D"] is True, "weight placement")
    require(data["owner_audit"]["past_pre8_included_in_physical_price"] is True, "pre8 price metadata")
    require(parse_fraction(data["objective"]["weighted_direct_demand_D"]) == EXPECTED_D, "D metadata")
    require(parse_fraction(data["objective"]["physical_graph_price_P"]) == EXPECTED_P, "P metadata")
    require(parse_fraction(data["objective"]["two_D_minus_P"]) == EXPECTED_MARGIN, "margin metadata")
    require(data["objective"]["positive"] is True, "margin sign metadata")
    require(data["objective"]["price_is_single_unweighted_physical_energy"] is True, "price weighting")
    require(data["objective"]["normalization_valid_because_same_M_terminals_zero"] is True, "normalization gate")
    scope = data["scope"]
    for key in (
        "C058", "Q1_Q2", "arbitrary_history_or_rank", "global_C103_owner_boundary_ledger",
        "nonanticipating_phase_rule", "phase_interval", "publication_novelty_or_prize",
    ):
        require(scope[key] is False, f"scope upgrade: {key}")
    require(scope["fixed_fixture_phase_only"] is True, "fixed scope")
    require(scope["formal_14_rows_retained_but_only_5_nonzero"] is True, "row scope")
    require(scope["same_atom_C133_exact_replay"] is True, "same-atom scope")
    entries = data["support"]
    require(len(entries) == 57, "support size")
    support = []
    seen = set()
    for entry in entries:
        root_index = entry["root_index"]
        require(type(root_index) is int and 0 <= root_index < len(c136.ROOTS), "root index")
        require(root_index not in seen, "duplicate root")
        seen.add(root_index)
        i, j = c136.ROOTS[root_index]
        require(entry["left"] == list(c136.CHANNELS[i][:2]), "left root label")
        require(entry["right"] == list(c136.CHANNELS[j][:2]), "right root label")
        support.append((i, j, parse_fraction(entry["coefficient"])))
    coefficients = tuple(value for _, _, value in support)
    require(all(value > 0 for value in coefficients), "positive coefficients")

    _, cells = c136.active_geometry()
    selected_keys = data["exactification"]["selected_rows_cell_epoch_multiplier"]
    require(len(selected_keys) == 57, "selected row count")
    rows = []
    rhs = []
    for cell_index, epoch, multiplier in selected_keys:
        state = cells[cell_index][2]
        group = set(c136.direct_group_indices((epoch, multiplier)))
        rows.append([
            ((state[i] if i in group else 0) - (state[j] if j in group else 0))
            * (state[i] - state[j])
            for i, j, _ in support
        ])
        rhs.append(WEIGHTS[epoch] * c136.direct_demand((epoch, multiplier), state))
    require(exact_square_solution(rows, rhs) == coefficients, "tight subsystem does not recover support")

    D = F(0)
    P = F(0)
    tight = strict = 0
    zero_capacity = positive_capacity = 0
    owner_partition_checks = 0
    pre8_zero = pre8_positive = 0
    pre8_integral = F(0)
    demand_by_epoch = {8: F(0), 16: F(0)}
    demand_signs = {"negative": 0, "zero": 0, "positive": 0}
    fibers = {
        label: {
            i for i, (rank, _, _) in enumerate(c136.CHANNELS)
            if c136.coordinate_owner(rank) == label
        }
        for label in ("past_epoch4", "epoch8", "epoch16")
    }
    for left, right, state in cells:
        length = right - left
        energy = c136.graph_energy(state, support)
        P += length * energy
        require(
            sum((c136.graph_owner_share(state, group, support) for group in fibers.values()), F(0)) == energy,
            "coordinate owner partition",
        )
        pre8 = c136.graph_owner_share(state, fibers["past_epoch4"], support)
        require(pre8 >= 0, "negative pre8/rank7 owner share")
        pre8_zero += int(pre8 == 0)
        pre8_positive += int(pre8 > 0)
        pre8_integral += length * pre8
        owner_partition_checks += 1
        for epoch, multiplier in c136.DIRECT_OWNERS:
            owned = c136.graph_owner_share(
                state, set(c136.direct_group_indices((epoch, multiplier))), support
            )
            unweighted_demand = c136.direct_demand((epoch, multiplier), state)
            demand = WEIGHTS[epoch] * unweighted_demand
            require(owned >= 0 and owned >= demand, "weighted owner inequality")
            zero_capacity += int(owned == 0)
            positive_capacity += int(owned > 0)
            tight += int(owned == demand)
            strict += int(owned > demand)
            D += length * demand
            demand_by_epoch[epoch] += length * unweighted_demand
            demand_signs["negative"] += int(unweighted_demand < 0)
            demand_signs["zero"] += int(unweighted_demand == 0)
            demand_signs["positive"] += int(unweighted_demand > 0)
    require((tight, strict) == (884, 308), "owner slack census")
    require((zero_capacity, positive_capacity) == (807, 385), "capacity sign census")
    require(owner_partition_checks == 149, "partition cell census")
    require((pre8_zero, pre8_positive, pre8_integral) == (145, 4, F(6489, 256)), "pre8 audit")
    require(demand_by_epoch == {8: F(36087, 1024), 16: F(80905, 1024)}, "epoch demands")
    require(demand_signs == {"negative": 40, "zero": 971, "positive": 181}, "demand signs")
    require((D, P, 2 * D - P) == (EXPECTED_D, EXPECTED_P, EXPECTED_MARGIN), "objective values")
    rank = graph_rank(support)

    events = tuple(sorted({
        F(c136.POINTS[rank_index]) + endpoint * (2**scale) * c136.PHASE
        for epoch in (4, 8, 16)
        for rank_index in range(epoch - 1, 2 * epoch)
        for scale in range(5)
        for endpoint in (0, 1, 2)
    }))
    ledger_cells = tuple(zip(events, events[1:]))
    integrated_lhs = F(0)
    integrated_rows = {}
    pointwise = 0
    terminal_zero_checks = 0
    increment_checks = 0
    for left, right in ledger_cells:
        x = (left + right) / 2
        u, C = same_atom_potential(x)
        for scale in range(5):
            require(C[16, scale] - C[8, scale] == u[8, scale], "Delta8 same atom")
            require(C[32, scale] - C[16, scale] == u[16, scale], "Delta16 same atom")
            increment_checks += 2
        require(u[4, 4] == u[8, 4] == u[16, 4] == 0, "scale-4 direct-M state")
        terminal_zero_checks += 3
        lhs, rows_at_x = c133_rows(C)
        direct = sum((
            WEIGHTS[8] * ACTIVE_C[s] * u[8, s]
            + WEIGHTS[16] * ACTIVE_C[s] * u[16, s]
            for s in range(4)
        ), F(0))
        require(lhs == direct and lhs == sum(rows_at_x.values(), F(0)), "pointwise C133 payment")
        length = right - left
        integrated_lhs += length * lhs
        for key, value in rows_at_x.items():
            integrated_rows[key] = integrated_rows.get(key, F(0)) + length * value
        pointwise += 1
    require(integrated_lhs == D, "C133 ledger does not integrate to weighted D")
    require(len(integrated_rows) == 14, "C133 row count")
    require(integrated_rows["terminal:e8:s4"] == 0, "epoch8 terminal")
    require(integrated_rows["terminal:e16:s4"] == 0, "epoch16 terminal")
    require(integrated_rows == EXPECTED_ROWS, "integrated C133 row vector")
    same_atom = data["same_atom_C133"]
    require(same_atom["baseline"] == "C8_s=U4_s", "same-atom baseline")
    require(same_atom["C16_minus_C8_equals_U8_pointwise"] is True, "Delta8 metadata")
    require(same_atom["C32_minus_C16_equals_U16_pointwise"] is True, "Delta16 metadata")
    require(same_atom["formal_rows"] == 14 and same_atom["nonzero_integrated_rows"] == 5, "row metadata")
    require(same_atom["joint_cells"] == 202, "ledger cell metadata")
    require(same_atom["prefix_increment_checks"] == 2020, "increment metadata")
    require(same_atom["terminal_state_checks"] == 606, "terminal metadata")
    require(same_atom["upper_terminal_rows_retained"] == 2, "terminal key metadata")
    require([parse_fraction(x) for x in same_atom["upper_terminal_values"]] == [F(0), F(0)], "terminal values")
    require(parse_fraction(same_atom["integrated_lhs_equals_weighted_D"]) == D, "ledger D metadata")
    require(
        {key: parse_fraction(value) for key, value in same_atom["integrated_rows"].items()}
        == EXPECTED_ROWS,
        "stored integrated rows",
    )
    return {
        "rank": rank,
        "owner_rows": tight + strict,
        "tight": tight,
        "strict": strict,
        "D": D,
        "P": P,
        "margin": 2 * D - P,
        "ledger_cells": pointwise,
        "increment_checks": increment_checks,
        "terminal_checks": terminal_zero_checks,
        "formal_rows": len(integrated_rows),
        "nonzero_rows": sum(value != 0 for value in integrated_rows.values()),
    }


def mutation_self_check(data: dict) -> dict:
    cases = []

    def add(name, mutator):
        changed = copy.deepcopy(data)
        mutator(changed)
        changed["integrity"] = {
            "canonical_json": True,
            "payload_sha256": canonical_hash({key: value for key, value in changed.items() if key != "integrity"}),
        }
        cases.append((name, changed))

    add("nonpositive_root", lambda x: x["support"][0].__setitem__("coefficient", "0/1"))
    add("float_root", lambda x: x["support"][0].__setitem__("coefficient", 0.1))
    add("duplicate_root", lambda x: x["support"][1].__setitem__("root_index", x["support"][0]["root_index"]))
    add("rank15_relabel", lambda x: x["support"][0].__setitem__("left", [15, 1]))
    add("bad_selected_row", lambda x: x["exactification"]["selected_rows_cell_epoch_multiplier"][0].__setitem__(0, 999))
    add("weight_physical_price", lambda x: x["objective"].__setitem__("price_is_single_unweighted_physical_energy", False))
    add("drop_pre8", lambda x: x["owner_audit"].__setitem__("pre8_rank7_owner_rows", 0))
    add("positive_part_demand", lambda x: x["owner_audit"]["direct_demand_sign_census"].__setitem__("negative", 0))
    add("delete_terminal_key", lambda x: x["same_atom_C133"]["integrated_rows"].pop("terminal:e8:s4"))
    add("nonzero_terminal", lambda x: x["same_atom_C133"]["integrated_rows"].__setitem__("terminal:e16:s4", "1/1"))
    add("double_A16", lambda x: x["same_atom_C133"]["integrated_rows"].__setitem__("band:A16:s0", "505218/16384"))
    add("free_potential", lambda x: x["same_atom_C133"].__setitem__("baseline", "free"))
    add("false_phase_interval", lambda x: x["scope"].__setitem__("phase_interval", True))
    add("false_C058", lambda x: x["scope"].__setitem__("C058", True))
    rejected = []
    for name, changed in cases:
        try:
            validate_certificate(changed)
        except (CertificateError, IndexError, KeyError, TypeError, ValueError):
            rejected.append(name)
        else:
            raise CertificateError(f"mutation accepted: {name}")
    return {"attempted": len(cases), "rejected": len(rejected), "cases": rejected}


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    require(type(value) is dict, "JSON root")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    data = load(args.certificate)
    result = validate_certificate(data)
    if args.self_check:
        mutations = mutation_self_check(data)
        print(f"MUTATION_OK rejected={mutations['rejected']}/{mutations['attempted']}")
    print(
        "C138_EXACT_OK "
        f"phase={c136.PHASE} roots=57 rank={result['rank']} owner_rows={result['owner_rows']} "
        f"tight={result['tight']} strict={result['strict']} D={result['D']} P={result['P']} "
        f"margin={result['margin']} C133_cells={result['ledger_cells']} "
        f"formal_rows={result['formal_rows']} nonzero_rows={result['nonzero_rows']} "
        f"terminals=0/0 pre8=nonnegative fixed_fixture_only C058_open"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
