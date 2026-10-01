#!/usr/bin/env python3
"""Exact two-row outer bank for the scalar C119 storage coefficient.

The positive-Delta-V C118 row supplies the C121 necessary lower bound on B.
An independently stored complete-phase dual bank for the negative-Delta-V
C120 row supplies a necessary upper bound.  Both are replayed exactly with
``fractions.Fraction`` and fraction-free integer positive-definiteness checks.

The resulting interval is nonempty.  This is a finite coefficient narrowing,
not a contradiction, a C058 resolution, or a claim about larger cones.
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
from typing import Any, Mapping, Sequence


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import ROUTE_C_C118_SUBDIVIDED_STORAGE_NO_GO_certificate as c121
import ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate as c120


DEFAULT_CERTIFICATE = HERE / "ROUTE_C_C122_TWO_ROW_SCALAR_STORAGE_BANK_certificate.json"
C120_DUAL_SOURCE = HERE / "ROUTE_C_C122_TWO_ROW_SCALAR_STORAGE_BANK_source.json"
C121_CERTIFICATE = HERE / "ROUTE_C_C118_SUBDIVIDED_STORAGE_NO_GO_certificate.json"
C120_MODEL = HERE / "ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate.py"

SCHEMA = "erdos1191.c122.two_row_scalar_storage_bank.v1"
STATUS = "EXACT_FINITE_TWO_ROW_SCALAR_BANK_NONEMPTY_C058_OPEN"
C120_DUAL_SOURCE_SHA256 = "e059c6680e6d90702748bf547397f5cf9242d5d3164d7a22a32de7636ef9ee5a"
C120_DUAL_INTERNAL_SHA256 = "e1a83f5da119c1cdbeb9052e5f5af8709a79b27fc0e3bd8defa9bbbaba4ac49c"
C120_MODEL_SHA256 = "6e8d7e3f975e952442672cb1d18e4512d616f343bb4f6379ba0c8701cd996fe9"
C121_CERTIFICATE_SHA256 = "1288d87e095a47f9fdf679a40656bafdef4ad4b03150ccb3254b25b043937a0b"
C121_PAYLOAD_SHA256 = "ee4074acc3e57c5f7fe991a74b7f33ad2424631ec75b814ab0c70c80cde11cff"

RHO = F(9, 16)
C120_DELTA_V_ABS = F(443_620_417, 1_928_247_678)
NORMALIZED_UPPER_FENCE = F(19, 250)
NECESSARY_B_LOWER = F(287_434_930_599, 860_203_021_250)
COARSE_NECESSARY_B_UPPER = 3 * NORMALIZED_UPPER_FENCE / C120_DELTA_V_ABS
BANK_WIDTH = COARSE_NECESSARY_B_UPPER - NECESSARY_B_LOWER
CONTRADICTION_THRESHOLD = NECESSARY_B_LOWER * C120_DELTA_V_ABS / 3

EXPECTED_SOURCES = {
    "C118_C121_certificate": C121_CERTIFICATE.name,
    "C118_C121_certificate_sha256": C121_CERTIFICATE_SHA256,
    "C118_C121_payload_sha256": C121_PAYLOAD_SHA256,
    "C120_full_phase_dual": C120_DUAL_SOURCE.name,
    "C120_full_phase_dual_sha256": C120_DUAL_SOURCE_SHA256,
    "C120_full_phase_dual_internal_sha256": C120_DUAL_INTERNAL_SHA256,
    "C120_model": C120_MODEL.name,
    "C120_model_sha256": C120_MODEL_SHA256,
}
EXPECTED_REPLAY = {
    "reverse_phase_chambers": 161,
    "reverse_epoch_duals": 322,
    "reverse_endpoint_positive_definite_checks": 644,
    "reverse_normalized_upper_less_than": "19/250",
}
EXPECTED_CONSTRAINTS = {
    "assumptions": "epsilon>=0; A>=0; e2=0; common scalar B; both fixed rows use the stated independent epoch-block cone",
    "C118_necessary_B_greater_than": "287434930599/860203021250",
    "C120_necessary_B_less_than": "2892371517/2918555375",
    "coarse_open_interval_width": "13193055646707058533/20084401210083413750",
    "reverse_normalized_upper_needed_for_contradiction": "14168000419188271087/552894826111299052500",
    "barriers_contradict": False,
    "scalar_B_refuted_by_these_two_rows": False,
}
EXPECTED_SCOPE = {
    "fixed_C118_C120_two_row_bank_only": True,
    "rho_9_over_16_only": True,
    "independent_epoch_block_cone_only": True,
    "all_scalar_storage_coefficients_refuted": False,
    "larger_cone_refuted": False,
    "arbitrary_rank_proved": False,
    "global_owner_ledger_constructed": False,
    "C058_resolved": False,
    "Q1_Q2_resolved": False,
    "publication_novelty_or_prize_claimed": False,
}

TOP_KEYS = {"schema", "status", "sources", "replay", "constraints", "scope", "integrity"}
INTEGRITY_KEYS = {"algorithm", "payload_sha256", "exact_replay_arithmetic"}
SOURCE_TOP_KEYS = {
    "H2", "H3", "approximate_recomputed_numerator_upper", "base",
    "breakpoints", "certified_log_integral_numerator_upper_bound", "eta_ratio",
    "exact_recomputed_numerator_less_than_bound", "payload_sha256_without_hash",
    "points", "records", "rho", "schema", "scope", "strictly_negative",
}


class CertificateError(RuntimeError):
    """Raised for a schema, provenance, arithmetic, PSD, or scope failure."""


def ftext(value: F | int) -> str:
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


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


def expected_certificate() -> dict[str, Any]:
    value: dict[str, Any] = {
        "schema": SCHEMA,
        "status": STATUS,
        "sources": dict(EXPECTED_SOURCES),
        "replay": dict(EXPECTED_REPLAY),
        "constraints": dict(EXPECTED_CONSTRAINTS),
        "scope": dict(EXPECTED_SCOPE),
        "integrity": {
            "algorithm": "sha256",
            "payload_sha256": "",
            "exact_replay_arithmetic": "fractions.Fraction plus fraction-free integer Bareiss/Sylvester",
        },
    }
    value["integrity"]["payload_sha256"] = payload_hash(value)
    return value


def _exact_dict(value: object, keys: set[str], label: str) -> Mapping[str, Any]:
    if type(value) is not dict or set(value) != keys:
        raise CertificateError(f"{label}: schema keys differ")
    return value


def _read_pinned_json(path: Path, expected_sha256: str, label: str) -> tuple[bytes, dict[str, Any]]:
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected_sha256:
        raise CertificateError(f"{label}: file sha256 mismatch")
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CertificateError(f"{label}: invalid UTF-8 JSON: {exc}") from exc
    if type(value) is not dict:
        raise CertificateError(f"{label}: expected object")
    return raw, value


def _validate_static(value: Mapping[str, Any]) -> None:
    _exact_dict(value, TOP_KEYS, "top")
    if value["schema"] != SCHEMA or value["status"] != STATUS:
        raise CertificateError("schema or status changed")
    if value["sources"] != EXPECTED_SOURCES:
        raise CertificateError("source provenance changed")
    if value["replay"] != EXPECTED_REPLAY:
        raise CertificateError("replay statement changed")
    if value["constraints"] != EXPECTED_CONSTRAINTS:
        raise CertificateError("constraint statement changed")
    if value["scope"] != EXPECTED_SCOPE:
        raise CertificateError("scope changed")
    integrity = _exact_dict(value["integrity"], INTEGRITY_KEYS, "integrity")
    if integrity["algorithm"] != "sha256" or integrity["payload_sha256"] != payload_hash(value):
        raise CertificateError("payload integrity mismatch")
    if integrity["exact_replay_arithmetic"] != "fractions.Fraction plus fraction-free integer Bareiss/Sylvester":
        raise CertificateError("arithmetic statement changed")


_REPLAY_CACHE: dict[str, dict[str, Any]] = {}


def _replay_sources() -> dict[str, Any]:
    digest = C120_DUAL_SOURCE_SHA256 + C121_CERTIFICATE_SHA256
    if digest in _REPLAY_CACHE:
        return dict(_REPLAY_CACHE[digest])

    if hashlib.sha256(C120_MODEL.read_bytes()).hexdigest() != C120_MODEL_SHA256:
        raise CertificateError("C120 model source sha256 mismatch")

    _, reverse = _read_pinned_json(
        C120_DUAL_SOURCE, C120_DUAL_SOURCE_SHA256, "C120 full-phase dual"
    )
    if set(reverse) != SOURCE_TOP_KEYS:
        raise CertificateError("C120 dual source schema keys differ")
    if reverse["schema"] != "erdos1191.c058_eta_negative_full_phase_dual.discovery.v1":
        raise CertificateError("C120 dual source schema changed")
    without_hash = dict(reverse)
    internal = without_hash.pop("payload_sha256_without_hash")
    if internal != C120_DUAL_INTERNAL_SHA256 or _object_hash(without_hash) != internal:
        raise CertificateError("C120 dual source internal hash mismatch")
    if tuple(reverse["points"]) != c120.POINTS or F(reverse["rho"]) != RHO:
        raise CertificateError("C120 fixture changed")

    breakpoints = tuple(F(text) for text in reverse["breakpoints"])
    if breakpoints != c120._breakpoints() or len(breakpoints) != 162:
        raise CertificateError("C120 breakpoint partition changed")
    records = reverse["records"]
    if type(records) is not list or len(records) != 161:
        raise CertificateError("C120 chamber count changed")

    raw_lower = F()
    raw_upper = F()
    dual_count = 0
    endpoint_pd_count = 0
    for index, (record, left, right) in enumerate(zip(records, breakpoints, breakpoints[1:])):
        if record["index"] != index or F(record["left"]) != left or F(record["right"]) != right:
            raise CertificateError(f"C120 chamber {index}: interval changed")
        for epoch, key in ((4, "n4"), (8, "n8")):
            dual = record[key]
            denominator = int(dual["denominator"])
            weights = tuple(int(weight) for weight in dual["weights"])
            if denominator <= 0 or len(weights) != 308 or min(weights) < 0:
                raise CertificateError(f"C120 chamber {index}, epoch {epoch}: dual data")
            hc, ho, weighted, dc, do, objective = c120._dual_epoch_reconstruction(
                left, right, epoch, denominator, weights
            )
            if dc != F(record[f"Dc{epoch}"]) or do != F(record[f"Do{epoch}"]):
                raise CertificateError(f"C120 chamber {index}, epoch {epoch}: demand")
            if objective != F(dual["objective"]):
                raise CertificateError(f"C120 chamber {index}, epoch {epoch}: objective")
            for endpoint in (left, right):
                slack = c120._integer_slack(hc, ho, weighted, denominator, endpoint)
                if not c120._bareiss_positive_definite(slack):
                    raise CertificateError(
                        f"C120 chamber {index}, epoch {epoch}: endpoint slack not PD"
                    )
                endpoint_pd_count += 1
            dual_count += 1
        lower, upper = c120._dual_piece_interval(record)
        raw_lower += lower
        raw_upper += upper

    log2_lower, log2_upper = c120._log_interval(F(2))
    normalized_lower = raw_lower / log2_upper
    normalized_upper = raw_upper / log2_lower
    if not normalized_lower <= normalized_upper < NORMALIZED_UPPER_FENCE:
        raise CertificateError("C120 normalized upper fence failed")

    _, c121_value = _read_pinned_json(
        C121_CERTIFICATE, C121_CERTIFICATE_SHA256, "C121 certificate"
    )
    c121_summary = c121.verify_certificate(c121_value)
    necessary_lower = c121_summary["necessary_B_lower_barrier"]
    if necessary_lower != NECESSARY_B_LOWER:
        raise CertificateError("C121 necessary lower barrier changed")
    if COARSE_NECESSARY_B_UPPER != F(2_892_371_517, 2_918_555_375):
        raise CertificateError("C120 coarse upper arithmetic changed")
    if BANK_WIDTH != F(13_193_055_646_707_058_533, 20_084_401_210_083_413_750):
        raise CertificateError("two-row interval width changed")
    if CONTRADICTION_THRESHOLD != F(
        14_168_000_419_188_271_087, 552_894_826_111_299_052_500
    ):
        raise CertificateError("contradiction threshold changed")

    summary = {
        "reverse_phase_chambers": len(records),
        "reverse_epoch_duals_replayed": dual_count,
        "reverse_endpoint_ldl_checks": endpoint_pd_count,
        "reverse_raw_lower": raw_lower,
        "reverse_raw_upper": raw_upper,
        "reverse_normalized_lower": normalized_lower,
        "reverse_normalized_upper": normalized_upper,
        "necessary_B_lower": necessary_lower,
        "coarse_necessary_B_upper": COARSE_NECESSARY_B_UPPER,
        "coarse_open_interval_width": BANK_WIDTH,
        "reverse_normalized_upper_needed_for_contradiction": CONTRADICTION_THRESHOLD,
        "barriers_contradict": COARSE_NECESSARY_B_UPPER <= necessary_lower,
    }
    if summary["barriers_contradict"]:
        raise CertificateError("stored noncontradiction statement is false")
    _REPLAY_CACHE[digest] = dict(summary)
    return summary


def replay_exact(value: Mapping[str, Any]) -> dict[str, Any]:
    _validate_static(value)
    return _replay_sources()


def verify_certificate(value: Mapping[str, Any]) -> dict[str, Any]:
    return replay_exact(value)


def _load(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CertificateError(f"certificate: invalid UTF-8 JSON: {exc}") from exc
    if type(value) is not dict or raw != rendered_bytes(value):
        raise CertificateError("certificate is not in canonical rendering")
    return value


def build_certificate(path: Path = DEFAULT_CERTIFICATE) -> dict[str, Any]:
    value = _load(Path(path))
    verify_certificate(value)
    return value


def self_check(value: Mapping[str, Any]) -> dict[str, int]:
    verify_certificate(value)
    mutations: list[tuple[str, dict[str, Any]]] = []

    def add(label: str, mutate: Any) -> None:
        changed = copy.deepcopy(value)
        mutate(changed)
        changed["integrity"]["payload_sha256"] = payload_hash(changed)
        mutations.append((label, changed))

    add("schema", lambda x: x.__setitem__("schema", SCHEMA + ".mutated"))
    add("status", lambda x: x.__setitem__("status", "UNSOUND"))
    add("C120-source-hash", lambda x: x["sources"].__setitem__("C120_full_phase_dual_sha256", "0" * 64))
    add("C121-payload-hash", lambda x: x["sources"].__setitem__("C118_C121_payload_sha256", "0" * 64))
    add("dual-count", lambda x: x["replay"].__setitem__("reverse_epoch_duals", 321))
    add("lower-barrier", lambda x: x["constraints"].__setitem__("C118_necessary_B_greater_than", "1/3"))
    add("false-contradiction", lambda x: x["constraints"].__setitem__("barriers_contradict", True))
    add("scope-C058", lambda x: x["scope"].__setitem__("C058_resolved", True))
    add("scope-all-B", lambda x: x["scope"].__setitem__("all_scalar_storage_coefficients_refuted", True))

    rejected = 0
    for label, changed in mutations:
        try:
            verify_certificate(changed)
        except (CertificateError, c120.CertificateError, c121.CertificateError):
            rejected += 1
        else:
            raise CertificateError(f"self-check mutation was accepted: {label}")
    return {"mutations_attempted": len(mutations), "mutations_rejected": rejected}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args(argv)
    value = _load(args.verify)
    summary = verify_certificate(value)
    mutations = self_check(value) if args.self_check else {"mutations_rejected": 0}
    print(
        "VERIFY_OK",
        f"reverse_phase_chambers={summary['reverse_phase_chambers']}",
        f"reverse_epoch_duals={summary['reverse_epoch_duals_replayed']}",
        f"reverse_endpoint_ldl_checks={summary['reverse_endpoint_ldl_checks']}",
        "C118_B_lower>1/3",
        "C120_B_upper<2892371517/2918555375",
        f"barriers_contradict={summary['barriers_contradict']}",
        f"mutations_rejected={mutations['mutations_rejected']}",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
