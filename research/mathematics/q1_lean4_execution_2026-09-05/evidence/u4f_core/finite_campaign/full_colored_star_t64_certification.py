#!/usr/bin/env python3
"""Full unchanged evaluator/checker on the one successful specified campaign."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json
from reference_evaluator import evaluate
from independent_checker import check,rank_conditions,output_condition,log_fixed,SCALE

HERE=Path(__file__).resolve().parent;OUT=HERE/'C100000000000000_m02_colored_star'
candidate=json.loads((OUT/'candidate_t64_trial1.json').read_text())
target=json.loads((OUT/'result.json').read_text())
assert target['status']=='CERTIFIED_SATURATED_JCORE_COUNTEREXAMPLE'
A=candidate['a'];a=[None]+A;M=len(A);b=candidate['b'];t=candidate['t'];C=F(candidate['C_exact'])
assert C==10**14 and candidate['m0']==2 and M==156 and t==64
def save(name,v): (OUT/name).write_text(json.dumps(v,indent=2)+'\n')
bank={a[p]+a[q]:(p,q) for p in (1,2) for q in range(3,t+3)}
assert len(bank)==2*t
fibers=defaultdict(list)
for i in range(b+1,M):
    for s,pair in bank.items():fibers[a[i]+s].append((*pair,i))
def direct_counts(fib):
    assert all(len(v)<=2 for v in fib.values())
    raw=sum(len(v)*(len(v)-1)//2 for v in fib.values())
    core=0
    for triples in fib.values():
        for x,y in combinations(triples,2):
            assert len(set(x+y))==6
            s,c=sorted((x[1],y[1]));i,r=sorted((x[2],y[2]))
            if rank_conditions(c,s,i,r) and output_condition(c,a[r]-a[i]):core+=1
    delta=sum(len(v)*(2-len(v)) for v in fib.values())
    return {'raw_collisions':raw,'core_collisions':core,'delta':delta,
            'E':raw-core,'D_eff':delta+2*(raw-core)}
before=direct_counts(fibers)
for s,pair in bank.items():fibers[a[M]+s].append((*pair,M))
after=direct_counts(fibers)
assert after['raw_collisions']-before['raw_collisions']==88
assert after['core_collisions']-before['core_collisions']==71
assert after['D_eff']-before['D_eff']==-14
large=[];target_rows=[]
for row in target['strict_core_target_collisions']:
    p,q,s,c=row['quad_ranks'];typ=row['type'];i=row['i'];r=row['r']
    gaps=[a[q]-a[p],a[s]-a[q],a[c]-a[s]]
    lo,hi=log_fixed(c)
    assert min(gaps)*lo**3>c*c*SCALE**3
    if typ==2:
        labelpairs=[(a[s]-a[p],p,s),(a[c]-a[q],q,c)]
    else: labelpairs=[(a[s]-a[q],q,s),(a[c]-a[p],p,c)]
    (dd,pd,qd),(ee,pe,qe)=sorted(labelpairs,reverse=True)
    assert dd-ee==row['t']
    target_rows.append([dd,ee,pd,qd,pe,qe,c,s,i,r,row['t']])
    large.append({'quad':row['quad_ranks'],'old_gaps':gaps,'type':typ,'i':i,'r':r,'all_large':True})
uM=(F(1,M*M*(M-1)**2)-F(1,M*M*(M+1)**2))/(a[M]-a[1])**2
extra={'before':before,'after':after,'delta_D_eff':after['D_eff']-before['D_eff'],
       'S':2*t,'d':2,'original_component_horizon':M,'genuine_u_M_exact':str(uM),
       'alpha_M_plus_1_preserved':True,'all_large_target_core_records':len(large),
       'large_target_checks':large,'target_original_11_column_records':target_rows,
       'scope':'Same existing one candidate; exact target deficit and large-gap check, before full-profile certification.'}
save('target_direct_deficit_and_large_gap.json',extra)
print(json.dumps({'stage':'TARGET_DIRECT_DEFICIT_PASS','before':before,'after':after,
      'all_large_target_records':len(large)},indent=2),flush=True)
print('START_UNCHANGED_FULL_REFERENCE_EVALUATOR',flush=True)
data,rows=evaluate(A,'C100000000000000_m02_colored_star_t64_M156',C=C,m0=2)
path=OUT/'C100000000000000_m02_colored_star_t64_M156.json'
save(path.name,data)
save(path.stem+'_records.json',{'columns':['d','e','p_d','q_d','p_e','q_e','c','s','i','r','t'],'records':rows})
assert set(map(tuple,target_rows))<=set(map(tuple,rows))
print(json.dumps({'stage':'REFERENCE_COMPLETE','core_records':len(rows),'N_approx':data['N_approx']}),flush=True)
print('START_UNCHANGED_INDEPENDENT_FULL_CHECKER',flush=True)
check(path)
cert=json.loads(path.with_name(path.stem+'_independent_check.json').read_text())
assert cert['status']=='PASS'
full_large=0
for dd,ee,pd,qd,pe,qe,c,s,i,r,tt in rows:
    p,q,ss,cc=sorted((pd,qd,pe,qe));assert cc==c
    lo,hi=log_fixed(c);min_gap=min(a[q]-a[p],a[ss]-a[q],a[c]-a[ss])
    if min_gap*lo**3>c*c*SCALE**3:full_large+=1
    else:assert min_gap*hi**3<=c*c*SCALE**3
summary={'status':'FULL_PROFILE_INDEPENDENTLY_CERTIFIED','C_exact':str(C),'m0':2,'M':M,'T':M,
 'core_records':len(rows),'all_large_old_gap_core_records':full_large,'N_approx':data['N_approx'],
 'cap_use_max_approx':data['cap_use_max_approx'],'cap_use_argmax':data['cap_use_argmax'],
 'blocks':data['blocks'],'dominant_intervals_by_total_I':data['dominant_intervals_by_total_I'],
 'target_J_core':71,'target_bound':64,'target_D_eff_increment':-14,
 'actual_graph_trials':1,'t96_trials':0,'source_sha256':{str(p.relative_to(HERE)):hashlib.sha256(p.read_bytes()).hexdigest()
     for p in [path,path.with_name(path.stem+'_records.json'),path.with_name(path.stem+'_independent_check.json'),
               OUT/'target_direct_deficit_and_large_gap.json',Path(__file__)]},
 'scope':'One full finite exact profile only. Refutes saturated gate-adjusted monotonicity, not uniform U4F/Q1. Decimal square-root/N/cap ratios are approximations; profile/I/coverage/gates and cap are certified by rational arithmetic.'}
save('full_profile_certification_summary.json',summary)
print(json.dumps({key:summary[key] for key in ['status','core_records','all_large_old_gap_core_records','N_approx',
       'cap_use_max_approx','cap_use_argmax','actual_graph_trials']},indent=2),flush=True)
