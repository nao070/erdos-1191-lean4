#!/usr/bin/env python3
"""Exact complete fixed-C123 common-phase rational primal certificate.

C130 replays one integer rational-Gram factor for each of epochs 4 and 8 on
every one of the 135 C123 chambers in the common completed-shell phase
``[82,164]``.  The accepted payload contains no numerical solver output.

This is a complete finite witness only for the fixed C123 row, fixed C125
coefficient candidate, and independent epoch-block cone.  It is not a C120 or
C103 witness, a phase-rule theorem, an arbitrary-rank theorem, or a resolution
of C058.
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

import ROUTE_C_C129_COMMON_PHASE_INTEGRATED_PRIMAL_SUBBANK_certificate as c129


DEFAULT_CERTIFICATE = HERE / "ROUTE_C_C130_COMPLETE_C123_PHASE_PRIMAL_certificate.json"
C129_VERIFIER = HERE / "ROUTE_C_C129_COMMON_PHASE_INTEGRATED_PRIMAL_SUBBANK_certificate.py"

SCHEMA = "erdos1191.c130.complete_c123_phase_primal.v1"
STATUS = "EXACT_FINITE_COMPLETE_FIXED_C123_COMMON_PHASE_PRIMAL_C058_OPEN"
C129_VERIFIER_SHA256 = "b211bae87c7a29bd9a4ec32fbe53f104b6366f922c743f6273aa61e7d800ddb6"
DISCOVERY_SOURCE_SHA256 = "a03646cb510c5117d9975260d9a3af08672752428309fa9155fa31436c3f099f"
DISCOVERY_SOURCE_INTERNAL_SHA256 = "034c90c99fa348a1b18e28cc7f6ca10ef643d730f7bc4a4cd6034a39069ab5aa"
FACTOR_BANK_SHA256 = "7d16af8eeba989c068e3d08ffaeff394cbf181a95cefa380834471f024d15173"

PHASE_LOWER = c129.PHASE_LOWER
PHASE_UPPER = c129.PHASE_UPPER
RHO = c129.RHO
LOG_TERMS = c129.LOG_TERMS
DENOMINATOR = c129.DENOMINATOR
RANK_PRIMES = c129.RANK_PRIMES
ALL_INDICES = tuple(range(135))

EXPECTED_SOURCES = {
    "C129_exact_replay_verifier": C129_VERIFIER.name,
    "C129_exact_replay_verifier_sha256": C129_VERIFIER_SHA256,
    "temporary_discovery_source_sha256": DISCOVERY_SOURCE_SHA256,
    "temporary_discovery_source_internal_sha256": DISCOVERY_SOURCE_INTERNAL_SHA256,
    "temporary_discovery_role": (
        "factor discovery only; all solver statuses, matrices, eigenvalue data, "
        "and numerical margins are excluded from the accepted certificate"
    ),
}
EXPECTED_CANDIDATE = copy.deepcopy(c129.EXPECTED_CANDIDATE)
EXPECTED_SELECTION = {
    "common_phase": ["82/1", "164/1"],
    "rho": "9/16",
    "C123_points": list(c129.c126.C123_POINTS),
    "C123_phase_chambers": 135,
    "factor_bank_indices": list(ALL_INDICES),
    "zero_extension_used": False,
}
EXPECTED_RESULTS = {
    "factor_bank_chambers": 135,
    "factor_bank_factors": 270,
    "factor_denominator": 100_000_000,
    "rank_min": 9,
    "rank_max": 25,
    "rank_sum": 4_288,
    "generic_owner_rows": 51_355,
    "generic_owner_endpoint_checks": 102_710,
    "collapsed_endpoint_owner_rows": 100_183,
    "structural_zero_generic_rows": 31_805,
    "structural_zero_collapsed_endpoint_rows": 62_713,
    "per_epoch_owner_recovery_state_evaluations": 10_395,
    "per_epoch_owner_recovery_checks": 20_790,
    "endpoint_epoch_objective_checks": 540,
    "endpoint_weighted_objective_checks": 270,
    "interior_owner_rows": 51_355,
    "structural_zero_interior_rows": 31_805,
    "interior_epoch_objective_checks": 270,
    "interior_weighted_objective_checks": 135,
    "negative_piece_indices": (
        list(range(27)) + list(range(31, 36))
        + [59, 60, 77, 78, 79]
    ),
    "strictly_negative_pieces": 37,
    "strictly_positive_pieces": 98,
    "minimum_active_owner_slack": "1137298595103/235750000000000000",
    "raw_margin_greater_than": "1/400",
    "normalized_margin_greater_than": "91/25000",
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
    "fixed_C123_16_mark_row_only": True,
    "fixed_C125_rational_candidate_only": True,
    "common_completed_shell_phase_82_to_164_only": True,
    "rho_9_over_16_only": True,
    "independent_epoch_block_cone_only": True,
    "complete_fixed_C123_common_phase_primal_constructed": True,
    "all_135_C123_phase_chambers_exactified": True,
    "zero_extension_used": False,
    "C120_phase_primal_constructed": False,
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
    "factor_bank", "scope", "integrity",
}
INTEGRITY_KEYS = {
    "algorithm", "payload_sha256", "factor_bank_sha256",
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


def _verify_provenance() -> None:
    if hashlib.sha256(C129_VERIFIER.read_bytes()).hexdigest() != C129_VERIFIER_SHA256:
        raise CertificateError("C129 verifier sha256 mismatch")
    c129._verify_provenance()
    if (
        c129.PHASE_LOWER != F(82)
        or c129.PHASE_UPPER != F(164)
        or c129.RHO != F(9, 16)
        or c129.LOG_TERMS != 30
        or c129.DENOMINATOR != 100_000_000
        or c129.RANK_PRIMES != (1_000_000_007, 1_000_000_009)
        or len(c129.c126.C123_POINTS) != 16
    ):
        raise CertificateError("C129 replay constants changed")


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
        for index, (actual_child, expected_child) in enumerate(zip(actual, expected)):
            _require_exact_types(actual_child, expected_child, f"{label}[{index}]")


def _validate_static(value: Mapping[str, Any]) -> None:
    _reject_floats(value)
    c129._exact_dict(value, TOP_KEYS, "top")
    if value["schema"] != SCHEMA or value["status"] != STATUS:
        raise CertificateError("schema or status changed")
    if value["sources"] != EXPECTED_SOURCES:
        raise CertificateError("source provenance changed")
    _require_exact_types(value["sources"], EXPECTED_SOURCES, "sources")
    if value["candidate"] != EXPECTED_CANDIDATE:
        raise CertificateError("candidate statement changed")
    _require_exact_types(value["candidate"], EXPECTED_CANDIDATE, "candidate")
    if value["selection"] != EXPECTED_SELECTION:
        raise CertificateError("complete selection statement changed")
    _require_exact_types(value["selection"], EXPECTED_SELECTION, "selection")
    if value["results"] != EXPECTED_RESULTS:
        raise CertificateError("exact result statement changed")
    _require_exact_types(value["results"], EXPECTED_RESULTS, "results")
    if value["scope"] != EXPECTED_SCOPE:
        raise CertificateError("scope changed")
    _require_exact_types(value["scope"], EXPECTED_SCOPE, "scope")
    factor_bank = c129._exact_dict(value["factor_bank"], FACTOR_BANK_KEYS, "factor_bank")
    factor_digest = _object_hash(factor_bank)
    integrity = c129._exact_dict(value["integrity"], INTEGRITY_KEYS, "integrity")
    if integrity["algorithm"] != "sha256":
        raise CertificateError("integrity algorithm changed")
    if (
        factor_digest != FACTOR_BANK_SHA256
        or integrity["factor_bank_sha256"] != FACTOR_BANK_SHA256
    ):
        raise CertificateError("factor bank hash changed")
    if integrity["payload_sha256"] != payload_hash(value):
        raise CertificateError("payload integrity mismatch")
    if integrity["exact_replay_arithmetic"] != (
        "fractions.Fraction; integer rational-Gram with exact positive midpoint scaling; "
        "30-term atanh log enclosures; modular exact-rank witnesses; separate epoch-4, "
        "epoch-8, and rho-weighted endpoint/interior objective reconstruction"
    ):
        raise CertificateError("arithmetic statement changed")
    if integrity["rank_witness_primes"] != list(RANK_PRIMES):
        raise CertificateError("rank witness primes changed")


def _validate_factor_bank_structure(
    factor_bank: Mapping[str, Any], model: Any
) -> list[dict[str, Any]]:
    c129._exact_dict(factor_bank, FACTOR_BANK_KEYS, "factor_bank")
    records = factor_bank["records"]
    if type(records) is not list or len(records) != 135:
        raise CertificateError("factor bank must contain exactly 135 chambers")
    breakpoints = model._breakpoints()
    if len(breakpoints) != 136:
        raise CertificateError("C123 chamber partition changed")
    checked_records: list[dict[str, Any]] = []
    for position, (record, index) in enumerate(zip(records, ALL_INDICES)):
        checked = c129._exact_dict(record, RECORD_KEYS, f"records[{position}]")
        left, right = breakpoints[index], breakpoints[index + 1]
        if (
            checked["index"] != index
            or checked["left"] != _fraction_text(left)
            or checked["right"] != _fraction_text(right)
        ):
            raise CertificateError(f"chamber {index}: index, order, or endpoint changed")
        denominator4, columns4 = c129._validate_epoch(
            checked["n4"], 19, f"chamber {index}.n4"
        )
        denominator8, columns8 = c129._validate_epoch(
            checked["n8"], 31, f"chamber {index}.n8"
        )
        for column in columns4:
            embedded = c129._embed_column(
                column, model.EPOCH4_INDICES, len(model.CHANNELS)
            )
            if sum(embedded) != 0:
                raise CertificateError(f"chamber {index}: epoch-4 embedded sum changed")
        for column in columns8:
            embedded = c129._embed_column(
                column, model.EPOCH8_INDICES, len(model.CHANNELS)
            )
            if sum(embedded) != 0:
                raise CertificateError(f"chamber {index}: epoch-8 embedded sum changed")
        checked_records.append({
            "index": index,
            "left": left,
            "right": right,
            "denominator4": denominator4,
            "columns4": columns4,
            "denominator8": denominator8,
            "columns8": columns8,
        })
    return checked_records


def _check_interior_objectives(
    *,
    index: int,
    actual4: F,
    actual8: F,
    expected4: F,
    expected8: F,
) -> None:
    """Reject separate epoch errors even if their rho-weighted sum cancels."""
    if actual4 != expected4:
        raise CertificateError(f"chamber {index}: epoch-4 interior objective mismatch")
    if actual8 != expected8:
        raise CertificateError(f"chamber {index}: epoch-8 interior objective mismatch")
    if actual4 + RHO * actual8 != expected4 + RHO * expected8:
        raise CertificateError(f"chamber {index}: weighted interior objective mismatch")


def _reconstruct_at_width(
    *,
    model: Any,
    index: int,
    width: F,
    context: str,
    evaluate: Callable[[tuple[int, ...]], tuple[dict[int, F], tuple[F, ...], tuple[F, ...]]],
) -> tuple[F, F, int, int, F | None]:
    demand_total = {4: F(), 8: F()}
    price_total = {4: F(), 8: F()}
    owner_rows = 0
    structural_zero_rows = 0
    minimum_owner: F | None = None
    for cell_left, cell_right, state in model._exact_cells(width):
        physical, owned, demands = evaluate(state)
        length = cell_right - cell_left
        for owner, owner_value, demand in zip(model.OWNERS, owned, demands):
            if not c129._owner_row_is_structural(model, owner, state):
                c129._check_structural_zero_owner(
                    index=index,
                    context=context,
                    owner_value=owner_value,
                    demand=demand,
                )
                structural_zero_rows += 1
                continue
            owner_margin = width * owner_value - demand
            if owner_margin <= 0:
                raise CertificateError(
                    f"chamber {index}: {context} owner row is not strict"
                )
            minimum_owner = (
                owner_margin if minimum_owner is None
                else min(minimum_owner, owner_margin)
            )
            demand_total[owner[0]] += length * demand / width
            owner_rows += 1
        for epoch in (4, 8):
            price_total[epoch] += length * physical[epoch]
    phi4 = width * (2 * demand_total[4] - price_total[4])
    phi8 = width * (2 * demand_total[8] - price_total[8])
    return phi4, phi8, owner_rows, structural_zero_rows, minimum_owner


def _audit_record(model: Any, record: Mapping[str, Any], target: tuple[F, F]) -> dict[str, Any]:
    index = record["index"]
    left, right = record["left"], record["right"]
    midpoint = (left + right) / 2
    base_evaluate = c129._make_scaled_evaluator(
        model,
        midpoint,
        record["denominator4"],
        record["columns4"],
        record["denominator8"],
        record["columns8"],
    )
    evaluated_states: set[tuple[int, ...]] = set()

    def evaluate(state: tuple[int, ...]) -> tuple[dict[int, F], tuple[F, ...], tuple[F, ...]]:
        evaluated_states.add(state)
        return base_evaluate(state)

    generic_rows = generic_endpoint_checks = 0
    structural_zero_generic_rows = 0
    minimum_owner: F | None = None
    for _, _, state in model._generic_cells(left, right):
        _, owned, demands = evaluate(state)
        for owner, owner_value, demand in zip(model.OWNERS, owned, demands):
            if not c129._owner_row_is_structural(model, owner, state):
                c129._check_structural_zero_owner(
                    index=index,
                    context="generic",
                    owner_value=owner_value,
                    demand=demand,
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

    collapsed_rows = 0
    structural_zero_collapsed_rows = 0
    for endpoint in (left, right):
        actual4, actual8, rows, structural_zero_rows, endpoint_minimum = _reconstruct_at_width(
            model=model,
            index=index,
            width=endpoint,
            context="collapsed",
            evaluate=evaluate,
        )
        collapsed_rows += rows
        structural_zero_collapsed_rows += structural_zero_rows
        if endpoint_minimum is not None:
            minimum_owner = (
                endpoint_minimum if minimum_owner is None
                else min(minimum_owner, endpoint_minimum)
            )
        expected4 = model._poly_eval(poly4, endpoint)
        expected8 = model._poly_eval(poly8, endpoint)
        c129._check_collapsed_objectives(
            index=index,
            endpoint_phi4=actual4,
            endpoint_phi8=actual8,
            expected_phi4=expected4,
            expected_phi8=expected8,
        )
        if actual4 + RHO * actual8 != model._poly_eval(weighted, endpoint):
            raise CertificateError(
                f"chamber {index}: weighted endpoint polynomial reconstruction mismatch"
            )

    actual4, actual8, interior_rows, structural_zero_interior_rows, interior_minimum = _reconstruct_at_width(
        model=model,
        index=index,
        width=midpoint,
        context="interior",
        evaluate=evaluate,
    )
    if interior_minimum is not None:
        minimum_owner = (
            interior_minimum if minimum_owner is None
            else min(minimum_owner, interior_minimum)
        )
    expected4 = model._poly_eval(poly4, midpoint)
    expected8 = model._poly_eval(poly8, midpoint)
    _check_interior_objectives(
        index=index,
        actual4=actual4,
        actual8=actual8,
        expected4=expected4,
        expected8=expected8,
    )
    if minimum_owner is None:
        raise CertificateError(f"chamber {index}: owner audit empty")
    return {
        "index": index,
        "margin_lower": margin_lower,
        "margin_upper": margin_upper,
        "generic_owner_rows": generic_rows,
        "generic_owner_endpoint_checks": generic_endpoint_checks,
        "collapsed_endpoint_owner_rows": collapsed_rows,
        "structural_zero_generic_rows": structural_zero_generic_rows,
        "structural_zero_collapsed_endpoint_rows": structural_zero_collapsed_rows,
        "interior_owner_rows": interior_rows,
        "structural_zero_interior_rows": structural_zero_interior_rows,
        "owner_recovery_state_evaluations": len(evaluated_states),
        "minimum_owner_margin": minimum_owner,
        "ranks": (len(record["columns4"]), len(record["columns8"])),
    }


def _replay_factor_bank(
    factor_bank: Mapping[str, Any], *, verify_provenance: bool = True
) -> dict[str, Any]:
    if verify_provenance:
        _verify_provenance()
    model = c129.c126._load_model(c129.c126.C123_POINTS, "c130_complete_c123_primal")
    if model.LOG_TERMS != LOG_TERMS:
        raise CertificateError("exact model log terms changed")
    checked_records = _validate_factor_bank_structure(factor_bank, model)
    target = c129._target_interval(model)
    audits = [_audit_record(model, record, target) for record in checked_records]
    complete = c129._aggregate(audits, ALL_INDICES, model)
    complete["interior_owner_rows"] = sum(
        audit["interior_owner_rows"] for audit in audits
    )
    complete["structural_zero_generic_rows"] = sum(
        audit["structural_zero_generic_rows"] for audit in audits
    )
    complete["structural_zero_collapsed_endpoint_rows"] = sum(
        audit["structural_zero_collapsed_endpoint_rows"] for audit in audits
    )
    complete["structural_zero_interior_rows"] = sum(
        audit["structural_zero_interior_rows"] for audit in audits
    )
    complete["owner_recovery_state_evaluations"] = sum(
        audit["owner_recovery_state_evaluations"] for audit in audits
    )
    complete["per_epoch_owner_recovery_checks"] = (
        2 * complete["owner_recovery_state_evaluations"]
    )
    complete["endpoint_epoch_objective_checks"] = 4 * len(audits)
    complete["endpoint_weighted_objective_checks"] = 2 * len(audits)
    complete["interior_epoch_objective_checks"] = 2 * len(audits)
    complete["interior_weighted_objective_checks"] = len(audits)
    complete["all_embedded_columns_zero_sum"] = True
    complete["all_gram_matrices_psd"] = True
    complete["all_epoch_objectives_reconstructed"] = True
    negative_indices = tuple(
        audit["index"] for audit in audits if audit["margin_upper"] < 0
    )
    positive_indices = tuple(
        audit["index"] for audit in audits if audit["margin_lower"] > 0
    )
    if len(negative_indices) + len(positive_indices) != len(audits):
        raise CertificateError("a chamber margin interval straddles zero")
    expected_negative = (
        tuple(range(27)) + tuple(range(31, 36))
        + (59, 60, 77, 78, 79)
    )
    if negative_indices != expected_negative or len(positive_indices) != 98:
        raise CertificateError("piece sign census changed")
    complete["negative_piece_indices"] = negative_indices
    complete["positive_piece_indices"] = positive_indices
    if complete["minimum_owner_margin"] != F(1_137_298_595_103, 235_750_000_000_000_000):
        raise CertificateError("minimum active owner slack changed")
    if not complete["raw_margin_lower"] > F(1, 400):
        raise CertificateError("complete raw clean fence failed")
    if not complete["normalized_margin_lower"] > F(91, 25_000):
        raise CertificateError("complete normalized clean fence failed")
    if not complete["raw_margin_upper"] - complete["raw_margin_lower"] < F(1, 10**26):
        raise CertificateError("raw margin enclosure width clean fence failed")
    actual_census = (
        complete["chambers"],
        complete["factors"],
        complete["rank_min"],
        complete["rank_max"],
        complete["rank_sum"],
        complete["generic_owner_rows"],
        complete["generic_owner_endpoint_checks"],
        complete["collapsed_endpoint_owner_rows"],
        complete["structural_zero_generic_rows"],
        complete["structural_zero_collapsed_endpoint_rows"],
        complete["owner_recovery_state_evaluations"],
        complete["per_epoch_owner_recovery_checks"],
        complete["endpoint_epoch_objective_checks"],
        complete["endpoint_weighted_objective_checks"],
        complete["interior_owner_rows"],
        complete["structural_zero_interior_rows"],
        complete["interior_epoch_objective_checks"],
        complete["interior_weighted_objective_checks"],
    )
    frozen_census = (
        135, 270, 9, 25, 4_288,
        51_355, 102_710, 100_183,
        31_805, 62_713, 10_395, 20_790,
        540, 270, 51_355, 31_805, 270, 135,
    )
    if actual_census != frozen_census:
        raise CertificateError(f"exact replay census changed: {actual_census!r}")
    return {
        "target_lower": target[0],
        "target_upper": target[1],
        "complete_C123": complete,
        "remaining_C123_chambers": 0,
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
        "candidate": copy.deepcopy(EXPECTED_CANDIDATE),
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
                "30-term atanh log enclosures; modular exact-rank witnesses; separate epoch-4, "
                "epoch-8, and rho-weighted endpoint/interior objective reconstruction"
            ),
            "rank_witness_primes": list(RANK_PRIMES),
        },
    }
    value["integrity"]["payload_sha256"] = payload_hash(value)
    return value


def _factor_bank_from_discovery(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != DISCOVERY_SOURCE_SHA256:
        raise CertificateError("discovery source sha256 mismatch")
    try:
        source = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CertificateError("discovery source is invalid JSON") from exc
    if type(source) is not dict or raw != rendered_bytes(source):
        raise CertificateError("discovery source is not canonical compact JSON")
    clone = dict(source)
    internal = clone.pop("payload_sha256_without_hash", None)
    if internal != DISCOVERY_SOURCE_INTERNAL_SHA256 or internal != _object_hash(clone):
        raise CertificateError("discovery source internal hash mismatch")
    if source.get("schema") != "erdos1191.c129.c123_integrated_sparse_subbank.temporary.v1":
        raise CertificateError("discovery source schema changed")
    selection = source.get("selection")
    if type(selection) is not dict or tuple(selection.get("all_indices", ())) != ALL_INDICES:
        raise CertificateError("discovery source is not the complete ordered bank")
    raw_records = source.get("records")
    if type(raw_records) is not list or len(raw_records) != 135:
        raise CertificateError("discovery source record count changed")
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
    factor_bank = {"records": records}
    if _object_hash(factor_bank) != FACTOR_BANK_SHA256:
        raise CertificateError("stripped factor bank hash changed")
    return factor_bank


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
    add("C129-hash", lambda x: x["sources"].__setitem__("C129_exact_replay_verifier_sha256", "0" * 64))
    add("candidate-C", lambda x: x["candidate"].__setitem__("C_ordered_suffix", "1/9"))
    add("selection", lambda x: x["selection"]["factor_bank_indices"].pop())
    add("raw-fence", lambda x: x["results"].__setitem__("raw_margin_greater_than", "1/100"))
    add("normalized-fence", lambda x: x["results"].__setitem__("normalized_margin_greater_than", "1/100"))
    add("census", lambda x: x["results"].__setitem__("generic_owner_rows", 1))
    add("false-C120", lambda x: x["scope"].__setitem__("C120_phase_primal_constructed", True))
    add("false-C103", lambda x: x["scope"].__setitem__("C103_phase_rule_admissible_proved", True))
    add("false-C103-ledger", lambda x: x["scope"].__setitem__("C103_Abel_boundary_terminal_ledger_constructed", True))
    add("false-global", lambda x: x["scope"].__setitem__("global_phase_rule_admissible_proved", True))
    add("false-master", lambda x: x["scope"].__setitem__("local_master_inequality_proved", True))
    add("false-rank", lambda x: x["scope"].__setitem__("arbitrary_rank_proved", True))
    add("false-owner-stitching", lambda x: x["scope"].__setitem__("global_owner_stitching_proved", True))
    add("false-C058", lambda x: x["scope"].__setitem__("C058_resolved", True))
    add("false-prize", lambda x: x["scope"].__setitem__("publication_novelty_or_prize_claimed", True))
    add("float-census", lambda x: x["results"].__setitem__("factor_bank_chambers", 135.0))
    add("integer-scope", lambda x: x["scope"].__setitem__("C058_resolved", 0))

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

    actual4, actual8 = F(2), F(3)
    expected4, expected8 = F(1), F(43, 9)
    if actual4 + RHO * actual8 != expected4 + RHO * expected8:
        raise CertificateError("controlled interior mutation is malformed")
    try:
        _check_interior_objectives(
            index=0,
            actual4=actual4,
            actual8=actual8,
            expected4=expected4,
            expected8=expected8,
        )
    except CertificateError:
        rejected += 1
    else:
        raise CertificateError("interior objective cancellation mutation was accepted")

    physical = {4: F(1), 8: F(4)}
    owners = ((4, 1), (8, 1))
    owned = (F(2), F(3))
    try:
        c129._check_epoch_owner_recovery(
            physical=physical,
            owned=owned,
            owners=owners,
        )
    except CertificateError:
        rejected += 1
    else:
        raise CertificateError("epoch owner recovery cancellation mutation was accepted")

    try:
        c129._check_structural_zero_owner(
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
    if attempted != 28:
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
    complete = summary["complete_C123"]
    print(
        "VERIFY_OK",
        "row=C123",
        "common_phase=[82,164]",
        "rho=9/16",
        f"chambers={complete['chambers']}",
        f"factors={complete['factors']}",
        f"generic_owner_rows={complete['generic_owner_rows']}",
        f"generic_owner_endpoint_checks={complete['generic_owner_endpoint_checks']}",
        f"collapsed_endpoint_owner_rows={complete['collapsed_endpoint_owner_rows']}",
        "raw_margin>1/400",
        "normalized_margin>91/25000",
        f"mutations_rejected={mutations['mutations_rejected']}",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
