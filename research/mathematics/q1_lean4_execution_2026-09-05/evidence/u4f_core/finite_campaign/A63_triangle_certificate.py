#!/usr/bin/env python3
"""One algebraically prescribed triangle; a separate fixed C=2,m0=2 campaign.

Reuse the original evaluator and the separately written fixed-point log checker.
This is a finite counterexample to a displayed-residual forest claim, not to Q1.
"""
from pathlib import Path
from fractions import Fraction as Q
import hashlib, json
from reference_evaluator import evaluate, differences, log_bounds, rank_core, physical_core
from independent_checker import check, log_fixed, SCALE, rank_conditions, output_condition

HERE = Path(__file__).resolve().parent
NAME = 'C2_m02_prescribed_triangle_M19'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

# These nine prescribed values realize the algebra with K=399,g=200,
# t1=20,t2=46. Fill the two specified rank intervals, keeping all nine.
seed = [1,201,353,379,465,599,1999,2019,2065]
a = seed[:]
fillers = []
def is_sidon(v):
    ds = [y-x for j,y in enumerate(v) for x in v[:j]]
    return len(ds) == len(set(ds))
for lower,upper,number in [(2,598,5),(600,1998,5)]:
    selected = []
    for x in range(lower,upper+1):
        if x in a:
            continue
        candidate = sorted(a+[x])
        if is_sidon(candidate):
            a = candidate
            selected.append(x)
            if len(selected) == number:
                break
    assert len(selected) == number
    fillers.append(selected)
assert a == [1,2,4,8,13,26,201,353,379,465,599,607,622,636,652,669,1999,2019,2065]
result, records = evaluate(a, NAME, Q(2), 2)
path = HERE/(NAME+'.json')
path.write_text(json.dumps(result,indent=2)+'\n')
rp = HERE/(NAME+'_records.json')
rp.write_text(json.dumps({'columns':['d','e','p_d','q_d','p_e','q_e','c','s','i','r','t'], 'records':records},separators=(',',':'))+'\n')
check(path)  # Repeated two-sum and output-based independent full reconstruction.

A = [None]+a
b,k,c,g,C = 12,19,11,200,Q(2)
K = A[c]-g
expected = [[220,200,9,11,1,7,11,7,17,18,20],
            [246,200,8,11,1,7,11,7,18,19,46],
            [200,134,1,7,10,11,11,7,17,19,66]]
assert all(row in records for row in expected)

def independent_bounds(n):
    lo,hi=log_fixed(n)
    return Q(lo,SCALE),Q(hi,SCALE)

def classify(row, bounds):
    d,e,x,y,w,z,cc,s,i,r,t=row
    assert cc==c and c<b<i<r<=k
    lb,ub=bounds(b);lc,uc=bounds(c)
    old=sorted(A[j] for j in [x,y,w,z])
    gaps=[v-u for u,v in zip(old,old[1:])]
    D=(i-c)**2*min(c,r-c)
    # Every expression is a lower bound for a required strictly positive margin.
    margins={
      'A43_not_short_component':(k-b)**4*lb**3-b**4,
      'A42_not_cut_far':b**8*lb**5-(k-1)**8,
      'A33_not_cut_span_far':(A[b]-A[1])*lb**2-(A[k]-A[1]),
      'A45_large_smaller_source':e**4*lb**5-b**8,
      'A46_large_output':t**2*lb**5-b**4,
      'A46_large_min_old_gap':min(gaps)**2*lb**5-b**4,
      'A45_source_upper_rank':s**8*(2*C)**4*lb**9-b**8,
      'A53_not_birth_far':c**8*lc**5-(k-1)**8,
      'A54_not_birth_span_far':(A[c]-A[1])*lc**2-(A[k]-A[1]),
      'A57_reverse_delay_product':D**4*lc**9-c**12,
    }
    assert all(value>0 for value in margins.values()), margins
    fresh=x if y==c else w
    mirror=2*K-A[fresh]
    assert mirror not in A[1:c]
    return {'strict_positive_margins':{n:str(v) for n,v in margins.items()},
            'old_gaps':gaps,'delay_product':D,'fresh_lower_rank':fresh,
            'missing_old_mirror_value':mirror}

def alpha(n):return Q(1,n*n*(n-1)**2)
lam=(alpha(k)-alpha(k+1))/(A[k]-A[1])**2
cert=[]
for row in expected:
    d,e,x,y,w,z,cc,s,i,r,t=row
    assert rank_core(c,s,i,r) is True and physical_core(c,t) is True
    assert rank_conditions(c,s,i,r) and output_condition(c,t)
    ref=classify(row,log_bounds);ind=classify(row,independent_bounds)
    assert ref['old_gaps']==ind['old_gaps']
    u=sum(((alpha(j)-alpha(j+1))/(A[j]-A[1])**2 for j in range(r,len(a)+1)),Q(0))
    cert.append({'record':row,'reference':ref,'independent':ind,
                 'de':d*e,'original_cut_interval_inclusive':[c+1,i-1],
                 'harmonic_coverage_exact':str(sum((Q(1,j) for j in range(c+1,i)),Q(0))),
                 'original_u_r_exact':str(u),'original_record_price_exact':str(d*e*u),
                 'selected_component19_price_exact':str(d*e*lam)})
cell=[]
for row in records:
    d,e,x,y,w,z,cc,s,i,r,t=row
    if cc!=c or not b<i<r<=k:continue
    old_g=e if y==c else d
    if old_g==g:cell.append(row)
assert sorted(cell)==sorted(expected)
assert A[8]+A[9]+A[10]==3*K
assert sum(x[0]*x[1] for x in expected)==3*g*g
out={'attempt':'A63','date':'2026-09-09','status':'EXACT_FINITE_PASS',
 'campaign':NAME,'C_exact':'2','m0':2,'M':19,'T':19,'a':a,
 'construction':{'prescribed_seed':seed,'fillers':fillers,'no_horizon_extension_claim':True},
 'b':b,'k':k,'c':c,'g':g,'K':K,'actual_output_vertices':[17,18,19],
 'actual_edge_colors':['+','+','-'],'exact_original_cell_edges':len(cell),
 'old_source_triple_values':[A[8],A[9],A[10]],'source_triple_sum':3*K,
 'unpriced_cycle_mass':3*g*g,'lambda19_exact':str(lam),
 'component_cycle_mass_exact':str(3*g*g*lam),
 'records':cert,'UNKNOWN':0,
 'claim_refuted':'Every fixed(c,g;b,k) graph satisfying all displayed A46.6/A53.6/A54.3/A57.4 and mirror deletion is a forest (or bipartite).',
 'scope_limits':['One finite history at fixed C2,m02; not a common-cap infinite family.',
 'Does not exclude an eventual forest theorem above a separately proved threshold.',
 'Displayed residual flags do not assert survival of unspecified already-paid finite initial ranges.',
 'Original full u_r values are retained separately; only component19 is certified in this displayed remainder.',
 'No uniform K, Q1 refutation, certified square-root enclosure or final Lean theorem.'],
 'source_sha256':{p.name:sha(p) for p in [Path(__file__),HERE/'reference_evaluator.py',HERE/'independent_checker.py',path,rp,HERE/(NAME+'_independent_check.json')]}}
(HERE/'A63_RESIDUAL_TRIANGLE_EXACT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'core_records':result['core_records'],'N_approx':result['N_approx'],
 'cap_use_max_approx':result['cap_use_max_approx'],'triangle':expected,'de_sum':3*g*g,'UNKNOWN':0}))
