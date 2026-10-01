#!/usr/bin/env python3
"""One prescribed fixed-cap Sidon witness to Phi_H<=UG, with nonempty core.

Reuse the existing full evaluator and independent output-oriented checker.
Auxiliary matchings certify only a lower bound on the A70 upper allowance.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import hashlib
import json
from reference_evaluator import evaluate, log_bounds, rank_core, physical_core
from independent_checker import check, log_fixed, SCALE, rank_conditions, output_condition

HERE = Path(__file__).resolve().parent
NAME = 'C2pow67_m02_prescribed_allowance_M50'
L, C = 1 << 60, Q(1 << 67)
c, b, k, M = 24, 25, 50, 50
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
base = [None, 0] + list(range(98, 121)) + [300] + [400 + 4*j for j in range(25)]
perturb = [0] + [1 << j for j in range(1, 51)]
perturb[42] = perturb[24] + perturb[8] + perturb[40] - perturb[4] - perturb[20]
a = [None] + [L*base[j] + perturb[j] - 1 for j in range(1, 51)]
assert len(a) == 51 and a[1] == 1
assert a[50]-a[1] < 512*L == 4*C
# For n>=2, log(2n)>=log4>1, so the single fixed cap also follows
# from H_n<4C<=Cn^2; the evaluator independently certifies each rank.
result, rows = evaluate(a[1:], NAME, C, 2)
hp, rp = HERE/(NAME+'.json'), HERE/(NAME+'_records.json')
hp.write_text(json.dumps(result, indent=2)+'\n')
rp.write_text(json.dumps({'columns':['d','e','p_d','q_d','p_e','q_e','c','s','i','r','t'],
                         'records':rows}, separators=(',', ':'))+'\n')
check(hp)
row = [a[24]-a[4], a[20]-a[8], 4,24,8,20,24,20,40,42,a[42]-a[40]]
assert row in rows and row[0]-row[1] == row[-1]

def fixed_bounds(n):
    lo, hi = log_fixed(n)
    return Q(lo, SCALE), Q(hi, SCALE)

def flags(bounds):
    d,e,x,y,w,z,cc,s,i,r,t = row
    lb,_ = bounds(b)
    lc,_ = bounds(c)
    gaps = [v-u for u,v in zip(sorted([a[x],a[y],a[w],a[z]]),
                              sorted([a[x],a[y],a[w],a[z]])[1:])]
    delay = (i-c)**2*min(c,r-c)
    margins = {
        'A43_not_short_component': (k-b)**4*lb**3-b**4,
        'A42_not_cut_far': b**8*lb**5-(k-1)**8,
        'A33_not_cut_span_far': (a[b]-a[1])*lb**2-(a[k]-a[1]),
        'A45_large_smaller_source': e**4*lb**5-b**8,
        'A46_large_output': t**2*lb**5-b**4,
        'A46_large_min_old_gap': min(gaps)**2*lb**5-b**4,
        'A45_source_upper_rank': s**8*(2*C)**4*lb**9-b**8,
        'A53_not_birth_far': c**8*lc**5-(k-1)**8,
        'A54_not_birth_span_far': (a[c]-a[1])*lc**2-(a[k]-a[1]),
        'A57_reverse_delay_product': delay**4*lc**9-c**12,
    }
    assert all(m > 0 for m in margins.values())
    return {name: str(value) for name,value in margins.items()}

assert rank_core(c,20,40,42) is True and physical_core(c,row[-1]) is True
assert rank_conditions(c,20,40,42) and output_condition(c,row[-1])
g = row[1]
center = a[c]-g
mirror = 2*center-a[4]
assert mirror not in a[1:c]
triples = [list(xs) for xs in combinations(range(1,c),3) if sum(a[x] for x in xs) == 3*center]
assert not triples  # the retained record is outside the A64 support

old, future, H = a[1:c], a[b+1:k+1], a[c]-a[1]
nodes = []
for z in range(1,len(old)+1):
    for q in range(1,len(future)+1):
        available = list(range(1,q))
        matching, value = [], 0
        for w in range(1,z):
            g0 = old[z-1]-old[w-1]
            for j in available:
                t0 = future[q-1]-future[j-1]
                if g0+t0 <= H:
                    matching.append([w,j])
                    value += g0*t0
                    available.remove(j)
                    break
        nodes.append(dict(z=z,q=q,matching=matching,value=value))
lower = sum(node['value'] for node in nodes)
U = sum(old[z]-old[w] for z in range(len(old)) for w in range(z))
G = sum(a[c]-x for x in old)
assert lower > U*G
alpha = lambda n: Q(1,n*n*(n-1)**2)
lam = (alpha(k)-alpha(k+1))/(a[k]-a[1])**2
u42 = sum(((alpha(j)-alpha(j+1))/(a[j]-a[1])**2 for j in range(42,M+1)), Q(0))
record_price = row[0]*row[1]*u42
out = dict(attempt='A72', status='EXACT_FINITE_ALLOWANCE_COUNTEREXAMPLE',
           claim_refuted='Phi_H(c,b,k)<=U(c)*G(c) for every actual fixed-cap Sidon history, even on the displayed near-birth/span domain.',
           campaign=NAME,C_exact=str(C),m0=2,M=M,T=M,c=c,b=b,k=k,
           construction=dict(L=L,base_values=base[1:],perturbations=perturb[1:],
                             exceptional_perturbation_index=42,
                             preserved_relation='a24+a8+a40=a4+a20+a42'),
           old_values=old,future_values=future,H_c=H,nodes=nodes,
           Phi_H_feasible_lower=lower,U=U,G=G,UG=U*G,
           positive_margin=lower-U*G,ratio_exact=str(Q(lower,U*G)),
           selected_record=row,selected_record_original_cut_interval=[25,39],
           selected_record_original_u42_exact=str(u42),
           selected_record_full_price_exact=str(record_price),
           lambda50_exact=str(lam),selected_record_component50_exact=str(row[0]*row[1]*lam),
           selected_record_residual_flags=dict(reference=flags(log_bounds),independent=flags(fixed_bounds)),
           missing_mirror_value=mirror,F3_rank_triples=triples,
           core_records=result['core_records'],N_approx=result['N_approx'],
           cap_use_max_approx=result['cap_use_max_approx'],UNKNOWN=0,
           source_sha256={p.name:sha(p) for p in [Path(__file__),HERE/'reference_evaluator.py',
               HERE/'independent_checker.py',hp,rp,HERE/(NAME+'_independent_check.json')]},
           limits=['One fixed C,m0 finite history, not an unbounded family or a Q1 counterexample.',
                   'The feasible matching values are auxiliary allowance values, not physical record masses.',
                   'All displayed residual flags hold for one actual record; unspecified paid initial ranks are not claimed to be surpassed.',
                   'This rejects the coefficient-one comparison, not the valid A70 upper bound or a different uniform norm proof.',
                   'N and square roots are presentation approximations; rational profiles and I_j are independently certified.'])
(HERE/'A72_SOURCE_ALLOWANCE_COUNTEREXAMPLE.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({key:out[key] for key in ['status','Phi_H_feasible_lower','UG','positive_margin','core_records','N_approx','cap_use_max_approx','UNKNOWN']}))
