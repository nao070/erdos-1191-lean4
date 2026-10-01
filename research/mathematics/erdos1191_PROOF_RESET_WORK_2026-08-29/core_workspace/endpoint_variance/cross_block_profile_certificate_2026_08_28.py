"""Deterministic exact certificate for cross-block diameter-profile packing."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
from itertools import combinations
import json
from pathlib import Path

from cross_block_profile import (
    cross_band_witness,
    diameter_profile_discrepancy,
    dyadic_tree_carleson_witness,
    profile_discrepancy_lower_bound,
    same_lag_packing_witness,
)
from gap_measure_dynamics import (
    dyadic_gap_matrix_update,
    normalized_gap_function_variance,
)
from growing_depth_no_go import (
    erdos_turan_points_without_quadratic_check,
    gap_measure_kolmogorov_discrepancy,
)
from sidon_block_variance import is_golomb_ruler


OUTPUT = Path(__file__).with_name(
    "cross_block_profile_certificate_2026-08-28.json"
)


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    arguments = parser.parse_args()

    exhaustive_candidates = 0
    exhaustive_rulers = 0
    kolmogorov_shift_checks = 0
    same_lag_checks = 0
    tree_checks = 0
    lower_bound_checks = 0

    for diameter in range(6, 19):
        for interior in combinations(range(1, diameter), 2):
            exhaustive_candidates += 1
            points = (0, *interior, diameter)
            if not is_golomb_ruler(points):
                continue
            exhaustive_rulers += 1
            profile = diameter_profile_discrepancy(points)
            kolmogorov = gap_measure_kolmogorov_discrepancy(points)
            if not profile <= kolmogorov <= profile + Fraction(1, len(points)):
                raise AssertionError("Kolmogorov/profile index-shift bound failed")
            kolmogorov_shift_checks += 1

            for lag in (1, 2, 3):
                same_lag_packing_witness(points, block_count=4, lag=lag)
                same_lag_checks += 1
            tree = dyadic_tree_carleson_witness(points)
            if tree.total_cross_differences != 6:
                raise AssertionError("four-mark tree partition failed")
            tree_checks += 1

            old_modulus = points[0] - points[0] + 1
            lower = profile_discrepancy_lower_bound(4, 4, old_modulus)
            if profile < lower:
                raise AssertionError("exact old-prefix discrepancy bound failed")
            lower_bound_checks += 1

    structured_records = []
    for count, prime in ((8, 11), (16, 17), (32, 37), (64, 67)):
        points = erdos_turan_points_without_quadratic_check(count, prime)
        profile = diameter_profile_discrepancy(points)
        kolmogorov = gap_measure_kolmogorov_discrepancy(points)
        if not profile <= kolmogorov <= profile + Fraction(1, count):
            raise AssertionError("structured Kolmogorov/profile bound failed")

        lag_records = []
        for block_count in (2, 4, 8):
            if block_count > count:
                continue
            for lag in range(1, block_count):
                witness = same_lag_packing_witness(points, block_count, lag)
                lag_records.append(
                    {
                        "block_count": block_count,
                        "lag": lag,
                        "difference_count": witness.difference_count,
                        "exact_global_band_length": (
                            witness.exact_global_band_length
                        ),
                        "discrepancy_band_upper_bound": fraction_text(
                            witness.discrepancy_band_upper_bound
                        ),
                    }
                )
                same_lag_checks += 1

        tree = dyadic_tree_carleson_witness(points)
        tree_checks += 1
        old_count = count // 4
        old_modulus = points[old_count - 1] - points[0] + 1
        lower = profile_discrepancy_lower_bound(count, 4, old_modulus)
        if profile < lower:
            raise AssertionError("structured profile lower bound failed")
        lower_bound_checks += 1

        old_new = cross_band_witness(points, 0, count // 2, count // 2, count)
        structured_records.append(
            {
                "mark_count": count,
                "prime": prime,
                "profile_discrepancy": fraction_text(profile),
                "kolmogorov_discrepancy": fraction_text(kolmogorov),
                "tree_weighted_span_sum": fraction_text(
                    tree.weighted_span_sum
                ),
                "tree_running_count_upper_sum": fraction_text(
                    tree.running_count_upper_sum
                ),
                "old_new_band_occupancy": fraction_text(
                    Fraction(old_new.difference_count, old_new.band_length)
                ),
                "same_lag_records": lag_records,
            }
        )

    scalar_discrepancy_records = []
    for height in (2, 10, 100, 1_000):
        points = (0, height, height + 1, 2 * height + 3)
        profile = diameter_profile_discrepancy(points)
        kolmogorov = gap_measure_kolmogorov_discrepancy(points)
        variance = normalized_gap_function_variance(points)
        expected = Fraction(5 * height + 9, 256 * (height + 2) ** 2)
        if profile != Fraction(1, 4) or kolmogorov != Fraction(1, 4):
            raise AssertionError("fixed-discrepancy Sidon family failed")
        if variance != expected:
            raise AssertionError("vanishing-variance Sidon formula failed")
        scalar_discrepancy_records.append(
            {
                "height": height,
                "profile_discrepancy": fraction_text(profile),
                "kolmogorov_discrepancy": fraction_text(kolmogorov),
                "gap_variance": fraction_text(variance),
            }
        )

    homometric_records = []
    for points in ((0, 1, 3, 7), (0, 1, 5, 7)):
        update = dyadic_gap_matrix_update(points, 2)
        normalized_innovation = tuple(
            tuple(entry / update.new_modulus for entry in row)
            for row in update.innovation
        )
        homometric_records.append(
            {
                "points": list(points),
                "profile_discrepancy": fraction_text(
                    diameter_profile_discrepancy(points)
                ),
                "kolmogorov_discrepancy": fraction_text(
                    gap_measure_kolmogorov_discrepancy(points)
                ),
                "normalized_innovation": [
                    [fraction_text(entry) for entry in row]
                    for row in normalized_innovation
                ],
            }
        )
    if homometric_records[0]["normalized_innovation"] == homometric_records[1][
        "normalized_innovation"
    ]:
        raise AssertionError("same-discrepancy innovation separation failed")

    payload = {
        "schema": "erdos1191.cross_block_profile_certificate.v1",
        "arithmetic": "integers and fractions.Fraction",
        "exhaustive_four_mark_range": {
            "diameter_inclusive": [6, 18],
            "normalized_candidates": exhaustive_candidates,
            "sidon_rulers": exhaustive_rulers,
        },
        "checks": {
            "kolmogorov_profile_shift": kolmogorov_shift_checks,
            "same_lag_exact_band": same_lag_checks,
            "dyadic_tree_partition": tree_checks,
            "old_prefix_profile_lower_bound": lower_bound_checks,
        },
        "structured_cases": structured_records,
        "scalar_discrepancy_counterexamples": scalar_discrepancy_records,
        "homometric_same_discrepancy_innovations": homometric_records,
        "scope_warning": (
            "The exact finite checks audit the cross-band formulas and the "
            "diameter-profile discrepancy lemma.  The resulting Carleson "
            "bound is O(log M), not the missing o(log J) innovation budget."
        ),
        "all_checks_passed": True,
    }
    canonical = json.dumps(
        payload, sort_keys=True, separators=(",", ":")
    ).encode()
    payload["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    arguments.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
