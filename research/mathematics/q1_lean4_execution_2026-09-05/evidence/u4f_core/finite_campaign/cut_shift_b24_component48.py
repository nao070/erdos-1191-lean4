#!/usr/bin/env python3
"""Only cut24->25 at component48 in the two existing M96 histories."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib,json
from independent_checker import log_fixed,SCALE,rank_conditions,output_condition

HERE=Path(__file__).resolve().parent
b=24;k=48;T=96;LS=(6,12,18)
thresholds_all=json.loads((HERE/'small_middle_gap_existing_M96.json').read_text())
results=[]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

for stem in ('C1_m02_greedy_M96','C1_m02_dense_variant1_M96'):
    dp=HERE/(stem+'.json');rp=HERE/(stem+'_records.json');cp=HERE/(stem+'_independent_check.json')
    data=json.loads(dp.read_text());rows=json.loads(rp.read_text())['records'];cert=json.loads(cp.read_text())
    assert cert['status']=='PASS' and cert['input_sha256']==digest(dp)
    assert data['C_exact']=='1' and data['m0']==2 and data['M']==data['T']==96
    a=[None]+data['a'];assert len(rows)==data['core_records']
    thresholds=next(t['thresholds_floor_certified'] for t in thresholds_all if t['input']==stem)
    for c in range(4,b+1):
        lo,hi=log_fixed(c);lower=F(c*c*SCALE**3,hi**3);upper=F(c*c*SCALE**3,lo**3)
        assert lower.numerator//lower.denominator==upper.numerator//upper.denominator==thresholds[str(c)]
    Hk=a[k]-a[1]
    price=(F(1,k*k*(k-1)**2)-F(1,k*k*(k+1)**2))/(Hk*Hk)
    banks={'all_core':[],'all_large_old_gaps_core':[]}
    for row in rows:
        dd,ee,pd,qd,pe,qe,c,s_old,i,r,tt=row
        if r>k or not (c<b+1 and i>b):continue
        p,q,s,cc=sorted((pd,qd,pe,qe));assert cc==c
        pairs={tuple(sorted((pd,qd))),tuple(sorted((pe,qe)))}
        if pairs=={(p,q),(s,c)}:continue
        typ=2 if pairs=={(p,s),(q,c)} else 3
        assert pairs==({(p,s),(q,c)} if typ==2 else {(q,s),(p,c)})
        assert s_old==s
        A=a[q]-a[p];B=a[s]-a[q];Cgap=a[c]-a[s];H=a[c]-a[p]
        assert dd*ee==(A*Cgap+B*H if typ==2 else B*H)
        rr={'quad':[p,q,s,c],'type':typ,'i':i,'r':r,'B':B,'Hquad':H,
            'BH_product':B*H,'original_record':row}
        banks['all_core'].append(rr)
        if min(A,B,Cgap)>thresholds[str(c)]:banks['all_large_old_gaps_core'].append(rr)
    raw_by_l={}
    for l in LS:
        L=range(1,l+1);R=range(l+1,b);Ffuture=range(b+2,k+1)
        u=Counter(a[x]+a[y]+a[z] for x,y,z in product(L,R,Ffuture))
        wp_pairs={};wm_pairs={}
        for x,z in product(L,Ffuture):
            value=a[x]+a[b]+a[z];assert value not in wp_pairs;wp_pairs[value]=(x,b,z)
        for x,y in product(L,R):
            value=a[x]+a[y]+a[b+1];assert value not in wm_pairs;wm_pairs[value]=(x,y,b+1)
        wp=Counter({z:1 for z in wp_pairs});wm=Counter({z:1 for z in wm_pairs})
        before=u+wm;after=u+wp
        N0=l*(b-1-l)*(k-b);N1=l*(b-l)*(k-b-1)
        d0=min(l,b-1-l,k-b);d1=min(l,b-l,k-b-1)
        assert sum(before.values())==N0 and sum(after.values())==N1
        assert max(before.values())<=d0 and max(after.values())<=d1
        comb=lambda v:sum(x*(x-1)//2 for x in v.values())
        C0=comb(before);C1=comb(after);Cu=comb(u)
        birth_raw=sum(u[z] for z in wp);retire_raw=sum(u[z] for z in wm)
        assert C0==Cu+retire_raw and C1==Cu+birth_raw
        assert C1-C0==sum(u[z]*(wp[z]-wm[z]) for z in wp.keys()|wm.keys())
        delta0=sum(v*(d0-v) for v in before.values());delta1=sum(v*(d1-v) for v in after.values())
        cap0=F((d0-1)*N0,2);cap1=F((d1-1)*N1,2)
        assert delta0==2*cap0-2*C0 and delta1==2*cap1-2*C1
        overlap=sorted(wp.keys()&wm.keys())
        raw_by_l[l]={'l':l,'old_right_ranks':[l+1,b-1],'new_right_ranks':[l+1,b],
          'old_future_ranks':[b+1,k],'new_future_ranks':[b+2,k],
          'common_triple_mass':sum(u.values()),'w_plus_mass':len(wp),'w_minus_mass':len(wm),
          'w_plus_zero_one':True,'w_minus_zero_one':True,'overlap_count':len(overlap),
          'overlap_sites':[{'sum':z,'w_plus_triple':wp_pairs[z],'w_minus_triple':wm_pairs[z]} for z in overlap],
          'N_before':N0,'N_after':N1,'d_before':d0,'d_after':d1,
          'capacity_before_exact':str(cap0),'capacity_after_exact':str(cap1),
          'capacity_change_exact':str(cap1-cap0),'C_common':Cu,'C_raw_before':C0,'C_raw_after':C1,
          'raw_birth':birth_raw,'raw_retirement':retire_raw,'raw_count_change':C1-C0,
          'delta_before':delta0,'delta_after':delta1,'delta_change':delta1-delta0,
          'identity_status':'PASS_EXACT_INTEGER',
          'common_u_nonzero':dict(sorted(u.items())),
          'w_plus_pair_triples':{z:v for z,v in sorted(wp_pairs.items())},
          'w_minus_pair_triples':{z:v for z,v in sorted(wm_pairs.items())}}
    scopes={}
    for selection,bank in banks.items():
        scopes[selection]={}
        for l in (*LS,None):
            subset=[rr for rr in bank if l is None or rr['quad'][1]<=l<rr['quad'][2]]
            before=[rr for rr in subset if rr['quad'][3]<b<rr['i']]
            after=[rr for rr in subset if rr['quad'][3]<b+1<rr['i']]
            born=[rr for rr in subset if rr['quad'][3]==b and rr['i']>b+1]
            retired=[rr for rr in subset if rr['quad'][3]<b and rr['i']==b+1]
            assert len(after)-len(before)==len(born)-len(retired)
            mass=lambda arr:sum(rr['BH_product'] for rr in arr)
            W0=mass(before);W1=mass(after);Wb=mass(born);Wr=mass(retired)
            assert W1-W0==Wb-Wr
            # Boundary rows checked directly with the independent strict-gate routines.
            for rr in born+retired:
                p,q,s,c=rr['quad'];i=rr['i'];r=rr['r'];row=rr['original_record']
                assert len({row[2],row[3],row[4],row[5],i,r})==6
                assert rank_conditions(c,s,i,r) and output_condition(c,row[-1])
            report={'C_core_before':len(before),'C_core_after':len(after),
              'birth_count':len(born),'retirement_count':len(retired),
              'core_count_change':len(after)-len(before),
              'retirement_ge_birth_counts':len(retired)>=len(born),
              'BH_product_before':W0,'BH_product_after':W1,'BH_product_birth':Wb,'BH_product_retirement':Wr,
              'BH_product_change':W1-W0,'retirement_ge_birth_BH':Wr>=Wb,
              'priced_BH_before_exact':str(price*W0),'priced_BH_after_exact':str(price*W1),
              'priced_BH_birth_exact':str(price*Wb),'priced_BH_retirement_exact':str(price*Wr),
              'priced_BH_change_exact':str(price*(W1-W0)),
              'birth_records':born,'retirement_records':retired,
              'boundary_identity_status':'PASS_EXACT_INTEGER_AND_RATIONAL',
              'independent_boundary_strict_gate_check':'PASS_UNKNOWN0'}
            if l is not None:
                raw=raw_by_l[l]
                assert len(before)<=raw['C_raw_before'] and len(after)<=raw['C_raw_after']
                report['E_before']=raw['C_raw_before']-len(before)
                report['E_after']=raw['C_raw_after']-len(after)
                report['D_eff_before']=raw['delta_before']+2*report['E_before']
                report['D_eff_after']=raw['delta_after']+2*report['E_after']
                report['D_eff_change']=report['D_eff_after']-report['D_eff_before']
            scopes[selection][str(l) if l is not None else 'whole_BH_no_l_filter']=report
    result={'input':stem,'C_exact':'1','m0':2,'M':96,'T':T,'component_k':k,
      'cut_before':b,'cut_after':b+1,'left_sizes':list(LS),
      'genuine_component_price_exact':str(price),'H_component':Hk,
      'raw_by_l':raw_by_l,'core_by_selection_and_l':scopes,
      'source_sha256':{str(p.relative_to(HERE)):digest(p) for p in
        [dp,rp,cp,HERE/'small_middle_gap_existing_M96.json',HERE/'independent_checker.py',Path(__file__)]},
      'frozen_source_sha256':data['source_sha256'],
      'scope':'Only two existing M96 histories, k48,T96, cut24->25 and l6/12/18, plus the same-cut whole BH sums. No new histories, horizon sweep or claim of a uniform norm bound.'}
    results.append(result)
    print(json.dumps({'input':stem,'raw':{l:{key:v[key] for key in ['overlap_count','C_raw_before','C_raw_after','raw_birth','raw_retirement','raw_count_change','capacity_change_exact','delta_change']}
        for l,v in raw_by_l.items()},'core':{sel:{l:{key:r[key] for key in ['birth_count','retirement_count','core_count_change','BH_product_birth','BH_product_retirement','BH_product_change','retirement_ge_birth_counts','retirement_ge_birth_BH']}
        for l,r in cells.items()} for sel,cells in scopes.items()}},indent=2))
(HERE/'cut_shift_b24_component48_exact.json').write_text(json.dumps(results,indent=2)+'\n')
