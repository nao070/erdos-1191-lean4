#!/usr/bin/env python3
"""Only the prescribed actual mixed pair, six cuts and two horizons."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

from reference_evaluator import log_bounds

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=HERE/'C1_m02_dense_variant1_M96.json'
certpath=HERE/'C1_m02_dense_variant1_M96_independent_check.json'
data=json.loads(source.read_text())
cert=json.loads(certpath.read_text())
assert sha(source)=='d2b47d3902725a6d2a7f9283f9ade3bfa9c02cbe9c899d0ce08fe8bc0adbbb3e'
assert cert['status']=='PASS' and cert['input_sha256']==sha(source)
assert data['C_exact']=='1' and data['m0']==2 and data['M']==data['T']==96
a=[None]+data['a']
p,f,c=24,30,547
assert a[f]-a[p]==c
cuts=[]
cells=[]
unknown=[]

for b in range(p,f):
    H=a[b]-a[1]
    ll,lu=log_bounds(b)
    Llo,Lhi=F(b*b)/lu**5,F(b*b)/ll**5
    floorlo,floorhi=Llo.numerator//Llo.denominator,Lhi.numerator//Lhi.denominator
    if floorlo!=floorhi:
        unknown.append({'b':b,'L_interval':[str(Llo),str(Lhi)],'status':'UNKNOWN'})
        continue
    ell=floorlo+1
    assert ell<=c<H
    past={}
    for q in range(2,b+1):
        for x in range(1,q):
            label=a[q]-a[x]
            assert label>0 and label not in past
            past[label]=(x,q)
    U0=set(range(ell,H))-past.keys()
    U=set(U0)
    previous=[]
    target_found=False
    for y in range(b+1,f+1):
        for x in range(1,b+1):
            label=a[y]-a[x]
            if (x,y)==(p,f):
                assert label==c and label in U
                target_found=True
                break
            if ell<=label<H:
                assert label in U
                previous.append([label,x,y])
                U.remove(label)
        if target_found:
            break
    assert target_found and c in U
    ordered=sorted(U)
    after=sorted(U-{c})
    rank=ordered.index(c)+1
    D={a[y]-a[x] for y in range(2,b) for x in range(1,y)}
    assert len(D)==(b-1)*(b-2)//2
    S=sum(d*d for d in D)
    cuts.append({'b':b,'H_b':H,'ell':ell,'log_interval':[str(ll),str(lu)],
                 'L_interval':[str(Llo),str(Lhi)],'threshold_status':'CERTIFIED',
                 'S_b':S,'source_D_count':len(D),
                 'past_difference_endpoint_map':dict(sorted(past.items())),
                 'canonical_prior_eligible_deletions':previous,
                 'canonical_predelete_allowed_U':ordered,
                 'canonical_rank_r':rank,'N_predelete':len(ordered)})
    for v in (47,48):
        h=(v-b)*(v-b-1)//2
        before=sum((F(H-t,H) for t in ordered[:h]),F(0))
        later=sum((F(H-t,H) for t in after[:h]),F(0))
        penalty=before-later
        Hpen=H*penalty
        Spen=S*penalty
        Hv=a[v]-a[1]
        price=(F(1,v*v*(v-1)**2)-F(1,v*v*(v+1)**2))/(Hv*Hv)
        cells.append({'b':b,'v':v,'M':96,'T':v,'component_k':v,
                      'target_birth_f':f,'h':h,'r':rank,'N':len(ordered),
                      'predelete_packing_exact':str(before),
                      'postdelete_packing_exact':str(later),
                      'p_exact':str(penalty),'H_times_p_exact':str(Hpen),
                      'S_times_p_exact':str(Spen),'genuine_component_price_exact':str(price),
                      'priced_p_exact':str(price*penalty),
                      'priced_H_times_p_exact':str(price*Hpen),
                      'priced_S_times_p_exact':str(price*Spen),
                      'next_selected_label_or_none':ordered[h] if h<len(ordered) else None})

comparisons=[]
for v in (47,48):
    indexed={row['b']:row for row in cells if row['v']==v}
    for b in range(p,f-1):
        if b not in indexed or b+1 not in indexed:
            continue
        comparisons.append({'v':v,'b_before':b,'b_after':b+1,
          'differences':{key:str(F(indexed[b+1][key])-F(indexed[b][key]))
                         for key in ('p_exact','H_times_p_exact','S_times_p_exact')},
          'nonincreasing_candidates':{key:F(indexed[b+1][key])<=F(indexed[b][key])
                         for key in ('p_exact','H_times_p_exact','S_times_p_exact')}})

result={'date':'2026-09-09','attempt':'A36','input':source.name,'C_exact':'1','m0':2,
        'source_M':96,'target_pair':{'p':p,'f':f,'a_p':a[p],'a_f':a[f],'label':c},
        'specified_cuts':list(range(p,f)),'specified_output_horizons':[47,48],
        'actual_prefix_through48':a[1:49],'cuts':cuts,'cells':cells,
        'adjacent_cut_comparisons':comparisons,'unknown_comparisons':unknown,
        'all_penalties_zero':all(F(row['p_exact'])==0 for row in cells),
        'source_sha256':{x.name:sha(x) for x in [source,certpath,HERE/'reference_evaluator.py',
                          HERE/'A34_DEFERRED_DELETION_PENALTY_REVIEW.md',Path(__file__)]},
        'scope':'One actual pair; exactly six cuts and two output/component horizons. No new history, original core enumeration or full profile evaluation. Penalties are the A34 fixed-cut sequential deletion quantities, not new independent physical record budgets.'}
out=HERE/'A36_mixed_pair_547_twelve_cells_exact.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'UNKNOWN' if unknown else 'PASS_EXACT_REFERENCE',
                 'cells':len(cells),'unknown':len(unknown),'all_zero':result['all_penalties_zero'],
                 'table':[[r['b'],r['v'],r['h'],r['r'],r['N'],r['p_exact'],r['H_times_p_exact'],r['S_times_p_exact']] for r in cells],
                 'counterexample_transitions':[x for x in comparisons if not all(x['nonincreasing_candidates'].values())]},indent=2))
