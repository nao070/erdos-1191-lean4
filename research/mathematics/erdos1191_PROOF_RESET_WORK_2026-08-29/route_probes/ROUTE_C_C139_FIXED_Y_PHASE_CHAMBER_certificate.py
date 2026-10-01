#!/usr/bin/env python3
"""Exact replay of the C139 fixed-Y maximal phase chamber.

The graph witness is the frozen 57-root C138 graph.  This replay proves only a
finite, fixed-fixture phase chamber.  It does not promote the result to C058.
"""

from __future__ import annotations

import argparse
import bisect
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_C139_FIXED_Y_PHASE_CHAMBER_certificate.json"
ROUTE_PROBES_DIR = HERE
if str(ROUTE_PROBES_DIR) not in sys.path:
    sys.path.insert(0, str(ROUTE_PROBES_DIR))
import ROUTE_C_C136_JOINT_GRAPH_MASTER_certificate as c136


SCHEMA = "erdos1191.c139.fixed_y_maximal_phase_chamber.v1"
CLASSIFICATION = "EXACT_MAXIMAL_CONNECTED_FIXED_Y_PHASE_CHAMBER_C058_OPEN"
AMBIENT = (F(5915, 16), F(5915, 8))
REFERENCE = F(17745, 32)
CHAMBER = (F(4425, 8), F(555))
ADJACENT = ((F(553), F(4425, 8)), (F(555), F(557)))
LEDGER_SPLITS = (F(4425, 8), F(554), F(1664, 3), F(555))
WEIGHTS = {8: F(1), 16: F(9, 16)}
ACTIVE_C = {s: F(2**s, 128) for s in range(4)}
SUPPORT_PAYLOAD_SHA256 = "9733c946ef369b797dee487c7693af56b101d5909bc8abf11da7d1a56549e680"
CANONICAL_C138 = ROUTE_PROBES_DIR / "ROUTE_C_C138_SAME_ATOM_WEIGHTED_MASTER_certificate.json"
CANONICAL_C138_REPO_RELATIVE = "route_probes/ROUTE_C_C138_SAME_ATOM_WEIGHTED_MASTER_certificate.json"
CANONICAL_C138_FILE_SHA256 = "9008c8639f13906abfb4866f8fa6e7b260c9e2fed76804656e1f773d534e70b9"
CANONICAL_C138_PAYLOAD_SHA256 = "2dcd5099a449587a27cddbea0785ef862c73e62e90573bfb39c3f3776f9fd760"
EXPECTED_PAYLOAD_SHA256 = "be2d4cd75229baaf3564546f06151982f7f0ee99e6dacf158af36136a6b2f0e4"

EXPECTED_GLOBAL_AFFINE = {
    "D": (F(-99, 512), F(765573, 4096)),
    "P": (F(36082193, 435322880), F(1599473659439, 16716398592)),
    "margin": (F(-204429713, 435322880), F(4649365900753, 16716398592)),
    "pre8": (F(0), F(6489, 256)),
}

EXPECTED_LEDGER_AFFINE = {
    **{f"band:A8:s{s}": (F(0), F(0)) for s in range(4)},
    "band:A16:s0": (F(-63, 512), F(85659, 1024)),
    **{f"band:A16:s{s}": (F(0), F(0)) for s in range(1, 4)},
    "band:A32:s0": (F(-5121, 32768), F(13790619, 131072)),
    "band:A32:s1": (F(-3483, 65536), F(6142905, 262144)),
    "band:A32:s2": (F(441, 2048), F(-3510675, 32768)),
    "band:A32:s3": (F(-4995, 65536), F(21429225, 262144)),
    "terminal:e8:s4": (F(0), F(0)),
    "terminal:e16:s4": (F(0), F(0)),
}

EXPECTED_REFERENCE_ROWS = {
    "band:A8:s0": F(0),
    "band:A8:s1": F(0),
    "band:A8:s2": F(0),
    "band:A8:s3": F(0),
    "band:A16:s0": F(252609, 16384),
    "band:A16:s1": F(0),
    "band:A16:s2": F(0),
    "band:A16:s3": F(0),
    "band:A32:s0": F(19452807, 1048576),
    "band:A32:s1": -F(12662595, 2097152),
    "band:A32:s2": F(804195, 65536),
    "band:A32:s3": F(82797525, 2097152),
    "terminal:e8:s4": F(0),
    "terminal:e16:s4": F(0),
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def ftext(value: F | int) -> str:
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def parse_fraction(value: object) -> F:
    require(type(value) is str and value.count("/") == 1, "noncanonical fraction field")
    numerator, denominator = value.split("/")
    parsed = F(int(numerator), int(denominator))
    require(ftext(parsed) == value, "unreduced fraction field")
    return parsed


def parse_affine(value: object) -> tuple[F, F]:
    require(type(value) is dict and set(value) == {"slope", "intercept"}, "affine schema")
    return parse_fraction(value["slope"]), parse_fraction(value["intercept"])


def affine_value(pair: tuple[F, F], phase: F) -> F:
    return pair[0] * phase + pair[1]


def canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def parse_support(data: dict) -> tuple[tuple[int, int, F], ...]:
    entries = data["support"]
    require(len(entries) == 57, "support count")
    require(canonical_hash(entries) == SUPPORT_PAYLOAD_SHA256, "frozen C138 support hash")
    support = []
    seen = set()
    for item in entries:
        root_index = item["root_index"]
        require(type(root_index) is int and 0 <= root_index < len(c136.ROOTS), "root index")
        require(root_index not in seen, "duplicate support root")
        seen.add(root_index)
        i, j = c136.ROOTS[root_index]
        require(item["left"] == list(c136.CHANNELS[i][:2]), "left root label")
        require(item["right"] == list(c136.CHANNELS[j][:2]), "right root label")
        coefficient = parse_fraction(item["coefficient"])
        require(coefficient > 0, "nonpositive graph coefficient")
        support.append((i, j, coefficient))
    require(c136.graph_rank(support) == 51, "graph rank")
    return tuple(support)


def global_lines() -> tuple[tuple[F, int], ...]:
    return tuple(sorted({
        (F(origin), shift * multiplier)
        for _, multiplier, origin in c136.CHANNELS
        for shift in (0, 1, 2)
    }))


def ledger_lines() -> tuple[tuple[F, int], ...]:
    return tuple(sorted({
        (F(c136.POINTS[rank]), shift * (2**scale))
        for epoch in (4, 8, 16)
        for rank in range(epoch - 1, 2 * epoch)
        for scale in range(5)
        for shift in (0, 1, 2)
    }))


def crossing_phases(lines, lower: F, upper: F) -> tuple[F, ...]:
    phases = set()
    for k, (a, b) in enumerate(lines):
        for aa, bb in lines[k + 1:]:
            if b == bb:
                continue
            phase = F(aa - a, b - bb)
            if lower < phase < upper:
                phases.add(phase)
    return tuple(sorted(phases))


def event_values(lines, phase: F) -> tuple[F, ...]:
    return tuple(sorted({a + b * phase for a, b in lines}))


def ordered_lines(lines, phase: F) -> tuple[tuple[F, int], ...]:
    ordered = tuple(sorted(lines, key=lambda line: (line[0] + line[1] * phase, line)))
    require(len({a + b * phase for a, b in ordered}) == len(ordered), "sample lies on an event crossing")
    return ordered


def global_state(x: F, phase: F) -> tuple[F, ...]:
    return tuple(
        F(8, multiplier) * c136.haar_sign(x, origin, multiplier * phase)
        for _, multiplier, origin in c136.CHANNELS
    )


def owner_fibers() -> dict[str, set[int]]:
    return {
        label: {
            i for i, (rank, _, _) in enumerate(c136.CHANNELS)
            if c136.coordinate_owner(rank) == label
        }
        for label in ("past_epoch4", "epoch8", "epoch16")
    }


def global_audit(phase: F, support) -> dict:
    events = event_values(global_lines(), phase)
    fibers = owner_fibers()
    groups = {
        owner: set(c136.direct_group_indices(owner))
        for owner in c136.DIRECT_OWNERS
    }
    D = P = pre8_integral = F(0)
    tight = strict = zero_capacity = positive_capacity = 0
    pre8_zero = pre8_positive = 0
    min_positive_slack = min_positive_capacity = None
    min_gate = None
    states = []
    for left, right in zip(events, events[1:]):
        require(left < right, "collapsed event was not removed")
        state = global_state((left + right) / 2, phase)
        states.append(state)
        length = right - left
        energy = c136.graph_energy(state, support)
        P += length * energy
        shares = {
            label: c136.graph_owner_share(state, group, support)
            for label, group in fibers.items()
        }
        require(sum(shares.values(), F(0)) == energy, "owner partition")
        pre8 = shares["past_epoch4"]
        pre8_integral += length * pre8
        pre8_zero += int(pre8 == 0)
        pre8_positive += int(pre8 > 0)
        min_gate = pre8 if min_gate is None else min(min_gate, pre8)
        for owner in c136.DIRECT_OWNERS:
            epoch, _ = owner
            capacity = c136.graph_owner_share(state, groups[owner], support)
            demand = WEIGHTS[epoch] * c136.direct_demand(owner, state)
            slack = capacity - demand
            min_gate = min(min_gate, capacity, slack)
            tight += int(slack == 0)
            strict += int(slack > 0)
            zero_capacity += int(capacity == 0)
            positive_capacity += int(capacity > 0)
            if slack > 0:
                min_positive_slack = slack if min_positive_slack is None else min(min_positive_slack, slack)
            if capacity > 0:
                min_positive_capacity = capacity if min_positive_capacity is None else min(min_positive_capacity, capacity)
            D += length * demand
    return {
        "events": len(events),
        "cells": len(events) - 1,
        "states": tuple(states),
        "D": D,
        "P": P,
        "margin": 2 * D - P,
        "pre8_integral": pre8_integral,
        "tight": tight,
        "strict": strict,
        "zero_capacity": zero_capacity,
        "positive_capacity": positive_capacity,
        "pre8_zero": pre8_zero,
        "pre8_positive": pre8_positive,
        "min_positive_slack": min_positive_slack,
        "min_positive_capacity": min_positive_capacity,
        "min_gate": min_gate,
    }


def global_affine(sample: F, support) -> dict[str, tuple[F, F]]:
    lines = ordered_lines(global_lines(), sample)
    fibers = owner_fibers()
    groups = {owner: set(c136.direct_group_indices(owner)) for owner in c136.DIRECT_OWNERS}
    result = {key: [F(0), F(0)] for key in ("D", "P", "pre8")}
    for (a, b), (aa, bb) in zip(lines, lines[1:]):
        left, right = a + b * sample, aa + bb * sample
        state = global_state((left + right) / 2, sample)
        densities = {
            "D": sum((
                WEIGHTS[epoch] * c136.direct_demand((epoch, multiplier), state)
                for epoch, multiplier in c136.DIRECT_OWNERS
            ), F(0)),
            "P": c136.graph_energy(state, support),
            "pre8": c136.graph_owner_share(state, fibers["past_epoch4"], support),
        }
        for key, density in densities.items():
            result[key][0] += (bb - b) * density
            result[key][1] += (aa - a) * density
    answer = {key: tuple(value) for key, value in result.items()}
    answer["margin"] = (
        2 * answer["D"][0] - answer["P"][0],
        2 * answer["D"][1] - answer["P"][1],
    )
    return answer


DIRECT_MATRICES = {epoch: c136.point_matrix(epoch) for epoch in (4, 8, 16)}


def direct_u(epoch: int, scale: int, x: F, phase: F) -> F:
    multiplier = 2**scale
    vector = tuple(
        F(8, multiplier) * c136.haar_sign(
            x, c136.POINTS[rank], multiplier * phase
        )
        for rank in range(epoch - 1, 2 * epoch)
    )
    return c136.quadratic(DIRECT_MATRICES[epoch], vector)


def ledger_at(x: F, phase: F) -> tuple[F, dict[str, F], int]:
    u = {
        (epoch, scale): direct_u(epoch, scale, x, phase)
        for epoch in (4, 8, 16)
        for scale in range(5)
    }
    C = {}
    for scale in range(5):
        C[8, scale] = u[4, scale]
        C[16, scale] = u[4, scale] + u[8, scale]
        C[32, scale] = u[4, scale] + u[8, scale] + u[16, scale]
        require(C[16, scale] - C[8, scale] == u[8, scale], "same-atom Delta8")
        require(C[32, scale] - C[16, scale] == u[16, scale], "same-atom Delta16")
    prefix = {}
    running = F(0)
    for scale in range(4):
        running += ACTIVE_C[scale]
        prefix[scale] = running
    rows = {}
    for scale in range(4):
        rows[f"band:A8:s{scale}"] = -WEIGHTS[8] * prefix[scale] * (
            C[8, scale] - C[8, scale + 1]
        )
        rows[f"band:A16:s{scale}"] = (WEIGHTS[8] - WEIGHTS[16]) * prefix[scale] * (
            C[16, scale] - C[16, scale + 1]
        )
        rows[f"band:A32:s{scale}"] = WEIGHTS[16] * prefix[scale] * (
            C[32, scale] - C[32, scale + 1]
        )
    rows["terminal:e8:s4"] = WEIGHTS[8] * prefix[3] * (C[16, 4] - C[8, 4])
    rows["terminal:e16:s4"] = WEIGHTS[16] * prefix[3] * (C[32, 4] - C[16, 4])
    direct = sum((
        WEIGHTS[epoch] * ACTIVE_C[scale] * u[epoch, scale]
        for epoch in (8, 16)
        for scale in range(4)
    ), F(0))
    require(direct == sum(rows.values(), F(0)), "pointwise C133 ledger")
    terminal_zero = sum(u[epoch, 4] == 0 for epoch in (4, 8, 16))
    return direct, rows, terminal_zero


def ledger_integral(phase: F) -> dict:
    events = event_values(ledger_lines(), phase)
    rows = {key: F(0) for key in EXPECTED_LEDGER_AFFINE}
    total = F(0)
    terminal_checks = 0
    pointwise_checks = 0
    for left, right in zip(events, events[1:]):
        direct, current, terminal_zero = ledger_at((left + right) / 2, phase)
        require(terminal_zero == 3, "nonzero terminal same-M state")
        length = right - left
        total += length * direct
        for key, value in current.items():
            rows[key] += length * value
        terminal_checks += terminal_zero
        pointwise_checks += 1
    return {
        "events": len(events),
        "cells": len(events) - 1,
        "rows": rows,
        "total": total,
        "terminal_checks": terminal_checks,
        "pointwise_checks": pointwise_checks,
    }


def ledger_affine(sample: F) -> dict[str, tuple[F, F]]:
    lines = ordered_lines(ledger_lines(), sample)
    result = {key: [F(0), F(0)] for key in EXPECTED_LEDGER_AFFINE}
    for (a, b), (aa, bb) in zip(lines, lines[1:]):
        left, right = a + b * sample, aa + bb * sample
        _, rows, terminal_zero = ledger_at((left + right) / 2, sample)
        require(terminal_zero == 3, "generic terminal same-M state")
        for key, density in rows.items():
            result[key][0] += (bb - b) * density
            result[key][1] += (aa - a) * density
    return {key: tuple(value) for key, value in result.items()}


def full_m16_audit(data: dict) -> None:
    m8, m16 = DIRECT_MATRICES[8], DIRECT_MATRICES[16]
    halves = [[F(0) for _ in range(17)] for _ in range(17)]
    for i in range(9):
        for j in range(9):
            halves[i][j] += m8[i][j] / 4
            halves[i + 8][j + 8] += m8[i][j] / 4
    residual = tuple(tuple(m16[i][j] - halves[i][j] for j in range(17)) for i in range(17))
    sources = tuple((i, j) for i in range(8) for j in range(8, 16) if j >= i + 2)
    require(len(sources) == 63, "M16 cross-half source count")
    require(sum(residual[i][j] != 0 for i in range(17) for j in range(17) if i != j) == 160, "M16 residual support")
    require(all(sum(row, F(0)) == 0 for row in residual), "M16 residual row sums")
    values = [residual[i][j] for i in range(17) for j in range(i + 1, 17) if residual[i][j]]
    require(min(values) < 0 < max(values), "M16 residual mixed sign")
    require(data["full_M16_audit"] == {
        "cross_half_sources": 63,
        "ordered_nonzero_offdiagonal_residual_entries": 160,
        "quarter_scaled_two_M8_replacement_used": False,
        "full_M16_used_in_every_epoch16_row": True,
    }, "full M16 metadata")


def verify_failure(spec: dict, support) -> None:
    chamber = tuple(parse_fraction(value) for value in spec["open_chamber"])
    representative = parse_fraction(spec["representative_phase"])
    require(chamber[0] < representative < chamber[1], "failure representative")
    left_line = tuple([parse_fraction(spec["cell"]["left_line"][0]), int(spec["cell"]["left_line"][1])])
    right_line = tuple([parse_fraction(spec["cell"]["right_line"][0]), int(spec["cell"]["right_line"][1])])
    ordered = ordered_lines(global_lines(), representative)
    left_index = ordered.index(left_line)
    require(ordered[left_index + 1] == right_line, "failure witness lines are not adjacent")
    left = left_line[0] + left_line[1] * representative
    right = right_line[0] + right_line[1] * representative
    require(left < right, "failure witness cell orientation")
    state = global_state((left + right) / 2, representative)
    require(canonical_hash(list(map(int, state))) == spec["cell"]["state_sha256"], "failure state hash")
    epoch, multiplier = map(int, spec["owner"])
    group = set(c136.direct_group_indices((epoch, multiplier)))
    capacity = c136.graph_owner_share(state, group, support)
    demand = WEIGHTS[epoch] * c136.direct_demand((epoch, multiplier), state)
    slack = capacity - demand
    require((capacity, demand, slack) == tuple(parse_fraction(spec[key]) for key in ("capacity", "weighted_demand", "slack")), "failure arithmetic")
    require(slack < 0 <= capacity, "stored adjacent chamber is not a domination failure")
    width = (right_line[1] - left_line[1], right_line[0] - left_line[0])
    require(width == parse_affine(spec["cell"]["width"]), "failure width affine")
    collapsed = chamber[1] if spec["side"] == "left" else chamber[0]
    require(affine_value(width, collapsed) == 0, "failure cell does not collapse at feasible endpoint")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    args = parser.parse_args(argv)
    data = json.loads(args.certificate.read_text())
    require(data["integrity"] == {
        "algorithm": "sha256-canonical-json-excluding-integrity",
        "payload_sha256": EXPECTED_PAYLOAD_SHA256,
    }, "integrity metadata")
    require(canonical_hash({key: value for key, value in data.items() if key != "integrity"}) == EXPECTED_PAYLOAD_SHA256, "certificate payload hash")
    require(data["schema"] == SCHEMA, "schema")
    require(data["classification"] == CLASSIFICATION, "classification")
    require(data["scope"] == {
        "fixed_fixture": True,
        "fixed_graph_Y": True,
        "phase_chamber_only": True,
        "arbitrary_history_or_rank": False,
        "nonanticipating_phase_rule": False,
        "global_C103": False,
        "C058": False,
    }, "scope metadata")
    require(data["fixture"] == {
        "points": list(c136.POINTS),
        "marks": 32,
        "distinct_positive_differences": 496,
        "channels": 100,
        "candidate_graph_roots": 4950,
        "positive_support_roots": 57,
        "graph_rank": 51,
    }, "fixture metadata")
    require(data["phase"]["x_cell_convention"] == "[event_i,event_(i+1)); coincident endpoints collapsed; zero-length cells omitted", "half-open convention")
    require(tuple(map(parse_fraction, data["phase"]["ambient_critical_band"])) == AMBIENT, "ambient phase band")
    require(parse_fraction(data["phase"]["reference"]) == REFERENCE, "reference phase")
    require(tuple(map(parse_fraction, data["phase"]["maximal_closed_feasible_interval"])) == CHAMBER, "phase chamber")
    require(tuple(tuple(map(parse_fraction, chamber)) for chamber in data["phase"]["immediately_adjacent_open_chambers"]) == ADJACENT, "adjacent chambers")
    require(data["phase"]["global_event_lines"] == 150, "global line metadata")
    require(data["phase"]["ambient_phase_breakpoints_including_band_ends"] == 564, "phase breakpoint metadata")
    require(tuple(map(parse_fraction, data["phase"]["generic_open_owner_chamber"])) == CHAMBER, "generic chamber metadata")
    require(data["phase"]["phase_subinterval_convention"] == "[lower,upper), except the final piece includes the closed upper endpoint", "phase subinterval convention")
    ancestry = data["support_ancestry"]
    require(ancestry == {
        "canonical_C138_certificate_path": CANONICAL_C138_REPO_RELATIVE,
        "canonical_C138_file_sha256": CANONICAL_C138_FILE_SHA256,
        "canonical_C138_payload_sha256": CANONICAL_C138_PAYLOAD_SHA256,
        "support_only_canonical_sha256": SUPPORT_PAYLOAD_SHA256,
        "source_schema": "erdos1191.c138.weighted_same_atom_exact_support.v1",
        "same_fixed_Y_as_C138": True,
    }, "C138 ancestry metadata")
    canonical_c138_raw = CANONICAL_C138.read_bytes()
    require(hashlib.sha256(canonical_c138_raw).hexdigest() == CANONICAL_C138_FILE_SHA256, "canonical C138 file hash")
    canonical_c138 = json.loads(canonical_c138_raw)
    require(canonical_c138["integrity"]["payload_sha256"] == CANONICAL_C138_PAYLOAD_SHA256, "canonical C138 stored payload hash")
    require(canonical_hash({key: value for key, value in canonical_c138.items() if key != "integrity"}) == CANONICAL_C138_PAYLOAD_SHA256, "canonical C138 semantic payload hash")
    require(canonical_hash(canonical_c138["support"]) == SUPPORT_PAYLOAD_SHA256, "canonical C138 support-only hash")
    require(canonical_c138["support"] == data["support"], "C139 Y differs from canonical C138")
    support = parse_support(data)
    full_m16_audit(data)

    lines = global_lines()
    require(len(lines) == 150, "global event-line count")
    breakpoints = tuple(sorted({AMBIENT[0], AMBIENT[1], *crossing_phases(lines, *AMBIENT)}))
    require(len(breakpoints) == 564, "global phase breakpoint census")
    lower_index = breakpoints.index(CHAMBER[0])
    upper_index = breakpoints.index(CHAMBER[1])
    require((breakpoints[lower_index - 1], breakpoints[upper_index + 1]) == (ADJACENT[0][0], ADJACENT[1][1]), "immediate adjacent breakpoints")
    require(upper_index == lower_index + 1, "hidden global crossing inside feasible chamber")
    require(CHAMBER[0] < REFERENCE < CHAMBER[1], "reference outside chamber")

    affine = global_affine(REFERENCE, support)
    require(affine == EXPECTED_GLOBAL_AFFINE, "global affine functions")
    require({key: parse_affine(value) for key, value in data["global_affine"].items()} == EXPECTED_GLOBAL_AFFINE, "global affine metadata")
    require(affine["margin"][0] < 0, "margin monotonicity")
    require(affine_value(affine["margin"], CHAMBER[1]) == F(292559857297, 16716398592) > 0, "margin endpoint positivity")

    expected_audits = {
        CHAMBER[0]: (148, 147, 871, 305, 796, 380, 143, 4, F(163749, 2048), F(2365859438759, 16716398592)),
        REFERENCE: (150, 149, 884, 308, 807, 385, 145, 4, F(1305537, 16384), F(2367807877181, 16716398592)),
        CHAMBER[1]: (147, 146, 868, 300, 793, 375, 142, 4, F(326013, 4096), F(2368457356655, 16716398592)),
    }
    expected_endpoint_values = {
        "lower": (CHAMBER[0], F(163749, 2048), F(2365859438759, 16716398592), F(307278796633, 16716398592)),
        "reference": (REFERENCE, F(1305537, 16384), F(2367807877181, 16716398592), F(296239592131, 16716398592)),
        "upper": (CHAMBER[1], F(326013, 4096), F(2368457356655, 16716398592), F(292559857297, 16716398592)),
    }
    for label, expected in expected_endpoint_values.items():
        field = data["endpoint_values"][label]
        observed = tuple(parse_fraction(field[key]) for key in ("phase", "D", "P", "margin"))
        require(observed == expected and parse_fraction(field["pre8_integral"]) == F(6489, 256), f"endpoint metadata {label}")
    require(data["owner_audit"] == {
        "generic_open_chamber": {
            "distinct_events": 150, "cells": 149, "weighted_rows": 1192,
            "tight": 884, "strict": 308, "zero_capacity": 807, "positive_capacity": 385,
            "pre8_zero": 145, "pre8_positive": 4,
            "minimum_positive_slack": "5/65536", "minimum_positive_capacity": "5/65536",
            "all_weighted_rows_and_pre8_nonnegative": True,
        },
        "lower_collapsed_endpoint": {
            "distinct_events": 148, "cells": 147, "weighted_rows": 1176,
            "tight": 871, "strict": 305, "zero_capacity": 796, "positive_capacity": 380,
            "pre8_zero": 143, "pre8_positive": 4,
            "all_weighted_rows_and_pre8_nonnegative": True,
        },
        "upper_collapsed_endpoint": {
            "distinct_events": 147, "cells": 146, "weighted_rows": 1168,
            "tight": 868, "strict": 300, "zero_capacity": 793, "positive_capacity": 375,
            "pre8_zero": 142, "pre8_positive": 4,
            "all_weighted_rows_and_pre8_nonnegative": True,
        },
    }, "owner audit metadata")
    for phase, expected in expected_audits.items():
        audit = global_audit(phase, support)
        observed = (
            audit["events"], audit["cells"], audit["tight"], audit["strict"],
            audit["zero_capacity"], audit["positive_capacity"], audit["pre8_zero"],
            audit["pre8_positive"], audit["D"], audit["P"],
        )
        require(observed == expected, f"global endpoint/reference audit at {phase}")
        require(audit["min_gate"] >= 0, f"negative feasible gate at {phase}")
        require(audit["pre8_integral"] == F(6489, 256), f"pre8 integral at {phase}")
        require(audit["min_positive_slack"] == audit["min_positive_capacity"] == F(5, 65536), f"minimum positive gate at {phase}")
        for key in ("D", "P", "margin", "pre8"):
            actual = audit["pre8_integral"] if key == "pre8" else audit[key]
            require(actual == affine_value(affine[key], phase), f"affine endpoint value {key}")

    for spec in data["adjacent_failures"]:
        verify_failure(spec, support)
    require({spec["side"] for spec in data["adjacent_failures"]} == {"left", "right"}, "failure sides")
    by_side = {spec["side"]: spec for spec in data["adjacent_failures"]}
    require(tuple(map(parse_fraction, by_side["left"]["open_chamber"])) == ADJACENT[0], "left failure chamber")
    require(tuple(map(parse_fraction, by_side["right"]["open_chamber"])) == ADJACENT[1], "right failure chamber")
    for side, collapsed in (("left", CHAMBER[0]), ("right", CHAMBER[1])):
        spec = by_side[side]
        require(spec["cell"]["convention"] == "[left_line(t),right_line(t))", "countercell convention")
        require(parse_fraction(spec["cell"]["collapsed_at"]) == collapsed, "countercell collapsed endpoint")
        require(spec["exact_failure_throughout_open_chamber"] is True, "adjacent failure scope")

    ledger = data["same_atom_ledger"]
    require(len(ledger_lines()) == 203, "ledger event-line count")
    require(crossing_phases(ledger_lines(), *CHAMBER) == LEDGER_SPLITS[1:-1], "internal ledger crossings")
    require(tuple(map(parse_fraction, ledger["phase_splits"])) == LEDGER_SPLITS, "ledger split metadata")
    require(tuple(map(parse_fraction, ledger["internal_event_crossings"])) == LEDGER_SPLITS[1:-1], "internal ledger metadata")
    require(ledger["event_lines"] == 203, "ledger event-line metadata")
    expected_subchambers = tuple(zip(LEDGER_SPLITS, LEDGER_SPLITS[1:]))
    require(len(ledger["subchambers"]) == 3, "ledger subchamber count")
    for item, (lower, upper) in zip(ledger["subchambers"], expected_subchambers):
        require(tuple(map(parse_fraction, item["closed_limits"])) == (lower, upper), "ledger subchamber limits")
        sample = (lower + upper) / 2
        current = ledger_affine(sample)
        require(current == EXPECTED_LEDGER_AFFINE, "ledger affine replay")
        require({key: parse_affine(value) for key, value in item["integrated_rows"].items()} == EXPECTED_LEDGER_AFFINE, "ledger affine metadata")
    require([item["phase_piece"] for item in ledger["subchambers"]] == ["[4425/8,554)", "[554,1664/3)", "[1664/3,555]"], "ledger phase-piece convention")
    require(set(EXPECTED_LEDGER_AFFINE) == set(EXPECTED_REFERENCE_ROWS) and len(EXPECTED_LEDGER_AFFINE) == 14, "formal ledger rows")
    summed = (
        sum(pair[0] for pair in EXPECTED_LEDGER_AFFINE.values()),
        sum(pair[1] for pair in EXPECTED_LEDGER_AFFINE.values()),
    )
    require(summed == EXPECTED_GLOBAL_AFFINE["D"], "ledger rows do not sum to D(t)")
    boundary_counts = {
        CHAMBER[0]: (201, 200),
        F(554): (201, 200),
        F(1664, 3): (202, 201),
        CHAMBER[1]: (200, 199),
    }
    require(ledger["collapsed_event_counts"] == {
        "4425/8": {"events": 201, "cells": 200},
        "554/1": {"events": 201, "cells": 200},
        "1664/3": {"events": 202, "cells": 201},
        "555/1": {"events": 200, "cells": 199},
    }, "collapsed ledger metadata")
    for phase, counts in boundary_counts.items():
        audit = ledger_integral(phase)
        require((audit["events"], audit["cells"]) == counts, f"collapsed ledger count at {phase}")
        require(audit["terminal_checks"] == 3 * audit["cells"], f"terminal audit at {phase}")
        require(audit["rows"] == {
            key: affine_value(pair, phase) for key, pair in EXPECTED_LEDGER_AFFINE.items()
        }, f"ledger endpoint rows at {phase}")
        require(audit["total"] == affine_value(EXPECTED_GLOBAL_AFFINE["D"], phase), f"ledger endpoint total at {phase}")
    require(ledger_integral(REFERENCE)["rows"] == EXPECTED_REFERENCE_ROWS, "reference ledger rows")
    require({key: parse_fraction(value) for key, value in ledger["reference_integrated_rows"].items()} == EXPECTED_REFERENCE_ROWS, "reference ledger metadata")
    require(ledger["formal_rows"] == 14 and ledger["integrated_rows_sum_exactly_to_D_t"] is True, "formal ledger metadata")
    require(ledger["terminal_rows_retained"] is True and ledger["terminal_rows_identically_zero_on_chamber"] is True, "terminal metadata")

    print(
        "C139_EXACT_PHASE_CHAMBER_OK "
        f"closed=[{CHAMBER[0]},{CHAMBER[1]}] reference={REFERENCE} roots=57 rank=51 "
        f"D(t)={EXPECTED_GLOBAL_AFFINE['D']} P(t)={EXPECTED_GLOBAL_AFFINE['P']} "
        f"minimum_margin={affine_value(EXPECTED_GLOBAL_AFFINE['margin'], CHAMBER[1])} "
        "adjacent_slacks=-549/131072,-15/8192 ledger_splits=554,1664/3 "
        "formal_rows=14 terminals_retained C058_open"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

