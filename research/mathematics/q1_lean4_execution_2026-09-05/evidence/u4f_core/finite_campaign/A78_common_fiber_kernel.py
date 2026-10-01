#!/usr/bin/env python3
"""All births at one saved cut/component: exact mixed-triple fiber kernel."""
from pathlib import Path
from collections import defaultdict
from itertools import combinations
import hashlib,json

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def run(name):
    p=HERE/name;d=json.loads(p.read_text())
    old=d['old_values']+[d['old_values'][0]+d['H_c']]
    future=d['future_values'];fibers=defaultdict(list)
    for u,v in combinations(range(len(old)),2):
        for q,f in enumerate(future):
            fibers[old[u]+old[v]+f].append((u,v,q))
    comparisons=[];total=0;witness=None;record_count=0
    for S,triples in sorted(fibers.items()):
        for left,right in combinations(triples,2):
            u,v,q=left;w,z,j=right
            assert len({u,v,w,z})==4 and q!=j
            L=old[v]-old[u];J=old[z]-old[w]
            t=abs(future[q]-future[j])
            numerator=max((L+J)**2-t*t,0)+max((L-J)**2-t*t,0)
            assert numerator%4==0
            kernel=numerator//4
            p0,p1,p2,p3=sorted([u,v,w,z]);a,b,c,e=[old[x] for x in [p0,p1,p2,p3]]
            products=[]
            for d1,d2 in [(b-a,e-c),(c-a,e-b),(e-a,c-b)]:
                if abs(d1-d2)==t:products.append(d1*d2)
            assert sum(products)==kernel
            total+=kernel;record_count+=len(products)
            row=dict(sum=S,triples=[[u+1,v+1,q+1],[w+1,z+1,j+1]],lengths=[L,J],
                     t=t,kernel=kernel,original_source_products=products)
            comparisons.append(row)
            if witness is None and kernel>L*J:
                witness={**row,'length_product':L*J,'determinant':L*L*J*J-kernel*kernel}
    # Independent full source enumeration across every c<=24, actual outputs.
    future_diffs={future[r]-future[i]:(i,r) for i,r in combinations(range(len(future)),2)}
    assert len(future_diffs)==len(future)*(len(future)-1)//2
    other=0;other_count=0
    for c in range(len(old)):
        for w,z in combinations(range(c),2):
            g=old[z]-old[w]
            for x in range(c):
                if x in [w,z]:continue
                h=old[c]-old[x]
                if abs(g-h) in future_diffs:other+=g*h;other_count+=1
    assert other==total and other_count==record_count
    return dict(input=name,input_sha256=sha(p),old_count=len(old),future_count=len(future),
                triple_count=sum(map(len,fibers.values())),nontrivial_fibers=sum(len(v)>1 for v in fibers.values()),
                maximum_fiber_size=max(map(len,fibers.values())),fiber_pair_count=len(comparisons),
                physical_record_count=record_count,full_unfiltered_product=total,
                factorized_bound_counterexample=witness,pairs=comparisons)

if __name__=='__main__':
    result=dict(attempt='A78',status='EXACT_FINITE',results=[run(n) for n in
                ['A70_FEASIBLE_MATCHING_EXACT.json','A72_SOURCE_ALLOWANCE_COUNTEREXAMPLE.json']],
                source_sha256={Path(__file__).name:sha(Path(__file__))},
                scope='Two saved histories, b25 and k48/k50; all source births c<25, both orientations, no strict-log/residual filter. Exact kernel and independent physical-source enumeration; no new history or original full profile.')
    (HERE/'A78_COMMON_FIBER_KERNEL.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps([{k:v for k,v in r.items() if k!='pairs'} for r in result['results']]))
