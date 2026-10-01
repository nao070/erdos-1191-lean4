#!/usr/bin/env python3
"""Exact replay certificate for a finite eta-negative full-phase obstruction.

The certificate is deliberately narrower than C058.  It records rational dual
weights for one 16-mark Golomb fixture in the four-width, disjoint-epoch owner
cone.  The verifier reconstructs every chamber from the fixture, recomputes all
dual objectives and ``Dc/Do`` coefficients, and checks both rational endpoints
of every semidefinite slack exactly.

The exploratory SDP was used only to discover the stored nonnegative weights.
This canonical verifier has no NumPy/CVXPY dependency: it uses ``Fraction`` for
the model and a fraction-free Bareiss/Sylvester test for positive definiteness.
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
from typing import Any, Mapping, Sequence

import direct_b_membership_sddm_lp_certificate as membership


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_ETA_NEGATIVE_FULL_PHASE_DUAL_NO_GO_certificate.json"
SCHEMA = "erdos1191.c058_eta_negative_full_phase_dual_no_go.v1"
STATUS = "EXACT_FINITE_FULL_PHASE_DUAL_NO_GO_ONLY_C058_OPEN"
DISCOVERY_SCHEMA = "erdos1191.c058_eta_negative_full_phase_dual.discovery.v1"

POINTS = (
    0, 26, 60, 77, 110, 175, 326, 519,
    529, 543, 566, 622, 724, 933, 1349, 2178,
)
MULTIPLIERS = (1, 2, 4, 8)
RHO = F(9, 16)
BASE = F(POINTS[15] - POINTS[8], 8)
PHASE_LOWER = BASE
PHASE_UPPER = 2 * BASE
LOG_TERMS = 20
STRICT_BOUND = -F(1, 40)
RAW_INTERVAL_LOWER = -F(13913, 500000)
RAW_INTERVAL_UPPER = -F(139, 5000)
NORMALIZED_INTERVAL_LOWER = -F(81, 2000)
NORMALIZED_INTERVAL_UPPER = -F(1, 25)
SOURCE_DISCOVERY_SHA256 = "d83acb7de05ff566c6ccad0e03348c32bb2038d08683c0f680d35aa67f609836"

# Channel ordering and line ordering are part of the certificate convention.
CHANNELS = tuple((rank, mult, POINTS[rank]) for mult in MULTIPLIERS for rank in range(3, 16))
EVENT_LINES = tuple(
    sorted({(origin, shift * mult) for _, mult, origin in CHANNELS for shift in (0, 1, 2)})
)

TOP_KEYS = {
    "schema", "status", "fixture", "phase", "model", "dual_certificate",
    "conclusion", "scope", "integrity",
}
FIXTURE_KEYS = {
    "points", "positive_difference_count", "H2", "H3", "eta_ratio",
    "finite_dyadic_envelope",
}
ENVELOPE_KEYS = {
    "canonical_constant", "actual_cap_formula", "rows", "all_rows_certified",
    "eventual_infinite_ray_constructed",
}
ENVELOPE_ROW_KEYS = {"m", "N_m", "required_log"}
PHASE_KEYS = {"lower", "upper", "event_line_count", "chamber_count", "breakpoints"}
MODEL_KEYS = {
    "rho", "multipliers", "channel_rank_range", "epoch_4_owned_rank_range",
    "epoch_8_demand_rank_range", "epoch_8_owned_rank_range",
    "haar_sign_convention", "log_enclosure", "positive_definite_test",
}
DUAL_KEYS = {"chambers"}
CHAMBER_KEYS = {"index", "left", "right", "Dc4", "Do4", "Dc8", "Do8", "n4", "n8"}
EPOCH_KEYS = {"denominator", "weights", "objective"}
CONCLUSION_KEYS = {
    "log_integral_upper_less_than", "normalized_log_phase_upper_less_than",
    "strictly_negative_full_phase_margin",
}
SCOPE_KEYS = {
    "finite_geometry_free_bare_eta_bridge_refuted",
    "large_rank_local_inequality_refuted",
    "eventual_critical_infinite_history_constructed",
    "C058_refuted", "Q1_Q2_resolved", "publication_novelty_or_prize_claimed",
}
INTEGRITY_KEYS = {
    "algorithm", "payload_sha256", "source_discovery_sha256", "exact_replay_arithmetic",
}

EXPECTED_ENVELOPE_ROWS = (
    {"m": 4, "N_m": 78, "required_log": "39/32"},
    {"m": 8, "N_m": 520, "required_log": "65/32"},
    {"m": 16, "N_m": 2179, "required_log": "2179/1024"},
)
EXPECTED_MODEL = {
    "rho": "9/16",
    "multipliers": [1, 2, 4, 8],
    "channel_rank_range": [3, 15],
    "epoch_4_owned_rank_range": [3, 7],
    "epoch_8_demand_rank_range": [7, 15],
    "epoch_8_owned_rank_range": [8, 15],
    "haar_sign_convention": "+1 on [0,t), -1 on [t,2t), 0 otherwise; half-open",
    "log_enclosure": "20-term rational atanh series with explicit positive tail",
    "positive_definite_test": "fraction-free Bareiss leading principal minors",
}
EXPECTED_SCOPE = {
    "finite_geometry_free_bare_eta_bridge_refuted": True,
    "large_rank_local_inequality_refuted": False,
    "eventual_critical_infinite_history_constructed": False,
    "C058_refuted": False,
    "Q1_Q2_resolved": False,
    "publication_novelty_or_prize_claimed": False,
}
EXPECTED_CONCLUSION = {
    "log_integral_upper_less_than": "-1/40",
    "normalized_log_phase_upper_less_than": "-1/40",
    "strictly_negative_full_phase_margin": True,
}


class CertificateError(RuntimeError):
    """Raised when a schema, exact identity, PSD check, or scope gate fails."""


def ftext(value: F | int) -> str:
    """Return the unique numerator/denominator spelling used in the payload."""
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
        raise CertificateError(f"{label}: expected an object")
    actual = set(value)
    if actual != expected:
        raise CertificateError(
            f"{label}: schema keys differ; missing={sorted(expected-actual)}, extra={sorted(actual-expected)}"
        )
    return value


def _exact_int(value: object, label: str, *, minimum: int | None = None) -> int:
    if type(value) is not int:
        raise CertificateError(f"{label}: expected an integer")
    if minimum is not None and value < minimum:
        raise CertificateError(f"{label}: integer is below {minimum}")
    return value


def rendered_bytes(value: Mapping[str, Any]) -> bytes:
    """Canonical JSON encoding (the final newline is part of the file)."""
    return (
        json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode("utf-8")


def payload_hash(value: Mapping[str, Any]) -> str:
    """Hash the payload with its own hash slot set to the empty string."""
    if type(value) is not dict or type(value.get("integrity")) is not dict:
        raise CertificateError("payload hash requires an integrity object")
    clone = copy.deepcopy(value)
    clone["integrity"]["payload_sha256"] = ""
    return hashlib.sha256(rendered_bytes(clone)).hexdigest()


def _positive_differences(points: Sequence[int]) -> tuple[int, ...]:
    if any(type(point) is not int for point in points):
        raise CertificateError("fixture points must be integers")
    if any(points[i] >= points[i + 1] for i in range(len(points) - 1)):
        raise CertificateError("fixture points are not strictly increasing")
    differences = tuple(
        points[j] - points[i]
        for i in range(len(points))
        for j in range(i + 1, len(points))
    )
    if len(differences) != len(set(differences)):
        raise CertificateError("fixture is not a Golomb ruler")
    return differences


def _breakpoints() -> tuple[F, ...]:
    result = {PHASE_LOWER, PHASE_UPPER}
    for origin_1, slope_1 in EVENT_LINES:
        for origin_2, slope_2 in EVENT_LINES:
            if slope_1 == slope_2:
                continue
            crossing = F(origin_2 - origin_1, slope_1 - slope_2)
            if PHASE_LOWER < crossing < PHASE_UPPER:
                result.add(crossing)
    return tuple(sorted(result))


def _sign_at(x: F, width: F, origin: int, multiplier: int) -> int:
    displacement = x - origin
    return int(0 <= displacement < multiplier * width) - int(
        multiplier * width <= displacement < 2 * multiplier * width
    )


def _state(x: F, width: F) -> tuple[int, ...]:
    return tuple(
        (8 // multiplier) * _sign_at(x, width, origin, multiplier)
        for _, multiplier, origin in CHANNELS
    )


def _zero_int_matrix(size: int) -> list[list[int]]:
    return [[0 for _ in range(size)] for _ in range(size)]


def _add_integer_outer(matrix: list[list[int]], coefficient: int, vector: Sequence[int]) -> None:
    nonzero = tuple((i, value) for i, value in enumerate(vector) if value)
    for i, left in nonzero:
        row = matrix[i]
        scaled = coefficient * left
        for j, right in nonzero:
            row[j] += scaled * right


def _add_integer_symmetric_outer(
    matrix: list[list[int]], coefficient: int, left: Sequence[int], right: Sequence[int]
) -> None:
    """Add coefficient*(left*right^T + right*left^T)."""
    left_nonzero = tuple((i, value) for i, value in enumerate(left) if value)
    right_nonzero = tuple((i, value) for i, value in enumerate(right) if value)
    for i, left_value in left_nonzero:
        scaled = coefficient * left_value
        for j, right_value in right_nonzero:
            contribution = scaled * right_value
            matrix[i][j] += contribution
            matrix[j][i] += contribution


def _integer_slack(
    constant_matrix: Sequence[Sequence[int]],
    reciprocal_matrix: Sequence[Sequence[int]],
    weighted_row_numerator: Sequence[Sequence[int]],
    denominator: int,
    endpoint: F,
) -> list[list[int]]:
    """Scale Hc + Ho/t - W/(2*denominator) to an integer matrix."""
    endpoint_numerator = endpoint.numerator
    endpoint_denominator = endpoint.denominator
    scale = math.lcm(endpoint_numerator, 2 * denominator)
    reciprocal_scale = endpoint_denominator * (scale // endpoint_numerator)
    row_scale = scale // (2 * denominator)
    return [
        [
            constant_matrix[i][j] * scale
            + reciprocal_matrix[i][j] * reciprocal_scale
            - weighted_row_numerator[i][j] * row_scale
            for j in range(len(constant_matrix))
        ]
        for i in range(len(constant_matrix))
    ]


def _bareiss_positive_definite(matrix: Sequence[Sequence[int]]) -> bool:
    """Use Sylvester's criterion with fraction-free Bareiss elimination."""
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise CertificateError("positive-definite check received a nonsquare matrix")
    if any(matrix[i][j] != matrix[j][i] for i in range(size) for j in range(i)):
        raise CertificateError("positive-definite check received a nonsymmetric matrix")
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
                numerator = (
                    work[i][j] * pivot
                    - work[i][pivot_index] * work[pivot_index][j]
                )
                quotient, remainder = divmod(numerator, previous)
                if remainder:
                    raise CertificateError("Bareiss division was not exact")
                work[i][j] = quotient
                work[j][i] = quotient
        previous = pivot
    raise AssertionError("unreachable")


def _epoch_reconstruction(
    left: F,
    right: F,
    epoch: int,
    denominator: int,
    integer_weights: Sequence[int],
) -> tuple[list[list[int]], list[list[int]], list[list[int]], F, F, F]:
    """Reconstruct one chamber/epoch and aggregate its 308 weighted rows."""
    midpoint = (left + right) / 2
    ordered = sorted(EVENT_LINES, key=lambda line: F(line[0]) + line[1] * midpoint)
    channel_index = {(rank, mult): i for i, (rank, mult, _) in enumerate(CHANNELS)}
    block = tuple(
        i for i, (rank, _, _) in enumerate(CHANNELS)
        if (epoch == 4 and rank <= 7) or (epoch == 8 and rank >= 8)
    )
    if epoch not in (4, 8):
        raise CertificateError("unsupported epoch")
    dimension = len(block) - 1
    constant_matrix = _zero_int_matrix(dimension)
    reciprocal_matrix = _zero_int_matrix(dimension)
    weighted_row_numerator = _zero_int_matrix(dimension)
    matrix_m = membership.point_m_matrix(epoch)
    demand_ranks = range(3, 8) if epoch == 4 else range(7, 16)
    owned_ranks = range(3, 8) if epoch == 4 else range(8, 16)
    dc_total = F(0)
    do_total = F(0)
    objective = F(0)
    row_index = 0

    for (left_origin, left_slope), (right_origin, right_slope) in zip(ordered, ordered[1:]):
        left_position = F(left_origin) + left_slope * midpoint
        right_position = F(right_origin) + right_slope * midpoint
        if not left_position < right_position:
            raise CertificateError("event order is not strict inside a chamber")
        q = _state((left_position + right_position) / 2, midpoint)
        origin_delta = right_origin - left_origin
        slope_delta = right_slope - left_slope
        values = [q[i] for i in block]
        y = tuple(value - values[-1] for value in values[:-1])
        _add_integer_outer(constant_matrix, slope_delta, y)
        _add_integer_outer(reciprocal_matrix, origin_delta, y)

        for multiplier in MULTIPLIERS:
            demand = tuple(channel_index[(rank, multiplier)] for rank in demand_ranks)
            owned = tuple(channel_index[(rank, multiplier)] for rank in owned_ranks)
            local = tuple(q[i] for i in demand)
            coefficient = F(multiplier, 128) * membership.quadratic(matrix_m, local)
            owned_vector = [0 for _ in CHANNELS]
            for i in owned:
                owned_vector[i] = q[i]
            owned_values = [owned_vector[i] for i in block]
            z = tuple(value - owned_values[-1] for value in owned_values[:-1])

            weight = integer_weights[row_index]
            if weight:
                _add_integer_symmetric_outer(weighted_row_numerator, weight, z, y)
            objective += F(weight, denominator) * coefficient
            dc_total += slope_delta * coefficient
            do_total += origin_delta * coefficient
            row_index += 1

    if row_index != 308 or len(ordered) - 1 != 77:
        raise CertificateError("unexpected cell/row count in chamber reconstruction")
    return (
        constant_matrix,
        reciprocal_matrix,
        weighted_row_numerator,
        dc_total,
        do_total,
        objective,
    )


def _log_interval(value: F, terms: int = LOG_TERMS) -> tuple[F, F]:
    """Exact lower/upper enclosure for log(value), for value >= 1."""
    if value < 1 or terms <= 0:
        raise ValueError("log enclosure needs value >= 1 and a positive term count")
    z = (value - 1) / (value + 1)
    lower = 2 * sum(
        (z ** (2 * index + 1) / (2 * index + 1) for index in range(terms)),
        F(0),
    )
    tail = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return lower, lower + tail


def _integral_piece_interval(chamber: Mapping[str, Any]) -> tuple[F, F]:
    """Return exact rational lower/upper bounds for one log-integral piece."""
    left = _fraction(chamber["left"], "chamber.left")
    right = _fraction(chamber["right"], "chamber.right")
    objective_4 = _fraction(chamber["n4"]["objective"], "chamber.n4.objective")
    objective_8 = _fraction(chamber["n8"]["objective"], "chamber.n8.objective")
    dc_4 = _fraction(chamber["Dc4"], "chamber.Dc4")
    do_4 = _fraction(chamber["Do4"], "chamber.Do4")
    dc_8 = _fraction(chamber["Dc8"], "chamber.Dc8")
    do_8 = _fraction(chamber["Do8"], "chamber.Do8")
    log_coefficient = 2 * (dc_4 + RHO * dc_8) - (objective_4 + RHO * objective_8)
    reciprocal_coefficient = 2 * (do_4 + RHO * do_8)
    log_lower, log_upper = _log_interval(right / left)
    reciprocal_piece = reciprocal_coefficient * (F(1, left) - F(1, right))
    if log_coefficient >= 0:
        return (
            log_coefficient * log_lower + reciprocal_piece,
            log_coefficient * log_upper + reciprocal_piece,
        )
    return (
        log_coefficient * log_upper + reciprocal_piece,
        log_coefficient * log_lower + reciprocal_piece,
    )


def _integral_piece(chamber: Mapping[str, Any]) -> F:
    """Return the exact rational upper bound used by the original certificate."""
    return _integral_piece_interval(chamber)[1]


def _validate_static(value: Mapping[str, Any], *, check_hash: bool = True) -> None:
    payload = _exact_keys(value, TOP_KEYS, "payload")
    if payload["schema"] != SCHEMA or payload["status"] != STATUS:
        raise CertificateError("schema or status mismatch")

    fixture = _exact_keys(payload["fixture"], FIXTURE_KEYS, "fixture")
    if fixture["points"] != list(POINTS):
        raise CertificateError("fixture points differ from the certified fixture")
    differences = _positive_differences(fixture["points"])
    if fixture["positive_difference_count"] != len(differences) or len(differences) != 120:
        raise CertificateError("positive-difference count mismatch")
    h2 = POINTS[7] - POINTS[3]
    h3 = POINTS[15] - POINTS[7]
    if fixture["H2"] != h2 or fixture["H3"] != h3:
        raise CertificateError("H2/H3 mismatch")
    if _fraction(fixture["eta_ratio"], "fixture.eta_ratio") != F(h3, 4 * h2):
        raise CertificateError("eta ratio mismatch")
    if not _fraction(fixture["eta_ratio"], "fixture.eta_ratio") < 1:
        raise CertificateError("fixture does not have a negative shell increment")

    envelope = _exact_keys(
        fixture["finite_dyadic_envelope"], ENVELOPE_KEYS, "fixture.finite_dyadic_envelope"
    )
    if envelope["canonical_constant"] != 2:
        raise CertificateError("finite-envelope constant mismatch")
    if envelope["actual_cap_formula"] != "N_m <= 2*C*m^2*log(m)":
        raise CertificateError("finite-envelope convention mismatch")
    if type(envelope["rows"]) is not list or len(envelope["rows"]) != 3:
        raise CertificateError("finite-envelope rows mismatch")
    log_two_lower, _ = _log_interval(F(2))
    for index, (row, expected) in enumerate(zip(envelope["rows"], EXPECTED_ENVELOPE_ROWS)):
        checked = _exact_keys(row, ENVELOPE_ROW_KEYS, f"envelope.rows[{index}]")
        if checked != expected:
            raise CertificateError("finite-envelope row differs from the exact fixture")
        required_log = _fraction(checked["required_log"], "envelope.required_log")
        exponent = {4: 2, 8: 3, 16: 4}[checked["m"]]
        if not required_log < exponent * log_two_lower:
            raise CertificateError("finite-envelope row is not certified by the rational log bound")
    if envelope["all_rows_certified"] is not True:
        raise CertificateError("finite-envelope rows are not marked certified")
    if envelope["eventual_infinite_ray_constructed"] is not False:
        raise CertificateError("finite fixture must not claim an eventual infinite ray")

    breakpoints = _breakpoints()
    phase = _exact_keys(payload["phase"], PHASE_KEYS, "phase")
    expected_breakpoint_text = [ftext(point) for point in breakpoints]
    if (
        phase["lower"] != ftext(PHASE_LOWER)
        or phase["upper"] != ftext(PHASE_UPPER)
        or phase["event_line_count"] != len(EVENT_LINES)
        or phase["chamber_count"] != len(breakpoints) - 1
        or phase["breakpoints"] != expected_breakpoint_text
    ):
        raise CertificateError("phase partition mismatch")
    if len(EVENT_LINES) != 78 or len(breakpoints) != 88:
        raise CertificateError("internal event/chamber convention drifted")

    model = _exact_keys(payload["model"], MODEL_KEYS, "model")
    if model != EXPECTED_MODEL:
        raise CertificateError("model convention mismatch")
    dual = _exact_keys(payload["dual_certificate"], DUAL_KEYS, "dual_certificate")
    chambers = dual["chambers"]
    if type(chambers) is not list or len(chambers) != len(breakpoints) - 1:
        raise CertificateError("dual chamber count mismatch")
    for index, (chamber, left, right) in enumerate(zip(chambers, breakpoints, breakpoints[1:])):
        checked = _exact_keys(chamber, CHAMBER_KEYS, f"chambers[{index}]")
        if checked["index"] != index:
            raise CertificateError("chamber index mismatch")
        if checked["left"] != ftext(left) or checked["right"] != ftext(right):
            raise CertificateError("chamber endpoints mismatch")
        for coefficient in ("Dc4", "Do4", "Dc8", "Do8"):
            _fraction(checked[coefficient], f"chambers[{index}].{coefficient}")
        for epoch_key in ("n4", "n8"):
            epoch = _exact_keys(checked[epoch_key], EPOCH_KEYS, f"chambers[{index}].{epoch_key}")
            denominator = _exact_int(epoch["denominator"], "dual denominator", minimum=1)
            if denominator != 100_000:
                raise CertificateError("unexpected dual denominator")
            weights = epoch["weights"]
            if type(weights) is not list or len(weights) != 308:
                raise CertificateError("dual weight-vector length mismatch")
            for weight in weights:
                _exact_int(weight, "dual weight", minimum=0)
            _fraction(epoch["objective"], "dual objective")

    conclusion = _exact_keys(payload["conclusion"], CONCLUSION_KEYS, "conclusion")
    if conclusion != EXPECTED_CONCLUSION:
        raise CertificateError("conclusion gate mismatch")
    scope = _exact_keys(payload["scope"], SCOPE_KEYS, "scope")
    if scope != EXPECTED_SCOPE:
        raise CertificateError("scope gate mismatch")

    integrity = _exact_keys(payload["integrity"], INTEGRITY_KEYS, "integrity")
    if integrity["algorithm"] != "sha256":
        raise CertificateError("integrity algorithm mismatch")
    if integrity["exact_replay_arithmetic"] != (
        "fractions.Fraction plus fraction-free integer Bareiss/Sylvester"
    ):
        raise CertificateError("exact replay arithmetic label mismatch")
    for name in ("payload_sha256", "source_discovery_sha256"):
        digest = integrity[name]
        if type(digest) is not str or re.fullmatch(r"[0-9a-f]{64}", digest) is None:
            raise CertificateError(f"{name}: invalid sha256 spelling")
    if integrity["source_discovery_sha256"] != SOURCE_DISCOVERY_SHA256:
        raise CertificateError("source discovery sha256 mismatch")
    if check_hash and integrity["payload_sha256"] != payload_hash(payload):
        raise CertificateError("payload sha256 mismatch")


_REPLAY_CACHE: dict[str, dict[str, Any]] = {}


def _replay_validated(value: Mapping[str, Any]) -> dict[str, Any]:
    digest = value["integrity"]["payload_sha256"]
    cached = _REPLAY_CACHE.get(digest)
    if cached is not None:
        return dict(cached)

    chambers = value["dual_certificate"]["chambers"]
    epoch_duals = 0
    endpoint_checks = 0
    for chamber in chambers:
        left = _fraction(chamber["left"], "chamber.left")
        right = _fraction(chamber["right"], "chamber.right")
        for epoch, key in ((4, "n4"), (8, "n8")):
            record = chamber[key]
            denominator = record["denominator"]
            weights = record["weights"]
            (
                constant_matrix,
                reciprocal_matrix,
                weighted_row_numerator,
                dc_total,
                do_total,
                objective,
            ) = _epoch_reconstruction(left, right, epoch, denominator, weights)
            if objective != _fraction(record["objective"], f"{key}.objective"):
                raise CertificateError(f"chamber {chamber['index']} {key}: objective mismatch")
            if dc_total != _fraction(chamber[f"Dc{epoch}"], f"Dc{epoch}"):
                raise CertificateError(f"chamber {chamber['index']} {key}: Dc mismatch")
            if do_total != _fraction(chamber[f"Do{epoch}"], f"Do{epoch}"):
                raise CertificateError(f"chamber {chamber['index']} {key}: Do mismatch")
            for endpoint in (left, right):
                integer_slack = _integer_slack(
                    constant_matrix,
                    reciprocal_matrix,
                    weighted_row_numerator,
                    denominator,
                    endpoint,
                )
                if not _bareiss_positive_definite(integer_slack):
                    raise CertificateError(
                        f"chamber {chamber['index']} {key}: endpoint slack is not positive definite"
                    )
                endpoint_checks += 1
            epoch_duals += 1

    integral_intervals = [_integral_piece_interval(chamber) for chamber in chambers]
    exact_lower = sum((lower for lower, _ in integral_intervals), F(0))
    exact_upper = sum((upper for _, upper in integral_intervals), F(0))
    if not exact_upper < STRICT_BOUND < 0:
        raise CertificateError("exact log-integral upper bound is not below -1/40")
    if not RAW_INTERVAL_LOWER < exact_lower <= exact_upper < RAW_INTERVAL_UPPER < 0:
        raise CertificateError("exact log-integral interval misses the strengthened rational bounds")
    log_two_lower, log_two_upper = _log_interval(F(2))
    if not (0 < log_two_lower < log_two_upper < 1):
        raise CertificateError("rational log(2) enclosure is insufficient for normalization")
    # Both numerator endpoints are negative.  The normalized ratio is therefore
    # minimized at (exact_lower, log_two_lower) and maximized at
    # (exact_upper, log_two_upper).
    normalized_lower = exact_lower / log_two_lower
    normalized_upper = exact_upper / log_two_upper
    if not (
        NORMALIZED_INTERVAL_LOWER
        < normalized_lower
        <= normalized_upper
        < NORMALIZED_INTERVAL_UPPER
        < 0
    ):
        raise CertificateError("normalized log-phase interval misses (-81/2000,-1/25)")
    summary = {
        "chambers_replayed": len(chambers),
        "epoch_duals_replayed": epoch_duals,
        "endpoint_ldl_checks": endpoint_checks,
        "all_weights_nonnegative": True,
        "all_endpoint_slacks_positive_definite": True,
        "exact_log_integral_lower": exact_lower,
        "exact_log_integral_upper": exact_upper,
        "normalized_log_phase_lower": normalized_lower,
        "normalized_log_phase_upper": normalized_upper,
        "normalized_log_phase_upper_less_than_bound": True,
    }
    _REPLAY_CACHE[digest] = dict(summary)
    return summary


def replay_exact(value: Mapping[str, Any]) -> dict[str, Any]:
    """Replay all 174 duals, 348 endpoint PSD checks, and the log integral."""
    _validate_static(value)
    return _replay_validated(value)


def verify_certificate(value: Mapping[str, Any]) -> dict[str, Any]:
    """Strictly validate schema/hash/scope, then perform the exact replay."""
    _validate_static(value)
    return _replay_validated(value)


def _load_canonical(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CertificateError(f"certificate is not canonical UTF-8 JSON: {exc}") from exc
    if type(value) is not dict or raw != rendered_bytes(value):
        raise CertificateError("certificate bytes are not in the canonical JSON encoding")
    return value


def build_certificate(path: Path = DEFAULT_CERTIFICATE) -> dict[str, Any]:
    """Load and completely verify the canonical checked-in certificate."""
    value = _load_canonical(Path(path))
    verify_certificate(value)
    return value


def self_check(value: Mapping[str, Any]) -> dict[str, int]:
    """Require independent rejection of a hardened mutation set."""
    verify_certificate(value)
    mutations: list[tuple[str, Any]] = []

    def add(label: str, mutator: Any) -> None:
        changed = copy.deepcopy(value)
        mutator(changed)
        changed["integrity"]["payload_sha256"] = payload_hash(changed)
        mutations.append((label, changed))

    add("schema", lambda x: x.__setitem__("schema", SCHEMA + ".mutated"))
    add("status", lambda x: x.__setitem__("status", "UNSOUND"))
    add("fixture", lambda x: x["fixture"]["points"].__setitem__(1, 25))
    add("envelope", lambda x: x["fixture"]["finite_dyadic_envelope"].__setitem__(
        "actual_cap_formula", "N_m <= C*m^2*log(m)"
    ))
    add("phase", lambda x: x["phase"]["breakpoints"].__setitem__(1, "207/1"))
    add("model", lambda x: x["model"].__setitem__("rho", "1/2"))
    add("chamber-index", lambda x: x["dual_certificate"]["chambers"][0].__setitem__("index", 1))
    add("negative-weight", lambda x: x["dual_certificate"]["chambers"][0]["n4"]["weights"].__setitem__(0, -1))
    add("short-weight-vector", lambda x: x["dual_certificate"]["chambers"][0]["n8"]["weights"].pop())
    add("conclusion", lambda x: x["conclusion"].__setitem__("strictly_negative_full_phase_margin", False))
    add("scope", lambda x: x["scope"].__setitem__("C058_refuted", True))
    add("arithmetic-label", lambda x: x["integrity"].__setitem__("exact_replay_arithmetic", "float"))

    rejected = 0
    for label, mutation in mutations:
        try:
            verify_certificate(mutation)
        except CertificateError:
            rejected += 1
        else:
            raise CertificateError(f"self-check mutation was accepted: {label}")
    return {"mutations_attempted": len(mutations), "mutations_rejected": rejected}


def _canonicalize_discovery(path: Path) -> dict[str, Any]:
    """Strip an exploratory payload down to the exact canonical witness."""
    raw = path.read_bytes()
    discovery = json.loads(raw.decode("utf-8"))
    if discovery.get("schema") != DISCOVERY_SCHEMA:
        raise CertificateError("unexpected discovery schema")
    breakpoints = _breakpoints()
    if (
        discovery.get("points") != list(POINTS)
        or discovery.get("base") != ftext(BASE)
        or discovery.get("rho") != ftext(RHO)
        or discovery.get("breakpoints") != [ftext(point) for point in breakpoints]
        or len(discovery.get("records", [])) != len(breakpoints) - 1
    ):
        raise CertificateError("discovery fixture/phase does not match the canonical model")

    chambers: list[dict[str, Any]] = []
    for index, (record, left, right) in enumerate(
        zip(discovery["records"], breakpoints, breakpoints[1:])
    ):
        if record.get("index") != index or record.get("left") != ftext(left) or record.get("right") != ftext(right):
            raise CertificateError("discovery chamber order mismatch")
        chamber: dict[str, Any] = {
            "index": index,
            "left": record["left"],
            "right": record["right"],
            "Dc4": record["Dc4"],
            "Do4": record["Do4"],
            "Dc8": record["Dc8"],
            "Do8": record["Do8"],
        }
        for key in ("n4", "n8"):
            epoch = record[key]
            chamber[key] = {
                "denominator": epoch["denominator"],
                "weights": epoch["weights"],
                "objective": epoch["objective"],
            }
        chambers.append(chamber)

    value: dict[str, Any] = {
        "schema": SCHEMA,
        "status": STATUS,
        "fixture": {
            "points": list(POINTS),
            "positive_difference_count": 120,
            "H2": POINTS[7] - POINTS[3],
            "H3": POINTS[15] - POINTS[7],
            "eta_ratio": ftext(F(POINTS[15] - POINTS[7], 4 * (POINTS[7] - POINTS[3]))),
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
        "dual_certificate": {"chambers": chambers},
        "conclusion": dict(EXPECTED_CONCLUSION),
        "scope": dict(EXPECTED_SCOPE),
        "integrity": {
            "algorithm": "sha256",
            "payload_sha256": "",
            "source_discovery_sha256": hashlib.sha256(raw).hexdigest(),
            "exact_replay_arithmetic": (
                "fractions.Fraction plus fraction-free integer Bareiss/Sylvester"
            ),
        },
    }
    value["integrity"]["payload_sha256"] = payload_hash(value)
    _validate_static(value)
    return value


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", type=Path)
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--canonicalize-discovery", type=Path)
    parser.add_argument("--output", type=Path, default=DEFAULT_CERTIFICATE)
    arguments = parser.parse_args(argv)

    if arguments.canonicalize_discovery is not None:
        value = _canonicalize_discovery(arguments.canonicalize_discovery)
        arguments.output.write_bytes(rendered_bytes(value))
        summary = verify_certificate(value)
        print(
            "CANONICALIZED",
            f"chambers_replayed={summary['chambers_replayed']}",
            f"output={arguments.output}",
        )
        return 0

    target = arguments.verify or DEFAULT_CERTIFICATE
    value = _load_canonical(target)
    summary = verify_certificate(value)
    fields = [
        "VERIFY_OK",
        f"chambers_replayed={summary['chambers_replayed']}",
        f"epoch_duals_replayed={summary['epoch_duals_replayed']}",
        f"endpoint_ldl_checks={summary['endpoint_ldl_checks']}",
        "exact_log_integral_upper<-1/40",
        "normalized_log_phase_upper<-1/25",
    ]
    if arguments.self_check:
        mutations = self_check(value)
        fields.append(f"mutations_rejected={mutations['mutations_rejected']}")
    print(" ".join(fields))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
