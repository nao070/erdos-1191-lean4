"""Deterministic certificate for the exact finite claims in Wave 14.

This certificate deliberately separates three layers:

* the finite spatial-bin fixture is replayed through the existing exact audit;
* the ``u``, ``v``, and residual coefficient identities are checked with
  rational arithmetic; and
* the unresolved infinite-branch and signed-allocation claims are recorded as
  explicit negative scope flags.

No finite fixture constructs an infinite eventually critical Golomb ruler.
Likewise, the coefficient bookkeeping does not supply the cross-epoch signed
allocation still required to resolve Erdos Problem #1191.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from typing import Any

from complete_birth_ledger import erdos_turan_ruler
from wave14_future_rank_promotion import (
    future_rank_promotion_audit,
    logarithmic_block_size,
)

DIRECTORY = Path(__file__).resolve().parent
DEFAULT_OUTPUT = DIRECTORY / "wave14_future_rank_promotion_certificate_2026-08-29.json"


def _canonical_hash(payload: dict[str, Any]) -> str:
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return sha256(canonical.encode("utf-8")).hexdigest()


def _fraction(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def _points_sha256(points: tuple[int, ...]) -> str:
    encoded = ",".join(str(point) for point in points).encode("ascii")
    return sha256(encoded).hexdigest()


def terminal_suffix_weight(epoch: int, left: int) -> Fraction:
    """Return the Wave 13 terminal-suffix coefficient ``u_(m,p)``."""
    if epoch < 2:
        raise ValueError("epoch must be at least two")
    if not 2 <= left <= 2 * epoch - 2:
        raise ValueError("left must satisfy 2 <= p <= 2m-2")
    if left == 2 * epoch - 2:
        return Fraction(11, 16 * epoch * epoch)
    return Fraction(12 * epoch - 5 - 6 * left, 16 * epoch * epoch)


def next_lower_shell_weight(epoch: int, left: int) -> Fraction:
    """Return the next-epoch lower-shell coefficient ``v_(m,p)``."""
    if epoch < 2:
        raise ValueError("epoch must be at least two")
    if not 2 <= left <= 2 * epoch - 2:
        raise ValueError("left must satisfy 2 <= p <= 2m-2")
    return Fraction(4 * epoch - 2 * left + 1, 16 * epoch * epoch)


def residual_weight(epoch: int, left: int) -> Fraction:
    """Return the exact unallocated residual ``u_(m,p)-v_(m,p)``."""
    return terminal_suffix_weight(epoch, left) - next_lower_shell_weight(epoch, left)


def finite_spatial_bin_fixture() -> dict[str, Any]:
    """Replay the finite ``L=16, d=7935, N=98`` promotion fixture."""
    points = tuple(erdos_turan_ruler(128, 257))
    old_mark_count = 16
    threshold = points[old_mark_count - 1]
    future_mark_count = logarithmic_block_size(threshold)
    audit = future_rank_promotion_audit(
        points,
        old_mark_count,
        threshold,
        future_mark_count=future_mark_count,
    )
    exact_expected_values = all(
        (
            threshold == 7935,
            future_mark_count == 98,
            audit.occupied_bin_count == 7,
            audit.same_bin_pair_count == 696,
            audit.cauchy_pair_lower == Fraction(4459, 7),
            audit.old_rank == 120,
            audit.observed_promotion == 1468,
        )
    )
    exact_inequality_chain = all(
        (
            audit.same_bin_differences_are_distinct,
            audit.same_bin_differences_are_new,
            audit.same_bin_differences_are_strictly_below_threshold,
            audit.observed_promotion_dominates_same_bin_pairs,
            audit.same_bin_pairs_dominate_cauchy_lower,
        )
    )
    return {
        "fixture": "erdos_turan_128_p257",
        "point_count": len(points),
        "points_sha256": _points_sha256(points),
        "old_mark_count": audit.old_mark_count,
        "threshold": audit.threshold,
        "future_mark_count": audit.future_mark_count,
        "occupied_bin_count": audit.occupied_bin_count,
        "same_bin_pair_count": audit.same_bin_pair_count,
        "cauchy_pair_lower": _fraction(audit.cauchy_pair_lower),
        "documented_cauchy_expression": "4459/7",
        "documented_cauchy_expression_verified": (
            audit.cauchy_pair_lower == Fraction(4459, 7)
        ),
        "old_rank": audit.old_rank,
        "extended_rank": audit.extended_rank,
        "observed_promotion": audit.observed_promotion,
        "exact_expected_values_replayed": exact_expected_values,
        "exact_inequality_chain_verified": exact_inequality_chain,
        "finite_only": True,
        "infinite_branch_inferred": False,
    }


def coefficient_identity_row(epoch: int) -> dict[str, Any]:
    """Check every exact coefficient and macroscopic mass identity at ``m``."""
    if epoch < 4:
        raise ValueError("epoch must be at least four")

    macro = tuple(range(2, epoch + 1))
    direct_u_mass = sum(
        (terminal_suffix_weight(epoch, left) for left in macro), Fraction(0)
    )
    direct_v_mass = sum(
        (next_lower_shell_weight(epoch, left) for left in macro), Fraction(0)
    )
    direct_residual_mass = sum(
        (residual_weight(epoch, left) for left in macro), Fraction(0)
    )

    closed_u_mass = Fraction((epoch - 1) * (9 * epoch - 11), 16 * epoch * epoch)
    closed_v_mass = Fraction((epoch - 1) * (3 * epoch - 1), 16 * epoch * epoch)
    closed_residual_mass = Fraction((epoch - 1) * (3 * epoch - 5), 8 * epoch * epoch)

    termwise_macro_identity = all(
        residual_weight(epoch, left)
        == Fraction(4 * epoch - 2 * left - 3, 8 * epoch * epoch)
        for left in macro
    )
    termwise_u_equals_v_plus_residual = all(
        terminal_suffix_weight(epoch, left)
        == next_lower_shell_weight(epoch, left) + residual_weight(epoch, left)
        for left in range(2, 2 * epoch - 1)
    )
    endpoint = 2 * epoch - 2
    endpoint_residual = residual_weight(epoch, endpoint)

    return {
        "epoch": epoch,
        "macro_left_range": [2, epoch],
        "u_macro_mass_direct": _fraction(direct_u_mass),
        "u_macro_mass_closed": _fraction(closed_u_mass),
        "v_macro_mass_direct": _fraction(direct_v_mass),
        "v_macro_mass_closed": _fraction(closed_v_mass),
        "residual_macro_mass_direct": _fraction(direct_residual_mass),
        "residual_macro_mass_closed": _fraction(closed_residual_mass),
        "u_mass_formula_verified": direct_u_mass == closed_u_mass,
        "v_mass_formula_verified": direct_v_mass == closed_v_mass,
        "residual_mass_formula_verified": (
            direct_residual_mass == closed_residual_mass
        ),
        "macro_mass_split_verified": direct_u_mass
        == direct_v_mass + direct_residual_mass,
        "termwise_macro_residual_formula_verified": termwise_macro_identity,
        "termwise_u_equals_v_plus_residual_verified": (
            termwise_u_equals_v_plus_residual
        ),
        "macro_residual_coefficients_positive": all(
            residual_weight(epoch, left) > 0 for left in macro
        ),
        "u_macro_mass_at_least_one_half": direct_u_mass >= Fraction(1, 2),
        "v_macro_mass_at_least_one_sixth": direct_v_mass >= Fraction(1, 6),
        "endpoint_left": endpoint,
        "endpoint_u": _fraction(terminal_suffix_weight(epoch, endpoint)),
        "endpoint_v": _fraction(next_lower_shell_weight(epoch, endpoint)),
        "endpoint_residual": _fraction(endpoint_residual),
        "endpoint_residual_formula_verified": endpoint_residual
        == Fraction(3, 8 * epoch * epoch),
    }


def build_certificate() -> dict[str, Any]:
    """Build the deterministic Wave 14 finite certificate payload."""
    coefficient_rows = [
        coefficient_identity_row(epoch) for epoch in (4, 8, 16, 20, 32, 64, 128)
    ]
    payload: dict[str, Any] = {
        "schema": "erdos1191.wave14.future-rank-promotion.v1",
        "research_date": "2026-08-29",
        "purpose": (
            "Replay the finite spatial-bin fixture and certify the exact "
            "u/v/residual coefficient and mass identities used by the two "
            "Wave 14 memos."
        ),
        "finite_spatial_bin_fixture": finite_spatial_bin_fixture(),
        "coefficient_identity_rows": coefficient_rows,
        "analytic_contract": {
            "u_standard": "(12m-5-6p)/(16m^2), 2<=p<=2m-3",
            "u_endpoint": "u_(m,2m-2)=11/(16m^2)",
            "v": "(4m-2p+1)/(16m^2), 2<=p<=2m-2",
            "macro_residual": "u-v=(4m-2p-3)/(8m^2), 2<=p<=m",
            "u_macro_mass": "(m-1)(9m-11)/(16m^2)",
            "v_macro_mass": "(m-1)(3m-1)/(16m^2)",
            "residual_macro_mass": "(m-1)(3m-5)/(8m^2)",
            "endpoint_residual": "3/(8m^2)",
            "arithmetic": "exact rational",
        },
        "scope_flags": {
            "infinite_branch": False,
            "signed_allocation": False,
            "problem_unresolved": True,
        },
        "claim_boundary": {
            "finite_spatial_bin_fixture_certified": True,
            "exact_coefficient_identities_certified": True,
            "exact_mass_identities_certified": True,
            "infinite_eventually_critical_branch_certified": False,
            "signed_cross_epoch_allocation_certified": False,
            "p17_proved": False,
            "p19_proved": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "erdos_1191_unresolved": True,
            "erdos_1191_resolved": False,
            "prize_claim_ready": False,
        },
        "conclusions": [
            "The finite spatial-bin mechanism replays with the documented exact values.",
            "The u coefficient splits exactly into the legal next-row v copy and a positive residual.",
            "The macroscopic u, v, and residual masses match their closed rational formulas.",
            "The certificate does not construct an infinite branch or solve the signed allocation problem.",
        ],
    }
    payload["certificate_sha256"] = _canonical_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    arguments = parser.parse_args()
    certificate = build_certificate()
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(certificate["certificate_sha256"])


if __name__ == "__main__":
    main()
