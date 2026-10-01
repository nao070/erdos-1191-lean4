import json
from fractions import Fraction
from hashlib import sha256
from pathlib import Path

from wave6_hall_candidate_probe import (
    COUNTEREXAMPLE_32_POINTS,
    COUNTEREXAMPLE_64_POINTS,
    COUNTEREXAMPLE_POINTS,
    adjacent_nn_pressure,
    audit_candidate_witness,
    critical_modulus_cap,
    scaled_candidate_value,
    targeted_extension_search,
)
from wave6_hall_candidate_probe_certificate import (
    build_certificate,
    canonical_hash,
)

SAWTOOTH_16 = (
    0,
    3,
    17,
    31,
    39,
    47,
    55,
    63,
    183,
    303,
    423,
    543,
    663,
    783,
    903,
    1023,
)


def test_independent_scorer_recovers_hand_checked_sawtooth_band() -> None:
    # Catches using pair count instead of same-lag family demand.
    pressure = adjacent_nn_pressure(SAWTOOTH_16, old_epoch=8)
    assert pressure.ratio == Fraction(12, 113)
    assert (pressure.lower, pressure.upper) == (8, 120)
    assert (pressure.demand, pressure.width) == (12, 113)
    assert tuple(
        (row.epoch, row.lag, row.demand, row.lower, row.upper)
        for row in pressure.families
    ) == (
        (8, 1, 3, 8, 8),
        (8, 2, 2, 16, 16),
        (16, 1, 7, 120, 120),
    )


def test_counterexample_has_exact_pressure_and_violates_candidate() -> None:
    # Catches omitting either represented epoch or using real rather than
    # inclusive integer width.
    pressure = adjacent_nn_pressure(COUNTEREXAMPLE_POINTS, old_epoch=8)
    assert pressure.ratio == Fraction(9, 14)
    assert (pressure.lower, pressure.upper) == (91, 104)
    assert (pressure.demand, pressure.width) == (9, 14)
    assert tuple(
        (row.epoch, row.lag, row.demand, row.lower, row.upper)
        for row in pressure.families
    ) == (
        (8, 2, 2, 91, 92),
        (16, 1, 7, 94, 104),
    )
    assert scaled_candidate_value(pressure, old_epoch=8) == Fraction(2592, 49)


def test_counterexample_is_golomb_and_all_prefix_c1_exactly() -> None:
    # Catches trusting the search state's used-difference set or float logs.
    audit = audit_candidate_witness(COUNTEREXAMPLE_POINTS, old_epoch=8)
    assert audit.is_golomb
    assert audit.pair_count == audit.difference_count == 120
    assert audit.sorted_difference_sha256 == (
        "20489f245d7935c77e244f4385f4436b8e2696af9844b846c8b2f973a5c1ac3f"
    )
    assert audit.prefix_moduli == (
        2,
        19,
        35,
        80,
        128,
        172,
        219,
        320,
        416,
        510,
        614,
        711,
        809,
        904,
        1003,
    )
    assert audit.prefix_caps == (
        5,
        19,
        44,
        80,
        129,
        190,
        266,
        355,
        460,
        580,
        715,
        866,
        1034,
        1218,
        1419,
    )
    assert audit.all_prefix_c1
    assert not audit.candidate_holds
    assert audit.scaled_value == Fraction(2592, 49)


def test_independent_log_enclosure_hits_boundary_caps() -> None:
    # Catches a one-unit error when 3, 5, 7, 9, or 10 is cap-tight nearby.
    assert tuple(critical_modulus_cap(n) for n in range(2, 17)) == (
        5,
        19,
        44,
        80,
        129,
        190,
        266,
        355,
        460,
        580,
        715,
        866,
        1034,
        1218,
        1419,
    )


def test_one_32_mark_ruler_violates_two_consecutive_transitions() -> None:
    # Catches recording an unaudited beam state or only its 16-mark prefix.
    assert COUNTEREXAMPLE_32_POINTS[:16] == COUNTEREXAMPLE_POINTS
    audit = audit_candidate_witness(COUNTEREXAMPLE_32_POINTS, old_epoch=16)
    assert audit.is_golomb
    assert audit.pair_count == audit.difference_count == 496
    assert audit.sorted_difference_sha256 == (
        "9f20726d727233a114634d5c557b7535a926c228862bce9c8a2919bf11ce6c42"
    )
    assert audit.all_prefix_c1
    assert audit.pressure.ratio == Fraction(17, 28)
    assert (audit.pressure.lower, audit.pressure.upper) == (488, 515)
    assert (audit.pressure.demand, audit.pressure.width) == (17, 28)
    assert tuple(
        (row.epoch, row.lag, row.demand, row.lower, row.upper)
        for row in audit.pressure.families
    ) == (
        (16, 5, 3, 488, 493),
        (32, 2, 14, 495, 515),
    )
    assert audit.scaled_value == Fraction(4624, 49)
    assert not audit.candidate_holds
    assert audit.prefix_moduli[-1] == 4931
    assert audit.prefix_caps[-1] == 7097


def test_targeted_beam_is_seeded_and_enforces_prefix_caps() -> None:
    # Catches a non-reproducible proposal stream or a missing per-prefix cap.
    result = targeted_extension_search(
        COUNTEREXAMPLE_POINTS,
        target_count=18,
        beam_width=4,
        candidates_per_state=8,
        seed=7,
        target_gap=250,
    )
    assert result.expanded_state_count == 488
    assert result.best_points == (
        *COUNTEREXAMPLE_POINTS,
        1041,
        1291,
    )
    assert result.best_points[-1] + 1 <= critical_modulus_cap(18)


def test_one_64_mark_ruler_violates_three_consecutive_transitions() -> None:
    # Catches retaining the exploratory 64-mark state without an exact audit.
    assert COUNTEREXAMPLE_64_POINTS[:32] == COUNTEREXAMPLE_32_POINTS
    audit = audit_candidate_witness(COUNTEREXAMPLE_64_POINTS, old_epoch=32)
    assert audit.is_golomb
    assert audit.pair_count == audit.difference_count == 2016
    assert audit.sorted_difference_sha256 == (
        "fd3e33ac286ab6748fdf133a6562ec4f6573723cbac4047ef26b432fee27a836"
    )
    assert audit.all_prefix_c1
    assert audit.pressure.ratio == Fraction(45, 118)
    assert (audit.pressure.lower, audit.pressure.upper) == (398, 515)
    assert (audit.pressure.demand, audit.pressure.width) == (45, 118)
    assert tuple(
        (row.epoch, row.lag, row.demand, row.lower, row.upper)
        for row in audit.pressure.families
    ) == (
        (32, 2, 14, 495, 515),
        (64, 1, 31, 398, 510),
    )
    assert audit.scaled_value == Fraction(259200, 3481)
    assert not audit.candidate_holds
    assert tuple(
        adjacent_nn_pressure(COUNTEREXAMPLE_64_POINTS, old_epoch=n).ratio
        for n in (8, 16, 32)
    ) == (Fraction(9, 14), Fraction(17, 28), Fraction(45, 118))


def test_certificate_authenticates_exact_audits_and_finite_scope() -> None:
    payload = build_certificate()
    recorded_hash = payload.pop("certificate_sha256")
    assert canonical_hash(payload) == recorded_hash
    assert payload["schema"] == "wave6_hall_candidate_probe_certificate_v1"
    assert payload["conclusion"]["universal_candidate_refuted"] is True
    assert payload["earliest_feasible_level"]["old_epoch"] == 8
    assert payload["earliest_feasible_level"]["ruler_search_complete"] is False
    assert payload["counterexamples"]["marks_16"]["transitions"][0][
        "scaled_value"
    ] == "2592/49"
    assert payload["counterexamples"]["marks_64"]["difference_count"] == 2016
    assert [
        row["scaled_value"]
        for row in payload["counterexamples"]["marks_64"]["transitions"]
    ] == ["2592/49", "4624/49", "259200/3481"]
    comparison = payload["authenticated_fixture_comparison"]
    assert comparison["transition_instance_count"] == 22
    assert comparison["all_candidate_holds"] is True
    assert comparison["parent_certificate_sha256"] == (
        "16a5e07165c767fe714f1044ae4c7c490265428e746653cfe40c385f0e9e671a"
    )
    assert payload["scope"]["asymptotic_claim"] is False
    assert payload["scope"]["beam_search_complete"] is False


def test_serialized_certificate_has_valid_internal_and_source_hashes() -> None:
    path = Path(__file__).with_name(
        "wave6_hall_candidate_probe_certificate_2026-08-28.json"
    )
    payload = json.loads(path.read_text(encoding="utf-8"))
    recorded_hash = payload.pop("certificate_sha256")
    assert canonical_hash(payload) == recorded_hash
    for name, recorded_source_hash in payload["reproducibility"][
        "source_sha256"
    ].items():
        source_bytes = path.with_name(name).read_bytes()
        assert sha256(source_bytes).hexdigest() == recorded_source_hash
