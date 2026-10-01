"""Generate a deterministic exact certificate for Wave 4 nested searches."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from wave4_nested_search import (
    NestedWitnessAudit,
    beam_search_nested,
    critical_modulus_cap,
    exhaustive_gap_search,
)


def _fraction(value: Fraction | None) -> str | None:
    return None if value is None else str(value)


def _difference_hash(differences: tuple[int, ...]) -> str:
    canonical = json.dumps(list(differences), separators=(",", ":")).encode()
    return hashlib.sha256(canonical).hexdigest()


def _witness_payload(witness: NestedWitnessAudit) -> dict[str, object]:
    differences = witness.difference_audit.sorted_differences
    return {
        "points": list(witness.points),
        "pair_count": witness.difference_audit.pair_count,
        "all_positive_differences": list(differences),
        "difference_sha256": _difference_hash(differences),
        "difference_collisions": [
            [difference, [list(pair) for pair in pairs]]
            for difference, pairs in witness.difference_audit.collisions
        ],
        "independent_difference_audit_passed": witness.difference_audit.is_golomb,
        "envelope_constant": str(witness.envelope_constant),
        "envelope_compatible": witness.envelope_compatible,
        "all_prefix_envelope_rows": [
            {
                "mark_count": row.mark_count,
                "modulus": row.modulus,
                "critical_modulus_cap": row.critical_modulus_cap,
                "certified": row.certified,
            }
            for row in witness.envelope_rows
        ],
        "minimum_gap_variance": str(witness.minimum_gap_variance),
        "minimum_innovation_q00_per_modulus": str(
            witness.minimum_innovation_q00_per_modulus
        ),
        "rows": [
            {
                "mark_count": row.mark_count,
                "modulus": row.modulus,
                "critical_modulus_cap": critical_modulus_cap(
                    row.mark_count, witness.envelope_constant
                ),
                "gap_variance": str(row.gap_variance),
                "gap_variance_decimal": f"{float(row.gap_variance):.15g}",
                "innovation_q00_per_modulus": _fraction(
                    row.innovation_q00_per_modulus
                ),
                "innovation_q00_per_modulus_decimal": (
                    None
                    if row.innovation_q00_per_modulus is None
                    else f"{float(row.innovation_q00_per_modulus):.15g}"
                ),
            }
            for row in witness.rows
        ],
    }


def build_payload(
    *,
    sizes: tuple[int, ...],
    constant: Fraction,
    beam_width: int,
    candidates_per_state: int,
    retain: int,
    seeds: tuple[int, ...],
) -> dict[str, object]:
    if not seeds:
        raise ValueError("at least one seed is required")
    initial_cap = critical_modulus_cap(sizes[0], constant)
    exact = exhaustive_gap_search(
        mark_count=sizes[0],
        max_modulus=initial_cap,
        envelope_constant=constant,
    )
    objectives = ("gap", "innovation")
    runs: list[dict[str, object]] = []
    for index, objective in enumerate(objectives):
        seed = seeds[index] if index < len(seeds) else seeds[-1]
        result = beam_search_nested(
            sizes=sizes,
            constant=constant,
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
                "beam_width": result.beam_width,
                "candidates_per_state": result.candidates_per_state,
                "expanded_state_count": result.expanded_state_count,
                "exact_root_candidate_count": result.exact_root_candidate_count,
                "exact_root_accepted_count": result.exact_root_accepted_count,
                "final_search_complete": False,
                "witnesses": [_witness_payload(witness) for witness in result.witnesses],
            }
        )
    return {
        "schema": "wave4_nested_search_certificate_v1",
        "research_date": "2026-08-28",
        "purpose": (
            "finite falsification and calibration of long-history conjectures; "
            "not an asymptotic claim"
        ),
        "method": (
            "complete normalized enumeration at the first checkpoint, then "
            "seeded integer-only beam extension; all final pair differences "
            "recomputed by an independent all-pairs oracle"
        ),
        "sizes": list(sizes),
        "envelope": "N_m <= 2*C*m^2*log(m)",
        "constant": str(constant),
        "critical_modulus_caps": {
            str(size): critical_modulus_cap(size, constant) for size in sizes
        },
        "exact_initial_checkpoint": {
            "mark_count": exact.mark_count,
            "max_modulus": exact.max_modulus,
            "complete": exact.complete,
            "candidate_count": exact.candidate_count,
            "accepted_count": exact.accepted_count,
            "node_count": exact.node_count,
            "best_gap_variance": str(exact.best_score),
            "best_rulers": [list(ruler) for ruler in exact.best_rulers],
        },
        "runs": runs,
    }


def _parse_sizes(value: str) -> tuple[int, ...]:
    return tuple(int(part) for part in value.split(",") if part)


def _parse_seeds(value: str) -> tuple[int, ...]:
    return tuple(int(part) for part in value.split(",") if part)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", default="4,8,16,32")
    parser.add_argument("--constant", default="1")
    parser.add_argument("--beam-width", type=int, default=512)
    parser.add_argument("--candidates-per-state", type=int, default=64)
    parser.add_argument("--retain", type=int, default=4)
    parser.add_argument("--seeds", default="1191,9119")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("wave4_nested_certificate_2026-08-28.json"),
    )
    arguments = parser.parse_args()
    payload = build_payload(
        sizes=_parse_sizes(arguments.sizes),
        constant=Fraction(arguments.constant),
        beam_width=arguments.beam_width,
        candidates_per_state=arguments.candidates_per_state,
        retain=arguments.retain,
        seeds=_parse_seeds(arguments.seeds),
    )
    canonical = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode()
    payload["certificate_sha256"] = hashlib.sha256(canonical).hexdigest()
    arguments.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    )
    print(arguments.output)


if __name__ == "__main__":
    main()
