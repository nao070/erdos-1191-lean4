#!/usr/bin/env python3
"""One prescribed history and feasible lower certificate; no reference import.

Full core completeness is reused from the saved source-bound independent
output checker. This file does not regenerate or rewrite that full profile.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations,combinations_with_replacement
from functools import lru_cache
import hashlib,json
from independent_checker import log_fixed,SCALE

HERE=Path(__file__).resolve().parent
CP=HERE/'A72_SOURCE_ALLOWANCE_COUNTEREXAMPLE.json'
OUT=HERE/'A72_SOURCE_ALLOWANCE_CHECK.json'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

@lru_cache(None)
def bounds(n):
    lo,hi=log_fixed(n)
    return Q(lo,SCALE),Q(hi,SCALE)

def verify():
    cert=json.loads(CP.read_text());cert_hash=sha(CP)
    sources=cert['source_sha256']
    for name,h in sources.items():assert sha(HERE/name)==h, ('Source hash',name)
    C=1<<67;L=1<<60;c,b,k,M,T,m0=24,25,50,50,50,2
    assert Q(cert['C_exact'])==C and cert['m0']==m0
    assert (cert['c'],cert['b'],cert['k'],cert['M'],cert['T'])==(c,b,k,M,T)
    base=[0]+list(range(98,121))+[300]+[400+4*j for j in range(25)]
    perturb=[1<<j for j in range(1,51)]
    perturb[41]=perturb[23]+perturb[7]+perturb[39]-perturb[3]-perturb[19]
    a=[L*base[j]+perturb[j]-1 for j in range(50)]
    value=lambda r:a[r-1]
    assert len(a)==50 and a[0]==1 and all(a[j]<a[j+1] for j in range(49))
    assert cert['construction']['L']==L
    assert cert['construction']['base_values']==base and cert['construction']['perturbations']==perturb
    exceptional_bits=[j for j in range(51) if perturb[41]>>j&1]
    assert exceptional_bits==[4,5,6,7,20,21,22,23,40]
    assert all((perturb[41]+(1<<j)).bit_count()>=6 for j in range(1,51) if j!=42)
    assert (2*perturb[41]).bit_count()==9
    assert max(perturb)*2<L

    hp=HERE/(cert['campaign']+'.json')
    rp=HERE/(cert['campaign']+'_records.json')
    ip=HERE/(cert['campaign']+'_independent_check.json')
    history=json.loads(hp.read_text());record_bank=json.loads(rp.read_text());prior=json.loads(ip.read_text())
    assert history['a']==a and Q(history['C_exact'])==C
    assert (history['m0'],history['M'],history['T'])==(m0,M,T)
    assert prior['status']=='PASS' and prior['M']==M and prior['core_records']==1
    assert prior['input_sha256']==sha(hp) and prior['checker_sha256']==sha(HERE/'independent_checker.py')
    assert 'every core record by output-centric reconstruction' in prior['verified']
    assert prior['unknown_comparisons']==0

    differences={}
    for lower,upper in combinations(range(1,51),2):
        diff=value(upper)-value(lower)
        assert diff>0 and diff not in differences, ('Duplicate positive difference',lower,upper)
        differences[diff]=[lower,upper]
    sums={}
    for x,y in combinations_with_replacement(range(1,51),2):
        sm=value(x)+value(y)
        assert sm not in sums, ('Repeated two-sum collision',x,y,sums.get(sm))
        sums[sm]=[x,y]
    assert len(differences)==1225 and len(sums)==1275

    cap=[]
    for rank in range(m0,M+1):
        lo,hi=bounds(2*rank);Hn=value(rank)-value(1)
        lower=C*rank*rank*lo-Hn;upper=C*rank*rank*hi-Hn
        assert lower>0, ('Cap not certified',rank)
        cap.append({'rank':rank,'H_rank':Hn,'cap_margin_interval':[str(lower),str(upper)]})
    assert value(M)-value(1)<512*L==4*C
    assert bounds(4)[0]>1

    d=value(24)-value(4);e=value(20)-value(8);t=value(42)-value(40)
    row=[d,e,4,24,8,20,24,20,40,42,t]
    assert d>e>0 and d-e==t>0 and len({4,24,8,20,40,42})==6
    assert value(24)+value(8)+value(40)==value(4)+value(20)+value(42)
    assert row==cert['selected_record'] and record_bank['records']==[row]
    assert history['core_records']==cert['core_records']==1
    lc,uc=bounds(c);lr,ur=bounds(42);lb,ub=bounds(b)
    strict={
      'older_birth':(20*lc**2-c,20*uc**2-c),
      'birth_output_gap':(16*lc**2-c,16*uc**2-c),
      'output_top_gap':(2*lr**3-42,2*ur**3-42),
      'upper_rank':(c*lc-42,c*uc-42),
      'physical_output':(t*lc**3-c*c,t*uc**3-c*c)}
    assert all(lo>0 for lo,hi in strict.values())
    old_quad=[4,8,20,24]
    gaps=[value(y)-value(x) for x,y in zip(old_quad,old_quad[1:])]
    delay=(40-c)**2*min(c,42-c)
    flags={
      'A43_not_short_component':((k-b)**4*lb**3-b**4,(k-b)**4*ub**3-b**4),
      'A42_not_cut_far':(b**8*lb**5-(k-1)**8,b**8*ub**5-(k-1)**8),
      'A33_not_cut_span_far':((value(b)-1)*lb**2-(value(k)-1),(value(b)-1)*ub**2-(value(k)-1)),
      'A45_large_smaller_source':(e**4*lb**5-b**8,e**4*ub**5-b**8),
      'A46_large_output':(t*t*lb**5-b**4,t*t*ub**5-b**4),
      'A46_large_min_old_gap':(min(gaps)**2*lb**5-b**4,min(gaps)**2*ub**5-b**4),
      'A45_source_upper_rank':(20**8*(2*C)**4*lb**9-b**8,20**8*(2*C)**4*ub**9-b**8),
      'A53_not_birth_far':(c**8*lc**5-(k-1)**8,c**8*uc**5-(k-1)**8),
      'A54_not_birth_span_far':((value(c)-1)*lc**2-(value(k)-1),(value(c)-1)*uc**2-(value(k)-1)),
      'A57_reverse_delay_product':(delay**4*lc**9-c**12,delay**4*uc**9-c**12)}
    assert all(lo>0 for lo,hi in flags.values())
    for key,(lower,upper) in flags.items():
        assert Q(cert['selected_record_residual_flags']['independent'][key])==lower
        assert Q(cert['selected_record_residual_flags']['reference'][key])>0
    center=value(c)-e;mirror=2*center-value(4)
    assert mirror==cert['missing_mirror_value'] and mirror not in a[:23]
    # Only the actual old F3 at this one source center is examined.
    triples=[list(xs) for xs in combinations(range(1,c),3) if sum(value(x) for x in xs)==3*center]
    assert triples==cert['F3_rank_triples']==[]

    old=a[:23];future=a[25:50];H=value(c)-1
    assert cert['old_values']==old and cert['future_values']==future and cert['H_c']==H
    assert len(cert['nodes'])==23*25
    nodes=[];seen=set();lower_total=0;edgecount=0
    for node in cert['nodes']:
        z,q=node['z'],node['q']
        assert type(z) is int and type(q) is int
        assert 1<=z<=23 and 1<=q<=25 and (z,q) not in seen
        seen.add((z,q));left=set();right=set();weight=0
        for pair in node['matching']:
            assert type(pair) is list and len(pair)==2
            w,j=pair;assert type(w) is int and type(j) is int
            assert 1<=w<z and 1<=j<q and w not in left and j not in right
            left.add(w);right.add(j)
            g0=old[z-1]-old[w-1];t0=future[q-1]-future[j-1]
            assert g0>0 and t0>0 and g0+t0<=H, ('Infeasible auxiliary edge',z,q,w,j)
            weight+=g0*t0;edgecount+=1
        assert type(node['value']) is int and weight==node['value']
        lower_total+=weight
        nodes.append({'z':z,'q':q,'matching_edges':len(node['matching']),'certified_feasible_weight':weight})
    assert seen=={(z,q) for z in range(1,24) for q in range(1,26)}
    U=sum(y-x for x,y in combinations(old,2));G=sum(value(c)-x for x in old);UG=U*G
    assert U==cert['U'] and G==cert['G'] and UG==cert['UG']
    assert lower_total==cert['Phi_H_feasible_lower'] and lower_total>UG
    assert lower_total-UG==cert['positive_margin']
    assert Q(lower_total,UG)==Q(cert['ratio_exact'])

    alpha=lambda n:Q(1,n*n*(n-1)**2)
    lam=(alpha(50)-alpha(51))/(value(50)-1)**2
    u42=sum(((alpha(j)-alpha(j+1))/(value(j)-1)**2 for j in range(42,51)),Q(0))
    price=d*e*u42
    assert Q(cert['lambda50_exact'])==lam==Q(history['u_M_exact'])
    assert Q(cert['selected_record_original_u42_exact'])==u42
    assert Q(cert['selected_record_full_price_exact'])==price
    assert Q(cert['selected_record_component50_exact'])==d*e*lam
    assert history['alpha_M_plus_1_preserved'] is True
    assert cert['selected_record_original_cut_interval']==[25,39]
    expected_profile={str(cut):price for cut in range(25,40)}
    assert {key:Q(value) for key,value in history['profile_exact'].items()}==expected_profile
    blocks=[]
    for block in history['blocks']:
        j=block['j'];start=2**j;end=min(2**(j+1),M)
        W=sum((Q(1,cut) for cut in range(start,end)),Q(0))
        cov=sum((Q(1,cut) for cut in range(max(25,start),min(40,end))),Q(0))
        assert Q(block['W_exact'])==W and Q(block['I_exact'])==price*cov
        blocks.append({'j':j,'original_record_harmonic_coverage':str(cov),'I_exact':str(price*cov)})
    assert all(sha(HERE/name)==h for name,h in sources.items()) and sha(CP)==cert_hash
    return {'date':'2026-09-09','attempt':'A72','status':'PASS_INDEPENDENT_FIXED_CAP_SOURCE_ALLOWANCE_COUNTEREXAMPLE',
      'scope':{'C_exact':str(C),'m0':m0,'M':M,'T':T,'c':c,'b':b,'k':k,'new_histories':0,'new_core_enumerations':0},
      'construction_formula_reproduced':True,'perturbation_42':perturb[41],'perturbation_42_one_bits':exceptional_bits,
      'positive_differences_unique':1225,'repeated_two_sums_unique':1275,'all_49_intermediate_caps_checked':cap,
      'simple_cap_check':{'H50':value(50)-1,'four_C':4*C,'H50_strictly_below_four_C':True,'log4_strictly_above_one':True},
      'preserved_relation_ranks':{'left':[24,8,40],'right':[4,20,42]},'selected_record':row,
      'strict_original_margin_intervals':{key:list(map(str,val)) for key,val in strict.items()},
      'residual_margin_intervals':{key:list(map(str,val)) for key,val in flags.items()},
      'old_quad_gaps':gaps,'delay_product':delay,'mirror_absent':True,'missing_mirror_value':mirror,
      'actual_F3_rank_triples':triples,'certified_nodes':575,'certified_auxiliary_matching_edges':edgecount,
      'nodes':nodes,'certified_Phi_H_lower_bound':lower_total,'U':U,'G':G,'UG':UG,
      'strict_lower_bound_minus_UG':lower_total-UG,'lower_bound_over_UG':str(Q(lower_total,UG)),
      'matching_maximality_proved_or_required':False,
      'lambda50_exact':str(lam),'terminal_alpha51_exact':str(alpha(51)),
      'original_u42_exact':str(u42),'original_record_full_price_exact':str(price),
      'original_component50_record_price_exact':str(d*e*lam),'once_per_record_blocks':blocks,
      'full_core_completeness_evidence':{'path':str(ip),'sha256':sha(ip),'status':prior['status'],'core_records':prior['core_records'],'method':'Reuse saved source-bound output-centric independent checker; no full scan rerun.'},
      'profile_scope':'Every saved exact profile coefficient and dyadic I is independently recovered from the one complete saved record and the genuine u42. N square roots are not certified here.',
      'unknown_comparisons':0,'source_sha256':{p.name:sha(p) for p in [Path(__file__),CP,hp,rp,ip,HERE/'independent_checker.py']},
      'scope_limits':['The universal coefficient-one Phi_H<=UG allowance comparison fails at this fixed C=2^67; this does not refute a C=1-only variant.',
        'Auxiliary matchings supply a lower bound on an upper allowance, not actual physical mass or hypothetical record prices.',
        'The one actual strict record passes the displayed residual conditions, not unspecified eventual or initial-range exclusions.',
        'No unbounded family, full core norm failure, or Q1 counterexample.','No reference run or source/evidence rewrite.']}

if __name__=='__main__':
    result=verify()
    OUT.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ['status','positive_differences_unique','repeated_two_sums_unique',
      'certified_nodes','certified_Phi_H_lower_bound','UG','strict_lower_bound_minus_UG','selected_record',
      'mirror_absent','actual_F3_rank_triples','unknown_comparisons']},indent=2))
