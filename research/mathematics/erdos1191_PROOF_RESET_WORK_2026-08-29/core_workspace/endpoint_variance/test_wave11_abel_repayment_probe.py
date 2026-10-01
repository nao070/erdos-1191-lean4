from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from wave11_abel_repayment_probe import (
    ExactLogForm,
    build_certificate,
    candidate_margins,
    changing_erdos_turan_calibration,
    cumulative_abel_audit,
    epoch_abel_audit,
    lower_tail_audit,
    split_bulk_floor_audit,
)

DIRECTORY = Path(__file__).resolve().parent
CERTIFICATE = DIRECTORY / "wave11_abel_repayment_certificate_2026-08-29.json"
OPTIMAL_EIGHT = (0, 1, 4, 9, 15, 22, 32, 34)


def test_exact_log_forms_combine_and_compare_without_floating_point() -> None:
    left = ExactLogForm.from_terms(((2, Fraction(1, 2)), (3, Fraction(1, 3))))
    right = ExactLogForm.from_terms(((2, Fraction(1, 2)),))

    assert left - right == ExactLogForm.from_terms(((3, Fraction(1, 3)),))
    assert (left - left).is_zero
    assert (left - right).exact_sign() == 1
    assert (right - left).exact_sign() == -1


def test_one_epoch_abel_repayment_identity_is_exact() -> None:
    audit = epoch_abel_audit(OPTIMAL_EIGHT, m=4)

    assert audit.direct_y == audit.q_positive - audit.t_full_span - audit.a_bulk
    assert audit.residual == audit.direct_y
    assert audit.p_premium == audit.h_hole_premium + audit.r_rearrangement_premium
    assert audit.s_boundary_slack.scale(
        1
    ) + audit.q_positive == audit.t_full_span.scale(2)
    assert audit.lower_shell.ramp_atom_count == 1
    assert audit.lower_shell.ramp_weight_mass == Fraction(5, 64)
    assert audit.direct_y.exact_sign() == 1
    assert audit.p_premium.exact_sign() >= 0
    assert audit.s_boundary_slack.exact_sign() >= 0


def test_cumulative_metrics_and_candidate_algebra_use_global_floor() -> None:
    audit = cumulative_abel_audit(OPTIMAL_EIGHT, epochs=(4,))
    margins = candidate_margins(audit)

    assert audit.residual == audit.direct_y
    assert audit.p_premium == audit.h_hole_premium + audit.r_rearrangement_premium
    assert margins["BULK_ONLY_FULL"] == -(audit.s_boundary_slack + audit.direct_y)
    assert margins["BOUNDARY_ONLY_FULL"] == -(audit.p_premium + audit.direct_y)
    assert margins["MIXED_ZERO_RESIDUAL"] == -audit.direct_y
    assert margins["NORMALIZED_HARMONIC"].exact_sign() in (-1, 0, 1)


def test_lower_quarter_tail_telescope_is_exact_at_every_finite_horizon() -> None:
    for terminal_right_gap in range(4, 8):
        tail = lower_tail_audit(
            OPTIMAL_EIGHT, m=4, terminal_right_gap=terminal_right_gap
        )

        assert tail.initial_repayment == tail.consumed + tail.terminal_remainder
        assert tail.identity_residual.is_zero
        assert tail.initial_repayment.exact_sign() == 1
        assert tail.consumed.exact_sign() == 1
        assert tail.terminal_remainder.exact_sign() == 1


def test_triangular_lower_floor_and_upper_global_floor_split_exactly() -> None:
    split = split_bulk_floor_audit(OPTIMAL_EIGHT, epochs=(4,))
    epoch = epoch_abel_audit(OPTIMAL_EIGHT, m=4)

    assert split.actual_bulk == epoch.a_bulk
    assert split.actual_bulk == split.lower_actual + split.upper_actual
    assert (
        split.lower_actual - epoch.lower_shell.actual_log_mass
        == ExactLogForm.from_terms(((5, Fraction(1, 16)),))
    )
    assert split.lower_floor_termwise_verified
    assert split.lower_actual_minus_floor.exact_sign() == 1
    assert split.upper_actual_minus_floor.exact_sign() >= 0
    assert split.actual_minus_combined_floor.exact_sign() >= 0
    assert split.strengthened_residual == epoch.direct_y
    # The asymptotic two-log split need not dominate the plain floor at m=4.
    assert split.combined_floor_minus_plain_floor.exact_sign() == -1


def test_changing_erdos_turan_calibration_is_explicitly_finite() -> None:
    rows = changing_erdos_turan_calibration(maximum_epoch=16)

    assert len(rows) == 1
    assert rows[0]["epoch"] == 16
    assert rows[0]["mark_count"] == 32
    assert rows[0]["changing_family_only"]
    assert not rows[0]["infinite_branch_inferred"]
    assert 0 < float(rows[0]["Y_m_float_projection"])
    assert 0 < float(rows[0]["Y_over_strengthened_envelope_projection"]) < 1


def test_certificate_replays_and_preserves_finite_scope() -> None:
    expected = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    observed = build_certificate()

    assert observed == expected
    assert observed["exhaustive_eight_mark_c1"]["c1_ruler_count"] == 1_146
    candidates = observed["exhaustive_eight_mark_c1"]["candidates"]
    assert candidates["BULK_ONLY_FULL"]["failure_count"] == 1_146
    assert candidates["BOUNDARY_ONLY_FULL"]["failure_count"] == 1_146
    assert candidates["LOWER_HOLE_QUARTER"]["failure_count"] == 1_146
    assert candidates["NORMALIZED_HARMONIC"]["failure_count"] == 0
    assert candidates["NORMALIZED_HARMONIC"]["exact_margin_sign"] == 1
    assert all(
        row["exact_identity_R_equals_consumed_plus_terminal_remainder"]
        for fixture in observed["fixture_audits"]
        for row in fixture["lower_tail_rows"]
    )
    assert all(
        row["split_bulk_floor"]["lower_floor_termwise_verified"]
        for fixture in observed["fixture_audits"]
        for row in fixture["cumulative_rows"]
    )
    assert observed["conclusions"]["finite_computation_only"]
    assert not observed["conclusions"]["infinite_survival_inferred"]
    assert not observed["conclusions"]["p16_proved"]
    assert not observed["conclusions"]["p15_proved"]
    assert not observed["conclusions"]["erdos_1191_resolved"]
