#!/usr/bin/env python3
"""One fixed-cap actual strict-core counterexample to degree <= 2*m.

The existing reference evaluator and independent full-profile checker are
reused unchanged. This finite witness does not refute uniform K(C,m0).
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement
from collections import defaultdict
import hashlib
import json

from reference_evaluator import evaluate
from independent_checker import check

HERE = Path(__file__).resolve().parent
NAME = 'C10pow35_m02_prescribed_pair_degree_M45'
L = 10**35
C = Q(L)
F = [1000 * 10**j for j in range(8)]
chosen = list(combinations(range(1, 8), 2))[:17]
old = [1, 3*L+1]
construction = []
for e, (i, r) in enumerate(chosen):
    z = 1000 * 10**(10+e)
    t = F[r]-F[i]
    p, q = L+z+1, 2*L+t-z+1
    old.extend([p, q])
    construction.append(dict(e=e, future_indices_zero_based=[i,r], z=z, t=t, p=p, q=q))
a = sorted(old) + [7*L//2+1] + [4*L+f+1 for f in F]
assert len(a) == 45 and a[0] == 1 and a[-1]-1 < 5*L
assert len(set(a[i]+a[j] for i,j in combinations_with_replacement(range(45),2))) == 1035
result, rows = evaluate(a, NAME, C, 2)
hp, rp = HERE/(NAME+'.json'), HERE/(NAME+'_records.json')
hp.write_text(json.dumps(result, indent=2)+'\n')
rp.write_text(json.dumps(dict(columns=['d','e','p_d','q_d','p_e','q_e','c','s','i','r','t'],
                             records=rows), separators=(',', ':'))+'\n')
check(hp)

# Vertex U is the one physical outer old pair; seventeen distinct nested
# neighbours each have a prescribed future output and a strict-core channel.
b, k, hub = 37, 45, (1,36)
rank = {v:i+1 for i,v in enumerate(a)}
witnesses = []
for item in construction:
    p, q, t = item['p'], item['q'], item['t']
    i0, r0 = item['future_indices_zero_based']
    i, r = 38+i0, 38+r0
    record = [q-1, 3*L+1-p, 1, rank[q], rank[p], 36, 36, rank[q], i, r, t]
    assert record in rows and record[0]-record[1] == t
    assert 36 < b < i < r <= k
    assert p+q-(a[0]+a[35]) == t == a[r-1]-a[i-1]
    witnesses.append(dict(neighbour=[rank[p],rank[q]], record=record,
                          original_cut_interval=[37,i-1], original_product=record[0]*record[1]))
assert len({tuple(w['neighbour']) for w in witnesses}) == 17 > 2*8

# Directly reconstruct all graph neighbours of this hub from actual sums;
# this distinguishes an exact degree from a lower certificate alone.
future_diff = {a[r-1]-a[i-1]:(i,r) for i,r in combinations(range(b+1,k+1),2)}
neighbours = []
strict_neighbours = set()
for v,w in combinations(range(2,36),2):
    t = abs(a[v-1]+a[w-1]-a[0]-a[35])
    if t in future_diff:
        neighbours.append([v,w])
for row in rows:
    d,e,x,y,w,z,c,s,i,r,t = row
    if c < b < i and r <= k:
        left, right = tuple(sorted((y,w))), tuple(sorted((x,z)))
        if left == hub: strict_neighbours.add(right)
        if right == hub: strict_neighbours.add(left)
assert len(neighbours) == 17 and len(strict_neighbours) == 17

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
out = dict(attempt='A82', status='EXACT_FINITE_COUNTEREXAMPLE',
           claim_refuted='Every old-pair vertex has degree at most twice the number of future points, even for original strict-core edges.',
           campaign=NAME, C_exact=str(C), m0=2, M=45, T=45, b=b, k=k,
           old_count=36, future_count=8, hub=list(hub), degree=17,
           strict_core_degree=17, proposed_upper=16, positive_integer_margin=1,
           construction=dict(L=L, future_offsets=F, neighbours=construction,
                             cut_point=7*L//2+1),
           witnesses=witnesses, all_neighbours=neighbours,
           core_records=result['core_records'], N_approx=result['N_approx'],
           cap_use_max_approx=result['cap_use_max_approx'], UNKNOWN=0,
           source_sha256={p.name:sha(p) for p in [Path(__file__), HERE/'reference_evaluator.py',
               HERE/'independent_checker.py', hp, rp, HERE/(NAME+'_independent_check.json')]},
           scope=['One prescribed fixed C,m0 finite history; no family with unbounded profile is asserted.',
                  'All seventeen displayed edges have an original strict-core channel. Later residual deletions and eventual initial-cut thresholds are not claimed to be survived.',
                  'All-rank cap, rational profile, original coverage and genuine terminal prices are checked by reused independent methods.',
                  'N, block square roots and cap usage are presentation approximations; exact profile and I_j are in the campaign file.'])
(HERE/'A82_TWO_FUTURE_DEGREE_COUNTEREXAMPLE.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({key:out[key] for key in ['status','degree','strict_core_degree','proposed_upper','core_records','N_approx','cap_use_max_approx','UNKNOWN']}))
