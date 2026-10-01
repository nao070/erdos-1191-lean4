"""Exact certificate for the Wave 19 ``Gmix`` self-cancellation no-go.

The companion memo observes that the proposed mixed signed functional is
not a smaller remainder.  After subtracting half of the birth energy it is
*exactly* the sum of five established slacks.  The Wave 17 rank surplus also
exceeds the current adaptive cap by more than ``1/40`` from epoch 2048.
Consequently the Fejer mean of ``Gmix`` has a linear lower bound.

All numerical comparisons in this module use :class:`fractions.Fraction`.
The analytic monotonicity steps are recorded with their exact derivative
formulas.  This certificate closes the bare ``Gmix`` upper target as a
standalone route; it does not prove P28 or Erdos Problem #1191.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Mapping, Sequence
from fractions import Fraction
from hashlib import sha256
from math import factorial
from pathlib import Path
from typing import Any

DIRECTORY = Path(__file__).resolve().parent
DEFAULT_OUTPUT = DIRECTORY / "wave19_p28_gmix_no_go_certificate_2026-08-29.json"

TARGET_ONSET = 2048
TARGET_ONSET_EXPONENT = 11
CAP_LIMIT_UPPER = Fraction(8_336_738_101, 10_000_000_000)
CAP_ERROR_UPPER = Fraction(3_009_853, 10_000_000)
UNIFORM_GAP_FLOOR = Fraction(1, 40)
DEFAULT_START_EXPONENT = TARGET_ONSET_EXPONENT

Vector = dict[str, Fraction]


def _require_integer(value: int, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    return value


def _require_nonnegative(value: int, name: str) -> int:
    value = _require_integer(value, name)
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")
    return value


def _fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _canonical_bytes(payload: Mapping[str, Any]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()


def _payload_hash(payload: Mapping[str, Any]) -> str:
    return sha256(_canonical_bytes(payload)).hexdigest()


def render_certificate(payload: Mapping[str, Any]) -> bytes:
    """Render stable, human-readable JSON."""
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()


def log_interval(value: Fraction, terms: int = 24) -> tuple[Fraction, Fraction]:
    """Return rigorous rational lower and upper bounds for ``log(value)``.

    This uses the positive atanh series with
    ``z=(value-1)/(value+1)`` and a geometric upper bound on the tail.
    """
    if value < 1:
        raise ValueError("value must be at least one")
    terms = _require_nonnegative(terms, "terms")
    z_value = (value - 1) / (value + 1)
    lower = 2 * sum(
        (z_value ** (2 * index + 1) / (2 * index + 1) for index in range(terms + 1)),
        Fraction(),
    )
    remainder = (
        2
        * z_value ** (2 * terms + 3)
        / (2 * terms + 3)
        / (1 - z_value * z_value)
    )
    return lower, lower + remainder


def exp_lower(value: Fraction, last_term: int = 14) -> Fraction:
    """Return a strict rational lower bound for ``exp(value)``, value > 0."""
    if value <= 0:
        raise ValueError("value must be positive")
    last_term = _require_nonnegative(last_term, "last_term")
    return sum(
        (value**index / factorial(index) for index in range(last_term + 1)),
        Fraction(),
    )


def _add_vectors(*vectors: Mapping[str, Fraction]) -> Vector:
    result: Vector = {}
    for vector in vectors:
        for key, value in vector.items():
            result[key] = result.get(key, Fraction()) + value
    return {key: value for key, value in sorted(result.items()) if value}


def _vector_text(vector: Mapping[str, Fraction]) -> dict[str, str]:
    return {key: _fraction_text(value) for key, value in sorted(vector.items())}


def gap_identity_audit() -> dict[str, Any]:
    """Verify the exact five-term identity in the formal ledger basis.

    The left vector is the hostile rewrite of ``Gmix-Y/2``.  The right
    vector is the sum of the cross deficit, current rank-cap surplus,
    pairing slack, actual-rank slack ``Qad``, and endpoint deficit.
    """
    left: Vector = {
        "D": Fraction(1),
        "Dpre": Fraction(2, 3),
        "Pair": Fraction(1),
        "Srank": Fraction(1),
        "ThetaCap": Fraction(-1),
        "ThetaExc": Fraction(-1),
        "Y": Fraction(1, 2),
    }
    terms: dict[str, Vector] = {
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
    right = _add_vectors(*terms.values())

    preceding_left = dict(left)
    del preceding_left["ThetaCap"]
    preceding_left["ThetaPrevCap"] = Fraction(-1)
    preceding_terms = dict(terms)
    preceding_terms["current_rank_cap_surplus"] = {
        "D": Fraction(1),
        "ThetaPrevCap": Fraction(-1),
    }
    preceding_right = _add_vectors(*preceding_terms.values())

    return {
        "identity": (
            "Gmix-Y/2=(Y/2-S_t)+(D-ThetaCap)+Pair+Qad+"
            "(2*Dpre/3-E_rank)"
        ),
        "left_coefficient_vector": _vector_text(left),
        "five_terms": {
            name: _vector_text(vector) for name, vector in terms.items()
        },
        "right_coefficient_vector": _vector_text(right),
        "current_index_identity_exact": left == right,
        "pre_reindexed_identity": (
            "GmixPre-Y/2=(Y/2-S_t)+(D-ThetaPrevCap)+Pair+Qad+"
            "(2*Dpre/3-E_rank)"
        ),
        "pre_reindexed_left_coefficient_vector": _vector_text(preceding_left),
        "pre_reindexed_right_coefficient_vector": _vector_text(preceding_right),
        "pre_reindexed_identity_exact": preceding_left == preceding_right,
        "nonnegative_terms_from_existing_theorems": {
            "cross_deficit": "S_t<=Y/2",
            "pairing_slack": "Pair>=0",
            "actual_rank_slack_Qad": "Qad>=0",
            "endpoint_deficit": "E_rank<=2*Dpre/3",
        },
    }


def current_index_cap_audit() -> dict[str, Any]:
    """Certify ``D_n-ThetaCap_n>1/40`` for every ``n>=2048``.

    The exact onset comparison reuses the established rational envelopes.
    The previous-scale envelope has error ``2*a/n``; the current cap has the
    strictly smaller envelope ``a/n``.  No unproved monotonicity of the
    actual deterministic cap profile is used.
    """
    log2_lower, log2_upper = log_interval(Fraction(2))
    log3_lower, log3_upper = log_interval(Fraction(3))
    exp_three_halves_lower = exp_lower(Fraction(3, 2))
    true_cap_limit_upper = Fraction(3, 4) + Fraction(3, 8) / exp_three_halves_lower

    delta0_lower = Fraction(3, 2) + Fraction(3, 4) * log3_lower - 2 * log2_upper
    log_onset_upper = TARGET_ONSET_EXPONENT * log2_upper
    d_onset_lower = delta0_lower - Fraction(18, TARGET_ONSET) * (
        1 + log_onset_upper
    )
    preceding_envelope = CAP_LIMIT_UPPER + 2 * CAP_ERROR_UPPER / TARGET_ONSET
    current_envelope = CAP_LIMIT_UPPER + CAP_ERROR_UPPER / TARGET_ONSET
    preceding_margin = d_onset_lower - preceding_envelope
    current_margin = d_onset_lower - current_envelope

    return {
        "onset": TARGET_ONSET,
        "onset_is_two_to_the_eleven": TARGET_ONSET == 2**TARGET_ONSET_EXPONENT,
        "log_interval_terms": 24,
        "exp_lower_last_term": 14,
        "log2_lower": _fraction_text(log2_lower),
        "log2_upper": _fraction_text(log2_upper),
        "log3_lower": _fraction_text(log3_lower),
        "log3_upper": _fraction_text(log3_upper),
        "true_cap_limit_rational_upper": _fraction_text(true_cap_limit_upper),
        "true_cap_limit_below_declared_upper": true_cap_limit_upper
        < CAP_LIMIT_UPPER,
        "elementary_cap_error_one_quarter_below_declared_error": Fraction(1, 4)
        < CAP_ERROR_UPPER,
        "delta0_rational_lower": _fraction_text(delta0_lower),
        "D_2048_rational_lower": _fraction_text(d_onset_lower),
        "preceding_cap_envelope_b_plus_2a_over_n": _fraction_text(
            preceding_envelope
        ),
        "current_cap_envelope_b_plus_a_over_n": _fraction_text(current_envelope),
        "current_envelope_strictly_smaller": current_envelope
        < preceding_envelope,
        "preceding_envelope_margin": _fraction_text(preceding_margin),
        "current_index_margin": _fraction_text(current_margin),
        "preceding_margin_exceeds_one_fortieth": preceding_margin
        > UNIFORM_GAP_FLOOR,
        "current_margin_exceeds_one_fortieth": current_margin > UNIFORM_GAP_FLOOR,
        "all_larger_epochs_proof": {
            "D_lower": "delta0-18(1+log n)/n",
            "D_lower_derivative": "18 log(n)/n^2>0 for n>1",
            "larger_cap_envelope": "b+2a/n",
            "larger_cap_envelope_derivative": "-2a/n^2<0",
            "current_cap_bound": "ThetaCap_n<=Cdet_n<b+a/n<b+2a/n",
            "conclusion": "D_n-ThetaCap_n>1/40 for every n>=2048",
        },
        "uses_monotonicity_of_actual_Cdet_profile": False,
    }


def fejer_weight(exponent: int, horizon: int) -> Fraction:
    """Return ``((J+1-k)/(J+1))^2``."""
    exponent = _require_nonnegative(exponent, "exponent")
    horizon = _require_nonnegative(horizon, "horizon")
    if exponent > horizon:
        raise ValueError("exponent must not exceed horizon")
    return Fraction((horizon + 1 - exponent) ** 2, (horizon + 1) ** 2)


def fejer_weight_sum(start: int, horizon: int) -> Fraction:
    """Enumerate the finite Fejer weight sum exactly."""
    start = _require_nonnegative(start, "start")
    horizon = _require_nonnegative(horizon, "horizon")
    if start > horizon:
        raise ValueError("start must not exceed horizon")
    return sum(
        (fejer_weight(exponent, horizon) for exponent in range(start, horizon + 1)),
        Fraction(),
    )


def closed_fejer_weight_sum(start: int, horizon: int) -> Fraction:
    """Return the exact sum-of-squares closed formula."""
    start = _require_nonnegative(start, "start")
    horizon = _require_nonnegative(horizon, "horizon")
    if start > horizon:
        raise ValueError("start must not exceed horizon")
    count = horizon + 1 - start
    return Fraction(
        count * (count + 1) * (2 * count + 1), 6 * (horizon + 1) ** 2
    )


def explicit_linear_weight_lower_holds(start: int, horizon: int) -> bool:
    """Check the convenient bound ``sum omega >= J/24``.

    It is used only when ``J+1>=2*start``.  Then the number of retained
    square weights is at least ``(J+1)/2``, and the sum-of-squares formula
    gives the displayed bound.
    """
    start = _require_nonnegative(start, "start")
    horizon = _require_nonnegative(horizon, "horizon")
    if start > horizon:
        raise ValueError("start must not exceed horizon")
    if horizon + 1 < 2 * start:
        raise ValueError("explicit linear bound requires horizon+1>=2*start")
    return closed_fejer_weight_sum(start, horizon) >= Fraction(horizon, 24)


def fejer_audit() -> dict[str, Any]:
    """Audit the exact Fejer sum and the resulting linear ``Gmix`` floor."""
    start = DEFAULT_START_EXPONENT
    horizons = (11, 12, 16, 21, 22, 32, 64, 128)
    exact_checks = []
    for horizon in horizons:
        enumerated = fejer_weight_sum(start, horizon)
        closed = closed_fejer_weight_sum(start, horizon)
        exact_checks.append(
            {
                "horizon": horizon,
                "enumerated": _fraction_text(enumerated),
                "closed": _fraction_text(closed),
                "equal": enumerated == closed,
            }
        )
    linear_horizons = tuple(horizon for horizon in horizons if horizon + 1 >= 2 * start)
    return {
        "start_exponent": start,
        "first_epoch": 2**start,
        "closed_formula": (
            "M(M+1)(2M+1)/(6(J+1)^2), where M=J+1-k0"
        ),
        "exact_checks": exact_checks,
        "all_exact_checks_pass": all(row["equal"] for row in exact_checks),
        "asymptotic_expansion": "sum omega=J/3+O_k0(1)",
        "gmix_asymptotic_floor_from_one_fortieth": (
            "sum omega Gmix>=J/120+O_k0(1)"
        ),
        "explicit_finite_bound": (
            "if J+1>=2*k0, sum omega>=J/24 and sum omega Gmix>=J/960"
        ),
        "explicit_linear_bound_horizons": list(linear_horizons),
        "explicit_linear_bounds_pass": all(
            explicit_linear_weight_lower_holds(start, horizon)
            for horizon in linear_horizons
        ),
    }


def no_go_audit() -> dict[str, Any]:
    """Record the exact implication and its deliberately narrow scope."""
    identity = gap_identity_audit()
    cap = current_index_cap_audit()
    fejer = fejer_audit()
    theorem_inputs_pass = (
        identity["current_index_identity_exact"]
        and cap["current_margin_exceeds_one_fortieth"]
        and fejer["all_exact_checks_pass"]
        and fejer["explicit_linear_bounds_pass"]
    )
    return {
        "theorem_inputs_pass": theorem_inputs_pass,
        "pointwise_theorem": "Gmix_n>=Y_n/2+1/40 for every n>=2048",
        "weighted_theorem": (
            "sum_(k=k0)^J omega_(k,J)Gmix_(2^k)>=J/120+O_k0(1)"
        ),
        "normalized_limit": "+infinity",
        "positive_part_has_same_eventual_lower": True,
        "strict_1_over_3072_C_log2_target_possible_on_an_extant_branch": False,
        "positive_part_o_logJ_target_possible_on_an_extant_branch": False,
        "interpretation": (
            "The bare Gmix target is saturated by an exact self-cancellation "
            "identity. This is a no-go for that intermediate functional, not "
            "a proof or refutation of P28 or either Erdos question."
        ),
        "ownership_legal": True,
        "ownership_reason": (
            "The proof only rewrites the already-defined Gmix and lower-bounds "
            "its numerical value. It neither reallocates v, reuses a dropped "
            "bracket as a new payment, nor spends any atom twice."
        ),
        "mandatory_next_ledger_change": (
            "Retain (D-ThetaPrevCap)+Qad+Pair before cap reindexing, keep "
            "S_t and E_rank uncollapsed, and introduce a separately owned "
            "negative cross-scale carrier for the residual Y-S_t."
        ),
    }


def build_certificate() -> dict[str, Any]:
    """Build the complete deterministic certificate payload."""
    identity = gap_identity_audit()
    cap = current_index_cap_audit()
    fejer = fejer_audit()
    no_go = no_go_audit()
    payload: dict[str, Any] = {
        "schema": "erdos1191.wave19.p28-gmix-self-cancellation-no-go.v1",
        "research_date": "2026-08-29",
        "purpose": (
            "Certify the exact five-term Gmix gap identity, the current-index "
            "rank-cap floor, and the resulting linear Fejer lower bound."
        ),
        "arithmetic": "all finite proof comparisons use fractions.Fraction",
        "gap_identity": identity,
        "current_index_cap_audit": cap,
        "fejer_audit": fejer,
        "no_go_theorem": no_go,
        "audit_counts": {
            "pytest_tests": 9,
            "formal_ledger_basis_coefficients": len(
                identity["left_coefficient_vector"]
            ),
            "formal_gap_terms": len(identity["five_terms"]),
            "fejer_exact_horizons": len(fejer["exact_checks"]),
            "rational_onset_comparisons": 2,
        },
        "scope_flags": {
            "five_term_identity_proved": True,
            "current_D_minus_ThetaCap_above_one_fortieth_from_2048": True,
            "gmix_fejer_mean_has_linear_lower_bound": True,
            "bare_gmix_strict_threshold_target_viable": False,
            "bare_gmix_positive_part_little_o_target_viable": False,
            "mixed_transport_theorem_remains_valid": True,
            "p28_proved": False,
            "p28_refuted": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "erdos_1191_resolved": False,
            "problem_unresolved": True,
            "prize_claim_ready": False,
        },
    }
    payload["certificate_sha256"] = _payload_hash(payload)
    return payload


def verify_certificate_hash(payload: Mapping[str, Any]) -> bool:
    """Verify the embedded hash after removing the hash field."""
    if "certificate_sha256" not in payload:
        return False
    unsigned = dict(payload)
    expected = unsigned.pop("certificate_sha256")
    return expected == _payload_hash(unsigned)


def write_certificate(path: Path = DEFAULT_OUTPUT) -> Path:
    """Write the deterministic JSON certificate."""
    path.write_bytes(render_certificate(build_certificate()))
    return path


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="write the canonical certificate to stdout instead of a file",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    rendered = render_certificate(build_certificate())
    if args.stdout:
        import sys

        sys.stdout.buffer.write(rendered)
    else:
        args.output.write_bytes(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
