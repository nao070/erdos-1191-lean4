#!/usr/bin/env python3
"""Exact local-dual no-go for the fixed C125 candidate on C123 chambers.

The pinned C126 dual sources are reconstructed chamber by chamber in exact
rational arithmetic.  On C123 common-phase chambers 0 through 21, the exact
dual upper bound for the chamber average is strictly below the exact lower
bound for the fixed C125 target.  Hence a scheme requiring that same target
on every chamber, and therefore an all-phase pointwise lower bound at that
target, cannot hold in the frozen cone.

This is a finite obstruction for one row and one coefficient vector.  It does
not make the physical phase impossible and does not refute integrated primal
feasibility.  It is not an integrated primal certificate, a local master
inequality, a global phase rule, an arbitrary-rank statement, or a resolution
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
from typing import Any, Mapping, Sequence


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import ROUTE_C_C125_ORDERED_SUFFIX_FIVE_ROW_BANK_certificate as c125
import ROUTE_C_C126_COMMON_COMPLETED_SHELL_PHASE_certificate as c126


DEFAULT_CERTIFICATE = HERE / "ROUTE_C_C128_COMMON_PHASE_POINTWISE_NO_GO_certificate.json"
C126_CERTIFICATE = HERE / "ROUTE_C_C126_COMMON_COMPLETED_SHELL_PHASE_certificate.json"
C126_VERIFIER_SOURCE = HERE / "ROUTE_C_C126_COMMON_COMPLETED_SHELL_PHASE_certificate.py"
C125_VERIFIER_SOURCE = HERE / "ROUTE_C_C125_ORDERED_SUFFIX_FIVE_ROW_BANK_certificate.py"

SCHEMA = "erdos1191.c128.common_phase_pointwise_no_go.v1"
STATUS = "EXACT_FINITE_C123_CHAMBERS_0_TO_21_POINTWISE_NO_GO_C058_OPEN"

C126_CERTIFICATE_SHA256 = "b1a37954b11a807161d85d916a875058d9a4dab51a5dc208468429fe937074cf"
C126_CERTIFICATE_PAYLOAD_SHA256 = "03a8df34c95e20b3e24d7d1a91d4de169136a699239c3b5f777a60916a1f1f86"
C126_VERIFIER_SHA256 = "830c6afa79d49d386e5bc57bdb5578b8074e783486cbaf991164ae25e91a5981"
C125_VERIFIER_SHA256 = "1d9f4d8ea7756eb89fa9e8cc5d44e15a6480057df82392afadd30cbcbcb48fe2"
C120_SOURCE_SHA256 = "ba68e13b5a70abe50d14784d4e8e6bd7cf70df4dacace162a28b3383b59627f1"
C120_INTERNAL_SHA256 = "feaada44db91313200e0c5f719421d0572af06b44d40bc7c31419fae726da304"
C123_SOURCE_SHA256 = "a47eff804bbdf4082ba61d60202855e2a22b86c2c771df44a1e6f5728e952fae"
C123_INTERNAL_SHA256 = "7415bafcae9c37e043d8d6088fa5471f5916f595c367fde8222d4fe194ac52ab"

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
LOG_TERMS = 30
DUAL_SOURCE_SCHEMA = "erdos1191.c058_eta_negative_full_phase_dual.discovery.v1"

EXPECTED_SOURCES = {
    "C125_ordered_candidate_verifier": C125_VERIFIER_SOURCE.name,
    "C125_ordered_candidate_verifier_sha256": C125_VERIFIER_SHA256,
    "C126_common_phase_certificate": C126_CERTIFICATE.name,
    "C126_common_phase_certificate_sha256": C126_CERTIFICATE_SHA256,
    "C126_common_phase_certificate_payload_sha256": C126_CERTIFICATE_PAYLOAD_SHA256,
    "C126_common_phase_verifier": C126_VERIFIER_SOURCE.name,
    "C126_common_phase_verifier_sha256": C126_VERIFIER_SHA256,
    "C120_common_phase_dual": c126.C120_SOURCE.name,
    "C120_common_phase_dual_sha256": C120_SOURCE_SHA256,
    "C120_common_phase_internal_sha256": C120_INTERNAL_SHA256,
    "C123_common_phase_dual": c126.C123_SOURCE.name,
    "C123_common_phase_dual_sha256": C123_SOURCE_SHA256,
    "C123_common_phase_internal_sha256": C123_INTERNAL_SHA256,
}
EXPECTED_REPLAY = {
    "common_phase": ["82/1", "164/1"],
    "rho": "9/16",
    "C120_phase_chambers": 147,
    "C120_stored_local_dual_separations": 0,
    "C123_phase_chambers": 135,
    "C123_stored_local_dual_separations": 22,
    "C123_separating_indices": list(range(22)),
    "C123_first_separating_interval": ["82/1", "493/6"],
    "C123_last_separating_interval": ["359/4", "90/1"],
    "C123_strongest_separating_index": 0,
    "epoch_dual_reconstructions": 564,
    "endpoint_positive_definite_checks": 1128,
}
EXPECTED_CANDIDATE = {
    "epsilon": "1/1000",
    "A": "1/1000",
    "B": "1/2",
    "C_ordered_suffix": "1/10",
    "e2": "0/1",
    "eta": "log(82/215)",
    "target_formula": "(epsilon-A*eta-B*DeltaV-C_ordered_suffix*DeltaVrt)/3-e2",
    "target_log_enclosure_terms": 30,
}
EXPECTED_BOUNDS = {
    "strongest_row": "C123",
    "strongest_chamber_index": 0,
    "strongest_chamber_interval": ["82/1", "493/6"],
    "target_greater_than": "9/250",
    "combined_local_dual_upper_less_than": "39/2000",
    "target_minus_upper_greater_than": "33/2000",
    "epoch4_weighted_local_upper_less_than": "-13/1000",
    "epoch8_weighted_local_upper_less_than": "33/1000",
}
EXPECTED_SCOPE = {
    "fixed_C120_C123_16_mark_pair_only": True,
    "fixed_C125_rational_candidate_only": True,
    "common_completed_shell_phase_T_equals_H3_over_8_only": True,
    "rho_9_over_16_only": True,
    "independent_epoch_block_cone_only": True,
    "C123_local_average_target_refuted_on_chambers_0_through_21": True,
    "fixed_C123_uniform_all_chambers_candidate_lower_refuted": True,
    "fixed_C123_all_phase_pointwise_candidate_lower_refuted": True,
    "phase_redistribution_is_load_bearing_for_this_candidate": True,
    "C120_stored_local_dual_separations_zero": True,
    "C120_per_chamber_candidate_lower_proved": False,
    "integrated_primal_certificate_constructed": False,
    "numerical_integrated_screen_promoted_to_proof": False,
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

TOP_KEYS = {
    "schema", "status", "sources", "replay", "candidate", "bounds", "scope", "integrity"
}
INTEGRITY_KEYS = {"algorithm", "payload_sha256", "exact_replay_arithmetic"}


class CertificateError(RuntimeError):
    """Raised for a schema, provenance, reconstruction, inequality, or scope failure."""


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
        "replay": copy.deepcopy(EXPECTED_REPLAY),
        "candidate": dict(EXPECTED_CANDIDATE),
        "bounds": dict(EXPECTED_BOUNDS),
        "scope": dict(EXPECTED_SCOPE),
        "integrity": {
            "algorithm": "sha256",
            "payload_sha256": "",
            "exact_replay_arithmetic": (
                "fractions.Fraction; pinned 30-term atanh log enclosures; "
                "fraction-free integer Bareiss/Sylvester endpoint PD"
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
    if value["bounds"] != EXPECTED_BOUNDS:
        raise CertificateError("clean bounds changed")
    if value["scope"] != EXPECTED_SCOPE:
        raise CertificateError("scope changed")
    integrity = _exact_dict(value["integrity"], INTEGRITY_KEYS, "integrity")
    if integrity["algorithm"] != "sha256" or integrity["payload_sha256"] != payload_hash(value):
        raise CertificateError("payload integrity mismatch")
    if integrity["exact_replay_arithmetic"] != (
        "fractions.Fraction; pinned 30-term atanh log enclosures; "
        "fraction-free integer Bareiss/Sylvester endpoint PD"
    ):
        raise CertificateError("arithmetic statement changed")


def _read_canonical_certificate(path: Path, digest: str, label: str) -> dict[str, Any]:
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


def _read_pinned_source(
    path: Path,
    file_digest: str,
    internal_digest: str,
    label: str,
) -> dict[str, Any]:
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != file_digest:
        raise CertificateError(f"{label}: sha256 mismatch")
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CertificateError(f"{label}: invalid JSON") from exc
    if type(value) is not dict:
        raise CertificateError(f"{label}: expected object")
    canonical = (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")
    if raw != canonical:
        raise CertificateError(f"{label}: noncanonical rendering")
    without_hash = dict(value)
    internal = without_hash.pop("payload_sha256_without_hash", None)
    if internal != internal_digest or _object_hash(without_hash) != internal:
        raise CertificateError(f"{label}: internal source hash mismatch")
    if value.get("schema") != DUAL_SOURCE_SCHEMA:
        raise CertificateError(f"{label}: source schema changed")
    return value


def _verify_dependency_provenance() -> dict[str, Any]:
    checks = (
        (C126_VERIFIER_SOURCE, C126_VERIFIER_SHA256, "C126 verifier"),
        (C125_VERIFIER_SOURCE, C125_VERIFIER_SHA256, "C125 verifier"),
        (c126.C120_SOURCE, C120_SOURCE_SHA256, "C120 source"),
        (c126.C123_SOURCE, C123_SOURCE_SHA256, "C123 source"),
    )
    for path, digest, label in checks:
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise CertificateError(f"{label}: sha256 mismatch")
    if c126.C120_INTERNAL_SHA256 != C120_INTERNAL_SHA256:
        raise CertificateError("C120 internal source hash changed")
    if c126.C123_INTERNAL_SHA256 != C123_INTERNAL_SHA256:
        raise CertificateError("C123 internal source hash changed")
    c126_value = _read_canonical_certificate(
        C126_CERTIFICATE, C126_CERTIFICATE_SHA256, "C126 certificate"
    )
    integrity = c126_value.get("integrity")
    if type(integrity) is not dict or integrity.get("payload_sha256") != C126_CERTIFICATE_PAYLOAD_SHA256:
        raise CertificateError("C126 payload hash changed")
    dependency = c126.verify_certificate(c126_value)
    expected_constants = (
        CANDIDATE_EPSILON,
        CANDIDATE_A,
        CANDIDATE_B,
        CANDIDATE_C,
        CANDIDATE_E2,
        ABS_DELTA_V,
        -DELTA_VRT_C120,
        DELTA_VRT_C123,
        LOG_TERMS,
    )
    actual_constants = (
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
    if actual_constants != expected_constants:
        raise CertificateError("C125 candidate, increments, or log terms changed")
    if (
        c126.PHASE_LOWER != PHASE_LOWER
        or c126.PHASE_UPPER != PHASE_UPPER
        or c126.RHO != RHO
    ):
        raise CertificateError("C126 common phase or rho changed")
    return dependency


def _target_interval(delta_vrt: F) -> tuple[F, F]:
    log_lower, log_upper = c125._log_interval(F(215, 82))
    rational = CANDIDATE_EPSILON + CANDIDATE_B * ABS_DELTA_V - CANDIDATE_C * delta_vrt
    lower = (rational + CANDIDATE_A * log_lower) / 3 - CANDIDATE_E2
    upper = (rational + CANDIDATE_A * log_upper) / 3 - CANDIDATE_E2
    if not F() < lower <= upper:
        raise CertificateError("candidate target interval is malformed")
    return lower, upper


def _log_piece_interval(
    model: Any,
    log_coefficient: F,
    reciprocal_coefficient: F,
    left: F,
    right: F,
) -> tuple[F, F]:
    log_lower, log_upper = model._log_interval(right / left)
    reciprocal = reciprocal_coefficient * (F(1) / left - F(1) / right)
    if log_coefficient >= 0:
        return (
            log_coefficient * log_lower + reciprocal,
            log_coefficient * log_upper + reciprocal,
        )
    return (
        log_coefficient * log_upper + reciprocal,
        log_coefficient * log_lower + reciprocal,
    )


def _positive_denominator_quotient_interval(
    numerator_lower: F,
    numerator_upper: F,
    denominator_lower: F,
    denominator_upper: F,
) -> tuple[F, F]:
    if not numerator_lower <= numerator_upper or not F() < denominator_lower <= denominator_upper:
        raise CertificateError("malformed quotient interval")
    corners = (
        numerator_lower / denominator_lower,
        numerator_lower / denominator_upper,
        numerator_upper / denominator_lower,
        numerator_upper / denominator_upper,
    )
    return min(corners), max(corners)


def _positive_piece_average_interval(
    numerator_lower: F,
    numerator_upper: F,
    log_lower: F,
    log_upper: F,
) -> tuple[F, F]:
    if not F() < numerator_lower <= numerator_upper:
        raise CertificateError("raw piece is not strictly positive")
    return _positive_denominator_quotient_interval(
        numerator_lower, numerator_upper, log_lower, log_upper
    )


def _audit_row(
    *,
    tag: str,
    points: tuple[int, ...],
    source_path: Path,
    source_sha: str,
    internal_sha: str,
    delta_vrt: F,
    expected_chambers: int,
) -> dict[str, Any]:
    source = _read_pinned_source(source_path, source_sha, internal_sha, tag)
    model = c126._load_model(points, f"c128_{tag.lower()}")
    breakpoints = tuple(F(text) for text in source["breakpoints"])
    if breakpoints != model._breakpoints() or len(breakpoints) != expected_chambers + 1:
        raise CertificateError(f"{tag}: chamber partition changed")
    records = source["records"]
    if type(records) is not list or len(records) != expected_chambers:
        raise CertificateError(f"{tag}: chamber count changed")
    target_lower, target_upper = _target_interval(delta_vrt)
    separating: list[dict[str, Any]] = []
    reconstructions = 0
    endpoint_checks = 0
    for index, (record, left, right) in enumerate(
        zip(records, breakpoints, breakpoints[1:])
    ):
        if record["index"] != index or F(record["left"]) != left or F(record["right"]) != right:
            raise CertificateError(f"{tag} chamber {index}: interval changed")
        piece_lower = F()
        piece_upper = F()
        epoch_intervals: dict[int, tuple[F, F]] = {}
        for epoch, weight in ((4, F(1)), (8, RHO)):
            key = f"n{epoch}"
            denominator = int(record[key]["denominator"])
            weights = tuple(int(value) for value in record[key]["weights"])
            if denominator <= 0 or len(weights) != 308 or min(weights) < 0:
                raise CertificateError(f"{tag} chamber {index}, epoch {epoch}: dual data")
            hc, ho, weighted, dc, do, objective = model._dual_epoch_reconstruction(
                left, right, epoch, denominator, weights
            )
            if dc != F(record[f"Dc{epoch}"]) or do != F(record[f"Do{epoch}"]):
                raise CertificateError(f"{tag} chamber {index}, epoch {epoch}: demand changed")
            if objective != F(record[key]["objective"]):
                raise CertificateError(f"{tag} chamber {index}, epoch {epoch}: objective changed")
            for endpoint in (left, right):
                slack = model._integer_slack(hc, ho, weighted, denominator, endpoint)
                if not model._bareiss_positive_definite(slack):
                    raise CertificateError(
                        f"{tag} chamber {index}, epoch {epoch}: endpoint not positive definite"
                    )
                endpoint_checks += 1
            epoch_lower, epoch_upper = _log_piece_interval(
                model, 2 * dc - objective, 2 * do, left, right
            )
            weighted_interval = (weight * epoch_lower, weight * epoch_upper)
            epoch_intervals[epoch] = weighted_interval
            piece_lower += weighted_interval[0]
            piece_upper += weighted_interval[1]
            reconstructions += 1
        stored_lower, stored_upper = model._dual_piece_interval(record)
        if not piece_lower <= stored_lower <= stored_upper <= piece_upper:
            raise CertificateError(f"{tag} chamber {index}: combined piece not contained")
        log_lower, log_upper = model._log_interval(right / left)
        local_lower, local_upper = _positive_piece_average_interval(
            stored_lower, stored_upper, log_lower, log_upper
        )
        if local_upper < target_lower:
            epoch4_local = _positive_denominator_quotient_interval(
                epoch_intervals[4][0], epoch_intervals[4][1], log_lower, log_upper
            )
            epoch8_local = _positive_denominator_quotient_interval(
                epoch_intervals[8][0], epoch_intervals[8][1], log_lower, log_upper
            )
            separating.append({
                "index": index,
                "interval": (left, right),
                "target_lower": target_lower,
                "target_upper": target_upper,
                "combined_local_lower": local_lower,
                "combined_local_upper": local_upper,
                "deficit_lower": target_lower - local_upper,
                "epoch4_weighted_local_upper": epoch4_local[1],
                "epoch8_weighted_local_upper": epoch8_local[1],
            })
    strongest = max(separating, key=lambda item: item["deficit_lower"]) if separating else None
    return {
        "phase_chambers": expected_chambers,
        "epoch_dual_reconstructions": reconstructions,
        "endpoint_pd_checks": endpoint_checks,
        "target_lower": target_lower,
        "target_upper": target_upper,
        "separating_indices": tuple(item["index"] for item in separating),
        "first_separating_interval": None if not separating else separating[0]["interval"],
        "last_separating_interval": None if not separating else separating[-1]["interval"],
        "strongest_chamber": strongest,
    }


_REPLAY_CACHE: dict[str, Any] | None = None


def _replay_exact() -> dict[str, Any]:
    global _REPLAY_CACHE
    if _REPLAY_CACHE is not None:
        return copy.deepcopy(_REPLAY_CACHE)
    dependency = _verify_dependency_provenance()
    if dependency["C120"]["phase_chambers"] != 147 or dependency["C123"]["phase_chambers"] != 135:
        raise CertificateError("C126 dependency chamber counts changed")
    c120_row = _audit_row(
        tag="C120",
        points=c126.C120_POINTS,
        source_path=c126.C120_SOURCE,
        source_sha=C120_SOURCE_SHA256,
        internal_sha=C120_INTERNAL_SHA256,
        delta_vrt=DELTA_VRT_C120,
        expected_chambers=147,
    )
    c123_row = _audit_row(
        tag="C123",
        points=c126.C123_POINTS,
        source_path=c126.C123_SOURCE,
        source_sha=C123_SOURCE_SHA256,
        internal_sha=C123_INTERNAL_SHA256,
        delta_vrt=DELTA_VRT_C123,
        expected_chambers=135,
    )
    if c120_row["separating_indices"] != ():
        raise CertificateError("C120 stored local-dual separation set changed")
    if c123_row["separating_indices"] != tuple(range(22)):
        raise CertificateError("C123 stored local-dual separation set changed")
    if c123_row["first_separating_interval"] != (F(82), F(493, 6)):
        raise CertificateError("C123 first separating interval changed")
    if c123_row["last_separating_interval"] != (F(359, 4), F(90)):
        raise CertificateError("C123 last separating interval changed")
    strongest = c123_row["strongest_chamber"]
    if strongest is None or strongest["index"] != 0:
        raise CertificateError("C123 strongest chamber changed")
    if not strongest["target_lower"] > F(9, 250):
        raise CertificateError("C123 chamber 0 target clean lower bound failed")
    if not strongest["combined_local_upper"] < F(39, 2000):
        raise CertificateError("C123 chamber 0 local upper clean bound failed")
    if not strongest["deficit_lower"] > F(33, 2000):
        raise CertificateError("C123 chamber 0 deficit clean bound failed")
    if not strongest["epoch4_weighted_local_upper"] < -F(13, 1000):
        raise CertificateError("C123 chamber 0 epoch-4 clean bound failed")
    if not strongest["epoch8_weighted_local_upper"] < F(33, 1000):
        raise CertificateError("C123 chamber 0 epoch-8 clean bound failed")
    if (
        c120_row["epoch_dual_reconstructions"] + c123_row["epoch_dual_reconstructions"]
        != 564
    ):
        raise CertificateError("epoch reconstruction count changed")
    if c120_row["endpoint_pd_checks"] + c123_row["endpoint_pd_checks"] != 1128:
        raise CertificateError("endpoint PD count changed")
    summary = {
        "common_phase": (PHASE_LOWER, PHASE_UPPER),
        "rho": RHO,
        "C120": c120_row,
        "C123": c123_row,
    }
    _REPLAY_CACHE = copy.deepcopy(summary)
    return summary


def verify_certificate(value: Mapping[str, Any]) -> dict[str, Any]:
    _validate_static(value)
    return _replay_exact()


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
    add("C126-hash", lambda x: x["sources"].__setitem__("C126_common_phase_verifier_sha256", "0" * 64))
    add("C125-hash", lambda x: x["sources"].__setitem__("C125_ordered_candidate_verifier_sha256", "0" * 64))
    add("C123-source-hash", lambda x: x["sources"].__setitem__("C123_common_phase_dual_sha256", "0" * 64))
    add("C123-count", lambda x: x["replay"].__setitem__("C123_stored_local_dual_separations", 21))
    add("C123-indices", lambda x: x["replay"]["C123_separating_indices"].pop())
    add("first-interval", lambda x: x["replay"].__setitem__("C123_first_separating_interval", ["82/1", "83/1"]))
    add("target-bound", lambda x: x["bounds"].__setitem__("target_greater_than", "1/25"))
    add("dual-bound", lambda x: x["bounds"].__setitem__("combined_local_dual_upper_less_than", "1/50"))
    add("deficit-bound", lambda x: x["bounds"].__setitem__("target_minus_upper_greater_than", "1/50"))
    add("no-redistribution", lambda x: x["scope"].__setitem__("phase_redistribution_is_load_bearing_for_this_candidate", False))
    add("false-integrated-primal", lambda x: x["scope"].__setitem__("integrated_primal_certificate_constructed", True))
    add("scope-C058", lambda x: x["scope"].__setitem__("C058_resolved", True))

    rejected = 0
    for label, changed in mutations:
        try:
            verify_certificate(changed)
        except (CertificateError, c126.CertificateError, c125.CertificateError):
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
    strongest = summary["C123"]["strongest_chamber"]
    print(
        "VERIFY_OK",
        "common_phase=[82,164]",
        "rho=9/16",
        f"C120_local_separations={len(summary['C120']['separating_indices'])}",
        f"C123_local_separations={len(summary['C123']['separating_indices'])}",
        "C123_indices=0..21",
        f"strongest={strongest['index']}:[82,493/6]",
        "target>9/250",
        "local_upper<39/2000",
        "deficit>33/2000",
        f"mutations_rejected={mutations['mutations_rejected']}",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
