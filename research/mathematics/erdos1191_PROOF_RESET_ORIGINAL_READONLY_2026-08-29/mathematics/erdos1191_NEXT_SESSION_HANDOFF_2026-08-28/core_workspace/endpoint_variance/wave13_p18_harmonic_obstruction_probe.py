"""Exact finite audit of the unavoidable new-birth floor in Wave 12 P18.

The proof itself is elementary and analytic.  The executable layer checks its
entire rational inequality chain on bounded exhaustive rulers and independent
fixtures.  Floating logarithms are reported only as calibrations.

No finite row constructs an infinite eventually critical Golomb ruler.  The
asymptotic conclusion is conditional: if such a fixed branch exists, its
``Z_m`` sum has a positive ``log J`` lower bound, so it cannot satisfy P18's
proposed ``o(log J)`` conclusion.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from dataclasses import asdict, dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import pairwise
from math import fsum, log
from pathlib import Path
from typing import Any

from complete_birth_ledger import erdos_turan_ruler
from wave6_hall_candidate_probe import COUNTEREXAMPLE_64_POINTS
from wave8_survival_debt_probe import bounded_golomb_exhaustion
from wave11_abel_repayment_probe import _all_prefix_c1

DIRECTORY = Path(__file__).resolve().parent


def _fraction_payload(value: Fraction) -> dict[str, str]:
    # Some exact aggregate denominators have thousands of decimal digits.
    # Hexadecimal is exempt from Python's decimal conversion safety limit and
    # remains a lossless, portable encoding.
    return {
        "numerator_hex": hex(value.numerator),
        "denominator_hex": hex(value.denominator),
    }


def _canonical_hash(payload: dict[str, Any]) -> str:
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return sha256(canonical.encode("utf-8")).hexdigest()


def _gap(points: Sequence[int], index: int) -> int:
    return points[index] - points[index - 1]


def is_golomb_ruler(points: Sequence[int]) -> bool:
    marks = tuple(points)
    if (
        not marks
        or marks[0] != 0
        or any(left >= right for left, right in pairwise(marks))
    ):
        return False
    differences = [
        marks[right] - marks[left]
        for right in range(1, len(marks))
        for left in range(right)
    ]
    return len(differences) == len(set(differences))


def suffix_gap_blocks(m: int) -> tuple[tuple[int, ...], ...]:
    """Partition h_(m-1),...,h_(2m-1) into q,q,q,q+1 indices."""
    if m < 4 or m & (m - 1):
        raise ValueError("m must be a dyadic integer at least four")
    q = m // 4
    start = m - 1
    return (
        tuple(range(start, start + q)),
        tuple(range(start + q, start + 2 * q)),
        tuple(range(start + 2 * q, start + 3 * q)),
        tuple(range(start + 3 * q, 2 * m)),
    )


def cross_ratio_value(points: Sequence[int], left: int, right: int) -> float:
    marks = tuple(points)
    numerator = (marks[right - 1] - marks[left - 1]) * (marks[right] - marks[left])
    denominator = (marks[right - 1] - marks[left]) * (marks[right] - marks[left - 1])
    return log(numerator / denominator)


def new_birth_value(points: Sequence[int], m: int) -> float:
    return fsum(
        ((right - left) / (2 * m)) ** 2 * cross_ratio_value(points, left, right)
        for right in range(m, 2 * m)
        for left in range(m - 1, right - 1)
    )


@dataclass(frozen=True)
class NewBirthFloorAudit:
    epoch: int
    suffix_first_gap: int
    suffix_last_gap: int
    suffix_gap_count: int
    suffix_span: int
    quarter_size: int
    block_sizes: tuple[int, int, int, int]
    block_masses: tuple[int, int, int, int]
    maximum_mass_block: int
    paired_block: int
    minimum_pair_distance: int
    pair_count: int
    selected_gaps_distinct: bool
    all_pairs_are_new_birth_pairs: bool
    far_radius: int
    minimum_far_gap_count: int
    minimum_far_gap_mass: int
    full_rank_product_energy: int
    far_rank_product_energy: int
    minimum_observed_layered_energy: int
    exact_layered_energy_floor: int
    rational_pair_floor: Fraction
    diameter_relaxed_floor: Fraction
    far_pair_floor: Fraction
    layered_floor: Fraction
    rational_block_floor: Fraction
    quarter_theorem_floor: Fraction
    theorem_floor: Fraction
    pair_floor_dominates_diameter_floor: bool
    diameter_floor_dominates_far_floor: bool
    diameter_floor_dominates_layered_floor: bool
    observed_layered_energy_dominates_floor: bool
    layered_floor_dominates_theorem_floor: bool
    pair_floor_dominates_block_floor: bool
    block_floor_dominates_quarter_floor: bool
    floating_new_birth_value: float
    floating_value_dominates_rational_pair_floor: bool


def new_birth_floor_audit(points: Sequence[int], m: int) -> NewBirthFloorAudit:
    marks = tuple(points)
    if len(marks) < 2 * m:
        raise ValueError("the ruler must contain marks a_0 through a_(2m-1)")
    if not is_golomb_ruler(marks):
        raise ValueError("points must form a normalized integer Golomb ruler")

    blocks = suffix_gap_blocks(m)
    q = m // 4
    selected_indices = tuple(range(m - 1, 2 * m))
    gaps = {index: _gap(marks, index) for index in selected_indices}
    suffix_span = marks[2 * m - 1] - marks[m - 2]
    if suffix_span != sum(gaps.values()):
        raise AssertionError("the suffix gap endpoints are inconsistent")

    masses = tuple(sum(gaps[index] for index in block) for block in blocks)
    maximum = max(range(4), key=lambda index: (masses[index], -index))
    partner = (2, 3, 0, 1)[maximum]
    earlier, later = sorted((maximum, partner))
    block_pair_indices = tuple(
        (left, right) for left in blocks[earlier] for right in blocks[later]
    )
    all_pair_indices = tuple(
        (left, right) for right in range(m, 2 * m) for left in range(m - 1, right - 1)
    )

    all_new_birth = all(
        m - 1 <= left <= right - 2 and m <= right <= 2 * m - 1
        for left, right in all_pair_indices
    )
    minimum_distance = min(right - left for left, right in block_pair_indices)
    rational_pair_floor = sum(
        (
            Fraction((right - left) ** 2, 4 * m * m)
            * Fraction(
                gaps[left] * gaps[right],
                (marks[right] - marks[left - 1]) ** 2,
            )
        )
        for left, right in all_pair_indices
    )
    full_rank_product_energy = sum(
        (right - left) ** 2 * gaps[left] * gaps[right]
        for left, right in all_pair_indices
    )
    diameter_relaxed_floor = Fraction(
        full_rank_product_energy,
        4 * m * m * suffix_span**2,
    )

    far_radius = max(2, m // 4)
    far_pair_indices = tuple(
        (left, right)
        for left in selected_indices
        for right in selected_indices
        if left < right and right - left >= far_radius
    )
    far_rank_product_energy = sum(
        (right - left) ** 2 * gaps[left] * gaps[right]
        for left, right in far_pair_indices
    )
    far_pair_floor = Fraction(
        far_rank_product_energy,
        4 * m * m * suffix_span**2,
    )
    far_sets = {
        left: tuple(
            right for right in selected_indices if abs(right - left) >= far_radius
        )
        for left in selected_indices
    }
    minimum_far_gap_count = min(len(indices) for indices in far_sets.values())
    minimum_far_gap_mass = min(
        sum(gaps[index] for index in indices) for indices in far_sets.values()
    )
    layered_energies = {
        left: sum(
            (right - left) ** 2 * gaps[right]
            for right in selected_indices
            if abs(right - left) >= 2
        )
        for left in selected_indices
    }
    minimum_observed_layered_energy = min(layered_energies.values())
    exact_layered_energy_floor = sum(
        (2 * radius - 1) * (m + 2 - 2 * radius) * (m + 3 - 2 * radius) // 2
        for radius in range(2, m // 2 + 1)
    )
    closed_layered_floor = m * (m - 2) * (m * m + 8 * m + 6) // 48
    if exact_layered_energy_floor != closed_layered_floor:
        raise AssertionError("the layered-energy closed form failed")
    layered_floor = Fraction(
        exact_layered_energy_floor,
        8 * m * m * suffix_span,
    )
    rational_block_floor = Fraction((q + 1) ** 2, 4 * m * m) * Fraction(
        masses[maximum] * masses[partner], suffix_span**2
    )
    quarter_theorem_floor = Fraction(m * m, 8192 * suffix_span)
    theorem_floor = Fraction(m * m, 384 * suffix_span)
    floating_value = new_birth_value(marks, m)

    return NewBirthFloorAudit(
        epoch=m,
        suffix_first_gap=m - 1,
        suffix_last_gap=2 * m - 1,
        suffix_gap_count=len(selected_indices),
        suffix_span=suffix_span,
        quarter_size=q,
        block_sizes=tuple(len(block) for block in blocks),
        block_masses=masses,
        maximum_mass_block=maximum,
        paired_block=partner,
        minimum_pair_distance=minimum_distance,
        pair_count=len(all_pair_indices),
        selected_gaps_distinct=(len(set(gaps.values())) == len(gaps)),
        all_pairs_are_new_birth_pairs=all_new_birth,
        far_radius=far_radius,
        minimum_far_gap_count=minimum_far_gap_count,
        minimum_far_gap_mass=minimum_far_gap_mass,
        full_rank_product_energy=full_rank_product_energy,
        far_rank_product_energy=far_rank_product_energy,
        minimum_observed_layered_energy=minimum_observed_layered_energy,
        exact_layered_energy_floor=exact_layered_energy_floor,
        rational_pair_floor=rational_pair_floor,
        diameter_relaxed_floor=diameter_relaxed_floor,
        far_pair_floor=far_pair_floor,
        layered_floor=layered_floor,
        rational_block_floor=rational_block_floor,
        quarter_theorem_floor=quarter_theorem_floor,
        theorem_floor=theorem_floor,
        pair_floor_dominates_diameter_floor=(
            rational_pair_floor >= diameter_relaxed_floor
        ),
        diameter_floor_dominates_far_floor=(diameter_relaxed_floor >= far_pair_floor),
        diameter_floor_dominates_layered_floor=(
            diameter_relaxed_floor >= layered_floor
        ),
        observed_layered_energy_dominates_floor=(
            minimum_observed_layered_energy >= exact_layered_energy_floor
        ),
        layered_floor_dominates_theorem_floor=(layered_floor >= theorem_floor),
        pair_floor_dominates_block_floor=(rational_pair_floor >= rational_block_floor),
        block_floor_dominates_quarter_floor=(
            rational_block_floor >= quarter_theorem_floor
        ),
        floating_new_birth_value=floating_value,
        floating_value_dominates_rational_pair_floor=(
            floating_value + 1e-14 >= float(rational_pair_floor)
        ),
    )


def _audit_payload(audit: NewBirthFloorAudit) -> dict[str, Any]:
    payload = asdict(audit)
    for key in (
        "rational_pair_floor",
        "diameter_relaxed_floor",
        "far_pair_floor",
        "layered_floor",
        "rational_block_floor",
        "quarter_theorem_floor",
        "theorem_floor",
    ):
        payload[key] = _fraction_payload(payload[key])
    return payload


def exhaustive_eight_mark_audit() -> dict[str, Any]:
    exhaustion = bounded_golomb_exhaustion(mark_count=8, maximum_last_mark=40)
    rulers = tuple(points for points in exhaustion.rulers if _all_prefix_c1(points))
    failures: list[dict[str, Any]] = []
    minimum_margin: Fraction | None = None
    for points in rulers:
        audit = new_birth_floor_audit(points, 4)
        margin = audit.rational_pair_floor - audit.theorem_floor
        minimum_margin = (
            margin if minimum_margin is None else min(minimum_margin, margin)
        )
        if not (
            audit.selected_gaps_distinct
            and audit.all_pairs_are_new_birth_pairs
            and audit.minimum_pair_distance >= audit.quarter_size + 1
            and audit.minimum_far_gap_count >= audit.epoch // 2
            and audit.pair_floor_dominates_diameter_floor
            and audit.diameter_floor_dominates_far_floor
            and audit.diameter_floor_dominates_layered_floor
            and audit.observed_layered_energy_dominates_floor
            and audit.layered_floor_dominates_theorem_floor
            and audit.pair_floor_dominates_block_floor
            and audit.block_floor_dominates_quarter_floor
            and audit.floating_value_dominates_rational_pair_floor
        ):
            failures.append({"points": list(points), "audit": _audit_payload(audit)})
    if minimum_margin is None:
        raise AssertionError("the exhaustive scope must be nonempty")
    return {
        "candidate_count": len(rulers),
        "failure_count": len(failures),
        "first_failure": failures[0] if failures else None,
        "minimum_pair_floor_minus_theorem_floor": _fraction_payload(minimum_margin),
        "finite_only": True,
        "infinite_survival_inferred": False,
    }


def _et_new_birth_floor(m: int) -> Fraction:
    return sum(
        Fraction((m - distance + 1) * distance * distance, (2 * distance + 3) ** 2)
        for distance in range(2, m + 1)
    ) / (4 * m * m)


def erdos_turan_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for m, prime in ((4, 11), (8, 17), (16, 37), (32, 67), (64, 131)):
        points = erdos_turan_ruler(2 * m, prime)
        audit = new_birth_floor_audit(points, m)
        et_floor = _et_new_birth_floor(m)
        uniform_floor = Fraction(m - 1, 98 * m)
        rows.append(
            {
                "epoch": m,
                "prime": prime,
                "point_count": len(points),
                "new_birth_value": audit.floating_new_birth_value,
                "exact_et_product_floor": _fraction_payload(et_floor),
                "uniform_et_floor": _fraction_payload(uniform_floor),
                "et_floor_dominates_uniform_floor": et_floor >= uniform_floor,
                "new_birth_value_dominates_et_floor": (
                    audit.floating_new_birth_value + 1e-14 >= float(et_floor)
                ),
                "finite_only": True,
            }
        )
    return rows


def build_certificate() -> dict[str, Any]:
    fixture_64 = tuple(COUNTEREXAMPLE_64_POINTS)
    fixture_128 = erdos_turan_ruler(128, 257)
    fixture_rows = []
    for name, points, epochs in (
        ("wave6_hall_counterexample_64", fixture_64, (4, 8, 16, 32)),
        ("erdos_turan_128_p257", fixture_128, (4, 8, 16, 32, 64)),
    ):
        fixture_rows.append(
            {
                "name": name,
                "point_count": len(points),
                "rows": [
                    _audit_payload(new_birth_floor_audit(points, m)) for m in epochs
                ],
                "finite_only": True,
            }
        )

    payload: dict[str, Any] = {
        "schema": "erdos1191.wave13.p18-harmonic-obstruction.v1",
        "research_date": "2026-08-29",
        "purpose": (
            "Audit the exact rational chain proving Z_m^nb >= m^2/(384 H_m) "
            "and its harmonic lower bound under an eventually critical cap."
        ),
        "theorem": {
            "suffix_span": "H_m=a_(2m-1)-a_(m-2)",
            "layered_energy_floor": ("E_m=m(m-2)(m^2+8m+6)/48 >= m^4/48"),
            "finite_floor": "Z_m^nb >= E_m/(8m^2 H_m) >= m^2/(384 H_m)",
            "critical_floor": "Z_m^nb >= 1/(1536 C log(4m)) eventually",
            "dyadic_sum_liminf": "at least 1/(1536 C log(2))",
            "logarithm": "natural",
        },
        "exhaustive_eight_mark_c1": exhaustive_eight_mark_audit(),
        "fixture_audits": fixture_rows,
        "erdos_turan_suffix_calibrations": erdos_turan_rows(),
        "claim_boundary": {
            "finite_rational_inequality_chain_certified": True,
            "conditional_harmonic_lower_bound_proved_in_memo": True,
            "p18_unconditionally_disproved": False,
            "an_existing_eventually_critical_branch_would_violate_p18_conclusion": True,
            "infinite_eventually_critical_branch_constructed": False,
            "p17_proved": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "erdos_1191_resolved": False,
            "prize_claim_ready": False,
        },
        "conclusions": [
            "The new-birth sector alone has an unavoidable integer harmonic floor.",
            "P18 cannot be treated as a small packing property of a surviving critical branch.",
            "Any P17 proof must retain the terminal R tail to absorb the harmonic Z mass.",
            "Finite Erdos-Turan suffixes refute local occupancy-only decay but do not create one infinite critical branch.",
        ],
    }
    payload["certificate_sha256"] = _canonical_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DIRECTORY
        / "wave13_p18_harmonic_obstruction_certificate_2026-08-29.json",
    )
    arguments = parser.parse_args()
    certificate = build_certificate()
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(certificate["certificate_sha256"])


if __name__ == "__main__":
    main()
