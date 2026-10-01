#!/usr/bin/env python3
"""Exact actual-prefix spectral obstruction; standard library only.

Verifies an old centered Rayleigh quotient above p-1 and a positive-definite
certificate placing every born-dead centered Rayleigh quotient below p-1.
No numerical eigensolver is used by this checker. This is a finite transfer
counterexample, not a refutation of an asymptotic capped-prefix lower bound.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement
from math import comb
import hashlib
import json


def actual_labels(points):
    pairs = list(combinations(points, 2))
    labels = {b - a for a, b in pairs}
    sums = [a + b for a, b in combinations_with_replacement(points, 2)]
    assert len(labels) == len(pairs) and len(set(sums)) == len(sums)
    return labels


def conv(points, labels, values):
    out = defaultdict(int)
    for a in points:
        for d in labels:
            out[a + d] += values[d]
    return dict(out)


def dot(f, g):
    return sum(v * g.get(x, 0) for x, v in f.items())


def add(*fs):
    out = defaultdict(int)
    for f in fs:
        for x, v in f.items():
            out[x] += v
    return dict(out)


P = [0, 2, 3, 11, 24, 28, 43, 70, 88, 122, 166, 196, 203, 258, 272, 278]
full = P.copy()
ds = actual_labels(full)
candidate = full[-1] + 1
while len(full) < 32:
    new = {candidate - a for a in full}
    if not ds & new:
        full.append(candidate)
        ds |= new
    candidate += 1
assert actual_labels(full) == ds
positive_full = [a + 1 for a in full]
assert actual_labels(positive_full) == ds
assert all(positive_full[n - 1] <= 2 * n * n for n in range(2, 33))
future = full[len(P):]
assert future == [361, 409, 419, 482, 518, 699, 704, 799, 853, 886,
                  970, 1031, 1258, 1296, 1420, 1517]

p = len(P)
birth = {P[j] - P[i]: j + 1 for j in range(p) for i in range(j)}
F = sorted(birth)
q = len(F)
assert q == comb(p, 2) == 120
A = [[0] * q for _ in F]
B = [[0] * q for _ in F]
for i, d in enumerate(F):
    for j in range(i + 1, q):
        e = F[j]
        t = e - d
        if t in birth:
            A[i][j] = A[j][i] = 1
            if birth[t] <= max(birth[d], birth[e]):
                B[i][j] = B[j][i] = 1
            else:
                # A retired edge has an actual, injectively paired born-dead mate.
                assert birth[t] > birth[d] and birth[t] > birth[e]
                assert e - t == d
                assert birth[d] <= max(birth[t], birth[e])

z = [-3,-3,-3,-3,-2,-4,-3,-3,-4,-4,-1,-4,-4,-4,-4,-2,-4,-3,-4,-5,
     -5,-3,-4,-3,-3,-3,-3,-3,-4,-2,-5,-3,-4,-2,-3,-2,-3,-1,-2,-1,
     -2,-1,-1,-2,0,0,0,-3,0,-1,-1,1,-3,-1,-1,-1,-1,-2,0,1,
     3,-1,1,1,-1,0,-1,1,0,1,2,2,3,3,2,2,3,3,1,2,
     3,3,3,3,3,2,4,2,3,3,2,3,3,1,2,2,4,1,3,2,
     3,4,3,4,4,3,4,4,4,2,3,3,4,2,3,3,3,3,3,3]
assert len(z) == q and sum(z) == 0
S = sum(x * x for x in z)
zAz = sum(z[i] * A[i][j] * z[j] for i in range(q) for j in range(q))
zBz = sum(z[i] * B[i][j] * z[j] for i in range(q) for j in range(q))
assert S == 918 and zAz == 13894 and zAz > (p - 1) * S

# Columns e_i-e_last form a basis of 1^perp. Sylvester's criterion is applied
# to E^T((p-1)I-B)E. Bareiss pivots are the exact leading principal minors.
n = q - 1
certificate = [[(p - 1) * (int(i == j) + 1) - B[i][j] + B[i][-1] + B[j][-1]
                for j in range(n)] for i in range(n)]
matrix_sha256 = hashlib.sha256(json.dumps(certificate, separators=(',', ':')).encode()).hexdigest()
work = [row.copy() for row in certificate]
previous = 1
minors = []
for k in range(n):
    pivot = work[k][k]
    minors.append(pivot)
    assert pivot > 0, (k, pivot)
    if k + 1 == n:
        break
    for i in range(k + 1, n):
        for j in range(i, n):
            numerator = pivot * work[i][j] - work[i][k] * work[k][j]
            value, remainder = divmod(numerator, previous)
            assert remainder == 0
            work[i][j] = work[j][i] = value
    previous = pivot
assert len(minors) == 119
assert zBz < (p - 1) * S

# Exact causal energy decomposition with the same terminal, centered label vector.
values = dict(zip(F, z))
prevP, prevF = [], set()
prev_f, prev_E = {}, 0
ret_total = 0
injection_minus_diagonal = 0
energy_records = []
for rank, a in enumerate(P, 1):
    Gn = {a - x for x in prevP}
    currP, currF = prevP + [a], prevF | Gn
    hn = {a + d: values[d] for d in prevF}
    gn = conv(currP, Gn, values)
    fn = conv(currP, currF, values)
    assert fn == add(prev_f, hn, gn)
    I = dot(gn, gn) + 2 * dot(add(prev_f, hn), gn)
    Ret = dot(prev_f, hn)
    Sprev = sum(values[d] ** 2 for d in prevF)
    SG = sum(values[d] ** 2 for d in Gn)
    E = dot(fn, fn)
    assert E - prev_E == Sprev + 2 * Ret + I
    ret_total += Ret
    injection_minus_diagonal += I - rank * SG
    energy_records.append({"rank": rank, "label_birth_energy_injection": I,
                           "new_diagonal_cost": rank * SG,
                           "retirement_quadratic": Ret})
    prevP, prevF, prev_f, prev_E = currP, currF, fn, E
assert 2 * ret_total == zAz - zBz
assert injection_minus_diagonal == zBz

# A compatible positive-demand future block; W=J+zz^T/25 is entrywise positive PSD.
lam = Q(1, 25)
assert all(1 + lam * x * y > 0 for x in z for y in z)
M = Q(q * q)
SW = q + lam * S
H = P[-1] - P[0]
L = future[-1] - future[0] + 1
capacity = L + H - p
delta0 = (p * p * M / capacity - p * q) / 2
deltaW = (p * p * M / capacity - p * SW) / 2
future_labels = actual_labels(future)
PsiW = sum(1 + lam * z[i] * z[j] for i in range(q) for j in range(i + 1, q)
           if F[j] - F[i] in future_labels)
assert 0 < deltaW <= PsiW
old_gap_gain = lam * (zAz - (p - 1) * S) / 2
historical_gap_gain = lam * (zBz - (p - 1) * S) / 2
assert old_gap_gain == Q(62, 25) > 0
assert historical_gap_gain < 0


def rational(x):
    return {"exact": str(x), "decimal_display_only": float(x)}


report = {
    "status": "EXACT_PSD_CERTIFICATE_PASS_Q1_UNRESOLVED",
    "scope": "Finite optimized-centered-cone transfer counterexample; not an asymptotic counterexample",
    "all_32_positive_points": positive_full,
    "old_prefix_size": p, "F": F, "label_birth_ranks": [birth[d] for d in F],
    "q": q, "H": H, "future_interval_length": L, "future_denominator": capacity,
    "integer_centered_witness": z, "witness_norm_squared": S,
    "old_quadratic": zAz, "born_dead_quadratic": zBz,
    "threshold_times_norm_squared": (p - 1) * S,
    "old_centered_Rayleigh_lower_bound": rational(Q(zAz, S)),
    "born_dead_centered_spectrum_strict_upper_bound": p - 1,
    "certificate_basis": "columns e_i-e_last, i=1,...,q-1",
    "certificate_matrix": "E^T((p-1)I-B)E",
    "certificate_matrix_sha256": matrix_sha256,
    "positive_leading_principal_minors": [str(x) for x in minors],
    "certificate_arithmetic": "fraction-free Bareiss; all divisions exact; all 119 minors positive",
    "old_edges": sum(map(sum, A)) // 2, "born_dead_edges": sum(map(sum, B)) // 2,
    "lambda": rational(lam), "uniform_raw_demand": rational(delta0),
    "corrected_raw_demand": rational(deltaW), "actual_internal_expenditure": rational(PsiW),
    "old_row_gap_gain": rational(old_gap_gain),
    "historical_capacity_minus_terminal_demand_gain": rational(historical_gap_gain),
    "causal_energy_records": energy_records,
    "not_claimed": ["asymptotic failure of Omega(p^2/log p)", "infinite fixed-onset capped history", "Q1 proof", "Lean verification"]
}
print(json.dumps(report, ensure_ascii=False, indent=2))
