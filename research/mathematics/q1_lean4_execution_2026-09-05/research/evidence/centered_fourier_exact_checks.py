#!/usr/bin/env python3
"""Exact rational-unit-circle carrier comparison; standard library only.

The angle is theta = 2 arctan(1/(2D)). Its sine and cosine are rational.
Gaussian-integer numerators avoid floating-point trigonometry entirely.
The general logarithmic-rate proof is mathematical, not inferred from this example.
"""
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement
from math import comb
import hashlib
import json


def sidon_labels(points):
    ds = [b - a for a, b in combinations(points, 2)]
    ss = [a + b for a, b in combinations_with_replacement(points, 2)]
    assert len(set(ds)) == len(ds) and len(set(ss)) == len(ss)
    return set(ds)


def rational_record(x):
    return {"numerator": str(x.numerator), "denominator": str(x.denominator),
            "decimal_display_only": float(x)}


P = [0, 1, 3, 7, 12, 20, 36, 46, 61, 83, 101, 131, 173, 200, 251, 279, 335]
A = P.copy()
labels = sidon_labels(A)
a = A[-1] + 1
while len(A) < 34:
    new = {a - x for x in A}
    if not new & labels:
        A.append(a)
        labels |= new
    a += 1
assert sidon_labels(A) == labels
B = A[len(P):]
old, future = sidon_labels(P), sidon_labels(B)
assert old.isdisjoint(future)
F = sorted(old)
p, m, q = len(P), len(B), len(F)
r = p // 8
D = P[p - r - 1] - P[r]
H = P[-1] - P[0]
L = B[-1] - B[0] + 1
capacity = L + H - m
assert p >= 16 and D > 0 and 0 < capacity
short = [d for d in F if 2 * d <= D]
long = [d for d in F if d >= D]
assert 16 * len(short) >= p * p and 256 * len(long) >= p * p

# exp(i theta)=(b^2-1+2bi)/(b^2+1), theta=2 arctan(1/b), b=2D.
b = 2 * D
re, im, h = b * b - 1, 2 * b, b * b + 1
assert re * re + im * im == h * h
powers = [(1, 0)]
for j in range(H):
    x, y = powers[-1]
    powers.append((x * re - y * im, x * im + y * re))
common = h ** H
unit = {d: (powers[d][0] * h ** (H - d), powers[d][1] * h ** (H - d))
        for d in range(H + 1)}
assert all(x * x + y * y == common * common for x, y in unit.values())
mean_num = (sum(unit[d][0] for d in F), sum(unit[d][1] for d in F))
z = {d: (q * unit[d][0] - mean_num[0], q * unit[d][1] - mean_num[1]) for d in F}
assert sum(x for x, y in z.values()) == 0 and sum(y for x, y in z.values()) == 0
zden = q * common
gram_den = zden * zden
S_R_num = sum(x * x + y * y for x, y in z.values())
assert S_R_num == q * gram_den - q * (mean_num[0] ** 2 + mean_num[1] ** 2)
assert Q(S_R_num, q * gram_den) >= Q(1, 24576)
assert S_R_num <= q * gram_den
P_num = (sum(unit[d][0] for d in P), sum(unit[d][1] for d in P))
assert 64 * (P_num[0] ** 2 + P_num[1] ** 2) >= p * p * common * common

twoT_R_num = 0
for d, e in combinations(F, 2):
    x, y = z[d]
    u, v = z[e]
    dot = x * u + y * v
    assert 8 * gram_den + dot >= 0
    if e - d in old:
        twoT_R_num += 2 * dot
phase_gain = Q(twoT_R_num - (m - 1) * S_R_num, 16 * gram_den)
assert phase_gain > 0

M = Q(q * q)
uniform_T = sum(1 for d, e in combinations(F, 2) if e - d in old)
uniform_C = (M - q) / 2 - uniform_T
uniform_delta = (m * m * M / capacity - m * q) / 2
scalar_records = []
scalar_gains = []
scalar_S = []
for coord, label in [(0, "real"), (1, "imaginary")]:
    for sign in [-1, 1]:
        nums = {d: 2 * zden + sign * z[d][coord] for d in F}
        assert all(v >= 0 for v in nums.values())
        den = 4 * gram_den
        assert sum(nums.values()) == 2 * zden * q
        S = Q(sum(v * v for v in nums.values()), den)
        assert q <= S <= Q(5 * q, 4)
        T = Q(sum(nums[d] * nums[e] for d, e in combinations(F, 2) if e - d in old), den)
        Psi = Q(sum(nums[d] * nums[e] for d, e in combinations(F, 2) if e - d in future), den)
        C = (M - S) / 2 - T
        delta = (m * m * M / capacity - m * S) / 2
        assert 0 < delta <= Psi <= C
        gain = (uniform_C - uniform_delta) - (C - delta)
        scalar_gains.append(gain)
        scalar_S.append(S)
        scalar_records.append({"coordinate": label, "sign": sign,
            "trace_decimal_display_only": float(S),
            "capacity_decimal_display_only": float(C),
            "demand_decimal_display_only": float(delta),
            "actual_expenditure_decimal_display_only": float(Psi),
            "row_gain_decimal_display_only": float(gain)})
assert sum(scalar_gains) / 4 == phase_gain
assert sum(scalar_S) / 4 == q + Q(S_R_num, 8 * gram_den)
best = max(range(4), key=lambda i: scalar_gains[i])
assert scalar_gains[best] >= phase_gain

# The earlier affine carrier is the mean of two nonnegative rank-one carriers.
mean_d = Q(sum(F), q)
centered = {d: Q(d) - mean_d for d in F}
for d, e in combinations(F, 2):
    xp, xm = 1 + centered[d] / H, 1 - centered[d] / H
    yp, ym = 1 + centered[e] / H, 1 - centered[e] / H
    assert min(xp, xm, yp, ym) >= 0
    assert (xp * yp + xm * ym) / 2 == 1 + centered[d] * centered[e] / H ** 2

report = {
    "status": "EXACT_PASS_Q1_UNRESOLVED",
    "scope": "One exact rational-phase productive finite comparison; no inference of an asymptotic theorem from numerical data",
    "all_34_positive_points": [x + 1 for x in A], "P_size": p, "B_size": m,
    "full_label_count": q, "central_trim_count": r, "central_width_D": D,
    "old_width_H": H, "future_interval_L": L, "denominator": capacity,
    "short_label_count": len(short), "long_label_count": len(long),
    "unit_circle_real_numerator": re, "unit_circle_imaginary_numerator": im,
    "unit_circle_denominator": h,
    "phase_definition": "theta = 2 arctan(1/(2D)); no floating-point trigonometry used",
    "phase_variance_decimal_display_only": float(Q(S_R_num, q * gram_den)),
    "phase_matrix_row_gain": rational_record(phase_gain),
    "phase_matrix_normalized_gain": rational_record(phase_gain / M),
    "four_nonnegative_scalar_carriers": scalar_records,
    "best_scalar_index": best,
    "best_scalar_row_gain": rational_record(scalar_gains[best]),
    "exact_mean_of_four_scalar_gains_matches_matrix": True,
    "not_claimed": ["uniform physical-envelope improvement", "Q1 proof", "Lean verification"]
}
print(json.dumps(report, ensure_ascii=False, indent=2))
