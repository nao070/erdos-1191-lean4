#!/usr/bin/env python3
"""Exact C123 common-phase integrated rational primal sub-bank.

The certificate replays rational Gram data for the fixed C125 coefficient
candidate on selected chambers of the C126 C123 common phase.  Early chambers
0--21 are compensated after log-phase integration by a sparse set of later
chambers.  The top six / top seven language refers only to the frozen C128
numerical ordering used for discovery; it is not a universal exact minimality
claim.

This is a finite selected-chamber certificate in the independent epoch-block
cone.  It is not a complete-phase witness, a phase-rule admissibility result,
an arbitrary-rank theorem, or a resolution of C058.
"""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any, Callable, Mapping, Sequence


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import ROUTE_C_C125_ORDERED_SUFFIX_FIVE_ROW_BANK_certificate as c125
import ROUTE_C_C126_COMMON_COMPLETED_SHELL_PHASE_certificate as c126


DEFAULT_CERTIFICATE = HERE / "ROUTE_C_C129_COMMON_PHASE_INTEGRATED_PRIMAL_SUBBANK_certificate.json"
C125_VERIFIER = HERE / "ROUTE_C_C125_ORDERED_SUFFIX_FIVE_ROW_BANK_certificate.py"
C126_VERIFIER = HERE / "ROUTE_C_C126_COMMON_COMPLETED_SHELL_PHASE_certificate.py"
C126_CERTIFICATE = HERE / "ROUTE_C_C126_COMMON_COMPLETED_SHELL_PHASE_certificate.json"
C128_VERIFIER = HERE / "ROUTE_C_C128_COMMON_PHASE_POINTWISE_NO_GO_certificate.py"
C128_CERTIFICATE = HERE / "ROUTE_C_C128_COMMON_PHASE_POINTWISE_NO_GO_certificate.json"

SCHEMA = "erdos1191.c129.common_phase_integrated_primal_subbank.v1"
STATUS = "EXACT_FINITE_C123_SELECTED_29_AND_32_CHAMBER_INTEGRATED_PRIMAL_SUBBANK_C058_OPEN"

C125_VERIFIER_SHA256 = "1d9f4d8ea7756eb89fa9e8cc5d44e15a6480057df82392afadd30cbcbcb48fe2"
C126_VERIFIER_SHA256 = "830c6afa79d49d386e5bc57bdb5578b8074e783486cbaf991164ae25e91a5981"
C126_CERTIFICATE_SHA256 = "b1a37954b11a807161d85d916a875058d9a4dab51a5dc208468429fe937074cf"
C126_CERTIFICATE_PAYLOAD_SHA256 = "03a8df34c95e20b3e24d7d1a91d4de169136a699239c3b5f777a60916a1f1f86"
C123_SOURCE_SHA256 = "a47eff804bbdf4082ba61d60202855e2a22b86c2c771df44a1e6f5728e952fae"
C123_INTERNAL_SHA256 = "7415bafcae9c37e043d8d6088fa5471f5916f595c367fde8222d4fe194ac52ab"
C120_MODEL_SHA256 = "6e8d7e3f975e952442672cb1d18e4512d616f343bb4f6379ba0c8701cd996fe9"
C128_VERIFIER_SHA256 = "d6cc32966f58bc6381d8673901f5438e2c2570d20bcd07f8662192a5c3f3dea2"
C128_CERTIFICATE_SHA256 = "6bf92fd94021878dbac450668fb5ccf8d6391e67d628c1bd1dd6a22f68c794e5"
C128_CERTIFICATE_PAYLOAD_SHA256 = "0e7a8418b47d516297ef327c46efb014c8cac9d0636d8517219e45dd0cfc47ad"
FACTOR_BANK_SHA256 = "9f4bf884515930a03502f785e0d6381d81fdd11be7cb01648370f19ce2b58e15"

PHASE_LOWER = F(82)
PHASE_UPPER = F(164)
RHO = F(9, 16)
EPSILON = F(1, 1000)
A_COEFFICIENT = F(1, 1000)
B_COEFFICIENT = F(1, 2)
C_COEFFICIENT = F(1, 10)
E2 = F(0)
ABS_DELTA_V = F(443_620_417, 1_928_247_678)
DELTA_VRT_C123 = F(51_059, 581_790)
LOG_TERMS = 30
DENOMINATOR = 100_000_000
RANK_PRIMES = (1_000_000_007, 1_000_000_009)

DEFICIT_INDICES = tuple(range(22))
TOP6_SURPLUS_INDICES = (120, 122, 126, 132, 133, 134)
MINIMAL_SPARSE7_SURPLUS_INDICES = (88, 120, 122, 126, 132, 133, 134)
ROBUST10_SURPLUS_INDICES = (43, 88, 119, 120, 122, 124, 126, 132, 133, 134)
TOP6_INDICES = DEFICIT_INDICES + TOP6_SURPLUS_INDICES
MINIMAL_SPARSE7_INDICES = DEFICIT_INDICES + MINIMAL_SPARSE7_SURPLUS_INDICES
ROBUST10_INDICES = DEFICIT_INDICES + ROBUST10_SURPLUS_INDICES

EXPECTED_SOURCES = {
    "C125_candidate_verifier": C125_VERIFIER.name,
    "C125_candidate_verifier_sha256": C125_VERIFIER_SHA256,
    "C126_common_phase_verifier": C126_VERIFIER.name,
    "C126_common_phase_verifier_sha256": C126_VERIFIER_SHA256,
    "C126_common_phase_certificate": C126_CERTIFICATE.name,
    "C126_common_phase_certificate_sha256": C126_CERTIFICATE_SHA256,
    "C126_common_phase_certificate_payload_sha256": C126_CERTIFICATE_PAYLOAD_SHA256,
    "C126_C123_dual_source": c126.C123_SOURCE.name,
    "C126_C123_dual_source_sha256": C123_SOURCE_SHA256,
    "C126_C123_dual_source_internal_sha256": C123_INTERNAL_SHA256,
    "C126_exact_model": c126.C120_MODEL_SOURCE.name,
    "C126_exact_model_sha256": C120_MODEL_SHA256,
    "C128_pointwise_no_go_verifier": C128_VERIFIER.name,
    "C128_pointwise_no_go_verifier_sha256": C128_VERIFIER_SHA256,
    "C128_pointwise_no_go_certificate": C128_CERTIFICATE.name,
    "C128_pointwise_no_go_certificate_sha256": C128_CERTIFICATE_SHA256,
    "C128_pointwise_no_go_certificate_payload_sha256": C128_CERTIFICATE_PAYLOAD_SHA256,
}
EXPECTED_CANDIDATE = {
    "epsilon": "1/1000",
    "A": "1/1000",
    "B": "1/2",
    "C_ordered_suffix": "1/10",
    "e2": "0/1",
    "eta": "log(82/215)",
    "DeltaV": "-443620417/1928247678",
    "DeltaVrt_C123": "51059/581790",
    "target_formula": "(epsilon-A*eta-B*DeltaV-C_ordered_suffix*DeltaVrt_C123)/3-e2",
    "log_enclosure_terms": 30,
}
EXPECTED_SELECTION = {
    "common_phase": ["82/1", "164/1"],
    "rho": "9/16",
    "C123_phase_chambers": 135,
    "deficit_indices": list(DEFICIT_INDICES),
    "top6_surplus_indices": list(TOP6_SURPLUS_INDICES),
    "minimal_sparse7_surplus_indices": list(MINIMAL_SPARSE7_SURPLUS_INDICES),
    "robust10_surplus_indices": list(ROBUST10_SURPLUS_INDICES),
    "factor_bank_indices": list(ROBUST10_INDICES),
    "minimality_witness_scope": (
        "exact top-six negative and top-seven positive transition within the frozen "
        "C128 numerical surplus ordering; not universal exact cardinality minimality"
    ),
}
EXPECTED_RESULTS = {
    "factor_bank_chambers": 32,
    "factor_bank_factors": 64,
    "factor_denominator": 100_000_000,
    "rank_min": 9,
    "rank_max": 24,
    "rank_sum": 1004,
    "generic_owner_rows": 12_140,
    "generic_owner_endpoint_checks": 24_280,
    "collapsed_endpoint_owner_rows": 23_745,
    "minimal_sparse7_chambers": 29,
    "minimal_sparse7_factors": 58,
    "minimal_sparse7_rank_sum": 910,
    "minimal_sparse7_generic_owner_rows": 10_987,
    "minimal_sparse7_generic_owner_endpoint_checks": 21_974,
    "minimal_sparse7_collapsed_endpoint_owner_rows": 21_500,
    "top6_raw_margin_less_than": "0/1",
    "minimal_sparse7_raw_margin_greater_than": "1/15000",
    "minimal_sparse7_normalized_margin_greater_than": "99/1000000",
    "robust10_raw_margin_greater_than": "143/400000",
    "robust10_normalized_margin_greater_than": "103/200000",
    "all_factor_columns_modularly_independent": True,
    "all_nonstructural_owner_rows_strictly_positive": True,
}
EXPECTED_SCOPE = {
    "fixed_C123_16_mark_row_only": True,
    "fixed_C125_rational_candidate_only": True,
    "common_completed_shell_phase_82_to_164_only": True,
    "rho_9_over_16_only": True,
    "independent_epoch_block_cone_only": True,
    "exact_selected_29_chamber_integrated_subbank_constructed": True,
    "exact_selected_32_chamber_integrated_subbank_constructed": True,
    "C128_numerical_ordering_used_only_for_selection": True,
    "universal_exact_cardinality_minimality_proved": False,
    "complete_C123_phase_primal_witness_constructed": False,
    "remaining_103_chambers_exactified": False,
    "all_phases_integrated_witness_constructed": False,
    "local_master_inequality_proved": False,
    "global_phase_rule_admissible_proved": False,
    "phase_representative_independence_proved": False,
    "arbitrary_rank_proved": False,
    "global_owner_ledger_constructed": False,
    "C058_resolved": False,
    "Q1_Q2_resolved": False,
    "publication_novelty_or_prize_claimed": False,
}

TOP_KEYS = {
    "schema", "status", "sources", "candidate", "selection", "results",
    "factor_bank", "scope", "integrity",
}
INTEGRITY_KEYS = {
    "algorithm", "payload_sha256", "factor_bank_sha256",
    "exact_replay_arithmetic", "rank_witness_primes",
}
FACTOR_BANK_KEYS = {"records"}
RECORD_KEYS = {"index", "left", "right", "n4", "n8"}
EPOCH_KEYS = {"denominator", "rank", "columns"}


class CertificateError(RuntimeError):
    """Raised for a schema, provenance, Gram, owner, objective, or scope failure."""


def _object_hash(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def payload_hash(value: Mapping[str, Any]) -> str:
    clone = copy.deepcopy(value)
    clone["integrity"]["payload_sha256"] = ""
    return _object_hash(clone)


def rendered_bytes(value: Mapping[str, Any]) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def _exact_dict(value: object, keys: set[str], label: str) -> Mapping[str, Any]:
    if type(value) is not dict or set(value) != keys:
        raise CertificateError(f"{label}: exact keys differ")
    return value


def _exact_int(value: object, label: str, minimum: int | None = None) -> int:
    if type(value) is not int or (minimum is not None and value < minimum):
        raise CertificateError(f"{label}: invalid integer")
    return value


def _fraction_text(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def _read_pinned_compact(path: Path, digest: str, payload_digest: str, label: str) -> dict[str, Any]:
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != digest:
        raise CertificateError(f"{label}: sha256 mismatch")
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CertificateError(f"{label}: invalid JSON") from exc
    if type(value) is not dict or raw != rendered_bytes(value):
        raise CertificateError(f"{label}: noncanonical rendering")
    integrity = value.get("integrity")
    if type(integrity) is not dict or integrity.get("payload_sha256") != payload_digest:
        raise CertificateError(f"{label}: payload hash changed")
    return value


def _verify_provenance() -> None:
    for path, digest, label in (
        (C125_VERIFIER, C125_VERIFIER_SHA256, "C125 verifier"),
        (C126_VERIFIER, C126_VERIFIER_SHA256, "C126 verifier"),
        (c126.C123_SOURCE, C123_SOURCE_SHA256, "C123 source"),
        (c126.C120_MODEL_SOURCE, C120_MODEL_SHA256, "C126 exact model"),
        (C128_VERIFIER, C128_VERIFIER_SHA256, "C128 verifier"),
    ):
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise CertificateError(f"{label}: sha256 mismatch")
    _read_pinned_compact(
        C126_CERTIFICATE, C126_CERTIFICATE_SHA256,
        C126_CERTIFICATE_PAYLOAD_SHA256, "C126 certificate",
    )
    _read_pinned_compact(
        C128_CERTIFICATE, C128_CERTIFICATE_SHA256,
        C128_CERTIFICATE_PAYLOAD_SHA256, "C128 certificate",
    )
    if (
        c126.C123_INTERNAL_SHA256 != C123_INTERNAL_SHA256
        or c126.C120_MODEL_SHA256 != C120_MODEL_SHA256
        or c126.C123_POINTS != (
            0, 22, 60, 83, 154, 284, 494, 513,
            575, 620, 711, 777, 880, 989, 1100, 1169,
        )
        or c126.PHASE_LOWER != PHASE_LOWER
        or c126.PHASE_UPPER != PHASE_UPPER
        or c126.RHO != RHO
    ):
        raise CertificateError("C126 model constants changed")
    actual_candidate = (
        c125.CANDIDATE_EPSILON, c125.CANDIDATE_A, c125.CANDIDATE_B,
        c125.CANDIDATE_C, c125.CANDIDATE_E2, c125.DELTA_V_NEGATIVE_ABS,
        c125.DELTA_VRT_C123, c125.LOG_TERMS,
    )
    expected_candidate = (
        EPSILON, A_COEFFICIENT, B_COEFFICIENT, C_COEFFICIENT, E2,
        ABS_DELTA_V, DELTA_VRT_C123, LOG_TERMS,
    )
    if actual_candidate != expected_candidate:
        raise CertificateError("C125 candidate constants changed")


def _validate_static(value: Mapping[str, Any]) -> None:
    _exact_dict(value, TOP_KEYS, "top")
    if value["schema"] != SCHEMA or value["status"] != STATUS:
        raise CertificateError("schema or status changed")
    if value["sources"] != EXPECTED_SOURCES:
        raise CertificateError("source provenance changed")
    if value["candidate"] != EXPECTED_CANDIDATE:
        raise CertificateError("candidate statement changed")
    if value["selection"] != EXPECTED_SELECTION:
        raise CertificateError("selection statement changed")
    if value["results"] != EXPECTED_RESULTS:
        raise CertificateError("exact result statement changed")
    if value["scope"] != EXPECTED_SCOPE:
        raise CertificateError("scope changed")
    factor_bank = _exact_dict(value["factor_bank"], FACTOR_BANK_KEYS, "factor_bank")
    factor_digest = _object_hash(factor_bank)
    integrity = _exact_dict(value["integrity"], INTEGRITY_KEYS, "integrity")
    if integrity["algorithm"] != "sha256":
        raise CertificateError("integrity algorithm changed")
    if factor_digest != FACTOR_BANK_SHA256 or integrity["factor_bank_sha256"] != FACTOR_BANK_SHA256:
        raise CertificateError("factor bank hash changed")
    if integrity["payload_sha256"] != payload_hash(value):
        raise CertificateError("payload integrity mismatch")
    if integrity["exact_replay_arithmetic"] != (
        "fractions.Fraction; integer rational-Gram with exact positive midpoint scaling; "
        "30-term atanh log enclosures; modular exact-rank witnesses"
    ):
        raise CertificateError("arithmetic statement changed")
    if integrity["rank_witness_primes"] != list(RANK_PRIMES):
        raise CertificateError("rank witness primes changed")


def _target_interval(model: Any) -> tuple[F, F]:
    log_lower, log_upper = model._log_interval(F(215, 82))
    rational = EPSILON + B_COEFFICIENT * ABS_DELTA_V - C_COEFFICIENT * DELTA_VRT_C123
    lower = (rational + A_COEFFICIENT * log_lower) / 3 - E2
    upper = (rational + A_COEFFICIENT * log_upper) / 3 - E2
    if not F(0) < lower <= upper:
        raise CertificateError("target interval malformed")
    return lower, upper


def _modular_column_rank(columns: Sequence[Sequence[int]], prime: int) -> int:
    matrix = [list(row) for row in zip(*columns)]
    row_count = len(matrix)
    column_count = len(columns)
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if matrix[row][column] % prime),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column] % prime, prime - 2, prime)
        matrix[pivot_row] = [(value * inverse) % prime for value in matrix[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            scale = matrix[row][column] % prime
            if scale:
                matrix[row] = [
                    (value - scale * pivot_value) % prime
                    for value, pivot_value in zip(matrix[row], matrix[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def _validate_epoch(value: object, dimension: int, label: str) -> tuple[int, tuple[tuple[int, ...], ...]]:
    epoch = _exact_dict(value, EPOCH_KEYS, label)
    denominator = _exact_int(epoch["denominator"], f"{label}.denominator", 1)
    rank = _exact_int(epoch["rank"], f"{label}.rank", 1)
    if denominator != DENOMINATOR:
        raise CertificateError(f"{label}: denominator changed")
    raw_columns = epoch["columns"]
    if type(raw_columns) is not list or len(raw_columns) != rank:
        raise CertificateError(f"{label}: rank or column count changed")
    columns: list[tuple[int, ...]] = []
    for raw in raw_columns:
        if type(raw) is not list or len(raw) != dimension:
            raise CertificateError(f"{label}: factor dimension changed")
        column = tuple(_exact_int(entry, f"{label}.entry") for entry in raw)
        if not any(column):
            raise CertificateError(f"{label}: zero factor column")
        columns.append(column)
    witnessed_ranks = tuple(
        _modular_column_rank(columns, prime) for prime in RANK_PRIMES
    )
    if any(witnessed != rank for witnessed in witnessed_ranks):
        raise CertificateError(
            f"{label}: factor columns lost independence for a pinned rank prime"
        )
    return denominator, tuple(columns)


def _validate_factor_bank_structure(factor_bank: Mapping[str, Any], model: Any) -> list[dict[str, Any]]:
    _exact_dict(factor_bank, FACTOR_BANK_KEYS, "factor_bank")
    records = factor_bank["records"]
    if type(records) is not list or len(records) != len(ROBUST10_INDICES):
        raise CertificateError("factor bank chamber count changed")
    breakpoints = model._breakpoints()
    if len(breakpoints) != 136:
        raise CertificateError("C123 chamber partition changed")
    checked_records: list[dict[str, Any]] = []
    for position, (record, index) in enumerate(zip(records, ROBUST10_INDICES)):
        checked = _exact_dict(record, RECORD_KEYS, f"records[{position}]")
        left, right = breakpoints[index], breakpoints[index + 1]
        if (
            checked["index"] != index
            or checked["left"] != _fraction_text(left)
            or checked["right"] != _fraction_text(right)
        ):
            raise CertificateError(f"chamber {index}: index or endpoint changed")
        denominator4, columns4 = _validate_epoch(checked["n4"], 19, f"chamber {index}.n4")
        denominator8, columns8 = _validate_epoch(checked["n8"], 31, f"chamber {index}.n8")
        checked_records.append({
            "index": index, "left": left, "right": right,
            "denominator4": denominator4, "columns4": columns4,
            "denominator8": denominator8, "columns8": columns8,
        })
    return checked_records


def _embed_column(column: Sequence[int], block: Sequence[int], size: int) -> tuple[int, ...]:
    if len(column) + 1 != len(block):
        raise CertificateError("reduced factor dimension does not match epoch block")
    full = [0 for _ in range(size)]
    for index, entry in zip(block[:-1], column):
        full[index] = entry
    full[block[-1]] = -sum(column)
    if sum(full) != 0 or not any(full):
        raise CertificateError("embedded factor lost zero sum or became zero")
    return tuple(full)


def _check_epoch_owner_recovery(
    *,
    physical: Mapping[int, F],
    owned: Sequence[F],
    owners: Sequence[tuple[int, int]],
) -> None:
    """Reject cross-epoch cancellation in the owner-share recovery identity."""
    recovered = {
        epoch: sum(
            (value for owner, value in zip(owners, owned) if owner[0] == epoch),
            F(),
        )
        for epoch in (4, 8)
    }
    if recovered[4] != physical[4]:
        raise CertificateError("epoch-4 owner shares do not recover physical energy")
    if recovered[8] != physical[8]:
        raise CertificateError("epoch-8 owner shares do not recover physical energy")
    if recovered[4] + recovered[8] != physical[4] + physical[8]:
        raise CertificateError("combined owner shares do not recover physical energy")


def _make_scaled_evaluator(
    model: Any,
    midpoint: F,
    denominator4: int,
    columns4: Sequence[Sequence[int]],
    denominator8: int,
    columns8: Sequence[Sequence[int]],
) -> Callable[[tuple[int, ...]], tuple[dict[int, F], tuple[F, ...], tuple[F, ...]]]:
    if denominator4 != denominator8:
        raise CertificateError("epoch factor denominators differ")
    full_columns = tuple(
        _embed_column(column, model.EPOCH4_INDICES, len(model.CHANNELS))
        for column in columns4
    ) + tuple(
        _embed_column(column, model.EPOCH8_INDICES, len(model.CHANNELS))
        for column in columns8
    )
    epochs = (4,) * len(columns4) + (8,) * len(columns8)
    scale = F(1, denominator4 * denominator4) / midpoint
    cache: dict[tuple[int, ...], tuple[dict[int, F], tuple[F, ...], tuple[F, ...]]] = {}

    def evaluate(state: tuple[int, ...]) -> tuple[dict[int, F], tuple[F, ...], tuple[F, ...]]:
        cached = cache.get(state)
        if cached is not None:
            return cached
        dots = tuple(
            sum(state[i] * column[i] for i in range(len(state)))
            for column in full_columns
        )
        physical = {
            epoch: scale * sum(
                dot * dot for dot, column_epoch in zip(dots, epochs)
                if column_epoch == epoch
            )
            for epoch in (4, 8)
        }
        owned: list[F] = []
        demands: list[F] = []
        for owner in model.OWNERS:
            group = model._owner_group_indices(owner)
            group_dots = tuple(
                sum(state[i] * column[i] for i in group)
                for column in full_columns
            )
            owned.append(scale * sum(left * right for left, right in zip(group_dots, dots)))
            demands.append(model._owner_c(owner, state))
        _check_epoch_owner_recovery(
            physical=physical,
            owned=owned,
            owners=model.OWNERS,
        )
        result = physical, tuple(owned), tuple(demands)
        cache[state] = result
        return result

    return evaluate


def _owner_row_is_structural(model: Any, owner: tuple[int, int], state: Sequence[int]) -> bool:
    epoch, _ = owner
    block = model.EPOCH4_INDICES if epoch == 4 else model.EPOCH8_INDICES
    values = [state[i] for i in block]
    y = tuple(value - values[-1] for value in values[:-1])
    grouped = [0 for _ in model.CHANNELS]
    for index in model._owner_group_indices(owner):
        grouped[index] = state[index]
    grouped_values = [grouped[i] for i in block]
    z = tuple(value - grouped_values[-1] for value in grouped_values[:-1])
    return any(y) and any(z)


def _check_structural_zero_owner(
    *,
    index: int,
    context: str,
    owner_value: F,
    demand: F,
) -> None:
    """Require both sides of a structurally zero owner row to be compatible."""
    if owner_value != 0:
        raise CertificateError(
            f"chamber {index}: {context} structural-zero owner share is nonzero"
        )
    if demand > 0:
        raise CertificateError(
            f"chamber {index}: positive {context} structural-zero demand"
        )


def _margin_piece_interval(
    model: Any,
    weighted_poly: tuple[F, F, F],
    left: F,
    right: F,
    target_lower: F,
    target_upper: F,
) -> tuple[F, F]:
    phi_lower, phi_upper = model._log_phase_piece_interval(weighted_poly, left, right)
    log_lower, log_upper = model._log_interval(right / left)
    if not phi_lower <= phi_upper or not F() < log_lower <= log_upper:
        raise CertificateError("phase/log interval malformed")
    if not F() < target_lower <= target_upper:
        raise CertificateError("target interval malformed at margin subtraction")
    result = (
        phi_lower - target_upper * log_upper,
        phi_upper - target_lower * log_lower,
    )
    if result[0] > result[1]:
        raise CertificateError("outward margin interval reversed")
    return result


def _check_collapsed_objectives(
    *,
    index: int,
    endpoint_phi4: F,
    endpoint_phi8: F,
    expected_phi4: F,
    expected_phi8: F,
) -> None:
    """Reject epoch errors even when their rho-weighted sum cancels."""
    if endpoint_phi4 != expected_phi4:
        raise CertificateError(f"chamber {index}: epoch-4 collapsed objective mismatch")
    if endpoint_phi8 != expected_phi8:
        raise CertificateError(f"chamber {index}: epoch-8 collapsed objective mismatch")
    if endpoint_phi4 + RHO * endpoint_phi8 != expected_phi4 + RHO * expected_phi8:
        raise CertificateError(f"chamber {index}: weighted collapsed objective mismatch")


def _audit_record(model: Any, record: Mapping[str, Any], target: tuple[F, F]) -> dict[str, Any]:
    index = record["index"]
    left, right = record["left"], record["right"]
    midpoint = (left + right) / 2
    evaluate = _make_scaled_evaluator(
        model, midpoint,
        record["denominator4"], record["columns4"],
        record["denominator8"], record["columns8"],
    )
    generic_rows = generic_endpoint_checks = collapsed_rows = 0
    minimum_owner_margin: F | None = None
    for _, _, state in model._generic_cells(left, right):
        _, owned, demands = evaluate(state)
        for owner, owner_value, demand in zip(model.OWNERS, owned, demands):
            if not _owner_row_is_structural(model, owner, state):
                _check_structural_zero_owner(
                    index=index,
                    context="generic",
                    owner_value=owner_value,
                    demand=demand,
                )
                continue
            margins = (left * owner_value - demand, right * owner_value - demand)
            if min(margins) <= 0:
                raise CertificateError(f"chamber {index}: generic owner row is not strict")
            minimum_owner_margin = (
                min(margins) if minimum_owner_margin is None
                else min(minimum_owner_margin, *margins)
            )
            generic_rows += 1
            generic_endpoint_checks += 2

    poly4 = model._epoch_polynomial(left, right, 4, evaluate)
    poly8 = model._epoch_polynomial(left, right, 8, evaluate)
    weighted = tuple(poly4[i] + RHO * poly8[i] for i in range(3))
    margin_lower, margin_upper = _margin_piece_interval(
        model, weighted, left, right, target[0], target[1]
    )

    for endpoint in (left, right):
        demand_total = {4: F(), 8: F()}
        price_total = {4: F(), 8: F()}
        for cell_left, cell_right, state in model._exact_cells(endpoint):
            physical, owned, demands = evaluate(state)
            length = cell_right - cell_left
            for owner, owner_value, demand in zip(model.OWNERS, owned, demands):
                if not _owner_row_is_structural(model, owner, state):
                    _check_structural_zero_owner(
                        index=index,
                        context="collapsed",
                        owner_value=owner_value,
                        demand=demand,
                    )
                    continue
                owner_margin = endpoint * owner_value - demand
                if owner_margin <= 0:
                    raise CertificateError(f"chamber {index}: collapsed owner row is not strict")
                minimum_owner_margin = (
                    owner_margin if minimum_owner_margin is None
                    else min(minimum_owner_margin, owner_margin)
                )
                demand_total[owner[0]] += length * demand / endpoint
                collapsed_rows += 1
            for epoch in (4, 8):
                price_total[epoch] += length * physical[epoch]
        endpoint_phi4 = endpoint * (2 * demand_total[4] - price_total[4])
        endpoint_phi8 = endpoint * (2 * demand_total[8] - price_total[8])
        _check_collapsed_objectives(
            index=index,
            endpoint_phi4=endpoint_phi4,
            endpoint_phi8=endpoint_phi8,
            expected_phi4=model._poly_eval(poly4, endpoint),
            expected_phi8=model._poly_eval(poly8, endpoint),
        )
        if endpoint_phi4 + RHO * endpoint_phi8 != model._poly_eval(weighted, endpoint):
            raise CertificateError(f"chamber {index}: weighted polynomial reconstruction mismatch")
    if minimum_owner_margin is None:
        raise CertificateError(f"chamber {index}: owner audit empty")
    ranks = (len(record["columns4"]), len(record["columns8"]))
    return {
        "index": index,
        "margin_lower": margin_lower,
        "margin_upper": margin_upper,
        "generic_owner_rows": generic_rows,
        "generic_owner_endpoint_checks": generic_endpoint_checks,
        "collapsed_endpoint_owner_rows": collapsed_rows,
        "minimum_owner_margin": minimum_owner_margin,
        "ranks": ranks,
    }


def _aggregate(
    audits: Sequence[Mapping[str, Any]],
    indices: Sequence[int],
    model: Any,
) -> dict[str, Any]:
    chosen = [audit for audit in audits if audit["index"] in indices]
    raw_lower = sum((audit["margin_lower"] for audit in chosen), F())
    raw_upper = sum((audit["margin_upper"] for audit in chosen), F())
    log2_lower, log2_upper = model._log_interval(F(2))
    normalized_lower = raw_lower / log2_upper if raw_lower >= 0 else raw_lower / log2_lower
    normalized_upper = raw_upper / log2_lower if raw_upper >= 0 else raw_upper / log2_upper
    if raw_lower > raw_upper or normalized_lower > normalized_upper:
        raise CertificateError("aggregate outward interval reversed")
    ranks = [rank for audit in chosen for rank in audit["ranks"]]
    return {
        "chambers": len(chosen),
        "factors": len(ranks),
        "raw_margin_lower": raw_lower,
        "raw_margin_upper": raw_upper,
        "normalized_margin_lower": normalized_lower,
        "normalized_margin_upper": normalized_upper,
        "generic_owner_rows": sum(audit["generic_owner_rows"] for audit in chosen),
        "generic_owner_endpoint_checks": sum(
            audit["generic_owner_endpoint_checks"] for audit in chosen
        ),
        "collapsed_endpoint_owner_rows": sum(
            audit["collapsed_endpoint_owner_rows"] for audit in chosen
        ),
        "minimum_owner_margin": min(audit["minimum_owner_margin"] for audit in chosen),
        "rank_min": min(ranks),
        "rank_max": max(ranks),
        "rank_sum": sum(ranks),
        "denominators": (DENOMINATOR,),
        "all_owner_rows_strictly_positive": True,
        "all_factor_columns_independent": True,
    }


def _replay_factor_bank(factor_bank: Mapping[str, Any], *, verify_provenance: bool = True) -> dict[str, Any]:
    if verify_provenance:
        _verify_provenance()
    model = c126._load_model(c126.C123_POINTS, "c129_c123_primal")
    if model.LOG_TERMS != LOG_TERMS:
        raise CertificateError("exact model log terms changed")
    checked_records = _validate_factor_bank_structure(factor_bank, model)
    target = _target_interval(model)
    audits = [_audit_record(model, record, target) for record in checked_records]
    top6 = _aggregate(audits, TOP6_INDICES, model)
    sparse7 = _aggregate(audits, MINIMAL_SPARSE7_INDICES, model)
    robust10 = _aggregate(audits, ROBUST10_INDICES, model)
    if not top6["raw_margin_upper"] < 0:
        raise CertificateError("top-six transition side is not strictly negative")
    if not sparse7["raw_margin_lower"] > F(1, 15_000):
        raise CertificateError("minimal sparse-seven raw clean fence failed")
    if not sparse7["normalized_margin_lower"] > F(99, 1_000_000):
        raise CertificateError("minimal sparse-seven normalized clean fence failed")
    if not robust10["raw_margin_lower"] > F(143, 400_000):
        raise CertificateError("robust-ten raw clean fence failed")
    if not robust10["normalized_margin_lower"] > F(103, 200_000):
        raise CertificateError("robust-ten normalized clean fence failed")
    expected_census = (
        robust10["chambers"], robust10["factors"], robust10["rank_min"],
        robust10["rank_max"], robust10["rank_sum"],
        robust10["generic_owner_rows"], robust10["generic_owner_endpoint_checks"],
        robust10["collapsed_endpoint_owner_rows"],
        sparse7["chambers"], sparse7["factors"], sparse7["rank_sum"],
        sparse7["generic_owner_rows"], sparse7["generic_owner_endpoint_checks"],
        sparse7["collapsed_endpoint_owner_rows"],
    )
    frozen_census = (
        32, 64, 9, 24, 1004, 12_140, 24_280, 23_745,
        29, 58, 910, 10_987, 21_974, 21_500,
    )
    if expected_census != frozen_census:
        raise CertificateError(f"exact replay census changed: {expected_census!r}")
    top6["surplus_indices"] = TOP6_SURPLUS_INDICES
    sparse7["surplus_indices"] = MINIMAL_SPARSE7_SURPLUS_INDICES
    robust10["surplus_indices"] = ROBUST10_SURPLUS_INDICES
    return {
        "target_lower": target[0],
        "target_upper": target[1],
        "top6": top6,
        "minimal_sparse7": sparse7,
        "robust10": robust10,
        "remaining_chambers": 135 - len(ROBUST10_INDICES),
    }


_REPLAY_CACHE: dict[str, dict[str, Any]] = {}


def verify_certificate(value: Mapping[str, Any]) -> dict[str, Any]:
    _validate_static(value)
    digest = value["integrity"]["payload_sha256"]
    cached = _REPLAY_CACHE.get(digest)
    if cached is not None:
        return copy.deepcopy(cached)
    summary = _replay_factor_bank(value["factor_bank"])
    _REPLAY_CACHE[digest] = copy.deepcopy(summary)
    return summary


def _load(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CertificateError(f"certificate: invalid JSON: {exc}") from exc
    if type(value) is not dict or raw != rendered_bytes(value):
        raise CertificateError("certificate is not in canonical rendering")
    return value


def _certificate_from_factor_bank(factor_bank: Mapping[str, Any]) -> dict[str, Any]:
    if _object_hash(factor_bank) != FACTOR_BANK_SHA256:
        raise CertificateError("generated factor bank hash changed")
    value: dict[str, Any] = {
        "schema": SCHEMA,
        "status": STATUS,
        "sources": dict(EXPECTED_SOURCES),
        "candidate": dict(EXPECTED_CANDIDATE),
        "selection": copy.deepcopy(EXPECTED_SELECTION),
        "results": dict(EXPECTED_RESULTS),
        "factor_bank": copy.deepcopy(factor_bank),
        "scope": dict(EXPECTED_SCOPE),
        "integrity": {
            "algorithm": "sha256",
            "payload_sha256": "",
            "factor_bank_sha256": FACTOR_BANK_SHA256,
            "exact_replay_arithmetic": (
                "fractions.Fraction; integer rational-Gram with exact positive midpoint scaling; "
                "30-term atanh log enclosures; modular exact-rank witnesses"
            ),
            "rank_witness_primes": list(RANK_PRIMES),
        },
    }
    value["integrity"]["payload_sha256"] = payload_hash(value)
    return value


def _factor_bank_from_discovery(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    try:
        source = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CertificateError("discovery source is invalid JSON") from exc
    if type(source) is not dict or raw != rendered_bytes(source):
        raise CertificateError("discovery source is not canonical compact JSON")
    clone = dict(source)
    internal = clone.pop("payload_sha256_without_hash", None)
    if internal != _object_hash(clone):
        raise CertificateError("discovery source internal hash mismatch")
    if source.get("schema") != "erdos1191.c129.c123_integrated_sparse_subbank.temporary.v1":
        raise CertificateError("discovery source schema changed")
    selection = source.get("selection")
    if type(selection) is not dict or tuple(selection.get("all_indices", ())) != ROBUST10_INDICES:
        raise CertificateError("discovery source selection changed")
    raw_records = source.get("records")
    if type(raw_records) is not list:
        raise CertificateError("discovery records missing")
    records = []
    for raw_record in raw_records:
        records.append({
            "index": raw_record["index"],
            "left": raw_record["left"],
            "right": raw_record["right"],
            "n4": {
                key: copy.deepcopy(raw_record["n4"][key])
                for key in ("denominator", "rank", "columns")
            },
            "n8": {
                key: copy.deepcopy(raw_record["n8"][key])
                for key in ("denominator", "rank", "columns")
            },
        })
    return {"records": records}


def self_check(value: Mapping[str, Any]) -> dict[str, int]:
    verify_certificate(value)
    mutations: list[tuple[str, dict[str, Any]]] = []

    def add(label: str, mutate: Callable[[dict[str, Any]], None]) -> None:
        changed = copy.deepcopy(value)
        mutate(changed)
        changed["integrity"]["payload_sha256"] = payload_hash(changed)
        mutations.append((label, changed))

    add("schema", lambda x: x.__setitem__("schema", SCHEMA + ".mutated"))
    add("status", lambda x: x.__setitem__("status", "UNSOUND"))
    add("C126-hash", lambda x: x["sources"].__setitem__("C126_common_phase_verifier_sha256", "0" * 64))
    add("C128-hash", lambda x: x["sources"].__setitem__("C128_pointwise_no_go_verifier_sha256", "0" * 64))
    add("candidate-C", lambda x: x["candidate"].__setitem__("C_ordered_suffix", "1/9"))
    add("top6-selection", lambda x: x["selection"]["top6_surplus_indices"].pop())
    add("raw-fence", lambda x: x["results"].__setitem__("robust10_raw_margin_greater_than", "1/100"))
    add("false-complete", lambda x: x["scope"].__setitem__("complete_C123_phase_primal_witness_constructed", True))
    add("false-remaining", lambda x: x["scope"].__setitem__("remaining_103_chambers_exactified", True))
    add("false-global-phase", lambda x: x["scope"].__setitem__("global_phase_rule_admissible_proved", True))
    add("false-arbitrary-rank", lambda x: x["scope"].__setitem__("arbitrary_rank_proved", True))
    add("false-C058", lambda x: x["scope"].__setitem__("C058_resolved", True))
    def mutate_factor_hash(x: dict[str, Any]) -> None:
        x["factor_bank"]["records"][0]["n4"]["columns"][0][0] += 1
        x["integrity"]["factor_bank_sha256"] = _object_hash(x["factor_bank"])
    add("factor-rehashed", mutate_factor_hash)

    rejected = 0
    for label, changed in mutations:
        try:
            verify_certificate(changed)
        except CertificateError:
            rejected += 1
        else:
            raise CertificateError(f"self-check mutation was accepted: {label}")

    direct_mutations: list[tuple[str, dict[str, Any]]] = []
    def add_direct(label: str, mutate: Callable[[dict[str, Any]], None]) -> None:
        bank = copy.deepcopy(value["factor_bank"])
        mutate(bank)
        direct_mutations.append((label, bank))

    add_direct(
        "arithmetic-factor-scale",
        lambda x: x["records"][0]["n4"].__setitem__(
            "columns",
            [[2 * entry for entry in column] for column in x["records"][0]["n4"]["columns"]],
        ),
    )
    add_direct("zero-column", lambda x: x["records"][0]["n4"]["columns"].__setitem__(0, [0] * 19))
    add_direct("drop-chamber", lambda x: x["records"].pop())
    add_direct("endpoint", lambda x: x["records"][0].__setitem__("right", "83/1"))
    add_direct("rank", lambda x: x["records"][0]["n4"].__setitem__("rank", 12))
    for label, bank in direct_mutations:
        try:
            _replay_factor_bank(bank, verify_provenance=False)
        except CertificateError:
            rejected += 1
        else:
            raise CertificateError(f"direct replay mutation was accepted: {label}")

    # This controlled mismatch preserves the rho-weighted sum.  It must still
    # fail the epoch-specific check before the combined identity is considered.
    expected4 = F(1)
    expected8 = F(43, 9)
    endpoint4 = F(2)
    endpoint8 = F(3)
    if endpoint4 + RHO * endpoint8 != expected4 + RHO * expected8:
        raise CertificateError("controlled cancellation mutation is malformed")
    try:
        _check_collapsed_objectives(
            index=0,
            endpoint_phi4=endpoint4,
            endpoint_phi8=endpoint8,
            expected_phi4=expected4,
            expected_phi8=expected8,
        )
    except CertificateError:
        rejected += 1
    else:
        raise CertificateError("epoch-specific cancellation mutation was accepted")

    physical = {4: F(1), 8: F(4)}
    owners = ((4, 1), (8, 1))
    owned = (F(2), F(3))
    if sum(owned, F()) != physical[4] + physical[8]:
        raise CertificateError("controlled owner cancellation mutation is malformed")
    try:
        _check_epoch_owner_recovery(
            physical=physical,
            owned=owned,
            owners=owners,
        )
    except CertificateError:
        rejected += 1
    else:
        raise CertificateError("epoch-specific owner recovery mutation was accepted")

    try:
        _check_structural_zero_owner(
            index=0,
            context="generic",
            owner_value=-F(1),
            demand=-F(1),
        )
    except CertificateError:
        rejected += 1
    else:
        raise CertificateError("nonzero structural-zero owner mutation was accepted")

    attempted = len(mutations) + len(direct_mutations) + 3
    if attempted != 21:
        raise CertificateError("mutation census changed")
    return {"mutations_attempted": attempted, "mutations_rejected": rejected}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--generate-from", type=Path)
    args = parser.parse_args(argv)
    if args.generate_from is not None:
        factor_bank = _factor_bank_from_discovery(args.generate_from)
        value = _certificate_from_factor_bank(factor_bank)
        DEFAULT_CERTIFICATE.write_bytes(rendered_bytes(value))
        print(
            "GENERATED",
            DEFAULT_CERTIFICATE.name,
            f"factor_bank_sha256={FACTOR_BANK_SHA256}",
            f"payload_sha256={value['integrity']['payload_sha256']}",
        )
        return 0
    value = _load(args.verify)
    summary = verify_certificate(value)
    mutations = self_check(value) if args.self_check else {"mutations_rejected": 0}
    sparse = summary["minimal_sparse7"]
    robust = summary["robust10"]
    print(
        "VERIFY_OK",
        "row=C123",
        "common_phase=[82,164]",
        "rho=9/16",
        f"factor_chambers={robust['chambers']}",
        f"factors={robust['factors']}",
        f"generic_owner_rows={robust['generic_owner_rows']}",
        f"generic_owner_endpoint_checks={robust['generic_owner_endpoint_checks']}",
        f"collapsed_endpoint_owner_rows={robust['collapsed_endpoint_owner_rows']}",
        "top6_raw_margin<0",
        "sparse7_raw_margin>1/15000",
        "sparse7_normalized_margin>99/1000000",
        "robust10_raw_margin>143/400000",
        "robust10_normalized_margin>103/200000",
        f"sparse7_factors={sparse['factors']}",
        f"mutations_rejected={mutations['mutations_rejected']}",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
