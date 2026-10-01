#!/usr/bin/env python3
"""Two fixed, exact checks of the actual birth-linear total and its fibers.

No parameter sweep or asymptotic inference. Python standard library only.
"""

from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations


SIX = (0, 1, 10, 13, 17, 39)
FIXTURE32 = (
    1, 3, 4, 12, 25, 29, 44, 71, 89, 123, 167, 197, 204, 259, 273, 279,
    362, 410, 420, 483, 519, 700, 705, 800, 854, 887, 971, 1032, 1259,
    1297, 1421, 1518,
)


def inspect(points):
    n = len(points)
    diameter = points[-1] - points[0]
    means = {j: Q(sum(points[:j]), j) for j in range(1, n)}
    bank = {}
    for j in range(1, n):
        for i in range(j):
            d = points[j] - points[i]
            assert d > 0 and d not in bank
            bank[d] = (j, i, (means[j] - points[i]) / diameter)
    for j in range(1, n):
        assert sum(z for upper, lower, z in bank.values() if upper == j) == 0
    square_sum = sum(z * z for j, i, z in bank.values())
    born = mixed = auto = repeated = six = Q(0)
    mixed_pairs = []
    for d, e in combinations(sorted(bank), 2):
        t = e - d
        if t not in bank:
            continue
        jd, id_, zd = bank[d]
        je, ie, ze = bank[e]
        jt, it, _ = bank[t]
        if jt > max(jd, je):
            continue
        weight = zd * ze
        born += weight
        if jd == je:
            continue
        mixed += weight
        mixed_pairs.append((d, e))
        # e=d+t restores a_je+a_id+a_it = a_ie+a_jd+a_jt.
        left = tuple(sorted((je, id_, it)))
        right = tuple(sorted((ie, jd, jt)))
        assert sum(points[j] for j in left) == sum(points[j] for j in right)
        if left == right:
            auto += weight
        elif len(set(left + right)) == 6:
            six += weight
        else:
            assert not set(left).intersection(right)
            repeated += weight
    total = born + square_sum / 2
    assert total == mixed == auto + repeated + six
    columns = [sum(z for j, i, z in bank.values() if i == h) for h in range(n)]
    auto_formula = (sum(c * c for c in columns) - square_sum) / 2
    assert auto_formula == auto

    fibers = defaultdict(list)
    for triple in combinations(range(n), 3):
        fibers[sum(points[j] for j in triple)].append(triple)
    direct_fiber_sum = Q(0)
    fiber_pair_count = 0
    for s, triples in fibers.items():
        for first, second in combinations(triples, 2):
            assert not set(first).intersection(second)
            old, new = (first, second) if max(first) < max(second) else (second, first)
            terminal = max(new)
            contribution = sum(
                (2 * means[terminal] - s + points[j])
                * sum(means[j] - points[h] for h in new if h < j)
                for j in old
            ) / diameter**2
            direct_fiber_sum += contribution
            fiber_pair_count += 1
    assert direct_fiber_sum == six
    assert abs(repeated) <= 12 * n**3

    def cut(d, k):
        j, i, _ = bank[d]
        if j < k:
            return Q(0)
        return Q(j - k, j) if i < k else -Q(k, j)

    def cut_kernel(k, ell):
        return sum(
            (cut(d, k) * cut(e, ell) + cut(d, ell) * cut(e, k)) / 2
            for d, e in mixed_pairs
        )

    print(f"N={n}; positive-difference injectivity and every class sum verified")
    print(f"S={square_sum}")
    print(f"X_direct={total}")
    print(f"X_automatic={auto}")
    print(f"X_repeated={repeated}")
    print(f"X_six_distinct={six}")
    print(f"six_distinct_triple_pairs={fiber_pair_count}")
    print("direct born, mixed born, automatic-column and all-fiber identities: PASS")
    return cut_kernel, total, diameter


def main():
    cut, total, diameter = inspect(SIX)
    matrix = [[cut(k, ell) for ell in range(1, 6)] for k in range(1, 6)]
    print("six-point exact cut matrix:")
    for row in matrix:
        print(" ".join(str(entry) for entry in row))
    assert matrix[0][2] == -Q(37, 240)
    gaps = [SIX[k] - SIX[k - 1] for k in range(1, 6)]
    assert sum(
        gaps[k] * gaps[ell] * matrix[k][ell] for k in range(5) for ell in range(5)
    ) == diameter**2 * total
    cut, _, _ = inspect(FIXTURE32)
    diagonal, mixed, late_diagonal = cut(1, 1), cut(1, 30), cut(30, 30)
    assert diagonal > 0 and mixed < 0 and late_diagonal == 0
    relaxation_gap = diagonal / (-2 * mixed) + 1
    relaxation_value = diagonal + 2 * relaxation_gap * mixed
    assert relaxation_value == 2 * mixed < 0
    print(f"K_1_1={diagonal}; K_1_30={mixed}; K_30_30={late_diagonal}")
    print(f"infeasible relaxed gap: delta_1=1; delta_30={relaxation_gap}; others=0")
    print(f"relaxed quadratic={relaxation_value}")
    assert FIXTURE32[1] + FIXTURE32[3] + FIXTURE32[31] == (
        FIXTURE32[0] + FIXTURE32[14] + FIXTURE32[28]
    )
    print("actual relation: a_2+a_4+a_32=a_1+a_15+a_29=1533")
    print(f"relaxation violates this relation by {1 + relaxation_gap}")
    print("No actual negative-total or asymptotic conclusion follows from the relaxation.")


if __name__ == "__main__":
    main()
