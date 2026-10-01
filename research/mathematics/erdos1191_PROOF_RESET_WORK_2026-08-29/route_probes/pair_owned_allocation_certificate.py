#!/usr/bin/env python3
"""Exact certificate for the pair-owned Route-C allocation and scalar no-go.

The certificate verifies four deliberately scoped facts:

* the positive finite-potential rows admit a proportional pair allocation;
* a birth-supported owner lift makes the preceding negative epoch row act on
  a zero state;
* the scale terminal and signless-completion diagonal price are exact; and
* one explicit nested Sidon pair defeats every phasewise scalar fractional
  allocation satisfying the stated envelope and adjacent nonnegative gate.

It does not pay the PSD diagonal price or resolve C058 or Erdős #1191.
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
DEFAULT_CERTIFICATE = HERE / "pair_owned_allocation_certificate.json"
SCHEMA = "erdos1191.pair_owned_allocation.v1"

OLD_PREFIX = (0, 1, 3, 7, 12, 20, 30, 44)
NEW_PREFIX = (
    0,
    1,
    3,
    7,
    12,
    20,
    30,
    44,
    1044,
    1094,
    2095,
    2155,
    2225,
    2305,
    2395,
    2495,
)


class CertificateError(RuntimeError):
    """Raised when an exact replay or scope check fails."""


def ftext(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def power_two(exponent: int) -> F:
    return F(1 << exponent) if exponent >= 0 else F(1, 1 << (-exponent))


def overlap(width: F, distance: int) -> F:
    return (width - distance) / (width * width) if distance < width else F(0)


def positive_difference_records(points: Sequence[int]) -> dict[int, tuple[tuple[int, int], ...]]:
    records: dict[int, list[tuple[int, int]]] = {}
    for left in range(len(points)):
        for right in range(left + 1, len(points)):
            records.setdefault(points[right] - points[left], []).append((left, right))
    return {difference: tuple(owners) for difference, owners in records.items()}


def require_sidon(points: Sequence[int]) -> dict[int, tuple[tuple[int, int], ...]]:
    records = positive_difference_records(points)
    if len(records) != len(points) * (len(points) - 1) // 2:
        raise CertificateError("difference count is not Sidon")
    if any(len(owners) != 1 for owners in records.values()):
        raise CertificateError("repeated positive difference")
    return records


def first_use_differences(old: Sequence[int], new: Sequence[int]) -> tuple[int, ...]:
    if tuple(new[: len(old)]) != tuple(old):
        raise CertificateError("prefixes are not nested by initial segment")
    values = []
    for left in range(len(new)):
        for right in range(left + 1, len(new)):
            if right >= len(old):
                values.append(new[right] - new[left])
    if len(set(values)) != len(values):
        raise CertificateError("first-use differences are not unique")
    return tuple(sorted(values))


def centered_first_use(width: F, differences: Sequence[int]) -> F:
    return 2 * sum((overlap(width, difference) for difference in differences), F(0))


def exact_first_use_supremum(differences: Sequence[int]) -> dict[str, object]:
    """Maximize 2 sum_(d<T)(T-d)/T^2 over all real T>0 exactly."""
    ordered = tuple(sorted(differences))
    running = 0
    best = (F(0), 0, F(0))
    range_best: dict[str, tuple[F, int, F]] = {}
    blocks = ((1, 16), (17, 44), (45, len(ordered)))
    for count, distance in enumerate(ordered, 1):
        running += distance
        next_distance = ordered[count] if count < len(ordered) else None
        candidates = [F(distance)]
        critical = F(2 * running, count)
        if critical >= distance and (next_distance is None or critical <= next_distance):
            candidates.append(critical)
        if next_distance is not None:
            candidates.append(F(next_distance))
        for width in candidates:
            value = F(2) * (count * width - running) / (width * width)
            if value > best[0]:
                best = (value, count, width)
            for start, stop in blocks:
                if start <= count <= stop:
                    key = f"{start}-{stop}"
                    if key not in range_best or value > range_best[key][0]:
                        range_best[key] = (value, count, width)
    return {
        "value": ftext(best[0]),
        "active_count": best[1],
        "width": ftext(best[2]),
        "range_maxima": {
            key: {"value": ftext(row[0]), "active_count": row[1], "width": ftext(row[2])}
            for key, row in range_best.items()
        },
    }


def beta(n: int, p: int, q: int) -> F:
    separation = q - p
    if separation == 0:
        return F(1, n * n)
    if separation == 1:
        return F(1, 4 * n * n)
    return F(1, 2 * n * n)


def positive_owners(points: Sequence[int], n: int) -> tuple[tuple[int, int, int, F], ...]:
    return tuple(
        (p, q, points[q] - points[p - 1], beta(n, p, q))
        for p in range(n + 1, 2 * n - 1)
        for q in range(p, 2 * n - 1)
    )


def tent(points: Sequence[int], i: int, j: int, width: F) -> F:
    middle = points[j - 1] - points[i]
    left_gap = points[i] - points[i - 1]
    right_gap = points[j] - points[j - 1]
    return (
        overlap(width, middle)
        + overlap(width, middle + left_gap + right_gap)
        - overlap(width, middle + left_gap)
        - overlap(width, middle + right_gap)
    )


def wave_density(points: Sequence[int], n: int, width: F) -> F:
    return sum(
        (
            F((j - i) ** 2, 4 * n * n) * tent(points, i, j, width)
            for j in range(n + 2, 2 * n)
            for i in range(n, j - 1)
        ),
        F(0),
    )


def positive_density(points: Sequence[int], n: int, width: F) -> F:
    return sum(
        (coefficient * overlap(width, distance) for _, _, distance, coefficient in positive_owners(points, n)),
        F(0),
    )


def proportional_allocation_rows(points: Sequence[int], n: int, exponents: Sequence[int]) -> tuple[dict[str, object], ...]:
    rows = []
    for exponent in exponents:
        width = power_two(exponent)
        q_value = wave_density(points, n, width)
        p_value = positive_density(points, n, width)
        if not (F(0) <= q_value <= p_value):
            raise CertificateError("positive density does not dominate Q")
        ratio = q_value / p_value if p_value else F(0)
        allocations = []
        total = F(0)
        for p, q, distance, coefficient in positive_owners(points, n):
            capacity = width * coefficient * overlap(width, distance)
            allocated = capacity * ratio
            if not (F(0) <= allocated <= capacity):
                raise CertificateError("proportional allocation left its capacity interval")
            total += allocated
            if allocated:
                allocations.append(
                    {
                        "p": p,
                        "q": q,
                        "distance": distance,
                        "capacity": ftext(capacity),
                        "allocated": ftext(allocated),
                    }
                )
        demand = width * q_value
        if total != demand:
            raise CertificateError("pair allocations do not sum to demand")
        rows.append(
            {
                "scale": exponent,
                "width": ftext(width),
                "Q": ftext(q_value),
                "P": ftext(p_value),
                "ratio": ftext(ratio),
                "demand": ftext(demand),
                "allocated_total": ftext(total),
                "nonzero_allocations": allocations,
            }
        )
    return tuple(rows)


def owner_lift_fixture() -> dict[str, object]:
    """Replay one finite birth row, its zero prebirth row, and scale terminal."""
    distance = 8
    birth = 1
    first_scale, last_scale = 2, 5
    coefficients = {2: F(0), 3: F(0), 4: F(1, 100), 5: F(1, 50)}
    cumulative: dict[int, F] = {}
    running = F(0)
    for scale in range(first_scale, last_scale + 1):
        running += coefficients[scale]
        cumulative[scale] = running
    state = {
        (epoch, scale): (2 * overlap(power_two(scale), distance) if epoch >= birth else F(0))
        for epoch in (birth - 1, birth)
        for scale in range(first_scale, last_scale + 2)
    }
    band = {
        (epoch, scale): state[epoch, scale] - state[epoch, scale + 1]
        for epoch in (birth - 1, birth)
        for scale in range(first_scale, last_scale + 1)
    }
    lhs = sum(
        (coefficients[scale] * state[birth, scale] for scale in range(first_scale, last_scale + 1)),
        F(0),
    )
    prebirth = sum(
        (-cumulative[scale] * band[birth - 1, scale] for scale in range(first_scale, last_scale + 1)),
        F(0),
    )
    birth_bulk = sum(
        (cumulative[scale] * band[birth, scale] for scale in range(first_scale, last_scale + 1)),
        F(0),
    )
    terminal = cumulative[last_scale] * state[birth, last_scale + 1]
    if prebirth != 0 or lhs != prebirth + birth_bulk + terminal:
        raise CertificateError("owner-lift transport fixture failed")

    band_diagonal = sum(
        (cumulative[scale] / power_two(scale) for scale in range(first_scale, last_scale + 1)),
        F(0),
    )
    tail_diagonal = cumulative[last_scale] / power_two(last_scale)
    swapped = 2 * sum(
        (coefficients[scale] / power_two(scale) for scale in range(first_scale, last_scale + 1)),
        F(0),
    )
    if band_diagonal + tail_diagonal != swapped:
        raise CertificateError("diagonal price summation failed")
    return {
        "distance": distance,
        "birth_epoch": birth,
        "first_scale": first_scale,
        "last_scale": last_scale,
        "coefficients": {str(scale): ftext(coefficients[scale]) for scale in coefficients},
        "cumulative": {str(scale): ftext(cumulative[scale]) for scale in cumulative},
        "prebirth_bands_all_zero": all(band[birth - 1, scale] == 0 for scale in cumulative),
        "formal_negative_prebirth_contribution": ftext(prebirth),
        "lhs": ftext(lhs),
        "positive_birth_bulk": ftext(birth_bulk),
        "scale_terminal": ftext(terminal),
        "transport_identity_verified": True,
        "band_diagonal_price": ftext(band_diagonal),
        "tail_diagonal_price": ftext(tail_diagonal),
        "swapped_diagonal_price": ftext(swapped),
        "diagonal_price_identity_verified": True,
    }


def cross_ratio_ratio(points: Sequence[int], i: int, j: int) -> F:
    middle = points[j - 1] - points[i]
    left_gap = points[i] - points[i - 1]
    right_gap = points[j] - points[j - 1]
    return F((middle + left_gap) * (middle + right_gap), middle * (middle + left_gap + right_gap))


def log_lower(alpha: F, ratio: F) -> F:
    """Use log(x)>=2(x-1)/(x+1), x>=1."""
    return alpha * 2 * (ratio - 1) / (ratio + 1)


def scalar_no_go_fixture() -> dict[str, object]:
    old_records = require_sidon(OLD_PREFIX)
    new_records = require_sidon(NEW_PREFIX)
    first_use = first_use_differences(OLD_PREFIX, NEW_PREFIX)
    supremum = exact_first_use_supremum(first_use)
    if F(supremum["value"]) != F(18, 385):
        raise CertificateError("first-use supremum changed")
    horizon = OLD_PREFIX[-1] - OLD_PREFIX[3]
    weight_ratio = F(100, 81)
    total_old_capacity = F(horizon, 4 * 4)
    scalar_upper = F(supremum["value"]) * weight_ratio * total_old_capacity
    if scalar_upper != F(185, 1386):
        raise CertificateError("scalar upper bound changed")

    selected = ((8, 10), (10, 15), (10, 14), (10, 13), (10, 12), (8, 15), (13, 15))
    comparison = (F(1, 40), F(1, 50), F(1, 60), F(1, 72), F(1, 100), F(1, 180), F(1, 230))
    rows = []
    for (i, j), threshold in zip(selected, comparison, strict=True):
        alpha = F((j - i) ** 2, 4 * 8 * 8)
        ratio = cross_ratio_ratio(NEW_PREFIX, i, j)
        lower = log_lower(alpha, ratio)
        if lower <= threshold:
            raise CertificateError("selected cross-ratio lower bound lost its rational margin")
        rows.append(
            {
                "i": i,
                "j": j,
                "alpha": ftext(alpha),
                "cross_ratio_exponential": ftext(ratio),
                "log_lower_contribution": ftext(lower),
                "comparison": ftext(threshold),
            }
        )
    comparison_sum = sum(comparison, F(0))
    target = F(37, 396)
    gap = comparison_sum - target
    if comparison_sum != F(494, 5175) or gap != F(461, 227700):
        raise CertificateError("rational contradiction gap changed")
    exponential_partial_sum = F(1) + F(7, 10) + F(49, 200) + F(343, 6000)
    if exponential_partial_sum != F(12013, 6000) or exponential_partial_sum <= 2:
        raise CertificateError("log(2)<7/10 witness changed")
    if scalar_upper * F(7, 10) != target:
        raise CertificateError("scalar logarithmic upper does not meet the target exactly")
    return {
        "old_prefix": list(OLD_PREFIX),
        "new_prefix": list(NEW_PREFIX),
        "old_difference_count": len(old_records),
        "new_difference_count": len(new_records),
        "first_use_difference_count": len(first_use),
        "old_horizon": horizon,
        "weight_ratio": ftext(weight_ratio),
        "total_old_scalar_capacity_bound": ftext(total_old_capacity),
        "first_use_supremum": supremum,
        "scalar_phase_integral_upper": ftext(scalar_upper),
        "selected_cross_ratio_rows": rows,
        "comparison_sum": ftext(comparison_sum),
        "target": ftext(target),
        "strict_rational_gap": ftext(gap),
        "exp_7_over_10_partial_sum": ftext(exponential_partial_sum),
        "log2_strictly_below_7_over_10": True,
        "contradiction_verified": True,
    }


def payload_hash(certificate: Mapping[str, object]) -> str:
    payload = {key: value for key, value in certificate.items() if key != "integrity"}
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def rendered_bytes(certificate: Mapping[str, object]) -> bytes:
    return (json.dumps(certificate, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def build_certificate() -> dict[str, object]:
    allocation_rows = proportional_allocation_rows(OLD_PREFIX, 4, tuple(range(0, 6)))
    owners = positive_owners(OLD_PREFIX, 4)
    beta_sum = sum((row[3] for row in owners), F(0))
    if beta_sum != F(9, 64):
        raise CertificateError("strict-interior beta sum changed")
    certificate: dict[str, object] = {
        "schema": SCHEMA,
        "purpose": "Certify the explicit pair LP, birth-supported owner lift, exact diagonal-price identity, and an exact scalar-aggregation no-go fixture.",
        "theorem_contract": {
            "pair_lp": "x_(gamma,r)=u_(gamma,r)*Q_n(T_r)/P_n(T_r), with x=0 when P=0",
            "owner_lift": "the coefficient -w_b*s_(gamma,r) multiplies O^gamma_(b-1,r)=0; +w_b*s_(gamma,r) multiplies the birth band",
            "scale_terminal": "s_(gamma,U)*v_(gamma,U+1)=sum_(r>U)s_(gamma,U)*(v_(gamma,r)-v_(gamma,r+1))",
            "diagonal_price": "D_(b,theta)=2*w_b*sum_(gamma,r<=U) a_(gamma,r)/T_r for the signless edge completion including its terminal tail",
            "scalar_no_go": "the displayed nested Sidon pair admits no phasewise scalar fractional allocation satisfying envelope, demand, and adjacent nonnegative gate (4.3)-(4.5)",
        },
        "pair_lp_fixture": {
            "points": list(OLD_PREFIX),
            "wave_epoch": 4,
            "strict_interior_owner_count": len(owners),
            "strict_interior_beta_sum": ftext(beta_sum),
            "rows": list(allocation_rows),
        },
        "owner_lift_fixture": owner_lift_fixture(),
        "scalar_no_go_fixture": scalar_no_go_fixture(),
        "scope": {
            "positive_potential_pair_lp_solved": True,
            "owner_lift_adjacent_sign_gate_removed": True,
            "finite_scale_terminal_kept": True,
            "signless_psd_diagonal_price_formula_certified": True,
            "scalar_fractional_fallback_universal": False,
            "psd_diagonal_price_paid": False,
            "gothic_ledger_rewritten": False,
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
    changed["pair_lp_fixture"]["rows"][-1]["allocated_total"] = "0/1"
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["owner_lift_fixture"]["formal_negative_prebirth_contribution"] = "1/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["owner_lift_fixture"]["scale_terminal"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["scalar_no_go_fixture"]["first_use_supremum"]["value"] = "1/20"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["scalar_no_go_fixture"]["new_prefix"][-1] += 1
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["scope"]["psd_diagonal_price_paid"] = True
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["scope"]["question_1_resolved"] = True
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
    parser.add_argument("--emit", action="store_true", help="print the canonical certificate JSON")
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
