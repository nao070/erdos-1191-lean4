"""Independent exact tests for the Wave 19 ``Gmix`` no-go certificate."""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import pairwise

import pytest

import wave19_p28_gmix_no_go_certificate as certificate


def _as_fractions(vector: dict[str, str]) -> dict[str, Fraction]:
    return {key: Fraction(value) for key, value in vector.items()}


def _sum_vectors(*vectors: dict[str, Fraction]) -> dict[str, Fraction]:
    result: dict[str, Fraction] = {}
    for vector in vectors:
        for key, value in vector.items():
            result[key] = result.get(key, Fraction()) + value
    return {key: value for key, value in result.items() if value}


def test_exact_gap_identity_has_the_hand_derived_literal_vector() -> None:
    audit = certificate.gap_identity_audit()
    expected = {
        "D": Fraction(1),
        "Dpre": Fraction(2, 3),
        "Pair": Fraction(1),
        "Srank": Fraction(1),
        "ThetaCap": Fraction(-1),
        "ThetaExc": Fraction(-1),
        "Y": Fraction(1, 2),
    }
    terms = [_as_fractions(vector) for vector in audit["five_terms"].values()]

    assert _as_fractions(audit["left_coefficient_vector"]) == expected
    assert _sum_vectors(*terms) == expected
    assert audit["current_index_identity_exact"] is True
    expected_pre = dict(expected)
    expected_pre["ThetaPrevCap"] = expected_pre.pop("ThetaCap")
    assert _as_fractions(audit["pre_reindexed_left_coefficient_vector"]) == expected_pre
    assert audit["pre_reindexed_identity_exact"] is True


def test_five_slack_terms_catch_endpoint_or_cap_sign_mutations() -> None:
    audit = certificate.gap_identity_audit()
    terms = {
        name: _as_fractions(vector) for name, vector in audit["five_terms"].items()
    }
    assert terms == {
        "cross_deficit": {"S_t": Fraction(-1), "Y": Fraction(1, 2)},
        "current_rank_cap_surplus": {
            "D": Fraction(1),
            "ThetaCap": Fraction(-1),
        },
        "pairing_slack": {"Pair": Fraction(1)},
        "actual_rank_slack_Qad": {
            "E_rank": Fraction(1),
            "S_t": Fraction(1),
            "Srank": Fraction(1),
            "ThetaExc": Fraction(-1),
        },
        "endpoint_deficit": {
            "Dpre": Fraction(2, 3),
            "E_rank": Fraction(-1),
        },
    }

    expected = _as_fractions(audit["left_coefficient_vector"])
    wrong_endpoint = {name: dict(vector) for name, vector in terms.items()}
    wrong_endpoint["endpoint_deficit"]["Dpre"] = Fraction(3, 4)
    wrong_cap = {name: dict(vector) for name, vector in terms.items()}
    wrong_cap["current_rank_cap_surplus"]["ThetaCap"] = Fraction(1)
    assert _sum_vectors(*wrong_endpoint.values()) != expected
    assert _sum_vectors(*wrong_cap.values()) != expected


def test_dyadic_current_gap_is_strictly_increasing_from_2048() -> None:
    gaps = [
        certificate.dyadic_current_gap_lower(exponent) for exponent in range(11, 18)
    ]

    assert certificate.dyadic_current_gap_lower(10) < Fraction(1, 40)
    assert gaps[0] > Fraction(1, 40)
    assert all(left < right for left, right in pairwise(gaps))


def test_independent_coarse_onset_envelope_clears_one_fortieth() -> None:
    # These decimal rationals are deliberately coarser than the certificate's
    # atanh bounds and were chosen independently:
    # log(2)<0.693147181 and log(3)>1.098612288.
    log2_upper = Fraction(693_147_181, 10**9)
    log3_lower = Fraction(1_098_612_288, 10**9)
    _, certified_log2_upper = certificate.log_interval(Fraction(2))
    certified_log3_lower, _ = certificate.log_interval(Fraction(3))
    assert certified_log2_upper < log2_upper
    assert certified_log3_lower > log3_lower

    delta_lower = Fraction(3, 2) + Fraction(3, 4) * log3_lower - 2 * log2_upper
    d_lower = delta_lower - Fraction(18, 2048) * (1 + 11 * log2_upper)
    cap_limit = Fraction(8_336_738_101, 10**10)
    cap_error = Fraction(3_009_853, 10**7)
    current_margin = d_lower - (cap_limit + cap_error / 2048)
    preceding_margin = d_lower - (cap_limit + 2 * cap_error / 2048)

    assert current_margin == Fraction(143_573_826_923, 5_120_000_000_000)
    assert preceding_margin == Fraction(142_821_363_673, 5_120_000_000_000)
    assert preceding_margin > Fraction(1, 40)

    audit = certificate.current_index_cap_audit()
    assert Fraction(audit["current_index_margin"]) > current_margin
    assert Fraction(audit["preceding_envelope_margin"]) > preceding_margin


@pytest.mark.parametrize(
    ("start", "horizon", "expected"),
    [
        (11, 11, Fraction(1, 144)),
        (11, 21, Fraction(253, 242)),
        (11, 22, Fraction(650, 529)),
        (3, 7, Fraction(55, 64)),
    ],
)
def test_fejer_closed_formula_matches_hand_checked_literals(
    start: int, horizon: int, expected: Fraction
) -> None:
    assert certificate.fejer_weight_sum(start, horizon) == expected
    assert certificate.closed_fejer_weight_sum(start, horizon) == expected


def test_weighted_gmix_floor_is_exact_and_eventually_linear() -> None:
    exact = certificate.weighted_gmix_floor(11, 22)

    assert exact == Fraction(65, 2116)
    assert exact >= Fraction(22, 960)
    for horizon in (21, 22, 32, 64, 128):
        assert certificate.weighted_gmix_floor(11, horizon) >= Fraction(horizon, 960)


def test_invalid_integer_domains_reject_bool_negative_and_bad_ranges() -> None:
    with pytest.raises(TypeError):
        certificate.fejer_weight(True, 11)
    with pytest.raises(ValueError):
        certificate.dyadic_current_gap_lower(-1)
    with pytest.raises(ValueError):
        certificate.fejer_weight_sum(12, 11)
    with pytest.raises(ValueError):
        certificate.exp_lower(Fraction(0))


def test_payload_hash_and_byte_replay_are_deterministic(tmp_path) -> None:
    first = certificate.build_certificate()
    second = certificate.build_certificate()
    output = tmp_path / "gmix.json"

    certificate.write_certificate(output)
    assert first == second == json.loads(output.read_text())
    assert certificate.render_certificate(first) == output.read_bytes()
    assert certificate.verify_certificate_hash(first) is True


def test_no_go_scope_is_narrow_and_keeps_erdos_1191_open() -> None:
    payload = certificate.build_certificate()
    theorem = payload["no_go_theorem"]
    scope = payload["scope_flags"]

    assert theorem["theorem_inputs_pass"] is True
    assert theorem["ownership_legal"] is True
    assert theorem["normalized_limit"] == "+infinity"
    assert (
        theorem["strict_1_over_3072_C_log2_target_possible_on_an_extant_branch"]
        is False
    )
    assert scope["bare_gmix_strict_threshold_target_viable"] is False
    assert scope["p28_proved"] is False
    assert scope["p28_refuted"] is False
    assert scope["question_1_resolved"] is False
    assert scope["question_2_resolved"] is False
    assert scope["erdos_1191_resolved"] is False
    assert scope["prize_claim_ready"] is False
