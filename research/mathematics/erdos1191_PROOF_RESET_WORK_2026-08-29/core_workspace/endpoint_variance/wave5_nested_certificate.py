"""Generate a deterministic certificate for Wave 5 nested extensions."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform

from wave5_nested_search import ExtensionWitness, beam_extend_nested


def _canonical_hash(payload: dict[str, object]) -> str:
    canonical = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return hashlib.sha256(canonical).hexdigest()


def _difference_hash(differences: tuple[int, ...]) -> str:
    canonical = json.dumps(list(differences), separators=(",", ":")).encode()
    return hashlib.sha256(canonical).hexdigest()


def _source_hashes() -> dict[str, str]:
    directory = Path(__file__).parent
    return {
        name: hashlib.sha256((directory / name).read_bytes()).hexdigest()
        for name in (
            "wave5_nested_search.py",
            "wave5_nested_certificate.py",
            "wave4_nested_search.py",
            "gap_measure_dynamics.py",
            "sidon_block_variance.py",
            "endpoint_variance.py",
        )
    }


def _load_wave4(
    path: Path,
) -> tuple[str, tuple[tuple[int, ...], ...], list[dict[str, object]]]:
    payload = json.loads(path.read_text())
    recorded_hash = payload.pop("certificate_sha256")
    if _canonical_hash(payload) != recorded_hash:
        raise ValueError("Wave 4 certificate hash mismatch")
    parents: list[tuple[int, ...]] = []
    metadata: list[dict[str, object]] = []
    for run in payload["runs"]:
        for witness_index, witness in enumerate(run["witnesses"]):
            points = tuple(witness["points"])
            parents.append(points)
            metadata.append(
                {
                    "parent_index": len(parents) - 1,
                    "wave4_objective": run["objective"],
                    "wave4_seed": run["seed"],
                    "wave4_witness_index": witness_index,
                    "points": list(points),
                    "difference_sha256": witness["difference_sha256"],
                }
            )
    return recorded_hash, tuple(parents), metadata


def _profile_payload(profile: object) -> dict[str, object]:
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


def _persistence_payload(persistence: object) -> dict[str, object]:
    return {
        "coarse_cell_count": persistence.coarse_cell_count,
        "fine_cell_count": persistence.fine_cell_count,
        "coarsening_factor": persistence.coarsening_factor,
        "coarsened_fine": [str(value) for value in persistence.coarsened_fine],
        "aligned_mass": str(persistence.aligned_mass),
        "opposed_mass": str(persistence.opposed_mass),
        "signed_overlap": str(persistence.signed_overlap),
        "normalization_mass": str(persistence.normalization_mass),
        "normalized_signed_overlap": str(
            persistence.normalized_signed_overlap
        ),
    }


def _witness_payload(witness: ExtensionWitness) -> dict[str, object]:
    differences = witness.nested_audit.difference_audit.sorted_differences
    return {
        "parent_index": witness.parent_index,
        "points": list(witness.points),
        "pair_count": witness.nested_audit.difference_audit.pair_count,
        "all_positive_differences": list(differences),
        "difference_sha256": _difference_hash(differences),
        "difference_collisions": [
            [difference, [list(pair) for pair in pairs]]
            for difference, pairs in witness.nested_audit.difference_audit.collisions
        ],
        "independent_difference_audit_passed": (
            witness.nested_audit.difference_audit.is_golomb
        ),
        "envelope_compatible": witness.nested_audit.envelope_compatible,
        "all_prefix_envelope_rows": [
            {
                "mark_count": row.mark_count,
                "modulus": row.modulus,
                "critical_modulus_cap": row.critical_modulus_cap,
                "certified": row.certified,
            }
            for row in witness.nested_audit.envelope_rows
        ],
        "minimum_gap_variance": str(witness.minimum_gap_variance),
        "minimum_innovation_q00_per_modulus": str(
            witness.minimum_innovation_q00_per_modulus
        ),
        "final_innovation_q00_per_modulus": str(
            witness.final_innovation_q00_per_modulus
        ),
        "dyadic_rows": [
            {
                "mark_count": row.mark_count,
                "modulus": row.modulus,
                "gap_variance": str(row.gap_variance),
                "innovation_q00_per_modulus": str(
                    row.innovation_q00_per_modulus
                ),
            }
            for row in witness.nested_audit.rows
        ],
        "reset_profiles": [
            _profile_payload(profile) for profile in witness.history.profiles
        ],
        "cross_epoch_persistence": [
            _persistence_payload(persistence)
            for persistence in witness.history.persistence
        ],
    }


def build_payload(
    *,
    wave4_certificate: Path,
    beam_width: int,
    candidates_per_state: int,
    retain: int,
    seeds: tuple[int, ...],
) -> dict[str, object]:
    source_sha256 = _source_hashes()
    wave4_hash, parents, parent_metadata = _load_wave4(wave4_certificate)
    if not seeds:
        raise ValueError("at least one seed is required")
    sizes = (4, 8, 16, 32, 64)
    objectives = ("persistence", "innovation")
    runs: list[dict[str, object]] = []
    for index, objective in enumerate(objectives):
        seed = seeds[index] if index < len(seeds) else seeds[-1]
        result = beam_extend_nested(
            parents=parents,
            sizes=sizes,
            constant=Fraction(1),
            objective=objective,
            beam_width=beam_width,
            candidates_per_state=candidates_per_state,
            seed=seed,
            retain=retain,
        )
        runs.append(
            {
                "objective": objective,
                "seed": seed,
                "beam_width": beam_width,
                "candidates_per_state": candidates_per_state,
                "retain": result.retain,
                "expanded_state_count": result.expanded_state_count,
                "final_search_complete": False,
                "witnesses": [
                    _witness_payload(witness) for witness in result.witnesses
                ],
            }
        )
    if _source_hashes() != source_sha256:
        raise RuntimeError("generator source changed during certificate build")
    return {
        "schema": "wave5_nested_extension_certificate_v2",
        "research_date": "2026-08-28",
        "purpose": (
            "finite falsification and profile-structure discovery beyond the "
            "saved Wave 4 witnesses; not an asymptotic claim"
        ),
        "method": (
            "seeded integer beam extension from authenticated Wave 4 parents; "
            "exact Fraction objectives; independent final all-pairs and "
            "all-prefix C=1 audits"
        ),
        "sizes": list(sizes),
        "constant": "1",
        "retain": retain,
        "reproducibility": {
            "canonical_byte_identity_scope": "recorded_python_runtime_only",
            "python_implementation": platform.python_implementation(),
            "python_version": platform.python_version(),
            "source_sha256": source_sha256,
        },
        "wave4_certificate_sha256": wave4_hash,
        "wave4_parents": parent_metadata,
        "runs": runs,
    }


def _parse_seeds(value: str) -> tuple[int, ...]:
    return tuple(int(part) for part in value.split(",") if part)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--wave4-certificate",
        type=Path,
        default=Path(__file__).with_name("wave4_nested_certificate_2026-08-28.json"),
    )
    parser.add_argument("--beam-width", type=int, default=128)
    parser.add_argument("--candidates-per-state", type=int, default=32)
    parser.add_argument("--retain", type=int, default=3)
    parser.add_argument("--seeds", default="501191,502191")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("wave5_nested_certificate_2026-08-28.json"),
    )
    arguments = parser.parse_args()
    payload = build_payload(
        wave4_certificate=arguments.wave4_certificate,
        beam_width=arguments.beam_width,
        candidates_per_state=arguments.candidates_per_state,
        retain=arguments.retain,
        seeds=_parse_seeds(arguments.seeds),
    )
    payload["certificate_sha256"] = _canonical_hash(payload)
    arguments.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    )
    print(arguments.output)


if __name__ == "__main__":
    main()
