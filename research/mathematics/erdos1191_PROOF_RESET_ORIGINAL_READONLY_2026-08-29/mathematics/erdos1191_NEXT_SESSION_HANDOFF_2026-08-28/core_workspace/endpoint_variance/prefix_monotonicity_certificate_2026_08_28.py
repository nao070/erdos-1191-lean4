"""Exhaustive certificate for the minimal fixed-modulus prefix counterexample."""
from __future__ import annotations

import argparse
import hashlib
import json
from itertools import combinations
from pathlib import Path

from prefix_monotonicity import (
    direct_same_modulus_prefix_variance,
    doubled_prefix_comparison,
    prefix_monotonicity_counterfamily,
)
from sidon_block_variance import is_golomb_ruler


OUTPUT = Path(__file__).with_name("prefix_monotonicity_certificate_2026-08-28.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def positive_compositions(total: int, parts: int):
    for cuts in combinations(range(1, total), parts - 1):
        boundaries = (0, *cuts, total)
        yield tuple(boundaries[index + 1] - boundaries[index] for index in range(parts))


def marks_from_internal_gaps(gaps: tuple[int, ...]) -> tuple[int, ...]:
    marks = [0]
    for gap in gaps:
        marks.append(marks[-1] + gap)
    return tuple(marks)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    arguments = parser.parse_args()
    r1_checks = 0
    for modulus in range(2, 41):
        for outside, gap in positive_compositions(modulus, 2):
            del outside
            points = (0, gap)
            # The one-mark prefix has variance zero; the two-mark load is nonnegative.
            require(
                direct_same_modulus_prefix_variance(points, 2, modulus) >= 0,
                "two-mark literal variance became negative",
            )
            r1_checks += 1

    r2_checks = 0
    r2_sidon_checks = 0
    arbitrary_decreases: list[dict[str, object]] = []
    sidon_decreases: list[dict[str, object]] = []
    for modulus in range(4, 41):
        for outside, gap1, gap2, gap3 in positive_compositions(modulus, 4):
            del outside
            points = marks_from_internal_gaps((gap1, gap2, gap3))
            comparison = doubled_prefix_comparison(points, 2, modulus)
            require(
                comparison.prefix_variance
                == direct_same_modulus_prefix_variance(points, 2, modulus),
                "four-gap prefix formula/oracle mismatch",
            )
            require(
                comparison.full_variance
                == direct_same_modulus_prefix_variance(points, 4, modulus),
                "four-gap full formula/oracle mismatch",
            )
            r2_checks += 1
            sidon = is_golomb_ruler(points)
            r2_sidon_checks += int(sidon)
            if comparison.change < 0:
                row = {
                    "modulus": modulus,
                    "points": points,
                    "prefix_variance": str(comparison.prefix_variance),
                    "full_variance": str(comparison.full_variance),
                    "change": str(comparison.change),
                }
                arbitrary_decreases.append(row)
                if sidon:
                    sidon_decreases.append(row)

    require(len(arbitrary_decreases) == 3, "unexpected arbitrary decrease count")
    require(len(sidon_decreases) == 2, "unexpected Sidon decrease count")
    require(sidon_decreases[0]["modulus"] == 40, "wrong minimal Sidon modulus")
    require(
        tuple(sidon_decreases[0]["points"]) == (0, 20, 21, 39),
        "wrong first Sidon counterexample",
    )

    r3_checks = 0
    r3_sidon_checks = 0
    for modulus in range(6, 40):
        for composition in positive_compositions(modulus, 6):
            points = marks_from_internal_gaps(composition[1:])
            comparison = doubled_prefix_comparison(points, 3, modulus)
            require(comparison.change >= 0, "six-gap monotonicity failure below N=40")
            r3_checks += 1
            r3_sidon_checks += int(is_golomb_ruler(points))

    family_checks = 0
    for modulus in range(40, 101):
        points = prefix_monotonicity_counterfamily(modulus)
        comparison = doubled_prefix_comparison(points, 2, modulus)
        require(
            comparison.prefix_variance
            == direct_same_modulus_prefix_variance(points, 2, modulus),
            "counterfamily prefix formula/oracle mismatch",
        )
        require(
            comparison.full_variance
            == direct_same_modulus_prefix_variance(points, 4, modulus),
            "counterfamily full formula/oracle mismatch",
        )
        require(comparison.change < 0, "counterfamily did not decrease variance")
        family_checks += 1

    payload = {
        "schema": "erdos1191.prefix_monotonicity_certificate.v1",
        "r1_literal_checks": r1_checks,
        "r2_formula_and_literal_checks": r2_checks,
        "r2_sidon_configurations": r2_sidon_checks,
        "r2_arbitrary_decreases": arbitrary_decreases,
        "r2_sidon_decreases": sidon_decreases,
        "r3_formula_checks": r3_checks,
        "r3_sidon_configurations": r3_sidon_checks,
        "counterfamily_literal_checks": family_checks,
        "doubled_prefix_global_minimal_modulus": 40,
        "all_checks_passed": True,
        "scope_warning": "Finite exhaustion supports, but does not replace, the analytic minimality proof.",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    arguments.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
