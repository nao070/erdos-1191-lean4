#!/usr/bin/env python3
"""Exact five-row outer audit for scalar and chronological storage columns.

The verifier combines the registered C118/C120/C123 full-phase dual audits
with two additional same-multiset ordered rows.  It reconstructs every new
rational dual and endpoint slack exactly, then checks that one rational
coefficient vector is not separated by any of the five stored dual-upper
tests.  This is finite necessary-side calibration only: no primal witness,
arbitrary-rank theorem, global owner ledger, or C058 conclusion is claimed.
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
import ROUTE_C_C122_TWO_ROW_SCALAR_STORAGE_BANK_certificate as c122
import ROUTE_C_C123_ORDERED_PERMUTATION_FULL_PHASE_DUAL_certificate as c123


DEFAULT_CERTIFICATE = HERE / "ROUTE_C_C125_ORDERED_SUFFIX_FIVE_ROW_BANK_certificate.json"
ROW12_SOURCE = HERE / "ROUTE_C_C125_ORDERED_SUFFIX_ROW12_source.json"
ROW3_SOURCE = HERE / "ROUTE_C_C125_ORDERED_SUFFIX_ROW3_source.json"
C121_CERTIFICATE = HERE / "ROUTE_C_C118_SUBDIVIDED_STORAGE_NO_GO_certificate.json"
C122_CERTIFICATE = HERE / "ROUTE_C_C122_TWO_ROW_SCALAR_STORAGE_BANK_certificate.json"
C123_CERTIFICATE = HERE / "ROUTE_C_C123_ORDERED_PERMUTATION_FULL_PHASE_DUAL_certificate.json"
C120_MODEL_SOURCE = HERE / "ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate.py"

SCHEMA = "erdos1191.c125.ordered_suffix_five_row_bank.v1"
STATUS = "EXACT_FINITE_FIVE_ROW_TWO_COLUMN_OUTER_BANK_FEASIBLE_C058_OPEN"

ROW12_SOURCE_SHA256 = "8c30fc674f40c2376df7ff2f6bec3b318c9a48710f347197109c3863ee84d0ec"
ROW12_INTERNAL_SHA256 = "6a991d9bb13646ca98d695f9572d9950a5a784683370e8c61177aca0ed7fb498"
ROW3_SOURCE_SHA256 = "2bcad3750da0f885260f03a5e1d5f251a7901e21c16d59fe61d4d1fd75215348"
ROW3_INTERNAL_SHA256 = "782cdd7c958dc9ccbb37a5442f23c8e49c2dcceada185ac2eb5919b515fcd80b"
C121_CERTIFICATE_SHA256 = "1288d87e095a47f9fdf679a40656bafdef4ad4b03150ccb3254b25b043937a0b"
C122_CERTIFICATE_SHA256 = "a9d30fa24e134b5884988e618b7ebb0b9342c26fb87b6174939c4f2b362d8900"
C123_CERTIFICATE_SHA256 = "91eb0e02db28909fe1cd49a31a50fe2589089b28521f11e1951b58521db42491"
C120_MODEL_SHA256 = "6e8d7e3f975e952442672cb1d18e4512d616f343bb4f6379ba0c8701cd996fe9"

ROW12_POINTS = (
    0, 22, 60, 83, 102, 312, 442, 513,
    579, 682, 791, 882, 944, 1055, 1100, 1169,
)
ROW3_POINTS = (
    0, 22, 60, 83, 102, 173, 303, 513,
    579, 690, 759, 868, 930, 1021, 1124, 1169,
)
RHO = F(9, 16)
PHASE_LOWER = F(295, 4)
PHASE_UPPER = F(295, 2)
ROW12_NORMALIZED_UPPER_FENCE = F(42_845_139, 1_000_000_000)
ROW3_NORMALIZED_UPPER_FENCE = F(6_627_733, 100_000_000)

DELTA_V_POSITIVE = F(3_440_812_085, 9_234_857_208)
DELTA_V_NEGATIVE_ABS = F(443_620_417, 1_928_247_678)
DELTA_VRT_C118 = F(601_940, 4_033_029)
DELTA_VRT_C120_ABS = F(13_171, 58_179)
DELTA_VRT_C123 = F(51_059, 581_790)
DELTA_VRT_ROW12 = F(113, 26_445)
DELTA_VRT_ROW3_ABS = F(12_913, 58_179)

CANDIDATE_EPSILON = F(1, 1000)
CANDIDATE_A = F(1, 1000)
CANDIDATE_B = F(1, 2)
CANDIDATE_C = F(1, 10)
CANDIDATE_E2 = F(0)
MIN_DUAL_UPPER_GAP = F(1, 10_000)
LOG_TERMS = 30

EXPECTED_SOURCES = {
    "C121_certificate": C121_CERTIFICATE.name,
    "C121_certificate_sha256": C121_CERTIFICATE_SHA256,
    "C122_certificate": C122_CERTIFICATE.name,
    "C122_certificate_sha256": C122_CERTIFICATE_SHA256,
    "C123_certificate": C123_CERTIFICATE.name,
    "C123_certificate_sha256": C123_CERTIFICATE_SHA256,
    "C120_model": C120_MODEL_SOURCE.name,
    "C120_model_sha256": C120_MODEL_SHA256,
    "index12_dual": ROW12_SOURCE.name,
    "index12_dual_sha256": ROW12_SOURCE_SHA256,
    "index12_dual_internal_sha256": ROW12_INTERNAL_SHA256,
    "index3_dual": ROW3_SOURCE.name,
    "index3_dual_sha256": ROW3_SOURCE_SHA256,
    "index3_dual_internal_sha256": ROW3_INTERNAL_SHA256,
}
EXPECTED_REPLAY = {
    "index12_phase": ["295/4", "295/2"],
    "index12_phase_chambers": 149,
    "index12_epoch_duals": 298,
    "index12_dual_weights": 91784,
    "index12_endpoint_positive_definite_checks": 596,
    "index12_normalized_upper_less_than": "42845139/1000000000",
    "index3_phase": ["295/4", "295/2"],
    "index3_phase_chambers": 155,
    "index3_epoch_duals": 310,
    "index3_dual_weights": 95480,
    "index3_endpoint_positive_definite_checks": 620,
    "index3_normalized_upper_less_than": "6627733/100000000",
}
EXPECTED_CANDIDATE = {
    "epsilon": "1/1000",
    "A": "1/1000",
    "B": "1/2",
    "C_ordered_suffix": "1/10",
    "e2": "0/1",
    "all_five_certified_dual_upper_gaps_greater_than": "1/10000",
    "outer_necessary_bank_infeasible": False,
    "local_master_inequality_proved": False,
}
EXPECTED_SCOPE = {
    "five_fixed_16_mark_rows_only": True,
    "same_C119_scalar_and_C124_ordered_suffix_columns_only": True,
    "adaptive_row_dependent_phase_rule_only": True,
    "phase_representative_independence_proved": False,
    "independent_epoch_block_cone_only": True,
    "explicit_rational_candidate_not_separated_by_stored_dual_uppers": True,
    "outer_bank_infeasible": False,
    "primal_phase_witnesses_for_candidate_constructed": False,
    "arbitrary_rank_proved": False,
    "global_owner_ledger_constructed": False,
    "C058_resolved": False,
    "Q1_Q2_resolved": False,
    "publication_novelty_or_prize_claimed": False,
}

TOP_KEYS = {"schema", "status", "sources", "replay", "candidate", "scope", "integrity"}
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
        "candidate": dict(EXPECTED_CANDIDATE),
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
    if value["candidate"] != EXPECTED_CANDIDATE:
        raise CertificateError("candidate statement changed")
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


def _log_interval(x: F) -> tuple[F, F]:
    if x < 1:
        raise CertificateError("log interval requires x>=1")
    z = (x - 1) / (x + 1)
    lower = 2 * sum(
        (z ** (2 * k + 1) / (2 * k + 1) for k in range(LOG_TERMS)), F()
    )
    tail = 2 * z ** (2 * LOG_TERMS + 1) / (
        (2 * LOG_TERMS + 1) * (1 - z * z)
    )
    return lower, lower + tail


def _load_model(points: tuple[int, ...], tag: str) -> Any:
    raw = C120_MODEL_SOURCE.read_bytes()
    if hashlib.sha256(raw).hexdigest() != C120_MODEL_SHA256:
        raise CertificateError("C120 model source sha256 mismatch")
    spec = importlib.util.spec_from_file_location(f"c125_model_{tag}", C120_MODEL_SOURCE)
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


def _replay_new_row(
    *,
    path: Path,
    file_sha: str,
    internal_sha: str,
    points: tuple[int, ...],
    chamber_count: int,
    normalized_fence: F,
    tag: str,
) -> dict[str, Any]:
    source = _read_pinned_json(path, file_sha, tag)
    if set(source) != SOURCE_TOP_KEYS:
        raise CertificateError(f"{tag}: source schema keys differ")
    if source["schema"] != "erdos1191.c058_eta_negative_full_phase_dual.discovery.v1":
        raise CertificateError(f"{tag}: source schema changed")
    without_hash = dict(source)
    internal = without_hash.pop("payload_sha256_without_hash")
    if internal != internal_sha or _object_hash(without_hash) != internal:
        raise CertificateError(f"{tag}: internal payload hash mismatch")
    if tuple(source["points"]) != points or F(source["rho"]) != RHO:
        raise CertificateError(f"{tag}: fixture changed")
    if source["base"] != "295/4" or source["H2"] != 430 or source["H3"] != 656:
        raise CertificateError(f"{tag}: phase or shell spans changed")
    if source["eta_ratio"] != "82/215":
        raise CertificateError(f"{tag}: eta ratio changed")

    model = _load_model(points, tag)
    breakpoints = tuple(F(text) for text in source["breakpoints"])
    if breakpoints != model._breakpoints() or len(breakpoints) != chamber_count + 1:
        raise CertificateError(f"{tag}: breakpoint partition changed")
    records = source["records"]
    if type(records) is not list or len(records) != chamber_count:
        raise CertificateError(f"{tag}: chamber count changed")

    raw_lower = F()
    raw_upper = F()
    dual_count = 0
    weight_count = 0
    endpoint_pd_count = 0
    for index, (record, left, right) in enumerate(zip(records, breakpoints, breakpoints[1:])):
        if record["index"] != index or F(record["left"]) != left or F(record["right"]) != right:
            raise CertificateError(f"{tag} chamber {index}: interval changed")
        for epoch, key in ((4, "n4"), (8, "n8")):
            dual = record[key]
            denominator = int(dual["denominator"])
            weights = tuple(int(weight) for weight in dual["weights"])
            if denominator <= 0 or len(weights) != 308 or min(weights) < 0:
                raise CertificateError(f"{tag} chamber {index}, epoch {epoch}: dual data")
            hc, ho, weighted, dc, do, objective = model._dual_epoch_reconstruction(
                left, right, epoch, denominator, weights
            )
            if dc != F(record[f"Dc{epoch}"]) or do != F(record[f"Do{epoch}"]):
                raise CertificateError(f"{tag} chamber {index}, epoch {epoch}: demand")
            if objective != F(dual["objective"]):
                raise CertificateError(f"{tag} chamber {index}, epoch {epoch}: objective")
            for endpoint in (left, right):
                slack = model._integer_slack(hc, ho, weighted, denominator, endpoint)
                if not model._bareiss_positive_definite(slack):
                    raise CertificateError(
                        f"{tag} chamber {index}, epoch {epoch}: endpoint slack not PD"
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
    if not normalized_lower <= normalized_upper < normalized_fence:
        raise CertificateError(f"{tag}: normalized upper fence failed")
    return {
        "phase_chambers": chamber_count,
        "epoch_duals": dual_count,
        "dual_weights": weight_count,
        "endpoint_pd_checks": endpoint_pd_count,
        "raw_lower": raw_lower,
        "raw_upper": raw_upper,
        "normalized_lower": normalized_lower,
        "normalized_upper": normalized_upper,
    }


_REPLAY_CACHE: dict[str, Any] | None = None


def _replay_sources() -> dict[str, Any]:
    global _REPLAY_CACHE
    if _REPLAY_CACHE is not None:
        return copy.deepcopy(_REPLAY_CACHE)

    c121_value = _read_pinned_json(C121_CERTIFICATE, C121_CERTIFICATE_SHA256, "C121")
    c122_value = _read_pinned_json(C122_CERTIFICATE, C122_CERTIFICATE_SHA256, "C122")
    c123_value = _read_pinned_json(C123_CERTIFICATE, C123_CERTIFICATE_SHA256, "C123")
    s121 = c121.verify_certificate(c121_value)
    s122 = c122.verify_certificate(c122_value)
    s123 = c123.verify_certificate(c123_value)
    if not s121["normalized_upper"] < -F(83, 2000):
        raise CertificateError("C121 upper changed")
    if not s122["reverse_normalized_upper"] < F(19, 250):
        raise CertificateError("C120 upper changed")
    if not s123["normalized_upper"] < F(73, 2000):
        raise CertificateError("C123 upper changed")

    row12 = _replay_new_row(
        path=ROW12_SOURCE,
        file_sha=ROW12_SOURCE_SHA256,
        internal_sha=ROW12_INTERNAL_SHA256,
        points=ROW12_POINTS,
        chamber_count=149,
        normalized_fence=ROW12_NORMALIZED_UPPER_FENCE,
        tag="index12",
    )
    row3 = _replay_new_row(
        path=ROW3_SOURCE,
        file_sha=ROW3_SOURCE_SHA256,
        internal_sha=ROW3_INTERNAL_SHA256,
        points=ROW3_POINTS,
        chamber_count=155,
        normalized_fence=ROW3_NORMALIZED_UPPER_FENCE,
        tag="index3",
    )

    _, log_plus_upper = _log_interval(F(1768, 1659))
    _, log_minus_upper = _log_interval(F(215, 82))
    common = CANDIDATE_EPSILON + CANDIDATE_A * log_minus_upper
    target_upper = {
        "C118": (
            CANDIDATE_EPSILON + CANDIDATE_A * log_plus_upper
            - CANDIDATE_B * DELTA_V_POSITIVE
            - CANDIDATE_C * DELTA_VRT_C118
        ) / 3 - CANDIDATE_E2,
        "C120": (
            common + CANDIDATE_B * DELTA_V_NEGATIVE_ABS
            + CANDIDATE_C * DELTA_VRT_C120_ABS
        ) / 3 - CANDIDATE_E2,
        "C123": (
            common + CANDIDATE_B * DELTA_V_NEGATIVE_ABS
            - CANDIDATE_C * DELTA_VRT_C123
        ) / 3 - CANDIDATE_E2,
        "index12": (
            common + CANDIDATE_B * DELTA_V_NEGATIVE_ABS
            - CANDIDATE_C * DELTA_VRT_ROW12
        ) / 3 - CANDIDATE_E2,
        "index3": (
            common + CANDIDATE_B * DELTA_V_NEGATIVE_ABS
            + CANDIDATE_C * DELTA_VRT_ROW3_ABS
        ) / 3 - CANDIDATE_E2,
    }
    dual_upper = {
        "C118": s121["normalized_upper"],
        "C120": s122["reverse_normalized_upper"],
        "C123": s123["normalized_upper"],
        "index12": row12["normalized_upper"],
        "index3": row3["normalized_upper"],
    }
    strict_margins = {name: dual_upper[name] - target_upper[name] for name in dual_upper}
    if not all(margin > MIN_DUAL_UPPER_GAP for margin in strict_margins.values()):
        raise CertificateError("rational candidate no longer clears every stored dual upper")

    summary = {
        "new_rows": {"index12": row12, "index3": row3},
        "candidate_epsilon": CANDIDATE_EPSILON,
        "candidate_A": CANDIDATE_A,
        "candidate_B": CANDIDATE_B,
        "candidate_C": CANDIDATE_C,
        "candidate_e2": CANDIDATE_E2,
        "target_upper": target_upper,
        "certified_dual_upper": dual_upper,
        "strict_margins": strict_margins,
        "outer_bank_infeasible": False,
    }
    _REPLAY_CACHE = copy.deepcopy(summary)
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
    add("row12-hash", lambda x: x["sources"].__setitem__("index12_dual_sha256", "0" * 64))
    add("row3-hash", lambda x: x["sources"].__setitem__("index3_dual_sha256", "0" * 64))
    add("row12-count", lambda x: x["replay"].__setitem__("index12_phase_chambers", 148))
    add("row3-fence", lambda x: x["replay"].__setitem__("index3_normalized_upper_less_than", "1/15"))
    add("candidate-B", lambda x: x["candidate"].__setitem__("B", "2/3"))
    add("candidate-margin", lambda x: x["candidate"].__setitem__("all_five_certified_dual_upper_gaps_greater_than", "0/1"))
    add("false-infeasible", lambda x: x["candidate"].__setitem__("outer_necessary_bank_infeasible", True))
    add("scope-phase", lambda x: x["scope"].__setitem__("phase_representative_independence_proved", True))
    add("scope-C058", lambda x: x["scope"].__setitem__("C058_resolved", True))
    add("scope-Q", lambda x: x["scope"].__setitem__("Q1_Q2_resolved", True))

    rejected = 0
    for label, changed in mutations:
        try:
            verify_certificate(changed)
        except (CertificateError, c121.CertificateError, c122.CertificateError, c123.CertificateError):
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
        "rows=5",
        f"index12_chambers={summary['new_rows']['index12']['phase_chambers']}",
        f"index3_chambers={summary['new_rows']['index3']['phase_chambers']}",
        "candidate_epsilon=A=1/1000",
        "candidate_B=1/2",
        "candidate_C=1/10",
        "all_dual_upper_gaps>1/10000",
        f"outer_bank_infeasible={summary['outer_bank_infeasible']}",
        f"mutations_rejected={mutations['mutations_rejected']}",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
