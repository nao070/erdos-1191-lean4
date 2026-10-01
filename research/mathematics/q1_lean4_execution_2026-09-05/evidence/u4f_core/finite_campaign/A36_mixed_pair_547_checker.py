#!/usr/bin/env python3
"""Independent closed-bank and integer-prefix check of the 12+6 cells."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

from independent_checker import log_fixed,SCALE

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
initial=HERE/'A36_mixed_pair_547_twelve_cells_exact.json'
extra=HERE/'A36_mixed_pair_547_horizon60_exact.json'
x=json.loads(initial.read_text());y=json.loads(extra.read_text())
assert y['source_sha256'][initial.name]==sha(initial)
source=HERE/x['input'];data=json.loads(source.read_text())
assert sha(source)==x['source_sha256'][source.name]
for name,expected in x['source_sha256'].items():assert sha(HERE/name)==expected
for name,expected in y['source_sha256'].items():assert sha(HERE/name)==expected
a=[None]+data['a'];p,f,c=24,30,547
assert a[f]-a[p]==c
independent_cuts=[]
checked=[]
for cut in x['cuts']:
    b,H=cut['b'],a[cut['b']]-a[1]
    lo,hi=log_fixed(b)
    Llo=F(b*b*SCALE**5,hi**5)
    Lhi=F(b*b*SCALE**5,lo**5)
    flo,fhi=Llo.numerator//Llo.denominator,Lhi.numerator//Lhi.denominator
    assert flo==fhi
    ell=flo+1
    assert ell==cut['ell'] and ell<=c<H
    bank={}
    for lower in range(1,b+1):
        for upper in range(lower+1,f):
            t=a[upper]-a[lower]
            assert t>0 and t not in bank
            bank[t]=[lower,upper]
    for lower in range(1,p):
        t=a[f]-a[lower]
        assert t>0 and t not in bank
        bank[t]=[lower,f]
    assert c not in bank
    assert len(bank)==b*(b-1)//2+b*(f-1-b)+(p-1)
    U=[t for t in range(ell,H) if t not in bank]
    assert U==cut['canonical_predelete_allowed_U']
    r=sum(t<=c for t in U);N=len(U)
    assert r==cut['canonical_rank_r'] and N==cut['N_predelete']
    old=a[1:b]
    S=len(old)*sum(t*t for t in old)-sum(old)**2
    assert S==cut['S_b']
    prefix={};total=0
    for label in range(ell,H):
        total+=label not in bank
        prefix[label]=total
    independent_cuts.append({'b':b,'H_b':H,'ell':ell,'S_b':S,'r':r,'N':N,
         'closed_prebank_endpoint_map':dict(sorted(bank.items())),
         'independent_L_interval':[str(Llo),str(Lhi)],
         'sequential_prebank_equals_closed_formula':True})
    for row in x['cells']+y['cells']:
        if row['b']!=b:continue
        v=row['v'];h=(v-b)*(v-b-1)//2
        paying_labels=[t for t in range(c,H) if prefix[t]<=h]
        numerator=len(paying_labels)
        penalty=F(numerator,H)
        price=F(4,v*(v*v-1)**2*(a[v]-a[1])**2)
        rho=F(numerator,H-c)
        assert row['h']==h and row['r']==r and row['N']==N
        for key,expected in [('p_exact',penalty),('H_times_p_exact',F(numerator)),
            ('S_times_p_exact',S*penalty),('genuine_component_price_exact',price),
            ('priced_p_exact',price*penalty),('priced_H_times_p_exact',price*numerator),
            ('priced_S_times_p_exact',price*S*penalty)]:
            assert F(row[key])==expected,(b,v,key)
        if 'rho_exact' in row:assert F(row['rho_exact'])==rho
        checked.append({'b':b,'v':v,'p_exact':str(penalty),'H_times_p_exact':numerator,
            'S_times_p_exact':str(S*penalty),'rho_exact':str(rho),
            'paying_integer_interval':None if not paying_labels else [paying_labels[0],paying_labels[-1]],
            'genuine_component_price_exact':str(price),'status':'PASS'})
assert len(checked)==18
out={'date':'2026-09-09','attempt':'A36','status':'PASS_INDEPENDENT_EXACT_18_CELLS',
 'target_pair':x['target_pair'],'unknown_comparisons':0,'independent_cuts':independent_cuts,
 'checked_cells':checked,'source_sha256':{p.name:sha(p) for p in [source,initial,extra,Path(__file__),HERE/'independent_checker.py']},
 'independence':'Closed prebank endpoint union replaces sequential deletion; integer prefix counting replaces subtraction of two packing sums; variance identity replaces squared-difference enumeration; fixed-point 50-term log intervals replace reference rational 40-term intervals; genuine price uses 4/[v(v^2-1)^2 H_v^2].',
 'scope':'Specified 12 cells plus authorized same-pair v60 six cells only. Existing C1,m02 M96 Sidon/cap certificate reused; no new whole-profile/core evaluation.'}
path=HERE/'A36_mixed_pair_547_independent_check.json';path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'unknown':0,'cells':len(checked),'input_sha256':sha(source),'checker_sha256':sha(Path(__file__))},indent=2))
