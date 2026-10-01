#!/usr/bin/env python3
"""Only aggregate the existing strict-core BH records; no raw fibers/search."""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,re
from independent_checker import rank_conditions,output_condition

HERE=Path(__file__).resolve().parent
E=HERE.parents[2]
WP=E/'research/u4f_core/WORKING_PROOF.md'
review=json.loads((HERE/'A16_A19_review_source_manifest.json').read_text())
text=WP.read_text();section_hashes={}
for name in ('A16','A17','A18','A19'):
    section=re.search(r'^## '+name+r'\..*?(?=^## |\Z)',text,re.M|re.S).group()
    digest=hashlib.sha256(section.encode()).hexdigest()
    assert digest==review['sections'][name]['sha256']
    section_hashes[name]=digest

results=[]
for stem in ('C1_m02_greedy_M96','C1_m02_dense_variant1_M96'):
    data_path=HERE/(stem+'.json');records_path=HERE/(stem+'_records.json')
    cert_path=HERE/(stem+'_independent_check.json')
    data=json.loads(data_path.read_text());rows=json.loads(records_path.read_text())['records']
    cert=json.loads(cert_path.read_text())
    assert cert['status']=='PASS' and cert['input_sha256']==hashlib.sha256(data_path.read_bytes()).hexdigest()
    assert data['M']==data['T']==96 and data['C_exact']=='1' and data['m0']==2
    assert len(rows)==data['core_records']
    a=[None]+data['a'];M=96
    planes={r:[[0]*(M+1) for _ in range(M+1)] for r in range(2,M+1)}
    BH=[]
    for row in rows:
        d,e,pd,qd,pe,qe,c,s_old,i,r,t=row
        p,q,s,cc=sorted((pd,qd,pe,qe));assert cc==c
        pairs={tuple(sorted((pd,qd))),tuple(sorted((pe,qe)))}
        if pairs=={(p,q),(s,c)}:
            continue  # type 1 is AC-only.
        typ=2 if pairs=={(p,s),(q,c)} else 3
        assert pairs==({(p,s),(q,c)} if typ==2 else {(q,s),(p,c)})
        assert s_old==s
        plane=planes[r]
        # Exactly c<b<i and q<=l<s; neither interval endpoint is changed.
        plane[c+1][q]+=1;plane[i][q]-=1
        plane[c+1][s]-=1;plane[i][s]+=1
        BH.append((p,q,s,c,typ,i,r,row))
    best=None;ties=[];violations=[];tested=0;positive_cells=0
    min_slack=None;by_b={};by_r={}
    for r in range(2,M+1):
        plane=planes[r]
        for b in range(1,M):
            running=0
            for l in range(1,M):
                running+=plane[b][l]
                plane[b][l]=running+plane[b-1][l]
        for b in range(5,r-1):
            n=b-1;m_before=r-1-b
            assert plane[b][1]==plane[b][n-1]==0
            for l in range(2,n-1):
                d=min(l,n-l)
                if m_before<d:
                    continue  # pre-saturation is a separately proved range.
                J=plane[b][l];assert J>=0
                S=l*(n-l);den=(d-1)*S;num=2*J
                slack=den-num;tested+=1;positive_cells+=int(J>0)
                cell={'b':b,'l':l,'new_output_rank':r,'m_before':m_before,
                      'd':d,'pair_bank_size_S':S,'J_core':J,
                      'candidate_bound_exact':str(F(den,2)),
                      'ratio_exact':str(F(num,den)),'ratio_approx':num/den,
                      'effective_deficit_increment_exact':slack,
                      'saturated':True}
                if min_slack is None or slack<min_slack['effective_deficit_increment_exact']:
                    min_slack=cell
                if best is None or num*best[1]>best[0]*den:
                    best=(num,den,cell);ties=[cell]
                elif num*best[1]==best[0]*den:
                    ties.append(cell)
                for table,key in ((by_b,b),(by_r,r)):
                    prev=table.get(key)
                    if prev is None or F(cell['ratio_exact'])>F(prev['ratio_exact']):
                        table[key]=cell
                if slack<0:
                    violations.append(cell)
    assert best is not None
    chosen=best[2];b=chosen['b'];l=chosen['l'];r=chosen['new_output_rank']
    witness=[rec for rec in BH if rec[3]<b<rec[5] and rec[1]<=l<rec[2] and rec[6]==r]
    assert len(witness)==chosen['J_core']
    for p,q,s,c,typ,i,rr,row in witness:
        dd,ee,pd,qd,pe,qe,cc,ss,ii,rrr,t=row
        assert dd==a[qd]-a[pd] and ee==a[qe]-a[pe]
        assert t==dd-ee==a[rr]-a[i]
        assert len({pd,qd,pe,qe,i,rr})==6
        assert rank_conditions(c,s,i,rr) and output_condition(c,t)
    result={'input':stem,'M':96,'T':96,'C_exact':'1','m0':2,
      'status':'STRICT_COUNTEREXAMPLE_FOUND' if violations else 'NO_STRICT_COUNTEREXAMPLE_IN_EXISTING_M96',
      'input_core_records':len(rows),'BH_records_used':len(BH),
      'domain':'5<=b<r-1<=95, 2<=l<=b-3, min(l,b-1-l)<=r-1-b; r is the newly added upper output.',
      'trivial_sides':'l=1 or l=b-2 have d=1 and J_core=0 by six-endpoint order; checked in the aggregate grids.',
      'saturated_nontrivial_cells_tested':tested,'positive_J_cells':positive_cells,
      'worst_ratio':chosen,'all_worst_ties':ties,'minimum_effective_increment':min_slack,
      'worst_by_b':by_b,'worst_by_r':by_r,'violating_cells':violations,
      'worst_witness_original_records':[rec[-1] for rec in witness],
      'worst_witness_BH_types':dict(sorted(Counter(rec[4] for rec in witness).items())),
      'worst_witness_original_strict_gates_independent_check':'PASS_UNKNOWN0',
      'fixed_actual_prefix_through_worst_output':data['a'][:r],
      'source_sha256':{str(p.relative_to(HERE)):hashlib.sha256(p.read_bytes()).hexdigest()
         for p in [data_path,records_path,cert_path,HERE/'independent_checker.py',Path(__file__)]},
      'frozen_source_sha256':data['source_sha256'],
      'scope':'Finite unpriced new-core-collision counts only; records keep original cut/core predicates. No raw-fiber scan, new history, or all-history monotonicity proof.'}
    results.append(result)
    print(json.dumps({key:result[key] for key in ['input','status','BH_records_used',
       'saturated_nontrivial_cells_tested','positive_J_cells','worst_ratio','minimum_effective_increment',
       'worst_witness_BH_types']},indent=2))
out={'date':'2026-09-09','A16_A19_source_section_hashes_confirmed':section_hashes,
 'working_proof_sha256':hashlib.sha256(WP.read_bytes()).hexdigest(),
 'results':results,'new_histories_generated':0,'raw_fiber_tests_repeated':False,
 'logical_limit':'If no counterexample is found, the saturated all-history candidate remains unproved. Passing the full core count implies passing for any fixed subset of the same old quadruples on these finite inputs.'}
(HERE/'saturated_Jcore_existing_M96_exact.json').write_text(json.dumps(out,indent=2)+'\n')
