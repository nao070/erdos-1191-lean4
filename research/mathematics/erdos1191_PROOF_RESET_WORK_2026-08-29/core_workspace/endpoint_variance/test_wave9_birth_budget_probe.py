from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from wave9_birth_budget_probe import (
    DEFAULT_SOURCE_CERTIFICATE,
    PERFECT_FOUR,
    audit_fixture,
    bounded_eight_mark_c1_audit,
    build_certificate,
    epoch_birth_budget_audit,
    exhaustive_four_mark_c1_audit,
    fixture_audits,
)

DIRECTORY = Path(__file__).resolve().parent
CERTIFICATE = DIRECTORY / "wave9_birth_budget_certificate_2026-08-29.json"


def test_perfect_four_has_exact_per_epoch_birth_budget() -> None:
    first = epoch_birth_budget_audit(PERFECT_FOUR, old_count=1)
    second = epoch_birth_budget_audit(PERFECT_FOUR, old_count=2)
    whole = audit_fixture("perfect", "test", PERFECT_FOUR)

    assert first.increment == Fraction(1, 35)
    assert second.increment == Fraction(83, 5488)
    assert second.signed_q_charge == Fraction(137, 10976)
    assert second.old_pair_subtraction == Fraction(29, 10976)
    assert whole.cumulative_birth_budget == Fraction(1199, 27440)
    assert whole.pair_partition_count == 6
    assert (
        first.increment == first.genuine_increment + first.artificial_boundary_increment
    )
    assert second.increment == (
        second.genuine_increment + second.artificial_boundary_increment
    )


def test_exact_atom_envelope_and_global_magnitude_capacity_hold_on_all_fixtures() -> (
    None
):
    rows = fixture_audits(str(DEFAULT_SOURCE_CERTIFICATE.resolve()))
    assert len(rows) == 11
    assert tuple(row.audited_mark_count for row in rows[:2]) == (4, 64)
    assert rows[-2].audited_mark_count == 512
    assert rows[-1].supplied_mark_count == 682
    assert rows[-1].audited_mark_count == 512

    for fixture in rows:
        assert fixture.pair_partition_count == (
            fixture.audited_mark_count * (fixture.audited_mark_count - 1) // 2
        )
        assert fixture.maximum_global_cell_occupancy_to_capacity <= 1
        for epoch in fixture.epoch_rows:
            assert epoch.increment == (
                epoch.genuine_increment + epoch.artificial_boundary_increment
            )
            assert epoch.increment == epoch.signed_q_charge + epoch.old_pair_subtraction
            assert epoch.macroscopic_long_rank_increment <= epoch.genuine_increment
            assert 0 <= epoch.macroscopic_long_rank_share <= 1
            assert (
                sum(
                    (band.total_charge for band in epoch.normalized_bands),
                    Fraction(0),
                )
                == epoch.increment
            )
            assert all(
                band.maximum_atom_envelope_ratio <= 1 for band in epoch.normalized_bands
            )


def test_exhaustive_four_mark_scope_and_minimal_cell_counterexample() -> None:
    audit = exhaustive_four_mark_c1_audit()
    assert audit["ruler_count"] == 1_672
    assert audit["strict_epoch_decrease_count"] == 1_672
    assert audit["epoch_1_minimum"] == (Fraction(16, 875), (0, 4, 5, 7))
    assert audit["epoch_1_maximum"] == (Fraction(1, 35), (0, 1, 18, 43))
    assert audit["epoch_2_minimum"] == (Fraction(169, 46_464), (0, 1, 3, 43))
    assert audit["epoch_2_maximum"] == (Fraction(83, 5_488), PERFECT_FOUR)
    one = audit["cell_one_minimum_diameter_witness"]
    rank = audit["cell_rank_lower_minimum_diameter_witness"]
    assert one["points"] == PERFECT_FOUR
    assert rank["points"] == PERFECT_FOUR
    assert one["cell"].rank_band_lower == 2
    assert one["cell"].absolute_magnitude_band_lower == 4
    assert one["cell"].atom_count == 3
    assert rank["cell"].occupancy_to_rank_lower == Fraction(3, 2)


def test_bounded_eight_scope_refutes_monotone_and_literal_harmonic_schedules() -> None:
    audit = bounded_eight_mark_c1_audit()
    assert audit["unrestricted_ruler_count"] == 1_468
    assert audit["c1_ruler_count"] == 1_146
    assert audit["search_node_count"] == 889_645
    assert audit["newest_increment_increase_count"] == 128
    monotone = audit["newest_increment_minimum_diameter_witness"]
    assert monotone["points"] == (0, 4, 12, 13, 19, 30, 33, 35)
    assert monotone["epoch_2_increment"] == Fraction(2_791, 329_280)
    assert monotone["epoch_4_increment"] == Fraction(340_841, 34_836_480)
    assert monotone["margin"] == Fraction(446_533, 341_397_504)

    assert audit["harmonic_schedule_failure_count"] == 1_146
    harmonic = audit["harmonic_schedule_minimum_diameter_witness"]
    assert harmonic["points"] == (0, 1, 4, 9, 15, 22, 32, 34)
    assert harmonic["epoch_2_increment"] == Fraction(143, 11_200)
    assert harmonic["epoch_4_increment"] == Fraction(4_147, 548_800)
    assert harmonic["margin"] == Fraction(1_287, 548_800)


def test_long_fixture_and_erdos_turan_calibrate_large_cell_overlap() -> None:
    rows = {
        row.name: row
        for row in fixture_audits(str(DEFAULT_SOURCE_CERTIFICATE.resolve()))
    }
    long_fixture = rows["wave8_modified_greedy_682_prefix_512"]
    erdos_turan = rows["wave7_erdos_turan_512_p1423"]

    assert long_fixture.points_sha256 == (
        "523c509485873262cf5c51c4ee974a8a9cd5b89b46cec24f9ed59c1f05d57a60"
    )
    assert long_fixture.all_prefix_c1_to_audited_count
    assert long_fixture.maximum_global_cell_occupancy_to_rank_lower == Fraction(553, 4)
    assert erdos_turan.maximum_global_cell_occupancy_to_rank_lower == Fraction(647, 2)
    assert not erdos_turan.all_prefix_c1_to_audited_count
    assert long_fixture.epoch_rows[-1].epoch == 256
    assert long_fixture.epoch_rows[-1].increment == Fraction(
        981_895_646_008_764_061_653,
        106_680_470_919_327_745_310_720,
    )
    assert erdos_turan.epoch_rows[-1].increment == Fraction(
        1_028_804_272_398_780_529_263,
        79_561_917_838_433_441_546_240,
    )
    assert long_fixture.epoch_rows[-1].macroscopic_long_rank_share == Fraction(
        13_242_199_924_089_976_348_090,
        20_619_808_566_184_045_294_713,
    )
    assert erdos_turan.epoch_rows[-1].macroscopic_long_rank_share == Fraction(
        2_738_923_201_748_154_301_783,
        4_115_217_089_595_122_117_052,
    )
    assert long_fixture.epoch_rows[-1].macroscopic_long_rank_share > Fraction(3, 5)
    assert erdos_turan.epoch_rows[-1].macroscopic_long_rank_share > Fraction(3, 5)


def test_certificate_replays_byte_identically_and_keeps_scope_guardrails() -> None:
    expected = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    observed = build_certificate(DEFAULT_SOURCE_CERTIFICATE)
    assert observed == expected
    assert observed["conclusions"]["finite_computation_only"]
    assert not observed["conclusions"]["infinite_survival_inferred"]
    assert not observed["conclusions"]["p15_proved"]
    assert not observed["conclusions"]["erdos_1191_resolved"]
