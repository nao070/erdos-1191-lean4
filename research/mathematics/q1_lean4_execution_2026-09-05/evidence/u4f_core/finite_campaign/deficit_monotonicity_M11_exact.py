#!/usr/bin/env python3
"""Certify the one specified actual Sidon counterexample; no search."""
from collections import Counter,defaultdict
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json
from reference_evaluator import evaluate,differences
from independent_checker import check

HERE=Path(__file__).resolve().parent
OUT=HERE/'C1000000_m02_M11_deficit_target'
OUT.mkdir(exist_ok=True)
A=[1,18,1000,1011,1024,2000,99959,99993,99994,99996,100000]
C=F(1000000);m0=2;M=T=11;b=6;l=2

def write(name,data):
    (OUT/name).write_text(json.dumps(data,indent=2)+'\n')

write('campaign_fixed_before_check.json',{
 'C_exact':str(C),'m0':m0,'M':M,'T':T,'b':b,'l':l,'a':A,
 'candidate_histories':1,'search_trials':0,
 'procedure':'Check only the exact user/parent specified sequence; no point or cap changes.',
 'scope':'Raw tripartite capacity-deficit monotonicity, not core/Q1.',
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
diffs=differences(A);assert len(diffs)==55
data,rows=evaluate(A,'C1000000_m02_M11_deficit_target',C=C,m0=m0)
canonical=OUT/'C1000000_m02_M11_deficit_target.json'
write(canonical.name,data)
write(canonical.stem+'_records.json',{
 'columns':['d','e','p_d','q_d','p_e','q_e','c','s','i','r','t'],
 'records':rows})
check(canonical)
a=[None]+A;n=b-1
bank={}
for u in range(1,l+1):
    for v in range(l+1,n+1):
        total=a[u]+a[v]
        assert total not in bank
        bank[total]=(u,v)
assert len(bank)==6

def fiber_data(last):
    fibers=defaultdict(list)
    for u in range(1,l+1):
        for v in range(l+1,n+1):
            for f in range(b+1,last+1):
                fibers[a[u]+a[v]+a[f]].append((u,v,f))
    m=last-b;d=min(l,n-l,m)
    assert all(len(triples)<=d for triples in fibers.values())
    delta=sum(len(triples)*(d-len(triples)) for triples in fibers.values())
    collision_rows=[]
    for total,triples in sorted(fibers.items()):
        for x,y in combinations(triples,2):
            assert len(set(x+y))==6
            p,q=sorted((x[0],y[0]));s,c=sorted((x[1],y[1]))
            i,r=sorted((x[2],y[2]))
            matching=3 if {(x[0],x[1]),(y[0],y[1])}=={(p,s),(q,c)} else 2
            assert {(x[0],x[1]),(y[0],y[1])}==({(p,s),(q,c)} if matching==3 else {(p,c),(q,s)})
            collision_rows.append({'sum':total,'triples_ranks':[list(x),list(y)],
                 'triples_points':[[a[t] for t in x],[a[t] for t in y]],
                 'old_quad_ranks':[p,q,s,c],'BH_matching_type':matching,
                 'future_output_ranks':[i,r],'future_output_value':a[r]-a[i]})
    count=len(collision_rows)
    assert 2*count==(d-1)*len(bank)*m-delta
    return fibers,{'future_last_rank':last,'future_ranks':list(range(b+1,last+1)),
      'future_points':a[b+1:last+1],'m':m,'d':d,'N':len(bank)*m,
      'delta_exact':delta,'collision_count':count,
      'fiber_size_histogram':dict(sorted(Counter(map(len,fibers.values())).items())),
      'all_fibers':[{'sum':z,'size':len(triples),'triples_ranks':[list(t) for t in triples]}
                    for z,triples in sorted(fibers.items())],
      'all_collisions':collision_rows}

before_fibers,before=fiber_data(10)
after_fibers,after=fiber_data(11)
new_sites=[{'sum':a[11]+u,'old_pair_sum':u,'old_pair_ranks':list(bank[u]),
            'previous_fiber_size':len(before_fibers.get(a[11]+u,[])),
            'previous_triples_ranks':[list(t) for t in before_fibers.get(a[11]+u,[])]}
           for u in sorted(bank)]
J=sum(row['previous_fiber_size'] for row in new_sites)
assert J==4
predicted=(after['d']-before['d'])*len(bank)*before['m']+(after['d']-1)*len(bank)-2*J
change=after['delta_exact']-before['delta_exact']
assert predicted==change==-2
new_collisions=[row for row in after['all_collisions'] if row['future_output_ranks'][1]==11]
assert len(new_collisions)==J
assert sorted(row['future_output_value'] for row in new_collisions)==[4,6,7,41]
assert data['core_records']==len(rows)==0
result={
 'status':'CERTIFIED_ACTUAL_SIDON_RAW_DEFICIT_MONOTONICITY_COUNTEREXAMPLE',
 'C_exact':str(C),'m0':m0,'M':M,'T':T,'a':A,'b':b,'l':l,'n':n,
 'positive_differences':55,'repeated_two_sum_independent_check':'PASS',
 'cap_all_ranks_certified':data['cap_all_ranks_certified'],
 'unknown_log_comparisons':0,'original_strict_core_records':0,
 'original_strict_core_profile':{},'original_strict_core_N_exact':'0',
 'left_ranks':[1,2],'left_points':a[1:3],
 'right_ranks':[3,4,5],'right_points':a[3:6],
 'old_pair_sum_bank':[{'sum':s,'left_rank':u,'right_rank':v,
        'left_point':a[u],'right_point':a[v]} for s,(u,v) in sorted(bank.items())],
 'before':before,'after':after,'new_point_rank':11,'new_point':a[11],
 'new_sites':new_sites,'J_new_collisions':J,'new_collisions':new_collisions,
 'exact_increment_formula_value':predicted,'actual_delta_increment':change,
 'scope':'Rejects monotonicity under future-point addition of raw tripartite deficit even in an actual Sidon finite history with fixed C=1000000,m0=2. The unchanged strict core is empty; this is not a core-profile, uniform-K, or Q1 counterexample.',
 'source_sha256':{str(p.relative_to(HERE)):hashlib.sha256(p.read_bytes()).hexdigest()
        for p in [canonical,canonical.with_name(canonical.stem+'_records.json'),
                  canonical.with_name(canonical.stem+'_independent_check.json'),
                  HERE/'reference_evaluator.py',HERE/'independent_checker.py',Path(__file__)]},
 'frozen_source_sha256':data['source_sha256']}
write('raw_deficit_monotonicity_counterexample_exact.json',result)
print(json.dumps({key:result[key] for key in ['status','positive_differences','original_strict_core_records',
     'old_pair_sum_bank','J_new_collisions','actual_delta_increment','new_collisions']},indent=2))
print(json.dumps({'delta_before':before['delta_exact'],'delta_after':after['delta_exact'],
      'collisions_before':before['collision_count'],'collisions_after':after['collision_count'],
      'histogram_before':before['fiber_size_histogram'],'histogram_after':after['fiber_size_histogram']},indent=2))
