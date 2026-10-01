"""Exact algebra certificate for the Wave 16 terminal potential.

All theorem checks use :class:`fractions.Fraction`.  The certificate audits
only finite coefficient identities and signs; it does not infer an infinite
critical Golomb ruler or resolve Erdos Problem #1191.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from hashlib import sha256
from itertools import pairwise
from pathlib import Path
from typing import Any

DIRECTORY = Path(__file__).resolve().parent
DEFAULT_OUTPUT = DIRECTORY / "wave16_terminal_potential_certificate_2026-08-29.json"
EPOCHS = tuple(2**power for power in range(2, 12))
FEJER_HORIZONS = (4, 8, 16, 32, 64, 128, 256)


def _fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def _canonical_hash(payload: dict[str, Any]) -> str:
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return sha256(canonical.encode("utf-8")).hexdigest()


def suffix_weight(epoch: int, left: int) -> Fraction:
    if left <= 2 * epoch - 3:
        return Fraction(12 * epoch - 5 - 6 * left, 16 * epoch * epoch)
    if left == 2 * epoch - 2:
        return Fraction(11, 16 * epoch * epoch)
    raise ValueError("left is outside the terminal suffix fan")


def next_lower_weight(epoch: int, left: int) -> Fraction:
    if not 2 <= left <= 2 * epoch - 2:
        raise ValueError("left is outside the next lower row")
    return Fraction(4 * epoch - 2 * left + 1, 16 * epoch * epoch)


def _epoch_audit(epoch: int) -> dict[str, Any]:
    denominator = 16 * epoch * epoch
    u_mass = sum(
        (suffix_weight(epoch, left) for left in range(2, 2 * epoch - 1)),
        Fraction(),
    )
    v_mass = sum(
        (next_lower_weight(epoch, left) for left in range(2, 2 * epoch - 1)),
        Fraction(),
    )
    f_mass = Fraction(12 * epoch * epoch - 28 * epoch + 15, denominator)
    cut_full_mass = Fraction((2 * epoch - 1) ** 2, denominator)
    next_bulk_mass = Fraction(3 * (2 * epoch - 1) ** 2, denominator)

    cut_coefficients = {
        index: Fraction((2 * epoch - index) ** 2, denominator)
        for index in range(1, 2 * epoch - 1)
    }
    suffix_expansion_matches = all(
        cut_coefficients[left - 1] - cut_coefficients[left]
        == next_lower_weight(epoch, left)
        for left in range(2, 2 * epoch - 1)
    )
    singleton_mass = Fraction(1, 4 * epoch * epoch)
    r_expansion_matches = (
        cut_coefficients[1] == cut_full_mass
        and suffix_expansion_matches
        and cut_coefficients[2 * epoch - 2] == singleton_mass
    )

    row_mass_matches = True
    for right in range(epoch, 2 * epoch - 1):
        prefix_mass = Fraction(2 * right - 1, 4 * epoch * epoch)
        descendant_mass = (
            Fraction(max(0, right - 3), 2 * epoch * epoch)
            + Fraction(1, 4 * epoch * epoch)
            + Fraction(1, epoch * epoch)
        )
        row_mass_matches &= prefix_mass == descendant_mass

    k_max = 6 * epoch * epoch - 5 * epoch + 1
    rank_min = Fraction(epoch * (epoch + 1), 2)
    promotion_count_ratio = Fraction(k_max, 1) / rank_min
    macro_u_mass = sum(
        (suffix_weight(epoch, left) for left in range(2, epoch + 1)),
        Fraction(),
    )

    return {
        "epoch": epoch,
        "u_mass": _fraction_text(u_mass),
        "u_formula_matches": u_mass
        == Fraction(12 * epoch * epoch - 28 * epoch + 19, denominator),
        "v_mass": _fraction_text(v_mass),
        "v_formula_matches": v_mass
        == Fraction(4 * epoch * epoch - 4 * epoch - 3, denominator),
        "f_mass": _fraction_text(f_mass),
        "cut_full_mass": _fraction_text(cut_full_mass),
        "terminal_mass_equality": u_mass + v_mass == f_mass + cut_full_mass,
        "terminal_common_mass": _fraction_text(u_mass + v_mass),
        "r_expansion_coefficients_match": r_expansion_matches,
        "singleton_cancellation_matches": singleton_mass
        == Fraction(1, 4 * epoch * epoch),
        "next_bulk_mass": _fraction_text(next_bulk_mass),
        "next_bulk_minus_u": _fraction_text(next_bulk_mass - u_mass),
        "next_bulk_minus_u_formula_matches": next_bulk_mass - u_mass
        == Fraction(epoch - 1, epoch * epoch),
        "all_q_row_mass_equalities": row_mass_matches,
        "promotion_count_ratio": _fraction_text(promotion_count_ratio),
        "promotion_count_ratio_below_12": promotion_count_ratio < 12,
        "macro_u_mass": _fraction_text(macro_u_mass),
        "macro_u_mass_below_1": macro_u_mass < 1,
        "delta_below_log_13_certified": promotion_count_ratio < 12 and macro_u_mass < 1,
    }


def _fejer_audit(horizon: int, first_index: int = 2) -> dict[str, Any]:
    denominator = (horizon + 1) ** 2
    weights = {
        index: Fraction((horizon + 1 - index) ** 2, denominator)
        for index in range(first_index, horizon + 1)
    }
    weighted_harmonic = sum(
        (weight / index for index, weight in weights.items()), Fraction()
    )
    harmonic = sum(
        (Fraction(1, index) for index in range(first_index, horizon + 1)),
        Fraction(),
    )
    term_count = horizon - first_index + 1
    index_sum = sum(range(first_index, horizon + 1))
    expanded = (
        harmonic
        - Fraction(2 * term_count, horizon + 1)
        + Fraction(index_sum, denominator)
    )
    ordered = tuple(weights[index] for index in range(first_index, horizon + 1))
    renewal_middle_coefficients = tuple(
        weights[index] - weights[index - 1]
        for index in range(first_index + 1, horizon + 1)
    )
    return {
        "horizon": horizon,
        "first_index": first_index,
        "exact_harmonic_expansion": weighted_harmonic == expanded,
        "weights_strictly_decreasing": all(
            left > right for left, right in pairwise(ordered)
        ),
        "renewal_middle_coefficients_nonpositive": all(
            coefficient <= 0 for coefficient in renewal_middle_coefficients
        ),
        "renewal_terminal_coefficient_nonpositive": -weights[horizon] <= 0,
        "terminal_weight": _fraction_text(weights[horizon]),
        "weight_drop_sum": _fraction_text(weights[first_index] - weights[horizon]),
    }


def build_certificate() -> dict[str, Any]:
    epoch_rows = [_epoch_audit(epoch) for epoch in EPOCHS]
    fejer_rows = [_fejer_audit(horizon) for horizon in FEJER_HORIZONS]
    payload: dict[str, Any] = {
        "schema": "erdos1191.wave16_terminal_potential.v1",
        "date": "2026-08-29",
        "arithmetic": "fractions.Fraction",
        "epochs": list(EPOCHS),
        "epoch_rows": epoch_rows,
        "fejer_rows": fejer_rows,
        "all_exact_checks_pass": all(
            row[key]
            for row in epoch_rows
            for key in (
                "u_formula_matches",
                "v_formula_matches",
                "terminal_mass_equality",
                "r_expansion_coefficients_match",
                "singleton_cancellation_matches",
                "next_bulk_minus_u_formula_matches",
                "all_q_row_mass_equalities",
                "promotion_count_ratio_below_12",
                "macro_u_mass_below_1",
                "delta_below_log_13_certified",
            )
        )
        and all(
            row[key]
            for row in fejer_rows
            for key in (
                "exact_harmonic_expansion",
                "weights_strictly_decreasing",
                "renewal_middle_coefficients_nonpositive",
                "renewal_terminal_coefficient_nonpositive",
            )
        ),
        "scope_flags": {
            "finite_algebra_only": True,
            "infinite_branch_constructed": False,
            "disjoint_floor_premium_proved": False,
            "p17_proved": False,
            "p19_proved": False,
            "p21_proved": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "erdos_1191_resolved": False,
            "problem_unresolved": True,
            "prize_claim_ready": False,
        },
    }
    payload["certificate_sha256"] = _canonical_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    arguments = parser.parse_args()
    arguments.output.write_text(
        json.dumps(build_certificate(), sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
