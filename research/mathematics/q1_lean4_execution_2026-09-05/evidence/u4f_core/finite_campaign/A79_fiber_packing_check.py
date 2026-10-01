#!/usr/bin/env python3
"""Compare the proved fiber packing allowance on two already checked cells."""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction as Q
import hashlib,json

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
src=HERE/'A78_COMMON_FIBER_KERNEL.json'
data=json.loads(src.read_text());results=[]
for cell in data['results']:
    inp=HERE/cell['input'];d=json.loads(inp.read_text())
    assert sha(inp)==cell['input_sha256']
    H=d['H_c'];n=cell['old_count'];assert H>=n*(n-1)//2
    fibers=defaultdict(list)
    for row in cell['pairs']:fibers[row['sum']].append(row)
    baseline=0;packed=Q(0);actual=0;diagonal=Q(0);certs=[]
    for S,rows in sorted(fibers.items()):
        triples={tuple(t) for row in rows for t in row['triples']}
        q=len(triples);N=q*(q-1)//2
        assert len(rows)==N and 2*q<=n and 4*N<=H
        differences=sorted(row['t'] for row in rows)
        assert len(set(differences))==N
        assert all(t>=j for j,t in enumerate(differences,1))
        for row in rows:
            assert Q(row['kernel'])<=max(Q(H*H)-Q(row['t']**2,4),Q(0))
        B=Q(N*H*H)-Q(N*(N+1)*(2*N+1),24)
        direct=sum(max(Q(H*H)-Q(j*j,4),Q(0)) for j in range(1,N+1))
        assert B==direct and Q(63,64)*N*H*H<=B<=N*H*H
        mass=sum(row['kernel'] for row in rows);assert mass<=B
        lengths={}
        for row in rows:
            for tr,L in zip(row['triples'],row['lengths']):
                tr=tuple(tr)
                if tr in lengths:assert lengths[tr]==L
                lengths[tr]=L
        diag=Q(q-1,2)*sum(L*L for L in lengths.values())
        assert mass<=diag
        baseline+=N*H*H;packed+=B;actual+=mass;diagonal+=diag
        certs.append({'sum':S,'q':q,'N':N,'packing_bound':str(B),'actual_kernel':mass})
    assert actual==cell['full_unfiltered_product']
    results.append({'input':cell['input'],'H':H,'old_count':n,'fibers':len(fibers),
                    'crude_allowance':baseline,'packing_allowance':str(packed),
                    'packing_saved':str(Q(baseline)-packed),'actual_kernel':actual,
                    'length_diagonal_allowance':str(diagonal),'certificates':certs})
out={'attempt':'A79','status':'EXACT_FINITE_ALLOWANCE_COMPARISON','results':results,
     'source_sha256':{src.name:sha(src),Path(__file__).name:sha(Path(__file__))},
     'limits':['The lower comparison is for the relaxed allowance, never actual core mass.',
               'Two existing unfiltered cells only; no new histories, profiles or fixed-cap asymptotic family.',
               'No uniform core norm or Q1 claim.']}
(HERE/'A79_FIBER_PACKING_EXACT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps([{k:v for k,v in r.items() if k!='certificates'} for r in results]))
