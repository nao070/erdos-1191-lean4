#!/usr/bin/env python3
"""Exact finite reverse-profile full-phase storage calibration.

The checked JSON contains one rational zero-row-sum epoch-block Gram factor
for each of the 161 exact event chambers.  This verifier reconstructs every
owner row and phase polynomial with ``fractions.Fraction``, integrates the
chosen witnesses with rigorous atanh-series logarithm enclosures, and checks
the trial storage constants epsilon=A=1/1000, B=1/3, e_2=0.

An independent eight-piece dual is also replayed on chamber zero.  It proves
that the same trial constants fail on that chamber average even though they
pass after integration over the complete factor-two phase.  This is a fixed
finite calibration in the independent epoch-block cone, not C058.
"""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import re
import sys
from typing import Any, Callable, Mapping, Sequence


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate.json"
SCHEMA = "erdos1191.c058_reverse_profile_full_phase_storage.v1"
STATUS = "EXACT_FINITE_FULL_PHASE_STORAGE_CALIBRATION_ONLY_C058_OPEN"

POINTS = (
    0, 22, 60, 83, 102, 173, 303, 513,
    616, 727, 772, 881, 972, 1041, 1103, 1169,
)
MULTIPLIERS = (1, 2, 4, 8)
RHO = F(9, 16)
PHASE_LOWER = F(553, 8)
PHASE_UPPER = F(553, 4)
LOG_TERMS = 30
EPSILON = F(1, 1000)
A_COEFFICIENT = F(1, 1000)
B_COEFFICIENT = F(1, 3)
E2 = F(0)
DELTA_V = -F(443620417, 1928247678)
SOURCE_PRIMAL_MANIFEST_SHA256 = "bd8bc014c5e3296bd65f9f1641923c21ebf6fbc187891ec6250202f1e3a3be10"
SOURCE_LOCAL_DUAL_SHA256 = "efa9d08158b6c55d64978063b57bd59e6658085322f783aa6c120bd73505cb13"

CHANNELS = tuple(
    (rank, multiplier, POINTS[rank])
    for multiplier in MULTIPLIERS
    for rank in range(3, 16)
)
OWNERS = tuple((epoch, multiplier) for multiplier in MULTIPLIERS for epoch in (4, 8))
EVENT_LINES = tuple(
    sorted({(origin, shift * multiplier) for _, multiplier, origin in CHANNELS for shift in (0, 1, 2)})
)
EPOCH4_INDICES = tuple(i for i, (rank, _, _) in enumerate(CHANNELS) if rank <= 7)
EPOCH8_INDICES = tuple(i for i, (rank, _, _) in enumerate(CHANNELS) if rank >= 8)

EXPECTED_ENVELOPE_ROWS = (
    {"m": 4, "N_m": 84, "required_log": "21/16"},
    {"m": 8, "N_m": 514, "required_log": "257/128"},
    {"m": 16, "N_m": 1170, "required_log": "585/512"},
)
EXPECTED_MODEL = {
    "rho": "9/16",
    "multipliers": [1, 2, 4, 8],
    "channel_rank_range": [3, 15],
    "epoch_4_owned_rank_range": [3, 7],
    "epoch_8_demand_rank_range": [7, 15],
    "epoch_8_owned_rank_range": [8, 15],
    "haar_sign_convention": "+1 on [0,t), -1 on [t,2t), 0 otherwise; half-open",
    "gram_representation": "rational zero-row-sum columns supported in one epoch block",
    "log_enclosure": "30-term rational atanh series with explicit positive tail",
}
EXPECTED_PROTOTYPE = {
    "k": 2,
    "epsilon": "1/1000",
    "A": "1/1000",
    "B": "1/3",
    "e2": "0/1",
    "target": "(epsilon-A*eta_2-B*(V3-V2))/3-e2",
}
EXPECTED_CONCLUSION = {
    "full_phase_raw_interval_inside": ["49/1000", "1/20"],
    "full_phase_normalized_interval_inside": ["719/10000", "9/125"],
    "prototype_rhs_interval_inside": ["13/500", "27/1000"],
    "full_phase_normalized_gap_greater_than": "457/10000",
    "chamber0_normalized_upper_less_than": "2601/100000",
    "chamber0_rhs_minus_upper_greater_than": "207/1000000",
    "complete_phase_integrated_prototype_survives": True,
    "chamber0_average_prototype_fails": True,
}
EXPECTED_SCOPE = {
    "fixed_reverse_16_mark_k2_C2_fixture_only": True,
    "rho_9_over_16_only_for_integrated_comparison": True,
    "independent_epoch_block_cone_only": True,
    "complete_phase_integrated_prototype_survival_proved": True,
    "pointwise_or_per_chamber_prototype_survival_proved": False,
    "eventual_critical_infinite_history_constructed": False,
    "global_owner_stitching_proved": False,
    "C058_resolved": False,
    "Q1_Q2_resolved": False,
    "publication_novelty_or_prize_claimed": False,
}

TOP_KEYS = {
    "schema", "status", "fixture", "phase", "model", "prototype",
    "primal_certificate", "local_chamber0_dual", "conclusion", "scope", "integrity",
}
FIXTURE_KEYS = {
    "points", "positive_difference_count", "H2", "H3", "eta_ratio",
    "V2", "V3", "delta_V", "finite_dyadic_envelope",
}
ENVELOPE_KEYS = {
    "canonical_constant", "actual_cap_formula", "rows", "all_rows_certified",
    "eventual_infinite_ray_constructed",
}
PHASE_KEYS = {"lower", "upper", "event_line_count", "chamber_count", "breakpoints"}
CHAMBER_KEYS = {"index", "left", "right", "denominator", "rank4", "rank8", "columns"}
LOCAL_KEYS = {"interval", "partition_count", "piece_records"}
DUAL_PIECE_KEYS = {"index", "left", "right", "Dc4", "Do4", "Dc8", "Do8", "n4", "n8"}
DUAL_EPOCH_KEYS = {"denominator", "weights", "objective"}
INTEGRITY_KEYS = {
    "algorithm", "payload_sha256", "source_primal_manifest_sha256",
    "source_local_dual_sha256", "exact_replay_arithmetic",
}


class CertificateError(RuntimeError):
    """Raised for a schema, arithmetic, owner, PSD, integral, or scope failure."""


def ftext(value: F | int) -> str:
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


_FRACTION_RE = re.compile(r"-?(?:0|[1-9][0-9]*)/[1-9][0-9]*\Z")


def _fraction(value: object, label: str) -> F:
    if type(value) is not str or _FRACTION_RE.fullmatch(value) is None:
        raise CertificateError(f"{label}: noncanonical rational text")
    result = F(value)
    if ftext(result) != value:
        raise CertificateError(f"{label}: rational text is not reduced")
    return result


def _exact_keys(value: object, expected: set[str], label: str) -> Mapping[str, Any]:
    if type(value) is not dict:
        raise CertificateError(f"{label}: expected object")
    if set(value) != expected:
        raise CertificateError(f"{label}: schema keys differ")
    return value


def _exact_int(value: object, label: str, *, minimum: int | None = None) -> int:
    if type(value) is not int:
        raise CertificateError(f"{label}: expected integer")
    if minimum is not None and value < minimum:
        raise CertificateError(f"{label}: integer below {minimum}")
    return value


def rendered_bytes(value: Mapping[str, Any]) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode("utf-8")


def payload_hash(value: Mapping[str, Any]) -> str:
    if type(value) is not dict or type(value.get("integrity")) is not dict:
        raise CertificateError("payload hash requires integrity object")
    clone = copy.deepcopy(value)
    clone["integrity"]["payload_sha256"] = ""
    return hashlib.sha256(rendered_bytes(clone)).hexdigest()


def _positive_differences(points: Sequence[int]) -> tuple[int, ...]:
    if any(type(point) is not int for point in points):
        raise CertificateError("fixture points must be integers")
    if any(points[i] >= points[i + 1] for i in range(len(points) - 1)):
        raise CertificateError("fixture points are not strictly increasing")
    values = tuple(
        points[j] - points[i]
        for i in range(len(points))
        for j in range(i + 1, len(points))
    )
    if len(values) != len(set(values)):
        raise CertificateError("fixture is not a Golomb ruler")
    return values


def _log_interval(value: F, terms: int = LOG_TERMS) -> tuple[F, F]:
    if value < 1 or terms <= 0:
        raise ValueError("log enclosure needs value >= 1 and positive terms")
    z = (value - 1) / (value + 1)
    lower = 2 * sum(
        (z ** (2 * index + 1) / (2 * index + 1) for index in range(terms)),
        F(0),
    )
    tail = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return lower, lower + tail


def _breakpoints() -> tuple[F, ...]:
    result = {PHASE_LOWER, PHASE_UPPER}
    for index, (origin_1, slope_1) in enumerate(EVENT_LINES):
        for origin_2, slope_2 in EVENT_LINES[index + 1 :]:
            if slope_1 == slope_2:
                continue
            crossing = F(origin_2 - origin_1, slope_1 - slope_2)
            if PHASE_LOWER < crossing < PHASE_UPPER:
                result.add(crossing)
    return tuple(sorted(result))


def _haar_sign(x: F, width: F, origin: int, multiplier: int) -> int:
    displacement = x - origin
    return int(0 <= displacement < multiplier * width) - int(
        multiplier * width <= displacement < 2 * multiplier * width
    )


def _state(x: F, width: F) -> tuple[int, ...]:
    return tuple(
        (8 // multiplier) * _haar_sign(x, width, origin, multiplier)
        for _, multiplier, origin in CHANNELS
    )


def _generic_cells(
    left: F, right: F,
) -> tuple[tuple[tuple[int, int], tuple[int, int], tuple[int, ...]], ...]:
    midpoint = (left + right) / 2
    ordered = tuple(sorted(EVENT_LINES, key=lambda line: F(line[0]) + line[1] * midpoint))
    if any(
        F(ordered[i][0]) + ordered[i][1] * midpoint
        >= F(ordered[i + 1][0]) + ordered[i + 1][1] * midpoint
        for i in range(len(ordered) - 1)
    ):
        raise CertificateError("event collision inside open chamber")
    cells = tuple(
        (
            line_left,
            line_right,
            _state(
                (
                    F(line_left[0]) + line_left[1] * midpoint
                    + F(line_right[0]) + line_right[1] * midpoint
                ) / 2,
                midpoint,
            ),
        )
        for line_left, line_right in zip(ordered, ordered[1:])
    )
    if len(cells) != 77:
        raise CertificateError("generic cell count changed")
    return cells


def _exact_cells(width: F) -> tuple[tuple[F, F, tuple[int, ...]], ...]:
    events = tuple(sorted({F(origin) + slope * width for origin, slope in EVENT_LINES}))
    cells = tuple(
        (left, right, _state((left + right) / 2, width))
        for left, right in zip(events, events[1:])
    )
    if not 69 <= len(cells) <= 77:
        raise CertificateError("collapsed endpoint cell count changed")
    return cells


def _wave_b_matrix(n: int) -> list[list[F]]:
    return [
        [
            F(0) if i == j or abs(i - j) == 1 else -F((j - i) ** 2, 8 * n * n)
            for j in range(n)
        ]
        for i in range(n)
    ]


def _incidence_matrix(n: int) -> list[list[F]]:
    return [[F((k == i) - (k == i + 1)) for k in range(n + 1)] for i in range(n)]


def _point_m_matrix(n: int) -> tuple[tuple[F, ...], ...]:
    b = _wave_b_matrix(n)
    d = _incidence_matrix(n)
    return tuple(
        tuple(
            sum((d[a][i] * b[a][c] * d[c][j] for a in range(n) for c in range(n)), F(0))
            for j in range(n + 1)
        )
        for i in range(n + 1)
    )


POINT_MATRICES = {n: _point_m_matrix(n) for n in (4, 8)}


def _quadratic(matrix: Sequence[Sequence[F]], vector: Sequence[int]) -> F:
    return sum(
        (F(vector[i]) * matrix[i][j] * vector[j] for i in range(len(vector)) for j in range(len(vector))),
        F(0),
    )


def _owner_full_indices(owner: tuple[int, int]) -> tuple[int, ...]:
    epoch, multiplier = owner
    ranks = range(3, 8) if epoch == 4 else range(7, 16)
    index = {(rank, mult): i for i, (rank, mult, _) in enumerate(CHANNELS)}
    return tuple(index[(rank, multiplier)] for rank in ranks)


def _owner_group_indices(owner: tuple[int, int]) -> tuple[int, ...]:
    epoch, multiplier = owner
    ranks = range(3, 8) if epoch == 4 else range(8, 16)
    index = {(rank, mult): i for i, (rank, mult, _) in enumerate(CHANNELS)}
    return tuple(index[(rank, multiplier)] for rank in ranks)


def _owner_c(owner: tuple[int, int], state: Sequence[int]) -> F:
    epoch, multiplier = owner
    local = tuple(state[i] for i in _owner_full_indices(owner))
    return F(multiplier, 128) * _quadratic(POINT_MATRICES[epoch], local)


def _validate_factor(
    record: Mapping[str, Any], index: int, left: F, right: F,
) -> tuple[int, tuple[tuple[int, ...], ...], int, int]:
    checked = _exact_keys(record, CHAMBER_KEYS, f"primal.chambers[{index}]")
    if checked["index"] != index or checked["left"] != ftext(left) or checked["right"] != ftext(right):
        raise CertificateError("primal chamber order/endpoints changed")
    denominator = _exact_int(checked["denominator"], "factor denominator", minimum=1)
    rank4 = _exact_int(checked["rank4"], "factor rank4", minimum=1)
    rank8 = _exact_int(checked["rank8"], "factor rank8", minimum=1)
    raw_columns = checked["columns"]
    if type(raw_columns) is not list or len(raw_columns) != rank4 + rank8:
        raise CertificateError("factor column count changed")
    columns: list[tuple[int, ...]] = []
    counted4 = 0
    counted8 = 0
    set4 = set(EPOCH4_INDICES)
    set8 = set(EPOCH8_INDICES)
    for raw in raw_columns:
        if type(raw) is not list or len(raw) != 52:
            raise CertificateError("factor column dimension changed")
        column = tuple(_exact_int(value, "factor entry") for value in raw)
        if sum(column) != 0 or not any(column):
            raise CertificateError("factor column is zero or lost zero sum")
        support = {i for i, value in enumerate(column) if value}
        if support <= set4:
            counted4 += 1
        elif support <= set8:
            counted8 += 1
        else:
            raise CertificateError("factor column crosses epoch blocks")
        columns.append(column)
    if (counted4, counted8) != (rank4, rank8):
        raise CertificateError("factor rank census changed")
    return denominator, tuple(columns), rank4, rank8


def _make_factor_evaluator(
    columns: tuple[tuple[int, ...], ...], denominator: int,
) -> Callable[[tuple[int, ...]], tuple[dict[int, F], tuple[F, ...], tuple[F, ...]]]:
    squared_denominator = denominator * denominator
    set4 = set(EPOCH4_INDICES)
    epochs = tuple(4 if {i for i, value in enumerate(column) if value} <= set4 else 8 for column in columns)
    cache: dict[tuple[int, ...], tuple[dict[int, F], tuple[F, ...], tuple[F, ...]]] = {}

    def evaluate(state: tuple[int, ...]) -> tuple[dict[int, F], tuple[F, ...], tuple[F, ...]]:
        cached = cache.get(state)
        if cached is not None:
            return cached
        dots = tuple(sum(state[i] * column[i] for i in range(52)) for column in columns)
        physical = {
            epoch: F(sum(dot * dot for dot, column_epoch in zip(dots, epochs) if column_epoch == epoch), squared_denominator)
            for epoch in (4, 8)
        }
        owned = []
        demands = []
        for owner in OWNERS:
            group = _owner_group_indices(owner)
            group_dots = tuple(sum(state[i] * column[i] for i in group) for column in columns)
            owned.append(F(sum(left * right for left, right in zip(group_dots, dots)), squared_denominator))
            demands.append(_owner_c(owner, state))
        if sum(owned, F(0)) != physical[4] + physical[8]:
            raise CertificateError("owner shares do not recover physical energy")
        result = physical, tuple(owned), tuple(demands)
        cache[state] = result
        return result

    return evaluate


def _epoch_polynomial(
    left: F,
    right: F,
    epoch: int,
    evaluate: Callable[[tuple[int, ...]], tuple[dict[int, F], tuple[F, ...], tuple[F, ...]]],
) -> tuple[F, F, F]:
    ap = bp = ad = bd = F(0)
    for left_line, right_line, state in _generic_cells(left, right):
        delta_origin = F(right_line[0] - left_line[0])
        delta_slope = F(right_line[1] - left_line[1])
        physical, _, demands = evaluate(state)
        demand = sum(
            (value for owner, value in zip(OWNERS, demands) if owner[0] == epoch),
            F(0),
        )
        ap += delta_origin * physical[epoch]
        bp += delta_slope * physical[epoch]
        ad += delta_origin * demand
        bd += delta_slope * demand
    return -bp, 2 * bd - ap, 2 * ad


def _poly_eval(poly: tuple[F, F, F], value: F) -> F:
    return poly[0] * value * value + poly[1] * value + poly[2]


def _poly_minimum(poly: tuple[F, F, F], left: F, right: F) -> F:
    candidates = [_poly_eval(poly, left), _poly_eval(poly, right)]
    if poly[0] > 0:
        vertex = -poly[1] / (2 * poly[0])
        if left < vertex < right:
            candidates.append(_poly_eval(poly, vertex))
    return min(candidates)


def _log_phase_piece_interval(poly: tuple[F, F, F], left: F, right: F) -> tuple[F, F]:
    log_lower, log_upper = _log_interval(right / left)
    fixed = poly[0] * (right - left) + poly[2] * (F(1, left) - F(1, right))
    if poly[1] >= 0:
        return fixed + poly[1] * log_lower, fixed + poly[1] * log_upper
    return fixed + poly[1] * log_upper, fixed + poly[1] * log_lower


def _zero_int_matrix(size: int) -> list[list[int]]:
    return [[0 for _ in range(size)] for _ in range(size)]


def _add_int_outer(matrix: list[list[int]], coefficient: int, vector: Sequence[int]) -> None:
    nonzero = tuple((i, value) for i, value in enumerate(vector) if value)
    for i, left in nonzero:
        for j, right in nonzero:
            matrix[i][j] += coefficient * left * right


def _add_int_symmetric_outer(
    matrix: list[list[int]], coefficient: int, left: Sequence[int], right: Sequence[int]
) -> None:
    left_nonzero = tuple((i, value) for i, value in enumerate(left) if value)
    right_nonzero = tuple((i, value) for i, value in enumerate(right) if value)
    for i, left_value in left_nonzero:
        for j, right_value in right_nonzero:
            contribution = coefficient * left_value * right_value
            matrix[i][j] += contribution
            matrix[j][i] += contribution


def _dual_epoch_reconstruction(
    left: F,
    right: F,
    epoch: int,
    denominator: int,
    integer_weights: Sequence[int],
) -> tuple[list[list[int]], list[list[int]], list[list[int]], F, F, F]:
    midpoint = (left + right) / 2
    ordered = sorted(EVENT_LINES, key=lambda line: F(line[0]) + line[1] * midpoint)
    channel_index = {(rank, multiplier): i for i, (rank, multiplier, _) in enumerate(CHANNELS)}
    block = EPOCH4_INDICES if epoch == 4 else EPOCH8_INDICES
    dimension = len(block) - 1
    constant_matrix = _zero_int_matrix(dimension)
    reciprocal_matrix = _zero_int_matrix(dimension)
    weighted_rows = _zero_int_matrix(dimension)
    demand_ranks = range(3, 8) if epoch == 4 else range(7, 16)
    owned_ranks = range(3, 8) if epoch == 4 else range(8, 16)
    dc_total = do_total = objective = F(0)
    row_index = 0
    for (origin_left, slope_left), (origin_right, slope_right) in zip(ordered, ordered[1:]):
        position_left = F(origin_left) + slope_left * midpoint
        position_right = F(origin_right) + slope_right * midpoint
        if position_left >= position_right:
            raise CertificateError("local dual event order is not strict")
        state = _state((position_left + position_right) / 2, midpoint)
        delta_origin = origin_right - origin_left
        delta_slope = slope_right - slope_left
        values = [state[i] for i in block]
        y = tuple(value - values[-1] for value in values[:-1])
        _add_int_outer(constant_matrix, delta_slope, y)
        _add_int_outer(reciprocal_matrix, delta_origin, y)
        for multiplier in MULTIPLIERS:
            full = tuple(channel_index[(rank, multiplier)] for rank in demand_ranks)
            group = tuple(channel_index[(rank, multiplier)] for rank in owned_ranks)
            local = tuple(state[i] for i in full)
            coefficient = F(multiplier, 128) * _quadratic(POINT_MATRICES[epoch], local)
            group_state = [0 for _ in CHANNELS]
            for i in group:
                group_state[i] = state[i]
            group_values = [group_state[i] for i in block]
            z = tuple(value - group_values[-1] for value in group_values[:-1])
            weight = integer_weights[row_index]
            if weight:
                _add_int_symmetric_outer(weighted_rows, weight, z, y)
            objective += F(weight, denominator) * coefficient
            dc_total += delta_slope * coefficient
            do_total += delta_origin * coefficient
            row_index += 1
    if row_index != 308 or len(ordered) - 1 != 77:
        raise CertificateError("local dual row count changed")
    return constant_matrix, reciprocal_matrix, weighted_rows, dc_total, do_total, objective


def _integer_slack(
    constant_matrix: Sequence[Sequence[int]],
    reciprocal_matrix: Sequence[Sequence[int]],
    weighted_rows: Sequence[Sequence[int]],
    denominator: int,
    endpoint: F,
) -> list[list[int]]:
    scale = math.lcm(endpoint.numerator, 2 * denominator)
    reciprocal_scale = endpoint.denominator * (scale // endpoint.numerator)
    row_scale = scale // (2 * denominator)
    return [
        [
            constant_matrix[i][j] * scale
            + reciprocal_matrix[i][j] * reciprocal_scale
            - weighted_rows[i][j] * row_scale
            for j in range(len(constant_matrix))
        ]
        for i in range(len(constant_matrix))
    ]


def _bareiss_positive_definite(matrix: Sequence[Sequence[int]]) -> bool:
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise CertificateError("positive-definite check received nonsquare matrix")
    if any(matrix[i][j] != matrix[j][i] for i in range(size) for j in range(i)):
        raise CertificateError("positive-definite check received nonsymmetric matrix")
    work = [list(row) for row in matrix]
    previous = 1
    for pivot_index in range(size):
        pivot = work[pivot_index][pivot_index]
        if pivot <= 0:
            return False
        if pivot_index + 1 == size:
            return True
        for i in range(pivot_index + 1, size):
            for j in range(i, size):
                numerator = work[i][j] * pivot - work[i][pivot_index] * work[pivot_index][j]
                quotient, remainder = divmod(numerator, previous)
                if remainder:
                    raise CertificateError("Bareiss division was not exact")
                work[i][j] = quotient
                work[j][i] = quotient
        previous = pivot
    raise AssertionError("unreachable")


def _dual_piece_interval(record: Mapping[str, Any]) -> tuple[F, F]:
    left = _fraction(record["left"], "dual.left")
    right = _fraction(record["right"], "dual.right")
    objective4 = _fraction(record["n4"]["objective"], "dual.n4.objective")
    objective8 = _fraction(record["n8"]["objective"], "dual.n8.objective")
    dc4 = _fraction(record["Dc4"], "dual.Dc4")
    do4 = _fraction(record["Do4"], "dual.Do4")
    dc8 = _fraction(record["Dc8"], "dual.Dc8")
    do8 = _fraction(record["Do8"], "dual.Do8")
    log_coefficient = 2 * (dc4 + RHO * dc8) - (objective4 + RHO * objective8)
    reciprocal_coefficient = 2 * (do4 + RHO * do8)
    log_lower, log_upper = _log_interval(right / left)
    reciprocal = reciprocal_coefficient * (F(1, left) - F(1, right))
    if log_coefficient >= 0:
        return log_coefficient * log_lower + reciprocal, log_coefficient * log_upper + reciprocal
    return log_coefficient * log_upper + reciprocal, log_coefficient * log_lower + reciprocal


def _prototype_interval() -> tuple[F, F]:
    log_lower, log_upper = _log_interval(F(215, 82))
    base = EPSILON - B_COEFFICIENT * DELTA_V
    return (
        (base + A_COEFFICIENT * log_lower) / 3 - E2,
        (base + A_COEFFICIENT * log_upper) / 3 - E2,
    )


def _validate_static(value: Mapping[str, Any], *, check_hash: bool = True) -> None:
    payload = _exact_keys(value, TOP_KEYS, "payload")
    if payload["schema"] != SCHEMA or payload["status"] != STATUS:
        raise CertificateError("schema or status mismatch")
    fixture = _exact_keys(payload["fixture"], FIXTURE_KEYS, "fixture")
    if fixture["points"] != list(POINTS):
        raise CertificateError("fixture points changed")
    differences = _positive_differences(fixture["points"])
    if fixture["positive_difference_count"] != len(differences) or len(differences) != 120:
        raise CertificateError("positive-difference count mismatch")
    if (fixture["H2"], fixture["H3"]) != (430, 656):
        raise CertificateError("shell spans changed")
    if _fraction(fixture["eta_ratio"], "eta_ratio") != F(82, 215):
        raise CertificateError("eta ratio changed")
    if _fraction(fixture["V2"], "V2") != F(20177, 66402):
        raise CertificateError("V2 changed")
    if _fraction(fixture["V3"], "V3") != F(2143, 29039):
        raise CertificateError("V3 changed")
    if _fraction(fixture["delta_V"], "delta_V") != DELTA_V:
        raise CertificateError("delta V changed")
    envelope = _exact_keys(fixture["finite_dyadic_envelope"], ENVELOPE_KEYS, "envelope")
    if envelope["canonical_constant"] != 2 or envelope["actual_cap_formula"] != "N_m <= 2*C*m^2*log(m)":
        raise CertificateError("finite-envelope convention changed")
    if envelope["rows"] != [dict(row) for row in EXPECTED_ENVELOPE_ROWS]:
        raise CertificateError("finite-envelope rows changed")
    log2_lower, _ = _log_interval(F(2))
    for row in envelope["rows"]:
        if _fraction(row["required_log"], "required_log") >= {4: 2, 8: 3, 16: 4}[row["m"]] * log2_lower:
            raise CertificateError("finite-envelope log comparison failed")
    if envelope["all_rows_certified"] is not True or envelope["eventual_infinite_ray_constructed"] is not False:
        raise CertificateError("finite-envelope scope changed")
    breakpoints = _breakpoints()
    phase = _exact_keys(payload["phase"], PHASE_KEYS, "phase")
    if (
        phase["lower"] != ftext(PHASE_LOWER)
        or phase["upper"] != ftext(PHASE_UPPER)
        or phase["event_line_count"] != 78
        or phase["chamber_count"] != 161
        or phase["breakpoints"] != [ftext(point) for point in breakpoints]
    ):
        raise CertificateError("phase partition changed")
    if len(EVENT_LINES) != 78 or len(breakpoints) != 162:
        raise CertificateError("phase census changed")
    if _exact_keys(payload["model"], set(EXPECTED_MODEL), "model") != EXPECTED_MODEL:
        raise CertificateError("model convention changed")
    if _exact_keys(payload["prototype"], set(EXPECTED_PROTOTYPE), "prototype") != EXPECTED_PROTOTYPE:
        raise CertificateError("prototype constants changed")
    primal = _exact_keys(payload["primal_certificate"], {"chambers"}, "primal_certificate")
    chambers = primal["chambers"]
    if type(chambers) is not list or len(chambers) != 161:
        raise CertificateError("primal chamber count changed")
    for index, (record, left, right) in enumerate(zip(chambers, breakpoints, breakpoints[1:])):
        _validate_factor(record, index, left, right)
    local = _exact_keys(payload["local_chamber0_dual"], LOCAL_KEYS, "local dual")
    if local["interval"] != ["553/8", "277/4"] or local["partition_count"] != 8:
        raise CertificateError("local chamber-zero interval changed")
    records = local["piece_records"]
    if type(records) is not list or len(records) != 8:
        raise CertificateError("local dual piece count changed")
    local_endpoints = tuple(PHASE_LOWER + F(i, 64) for i in range(9))
    for index, (record, left, right) in enumerate(zip(records, local_endpoints, local_endpoints[1:])):
        checked = _exact_keys(record, DUAL_PIECE_KEYS, f"local.pieces[{index}]")
        if checked["index"] != index or checked["left"] != ftext(left) or checked["right"] != ftext(right):
            raise CertificateError("local dual piece order changed")
        for coefficient in ("Dc4", "Do4", "Dc8", "Do8"):
            _fraction(checked[coefficient], f"local.{coefficient}")
        for key in ("n4", "n8"):
            epoch = _exact_keys(checked[key], DUAL_EPOCH_KEYS, f"local.{key}")
            if _exact_int(epoch["denominator"], "dual denominator", minimum=1) != 100000:
                raise CertificateError("local dual denominator changed")
            weights = epoch["weights"]
            if type(weights) is not list or len(weights) != 308:
                raise CertificateError("local dual weight count changed")
            for weight in weights:
                _exact_int(weight, "dual weight", minimum=0)
            _fraction(epoch["objective"], "dual objective")
    if _exact_keys(payload["conclusion"], set(EXPECTED_CONCLUSION), "conclusion") != EXPECTED_CONCLUSION:
        raise CertificateError("conclusion gate changed")
    if _exact_keys(payload["scope"], set(EXPECTED_SCOPE), "scope") != EXPECTED_SCOPE:
        raise CertificateError("scope gate changed")
    integrity = _exact_keys(payload["integrity"], INTEGRITY_KEYS, "integrity")
    if integrity["algorithm"] != "sha256":
        raise CertificateError("integrity algorithm changed")
    if integrity["source_primal_manifest_sha256"] != SOURCE_PRIMAL_MANIFEST_SHA256:
        raise CertificateError("source primal manifest hash changed")
    if integrity["source_local_dual_sha256"] != SOURCE_LOCAL_DUAL_SHA256:
        raise CertificateError("source local dual hash changed")
    if integrity["exact_replay_arithmetic"] != "fractions.Fraction plus integer rational-Gram and Bareiss/Sylvester replay":
        raise CertificateError("arithmetic label changed")
    for name in ("payload_sha256", "source_primal_manifest_sha256", "source_local_dual_sha256"):
        if type(integrity[name]) is not str or re.fullmatch(r"[0-9a-f]{64}", integrity[name]) is None:
            raise CertificateError(f"{name}: invalid sha256")
    if check_hash and integrity["payload_sha256"] != payload_hash(payload):
        raise CertificateError("payload sha256 mismatch")


_REPLAY_CACHE: dict[str, dict[str, Any]] = {}


def _replay_validated(value: Mapping[str, Any]) -> dict[str, Any]:
    digest = value["integrity"]["payload_sha256"]
    cached = _REPLAY_CACHE.get(digest)
    if cached is not None:
        return dict(cached)
    breakpoints = _breakpoints()
    raw_lower = raw_upper = F(0)
    rational_columns = generic_rows = generic_endpoint_checks = collapsed_rows = 0
    chamber0_primal_interval: tuple[F, F] | None = None
    for index, (record, left, right) in enumerate(
        zip(value["primal_certificate"]["chambers"], breakpoints, breakpoints[1:])
    ):
        denominator, columns, _, _ = _validate_factor(record, index, left, right)
        rational_columns += len(columns)
        evaluate = _make_factor_evaluator(columns, denominator)
        cells = _generic_cells(left, right)
        for _, _, state in cells:
            _, owned, demands = evaluate(state)
            for owner_value, demand in zip(owned, demands):
                if left * owner_value - demand < 0 or right * owner_value - demand < 0:
                    raise CertificateError(f"chamber {index}: generic owner row failed")
                generic_rows += 1
                generic_endpoint_checks += 2
        poly4 = _epoch_polynomial(left, right, 4, evaluate)
        poly8 = _epoch_polynomial(left, right, 8, evaluate)
        weighted = tuple(poly4[i] + RHO * poly8[i] for i in range(3))
        unweighted = tuple(poly4[i] + poly8[i] for i in range(3))
        if _poly_minimum(weighted, left, right) <= 0 or _poly_minimum(unweighted, left, right) <= 0:
            raise CertificateError(f"chamber {index}: phase polynomial is not positive")
        piece_lower, piece_upper = _log_phase_piece_interval(weighted, left, right)
        raw_lower += piece_lower
        raw_upper += piece_upper
        if index == 0:
            chamber0_primal_interval = piece_lower, piece_upper
        for endpoint in (left, right):
            demand_total = {4: F(0), 8: F(0)}
            price_total = {4: F(0), 8: F(0)}
            for cell_left, cell_right, state in _exact_cells(endpoint):
                physical, owned, demands = evaluate(state)
                length = cell_right - cell_left
                for owner, owner_value, demand in zip(OWNERS, owned, demands):
                    if endpoint * owner_value - demand < 0:
                        raise CertificateError(f"chamber {index}: collapsed owner row failed")
                    demand_total[owner[0]] += length * demand / endpoint
                    collapsed_rows += 1
                for epoch in (4, 8):
                    price_total[epoch] += length * physical[epoch]
            endpoint_phi4 = endpoint * (2 * demand_total[4] - price_total[4])
            endpoint_phi8 = endpoint * (2 * demand_total[8] - price_total[8])
            if endpoint_phi4 + RHO * endpoint_phi8 != _poly_eval(weighted, endpoint):
                raise CertificateError(f"chamber {index}: weighted collapsed polynomial mismatch")
            if endpoint_phi4 + endpoint_phi8 != _poly_eval(unweighted, endpoint):
                raise CertificateError(f"chamber {index}: unweighted collapsed polynomial mismatch")
    log2_lower, log2_upper = _log_interval(F(2))
    normalized_lower = raw_lower / log2_upper
    normalized_upper = raw_upper / log2_lower
    prototype_lower, prototype_upper = _prototype_interval()
    if not (
        F(49, 1000) < raw_lower <= raw_upper < F(1, 20)
        and F(719, 10000) < normalized_lower <= normalized_upper < F(9, 125)
        and F(13, 500) < prototype_lower <= prototype_upper < F(27, 1000)
        and normalized_lower - prototype_upper > F(457, 10000)
    ):
        raise CertificateError("full-phase exact bounds changed")
    if chamber0_primal_interval is None:
        raise AssertionError("missing chamber zero")
    chamber0_log_lower, chamber0_log_upper = _log_interval(F(277, 4) / F(553, 8))
    chamber0_lower = chamber0_primal_interval[0] / chamber0_log_upper
    chamber0_primal_upper = chamber0_primal_interval[1] / chamber0_log_lower

    local_records = value["local_chamber0_dual"]["piece_records"]
    local_raw_lower = local_raw_upper = F(0)
    local_duals = local_checks = 0
    for record in local_records:
        left = _fraction(record["left"], "local.left")
        right = _fraction(record["right"], "local.right")
        for epoch, key in ((4, "n4"), (8, "n8")):
            dual = record[key]
            denominator = dual["denominator"]
            weights = dual["weights"]
            hc, ho, weighted_rows, dc, do, objective = _dual_epoch_reconstruction(
                left, right, epoch, denominator, weights
            )
            if dc != _fraction(record[f"Dc{epoch}"], f"local.Dc{epoch}"):
                raise CertificateError("local dual Dc mismatch")
            if do != _fraction(record[f"Do{epoch}"], f"local.Do{epoch}"):
                raise CertificateError("local dual Do mismatch")
            if objective != _fraction(dual["objective"], "local dual objective"):
                raise CertificateError("local dual objective mismatch")
            for endpoint in (left, right):
                if not _bareiss_positive_definite(
                    _integer_slack(hc, ho, weighted_rows, denominator, endpoint)
                ):
                    raise CertificateError("local dual endpoint slack is not positive definite")
                local_checks += 1
            local_duals += 1
        piece_lower, piece_upper = _dual_piece_interval(record)
        local_raw_lower += piece_lower
        local_raw_upper += piece_upper
    chamber0_upper = local_raw_upper / chamber0_log_lower
    if not (
        chamber0_lower <= chamber0_primal_upper <= chamber0_upper < F(2601, 100000)
        and prototype_lower > chamber0_upper
        and prototype_lower - chamber0_upper > F(207, 1000000)
    ):
        raise CertificateError("chamber-zero exact obstruction changed")
    summary = {
        "chambers_replayed": 161,
        "rational_gram_columns": rational_columns,
        "generic_owner_rows": generic_rows,
        "generic_owner_endpoint_checks": generic_endpoint_checks,
        "collapsed_endpoint_owner_rows": collapsed_rows,
        "all_gram_matrices_psd_by_rational_factor": True,
        "all_owner_rows_nonnegative": True,
        "raw_integral_lower": raw_lower,
        "raw_integral_upper": raw_upper,
        "normalized_lower": normalized_lower,
        "normalized_upper": normalized_upper,
        "prototype_rhs_lower": prototype_lower,
        "prototype_rhs_upper": prototype_upper,
        "chamber0_lower": chamber0_lower,
        "chamber0_upper": chamber0_upper,
        "local_dual_pieces": len(local_records),
        "local_duals_replayed": local_duals,
        "local_dual_endpoint_ldl_checks": local_checks,
    }
    if (
        rational_columns != 2285
        or generic_rows != 99176
        or generic_endpoint_checks != 198352
        or collapsed_rows != 194528
        or local_duals != 16
        or local_checks != 32
    ):
        raise CertificateError("replay census changed")
    _REPLAY_CACHE[digest] = dict(summary)
    return summary


def replay_exact(value: Mapping[str, Any]) -> dict[str, Any]:
    _validate_static(value)
    return _replay_validated(value)


def verify_certificate(value: Mapping[str, Any]) -> dict[str, Any]:
    _validate_static(value)
    return _replay_validated(value)


def _load_canonical(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise CertificateError(f"certificate is not canonical UTF-8 JSON: {error}") from error
    if type(value) is not dict or raw != rendered_bytes(value):
        raise CertificateError("certificate bytes are not canonical JSON")
    return value


def build_certificate(path: Path = DEFAULT_CERTIFICATE) -> dict[str, Any]:
    value = _load_canonical(Path(path))
    verify_certificate(value)
    return value


def self_check(value: Mapping[str, Any]) -> dict[str, int]:
    verify_certificate(value)
    mutations: list[tuple[str, dict[str, Any]]] = []

    def add(label: str, mutator: Any) -> None:
        changed = copy.deepcopy(value)
        mutator(changed)
        changed["integrity"]["payload_sha256"] = payload_hash(changed)
        mutations.append((label, changed))

    add("schema", lambda x: x.__setitem__("schema", SCHEMA + ".mutated"))
    add("status", lambda x: x.__setitem__("status", "UNSOUND"))
    add("fixture", lambda x: x["fixture"]["points"].__setitem__(1, 21))
    add("envelope", lambda x: x["fixture"]["finite_dyadic_envelope"].__setitem__("actual_cap_formula", "N_m <= C*m^2*log(m)"))
    add("phase", lambda x: x["phase"]["breakpoints"].__setitem__(1, "70/1"))
    add("model", lambda x: x["model"].__setitem__("rho", "1/2"))
    add("prototype", lambda x: x["prototype"].__setitem__("B", "1/4"))
    add("primal-index", lambda x: x["primal_certificate"]["chambers"][0].__setitem__("index", 1))
    add("primal-column", lambda x: x["primal_certificate"]["chambers"][0]["columns"][0].__setitem__(0, x["primal_certificate"]["chambers"][0]["columns"][0][0] + 1))
    add("negative-dual", lambda x: x["local_chamber0_dual"]["piece_records"][0]["n4"]["weights"].__setitem__(0, -1))
    add("conclusion", lambda x: x["conclusion"].__setitem__("complete_phase_integrated_prototype_survives", False))
    add("scope", lambda x: x["scope"].__setitem__("C058_resolved", True))
    add("arithmetic", lambda x: x["integrity"].__setitem__("exact_replay_arithmetic", "float"))
    rejected = 0
    for label, mutation in mutations:
        try:
            verify_certificate(mutation)
        except CertificateError:
            rejected += 1
        else:
            raise CertificateError(f"self-check mutation accepted: {label}")
    return {"mutations_attempted": len(mutations), "mutations_rejected": rejected}


def _canonicalize_discovery(directory: Path, local_dual_path: Path) -> dict[str, Any]:
    breakpoints = _breakpoints()
    chambers = []
    for index, (left, right) in enumerate(zip(breakpoints, breakpoints[1:])):
        path = directory / f"erdos1191_reverse_primal_chamber_{index:03d}.json"
        discovered = json.loads(path.read_text(encoding="utf-8"))
        if F(discovered["a"]) != left or F(discovered["b"]) != right:
            raise CertificateError("discovery chamber endpoints changed")
        chambers.append({
            "index": index,
            "left": ftext(left),
            "right": ftext(right),
            "denominator": int(discovered["den"]),
            "rank4": int(discovered["rank4"]),
            "rank8": int(discovered["rank8"]),
            "columns": discovered["columns"],
        })
    local_source = local_dual_path.read_bytes()
    local_discovery = json.loads(local_source.decode("utf-8"))
    if hashlib.sha256(local_source).hexdigest() != SOURCE_LOCAL_DUAL_SHA256:
        raise CertificateError("local dual discovery hash differs")
    local_records = []
    for record in local_discovery["dual_piece_records"]:
        simplified = {
            key: record[key]
            for key in ("index", "left", "right", "Dc4", "Do4", "Dc8", "Do8")
        }
        for key in ("n4", "n8"):
            simplified[key] = {
                "denominator": record[key]["denominator"],
                "weights": record[key]["weights"],
                "objective": record[key]["objective"],
            }
        local_records.append(simplified)
    value: dict[str, Any] = {
        "schema": SCHEMA,
        "status": STATUS,
        "fixture": {
            "points": list(POINTS),
            "positive_difference_count": 120,
            "H2": 430,
            "H3": 656,
            "eta_ratio": "82/215",
            "V2": "20177/66402",
            "V3": "2143/29039",
            "delta_V": "-443620417/1928247678",
            "finite_dyadic_envelope": {
                "canonical_constant": 2,
                "actual_cap_formula": "N_m <= 2*C*m^2*log(m)",
                "rows": [dict(row) for row in EXPECTED_ENVELOPE_ROWS],
                "all_rows_certified": True,
                "eventual_infinite_ray_constructed": False,
            },
        },
        "phase": {
            "lower": ftext(PHASE_LOWER),
            "upper": ftext(PHASE_UPPER),
            "event_line_count": len(EVENT_LINES),
            "chamber_count": len(breakpoints) - 1,
            "breakpoints": [ftext(point) for point in breakpoints],
        },
        "model": copy.deepcopy(EXPECTED_MODEL),
        "prototype": copy.deepcopy(EXPECTED_PROTOTYPE),
        "primal_certificate": {"chambers": chambers},
        "local_chamber0_dual": {
            "interval": ["553/8", "277/4"],
            "partition_count": 8,
            "piece_records": local_records,
        },
        "conclusion": copy.deepcopy(EXPECTED_CONCLUSION),
        "scope": copy.deepcopy(EXPECTED_SCOPE),
        "integrity": {
            "algorithm": "sha256",
            "payload_sha256": "",
            "source_primal_manifest_sha256": SOURCE_PRIMAL_MANIFEST_SHA256,
            "source_local_dual_sha256": SOURCE_LOCAL_DUAL_SHA256,
            "exact_replay_arithmetic": "fractions.Fraction plus integer rational-Gram and Bareiss/Sylvester replay",
        },
    }
    value["integrity"]["payload_sha256"] = payload_hash(value)
    _validate_static(value)
    return value


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", type=Path)
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--canonicalize-discovery-dir", type=Path)
    parser.add_argument("--local-dual", type=Path)
    parser.add_argument("--output", type=Path, default=DEFAULT_CERTIFICATE)
    arguments = parser.parse_args(argv)
    if arguments.canonicalize_discovery_dir is not None:
        if arguments.local_dual is None:
            raise CertificateError("--local-dual is required for canonicalization")
        value = _canonicalize_discovery(arguments.canonicalize_discovery_dir, arguments.local_dual)
        arguments.output.write_bytes(rendered_bytes(value))
        print(f"CANONICALIZED chambers=161 output={arguments.output}")
        return 0
    target = arguments.verify or DEFAULT_CERTIFICATE
    value = _load_canonical(target)
    summary = verify_certificate(value)
    fields = [
        "VERIFY_OK",
        f"chambers_replayed={summary['chambers_replayed']}",
        f"gram_columns={summary['rational_gram_columns']}",
        f"owner_endpoint_checks={summary['generic_owner_endpoint_checks']}",
        f"local_endpoint_ldl_checks={summary['local_dual_endpoint_ldl_checks']}",
        "full_phase_prototype_survives_exactly",
        "chamber0_pointwise_prototype_fails_exactly",
    ]
    if arguments.self_check:
        mutations = self_check(value)
        fields.append(f"mutations_rejected={mutations['mutations_rejected']}")
    print(" ".join(fields))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
