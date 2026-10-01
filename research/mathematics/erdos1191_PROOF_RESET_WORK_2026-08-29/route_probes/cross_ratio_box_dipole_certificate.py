#!/usr/bin/env python3
"""Exact box-dipole certificate for the Route-C/Wave-19 interface.

The certificate proves a continuous-scale identity and a pointwise capacity
map.  It also certifies that one scheduled scale and one unshifted dyadic grid
cannot recover the continuous logarithmic mass with universal constants.
Nothing here closes the common signed history coupling or Erdős #1191.
"""
from __future__ import annotations

import argparse
import copy
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
from typing import Iterable, Sequence


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "cross_ratio_box_dipole_certificate.json"
STATUS = "CONTINUOUS_IDENTITY_AND_POINTWISE_MAP_ONLY_HISTORY_COUPLING_OPEN"
EPOCHS = (4, 5, 8, 16, 32, 64)

MINIMAL_EIGHT = (0, 1, 4, 9, 15, 22, 32, 34)
HALL_64 = (
    0, 1, 18, 34, 79, 127, 171, 218, 319, 415, 509, 613, 710, 808, 903,
    1002, 1135, 1385, 1636, 1885, 2133, 2380, 2632, 2885, 3139, 3396,
    3651, 3909, 4165, 4424, 4669, 4930, 5080, 5578, 6074, 6564, 7066,
    7569, 8079, 8573, 9040, 9513, 9970, 10431, 10852, 11311, 11723,
    12133, 12607, 13079, 13488, 13896, 14303, 14708, 15109, 15559,
    15961, 16359, 16765, 17164, 17618, 18051, 18451, 18854,
)


class CertificateError(ValueError):
    pass


def canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def rendered_bytes(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()


def ftext(value: F) -> str:
    return str(value)


def r_box(width: int, distance: int) -> F:
    if width < 1 or distance < 0:
        raise ValueError("width must be positive and distance nonnegative")
    return F(max(width - distance, 0), width * width)


def psi(width: int, middle: int, left_gap: int, right_gap: int) -> F:
    return (
        r_box(width, middle)
        + r_box(width, middle + left_gap + right_gap)
        - r_box(width, middle + left_gap)
        - r_box(width, middle + right_gap)
    )


def psi_piecewise(width: int, middle: int, left_gap: int, right_gap: int) -> F:
    if min(width, middle, left_gap, right_gap) < 1:
        raise ValueError("positive integer parameters required")
    small, large = sorted((left_gap, right_gap))
    terminal = middle + small + large
    if width <= middle or width >= terminal:
        return F(0)
    if width <= middle + small:
        return F(width - middle, width * width)
    if width <= middle + large:
        return F(small, width * width)
    return F(terminal - width, width * width)


def edge_inner_product(width: int, middle: int, left_gap: int, right_gap: int) -> F:
    """<e_i*K_T,e_j*K_T> for local marks 0,h,h+M,h+M+k."""
    return (
        r_box(width, middle + left_gap)
        - r_box(width, middle + left_gap + right_gap)
        - r_box(width, middle)
        + r_box(width, middle + right_gap)
    )


@dataclass(frozen=True)
class FormalIntegral:
    logs: tuple[tuple[int, F], ...]
    constant: F = F(0)

    @classmethod
    def from_parts(cls, logs: Iterable[tuple[int, F | int]], constant: F | int = 0) -> "FormalIntegral":
        combined: defaultdict[int, F] = defaultdict(F)
        for base, coefficient in logs:
            if base < 1:
                raise ValueError("formal logarithm base must be positive")
            combined[base] += F(coefficient)
        return cls(tuple((base, value) for base, value in sorted(combined.items()) if base != 1 and value), F(constant))

    def __add__(self, other: "FormalIntegral") -> "FormalIntegral":
        return FormalIntegral.from_parts((*self.logs, *other.logs), self.constant + other.constant)

    def scale(self, coefficient: F | int) -> "FormalIntegral":
        factor = F(coefficient)
        return FormalIntegral.from_parts(((base, factor * value) for base, value in self.logs), factor * self.constant)


def integral_r_interval(distance: int, lower: int, upper: int) -> FormalIntegral:
    """Formal integral of R_T(distance) dT over [lower,upper]."""
    if distance < 1 or lower < 1 or upper < lower:
        raise ValueError("invalid positive interval")
    start = max(distance, lower)
    if upper <= start:
        return FormalIntegral(())
    return FormalIntegral.from_parts(
        ((upper, 1), (start, -1)),
        F(distance, upper) - F(distance, start),
    )


def integral_psi_interval(middle: int, left_gap: int, right_gap: int, lower: int, upper: int) -> FormalIntegral:
    distances = (
        (middle, 1),
        (middle + left_gap + right_gap, 1),
        (middle + left_gap, -1),
        (middle + right_gap, -1),
    )
    total = FormalIntegral(())
    for distance, sign in distances:
        total = total + integral_r_interval(distance, lower, upper).scale(sign)
    return total


def integral_psi_form(middle: int, left_gap: int, right_gap: int) -> FormalIntegral:
    terminal = middle + left_gap + right_gap
    # Beyond terminal the four affine tails cancel exactly.
    value = integral_psi_interval(middle, left_gap, right_gap, middle, terminal)
    expected = FormalIntegral.from_parts(
        ((middle + left_gap, 1), (middle + right_gap, 1), (middle, -1), (terminal, -1))
    )
    if value != expected:
        raise CertificateError("continuous integral/cross-ratio exponent map failed")
    return value


def phase_partition_audit(middle: int, left_gap: int, right_gap: int) -> dict[str, object]:
    """Finite reindex check behind the exact log-phase average theorem."""
    terminal = middle + left_gap + right_gap
    lower_power = 1
    while 2 * lower_power <= middle:
        lower_power *= 2
    upper_power = lower_power
    while upper_power < terminal:
        upper_power *= 2
    pieces = []
    total = FormalIntegral(())
    value = lower_power
    while value < upper_power:
        following = 2 * value
        pieces.append((value, following))
        total = total + integral_psi_interval(middle, left_gap, right_gap, value, following)
        value = following
    expected = integral_psi_form(middle, left_gap, right_gap)
    if total != expected:
        raise CertificateError("finite dyadic partition/reindex failed")
    return {
        "middle": middle,
        "left_gap": left_gap,
        "right_gap": right_gap,
        "partition": [list(piece) for piece in pieces],
        "partition_contiguous": all(pieces[index][1] == pieces[index + 1][0] for index in range(len(pieces) - 1)),
        "formal_log_terms": [[base, ftext(value)] for base, value in expected.logs],
        "rational_constant": ftext(expected.constant),
    }


def w_atom_coefficient(epoch: int, left: int, right: int) -> F:
    if epoch <= left <= right - 2 and epoch + 2 <= right <= 2 * epoch - 1:
        return F((right - left) ** 2, 4 * epoch * epoch)
    return F(0)


def lambda_formula(epoch: int, point_left: int, point_right: int) -> F:
    """Coefficient of R_T(a_q-a_p) after expanding all W dipoles."""
    return (
        w_atom_coefficient(epoch, point_left, point_right + 1)
        + w_atom_coefficient(epoch, point_left + 1, point_right)
        - w_atom_coefficient(epoch, point_left + 1, point_right + 1)
        - w_atom_coefficient(epoch, point_left, point_right)
    )


def direct_lambda_map(epoch: int) -> dict[tuple[int, int], F]:
    result: defaultdict[tuple[int, int], F] = defaultdict(F)
    for right in range(epoch + 2, 2 * epoch):
        for left in range(epoch, right - 1):
            weight = w_atom_coefficient(epoch, left, right)
            for pair, sign in (
                ((left, right - 1), 1),
                ((left - 1, right), 1),
                ((left - 1, right - 1), -1),
                ((left, right), -1),
            ):
                result[pair] += sign * weight
    return {pair: value for pair, value in result.items() if value}


def lambda_audit(epoch: int) -> dict[str, object]:
    direct = direct_lambda_map(epoch)
    formula = {
        (left, right): lambda_formula(epoch, left, right)
        for left in range(epoch - 1, 2 * epoch)
        for right in range(left + 1, 2 * epoch)
        if lambda_formula(epoch, left, right)
    }
    if direct != formula:
        raise CertificateError("lambda expansion/formula mismatch")
    full_span = (epoch - 1, 2 * epoch - 1)
    expected_full = F((epoch - 1) ** 2, 4 * epoch * epoch)
    if direct.get(full_span) != expected_full:
        raise CertificateError("unexpected full-span boundary coefficient")
    remaining_positive = [value for pair, value in direct.items() if pair != full_span and value > 0]
    if max(remaining_positive) != F(1, epoch * epoch):
        raise CertificateError("sharp remaining positive lambda changed")
    ledger = ";".join(f"{left},{right}:{value}" for (left, right), value in sorted(direct.items()))
    return {
        "epoch": epoch,
        "nonzero_coefficients": len(direct),
        "positive_coefficients": sum(value > 0 for value in direct.values()),
        "negative_coefficients": sum(value < 0 for value in direct.values()),
        "full_span_pair": list(full_span),
        "full_span_coefficient": ftext(expected_full),
        "maximum_other_positive": ftext(max(remaining_positive)),
        "sharp_bound": ftext(F(1, epoch * epoch)),
        "ledger_sha256": hashlib.sha256(ledger.encode("ascii")).hexdigest(),
    }


def finite_horizon_potential(distance: int, horizon: int) -> FormalIntegral:
    """Formal F_H(d)=integral_0^H R_T(d)dT."""
    if distance < 1 or horizon < 1:
        raise ValueError("distance and horizon must be positive")
    if distance >= horizon:
        return FormalIntegral(())
    return FormalIntegral.from_parts(
        ((horizon, 1), (distance, -1)),
        F(distance, horizon) - 1,
    )


def symbolic_lambda_moments(epoch: int) -> tuple[F, tuple[F, ...]]:
    """Return sum lambda and every gap coefficient in sum lambda*(a_q-a_p)."""
    coefficients = direct_lambda_map(epoch)
    total = sum(coefficients.values(), F(0))
    gap_loads = []
    for gap_index in range(epoch, 2 * epoch):
        # a_q-a_p contains h_r=a_r-a_(r-1) iff p<r<=q.
        gap_loads.append(sum(
            (value for (point_left, point_right), value in coefficients.items()
             if point_left < gap_index <= point_right),
            F(0),
        ))
    return total, tuple(gap_loads)


def superincreasing_points(count: int) -> tuple[int, ...]:
    return tuple((1 << index) - 1 for index in range(count))


def potential_decomposition_audit(epoch: int) -> dict[str, object]:
    coefficients = direct_lambda_map(epoch)
    lambda_sum, gap_loads = symbolic_lambda_moments(epoch)
    if lambda_sum or any(gap_loads):
        raise CertificateError("symbolic lambda constant/linear moments failed")

    full_span_pair = (epoch - 1, 2 * epoch - 1)
    positive_pairs = tuple(pair for pair, value in coefficients.items() if value > 0)
    other_positive = tuple(pair for pair in positive_pairs if pair != full_span_pair)
    # In Gothic D_(p,q)=a_q-a_(p-1), point_left=p-1.  Thus
    # point_left>=n is exactly the requested strict-interior source p>n.
    if not all(point_left >= epoch and point_right < 2 * epoch - 1 for point_left, point_right in other_positive):
        raise CertificateError("remaining positive lambda is not strict Gothic interior")
    terminal_rows = tuple(
        ((point_left, point_right), value)
        for (point_left, point_right), value in coefficients.items()
        if point_right == 2 * epoch - 1 and (point_left, point_right) != full_span_pair
    )
    if not terminal_rows or not all(value <= 0 for _, value in terminal_rows):
        raise CertificateError("non-full-span terminal lambda must be nonpositive")

    marks = superincreasing_points(2 * epoch)
    if not is_golomb(marks):
        raise CertificateError("superincreasing potential fixture is not Golomb")
    horizon = marks[-1] - marks[epoch - 1]
    full_span_value = finite_horizon_potential(horizon, horizon)
    if full_span_value != FormalIntegral(()) or full_span_value.constant:
        raise CertificateError("F_H(H) must vanish exactly")
    potential = FormalIntegral(())
    for (point_left, point_right), coefficient in coefficients.items():
        distance = marks[point_right] - marks[point_left]
        potential = potential + finite_horizon_potential(distance, horizon).scale(coefficient)
    expected = FormalIntegral.from_parts(formal_w_map(marks, epoch))
    if potential != expected or potential.constant:
        raise CertificateError("finite-horizon potential/W formal identity failed")

    gap_ledger = ";".join(f"{index}:{value}" for index, value in enumerate(gap_loads, start=epoch))
    terminal_ledger = ";".join(f"{left},{right}:{value}" for (left, right), value in terminal_rows)
    return {
        "epoch": epoch,
        "lambda_sum": ftext(lambda_sum),
        "symbolic_gap_load_count": len(gap_loads),
        "all_symbolic_gap_loads_zero": all(not value for value in gap_loads),
        "gap_load_ledger_sha256": hashlib.sha256(gap_ledger.encode("ascii")).hexdigest(),
        "full_span_Gothic_atom": [epoch, 2 * epoch - 1],
        "F_H_of_H": {"logs": [], "constant": "0"},
        "other_positive_count": len(other_positive),
        "other_positive_strict_Gothic_interior": True,
        "terminal_nonfull_count": len(terminal_rows),
        "terminal_nonfull_all_nonpositive": True,
        "terminal_ledger_sha256": hashlib.sha256(terminal_ledger.encode("ascii")).hexdigest(),
        "concrete_horizon": horizon,
        "potential_rational_constant": ftext(potential.constant),
        "potential_log_digest": formal_digest(potential.logs),
        "W_log_digest": formal_digest(expected.logs),
    }


def is_golomb(points: Sequence[int]) -> bool:
    marks = tuple(points)
    differences = [marks[right] - marks[left] for right in range(1, len(marks)) for left in range(right)]
    return marks and marks[0] == 0 and all(a < b for a, b in zip(marks, marks[1:])) and len(differences) == len(set(differences))


def psi_for_marks(points: Sequence[int], width: int, left: int, right: int) -> F:
    marks = tuple(points)
    return psi(width, marks[right - 1] - marks[left], marks[left] - marks[left - 1], marks[right] - marks[right - 1])


def psi_wave(points: Sequence[int], epoch: int, width: int) -> F:
    return sum(
        (w_atom_coefficient(epoch, left, right) * psi_for_marks(points, width, left, right)
         for right in range(epoch + 2, 2 * epoch) for left in range(epoch, right - 1)),
        F(0),
    )


def centered_suffix_capacity(points: Sequence[int], epoch: int, width: int) -> F:
    marks = tuple(points)
    return 2 * sum(
        (r_box(width, marks[right] - marks[left])
         for left in range(epoch - 1, 2 * epoch) for right in range(left + 1, 2 * epoch)),
        F(0),
    )


def expanded_wave(points: Sequence[int], epoch: int, width: int) -> F:
    marks = tuple(points)
    return sum(
        (coefficient * r_box(width, marks[right] - marks[left])
         for (left, right), coefficient in direct_lambda_map(epoch).items()),
        F(0),
    )


def pointwise_map_check(points: Sequence[int], epoch: int, width: int) -> dict[str, object]:
    marks = tuple(points[: 2 * epoch])
    if len(marks) != 2 * epoch or not is_golomb(marks):
        raise CertificateError("pointwise fixture must be a 2n-mark Golomb ruler")
    value = psi_wave(marks, epoch, width)
    expanded = expanded_wave(marks, epoch, width)
    capacity = centered_suffix_capacity(marks, epoch, width)
    if value != expanded:
        raise CertificateError("dipole/lambda expansion failed on fixture")
    full_span = marks[-1] - marks[epoch - 1]
    if width <= full_span and r_box(width, full_span) != 0:
        raise CertificateError("full-span positive term did not vanish")
    if width >= full_span and value != 0:
        raise CertificateError("Psi must vanish after the full span")
    upper = capacity * F(1, 2 * epoch * epoch)
    if value < 0 or value > upper:
        raise CertificateError("sharpened pointwise capacity map failed")
    return {
        "epoch": epoch,
        "T": width,
        "Psi": ftext(value),
        "Delta_suffix": ftext(capacity),
        "upper": ftext(upper),
        "full_span": full_span,
    }


def lowpass_centered(points: Sequence[int], width: int) -> F:
    marks = tuple(points)
    return 2 * sum(
        (r_box(width, marks[right] - marks[left]) for right in range(1, len(marks)) for left in range(right)),
        F(0),
    )


def ceil_power_two(value: F) -> int:
    answer = 1
    while F(answer) < value:
        answer *= 2
    return answer


def scheduled_width(points: Sequence[int]) -> int:
    count = len(points)
    ambient = points[-1] + 1
    return count * ceil_power_two(F(8 * ambient, count * count))


def formal_w_map(points: Sequence[int], epoch: int) -> tuple[tuple[int, F], ...]:
    marks = tuple(points)
    combined: defaultdict[int, F] = defaultdict(F)
    for right in range(epoch + 2, 2 * epoch):
        for left in range(epoch, right - 1):
            weight = w_atom_coefficient(epoch, left, right)
            bases = (
                (marks[right - 1] - marks[left - 1], 1),
                (marks[right] - marks[left], 1),
                (marks[right - 1] - marks[left], -1),
                (marks[right] - marks[left - 1], -1),
            )
            for base, sign in bases:
                combined[base] += sign * weight
    return tuple((base, value) for base, value in sorted(combined.items()) if base != 1 and value)


def formal_digest(form: Sequence[tuple[int, F]]) -> str:
    text = ";".join(f"{base}:{value.numerator}/{value.denominator}" for base, value in form)
    return hashlib.sha256(text.encode("ascii")).hexdigest()


def hall_no_go(epoch: int) -> dict[str, object]:
    marks = HALL_64[: 2 * epoch]
    if not is_golomb(marks):
        raise CertificateError("Hall prefix is not Golomb")
    width = scheduled_width(marks)
    old = marks[:epoch]
    records = {}
    for multiplier in (2, 4):
        full_band = lowpass_centered(marks, width) - lowpass_centered(marks, multiplier * width)
        old_band = lowpass_centered(old, width) - lowpass_centered(old, multiplier * width)
        records[str(multiplier)] = ftext(full_band - old_band)
    all_arguments_above_one = all(
        F(
            (marks[right - 1] - marks[left - 1]) * (marks[right] - marks[left]),
            (marks[right - 1] - marks[left]) * (marks[right] - marks[left - 1]),
        ) > 1
        for right in range(epoch + 2, 2 * epoch) for left in range(epoch, right - 1)
    )
    return {
        "epoch": epoch,
        "N": marks[-1] + 1,
        "T": width,
        "X_first_use": records,
        "W_atom_count": (epoch - 1) * (epoch - 2) // 2,
        "W_form_sha256": formal_digest(formal_w_map(marks, epoch)),
        "all_cross_ratios_above_one": all_arguments_above_one,
    }


def dyadic_sum_atom(middle: int, left_gap: int, right_gap: int) -> F:
    terminal = middle + left_gap + right_gap
    width = 1
    total = F(0)
    while width <= terminal:
        total += width * psi(width, middle, left_gap, right_gap)
        width *= 2
    return total


def dyadic_no_go() -> dict[str, object]:
    lower = (4, 1, 2)
    lower_sum = dyadic_sum_atom(*lower)
    if lower_sum != 0:
        raise CertificateError("dyadic lower no-go fixture changed")
    upper_rows = []
    for exponent in range(3, 21):
        width = 1 << exponent
        middle, left_gap, right_gap = width - 1, 1, 2
        total = dyadic_sum_atom(middle, left_gap, right_gap)
        denominator = (width - 1) * (width + 2)
        ratio_lower = F(denominator, 2 * width)  # log(1+2/D)<=2/D.
        if total != F(1, width):
            raise CertificateError("dyadic upper no-go family changed")
        upper_rows.append({"exponent": exponent, "T": width, "sum": ftext(total), "S_over_log_lower": ftext(ratio_lower)})
    return {
        "lower_constant_no_go": {
            "middle_left_right": list(lower),
            "local_golomb_points": [0, 1, 5, 7],
            "cross_ratio": "15/14",
            "dyadic_sum": ftext(lower_sum),
        },
        "upper_constant_no_go_family": {
            "exponent_range": [3, 20],
            "count": len(upper_rows),
            "first": upper_rows[0],
            "last": upper_rows[-1],
            "ledger_sha256": hashlib.sha256(
                ";".join(f"{row['exponent']}:{row['sum']}:{row['S_over_log_lower']}" for row in upper_rows).encode("ascii")
            ).hexdigest(),
        },
        "proof": "for M=2^r-1,h=1,k=2: S=2^-r and log(CR)<=2/((2^r-1)(2^r+2)), so S/log(CR)>=(T^2+T-2)/(2T)->infinity",
    }


def build_body() -> dict[str, object]:
    # Independent tent/sign/factor exhaustion.
    tent_checks = 0
    for middle in range(1, 13):
        for left_gap in range(1, 9):
            for right_gap in range(1, 9):
                for width in range(1, middle + left_gap + right_gap + 3):
                    value = psi(width, middle, left_gap, right_gap)
                    if value != psi_piecewise(width, middle, left_gap, right_gap) or value < 0:
                        raise CertificateError("psi tent/sign check failed")
                    if value != -edge_inner_product(width, middle, left_gap, right_gap):
                        raise CertificateError("psi dipole factor/sign failed")
                    tent_checks += 1
                integral_psi_form(middle, left_gap, right_gap)
    lambda_rows = [lambda_audit(epoch) for epoch in EPOCHS]
    potential_rows = [potential_decomposition_audit(epoch) for epoch in EPOCHS]
    fixtures = (
        (MINIMAL_EIGHT, 4),
        (tuple(100 * index + index * index for index in range(10)), 5),
        (HALL_64[:16], 8),
    )
    pointwise_rows = []
    for marks, epoch in fixtures:
        full_span = marks[-1] - marks[epoch - 1]
        for width in range(1, full_span + 3):
            pointwise_rows.append(pointwise_map_check(marks, epoch, width))
    minimal_width = scheduled_width(MINIMAL_EIGHT)
    minimal_psi = psi_wave(MINIMAL_EIGHT, 4, minimal_width)
    if minimal_width != 64 or minimal_psi != 0:
        raise CertificateError("minimal scheduled-density no-go changed")
    hall8 = hall_no_go(8)
    hall32 = hall_no_go(32)
    if hall8["X_first_use"]["2"] != "-5105/524288":
        raise CertificateError("Hall n=8 negative X changed")
    if hall32["X_first_use"] != {"2": "-383937/33554432", "4": "-2351661/134217728"}:
        raise CertificateError("Hall n=32 negative X changed")
    phase_rows = [phase_partition_audit(*row) for row in ((4, 1, 2), (7, 3, 5), (31, 1, 2), (20, 9, 4))]
    return {
        "schema": "erdos1191.cross_ratio_box_dipole.v1",
        "status": STATUS,
        "scope": {
            "continuous_scale_identity": True,
            "pointwise_capacity_map": True,
            "fixed_scheduled_scale_recovers_W": False,
            "unshifted_dyadic_quadrature_equivalent_to_W": False,
            "common_signed_history_coupling": False,
            "q1_resolved": False,
            "q2_resolved": False,
            "publication_ready": False,
            "prize_claim_ready": False,
            "novelty_claim": False,
        },
        "psi": {
            "formula": "R_T(M)+R_T(M+h+k)-R_T(M+h)-R_T(M+k)=-<e_i*K_T,e_j*K_T>",
            "tent": "0,(T-M)/T^2,min(h,k)/T^2,(M+h+k-T)/T^2,0",
            "support": "M<T<M+h+k",
            "exact_tent_sign_factor_checks": tent_checks,
        },
        "continuous_integral": {
            "identity": "integral_0^infinity psi_T dT=log((M+h)(M+k)/(M(M+h+k)))",
            "formal_exponent_map": {"M+h": 1, "M+k": 1, "M": -1, "M+h+k": -1},
            "rational_constant": "0",
            "Wave19_identity": "integral Psi_(n,T) dT=W_n",
        },
        "lambda_audits": lambda_rows,
        "finite_horizon_potential": {
            "definition": "F_H(d)=0 for d>=H; for 0<d<H, F_H(d)=log(H/d)+d/H-1",
            "moment_cancellation": "in Gothic indexing p<=q: sum lambda=0 and sum lambda*D_(p,q)=sum lambda*(a_q-a_(p-1))=0 as an exact linear form in h_n,...,h_(2n-1)",
            "identity": "in Gothic indexing p<=q: W_n=sum lambda_(p,q)F_H(D_(p,q))=-sum lambda_(p,q)log D_(p,q), H=D_(n,2n-1)",
            "ownership": "F_H(H)=0 on D_(n,2n-1); every other positive lambda has Gothic p>n,q<2n-1; terminal q=2n-1 is otherwise nonpositive",
            "epoch_audits": potential_rows,
            "nonclaim": "This terminal localization does not authorize reuse of Gothic atoms and does not close C058.",
        },
        "pointwise_map": {
            "identity": "Psi=sum lambda_(p,q)R_T(a_q-a_p)",
            "full_span_rule": "if T<=H then R_T(H)=0; if T>=H then every psi atom is zero",
            "bound": "0<=Psi_(n,T)<=Delta_suffix(n,T)/(2n^2), Delta_suffix=2 sum_(n-1<=p<q<=2n-1)R_T(a_q-a_p)",
            "fixture_rows": len(pointwise_rows),
            "fixture_digest": hashlib.sha256(";".join(f"{row['epoch']},{row['T']}:{row['Psi']}:{row['upper']}" for row in pointwise_rows).encode("ascii")).hexdigest(),
        },
        "scheduled_scale_no_go": {
            "ruler": list(MINIMAL_EIGHT),
            "epoch": 4,
            "T": minimal_width,
            "Psi": ftext(minimal_psi),
            "Delta_suffix": ftext(centered_suffix_capacity(MINIMAL_EIGHT, 4, minimal_width)),
            "cross_ratios": ["221/161", "437/425", "102/95"],
            "interpretation": "W>0 but the scheduled point density is zero",
        },
        "dyadic_quadrature_no_go": dyadic_no_go(),
        "log_phase_average": {
            "theorem": "integral_0^1 sum_r 2^(r+u)Psi_(2^(r+u))du=W_n/log(2)",
            "change_of_variables": "T=2^(r+u), dT=log(2)Tdu; dyadic intervals partition (0,infinity)",
            "finite_partition_reindex_checks": phase_rows,
        },
        "ordinary_X_no_go": {"Hall_n8": hall8, "Hall_n32": hall32},
        "open_obligation": "A continuum/global log-phase carrier must still be put in one finite signed capacity/history ledger with the Wave-19 atoms; no fixed finite phase grid has been justified.",
    }


_EXPECTED: dict[str, object] | None = None


def build_certificate() -> dict[str, object]:
    body = build_body()
    body["payload_sha256"] = hashlib.sha256(canonical_bytes(body)).hexdigest()
    return body


def expected_certificate() -> dict[str, object]:
    global _EXPECTED
    if _EXPECTED is None:
        _EXPECTED = build_certificate()
    return copy.deepcopy(_EXPECTED)


def rehash(value: dict[str, object]) -> None:
    value.pop("payload_sha256", None)
    value["payload_sha256"] = hashlib.sha256(canonical_bytes(value)).hexdigest()


def validate_certificate(value: dict[str, object]) -> None:
    body = dict(value)
    supplied = body.pop("payload_sha256", None)
    if supplied != hashlib.sha256(canonical_bytes(body)).hexdigest():
        raise CertificateError("payload hash mismatch")
    if value != expected_certificate():
        raise CertificateError("semantic replay mismatch")


def self_check(value: dict[str, object]) -> int:
    validate_certificate(value)
    mutations = (
        (("scope", "q1_resolved"), True),
        (("scope", "common_signed_history_coupling"), True),
        (("psi", "support"), "all T"),
        (("continuous_integral", "rational_constant"), "1"),
        (("finite_horizon_potential", "ownership"), "terminal reusable"),
        (("pointwise_map", "bound"), "Psi<=0"),
        (("scheduled_scale_no_go", "Psi"), "1"),
        (("dyadic_quadrature_no_go", "lower_constant_no_go", "dyadic_sum"), "1"),
        (("log_phase_average", "theorem"), "false"),
        (("ordinary_X_no_go", "Hall_n8", "X_first_use", "2"), "1"),
        (("open_obligation",), "closed"),
    )
    for path, replacement in mutations:
        changed = copy.deepcopy(value)
        cursor = changed
        for key in path[:-1]:
            cursor = cursor[key]
        cursor[path[-1]] = replacement
        rehash(changed)
        try:
            validate_certificate(changed)
        except CertificateError:
            pass
        else:
            raise AssertionError(f"mutation accepted: {path}")
    bad_hash = copy.deepcopy(value)
    bad_hash["payload_sha256"] = "0" * 64
    try:
        validate_certificate(bad_hash)
    except CertificateError:
        pass
    else:
        raise AssertionError("hash mutation accepted")
    return len(mutations) + 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args(argv)
    if args.verify:
        value = json.loads(args.verify.read_text(encoding="utf-8"))
        validate_certificate(value)
        if args.verify.read_bytes() != rendered_bytes(value):
            raise CertificateError("certificate is not byte-canonical")
        print(f"certificate verify: PASS {value['payload_sha256']}")
    else:
        value = build_certificate()
        print(rendered_bytes(value).decode(), end="")
    if args.self_check:
        print(f"self-check: PASS ({self_check(value)} mutations rejected)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
