"""Check one graph-defect identity on already-certified finite campaign data.

No search or new admissibility evaluator. All arithmetic in identities is exact;
the three displayed ratios alone are approximate.
"""
from pathlib import Path
from fractions import Fraction as F
import json
import hashlib

HERE = Path(__file__).resolve().parent
D = HERE / 'finite_campaign'
out = []
for name in ['C1_m02_greedy_M96', 'C1_m02_dense_variant1_M96']:
    source = D / (name + '.json')
    data = json.loads(source.read_text())
    a = data['a']
    M = len(a)
    records = json.loads((D / (name + '_records.json')).read_text())['records']
    u = {r: sum(((F(1, k*k*(k-1)**2) - F(1, k*k*(k+1)**2)) /
                 (a[k-1]-a[0])**2 for k in range(r, M+1)), F(0))
         for r in range(2, M+1)}
    for b in [8, 16, 32, 64]:
        labels = {a[q]-a[p] for q in range(b-1) for p in range(q)}
        S = sum(d*d for d in labels)
        groups = {}
        for d, e, p, q, pe, qe, c, s, i, r, t in records:
            if c < b < i:
                groups.setdefault((i, r, t), []).append((d, e))
        A = sum((F(r-b-1)*u[r] for r in range(b+2, M+1)), F(0))
        budget = S*A
        boundary = budget
        gradient = F(0)
        profile = F(0)
        maxdeg = 0
        for (i, r, t), edges in groups.items():
            assert len(edges) == len(set(edges))
            degrees = {}
            endenergy = K = 0
            for d, e in edges:
                assert d-e == t and d in labels and e in labels
                degrees[d] = degrees.get(d, 0)+1
                degrees[e] = degrees.get(e, 0)+1
                endenergy += d*d+e*e
                K += d*e
            assert max(degrees.values()) <= 2
            maxdeg = max(maxdeg, max(degrees.values()))
            B = F(S) - F(endenergy, 2)
            G = F(t*t*len(edges), 2)
            assert B >= 0 and K+B+G == S
            boundary -= u[r]*F(endenergy, 2)
            gradient += u[r]*G
            profile += u[r]*K
        assert profile+boundary+gradient == budget
        assert profile == F(data['profile_exact'].get(str(b), '0'))
        out.append({
            'history': name, 'b': b, 'output_fibers_with_core': len(groups),
            'max_degree': maxdeg, 'profile': str(profile),
            'full_degree_budget': str(budget), 'boundary_defect': str(boundary),
            'edge_gradient_defect': str(gradient), 'identity_exact': True,
            'ratios_approx': {k: float(v/budget) for k, v in
                             [('profile', profile), ('boundary', boundary),
                              ('gradient', gradient)]},
            'input_sha256': hashlib.sha256(source.read_bytes()).hexdigest()
        })
(HERE / 'graph_defect_checks.json').write_text(json.dumps({
    'scope': '8 cuts of two previously certified histories; no uniform theorem',
    'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'checks': out
}, indent=2)+'\n')
for row in out:
    print(row['history'], row['b'], row['ratios_approx'])
