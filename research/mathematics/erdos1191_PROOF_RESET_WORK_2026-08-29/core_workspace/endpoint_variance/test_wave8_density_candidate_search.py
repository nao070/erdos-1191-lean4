from __future__ import annotations

import json
from fractions import Fraction
from hashlib import sha256

import pytest

from wave8_density_candidate_search import (
    EIGHT_MARK_FINITE_WITNESS,
    FOUR_MARK_INITIAL_ERROR,
    FOUR_MARK_LOCAL_COUNTEREXAMPLE,
    LATEST_SHELL_COUNTEREXAMPLE,
    SIXTEEN_MARK_FINITE_WITNESS,
    UNIVERSAL_INNOVATION_UPPER_BOUND,
    _fast_latest_epoch_events,
    build_report,
    conditional_c1_cap_factor,
    cumulative_first_cross_audit,
    density_event,
    deterministic_c1_search,
    exhaustive_four_mark_audit,
    latest_epoch_events,
    long_secondary_fixture_audit,
    mian_chowla_third_at_661_points,
    renewal_outstanding_transition,
    unrestricted_scaling_event,
)
from wave8_survival_debt_probe import critical_survival_audit


def test_unrestricted_scaling_counterexample_replays_exactly() -> None:
    event = unrestricted_scaling_event()
    assert event.threshold == Fraction(42_449, 2)
    assert event.global_reservoir_count == 5
    assert event.global_margin == Fraction(
        -637_727_146_686_430_915,
        325_192_783_420_663_937_856,
    )
    assert event.global_square_margin > 0


def test_literal_local_candidate_is_refuted_inside_c1_exhaustively() -> None:
    audit = exhaustive_four_mark_audit()
    assert audit.ruler_count == 1_672
    assert audit.activation_event_count == 3_344
    assert audit.negative_global_event_count == 601
    assert audit.negative_square_event_count == 601
    witness = audit.minimum_global_event
    assert witness.points == FOUR_MARK_LOCAL_COUNTEREXAMPLE
    assert witness.threshold == 3
    assert witness.global_reservoir_count == 0
    assert witness.normalized_adjoint_innovation == Fraction(137, 10_976)
    assert witness.global_margin == -FOUR_MARK_INITIAL_ERROR
    survival = critical_survival_audit(FOUR_MARK_LOCAL_COUNTEREXAMPLE, depth=2)
    assert survival.level_counts == (1, 67, 4_879)
    assert survival.survives_requested_depth is True


def test_latest_shell_candidate_fails_at_a_finitely_extendable_m4_event() -> None:
    event = density_event(
        LATEST_SHELL_COUNTEREXAMPLE,
        old_count=4,
        antidiagonal=1,
    )
    assert event.threshold == 72
    assert event.latest_reservoir_count == 0
    assert event.latest_margin == Fraction(-5_539_453, 1_075_200_000)
    assert event.global_reservoir_count == 1
    assert event.global_margin == Fraction(28_181_641, 3_225_600_000)
    survival = critical_survival_audit(LATEST_SHELL_COUNTEREXAMPLE, depth=2)
    assert survival.level_counts == (1, 121, 16_030)
    assert survival.survives_requested_depth is True


def test_m4_global_candidate_survives_the_strong_fixed_witness() -> None:
    event = min(
        latest_epoch_events(EIGHT_MARK_FINITE_WITNESS),
        key=lambda row: row.global_margin,
    )
    assert event.threshold == Fraction(303, 4)
    assert event.global_reservoir_count == 1
    assert event.normalized_adjoint_innovation == Fraction(207_413, 35_532_000)
    assert event.global_margin == Fraction(26_427_287, 3_588_732_000)
    assert event.global_square_margin == Fraction(1_926_931_987, 362_461_932_000)
    survival = critical_survival_audit(EIGHT_MARK_FINITE_WITNESS, depth=2)
    assert survival.level_counts == (1, 90, 10_838)


def test_m8_global_candidate_survives_the_fixed_sixteen_mark_witness() -> None:
    event = min(
        latest_epoch_events(SIXTEEN_MARK_FINITE_WITNESS),
        key=lambda row: row.global_margin,
    )
    assert event.threshold == Fraction(14_141, 8)
    assert event.global_reservoir_count == 59
    assert event.normalized_adjoint_innovation == Fraction(
        771_145_152_181,
        82_911_515_904_000,
    )
    assert event.global_margin == Fraction(
        28_229_471_909_696_479,
        1_172_451_746_398_464_000,
    )
    survival = critical_survival_audit(SIXTEEN_MARK_FINITE_WITNESS, depth=1)
    assert survival.level_counts == (1, 193)


def test_conditional_critical_cap_factor_is_exact_but_requires_nonempty_u() -> None:
    empty = conditional_c1_cap_factor(FOUR_MARK_LOCAL_COUNTEREXAMPLE)
    assert empty.reservoir_nonempty is False
    assert empty.factored_margin is None

    nonempty = conditional_c1_cap_factor(EIGHT_MARK_FINITE_WITNESS)
    assert nonempty.terminal_cap == 266
    assert nonempty.exact_factor == Fraction(2, 399)
    assert nonempty.event.threshold < EIGHT_MARK_FINITE_WITNESS[-1] + 1
    assert (
        nonempty.event.normalized_adjoint_innovation <= UNIVERSAL_INNOVATION_UPPER_BOUND
    )
    assert nonempty.factored_margin is not None
    assert nonempty.factored_margin > 0


def test_initial_error_cumulative_repair_is_only_finite_evidence() -> None:
    four = cumulative_first_cross_audit(FOUR_MARK_LOCAL_COUNTEREXAMPLE)
    assert four.corrected_global_margin == 0
    eight = cumulative_first_cross_audit(EIGHT_MARK_FINITE_WITNESS)
    sixteen = cumulative_first_cross_audit(SIXTEEN_MARK_FINITE_WITNESS)
    assert eight.corrected_global_margin == Fraction(
        830_354_017_403,
        4_352_234_733_000,
    )
    assert sixteen.corrected_global_margin > 0
    assert eight.corrected_square_margin > 0
    assert sixteen.corrected_square_margin > 0


def test_new_pay_only_retains_an_older_renewal_debt() -> None:
    assert renewal_outstanding_transition(
        had_older_debt=True,
        ancestry_cleared=False,
        new_family_paid=True,
    )
    assert not renewal_outstanding_transition(
        had_older_debt=True,
        ancestry_cleared=True,
        new_family_paid=True,
    )
    assert renewal_outstanding_transition(
        had_older_debt=False,
        ancestry_cleared=True,
        new_family_paid=False,
    )
    with pytest.raises(ValueError):
        renewal_outstanding_transition(
            had_older_debt=False,
            ancestry_cleared=False,
            new_family_paid=False,
        )


def test_fast_shared_precompute_matches_independent_event_audits() -> None:
    direct = latest_epoch_events(EIGHT_MARK_FINITE_WITNESS)
    fast = _fast_latest_epoch_events(EIGHT_MARK_FINITE_WITNESS, old_count=4)
    assert tuple(
        (
            row.epoch,
            row.antidiagonal,
            row.threshold,
            row.global_reservoir_count,
            row.normalized_adjoint_innovation,
            row.global_margin,
            row.global_square_margin,
        )
        for row in direct
    ) == tuple(
        (
            row.epoch,
            row.antidiagonal,
            row.threshold,
            row.global_reservoir_count,
            row.normalized_adjoint_innovation,
            row.global_margin,
            row.global_square_margin,
        )
        for row in fast
    )


def test_long_secondary_fixture_and_all_510_events_replay_exactly() -> None:
    points = mian_chowla_third_at_661_points()
    assert len(points) == 682
    assert points[661] == 4_466_351
    assert points[680] == 4_795_424
    assert points[681] == 4_848_816

    audit = long_secondary_fixture_audit()
    assert audit.difference_count == 232_221
    assert audit.points_sha256 == (
        "523c509485873262cf5c51c4ee974a8a9cd5b89b46cec24f9ed59c1f05d57a60"
    )
    assert audit.events_sha256 == (
        "470ac1e6ff85a2b65ff75ce3e10198b55814686b393a9b6adc394e728e3c4ff8"
    )
    assert audit.envelope_holds_through_680 is True
    assert audit.envelope_fails_at_681 is True
    assert audit.activation_event_count == 510
    assert audit.negative_global_event_count == 0
    assert audit.negative_square_event_count == 0
    minimum = audit.minimum_global_event
    assert minimum.epoch == 256
    assert minimum.antidiagonal == 256
    assert minimum.threshold == Fraction(586_977_593, 256)
    assert minimum.global_reservoir_count == 86_368
    assert minimum.normalized_adjoint_innovation == Fraction(
        5_519_259_934_588_816_529_861_353,
        630_054_861_249_549_663_805_112_320,
    )
    assert minimum.global_margin == Fraction(
        10_690_962_122_092_402_001_644_475_250_899_231,
        369_828_085_914_209_633_994_284_050_688_245_760,
    )
    assert audit.infinite_survival_inferred is False


def test_zero_trial_cli_report_has_a_replayable_internal_hash() -> None:
    report = build_report(trials8=0, trials16=0)
    internal_hash = report.pop("report_sha256")
    canonical = json.dumps(report, sort_keys=True, separators=(",", ":"))
    assert sha256(canonical.encode("utf-8")).hexdigest() == internal_hash
    assert internal_hash == (
        "f0da0bec2736d7a813416d701e1067e45e0859a3278109967776585c753ea7ee"
    )


def test_deterministic_search_replays_anchor_and_never_claims_infinity() -> None:
    first = deterministic_c1_search(
        mark_count=8,
        trials=10,
        seed=8_119_108,
        survival_depth=2,
    )
    second = deterministic_c1_search(
        mark_count=8,
        trials=10,
        seed=8_119_108,
        survival_depth=2,
    )
    assert first == second
    assert first.generated_ruler_count == 10
    assert first.unique_ruler_count == 11
    assert first.activation_event_count == 44
    assert first.negative_global_event_count == 0
    assert first.minimum_global_event.points == EIGHT_MARK_FINITE_WITNESS
    assert first.minimum_witness_survival_level_counts == (1, 90, 10_838)
    assert first.infinite_survival_inferred is False


def test_rejects_invalid_scope_parameters() -> None:
    with pytest.raises(ValueError):
        density_event((0, 1, 4, 6), old_count=3, antidiagonal=1)
    with pytest.raises(ValueError):
        deterministic_c1_search(mark_count=4, trials=1, seed=1)
