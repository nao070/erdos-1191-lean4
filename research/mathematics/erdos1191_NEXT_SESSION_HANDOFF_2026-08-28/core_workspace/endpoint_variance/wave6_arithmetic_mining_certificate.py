"""Generate the exact Wave 6 arithmetic-mining certificate."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
from typing import Any

from wave4_nested_search import NestedWitnessAudit, audit_nested_witness
from wave5_cross_epoch import build_sawtooth_gap_profile
from wave5_nested_search import (
    ExtensionWitness,
    ProfilePersistence,
    ResetProfile,
    beam_extend_nested,
)
from wave6_arithmetic_mining_search import (
    ArithmeticWitnessAudit,
    CategorySpectrumAudit,
    HallPressureAudit,
    LagFamilyAudit,
    TransitionPackingAudit,
    audit_arithmetic_witness,
)


EXPECTED_WAVE5_HASH = (
    "a26c13574002eb442731bcbec465a5fa7553a25728e2225ddba942e6df4d3ceb"
)
SOURCE_DEPENDENCIES = (
    "wave6_arithmetic_mining_search.py",
    "wave6_arithmetic_mining_certificate.py",
    "wave6_arithmetic_mining_test.py",
    "wave5_nested_search.py",
    "wave5_cross_epoch.py",
    "wave4_nested_search.py",
    "gap_measure_dynamics.py",
    "sidon_block_variance.py",
    "endpoint_variance.py",
)


@dataclass(frozen=True)
class AuthenticatedWave5Witness:
    objective: str
    seed: int
    witness_index: int
    parent_index: int
    points: tuple[int, ...]
    recorded_difference_sha256: str
    minimum_gap_variance: str
    minimum_innovation_q00_per_modulus: str
    final_innovation_q00_per_modulus: str
    latest_normalized_signed_overlap: str


def canonical_hash(payload: dict[str, Any]) -> str:
    canonical = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def difference_hash(differences: tuple[int, ...]) -> str:
    canonical = json.dumps(
        list(differences), separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def source_hashes() -> dict[str, str]:
    directory = Path(__file__).parent
    return {
        name: hashlib.sha256((directory / name).read_bytes()).hexdigest()
        for name in SOURCE_DEPENDENCIES
    }


def load_authenticated_wave5(
    path: Path,
) -> tuple[str, tuple[AuthenticatedWave5Witness, ...]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    recorded_hash = payload.pop("certificate_sha256", None)
    if not isinstance(recorded_hash, str) or canonical_hash(payload) != recorded_hash:
        raise ValueError("Wave 5 certificate hash mismatch")
    if recorded_hash != EXPECTED_WAVE5_HASH:
        raise ValueError("Wave 5 certificate is not the required canonical input")
    if payload.get("schema") != "wave5_nested_extension_certificate_v2":
        raise ValueError("unexpected Wave 5 certificate schema")
    witnesses: list[AuthenticatedWave5Witness] = []
    for run in payload.get("runs", []):
        objective = run.get("objective")
        if objective not in {"persistence", "innovation"}:
            raise ValueError("unexpected Wave 5 objective")
        seed = run.get("seed")
        if not isinstance(seed, int):
            raise ValueError("Wave 5 seed is not an integer")
        for witness_index, row in enumerate(run.get("witnesses", [])):
            persistence_rows = row.get("cross_epoch_persistence", [])
            if not persistence_rows:
                raise ValueError("Wave 5 witness lacks persistence history")
            witnesses.append(
                AuthenticatedWave5Witness(
                    objective=objective,
                    seed=seed,
                    witness_index=witness_index,
                    parent_index=row["parent_index"],
                    points=tuple(row["points"]),
                    recorded_difference_sha256=row["difference_sha256"],
                    minimum_gap_variance=row["minimum_gap_variance"],
                    minimum_innovation_q00_per_modulus=(
                        row["minimum_innovation_q00_per_modulus"]
                    ),
                    final_innovation_q00_per_modulus=(
                        row["final_innovation_q00_per_modulus"]
                    ),
                    latest_normalized_signed_overlap=(
                        persistence_rows[-1]["normalized_signed_overlap"]
                    ),
                )
            )
    expected_labels = [
        (objective, witness_index)
        for objective in ("persistence", "innovation")
        for witness_index in range(3)
    ]
    if [(row.objective, row.witness_index) for row in witnesses] != expected_labels:
        raise ValueError("Wave 5 certificate does not contain the six retained records")
    if any(len(row.points) != 64 for row in witnesses):
        raise ValueError("a Wave 5 retained witness does not have 64 marks")
    return recorded_hash, tuple(witnesses)


def _collisions_payload(
    collisions: tuple[tuple[int, tuple[tuple[int, int], ...]], ...],
) -> list[dict[str, object]]:
    return [
        {
            "difference": difference,
            "pairs": [list(pair) for pair in pairs],
        }
        for difference, pairs in collisions
    ]


def _family_key(family: LagFamilyAudit) -> list[object]:
    return [family.epoch, family.category, family.lag]


def _family_payload(family: LagFamilyAudit) -> dict[str, object]:
    return {
        "epoch": family.epoch,
        "category": family.category,
        "lag": family.lag,
        "pairs": [list(pair) for pair in family.pairs],
        "differences": list(family.differences),
        "demand": family.demand,
        "distinct_count": family.distinct_count,
        "collision_deficit": family.collision_deficit,
        "lower": family.lower,
        "upper": family.upper,
        "width": family.width,
    }


def _hall_payload(pressure: HallPressureAudit | None) -> dict[str, object] | None:
    if pressure is None:
        return None
    return {
        "lower": pressure.lower,
        "upper": pressure.upper,
        "width": pressure.width,
        "demand": pressure.demand,
        "ratio": str(pressure.ratio),
        "represented_epochs": list(pressure.represented_epochs),
        "families": [_family_key(family) for family in pressure.families],
    }


def _spectrum_payload(spectrum: CategorySpectrumAudit) -> dict[str, object]:
    return {
        "category": spectrum.category,
        "pair_count": spectrum.pair_count,
        "distinct_count": spectrum.distinct_count,
        "collision_deficit": spectrum.collision_deficit,
        "lower": spectrum.lower,
        "upper": spectrum.upper,
        "width": spectrum.width,
        "differences": list(spectrum.differences),
        "collisions": _collisions_payload(spectrum.collisions),
    }


def _transition_payload(row: TransitionPackingAudit) -> dict[str, object]:
    return {
        "old_count": row.old_count,
        "new_count": row.new_count,
        "old_new": _spectrum_payload(row.old_new),
        "new_new": _spectrum_payload(row.new_new),
        "overlap_lower": row.overlap_lower,
        "overlap_upper": row.overlap_upper,
        "overlap_width": row.overlap_width,
        "old_new_occupied_in_overlap": list(
            row.old_new_occupied_in_overlap
        ),
        "new_new_occupied_in_overlap": list(
            row.new_new_occupied_in_overlap
        ),
        "cross_collision_values": list(row.cross_collision_values),
    }


def arithmetic_audit_payload(
    audit: ArithmeticWitnessAudit,
) -> dict[str, object]:
    return {
        "points": list(audit.points),
        "pair_count": audit.pair_count,
        "distinct_difference_count": len(audit.sorted_differences),
        "all_positive_differences": list(audit.sorted_differences),
        "difference_sha256": difference_hash(audit.sorted_differences),
        "difference_collisions": _collisions_payload(
            audit.difference_collisions
        ),
        "is_golomb": audit.is_golomb,
        "family_pair_count": sum(row.demand for row in audit.families),
        "birth_lag_families": [
            _family_payload(row) for row in audit.families
        ],
        "transition_packing": [
            _transition_payload(row) for row in audit.transitions
        ],
        "adjacent_nn_hall_pressure": [
            {
                "epochs": list(row.epochs),
                "pressure": _hall_payload(row.pressure),
            }
            for row in audit.adjacent_nn_pressures
        ],
        "all_epoch_nn_hall_pressure": _hall_payload(
            audit.all_epoch_nn_pressure
        ),
    }


def _nested_payload(audit: NestedWitnessAudit) -> dict[str, object]:
    return {
        "envelope_constant": str(audit.envelope_constant),
        "envelope_compatible": audit.envelope_compatible,
        "minimum_gap_variance": str(audit.minimum_gap_variance),
        "minimum_innovation_q00_per_modulus": str(
            audit.minimum_innovation_q00_per_modulus
        ),
        "all_prefix_envelope_rows": [
            {
                "mark_count": row.mark_count,
                "modulus": row.modulus,
                "critical_modulus_cap": row.critical_modulus_cap,
                "certified": row.certified,
            }
            for row in audit.envelope_rows
        ],
        "dyadic_rows": [
            {
                "mark_count": row.mark_count,
                "modulus": row.modulus,
                "gap_variance": str(row.gap_variance),
                "innovation_q00_per_modulus": str(
                    row.innovation_q00_per_modulus
                ),
            }
            for row in audit.rows
        ],
    }


def _profile_payload(profile: ResetProfile) -> dict[str, object]:
    return {
        "old_count": profile.old_count,
        "new_count": profile.new_count,
        "old_modulus": profile.old_modulus,
        "new_modulus": profile.new_modulus,
        "shell_growth": profile.shell_growth,
        "signed_cells": [str(value) for value in profile.signed_cells],
        "cumulative": [str(value) for value in profile.cumulative],
        "maximum_absolute_cumulative": str(
            profile.maximum_absolute_cumulative
        ),
        "extremum_boundary": str(profile.extremum_boundary),
        "extremum_sign": profile.extremum_sign,
        "l1_mass": str(profile.l1_mass),
    }


def _persistence_payload(row: ProfilePersistence) -> dict[str, object]:
    return {
        "coarse_cell_count": row.coarse_cell_count,
        "fine_cell_count": row.fine_cell_count,
        "coarsening_factor": row.coarsening_factor,
        "coarsened_fine": [str(value) for value in row.coarsened_fine],
        "aligned_mass": str(row.aligned_mass),
        "opposed_mass": str(row.opposed_mass),
        "signed_overlap": str(row.signed_overlap),
        "normalization_mass": str(row.normalization_mass),
        "normalized_signed_overlap": str(row.normalized_signed_overlap),
    }


def _extension_score_payload(witness: ExtensionWitness) -> dict[str, object]:
    return {
        "minimum_gap_variance": str(witness.minimum_gap_variance),
        "minimum_innovation_q00_per_modulus": str(
            witness.minimum_innovation_q00_per_modulus
        ),
        "final_innovation_q00_per_modulus": str(
            witness.final_innovation_q00_per_modulus
        ),
        "latest_persistence": _persistence_payload(
            witness.latest_persistence
        ),
        "reset_profiles": [
            _profile_payload(row) for row in witness.history.profiles
        ],
        "cross_epoch_persistence": [
            _persistence_payload(row) for row in witness.history.persistence
        ],
    }


def _assert_matching_difference_audits(
    arithmetic: ArithmeticWitnessAudit, nested: NestedWitnessAudit
) -> None:
    if (
        arithmetic.points != nested.points
        or arithmetic.pair_count != nested.difference_audit.pair_count
        or arithmetic.sorted_differences
        != nested.difference_audit.sorted_differences
        or arithmetic.difference_collisions
        != nested.difference_audit.collisions
    ):
        raise AssertionError("independent difference audits disagree")


def build_payload(
    *,
    wave5_certificate: Path,
    beam_width: int = 32,
    candidates_per_state: int = 16,
    seed: int = 601191,
    retain: int = 1,
) -> dict[str, object]:
    initial_source_hashes = source_hashes()
    wave5_file_sha256 = hashlib.sha256(wave5_certificate.read_bytes()).hexdigest()
    wave5_hash, wave5_witnesses = load_authenticated_wave5(wave5_certificate)

    mined_64: list[dict[str, object]] = []
    for source in wave5_witnesses:
        arithmetic = audit_arithmetic_witness(source.points)
        nested = audit_nested_witness(
            source.points, sizes=(4, 8, 16, 32, 64), constant=Fraction(1)
        )
        _assert_matching_difference_audits(arithmetic, nested)
        if not nested.envelope_compatible:
            raise AssertionError("a Wave 5 witness violates the C=1 envelope")
        if difference_hash(arithmetic.sorted_differences) != source.recorded_difference_sha256:
            raise AssertionError("a Wave 5 witness difference hash changed")
        mined_64.append(
            {
                "source": {
                    "objective": source.objective,
                    "seed": source.seed,
                    "witness_index": source.witness_index,
                    "parent_index": source.parent_index,
                    "recorded_difference_sha256": (
                        source.recorded_difference_sha256
                    ),
                    "minimum_gap_variance": source.minimum_gap_variance,
                    "minimum_innovation_q00_per_modulus": (
                        source.minimum_innovation_q00_per_modulus
                    ),
                    "final_innovation_q00_per_modulus": (
                        source.final_innovation_q00_per_modulus
                    ),
                    "latest_normalized_signed_overlap": (
                        source.latest_normalized_signed_overlap
                    ),
                },
                "arithmetic_audit": arithmetic_audit_payload(arithmetic),
                "nested_prefix_audit": _nested_payload(nested),
            }
        )

    sawtooth = build_sawtooth_gap_profile(6)
    sawtooth_audit = audit_arithmetic_witness(
        sawtooth.points, require_golomb=False
    )
    if sawtooth_audit.is_golomb:
        raise AssertionError("the sawtooth control unexpectedly became Golomb")

    leading_parent = wave5_witnesses[0]
    extension_result = beam_extend_nested(
        parents=(leading_parent.points,),
        sizes=(4, 8, 16, 32, 64, 128),
        constant=Fraction(1),
        objective="persistence",
        beam_width=beam_width,
        candidates_per_state=candidates_per_state,
        seed=seed,
        retain=retain,
    )
    if len(extension_result.witnesses) != retain:
        raise RuntimeError("the heuristic extension did not retain the requested witnesses")
    extension_witness = extension_result.witnesses[0]
    extension_arithmetic = audit_arithmetic_witness(extension_witness.points)
    _assert_matching_difference_audits(
        extension_arithmetic, extension_witness.nested_audit
    )
    if (
        extension_arithmetic.pair_count != 8128
        or not extension_witness.nested_audit.envelope_compatible
    ):
        raise AssertionError("the 128-mark witness failed its exact final audit")

    if source_hashes() != initial_source_hashes:
        raise RuntimeError("generator source changed during certificate build")
    return {
        "schema": "wave6_arithmetic_mining_certificate_v1",
        "research_date": "2026-08-28",
        "purpose": (
            "finite arithmetic-invariant calibration and counterexample "
            "discovery; not an asymptotic reset-renewal claim"
        ),
        "method": (
            "authenticated Wave 5 input; exact integer all-pairs, birth-lag, "
            "Hall-pressure, transition-packing, and C=1 prefix audits; one "
            "seeded heuristic 64-to-128 beam extension"
        ),
        "hall_statement": {
            "interval_family": (
                "F_(n,c,ell) partitions rank pairs by right-endpoint birth "
                "epoch, ON/NN category, and rank lag"
            ),
            "pressure": (
                "maximum contained family demand divided by inclusive integer "
                "interval width"
            ),
            "exact_finite_theorem": (
                "global difference injectivity implies every recorded Hall "
                "pressure is at most 1"
            ),
            "endpoint_scan_complete": True,
        },
        "wave5_input": {
            "filename": wave5_certificate.name,
            "internal_certificate_sha256": wave5_hash,
            "file_sha256": wave5_file_sha256,
            "retained_record_count": len(wave5_witnesses),
        },
        "reproducibility": {
            "canonical_byte_identity_scope": "recorded_python_runtime_only",
            "python_implementation": platform.python_implementation(),
            "python_version": platform.python_version(),
            "source_sha256": initial_source_hashes,
        },
        "sixty_four_mark_witnesses": mined_64,
        "sawtooth_64_control": {
            "explicitly_non_sidon": True,
            "smallest_repeated_difference": sawtooth.smallest_repeated_difference,
            "dyadic_moduli": list(sawtooth.dyadic_moduli),
            "levels": [
                {
                    "exponent": row.exponent,
                    "mark_count": row.mark_count,
                    "multiplier": row.multiplier,
                    "modulus": row.modulus,
                    "scalar_sidon_lower_bound": row.scalar_sidon_lower_bound,
                    "critical_c1_dyadic_bound": row.critical_c1_dyadic_bound,
                }
                for row in sawtooth.levels
            ],
            "arithmetic_audit": arithmetic_audit_payload(sawtooth_audit),
        },
        "heuristic_extension_128": {
            "search_is_exhaustive": False,
            "existence_after_exact_audit_is_finite_fact": True,
            "objective": extension_result.objective,
            "beam_width": extension_result.beam_width,
            "candidates_per_state": extension_result.candidates_per_state,
            "seed": extension_result.seed,
            "retain": extension_result.retain,
            "parent_count": extension_result.parent_count,
            "expanded_state_count": extension_result.expanded_state_count,
            "source_parent": {
                "objective": leading_parent.objective,
                "witness_index": leading_parent.witness_index,
                "difference_sha256": leading_parent.recorded_difference_sha256,
            },
            "scores": _extension_score_payload(extension_witness),
            "arithmetic_audit": arithmetic_audit_payload(extension_arithmetic),
            "nested_prefix_audit": _nested_payload(
                extension_witness.nested_audit
            ),
        },
    }


def load_certificate(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    recorded_hash = payload.pop("certificate_sha256", None)
    if not isinstance(recorded_hash, str) or canonical_hash(payload) != recorded_hash:
        raise ValueError("Wave 6 certificate hash mismatch")
    payload["certificate_sha256"] = recorded_hash
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--wave5-certificate",
        type=Path,
        default=Path(__file__).with_name(
            "wave5_nested_certificate_2026-08-28.json"
        ),
    )
    parser.add_argument("--beam-width", type=int, default=32)
    parser.add_argument("--candidates-per-state", type=int, default=16)
    parser.add_argument("--seed", type=int, default=601191)
    parser.add_argument("--retain", type=int, default=1)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name(
            "wave6_arithmetic_mining_certificate_2026-08-28.json"
        ),
    )
    arguments = parser.parse_args()
    payload = build_payload(
        wave5_certificate=arguments.wave5_certificate,
        beam_width=arguments.beam_width,
        candidates_per_state=arguments.candidates_per_state,
        seed=arguments.seed,
        retain=arguments.retain,
    )
    payload["certificate_sha256"] = canonical_hash(payload)
    arguments.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(arguments.output)


if __name__ == "__main__":
    main()
