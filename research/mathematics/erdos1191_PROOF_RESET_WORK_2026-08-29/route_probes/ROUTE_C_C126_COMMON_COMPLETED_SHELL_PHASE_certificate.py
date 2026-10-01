#!/usr/bin/env python3
"""Exact common completed-shell phase audit for the C120/C123 pair.

Both same-multiset rows are placed on the order-independent finite phase
``T=H3/8=82``, ``[T,2T]=[82,164]``.  Stored duals are reconstructed exactly
on every chamber and endpoint.  The resulting scalar fences remain
noncontradictory.  Global admissibility of this phase choice is not proved.
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


DEFAULT_CERTIFICATE = HERE / "ROUTE_C_C126_COMMON_COMPLETED_SHELL_PHASE_certificate.json"
C120_SOURCE = HERE / "ROUTE_C_C126_COMMON_PHASE_C120_source.json"
C123_SOURCE = HERE / "ROUTE_C_C126_COMMON_PHASE_C123_source.json"
C121_CERTIFICATE = HERE / "ROUTE_C_C118_SUBDIVIDED_STORAGE_NO_GO_certificate.json"
C121_VERIFIER_SOURCE = HERE / "ROUTE_C_C118_SUBDIVIDED_STORAGE_NO_GO_certificate.py"
C120_MODEL_SOURCE = HERE / "ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate.py"

SCHEMA = "erdos1191.c126.common_completed_shell_phase.v1"
STATUS = "EXACT_FINITE_COMMON_PHASE_SCALAR_BANK_NONEMPTY_C058_OPEN"

C120_SOURCE_SHA256 = "ba68e13b5a70abe50d14784d4e8e6bd7cf70df4dacace162a28b3383b59627f1"
C120_INTERNAL_SHA256 = "feaada44db91313200e0c5f719421d0572af06b44d40bc7c31419fae726da304"
C123_SOURCE_SHA256 = "a47eff804bbdf4082ba61d60202855e2a22b86c2c771df44a1e6f5728e952fae"
C123_INTERNAL_SHA256 = "7415bafcae9c37e043d8d6088fa5471f5916f595c367fde8222d4fe194ac52ab"
C121_CERTIFICATE_SHA256 = "1288d87e095a47f9fdf679a40656bafdef4ad4b03150ccb3254b25b043937a0b"
C121_VERIFIER_SHA256 = "e568d5562dd8c51c82ff603d678cd712f3f3250398d927982fa9c3fcd0469953"
C120_MODEL_SHA256 = "6e8d7e3f975e952442672cb1d18e4512d616f343bb4f6379ba0c8701cd996fe9"
DUAL_SOURCE_SCHEMA = "erdos1191.c058_eta_negative_full_phase_dual.discovery.v1"

C120_POINTS = (
    0, 22, 60, 83, 102, 173, 303, 513,
    616, 727, 772, 881, 972, 1041, 1103, 1169,
)
C123_POINTS = (
    0, 22, 60, 83, 154, 284, 494, 513,
    575, 620, 711, 777, 880, 989, 1100, 1169,
)
PHASE_LOWER = F(82)
PHASE_UPPER = F(164)
RHO = F(9, 16)
ABS_DELTA_V = F(443_620_417, 1_928_247_678)
DELTA_V_POSITIVE = F(3_440_812_085, 9_234_857_208)
C120_NORMALIZED_FENCE = F(89, 1000)
C123_NORMALIZED_FENCE = F(87, 2000)
CLEAN_B_LOWER = F(1341, 4000)
CLEAN_B_UPPER = F(1133, 2000)
CLEAN_WIDTH = F(37, 160)
EXACT_B_WITNESS = F(1, 2)

EXPECTED_SOURCES = {
    "C121_certificate": C121_CERTIFICATE.name,
    "C121_certificate_sha256": C121_CERTIFICATE_SHA256,
    "C121_verifier": C121_VERIFIER_SOURCE.name,
    "C121_verifier_sha256": C121_VERIFIER_SHA256,
    "C120_model": C120_MODEL_SOURCE.name,
    "C120_model_sha256": C120_MODEL_SHA256,
    "C120_common_phase_dual": C120_SOURCE.name,
    "C120_common_phase_dual_sha256": C120_SOURCE_SHA256,
    "C120_common_phase_internal_sha256": C120_INTERNAL_SHA256,
    "C123_common_phase_dual": C123_SOURCE.name,
    "C123_common_phase_dual_sha256": C123_SOURCE_SHA256,
    "C123_common_phase_internal_sha256": C123_INTERNAL_SHA256,
}
EXPECTED_REPLAY = {
    "common_phase": ["82/1", "164/1"],
    "rho": "9/16",
    "C120_phase_chambers": 147,
    "C120_epoch_duals": 294,
    "C120_dual_weights": 90552,
    "C120_endpoint_positive_definite_checks": 588,
    "C120_normalized_upper_less_than": "89/1000",
    "C123_phase_chambers": 135,
    "C123_epoch_duals": 270,
    "C123_dual_weights": 83160,
    "C123_endpoint_positive_definite_checks": 540,
    "C123_normalized_upper_less_than": "87/2000",
}
EXPECTED_CONSTRAINTS = {
    "assumptions": "epsilon=A=e2=0; common scalar B; fixed C121, C120, and C123 rows in the stated independent epoch-block cone",
    "C121_clean_necessary_B_greater_than": "1341/4000",
    "C123_common_phase_clean_necessary_B_less_than": "1133/2000",
    "clean_open_interval_width": "37/160",
    "exact_rational_witness_B": "1/2",
    "exact_common_phase_interval_nonempty": True,
    "barriers_contradict": False,
    "phase_base_difference_explains_scalar_noncontradiction": False,
}
EXPECTED_SCOPE = {
    "fixed_C120_C123_16_mark_pair_only": True,
    "common_phase_for_C120_C123_proved": True,
    "completed_shell_rule_T_equals_H3_over_8_only": True,
    "rho_9_over_16_only": True,
    "independent_epoch_block_cone_only": True,
    "global_C103_phase_rule_admissible_proved": False,
    "scalar_storage_refuted": False,
    "ordered_vector_storage_refuted": False,
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
            "exact_replay_arithmetic": (
                "fractions.Fraction plus fraction-free integer Bareiss/Sylvester"
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
    if value["constraints"] != EXPECTED_CONSTRAINTS:
        raise CertificateError("constraint statement changed")
    if value["scope"] != EXPECTED_SCOPE:
        raise CertificateError("scope changed")
    integrity = _exact_dict(value["integrity"], INTEGRITY_KEYS, "integrity")
    if integrity["algorithm"] != "sha256" or integrity["payload_sha256"] != payload_hash(value):
        raise CertificateError("payload integrity mismatch")
    if integrity["exact_replay_arithmetic"] != (
        "fractions.Fraction plus fraction-free integer Bareiss/Sylvester"
    ):
        raise CertificateError("arithmetic statement changed")


def _read_pinned_json(path: Path, digest: str, label: str) -> dict[str, Any]:
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != digest:
        raise CertificateError(f"{label}: sha256 mismatch")
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CertificateError(f"{label}: invalid JSON") from exc
    if type(value) is not dict:
        raise CertificateError(f"{label}: expected object")
    return value


def _load_model(points: tuple[int, ...], tag: str) -> Any:
    raw = C120_MODEL_SOURCE.read_bytes()
    if hashlib.sha256(raw).hexdigest() != C120_MODEL_SHA256:
        raise CertificateError("C120 model source sha256 mismatch")
    spec = importlib.util.spec_from_file_location(f"c126_model_{tag}", C120_MODEL_SOURCE)
    if spec is None or spec.loader is None:
        raise CertificateError("cannot load C120 exact model")
    model = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(model)
    model.POINTS = points
    model.PHASE_LOWER = PHASE_LOWER
    model.PHASE_UPPER = PHASE_UPPER
    model.CHANNELS = tuple(
        (rank, multiplier, points[rank])
        for multiplier in model.MULTIPLIERS
        for rank in range(3, 16)
    )
    model.EVENT_LINES = tuple(sorted({
        (origin, shift * multiplier)
        for _, multiplier, origin in model.CHANNELS
        for shift in (0, 1, 2)
    }))
    model.EPOCH4_INDICES = tuple(
        i for i, (rank, _, _) in enumerate(model.CHANNELS) if rank <= 7
    )
    model.EPOCH8_INDICES = tuple(
        i for i, (rank, _, _) in enumerate(model.CHANNELS) if rank >= 8
    )
    return model


def _replay_row(
    *,
    path: Path,
    file_sha: str,
    internal_sha: str,
    points: tuple[int, ...],
    chambers: int,
    normalized_fence: F,
    clean_b_fence: F,
    tag: str,
) -> dict[str, Any]:
    source = _read_pinned_json(path, file_sha, tag)
    if set(source) != SOURCE_TOP_KEYS:
        raise CertificateError(f"{tag}: source keys changed")
    without_hash = dict(source)
    internal = without_hash.pop("payload_sha256_without_hash")
    if internal != internal_sha or _object_hash(without_hash) != internal:
        raise CertificateError(f"{tag}: internal hash mismatch")
    if source["schema"] != DUAL_SOURCE_SCHEMA:
        raise CertificateError(f"{tag}: source schema changed")
    if tuple(source["points"]) != points or source["base"] != "82/1":
        raise CertificateError(f"{tag}: fixture or phase changed")
    if F(source["rho"]) != RHO or source["H2"] != 430 or source["H3"] != 656:
        raise CertificateError(f"{tag}: scalar fixture changed")
    if source["eta_ratio"] != "82/215":
        raise CertificateError(f"{tag}: eta ratio changed")

    model = _load_model(points, tag)
    breakpoints = tuple(F(text) for text in source["breakpoints"])
    if breakpoints != model._breakpoints() or len(breakpoints) != chambers + 1:
        raise CertificateError(f"{tag}: breakpoints changed")
    records = source["records"]
    if type(records) is not list or len(records) != chambers:
        raise CertificateError(f"{tag}: chamber count changed")

    raw_lower = F()
    raw_upper = F()
    dual_count = 0
    weight_count = 0
    endpoint_count = 0
    for index, (record, left, right) in enumerate(zip(records, breakpoints, breakpoints[1:])):
        if record["index"] != index or F(record["left"]) != left or F(record["right"]) != right:
            raise CertificateError(f"{tag} chamber {index}: interval changed")
        for epoch, key in ((4, "n4"), (8, "n8")):
            denominator = int(record[key]["denominator"])
            weights = tuple(int(weight) for weight in record[key]["weights"])
            if denominator <= 0 or len(weights) != 308 or min(weights) < 0:
                raise CertificateError(f"{tag} chamber {index}, epoch {epoch}: dual data")
            hc, ho, weighted, dc, do, objective = model._dual_epoch_reconstruction(
                left, right, epoch, denominator, weights
            )
            if dc != F(record[f"Dc{epoch}"]) or do != F(record[f"Do{epoch}"]):
                raise CertificateError(f"{tag} chamber {index}, epoch {epoch}: demand")
            if objective != F(record[key]["objective"]):
                raise CertificateError(f"{tag} chamber {index}, epoch {epoch}: objective")
            for endpoint in (left, right):
                slack = model._integer_slack(hc, ho, weighted, denominator, endpoint)
                if not model._bareiss_positive_definite(slack):
                    raise CertificateError(f"{tag} chamber {index}, epoch {epoch}: endpoint not PD")
                endpoint_count += 1
            dual_count += 1
            weight_count += len(weights)
        lower, upper = model._dual_piece_interval(record)
        raw_lower += lower
        raw_upper += upper

    log2_lower, log2_upper = model._log_interval(F(2))
    normalized_lower = raw_lower / log2_upper
    normalized_upper = raw_upper / log2_lower
    exact_b_upper = 3 * normalized_upper / ABS_DELTA_V
    if not F() < normalized_lower <= normalized_upper < normalized_fence:
        raise CertificateError(f"{tag}: normalized fence failed")
    if not exact_b_upper < clean_b_fence:
        raise CertificateError(f"{tag}: clean B fence failed")
    return {
        "phase_chambers": chambers,
        "epoch_duals": dual_count,
        "dual_weights": weight_count,
        "endpoint_pd_checks": endpoint_count,
        "raw_lower": raw_lower,
        "raw_upper": raw_upper,
        "normalized_lower": normalized_lower,
        "normalized_upper": normalized_upper,
        "exact_B_upper": exact_b_upper,
    }


_REPLAY_CACHE: dict[str, Any] | None = None


def _replay_sources() -> dict[str, Any]:
    global _REPLAY_CACHE
    if _REPLAY_CACHE is not None:
        return copy.deepcopy(_REPLAY_CACHE)
    if hashlib.sha256(C121_VERIFIER_SOURCE.read_bytes()).hexdigest() != C121_VERIFIER_SHA256:
        raise CertificateError("C121 verifier source sha256 mismatch")
    c121_value = _read_pinned_json(C121_CERTIFICATE, C121_CERTIFICATE_SHA256, "C121")
    c121_summary = c121.verify_certificate(c121_value)
    exact_c121_lower = -3 * c121_summary["normalized_upper"] / DELTA_V_POSITIVE
    if not exact_c121_lower > CLEAN_B_LOWER:
        raise CertificateError("C121 clean lower fence failed")

    r120 = _replay_row(
        path=C120_SOURCE,
        file_sha=C120_SOURCE_SHA256,
        internal_sha=C120_INTERNAL_SHA256,
        points=C120_POINTS,
        chambers=147,
        normalized_fence=C120_NORMALIZED_FENCE,
        clean_b_fence=F(29, 25),
        tag="C120",
    )
    r123 = _replay_row(
        path=C123_SOURCE,
        file_sha=C123_SOURCE_SHA256,
        internal_sha=C123_INTERNAL_SHA256,
        points=C123_POINTS,
        chambers=135,
        normalized_fence=C123_NORMALIZED_FENCE,
        clean_b_fence=CLEAN_B_UPPER,
        tag="C123",
    )
    if CLEAN_B_UPPER - CLEAN_B_LOWER != CLEAN_WIDTH:
        raise CertificateError("clean interval arithmetic changed")
    exact_interval_nonempty = (
        exact_c121_lower < EXACT_B_WITNESS < r120["exact_B_upper"]
        and EXACT_B_WITNESS < r123["exact_B_upper"]
    )
    if not exact_interval_nonempty:
        raise CertificateError("exact rational witness no longer lies in every scalar half-line")
    summary = {
        "C120": r120,
        "C123": r123,
        "clean_B_lower": CLEAN_B_LOWER,
        "clean_B_upper": CLEAN_B_UPPER,
        "clean_width": CLEAN_WIDTH,
        "exact_C121_B_lower": exact_c121_lower,
        "exact_B_witness": EXACT_B_WITNESS,
        "exact_common_phase_interval_nonempty": exact_interval_nonempty,
        "barriers_contradict": not exact_interval_nonempty,
    }
    if summary["barriers_contradict"]:
        raise CertificateError("stored noncontradiction is false")
    _REPLAY_CACHE = copy.deepcopy(summary)
    return summary


def verify_certificate(value: Mapping[str, Any]) -> dict[str, Any]:
    _validate_static(value)
    return _replay_sources()


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
    add("C120-hash", lambda x: x["sources"].__setitem__("C120_common_phase_dual_sha256", "0" * 64))
    add("C123-hash", lambda x: x["sources"].__setitem__("C123_common_phase_dual_sha256", "0" * 64))
    add("C120-count", lambda x: x["replay"].__setitem__("C120_epoch_duals", 293))
    add("C123-fence", lambda x: x["constraints"].__setitem__("C123_common_phase_clean_necessary_B_less_than", "1/2"))
    add("exact-witness", lambda x: x["constraints"].__setitem__("exact_rational_witness_B", "2/3"))
    add("exact-nonempty", lambda x: x["constraints"].__setitem__("exact_common_phase_interval_nonempty", False))
    add("false-contradiction", lambda x: x["constraints"].__setitem__("barriers_contradict", True))
    add("global-phase", lambda x: x["scope"].__setitem__("global_C103_phase_rule_admissible_proved", True))
    add("scope-C058", lambda x: x["scope"].__setitem__("C058_resolved", True))
    add("scope-scalar", lambda x: x["scope"].__setitem__("scalar_storage_refuted", True))

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
        "clean_B_interval=(1341/4000,1133/2000)",
        "exact_witness_B=1/2",
        "width=37/160",
        f"barriers_contradict={summary['barriers_contradict']}",
        f"mutations_rejected={mutations['mutations_rejected']}",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
