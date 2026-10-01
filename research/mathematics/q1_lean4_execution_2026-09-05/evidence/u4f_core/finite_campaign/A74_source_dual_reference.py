#!/usr/bin/env python3
"""One-copy source penalties plus exact node matching duals on two saved cells."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib
import json
from A70_feasible_matching_reference import assignment_dual

HERE = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
INPUTS = ['A70_FEASIBLE_MATCHING_EXACT.json', 'A72_SOURCE_ALLOWANCE_COUNTEREXAMPLE.json']

def calculate(path):
    source = json.loads(path.read_text())
    old, future = source['old_values'], source['future_values']
    ac = old[0] + source['H_c']
    fresh = [ac - x for x in old]
    bank = 0
    permitted = {}
    for z in range(len(old)):
        for w in range(z):
            g = old[z] - old[w]
            permitted[w,z] = sorted(fresh[x] for x in range(len(old)) if x not in [w,z])
            bank += sum(g*max(h-g,0) for h in permitted[w,z])
    beta = source.get('actual_Beta')
    if beta is None:
        assert source['core_records'] == 1
        row = source['selected_record']
        assert row[3] == source['c']
        beta = row[1] * row[-1]
    cases = []
    for numerator, denominator in [(0,1),(1,2),(1,1)]:
        nodes = []
        matching_sum = 0
        for z in range(len(old)):
            for q in range(len(future)):
                N = max(z,q)
                weights = [[0]*N for _ in range(N)]
                for w in range(z):
                    g = old[z]-old[w]
                    for j in range(q):
                        t = future[q]-future[j]
                        h = next((h for h in permitted[w,z] if h>=g+t), None)
                        if h is not None:
                            weights[w][j] = max(denominator*g*t - numerator*g*(h-g),0)
                left,right,assignment = assignment_dual(weights)
                value = sum(left)+sum(right)
                assert value == sum(weights[i][assignment[i]] for i in range(N))
                matching_sum += value
                nodes.append(dict(z=z+1,q=q+1,value_scaled=value,dual_left=left,
                                  dual_right=right,assignment=assignment))
        upper = Q(numerator*bank + matching_sum, denominator)
        assert beta <= upper
        if numerator == denominator:
            assert matching_sum == 0 and upper == bank
        cases.append(dict(theta=str(Q(numerator,denominator)),numerator=numerator,
                          denominator=denominator,matching_sum_scaled=matching_sum,
                          bound_exact=str(upper),nodes=nodes))
    return dict(input=path.name,input_sha256=sha(path),B_source_positive=bank,
                actual_Beta=beta,old_values=old,future_values=future,ac=ac,cases=cases,
                minimum_tested_bound_exact=str(min(Q(x['bound_exact']) for x in cases)))

def main():
    cases = [calculate(HERE/name) for name in INPUTS]
    result = dict(attempt='A74',status='EXACT_FINITE_SOURCE_DUAL_CERTIFICATES',
                  cases=cases,source_sha256={p.name:sha(p) for p in
                      [Path(__file__),HERE/'A70_feasible_matching_reference.py',*(HERE/n for n in INPUTS)]},
                  limits=['Two existing cells only; no new history or full profile.',
                          'The dual bounds positive boundary, not the entire original product mass.',
                          'No all-history summable profile estimate is established.',
                          'Every original k>T component and alpha_(M+1) are retained in the general inequality.'])
    (HERE/'A74_SOURCE_DUAL_EXACT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps([dict(input=c['input'],Bsrc=c['B_source_positive'],actual_Beta=c['actual_Beta'],
                           bounds=[(s['theta'],s['bound_exact']) for s in c['cases']]) for c in cases]))

if __name__=='__main__':
    main()
