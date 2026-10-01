#!/usr/bin/env python3
"""Exact finite retained-covariance probe for two uniform box kernels.

The probe concerns finite Golomb rulers only.  It does not prove a compatible
infinite-history theorem and makes no Question 1 or Question 2 claim.
Floating point is used only to discover a dual active set.  Every accepted
boundary cover is reconstructed and checked with ``Fraction`` arithmetic.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
import itertools
import json
from math import gcd
from pathlib import Path
from typing import Iterable, Sequence


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "retained_covariance_box_certificate.json"
MAX_SPAN = 12
MARK_COUNTS = (2, 3, 4, 5)
T_VALUES = (1, 2, 3, 4)
THETA_VALUES = (F(1, 16), F(1, 8), F(3, 16))
COVER_KINDS = ("simple_gamma", "D_optimal", "H_optimal")
EXPECTED_RULER_COUNTS = {2: 1, 3: 44, 4: 112, 5: 18}
STATUS = "FINITE_ONLY_NO_Q1_Q2_OR_COMPATIBLE_HISTORY_CLAIM"


class CertificateError(ValueError):
    pass


def canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def rendered_bytes(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()


def fraction_text(value: F) -> str:
    return str(value)


def dot(left: Sequence[F], right: Sequence[F]) -> F:
    return sum((x * y for x, y in zip(left, right)), F(0))


def matvec(matrix: Sequence[Sequence[F]], vector: Sequence[F]) -> list[F]:
    return [dot(row, vector) for row in matrix]


def transpose(matrix: Sequence[Sequence[F]]) -> list[list[F]]:
    return [list(row) for row in zip(*matrix)]


def solve_linear(matrix: Sequence[Sequence[F]], rhs: Sequence[F]) -> list[F]:
    size = len(matrix)
    if size == 0:
        return []
    work = [list(row) + [value] for row, value in zip(matrix, rhs)]
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        if pivot is None:
            raise CertificateError("singular exact active-set system")
        work[column], work[pivot] = work[pivot], work[column]
        pivot_value = work[column][column]
        work[column] = [value / pivot_value for value in work[column]]
        for row in range(size):
            if row == column or not work[row][column]:
                continue
            scale = work[row][column]
            work[row] = [x - scale * y for x, y in zip(work[row], work[column])]
    return [work[row][-1] for row in range(size)]


def solve_linear_float(
    matrix: Sequence[Sequence[float]], rhs: Sequence[float], tolerance: float = 1e-12
) -> list[float]:
    size = len(matrix)
    work = [list(row) + [value] for row, value in zip(matrix, rhs)]
    for column in range(size):
        pivot = max(range(column, size), key=lambda row: abs(work[row][column]))
        if abs(work[pivot][column]) <= tolerance:
            raise CertificateError("singular floating active-set system")
        work[column], work[pivot] = work[pivot], work[column]
        pivot_value = work[column][column]
        for row in range(column + 1, size):
            scale = work[row][column] / pivot_value
            for index in range(column, size + 1):
                work[row][index] -= scale * work[column][index]
    answer = [0.0] * size
    for row in range(size - 1, -1, -1):
        tail = sum(work[row][column] * answer[column] for column in range(row + 1, size))
        answer[row] = (work[row][-1] - tail) / work[row][row]
    return answer


def apply_blocks(block: Sequence[Sequence[F]], vector: Sequence[F], count: int) -> list[F]:
    result: list[F] = []
    for index in range(count):
        result.extend(matvec(block, vector[2 * index : 2 * index + 2]))
    return result


def box_kernel(width: int) -> tuple[F, ...]:
    if width < 1:
        raise ValueError("box width must be positive")
    return tuple(F(1, width) for _ in range(width))


def haar_kernel(width: int, shift: int | None = None) -> tuple[F, ...]:
    """Return K_T-K_2T; ``shift`` is exposed for adversarial tests."""
    if width < 1:
        raise ValueError("Haar width must be positive")
    actual_shift = width if shift is None else shift
    if actual_shift != width:
        raise CertificateError("dyadic split must use translation by exactly T")
    return tuple([F(1, 2 * width)] * width + [F(-1, 2 * width)] * width)


def correlation(kernel: Sequence[F], shift: int) -> F:
    if shift < 0:
        shift = -shift
    if shift >= len(kernel):
        return F(0)
    return sum((kernel[index] * kernel[index + shift] for index in range(len(kernel) - shift)), F(0))


def box_correlation(width: int, shift: int) -> F:
    shift = abs(shift)
    return F(width - shift, width * width) if shift < width else F(0)


def haar_correlation_formula(width: int, shift: int) -> F:
    shift = abs(shift)
    if shift <= width:
        return F(2 * width - 3 * shift, 4 * width * width)
    if shift < 2 * width:
        return F(shift - 2 * width, 4 * width * width)
    return F(0)


def convolve_indicator(ruler: Sequence[int], kernel: Sequence[F]) -> tuple[F, ...]:
    if not ruler:
        return ()
    result = [F(0)] * (ruler[-1] + len(kernel))
    for mark in ruler:
        for offset, value in enumerate(kernel):
            result[mark + offset] += value
    return tuple(result)


def squared_norm(vector: Sequence[F]) -> F:
    return dot(vector, vector)


def pad(vector: Sequence[F], length: int) -> tuple[F, ...]:
    return tuple(vector) + (F(0),) * (length - len(vector))


def covariance_v_direct(ruler: Sequence[int], width: int) -> F:
    first = convolve_indicator(ruler, box_kernel(width))
    second = convolve_indicator(ruler, box_kernel(2 * width))
    length = max(len(first), len(second))
    return squared_norm(tuple(x - y for x, y in zip(pad(first, length), pad(second, length))))


def positive_differences(ruler: Sequence[int]) -> tuple[int, ...]:
    return tuple(ruler[right] - ruler[left] for left in range(len(ruler)) for right in range(left + 1, len(ruler)))


def covariance_v_formula(ruler: Sequence[int], width: int) -> F:
    return len(ruler) * haar_correlation_formula(width, 0) + 2 * sum(
        (haar_correlation_formula(width, difference) for difference in positive_differences(ruler)), F(0)
    )


def verify_dyadic_box_identity(ruler: Sequence[int], width: int) -> F:
    narrow = convolve_indicator(ruler, box_kernel(width))
    wide = convolve_indicator(ruler, box_kernel(2 * width))
    length = max(len(narrow), len(wide))
    narrow_norm = squared_norm(pad(narrow, length))
    wide_norm = squared_norm(pad(wide, length))
    value = covariance_v_direct(ruler, width)
    if narrow_norm != wide_norm + value:
        raise CertificateError("dyadic box/Haar energy identity failed")
    if value != covariance_v_formula(ruler, width):
        raise CertificateError("Haar correlation formula failed")
    return value


def centered_covariance(ruler: Sequence[int], width: int) -> F:
    """Remove the diagonal Parseval contribution from V_T."""
    return verify_dyadic_box_identity(ruler, width) - F(len(ruler), 2 * width)


def negative_haar_budget(width: int) -> F:
    return sum((min(F(0), haar_correlation_formula(width, shift)) for shift in range(1, 2 * width)), F(0))


def golomb_covariance_lower_bound(mark_count: int, width: int) -> F:
    """Worst legal negative-lag fill when each positive difference occurs once."""
    return F(mark_count, 2 * width) + 2 * negative_haar_budget(width)


def lag_wavelet_partial_sum(shift: int, max_power: int) -> F:
    if shift <= 0:
        raise ValueError("lag must be positive")
    total = sum((haar_correlation_formula(1 << power, shift) for power in range(max_power + 1)), F(0))
    terminal_width = 1 << (max_power + 1)
    expected = -F(max(terminal_width - shift, 0), terminal_width * terminal_width)
    if total != expected:
        raise CertificateError("per-lag centered wavelet identity failed")
    return total


def telescoping_profile(ruler: Sequence[int], max_power: int = 3) -> dict[str, object]:
    values = [verify_dyadic_box_identity(ruler, 1 << power) for power in range(max_power + 1)]
    centered = [value - F(len(ruler), 2 * (1 << power)) for power, value in enumerate(values)]
    tail_width = 1 << (max_power + 1)
    tail = squared_norm(convolve_indicator(ruler, box_kernel(tail_width)))
    if sum(values, F(0)) + tail != F(len(ruler)):
        raise CertificateError("finite dyadic telescoping identity failed")
    centered_sum = sum(centered, F(0))
    centered_rhs = F(len(ruler), tail_width) - tail
    difference_rhs = -2 * sum(
        (F(tail_width - difference, tail_width * tail_width)
         for difference in positive_differences(ruler) if difference < tail_width),
        F(0),
    )
    if centered_sum != centered_rhs or centered_sum != difference_rhs or centered_sum > 0:
        raise CertificateError("centered off-diagonal telescope failed")
    for difference in set(positive_differences(ruler)):
        lag_wavelet_partial_sum(difference, max_power)
    return {
        "widths": [1 << power for power in range(max_power + 1)],
        "V": [fraction_text(value) for value in values],
        "O": [fraction_text(value) for value in centered],
        "tail_width": tail_width,
        "tail_energy": fraction_text(tail),
        "partial_plus_tail": fraction_text(sum(values, F(0)) + tail),
        "centered_partial_sum": fraction_text(centered_sum),
        "centered_terminal_identity": fraction_text(centered_rhs),
    }


def prefix_scale_ownership(ruler: Sequence[int], max_power: int = 3) -> dict[str, object]:
    """Exact two-dimensional prefix/scale Abel ownership table."""
    prefixes = [tuple(ruler[:count]) for count in range(1, len(ruler) + 1)]
    v_rows = [[verify_dyadic_box_identity(prefix, 1 << power) for power in range(max_power + 1)] for prefix in prefixes]
    o_rows = [[value - F(len(prefix), 2 * (1 << power)) for power, value in enumerate(row)] for prefix, row in zip(prefixes, v_rows)]

    def prefix_differences(rows: Sequence[Sequence[F]]) -> list[list[F]]:
        zero = [F(0)] * (max_power + 1)
        previous = zero
        result = []
        for row in rows:
            result.append([value - old for value, old in zip(row, previous)])
            previous = list(row)
        return result

    omega_v = prefix_differences(v_rows)
    omega_o = prefix_differences(o_rows)
    terminal_width = 1 << (max_power + 1)
    terminal_energies = [squared_norm(convolve_indicator(prefix, box_kernel(terminal_width))) for prefix in prefixes]
    previous_tail = F(0)
    owner_checks = []
    for index, (row_v, row_o, tail) in enumerate(zip(omega_v, omega_o, terminal_energies), start=1):
        tail_increment = tail - previous_tail
        if sum(row_v, F(0)) + tail_increment != 1:
            raise CertificateError("full-V prefix owner does not own unit mass")
        if sum(row_o, F(0)) != F(1, terminal_width) - tail_increment:
            raise CertificateError("centered prefix owner identity failed")
        owner_checks.append(
            {
                "new_mark": ruler[index - 1],
                "sum_Omega_V": fraction_text(sum(row_v, F(0))),
                "terminal_energy_increment": fraction_text(tail_increment),
                "unit_owner_total": "1",
                "sum_Omega_O": fraction_text(sum(row_o, F(0))),
            }
        )
        previous_tail = tail

    # Prefix Abel/Fubini check for a deterministic rational two-dimensional weight.
    weights = [[F((j + 1) * (power + 2) + 1, (j + 2) * (power + 3)) for power in range(max_power + 1)] for j in range(len(prefixes))]
    lhs_v = sum((weights[j][r] * v_rows[j][r] for j in range(len(prefixes)) for r in range(max_power + 1)), F(0))
    rhs_v = sum(
        (omega_v[i][r] * sum((weights[j][r] for j in range(i, len(prefixes))), F(0))
         for i in range(len(prefixes)) for r in range(max_power + 1)),
        F(0),
    )
    lhs_o = sum((weights[j][r] * o_rows[j][r] for j in range(len(prefixes)) for r in range(max_power + 1)), F(0))
    rhs_o = sum(
        (omega_o[i][r] * sum((weights[j][r] for j in range(i, len(prefixes))), F(0))
         for i in range(len(prefixes)) for r in range(max_power + 1)),
        F(0),
    )
    if lhs_v != rhs_v or lhs_o != rhs_o:
        raise CertificateError("two-dimensional prefix Abel identity failed")
    return {
        "widths": [1 << power for power in range(max_power + 1)],
        "Omega_V": [[fraction_text(value) for value in row] for row in omega_v],
        "Omega_O": [[fraction_text(value) for value in row] for row in omega_o],
        "owner_checks": owner_checks,
        "weighted_Abel_V": fraction_text(lhs_v),
        "weighted_Abel_O": fraction_text(lhs_o),
    }


def is_golomb(ruler: Sequence[int]) -> bool:
    differences = positive_differences(ruler)
    return len(differences) == len(set(differences))


def normalized_golomb_rulers(max_span: int = MAX_SPAN) -> tuple[tuple[int, ...], ...]:
    rulers: list[tuple[int, ...]] = []
    for mark_count in MARK_COUNTS:
        for positive_marks in itertools.combinations(range(1, max_span + 1), mark_count - 1):
            ruler = (0,) + positive_marks
            if gcd(*positive_marks) == 1 and is_golomb(ruler):
                rulers.append(ruler)
    return tuple(rulers)


def covariance_matrix(theta: F) -> tuple[tuple[F, F], tuple[F, F]]:
    if not F(0) <= theta < F(1, 4):
        raise CertificateError("H_theta is not positive definite")
    return ((F(1, 2) - theta, theta), (theta, F(1, 2) - theta))


def boundary_matrix(ambient_length: int, width: int) -> tuple[list[list[F]], int]:
    if ambient_length < 1 or width < 1:
        raise ValueError("ambient length and width must be positive")
    site_count = ambient_length + 2 * width - 1
    variable_count = 2 * site_count
    cover = [[F(0) for _ in range(variable_count)] for _ in range(ambient_length)]
    for mark in range(ambient_length):
        for offset in range(width):
            cover[mark][2 * (mark + offset)] += F(1, width)
        for offset in range(2 * width):
            cover[mark][2 * (mark + offset) + 1] += F(1, 2 * width)
    if max(index for row in cover for index, value in enumerate(row) if value) != variable_count - 1:
        raise CertificateError("right convolution endpoint is missing")
    return cover, site_count


def simple_gamma_cover(ambient_length: int, width: int) -> tuple[F, ...]:
    _, site_count = boundary_matrix(ambient_length, width)
    return tuple(F(1, 2) for _ in range(2 * site_count))


def cover_values(cover: Sequence[Sequence[F]], weights: Sequence[F]) -> tuple[F, ...]:
    return tuple(matvec(cover, weights))


def gram_matrix(cover: Sequence[Sequence[F]], covariance: Sequence[Sequence[F]], site_count: int) -> list[list[F]]:
    transformed = [apply_blocks(covariance, row, site_count) for row in cover]
    return [[dot(left, right) for right in transformed] for left in cover]


def discover_active_set(gram: Sequence[Sequence[F]]) -> tuple[int, ...]:
    constraint_count = len(gram)
    float_gram = [[float(value) for value in row] for row in gram]
    target = [2.0] * constraint_count
    dual = [0.0] * constraint_count
    passive: list[int] = []
    tolerance = 1e-10
    for _ in range(20 * constraint_count * constraint_count + 1):
        residual = [
            target[row] - sum(float_gram[row][column] * dual[column] for column in range(constraint_count))
            for row in range(constraint_count)
        ]
        entering = [row for row in range(constraint_count) if row not in passive and residual[row] > tolerance]
        if not entering:
            return tuple(passive)
        chosen = min(entering, key=lambda row: (-residual[row], row))
        passive.append(chosen)
        passive.sort()
        while True:
            submatrix = [[float_gram[row][column] for column in passive] for row in passive]
            candidate_values = solve_linear_float(submatrix, [2.0] * len(passive))
            if all(value > tolerance for value in candidate_values):
                dual = [0.0] * constraint_count
                for row, value in zip(passive, candidate_values):
                    dual[row] = value
                break
            candidate = [0.0] * constraint_count
            for row, value in zip(passive, candidate_values):
                candidate[row] = value
            ratios = [
                dual[row] / (dual[row] - candidate[row])
                for row in passive
                if candidate[row] <= tolerance and dual[row] - candidate[row] > tolerance
            ]
            alpha = min(ratios, default=0.0)
            dual = [old + alpha * (new - old) for old, new in zip(dual, candidate)]
            passive = [row for row in passive if dual[row] > tolerance]
    raise CertificateError("floating active-set discovery did not converge")


def exact_qp_candidate(
    cover: Sequence[Sequence[F]], site_count: int, covariance: Sequence[Sequence[F]], active: Sequence[int]
) -> dict[str, object]:
    constraint_count = len(cover)
    selected = [cover[row] for row in active]
    if active:
        gram = gram_matrix(selected, covariance, site_count)
        dual_active = solve_linear(gram, [F(2)] * len(active))
        at_dual = [
            sum((selected[row][column] * dual_active[row] for row in range(len(active))), F(0))
            for column in range(2 * site_count)
        ]
        weights = tuple(value / 2 for value in apply_blocks(covariance, at_dual, site_count))
    else:
        dual_active = []
        weights = tuple(F(0) for _ in range(2 * site_count))
    dual = [F(0)] * constraint_count
    for row, value in zip(active, dual_active):
        dual[row] = value
    slack = tuple(value - 1 for value in cover_values(cover, weights))
    inverse = inverse_2x2(covariance)
    metric_weights = apply_blocks(inverse, weights, site_count)
    stationarity = tuple(
        2 * left - right
        for left, right in zip(metric_weights, matvec(transpose(cover), dual))
    )
    complementarity = tuple(value * gap for value, gap in zip(dual, slack))
    objective = dot(weights, metric_weights)
    transformed_at_dual = apply_blocks(covariance, matvec(transpose(cover), dual), site_count)
    dual_value = sum(dual, F(0)) - dot(dual, matvec(cover, transformed_at_dual)) / 4
    result = {
        "active": tuple(active),
        "z": weights,
        "y": tuple(dual),
        "slack": slack,
        "stationarity": stationarity,
        "complementarity": complementarity,
        "objective": objective,
        "dual_value": dual_value,
    }
    validate_qp(cover, site_count, covariance, result)
    return result


def inverse_2x2(matrix: Sequence[Sequence[F]]) -> tuple[tuple[F, F], tuple[F, F]]:
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if determinant <= 0:
        raise CertificateError("covariance matrix is not positive definite")
    return (
        (matrix[1][1] / determinant, -matrix[0][1] / determinant),
        (-matrix[1][0] / determinant, matrix[0][0] / determinant),
    )


def validate_qp(
    cover: Sequence[Sequence[F]], site_count: int, covariance: Sequence[Sequence[F]], result: dict[str, object]
) -> None:
    weights = result["z"]
    dual = result["y"]
    if not isinstance(weights, tuple) or len(weights) != 2 * site_count:
        raise CertificateError("boundary vector has wrong endpoint convention")
    if any(value < 0 for value in result["slack"]):
        raise CertificateError("cover failure")
    if any(value < 0 for value in dual):
        raise CertificateError("dual failure")
    if any(result["stationarity"]):
        raise CertificateError("stationarity failure")
    if any(result["complementarity"]):
        raise CertificateError("complementarity failure")
    if result["objective"] != result["dual_value"]:
        raise CertificateError("primal/dual mismatch")


def solve_boundary_qp(ambient_length: int, width: int, theta: F) -> dict[str, object]:
    covariance = covariance_matrix(theta)
    cover, site_count = boundary_matrix(ambient_length, width)
    gram = gram_matrix(cover, covariance, site_count)
    discovered = discover_active_set(gram)
    # Exact fallback is only for the bounded N<=13 replay scope.  Keep it lazy:
    # normally the first, float-discovered set passes the exact verifier.
    candidates = itertools.chain(
        (discovered,),
        (
            subset
            for size in range(ambient_length + 1)
            for subset in itertools.combinations(range(ambient_length), size)
            if subset != discovered
        ),
    )
    first_error: Exception | None = None
    for active in candidates:
        try:
            return exact_qp_candidate(cover, site_count, covariance, active)
        except CertificateError as error:
            first_error = first_error or error
    raise CertificateError(f"no exact KKT active set: {first_error}")


def vector_hash(vector: Sequence[F]) -> str:
    return hashlib.sha256("\n".join(str(value) for value in vector).encode()).hexdigest()


def cover_for_kind(
    ambient_length: int,
    width: int,
    theta: F,
    kind: str,
    cache: dict[tuple[object, ...], dict[str, object]],
) -> tuple[tuple[F, ...], dict[str, object] | None]:
    if kind == "simple_gamma":
        return simple_gamma_cover(ambient_length, width), None
    solve_theta = F(0) if kind == "D_optimal" else theta
    key = (kind, ambient_length, width, solve_theta)
    if key not in cache:
        cache[key] = solve_boundary_qp(ambient_length, width, solve_theta)
    result = cache[key]
    return result["z"], result


def combined_correlation(width: int, theta: F, shift: int) -> F:
    return (
        box_correlation(width, shift) / 2
        + box_correlation(2 * width, shift) / 2
        - theta * haar_correlation_formula(width, shift)
    )


def evaluate_pattern(
    ruler: Sequence[int],
    width: int,
    theta: F,
    cover_kind: str,
    cache: dict[tuple[object, ...], dict[str, object]],
) -> dict[str, object]:
    ambient_length = ruler[-1] + 1
    cover, site_count = boundary_matrix(ambient_length, width)
    weights, qp = cover_for_kind(ambient_length, width, theta, cover_kind, cache)
    if any(value < 1 for value in cover_values(cover, weights)):
        raise CertificateError("boundary cover is not feasible")
    b_d = sum((2 * weights[2 * site] ** 2 + 2 * weights[2 * site + 1] ** 2 for site in range(site_count)), F(0))
    q_value = sum((4 * (weights[2 * site] - weights[2 * site + 1]) ** 2 for site in range(site_count)), F(0))
    kappa = theta / (1 - 4 * theta)
    b_h = b_d + kappa * q_value
    covariance = verify_dyadic_box_identity(ruler, width)
    upper = F(1) + F(3 * (len(ruler) - 1), 4 * width)
    retained_upper = upper - theta * covariance
    if retained_upper <= 0:
        raise CertificateError("retained upper energy is not positive")
    gain = theta * b_d * covariance - kappa * q_value * upper + kappa * theta * q_value * covariance
    if gain != b_d * upper - b_h * retained_upper:
        raise CertificateError("same-fixed-cover G identity failed")
    if cover_kind == "simple_gamma" and (b_d != site_count or q_value != 0):
        raise CertificateError("constant gamma baseline mismatch")
    if cover_kind == "D_optimal" and qp is not None and qp["objective"] != b_d:
        raise CertificateError("D-optimal cover objective mismatch")
    if cover_kind == "H_optimal" and qp is not None and qp["objective"] != b_h:
        raise CertificateError("H-optimal cover objective mismatch")
    correlations = [combined_correlation(width, theta, shift) for shift in range(1, 2 * width)]
    result = {
        "ruler": list(ruler),
        "k": len(ruler),
        "N": ambient_length,
        "T": width,
        "theta": fraction_text(theta),
        "cover": cover_kind,
        "site_count": site_count,
        "B_D": fraction_text(b_d),
        "Q": fraction_text(q_value),
        "kappa": fraction_text(kappa),
        "B_H": fraction_text(b_h),
        "V": fraction_text(covariance),
        "U_D": fraction_text(upper),
        "U_D_minus_theta_V": fraction_text(retained_upper),
        "G": fraction_text(gain),
        "G_over_N": fraction_text(gain / ambient_length),
        "sign": "positive" if gain > 0 else "negative" if gain < 0 else "zero",
        "combined_correlation_gate": all(value >= 0 for value in correlations),
        "combined_correlation_min": fraction_text(min(correlations, default=F(0))),
        "z_sha256": vector_hash(weights),
    }
    if qp is not None:
        result.update(
            {
                "active_rows": list(qp["active"]),
                "y_sha256": vector_hash(qp["y"]),
                "slack_sha256": vector_hash(qp["slack"]),
                "exact_kkt": True,
            }
        )
    return result


def pattern_key(record: dict[str, object]) -> tuple[object, ...]:
    return (tuple(record["ruler"]), record["T"], F(record["theta"]), COVER_KINDS.index(record["cover"]))


def summarize_records(records: Iterable[dict[str, object]]) -> dict[str, object]:
    records = list(records)
    counts = {sign: sum(record["sign"] == sign for record in records) for sign in ("positive", "zero", "negative")}
    minimum = min(records, key=lambda record: (F(record["G_over_N"]), pattern_key(record)))
    maximum = min(records, key=lambda record: (-F(record["G_over_N"]), pattern_key(record)))
    return {
        "count": len(records),
        "sign_counts": counts,
        "combined_correlation_gate_pass_count": sum(bool(record["combined_correlation_gate"]) for record in records),
        "minimum_G_over_N": minimum,
        "maximum_G_over_N": maximum,
    }


def dyadic_rule_summary(
    rulers: Sequence[tuple[int, ...]], cover_kind: str, cache: dict[tuple[object, ...], dict[str, object]]
) -> dict[str, object]:
    theta = F(1, 8)
    width = 1
    chains = []
    for ruler in (value for value in rulers if len(value) == 4):
        prefixes = (ruler[:1], ruler[:2], ruler[:4])
        records = [evaluate_pattern(prefix, width, theta, cover_kind, cache) for prefix in prefixes]
        chains.append({"ruler": list(ruler), "prefix_records": records})
    all_positive = [chain for chain in chains if all(record["sign"] == "positive" for record in chain["prefix_records"])]
    failing = [chain for chain in chains if any(record["sign"] != "positive" for record in chain["prefix_records"])]
    first_failure = min(failing, key=lambda chain: tuple(chain["ruler"])) if failing else None
    stage_counts = []
    for stage, mark_count in enumerate((1, 2, 4)):
        stage_counts.append(
            {
                "k": mark_count,
                "positive": sum(chain["prefix_records"][stage]["sign"] == "positive" for chain in chains),
                "zero": sum(chain["prefix_records"][stage]["sign"] == "zero" for chain in chains),
                "negative": sum(chain["prefix_records"][stage]["sign"] == "negative" for chain in chains),
            }
        )
    return {
        "Pi": {"T": 1, "theta": "1/8", "cover_rule": cover_kind, "uses_only_current_prefix": True},
        "chain_count": len(chains),
        "all_positive_chain_count": len(all_positive),
        "failing_chain_count": len(failing),
        "stage_sign_counts": stage_counts,
        "lexicographically_first_failure": first_failure,
    }


def dyadic_t_equals_k_summary(
    rulers: Sequence[tuple[int, ...]], cache: dict[tuple[object, ...], dict[str, object]]
) -> dict[str, object]:
    theta = F(1, 8)
    chains = []
    for ruler in (value for value in rulers if len(value) == 4):
        records = []
        for mark_count in (1, 2, 4):
            prefix = ruler[:mark_count]
            record = evaluate_pattern(prefix, mark_count, theta, "simple_gamma", cache)
            if F(record["V"]) < F(1, 8) or F(record["G_over_N"]) < theta / 8:
                raise CertificateError("T=k dyadic analytic lower bound failed")
            records.append(record)
        chains.append({"ruler": list(ruler), "prefix_records": records})
    minimum = min(
        (record for chain in chains for record in chain["prefix_records"]),
        key=lambda record: (F(record["G_over_N"]), tuple(record["ruler"])),
    )
    return {
        "Pi": {"T": "current prefix cardinality k", "theta": "1/8", "cover_rule": "simple_gamma", "uses_only_current_prefix": True},
        "chain_count": len(chains),
        "all_positive_chain_count": len(chains),
        "certified_lower_bounds": {"V": "1/8", "G_over_N": "1/64"},
        "minimum_record": minimum,
    }


def energy_distribution_summary(rulers: Sequence[tuple[int, ...]]) -> dict[str, object]:
    four_mark = [ruler for ruler in rulers if len(ruler) == 4]
    stages = []
    for stage, mark_count in enumerate((1, 2, 4)):
        rows = []
        for ruler in four_mark:
            prefix = ruler[:mark_count]
            profile = telescoping_profile(prefix, 3)
            rows.append([F(value) / mark_count for value in profile["V"]])
        stages.append(
            {
                "k": mark_count,
                "scale_statistics_for_V_over_k": [
                    {
                        "T": 1 << power,
                        "minimum": fraction_text(min(row[power] for row in rows)),
                        "mean": fraction_text(sum((row[power] for row in rows), F(0)) / len(rows)),
                        "maximum": fraction_text(max(row[power] for row in rows)),
                    }
                    for power in range(4)
                ],
            }
        )
    representative = (0, 1, 3, 7)
    return {
        "identity": "sum_{r=0}^R V_{2^r}(A)+||1_A*K_{2^(R+1)}||_2^2=|A|; hence sum_{r>=0}V_{2^r}(A)=|A|",
        "compatible_chain_count": len(four_mark),
        "stages": stages,
        "representative_chain": {
            "ruler": list(representative),
            "prefixes": [
                {"k": mark_count, **telescoping_profile(representative[:mark_count], 3)}
                for mark_count in (1, 2, 4)
            ],
            "prefix_scale_ownership": prefix_scale_ownership(representative, 3),
        },
    }


def build_body() -> dict[str, object]:
    rulers = normalized_golomb_rulers()
    counts = {mark_count: sum(len(ruler) == mark_count for ruler in rulers) for mark_count in MARK_COUNTS}
    if counts != EXPECTED_RULER_COUNTS:
        raise CertificateError("ruler enumeration scope changed")
    cache: dict[tuple[object, ...], dict[str, object]] = {}
    grouped: dict[str, list[dict[str, object]]] = {kind: [] for kind in COVER_KINDS}
    for ruler in rulers:
        for width in T_VALUES:
            for theta in THETA_VALUES:
                for kind in COVER_KINDS:
                    grouped[kind].append(evaluate_pattern(ruler, width, theta, kind, cache))
    summaries = {kind: summarize_records(grouped[kind]) for kind in COVER_KINDS}
    lower_bound_checks = []
    for ruler in rulers:
        width = len(ruler)
        value = covariance_v_direct(ruler, width)
        lower = golomb_covariance_lower_bound(len(ruler), width)
        if value < lower:
            raise CertificateError("Golomb covariance lower bound failed")
        if width >= 2 and negative_haar_budget(width) < -F(3, 16):
            raise CertificateError("uniform negative Haar budget failed")
        lower_bound_checks.append((value, lower, ruler))
    tightest_value, tightest_lower, tightest_ruler = min(
        lower_bound_checks, key=lambda item: (item[0] - item[1], item[2])
    )
    return {
        "schema": "erdos1191.retained_covariance_box.v1",
        "status": STATUS,
        "scope": {
            "finite_only": True,
            "global_optimum": False,
            "compatible_history": False,
            "q1_resolved": False,
            "q2_resolved": False,
            "current_best": False,
            "novelty": False,
        },
        "convention": {
            "ruler": "A subset {0,...,N-1}, min(A)=0, max(A)=N-1",
            "K_T": "1/T on {0,...,T-1}",
            "K_2T": "1/(2T) on {0,...,2T-1}",
            "lambda": "1/2",
            "H_theta": "[[1/2-theta,theta],[theta,1/2-theta]], 0<=theta<1/4",
            "boundary_sites": "x=0,...,N+2T-2 (exactly N+2T-1 sites)",
            "cover_rows": "every ambient a=0,...,N-1",
            "comparison": "G compares H_theta and D at the same fixed z",
            "cover_kinds": {
                "simple_gamma": "z(x)=(1/2,1/2) on every boundary site",
                "D_optimal": "minimize B_D for the ambient cover, then hold that z fixed",
                "H_optimal": "minimize B_Htheta for the ambient cover, then hold that z fixed",
            },
        },
        "identities": {
            "haar_kernel": "K_T-K_2T=(delta_0-block - delta_T-block)/(2T)",
            "haar_correlation": "(2T-3d)/(4T^2) for 0<=d<=T; (d-2T)/(4T^2) for T<=d<2T; 0 after",
            "dyadic_split": "K_2T=(K_T+tau_T K_T)/2",
            "dyadic_energy": "||f*K_T||^2=||f*K_2T||^2+V_T",
            "centered_square": "O_T(A)=V_T(A)-|A|/(2T)",
            "centered_telescope": "sum_{r=0}^R O_(2^r)=|A|/M-||1_A*K_M||^2=-2 sum_{d in Delta(A),d<M}(M-d)/M^2<=0, M=2^(R+1)",
            "per_lag_telescope": "sum_{r=0}^R <h_(2^r),tau_d h_(2^r)>=-(M-d)_+/M^2",
            "golomb_lower_bound": "V_T>=|A|/(2T)+2 sum_d min(0,rho_T(d)); for T>=2 the negative sum is >=-3/16",
            "dyadic_T_equals_k": "for k=T in {1,2,4,...}, V_T>=1/8 (k=1 is direct)",
            "prefix_scale_ownership": "Omega_(j,r)=Delta_j V_(j,r); sum_r Omega_(j,r)+Delta_j terminal_energy=1, with exact prefix Abel reindexing",
            "G": "theta*B_D*V-kappa*Q*U_D+kappa*theta*Q*V",
            "kappa": "theta/(1-4theta)",
        },
        "enumeration": {
            "max_span": MAX_SPAN,
            "mark_counts": list(MARK_COUNTS),
            "primitive_gcd_one": True,
            "ruler_counts": {str(key): value for key, value in counts.items()},
            "total_rulers": len(rulers),
            "T_values": list(T_VALUES),
            "theta_values": [fraction_text(value) for value in THETA_VALUES],
            "records_per_cover": len(rulers) * len(T_VALUES) * len(THETA_VALUES),
            "exact_qp_cache_entries": len(cache),
        },
        "analytic_checks": {
            "golomb_T_equals_k_count": len(lower_bound_checks),
            "tightest_lower_bound_ruler": list(tightest_ruler),
            "tightest_V": fraction_text(tightest_value),
            "tightest_lower_bound": fraction_text(tightest_lower),
            "tightest_slack": fraction_text(tightest_value - tightest_lower),
            "negative_haar_budget_bound_for_T_at_least_2": "-3/16",
        },
        "cover_summaries": summaries,
        "dyadic_nonanticipating_rules": {
            **{kind: dyadic_rule_summary(rulers, kind, cache) for kind in COVER_KINDS},
            "simple_T_equals_k": dyadic_t_equals_k_summary(rulers, cache),
        },
        "dyadic_energy_distribution": energy_distribution_summary(rulers),
        "interpretation": {
            "positive_finite_pattern": "simple gamma has Q=0, hence G=theta*B_D*V>0 in every enumerated nonempty ruler",
            "analytic_T_equals_k_pattern": "on dyadic k-mark prefixes, T=k and simple gamma give V>=1/8 and G/N>=theta/8",
            "centered_warning": "the infinite dyadic sum of O_T=V_T-|A|/(2T) is zero; the easy full-V carrier includes diagonal Parseval mass",
            "falsification_rule": "a nonpositive dyadic prefix refutes only the displayed fixed Pi, not all nonanticipating rules",
            "boundary_warning": "differences of separately optimized products are not labelled G",
            "global_status": "UNRESOLVED_AT_HARD_LIMIT",
        },
    }


_EXPECTED_CACHE: dict[str, object] | None = None


def build_certificate() -> dict[str, object]:
    body = build_body()
    body["payload_sha256"] = hashlib.sha256(canonical_bytes(body)).hexdigest()
    return body


def expected_certificate() -> dict[str, object]:
    global _EXPECTED_CACHE
    if _EXPECTED_CACHE is None:
        _EXPECTED_CACHE = build_certificate()
    return copy.deepcopy(_EXPECTED_CACHE)


def validate_certificate(value: dict[str, object]) -> None:
    if not isinstance(value, dict):
        raise CertificateError("certificate must be an object")
    body = dict(value)
    supplied = body.pop("payload_sha256", None)
    if supplied != hashlib.sha256(canonical_bytes(body)).hexdigest():
        raise CertificateError("payload hash mismatch")
    if value != expected_certificate():
        raise CertificateError("semantic replay mismatch")


def rehash(value: dict[str, object]) -> None:
    value.pop("payload_sha256", None)
    value["payload_sha256"] = hashlib.sha256(canonical_bytes(value)).hexdigest()


def self_check(value: dict[str, object]) -> int:
    validate_certificate(value)
    mutations = (
        (("scope", "q1_resolved"), True),
        (("scope", "compatible_history"), True),
        (("convention", "boundary_sites"), "x=0,...,N+2T-3"),
        (("identities", "dyadic_split"), "wrong shift"),
        (("identities", "haar_correlation"), "wrong normalization"),
        (("identities", "centered_telescope"), "wrong sign"),
        (("enumeration", "total_rulers"), 0),
        (("analytic_checks", "negative_haar_budget_bound_for_T_at_least_2"), "-1/4"),
        (("cover_summaries", "simple_gamma", "sign_counts", "negative"), 1),
        (("dyadic_energy_distribution", "identity"), "false"),
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
    parser.add_argument("--output", type=Path)
    parser.add_argument("--verify", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args(argv)
    if args.verify:
        value = json.loads(args.verify.read_text(encoding="utf-8"))
        validate_certificate(value)
        if args.verify.read_bytes() != rendered_bytes(value):
            raise CertificateError("certificate is not byte-canonical")
        print(f"certificate verify: PASS {value['payload_sha256']}")
        if args.self_check:
            print(f"self-check: PASS ({self_check(value)} mutations rejected)")
        return 0
    value = build_certificate()
    if args.output:
        args.output.write_bytes(rendered_bytes(value))
        print(f"wrote {args.output}")
        print(f"payload_sha256={value['payload_sha256']}")
    else:
        summary = {
            "payload_sha256": value["payload_sha256"],
            "rulers": value["enumeration"]["total_rulers"],
            "records_per_cover": value["enumeration"]["records_per_cover"],
            "sign_counts": {kind: data["sign_counts"] for kind, data in value["cover_summaries"].items()},
            "status": STATUS,
        }
        print(json.dumps(summary, sort_keys=True, indent=2))
    if args.self_check:
        print(f"self-check: PASS ({self_check(value)} mutations rejected)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
