#!/usr/bin/env python3
"""One prescribed nonuniform source penalty; only23 changed nodes are solved."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib,json
from A70_feasible_matching_reference import assignment_dual

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
hp=HERE/'A70_FEASIBLE_MATCHING_EXACT.json'
bp=HERE/'A74_PARAMETRIC_DUAL_EXACT.json'
d=json.loads(hp.read_text());base=json.loads(bp.read_text())['results'][0]
assert base['input']==hp.name and base['input_sha256']==sha(hp)
assert base['optimum_theta_exact']=='0' and base['minimum_D_exact']=='80331512'
old,future=d['old_values'],d['future_values'];ac=old[0]+d['H_c'];fresh=[ac-x for x in old]
# Fixed BEFORE the test: physical old source a16-a1=283 and theta=1/1000.
w0,z0,p,den=0,15,1,1000
g0=old[z0]-old[w0];assert g0==283
bank=sum(g0*max(fresh[x]-g0,0) for x in range(len(old)) if x not in [w0,z0])
old_node_sum=sum(n['value_scaled'] for n in base['upper_node_duals'] if n['z']==z0+1)
unchanged=Q(base['minimum_D_exact'])-old_node_sum
new_total=0;nodes=[]
for q in range(len(future)):
    N=max(z0,q);matrix=[[0]*N for _ in range(N)]
    for w in range(z0):
        g=old[z0]-old[w]
        hs=sorted(fresh[x] for x in range(len(old)) if x not in [w,z0])
        for j in range(q):
            t=future[q]-future[j]
            h=next((h for h in hs if h>=g+t),None)
            if h is not None:
                penalty=p*g*(h-g) if w==w0 else 0
                matrix[w][j]=max(den*g*t-penalty,0)
    left,right,assignment=assignment_dual(matrix)
    value=sum(left)+sum(right);new_total+=value
    nodes.append(dict(z=z0+1,q=q+1,value_scaled=value,dual_left=left,
                      dual_right=right,assignment=assignment))
bound=unchanged+Q(p*bank+new_total,den)
gain=Q(base['minimum_D_exact'])-bound
assert d['actual_Beta']<=bound
out=dict(attempt='A75',status='EXACT_ONE_SOURCE_PENALTY_TEST',
         physical_old_pair=[w0+1,z0+1],g=g0,theta_exact=str(Q(p,den)),
         numerator=p,denominator=den,B_selected_source=bank,
         unchanged_node_sum_exact=str(unchanged),old_changed_node_sum=old_node_sum,
         new_changed_node_sum_scaled=new_total,new_bound_exact=str(bound),
         previous_scalar_optimum_exact=base['minimum_D_exact'],gain_exact=str(gain),
         strict_improvement=gain>0,nodes=nodes,actual_Beta=d['actual_Beta'],
         source_sha256={p.name:sha(p) for p in [Path(__file__),hp,bp,HERE/'A70_feasible_matching_reference.py']},
         limits=['Only one prescribed source penalty on the existing C1 cell.',
                 'No optimum over nonuniform penalties, no uniform norm, and no Q1 claim.',
                 'The unused nodes reuse the exact A74 theta0 certificate; no new history or profile.'])
(HERE/'A75_ONE_SOURCE_PENALTY_EXACT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({key:out[key] for key in ['status','B_selected_source','new_bound_exact','gain_exact','strict_improvement']}))
