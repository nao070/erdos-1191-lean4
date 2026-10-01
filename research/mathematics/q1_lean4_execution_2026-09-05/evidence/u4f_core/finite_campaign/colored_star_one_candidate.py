#!/usr/bin/env python3
"""One explicit t64 colored-star graph; broad authorized trial budget unused."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,random
from reference_evaluator import differences,cap_check,rank_core,physical_core
from independent_checker import log_fixed,SCALE,rank_conditions,output_condition

HERE=Path(__file__).resolve().parent;OUT=HERE/'C100000000000000_m02_colored_star'
OUT.mkdir(exist_ok=True)
C=F(10**14);m0=2;seed=119120064;t=64;half=t//2
def save(name,v): (OUT/name).write_text(json.dumps(v,indent=2)+'\n')
save('campaign_fixed_before_trials.json',{'C_exact':str(C),'m0':m0,'authorized_t':[64,96],
 'authorized_max_trials_per_t':200,'actual_plan':'One explicit t64 candidate only, then analytical review.',
 'seed':seed,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
rng=random.Random(seed);span=10**10;step=span//(t-1);h=6*10**9;X=10**12
R=[2*span+j*step+rng.randrange(-step//8,step//8+1) for j in range(t)]
cycle=list(range(0,half,2))+list(range(1,half,2))[::-1]
next_j={cycle[j]:cycle[(j+1)%half] for j in range(half)}
edges=[(j,half+j,1) for j in range(half)]+[(half+j,next_j[j],1) for j in range(half)]
shift=8
edges += [(j,half+j+shift,-1) for j in range(half-shift)]
ts=[R[v]-R[u]+sign*h for u,v,sign in edges]
assert min(ts)>0 and len(ts)==len(set(ts))
cut=R[-1]+span//7+12345
a=[1,1+h]+R+[cut]+sorted(X-v for v in ts)+[X]
b=t+3;l=2;M=len(a)
candidate={'t':t,'trial':1,'C_exact':str(C),'m0':m0,'b':b,'l':l,'M':M,'T':M,
 'h':h,'X':X,'R':R,'a':a,'cut_point':cut,'edges':[{'u':u,'v':v,'sign':sign,'t_value':vout}
       for (u,v,sign),vout in zip(edges,ts)],'actual_trials_by_t':{'64':1,'96':0}}
save('candidate_t64_trial1.json',candidate)
try:
    diff=differences(a)
except AssertionError as ex:
    save('result.json',{'status':'ACTUAL_SIDON_FAILED','error':str(ex),'actual_trials_by_t':{'64':1,'96':0},
         'scope':'One explicit candidate only, no impossibility claim.'})
    print(json.dumps({'status':'ACTUAL_SIDON_FAILED','error':str(ex)}));raise SystemExit(0)
# Independent repeated two-sum check, including doubled points.
sums={}
for i in range(M):
    for j in range(i,M):
        value=a[i]+a[j];assert value not in sums,(i,j,sums.get(value));sums[value]=(i,j)
caps=cap_check(a,C,m0)
for n in range(m0,M+1):
    lo,hi=log_fixed(2*n)
    assert (a[n-1]-a[0])*SCALE<=C.numerator*n*n*lo
future={X-a[i-1]:i for i in range(b+1,M)}
raw=[];core=[];failures={}
for low in range(t):
    for high in range(low+1,t):
        s=low+3;c=high+3;delta=R[high]-R[low]
        for typ,vout in [(2,abs(delta-h)),(3,delta+h)]:
            i=future.get(vout)
            if i is None:continue
            assert c<b<i<M
            rr={'quad_ranks':[1,2,s,c],'type':typ,'c':c,'s':s,'i':i,'r':M,'t':vout}
            ref_rank=rank_core(c,s,i,M);ref_phys=physical_core(c,vout)
            assert ref_rank is not None and ref_phys is not None
            ind_rank=rank_conditions(c,s,i,M);ind_phys=output_condition(c,vout)
            assert ref_rank==ind_rank and ref_phys==ind_phys
            rr['strict_core']=bool(ref_rank and ref_phys);raw.append(rr)
            if rr['strict_core']:core.append(rr)
            else:
                lc,uc=log_fixed(c);lr,ur=log_fixed(M)
                tests={'old_partner':s*lc*lc>c*SCALE*SCALE,
                    'coverage':(i-c)*lc*lc>c*SCALE*SCALE,
                    'top_lag':(M-i)*lr**3>M*SCALE**3,
                    'far_output':c*lc>M*SCALE,
                    'physical_output':vout*lc**3>c*c*SCALE**3}
                rr['failed_gates']=[name for name,passes in tests.items() if not passes]
                for name in rr['failed_gates']:failures[name]=failures.get(name,0)+1
# Independent new-future collision reconstruction from the full actual pair bank.
bank={a[p-1]+a[q-1]:(p,q) for p in (1,2) for q in range(3,t+3)}
assert len(bank)==2*t
oldfib={}
for f in range(b+1,M):
    for value,(p,q) in bank.items():oldfib.setdefault(a[f-1]+value,[]).append((p,q,f))
ind_core=[];ind_raw=[]
for value,(p,q) in bank.items():
    for pp,qq,i in oldfib.get(X+value,[]):
        assert len({p,q,pp,qq,i,M})==6
        s,c=sorted((q,qq))
        typ=3 if (p==1 and q==s) or (pp==1 and qq==s) else 2
        key=(s,c,typ,i,M,X-a[i-1]);ind_raw.append(key)
        if rank_conditions(c,s,i,M) and output_condition(c,X-a[i-1]):ind_core.append(key)
assert sorted(ind_raw)==sorted((r['s'],r['c'],r['type'],r['i'],r['r'],r['t']) for r in raw)
assert sorted(ind_core)==sorted((r['s'],r['c'],r['type'],r['i'],r['r'],r['t']) for r in core)
result={'status':'CERTIFIED_SATURATED_JCORE_COUNTEREXAMPLE' if len(core)>t else 'ACTUAL_SIDON_BUT_TARGET_NOT_REACHED',
 'C_exact':str(C),'m0':m0,'t':t,'b':b,'l':l,'M':M,'T':M,'S':2*t,'d':2,'m_before':M-1-b,
 'J_raw':len(raw),'J_core':len(core),'candidate_bound_exact':str(t),
 'ratio_exact':str(F(len(core),t)),'effective_deficit_increment_exact':2*t-2*len(core),
 'positive_differences':len(diff),'repeated_two_sum_independent_check':'PASS',
 'all_rank_cap_independent_check':'PASS','cap_certificates':caps,'unknown_comparisons':0,
 'gate_failure_counts_nonexclusive':failures,'all_raw_target_collisions':raw,'strict_core_target_collisions':core,
 'independent_pair_bank_collision_check':'PASS','actual_trials_by_t':{'64':1,'96':0},
 'scope':'Only the target new-output J_core and actual Sidon/all-rank fixed cap are certified. Full profile is not evaluated. Any counterexample rejects saturated gate-adjusted monotonicity only, not U4F/Q1.',
 'source_sha256':{str(p.relative_to(HERE)):hashlib.sha256(p.read_bytes()).hexdigest()
        for p in [Path(__file__),HERE/'reference_evaluator.py',HERE/'independent_checker.py',OUT/'candidate_t64_trial1.json']}}
save('result.json',result)
print(json.dumps({key:result[key] for key in ['status','t','b','l','M','J_raw','J_core','candidate_bound_exact',
       'ratio_exact','effective_deficit_increment_exact','gate_failure_counts_nonexclusive']},indent=2))
