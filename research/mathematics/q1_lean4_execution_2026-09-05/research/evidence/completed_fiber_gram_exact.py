#!/usr/bin/env python3
"""Exact identity checks on two fixed complete same-sum fibers; no search."""

from fractions import Fraction as F
from itertools import combinations


SIX = (0, 1, 10, 13, 17, 39)
THIRTY_TWO = (
    1, 3, 4, 12, 25, 29, 44, 71, 89, 123, 167, 197, 204, 259, 273, 279,
    362, 410, 420, 483, 519, 700, 705, 800, 854, 887, 971, 1032, 1259,
    1297, 1421, 1518,
)


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def apply(matrix, v):
    return [dot(row, v) for row in matrix]


def bilinear(u, matrix, v):
    return dot(u, apply(matrix, v))


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def inspect(points, target_sum):
    n = len(points)
    h = points[-1] - points[0]
    differences = [points[j] - points[i] for i in range(n) for j in range(i + 1, n)]
    assert len(set(differences)) == len(differences)
    triples = sorted(
        (t for t in combinations(range(n), 3) if sum(points[i] for i in t) == target_sum),
        key=max,
    )
    count = len(triples)
    assert count >= 2
    endpoints = [i for triple in triples for i in triple]
    assert len(set(endpoints)) == 3 * count
    center = F(target_sum, 3)
    means = [F(points[0])] + [F(sum(points[:j]), j) for j in range(1, n)]
    x = [(F(a) - center) / h for a in points]
    mu = [(m - center) / h for m in means]
    lag = [(F(a) - m) / h for a, m in zip(points, means)]
    times = [a + m for a, m in zip(x, mu)]
    q = [[mu[j] - x[i] if i < j else F(0) for i in range(n)] for j in range(n)]
    qt = transpose(q)
    qs = [[q[i][j] + qt[i][j] for j in range(n)] for i in range(n)]
    assert all(sum(row) == 0 for row in q)
    assert all(0 <= b <= 1 for b in lag)
    assert all(times[i] < times[i + 1] for i in range(n - 1))
    nus = [[F(int(i in triple)) for i in range(n)] for triple in triples]
    average = [F(int(i in endpoints), count) for i in range(n)]
    lambdas = [2 * mu[max(triple)] for triple in triples]
    cumulative = [[F(0)] * n]
    bridge = [[F(0)] * n]
    for r, nu in enumerate(nus, 1):
        cumulative.append([a + b for a, b in zip(cumulative[-1], nu)])
        bridge.append([a - r * b for a, b in zip(cumulative[-1], average)])
        assert sum(bridge[-1]) == 0
        assert dot(x, bridge[-1]) == 0
        assert dot(bridge[-1], bridge[-1]) == F(3 * r * (count - r), count)
    assert all(value == 0 for value in bridge[-1])
    increments = [[a - b for a, b in zip(bridge[r], bridge[r - 1])] for r in range(1, count + 1)]
    operators = [
        [[(x[i] + lam) * q[i][j] for j in range(n)] for i in range(n)]
        for lam in lambdas
    ]
    symmetric = [
        [[a[i][j] + a[j][i] for j in range(n)] for i in range(n)] for a in operators
    ]
    skew = [
        [[a[i][j] - a[j][i] for j in range(n)] for i in range(n)] for a in operators
    ]

    def brownian_gram(v):
        return sum(
            (times[k + 1] - times[k]) * sum(v[k + 1:])**2 for k in range(n - 1)
        )

    for xi in bridge:
        assert bilinear(xi, qs, xi) == sum(b * value**2 for b, value in zip(lag, xi)) - brownian_gram(xi)

    original = sum(
        bilinear(cumulative[r], operators[r], nus[r]) for r in range(count)
    )
    direct = F(0)
    for r, new in enumerate(triples):
        terminal = max(new)
        for old in triples[:r]:
            direct += sum(
                (2 * mu[terminal] + x[j]) * sum(mu[j] - x[i] for i in new if i < j)
                for j in old
            )
    assert original == direct
    # Check the monotone-hinge minus downward-jump representation separately.
    for nu, new in zip(nus, triples):
        values = apply(q, nu)
        for j in range(n):
            increasing = sum(mu[j] - mu[i] for i in new if i < j)
            jumps = sum(lag[i] for i in new if i < j)
            assert values[j] == increasing - jumps

    gram = sum(
        (lambdas[r] - lambdas[r - 1]) * brownian_gram(bridge[r]) / 4
        for r in range(1, count)
    )
    diagonal = -sum(
        bilinear(increments[r], symmetric[r], increments[r]) / 4 for r in range(count)
    ) - sum(
        (lambdas[r] - lambdas[r - 1]) * sum(b * value**2 for b, value in zip(lag, bridge[r])) / 4
        for r in range(1, count)
    )
    circulation = sum(
        bilinear(bridge[r], skew[r], increments[r]) / 2 for r in range(count)
    ) + sum(
        bilinear(bridge[r], skew[r], average) for r in range(1, count)
    )
    average_drift = sum(
        r * bilinear(average, operators[r], average) for r in range(count)
    ) - sum(
        (r - 1) * (lambdas[r] - lambdas[r - 1]) * bilinear(bridge[r], qt, average)
        for r in range(1, count)
    )
    assert gram >= 0
    assert abs(diagonal) <= 28 * count
    assert original == gram + diagonal + circulation + average_drift
    print(f"N={n}; fixed sum={target_sum}; complete fiber size={count}")
    print("triples=" + repr([tuple(points[i] for i in triple) for triple in triples]))
    print(f"original_fiber={original}")
    print(f"nonnegative_gram={gram}")
    print(f"diagonal_error={diagonal}")
    print(f"skew_circulation={circulation}")
    print(f"fiber_average_drift={average_drift}")
    print("complete-fiber formula, Brownian Gram, bridge and four-channel decomposition: PASS")


if __name__ == "__main__":
    inspect(SIX, 40)
    inspect(THIRTY_TWO, 1533)
    print("Only the two fixed identities above were checked; no asymptotic sign conclusion.")
