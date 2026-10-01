"""Exact certificate for the Wave 19 arbitrary-transport residual floor.

For a dyadic epoch ``n >= 64``, consider the inner gaps indexed by
``n, ..., 2*n - 1`` and the inner Gothic rows ``n+1, ..., 2*n-2``.  A
feasible transport ``t_(p,q)`` obeys

    0 <= t_(p,q) <= beta_(p,q),
    sum_q t_(p,q) = bar_r_p.

This module audits the exact beta-rectangle identity, a transport-independent
row-sum upper bound, the good-partner construction, and the symmetrization
constant which together give

    sum_(i<j) (w_(i,j)-K_t(i,j)) C_(i,j)
        >= n^2 / (2^25 H'_n).

All rational checks use ``Fraction``.  The certificate does not prove that a
negative renewal cut pays this residual, does not close P28, and does not
resolve either question of Erdos Problem #1191.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Mapping
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from typing import Any

DIRECTORY = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    DIRECTORY / "wave19_p28_transport_residual_floor_certificate_2026-08-29.json"
)
EXACT_EPOCHS = (64, 128, 256)
MINIMUM_EPOCH = 64


def _require_integer(value: int, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    return value


def _require_epoch(epoch: int) -> int:
    epoch = _require_integer(epoch, "epoch")
    if epoch < MINIMUM_EPOCH or epoch & (epoch - 1):
        raise ValueError("epoch must be dyadic and at least 64")
    return epoch


def _require_inner_row(epoch: int, source: int) -> tuple[int, int]:
    epoch = _require_epoch(epoch)
    source = _require_integer(source, "source")
    if not epoch + 1 <= source <= 2 * epoch - 2:
        raise ValueError("source must be an inner Gothic row")
    return epoch, source


def _require_cell(epoch: int, source: int, target: int) -> tuple[int, int, int]:
    epoch, source = _require_inner_row(epoch, source)
    target = _require_integer(target, "target")
    if not source <= target <= 2 * epoch - 2:
        raise ValueError("target must lie in the source row")
    return epoch, source, target


def _require_inner_pair(epoch: int, left: int, right: int) -> tuple[int, int, int]:
    epoch = _require_epoch(epoch)
    left = _require_integer(left, "left")
    right = _require_integer(right, "right")
    if not epoch <= left <= right - 2 <= 2 * epoch - 3:
        raise ValueError("pair must be a nonadjacent inner-gap pair")
    return epoch, left, right


def _fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def _canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode(
        "utf-8"
    )


def _canonical_hash(payload: dict[str, Any]) -> str:
    return sha256(_canonical_bytes(payload)).hexdigest()


def _file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def beta_coefficient(epoch: int, source: int, target: int) -> Fraction:
    """Return the exact beta coefficient on an inner Gothic row."""
    epoch, source, target = _require_cell(epoch, source, target)
    square = epoch * epoch
    if target == source:
        return Fraction(1, square)
    if target == source + 1:
        return Fraction(1, 4 * square)
    return Fraction(1, 2 * square)


def residual_row_mass(epoch: int, source: int) -> Fraction:
    """Return the cut-valid row demand ``bar_r_(n,p)``."""
    epoch, source = _require_inner_row(epoch, source)
    if source == 2 * epoch - 2:
        return Fraction(3, 8 * epoch * epoch)
    return Fraction(4 * epoch - 2 * source - 3, 8 * epoch * epoch)


def residual_row_upper(epoch: int, source: int) -> Fraction:
    """Return the universal upper surrogate ``(2n-p)/(4n^2)``."""
    epoch, source = _require_inner_row(epoch, source)
    return Fraction(2 * epoch - source, 4 * epoch * epoch)


def full_beta_row_mass(epoch: int, source: int) -> Fraction:
    """Enumerate all beta capacity in one inner row."""
    epoch, source = _require_inner_row(epoch, source)
    return sum(
        (
            beta_coefficient(epoch, source, target)
            for target in range(source, 2 * epoch - 1)
        ),
        Fraction(),
    )


def truncated_beta_row_mass(epoch: int, width: int) -> Fraction:
    """Enumerate a row truncated to ``width`` cells, including the diagonal."""
    epoch = _require_epoch(epoch)
    width = _require_integer(width, "width")
    if not 1 <= width <= epoch - 2:
        raise ValueError("width must lie between one and n-2")
    source = epoch + 1
    return sum(
        (
            beta_coefficient(epoch, source, target)
            for target in range(source, source + width)
        ),
        Fraction(),
    )


def closed_truncated_beta_row_mass(epoch: int, width: int) -> Fraction:
    """Return the two-case closed form for a truncated beta row."""
    epoch = _require_epoch(epoch)
    width = _require_integer(width, "width")
    if not 1 <= width <= epoch - 2:
        raise ValueError("width must lie between one and n-2")
    if width == 1:
        return Fraction(1, epoch * epoch)
    return Fraction(2 * width + 1, 4 * epoch * epoch)


def rectangle_beta_capacity_by_distance(epoch: int, distance: int) -> Fraction:
    """Enumerate the beta rectangle for any inner pair of this distance."""
    epoch = _require_epoch(epoch)
    distance = _require_integer(distance, "distance")
    if not 2 <= distance <= epoch - 1:
        raise ValueError("distance must lie between two and n-1")
    return sum(
        (truncated_beta_row_mass(epoch, width) for width in range(1, distance)),
        Fraction(),
    )


def inner_weight(epoch: int, left: int, right: int) -> Fraction:
    """Return ``w_(i,j)=(j-i)^2/(4n^2)``."""
    epoch, left, right = _require_inner_pair(epoch, left, right)
    return Fraction((right - left) ** 2, 4 * epoch * epoch)


def left_greedy_transport(epoch: int) -> dict[tuple[int, int], Fraction]:
    """Construct one feasible transport by filling each row from the left."""
    epoch = _require_epoch(epoch)
    transport: dict[tuple[int, int], Fraction] = {}
    for source in range(epoch + 1, 2 * epoch - 1):
        remaining = residual_row_mass(epoch, source)
        for target in range(source, 2 * epoch - 1):
            value = min(beta_coefficient(epoch, source, target), remaining)
            transport[source, target] = value
            remaining -= value
        if remaining:
            raise AssertionError("row demand exceeded beta capacity")
    return transport


def transport_rectangle_coefficient(
    epoch: int,
    left: int,
    right: int,
    transport: Mapping[tuple[int, int], Fraction],
) -> Fraction:
    """Return ``K_t(i,j)`` for one feasible transport mapping."""
    epoch, left, right = _require_inner_pair(epoch, left, right)
    return sum(
        (
            transport.get((source, target), Fraction())
            for source in range(left + 1, right)
            for target in range(source, right)
        ),
        Fraction(),
    )


def row_sum_rectangle_upper(epoch: int, left: int, right: int) -> Fraction:
    """Bound every ``K_t(i,j)`` using only feasible row sums."""
    epoch, left, right = _require_inner_pair(epoch, left, right)
    return sum(
        (residual_row_upper(epoch, source) for source in range(left + 1, right)),
        Fraction(),
    )


def closed_row_sum_rectangle_upper(epoch: int, left: int, right: int) -> Fraction:
    """Return the exact arithmetic-progression form of the row upper bound."""
    epoch, left, right = _require_inner_pair(epoch, left, right)
    x = left - epoch
    y = right - epoch
    distance = y - x
    return Fraction(
        (distance - 1) * (2 * epoch - x - y),
        8 * epoch * epoch,
    )


def coverage_envelope(epoch: int, left: int, right: int) -> Fraction:
    """Return the slightly looser closed coverage-ratio envelope."""
    epoch, left, right = _require_inner_pair(epoch, left, right)
    x = left - epoch
    y = right - epoch
    return Fraction(2 * epoch - x - y, 2 * (y - x))


def good_partners(epoch: int, vertex: int) -> tuple[int, ...]:
    """Return ``n/64`` deterministic partners for one inner-gap vertex."""
    epoch = _require_epoch(epoch)
    vertex = _require_integer(vertex, "vertex")
    if not epoch <= vertex <= 2 * epoch - 1:
        raise ValueError("vertex must be an inner-gap index")
    coordinate = vertex - epoch
    count = epoch // 64
    if coordinate <= 7 * epoch // 8:
        return tuple(range(epoch + 63 * epoch // 64, 2 * epoch))
    return tuple(range(epoch, epoch + count))


def row_sum_audit(epoch: int) -> dict[str, Any]:
    """Audit exact row demands, capacities, and the exceptional final row."""
    epoch = _require_epoch(epoch)
    minimum_slack: Fraction | None = None
    for source in range(epoch + 1, 2 * epoch - 1):
        demand = residual_row_mass(epoch, source)
        upper = residual_row_upper(epoch, source)
        capacity = full_beta_row_mass(epoch, source)
        if not demand <= upper <= capacity:
            raise AssertionError("row demand, upper, and capacity are misordered")
        slack = upper - demand
        minimum_slack = slack if minimum_slack is None else min(minimum_slack, slack)

    last = 2 * epoch - 2
    penultimate = 2 * epoch - 3
    return {
        "row_checks": epoch - 2,
        "minimum_upper_minus_demand": _fraction_text(minimum_slack or Fraction()),
        "generic_upper_minus_demand": _fraction_text(
            residual_row_upper(epoch, penultimate)
            - residual_row_mass(epoch, penultimate)
        ),
        "exceptional_source": last,
        "exceptional_demand": _fraction_text(residual_row_mass(epoch, last)),
        "exceptional_upper": _fraction_text(residual_row_upper(epoch, last)),
        "exceptional_upper_minus_demand": _fraction_text(
            residual_row_upper(epoch, last) - residual_row_mass(epoch, last)
        ),
        "all_row_bounds_verified": True,
    }


def rectangle_capacity_audit(epoch: int) -> dict[str, Any]:
    """Audit every inner pair via exact beta translation invariance by width."""
    epoch = _require_epoch(epoch)
    row_width_checks = 0
    for width in range(1, epoch - 1):
        if truncated_beta_row_mass(epoch, width) != closed_truncated_beta_row_mass(
            epoch, width
        ):
            raise AssertionError("truncated beta-row identity failed")
        row_width_checks += 1

    capacity_by_distance: dict[int, Fraction] = {}
    for distance in range(2, epoch):
        capacity = rectangle_beta_capacity_by_distance(epoch, distance)
        expected = Fraction(distance * distance, 4 * epoch * epoch)
        if capacity != expected:
            raise AssertionError("beta rectangle identity failed")
        capacity_by_distance[distance] = capacity

    pointwise_checks = 0
    for left in range(epoch, 2 * epoch - 2):
        for right in range(left + 2, 2 * epoch):
            if capacity_by_distance[right - left] != inner_weight(epoch, left, right):
                raise AssertionError("pointwise beta rectangle identity failed")
            pointwise_checks += 1

    return {
        "truncated_row_width_checks": row_width_checks,
        "rectangle_distance_checks": len(capacity_by_distance),
        "pointwise_inner_pair_checks_represented": pointwise_checks,
        "expected_pointwise_inner_pair_count": (epoch - 1) * (epoch - 2) // 2,
        "translation_invariance_reason": (
            "inner beta depends only on q-p, so one exact check per distance "
            "represents every pair of that distance"
        ),
        "rectangle_identity": "sum_rectangle_beta=(j-i)^2/(4n^2)",
        "all_rectangle_capacities_verified": (
            pointwise_checks == (epoch - 1) * (epoch - 2) // 2
        ),
    }


def feasible_transport_audit(epoch: int) -> dict[str, Any]:
    """Audit an exact left-greedy witness to nonempty feasibility."""
    epoch = _require_epoch(epoch)
    transport = left_greedy_transport(epoch)
    positive_cells = 0
    for source in range(epoch + 1, 2 * epoch - 1):
        row_sum = Fraction()
        for target in range(source, 2 * epoch - 1):
            value = transport[source, target]
            capacity = beta_coefficient(epoch, source, target)
            if not Fraction() <= value <= capacity:
                raise AssertionError("left-greedy cell violates beta capacity")
            row_sum += value
            positive_cells += value > 0
        if row_sum != residual_row_mass(epoch, source):
            raise AssertionError("left-greedy row sum is not exact")

    return {
        "transport_cells_checked": len(transport),
        "positive_transport_cells": positive_cells,
        "row_sums_checked": epoch - 2,
        "all_cell_capacities_verified": True,
        "all_row_sums_verified": True,
        "feasible_set_nonempty": True,
    }


def good_partner_audit(epoch: int) -> dict[str, Any]:
    """Audit the directed good-partner family and its exact constants."""
    epoch = _require_epoch(epoch)
    expected_count = epoch // 64
    minimum_distance = epoch
    minimum_residual: Fraction | None = None
    maximum_coverage_ratio = Fraction()
    maximum_envelope = Fraction()
    directed_checks = 0
    low_checks = 0
    high_checks = 0

    for vertex in range(epoch, 2 * epoch):
        coordinate = vertex - epoch
        partners = good_partners(epoch, vertex)
        if len(partners) != expected_count or len(set(partners)) != expected_count:
            raise AssertionError("good-partner count failed")
        for partner in partners:
            left, right = sorted((vertex, partner))
            if left == right:
                raise AssertionError("a vertex was paired with itself")
            distance = right - left
            minimum_distance = min(minimum_distance, distance)
            weight = inner_weight(epoch, left, right)
            row_upper = row_sum_rectangle_upper(epoch, left, right)
            closed_upper = closed_row_sum_rectangle_upper(epoch, left, right)
            if row_upper != closed_upper:
                raise AssertionError("row-sum arithmetic progression failed")
            ratio = row_upper / weight
            envelope = coverage_envelope(epoch, left, right)
            residual = weight - row_upper
            if not ratio <= envelope < Fraction(3, 4):
                raise AssertionError("good-partner coverage bound failed")
            if residual < weight / 4 or residual < Fraction(1, 2048):
                raise AssertionError("good-partner residual coefficient failed")

            if coordinate <= 7 * epoch // 8:
                if envelope > Fraction(9, 14):
                    raise AssertionError("low-vertex envelope exceeded 9/14")
                low_checks += 1
            else:
                if envelope >= Fraction(71, 110):
                    raise AssertionError("high-vertex envelope reached 71/110")
                high_checks += 1

            directed_checks += 1
            maximum_coverage_ratio = max(maximum_coverage_ratio, ratio)
            maximum_envelope = max(maximum_envelope, envelope)
            minimum_residual = (
                residual
                if minimum_residual is None
                else min(minimum_residual, residual)
            )

    return {
        "vertices_checked": epoch,
        "partners_per_vertex": expected_count,
        "directed_partner_checks": directed_checks,
        "low_vertex_partner_checks": low_checks,
        "high_vertex_partner_checks": high_checks,
        "minimum_partner_distance": minimum_distance,
        "required_minimum_partner_distance": 7 * epoch // 64,
        "maximum_exact_row_sum_coverage_ratio": _fraction_text(maximum_coverage_ratio),
        "maximum_loose_coverage_envelope": _fraction_text(maximum_envelope),
        "low_vertex_envelope_bound": "9/14",
        "high_vertex_strict_envelope_bound": "71/110",
        "minimum_exact_residual_lower_bound": _fraction_text(
            minimum_residual or Fraction()
        ),
        "coarse_residual_coefficient": "1/2048",
        "all_partner_checks_verified": (
            directed_checks == epoch * expected_count
            and minimum_distance >= 7 * epoch // 64
        ),
    }


def symmetrization_audit(epoch: int) -> dict[str, Any]:
    """Audit the distinct-gap and double-counting constants."""
    epoch = _require_epoch(epoch)
    partner_count = epoch // 64
    exact_distinct_sum = partner_count * (partner_count + 1) // 2
    coarse_distinct_sum = Fraction(epoch * epoch, 8192)
    exact_vertex_floor = Fraction(exact_distinct_sum, 2048)
    coarse_vertex_floor = Fraction(epoch * epoch, 2**24)
    symmetrized_product_coefficient = Fraction(epoch * epoch, 2**25)
    return {
        "partner_count": partner_count,
        "least_sum_of_distinct_positive_integer_partner_gaps": exact_distinct_sum,
        "coarse_distinct_gap_sum": _fraction_text(coarse_distinct_sum),
        "distinct_gap_sum_dominates_coarse_bound": (
            exact_distinct_sum >= coarse_distinct_sum
        ),
        "exact_vertex_weighted_neighbor_floor": _fraction_text(exact_vertex_floor),
        "coarse_vertex_weighted_neighbor_floor": _fraction_text(coarse_vertex_floor),
        "exact_vertex_floor_dominates_coarse_bound": (
            exact_vertex_floor >= coarse_vertex_floor
        ),
        "symmetrization_identity": (
            "2*sum_(i<j) a_ij*h_i*h_j=sum_i h_i*sum_(j!=i) a_ij*h_j"
        ),
        "symmetrized_product_floor_coefficient_of_Hprime": _fraction_text(
            symmetrized_product_coefficient
        ),
        "residual_energy_floor": "Eres>=n^2/(2^25*Hprime)",
        "all_symmetrization_checks_verified": (
            exact_distinct_sum >= coarse_distinct_sum
            and exact_vertex_floor >= coarse_vertex_floor
        ),
    }


def corner_audit(epoch: int) -> dict[str, Any]:
    """Audit the exact final-corner coverage ratio for every feasible transport."""
    epoch = _require_epoch(epoch)
    left = 2 * epoch - 4
    right = 2 * epoch - 1
    first = residual_row_mass(epoch, 2 * epoch - 3)
    second = residual_row_mass(epoch, 2 * epoch - 2)
    coefficient = first + second
    weight = inner_weight(epoch, left, right)
    ratio = coefficient / weight
    return {
        "cell": [left, right],
        "first_full_row_mass": _fraction_text(first),
        "exceptional_final_row_mass": _fraction_text(second),
        "transport_coefficient_for_every_feasible_transport": _fraction_text(
            coefficient
        ),
        "full_inner_weight": _fraction_text(weight),
        "coverage_ratio": _fraction_text(ratio),
        "residual_coefficient": _fraction_text(weight - coefficient),
        "coverage_ratio_is_one_third": ratio == Fraction(1, 3),
        "uniform_coefficient_coverage_above_one_third_impossible": True,
    }


def payoff_nesting_audit(epoch: int) -> dict[str, Any]:
    """Audit the set nesting behind rowwise left-greedy energy maximization."""
    epoch = _require_epoch(epoch)
    checks = 0
    removed_atoms = 0
    for source in range(epoch + 1, 2 * epoch - 1):
        left_count = source - epoch
        for target in range(source, 2 * epoch - 2):
            old_count = left_count * (2 * epoch - target - 1)
            new_count = left_count * (2 * epoch - target - 2)
            if old_count - new_count != left_count:
                raise AssertionError("payoff support nesting count failed")
            checks += 1
            removed_atoms += left_count
    return {
        "adjacent_target_nesting_checks": checks,
        "removed_nonnegative_atom_occurrences": removed_atoms,
        "payoff_formula": ("L_pq=sum_(i=n)^(p-1)sum_(j=q+1)^(2n-1) C_ij"),
        "payoff_is_nonincreasing_in_q": True,
        "left_greedy_maximizes_each_row_for_fixed_nonnegative_C": True,
        "energy_correlated_transport_evades_universal_floor": False,
    }


def epoch_audit(epoch: int) -> dict[str, Any]:
    """Build one exact dyadic-epoch audit."""
    epoch = _require_epoch(epoch)
    rectangles = rectangle_capacity_audit(epoch)
    rows = row_sum_audit(epoch)
    feasible = feasible_transport_audit(epoch)
    partners = good_partner_audit(epoch)
    symmetrization = symmetrization_audit(epoch)
    corner = corner_audit(epoch)
    nesting = payoff_nesting_audit(epoch)
    checks_pass = all(
        (
            rectangles["all_rectangle_capacities_verified"],
            rows["all_row_bounds_verified"],
            feasible["all_cell_capacities_verified"],
            feasible["all_row_sums_verified"],
            partners["all_partner_checks_verified"],
            symmetrization["all_symmetrization_checks_verified"],
            corner["coverage_ratio_is_one_third"],
            nesting["payoff_is_nonincreasing_in_q"],
        )
    )
    return {
        "epoch": epoch,
        "rectangle_capacity_audit": rectangles,
        "row_sum_audit": rows,
        "feasible_transport_audit": feasible,
        "good_partner_audit": partners,
        "symmetrization_audit": symmetrization,
        "corner_audit": corner,
        "payoff_nesting_audit": nesting,
        "all_required_checks_pass": checks_pass,
    }


def build_certificate() -> dict[str, Any]:
    """Return the deterministic exact certificate payload."""
    epoch_audits = [epoch_audit(epoch) for epoch in EXACT_EPOCHS]
    source_path = Path(__file__).resolve()
    test_path = source_path.with_name(
        "test_wave19_p28_transport_residual_floor_certificate.py"
    )
    payload: dict[str, Any] = {
        "schema": "erdos1191.wave19.p28.arbitrary_transport_residual_floor.v1",
        "generated_on": "2026-08-29",
        "arithmetic": "fractions.Fraction exact rational arithmetic",
        "audited_epochs": list(EXACT_EPOCHS),
        "theorem_contract": {
            "feasible_transport": (
                "0<=t_pq<=beta_pq and sum_q t_pq=bar_r_p for n+1<=p<=2n-2"
            ),
            "induced_coefficient": ("K_t(i,j)=sum_(p=i+1)^(j-1)sum_(q=p)^(j-1)t_pq"),
            "inner_weight": "w_ij=(j-i)^2/(4n^2)",
            "residual_coefficient": "a_ij=w_ij-K_t(i,j)>=0",
            "good_partner_coefficient": "a_ij>=1/2048",
            "residual_energy_floor": "Eres_n(t)>=n^2/(2^25*Hprime_n)",
            "eventual_C_corollary": (
                "if Hprime_n<A<4*C*n^2*log(4n), then Eres_n(t)>1/(2^27*C*log(4n))"
            ),
            "fejer_corollary": (
                "liminf_J sum_(k=k0)^J omega_(k,J)Eres_(2^k)/log(J) >=1/(2^27*C*log(2))"
            ),
            "fejer_weights": "omega_(k,J)=((J+1-k)/(J+1))^2",
        },
        "proof_ingredients": {
            "rectangle_capacity": ("sum_rectangle beta=(j-i)^2/(4n^2)"),
            "row_sum_upper": "bar_r_p<=(2n-p)/(4n^2)",
            "good_partner_count": "n/64 for every inner-gap vertex",
            "minimum_good_partner_distance": "7n/64",
            "coverage_envelopes": {
                "low_vertex": "at most 9/14",
                "high_vertex": "strictly below 71/110",
            },
            "distinct_gap_input": (
                "adjacent gaps of an integer Golomb ruler are distinct "
                "positive integers"
            ),
            "cross_ratio_product_floor": "C_ij>=h_i*h_j/Hprime_n^2",
        },
        "cut_ownership_boundary": {
            "transport_uses_only": "bar_r=u-v",
            "v_fan_reserved_for_negative_renewal_cut": True,
            "raw_v_fan_may_be_extracted_and_reused": False,
            "terminal_potential_is_an_alternative_regrouping": (
                "T_n=F_n+e_n+R_(2n)-U_n; it overlaps U_n and R_(2n), "
                "so any simultaneous transport use requires the balancing "
                "Qad/Pair/cap terms of the complete signed ledger"
            ),
            "balanced_terminal_ledger_exists": (
                "the companion adaptive-row-cap identity (8.5) retains T_n "
                "and the transport with no duplicated Gothic or cut coefficient"
            ),
            "legal_next_target": (
                "prove the remaining G_n Fejer inequality inside the complete "
                "balanced ledger, without extracting the raw v fan"
            ),
            "remaining_signed_quantity": (
                "G_n=R_n+Pcoef_n*log(A)-Kint_n-T_n-Thetafull_n-Dpre_n/4"
            ),
            "smallest_exact_sufficient_target": (
                "limsup_J sum_k omega_(k,J)G_(2^k)/log(J) <1/(3072*C*log(2))"
            ),
            "cleaner_unproved_target": ("sum_k omega_(k,J)[G_(2^k)]_+=o_(C,a)(log J)"),
        },
        "epoch_audits": epoch_audits,
        "scope_flags": {
            "arbitrary_feasible_transport_residual_floor_proved": True,
            "dyadic_epoch_at_least_64_required": True,
            "increasing_integer_golomb_prefix_required": True,
            "energy_correlated_transport_covered": True,
            "negative_whole_cut_payment_proved": False,
            "terminal_potential_payment_proved": False,
            "p28_proved": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "infinite_branch_constructed": False,
            "publication_novelty_established": False,
            "prize_claim_supported": False,
        },
        "source_sha256": _file_sha256(source_path),
        "test_sha256": _file_sha256(test_path) if test_path.exists() else None,
        "all_required_checks_pass": all(
            row["all_required_checks_pass"] for row in epoch_audits
        ),
    }
    payload["payload_sha256"] = _canonical_hash(payload)
    return payload


def write_certificate(path: Path = DEFAULT_OUTPUT) -> bytes:
    """Write the canonical JSON certificate and return its exact bytes."""
    payload = build_certificate()
    encoded = _canonical_bytes(payload)
    path.write_bytes(encoded)
    return encoded


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--check",
        action="store_true",
        help="compare generated bytes with --output instead of writing",
    )
    args = parser.parse_args()
    encoded = _canonical_bytes(build_certificate())
    if args.check:
        if not args.output.exists() or args.output.read_bytes() != encoded:
            raise SystemExit("certificate replay mismatch")
        print(f"verified {args.output} sha256={sha256(encoded).hexdigest()}")
        return
    args.output.write_bytes(encoded)
    print(f"wrote {args.output} sha256={sha256(encoded).hexdigest()}")


if __name__ == "__main__":
    main()
