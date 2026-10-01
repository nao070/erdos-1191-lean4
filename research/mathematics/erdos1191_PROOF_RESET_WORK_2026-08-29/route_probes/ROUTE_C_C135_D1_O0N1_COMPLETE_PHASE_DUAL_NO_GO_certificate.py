#!/usr/bin/env python3
"""Exact C135 certificate for the frozen D1 O0N1 complete-phase no-go.

The accepted claim is only about one finite, frozen 16-mark instance, one
common phase, one coefficient vector, and the independent epoch-4/epoch-8
zero-row-sum PSD aggregate cone. An adaptive piecewise-constant exact dual
has complete-phase upper bound U^+ below the frozen target T^-.

The source bank is preserved byte-for-byte from discovery, but floating
solver fields are provenance only. Every accepted inequality is replayed
with Fraction arithmetic, endpoint Bareiss positive-definiteness, and exact
atanh-series log enclosures. No chamberwise sign condition is imposed.
"""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import sys
from typing import Any, Mapping, Sequence


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
CANONICAL_ROUTE = Path(
    "/Users/USER/Documents/ChatGPT/mathematics/"
    "erdos1191_PROOF_RESET_WORK_2026-08-29/route_probes"
)
if str(CANONICAL_ROUTE) not in sys.path:
    sys.path.insert(0, str(CANONICAL_ROUTE))

import ROUTE_C_C126_COMMON_COMPLETED_SHELL_PHASE_certificate as c126
import ROUTE_C_C128_COMMON_PHASE_POINTWISE_NO_GO_certificate as c128


SCHEMA = "erdos1191.route_c.c135.d1_o0n1_complete_phase_dual_no_go.v1"
STATUS = "EXACT_FROZEN_D1_O0N1_COMPLETE_PHASE_DUAL_SEPARATOR_C058_OPEN"
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_C135_D1_O0N1_COMPLETE_PHASE_DUAL_NO_GO_certificate.json"
SOURCE = HERE / "ROUTE_C_C135_D1_O0N1_COMPLETE_PHASE_DUAL_NO_GO_source.json"
PARENT_SOURCE = HERE / "ROUTE_C_C135_D1_O0N1_ONE_DUAL_PER_CHAMBER_parent_source.json"

SOURCE_SHA256 = "2949602baa0cb68aa3131bcb003fa2ac35156743bb2202e9a02f906ccf960c6b"
SOURCE_INTERNAL_SHA256 = "8c19def256d58813a22220d80fe1ec96fcd5da1a3cb580381e5fee70fb38310d"
PARENT_SOURCE_SHA256 = "93efb6b9846800f4025d72bd79536cc052f46f750e706b2966efa90928002912"
PARENT_INTERNAL_SHA256 = "325d1c4e5556ab654a21c698583628478e750c61859622140a414ac0228aac43"
C126_SHA256 = "830c6afa79d49d386e5bc57bdb5578b8074e783486cbaf991164ae25e91a5981"
C128_SHA256 = "d6cc32966f58bc6381d8673901f5438e2c2570d20bcd07f8662192a5c3f3dea2"
MODEL_SHA256 = "6e8d7e3f975e952442672cb1d18e4512d616f343bb4f6379ba0c8701cd996fe9"

PREFIX = (22, 38, 23)
OLD_GAPS = (71, 130, 210, 19)
NEW_CANONICAL_GAPS = (62, 45, 91, 66, 103, 109, 111, 69)
NEW_O0N1_GAPS = NEW_CANONICAL_GAPS[1:] + NEW_CANONICAL_GAPS[:1]
POINTS = (0, 22, 60, 83, 154, 284, 494, 513, 558, 649, 715, 818, 927, 1038, 1107, 1169)
PHASE = (F(82), F(164))
RHO = F(9, 16)
EPSILON = F(1, 1000)
A_COEFFICIENT = F(1, 1000)
B_COEFFICIENT = F(1, 2)
C_ORDERED_SUFFIX = F(1, 10)
E2 = F(0)
LOG_TERMS = 30

SOURCE_KEYS = {
    "schema", "scope", "rotation", "points", "parent_artifact",
    "parent_sha256", "uniform_subdivision_factor",
    "selected_parent_chambers", "records", "exact_replay",
    "payload_sha256_without_hash",
}
PARENT_KEYS = {
    "schema", "scope", "points", "base", "H2", "H3", "eta_ratio",
    "rho", "breakpoints", "records", "strictly_negative",
    "certified_log_integral_numerator_upper_bound",
    "exact_recomputed_numerator_less_than_bound",
    "approximate_recomputed_numerator_upper", "payload_sha256_without_hash",
}
RECORD_KEYS = {
    "index", "parent_index", "sub_index", "left", "right",
    "Dc4", "Do4", "Dc8", "Do8", "n4", "n8",
}
PARENT_RECORD_KEYS = {"index", "left", "right", "Dc4", "Do4", "Dc8", "Do8", "n4", "n8"}
REFINED_DUAL_REQUIRED = {
    "alpha", "denominator", "fallback", "float_objective",
    "improvement_over_parent", "objective", "status", "weights",
}
REFINED_DUAL_OPTIONAL = {"min_pivot_left", "min_pivot_right", "support"}
PARENT_DUAL_KEYS = {
    "alpha", "denominator", "float_objective", "min_pivot_left",
    "min_pivot_right", "objective", "status", "support", "weights",
}

EXPECTED_SCOPE = {
    "frozen_D1_setup_only": True,
    "O0N1_rotation_only": True,
    "common_phase_82_to_164_only": True,
    "rho_9_over_16_only": True,
    "fixed_coefficients_only": True,
    "k2_finite_envelope_C2_only": True,
    "independent_epoch4_epoch8_zero_row_sum_PSD_aggregate_cone_only": True,
    "complete_phase_integrated_dual_separator_constructed": True,
    "frozen_O0N1_candidate_lower_bound_refuted_by_weak_duality": True,
    "chamberwise_sign_test_used": False,
    "original_universal_D1_same_multiset_rotation_lemma_false": True,
    "O0N1_primal_feasibility_certified": False,
    "O0N1_physical_primal_infeasibility_claimed": False,
    "dual_optimality_proved": False,
    "all_D1_rotations_refuted": False,
    "Route_C_false": False,
    "C130_invalid": False,
    "C131_invalid": False,
    "arbitrary_representative_independence_globally_false": False,
    "C103_global_owner_ledger_resolved": False,
    "common_phase_rule_globally_admissible_proved": False,
    "cross_row_compatibility_proved": False,
    "arbitrary_history_proved": False,
    "arbitrary_rank_proved": False,
    "C058_false_or_resolved": False,
    "Erdos_1191_resolved": False,
    "Q1_Q2_resolved": False,
    "publication_novelty_or_prize_claimed": False,
}


class CertificateError(RuntimeError):
    pass


def ftext(value: F | int) -> str:
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def object_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def payload_hash(value: Mapping[str, Any]) -> str:
    clone = copy.deepcopy(value)
    clone["integrity"]["payload_sha256"] = ""
    return object_hash(clone)


def _exact_int(value: object, label: str) -> int:
    if type(value) is not int:
        raise CertificateError(f"{label}: expected exact integer")
    return value


def _fraction(value: object, label: str) -> F:
    if type(value) is not str:
        raise CertificateError(f"{label}: expected rational text")
    try:
        return F(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise CertificateError(f"{label}: invalid rational text") from exc


def _read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CertificateError(f"cannot read JSON {path.name}") from exc
    if type(value) is not dict:
        raise CertificateError(f"{path.name}: expected object")
    return value


def _verify_provenance() -> None:
    expected = (
        (SOURCE, SOURCE_SHA256, "refined source"),
        (PARENT_SOURCE, PARENT_SOURCE_SHA256, "parent source"),
        (CANONICAL_ROUTE / Path(c126.__file__).name, C126_SHA256, "C126 verifier"),
        (CANONICAL_ROUTE / Path(c128.__file__).name, C128_SHA256, "C128 verifier"),
        (CANONICAL_ROUTE / "ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate.py", MODEL_SHA256, "exact model"),
    )
    for path, digest, label in expected:
        if sha256(path) != digest:
            raise CertificateError(f"{label}: sha256 mismatch")


def variation(gaps: Sequence[int]) -> F:
    total = sum(gaps)
    return F(1) - F(total * total, len(gaps) * sum(g * g for g in gaps))


def right_tail_variation(gaps: Sequence[int]) -> F:
    n = len(gaps)
    levels = n.bit_length() - 1
    if n != 2 ** levels:
        raise CertificateError("right-tail variation requires dyadic length")
    total = sum(gaps)
    c_rt = sum((F(sum(gaps[-2 ** ell:]), total) for ell in range(levels)), F()) / levels - F(n - 1, n * levels)
    return (8 * c_rt + 3) / 11


def log_interval(value: F, terms: int = LOG_TERMS) -> tuple[F, F]:
    if value < 1:
        raise CertificateError("log enclosure input below one")
    z = (value - 1) / (value + 1)
    lower = 2 * sum((z ** (2 * k + 1) / (2 * k + 1) for k in range(terms)), F())
    tail = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return lower, lower + tail


def target_interval() -> tuple[F, F]:
    delta_v = variation(NEW_O0N1_GAPS) - variation(OLD_GAPS)
    delta_vrt = right_tail_variation(NEW_O0N1_GAPS) - right_tail_variation(OLD_GAPS)
    if delta_v != -F(443_620_417, 1_928_247_678) or delta_vrt != F(5034, 96965):
        raise CertificateError("frozen variation increments changed")
    log_lower, log_upper = log_interval(F(215, 82))
    rational = EPSILON + B_COEFFICIENT * abs(delta_v) - C_ORDERED_SUFFIX * delta_vrt
    return (
        (rational + A_COEFFICIENT * log_lower) / 3 - E2,
        (rational + A_COEFFICIENT * log_upper) / 3 - E2,
    )


def _fixture_audit(payload: Mapping[str, Any]) -> Any:
    gaps = PREFIX + OLD_GAPS + NEW_O0N1_GAPS
    points = [0]
    for gap in gaps:
        points.append(points[-1] + gap)
    if tuple(points) != POINTS or tuple(payload.get("points", ())) != POINTS:
        raise CertificateError("O0N1 points changed")
    seen: dict[int, tuple[int, int]] = {}
    for i in range(16):
        for j in range(i + 1, 16):
            difference = POINTS[j] - POINTS[i]
            if difference in seen:
                raise CertificateError("O0N1 is not Golomb")
            seen[difference] = (i, j)
    if len(seen) != math.comb(16, 2):
        raise CertificateError("positive difference census changed")
    if POINTS[7] - POINTS[3] != 430 or POINTS[15] - POINTS[7] != 656:
        raise CertificateError("completed-shell spans changed")
    model = c126._load_model(POINTS, "c135_o0n1")
    breakpoints = tuple(model._breakpoints())
    if breakpoints[0] != PHASE[0] or breakpoints[-1] != PHASE[1] or len(breakpoints) != 135:
        raise CertificateError("canonical O0N1 phase partition changed")
    return model, breakpoints


def _source_internal_hash(payload: Mapping[str, Any], expected: str, label: str) -> None:
    clone = copy.deepcopy(payload)
    embedded = clone.pop("payload_sha256_without_hash", None)
    if embedded != expected or object_hash(clone) != expected:
        raise CertificateError(f"{label}: internal sha256 mismatch")


def _dual_epoch_replay(model: Any, record: Mapping[str, Any], left: F, right: F, epoch: int, *, refined: bool) -> tuple[F, int, int]:
    dual = record.get(f"n{epoch}")
    if type(dual) is not dict:
        raise CertificateError("dual record missing")
    keys = set(dual)
    if refined:
        if not REFINED_DUAL_REQUIRED <= keys <= REFINED_DUAL_REQUIRED | REFINED_DUAL_OPTIONAL:
            raise CertificateError("refined dual keys changed")
    elif keys != PARENT_DUAL_KEYS:
        raise CertificateError("parent dual keys changed")
    denominator = _exact_int(dual.get("denominator"), "dual denominator")
    weights_raw = dual.get("weights")
    if denominator <= 0 or type(weights_raw) is not list or len(weights_raw) != 308:
        raise CertificateError("malformed exact dual")
    weights = tuple(_exact_int(x, "dual weight") for x in weights_raw)
    if min(weights) < 0:
        raise CertificateError("negative dual weight")
    hc, ho, weighted, dc, do, objective = model._dual_epoch_reconstruction(
        left, right, epoch, denominator, weights
    )
    if dc != _fraction(record[f"Dc{epoch}"], "Dc") or do != _fraction(record[f"Do{epoch}"], "Do"):
        raise CertificateError("dual scalar reconstruction changed")
    if objective != _fraction(dual.get("objective"), "dual objective"):
        raise CertificateError("dual objective reconstruction changed")
    for endpoint in (left, right):
        slack = model._integer_slack(hc, ho, weighted, denominator, endpoint)
        if not model._bareiss_positive_definite(slack):
            raise CertificateError("exact endpoint dual slack is not positive definite")
    return objective, denominator, sum(weight > 0 for weight in weights)


def _integrate_piece(record: Mapping[str, Any], objectives: Mapping[int, F]) -> tuple[F, F]:
    left = _fraction(record["left"], "left")
    right = _fraction(record["right"], "right")
    a = 2 * (
        _fraction(record["Dc4"], "Dc4") + RHO * _fraction(record["Dc8"], "Dc8")
    ) - (objectives[4] + RHO * objectives[8])
    b = 2 * (
        _fraction(record["Do4"], "Do4") + RHO * _fraction(record["Do8"], "Do8")
    )
    log_lower, log_upper = log_interval(right / left)
    reciprocal = b * (F(1, left) - F(1, right))
    if a >= 0:
        return a * log_lower + reciprocal, a * log_upper + reciprocal
    return a * log_upper + reciprocal, a * log_lower + reciprocal


def _normalize(raw_lower: F, raw_upper: F) -> tuple[F, F]:
    log2_lower, log2_upper = log_interval(F(2))
    if not F() < raw_lower <= raw_upper or not F() < log2_lower <= log2_upper:
        raise CertificateError("positive normalization precondition failed")
    corners = (
        raw_lower / log2_lower, raw_lower / log2_upper,
        raw_upper / log2_lower, raw_upper / log2_upper,
    )
    return min(corners), max(corners)


def replay_parent(payload: Mapping[str, Any], model: Any, breakpoints: Sequence[F]) -> dict[str, Any]:
    if set(payload) != PARENT_KEYS:
        raise CertificateError("parent source keys changed")
    _source_internal_hash(payload, PARENT_INTERNAL_SHA256, "parent source")
    if (
        payload["schema"] != "erdos1191.c058_eta_negative_full_phase_dual.discovery.v1"
        or payload["scope"] != "temporary exploratory exact replay; not canonical or registered"
        or tuple(payload["points"]) != POINTS
        or payload["base"] != "82/1"
        or payload["H2"] != 430
        or payload["H3"] != 656
        or _fraction(payload["eta_ratio"], "eta ratio") != F(82, 215)
        or _fraction(payload["rho"], "rho") != RHO
    ):
        raise CertificateError("parent fixture changed")
    if tuple(_fraction(x, "parent breakpoint") for x in payload["breakpoints"]) != tuple(breakpoints):
        raise CertificateError("parent breakpoint list changed")
    records = payload.get("records")
    if type(records) is not list or len(records) != 134:
        raise CertificateError("parent record census changed")
    raw_lower = F()
    raw_upper = F()
    denominators: set[int] = set()
    supports: list[int] = []
    for index, (record, left, right) in enumerate(zip(records, breakpoints, breakpoints[1:])):
        if type(record) is not dict or set(record) != PARENT_RECORD_KEYS:
            raise CertificateError("parent record shape changed")
        if (
            _exact_int(record["index"], "parent index") != index
            or _fraction(record["left"], "parent left") != left
            or _fraction(record["right"], "parent right") != right
        ):
            raise CertificateError("parent partition order changed")
        objectives: dict[int, F] = {}
        for epoch in (4, 8):
            objective, denominator, support = _dual_epoch_replay(
                model, record, left, right, epoch, refined=False
            )
            objectives[epoch] = objective
            denominators.add(denominator)
            supports.append(support)
        piece_lower, piece_upper = _integrate_piece(record, objectives)
        raw_lower += piece_lower
        raw_upper += piece_upper
    normalized = _normalize(raw_lower, raw_upper)
    target = target_interval()
    gap = normalized[0] - target[1]
    if not F(1887, 1_000_000) < gap < F(1888, 1_000_000):
        raise CertificateError("parent exact NO_SEPARATION gap changed")
    return {
        "classification": "EXACT_STORED_DUAL_NO_SEPARATION_NOT_PRIMAL_FEASIBILITY",
        "pieces": 134,
        "epoch_duals": 268,
        "weights": 134 * 2 * 308,
        "endpoint_PD_checks": 536,
        "denominators": tuple(sorted(denominators)),
        "support_range": (min(supports), max(supports)),
        "raw_interval": (raw_lower, raw_upper),
        "normalized_interval": normalized,
        "target_interval": target,
        "lower_minus_target_upper": gap,
    }


def replay_refined(
    payload: Mapping[str, Any],
    parent: Mapping[str, Any],
    model: Any,
    breakpoints: Sequence[F],
    *,
    require_embedded: bool = True,
) -> dict[str, Any]:
    if set(payload) != SOURCE_KEYS:
        raise CertificateError("refined source keys changed")
    if require_embedded:
        _source_internal_hash(payload, SOURCE_INTERNAL_SHA256, "refined source")
    if (
        payload["schema"] != "erdos1191.d1.o0n1.refined_complete_phase_dual.scratch.v1"
        or payload["scope"] != "scratch-only exact falsification search; no canonical claim"
        or payload["rotation"] != [0, 1]
        or payload["parent_sha256"] != PARENT_SOURCE_SHA256
        or _exact_int(payload["uniform_subdivision_factor"], "subdivision factor") != 4
    ):
        raise CertificateError("refined source frozen setup changed")
    selected = payload.get("selected_parent_chambers")
    if type(selected) is not list or len(selected) != 60 or any(type(x) is not int for x in selected):
        raise CertificateError("selected chamber census changed")
    if selected != sorted(set(selected)) or any(not 0 <= x < 134 for x in selected):
        raise CertificateError("selected chamber indices changed")
    selected_set = set(selected)
    expected_partition: list[tuple[int, int, F, F]] = []
    for parent_index, (left, right) in enumerate(zip(breakpoints, breakpoints[1:])):
        factor = 4 if parent_index in selected_set else 1
        for sub_index in range(factor):
            expected_partition.append((
                parent_index,
                sub_index,
                left + (right - left) * sub_index / factor,
                left + (right - left) * (sub_index + 1) / factor,
            ))
    records = payload.get("records")
    if type(records) is not list or len(records) != len(expected_partition) or len(records) != 314:
        raise CertificateError("refined partition census changed")
    raw_lower = F()
    raw_upper = F()
    denominators: set[int] = set()
    supports: list[int] = []
    improvements = 0
    inherited = 0
    partition_text: list[list[str | int]] = []
    for index, (record, expected) in enumerate(zip(records, expected_partition)):
        if type(record) is not dict or set(record) != RECORD_KEYS:
            raise CertificateError("refined record shape changed")
        parent_index, sub_index, left, right = expected
        if (
            _exact_int(record["index"], "record index") != index
            or _exact_int(record["parent_index"], "parent index") != parent_index
            or _exact_int(record["sub_index"], "sub index") != sub_index
            or _fraction(record["left"], "record left") != left
            or _fraction(record["right"], "record right") != right
        ):
            raise CertificateError("refined partition construction changed")
        partition_text.append([parent_index, sub_index, ftext(left), ftext(right)])
        objectives: dict[int, F] = {}
        for epoch in (4, 8):
            objective, denominator, support = _dual_epoch_replay(
                model, record, left, right, epoch, refined=True
            )
            objectives[epoch] = objective
            denominators.add(denominator)
            supports.append(support)
            parent_objective = _fraction(
                parent["records"][parent_index][f"n{epoch}"]["objective"],
                "parent objective",
            )
            improvement = _fraction(
                record[f"n{epoch}"]["improvement_over_parent"], "improvement"
            )
            if improvement != objective - parent_objective:
                raise CertificateError("parent improvement reconstruction changed")
            if parent_index in selected_set:
                if not improvement > 0 or record[f"n{epoch}"]["fallback"] is not False:
                    raise CertificateError("selected refined dual is not a strict exact improvement")
                improvements += 1
            else:
                if improvement != 0 or record[f"n{epoch}"]["fallback"] is not True:
                    raise CertificateError("unselected chamber did not inherit parent dual")
                inherited += 1
        piece_lower, piece_upper = _integrate_piece(record, objectives)
        raw_lower += piece_lower
        raw_upper += piece_upper
    normalized = _normalize(raw_lower, raw_upper)
    target = target_interval()
    margin = target[0] - normalized[1]
    if not normalized[1] < target[0]:
        raise CertificateError("exact complete-phase separator disappeared")
    if not (
        normalized[1] < F(36_849_435_771, 10**12)
        and target[0] > F(18_634_061_003, 5 * 10**11)
        and margin > F(83_737_247, 2 * 10**11)
        and margin > F(1, 2500)
    ):
        raise CertificateError("clean separator fences changed")
    if improvements != 480 or inherited != 148:
        raise CertificateError("refinement improvement census changed")
    if require_embedded:
        embedded = payload.get("exact_replay")
        if type(embedded) is not dict:
            raise CertificateError("embedded exact replay missing")
        if (
            embedded.get("classification") != "EXACT_SEPARATOR_KILL"
            or embedded.get("refined_pieces") != 314
            or embedded.get("epoch_duals") != 628
            or embedded.get("endpoint_PD_checks") != 1256
            or embedded.get("strictly_improved_epoch_pieces") != 480
            or tuple(_fraction(x, "embedded raw") for x in embedded.get("raw_interval", ())) != (raw_lower, raw_upper)
            or tuple(_fraction(x, "embedded normalized") for x in embedded.get("normalized_interval", ())) != normalized
            or tuple(_fraction(x, "embedded target") for x in embedded.get("target_interval", ())) != target
            or _fraction(embedded.get("classification_margin"), "embedded margin") != margin
        ):
            raise CertificateError("embedded exact replay changed")
    return {
        "classification": "EXACT_COMPLETE_PHASE_SEPARATOR",
        "parent_chambers": 134,
        "selected_parent_chambers": tuple(selected),
        "subdivision_factor": 4,
        "refined_pieces": 314,
        "epoch_duals": 628,
        "weights": 314 * 2 * 308,
        "endpoint_PD_checks": 1256,
        "denominators": tuple(sorted(denominators)),
        "support_range": (min(supports), max(supports)),
        "strict_improvements": improvements,
        "inherited_epoch_duals": inherited,
        "partition_sha256": object_hash(partition_text),
        "raw_interval": (raw_lower, raw_upper),
        "normalized_interval": normalized,
        "target_interval": target,
        "margin": margin,
    }


def replay_sources(
    *,
    verify_provenance: bool = True,
    refined_override: Mapping[str, Any] | None = None,
    parent_override: Mapping[str, Any] | None = None,
    require_embedded: bool = True,
) -> dict[str, Any]:
    if verify_provenance:
        _verify_provenance()
    refined = dict(refined_override) if refined_override is not None else _read_json(SOURCE)
    parent = dict(parent_override) if parent_override is not None else _read_json(PARENT_SOURCE)
    model, breakpoints = _fixture_audit(refined)
    parent_summary = replay_parent(parent, model, breakpoints)
    refined_summary = replay_refined(
        refined, parent, model, breakpoints, require_embedded=require_embedded
    )
    improvement = parent_summary["normalized_interval"][0] - refined_summary["normalized_interval"][1]
    if improvement <= F(461_159_269, 2 * 10**11):
        raise CertificateError("strict dual-expressivity improvement fence changed")
    return {"parent": parent_summary, "refined": refined_summary, "improvement": improvement}


def _serialize_summary(summary: Mapping[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in summary.items():
        if isinstance(value, F):
            result[key] = ftext(value)
        elif isinstance(value, tuple):
            result[key] = [ftext(x) if isinstance(x, F) else x for x in value]
        else:
            result[key] = value
    return result


def build_certificate(summaries: Mapping[str, Any] | None = None) -> dict[str, Any]:
    if summaries is None:
        summaries = replay_sources()
    delta_v = variation(NEW_O0N1_GAPS) - variation(OLD_GAPS)
    delta_vrt = right_tail_variation(NEW_O0N1_GAPS) - right_tail_variation(OLD_GAPS)
    value: dict[str, Any] = {
        "schema": SCHEMA,
        "status": STATUS,
        "claim_id": "C135",
        "frozen_setup": {
            "D1_prefix_gaps": list(PREFIX),
            "old_gap_multiset_in_O0_order": list(OLD_GAPS),
            "new_gap_multiset_canonical_order": list(NEW_CANONICAL_GAPS),
            "new_gap_sequence_in_N1_rotation": list(NEW_O0N1_GAPS),
            "rotation": [0, 1],
            "points": list(POINTS),
            "positive_difference_count": 120,
            "H2": 430,
            "H3": 656,
            "common_phase": ["82/1", "164/1"],
            "eta_ratio": "82/215",
            "rho": "9/16",
            "k": 2,
            "finite_envelope_C": 2,
            "coefficients": {
                "epsilon": "1/1000",
                "A": "1/1000",
                "B": "1/2",
                "C_ordered_suffix": "1/10",
                "e2": "0/1",
            },
            "delta_V": ftext(delta_v),
            "delta_Vrt": ftext(delta_vrt),
            "cone": "52-coordinate independent epoch-4/epoch-8 zero-row-sum PSD aggregate cone",
        },
        "partition_construction": {
            "canonical_parent_chambers": 134,
            "selected_parent_chambers": list(summaries["refined"]["selected_parent_chambers"]),
            "selected_parent_chamber_count": 60,
            "uniform_exact_subdivision_factor": 4,
            "unselected_parent_chambers": 74,
            "complete_refined_piece_count": 314,
            "start": "82/1",
            "end": "164/1",
            "construction": "selected parent interval [l,r] maps to four exact equal rational subintervals; every unselected interval is retained whole",
            "partition_sha256": summaries["refined"]["partition_sha256"],
        },
        "exact_results": {
            "parent_one_stored_dual_per_chamber": _serialize_summary(summaries["parent"]),
            "adaptive_refined_complete_phase_dual": _serialize_summary(summaries["refined"]),
            "parent_lower_minus_refined_upper": ftext(summaries["improvement"]),
            "separator_fences": {
                "U_plus_less_than": "36849435771/1000000000000",
                "T_minus_greater_than": "18634061003/500000000000",
                "T_minus_minus_U_plus_greater_than": "83737247/200000000000",
            },
            "integration_rule": "sum all 314 exact piece enclosures over the complete phase, then divide by an exact enclosure of log(2)",
            "chamberwise_sign_criterion_used": False,
            "floating_solver_fields_used_as_evidence": False,
        },
        "logical_consequence": {
            "frozen_D1_rotation_hypothesis": (
                "Every Golomb member of the specified frozen 4x8 cyclic old/new same-multiset rotation bank satisfies the frozen candidate complete-phase lower bound"
            ),
            "counterexample": "O0N1",
            "conclusion": "the displayed universal finite D1 rotation hypothesis is false",
            "reason": "the exact separator refutes the frozen candidate lower bound for O0N1 by weak duality",
            "naming_disambiguation": "this isolated D1 rotation hypothesis is not the repository Q2 DAG node D1 or the approach-registry D1 label",
            "C130_O0N0_status": "unchanged and valid within its own frozen scope",
            "global_representative_independence_conclusion": "none",
        },
        "false_negative_record": {
            "earlier_result": "EXACT_STORED_DUAL_NO_SEPARATION_NOT_PRIMAL_FEASIBILITY",
            "restricted_stored_bank": "one stored constant dual vector for each whole canonical combinatorial chamber",
            "cause": "the stored construction lacked enough piecewise expressivity; subdivision exposed a separator",
            "strictly_improved_refined_epoch_duals": 480,
            "unchanged_inherited_epoch_duals": 148,
            "classification": "false negative as an infeasibility classifier; never a primal-feasibility certificate",
            "unsplit_dual_optimality_claimed": False,
        },
        "scope": dict(EXPECTED_SCOPE),
        "sources": {
            "refined_exact_dual_bank": SOURCE.name,
            "refined_exact_dual_bank_sha256": SOURCE_SHA256,
            "refined_exact_dual_bank_internal_sha256": SOURCE_INTERNAL_SHA256,
            "parent_exact_dual_bank": PARENT_SOURCE.name,
            "parent_exact_dual_bank_sha256": PARENT_SOURCE_SHA256,
            "parent_exact_dual_bank_internal_sha256": PARENT_INTERNAL_SHA256,
            "C126_exact_machinery_sha256": C126_SHA256,
            "C128_target_machinery_sha256": C128_SHA256,
            "exact_model_sha256": MODEL_SHA256,
            "discovery_only_fields": [
                "status", "float_objective", "min_pivot_left", "min_pivot_right"
            ],
        },
        "integrity": {
            "algorithm": "sha256",
            "payload_sha256": "",
            "accepted_arithmetic": "fractions.Fraction, nonnegative integer rational weights, exact endpoint Bareiss positive-definiteness, 30-term rational atanh log enclosures",
        },
    }
    value["integrity"]["payload_sha256"] = payload_hash(value)
    return value


def verify_certificate(
    value: Mapping[str, Any],
    *,
    summaries: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if type(value) is not dict:
        raise CertificateError("certificate must be an object")
    expected_keys = {
        "schema", "status", "claim_id", "frozen_setup", "partition_construction",
        "exact_results", "logical_consequence", "false_negative_record", "scope",
        "sources", "integrity",
    }
    if (
        set(value) != expected_keys
        or value.get("schema") != SCHEMA
        or value.get("status") != STATUS
        or value.get("claim_id") != "C135"
    ):
        raise CertificateError("certificate schema, status, claim id, or keys changed")
    if value.get("scope") != EXPECTED_SCOPE:
        raise CertificateError("scope changed")
    integrity = value.get("integrity")
    if (
        type(integrity) is not dict
        or integrity.get("algorithm") != "sha256"
        or integrity.get("payload_sha256") != payload_hash(value)
    ):
        raise CertificateError("certificate payload hash mismatch")
    if summaries is None:
        summaries = replay_sources()
    rebuilt = build_certificate(summaries)
    if value != rebuilt:
        raise CertificateError("stored certificate differs from exact rebuild")
    return dict(summaries)


def mutation_audit(value: Mapping[str, Any], summaries: Mapping[str, Any]) -> int:
    mutations: list[tuple[str, dict[str, Any]]] = []

    def add(label: str, mutator: Any) -> None:
        changed = copy.deepcopy(value)
        mutator(changed)
        changed["integrity"]["payload_sha256"] = payload_hash(changed)
        mutations.append((label, changed))

    add("route-c-upgrade", lambda x: x["scope"].__setitem__("Route_C_false", True))
    add("C130-upgrade", lambda x: x["scope"].__setitem__("C130_invalid", True))
    add("C131-upgrade", lambda x: x["scope"].__setitem__("C131_invalid", True))
    add(
        "representative-upgrade",
        lambda x: x["scope"].__setitem__(
            "arbitrary_representative_independence_globally_false", True
        ),
    )
    add("C058-upgrade", lambda x: x["scope"].__setitem__("C058_false_or_resolved", True))
    add("erdos-upgrade", lambda x: x["scope"].__setitem__("Erdos_1191_resolved", True))
    add(
        "chamberwise-sign",
        lambda x: x["exact_results"].__setitem__("chamberwise_sign_criterion_used", True),
    )
    add("rotation", lambda x: x["frozen_setup"].__setitem__("rotation", [0, 2]))
    rejected = 0
    for label, changed in mutations:
        try:
            verify_certificate(changed, summaries=summaries)
        except CertificateError:
            rejected += 1
        else:
            raise CertificateError(f"mutation accepted: {label}")
    return rejected


def write_certificate(
    path: Path = DEFAULT_CERTIFICATE,
    *,
    summaries: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    value = build_certificate(summaries)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    summaries = replay_sources()
    value = (
        write_certificate(summaries=summaries)
        if args.write
        else _read_json(DEFAULT_CERTIFICATE)
    )
    summaries = verify_certificate(value, summaries=summaries)
    rejected = mutation_audit(value, summaries)
    refined = summaries["refined"]
    print(
        "EXACT_C135_OK",
        f"payload_sha256={value['integrity']['payload_sha256']}",
        f"source_sha256={SOURCE_SHA256}",
        f"partition_sha256={refined['partition_sha256']}",
        f"pieces={refined['refined_pieces']}",
        f"epoch_duals={refined['epoch_duals']}",
        f"endpoint_PD_checks={refined['endpoint_PD_checks']}",
        f"margin_gt_1_over_2500={refined['margin'] > F(1, 2500)}",
        f"mutations_rejected={rejected}",
        "C058_OPEN",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
