#!/usr/bin/env python3
"""One existing-history component, with all losses reconstructed exactly."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json
from independent_checker import log_fixed,SCALE

HERE=Path(__file__).resolve().parent
b,k,T=24,48,96
n=b-1;m=min(k,T)-b
threshold_path=HERE/'small_middle_gap_existing_M96.json'
threshold_data=json.loads(threshold_path.read_text())
results=[]

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

for stem in ['C1_m02_greedy_M96','C1_m02_dense_variant1_M96']:
    data_path=HERE/(stem+'.json')
    record_path=HERE/(stem+'_records.json')
    cert_path=HERE/(stem+'_independent_check.json')
    data=json.loads(data_path.read_text())
    rows=json.loads(record_path.read_text())['records']
    cert=json.loads(cert_path.read_text())
    assert cert['status']=='PASS' and cert['input_sha256']==sha(data_path)
    a=data['a'];assert len(a)==96 and data['C_exact']=='1' and data['m0']==2
    assert len(rows)==data['core_records']
    aa=[None]+a
    g={l:aa[l+1]-aa[l] for l in range(1,n)}
    H_b=aa[b]-aa[1];H_k=aa[k]-aa[1]
    price=(F(1,k*k*(k-1)**2)-F(1,k*k*(k+1)**2))/(H_k*H_k)
    thresholds=next(t['thresholds_floor_certified'] for t in threshold_data if t['input']==stem)
    for c in range(4,b):
        lo,hi=log_fixed(c)
        low=F(c*c*SCALE**3,hi**3);high=F(c*c*SCALE**3,lo**3)
        assert low.numerator//low.denominator==high.numerator//high.denominator==thresholds[str(c)]

    selected={'all_core':{},'all_large_old_gaps_core':{}}
    for row in rows:
        d,e,pd,qd,pe,qe,c,s_old,i,r,t=row
        if not (c<b<i<r<=min(k,T)):
            continue
        p,q,s,c_quad=sorted((pd,qd,pe,qe))
        assert c==c_quad
        pairs={tuple(sorted((pd,qd))),tuple(sorted((pe,qe)))}
        A=aa[q]-aa[p];B=aa[s]-aa[q];Cgap=aa[c]-aa[s];H=aa[c]-aa[p]
        if pairs=={(p,q),(s,c)}:
            assert d*e==A*Cgap
            continue  # AC-only type 1 must not duplicate a BH collision.
        typ=2 if pairs=={(p,s),(q,c)} else 3
        assert pairs==({(p,s),(q,c)} if typ==2 else {(q,s),(p,c)})
        assert d*e==(A*Cgap+B*H if typ==2 else B*H)
        assert s_old==s
        key=(p,q,s,c,typ,i,r)
        assert key not in selected['all_core']
        payload={'B':B,'Hquad':H,'original_row':row}
        selected['all_core'][key]=payload
        if min(A,B,Cgap)>thresholds[str(c)]:
            selected['all_large_old_gaps_core'][key]=payload

    U=F(0);capacity_deficit=F(0)
    all_l=[]
    for l in range(1,n):
        dcap=min(l,n-l,m);N=l*(n-l)*m
        fibers=defaultdict(list)
        for u in range(1,l+1):
            for v in range(l+1,n+1):
                for f in range(b+1,min(k,T)+1):
                    fibers[aa[u]+aa[v]+aa[f]].append((u,v,f))
        size_hist=Counter(map(len,fibers.values()))
        assert sum(size*count for size,count in size_hist.items())==N
        assert max(size_hist,default=0)<=dcap
        delta=sum(len(v)*(dcap-len(v)) for v in fibers.values())
        C_all=sum(len(v)*(len(v)-1)//2 for v in fibers.values())
        assert 2*C_all==(dcap-1)*N-delta
        keys=set()
        for triples in fibers.values():
            for tr1,tr2 in combinations(triples,2):
                assert len(set(tr1+tr2))==6
                p,q=sorted((tr1[0],tr2[0]));s,c=sorted((tr1[1],tr2[1]))
                i,r=sorted((tr1[2],tr2[2]))
                oldpairs={(tr1[0],tr1[1]),(tr2[0],tr2[1])}
                typ=3 if oldpairs=={(p,s),(q,c)} else 2
                assert oldpairs==({(p,s),(q,c)} if typ==3 else {(p,c),(q,s)})
                key=(p,q,s,c,typ,i,r)
                assert key not in keys
                keys.add(key)
        assert len(keys)==C_all
        core_counts={}
        for label,bank in selected.items():
            wanted={key for key in bank if key[1]<=l<key[2]}
            assert wanted<=keys
            assert len(wanted)==sum(key in bank for key in keys)
            core_counts[label]=len(wanted)
        U+=F(H_b,2)*g[l]*(dcap-1)*N
        capacity_deficit+=F(H_b,2)*g[l]*delta
        all_l.append({'l':l,'g_l':g[l],'d_capacity':dcap,'N_triples':N,
                      'fiber_size_histogram':dict(sorted(size_hist.items())),
                      'delta_exact':delta,'C_all':C_all,'C_core_by_selection':core_counts,
                      'E_by_selection':{label:C_all-v for label,v in core_counts.items()}})
    scopes={}
    for label,bank in selected.items():
        gate=sum(F(H_b)*g[row['l']]*row['E_by_selection'][label] for row in all_l)
        outer=sum(F(v['B'])*(H_b-v['Hquad']) for v in bank.values())
        raw=sum(F(v['B'])*v['Hquad'] for v in bank.values())
        assert raw==U-capacity_deficit-gate-outer
        assert all(v>=0 for v in (U,capacity_deficit,gate,outer,raw))
        terms={'capacity_U':U,'capacity_deficit':capacity_deficit,'gate_deletion':gate,
               'outer_width_loss':outer,'actual_raw_BH':raw}
        scopes[label]={'eligible_BH_matching_records':len(bank),
            'matching_type_counts':dict(sorted(Counter(key[4] for key in bank).items())),
            'raw_terms_exact':{name:str(v) for name,v in terms.items()},
            'terms_over_U_exact':{name:str(v/U) for name,v in terms.items()},
            'terms_over_U_approx':{name:float(v/U) for name,v in terms.items()},
            'priced_component_terms_exact':{name:str(price*v) for name,v in terms.items()},
            'identity_status':'PASS_EXACT_RATIONAL',
            'selected_record_keys_and_widths':[{'key':list(key),'B':v['B'],'Hquad':v['Hquad']}
                                                for key,v in sorted(bank.items())]}
    result={'input':stem,'b':b,'k':k,'T':T,'M':96,'n':n,'m':m,'H_b':H_b,'H_k':H_k,
        'g_old':g,'genuine_single_component_price_exact':str(price),
        'component_price_scope':'kappa_48/H_48^2 only, not u_r and not a terminal reset',
        'per_l_exact':all_l,'scopes':scopes,'unknown_log_comparisons':0,
        'source_sha256':{str(p.relative_to(HERE)):sha(p) for p in
              [data_path,record_path,cert_path,threshold_path,Path(__file__)]},
        'frozen_source_sha256':data['source_sha256'],
        'scope':'Existing two M96 histories, single b24/k48/T96 component. Does not establish an all-rank deficit lower bound.'}
    results.append(result)
    print(json.dumps({'input':stem,'H_b':H_b,'H_k':H_k,'scopes':{label:{name:value for name,value in scope.items()
          if name in ['eligible_BH_matching_records','matching_type_counts','raw_terms_exact','terms_over_U_approx','identity_status']}
          for label,scope in scopes.items()}},indent=2))
(HERE/'tripartite_deficit_b24_k48_exact.json').write_text(json.dumps(results,indent=2)+'\n')
