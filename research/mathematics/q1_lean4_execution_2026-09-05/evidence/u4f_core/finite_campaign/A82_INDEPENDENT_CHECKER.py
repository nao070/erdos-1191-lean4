#!/usr/bin/env python3
"""Independent prescribed A82 hub certificate; no full-profile invocation."""
import sys
sys.dont_write_bytecode = True
import hashlib
import importlib.util
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def helper(name):
    spec = importlib.util.spec_from_file_location(name, HERE/(name+'.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    certpath = HERE/'A82_TWO_FUTURE_DEGREE_COUNTEREXAMPLE.json'
    cert = json.loads(certpath.read_text())
    for name,digest in cert['source_sha256'].items():
        assert sha(HERE/name) == digest, name
    history_name = cert['campaign']+'.json'
    hist = json.loads((HERE/history_name).read_text())
    saved_rows = json.loads((HERE/(cert['campaign']+'_records.json')).read_text())['records']
    full_check = json.loads((HERE/(cert['campaign']+'_independent_check.json')).read_text())
    ref, ind = helper('reference_evaluator'), helper('independent_checker')
    a = [None]+hist['a']; C=10**35; M=T=k=45; b=37; L=C
    assert (hist['C_exact'],hist['m0'],hist['M'],hist['T']) == (str(C),2,M,T)
    assert (cert['C_exact'],cert['m0'],cert['M'],cert['T'],cert['b'],cert['k']) == (str(C),2,M,T,b,k)
    assert full_check['status']=='PASS' and full_check['core_records']==135
    assert full_check['input_sha256']==sha(HERE/history_name)
    assert full_check['checker_sha256']==sha(HERE/'independent_checker.py')
    assert full_check['unknown_comparisons']==0 and len(saved_rows)==135
    assert hist['core_records']==135 and hist['unknown_core_comparisons']==0
    offsets=[1000*10**j for j in range(8)]
    old=[1,3*L+1]
    expected_pairs=[]
    for e,(i,r) in enumerate(list(itertools.combinations(range(1,8),2))[:17]):
        z=1000*10**(10+e); t=offsets[r]-offsets[i]
        p,q=L+z+1,2*L+t-z+1
        old.extend([p,q]);expected_pairs.append((p,q,t,i,r))
    reconstructed=sorted(old)+[7*L//2+1]+[4*L+f+1 for f in offsets]
    assert reconstructed==hist['a']
    assert all(a[i]<a[i+1] for i in range(1,M))
    differences={};two_sums={}
    for y in range(1,M+1):
        for x in range(1,y):
            d=a[y]-a[x]
            assert d>0 and d not in differences
            differences[d]=(x,y)
        for x in range(1,y+1):
            val=a[y]+a[x]
            assert val not in two_sums
            two_sums[val]=(x,y)
    caps=[]
    for n in range(2,M+1):
        lo,hi=ref.log_bounds(2*n); ilo,ihi=ind.log_fixed(2*n); H=a[n]-a[1]
        assert H<=C*n*n*lo and H*ind.SCALE<=C*n*n*ilo
        caps.append({'n':n,'H':H,'status':'PASS','reference_log_interval':[str(lo),str(hi)],
                     'independent_log_numerators':[str(ilo),str(ihi)],'independent_log_denominator':str(ind.SCALE)})
    hub=(1,36); hubsum=a[1]+a[36]
    future={a[r]-a[i]:(i,r) for i,r in itertools.combinations(range(b+1,k+1),2)}
    neighbors={}
    for p,q in itertools.combinations(range(1,b),2):
        if len({*hub,p,q})!=4 or not max(hub[0],p)<min(hub[1],q):continue
        t=abs(a[p]+a[q]-hubsum)
        if t in future:neighbors[(p,q)]=future[t]
    oldsum={a[p]+a[q]:(p,q) for p,q in itertools.combinations(range(1,b),2)}
    reverse={}
    for t,out in future.items():
        for s in (hubsum-t,hubsum+t):
            pair=oldsum.get(s)
            if pair and len(set(hub+pair))==4 and max(hub[0],pair[0])<min(hub[1],pair[1]):
                assert pair not in reverse
                reverse[pair]=out
    assert neighbors==reverse and len(neighbors)==17
    assert sorted(map(list,neighbors))==sorted(cert['all_neighbours'])
    pos={value:i for i,value in enumerate(a) if i}
    assert {(pos[p],pos[q]) for p,q,*_ in expected_pairs}==set(neighbors)

    def gate_check(row):
        d,e,x,y,w,z,c,s,i,r,t=row
        lc,uc=ref.log_bounds(c);lr,ur=ref.log_bounds(r)
        refbounds=[(s*lc**2,s*uc**2,c),((i-c)*lc**2,(i-c)*uc**2,c),
                   ((r-i)*lr**3,(r-i)*ur**3,r),(c*lc,c*uc,r),(t*lc**3,t*uc**3,c*c)]
        decisions=[ref.strict_positive(lo,hi,rhs) for lo,hi,rhs in refbounds]
        il,iu=ind.log_fixed(c);rl,ru=ind.log_fixed(r);S=ind.SCALE
        intbounds=[(s*il**2,s*iu**2,c*S*S),((i-c)*il**2,(i-c)*iu**2,c*S*S),
                   ((r-i)*rl**3,(r-i)*ru**3,r*S**3),(c*il,c*iu,r*S),(t*il**3,t*iu**3,c*c*S**3)]
        idecisions=[True if lo>rhs else False if hi<=rhs else None for lo,hi,rhs in intbounds]
        assert decisions==idecisions and None not in decisions
        names=['older_birth','birth_to_lower_output','output_rank_gap','birth_log_upper_output','physical_output']
        return {'status':'PASS' if all(decisions) else 'FAIL',
                'gates':{name:{'pass':decision,'independent_margin_integer_interval':[str(lo-rhs),str(hi-rhs)]}
                         for name,decision,(lo,hi,rhs) in zip(names,decisions,intbounds)},
                'margin_scales':[str(S*S),str(S*S),str(S**3),str(S),str(S**3)]}

    details=[];weighted=F(0);all_hub_rows=[]
    for (p,q),(i,r) in sorted(neighbors.items()):
        quad=(1,p,q,36); t=a[r]-a[i];rows=[]
        for (x,y),(w,z) in [((1,p),(q,36)),((1,q),(p,36)),((1,36),(p,q))]:
            d,e=a[y]-a[x],a[z]-a[w]
            if d<e:d,e,x,y,w,z=e,d,w,z,x,y
            if d-e!=t:continue
            row=[d,e,x,y,w,z,max(y,z),min(y,z),i,r,t]
            assert len({x,y,w,z,i,r})==6 and row[6]<b<i<r<=k
            gates=gate_check(row);count=saved_rows.count(row)
            assert count==(1 if gates['status']=='PASS' else 0)
            rows.append({'record':row,'product':d*e,'core':gates,'original_cut_interval':[row[6]+1,i-1],
                         'saved_original_core_bank_occurrences':count})
            all_hub_rows.append(row)
        assert len(rows)==2
        h,j=a[36]-a[1],a[q]-a[p]
        K=F(max((h+j)**2-t*t,0)+max((h-j)**2-t*t,0),4)
        full=sum(row['product'] for row in rows);core=sum(row['product'] for row in rows if row['core']['status']=='PASS')
        assert K==full and core>0
        theta=F(core,full);weighted+=theta
        details.append({'neighbor':[p,q],'points':[a[p],a[q]],'output':[i,r],'t':t,
                        'K_full':full,'K_core':core,'theta_exact':str(theta),'records':rows})
    assert len({tuple(row) for row in all_hub_rows})==34
    strict_count=sum(row['core']['status']=='PASS' for e in details for row in e['records'])
    assert strict_count==33 and sum(e['theta_exact']=='1' for e in details)==16
    for w in cert['witnesses']:
        match=next(e for e in details if e['neighbor']==w['neighbour'])
        assert any(rr['record']==w['record'] and rr['core']['status']=='PASS' for rr in match['records'])
    assert weighted>16
    alpha=lambda j:F(1,j*j*(j-1)**2)
    lambdas={j:(alpha(j)-alpha(j+1))/(a[j]-a[1])**2 for j in range(2,M+1)}
    output_ranks=sorted({e['output'][1] for e in details})
    prices={r:sum((lambdas[j] for j in range(r,M+1)),F(0)) for r in output_ranks}
    out={'attempt':'A82','status':'PASS_INDEPENDENT_HUB_AND_WEIGHTED_DEGREE_COUNTEREXAMPLE',
         'campaign':{'C_exact':str(C),'m0':2,'M':M,'T':T,'b':b,'k':k},
         'source_sha256':{name:sha(HERE/name) for name in [certpath.name,history_name,cert['campaign']+'_records.json',
            cert['campaign']+'_independent_check.json','reference_evaluator.py','independent_checker.py',Path(__file__).name]},
         'construction_matches_actual_input':True,'positive_difference_count':len(differences),
         'repeated_two_sum_count':len(two_sums),'all_rank_cap_certificates':caps,
         'hub':list(hub),'hub_points':[a[x] for x in hub],'old_count':36,'future_count':8,
         'degree':len(neighbors),'strict_core_edge_degree':len(neighbors),'proposed_2m':16,
         'hub_source_channels':34,'strict_hub_source_channels':strict_count,
         'weighted_degree_exact':str(weighted),'weighted_degree_excess_over_2m_exact':str(weighted-16),
         'neighbors':details,'UNKNOWN':0,'genuine_lambda45_exact':str(lambdas[45]),
         'genuine_full_u_r_M45_exact':{str(r):str(p) for r,p in prices.items()},
         'alpha46_preserved_exact':str(alpha(46)),
         'saved_full_profile_check':{'status':full_check['status'],'core_records':full_check['core_records'],
             'verified':full_check['verified'],'rerun_in_this_task':False},
         'scope':['One existing fixed huge-C finite history; no new history/profile run.',
                  'Actual original strict-core hub only; later fully localized residual selectors are not checked.',
                  'Unweighted degree and theta=K_core/K_full weighted degree both exceed 2m.',
                  'No asymptotic family, uniform-K nonexistence, or Q1 conclusion.']}
    p=HERE/'A82_INDEPENDENT_CHECK.json';p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','all_rank_cap_certificates','neighbors','genuine_full_u_r_M45_exact']},indent=2))
    print('HASHES',json.dumps({Path(__file__).name:sha(Path(__file__)),p.name:sha(p)}))


if __name__=='__main__':main()
