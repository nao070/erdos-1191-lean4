#!/usr/bin/env python3
"""Exact certificate for the scoped ramp/common-master insertion no-go.

The companion memo proves the universal statements.  This replay locks the
formal three-channel non-span, the zero-mass fourth-channel Schur price, the
small-scale divergence, and an affine Golomb family on which even the
optimally shifted active ramp baseline has a larger logarithmic coefficient
than the complete positive same-epoch Gothic sector.

This is not a no-go for the exact ordered-root dual matrix B, a genuinely
signed whole-cut rewrite, a membership-sensitive master, or Erdős #1191.
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
DEFAULT_CERTIFICATE = HERE / "ramp_common_master_no_go_certificate.json"
SCHEMA = "erdos1191.ramp_common_master_no_go.v1"
L0 = 2**18


class CertificateError(RuntimeError):
    """Raised when an exact replay or scope check fails."""


def ftext(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def determinant(matrix: Sequence[Sequence[F]]) -> F:
    size = len(matrix)
    if size == 0:
        return F(1)
    if any(len(row) != size for row in matrix):
        raise ValueError("matrix must be square")
    work = [list(row) for row in matrix]
    sign = 1
    result = F(1)
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        if pivot is None:
            return F(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign *= -1
        value = work[column][column]
        result *= value
        for row in range(column + 1, size):
            factor = work[row][column] / value
            for entry in range(column, size):
                work[row][entry] -= factor * work[column][entry]
    return sign * result


def solve(matrix: Sequence[Sequence[F]], rhs: Sequence[F]) -> tuple[F, ...]:
    size = len(matrix)
    if len(rhs) != size or any(len(row) != size for row in matrix):
        raise ValueError("solve dimension mismatch")
    work = [list(matrix[row]) + [rhs[row]] for row in range(size)]
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        if pivot is None:
            raise CertificateError("singular exact system")
        work[column], work[pivot] = work[pivot], work[column]
        value = work[column][column]
        work[column] = [entry / value for entry in work[column]]
        for row in range(size):
            if row == column:
                continue
            factor = work[row][column]
            work[row] = [
                work[row][entry] - factor * work[column][entry]
                for entry in range(size + 1)
            ]
    return tuple(work[row][-1] for row in range(size))


def dot(left: Sequence[F], right: Sequence[F]) -> F:
    return sum((a * b for a, b in zip(left, right, strict=True)), F(0))


def affine_points() -> tuple[tuple[int, int], ...]:
    """Return a_k = slope*L + intercept for the A_L family."""
    return (
        (0, 0),
        (0, 2),
        (0, 5),
        (0, 16),
        (1, 16),
        (1, 17),
        (1, 25),
        (3, 25),
    )


def affine_golomb_fixture() -> dict[str, object]:
    points = affine_points()
    differences: list[tuple[int, int, int, int]] = []
    for left in range(len(points)):
        for right in range(left + 1, len(points)):
            slope = points[right][0] - points[left][0]
            intercept = points[right][1] - points[left][1]
            differences.append((slope, intercept, left, right))
    if len(differences) != 28:
        raise CertificateError("affine difference count changed")

    positive_collision_roots: set[F] = set()
    for first in range(len(differences)):
        slope_a, intercept_a, _, _ = differences[first]
        for second in range(first + 1, len(differences)):
            slope_b, intercept_b, _, _ = differences[second]
            if slope_a == slope_b:
                if intercept_a == intercept_b:
                    raise CertificateError("two affine differences agree identically")
                continue
            root = F(intercept_b - intercept_a, slope_a - slope_b)
            if root > 0:
                positive_collision_roots.add(root)
    largest = max(positive_collision_roots)
    if largest != 25:
        raise CertificateError("largest positive collision root changed")

    evaluated_points = tuple(slope * L0 + intercept for slope, intercept in points)
    if any(evaluated_points[index] >= evaluated_points[index + 1] for index in range(7)):
        raise CertificateError("finite A_L fixture is not increasing")
    evaluated_differences = tuple(
        evaluated_points[right] - evaluated_points[left]
        for left in range(8)
        for right in range(left + 1, 8)
    )
    if len(set(evaluated_differences)) != 28:
        raise CertificateError("finite A_L fixture is not Golomb")

    return {
        "point_affine_pairs": [list(row) for row in points],
        "difference_affine_rows": [
            {"slope": slope, "intercept": intercept, "left": left, "right": right}
            for slope, intercept, left, right in differences
        ],
        "difference_count": 28,
        "largest_positive_collision_root": ftext(largest),
        "golomb_for_every_real_L_greater_than_25": True,
        "finite_L": L0,
        "finite_points": list(evaluated_points),
        "finite_difference_count": len(set(evaluated_differences)),
    }


def formal_nonspan_fixture() -> dict[str, object]:
    """Coefficient-tensor obstruction for the fixed full-prefix channels."""
    gap_eta = (F(-3, 16), F(-1, 16), F(1, 16), F(3, 16))
    point_weights = (
        F(0),
        F(0),
        F(0),
        gap_eta[0],
        gap_eta[1] - gap_eta[0],
        gap_eta[2] - gap_eta[1],
        gap_eta[3] - gap_eta[2],
        -gap_eta[3],
    )
    expected = (F(0), F(0), F(0), F(-3, 16), F(1, 8), F(1, 8), F(1, 8), F(-3, 16))
    if point_weights != expected or sum(point_weights, F(0)) != 0:
        raise CertificateError("midpoint ramp point weights changed")
    # A full-prefix three-channel mixer assigns the same formal kernel vector
    # (v_1,v_2,v_3) to every mark.  The ramp tensor has (w_k,0,0), and hence
    # could belong to that formal subspace only if all w_k were equal.
    if len(set(point_weights)) == 1:
        raise CertificateError("ramp weights unexpectedly became constant")
    return {
        "gap_eta": [ftext(value) for value in gap_eta],
        "point_weights": [ftext(value) for value in point_weights],
        "point_weight_sum": ftext(sum(point_weights, F(0))),
        "fixed_three_channel_form": "each mark has the identical formal coefficient row (v1,v2,v3)",
        "ramp_form": "mark k has formal coefficient row (w_k,0,0)",
        "ramp_is_in_fixed_full_prefix_channel_span": False,
        "claim_is_architectural_not_accidental_pointwise_nonidentity": True,
    }


def schur_extension_fixture() -> dict[str, object]:
    """Exact zero-mass fourth-channel boundary/Schur calculation."""
    h = (
        (F(13, 100), F(3, 25), F(0)),
        (F(3, 25), F(13, 50), F(3, 25)),
        (F(0), F(3, 25), F(13, 100)),
    )
    gamma = (F(1, 4), F(1, 2), F(1, 4))
    mass = (F(1), F(1), F(1))
    if tuple(sum(row, F(0)) for row in h) != gamma:
        raise CertificateError("three-channel mass row changed")
    leading_minors = tuple(determinant(tuple(row[:size] for row in h[:size])) for size in range(1, 4))
    if leading_minors != (F(13, 100), F(97, 5000), F(13, 20000)):
        raise CertificateError("three-channel positive minors changed")

    b = (F(1, 100), F(-1, 50), F(1, 100))
    if sum(b, F(0)) != 0:
        raise CertificateError("cross row does not annihilate bulk mass")
    h_inv_b = solve(h, b)
    schur_price = dot(b, h_inv_b)
    if h_inv_b != (F(1), F(-1), F(1)) or schur_price != F(1, 25):
        raise CertificateError("fourth-channel Schur price changed")
    d = F(1, 20)
    residual = d - schur_price
    if residual != F(1, 100):
        raise CertificateError("strict Schur residual changed")
    extended = tuple(
        tuple(h[row][column] for column in range(3)) + (b[row],)
        for row in range(3)
    ) + (tuple(b) + (d,),)
    extended_minors = tuple(
        determinant(tuple(row[:size] for row in extended[:size]))
        for size in range(1, 5)
    )
    if any(value <= 0 for value in extended_minors):
        raise CertificateError("strict extended block is not positive definite")
    extended_gamma = gamma + (F(0),)
    extended_mass = mass + (F(0),)
    if solve(extended, extended_gamma) != extended_mass:
        raise CertificateError("zero-mass extension changed the cover inverse")
    inverse_cover_price = dot(extended_gamma, extended_mass)
    if inverse_cover_price != 1:
        raise CertificateError("leading boundary normalization changed")
    return {
        "H": [[ftext(value) for value in row] for row in h],
        "gamma": [ftext(value) for value in gamma],
        "leading_principal_minors": [ftext(value) for value in leading_minors],
        "cross_b": [ftext(value) for value in b],
        "b_sum": ftext(sum(b, F(0))),
        "H_inverse_b": [ftext(value) for value in h_inv_b],
        "minimum_fourth_diagonal_for_psd": ftext(schur_price),
        "chosen_fourth_diagonal": ftext(d),
        "strict_schur_residual": ftext(residual),
        "extended_leading_principal_minors": [ftext(value) for value in extended_minors],
        "inverse_cover_price": ftext(inverse_cover_price),
        "boundary_normalization_is_unchanged": True,
        "nonzero_cross_coupling_has_zero_energy_price": False,
    }


def active_gate_fixture() -> dict[str, object]:
    n = 4
    divergence = F(n * n - 1, 8 * n * n)
    if divergence != F(15, 128):
        raise CertificateError("small-scale divergence coefficient changed")
    coefficients = (F(2), F(3), F(5))
    low_pass = (F(11), F(7), F(3), F(1))
    cumulative = tuple(sum(coefficients[: index + 1], F(0)) for index in range(3))
    lhs = sum((coefficients[index] * low_pass[index] for index in range(3)), F(0))
    rhs = sum(
        (cumulative[index] * (low_pass[index] - low_pass[index + 1]) for index in range(3)),
        F(0),
    ) + cumulative[-1] * low_pass[-1]
    if lhs != rhs or lhs != 58:
        raise CertificateError("finite low-pass Abel terminal changed")
    return {
        "general_optimal_small_T_coefficient_over_T": "(n^2-1)/(8*n^2)",
        "n4_small_T_coefficient_over_T": ftext(divergence),
        "ungated_integral_diverges_at_zero": True,
        "active_gate_for_A_L_contains": "9<T<L",
        "finite_abel_coefficients": [ftext(value) for value in coefficients],
        "finite_abel_low_pass_values_including_terminal": [ftext(value) for value in low_pass],
        "finite_abel_cumulative": [ftext(value) for value in cumulative],
        "finite_abel_lhs": ftext(lhs),
        "finite_abel_rhs_with_terminal": ftext(rhs),
        "terminal_is_nonzero_for_nonzero_ramp_measure_and_finite_box_width": True,
        "gate_endpoint_and_scale_terminal_must_be_owned": True,
    }


def asymptotic_no_go_fixture() -> dict[str, object]:
    q_log = F(9, 64)
    q_inverse_square = F(-45, 64)
    surplus_log = F(9, 128)
    surplus_inverse_square = F(9, 64)
    ramp_log = q_log + surplus_log
    ramp_inverse_square = q_inverse_square + surplus_inverse_square
    if ramp_log != F(27, 128) or ramp_inverse_square != F(-9, 16):
        raise CertificateError("ramp density coefficients changed")

    gothic_weights = (F(1, 16), F(1, 64), F(1, 16))
    gothic_log = sum(gothic_weights, F(0))
    if gothic_log != F(9, 64):
        raise CertificateError("positive Gothic leading coefficient changed")
    leading_gap = ramp_log - gothic_log
    if leading_gap != F(9, 128):
        raise CertificateError("ramp-versus-Gothic leading gap changed")
    wave_log = F(9, 64)
    reserve_log = gothic_log - wave_log
    if reserve_log != 0:
        raise CertificateError("unused potential acquired logarithmic mass")

    endpoint_edge = F(9, 64)
    hilbert_boundary = endpoint_edge / 2
    if hilbert_boundary != surplus_log:
        raise CertificateError("sharp endpoint Hilbert price changed")

    # Exact elementary finite separation at L=2^18.  The human proof uses
    # log 2 > 2/3, log 9 < 3, log 4 < 2, H=3L+9 <= 4L, drops positive
    # log 8/log 9 terms, and observes 9/(16L)-45/(64H)>0.
    log_l_lower = 18 * F(2, 3)
    finite_lower = (
        9 * log_l_lower - 27 * F(3) - 18 * F(2) + 10
    ) / 128
    if log_l_lower != 12 or finite_lower != F(1, 128):
        raise CertificateError("finite logarithmic separation lower bound changed")

    return {
        "family": "A_L=(0,2,5,16,16+L,17+L,25+L,25+3L), L>25",
        "current_gaps": ["L", "1", "8", "2L"],
        "scale_interval": "9<T<L",
        "singleton_rho": {"4": "1/T", "5": "0", "6": "0", "7": "1/T"},
        "adjacent_psi": {"45": "1/T^2", "56": "0", "67": "8/T^2"},
        "optimal_shift": ftext(F(11, 2)),
        "Q_density": "9/(64*T)-45/(64*T^2)",
        "Q_log_coefficient": ftext(q_log),
        "Q_inverse_square_coefficient": ftext(q_inverse_square),
        "optimal_surplus_density": "9/(128*T)+9/(64*T^2)",
        "surplus_log_coefficient": ftext(surplus_log),
        "surplus_inverse_square_coefficient": ftext(surplus_inverse_square),
        "optimal_ramp_density": "27/(128*T)-9/(16*T^2)",
        "ramp_log_coefficient": ftext(ramp_log),
        "ramp_inverse_square_coefficient": ftext(ramp_inverse_square),
        "ramp_integral_9_to_L": "(27/128)*log(L/9)-1/16+9/(16L)",
        "positive_gothic_capacity": "F_H(1)/16+F_H(9)/64+F_H(8)/16, H=3L+9",
        "positive_gothic_log_L_coefficient": ftext(gothic_log),
        "ramp_minus_positive_gothic_log_L_coefficient": ftext(leading_gap),
        "wave_log_L_coefficient": ftext(wave_log),
        "unused_potential_G_minus_W_log_L_coefficient": ftext(reserve_log),
        "wave_edge_47_squared_distance": ftext(endpoint_edge),
        "sharp_two_endpoint_Hilbert_boundary_coefficient": ftext(hilbert_boundary),
        "finite_separation_L": L0,
        "finite_log_L_lower": ftext(log_l_lower),
        "finite_ramp_integral_minus_gothic_lower_bound": ftext(finite_lower),
        "active_ramp_baseline_exceeds_positive_gothic_at_finite_L": True,
    }


def ordered_dual_caveat_fixture() -> dict[str, object]:
    vertices = (4, 5, 6, 7)
    edge_alpha = {(4, 6): F(1, 16), (4, 7): F(9, 64), (5, 7): F(1, 16)}
    b = [[F(0) for _ in vertices] for _ in vertices]
    position = {vertex: index for index, vertex in enumerate(vertices)}
    for (left, right), alpha in edge_alpha.items():
        b[position[left]][position[right]] = -alpha / 2
        b[position[right]][position[left]] = -alpha / 2
    roots = {}
    for left in range(4, 8):
        for right in range(left + 1, 8):
            value = b[position[left]][position[left]] + b[position[right]][position[right]] - 2 * b[position[left]][position[right]]
            roots[f"{left}{right}"] = value
            if value < 0:
                raise CertificateError("B left the ordered-root dual cone")
    if determinant(((b[0][0], b[0][3]), (b[3][0], b[3][3]))) >= 0:
        raise CertificateError("B unexpectedly became coefficient PSD")
    return {
        "B": [[ftext(value) for value in row] for row in b],
        "singleton_values": [ftext(F(0)) for _ in vertices],
        "root_values": {key: ftext(value) for key, value in roots.items()},
        "B_is_in_actual_ordered_root_dual": True,
        "B_is_coefficient_psd": False,
        "minus_B_is_in_actual_ordered_root_dual_when_a_wave_edge_is_active": False,
        "contraction": "<B,G_T>=Q_n(T) with zero ramp surplus",
        "negative_common_carrier_follows_from_dual_positivity_alone": False,
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
        "purpose": "Certify the scoped obstruction to inserting the active ordered-Gram ramp into the fixed three full-prefix centered carrier while paying its baseline only from the same positive Gothic beta sector.",
        "theorem_contract": {
            "formal_nonspan": "the rank-weighted ramp is a new membership-sensitive zero-mass input channel, not a channel-space combination of the fixed three full-prefix convolutions",
            "active_gate": "ungated ramp energy diverges at zero; a finite active gate leaves explicit first/last rows and a nonzero low-pass terminal",
            "schur_price": "a zero-mass fourth channel can preserve leading boundary normalization, but positive definiteness forces d>=b^T H^-1 b and hence no nonzero cross coupling is energy-free",
            "asymptotic_no_go": "on A_L, the optimal active ramp baseline has log coefficient 27/128 while the complete positive same-epoch Gothic sector has 18/128",
            "ordered_dual_caveat": "B itself has zero surplus in the actual ordered-root dual, but this positive contraction is not by itself a negative common Cauchy carrier",
        },
        "affine_golomb_fixture": affine_golomb_fixture(),
        "formal_nonspan_fixture": formal_nonspan_fixture(),
        "schur_extension_fixture": schur_extension_fixture(),
        "active_gate_fixture": active_gate_fixture(),
        "asymptotic_no_go_fixture": asymptotic_no_go_fixture(),
        "ordered_dual_caveat_fixture": ordered_dual_caveat_fixture(),
        "scope": {
            "linear_cellwise_ramp_insertion_into_fixed_three_full_prefix_carrier_closed": True,
            "positive_same_epoch_gothic_beta_alone_pays_optimal_ramp_baseline": False,
            "unused_negative_potential_pays_ramp_surplus_on_A_L": False,
            "actual_ordered_root_dual_identity_exact": True,
            "direct_actual_cell_signed_rewrite_ruled_out": False,
            "membership_sensitive_common_master_ruled_out": False,
            "cross_epoch_or_cross_phase_payment_ruled_out": False,
            "disjoint_external_reserve_ruled_out": False,
            "c058_resolved": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "publication_novelty_claimed": False,
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
    changed["integrity"]["payload_sha256"] = "0" * 64
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["formal_nonspan_fixture"]["ramp_is_in_fixed_full_prefix_channel_span"] = True
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["schur_extension_fixture"]["minimum_fourth_diagonal_for_psd"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["active_gate_fixture"]["ungated_integral_diverges_at_zero"] = False
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["asymptotic_no_go_fixture"]["ramp_minus_positive_gothic_log_L_coefficient"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["asymptotic_no_go_fixture"]["finite_ramp_integral_minus_gothic_lower_bound"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["ordered_dual_caveat_fixture"]["B_is_coefficient_psd"] = True
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["scope"]["direct_actual_cell_signed_rewrite_ruled_out"] = True
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
