#!/usr/bin/env python3
"""New exact mean-correction identities on the fixed sum-1533 fiber."""

from fractions import Fraction as F
from itertools import combinations


P = (
    1, 3, 4, 12, 25, 29, 44, 71, 89, 123, 167, 197, 204, 259, 273, 279,
    362, 410, 420, 483, 519, 700, 705, 800, 854, 887, 971, 1032, 1259,
    1297, 1421, 1518,
)
TARGET = 1533


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def apply(matrix, vector):
    return [dot(row, vector) for row in matrix]


def main():
    n = len(P)
    h = P[-1] - P[0]
    differences = [P[j] - P[i] for i in range(n) for j in range(i + 1, n)]
    assert len(set(differences)) == len(differences)
    triples = sorted(
        (u for u in combinations(range(n), 3) if sum(P[i] for i in u) == TARGET), key=max
    )
    assert triples == [(13, 18, 24), (0, 14, 28), (1, 3, 31)]
    r_total = len(triples)
    endpoints = sorted(i for triple in triples for i in triple)
    assert len(set(endpoints)) == 3 * r_total
    center = F(TARGET, 3)
    means = [F(P[0])] + [F(sum(P[:j]), j) for j in range(1, n)]
    x = [(F(a) - center) / h for a in P]
    mu = [(m - center) / h for m in means]
    lag = [a - m for a, m in zip(x, mu)]
    times = [a + m for a, m in zip(x, mu)]
    q = [[mu[j] - x[i] if i < j else F(0) for i in range(n)] for j in range(n)]
    qt = [list(row) for row in zip(*q)]
    e = [F(int(i in endpoints), r_total) for i in range(n)]
    assert sum(e) == 3 and dot(e, x) == 0 and all(a >= 0 for a in e)
    lambdas = [2 * mu[max(triple)] for triple in triples]
    xis = [[F(0)] * n]
    for r in range(1, r_total + 1):
        completed = {i for triple in triples[:r] for i in triple}
        xis.append([F(int(i in completed)) - r * e[i] for i in range(n)])
    deltas = {r: lambdas[r] - lambdas[r - 1] for r in range(1, r_total)}
    assert all(delta >= 0 for delta in deltas.values())
    rho = [sum((r - 1) * deltas[r] * xis[r][i] for r in deltas) for i in range(n)]
    assert sum(rho) == 0 and dot(rho, x) == 0
    qe = apply(q, e)
    qte = apply(qt, e)
    a_self = sum(e[i] * x[i] * qe[i] for i in range(n))
    b_self = dot(e, qe)
    distance = sum(e[i] * e[j] * abs(times[i] - times[j]) for i in endpoints for j in endpoints)
    assert b_self == distance / 4 - (3 - F(1, r_total)) * dot(e, lag) / 2
    choose_r = F(r_total * (r_total - 1), 2)
    lambda_total = sum(r * lambdas[r] for r in range(r_total))
    base = choose_r * a_self + lambda_total * b_self
    original_mean = base - sum(
        (r - 1) * deltas[r] * dot(xis[r], qte) for r in deltas
    )
    assert original_mean == F(140483860774477, 912870110401704)
    endpoint_drift = F(0)
    for k, i in enumerate(endpoints, 1):
        discrepancy = mu[i] - sum(x[j] for j in endpoints[:k - 1]) / (k - 1) if k > 1 else F(0)
        assert qe[i] == F(k - 1, r_total) * discrepancy
        endpoint_drift += F(k - 1, r_total**2) * discrepancy * (
            choose_r * x[i] + lambda_total + r_total * rho[i]
        )
    assert endpoint_drift == base + dot(rho, qe)

    f_norm = cross = gram = completed_gram = F(0)
    for k in range(1, len(endpoints)):
        width = times[endpoints[k]] - times[endpoints[k - 1]]
        assert width > 0
        f_value = -F(k - 1, r_total)
        rho_tail = sum(rho[i] for i in endpoints[k:])
        cross += width * rho_tail * f_value
        f_norm += width * f_value**2
        for r in deltas:
            xi_tail = sum(xis[r][i] for i in endpoints[k:])
            completed_count = sum(i in {j for triple in triples[:r] for j in triple} for i in endpoints[:k])
            assert xi_tail == F(r * k, r_total) - completed_count
            gram += deltas[r] * width * xi_tail**2 / 4
            completed_gram += deltas[r] * width * (xi_tail + 2 * (r - 1) * f_value)**2 / 4
    clock_second_moment = sum((r - 1)**2 * deltas[r] for r in deltas)
    residual = endpoint_drift - clock_second_moment * f_norm
    assert original_mean == endpoint_drift + cross
    assert gram + original_mean == completed_gram + residual
    assert completed_gram >= 0 and abs(residual) <= 52 * r_total**2

    columns = [sum(q[j][i] for j in range(n)) for i in range(n)]
    outside_columns = [sum(q[j][i] for j in range(n) if j not in endpoints) for i in range(n)]
    aggregate = [value / r_total for value in rho]
    outside = dot(rho, outside_columns) / r_total
    assert original_mean == base + outside - dot(columns, aggregate)
    automatic = dot(columns, columns) / 2
    shifted_columns = [a - b for a, b in zip(columns, aggregate)]
    automatic_residual = base + outside - dot(aggregate, aggregate) / 2
    assert automatic + original_mean == dot(shifted_columns, shifted_columns) / 2 + automatic_residual

    print('N=32; fixed complete sum=1533; fiber size=3; actual Sidon and disjointness: PASS')
    print(f'positive_e_mass={sum(e)}; e_x_moment={dot(e, x)}')
    print(f'original_full_mean={original_mean}')
    print(f'endpoint_drift={endpoint_drift}')
    print(f'tail_cross_term={cross}')
    print(f'original_gram={gram}')
    print(f'completed_gram={completed_gram}')
    print(f'clock_second_moment={clock_second_moment}')
    print(f'e_tail_square_norm={f_norm}')
    print(f'signed_endpoint_residual={residual}')
    print('positive-mass self identity, endpoint discrepancy, full mean, completed square, and automatic-column identity: PASS')
    print('One fixed identity check; no unrestricted sign search or asymptotic conclusion.')


if __name__ == '__main__':
    main()
