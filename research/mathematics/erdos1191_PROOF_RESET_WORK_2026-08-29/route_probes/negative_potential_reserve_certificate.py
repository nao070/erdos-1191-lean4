#!/usr/bin/env python3
"""Exact replay for the isolated negative-potential reserve no-go.

The companion memo proves the quantified identities.  This program certifies
one eight-mark Golomb fixture at a single scale, one complete logarithmic
phase, three integrated rational separations, and the affine-difference
structure of an asymptotic Golomb family.

Only the isolated nonnegative reserve interpretation is rejected.  Exact
signed use of the negative rows, the ordered Gram coupling, cross-epoch
payment, and larger masters remain open.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
from typing import Mapping, Sequence


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "negative_potential_reserve_certificate.json"
SCHEMA = "erdos1191.negative_potential_reserve.v1"
FIXTURE = (0, 2, 5, 16, 22, 23, 31, 35)
POSITIVE_OWNERS = ((F(1, 16), 1), (F(1, 16), 8), (F(1, 64), 9))
NEGATIVE_ROWS = ((F(1, 16), 7), (F(5, 64), 15), (F(1, 16), 12), (F(5, 64), 13))


class CertificateError(RuntimeError):
    """Raised when an exact replay or scope guard fails."""


def ftext(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def positive_differences(points: Sequence[int]) -> tuple[int, ...]:
    values = tuple(
        points[right] - points[left]
        for left in range(len(points))
        for right in range(left + 1, len(points))
    )
    if len(values) != len(set(values)):
        raise CertificateError("fixture is not a Golomb ruler")
    return tuple(sorted(values))


def log_bounds(ratio: F) -> tuple[F, F]:
    if ratio <= 1:
        raise ValueError("log ratio must exceed one")
    z = (ratio - 1) / (ratio + 1)
    lower = 2 * z
    upper = 2 * (z + z**3 / (3 * (1 - z * z)))
    return lower, upper


def ramp(width: F, distance: int) -> F:
    if width <= distance:
        return F(0)
    return (width - distance) / (width * width)


def density_components(width: F) -> tuple[F, F, F]:
    positive = sum((beta * ramp(width, distance) for beta, distance in POSITIVE_OWNERS), F(0))
    negative = sum((weight * ramp(width, distance) for weight, distance in NEGATIVE_ROWS), F(0))
    wave = positive - negative
    if wave < 0:
        raise CertificateError("Wave density became negative")
    return positive, negative, wave


def reserve_fixture() -> dict[str, object]:
    differences = positive_differences(FIXTURE)
    expected = (
        1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15,
        16, 17, 18, 19, 20, 21, 22, 23, 26, 29, 30, 31, 33, 35,
    )
    if differences != expected:
        raise CertificateError("fixture difference list changed")

    horizon = 19
    rational_part = sum(
        (weight * (F(distance, horizon) - 1) for weight, distance in NEGATIVE_ROWS),
        F(0),
    )
    reserve_lower = sum(
        (
            weight * (log_bounds(F(horizon, distance))[0] + F(distance, horizon) - 1)
            for weight, distance in NEGATIVE_ROWS
        ),
        F(0),
    )
    reserve_upper = sum(
        (
            weight * (log_bounds(F(horizon, distance))[1] + F(distance, horizon) - 1)
            for weight, distance in NEGATIVE_ROWS
        ),
        F(0),
    )
    if rational_part != F(-63, 608):
        raise CertificateError("reserve rational part changed")
    if reserve_upper != F(75853397, 2099365632):
        raise CertificateError("reserve upper bound changed")
    return {
        "points": list(FIXTURE),
        "positive_differences": list(differences),
        "difference_count": len(differences),
        "current_gaps": [6, 1, 8, 4],
        "horizon": horizon,
        "positive_owner_rows": [
            {"beta": ftext(beta), "distance": distance} for beta, distance in POSITIVE_OWNERS
        ],
        "negative_lambda_rows": [
            {"absolute_lambda": ftext(weight), "distance": distance}
            for weight, distance in NEGATIVE_ROWS
        ],
        "reserve_exact_expression": "(1/16)log(19/7)+(5/64)log(19/15)+(1/16)log(19/12)+(5/64)log(19/13)-63/608",
        "reserve_atanh_lower": ftext(reserve_lower),
        "reserve_atanh_upper": ftext(reserve_upper),
        "unused_equals_negative_potential": True,
    }


def pointwise_fixture() -> dict[str, object]:
    width = F(2)
    positive, negative, wave = density_components(width)
    g_left = 2 * min(F(6), width) / (width * width)
    g_right = 2 * min(F(8), width) / (width * width)
    psd_price = F(1, 16) * g_left  # g_left=g_right=1 on this fixture
    marginal_price = F(1, 32)
    owner_capacity = width * F(1, 16) * ramp(width, 1)
    owner_state = 2 * ramp(width, 1)
    owner_coefficient = owner_capacity / owner_state
    full_signless_price = 2 * owner_coefficient / width
    if (positive, negative, wave) != (F(1, 64), F(0), F(1, 64)):
        raise CertificateError("pointwise density fixture changed")
    if (g_left, g_right, psd_price) != (F(1), F(1), F(1, 16)):
        raise CertificateError("pointwise PSD price changed")
    if owner_coefficient != F(1, 16) or full_signless_price != F(1, 16):
        raise CertificateError("pointwise owner price changed")
    return {
        "width": ftext(width),
        "positive_density": ftext(positive),
        "negative_density": ftext(negative),
        "wave_density": ftext(wave),
        "g_left": ftext(g_left),
        "g_right": ftext(g_right),
        "coefficient_psd_price": ftext(psd_price),
        "ordered_marginal_price": ftext(marginal_price),
        "owner_capacity_x": ftext(owner_capacity),
        "owner_state_v": ftext(owner_state),
        "owner_coefficient_a": ftext(owner_coefficient),
        "full_signless_price_attributable_to_scale": ftext(full_signless_price),
        "unused_scale_capacity": ftext(width * negative),
        "zero_reserve_positive_prices_verified": True,
    }


def phase_fixture() -> dict[str, object]:
    widths = (F(5, 4), F(5, 2), F(5), F(10))
    cumulative = [F(0), F(0), F(0)]
    scale_rows = []
    phase_reserve = F(0)
    pair_price = F(0)
    for width in widths:
        positive, negative, wave = density_components(width)
        quotient = wave / positive if positive else F(0)
        allocations = []
        for index, (beta, distance) in enumerate(POSITIVE_OWNERS):
            value = width * beta * quotient / 2 if width > distance else F(0)
            cumulative[index] += value
            allocations.append(value)
        phase_reserve += width * negative
        pair_price += 2 * sum(allocations, F(0)) / width
        scale_rows.append(
            {
                "width": ftext(width),
                "q_over_positive": ftext(quotient),
                "unused_capacity": ftext(width * negative),
                "owner_coefficients_a": [ftext(value) for value in allocations],
            }
        )
    terminal_width = F(10)
    terminal_diagonal = sum(cumulative, F(0)) / terminal_width
    terminal_off_diagonal = sum(
        (
            cumulative[index] * 2 * ramp(2 * terminal_width, distance)
            for index, (_, distance) in enumerate(POSITIVE_OWNERS)
        ),
        F(0),
    )
    expected_cumulative = (F(193, 384), F(11, 48), F(11, 192))
    if tuple(cumulative) != expected_cumulative:
        raise CertificateError("phase cumulative coefficients changed")
    expected = (F(3, 160), F(93, 320), F(101, 1280), F(331, 5120))
    if (phase_reserve, pair_price, terminal_diagonal, terminal_off_diagonal) != expected:
        raise CertificateError("phase prices changed")
    return {
        "last_width": ftext(terminal_width),
        "next_width": ftext(2 * terminal_width),
        "scale_rows": scale_rows,
        "cumulative_owner_coefficients": [ftext(value) for value in cumulative],
        "phase_unused_reserve": ftext(phase_reserve),
        "pair_signless_total_price": ftext(pair_price),
        "terminal_diagonal_price": ftext(terminal_diagonal),
        "terminal_off_diagonal_row": ftext(terminal_off_diagonal),
        "pair_price_over_reserve": ftext(pair_price / phase_reserve),
        "terminal_diagonal_over_reserve": ftext(terminal_diagonal / phase_reserve),
        "terminal_off_diagonal_over_reserve": ftext(terminal_off_diagonal / phase_reserve),
    }


def q_piecewise_rows() -> tuple[dict[str, object], ...]:
    breakpoints = (1, 7, 8, 9, 12, 13, 15, 19)
    rows = []
    for left, right in zip(breakpoints, breakpoints[1:]):
        midpoint = F(left + right, 2)
        active_positive = tuple((weight, distance) for weight, distance in POSITIVE_OWNERS if midpoint > distance)
        active_negative = tuple((weight, distance) for weight, distance in NEGATIVE_ROWS if midpoint > distance)
        denominator_slope = sum((weight for weight, _ in active_positive), F(0))
        denominator_constant = -sum((weight * distance for weight, distance in active_positive), F(0))
        negative_slope = sum((weight for weight, _ in active_negative), F(0))
        negative_constant = -sum((weight * distance for weight, distance in active_negative), F(0))
        numerator_slope = denominator_slope - negative_slope
        numerator_constant = denominator_constant - negative_constant
        derivative_numerator = (
            numerator_slope * denominator_constant
            - numerator_constant * denominator_slope
        )
        if derivative_numerator > 0:
            raise CertificateError("Q/P+ is not nonincreasing")
        rows.append(
            {
                "interval": [left, right],
                "numerator_slope": ftext(numerator_slope),
                "numerator_constant": ftext(numerator_constant),
                "denominator_slope": ftext(denominator_slope),
                "denominator_constant": ftext(denominator_constant),
                "derivative_numerator": ftext(derivative_numerator),
            }
        )
    return tuple(rows)


def terminal_off_lower_segments() -> tuple[dict[str, object], ...]:
    points = (F(19, 2),) + tuple(F(value) for value in range(10, 20))
    rows = []
    total = F(0)
    for left, right in zip(points, points[1:]):
        segment = F(0)
        for exponent in range(6):
            scale = 2**exponent
            midpoint = (left + right) / (2 * scale)
            owners = tuple((beta, distance) for beta, distance in POSITIVE_OWNERS if midpoint > distance)
            if not owners:
                continue
            positive, _, wave = density_components(right / scale)
            quotient_lower = wave / positive if positive else F(0)
            if quotient_lower <= 0:
                continue
            log_lower = log_bounds(right / left)[0]
            for beta, distance in owners:
                segment += beta * quotient_lower / (4 * scale) * (
                    2 * log_lower + distance * (F(1, right) - F(1, left))
                )
        if segment <= 0:
            raise CertificateError("terminal lower segment is not positive")
        total += segment
        rows.append(
            {
                "last_width_interval": [ftext(left), ftext(right)],
                "rational_lower_contribution": ftext(segment),
            }
        )
    expected = F(48804306505243169, 1330823143467417600)
    if total != expected:
        raise CertificateError("terminal integrated lower bound changed")
    return tuple(rows)


def integrated_witnesses() -> dict[str, object]:
    reserve_upper = F(reserve_fixture()["reserve_atanh_upper"])
    psd_lower = F(2, 13)
    pair_lower = F(3, 32)
    terminal_rows = terminal_off_lower_segments()
    terminal_lower = sum((F(row["rational_lower_contribution"]) for row in terminal_rows), F(0))
    psd_gap = psd_lower - reserve_upper
    pair_gap = pair_lower - reserve_upper
    terminal_gap = terminal_lower - reserve_upper
    if min(psd_gap, pair_gap, terminal_gap) <= 0:
        raise CertificateError("an integrated reserve separation closed")
    return {
        "reserve_upper": ftext(reserve_upper),
        "coefficient_psd_lower": ftext(psd_lower),
        "coefficient_psd_lower_minus_reserve_upper": ftext(psd_gap),
        "pair_signless_lower": ftext(pair_lower),
        "pair_signless_lower_minus_reserve_upper": ftext(pair_gap),
        "terminal_off_diagonal_lower_segments": list(terminal_rows),
        "terminal_off_diagonal_lower": ftext(terminal_lower),
        "terminal_off_diagonal_lower_minus_reserve_upper": ftext(terminal_gap),
        "terminal_diagonal_is_termwise_larger": True,
    }


def asymptotic_family() -> dict[str, object]:
    affine_points = ((0, 0), (0, 2), (0, 5), (0, 16), (1, 16), (1, 17), (1, 25), (3, 25))
    groups: dict[int, set[int]] = {}
    count = 0
    for left in range(len(affine_points)):
        for right in range(left + 1, len(affine_points)):
            slope = affine_points[right][0] - affine_points[left][0]
            constant = affine_points[right][1] - affine_points[left][1]
            constants = groups.setdefault(slope, set())
            if constant in constants:
                raise CertificateError("affine difference collision")
            constants.add(constant)
            count += 1
    expected_groups = {
        0: {1, 2, 3, 5, 8, 9, 11, 14, 16},
        1: {0, 1, 9, 11, 12, 14, 15, 16, 17, 20, 23, 25},
        2: {0, 8, 9},
        3: {9, 20, 23, 25},
    }
    if groups != expected_groups or count != 28:
        raise CertificateError("asymptotic difference groups changed")
    onset = 26
    separation_margins = []
    for slope in range(3):
        current_max = slope * onset + max(groups[slope])
        next_min = (slope + 1) * onset + min(groups[slope + 1])
        margin = next_min - current_max
        if margin <= 0:
            raise CertificateError("affine groups do not separate at onset")
        separation_margins.append(margin)
    return {
        "parameter_domain": "integer L>=26",
        "points": ["0", "2", "5", "16", "L+16", "L+17", "L+25", "3L+25"],
        "current_gaps": ["L", "1", "8", "2L"],
        "horizon": "3L+9",
        "difference_constants_by_slope": {
            str(slope): sorted(constants) for slope, constants in sorted(groups.items())
        },
        "separation_margins_at_L_26": separation_margins,
        "golomb_for_every_integer_L_at_least_26": True,
        "reserve_limit": "(9/64)*(log(9/2)-1)",
        "pair_price_lower": "(9/64)*log((L+1)/9)",
        "marginal_price_lower": "(9/64)*log(L/9)",
        "marginal_transport_witness": "for 9<T<L, edge (4,7) is active, mu_4=nu_7=1/T, and y_47=1/T is dual feasible",
        "long_edge_cross_ratio": "((L+9)*(2L+9))/(9*(3L+9))",
        "coefficient_psd_lower": "(9/32)*log(((L+9)*(2L+9))/(9*(3L+9)))",
        "reserve_over_pair_price_tends_to_zero": True,
        "reserve_over_marginal_price_tends_to_zero": True,
        "reserve_over_coefficient_psd_price_tends_to_zero": True,
    }


def payload_hash(certificate: Mapping[str, object]) -> str:
    payload = {key: value for key, value in certificate.items() if key != "integrity"}
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def rendered_bytes(certificate: Mapping[str, object]) -> bytes:
    return (json.dumps(certificate, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def build_certificate() -> dict[str, object]:
    certificate: dict[str, object] = {
        "schema": SCHEMA,
        "purpose": "Certify that the isolated unused negative-potential reserve does not universally pay the active PSD price, marginal-only price, pair-lift price, or finite terminal.",
        "theorem_contract": {
            "reserve_identity": "U_n=G_n-W_n=sum_(lambda<0)(-lambda)F_H(D)=int_0^H N_n(T)dT",
            "phase_identity": "(log 2) int_0^1 sum_r T_r*N_n(T_r) dtheta=U_n",
            "fixture_obstruction": "the displayed n=4 Golomb ruler fails scale, phase, and integrated isolated-reserve payment",
            "asymptotic_obstruction": "on A_L, U_L stays bounded while the PSD, marginal-only, and pair-lift prices diverge",
        },
        "reserve_fixture": reserve_fixture(),
        "pointwise_fixture": pointwise_fixture(),
        "phase_fixture": phase_fixture(),
        "q_monotonicity_rows": list(q_piecewise_rows()),
        "integrated_witnesses": integrated_witnesses(),
        "asymptotic_family": asymptotic_family(),
        "scope": {
            "isolated_nonnegative_negative_potential_reserve_universally_pays_all_prices": False,
            "isolated_reserve_pays_any_positive_pointwise_share_of_psd_marginal_or_pair_price": False,
            "constant_fraction_of_integrated_psd_price_proved": False,
            "constant_fraction_of_integrated_pair_price_proved": False,
            "constant_fraction_of_integrated_marginal_price_proved": False,
            "exact_signed_negative_rows_ruled_out": False,
            "ordered_gram_intersection_route_ruled_out": False,
            "cross_epoch_payment_ruled_out": False,
            "larger_master_ruled_out": False,
            "c058_resolved": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "complete_proof": False,
            "prize_claim_ready": False,
        },
    }
    certificate["integrity"] = {"payload_sha256": payload_hash(certificate)}
    return certificate


def validate_certificate(certificate: Mapping[str, object]) -> None:
    if certificate.get("schema") != SCHEMA:
        raise CertificateError("schema mismatch")
    integrity = certificate.get("integrity")
    if not isinstance(integrity, Mapping) or integrity.get("payload_sha256") != payload_hash(certificate):
        raise CertificateError("payload hash mismatch")
    if certificate != build_certificate():
        raise CertificateError("semantic replay mismatch")


def rehash(certificate: dict[str, object]) -> None:
    certificate["integrity"] = {"payload_sha256": payload_hash(certificate)}


def self_check(certificate: Mapping[str, object]) -> int:
    validate_certificate(certificate)
    mutations = []

    changed = copy.deepcopy(certificate)
    changed["pointwise_fixture"]["negative_density"] = "1/1"
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["pointwise_fixture"]["coefficient_psd_price"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["phase_fixture"]["phase_unused_reserve"] = "1/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["phase_fixture"]["pair_signless_total_price"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["phase_fixture"]["terminal_off_diagonal_row"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["integrated_witnesses"]["reserve_upper"] = "1/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["integrated_witnesses"]["terminal_off_diagonal_lower"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["asymptotic_family"]["difference_constants_by_slope"]["1"][0] = 1
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["scope"]["exact_signed_negative_rows_ruled_out"] = True
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["scope"]["ordered_gram_intersection_route_ruled_out"] = True
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["scope"]["c058_resolved"] = True
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["scope"]["prize_claim_ready"] = True
    rehash(changed)
    mutations.append(changed)

    rejected = 0
    for mutation in mutations:
        try:
            validate_certificate(mutation)
        except CertificateError:
            rejected += 1
    if rejected != len(mutations):
        raise CertificateError("a semantic mutation was not rejected")
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit", action="store_true", help="print canonical certificate JSON")
    parser.add_argument("--verify", type=Path, help="verify an existing certificate")
    parser.add_argument("--self-check", action="store_true", help="run semantic mutation checks")
    args = parser.parse_args()
    if args.verify:
        certificate = json.loads(args.verify.read_text(encoding="utf-8"))
        validate_certificate(certificate)
    else:
        certificate = build_certificate()
    if args.self_check:
        self_check(certificate)
    if args.emit or not args.verify:
        print(rendered_bytes(certificate).decode("utf-8"), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
