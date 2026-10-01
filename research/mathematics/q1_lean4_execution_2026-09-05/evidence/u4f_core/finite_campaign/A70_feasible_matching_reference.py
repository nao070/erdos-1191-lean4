#!/usr/bin/env python3
"""Exact A70 allowance, with integer assignment duals for independent checking.

Only the existing A65 residual cell is used; no history/profile is generated.
The auxiliary matching graph permits every g+t<=H_c edge. It does not claim
that its maximizing edges are physical records or actual fresh labels.
"""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import hashlib
import json

HERE = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

def assignment_dual(weights):
    """Square minimum-cost assignment on -weights; return checked max duals."""
    n = len(weights)
    if not n:
        return [], [], []
    cost = [[-w for w in row] for row in weights]
    u, v, p, way = ([0] * (n + 1) for _ in range(4))
    for i in range(1, n + 1):
        p[0] = i
        j0 = 0
        minimum = [None] * (n + 1)
        used = [False] * (n + 1)
        while True:
            used[j0] = True
            i0 = p[j0]
            delta, j1 = None, 0
            for j in range(1, n + 1):
                if not used[j]:
                    cur = cost[i0 - 1][j - 1] - u[i0] - v[j]
                    if minimum[j] is None or cur < minimum[j]:
                        minimum[j], way[j] = cur, j0
                    if delta is None or minimum[j] < delta:
                        delta, j1 = minimum[j], j
            assert delta is not None
            for j in range(n + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                elif minimum[j] is not None:
                    minimum[j] -= delta
            j0 = j1
            if not p[j0]:
                break
        while j0:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
    assignment = [0] * n
    for j in range(1, n + 1):
        assignment[p[j] - 1] = j - 1
    left, right = [-x for x in u[1:]], [-x for x in v[1:]]
    assert all(left[i] + right[j] >= weights[i][j]
               for i in range(n) for j in range(n))
    assert sum(left) + sum(right) == sum(weights[i][assignment[i]] for i in range(n))
    return left, right, assignment

def main():
    hp = HERE / 'C1_m02_dense_variant1_M96.json'
    rp = HERE / 'A65_SPARSE_FIBER_FOLLOWUP_EXACT.json'
    ap = HERE / 'A69_TAIL_ALLOWANCE_EXACT.json'
    records, prior = json.loads(rp.read_text()), json.loads(ap.read_text())
    assert sha(hp) == records['source_sha256'][hp.name]
    assert sha(rp) == prior['source_sha256'][rp.name]
    a = [None] + json.loads(hp.read_text())['a']
    c, b, k = 24, 25, 48
    old, future, H = a[1:c], a[b + 1:k + 1], a[c] - a[1]
    assert old == prior['old_values'] and future == prior['future_values']
    beta = defaultdict(int)
    rows = [x for x in records['records'] if x['category'] != 'paid_sparse_support']
    assert len(rows) == 125
    for item in rows:
        D, e, x, y, w, z, cc, s, i, r, t = item['record']
        assert cc == c
        if y == c:
            beta[z, r - b] += e * t
    nodes = []
    for z in range(1, len(old) + 1):
        for q in range(1, len(future) + 1):
            G = [old[z - 1] - old[w - 1] for w in range(1, z)]
            T = [future[q - 1] - future[j - 1] for j in range(1, q)]
            # G and T are decreasing; infeasible T vertices stay for later G.
            available = set(range(len(T)))
            matching = []
            value = 0
            for w, g in enumerate(G):
                candidates = [j for j in sorted(available) if g + T[j] <= H]
                if candidates:
                    j = candidates[0]
                    available.remove(j)
                    matching.append([w + 1, j + 1])
                    value += g * T[j]
            N = max(len(G), len(T))
            matrix = [[G[w] * T[j] if w < len(G) and j < len(T)
                       and G[w] + T[j] <= H else 0 for j in range(N)] for w in range(N)]
            left, right, assignment = assignment_dual(matrix)
            assert value == sum(left) + sum(right)
            unrestricted = sum(g * t for g, t in zip(G, T))
            assert beta[z, q] <= value <= unrestricted
            nodes.append(dict(z=z, q=q, matching=matching, value=value,
                              dual_left=left, dual_right=right, assignment=assignment,
                              actual_positive_charge=beta[z, q], unrestricted=unrestricted))
    Phi_H = sum(node['value'] for node in nodes)
    assert Phi_H == 80331512
    assert sum(beta.values()) == prior['actual_Beta'] == 8716524
    assert sum(node['unrestricted'] for node in nodes) == prior['Phi']
    lam = Fraction(4, k * (k*k - 1)**2 * (a[k] - a[1])**2)
    out = dict(attempt='A70', status='EXACT_FINITE_MATCHING_DUAL_CERTIFICATE',
               scope=dict(C_exact='1', m0=2, M=96, T=96, c=c, b=b, k=k,
                          certified_records_reused=125, new_histories=0, full_profile_evaluations=0),
               old_values=old, future_values=future, H_c=H, nodes=nodes,
               Phi_H=Phi_H, Phi=prior['Phi'], UG=prior['UG'], actual_Beta=sum(beta.values()),
               lambda48_exact=str(lam), priced_Phi_H_exact=str(Phi_H * lam),
               source_sha256={p.name: sha(p) for p in [Path(__file__), hp, rp, ap]},
               limits=['Only the one prescribed actual cell; no uniform K conclusion.',
                       'Auxiliary maximizing edges need not have actual fresh-label membership.',
                       'Positive boundary only; original old-g-square mass remains separate.',
                       'Prices refer to genuine component48, not a substituted full u_r.'])
    (HERE / 'A70_FEASIBLE_MATCHING_EXACT.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({key: out[key] for key in ['status', 'Phi_H', 'Phi', 'UG', 'actual_Beta']}))

if __name__ == '__main__':
    main()
