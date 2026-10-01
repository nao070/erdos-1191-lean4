#!/usr/bin/env python3
"""Exact hybrid dual certificate closing the C118 storage window.

Five hotspot event chambers from the canonical C118 certificate are each
split into four equal pieces in the affine slack coordinate ``u = 1/t``.
The other 82 chambers retain their canonical duals.  Every stored weight is
nonnegative and rational; all objectives, demand coefficients, endpoint
positive-definiteness checks, logarithm enclosures, and storage comparisons
are replayed with integers and ``fractions.Fraction`` only.

The conclusion is finite and cone-specific.  It refutes the displayed trial
storage coefficients and, more generally, their stated coefficient box on
this one fixture.  It does not refute arbitrary scalar storage coefficients,
C058, or Erdős Problem #1191.
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
from typing import Any, Mapping, Sequence

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

import ROUTE_C_ETA_NEGATIVE_FULL_PHASE_DUAL_NO_GO_certificate as base


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_C118_SUBDIVIDED_STORAGE_NO_GO_certificate.json"
BASE_CERTIFICATE_NAME = "ROUTE_C_ETA_NEGATIVE_FULL_PHASE_DUAL_NO_GO_certificate.json"
BASE_FILE_SHA256 = "331da5cdf1e553c65cace050ffc2ac2ae2dee847f949e2b932aceaa43dafd55f"
BASE_PAYLOAD_SHA256 = "176cc369f21e9002945e4716b66a1a58a1e358e5e92c03572ae00039c2e01b16"
SOURCE_REFINEMENT_SHA256 = "0c975c10fea08aa33d4eed9f120bd5381d2355f7ea82f235216f7e08a06dcf5d"
REFINEMENT_PAYLOAD_SHA256 = "6f48fcfc0f39d7a929a2d766af11701ee95934a2276c17a5ad279092fc52903a"

SCHEMA = "erdos1191.c118.subdivided_storage_no_go.v1"
STATUS = "EXACT_FINITE_SUBDIVIDED_STORAGE_NO_GO_ONLY_C058_OPEN"
LOG_TERMS = 30
SELECTED_CHAMBERS = (49, 64, 70, 73, 74)
SUBDIVISIONS = 4
RHO = F(9, 16)
DELTA_V = F(3440812085, 9234857208)
EPSILON = F(1, 1000)
A_COEFFICIENT = F(1, 1000)
B_COEFFICIENT = F(1, 3)
E2 = F(0)
NORMALIZED_BARRIER = -F(83, 2000)
BOX_SEPARATION = F(1, 10000)
PROTOTYPE_SEPARATION = F(1, 2000)
NECESSARY_B_LOWER_BARRIER = F(249, 2000) / DELTA_V

EXPECTED_BASE = {
    "file": BASE_CERTIFICATE_NAME,
    "file_sha256": BASE_FILE_SHA256,
    "payload_sha256": BASE_PAYLOAD_SHA256,
}
EXPECTED_PROTOTYPE = {
    "k": 2,
    "epsilon": "1/1000",
    "A": "1/1000",
    "B": "1/3",
    "e2": "0/1",
    "eta_ratio": "1659/1768",
    "eta_absolute_log_ratio": "1768/1659",
    "delta_V": "3440812085/9234857208",
    "target": "(epsilon-A*eta_2-B*(V3-V2))/3-e2",
}
EXPECTED_BOX = {
    "epsilon_lower": "0/1",
    "A_lower": "0/1",
    "B_lower": "0/1",
    "B_upper": "1/3",
    "eta_is_negative": True,
    "delta_V_is_positive": True,
}
EXPECTED_CONCLUSION = {
    "normalized_dual_upper_less_than": "-83/2000",
    "prototype_rhs_lower_greater_than": "-83/2000",
    "prototype_gap_greater_than": "1/2000",
    "coefficient_box_rhs_lower_greater_than": "-207/5000",
    "coefficient_box_gap_greater_than": "1/10000",
    "necessary_B_greater_than": "287434930599/860203021250",
    "necessary_B_lower_barrier_greater_than_one_third": True,
    "fixed_C118_storage_prototype_refuted": True,
    "nonnegative_epsilon_A_and_B_at_most_one_third_refuted": True,
}
EXPECTED_SCOPE = {
    "fixed_C118_storage_prototype_refuted": True,
    "nonnegative_epsilon_A_and_B_at_most_one_third_refuted": True,
    "fixed_16_mark_k2_C2_fixture_only": True,
    "rho_9_over_16_only": True,
    "independent_epoch_block_cone_only": True,
    "all_scalar_storage_coefficients_refuted": False,
    "large_rank_local_inequality_refuted": False,
    "eventual_critical_infinite_history_constructed": False,
    "C058_refuted": False,
    "Q1_Q2_resolved": False,
    "publication_novelty_or_prize_claimed": False,
}

TOP_KEYS = {
    "schema", "status", "base_certificate", "prototype", "coefficient_box",
    "refinement", "conclusion", "scope", "integrity",
}
BASE_KEYS = {"file", "file_sha256", "payload_sha256"}
REFINEMENT_KEYS = {
    "selected_chambers", "subdivisions_in_reciprocal_coordinate", "pieces",
}
PIECE_KEYS = {"chamber", "piece", "left", "right", "Dc4", "Do4", "Dc8", "Do8", "n4", "n8"}
EPOCH_KEYS = {"denominator", "weights", "objective"}
INTEGRITY_KEYS = {
    "algorithm", "payload_sha256", "source_refinement_sha256",
    "refinement_payload_sha256",
    "exact_replay_arithmetic",
}


class CertificateError(RuntimeError):
    """Raised for a schema, provenance, arithmetic, PSD, or scope failure."""


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
        raise CertificateError(
            f"{label}: schema keys differ; missing={sorted(expected-set(value))}, "
            f"extra={sorted(set(value)-expected)}"
        )
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


def _object_hash(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def _load_canonical(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CertificateError(f"certificate is not canonical UTF-8 JSON: {exc}") from exc
    if type(value) is not dict or raw != rendered_bytes(value):
        raise CertificateError("certificate bytes are not canonical JSON")
    return value


def _load_and_validate_base(reference: Mapping[str, Any]) -> dict[str, Any]:
    checked = _exact_keys(reference, BASE_KEYS, "base_certificate")
    if checked != EXPECTED_BASE:
        raise CertificateError("base certificate reference changed")
    path = HERE / checked["file"]
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != checked["file_sha256"]:
        raise CertificateError("base certificate file sha256 mismatch")
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CertificateError(f"base certificate is not UTF-8 JSON: {exc}") from exc
    if type(value) is not dict or raw != base.rendered_bytes(value):
        raise CertificateError("base certificate bytes are not canonical")
    # This validates the base payload hash and its complete strict schema.  The
    # hybrid replay below independently replays exactly the 82 retained duals.
    base._validate_static(value)
    if value["integrity"]["payload_sha256"] != checked["payload_sha256"]:
        raise CertificateError("base certificate payload sha256 mismatch")
    return value


def _log_interval(value: F, terms: int = LOG_TERMS) -> tuple[F, F]:
    if value < 1 or terms <= 0:
        raise ValueError("log enclosure requires value >= 1 and positive terms")
    z = (value - 1) / (value + 1)
    lower = 2 * sum(
        (z ** (2 * index + 1) / (2 * index + 1) for index in range(terms)),
        F(0),
    )
    tail = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return lower, lower + tail


def _split_reciprocal(left: F, right: F) -> tuple[F, ...]:
    reciprocal_left = F(1, left)
    reciprocal_right = F(1, right)
    return tuple(
        F(1, reciprocal_left + (reciprocal_right - reciprocal_left) * index / SUBDIVISIONS)
        for index in range(SUBDIVISIONS + 1)
    )


def _piece_interval(record: Mapping[str, Any]) -> tuple[F, F]:
    left = _fraction(record["left"], "piece.left")
    right = _fraction(record["right"], "piece.right")
    objective4 = _fraction(record["n4"]["objective"], "piece.n4.objective")
    objective8 = _fraction(record["n8"]["objective"], "piece.n8.objective")
    dc4 = _fraction(record["Dc4"], "piece.Dc4")
    do4 = _fraction(record["Do4"], "piece.Do4")
    dc8 = _fraction(record["Dc8"], "piece.Dc8")
    do8 = _fraction(record["Do8"], "piece.Do8")
    log_coefficient = 2 * (dc4 + RHO * dc8) - (objective4 + RHO * objective8)
    reciprocal_coefficient = 2 * (do4 + RHO * do8)
    log_lower, log_upper = _log_interval(right / left)
    reciprocal = reciprocal_coefficient * (F(1, left) - F(1, right))
    if log_coefficient >= 0:
        return (
            log_coefficient * log_lower + reciprocal,
            log_coefficient * log_upper + reciprocal,
        )
    return (
        log_coefficient * log_upper + reciprocal,
        log_coefficient * log_lower + reciprocal,
    )


def _prototype_interval() -> tuple[F, F]:
    eta_lower, eta_upper = _log_interval(F(1768, 1659))
    constant = EPSILON - B_COEFFICIENT * DELTA_V
    return (
        (constant + A_COEFFICIENT * eta_lower) / 3 - E2,
        (constant + A_COEFFICIENT * eta_upper) / 3 - E2,
    )


def _validate_static(
    value: Mapping[str, Any], *, check_hash: bool = True,
) -> dict[str, Any]:
    payload = _exact_keys(value, TOP_KEYS, "payload")
    if payload["schema"] != SCHEMA or payload["status"] != STATUS:
        raise CertificateError("schema or status mismatch")
    base_value = _load_and_validate_base(payload["base_certificate"])
    if _exact_keys(payload["prototype"], set(EXPECTED_PROTOTYPE), "prototype") != EXPECTED_PROTOTYPE:
        raise CertificateError("prototype constants changed")
    if _exact_keys(payload["coefficient_box"], set(EXPECTED_BOX), "coefficient_box") != EXPECTED_BOX:
        raise CertificateError("coefficient box changed")

    refinement = _exact_keys(payload["refinement"], REFINEMENT_KEYS, "refinement")
    if refinement["selected_chambers"] != list(SELECTED_CHAMBERS):
        raise CertificateError("selected chamber list changed")
    if refinement["subdivisions_in_reciprocal_coordinate"] != SUBDIVISIONS:
        raise CertificateError("subdivision count changed")
    pieces = refinement["pieces"]
    if type(pieces) is not list or len(pieces) != len(SELECTED_CHAMBERS) * SUBDIVISIONS:
        raise CertificateError("refined piece count changed")
    breakpoints = base._breakpoints()
    expected_order = [
        (chamber, piece)
        for chamber in SELECTED_CHAMBERS
        for piece in range(SUBDIVISIONS)
    ]
    for record, (chamber, piece) in zip(pieces, expected_order):
        checked = _exact_keys(record, PIECE_KEYS, f"pieces[{chamber},{piece}]")
        if checked["chamber"] != chamber or checked["piece"] != piece:
            raise CertificateError("refined piece order changed")
        endpoints = _split_reciprocal(breakpoints[chamber], breakpoints[chamber + 1])
        if checked["left"] != ftext(endpoints[piece]) or checked["right"] != ftext(endpoints[piece + 1]):
            raise CertificateError("refined piece is not the exact equal-reciprocal split")
        for coefficient in ("Dc4", "Do4", "Dc8", "Do8"):
            _fraction(checked[coefficient], f"piece.{coefficient}")
        for epoch_key in ("n4", "n8"):
            epoch = _exact_keys(checked[epoch_key], EPOCH_KEYS, f"piece.{epoch_key}")
            _exact_int(epoch["denominator"], "dual denominator", minimum=1)
            weights = epoch["weights"]
            if type(weights) is not list or len(weights) != 308:
                raise CertificateError("dual weight count changed")
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
    if integrity["source_refinement_sha256"] != SOURCE_REFINEMENT_SHA256:
        raise CertificateError("source refinement sha256 changed")
    if (
        integrity["refinement_payload_sha256"] != REFINEMENT_PAYLOAD_SHA256
        or _object_hash(refinement) != REFINEMENT_PAYLOAD_SHA256
    ):
        raise CertificateError("canonical refinement payload sha256 mismatch")
    if integrity["exact_replay_arithmetic"] != (
        "fractions.Fraction plus fraction-free integer Bareiss/Sylvester"
    ):
        raise CertificateError("exact replay arithmetic label changed")
    for key in ("payload_sha256", "source_refinement_sha256", "refinement_payload_sha256"):
        digest = integrity[key]
        if type(digest) is not str or re.fullmatch(r"[0-9a-f]{64}", digest) is None:
            raise CertificateError(f"{key}: invalid sha256")
    if check_hash and integrity["payload_sha256"] != payload_hash(payload):
        raise CertificateError("payload sha256 mismatch")
    return base_value


def _replay_dual(
    record: Mapping[str, Any], epoch: int,
) -> tuple[F, F, F, int]:
    left = _fraction(record["left"], "dual.left")
    right = _fraction(record["right"], "dual.right")
    epoch_record = record[f"n{epoch}"]
    denominator = epoch_record["denominator"]
    weights = epoch_record["weights"]
    hc, ho, weighted_rows, dc, do, objective = base._epoch_reconstruction(
        left, right, epoch, denominator, weights
    )
    if dc != _fraction(record[f"Dc{epoch}"], f"dual.Dc{epoch}"):
        raise CertificateError("dual Dc coefficient mismatch")
    if do != _fraction(record[f"Do{epoch}"], f"dual.Do{epoch}"):
        raise CertificateError("dual Do coefficient mismatch")
    if objective != _fraction(epoch_record["objective"], "dual objective"):
        raise CertificateError("dual objective mismatch")
    endpoint_checks = 0
    for endpoint in (left, right):
        integer_slack = base._integer_slack(
            hc, ho, weighted_rows, denominator, endpoint
        )
        if not base._bareiss_positive_definite(integer_slack):
            raise CertificateError("dual endpoint slack is not positive definite")
        endpoint_checks += 1
    return dc, do, objective, endpoint_checks


_REPLAY_CACHE: dict[str, dict[str, Any]] = {}


def _replay_validated(
    value: Mapping[str, Any], base_value: Mapping[str, Any],
) -> dict[str, Any]:
    digest = value["integrity"]["payload_sha256"]
    cached = _REPLAY_CACHE.get(digest)
    if cached is not None:
        return dict(cached)

    raw_lower = raw_upper = F(0)
    phase_pieces = epoch_duals = weights_replayed = endpoint_checks = 0
    selected = set(SELECTED_CHAMBERS)
    for record in base_value["dual_certificate"]["chambers"]:
        if record["index"] in selected:
            continue
        for epoch in (4, 8):
            _, _, _, checks = _replay_dual(record, epoch)
            endpoint_checks += checks
            epoch_duals += 1
            weights_replayed += len(record[f"n{epoch}"]["weights"])
        lower, upper = _piece_interval(record)
        raw_lower += lower
        raw_upper += upper
        phase_pieces += 1

    for record in value["refinement"]["pieces"]:
        for epoch in (4, 8):
            _, _, _, checks = _replay_dual(record, epoch)
            endpoint_checks += checks
            epoch_duals += 1
            weights_replayed += len(record[f"n{epoch}"]["weights"])
        lower, upper = _piece_interval(record)
        raw_lower += lower
        raw_upper += upper
        phase_pieces += 1

    if (phase_pieces, epoch_duals, weights_replayed, endpoint_checks) != (102, 204, 62_832, 408):
        raise CertificateError("hybrid replay census changed")
    log2_lower, log2_upper = _log_interval(F(2))
    if not raw_lower <= raw_upper < 0:
        raise CertificateError("hybrid raw integral does not have the expected sign")
    # Both numerator endpoints are negative.
    normalized_lower = raw_lower / log2_lower
    normalized_upper = raw_upper / log2_upper
    prototype_lower, prototype_upper = _prototype_interval()
    coefficient_box_rhs_lower = -DELTA_V / 9
    coefficient_box_gap = coefficient_box_rhs_lower - normalized_upper
    if not (
        normalized_lower <= normalized_upper < NORMALIZED_BARRIER
        < prototype_lower <= prototype_upper
        and prototype_lower - normalized_upper > PROTOTYPE_SEPARATION
    ):
        raise CertificateError("fixed-prototype exact separation failed")
    if not (
        coefficient_box_rhs_lower > NORMALIZED_BARRIER + BOX_SEPARATION
        and coefficient_box_gap > BOX_SEPARATION
        and NECESSARY_B_LOWER_BARRIER == F(287434930599, 860203021250)
        and NECESSARY_B_LOWER_BARRIER > F(1, 3)
    ):
        raise CertificateError("coefficient-box exact separation failed")

    summary = {
        "hybrid_phase_pieces": phase_pieces,
        "untouched_base_chambers": 82,
        "refined_original_chambers": 5,
        "refined_phase_pieces": 20,
        "epoch_duals_replayed": epoch_duals,
        "dual_weights_replayed": weights_replayed,
        "endpoint_ldl_checks": endpoint_checks,
        "raw_integral_lower": raw_lower,
        "raw_integral_upper": raw_upper,
        "normalized_lower": normalized_lower,
        "normalized_upper": normalized_upper,
        "prototype_rhs_lower": prototype_lower,
        "prototype_rhs_upper": prototype_upper,
        "prototype_gap_lower_bound": prototype_lower - normalized_upper,
        "coefficient_box_rhs_lower": coefficient_box_rhs_lower,
        "coefficient_box_gap_lower_bound": coefficient_box_gap,
        "necessary_B_lower_barrier": NECESSARY_B_LOWER_BARRIER,
        "all_weights_nonnegative": True,
        "all_endpoint_slacks_positive_definite": True,
        "fixed_C118_storage_prototype_refuted": True,
        "nonnegative_epsilon_A_and_B_at_most_one_third_refuted": True,
    }
    _REPLAY_CACHE[digest] = dict(summary)
    return summary


def replay_exact(value: Mapping[str, Any]) -> dict[str, Any]:
    """Replay the 102-piece hybrid dual and exact storage comparisons."""
    base_value = _validate_static(value)
    return _replay_validated(value, base_value)


def verify_certificate(value: Mapping[str, Any]) -> dict[str, Any]:
    """Strictly validate the payload and perform its exact replay."""
    base_value = _validate_static(value)
    return _replay_validated(value, base_value)


def build_certificate(path: Path = DEFAULT_CERTIFICATE) -> dict[str, Any]:
    value = _load_canonical(Path(path))
    verify_certificate(value)
    return value


def self_check(value: Mapping[str, Any]) -> dict[str, int]:
    """Require rejection of structural, arithmetic, provenance, and scope mutations."""
    verify_certificate(value)
    mutations: list[tuple[str, Any]] = []

    def add(label: str, mutator: Any) -> None:
        changed = copy.deepcopy(value)
        mutator(changed)
        changed["integrity"]["payload_sha256"] = payload_hash(changed)
        mutations.append((label, changed))

    add("schema", lambda x: x.__setitem__("schema", SCHEMA + ".mutated"))
    add("status", lambda x: x.__setitem__("status", "UNSOUND"))
    add("base-file", lambda x: x["base_certificate"].__setitem__("file", "other.json"))
    add("base-file-hash", lambda x: x["base_certificate"].__setitem__("file_sha256", "0" * 64))
    add("base-payload-hash", lambda x: x["base_certificate"].__setitem__("payload_sha256", "0" * 64))
    add("prototype", lambda x: x["prototype"].__setitem__("B", "1/4"))
    add("coefficient-box", lambda x: x["coefficient_box"].__setitem__("B_upper", "1/2"))
    add("selection", lambda x: x["refinement"]["selected_chambers"].__setitem__(0, 48))
    add("subdivision", lambda x: x["refinement"].__setitem__("subdivisions_in_reciprocal_coordinate", 8))
    add("piece-index", lambda x: x["refinement"]["pieces"][0].__setitem__("piece", 1))
    add("piece-endpoint", lambda x: x["refinement"]["pieces"][0].__setitem__("right", "1/1"))
    add("negative-weight", lambda x: x["refinement"]["pieces"][0]["n4"]["weights"].__setitem__(0, -1))
    add("weight-value", lambda x: x["refinement"]["pieces"][0]["n4"]["weights"].__setitem__(0, x["refinement"]["pieces"][0]["n4"]["weights"][0] + 1))
    add("short-weight-vector", lambda x: x["refinement"]["pieces"][0]["n8"]["weights"].pop())
    add("objective", lambda x: x["refinement"]["pieces"][0]["n4"].__setitem__("objective", "0/1"))
    add("conclusion", lambda x: x["conclusion"].__setitem__("fixed_C118_storage_prototype_refuted", False))
    add("scope", lambda x: x["scope"].__setitem__("C058_refuted", True))
    add("source-hash", lambda x: x["integrity"].__setitem__("source_refinement_sha256", "0" * 64))

    rejected = 0
    for label, mutation in mutations:
        try:
            verify_certificate(mutation)
        except (CertificateError, base.CertificateError):
            rejected += 1
        else:
            raise CertificateError(f"self-check mutation was accepted: {label}")
    return {"mutations_attempted": len(mutations), "mutations_rejected": rejected}


def _import_refinement(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != SOURCE_REFINEMENT_SHA256:
        raise CertificateError("source refinement file sha256 mismatch")
    try:
        source = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CertificateError(f"source refinement is not UTF-8 JSON: {exc}") from exc
    if source.get("schema") != "erdos1191.c118.subdivided.dual.disposable.v1":
        raise CertificateError("source refinement schema mismatch")
    if source.get("exact") is not True:
        raise CertificateError("source refinement is not exact")
    if source.get("selected_chambers") != list(SELECTED_CHAMBERS):
        raise CertificateError("source refinement chamber selection mismatch")
    if source.get("subdivisions_in_reciprocal_coordinate") != SUBDIVISIONS:
        raise CertificateError("source refinement subdivision mismatch")
    source_hash = source.get("payload_sha256_without_hash")
    source_without_hash = dict(source)
    source_without_hash.pop("payload_sha256_without_hash", None)
    if source_hash != hashlib.sha256(
        json.dumps(source_without_hash, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest():
        raise CertificateError("source refinement internal payload hash mismatch")

    pieces = []
    for record in source.get("records", []):
        piece = {
            key: record[key]
            for key in ("chamber", "piece", "left", "right", "Dc4", "Do4", "Dc8", "Do8")
        }
        for epoch_key in ("n4", "n8"):
            epoch = record[epoch_key]
            piece[epoch_key] = {
                "denominator": epoch["denominator"],
                "weights": epoch["weights"],
                "objective": epoch["objective"],
            }
        pieces.append(piece)
    pieces.sort(key=lambda item: (item["chamber"], item["piece"]))

    value: dict[str, Any] = {
        "schema": SCHEMA,
        "status": STATUS,
        "base_certificate": dict(EXPECTED_BASE),
        "prototype": dict(EXPECTED_PROTOTYPE),
        "coefficient_box": dict(EXPECTED_BOX),
        "refinement": {
            "selected_chambers": list(SELECTED_CHAMBERS),
            "subdivisions_in_reciprocal_coordinate": SUBDIVISIONS,
            "pieces": pieces,
        },
        "conclusion": dict(EXPECTED_CONCLUSION),
        "scope": dict(EXPECTED_SCOPE),
        "integrity": {
            "algorithm": "sha256",
            "payload_sha256": "",
            "source_refinement_sha256": SOURCE_REFINEMENT_SHA256,
            "refinement_payload_sha256": REFINEMENT_PAYLOAD_SHA256,
            "exact_replay_arithmetic": (
                "fractions.Fraction plus fraction-free integer Bareiss/Sylvester"
            ),
        },
    }
    value["integrity"]["payload_sha256"] = payload_hash(value)
    verify_certificate(value)
    return value


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--import-refinement", type=Path)
    parser.add_argument("--write", type=Path)
    args = parser.parse_args(argv)
    if args.import_refinement is not None:
        value = _import_refinement(args.import_refinement)
        destination = args.write or DEFAULT_CERTIFICATE
        destination.write_bytes(rendered_bytes(value))
    else:
        value = _load_canonical(args.verify)
    summary = verify_certificate(value)
    mutations = self_check(value) if args.self_check else {"mutations_rejected": 0}
    print(
        "VERIFY_OK",
        f"hybrid_phase_pieces={summary['hybrid_phase_pieces']}",
        f"epoch_duals={summary['epoch_duals_replayed']}",
        f"weights={summary['dual_weights_replayed']}",
        f"endpoint_ldl_checks={summary['endpoint_ldl_checks']}",
        "normalized_upper<-83/2000",
        "coefficient_box_B<=1/3_refuted_exactly",
        "prototype_refuted_exactly",
        f"mutations_rejected={mutations['mutations_rejected']}",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
