#!/usr/bin/env python3
"""Exact certificate for the active dipole coefficient-PSD price obstruction.

The universal SDP formula is proved in the companion memo.  This certificate
locks its factors on an exact rational primal/dual fixture, checks the
pointwise price-versus-tent inequality without floating point, and replays the
eight-mark rational logarithmic separation G_4 < 2 W_4.

It does not rule out Gram-restricted, signed, or cross-epoch masters.
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
DEFAULT_CERTIFICATE = HERE / "dipole_psd_price_certificate.json"
SCHEMA = "erdos1191.dipole_psd_price.v1"
GOLomb = (0, 101, 204, 309, 416, 525, 636, 749)


class CertificateError(RuntimeError):
    """Raised when an exact replay or scope check fails."""


def ftext(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def positive_differences(points: Sequence[int]) -> tuple[int, ...]:
    values = tuple(
        points[right] - points[left]
        for left in range(len(points))
        for right in range(left + 1, len(points))
    )
    if len(set(values)) != len(values):
        raise CertificateError("fixture is not a Golomb ruler")
    return tuple(sorted(values))


def log_bounds(ratio: F) -> tuple[F, F]:
    """Return exact lower/upper atanh bounds for log(ratio), ratio>1."""
    if ratio <= 1:
        raise ValueError("ratio must exceed one")
    z = (ratio - 1) / (ratio + 1)
    lower = 2 * z
    upper = 2 * (z + z**3 / (3 * (1 - z * z)))
    return lower, upper


def completion_fixture() -> dict[str, object]:
    """Rational square g_i fixture for the exact weighted SDP factors."""
    roots = (F(1), F(2), F(3), F(4))
    g = tuple(root * root for root in roots)
    edges = {
        (0, 1): F(1, 3),
        (0, 2): F(2, 5),
        (1, 3): F(3, 7),
        (2, 3): F(5, 11),
    }
    diagonal = []
    for vertex, root in enumerate(roots):
        weighted_neighbors = sum(
            (
                alpha * roots[right if left == vertex else left]
                for (left, right), alpha in edges.items()
                if vertex in (left, right)
            ),
            F(0),
        )
        diagonal.append(weighted_neighbors / (2 * root))
    primal = sum((g[index] * diagonal[index] for index in range(len(g))), F(0))
    dual = sum((alpha * roots[left] * roots[right] for (left, right), alpha in edges.items()), F(0))
    if primal != dual or primal != F(12416, 1155):
        raise CertificateError("weighted completion primal and dual disagree")
    edge_blocks = []
    for (left, right), alpha in edges.items():
        upper_left = alpha * roots[right] / (2 * roots[left])
        lower_right = alpha * roots[left] / (2 * roots[right])
        off_diagonal = -alpha / 2
        determinant = upper_left * lower_right - off_diagonal * off_diagonal
        if upper_left <= 0 or lower_right <= 0 or determinant != 0:
            raise CertificateError("rank-one edge block is not PSD")
        edge_blocks.append(
            {
                "left": left,
                "right": right,
                "alpha": ftext(alpha),
                "upper_left": ftext(upper_left),
                "off_diagonal": ftext(off_diagonal),
                "lower_right": ftext(lower_right),
                "determinant": ftext(determinant),
            }
        )
    return {
        "g": [ftext(value) for value in g],
        "sqrt_g": [ftext(value) for value in roots],
        "diagonal_optimizer": [ftext(value) for value in diagonal],
        "edge_blocks": edge_blocks,
        "primal_weighted_diagonal_cost": ftext(primal),
        "rank_one_dual_value": ftext(dual),
        "strong_duality_verified": True,
    }


def tent_numerator(middle: int, left_gap: int, right_gap: int, width: int) -> int:
    def positive(value: int) -> int:
        return max(value, 0)

    return (
        positive(width - middle)
        + positive(width - middle - left_gap - right_gap)
        - positive(width - middle - left_gap)
        - positive(width - middle - right_gap)
    )


def pointwise_price_rows() -> tuple[dict[str, object], ...]:
    fixtures = (
        (4, 1, 2, 5),
        (4, 1, 2, 6),
        (4, 1, 2, 7),
        (109, 107, 111, 110),
        (109, 107, 111, 216),
        (220, 107, 113, 327),
    )
    rows = []
    for middle, left_gap, right_gap, width in fixtures:
        numerator = tent_numerator(middle, left_gap, right_gap, width)
        psi = F(numerator, width * width)
        g_left = F(2 * min(left_gap, width), width * width)
        g_right = F(2 * min(right_gap, width), width * width)
        squared_margin = g_left * g_right - 4 * psi * psi
        if psi < 0 or squared_margin < 0:
            raise CertificateError("pointwise price bound failed")
        rows.append(
            {
                "middle": middle,
                "left_gap": left_gap,
                "right_gap": right_gap,
                "width": width,
                "psi": ftext(psi),
                "g_left": ftext(g_left),
                "g_right": ftext(g_right),
                "g_product_minus_4psi_squared": ftext(squared_margin),
            }
        )
    return tuple(rows)


def golomb_obstruction_fixture() -> dict[str, object]:
    differences = positive_differences(GOLomb)
    expected = (
        101,
        103,
        105,
        107,
        109,
        111,
        113,
        204,
        208,
        212,
        216,
        220,
        224,
        309,
        315,
        321,
        327,
        333,
        416,
        424,
        432,
        440,
        525,
        535,
        545,
        636,
        648,
        749,
    )
    if differences != expected:
        raise CertificateError("Golomb difference list changed")

    wave_ratios = (F(15840, 11881), F(49280, 36963), F(108891, 96800))
    wave_weights = (F(1, 16), F(1, 16), F(9, 64))
    wave_lower = sum(
        (weight * log_bounds(ratio)[0] for weight, ratio in zip(wave_weights, wave_ratios, strict=True)),
        F(0),
    )
    gothic_rows = (
        (F(1, 16), F(440, 109), F(109, 440) - 1),
        (F(1, 64), F(2), F(1, 2) - 1),
        (F(1, 16), F(440, 111), F(111, 440) - 1),
    )
    gothic_upper = sum(
        (weight * (log_bounds(ratio)[1] + affine) for weight, ratio, affine in gothic_rows),
        F(0),
    )
    margin = 2 * wave_lower - gothic_upper
    expected_wave = F(822003631010073, 15736132943272736)
    expected_gothic = F(81908500355, 936943462656)
    expected_margin = F(413517772924972663409287, 24249781066916299488221952)
    if wave_lower != expected_wave or gothic_upper != expected_gothic or margin != expected_margin:
        raise CertificateError("exact logarithmic separation changed")
    if margin <= 0:
        raise CertificateError("Gothic upper is not below twice the Wave lower")

    complete_wave_edges = ((4, 6), (4, 7), (5, 7))
    colors = {4: 0, 5: 0, 6: 1, 7: 1}
    if any(colors[left] == colors[right] for left, right in complete_wave_edges):
        raise CertificateError("n=4 Wave graph is not bipartite")
    alpha_sum = F(1, 16) + F(9, 64) + F(1, 16)
    nonlocalized_small_scale_coefficient = 2 * alpha_sum
    if nonlocalized_small_scale_coefficient != F(17, 32):
        raise CertificateError("nonlocalized 1/T divergence coefficient changed")
    return {
        "points": list(GOLomb),
        "positive_differences": list(differences),
        "difference_count": len(differences),
        "current_gaps": [107, 109, 111, 113],
        "horizon": 440,
        "wave_log_ratios": [ftext(value) for value in wave_ratios],
        "wave_lower": ftext(wave_lower),
        "gothic_upper": ftext(gothic_upper),
        "two_wave_lower_minus_gothic_upper": ftext(margin),
        "strict_separation_verified": True,
        "complete_wave_edges": [list(edge) for edge in complete_wave_edges],
        "bipartition": {str(vertex): color for vertex, color in colors.items()},
        "direct_sign_fixture_is_bipartite": True,
        "nonlocalized_price_coefficient_over_T": ftext(nonlocalized_small_scale_coefficient),
        "nonlocalized_integral_diverges_at_zero": True,
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
        "purpose": "Certify the exact weighted diagonal-completion factors, P>=2Q pointwise gate, and the n=4 positive-Gothic-capacity obstruction.",
        "theorem_contract": {
            "minimum_price": "min sum_i g_i*d_i subject to diag(d)+B>=0 equals sum_(active i,j) alpha_ij*sqrt(g_i*g_j)",
            "pointwise_gate": "sqrt(g_i(T)*g_j(T))>=2*psi_ij(T), hence P_n(T)>=2*Q_n(T)",
            "integrated_gate": "Pi_n=int_0^infinity P_n(T)dT>=2*W_n",
            "fixture_obstruction": "for the displayed n=4 Golomb prefix, positive finite-horizon Gothic capacity G_4<2*W_4<=Pi_4",
        },
        "completion_fixture": completion_fixture(),
        "pointwise_price_rows": list(pointwise_price_rows()),
        "golomb_obstruction_fixture": golomb_obstruction_fixture(),
        "scope": {
            "weighted_coefficient_psd_price_exact": True,
            "active_localization_required_for_integrability": True,
            "positive_same_epoch_gothic_capacity_alone_universally_pays_price": False,
            "gram_restricted_route_ruled_out": False,
            "signed_cancellation_ruled_out": False,
            "cross_epoch_payment_ruled_out": False,
            "larger_psd_master_ruled_out": False,
            "c058_resolved": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
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
    expected = build_certificate()
    if certificate != expected:
        raise CertificateError("semantic replay mismatch")


def rehash(certificate: dict[str, object]) -> None:
    certificate["integrity"] = {"payload_sha256": payload_hash(certificate)}


def self_check(certificate: Mapping[str, object]) -> int:
    validate_certificate(certificate)
    mutations = []

    changed = copy.deepcopy(certificate)
    changed["completion_fixture"]["rank_one_dual_value"] = "0/1"
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["completion_fixture"]["diagonal_optimizer"][0] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["pointwise_price_rows"][0]["g_product_minus_4psi_squared"] = "-1/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["golomb_obstruction_fixture"]["points"][-1] += 1
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["golomb_obstruction_fixture"]["two_wave_lower_minus_gothic_upper"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["scope"]["positive_same_epoch_gothic_capacity_alone_universally_pays_price"] = True
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
