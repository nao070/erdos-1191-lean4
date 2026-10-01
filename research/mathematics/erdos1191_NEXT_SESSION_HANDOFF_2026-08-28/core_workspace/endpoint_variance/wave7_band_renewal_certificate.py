"""Generate the deterministic Wave 7 finite band-renewal certificate."""

from __future__ import annotations

import argparse
from dataclasses import asdict
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

from wave6_hall_candidate_probe import COUNTEREXAMPLE_64_POINTS
from wave7_band_renewal_probe import (
    adjacent_half_overlap_debt,
    all_prefix_c1,
    compatible_adjacent_gap_swaps,
    enumerate_compatible_four_mark_rulers,
    enumerate_four_mark_est_failure_region,
    epoch_size_tax_candidate,
    harmonic_epoch_tax_candidate,
    is_golomb,
    load_authenticated_wave6_fixtures,
    positive_differences,
    renewal_hole_candidate,
    short_shell_eight_mark_audit,
)


def _encode(value: Any) -> Any:
    if isinstance(value, Fraction):
        return f"{value.numerator}/{value.denominator}"
    if isinstance(value, tuple):
        return [_encode(item) for item in value]
    if isinstance(value, list):
        return [_encode(item) for item in value]
    if isinstance(value, dict):
        return {key: _encode(item) for key, item in value.items()}
    return value


def _difference_hash(points: tuple[int, ...]) -> str:
    rendered = "\n".join(str(value) for value in sorted(positive_differences(points)))
    return sha256((rendered + "\n").encode("ascii")).hexdigest()


def _fixed_ruler_audit(name: str, points: tuple[int, ...]) -> dict[str, Any]:
    renewal = renewal_hole_candidate(points)
    harmonic = harmonic_epoch_tax_candidate(points)
    epoch_rows: dict[str, Any] = {}
    overlap_rows: dict[str, Any] = {}
    for minimum in range(2, 8):
        try:
            row = epoch_size_tax_candidate(
                points,
                minimum_active_epochs=minimum,
            )
        except ValueError:
            continue
        epoch_rows[str(minimum)] = asdict(row)
        overlap_rows[str(minimum)] = asdict(
            adjacent_half_overlap_debt(points, row.threshold)
        )
    return {
        "name": name,
        "point_count": len(points),
        "points": points,
        "is_golomb": is_golomb(points),
        "all_prefix_c1": all_prefix_c1(points),
        "sorted_difference_sha256": _difference_hash(points),
        "renewal_hole_minimum": asdict(renewal),
        "harmonic_epoch_tax_minimum": asdict(harmonic),
        "epoch_size_tax_minima_by_required_active_epoch_count": epoch_rows,
        "cheap_adjacent_half_overlap_at_epoch_size_minima": overlap_rows,
    }


def _four_mark_exhaustion() -> dict[str, Any]:
    count = 0
    equality_count = 0
    negative_count = 0
    best_key: tuple[Any, ...] | None = None
    best_points: tuple[int, ...] | None = None
    best_row: Any = None
    margin_histogram: dict[int, int] = {}
    for points in enumerate_compatible_four_mark_rulers():
        count += 1
        row = epoch_size_tax_candidate(points, minimum_active_epochs=2)
        margin_histogram[row.margin] = margin_histogram.get(row.margin, 0) + 1
        equality_count += row.margin == 0
        negative_count += row.margin < 0
        key = (row.margin, row.threshold, row.cumulative_weight, points)
        if best_key is None or key < best_key:
            best_key = key
            best_points = points
            best_row = row
    if best_points is None:
        raise AssertionError("four-mark enumeration unexpectedly empty")
    universal_failure_region = tuple(enumerate_four_mark_est_failure_region())
    universal_failure_rows = tuple(
        epoch_size_tax_candidate(points, minimum_active_epochs=2)
        for points in universal_failure_region
    )
    return {
        "enumeration_is_exhaustive_for_stated_scope": True,
        "scope": (
            "normalized four-mark Golomb rulers satisfying the exact C=1 "
            "prefix cap at counts 2, 3, and 4"
        ),
        "ruler_count": count,
        "negative_margin_count": negative_count,
        "equality_count": equality_count,
        "minimum_margin_points": best_points,
        "minimum_margin_row": asdict(best_row),
        "margin_histogram": {
            str(margin): margin_histogram[margin] for margin in sorted(margin_histogram)
        },
        "universal_failure_region": {
            "analytic_reduction": (
                "any first m=2 failure forces a_1<=4 and a_3-a_1<=5; "
                "any second m=2 failure lies in the same region"
            ),
            "ruler_count": len(universal_failure_region),
            "negative_margin_count": sum(
                row.margin < 0 for row in universal_failure_rows
            ),
            "minimum_margin": min(row.margin for row in universal_failure_rows),
            "points": universal_failure_region,
        },
    }


def build_certificate(source_certificate: Path) -> dict[str, Any]:
    fixtures = load_authenticated_wave6_fixtures(source_certificate)
    bases = [
        ("wave6_hall_counterexample_64", tuple(COUNTEREXAMPLE_64_POINTS)),
        *(
            (f"authenticated_wave6_64_{index}", points)
            for index, points in enumerate(fixtures.sixty_four_mark_points)
        ),
        ("authenticated_wave6_128", fixtures.one_hundred_twenty_eight_mark_points),
    ]
    fixed_audits = [_fixed_ruler_audit(name, points) for name, points in bases]

    transformations: list[dict[str, Any]] = []
    for parent_index, parent in enumerate(fixtures.sixty_four_mark_points):
        for variant in compatible_adjacent_gap_swaps(parent):
            audit = _fixed_ruler_audit(
                f"wave6_64_{parent_index}_gap_swap_{variant.swapped_gap_index}",
                variant.points,
            )
            audit["parent_index"] = parent_index
            audit["swapped_gap_index_zero_based"] = variant.swapped_gap_index
            transformations.append(audit)

    all_audits = fixed_audits + transformations
    survivor_minima: dict[str, Any] = {}
    for minimum in range(2, 8):
        eligible = [
            audit["epoch_size_tax_minima_by_required_active_epoch_count"][str(minimum)]
            for audit in all_audits
            if str(minimum)
            in audit["epoch_size_tax_minima_by_required_active_epoch_count"]
        ]
        if not eligible:
            continue
        best = min(
            eligible,
            key=lambda row: (
                row["margin"],
                row["threshold"],
                row["cumulative_weight"],
            ),
        )
        survivor_minima[str(minimum)] = best

    eight_mark_audit = short_shell_eight_mark_audit()
    payload: dict[str, Any] = {
        "schema": "wave7_band_renewal_certificate_v1",
        "research_date": "2026-08-28",
        "purpose": (
            "exact finite falsification and calibration of three candidate "
            "improvements to the Wave 6 threshold ledger"
        ),
        "source_authentication": {
            "wave6_arithmetic_certificate_filename": source_certificate.name,
            "wave6_arithmetic_certificate_file_sha256": (
                fixtures.certificate_file_sha256
            ),
        },
        "candidates": {
            "RH": (
                "C(K)+E(K)-1 <= |K| for every integer interval K meeting "
                "at least two dyadic epochs"
            ),
            "EST": ("S(T)+sum_{active dyadic m}(m-1) <= floor(T) at every threshold T"),
            "HT": (
                "H_{S(T)}-sum_{tau<=T} k/tau >= (E(T)-1)/ceil(T) at every threshold T"
            ),
        },
        "fixed_ruler_audits": fixed_audits,
        "four_mark_exhaustive_audit": _four_mark_exhaustion(),
        "eight_mark_short_shell_exhaustive_audit": {
            **asdict(eight_mark_audit),
            "enumeration_is_exhaustive_for_stated_scope": True,
            "scope": (
                "all normalized eight-mark Golomb rulers with a_3<=34 and "
                "m=4 shell span at most 35; no C=1 assumption"
            ),
            "analytic_scope_completion": (
                "an EST failure at the first m=4 activation forces shell "
                "span at most 35; once floor(tau_4,1)>=9, the universal "
                "M_4>=29/8 bound makes all later m=4 activations safe"
            ),
        },
        "adjacent_gap_swap_audit": {
            "generation_scope": (
                "every single adjacent-gap transposition of each of the six "
                "authenticated Wave 6 64-mark rulers"
            ),
            "generation_is_exhaustive_within_stated_scope": True,
            "accepted_variant_count": len(transformations),
            "accepted_variants": transformations,
        },
        "epoch_size_tax_survivor_minima_across_fixed_and_swap_audits": (
            survivor_minima
        ),
        "conclusions": {
            "RH": "refuted by exact finite Golomb witnesses",
            "HT": "refuted by exact finite Golomb witnesses",
            "EST": (
                "proved for all normalized Golomb rulers through eight marks and "
                "not refuted in the authenticated 64/128 and gap-swap "
                "scope; no unbounded theorem is claimed"
            ),
            "erdos_1191_resolved": False,
            "infinite_extension_claimed": False,
        },
    }
    encoded = _encode(payload)
    canonical = json.dumps(encoded, sort_keys=True, separators=(",", ":"))
    encoded["certificate_sha256"] = sha256(canonical.encode("utf-8")).hexdigest()
    return encoded


def main() -> None:
    parser = argparse.ArgumentParser()
    directory = Path(__file__).resolve().parent
    parser.add_argument(
        "--source-certificate",
        type=Path,
        default=directory / "wave6_arithmetic_mining_certificate_2026-08-28.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=directory / "wave7_band_renewal_certificate_2026-08-28.json",
    )
    arguments = parser.parse_args()
    payload = build_certificate(arguments.source_certificate)
    arguments.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(arguments.output)
    print(payload["certificate_sha256"])


if __name__ == "__main__":
    main()
