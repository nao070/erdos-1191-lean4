#!/usr/bin/env python3
"""Exact necessary-side audit of the C125 candidate on the C126 phase.

The verifier replays the pinned C126 common-phase dual certificate and checks
the C125 rational coefficient vector against the C120 and C123 dual upper
objectives.  It proves only that these two necessary-side upper certificates
do not separate the candidate.  It does not construct a primal witness or
prove a local or infinite master inequality.
"""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Mapping, Sequence


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import ROUTE_C_C125_ORDERED_SUFFIX_FIVE_ROW_BANK_certificate as c125
import ROUTE_C_C126_COMMON_COMPLETED_SHELL_PHASE_certificate as c126


DEFAULT_CERTIFICATE = HERE / "ROUTE_C_C127_COMMON_PHASE_ORDERED_CANDIDATE_certificate.json"
C126_CERTIFICATE = HERE / "ROUTE_C_C126_COMMON_COMPLETED_SHELL_PHASE_certificate.json"
C126_VERIFIER_SOURCE = HERE / "ROUTE_C_C126_COMMON_COMPLETED_SHELL_PHASE_certificate.py"
C125_VERIFIER_SOURCE = HERE / "ROUTE_C_C125_ORDERED_SUFFIX_FIVE_ROW_BANK_certificate.py"

SCHEMA = "erdos1191.c127.common_phase_ordered_candidate.v1"
STATUS = "EXACT_FINITE_COMMON_PHASE_ORDERED_CANDIDATE_NOT_SEPARATED_C058_OPEN"

C126_CERTIFICATE_SHA256 = "b1a37954b11a807161d85d916a875058d9a4dab51a5dc208468429fe937074cf"
C126_CERTIFICATE_PAYLOAD_SHA256 = "03a8df34c95e20b3e24d7d1a91d4de169136a699239c3b5f777a60916a1f1f86"
C126_VERIFIER_SHA256 = "830c6afa79d49d386e5bc57bdb5578b8074e783486cbaf991164ae25e91a5981"
C125_VERIFIER_SHA256 = "1d9f4d8ea7756eb89fa9e8cc5d44e15a6480057df82392afadd30cbcbcb48fe2"

PHASE_LOWER = F(82)
PHASE_UPPER = F(164)
RHO = F(9, 16)
CANDIDATE_EPSILON = F(1, 1000)
CANDIDATE_A = F(1, 1000)
CANDIDATE_B = F(1, 2)
CANDIDATE_C = F(1, 10)
CANDIDATE_E2 = F(0)
ABS_DELTA_V = F(443_620_417, 1_928_247_678)
DELTA_VRT_C120 = -F(13_171, 58_179)
DELTA_VRT_C123 = F(51_059, 581_790)
C120_MARGIN_FENCE = F(21, 500)
C123_MARGIN_FENCE = F(7, 1000)
COMMON_MARGIN_FENCE = F(1, 10_000)

EXPECTED_SOURCES = {
    "C126_common_phase_certificate": C126_CERTIFICATE.name,
    "C126_common_phase_certificate_sha256": C126_CERTIFICATE_SHA256,
    "C126_common_phase_certificate_payload_sha256": C126_CERTIFICATE_PAYLOAD_SHA256,
    "C126_common_phase_verifier": C126_VERIFIER_SOURCE.name,
    "C126_common_phase_verifier_sha256": C126_VERIFIER_SHA256,
    "C125_ordered_candidate_verifier": C125_VERIFIER_SOURCE.name,
    "C125_ordered_candidate_verifier_sha256": C125_VERIFIER_SHA256,
}
EXPECTED_REPLAY = {
    "common_phase": ["82/1", "164/1"],
    "rho": "9/16",
    "C120_phase_chambers": 147,
    "C120_epoch_duals": 294,
    "C120_dual_weights": 90_552,
    "C120_endpoint_positive_definite_checks": 588,
    "C123_phase_chambers": 135,
    "C123_epoch_duals": 270,
    "C123_dual_weights": 83_160,
    "C123_endpoint_positive_definite_checks": 540,
}
EXPECTED_CANDIDATE = {
    "epsilon": "1/1000",
    "A": "1/1000",
    "B": "1/2",
    "C_ordered_suffix": "1/10",
    "e2": "0/1",
    "eta": "log(82/215)",
    "target_formula": "(epsilon-A*eta-B*DeltaV-C_ordered_suffix*DeltaVrt)/3-e2",
}
EXPECTED_MARGINS = {
    "rigorous_comparison": "normalized_dual_lower_minus_target_upper",
    "C120_certified_margin_greater_than": "21/500",
    "C123_certified_margin_greater_than": "7/1000",
    "both_certified_margins_greater_than": "1/10000",
    "stored_dual_upper_checks_separate_candidate": False,
}
EXPECTED_SCOPE = {
    "fixed_C120_C123_16_mark_pair_only": True,
    "common_completed_shell_phase_T_equals_H3_over_8_only": True,
    "rho_9_over_16_only": True,
    "independent_epoch_block_cone_only": True,
    "fixed_C125_rational_candidate_only": True,
    "failure_of_two_necessary_side_dual_checks_only": True,
    "candidate_not_separated_by_stored_dual_uppers": True,
    "primal_phase_witness_constructed": False,
    "local_master_inequality_proved": False,
    "global_phase_rule_admissible_proved": False,
    "phase_representative_independence_proved": False,
    "ordered_vector_storage_proved": False,
    "ordered_vector_storage_refuted": False,
    "arbitrary_rank_proved": False,
    "global_owner_ledger_constructed": False,
    "C058_resolved": False,
    "Q1_Q2_resolved": False,
    "publication_novelty_or_prize_claimed": False,
}

TOP_KEYS = {"schema", "status", "sources", "replay", "candidate", "margins", "scope", "integrity"}
INTEGRITY_KEYS = {"algorithm", "payload_sha256", "exact_replay_arithmetic"}


class CertificateError(RuntimeError):
    """Raised for a schema, provenance, arithmetic, margin, or scope failure."""


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
        "candidate": dict(EXPECTED_CANDIDATE),
        "margins": dict(EXPECTED_MARGINS),
        "scope": dict(EXPECTED_SCOPE),
        "integrity": {
            "algorithm": "sha256",
            "payload_sha256": "",
            "exact_replay_arithmetic": (
                "fractions.Fraction plus pinned C125 atanh enclosure and C126 exact replay"
            ),
        },
    }
    value["integrity"]["payload_sha256"] = payload_hash(value)
    return value


def _exact_dict(value: object, keys: set[str], label: str) -> Mapping[str, Any]:
    if type(value) is not dict or set(value) != keys:
        raise CertificateError(f"{label}: exact keys differ")
    return value


def _validate_static(value: Mapping[str, Any]) -> None:
    _exact_dict(value, TOP_KEYS, "top")
    if value["schema"] != SCHEMA or value["status"] != STATUS:
        raise CertificateError("schema or status changed")
    if value["sources"] != EXPECTED_SOURCES:
        raise CertificateError("source provenance changed")
    if value["replay"] != EXPECTED_REPLAY:
        raise CertificateError("replay statement changed")
    if value["candidate"] != EXPECTED_CANDIDATE:
        raise CertificateError("candidate statement changed")
    if value["margins"] != EXPECTED_MARGINS:
        raise CertificateError("margin statement changed")
    if value["scope"] != EXPECTED_SCOPE:
        raise CertificateError("scope changed")
    integrity = _exact_dict(value["integrity"], INTEGRITY_KEYS, "integrity")
    if integrity["algorithm"] != "sha256" or integrity["payload_sha256"] != payload_hash(value):
        raise CertificateError("payload integrity mismatch")
    if integrity["exact_replay_arithmetic"] != (
        "fractions.Fraction plus pinned C125 atanh enclosure and C126 exact replay"
    ):
        raise CertificateError("arithmetic statement changed")


def _read_canonical_pinned_json(path: Path, digest: str, label: str) -> dict[str, Any]:
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != digest:
        raise CertificateError(f"{label}: sha256 mismatch")
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CertificateError(f"{label}: invalid JSON") from exc
    if type(value) is not dict or raw != c126.rendered_bytes(value):
        raise CertificateError(f"{label}: noncanonical rendering")
    return value


def _verify_dependency_provenance() -> dict[str, Any]:
    if hashlib.sha256(C126_VERIFIER_SOURCE.read_bytes()).hexdigest() != C126_VERIFIER_SHA256:
        raise CertificateError("C126 verifier sha256 mismatch")
    if hashlib.sha256(C125_VERIFIER_SOURCE.read_bytes()).hexdigest() != C125_VERIFIER_SHA256:
        raise CertificateError("C125 verifier sha256 mismatch")
    c126_value = _read_canonical_pinned_json(
        C126_CERTIFICATE, C126_CERTIFICATE_SHA256, "C126 certificate"
    )
    if c126_value.get("schema") != c126.SCHEMA or c126_value.get("status") != c126.STATUS:
        raise CertificateError("C126 schema or status changed")
    integrity = c126_value.get("integrity")
    if type(integrity) is not dict or integrity.get("payload_sha256") != C126_CERTIFICATE_PAYLOAD_SHA256:
        raise CertificateError("C126 payload hash changed")
    if c125.SCHEMA != "erdos1191.c125.ordered_suffix_five_row_bank.v1":
        raise CertificateError("C125 schema changed")
    expected_c125_constants = (
        CANDIDATE_EPSILON,
        CANDIDATE_A,
        CANDIDATE_B,
        CANDIDATE_C,
        CANDIDATE_E2,
        ABS_DELTA_V,
        -DELTA_VRT_C120,
        DELTA_VRT_C123,
        30,
    )
    actual_c125_constants = (
        c125.CANDIDATE_EPSILON,
        c125.CANDIDATE_A,
        c125.CANDIDATE_B,
        c125.CANDIDATE_C,
        c125.CANDIDATE_E2,
        c125.DELTA_V_NEGATIVE_ABS,
        c125.DELTA_VRT_C120_ABS,
        c125.DELTA_VRT_C123,
        c125.LOG_TERMS,
    )
    if actual_c125_constants != expected_c125_constants:
        raise CertificateError("C125 candidate, storage increments, or log terms changed")
    return c126_value


def _target_interval(delta_vrt: F, log_lower: F, log_upper: F) -> tuple[F, F]:
    rational_part = (
        CANDIDATE_EPSILON
        + CANDIDATE_B * ABS_DELTA_V
        - CANDIDATE_C * delta_vrt
    )
    lower = (rational_part + CANDIDATE_A * log_lower) / 3 - CANDIDATE_E2
    upper = (rational_part + CANDIDATE_A * log_upper) / 3 - CANDIDATE_E2
    if not F() < lower <= upper:
        raise CertificateError("candidate target interval is malformed")
    return lower, upper


def _candidate_row(
    dependency_row: Mapping[str, Any],
    delta_vrt: F,
    clean_fence: F,
    tag: str,
    log_lower: F,
    log_upper: F,
) -> dict[str, Any]:
    target_lower, target_upper = _target_interval(delta_vrt, log_lower, log_upper)
    dual_lower = dependency_row["normalized_lower"]
    dual_upper = dependency_row["normalized_upper"]
    margin_lower = dual_lower - target_upper
    margin_upper = dual_upper - target_lower
    if not F() < margin_lower <= margin_upper:
        raise CertificateError(f"{tag}: certified positive stored-dual margin is missing")
    if not margin_lower > clean_fence > COMMON_MARGIN_FENCE:
        raise CertificateError(f"{tag}: exact clean margin fence failed")
    return {
        "phase_chambers": dependency_row["phase_chambers"],
        "epoch_duals": dependency_row["epoch_duals"],
        "dual_weights": dependency_row["dual_weights"],
        "endpoint_pd_checks": dependency_row["endpoint_pd_checks"],
        "delta_Vrt": delta_vrt,
        "target_lower": target_lower,
        "target_upper": target_upper,
        "normalized_dual_lower": dual_lower,
        "normalized_dual_upper": dual_upper,
        "certified_margin_lower": margin_lower,
        "certified_margin_upper": margin_upper,
    }


_REPLAY_CACHE: dict[str, Any] | None = None


def _replay_dependencies() -> dict[str, Any]:
    global _REPLAY_CACHE
    if _REPLAY_CACHE is not None:
        return copy.deepcopy(_REPLAY_CACHE)
    c126_value = _verify_dependency_provenance()
    dependency = c126.verify_certificate(c126_value)
    if (
        c126.PHASE_LOWER != PHASE_LOWER
        or c126.PHASE_UPPER != PHASE_UPPER
        or c126.RHO != RHO
    ):
        raise CertificateError("C126 common phase or rho changed")
    log_lower, log_upper = c125._log_interval(F(215, 82))
    c120_row = _candidate_row(
        dependency["C120"], DELTA_VRT_C120, C120_MARGIN_FENCE,
        "C120", log_lower, log_upper,
    )
    c123_row = _candidate_row(
        dependency["C123"], DELTA_VRT_C123, C123_MARGIN_FENCE,
        "C123", log_lower, log_upper,
    )
    candidate = {
        "epsilon": CANDIDATE_EPSILON,
        "A": CANDIDATE_A,
        "B": CANDIDATE_B,
        "C_ordered_suffix": CANDIDATE_C,
        "e2": CANDIDATE_E2,
    }
    summary = {
        "common_phase": (PHASE_LOWER, PHASE_UPPER),
        "rho": RHO,
        "candidate": candidate,
        "eta_abs_log_lower": log_lower,
        "eta_abs_log_upper": log_upper,
        "C120": c120_row,
        "C123": c123_row,
        "stored_dual_upper_checks_separate_candidate": False,
    }
    _REPLAY_CACHE = copy.deepcopy(summary)
    return summary


def verify_certificate(value: Mapping[str, Any]) -> dict[str, Any]:
    _validate_static(value)
    return _replay_dependencies()


def _load(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CertificateError(f"certificate: invalid JSON: {exc}") from exc
    if type(value) is not dict or raw != rendered_bytes(value):
        raise CertificateError("certificate is not in canonical rendering")
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
    add("C126-verifier", lambda x: x["sources"].__setitem__("C126_common_phase_verifier_sha256", "0" * 64))
    add("C126-certificate", lambda x: x["sources"].__setitem__("C126_common_phase_certificate_sha256", "0" * 64))
    add("C125-verifier", lambda x: x["sources"].__setitem__("C125_ordered_candidate_verifier_sha256", "0" * 64))
    add("C120-count", lambda x: x["replay"].__setitem__("C120_epoch_duals", 293))
    add("candidate-B", lambda x: x["candidate"].__setitem__("B", "2/3"))
    add("target-formula", lambda x: x["candidate"].__setitem__("target_formula", "mutated"))
    add("C120-margin", lambda x: x["margins"].__setitem__("C120_certified_margin_greater_than", "1/20"))
    add("C123-margin", lambda x: x["margins"].__setitem__("C123_certified_margin_greater_than", "1/100"))
    add("separated", lambda x: x["margins"].__setitem__("stored_dual_upper_checks_separate_candidate", True))
    add("scope-primal", lambda x: x["scope"].__setitem__("primal_phase_witness_constructed", True))
    add("scope-C058", lambda x: x["scope"].__setitem__("C058_resolved", True))

    rejected = 0
    for label, changed in mutations:
        try:
            verify_certificate(changed)
        except (CertificateError, c125.CertificateError, c126.CertificateError):
            rejected += 1
        else:
            raise CertificateError(f"self-check mutation was accepted: {label}")
    return {"mutations_attempted": len(mutations), "mutations_rejected": rejected}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--print-expected", action="store_true")
    args = parser.parse_args(argv)
    if args.print_expected:
        sys.stdout.buffer.write(rendered_bytes(expected_certificate()))
        return 0
    value = _load(args.verify)
    summary = verify_certificate(value)
    mutations = self_check(value) if args.self_check else {"mutations_rejected": 0}
    print(
        "VERIFY_OK",
        "common_phase=[82,164]",
        f"C120_chambers={summary['C120']['phase_chambers']}",
        f"C123_chambers={summary['C123']['phase_chambers']}",
        "C120_margin>21/500",
        "C123_margin>7/1000",
        f"separated={summary['stored_dual_upper_checks_separate_candidate']}",
        f"mutations_rejected={mutations['mutations_rejected']}",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
