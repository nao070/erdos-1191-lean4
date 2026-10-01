#!/usr/bin/env python3
"""One saved A53/A54 witness only: A55 full-price short output delay."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib,json
from reference_evaluator import log_bounds,rank_core,physical_core
from independent_checker import log_fixed,SCALE,rank_conditions,output_condition

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
wp=HERE/'A53_EXISTING_RESTART_WITNESS_EXACT.json'
wdata=json.loads(wp.read_text()); w=wdata['witness']
sp=HERE/wdata['input']; data=json.loads(sp.read_text())
assert sha(sp)==wdata['source_sha256'][sp.name]
cp=HERE/'C1_m02_dense_variant1_M96_independent_check.json'
cert=json.loads(cp.read_text())
assert cert['status']=='PASS' and cert['input_sha256']==sha(sp)
assert data['C_exact']=='1' and data['m0']==2 and data['M']==data['T']==96
a=[None]+data['a']; row=w['record']
assert row==[215,174,14,19,21,24,24,19,27,28,41]
d,e,x,y,ww,z,c,s,i,r,t=row
b,k,M,T=w['b'],w['k'],96,96
assert (c,r,b,k)==(24,28,25,48)
assert len({x,y,ww,z,i,r})==6 and c<b<i<r<=k<=T<=M
assert d==a[y]-a[x] and e==a[z]-a[ww] and t==a[r]-a[i]==d-e
assert rank_core(c,s,i,r) is True and physical_core(c,t) is True
assert rank_conditions(c,s,i,r) and output_condition(c,t)
# Reverse recovery checks only the three labels in this one saved record.
value_rank={v:j for j,v in enumerate(data['a'],1)}
recovery={}
for label,pair in [(d,[x,y]),(e,[ww,z]),(t,[i,r])]:
 found=[[j,value_rank[a[j]+label]] for j in range(1,97) if a[j]+label in value_rank]
 assert found==[pair]; recovery[str(label)]=pair

def floor_three_quarter(n):
 lo,hi=log_bounds(n)
 il,iu=log_fixed(n); ilo,ihi=Q(il,SCALE),Q(iu,SCALE)
 def certify(left,right):
  valid=[j for j in range(n+1) if j**4*right**3<=n**4<(j+1)**4*left**3]
  if len(valid)!=1:raise ArithmeticError('UNKNOWN integer floor')
  j=valid[0]
  return j,{'lower_floor_margin_exact':str(n**4-j**4*right**3),
    'upper_floor_margin_exact':str((j+1)**4*left**3-n**4)}
 j,proof=certify(lo,hi); jj,ip=certify(ilo,ihi); assert j==jj
 return {'n':n,'q_exact':'3/4','floor_n_over_log_q_n':j,
  'reference_log_interval':list(map(str,(lo,hi))),
  'independent_log_interval':list(map(str,(ilo,ihi))),
  'statement':'R^4*(log n)^3 <= n^4 < (R+1)^4*(log n)^3',
  'reference_power_proof':proof,'independent_power_proof':ip}
birth=floor_three_quarter(c); cut=floor_three_quarter(b)
R=birth['floor_n_over_log_q_n']; L=cut['floor_n_over_log_q_n']
assert r-c<=R and k-b>L
# These are original genuine tails, independently read back via alpha differences.
def alpha(j):return Q(1,j*j*(j-1)**2)
lam=Q(4,k*(k*k-1)**2*(a[k]-a[1])**2)
u=sum(((alpha(j)-alpha(j+1))/(a[j]-a[1])**2 for j in range(r,M+1)),Q(0))
assert u==Q(w['original_u_r_96_exact']) and lam==Q(w['lambda48_exact'])
coverage=sum((Q(1,j) for j in range(c+1,i)),Q(0))
assert coverage<=Q(r-c,c)
out={'date':'2026-09-09','attempt':'A55_SAVED_WITNESS','status':'PASS_ONE_RECORD_DUAL_EXACT_CHECK',
 'input':sp.name,'C_exact':'1','m0':2,'M':M,'T':T,'record':row,'original_bank_index':w['original_bank_index'],
 'birth_c':c,'output_r':r,'cut_b':b,'component_k':k,'output_delay':r-c,'component_cut_delay':k-b,
 'birth_delay_threshold':birth,'A43_cut_short_threshold':cut,
 'A55_full_original_record_paid':True,'A43_cut_short_does_not_pay_component48_at_cut25':True,
 'six_distinct_endpoints':True,'original_strict_reference_check':True,'original_strict_independent_check':True,
 'source_values':[a[j] for j in [x,y,ww,z]],'output_values':[a[i],a[r]],
 'unique_endpoint_recovery':recovery,'de':d*e,
 'original_cut_interval_inclusive':[c+1,i-1],'harmonic_coverage_exact':str(coverage),
 'harmonic_coverage_delay_upper_exact':str(Q(r-c,c)),
 'original_u28_96_exact':str(u),'original_full_record_price_exact':str(d*e*u),
 'lambda48_exact':str(lam),'component48_record_mass_exact':str(lam*d*e),'alpha97_exact':str(alpha(M+1)),
 'price_scope':'A55 membership depends only on c and r: this entire original physical record is paid, including every original component28..96 and both covered cuts25,26. No output rank, component denominator or alpha97 is reset. Its full price is distinct from lambda48.',
 'scope':'One already saved witness only. Reuses certified C1,m02 M96; no new history, source/bin, profile evaluation, record-pool scan or additional witness search.',
 'unknown_comparisons':[],
 'source_sha256':{p.name:sha(p) for p in (wp,sp,cp,HERE/'A54_EXISTING_WITNESS_FLAG_EXACT.json',HERE/'reference_evaluator.py',HERE/'independent_checker.py',Path(__file__))}}
(HERE/'A55_SAVED_WITNESS_EXACT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'R24':R,'A43_L25':L,'r_minus_c':r-c,'k_minus_b':k-b,'de':d*e,'coverage':str(coverage),'lambda48':str(lam),'unknown':0},indent=2))
