#!/usr/bin/env python3
"""Actual A68 matching/tail allowance on the already certified125 residual rows.
No new history, core enumeration, or full profile evaluation.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import hashlib,json

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rp=HERE/'A65_SPARSE_FIBER_FOLLOWUP_EXACT.json'
d=json.loads(rp.read_text());hp=HERE/'C1_m02_dense_variant1_M96.json'
assert sha(hp)==d['source_sha256'][hp.name]
a=[None]+json.loads(hp.read_text())['a'];c,b,k=24,25,48
old=a[1:c];future=a[b+1:k+1];n,m=len(old),len(future)
rows=[x for x in d['records'] if x['category']!='paid_sparse_support']
assert len(rows)==125
incoming=defaultdict(list);positive=defaultdict(int)
for item in rows:
    D,e,x,y,w,z,cc,s,i,r,t=item['record'];assert cc==c and c<b<i<r<=k
    if y==c:
        ow,oz,j,q=w,z,i-b,r-b;g,h=e,D
    else:
        ow,oz,j,q=x,y,r-b,i-b;g,h=D,e
    fresh=item['fresh_x']
    assert a[c]+a[ow]+future[j-1]==a[fresh]+a[oz]+future[q-1]
    assert a[oz]-a[ow]==g and g+future[q-1]-future[j-1]==h
    incoming[oz,q].append((ow,j,item['bank_index']))
    if h>g:positive[oz,q]+=g*t
for key,edges in incoming.items():
    assert len({w for w,j,idx in edges})==len(edges)
    assert len({j for w,j,idx in edges})==len(edges)
    assert len(edges)<=min(key[0]-1,m-1)
O=[sum(old[z]-old[l] for z in range(l+1,n)) for l in range(n-1)]
F=[sum(future[q]-future[l] for q in range(l+1,m)) for l in range(m-1)]
Phi=sum(x*y for x,y in zip(O,F))
node_bounds=[]
for z in range(1,n+1):
    for q in range(1,m+1):
        upper=sum((a[z]-a[l])*(future[q-1]-future[l-1]) for l in range(1,min(z-1,q-1)+1))
        assert positive[z,q]<=upper
        if positive[z,q]:node_bounds.append({'old_upper_rank':z,'future_position':q,
          'actual_positive_charge':positive[z,q],'matching_allowance':upper})
assert sum(sum((a[z]-a[l])*(future[q-1]-future[l-1]) for l in range(1,min(z-1,q-1)+1))
           for z in range(1,n+1) for q in range(1,m+1))==Phi
U=sum(old[z]-old[w] for z in range(n) for w in range(z))
G=sum(a[c]-x for x in old)
assert U==sum(O)
assert (Phi,U,G,U*G)==(1181503640,58548,11745,687646260)
assert sum(positive.values())==8716524 and Phi>U*G
coefficient=Q(4,k*(k*k-1)**2*(a[k]-a[1])**2)
count_bound=m*sum(min(z-1,m-1) for z in range(1,n+1))
actual_products=sum(x['record'][0]*x['record'][1] for x in rows)
out={'attempt':'A69','date':'2026-09-09','status':'EXACT_FINITE_ALLOWANCE_COMPARISON_PASS',
 'scope':{'C_exact':'1','m0':2,'M':96,'T':96,'c':c,'b':b,'k':k,
          'certified_records_reused':125,'new_histories':0,'full_profile_evaluations':0},
 'n':n,'m':m,'old_values':old,'future_values':future,'O_tails':O,'F_tails':F,
 'incoming_coordinate_matchings_pass':True,'joint_count_bound':count_bound,
 'positive_node_matching_bounds':node_bounds,'Phi':Phi,'U':U,'G':G,'UG':U*G,
 'Phi_minus_UG':Phi-U*G,'Phi_over_UG_exact':str(Q(Phi,U*G)),
 'actual_Beta':sum(positive.values()),'actual_original_products':actual_products,
 'F_n_minus_1':F[n-2],'sufficient_F_last_ge_G':F[n-2]>=G,
 'lambda48_exact':str(coefficient),
 'priced_Phi_exact':str(Phi*coefficient),'priced_UG_exact':str(U*G*coefficient),
 'exact_triple_sum_tail_interchange_pass':True,
 'scope_limits':['Phi and UG are upper allowances, not actual profile masses.',
 'No uniform norm or all-history improvement is established.',
 'All prices here concern component48 only; no full u_r is substituted.'],
 'source_sha256':{p.name:sha(p) for p in [Path(__file__),rp,hp]}}
(HERE/'A69_TAIL_ALLOWANCE_EXACT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({x:out[x] for x in ['status','Phi','UG','Phi_minus_UG','actual_Beta','joint_count_bound','sufficient_F_last_ge_G']}))
