#!/usr/bin/env python3
"""Exact convex one-parameter optimization on the two already saved cells.

Upper certificates are node assignment duals. Lower certificates are actual
partial matchings defining affine lines below D(theta) for every theta.
"""
from pathlib import Path
from fractions import Fraction as Q
import hashlib
import json
from A70_feasible_matching_reference import assignment_dual

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def optimize(path):
    data=json.loads(path.read_text())
    old,future=data['old_values'],data['future_values']
    ac=old[0]+data['H_c'];fresh=[ac-x for x in old]
    bank=0;allowed={}
    for z in range(len(old)):
        for w in range(z):
            g=old[z]-old[w]
            allowed[w,z]=sorted(fresh[x] for x in range(len(old)) if x not in [w,z])
            bank+=sum(g*max(h-g,0) for h in allowed[w,z])
    edges={}
    for z in range(len(old)):
        for q in range(len(future)):
            cell={}
            for w in range(z):
                g=old[z]-old[w]
                for j in range(q):
                    t=future[q]-future[j]
                    h=next((x for x in allowed[w,z] if x>=g+t),None)
                    if h is not None:cell[w,j]=(g*t,g*(h-g))
            edges[z,q]=cell
    cache={};trace=[];lines={}

    def oracle(theta):
        assert theta not in cache
        p,d=theta.numerator,theta.denominator
        A,cost,total=0,0,0;nodes=[];positive=[]
        for (z,q),cell in edges.items():
            N=max(z,q);weights=[[0]*N for _ in range(N)]
            for (w,j),(benefit,charge) in cell.items():
                weights[w][j]=max(d*benefit-p*charge,0)
            left,right,assignment=assignment_dual(weights)
            value=sum(left)+sum(right);total+=value
            for w,j in enumerate(assignment):
                if weights[w][j]>0:
                    benefit,charge=cell[w,j]
                    A+=benefit;cost+=charge;positive.append([z+1,q+1,w+1,j+1])
            nodes.append(dict(z=z+1,q=q+1,value_scaled=value,dual_left=left,
                              dual_right=right,assignment=assignment))
        S=bank-cost;value=Q(p*bank+total,d)
        assert value==A+theta*S
        record=dict(theta_exact=str(theta),value_exact=str(value),intercept=A,slope=S,
                    nodes=nodes,positive_edges=positive)
        cache[theta]=record;lines[A,S]=record
        trace.append({k:record[k] for k in ['theta_exact','value_exact','intercept','slope']})
        print(json.dumps(dict(input=path.name,iteration=len(trace),**trace[-1])),flush=True)
        return record

    oracle(Q(0));oracle(Q(1))
    while True:
        candidates={Q(0),Q(1)}
        keys=list(lines)
        for i,(a,s) in enumerate(keys):
            for aa,ss in keys[:i]:
                if s!=ss:
                    t=Q(aa-a,s-ss)
                    if 0<=t<=1:candidates.add(t)
        lower,theta=min((max(Q(a)+t*s for a,s in lines),t) for t in candidates)
        if theta in cache:
            upper=cache[theta]
        else:
            upper=oracle(theta)
        if Q(upper['value_exact'])==lower:
            break
        assert (upper['intercept'],upper['slope']) in lines
        assert Q(upper['value_exact'])>lower
    active=[r for (a,s),r in lines.items() if a+theta*s==lower]
    if theta==0:
        support=[next(r for r in active if r['slope']>=0)]
    elif theta==1:
        support=[next(r for r in active if r['slope']<=0)]
    elif any(r['slope']==0 for r in active):
        support=[next(r for r in active if r['slope']==0)]
    else:
        support=[next(r for r in active if r['slope']<0),next(r for r in active if r['slope']>0)]
    lower_certificates=[{k:r[k] for k in ['theta_exact','intercept','slope','positive_edges']} for r in support]
    return dict(input=path.name,input_sha256=sha(path),B_source_positive=bank,
                optimum_theta_exact=str(theta),minimum_D_exact=str(lower),
                endpoint_0_exact=cache[Q(0)]['value_exact'],endpoint_1_exact=str(bank),
                oracle_count=len(trace),trace=trace,lower_supports=lower_certificates,
                upper_node_duals=upper['nodes'])

def main():
    inputs=['A70_FEASIBLE_MATCHING_EXACT.json','A72_SOURCE_ALLOWANCE_COUNTEREXAMPLE.json']
    results=[optimize(HERE/name) for name in inputs]
    out=dict(attempt='A74',status='EXACT_PARAMETRIC_MATCHING_DUAL_OPTIMA',results=results,
             source_sha256={p.name:sha(p) for p in [Path(__file__),HERE/'A70_feasible_matching_reference.py',*(HERE/x for x in inputs)]},
             limits=['One-dimensional coefficient optimization on two fixed cells only.',
                     'This does not prove a uniform core-profile norm or original Q1.',
                     'Neither selected auxiliary edges nor per-cut allowances are extra physical budgets.'])
    (HERE/'A74_PARAMETRIC_DUAL_EXACT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps([{k:r[k] for k in ['input','optimum_theta_exact','minimum_D_exact','oracle_count']} for r in results]))

if __name__=='__main__':main()
