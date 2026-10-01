#!/usr/bin/env python3
"""Stdlib-only independent oracle for the load-bearing C137 state collisions.

This file does not import the main verifier.  It independently reconstructs
the 100-channel Haar state and the fourteen-row one-sided box-carrier ledger.
"""

from __future__ import annotations

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping


HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE / "ROUTE_C_C137_LOCAL_GRAPH_C133_CHARGE_NO_GO_certificate.json"

POINTS = (
    0, 22, 60, 83, 102, 173, 303, 513,
    616, 727, 772, 881, 972, 1041, 1103, 1169,
    1239, 1349, 1539, 1654, 2009, 2659, 3709, 3804,
    4114, 4339, 4794, 5124, 5639, 6184, 6739, 7084,
)
PHASE = F(17745, 32)
MULTIPLIERS = (1, 2, 4, 8)
WEIGHT8 = F(1)
WEIGHT16 = F(9, 16)
CHANNELS = tuple(
    (rank, multiplier, POINTS[rank])
    for multiplier in MULTIPLIERS
    for rank in range(7, 32)
)
CHANNEL_INDEX = {(rank, multiplier): index for index, (rank, multiplier, _) in enumerate(CHANNELS)}

# Root labels only.  Coefficients are irrelevant to the zero-feature gates.
ROOT_LABELS = (
    ((7, 1), (8, 1)), ((13, 1), (15, 1)), ((14, 1), (15, 1)),
    ((15, 1), (16, 1)), ((16, 1), (17, 1)), ((16, 1), (16, 2)),
    ((17, 1), (18, 1)), ((18, 1), (19, 1)), ((18, 1), (18, 2)),
    ((18, 1), (26, 4)), ((19, 1), (24, 4)), ((22, 1), (16, 4)),
    ((22, 1), (19, 4)), ((23, 1), (26, 2)), ((24, 1), (22, 2)),
    ((24, 1), (25, 2)), ((29, 1), (28, 2)), ((15, 2), (16, 2)),
    ((16, 2), (17, 2)), ((16, 2), (18, 2)), ((17, 2), (20, 2)),
    ((18, 2), (19, 2)), ((21, 2), (26, 4)), ((22, 2), (23, 2)),
    ((23, 2), (20, 4)), ((25, 2), (20, 4)), ((25, 2), (22, 4)),
    ((26, 2), (22, 4)), ((28, 2), (27, 4)), ((29, 2), (27, 4)),
    ((30, 2), (31, 2)), ((31, 2), (26, 4)), ((15, 4), (16, 4)),
    ((16, 4), (17, 4)), ((16, 4), (19, 4)), ((16, 4), (22, 4)),
    ((16, 4), (24, 4)), ((16, 4), (26, 4)), ((18, 4), (19, 4)),
    ((20, 4), (21, 4)), ((24, 4), (31, 4)), ((25, 4), (31, 4)),
    ((26, 4), (31, 4)), ((27, 4), (28, 4)), ((28, 4), (29, 4)),
    ((29, 4), (31, 4)), ((30, 4), (31, 4)), ((15, 8), (16, 8)),
    ((15, 8), (17, 8)), ((16, 8), (18, 8)), ((17, 8), (18, 8)),
    ((18, 8), (21, 8)), ((19, 8), (20, 8)), ((20, 8), (21, 8)),
    ((28, 8), (29, 8)), ((28, 8), (30, 8)), ((30, 8), (31, 8)),
)


class OracleError(RuntimeError):
    pass


def ftext(value: F | int) -> str:
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def canonical_hash(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    return hashlib.sha256(encoded).hexdigest()


def reject_floats(value: object) -> None:
    if isinstance(value, float):
        raise OracleError("float in certificate")
    if isinstance(value, Mapping):
        for item in value.values():
            reject_floats(item)
    elif isinstance(value, list):
        for item in value:
            reject_floats(item)


def sign_wave(x: F, origin: int, half_width: F) -> int:
    if F(origin) <= x < F(origin) + half_width:
        return 1
    if F(origin) + half_width <= x < F(origin) + 2 * half_width:
        return -1
    return 0


def state_at(x: F) -> tuple[int, ...]:
    values = []
    for _, multiplier, origin in CHANNELS:
        values.append((8 // multiplier) * sign_wave(x, origin, multiplier * PHASE))
    return tuple(values)


def carrier(prefix: int, scale: int, x: F) -> F:
    width = (2**scale) * PHASE
    count = 0
    for point in POINTS[:prefix]:
        if F(point) <= x < F(point) + width:
            count += 1
    return F(count * (count - 1), width * width)


def ledger_at(x: F) -> tuple[F, dict[str, F]]:
    values = {(prefix, scale): carrier(prefix, scale, x) for prefix in (8, 16, 32) for scale in range(5)}
    cumulative = []
    running = F(0)
    for scale in range(4):
        running += F(2**scale, 128)
        cumulative.append(running)

    rows: dict[str, F] = {}
    for scale, coefficient in enumerate(cumulative):
        d8 = values[8, scale] - values[8, scale + 1]
        d16 = values[16, scale] - values[16, scale + 1]
        d32 = values[32, scale] - values[32, scale + 1]
        rows[f"band:A8:s{scale}"] = -WEIGHT8 * coefficient * d8
        rows[f"band:A16:s{scale}"] = (WEIGHT8 - WEIGHT16) * coefficient * d16
        rows[f"band:A32:s{scale}"] = WEIGHT16 * coefficient * d32
    rows["terminal:e8:s4"] = WEIGHT8 * cumulative[3] * (values[16, 4] - values[8, 4])
    rows["terminal:e16:s4"] = WEIGHT16 * cumulative[3] * (values[32, 4] - values[16, 4])

    lhs = F(0)
    for scale in range(4):
        coefficient = F(2**scale, 128)
        lhs += WEIGHT8 * coefficient * (values[16, scale] - values[8, scale])
        lhs += WEIGHT16 * coefficient * (values[32, scale] - values[16, scale])
    if lhs != sum(rows.values(), F(0)):
        raise OracleError("independent C133 identity failed")
    return lhs, rows


def exact_cell(left: F, right: F) -> dict[str, Any]:
    events = sorted({
        F(point) + endpoint * (2**scale) * PHASE
        for point in POINTS
        for scale in range(5)
        for endpoint in (0, 1)
    })
    index = events.index(left)
    if events[index + 1] != right:
        raise OracleError("oracle witness is not a carrier cell")
    midpoint = (left + right) / 2
    state = state_at(midpoint)
    lhs, rows = ledger_at(midpoint)
    features = tuple(
        (state[CHANNEL_INDEX[left_label]] - state[CHANNEL_INDEX[right_label]]) ** 2
        for left_label, right_label in ROOT_LABELS
    )
    return {
        "state": state,
        "state_hash": canonical_hash(list(state)),
        "row_hash": canonical_hash({key: ftext(value) for key, value in rows.items()}),
        "root_zero": all(value == 0 for value in features),
        "lhs": lhs,
        "terminal_e8": rows["terminal:e8:s4"],
        "terminal_e16": rows["terminal:e16:s4"],
    }


def verify() -> None:
    with CERTIFICATE.open("r", encoding="utf-8") as handle:
        stored = json.load(handle, parse_float=lambda _: (_ for _ in ()).throw(OracleError("float")))
    reject_floats(stored)
    if stored.get("schema") != "erdos1191.c137.local_graph_c133_charge_no_go.v1":
        raise OracleError("schema mismatch")
    if stored.get("status") != "EXACT_LOCAL_GRAPH_TO_C133_BOX_CARRIER_CHARGE_NO_GO_C058_OPEN":
        raise OracleError("status mismatch")
    payload = stored.get("payload")
    if not isinstance(payload, Mapping):
        raise OracleError("payload missing")
    if stored.get("payload_sha256") != canonical_hash(payload):
        raise OracleError("payload hash mismatch")

    differences = {POINTS[j] - POINTS[i] for i in range(32) for j in range(i + 1, 32)}
    fixture = payload["fixture"]
    if len(differences) != 496 or len(CHANNELS) != 100 or len(ROOT_LABELS) != 57:
        raise OracleError("fixture/channel/root census mismatch")
    if (fixture["channels"], fixture["supported_graph_roots"], fixture["phase"]) != (100, 57, "17745/32"):
        raise OracleError("stored fixture mismatch")

    a = exact_cell(F(616), F(20401, 32))
    b = exact_cell(F(20401, 32), F(21009, 32))
    if (
        a["state"] != b["state"]
        or a["lhs"] != F(64, 104961675)
        or b["lhs"] != F(176, 314885025)
        or a["row_hash"] == b["row_hash"]
        or not a["root_zero"]
        or not b["root_zero"]
        or a["terminal_e8"] != F(1, 41984670)
    ):
        raise OracleError("independent total collision failed")
    saved = payload["same_state_different_C133_total"]
    if (
        saved["cell_a"]["state_hash"] != a["state_hash"]
        or saved["cell_b"]["state_hash"] != b["state_hash"]
        or saved["cell_a"]["C133_lhs"] != ftext(a["lhs"])
        or saved["cell_b"]["C133_lhs"] != ftext(b["lhs"])
    ):
        raise OracleError("stored total collision differs")

    ta = exact_cell(F(35101, 4), F(17745, 2))
    tb = exact_cell(F(17745, 2), F(17789, 2))
    if (
        ta["state"] != tb["state"]
        or (ta["terminal_e8"], tb["terminal_e8"])
        != (F(23, 83969340), F(1, 3998540))
        or (ta["terminal_e16"], tb["terminal_e16"])
        != (F(141, 223918240), F(27, 44783648))
    ):
        raise OracleError("independent terminal collision failed")
    saved_terminal = payload["same_state_different_terminal_rows"]
    if (
        saved_terminal["cell_a"]["state_hash"] != ta["state_hash"]
        or saved_terminal["cell_b"]["state_hash"] != tb["state_hash"]
        or saved_terminal["cell_a"]["terminal_e8"] != ftext(ta["terminal_e8"])
        or saved_terminal["cell_b"]["terminal_e16"] != ftext(tb["terminal_e16"])
    ):
        raise OracleError("stored terminal collision differs")

    e16 = exact_cell(F(23063, 2), F(25163, 2))
    if not e16["root_zero"] or e16["terminal_e16"] != F(27, 358269184):
        raise OracleError("independent epoch-16 zero-root terminal witness failed")
    scope = payload["scope"]
    if scope["C058_resolved"] or scope["rules_out_nonlocal_cross_cell_transport"]:
        raise OracleError("scope upgrade detected")


def main() -> int:
    verify()
    print(
        "C137_INDEPENDENT_ORACLE_OK "
        "full_state_collision terminal_collision root_zero_terminals C058_open"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
