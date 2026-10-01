#!/usr/bin/env python3
"""Exact full-phase dual for the best screened C120 gap permutation.

The fixture keeps the C120 old-gap and new-gap multisets but changes their
orders.  Stored rational duals are replayed on every exact phase chamber and
at both endpoints.  Together with a clean exact C121 lower fence, this row
narrows a common scalar storage coefficient to a nonempty open interval.
"""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from typing import Any, Mapping, Sequence


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import ROUTE_C_C118_SUBDIVIDED_STORAGE_NO_GO_certificate as c121


DEFAULT_CERTIFICATE = HERE / "ROUTE_C_C123_ORDERED_PERMUTATION_FULL_PHASE_DUAL_certificate.json"
PERMUTATION_SOURCE = HERE / "ROUTE_C_C123_ORDERED_PERMUTATION_FULL_PHASE_DUAL_source.json"
C121_CERTIFICATE = HERE / "ROUTE_C_C118_SUBDIVIDED_STORAGE_NO_GO_certificate.json"
C120_MODEL_SOURCE = HERE / "ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate.py"

SCHEMA = "erdos1191.c123.ordered_permutation_full_phase_dual.v1"
STATUS = "EXACT_FINITE_ORDERED_PERMUTATION_SCALAR_BANK_NARROWING_C058_OPEN"
PERMUTATION_SOURCE_SHA256 = "85951114431d84b327b976b8ccc914068181f64302b3c308470be9b419a398f5"
PERMUTATION_INTERNAL_SHA256 = "2e27fdcb950b3bd5de025b8364edcfcafe93bef33cb8370bc70a893876b071ba"
C120_MODEL_SHA256 = "6e8d7e3f975e952442672cb1d18e4512d616f343bb4f6379ba0c8701cd996fe9"
C121_CERTIFICATE_SHA256 = "1288d87e095a47f9fdf679a40656bafdef4ad4b03150ccb3254b25b043937a0b"
C121_PAYLOAD_SHA256 = "ee4074acc3e57c5f7fe991a74b7f33ad2424631ec75b814ab0c70c80cde11cff"

POINTS = (0, 22, 60, 83, 154, 284, 494, 513, 575, 620, 711, 777, 880, 989, 1100, 1169)
C120_POINTS = (0, 22, 60, 83, 102, 173, 303, 513, 616, 727, 772, 881, 972, 1041, 1103, 1169)
PREFIX_GAPS = (22, 38, 23)
OLD_GAPS = (71, 130, 210, 19)
NEW_GAPS = (62, 45, 91, 66, 103, 109, 111, 69)
C120_OLD_GAPS = (19, 71, 130, 210)
C120_NEW_GAPS = (103, 111, 45, 109, 91, 69, 62, 66)
RHO = F(9, 16)
PHASE_LOWER = F(297, 4)
PHASE_UPPER = F(297, 2)
DELTA_V = -F(443_620_417, 1_928_247_678)

CLEAN_B_LOWER = F(1341, 4000)
CLEAN_B_UPPER = F(4753, 10000)
CLEAN_INTERVAL_WIDTH = CLEAN_B_UPPER - CLEAN_B_LOWER
C121_NORMALIZED_UPPER_FENCE = -F(102_536_200_133, 2_462_628_588_800)
PERMUTATION_NORMALIZED_UPPER_FENCE = CLEAN_B_UPPER * abs(DELTA_V) / 3

EXPECTED_FIXTURE = {
    "points": list(POINTS),
    "old_gaps": list(OLD_GAPS),
    "new_gaps": list(NEW_GAPS),
    "same_old_gap_multiset_as_C120": sorted(OLD_GAPS) == sorted(C120_OLD_GAPS),
    "same_new_gap_multiset_as_C120": sorted(NEW_GAPS) == sorted(C120_NEW_GAPS),
    "different_order_from_C120": POINTS != C120_POINTS,
    "H2": 430,
    "H3": 656,
    "eta_ratio": "82/215",
    "delta_V": "-443620417/1928247678",
    "phase": ["297/4", "297/2"],
    "rho": "9/16",
}
EXPECTED_SOURCES = {
    "permutation_dual": PERMUTATION_SOURCE.name,
    "permutation_dual_sha256": PERMUTATION_SOURCE_SHA256,
    "permutation_dual_internal_sha256": PERMUTATION_INTERNAL_SHA256,
    "C120_model": C120_MODEL_SOURCE.name,
    "C120_model_sha256": C120_MODEL_SHA256,
    "C121_certificate": C121_CERTIFICATE.name,
    "C121_certificate_sha256": C121_CERTIFICATE_SHA256,
    "C121_payload_sha256": C121_PAYLOAD_SHA256,
}
EXPECTED_REPLAY = {
    "phase_chambers": 140,
    "epoch_duals": 280,
    "dual_weights": 86240,
    "endpoint_positive_definite_checks": 560,
    "normalized_upper_less_than": "301218263143/8263918620000",
}
EXPECTED_CONSTRAINTS = {
    "assumptions": "epsilon>=0; A>=0; e2=0; common scalar B; fixed C118 and ordered-permutation rows in the stated independent epoch-block cone",
    "C121_clean_necessary_B_greater_than": "1341/4000",
    "ordered_permutation_clean_necessary_B_less_than": "4753/10000",
    "clean_open_interval_width": "2801/20000",
    "barriers_contradict": False,
    "all_scalar_B_refuted": False,
}
EXPECTED_SCOPE = {
    "fixed_ordered_permutation_16_mark_row_only": True,
    "same_multisets_order_sensitivity_certified": True,
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

TOP_KEYS = {"schema", "status", "fixture", "sources", "replay", "constraints", "scope", "integrity"}
INTEGRITY_KEYS = {"algorithm", "payload_sha256", "exact_replay_arithmetic"}
SOURCE_TOP_KEYS = {
    "H2", "H3", "approximate_recomputed_numerator_upper", "base",
    "breakpoints", "certified_log_integral_numerator_upper_bound", "eta_ratio",
    "exact_recomputed_numerator_less_than_bound", "payload_sha256_without_hash",
    "points", "records", "rho", "schema", "scope", "strictly_negative",
}


class CertificateError(RuntimeError):
    """Raised for a schema, provenance, arithmetic, PSD, or scope failure."""


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
        "fixture": copy.deepcopy(EXPECTED_FIXTURE),
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


def _read_json(path: Path, expected_sha: str, label: str) -> tuple[bytes, dict[str, Any]]:
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected_sha:
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
    if value["fixture"] != EXPECTED_FIXTURE:
        raise CertificateError("fixture statement changed")
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


def _load_fresh_model() -> Any:
    raw = C120_MODEL_SOURCE.read_bytes()
    if hashlib.sha256(raw).hexdigest() != C120_MODEL_SHA256:
        raise CertificateError("C120 model source sha256 mismatch")
    spec = importlib.util.spec_from_file_location("c123_permutation_model", C120_MODEL_SOURCE)
    if spec is None or spec.loader is None:
        raise CertificateError("cannot load C120 exact model")
    model = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(model)
    model.POINTS = POINTS
    model.PHASE_LOWER = PHASE_LOWER
    model.PHASE_UPPER = PHASE_UPPER
    model.CHANNELS = tuple(
        (rank, multiplier, POINTS[rank])
        for multiplier in model.MULTIPLIERS
        for rank in range(3, 16)
    )
    model.EVENT_LINES = tuple(
        sorted({
            (origin, shift * multiplier)
            for _, multiplier, origin in model.CHANNELS
            for shift in (0, 1, 2)
        })
    )
    model.EPOCH4_INDICES = tuple(
        i for i, (rank, _, _) in enumerate(model.CHANNELS) if rank <= 7
    )
    model.EPOCH8_INDICES = tuple(
        i for i, (rank, _, _) in enumerate(model.CHANNELS) if rank >= 8
    )
    return model


_REPLAY_CACHE: dict[str, dict[str, Any]] = {}


def _replay_sources() -> dict[str, Any]:
    digest = PERMUTATION_SOURCE_SHA256 + C121_CERTIFICATE_SHA256
    if digest in _REPLAY_CACHE:
        return dict(_REPLAY_CACHE[digest])

    model = _load_fresh_model()
    _, source = _read_json(PERMUTATION_SOURCE, PERMUTATION_SOURCE_SHA256, "permutation dual")
    if set(source) != SOURCE_TOP_KEYS:
        raise CertificateError("permutation source schema keys differ")
    if source["schema"] != "erdos1191.c058_eta_negative_full_phase_dual.discovery.v1":
        raise CertificateError("permutation source schema changed")
    without_hash = dict(source)
    internal = without_hash.pop("payload_sha256_without_hash")
    if internal != PERMUTATION_INTERNAL_SHA256 or _object_hash(without_hash) != internal:
        raise CertificateError("permutation source internal hash mismatch")
    if tuple(source["points"]) != POINTS or F(source["rho"]) != RHO:
        raise CertificateError("permutation fixture changed")
    if source["H2"] != 430 or source["H3"] != 656 or source["eta_ratio"] != "82/215":
        raise CertificateError("permutation scalar profile changed")

    breakpoints = tuple(F(text) for text in source["breakpoints"])
    if breakpoints != model._breakpoints() or len(breakpoints) != 141:
        raise CertificateError("permutation breakpoint partition changed")
    records = source["records"]
    if type(records) is not list or len(records) != 140:
        raise CertificateError("permutation chamber count changed")

    raw_lower = F()
    raw_upper = F()
    dual_count = 0
    weight_count = 0
    endpoint_pd_count = 0
    for index, (record, left, right) in enumerate(zip(records, breakpoints, breakpoints[1:])):
        if record["index"] != index or F(record["left"]) != left or F(record["right"]) != right:
            raise CertificateError(f"chamber {index}: interval changed")
        for epoch, key in ((4, "n4"), (8, "n8")):
            dual = record[key]
            denominator = int(dual["denominator"])
            weights = tuple(int(weight) for weight in dual["weights"])
            if denominator <= 0 or len(weights) != 308 or min(weights) < 0:
                raise CertificateError(f"chamber {index}, epoch {epoch}: dual data")
            hc, ho, weighted, dc, do, objective = model._dual_epoch_reconstruction(
                left, right, epoch, denominator, weights
            )
            if dc != F(record[f"Dc{epoch}"]) or do != F(record[f"Do{epoch}"]):
                raise CertificateError(f"chamber {index}, epoch {epoch}: demand")
            if objective != F(dual["objective"]):
                raise CertificateError(f"chamber {index}, epoch {epoch}: objective")
            for endpoint in (left, right):
                slack = model._integer_slack(hc, ho, weighted, denominator, endpoint)
                if not model._bareiss_positive_definite(slack):
                    raise CertificateError(
                        f"chamber {index}, epoch {epoch}: endpoint slack not positive definite"
                    )
                endpoint_pd_count += 1
            dual_count += 1
            weight_count += len(weights)
        lower, upper = model._dual_piece_interval(record)
        raw_lower += lower
        raw_upper += upper

    log2_lower, log2_upper = model._log_interval(F(2))
    normalized_lower = raw_lower / log2_upper
    normalized_upper = raw_upper / log2_lower
    if not normalized_lower <= normalized_upper < PERMUTATION_NORMALIZED_UPPER_FENCE:
        raise CertificateError("ordered-permutation normalized upper fence failed")

    _, c121_value = _read_json(C121_CERTIFICATE, C121_CERTIFICATE_SHA256, "C121 certificate")
    c121_summary = c121.verify_certificate(c121_value)
    if not c121_summary["normalized_upper"] < C121_NORMALIZED_UPPER_FENCE:
        raise CertificateError("C121 clean lower fence failed")
    if CLEAN_INTERVAL_WIDTH != F(2801, 20000):
        raise CertificateError("clean scalar interval width changed")

    summary = {
        "phase_chambers": len(records),
        "epoch_duals_replayed": dual_count,
        "dual_weights_replayed": weight_count,
        "endpoint_ldl_checks": endpoint_pd_count,
        "raw_lower": raw_lower,
        "raw_upper": raw_upper,
        "normalized_lower": normalized_lower,
        "normalized_upper": normalized_upper,
        "clean_necessary_B_lower": CLEAN_B_LOWER,
        "clean_necessary_B_upper": CLEAN_B_UPPER,
        "clean_open_interval_width": CLEAN_INTERVAL_WIDTH,
        "barriers_contradict": CLEAN_B_UPPER <= CLEAN_B_LOWER,
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
    add("point", lambda x: x["fixture"]["points"].__setitem__(4, 153))
    add("source-hash", lambda x: x["sources"].__setitem__("permutation_dual_sha256", "0" * 64))
    add("C121-hash", lambda x: x["sources"].__setitem__("C121_payload_sha256", "0" * 64))
    add("dual-count", lambda x: x["replay"].__setitem__("epoch_duals", 279))
    add("upper", lambda x: x["constraints"].__setitem__("ordered_permutation_clean_necessary_B_less_than", "1/2"))
    add("contradiction", lambda x: x["constraints"].__setitem__("barriers_contradict", True))
    add("scope-C058", lambda x: x["scope"].__setitem__("C058_resolved", True))
    add("scope-all-B", lambda x: x["scope"].__setitem__("all_scalar_storage_coefficients_refuted", True))

    rejected = 0
    for label, changed in mutations:
        try:
            verify_certificate(changed)
        except (CertificateError, c121.CertificateError):
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
        f"phase_chambers={summary['phase_chambers']}",
        f"epoch_duals={summary['epoch_duals_replayed']}",
        f"dual_weights={summary['dual_weights_replayed']}",
        f"endpoint_ldl_checks={summary['endpoint_ldl_checks']}",
        "clean_B_lower>1341/4000",
        "clean_B_upper<4753/10000",
        f"barriers_contradict={summary['barriers_contradict']}",
        f"mutations_rejected={mutations['mutations_rejected']}",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
