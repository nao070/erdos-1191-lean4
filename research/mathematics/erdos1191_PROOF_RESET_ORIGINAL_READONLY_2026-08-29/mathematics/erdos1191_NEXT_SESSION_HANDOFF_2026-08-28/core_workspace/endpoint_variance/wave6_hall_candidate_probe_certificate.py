"""Generate the exact Wave 6 adjacent-epoch Hall-candidate certificate."""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from fractions import Fraction
from pathlib import Path
from typing import Any

from wave6_hall_candidate_probe import (
    COUNTEREXAMPLE_32_POINTS,
    COUNTEREXAMPLE_64_POINTS,
    COUNTEREXAMPLE_POINTS,
    CandidateWitnessAudit,
    NNFamily,
    NNPressure,
    adjacent_nn_pressure,
    audit_candidate_witness,
    scaled_candidate_value,
    targeted_extension_search,
)

EXPECTED_ARITHMETIC_MINING_HASH = (
    "16a5e07165c767fe714f1044ae4c7c490265428e746653cfe40c385f0e9e671a"
)
SOURCE_DEPENDENCIES = (
    "wave6_hall_candidate_probe.py",
    "wave6_hall_candidate_probe_certificate.py",
    "test_wave6_hall_candidate_probe.py",
)


def canonical_hash(payload: dict[str, Any]) -> str:
    """Hash a JSON-compatible mapping with the package's canonical encoding."""
    rendered = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(rendered).hexdigest()


def source_hashes() -> dict[str, str]:
    directory = Path(__file__).parent
    return {
        name: hashlib.sha256((directory / name).read_bytes()).hexdigest()
        for name in SOURCE_DEPENDENCIES
    }


def _family_payload(family: NNFamily) -> dict[str, object]:
    return {
        "epoch": family.epoch,
        "lag": family.lag,
        "demand": family.demand,
        "lower": family.lower,
        "upper": family.upper,
        "differences": list(family.differences),
    }


def _pressure_payload(pressure: NNPressure) -> dict[str, object]:
    return {
        "old_epoch": pressure.old_epoch,
        "new_epoch": pressure.new_epoch,
        "lower": pressure.lower,
        "upper": pressure.upper,
        "width": pressure.width,
        "demand": pressure.demand,
        "ratio": str(pressure.ratio),
        "scaled_value": str(
            scaled_candidate_value(pressure, old_epoch=pressure.old_epoch)
        ),
        "candidate_holds": (
            scaled_candidate_value(pressure, old_epoch=pressure.old_epoch) <= 1
        ),
        "families": [_family_payload(row) for row in pressure.families],
    }


def _audit_payload(
    audit: CandidateWitnessAudit, transition_epochs: tuple[int, ...]
) -> dict[str, object]:
    return {
        "points": list(audit.points),
        "mark_count": len(audit.points),
        "pair_count": audit.pair_count,
        "difference_count": audit.difference_count,
        "is_golomb": audit.is_golomb,
        "sorted_difference_serialization": (
            "ascending decimal integers, one per line, final newline"
        ),
        "sorted_difference_sha256": audit.sorted_difference_sha256,
        "prefix_counts": list(range(2, len(audit.points) + 1)),
        "prefix_moduli": list(audit.prefix_moduli),
        "prefix_caps_floor_2n2_log_n": list(audit.prefix_caps),
        "all_prefix_c1": audit.all_prefix_c1,
        "transitions": [
            _pressure_payload(
                adjacent_nn_pressure(audit.points, old_epoch=old_epoch)
            )
            for old_epoch in transition_epochs
        ],
    }


def _load_authenticated_fixture_points(
    path: Path,
) -> tuple[str, tuple[tuple[str, tuple[int, ...]], ...], tuple[int, ...]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    recorded_hash = payload.pop("certificate_sha256", None)
    if not isinstance(recorded_hash, str) or canonical_hash(payload) != recorded_hash:
        raise ValueError("arithmetic-mining certificate hash mismatch")
    if recorded_hash != EXPECTED_ARITHMETIC_MINING_HASH:
        raise ValueError("unexpected arithmetic-mining certificate")

    retained: list[tuple[str, tuple[int, ...]]] = []
    for index, row in enumerate(payload["sixty_four_mark_witnesses"]):
        source = row["source"]
        label = (
            f"{source['objective']}_{source['witness_index']}"
            f"_parent_{source['parent_index']}"
        )
        points = tuple(row["arithmetic_audit"]["points"])
        if len(points) != 64:
            raise ValueError(f"retained fixture {index} does not have 64 marks")
        retained.append((label, points))
    if len(retained) != 6:
        raise ValueError("expected exactly six retained 64-mark fixtures")

    continuation = tuple(
        payload["heuristic_extension_128"]["arithmetic_audit"]["points"]
    )
    if len(continuation) != 128:
        raise ValueError("retained continuation does not have 128 marks")
    return recorded_hash, tuple(retained), continuation


def _authenticated_fixture_comparison(directory: Path) -> dict[str, object]:
    parent_hash, retained, continuation = _load_authenticated_fixture_points(
        directory / "wave6_arithmetic_mining_certificate_2026-08-28.json"
    )
    rows: list[dict[str, object]] = []
    for label, points in retained:
        rows.append(
            {
                "source": label,
                "mark_count": 64,
                "transitions": [
                    _pressure_payload(
                        adjacent_nn_pressure(points, old_epoch=old_epoch)
                    )
                    for old_epoch in (8, 16, 32)
                ],
            }
        )
    rows.append(
        {
            "source": "retained_128_continuation",
            "mark_count": 128,
            "transitions": [
                _pressure_payload(
                    adjacent_nn_pressure(continuation, old_epoch=old_epoch)
                )
                for old_epoch in (8, 16, 32, 64)
            ],
        }
    )
    transition_rows = [
        transition
        for row in rows
        for transition in row["transitions"]  # type: ignore[index]
    ]
    scaled_values = tuple(
        Fraction(transition["scaled_value"]) for transition in transition_rows
    )
    return {
        "parent_certificate_sha256": parent_hash,
        "fixed_source_count": len(rows),
        "transition_instance_count": len(transition_rows),
        "all_candidate_holds": all(value <= 1 for value in scaled_values),
        "maximum_scaled_value": str(max(scaled_values)),
        "endpoint_scan_complete_for_each_fixed_source": True,
        "selection_is_not_exhaustive_over_golomb_rulers": True,
        "sources": rows,
    }


def replay_targeted_searches() -> dict[str, object]:
    """Replay the two deterministic discovery beams and require exact output."""
    search_32 = targeted_extension_search(
        COUNTEREXAMPLE_POINTS,
        target_count=32,
        beam_width=128,
        candidates_per_state=96,
        seed=861191,
        target_gap=250,
    )
    search_64 = targeted_extension_search(
        COUNTEREXAMPLE_32_POINTS,
        target_count=64,
        beam_width=16,
        candidates_per_state=32,
        seed=862191,
        target_gap=500,
    )
    if (
        search_32.best_points != COUNTEREXAMPLE_32_POINTS
        or search_32.expanded_state_count != 528317
    ):
        raise RuntimeError("32-mark beam replay did not match the certificate")
    if (
        search_64.best_points != COUNTEREXAMPLE_64_POINTS
        or search_64.expanded_state_count != 39716
    ):
        raise RuntimeError("64-mark beam replay did not match the certificate")
    return {
        "search_32_matches": True,
        "search_32_expanded_state_count": search_32.expanded_state_count,
        "search_64_matches": True,
        "search_64_expanded_state_count": search_64.expanded_state_count,
    }


def build_certificate() -> dict[str, Any]:
    directory = Path(__file__).parent
    audit_16 = audit_candidate_witness(COUNTEREXAMPLE_POINTS, old_epoch=8)
    audit_32 = audit_candidate_witness(COUNTEREXAMPLE_32_POINTS, old_epoch=16)
    audit_64 = audit_candidate_witness(COUNTEREXAMPLE_64_POINTS, old_epoch=32)
    if not all(
        audit.is_golomb and audit.all_prefix_c1 and not audit.candidate_holds
        for audit in (audit_16, audit_32, audit_64)
    ):
        raise RuntimeError("a retained counterexample failed its exact audit")

    payload: dict[str, Any] = {
        "schema": "wave6_hall_candidate_probe_certificate_v1",
        "research_date": "2026-08-28",
        "purpose": (
            "Exact finite falsification of the proposed adjacent-epoch NN "
            "Hall-pressure inequality under Golomb and all-prefix C=1."
        ),
        "candidate": {
            "definition": "R_n = 16*n*Lambda_NN(n,2n)^2",
            "proposed_bound": "R_n <= 1",
            "integer_width_convention": "upper-lower+1",
            "family_filter": "NN, demand at least two, two represented epochs",
        },
        "conclusion": {
            "universal_candidate_refuted": True,
            "first_recorded_counterexample_transition": [8, 16],
            "one_ruler_has_three_consecutive_violations": True,
            "claim_of_shortest_or_optimal_ruler": False,
        },
        "earliest_feasible_level": {
            "old_epoch": 8,
            "reason": (
                "At old epoch 4 the newborn block has two ranks, so every NN "
                "lag family has demand at most one and the demand>=2 filter "
                "cannot represent that epoch. At old epoch 8, NN lag 1 and "
                "lag 2 have demands 3 and 2."
            ),
            "family_feasibility_complete": True,
            "ruler_search_complete": False,
        },
        "counterexamples": {
            "marks_16": _audit_payload(audit_16, (8,)),
            "marks_32": _audit_payload(audit_32, (8, 16)),
            "marks_64": _audit_payload(audit_64, (8, 16, 32)),
        },
        "discovery_searches": [
            {
                "parent_count": 16,
                "target_count": 32,
                "beam_width": 128,
                "candidates_per_state": 96,
                "seed": 861191,
                "target_gap": 250,
                "expanded_state_count": 528317,
                "complete": False,
            },
            {
                "parent_count": 32,
                "target_count": 64,
                "beam_width": 16,
                "candidates_per_state": 32,
                "seed": 862191,
                "target_gap": 500,
                "expanded_state_count": 39716,
                "complete": False,
            },
        ],
        "authenticated_fixture_comparison": _authenticated_fixture_comparison(
            directory
        ),
        "scope": {
            "fixed_witness_difference_and_prefix_audits_complete": True,
            "fixed_witness_endpoint_scans_complete": True,
            "beam_search_complete": False,
            "all_golomb_rulers_enumerated": False,
            "asymptotic_claim": False,
            "optimality_claim": False,
        },
        "reproducibility": {
            "python": platform.python_version(),
            "generate_command": (
                "python wave6_hall_candidate_probe_certificate.py "
                "--replay-search"
            ),
            "focused_test_command": (
                "pytest -q test_wave6_hall_candidate_probe.py"
            ),
            "search_replay_is_optional_for_exact_witness_audit": True,
            "source_sha256": source_hashes(),
        },
    }
    payload["certificate_sha256"] = canonical_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name(
            "wave6_hall_candidate_probe_certificate_2026-08-28.json"
        ),
    )
    parser.add_argument("--replay-search", action="store_true")
    args = parser.parse_args()
    if args.replay_search:
        replay_targeted_searches()
    payload = build_certificate()
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(payload["certificate_sha256"])


if __name__ == "__main__":
    main()
