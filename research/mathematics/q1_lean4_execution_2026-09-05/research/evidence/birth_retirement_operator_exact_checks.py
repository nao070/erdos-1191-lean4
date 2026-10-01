#!/usr/bin/env python3
"""Exact checks supporting an analytic asymptotic retirement obstruction.

This does not test the large-prime theorem by extrapolation. It checks its
rational constants, and checks every actual edge/energy identity of the
three-cluster lemma on two fixed, bounded Sidon fixtures. No eigensolver.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement
import json
from math import isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def labels(points):
    differences = [b - a for a, b in combinations(points, 2)]
    sums = [a + b for a, b in combinations_with_replacement(points, 2)]
    assert len(set(differences)) == len(differences)
    assert len(set(sums)) == len(sums)
    return set(differences)


def quadratic(edges, z):
    return 2 * sum(z[d] * z[e] for d, e in edges)


def test_fixture(r, ell, usize):
    assert prime(r) and r % 2 and 7 * ell <= r
    base = [2 * r * i + (i * i % r) + 1 for i in range(r)]
    assert all(base[i + 1] - base[i] >= r + 1 for i in range(r - 1))
    L, U, V = base[:ell], base[3 * ell:3 * ell + usize], base[6 * ell:7 * ell]
    P = L + U + V
    F = labels(P)
    dl, du, dv = labels(L), labels(U), labels(V)
    birth = {b - a: j + 1 for j, b in enumerate(P) for a in P[:j]}
    assert set(birth) == F
    hsrc = L[-1] - L[0] + U[-1] - U[0]
    assert U[0] - L[-1] > hsrc and V[0] - U[-1] > hsrc
    source = {b - a: ell * a - sum(L) for b in U for a in L}
    assert len(source) == ell * usize
    by_birth = defaultdict(int)
    for d, z in source.items():
        by_birth[birth[d]] += z
    assert all(v == 0 for v in by_birth.values())
    S = sum(z * z for z in source.values())
    assert sum(source.values()) == 0 and S > 0
    # Integer feature is ell times the real feature used in the note.
    assert sum(d * z for d, z in source.items()) * ell == -S
    retirement, from_v, remainder_u = [], [], []
    for d, e in combinations(sorted(source), 2):
        t = e - d
        assert 0 < t <= hsrc
        isret = t in birth and birth[t] > max(birth[d], birth[e])
        isv = t in dv
        isu = t in du and isret
        assert isret == (isv or isu)
        if isret:
            retirement.append((d, e))
        if isv:
            from_v.append((d, e))
        if isu:
            remainder_u.append((d, e))
    zret = quadratic(retirement, source)
    zv = quadratic(from_v, source)
    zu = quadratic(remainder_u, source)
    assert zret == zv + zu
    degrees = defaultdict(int)
    for d, e in remainder_u:
        degrees[d] += 1
        degrees[e] += 1
    assert max(degrees.values(), default=0) <= usize * (usize - 1)
    assert zu >= -usize * (usize - 1) * S
    f = defaultdict(int)
    for a in V:
        for d, z in source.items():
            f[a + d] += z
    energy = sum(y * y for y in f.values())
    assert energy == len(V) * S + zv
    assert sum(f.values()) == 0
    assert sum(x * y for x, y in f.items()) * ell == -len(V) * S
    D = (L[-1] - L[0]) + (U[-1] - U[0]) + (V[-1] - V[0])
    denominator = D * (D + 1) * (D + 2)
    assert 12 * len(V) ** 2 * S * S <= energy * denominator * ell ** 2
    lower = Q(12 * len(V) ** 2 * S, denominator * ell ** 2) - len(V) - usize * (usize - 1)
    assert Q(zret, S) >= lower

    # Full actual matching block factorization, on the smaller fixture only.
    matching_count = 0
    maximum_row_degree = maximum_column_degree = 0
    if r == 101:
        N = len(P)
        accounted = defaultdict(int)
        for j in range(1, N):
            for l in range(1, N):
                for n in range(max(j, l) + 1, N):
                    rows, columns = defaultdict(int), defaultdict(int)
                    for i in range(j):
                        for k in range(l):
                            d, e = P[j] - P[i], P[l] - P[k]
                            t = e - d
                            if t > 0 and birth.get(t) == n + 1:
                                assert birth[t] > max(birth[d], birth[e])
                                rows[i] += 1
                                columns[k] += 1
                                accounted[(d, e)] += 1
                                matching_count += 1
                    maximum_row_degree = max(maximum_row_degree, max(rows.values(), default=0))
                    maximum_column_degree = max(maximum_column_degree, max(columns.values(), default=0))
                    assert max(rows.values(), default=0) <= 1
                    assert max(columns.values(), default=0) <= 2
        literal = {(d, e) for d, e in combinations(sorted(F), 2)
                   if e - d in birth and birth[e - d] > max(birth[d], birth[e])}
        assert set(accounted) == literal and all(v == 1 for v in accounted.values())
    return {
        'prime': r, 'ell': ell, 'u': usize, 'all_positive_points': P,
        'scope': 'finite exact identity check, not evidence by asymptotic extrapolation',
        'source_labels': len(source), 'birth_centered': True,
        'integer_scaled_feature_norm_squared': S,
        'retirement_quadratic': zret, 'future_cluster_quadratic': zv,
        'within_U_retirement_quadratic': zu, 'convolution_energy': energy,
        'source_width': hsrc, 'convolution_support_width': D,
        'retirement_Rayleigh': str(Q(zret, S)), 'proved_moment_lower_bound': str(lower),
        'matching_factorization_checked': r == 101,
        'matching_edge_count': matching_count if r == 101 else None,
        'matching_max_row_degree': maximum_row_degree if r == 101 else None,
        'matching_max_column_degree': maximum_column_degree if r == 101 else None,
    }

r0 = 2 ** 34
assert r0 >= 72 and r0 >= 2 ** 19
assert Q(1, 2) + Q(1, 2 ** 17) + Q(2, r0 ** 2) <= Q(2, 3)
positive_coefficient = Q(12, 81 * 24 * 729) / Q(2, 3) ** 3
assert positive_coefficient == Q(1, 34992) >= Q(1, 2 ** 16)
assert Q(1, 2 ** 16) - Q(1, 2 ** 18) >= Q(1, 2 ** 17)
assert Q(1, 2 ** 17) * Q(1, 2 ** 19) == Q(1, 2 ** 36)
assert Q(r0 * r0, 2 ** 36) - Q(r0, 8) == Q(r0 * r0, 2 ** 37)
assert Q(81, 2) < 41

print(json.dumps({
    'status': 'EXACT_FACTOR_AND_MOMENT_CHECKS_PASS_ASYMPTOTIC_PROOF_IN_NOTE',
    'analytic_theorem': 'infinitely many actual Sidon P, diam(P)<=41|P|^2, lambda_max(C Rret C)>=|P|^2/2^37',
    'theorem_prime_threshold': r0,
    'positive_moment_coefficient': str(positive_coefficient),
    'fixtures': [test_fixture(101, 12, 2), test_fixture(1031, 128, 4)],
    'not_claimed': ['fixed-onset cap at all prefix ranks', 'Q1 proof or disproof',
                    'Lean verification', 'the large-prime theorem inferred from the fixtures'],
}, indent=2))
