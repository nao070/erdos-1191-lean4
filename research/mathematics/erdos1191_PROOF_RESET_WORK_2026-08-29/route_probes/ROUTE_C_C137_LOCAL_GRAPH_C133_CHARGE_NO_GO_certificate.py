#!/usr/bin/env python3
"""Exact C137 certificate: local graph-to-C133 charge-map no-go.

The claim is finite and deliberately narrow.  On one 32-mark fixture and one
phase, the complete 100-channel graph state is identical on exact pairs of
spatial cells while the one-sided box-carrier C133 ledger changes.  Hence no
pointwise memoryless function of that graph state can recover the ledger.
Nonlocal transport, an enlarged channel bank, and a new same-atom potential
remain open.  Nothing here resolves C058, Q1, or Q2.
"""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_C137_LOCAL_GRAPH_C133_CHARGE_NO_GO_certificate.json"
SCHEMA = "erdos1191.c137.local_graph_c133_charge_no_go.v1"
STATUS = "EXACT_LOCAL_GRAPH_TO_C133_BOX_CARRIER_CHARGE_NO_GO_C058_OPEN"

POINTS = (
    0, 22, 60, 83, 102, 173, 303, 513,
    616, 727, 772, 881, 972, 1041, 1103, 1169,
    1239, 1349, 1539, 1654, 2009, 2659, 3709, 3804,
    4114, 4339, 4794, 5124, 5639, 6184, 6739, 7084,
)
MULTIPLIERS = (1, 2, 4, 8)
PHASE = F(17745, 32)
WEIGHTS = {8: F(1), 16: F(9, 16)}
ACTIVE_SCALE_COEFFICIENTS = {scale: F(2**scale, 128) for scale in range(4)}

CHANNELS = tuple(
    (rank, multiplier, POINTS[rank])
    for multiplier in MULTIPLIERS
    for rank in range(7, 32)
)
CHANNEL_INDEX = {(rank, multiplier): index for index, (rank, multiplier, _) in enumerate(CHANNELS)}
DIRECT_OWNERS = tuple((epoch, multiplier) for multiplier in MULTIPLIERS for epoch in (8, 16))

# Exact positive graph-root support; labels are (rank,multiplier).
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
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    return hashlib.sha256(payload).hexdigest()


def fixture_audit() -> dict[str, Any]:
    if len(POINTS) != 32 or POINTS[0] != 0 or any(a >= b for a, b in zip(POINTS, POINTS[1:])):
        raise CertificateError("fixture ordering changed")
    differences = [POINTS[j] - POINTS[i] for i in range(32) for j in range(i + 1, 32)]
    if len(differences) != 496 or len(set(differences)) != 496:
        raise CertificateError("fixture lost Golomb/Sidon validity")
    if len(CHANNELS) != 100 or len(set(CHANNELS)) != 100:
        raise CertificateError("100-channel bank changed")
    return {
        "marks": 32,
        "span": 7084,
        "positive_differences": 496,
        "distinct_positive_differences": 496,
        "phase": ftext(PHASE),
        "channels": 100,
    }


def haar_sign(x: F, origin: int, width: F) -> int:
    displacement = x - origin
    return int(0 <= displacement < width) - int(width <= displacement < 2 * width)


def active_state(x: F) -> tuple[int, ...]:
    return tuple(
        (8 // multiplier) * haar_sign(x, origin, multiplier * PHASE)
        for _, multiplier, origin in CHANNELS
    )


def support_indices() -> tuple[tuple[int, int, F], ...]:
    rows: list[tuple[int, int, F]] = []
    seen: set[tuple[int, int]] = set()
    for left, right, coefficient in SUPPORT:
        i, j = CHANNEL_INDEX[left], CHANNEL_INDEX[right]
        if i > j:
            i, j = j, i
        if i == j or (i, j) in seen or coefficient <= 0:
            raise CertificateError("invalid graph root")
        seen.add((i, j))
        rows.append((i, j, coefficient))
    if len(rows) != 57:
        raise CertificateError("57-root support changed")
    return tuple(rows)


def graph_energy(state: Sequence[int], support: Sequence[tuple[int, int, F]]) -> F:
    return sum((coefficient * (state[i] - state[j]) ** 2 for i, j, coefficient in support), F(0))


def point_matrix(n: int) -> tuple[tuple[F, ...], ...]:
    base = tuple(tuple(
        F(0) if i == j or abs(i - j) == 1 else -F((j - i) ** 2, 8 * n * n)
        for j in range(n)
    ) for i in range(n))
    difference = tuple(
        tuple(F((k == i) - (k == i + 1)) for k in range(n + 1))
        for i in range(n)
    )
    return tuple(tuple(
        sum((difference[a][i] * base[a][b] * difference[b][j] for a in range(n) for b in range(n)), F(0))
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


def direct_demand(owner: tuple[int, int], state: Sequence[int]) -> F:
    epoch, multiplier = owner
    local = tuple(state[index] for index in direct_full_indices(owner))
    return F(multiplier, 128) * quadratic(POINT_MATRICES[epoch], local)


def carrier_density(prefix: int, scale: int, x: F) -> F:
    width = (2**scale) * PHASE
    active = sum(int(F(point) <= x < F(point) + width) for point in POINTS[:prefix])
    return F(active * active - active, width * width)


def c133_row_values(carrier: Mapping[tuple[int, int], F]) -> tuple[F, dict[str, F]]:
    prefix_coefficient: dict[int, F] = {}
    running = F(0)
    for scale in range(4):
        running += ACTIVE_SCALE_COEFFICIENTS[scale]
        prefix_coefficient[scale] = running

    rows: dict[str, F] = {}
    for scale in range(4):
        o8 = carrier[8, scale] - carrier[8, scale + 1]
        o16 = carrier[16, scale] - carrier[16, scale + 1]
        o32 = carrier[32, scale] - carrier[32, scale + 1]
        rows[f"band:A8:s{scale}"] = -WEIGHTS[8] * prefix_coefficient[scale] * o8
        rows[f"band:A16:s{scale}"] = (
            WEIGHTS[8] - WEIGHTS[16]
        ) * prefix_coefficient[scale] * o16
        rows[f"band:A32:s{scale}"] = WEIGHTS[16] * prefix_coefficient[scale] * o32
    rows["terminal:e8:s4"] = (
        WEIGHTS[8] * prefix_coefficient[3] * (carrier[16, 4] - carrier[8, 4])
    )
    rows["terminal:e16:s4"] = (
        WEIGHTS[16] * prefix_coefficient[3] * (carrier[32, 4] - carrier[16, 4])
    )
    lhs = sum((
        WEIGHTS[8] * ACTIVE_SCALE_COEFFICIENTS[scale] * (carrier[16, scale] - carrier[8, scale])
        + WEIGHTS[16] * ACTIVE_SCALE_COEFFICIENTS[scale] * (carrier[32, scale] - carrier[16, scale])
        for scale in range(4)
    ), F(0))
    if len(rows) != 14 or lhs != sum(rows.values(), F(0)):
        raise CertificateError("C133 fourteen-row identity failed")
    return lhs, rows


def joint_events() -> tuple[F, ...]:
    carrier_events = {
        F(point) + endpoint * (2**scale) * PHASE
        for point in POINTS
        for scale in range(5)
        for endpoint in (0, 1)
    }
    graph_events = {
        F(origin) + shift * multiplier * PHASE
        for _, multiplier, origin in CHANNELS
        for shift in (0, 1, 2)
    }
    if not graph_events.issubset(carrier_events):
        raise CertificateError("graph events not contained in joint refinement")
    events = tuple(sorted(carrier_events))
    if (len(events), events[0], events[-1]) != (192, F(0), F(31913, 2)):
        raise CertificateError("joint geometry changed")
    return events


def exact_cell(left: F, right: F) -> dict[str, Any]:
    events = joint_events()
    try:
        index = events.index(left)
    except ValueError as exc:
        raise CertificateError(f"not a joint left endpoint: {left}") from exc
    if index + 1 >= len(events) or events[index + 1] != right:
        raise CertificateError(f"not a joint cell: [{left},{right})")

    midpoint = (left + right) / 2
    state = active_state(midpoint)
    support = support_indices()
    root_features = tuple((state[i] - state[j]) ** 2 for i, j, _ in support)
    demands = tuple(direct_demand(owner, state) for owner in DIRECT_OWNERS)
    weighted_direct = sum((
        WEIGHTS[owner[0]] * demand for owner, demand in zip(DIRECT_OWNERS, demands)
    ), F(0))
    carrier = {
        (prefix, scale): carrier_density(prefix, scale, midpoint)
        for prefix in (8, 16, 32)
        for scale in range(5)
    }
    lhs, rows = c133_row_values(carrier)
    return {
        "state": state,
        "state_hash": canonical_hash(list(state)),
        "row_hash": canonical_hash({key: ftext(value) for key, value in rows.items()}),
        "root_features_all_zero": all(value == 0 for value in root_features),
        "graph_energy": graph_energy(state, support),
        "direct_demands": demands,
        "weighted_direct": weighted_direct,
        "lhs": lhs,
        "terminal_e8": rows["terminal:e8:s4"],
        "terminal_e16": rows["terminal:e16:s4"],
    }


def integrate() -> dict[str, F]:
    events = joint_events()
    support = support_indices()
    graph_price = F(0)
    direct_unweighted = F(0)
    direct_weighted = F(0)
    ledger_lhs = F(0)
    for left, right in zip(events, events[1:]):
        midpoint = (left + right) / 2
        length = right - left
        state = active_state(midpoint)
        graph_price += length * graph_energy(state, support)
        for owner in DIRECT_OWNERS:
            demand = direct_demand(owner, state)
            direct_unweighted += length * demand
            direct_weighted += length * WEIGHTS[owner[0]] * demand
        carrier = {
            (prefix, scale): carrier_density(prefix, scale, midpoint)
            for prefix in (8, 16, 32)
            for scale in range(5)
        }
        lhs, _ = c133_row_values(carrier)
        ledger_lhs += length * lhs
    values = {
        "P": graph_price,
        "D": direct_unweighted,
        "Dw": direct_weighted,
        "I": ledger_lhs,
    }
    if values != {
        "P": F(1878008419901, 9402974208),
        "D": F(457, 4),
        "Dw": F(1305537, 16384),
        "I": F(10229179, 1007632080),
    }:
        raise CertificateError("integrated values changed")
    return values


def public_cell(left: F, right: F, value: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "cell": [ftext(left), ftext(right)],
        "state_hash": value["state_hash"],
        "row_hash": value["row_hash"],
        "root_features_all_zero": value["root_features_all_zero"],
        "graph_energy": ftext(value["graph_energy"]),
        "direct_demands_all_zero": all(demand == 0 for demand in value["direct_demands"]),
        "weighted_direct": ftext(value["weighted_direct"]),
        "C133_lhs": ftext(value["lhs"]),
        "terminal_e8": ftext(value["terminal_e8"]),
        "terminal_e16": ftext(value["terminal_e16"]),
    }


def build_payload() -> dict[str, Any]:
    total_left = (F(616), F(20401, 32))
    total_right = (F(20401, 32), F(21009, 32))
    terminal_left = (F(35101, 4), F(17745, 2))
    terminal_right = (F(17745, 2), F(17789, 2))
    epoch16_zero = (F(23063, 2), F(25163, 2))
    graph_positive = (F(513), F(17745, 32))
    direct_positive = (F(44701, 4), F(46081, 4))

    a = exact_cell(*total_left)
    b = exact_cell(*total_right)
    ta = exact_cell(*terminal_left)
    tb = exact_cell(*terminal_right)
    e16 = exact_cell(*epoch16_zero)
    gp = exact_cell(*graph_positive)
    dp = exact_cell(*direct_positive)

    if (
        a["state"] != b["state"]
        or a["lhs"] != F(64, 104961675)
        or b["lhs"] != F(176, 314885025)
        or a["row_hash"] == b["row_hash"]
        or not a["root_features_all_zero"]
        or not b["root_features_all_zero"]
        or any(a["direct_demands"])
        or any(b["direct_demands"])
        or a["terminal_e8"] != F(1, 41984670)
    ):
        raise CertificateError("total state-collision gate changed")
    if (
        ta["state"] != tb["state"]
        or ta["lhs"] != F(17, 279897800)
        or tb["lhs"] != F(17, 279897800)
        or (ta["terminal_e8"], tb["terminal_e8"])
        != (F(23, 83969340), F(1, 3998540))
        or (ta["terminal_e16"], tb["terminal_e16"])
        != (F(141, 223918240), F(27, 44783648))
    ):
        raise CertificateError("terminal state-collision gate changed")
    if (
        not e16["root_features_all_zero"]
        or any(e16["direct_demands"])
        or e16["terminal_e16"] != F(27, 358269184)
    ):
        raise CertificateError("epoch-16 terminal zero-capacity gate changed")
    if gp["graph_energy"] != F(21, 256) or gp["lhs"] != 0:
        raise CertificateError("graph-positive/ledger-zero gate changed")
    if dp["weighted_direct"] != F(225, 32768) or dp["lhs"] != 0:
        raise CertificateError("direct-positive/ledger-zero gate changed")

    totals = integrate()
    return {
        "fixture": {
            **fixture_audit(),
            "supported_graph_roots": len(support_indices()),
            "support_sha256": canonical_hash([
                [[*left], [*right], ftext(coefficient)]
                for left, right, coefficient in SUPPORT
            ]),
            "joint_events": len(joint_events()),
            "joint_cells": len(joint_events()) - 1,
        },
        "same_state_different_C133_total": {
            "cell_a": public_cell(*total_left, a),
            "cell_b": public_cell(*total_right, b),
        },
        "same_state_different_terminal_rows": {
            "cell_a": public_cell(*terminal_left, ta),
            "cell_b": public_cell(*terminal_right, tb),
        },
        "zero_capacity_epoch16_terminal": public_cell(*epoch16_zero, e16),
        "positive_graph_zero_ledger": public_cell(*graph_positive, gp),
        "positive_direct_zero_ledger": public_cell(*direct_positive, dp),
        "integrated_values": {
            "graph_price_P": ftext(totals["P"]),
            "unweighted_direct_D": ftext(totals["D"]),
            "weighted_direct_Dw": ftext(totals["Dw"]),
            "box_carrier_C133_integral_I": ftext(totals["I"]),
            "post_hoc_ratio_P_over_I": ftext(totals["P"] / totals["I"]),
            "post_hoc_ratio_D_over_I": ftext(totals["D"] / totals["I"]),
            "post_hoc_ratio_Dw_over_I": ftext(totals["Dw"] / totals["I"]),
        },
        "proved_no_go_classes": {
            "arbitrary_pointwise_function_full_state_to_C133_total": True,
            "arbitrary_pointwise_function_full_state_to_14row_vector": True,
            "arbitrary_pointwise_function_full_state_to_both_terminals": True,
            "affine_or_linear_map_supported_root_features_to_C133_ledger": True,
            "owner_block_or_multiplier_diagonal_pointwise_map": True,
            "constant_pointwise_graph_or_direct_scalar_identification": True,
            "finite_pointwise_graph_domination_of_positive_C133_total": True,
        },
        "scope": {
            "single_explicit_32_mark_fixture_only": True,
            "single_phase_17745_over_32_only": True,
            "current_100_channel_57_root_graph_only": True,
            "one_sided_box_pair_carrier_only": True,
            "rules_out_nonlocal_cross_cell_transport": False,
            "rules_out_phase_integrated_signed_transport": False,
            "rules_out_same_atom_M8_M16_potential": False,
            "rules_out_enlarged_channel_bank": False,
            "C058_resolved": False,
            "Q1_resolved": False,
            "Q2_resolved": False,
        },
        "next_missing_hypothesis": (
            "Construct a potential from the same signed M8/M16 atoms as the direct demands, "
            "or prove a genuinely nonlocal transport identity.  It must carry the initial A8 "
            "history and both scale-4 terminal balances without fixture-fitted coefficients "
            "or future information."
        ),
    }


def build_certificate() -> dict[str, Any]:
    payload = build_payload()
    return {
        "schema": SCHEMA,
        "status": STATUS,
        "payload_sha256": canonical_hash(payload),
        "payload": payload,
    }


def reject_floats(value: object, path: str = "root") -> None:
    if isinstance(value, float):
        raise CertificateError(f"float rejected at {path}")
    if isinstance(value, Mapping):
        for key, item in value.items():
            reject_floats(item, f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            reject_floats(item, f"{path}[{index}]")


def validate_certificate(value: Mapping[str, Any]) -> dict[str, Any]:
    reject_floats(value)
    expected = build_certificate()
    if value != expected:
        raise CertificateError("certificate differs from exact recomputation")
    if value.get("payload_sha256") != canonical_hash(value.get("payload")):
        raise CertificateError("payload hash mismatch")
    return dict(value)


def mutation_self_check(value: Mapping[str, Any]) -> dict[str, int]:
    mutations = (
        (("status",), "C058_PROVED"),
        (("payload", "same_state_different_C133_total", "cell_b", "C133_lhs"), "64/104961675"),
        (("payload", "same_state_different_C133_total", "cell_b", "state_hash"), "f" * 64),
        (("payload", "same_state_different_C133_total", "cell_a", "terminal_e8"), "0/1"),
        (("payload", "zero_capacity_epoch16_terminal", "terminal_e16"), "0/1"),
        (("payload", "positive_graph_zero_ledger", "graph_energy"), "0/1"),
        (("payload", "positive_direct_zero_ledger", "weighted_direct"), "0/1"),
        (("payload", "scope", "C058_resolved"), True),
    )
    rejected = 0
    for path, replacement in mutations:
        mutant = copy.deepcopy(value)
        cursor: Any = mutant
        for key in path[:-1]:
            cursor = cursor[key]
        cursor[path[-1]] = replacement
        try:
            validate_certificate(mutant)
        except CertificateError:
            rejected += 1
    if rejected != len(mutations):
        raise CertificateError("mutation gate accepted a corrupted certificate")
    return {"mutations": len(mutations), "rejected": rejected}


def load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(
            handle,
            parse_float=lambda _: (_ for _ in ()).throw(CertificateError("float rejected")),
        )
    if not isinstance(value, dict):
        raise CertificateError("certificate root must be an object")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--emit-json", action="store_true")
    args = parser.parse_args()

    value = validate_certificate(load(args.certificate) if args.verify else build_certificate())
    if args.self_check:
        mutation = mutation_self_check(value)
        print(f"MUTATION_OK rejected={mutation['rejected']}/{mutation['mutations']}")
    if args.emit_json:
        print(json.dumps(value, indent=2, sort_keys=True))
    else:
        collision = value["payload"]["same_state_different_C133_total"]
        print(
            "C137_LOCAL_CHARGE_NO_GO_OK "
            f"state={collision['cell_a']['state_hash'][:12]} "
            f"lhsA={collision['cell_a']['C133_lhs']} "
            f"lhsB={collision['cell_b']['C133_lhs']} "
            "C058_open"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
