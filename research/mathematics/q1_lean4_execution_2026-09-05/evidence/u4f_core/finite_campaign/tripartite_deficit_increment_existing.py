#!/usr/bin/env python3
"""Bounded future-addition potential check on existing M96 histories only."""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import hashlib,json

HERE=Path(__file__).resolve().parent
stems=['C1_m02_greedy_M96','C1_m02_dense_variant1_M96']
inputs={stem:json.loads((HERE/(stem+'.json')).read_text()) for stem in stems}
results=[];violations=[]
for b in (24,12,48):
    batch=[]
    for stem in stems:
        a=[None]+inputs[stem]['a'];n=b-1
        cert=json.loads((HERE/(stem+'_independent_check.json')).read_text())
        assert cert['status']=='PASS'
        assert cert['input_sha256']==hashlib.sha256((HERE/(stem+'.json')).read_bytes()).hexdigest()
        for l in range(1,n):
            U={}
            for u in range(1,l+1):
                for v in range(l+1,n+1):
                    value=a[u]+a[v]
                    assert value not in U
                    U[value]=(u,v)
            size=len(U);assert size==l*(n-l)
            fiber=Counter(a[b+1]+value for value in U)
            m=1;d=min(l,n-l,m);Q=sum(v*v for v in fiber.values())
            delta=d*size*m-Q;assert delta==0
            minrow=None;negative_count=0;zero_count=0;tested=0
            for k in range(b+1,96):
                assert m==k-b
                dp=min(l,n-l,m+1)
                J=sum(fiber.get(a[k+1]+value,0) for value in U)
                change=(dp-d)*size*m+(dp-1)*size-2*J
                row={'input':stem,'b':b,'l':l,'k_before':k,'new_rank':k+1,
                     'm_before':m,'d_before':d,'d_after':dp,'pair_bank_size':size,
                     'J_new_collisions':J,'delta_before':delta,'delta_increment':change}
                if minrow is None or change<minrow['delta_increment']:
                    minrow=dict(row)
                if change<0:
                    negative_count+=1
                    witness=dict(row)
                    witness['actual_prefix']=a[1:k+2]
                    witness['old_pair_sum_bank']=[{'sum':value,'left_rank':u,'right_rank':v,
                          'left_point':a[u],'right_point':a[v]} for value,(u,v) in sorted(U.items())]
                    witness['overlap_at_new_sites']=[{'z':a[k+1]+value,
                          'old_fiber_size':fiber.get(a[k+1]+value,0),'new_pair_sum':value}
                          for value in sorted(U) if fiber.get(a[k+1]+value,0)]
                    witness['fiber_size_histogram_before']=dict(sorted(Counter(fiber.values()).items()))
                    assert sum(v*(d-v) for v in fiber.values())==delta
                if change==0:zero_count+=1
                for value in U:
                    z=a[k+1]+value;fiber[z]+=1
                    assert fiber[z]<=dp
                Q+=2*J+size;m+=1
                newdelta=dp*size*m-Q
                assert newdelta==delta+change and newdelta>=0
                if change<0:
                    witness['delta_after']=newdelta
                    witness['fiber_size_histogram_after']=dict(sorted(Counter(fiber.values()).items()))
                    assert sum(v*(dp-v) for v in fiber.values())==newdelta
                    witness['independent_direct_delta_reconstruction']='PASS'
                    violations.append(witness)
                d=dp;delta=newdelta;tested+=1
            assert sum(v*v for v in fiber.values())==Q
            assert sum(v*(d-v) for v in fiber.values())==delta
            batch.append({'input':stem,'b':b,'l':l,'steps_tested':tested,
                          'negative_steps':negative_count,'zero_steps':zero_count,
                          'minimum_increment_witness':minrow,'final_delta':delta})
    results.extend(batch)
    print(json.dumps({'b':b,'steps':sum(v['steps_tested'] for v in batch),
          'negative_steps':sum(v['negative_steps'] for v in batch),
          'minimum_nontrivial_increment':min(v['minimum_increment_witness']['delta_increment']
                              for v in batch if 1<v['l']<b-2)},indent=2))
    if violations:
        break
violations.sort(key=lambda v:(v['new_rank'],stems.index(v['input']),v['l']))
out={'status':'CERTIFIED_NEGATIVE_INCREMENT' if violations else 'NO_NEGATIVE_INCREMENT_IN_BOUNDED_SCOPE',
     'scope':'Existing two C1,m02,M96 histories only. b24 checked first; if no negative, b12 then b48. No history generation or core re-enumeration.',
     'tests':results,'total_steps':sum(v['steps_tested'] for v in results),
     'negative_steps':len(violations),
     'first_negative_order':'Smallest new rank, then greedy before variant1, then l, in first tested b batch with a violation.',
     'first_negative':violations[0] if violations else None,
     'all_negative_summary':[{key:v[key] for key in ['input','b','l','k_before','new_rank','J_new_collisions','delta_before','delta_increment','delta_after']}
                             for v in violations],
     'source_sha256':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
          for name in [s+'.json' for s in stems]+[s+'_independent_check.json' for s in stems]+[Path(__file__).name]},
     'logical_limit':'Finite checks do not establish monotonicity, uniform deficit ratios, U4F, or Q1. A negative increment, if present, rejects only future-addition monotonicity of this exact deficit.'}
(HERE/'tripartite_deficit_increment_existing_exact.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'total_steps':out['total_steps'],
      'negative_steps':out['negative_steps'],'first_negative':None if not violations else
       {key:violations[0][key] for key in ['input','b','l','new_rank','J_new_collisions','delta_before','delta_increment','delta_after']}},indent=2))
