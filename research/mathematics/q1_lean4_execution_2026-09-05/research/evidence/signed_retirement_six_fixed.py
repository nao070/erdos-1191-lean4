#!/usr/bin/env python3
"""One exact actual six-point signed retirement/core identity check."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations

POINTS = (0, 13, 29, 35, 37, 40)


def main():
    p = POINTS
    two_sums = [p[i]+p[j] for i in range(len(p)) for j in range(i,len(p))]
    assert len(two_sums) == len(set(two_sums))
    bank = {}
    for j in range(len(p)):
        for i in range(j):
            d = p[j]-p[i]
            assert d not in bank
            bank[d] = (j,i,j+1)
            bank[-d] = (i,j,j+1)
    direct = defaultdict(int)
    pairs = defaultdict(list)
    repeated = 0
    for d,e in combinations(sorted(bank),2):
        t = e-d
        if t not in bank:
            continue
        di,dj,db = bank[d]
        ei,ej,eb = bank[e]
        n,m,r = bank[t]
        b = max(db,eb)
        if r <= b:
            continue
        left = tuple(sorted((ei,dj,m)))
        right = tuple(sorted((di,ej,n)))
        assert sum(p[i] for i in left) == sum(p[i] for i in right)
        assert not set(left).intersection(right)
        if len(set(left+right)) != 6:
            repeated += d*e
            continue
        assert max(left)<max(right)
        direct[(left,right)] += d*e
        pairs[(left,right)].append((d,e,t,b,r,d*e))
    fibers=defaultdict(list)
    for u in combinations(range(len(p)),3):
        fibers[sum(p[i] for i in u)].append(u)
    formula=defaultdict(Fraction)
    for s,rows in fibers.items():
        for u,v in combinations(sorted(rows,key=max),2):
            assert not set(u).intersection(v)
            n=max(p[i] for i in v)
            center=Fraction(s,3)
            su=sum((p[i]-center)**2 for i in u)
            sv=sum((p[i]-center)**2 for i in v)
            formula[(u,v)] = 2*su+6*sv-12*(n-center)**2
    assert dict(direct)==dict(formula)
    assert len(direct)==1
    key=next(iter(direct))
    assert direct[key]==4008 and len(pairs[key])==12
    assert all(b==5 and r==6 for d,e,t,b,r,w in pairs[key])
    print(f'points={p}; repeated-sum Sidon: PASS')
    print(f'positive_difference_labels={sorted(d for d in bank if d>0)}')
    print(f'equal_sum_fiber_pairs={len(direct)}; shared_sum=77')
    print(f'U={tuple(p[i] for i in key[0])}; V={tuple(p[i] for i in key[1])}')
    print(f'six_distinct_direct={direct[key]}; centered_formula={formula[key]}')
    print('complete core pair records (d,e,output,source_birth,output_birth,product):')
    for pair in pairs[key]:
        print(pair)
    print(f'repeated_endpoint_retirement={repeated}; full_retirement={sum(direct.values())+repeated}')
    print('Actual finite six-endpoint sign counterexample and formula identity: PASS')
    print('No parameter sweep, cap-preserving infinite history, asymptotic bound, or Lean claim.')


if __name__=='__main__':
    main()
