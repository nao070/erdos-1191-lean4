#!/usr/bin/env python3
"""Exact complete fixed-C120 common-phase rational primal certificate.

C131 replays all 147 exact C120 chambers on ``[82,164]`` for the frozen
C125 coefficient candidate.  Chambers 0--114 are the unchanged factors from
chambers 46--160 of the hash-pinned reverse-profile full-phase certificate;
only chambers 115--146 are stored here as reduced, midpoint-scaled integer
Gram factors.  Every accepted factor is audited without a numerical solver.

This is a fixed finite witness in the independent epoch-block cone.  It does
not prove the C103 phase rule, the Abel boundary/terminal ledger, the local or
global master inequality, arbitrary rank, C058, Q1/Q2, or prize readiness.
"""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Callable, Mapping, Sequence


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate as prefix
import ROUTE_C_C126_COMMON_COMPLETED_SHELL_PHASE_certificate as c126
import ROUTE_C_C129_COMMON_PHASE_INTEGRATED_PRIMAL_SUBBANK_certificate as c129


DEFAULT_CERTIFICATE = HERE / "ROUTE_C_C131_COMPLETE_C120_PHASE_PRIMAL_certificate.json"
PREFIX_VERIFIER = HERE / "ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate.py"
PREFIX_CERTIFICATE = HERE / "ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate.json"
C126_VERIFIER = HERE / "ROUTE_C_C126_COMMON_COMPLETED_SHELL_PHASE_certificate.py"
C129_VERIFIER = HERE / "ROUTE_C_C129_COMMON_PHASE_INTEGRATED_PRIMAL_SUBBANK_certificate.py"

SCHEMA = "erdos1191.c131.complete_c120_phase_primal.v1"
STATUS = "EXACT_FINITE_COMPLETE_FIXED_C120_COMMON_PHASE_PRIMAL_C058_OPEN"

PREFIX_VERIFIER_SHA256 = "6e8d7e3f975e952442672cb1d18e4512d616f343bb4f6379ba0c8701cd996fe9"
PREFIX_CERTIFICATE_SHA256 = "6d0382b1267aac07e1ba5533a6a8d292dc29ba937911cae2bef9628052c21e74"
PREFIX_PAYLOAD_SHA256 = "388daa5b719a6f817f3d2de2f5227340b2ec355ca53e93ba2753edc3d270b10d"
C126_VERIFIER_SHA256 = "830c6afa79d49d386e5bc57bdb5578b8074e783486cbaf991164ae25e91a5981"
C129_VERIFIER_SHA256 = "b211bae87c7a29bd9a4ec32fbe53f104b6366f922c743f6273aa61e7d800ddb6"
TAIL_DISCOVERY_SHA256 = "c39708a826344077fad6e4910982a45e0e0b1319cbf5ced901f085407baed909"
TAIL_FACTOR_BANK_SHA256 = "bb8629e4248bc6467fe6617f319e74f42457350dd797e821e320a7dc8b0477e8"

PHASE_LOWER = F(82)
PHASE_UPPER = F(164)
RHO = F(9, 16)
EPSILON = F(1, 1000)
A_COEFFICIENT = F(1, 1000)
B_COEFFICIENT = F(1, 2)
C_COEFFICIENT = F(1, 10)
E2 = F(0)
ABS_DELTA_V = F(443_620_417, 1_928_247_678)
DELTA_VRT_C120 = -F(13_171, 58_179)
LOG_TERMS = 30
TAIL_DENOMINATOR = 100_000_000
RANK_PRIMES = (1_000_000_007, 1_000_000_009)
PREFIX_OLD_INDICES = tuple(range(46, 161))
PREFIX_NEW_INDICES = tuple(range(115))
TAIL_INDICES = tuple(range(115, 147))
ALL_INDICES = tuple(range(147))

EXPECTED_SOURCES = {
    "prefix_exact_replay_verifier": PREFIX_VERIFIER.name,
    "prefix_exact_replay_verifier_sha256": PREFIX_VERIFIER_SHA256,
    "prefix_certificate": PREFIX_CERTIFICATE.name,
    "prefix_certificate_sha256": PREFIX_CERTIFICATE_SHA256,
    "prefix_certificate_payload_sha256": PREFIX_PAYLOAD_SHA256,
    "C126_common_phase_verifier": C126_VERIFIER.name,
    "C126_common_phase_verifier_sha256": C126_VERIFIER_SHA256,
    "C129_exact_replay_helpers": C129_VERIFIER.name,
    "C129_exact_replay_helpers_sha256": C129_VERIFIER_SHA256,
    "temporary_tail_discovery_sha256": TAIL_DISCOVERY_SHA256,
    "temporary_tail_discovery_role": (
        "tail factor discovery only; solver statuses, matrices, eigenvalue data, "
        "and numerical margins are excluded from the accepted certificate"
    ),
}
EXPECTED_CANDIDATE = {
    "epsilon": "1/1000",
    "A": "1/1000",
    "B": "1/2",
    "C_ordered_suffix": "1/10",
    "e2": "0/1",
    "eta": "log(82/215)",
    "DeltaV": "-443620417/1928247678",
    "DeltaVrt_C120": "-13171/58179",
    "target_formula": "(epsilon-A*eta-B*DeltaV-C_ordered_suffix*DeltaVrt_C120)/3-e2",
    "log_enclosure_terms": 30,
}
EXPECTED_SELECTION = {
    "common_phase": ["82/1", "164/1"],
    "rho": "9/16",
    "C120_points": list(c126.C120_POINTS),
    "C120_phase_chambers": 147,
    "prefix_old_indices": list(PREFIX_OLD_INDICES),
    "prefix_new_indices": list(PREFIX_NEW_INDICES),
    "prefix_mapping": "old index 46..160 maps in order to new index 0..114",
    "stored_tail_indices": list(TAIL_INDICES),
    "zero_extension_used": False,
}
EXPECTED_RESULTS = {
    "complete_chambers": 147,
    "complete_factors": 294,
    "prefix_chambers": 115,
    "prefix_factors": 230,
    "tail_chambers": 32,
    "tail_factors": 64,
    "rank_min": 4,
    "rank_max": 31,
    "rank_sum": 3_205,
    "prefix_rank_sum": 1_605,
    "tail_rank_sum": 1_600,
    "generic_owner_rows": 53_312,
    "generic_owner_endpoint_checks": 106_624,
    "structural_zero_generic_rows": 37_240,
    "collapsed_endpoint_owner_rows": 104_080,
    "structural_zero_collapsed_endpoint_rows": 73_440,
    "interior_owner_rows": 53_312,
    "structural_zero_interior_rows": 37_240,
    "owner_recovery_unique_state_evaluations": 11_319,
    "per_epoch_owner_recovery_checks": 22_638,
    "owner_recovery_context_references": 44_828,
    "per_epoch_owner_recovery_context_references": 89_656,
    "endpoint_epoch_objective_checks": 588,
    "endpoint_weighted_objective_checks": 294,
    "interior_epoch_objective_checks": 294,
    "interior_weighted_objective_checks": 147,
    "strictly_negative_pieces": 0,
    "strictly_positive_pieces": 147,
    "minimum_active_owner_slack": "305733/87500000000000",
    "raw_margin_greater_than": "21/1000",
    "normalized_margin_greater_than": "3/100",
    "normalized_margin_less_than": "31/1000",
    "raw_margin_interval_width_less_than": "1/100000000000000000000000000",
    "all_factor_columns_modularly_independent": True,
    "all_embedded_factor_columns_zero_sum": True,
    "all_matrices_integer_Gram_PSD": True,
    "all_epoch_owner_recoveries_exact": True,
    "all_structural_zero_rows_have_zero_owned_share_and_nonpositive_demand": True,
    "all_nonstructural_owner_rows_strictly_positive": True,
    "all_endpoint_and_interior_epoch_objectives_exact": True,
}
EXPECTED_SCOPE = {
    "fixed_C120_16_mark_row_only": True,
    "fixed_C125_rational_candidate_only": True,
    "common_completed_shell_phase_82_to_164_only": True,
    "rho_9_over_16_only": True,
    "independent_epoch_block_cone_only": True,
    "complete_fixed_C120_common_phase_primal_constructed": True,
    "all_147_C120_phase_chambers_exactified": True,
    "zero_extension_used": False,
    "C103_phase_rule_admissible_proved": False,
    "C103_Abel_boundary_terminal_ledger_constructed": False,
    "all_rows_complete_phase_primal_constructed": False,
    "local_master_inequality_proved": False,
    "global_phase_rule_admissible_proved": False,
    "phase_representative_independence_proved": False,
    "arbitrary_rank_proved": False,
    "global_owner_ledger_constructed": False,
    "global_owner_stitching_proved": False,
    "C058_resolved": False,
    "Q1_Q2_resolved": False,
    "publication_novelty_or_prize_claimed": False,
}

TOP_KEYS = {
    "schema", "status", "sources", "candidate", "selection", "results",
    "tail_factor_bank", "scope", "integrity",
}
INTEGRITY_KEYS = {
    "algorithm", "payload_sha256", "tail_factor_bank_sha256",
    "exact_replay_arithmetic", "rank_witness_primes",
}
FACTOR_BANK_KEYS = {"records"}
RECORD_KEYS = {"index", "left", "right", "n4", "n8"}


CertificateError = c129.CertificateError


def _object_hash(value: object) -> str:
    return c129._object_hash(value)


def rendered_bytes(value: Mapping[str, Any]) -> bytes:
    return c129.rendered_bytes(value)


def payload_hash(value: Mapping[str, Any]) -> str:
    clone = copy.deepcopy(value)
    clone["integrity"]["payload_sha256"] = ""
    return _object_hash(clone)


def _fraction_text(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def _reject_floats(value: object, label: str = "payload") -> None:
    if type(value) is float:
        raise CertificateError(f"{label}: floating value forbidden")
    if type(value) is dict:
        for key, child in value.items():
            _reject_floats(child, f"{label}.{key}")
    elif type(value) is list:
        for index, child in enumerate(value):
            _reject_floats(child, f"{label}[{index}]")


def _require_exact_types(actual: object, expected: object, label: str) -> None:
    if type(actual) is not type(expected):
        raise CertificateError(f"{label}: exact value type changed")
    if type(expected) is dict:
        if set(actual) != set(expected):
            raise CertificateError(f"{label}: exact keys changed")
        for key in expected:
            _require_exact_types(actual[key], expected[key], f"{label}.{key}")
    elif type(expected) is list:
        if len(actual) != len(expected):
            raise CertificateError(f"{label}: exact list length changed")
        for index, (left, right) in enumerate(zip(actual, expected)):
            _require_exact_types(left, right, f"{label}[{index}]")


def _load_pinned_prefix() -> dict[str, Any]:
    if hashlib.sha256(PREFIX_VERIFIER.read_bytes()).hexdigest() != PREFIX_VERIFIER_SHA256:
        raise CertificateError("prefix verifier sha256 mismatch")
    raw = PREFIX_CERTIFICATE.read_bytes()
    if hashlib.sha256(raw).hexdigest() != PREFIX_CERTIFICATE_SHA256:
        raise CertificateError("prefix certificate sha256 mismatch")
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CertificateError("prefix certificate invalid JSON") from exc
    if type(value) is not dict or raw != prefix.rendered_bytes(value):
        raise CertificateError("prefix certificate noncanonical rendering")
    if value.get("integrity", {}).get("payload_sha256") != PREFIX_PAYLOAD_SHA256:
        raise CertificateError("prefix certificate payload hash changed")
    prefix._validate_static(value)
    return value


def _verify_provenance() -> dict[str, Any]:
    for path, digest, label in (
        (C126_VERIFIER, C126_VERIFIER_SHA256, "C126 verifier"),
        (C129_VERIFIER, C129_VERIFIER_SHA256, "C129 verifier"),
    ):
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise CertificateError(f"{label}: sha256 mismatch")
    if (
        c126.C120_POINTS != prefix.POINTS
        or c126.PHASE_LOWER != PHASE_LOWER
        or c126.PHASE_UPPER != PHASE_UPPER
        or c126.RHO != RHO
        or c129.RANK_PRIMES != RANK_PRIMES
    ):
        raise CertificateError("pinned model constants changed")
    return _load_pinned_prefix()


def _validate_static(value: Mapping[str, Any]) -> None:
    _reject_floats(value)
    c129._exact_dict(value, TOP_KEYS, "top")
    if value["schema"] != SCHEMA or value["status"] != STATUS:
        raise CertificateError("schema or status changed")
    for name, expected in (
        ("sources", EXPECTED_SOURCES),
        ("candidate", EXPECTED_CANDIDATE),
        ("selection", EXPECTED_SELECTION),
        ("results", EXPECTED_RESULTS),
        ("scope", EXPECTED_SCOPE),
    ):
        if value[name] != expected:
            raise CertificateError(f"{name} statement changed")
        _require_exact_types(value[name], expected, name)
    bank = c129._exact_dict(value["tail_factor_bank"], FACTOR_BANK_KEYS, "tail_factor_bank")
    integrity = c129._exact_dict(value["integrity"], INTEGRITY_KEYS, "integrity")
    if integrity["algorithm"] != "sha256":
        raise CertificateError("integrity algorithm changed")
    if (
        _object_hash(bank) != TAIL_FACTOR_BANK_SHA256
        or integrity["tail_factor_bank_sha256"] != TAIL_FACTOR_BANK_SHA256
    ):
        raise CertificateError("tail factor bank hash changed")
    if integrity["payload_sha256"] != payload_hash(value):
        raise CertificateError("payload integrity mismatch")
    arithmetic = (
        "fractions.Fraction; hash-pinned unchanged prefix rational-Gram; integer tail "
        "rational-Gram with exact positive midpoint scaling; 30-term atanh log "
        "enclosures; modular exact-rank witnesses; separate epoch-4, epoch-8, and "
        "rho-weighted endpoint/interior objective reconstruction"
    )
    if integrity["exact_replay_arithmetic"] != arithmetic:
        raise CertificateError("arithmetic statement changed")
    if integrity["rank_witness_primes"] != list(RANK_PRIMES):
        raise CertificateError("rank witness primes changed")


def _tail_bank_from_discovery(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != TAIL_DISCOVERY_SHA256:
        raise CertificateError("tail discovery sha256 mismatch")
    try:
        source = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CertificateError("tail discovery invalid JSON") from exc
    if type(source) is not dict or set(source) != FACTOR_BANK_KEYS:
        raise CertificateError("tail discovery schema changed")
    records = source["records"]
    if type(records) is not list or len(records) != 32:
        raise CertificateError("tail discovery chamber count changed")
    bank = copy.deepcopy(source)
    for record in bank["records"]:
        record["left"] = _fraction_text(F(record["left"]))
        record["right"] = _fraction_text(F(record["right"]))
    if _object_hash(bank) != TAIL_FACTOR_BANK_SHA256:
        raise CertificateError("canonical tail factor bank hash changed")
    return bank


def _certificate_from_tail_bank(bank: Mapping[str, Any]) -> dict[str, Any]:
    if _object_hash(bank) != TAIL_FACTOR_BANK_SHA256:
        raise CertificateError("generated tail factor bank hash changed")
    arithmetic = (
        "fractions.Fraction; hash-pinned unchanged prefix rational-Gram; integer tail "
        "rational-Gram with exact positive midpoint scaling; 30-term atanh log "
        "enclosures; modular exact-rank witnesses; separate epoch-4, epoch-8, and "
        "rho-weighted endpoint/interior objective reconstruction"
    )
    value: dict[str, Any] = {
        "schema": SCHEMA,
        "status": STATUS,
        "sources": dict(EXPECTED_SOURCES),
        "candidate": dict(EXPECTED_CANDIDATE),
        "selection": copy.deepcopy(EXPECTED_SELECTION),
        "results": dict(EXPECTED_RESULTS),
        "tail_factor_bank": copy.deepcopy(bank),
        "scope": dict(EXPECTED_SCOPE),
        "integrity": {
            "algorithm": "sha256",
            "payload_sha256": "",
            "tail_factor_bank_sha256": TAIL_FACTOR_BANK_SHA256,
            "exact_replay_arithmetic": arithmetic,
            "rank_witness_primes": list(RANK_PRIMES),
        },
    }
    value["integrity"]["payload_sha256"] = payload_hash(value)
    return value


def _target_interval(model: Any) -> tuple[F, F]:
    log_lower, log_upper = model._log_interval(F(215, 82))
    rational = (
        EPSILON + B_COEFFICIENT * ABS_DELTA_V
        - C_COEFFICIENT * DELTA_VRT_C120
    )
    lower = (rational + A_COEFFICIENT * log_lower) / 3 - E2
    upper = (rational + A_COEFFICIENT * log_upper) / 3 - E2
    if not F() < lower <= upper:
        raise CertificateError("target interval malformed")
    return lower, upper


def _check_modular_rank(
    columns: Sequence[Sequence[int]], rank: int, label: str
) -> None:
    for prime in RANK_PRIMES:
        if c129._modular_column_rank(columns, prime) != rank:
            raise CertificateError(f"{label}: factor columns lost modular rank")


def _prepare_prefix_records(
    model: Any, source: Mapping[str, Any]
) -> list[dict[str, Any]]:
    new_breakpoints = model._breakpoints()
    old_breakpoints = prefix._breakpoints()
    if len(new_breakpoints) != 148 or len(old_breakpoints) != 162:
        raise CertificateError("prefix or C120 chamber partition changed")
    if tuple(new_breakpoints[:116]) != tuple(old_breakpoints[46:]):
        raise CertificateError("prefix endpoint mapping changed")
    raw_records = source["primal_certificate"]["chambers"]
    records: list[dict[str, Any]] = []
    epoch4 = set(model.EPOCH4_INDICES)
    for new_index, old_index in zip(PREFIX_NEW_INDICES, PREFIX_OLD_INDICES):
        denominator, columns, rank4, rank8 = prefix._validate_factor(
            raw_records[old_index], old_index,
            old_breakpoints[old_index], old_breakpoints[old_index + 1],
        )
        columns4 = tuple(
            column for column in columns
            if {i for i, entry in enumerate(column) if entry} <= epoch4
        )
        columns8 = tuple(column for column in columns if column not in columns4)
        if (len(columns4), len(columns8)) != (rank4, rank8):
            raise CertificateError(f"prefix chamber {new_index}: epoch split changed")
        _check_modular_rank(columns4, rank4, f"prefix chamber {new_index}.n4")
        _check_modular_rank(columns8, rank8, f"prefix chamber {new_index}.n8")
        records.append({
            "index": new_index,
            "left": new_breakpoints[new_index],
            "right": new_breakpoints[new_index + 1],
            "denominators": (denominator,),
            "columns4": columns4,
            "columns8": columns8,
            "scale": F(1, denominator * denominator),
            "source": "prefix",
        })
    return records


def _prepare_tail_records(
    model: Any, bank: Mapping[str, Any]
) -> list[dict[str, Any]]:
    c129._exact_dict(bank, FACTOR_BANK_KEYS, "tail_factor_bank")
    raw_records = bank["records"]
    if type(raw_records) is not list or len(raw_records) != 32:
        raise CertificateError("tail factor bank must contain 32 chambers")
    breakpoints = model._breakpoints()
    records: list[dict[str, Any]] = []
    for position, (raw, index) in enumerate(zip(raw_records, TAIL_INDICES)):
        checked = c129._exact_dict(raw, RECORD_KEYS, f"tail.records[{position}]")
        left, right = breakpoints[index], breakpoints[index + 1]
        if (
            checked["index"] != index
            or checked["left"] != _fraction_text(left)
            or checked["right"] != _fraction_text(right)
        ):
            raise CertificateError(f"tail chamber {index}: index or endpoint changed")
        denominator4, reduced4 = c129._validate_epoch(
            checked["n4"], 19, f"tail chamber {index}.n4"
        )
        denominator8, reduced8 = c129._validate_epoch(
            checked["n8"], 31, f"tail chamber {index}.n8"
        )
        if denominator4 != TAIL_DENOMINATOR or denominator8 != TAIL_DENOMINATOR:
            raise CertificateError(f"tail chamber {index}: denominator changed")
        columns4 = tuple(
            c129._embed_column(column, model.EPOCH4_INDICES, len(model.CHANNELS))
            for column in reduced4
        )
        columns8 = tuple(
            c129._embed_column(column, model.EPOCH8_INDICES, len(model.CHANNELS))
            for column in reduced8
        )
        if any(sum(column) for column in columns4 + columns8):
            raise CertificateError(f"tail chamber {index}: embedded zero sum changed")
        midpoint = (left + right) / 2
        records.append({
            "index": index,
            "left": left,
            "right": right,
            "denominators": (denominator4,),
            "columns4": columns4,
            "columns8": columns8,
            "scale": F(1, denominator4 * denominator4) / midpoint,
            "source": "tail",
        })
    return records


def _make_evaluator(
    model: Any,
    scale: F,
    columns4: Sequence[Sequence[int]],
    columns8: Sequence[Sequence[int]],
) -> Callable[[tuple[int, ...]], tuple[dict[int, F], tuple[F, ...], tuple[F, ...]]]:
    if scale <= 0:
        raise CertificateError("Gram scale is not positive")
    columns = tuple(columns4) + tuple(columns8)
    epochs = (4,) * len(columns4) + (8,) * len(columns8)
    cache: dict[
        tuple[int, ...], tuple[dict[int, F], tuple[F, ...], tuple[F, ...]]
    ] = {}

    def evaluate(
        state: tuple[int, ...],
    ) -> tuple[dict[int, F], tuple[F, ...], tuple[F, ...]]:
        cached = cache.get(state)
        if cached is not None:
            return cached
        dots = tuple(
            sum(state[i] * column[i] for i in range(len(state)))
            for column in columns
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
                sum(state[i] * column[i] for i in group) for column in columns
            )
            owned.append(scale * sum(a * b for a, b in zip(group_dots, dots)))
            demands.append(model._owner_c(owner, state))
        c129._check_epoch_owner_recovery(
            physical=physical, owned=owned, owners=model.OWNERS
        )
        result = physical, tuple(owned), tuple(demands)
        cache[state] = result
        return result

    return evaluate


def _check_interior_objectives(
    *, index: int, actual4: F, actual8: F, expected4: F, expected8: F
) -> None:
    if actual4 != expected4:
        raise CertificateError(f"chamber {index}: epoch-4 interior objective mismatch")
    if actual8 != expected8:
        raise CertificateError(f"chamber {index}: epoch-8 interior objective mismatch")
    if actual4 + RHO * actual8 != expected4 + RHO * expected8:
        raise CertificateError(f"chamber {index}: weighted interior objective mismatch")


def _reconstruct_at_width(
    *, model: Any, index: int, width: F, context: str,
    evaluate: Callable[[tuple[int, ...]], tuple[dict[int, F], tuple[F, ...], tuple[F, ...]]],
) -> tuple[F, F, int, int, F | None, int]:
    demand_total = {4: F(), 8: F()}
    price_total = {4: F(), 8: F()}
    owner_rows = structural_zero_rows = context_count = 0
    minimum_owner: F | None = None
    for cell_left, cell_right, state in model._exact_cells(width):
        context_count += 1
        physical, owned, demands = evaluate(state)
        length = cell_right - cell_left
        for owner, owner_value, demand in zip(model.OWNERS, owned, demands):
            if not c129._owner_row_is_structural(model, owner, state):
                c129._check_structural_zero_owner(
                    index=index, context=context,
                    owner_value=owner_value, demand=demand,
                )
                structural_zero_rows += 1
                continue
            margin = width * owner_value - demand
            if margin <= 0:
                raise CertificateError(f"chamber {index}: {context} owner row is not strict")
            minimum_owner = margin if minimum_owner is None else min(minimum_owner, margin)
            demand_total[owner[0]] += length * demand / width
            owner_rows += 1
        for epoch in (4, 8):
            price_total[epoch] += length * physical[epoch]
    phi4 = width * (2 * demand_total[4] - price_total[4])
    phi8 = width * (2 * demand_total[8] - price_total[8])
    return phi4, phi8, owner_rows, structural_zero_rows, minimum_owner, context_count


def _audit_record(
    model: Any, record: Mapping[str, Any], target: tuple[F, F]
) -> dict[str, Any]:
    index = record["index"]
    left, right = record["left"], record["right"]
    midpoint = (left + right) / 2
    base_evaluate = _make_evaluator(
        model, record["scale"], record["columns4"], record["columns8"]
    )
    evaluated_states: set[tuple[int, ...]] = set()

    def evaluate(state: tuple[int, ...]):
        evaluated_states.add(state)
        return base_evaluate(state)

    generic_rows = generic_endpoint_checks = structural_zero_generic_rows = 0
    context_references = 0
    minimum_owner: F | None = None
    generic_cells = model._generic_cells(left, right)
    for _, _, state in generic_cells:
        context_references += 1
        _, owned, demands = evaluate(state)
        for owner, owner_value, demand in zip(model.OWNERS, owned, demands):
            if not c129._owner_row_is_structural(model, owner, state):
                c129._check_structural_zero_owner(
                    index=index, context="generic",
                    owner_value=owner_value, demand=demand,
                )
                structural_zero_generic_rows += 1
                continue
            margins = (left * owner_value - demand, right * owner_value - demand)
            if min(margins) <= 0:
                raise CertificateError(f"chamber {index}: generic owner row is not strict")
            minimum_owner = (
                min(margins) if minimum_owner is None
                else min(minimum_owner, *margins)
            )
            generic_rows += 1
            generic_endpoint_checks += 2

    poly4 = model._epoch_polynomial(left, right, 4, evaluate)
    poly8 = model._epoch_polynomial(left, right, 8, evaluate)
    weighted = tuple(poly4[i] + RHO * poly8[i] for i in range(3))
    margin_lower, margin_upper = c129._margin_piece_interval(
        model, weighted, left, right, target[0], target[1]
    )

    collapsed_rows = structural_zero_collapsed_rows = 0
    for endpoint in (left, right):
        actual4, actual8, rows, zeros, endpoint_minimum, contexts = _reconstruct_at_width(
            model=model, index=index, width=endpoint, context="collapsed",
            evaluate=evaluate,
        )
        collapsed_rows += rows
        structural_zero_collapsed_rows += zeros
        context_references += contexts
        if endpoint_minimum is not None:
            minimum_owner = (
                endpoint_minimum if minimum_owner is None
                else min(minimum_owner, endpoint_minimum)
            )
        expected4 = model._poly_eval(poly4, endpoint)
        expected8 = model._poly_eval(poly8, endpoint)
        c129._check_collapsed_objectives(
            index=index, endpoint_phi4=actual4, endpoint_phi8=actual8,
            expected_phi4=expected4, expected_phi8=expected8,
        )
        if actual4 + RHO * actual8 != model._poly_eval(weighted, endpoint):
            raise CertificateError(f"chamber {index}: weighted endpoint objective mismatch")

    actual4, actual8, interior_rows, interior_zeros, interior_minimum, contexts = (
        _reconstruct_at_width(
            model=model, index=index, width=midpoint, context="interior",
            evaluate=evaluate,
        )
    )
    context_references += contexts
    if interior_minimum is not None:
        minimum_owner = (
            interior_minimum if minimum_owner is None
            else min(minimum_owner, interior_minimum)
        )
    _check_interior_objectives(
        index=index, actual4=actual4, actual8=actual8,
        expected4=model._poly_eval(poly4, midpoint),
        expected8=model._poly_eval(poly8, midpoint),
    )
    if minimum_owner is None:
        raise CertificateError(f"chamber {index}: owner audit empty")
    return {
        "index": index,
        "source": record["source"],
        "margin_lower": margin_lower,
        "margin_upper": margin_upper,
        "generic_owner_rows": generic_rows,
        "generic_owner_endpoint_checks": generic_endpoint_checks,
        "structural_zero_generic_rows": structural_zero_generic_rows,
        "collapsed_endpoint_owner_rows": collapsed_rows,
        "structural_zero_collapsed_endpoint_rows": structural_zero_collapsed_rows,
        "interior_owner_rows": interior_rows,
        "structural_zero_interior_rows": interior_zeros,
        "owner_recovery_unique_state_evaluations": len(evaluated_states),
        "owner_recovery_context_references": context_references,
        "minimum_owner_margin": minimum_owner,
        "ranks": (len(record["columns4"]), len(record["columns8"])),
        "denominators": record["denominators"],
    }


def _aggregate(audits: Sequence[Mapping[str, Any]], model: Any) -> dict[str, Any]:
    raw_lower = sum((audit["margin_lower"] for audit in audits), F())
    raw_upper = sum((audit["margin_upper"] for audit in audits), F())
    log2_lower, log2_upper = model._log_interval(F(2))
    normalized_lower = raw_lower / log2_upper
    normalized_upper = raw_upper / log2_lower
    ranks = [rank for audit in audits for rank in audit["ranks"]]
    result = {
        "chambers": len(audits),
        "factors": len(ranks),
        "raw_margin_lower": raw_lower,
        "raw_margin_upper": raw_upper,
        "normalized_margin_lower": normalized_lower,
        "normalized_margin_upper": normalized_upper,
        "rank_min": min(ranks),
        "rank_max": max(ranks),
        "rank_sum": sum(ranks),
        "denominators": tuple(sorted({d for audit in audits for d in audit["denominators"]})),
        "minimum_owner_margin": min(audit["minimum_owner_margin"] for audit in audits),
    }
    for key in (
        "generic_owner_rows", "generic_owner_endpoint_checks",
        "structural_zero_generic_rows", "collapsed_endpoint_owner_rows",
        "structural_zero_collapsed_endpoint_rows", "interior_owner_rows",
        "structural_zero_interior_rows", "owner_recovery_unique_state_evaluations",
        "owner_recovery_context_references",
    ):
        result[key] = sum(audit[key] for audit in audits)
    result["per_epoch_owner_recovery_checks"] = 2 * result[
        "owner_recovery_unique_state_evaluations"
    ]
    result["per_epoch_owner_recovery_context_references"] = 2 * result[
        "owner_recovery_context_references"
    ]
    count = len(audits)
    result.update({
        "endpoint_epoch_objective_checks": 4 * count,
        "endpoint_weighted_objective_checks": 2 * count,
        "interior_epoch_objective_checks": 2 * count,
        "interior_weighted_objective_checks": count,
        "all_factor_columns_independent": True,
        "all_embedded_columns_zero_sum": True,
        "all_gram_matrices_psd": True,
        "all_epoch_owner_recoveries_exact": True,
        "all_epoch_objectives_reconstructed": True,
    })
    return result


def _replay_tail_bank(
    bank: Mapping[str, Any], *, verify_provenance: bool = True
) -> dict[str, Any]:
    source = _verify_provenance() if verify_provenance else _load_pinned_prefix()
    model = c126._load_model(c126.C120_POINTS, "c131_complete_c120_primal")
    if model.LOG_TERMS != LOG_TERMS:
        raise CertificateError("exact model log terms changed")
    prefix_records = _prepare_prefix_records(model, source)
    tail_records = _prepare_tail_records(model, bank)
    target = _target_interval(model)
    audits = [
        _audit_record(model, record, target)
        for record in prefix_records + tail_records
    ]
    complete = _aggregate(audits, model)
    prefix_summary = _aggregate(audits[:115], model)
    tail_summary = _aggregate(audits[115:], model)
    positive = tuple(audit["index"] for audit in audits if audit["margin_lower"] > 0)
    negative = tuple(audit["index"] for audit in audits if audit["margin_upper"] < 0)
    if len(positive) + len(negative) != 147 or positive != ALL_INDICES:
        raise CertificateError("piece sign census changed")
    complete["positive_piece_indices"] = positive
    complete["negative_piece_indices"] = negative
    if complete["minimum_owner_margin"] != F(305_733, 87_500_000_000_000):
        raise CertificateError("minimum active owner slack changed")
    if not complete["raw_margin_lower"] > F(21, 1000):
        raise CertificateError("complete raw clean fence failed")
    if not complete["normalized_margin_lower"] > F(3, 100):
        raise CertificateError("complete normalized lower fence failed")
    if not complete["normalized_margin_upper"] < F(31, 1000):
        raise CertificateError("complete normalized upper fence failed")
    if not complete["raw_margin_upper"] - complete["raw_margin_lower"] < F(1, 10**26):
        raise CertificateError("raw margin enclosure width fence failed")
    actual_census = (
        complete["chambers"], complete["factors"], complete["rank_min"],
        complete["rank_max"], complete["rank_sum"], prefix_summary["rank_sum"],
        tail_summary["rank_sum"], complete["generic_owner_rows"],
        complete["generic_owner_endpoint_checks"],
        complete["structural_zero_generic_rows"],
        complete["collapsed_endpoint_owner_rows"],
        complete["structural_zero_collapsed_endpoint_rows"],
        complete["interior_owner_rows"], complete["structural_zero_interior_rows"],
        complete["owner_recovery_unique_state_evaluations"],
        complete["per_epoch_owner_recovery_checks"],
        complete["owner_recovery_context_references"],
        complete["per_epoch_owner_recovery_context_references"],
        complete["endpoint_epoch_objective_checks"],
        complete["endpoint_weighted_objective_checks"],
        complete["interior_epoch_objective_checks"],
        complete["interior_weighted_objective_checks"],
    )
    frozen_census = (
        147, 294, 4, 31, 3205, 1605, 1600,
        53312, 106624, 37240, 104080, 73440, 53312, 37240,
        11319, 22638, 44828, 89656, 588, 294, 294, 147,
    )
    if actual_census != frozen_census:
        raise CertificateError(f"exact replay census changed: {actual_census!r}")
    return {
        "target_lower": target[0],
        "target_upper": target[1],
        "complete_C120": complete,
        "prefix_C120": prefix_summary,
        "tail_C120": tail_summary,
        "remaining_C120_chambers": 0,
    }


def _load(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CertificateError("certificate invalid JSON") from exc
    if type(value) is not dict or raw != rendered_bytes(value):
        raise CertificateError("certificate is not in canonical rendering")
    return value


_REPLAY_CACHE: dict[str, dict[str, Any]] = {}


def verify_certificate(value: Mapping[str, Any]) -> dict[str, Any]:
    _validate_static(value)
    # A cached arithmetic replay is valid only while every pinned executable
    # dependency and model constant still has its certified provenance.  Keep
    # this check ahead of the cache lookup so a long-lived verifier cannot
    # accept the payload after a dependency is changed or removed.
    _verify_provenance()
    digest = value["integrity"]["payload_sha256"]
    cached = _REPLAY_CACHE.get(digest)
    if cached is not None:
        return copy.deepcopy(cached)
    summary = _replay_tail_bank(value["tail_factor_bank"], verify_provenance=False)
    _REPLAY_CACHE[digest] = copy.deepcopy(summary)
    return summary


def self_check(value: Mapping[str, Any]) -> dict[str, Any]:
    verify_certificate(value)
    rejected = 0

    payload_changed = copy.deepcopy(value)
    payload_changed["integrity"]["payload_sha256"] = "0" * 64
    try:
        verify_certificate(payload_changed)
    except CertificateError:
        rejected += 1
    else:
        raise CertificateError("payload mutation was accepted")

    factor_changed = copy.deepcopy(value)
    factor_changed["tail_factor_bank"]["records"][0]["n4"]["columns"][0][0] += 1
    factor_changed["integrity"]["tail_factor_bank_sha256"] = _object_hash(
        factor_changed["tail_factor_bank"]
    )
    factor_changed["integrity"]["payload_sha256"] = payload_hash(factor_changed)
    try:
        verify_certificate(factor_changed)
    except CertificateError:
        rejected += 1
    else:
        raise CertificateError("factor mutation was accepted")

    endpoint_changed = copy.deepcopy(value["tail_factor_bank"])
    endpoint_changed["records"][0]["right"] = "139/1"
    try:
        _replay_tail_bank(endpoint_changed, verify_provenance=False)
    except CertificateError:
        rejected += 1
    else:
        raise CertificateError("endpoint mutation was accepted")

    scope_changed = copy.deepcopy(value)
    scope_changed["scope"]["C058_resolved"] = True
    scope_changed["integrity"]["payload_sha256"] = payload_hash(scope_changed)
    try:
        verify_certificate(scope_changed)
    except CertificateError:
        rejected += 1
    else:
        raise CertificateError("scope mutation was accepted")

    return {
        "cases": ("normal", "payload", "factor", "endpoint", "scope"),
        "normal_verified": 1,
        "mutations_attempted": 4,
        "mutations_rejected": rejected,
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--generate-from", type=Path)
    args = parser.parse_args(argv)
    if args.generate_from is not None:
        bank = _tail_bank_from_discovery(args.generate_from)
        value = _certificate_from_tail_bank(bank)
        DEFAULT_CERTIFICATE.write_bytes(rendered_bytes(value))
        print(
            "GENERATED",
            DEFAULT_CERTIFICATE.name,
            f"tail_factor_bank_sha256={TAIL_FACTOR_BANK_SHA256}",
            f"payload_sha256={value['integrity']['payload_sha256']}",
        )
        return 0
    value = _load(args.verify)
    summary = verify_certificate(value)
    checks = self_check(value) if args.self_check else {"mutations_rejected": 0}
    complete = summary["complete_C120"]
    print(
        "VERIFY_OK",
        "row=C120",
        "common_phase=[82,164]",
        "rho=9/16",
        f"chambers={complete['chambers']}",
        f"factors={complete['factors']}",
        "raw_margin>21/1000",
        "3/100<normalized_margin<31/1000",
        f"mutations_rejected={checks['mutations_rejected']}",
        "C058_open",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
