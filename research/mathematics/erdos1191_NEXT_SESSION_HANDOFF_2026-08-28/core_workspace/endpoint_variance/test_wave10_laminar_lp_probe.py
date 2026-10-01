from __future__ import annotations

import json
from fractions import Fraction
from itertools import pairwise
from pathlib import Path

from wave10_laminar_lp_probe import (
    PERFECT_FOUR,
    audit_laminar_tile_lp,
    audit_rlp_all_subsets,
    build_certificate,
    scale_slack_no_go,
)

DIRECTORY = Path(__file__).resolve().parent
CERTIFICATE = DIRECTORY / "wave10_laminar_lp_certificate_2026-08-29.json"


def test_all_subset_rlp_dynamic_program_is_exact_on_perfect_four() -> None:
    audit = audit_rlp_all_subsets(PERFECT_FOUR)

    assert audit.epoch_moduli == ((1, 2), (2, 7))
    assert audit.selection_vector_count == 5
    assert audit.reachable_positive_totals == 5
    assert audit.minimum_slack == 1
    assert audit.minimum_slack_choices == ((1, 1),)
    assert audit.maximum_pressure == Fraction(2, 3)
    assert audit.maximum_pressure_choices == ((1, 1), (2, 1))
    assert audit.violation_count == 0


def test_tile_primal_and_dual_match_and_majorize_the_exact_objective() -> None:
    audit = audit_laminar_tile_lp("perfect_four", PERFECT_FOUR)

    assert audit.epoch_count == 2
    assert audit.nonadjacent_genuine_pair_count == 1
    assert audit.exact_retained_cross_ratio_lower_objective == Fraction(1, 98)
    assert audit.exact_h_objective == Fraction(2, 1_715)
    assert audit.tile_lp_primal == Fraction(576, 1_715)
    assert audit.tile_lp_dual == audit.tile_lp_primal
    assert audit.exact_h_objective <= audit.tile_lp_primal
    assert audit.actual_count_capacity_violations == 0
    assert audit.global_magnitude_capacity_violations == 0
    assert tuple(row.epoch for row in audit.epoch_rows) == (1, 2)
    assert audit.epoch_rows[0].exact_h_objective == 0
    assert audit.epoch_rows[1].exact_h_objective == Fraction(2, 1_715)
    assert audit.epoch_rows[1].exact_retained_cross_ratio_lower_objective == Fraction(
        1, 98
    )


def test_common_dilation_makes_rlp_slack_and_objective_increase_together() -> None:
    audit = scale_slack_no_go(PERFECT_FOUR, scales=(1, 2, 3, 4))

    assert tuple(row.scale for row in audit) == (1, 2, 3, 4)
    assert all(row.all_prefix_c1 for row in audit)
    assert tuple(row.minimum_rlp_slack for row in audit) == (1, 2, 3, 4)
    objectives = tuple(row.retained_cross_ratio_lower_objective for row in audit)
    assert objectives == tuple(
        Fraction(scale * scale, 2 * (6 * scale + 1) ** 2) for scale in (1, 2, 3, 4)
    )
    assert all(left < right for left, right in pairwise(objectives))


def test_certificate_replays_byte_identically_and_keeps_scope_guardrails() -> None:
    expected = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    observed = build_certificate()

    assert observed == expected
    assert observed["candidate_verdicts"]["RLP_TILE_COUPLING"]["verdict"] == (
        "NO_COUPLING_IN_THE_TESTED_RELAXATION"
    )
    assert observed["conclusions"]["finite_computation_only"]
    assert not observed["conclusions"]["infinite_survival_inferred"]
    assert not observed["conclusions"]["p15_proved"]
    assert not observed["conclusions"]["erdos_1191_resolved"]
