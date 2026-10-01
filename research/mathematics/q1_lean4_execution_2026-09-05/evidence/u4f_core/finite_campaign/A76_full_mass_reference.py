#!/usr/bin/env python3
"""Full original-product dual, both output orientations, on two saved cells."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import hashlib,json
from A70_feasible_matching_reference import assignment_dual

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def calculate(input_name):
    path=HERE/input_name;data=json.loads(path.read_text())
    old,future=data['old_values'],data['future_values'];ac=old[0]+data['H_c']
    fresh=[ac-a for a in old];c,b,k=24,25,(48 if input_name.startswith('A70') else 50)
    if input_name.startswith('A70'):
        rp=HERE/'A65_SPARSE_FIBER_FOLLOWUP_EXACT.json'
        rd=json.loads(rp.read_text())
        rows=[r['record'] for r in rd['records'] if r['category']!='paid_sparse_support']
        assert len(rows)==125
    else:
        rp=HERE/'C2pow67_m02_prescribed_allowance_M50_records.json'
        rows=json.loads(rp.read_text())['records'];assert len(rows)==1
    node_actual=defaultdict(int);actual_edges=defaultdict(list)
    for row in rows:
        D,e,x,y,w,z,cc,s,i,r,t=row
        assert cc==c and c<b<i<r<=k
        if y==c:ow,oz,j,q,g,h=w,z,i-b,r-b,e,D
        else:ow,oz,j,q,g,h=x,y,r-b,i-b,D,e
        assert old[oz-1]-old[ow-1]==g
        assert g+future[q-1]-future[j-1]==h
        node_actual[oz,q]+=g*h;actual_edges[oz,q].append((ow,j))
    for edges in actual_edges.values():
        assert len({w for w,j in edges})==len(edges)==len({j for w,j in edges})
    bank={};permitted={}
    for z in range(len(old)):
        for w in range(z):
            g=old[z]-old[w]
            permitted[w,z]=sorted(fresh[x] for x in range(len(old)) if x not in [w,z])
            bank[w,z]=g*sum(permitted[w,z])
    total_bank=sum(bank.values());cases=[]
    for p,den in [(0,1),(1,2),(1,1)]:
        nodes=[];total=0
        for z in range(len(old)):
            for q in range(len(future)):
                N=max(z,len(future));weights=[[0]*N for _ in range(N)]
                for w in range(z):
                    g=old[z]-old[w]
                    for j in range(len(future)):
                        if j==q:continue
                        value_h=g+future[q]-future[j]
                        if value_h<=0:continue
                        h=next((h for h in permitted[w,z] if h>=value_h),None)
                        if h is not None:weights[w][j]=max(den*g*value_h-p*g*h,0)
                left,right,assignment=assignment_dual(weights)
                value=sum(left)+sum(right);total+=value
                assert value>=(den-p)*node_actual[z+1,q+1]
                nodes.append(dict(z=z+1,q=q+1,value_scaled=value,dual_left=left,
                                  dual_right=right,assignment=assignment))
        bound=Q(p*total_bank+total,den)
        assert bound>=sum(node_actual.values())
        if p==den:assert total==0 and bound==total_bank
        cases.append(dict(theta_exact=str(Q(p,den)),numerator=p,denominator=den,
                          bound_exact=str(bound),matching_sum_scaled=total,nodes=nodes))
    return dict(input=input_name,input_sha256=sha(path),record_source=rp.name,
                record_source_sha256=sha(rp),original_record_count=len(rows),
                full_actual_product=sum(node_actual.values()),six_distinct_source_bank=total_bank,
                node_actual_products={f'{z},{q}':v for (z,q),v in node_actual.items() if v},
                cases=cases,minimum_tested_bound_exact=str(min(Q(s['bound_exact']) for s in cases)))

def main():
    names=['A70_FEASIBLE_MATCHING_EXACT.json','A72_SOURCE_ALLOWANCE_COUNTEREXAMPLE.json']
    out=dict(attempt='A76',status='EXACT_FINITE_FULL_MASS_DUALS',results=[calculate(n) for n in names],
             source_sha256={p.name:sha(p) for p in [Path(__file__),HERE/'A70_feasible_matching_reference.py',*(HERE/n for n in names)]},
             limits=['Both orientations and original gh product mass are included.',
                     'Only three prescribed coefficients on two saved cells; no coefficient optimum claim.',
                     'No new history/profile and no all-history uniform norm or Q1 theorem.'])
    (HERE/'A76_FULL_MASS_EXACT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps([dict(input=r['input'],Q=r['full_actual_product'],bank=r['six_distinct_source_bank'],
                          bounds=[(s['theta_exact'],s['bound_exact']) for s in r['cases']]) for r in out['results']]))

if __name__=='__main__':main()
