#!/usr/bin/env python3
"""Stdlib-only independent exact oracle for the C139 phase chamber.

This program imports neither C136/C138/C139 replay code nor any numerical
package.  It reconstructs the fixture, full M8/M16 matrices, fixed graph,
owner inequalities, phase chambers, and fourteen-row same-atom ledger.
"""

from __future__ import annotations

import argparse
import bisect
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_C139_FIXED_Y_PHASE_CHAMBER_certificate.json"
CANONICAL_C138 = HERE / "ROUTE_C_C138_SAME_ATOM_WEIGHTED_MASTER_certificate.json"
CANONICAL_C138_FILE_SHA256 = "9008c8639f13906abfb4866f8fa6e7b260c9e2fed76804656e1f773d534e70b9"
CANONICAL_C138_PAYLOAD_SHA256 = "2dcd5099a449587a27cddbea0785ef862c73e62e90573bfb39c3f3776f9fd760"
EXPECTED_PAYLOAD_SHA256 = "be2d4cd75229baaf3564546f06151982f7f0ee99e6dacf158af36136a6b2f0e4"
POINTS = (
    0, 22, 60, 83, 102, 173, 303, 513,
    616, 727, 772, 881, 972, 1041, 1103, 1169,
    1239, 1349, 1539, 1654, 2009, 2659, 3709, 3804,
    4114, 4339, 4794, 5124, 5639, 6184, 6739, 7084,
)
MULTIPLIERS = (1, 2, 4, 8)
CHANNELS = tuple(
    (rank, multiplier, POINTS[rank])
    for multiplier in MULTIPLIERS
    for rank in range(7, 32)
)
INDEX = {(rank, multiplier): i for i, (rank, multiplier, _) in enumerate(CHANNELS)}
ROOTS = tuple((i, j) for i in range(100) for j in range(i + 1, 100))
OWNERS = tuple((epoch, multiplier) for multiplier in MULTIPLIERS for epoch in (8, 16))
WEIGHTS = {8: Q(1), 16: Q(9, 16)}
ACTIVE_C = {scale: Q(2**scale, 128) for scale in range(4)}
AMBIENT = (Q(5915, 16), Q(5915, 8))
REFERENCE = Q(17745, 32)
CHAMBER = (Q(4425, 8), Q(555))
LEDGER_SPLITS = (Q(4425, 8), Q(554), Q(1664, 3), Q(555))
EXPECTED_AFFINE = {
    "D": (Q(-99, 512), Q(765573, 4096)),
    "P": (Q(36082193, 435322880), Q(1599473659439, 16716398592)),
    "margin": (Q(-204429713, 435322880), Q(4649365900753, 16716398592)),
    "pre8": (Q(0), Q(6489, 256)),
}
EXPECTED_ROWS = {
    **{f"band:A8:s{s}": (Q(0), Q(0)) for s in range(4)},
    "band:A16:s0": (Q(-63, 512), Q(85659, 1024)),
    **{f"band:A16:s{s}": (Q(0), Q(0)) for s in range(1, 4)},
    "band:A32:s0": (Q(-5121, 32768), Q(13790619, 131072)),
    "band:A32:s1": (Q(-3483, 65536), Q(6142905, 262144)),
    "band:A32:s2": (Q(441, 2048), Q(-3510675, 32768)),
    "band:A32:s3": (Q(-4995, 65536), Q(21429225, 262144)),
    "terminal:e8:s4": (Q(0), Q(0)),
    "terminal:e16:s4": (Q(0), Q(0)),
}


def need(condition, message):
    if not condition:
        raise RuntimeError(message)


def fraction(text):
    need(type(text) is str and text.count("/") == 1, "fraction schema")
    numerator, denominator = text.split("/")
    value = Q(int(numerator), int(denominator))
    need(f"{value.numerator}/{value.denominator}" == text, "unreduced fraction")
    return value


def affine(field):
    need(set(field) == {"slope", "intercept"}, "affine schema")
    return fraction(field["slope"]), fraction(field["intercept"])


def value(pair, phase):
    return pair[0] * phase + pair[1]


def digest(obj):
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


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
    return sum((
        vector[i] * matrix[i][j] * vector[j]
        for i in range(len(vector))
        for j in range(len(vector))
    ), Q(0))


def haar(x, origin, width):
    displacement = x - origin
    return int(0 <= displacement < width) - int(width <= displacement < 2 * width)


def global_state(x, phase):
    return tuple(Q(8, multiplier) * haar(x, origin, multiplier * phase) for _, multiplier, origin in CHANNELS)


def global_lines():
    return tuple(sorted({
        (Q(origin), shift * multiplier)
        for _, multiplier, origin in CHANNELS
        for shift in (0, 1, 2)
    }))


def ledger_lines():
    return tuple(sorted({
        (Q(POINTS[rank]), shift * (2**scale))
        for epoch in (4, 8, 16)
        for rank in range(epoch - 1, 2 * epoch)
        for scale in range(5)
        for shift in (0, 1, 2)
    }))


def crossings(lines, lower, upper):
    answer = set()
    for k, (origin, slope) in enumerate(lines):
        for other_origin, other_slope in lines[k + 1:]:
            if slope == other_slope:
                continue
            phase = Q(other_origin - origin, slope - other_slope)
            if lower < phase < upper:
                answer.add(phase)
    return tuple(sorted(answer))


def events(lines, phase):
    return tuple(sorted({origin + slope * phase for origin, slope in lines}))


def direct_group(epoch, multiplier):
    return {INDEX[rank, multiplier] for rank in range(epoch, 2 * epoch)}


def direct_demand(epoch, multiplier, state):
    vector = tuple(state[INDEX[rank, multiplier]] for rank in range(epoch - 1, 2 * epoch))
    return Q(multiplier, 128) * quadratic(M[epoch], vector)


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
        need(coefficient > 0, "nonpositive graph edge")
        a, b = find(i), find(j)
        if a != b:
            parent[b] = a
    return 100 - len({find(i) for i in range(100)})


FIBERS = {
    "pre8": {i for i, (rank, _, _) in enumerate(CHANNELS) if rank == 7},
    "e8": {i for i, (rank, _, _) in enumerate(CHANNELS) if 8 <= rank <= 15},
    "e16": {i for i, (rank, _, _) in enumerate(CHANNELS) if 16 <= rank <= 31},
}


def global_audit(phase, support):
    ev = events(global_lines(), phase)
    result = {
        "events": len(ev), "cells": len(ev) - 1,
        "D": Q(0), "P": Q(0), "pre8": Q(0),
        "tight": 0, "strict": 0, "zero": 0, "positive": 0,
        "prezero": 0, "prepositive": 0, "minimum": None,
    }
    signatures = []
    for left, right in zip(ev, ev[1:]):
        state = global_state((left + right) / 2, phase)
        signatures.append(state)
        length = right - left
        energy = graph_energy(state, support)
        result["P"] += length * energy
        shares = [owner_share(state, group, support) for group in FIBERS.values()]
        need(sum(shares, Q(0)) == energy, "owner fibers do not recover price")
        pre8 = shares[0]
        result["pre8"] += length * pre8
        result["prezero"] += int(pre8 == 0)
        result["prepositive"] += int(pre8 > 0)
        result["minimum"] = pre8 if result["minimum"] is None else min(result["minimum"], pre8)
        for epoch, multiplier in OWNERS:
            capacity = owner_share(state, direct_group(epoch, multiplier), support)
            demand = WEIGHTS[epoch] * direct_demand(epoch, multiplier, state)
            slack = capacity - demand
            result["minimum"] = min(result["minimum"], capacity, slack)
            result["tight"] += int(slack == 0)
            result["strict"] += int(slack > 0)
            result["zero"] += int(capacity == 0)
            result["positive"] += int(capacity > 0)
            result["D"] += length * demand
    result["margin"] = 2 * result["D"] - result["P"]
    result["signature"] = tuple(signatures)
    return result


def local_u(epoch, scale, x, phase):
    multiplier = 2**scale
    vector = tuple(
        Q(8, multiplier) * haar(x, POINTS[rank], multiplier * phase)
        for rank in range(epoch - 1, 2 * epoch)
    )
    return quadratic(M[epoch], vector)


def ledger_density(x, phase):
    u = {(epoch, scale): local_u(epoch, scale, x, phase) for epoch in (4, 8, 16) for scale in range(5)}
    C = {}
    for scale in range(5):
        C[8, scale] = u[4, scale]
        C[16, scale] = u[4, scale] + u[8, scale]
        C[32, scale] = u[4, scale] + u[8, scale] + u[16, scale]
        need(C[16, scale] - C[8, scale] == u[8, scale], "same atom 8")
        need(C[32, scale] - C[16, scale] == u[16, scale], "same atom 16")
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
    direct = sum((WEIGHTS[epoch] * ACTIVE_C[scale] * u[epoch, scale] for epoch in (8, 16) for scale in range(4)), Q(0))
    need(direct == sum(rows.values(), Q(0)), "ledger identity")
    need(all(u[epoch, 4] == 0 for epoch in (4, 8, 16)), "terminal state")
    return direct, rows


def ledger_integral(phase):
    ev = events(ledger_lines(), phase)
    rows = {key: Q(0) for key in EXPECTED_ROWS}
    total = Q(0)
    signatures = []
    for left, right in zip(ev, ev[1:]):
        midpoint = (left + right) / 2
        direct, density = ledger_density(midpoint, phase)
        signatures.append(tuple(density[key] for key in sorted(density)))
        length = right - left
        total += length * direct
        for key, amount in density.items():
            rows[key] += length * amount
    return {"events": len(ev), "cells": len(ev)-1, "rows": rows, "total": total, "signature": tuple(signatures)}


def interpolate(first_phase, first, second_phase, second):
    slope = (second - first) / (second_phase - first_phase)
    return slope, first - slope * first_phase


def parse_support(data):
    need(digest(data["support"]) == "9733c946ef369b797dee487c7693af56b101d5909bc8abf11da7d1a56549e680", "support digest")
    support = []
    seen = set()
    for item in data["support"]:
        root = item["root_index"]
        need(type(root) is int and root not in seen and 0 <= root < len(ROOTS), "root index")
        seen.add(root)
        i, j = ROOTS[root]
        need(item["left"] == list(CHANNELS[i][:2]) and item["right"] == list(CHANNELS[j][:2]), "root labels")
        support.append((i, j, fraction(item["coefficient"])))
    need(len(support) == 57 and graph_rank(support) == 51, "support size/rank")
    return tuple(support)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    args = parser.parse_args(argv)
    data = json.loads(args.certificate.read_text())
    need(data["integrity"] == {
        "algorithm": "sha256-canonical-json-excluding-integrity",
        "payload_sha256": EXPECTED_PAYLOAD_SHA256,
    }, "integrity metadata")
    need(digest({key: value for key, value in data.items() if key != "integrity"}) == EXPECTED_PAYLOAD_SHA256, "certificate payload hash")
    need(data["schema"] == "erdos1191.c139.fixed_y_maximal_phase_chamber.v1", "schema")
    need(data["classification"] == "EXACT_MAXIMAL_CONNECTED_FIXED_Y_PHASE_CHAMBER_C058_OPEN", "classification")
    need(data["scope"]["C058"] is False and data["scope"]["phase_chamber_only"] is True, "scope")
    need(tuple(data["fixture"]["points"]) == POINTS, "fixture points")
    differences = [POINTS[j] - POINTS[i] for i in range(32) for j in range(i+1, 32)]
    need(len(differences) == len(set(differences)) == 496, "Golomb/Sidon fixture")
    ancestry = data["support_ancestry"]
    need(ancestry["canonical_C138_certificate_path"] == "route_probes/ROUTE_C_C138_SAME_ATOM_WEIGHTED_MASTER_certificate.json", "relative C138 ancestry path")
    need(ancestry["canonical_C138_file_sha256"] == CANONICAL_C138_FILE_SHA256, "C138 file hash metadata")
    need(ancestry["canonical_C138_payload_sha256"] == CANONICAL_C138_PAYLOAD_SHA256, "C138 payload metadata")
    raw_c138 = CANONICAL_C138.read_bytes()
    need(hashlib.sha256(raw_c138).hexdigest() == CANONICAL_C138_FILE_SHA256, "canonical C138 file hash")
    canonical_c138 = json.loads(raw_c138)
    need(canonical_c138["integrity"]["payload_sha256"] == CANONICAL_C138_PAYLOAD_SHA256, "canonical C138 payload field")
    need(digest({key: value for key, value in canonical_c138.items() if key != "integrity"}) == CANONICAL_C138_PAYLOAD_SHA256, "canonical C138 payload hash")
    need(canonical_c138["support"] == data["support"], "C139 support differs from canonical C138")
    support = parse_support(data)

    # Reconstruct the full M16 residual independently.
    halves = [[Q(0) for _ in range(17)] for _ in range(17)]
    for i in range(9):
        for j in range(9):
            halves[i][j] += M[8][i][j] / 4
            halves[i+8][j+8] += M[8][i][j] / 4
    residual = tuple(tuple(M[16][i][j] - halves[i][j] for j in range(17)) for i in range(17))
    need(sum(residual[i][j] != 0 for i in range(17) for j in range(17) if i != j) == 160, "full M16 residual")
    need(min(v for row in residual for v in row) < 0 < max(v for row in residual for v in row), "M16 mixed residual")
    need(data["full_M16_audit"]["quarter_scaled_two_M8_replacement_used"] is False, "M16 scope")

    glines = global_lines()
    need(len(glines) == 150, "global lines")
    phase_breaks = tuple(sorted({AMBIENT[0], AMBIENT[1], *crossings(glines, *AMBIENT)}))
    need(len(phase_breaks) == 564, "global phase census")
    li, ui = phase_breaks.index(CHAMBER[0]), phase_breaks.index(CHAMBER[1])
    need(ui == li + 1 and phase_breaks[li-1] == Q(553) and phase_breaks[ui+1] == Q(557), "maximal chamber neighbors")

    # A different affine audit: interpolate two exact interior evaluations after
    # verifying their ordered state sequence is identical.
    p = (2 * CHAMBER[0] + REFERENCE) / 3
    q = (REFERENCE + 2 * CHAMBER[1]) / 3
    ap, aq = global_audit(p, support), global_audit(q, support)
    need(ap["signature"] == aq["signature"], "global state order changed inside chamber")
    reconstructed = {}
    for key in ("D", "P", "pre8"):
        reconstructed[key] = interpolate(p, ap[key], q, aq[key])
    reconstructed["margin"] = (2*reconstructed["D"][0]-reconstructed["P"][0], 2*reconstructed["D"][1]-reconstructed["P"][1])
    need(reconstructed == EXPECTED_AFFINE, "independent global affine formulas")
    need({key: affine(field) for key, field in data["global_affine"].items()} == EXPECTED_AFFINE, "affine metadata")

    endpoint_expectations = {
        CHAMBER[0]: (148,147,871,305,796,380,143,4,Q(163749,2048),Q(2365859438759,16716398592)),
        REFERENCE: (150,149,884,308,807,385,145,4,Q(1305537,16384),Q(2367807877181,16716398592)),
        CHAMBER[1]: (147,146,868,300,793,375,142,4,Q(326013,4096),Q(2368457356655,16716398592)),
    }
    for phase, expected in endpoint_expectations.items():
        audit = global_audit(phase, support)
        observed = (audit["events"],audit["cells"],audit["tight"],audit["strict"],audit["zero"],audit["positive"],audit["prezero"],audit["prepositive"],audit["D"],audit["P"])
        need(observed == expected and audit["minimum"] >= 0, f"feasible endpoint {phase}")
        need(audit["pre8"] == Q(6489,256), f"pre8 at {phase}")
        for key in ("D","P","margin","pre8"):
            need(audit[key] == value(EXPECTED_AFFINE[key], phase), f"affine endpoint {key}")
    need(value(EXPECTED_AFFINE["margin"], CHAMBER[1]) == Q(292559857297,16716398592) > 0, "margin positivity")

    # Adjacent countercells are reconstructed from their two event lines.
    for spec in data["adjacent_failures"]:
        phase = fraction(spec["representative_phase"])
        left_line = (fraction(spec["cell"]["left_line"][0]), spec["cell"]["left_line"][1])
        right_line = (fraction(spec["cell"]["right_line"][0]), spec["cell"]["right_line"][1])
        order = tuple(sorted(glines, key=lambda line: line[0] + line[1]*phase))
        k = order.index(left_line)
        need(order[k+1] == right_line, "countercell adjacency")
        left = left_line[0] + left_line[1] * phase
        right = right_line[0] + right_line[1] * phase
        state = global_state((left+right)/2, phase)
        need(digest(list(map(int,state))) == spec["cell"]["state_sha256"], "countercell state")
        epoch, multiplier = spec["owner"]
        capacity = owner_share(state, direct_group(epoch,multiplier), support)
        demand = WEIGHTS[epoch] * direct_demand(epoch,multiplier,state)
        need((capacity,demand,capacity-demand) == (fraction(spec["capacity"]),fraction(spec["weighted_demand"]),fraction(spec["slack"])), "countercell values")
        need(capacity >= 0 and capacity-demand < 0, "countercell failure")

    llines = ledger_lines()
    need(len(llines) == 203 and crossings(llines,*CHAMBER) == LEDGER_SPLITS[1:-1], "ledger crossings")
    need(tuple(map(fraction,data["same_atom_ledger"]["phase_splits"])) == LEDGER_SPLITS, "ledger split metadata")
    for lower, upper in zip(LEDGER_SPLITS,LEDGER_SPLITS[1:]):
        p = (2*lower+upper)/3
        q = (lower+2*upper)/3
        first, second = ledger_integral(p), ledger_integral(q)
        need(first["signature"] == second["signature"], "ledger state order changed")
        reconstructed_rows = {
            key: interpolate(p, first["rows"][key], q, second["rows"][key])
            for key in EXPECTED_ROWS
        }
        need(reconstructed_rows == EXPECTED_ROWS, "ledger affine rows")
    counts = {CHAMBER[0]:(201,200),Q(554):(201,200),Q(1664,3):(202,201),CHAMBER[1]:(200,199)}
    for phase, expected in counts.items():
        audit = ledger_integral(phase)
        need((audit["events"],audit["cells"]) == expected, "collapsed ledger counts")
        need(audit["rows"] == {key:value(pair,phase) for key,pair in EXPECTED_ROWS.items()}, "ledger endpoint rows")
        need(audit["total"] == value(EXPECTED_AFFINE["D"],phase), "ledger endpoint total")
    need(sum(pair[0] for pair in EXPECTED_ROWS.values()) == EXPECTED_AFFINE["D"][0], "ledger D slope")
    need(sum(pair[1] for pair in EXPECTED_ROWS.values()) == EXPECTED_AFFINE["D"][1], "ledger D intercept")
    need(len(EXPECTED_ROWS) == 14 and EXPECTED_ROWS["terminal:e8:s4"] == EXPECTED_ROWS["terminal:e16:s4"] == (Q(0),Q(0)), "formal terminal rows")

    print(
        "INDEPENDENT_C139_OK closed=[4425/8,555] roots=57 rank=51 "
        "adjacent_slacks=-549/131072,-15/8192 affine_D_P_margin=exact "
        "ledger_splits=554,1664/3 formal_rows=14 full_M16 pre8_nonnegative C058_open"
    )


if __name__ == "__main__":
    main()

