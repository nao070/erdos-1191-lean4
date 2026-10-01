#!/usr/bin/env python3
"""Exact-membership graph versus independently enumerated physical sources."""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import hashlib, json

HERE = Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def run(name):
    p = HERE / name
    data = json.loads(p.read_text())
    old, future = data['old_values'], data['future_values']
    ac = old[0] + data['H_c']
    fresh = {ac-a: x for x,a in enumerate(old)}
    nodes = defaultdict(list)
    source_mass = defaultdict(int)
    graph = set()
    for z in range(len(old)):
        for q in range(len(future)):
            for w in range(z):
                g = old[z]-old[w]
                for j in range(len(future)):
                    if j == q: continue
                    h = g+future[q]-future[j]
                    x = fresh.get(h)
                    if x is None or x in [w,z]: continue
                    record = (w+1,z+1,x+1,j+1,q+1,g,h)
                    graph.add(record)
                    nodes[z+1,q+1].append(record)
                    source_mass[w+1,z+1] += g*h
    for edges in nodes.values():
        assert len(edges)==len({r[0] for r in edges})==len({r[3] for r in edges})==len({r[2] for r in edges})
    assert len(graph)==len({r[:3] for r in graph})
    # Independent direction: enumerate physical sources, then retrieve outputs.
    differences = {}
    for lo in range(len(future)):
        for hi in range(lo+1,len(future)):
            t = future[hi]-future[lo]
            assert t not in differences
            differences[t] = (lo,hi)
    other = set()
    banks = {}
    for z in range(len(old)):
        for w in range(z):
            g=old[z]-old[w]
            banks[w+1,z+1] = g*sum(ac-old[x] for x in range(len(old)) if x not in [w,z])
            for x in range(len(old)):
                if x in [w,z]: continue
                h=ac-old[x]; hit=differences.get(abs(h-g))
                if hit is None: continue
                lo,hi=hit
                j,q=(lo,hi) if h>g else (hi,lo)
                other.add((w+1,z+1,x+1,j+1,q+1,g,h))
    assert graph==other
    Q=sum(r[-2]*r[-1] for r in graph)
    assert Q==sum(source_mass.values())
    assert all(source_mass[g]<=s for g,s in banks.items())
    a76=json.loads((HERE/'A76_FULL_MASS_EXACT.json').read_text())
    prior=next(r for r in a76['results'] if r['input']==name)
    assert prior['six_distinct_source_bank']==sum(banks.values())
    assert Q>=prior['full_actual_product']
    D0=Fraction(prior['cases'][0]['bound_exact'])
    assert D0>=Q
    return {'input':name,'input_sha256':sha(p),'exact_unfiltered_records':len(graph),
            'exact_unfiltered_mass':Q,'selected_residual_mass':prior['full_actual_product'],
            'source_bank':sum(banks.values()),'A76_threshold_bound_theta0':str(D0),
            'threshold_excess_over_exact_mass':str(D0-Q),
            'exact_mass_excess_over_selected':Q-prior['full_actual_product'],
            'records':[list(r) for r in sorted(graph)],
            'source_slacks':[{'w':w,'z':z,'S_g':s,'Q_g':source_mass[w,z],'slack':s-source_mass[w,z]}
                             for (w,z),s in sorted(banks.items())],
            'scalar_exact_domain_bounds':{str(t):str(Q+t*(sum(banks.values())-Q))
                                          for t in [Fraction(0),Fraction(1,2),Fraction(1)]}}

if __name__=='__main__':
    result={'attempt':'A77','status':'EXACT_FINITE','results':[run(n) for n in
            ['A70_FEASIBLE_MATCHING_EXACT.json','A72_SOURCE_ALLOWANCE_COUNTEREXAMPLE.json']],
            'source_sha256':{Path(__file__).name:sha(Path(__file__)),
                             'A76_FULL_MASS_EXACT.json':sha(HERE/'A76_FULL_MASS_EXACT.json')},
            'scope':'Original six distinct endpoints and causal order, both orientations; original strict log gates and residual selectors are not imposed on this enlarged graph. No new history, cap, profile, optimization or Lean claim.'}
    (HERE/'A77_EXACT_MEMBERSHIP.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps([{k:v for k,v in r.items() if k not in ['records','source_slacks','scalar_exact_domain_bounds']} for r in result['results']]))
