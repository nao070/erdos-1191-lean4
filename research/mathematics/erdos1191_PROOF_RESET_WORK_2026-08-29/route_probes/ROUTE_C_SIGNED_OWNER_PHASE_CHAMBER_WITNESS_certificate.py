#!/usr/bin/env python3
"""Exact fixed-midpoint rational PSD witness for the signed owner model.

This certificate checks only t=4835/48.  It does not certify a phase
interval, the legality of the proposed whole-stencil accounting, C058, either
Erdos question, novelty, or any prize claim.
"""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
import json
from functools import lru_cache
from pathlib import Path
import sys
from typing import Mapping

import direct_b_membership_sddm_lp_certificate as membership


SCHEMA = "erdos1191.route_c_signed_owner_phase_chamber_witness.v1"
STATUS = "EXACT_FIXED_RATIONAL_PSD_PHASE_MIDPOINT_WITNESS_C058_OPEN"
HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_SIGNED_OWNER_PHASE_CHAMBER_WITNESS_certificate.json"

BASE_WIDTH = F(4835, 48)
WIDTH_MULTIPLIERS = (1, 2, 4, 8)
UPPER_TERMINAL_WIDTH = 16 * BASE_WIDTH
POINTS = tuple(k * (k + 100) for k in range(16))
CHANNELS = tuple(
    (rank, multiplier, POINTS[rank])
    for multiplier in WIDTH_MULTIPLIERS
    for rank in range(3, 16)
)
OWNER_ORDER = tuple(
    (n, multiplier) for multiplier in WIDTH_MULTIPLIERS for n in (4, 8)
)

PSD_FACTOR_DENOMINATOR = 2_000_000
PSD_FACTOR_COLUMNS = (
    (-1493, -920, 411, 383, -449, 65, 359, -20, 22, -97, -17, 103,
     -24, -799, -1526, 208, 2213, -185, 283, 1098, 1731, 672, -308,
     627, 189, 166, 7447, -3138, -4753, 1097, 6179, -1750, -18, 139,
     -68, 2485, -1884, -268, 837, 993, -5619, -8327, 1574, 20983,
     -14238, -3568, 2771, -3725, -1018, -1696, 1478, 1395),
    (40, -1226, -19, 1526, 449, -3, 149, -282, -113, 1115, -608, 273,
     -4, 2467, -3064, -4467, -2024, 846, 653, 732, 109, 846, 454,
     -408, -826, -516, -1746, 4432, -1029, -1826, -786, 897, -1282,
     2083, 553, -2268, 6456, -2796, 1934, -4899, 11798, 2436, -16258,
     7440, -1439, 509, -773, 3939, -4574, 63, 286, 751),
    (-1061, -699, 428, -172, 660, -62, 107, -493, 78, 117, 812, 102,
     14, -1253, -3186, -981, 1681, 677, -439, -533, 388, 13, 218,
     -657, 4, 1246, 7442, -1653, -5480, 309, 7472, -2355, -1079, 43,
     -2383, 1391, -3027, -2345, 2398, -1082, 3965, -8304, -946, -2435,
     11995, -2142, 2993, 676, -3438, -799, -665, 2440),
    (383, 614, -95, 113, -594, -261, 343, 312, -155, 429, -8, -68, 68,
     58, 2071, 969, -70, -257, -2459, -946, -1008, -1698, -406, -564,
     205, 1037, -651, -20, 1390, 1353, 1139, -1974, 898, 2272, -2454,
     166, 3123, -3386, 4931, -1512, -6595, 7672, -1192, 3808, 4940,
     -10364, -516, -1750, -1090, 1800, -7801, 7800),
    (-960, -1061, -248, 623, 412, -214, 65, 3, 279, -660, -87, 17, 29,
     2077, -31, 630, -50, 170, 47, -1162, -1142, 967, 653, 903, -65,
     -76, 1352, -4873, 1697, 124, 1594, 4433, 220, 2869, 1890, 4265,
     942, -3042, 5129, -4095, 1475, -947, 329, -6126, -6417, -1682,
     2566, 1290, -571, -2313, -2685, 1457),
    (491, 733, 690, -859, -2, -229, -160, 20, 248, -233, -430, 104, -2,
     472, -219, 3900, 3347, 491, 441, -806, -1194, 282, 344, -538,
     -815, 593, -1662, -512, -1240, 1577, -3160, 3317, 1577, -4537,
     -69, 1202, 204, 818, -1909, -3088, 4045, -2646, 1750, 2278, 1116,
     -3111, -3747, 608, 1737, -1257, -3283, 3323),
    (-944, -1207, 228, 307, 8, 207, 51, 75, -111, -254, -348, 87, -43,
     1507, -1990, -1172, 113, 1097, -367, 993, -704, -17, -1145,
     -1018, -745, 365, -1225, 1227, -1995, 2311, -1770, -50, 5510,
     3360, 1205, 2325, 2092, 279, -2422, 3809, -1689, -3244, -3244,
     -1510, 268, -543, 1540, -2027, 2837, -405, -2223, 611),
    (587, 537, -95, 155, -544, -378, -276, 352, 639, 5, 458, 70, 17,
     -730, 515, -247, -1792, -118, 177, -283, 776, 164, -283, -1667,
     -104, 2095, -2111, -58, 1665, -1272, -1320, -5434, -551, -517,
     -72, 4651, -1062, -1873, 3651, 3381, 3516, -1268, 945, 441,
     -781, -289, -2365, -542, 1056, -170, -295, 644),
    (-135, -379, 51, 209, 95, 288, 72, -177, 53, 72, 302, 77, -111,
     874, 384, -87, 450, -684, 980, 1533, -151, -306, -66, -663, 888,
     -268, 103, -840, -194, 1673, -770, -3273, 2529, 1346, -1214,
     -1238, -980, 1161, 516, -3231, 699, 217, 700, -223, -538, 965,
     -269, -330, -542, 177, -255, 510),
    (173, 333, 64, -176, -32, 13, 10, -80, 147, 98, -298, -1, -67,
     -504, 88, 333, 113, -221, 283, 217, 31, 135, 413, 119, -1547,
     46, 567, -572, -137, -78, 247, -994, -607, -371, -104, -202,
     2488, -807, -1179, -389, 1221, 278, 866, -366, -348, 158, 1337,
     -1943, 497, 1526, -254, -524),
    (-134, -1, 64, 15, -47, -180, -59, 74, 8, 49, 180, 26, -101, 49,
     -246, 314, 186, 229, -43, -394, 76, 104, 503, -195, 327, 460,
     288, -732, -505, 126, 369, -400, -376, 123, 279, -481, 417, 903,
     1, 469, 29, 274, -456, -422, -335, -238, -865, -42, 143, -27,
     -48, 242),
)


class CertificateError(RuntimeError):
    """Raised when an exact witness, scope gate, or byte replay fails."""


def ftext(value: F | int) -> str:
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def _haar_sign(x: F, origin: int, width: F) -> int:
    displacement = x - origin
    if 0 <= displacement < width:
        return 1
    if width <= displacement < 2 * width:
        return -1
    return 0


@lru_cache(maxsize=1)
def _geometry() -> tuple[
    tuple[F, ...], tuple[tuple[F, F], ...], tuple[tuple[int, ...], ...]
]:
    events = tuple(
        sorted(
            {
                F(origin) + shift * multiplier * BASE_WIDTH
                for _, multiplier, origin in CHANNELS
                for shift in (0, 1, 2)
            }
        )
    )
    cells = tuple(zip(events, events[1:]))
    states = tuple(
        tuple(
            (8 // multiplier)
            * _haar_sign(left, origin, multiplier * BASE_WIDTH)
            for _, multiplier, origin in CHANNELS
        )
        for left, _ in cells
    )
    if (len(CHANNELS), len(events), len(cells)) != (52, 78, 77):
        raise CertificateError("52/78/77 midpoint fixture census changed")
    exterior_points = (events[0] - 1, events[-1])
    for point in exterior_points:
        exterior_state = tuple(
            (8 // multiplier)
            * _haar_sign(point, origin, multiplier * BASE_WIDTH)
            for _, multiplier, origin in CHANNELS
        )
        if any(exterior_state):
            raise CertificateError("a zero exterior cell became active")
    return events, cells, states


def _owner_full_indices(owner: tuple[int, int]) -> tuple[int, ...]:
    n, multiplier = owner
    ranks = range(3, 8) if n == 4 else range(7, 16)
    return tuple(
        CHANNELS.index((rank, multiplier, POINTS[rank])) for rank in ranks
    )


def _owner_group_indices(owner: tuple[int, int]) -> tuple[int, ...]:
    n, multiplier = owner
    ranks = range(3, 8) if n == 4 else range(8, 16)
    return tuple(
        CHANNELS.index((rank, multiplier, POINTS[rank])) for rank in ranks
    )


def _quadratic(matrix: tuple[tuple[F, ...], ...], vector: tuple[int, ...]) -> F:
    return sum(
        (
            F(vector[i]) * matrix[i][j] * vector[j]
            for i in range(len(vector))
            for j in range(len(vector))
        ),
        F(0),
    )


def _demand(owner: tuple[int, int], state: tuple[int, ...]) -> F:
    n, multiplier = owner
    indices = _owner_full_indices(owner)
    local = tuple(state[index] for index in indices)
    matrix = membership.point_m_matrix(n)
    return F(multiplier, 128 * BASE_WIDTH) * _quadratic(matrix, local)


def _factor_integer_dot(
    indices: tuple[int, ...],
    state: tuple[int, ...],
    column: tuple[int, ...],
) -> int:
    return sum(state[index] * column[index] for index in indices)


def _witness_audit() -> tuple[dict[str, object], dict[str, str]]:
    if len(PSD_FACTOR_COLUMNS) != 11:
        raise CertificateError("PSD factor rank changed")
    if any(len(column) != 52 for column in PSD_FACTOR_COLUMNS):
        raise CertificateError("PSD factor coordinate count changed")
    if any(sum(column) != 0 for column in PSD_FACTOR_COLUMNS):
        raise CertificateError("PSD factor lost exact zero column sums")

    _, cells, states = _geometry()
    all_indices = tuple(range(52))
    slacks: list[F] = []
    price = F(0)
    integrated = {owner: F(0) for owner in OWNER_ORDER}
    ownership_identity_checks = 0

    for (left, right), state in zip(cells, states):
        total_dots = tuple(
            _factor_integer_dot(all_indices, state, column)
            for column in PSD_FACTOR_COLUMNS
        )
        physical_numerator = sum(value * value for value in total_dots)
        physical = F(
            physical_numerator,
            PSD_FACTOR_DENOMINATOR * PSD_FACTOR_DENOMINATOR,
        )
        price += (right - left) * physical

        total_owned = F(0)
        for owner in OWNER_ORDER:
            group = _owner_group_indices(owner)
            group_dots = tuple(
                _factor_integer_dot(group, state, column)
                for column in PSD_FACTOR_COLUMNS
            )
            owned = F(
                sum(left_dot * right_dot for left_dot, right_dot in zip(group_dots, total_dots)),
                PSD_FACTOR_DENOMINATOR * PSD_FACTOR_DENOMINATOR,
            )
            demand = _demand(owner, state)
            slack = owned - demand
            if slack < 0:
                raise CertificateError(
                    f"rational midpoint witness violates owner {owner} on {(left, right)}"
                )
            slacks.append(slack)
            integrated[owner] += (right - left) * demand
            total_owned += owned
        if total_owned != physical:
            raise CertificateError("owner shares do not recover physical energy")
        ownership_identity_checks += 1

    integrated_demand = sum(integrated.values(), F(0))
    margin = 2 * integrated_demand - price
    positive_slacks = tuple(slack for slack in slacks if slack > 0)
    if integrated_demand != F(6221, 30944):
        raise CertificateError("integrated demand changed")
    if price != F(951134501701, 3000000000000):
        raise CertificateError("physical price changed")
    if margin != F(246690436855133, 2901000000000000) or margin <= 0:
        raise CertificateError("positive 2D-P margin changed")
    if len(slacks) != 616 or sum(slack == 0 for slack in slacks) != 259:
        raise CertificateError("owner-row slack census changed")
    if min(positive_slacks) != F(40498647, 1934000000000000):
        raise CertificateError("minimum positive owner-row slack changed")

    witness = {
        "coordinate_scaling": "q=16*t*h=(8*t/T)*g",
        "factor_shape": [52, 11],
        "factor_common_denominator": PSD_FACTOR_DENOMINATOR,
        "factor_integer_columns": [list(column) for column in PSD_FACTOR_COLUMNS],
        "maximum_factor_integer_absolute_value": max(
            abs(value) for column in PSD_FACTOR_COLUMNS for value in column
        ),
        "zero_row_sum_exact": True,
        "PSD_by_rational_Gram_factor": True,
        "owner_rows_checked": len(slacks),
        "all_owner_rows_feasible_exactly": True,
        "tight_owner_row_count": sum(slack == 0 for slack in slacks),
        "strictly_positive_owner_row_count": len(positive_slacks),
        "minimum_owner_row_slack": ftext(min(slacks)),
        "minimum_positive_owner_row_slack": ftext(min(positive_slacks)),
        "pointwise_owner_energy_identities_checked": ownership_identity_checks,
        "integrated_signed_demand": ftext(integrated_demand),
        "twice_integrated_signed_demand": ftext(2 * integrated_demand),
        "physical_price": ftext(price),
        "below_twice_demand_margin": ftext(margin),
        "positive_2D_minus_P": True,
        "exact_PSD_optimum_claimed": False,
    }
    integrated_text = {
        f"n{n}_T{multiplier}t": ftext(value)
        for (n, multiplier), value in integrated.items()
    }
    return witness, integrated_text


def payload_hash(certificate: Mapping[str, object]) -> str:
    payload = {key: value for key, value in certificate.items() if key != "integrity"}
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _build_uncached() -> dict[str, object]:
    witness, owner_integrals = _witness_audit()
    events, cells, _ = _geometry()
    groups = tuple(
        set(_owner_group_indices(owner)) for owner in OWNER_ORDER
    )
    union = set().union(*groups)
    if len(union) != 52 or sum(len(group) for group in groups) != 52:
        raise CertificateError("owner coordinate groups do not form a partition")

    certificate: dict[str, object] = {
        "schema": SCHEMA,
        "status": STATUS,
        "scope": {
            "fixed_midpoint_fixture_only": True,
            "one_exact_rational_PSD_feasible_witness": True,
            "exact_PSD_optimum_known": False,
            "continuum_phase_interval_proved": False,
            "adjacent_phase_chambers_proved": False,
            "finite_whole_stencil_accounting_legal_proved": False,
            "C067_terminal_or_Gothic_ledger_included": False,
            "directed_current_to_past_source_map_constructed": False,
            "compatible_infinite_history_constructed": False,
            "C058_Q1_Q2_proved": False,
            "publication_novelty_or_prize_claimed": False,
        },
        "fixture": {
            "tower": "a_k=k(k+100), 0<=k<=15",
            "base_width": ftext(BASE_WIDTH),
            "widths": [
                ftext(multiplier * BASE_WIDTH)
                for multiplier in WIDTH_MULTIPLIERS
            ],
            "upper_terminal_width": ftext(UPPER_TERMINAL_WIDTH),
            "epochs": [4, 8],
            "coordinate_order": [
                f"T{multiplier}t:a{rank}"
                for rank, multiplier, _ in CHANNELS
            ],
            "physical_coordinate_count": len(CHANNELS),
            "finite_event_count": len(events),
            "positive_length_cell_count": len(cells),
            "zero_exterior_cells_checked": 2,
            "first_event": ftext(events[0]),
            "last_event": ftext(events[-1]),
            "owner_order": [
                f"n{n}_T{multiplier}t" for n, multiplier in OWNER_ORDER
            ],
            "owner_count": len(OWNER_ORDER),
            "owner_cell_row_count": len(OWNER_ORDER) * len(cells),
            "coordinate_groups_partition_all_coordinates": True,
            "shared_a7_endpoint_owned_once_by_past_epoch": True,
            "owner_integrated_signed_demands": owner_integrals,
        },
        "rational_PSD_witness": witness,
        "theorem_boundary": {
            "proved": (
                "at t=4835/48, the stored rational zero-row-sum PSD Gram "
                "factor satisfies all 616 canonical aggregate owner-cell rows "
                "and has P<2D"
            ),
            "not_proved": (
                "the accounting interpretation, another t, a phase interval, "
                "an exact optimum, the C067 terminal ledger, a compatible "
                "history, C058, either Erdos question, novelty, or a prize claim"
            ),
        },
    }
    certificate["integrity"] = {
        "canonical_json": True,
        "payload_sha256": payload_hash(certificate),
    }
    return certificate


@lru_cache(maxsize=1)
def _cached_certificate_json() -> str:
    return json.dumps(
        _build_uncached(), sort_keys=True, separators=(",", ":"), ensure_ascii=False
    )


def build_certificate() -> dict[str, object]:
    return json.loads(_cached_certificate_json())


def rendered_bytes(certificate: Mapping[str, object]) -> bytes:
    return (
        json.dumps(
            certificate,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n"
    ).encode("utf-8")


def _check_boolean_types(actual: object, expected: object, path: str = "root") -> None:
    if isinstance(expected, bool):
        if type(actual) is not bool:
            raise CertificateError(f"{path} must be a literal boolean")
        return
    if type(expected) is int and type(actual) is bool:
        raise CertificateError(f"{path} must be an integer, not a boolean")
    if isinstance(expected, Mapping):
        if not isinstance(actual, Mapping):
            raise CertificateError(f"{path} must be an object")
        for key, value in expected.items():
            if key in actual:
                _check_boolean_types(actual[key], value, f"{path}.{key}")
    elif isinstance(expected, list) and isinstance(actual, list):
        for index, (left, right) in enumerate(zip(actual, expected)):
            _check_boolean_types(left, right, f"{path}[{index}]")


def verify_certificate(certificate: Mapping[str, object]) -> None:
    if not isinstance(certificate, Mapping):
        raise CertificateError("JSON root must be an object")
    integrity = certificate.get("integrity")
    if not isinstance(integrity, Mapping):
        raise CertificateError("missing integrity row")
    if integrity.get("canonical_json") is not True:
        raise CertificateError("canonical_json must be the boolean true")
    if integrity.get("payload_sha256") != payload_hash(certificate):
        raise CertificateError("payload hash mismatch")
    expected = build_certificate()
    _check_boolean_types(certificate, expected)
    if certificate != expected:
        raise CertificateError("certificate differs from exact semantic replay")


def _rehash(certificate: dict[str, object]) -> None:
    certificate["integrity"]["payload_sha256"] = payload_hash(certificate)  # type: ignore[index]


def self_check(certificate: Mapping[str, object]) -> dict[str, int]:
    verify_certificate(certificate)
    specs = (
        (("schema",), "wrong.schema"),
        (("status",), "C058_SOLVED"),
        (("scope", "fixed_midpoint_fixture_only"), False),
        (("scope", "C058_Q1_Q2_proved"), True),
        (("scope", "continuum_phase_interval_proved"), True),
        (("scope", "finite_whole_stencil_accounting_legal_proved"), True),
        (("fixture", "base_width"), "100/1"),
        (("fixture", "finite_event_count"), 77),
        (("rational_PSD_witness", "factor_common_denominator"), 1),
        (("rational_PSD_witness", "physical_price"), "0/1"),
        (("rational_PSD_witness", "below_twice_demand_margin"), "0/1"),
        (("rational_PSD_witness", "factor_integer_columns", 0, 0), 0),
    )
    mutations: list[dict[str, object]] = []
    for path, value in specs:
        changed = copy.deepcopy(certificate)
        target: object = changed
        for key in path[:-1]:
            target = target[key]  # type: ignore[index]
        target[path[-1]] = value  # type: ignore[index]
        _rehash(changed)
        mutations.append(changed)
    rejected = 0
    for changed in mutations:
        try:
            verify_certificate(changed)
        except CertificateError:
            rejected += 1
    if rejected != len(mutations):
        raise CertificateError("a rehashed semantic mutation was accepted")
    return {"mutations_attempted": len(mutations), "mutations_rejected": rejected}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--verify", type=Path)
    parser.add_argument("--self-check", action="store_true")
    arguments = parser.parse_args()
    try:
        if arguments.verify is not None:
            raw = arguments.verify.read_bytes()
            parsed = json.loads(raw.decode("utf-8"))
            if not isinstance(parsed, dict):
                raise CertificateError("JSON root must be an object")
            certificate = parsed
            if raw != rendered_bytes(certificate):
                raise CertificateError("certificate bytes are not canonical JSON")
            verify_certificate(certificate)
        else:
            certificate = build_certificate()
        if arguments.output is not None:
            arguments.output.write_bytes(rendered_bytes(certificate))
        elif arguments.verify is None:
            sys.stdout.buffer.write(rendered_bytes(certificate))
        machine_stdout = arguments.output is None and arguments.verify is None
        if not machine_stdout:
            print(
                "verified payload_sha256="
                f"{certificate['integrity']['payload_sha256']}"  # type: ignore[index]
            )
        if arguments.self_check:
            result = self_check(certificate)
            print(
                "self_check mutations_attempted="
                f"{result['mutations_attempted']} "
                f"mutations_rejected={result['mutations_rejected']}",
                file=sys.stderr if machine_stdout else sys.stdout,
            )
    except (CertificateError, OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
