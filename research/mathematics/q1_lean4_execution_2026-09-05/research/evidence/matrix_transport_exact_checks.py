#!/usr/bin/env python3
"""Exact finite checks for matrix_transport_route.md; Python standard library only.

This checks one 34-point Sidon history and the stated finite carrier comparison.
It does not establish a uniform physical-envelope gain or resolve Erdős #1191 Q1.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement
from math import comb
import json


def encode(x):
    if isinstance(x, Q):
        return {"exact": str(x), "decimal_display_only": float(x)}
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [encode(v) for v in x]
    return x


def labels(points):
    ds = [b - a for a, b in combinations(points, 2)]
    assert len(ds) == len(set(ds))
    sums = [a + b for a, b in combinations_with_replacement(points, 2)]
    assert len(sums) == len(set(sums)), "repeated summands are included"
    return set(ds)


P = [0, 1, 3, 7, 12, 20, 36, 46, 61, 83, 101, 131, 173, 200, 251, 279, 335]
A = P.copy()
D = labels(A)
x = A[-1] + 1
while len(A) < 34:
    new = {x - a for a in A}
    if not new & D:
        A.append(x)
        D |= new
    x += 1
B = A[len(P):]
assert B == [356, 387, 453, 521, 596, 698, 751, 813, 880, 989, 1075,
             1213, 1316, 1339, 1432, 1574, 1707]
assert labels(A) == D
positive_A = [a + 1 for a in A]
assert labels(positive_A) == D
F = sorted(labels(P))
old = set(F)
future = labels(B)
assert old.isdisjoint(future)
p, m, q = len(P), len(B), len(F)
H, L = P[-1] - P[0], B[-1] - B[0] + 1
capacity = L + H - m
assert q == comb(p, 2) and capacity > 0 and H - 1 <= L - 1
mean = Q(sum(F), q)
z = {d: Q(d) - mean for d in F}
assert sum(z.values()) == 0
V = sum(v * v for v in z.values())
eps = Q(1, H * H)
K0, KR = defaultdict(Q), defaultdict(Q)
for d, e in combinations(F, 2):
    K0[e - d] += 1
    KR[e - d] += z[d] * z[e]
    entry = 1 + eps * z[d] * z[e]
    assert Q(3, 4) <= entry <= 2
K1 = {t: K0[t] + eps * KR[t] for t in K0}
M = Q(q * q)
S0, S1 = Q(q), Q(q) + eps * V
assert q <= S1 <= Q(5, 4) * q
assert S0 + 2 * sum(K0.values()) == M
assert S1 + 2 * sum(K1.values()) == M
assert sum(KR.values()) == -V / 2
T0 = sum(K0[t] for t in old)
TR = sum(KR[t] for t in old)
T1 = T0 + eps * TR
C0 = sum(K0[t] for t in K0 if t not in old)
C1 = sum(K1[t] for t in K1 if t not in old)
assert C0 == (M - S0) / 2 - T0
assert C1 == (M - S1) / 2 - T1
Psi0 = sum(K0[t] for t in future)
Psi1 = sum(K1.get(t, Q(0)) for t in future)
delta0 = (m * m * M / capacity - m * S0) / 2
delta1 = (m * m * M / capacity - m * S1) / 2
assert 0 < delta1 <= Psi1 <= C1
assert 0 < delta0 <= Psi0 <= C0
gain = (C0 - delta0) - (C1 - delta1)
assert gain == eps * (2 * TR - (m - 1) * V) / 2
assert gain == Q(9021202961, 259464200) > 0

# Direct vector-valued convolution check, independently of the kernel expansion.
shadow = defaultdict(lambda: [Q(0), Q(0)])
for b in B:
    for d in F:
        shadow[b + d][0] += 1
        shadow[b + d][1] += z[d] / H
assert set(shadow).isdisjoint(B)
assert len(shadow) <= capacity
assert sum(v[0] for v in shadow.values()) == m * q
assert sum(v[1] for v in shadow.values()) == 0
shadow_energy = sum(v[0] ** 2 + v[1] ** 2 for v in shadow.values())
assert shadow_energy == m * S1 + 2 * Psi1
assert m * m * M <= capacity * shadow_energy

old_shadow = defaultdict(Q)
for a in P:
    for d in F:
        old_shadow[a + d] += z[d]
E = sum(v * v for v in old_shadow.values())
assert sum(old_shadow.values()) == 0
assert sum(t * v for t, v in old_shadow.items()) == p * V
assert E == p * V + 2 * TR
assert E >= Q(p * p) * V * V / (2 * H ** 3)
assert V >= Q(q * (q * q - 1), 12)

# Sharpness of M/S <= p-1 for PSD matrices vanishing on every old edge.
zero_old_sharpness = []
for size in range(2, 8):
    pp = [10 ** i for i in range(size)]
    dd = labels(pp)
    ff = [pp[i + 1] - pp[i] for i in range(size - 1)]
    assert all(abs(e - d) not in dd for d, e in combinations(ff, 2))
    zero_old_sharpness.append({"p": size, "F": ff, "M_over_S": size - 1})

# Exact four-endpoint source-birth count on uncapped, actual base-10 Sidon prefixes.
birth_checks = []
for size in [4, 8, 16]:
    pp = [10 ** i for i in range(size)]
    dd = labels(pp)
    pair_of_label = {pp[j] - pp[i]: (i, j)
                     for i in range(size) for j in range(i + 1, size)}
    four_births = defaultdict(int)
    four_earlier = set()
    for d, e in combinations(sorted(dd), 2):
        ends = set(pair_of_label[d] + pair_of_label[e])
        if len(ends) != 4:
            continue
        t = e - d
        assert t not in dd
        if max(ends) >= size // 2:
            four_births[t] += 1
        else:
            four_earlier.add(t)
    assert set(four_births).isdisjoint(four_earlier)
    expected = 3 * (comb(size, 4) - comb(size // 2, 4))
    assert sum(four_births.values()) == expected
    birth_checks.append({"p": size, "four_endpoint_relations": expected,
                         "normalized_birth_mass": Q(expected, comb(size, 2) ** 2)})

report = {
    "status": "EXACT_PASS_Q1_UNRESOLVED",
    "scope": "One finite productive row comparison, exact convolution checks, and finite obstruction checks",
    "greedy_rule": "Starting after the seed maximum, choose the least next integer whose positive differences with all existing points are unused; stop at 34 points.",
    "seed_P_zero_based": P, "future_B_zero_based": B,
    "all_34_positive_points": positive_A,
    "F": F, "p": p, "m": m, "q": q, "H": H, "L": L,
    "capacity_denominator": capacity, "mean_F": mean, "variance_sum_V": V,
    "epsilon": eps, "M_both": M, "S_uniform": S0, "S_affine": S1,
    "old_expenditure_uniform": T0, "old_expenditure_affine": T1,
    "available_capacity_uniform": C0, "available_capacity_affine": C1,
    "raw_demand_uniform": delta0, "raw_demand_affine": delta1,
    "actual_expenditure_uniform": Psi0, "actual_expenditure_affine": Psi1,
    "capacity_minus_demand_improvement": gain,
    "normalized_improvement": gain / M,
    "old_centered_energy": E, "old_centered_2T": 2 * TR,
    "future_shadow_support_card": len(shadow), "future_shadow_energy": shadow_energy,
    "zero_old_sharpness_checks": zero_old_sharpness,
    "uncapped_source_birth_checks": birth_checks,
    "not_claimed": ["uniform physical-envelope improvement", "fixed-onset infinite capped history", "Q1 proof", "Lean verification of this note"],
}
print(json.dumps(encode(report), ensure_ascii=False, indent=2))
