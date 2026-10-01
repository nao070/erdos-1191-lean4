#!/usr/bin/env python3
"""Exact BH gap-kernel check on the already-certified A14 M12 only."""
from fractions import Fraction as F
from pathlib import Path
import hashlib, json
from independent_checker import rank_conditions, output_condition

HERE=Path(__file__).resolve().parent
TARGET=HERE/'C1000000_m02_M12_target'
canonical=TARGET/'C1000000_m02_M12_target.json'
records_path=TARGET/'C1000000_m02_M12_target_records.json'
certificate_path=TARGET/'C1000000_m02_M12_target_independent_check.json'
data=json.loads(canonical.read_text())
rows=json.loads(records_path.read_text())['records']
cert=json.loads(certificate_path.read_text())
assert cert['status']=='PASS'
assert hashlib.sha256(canonical.read_bytes()).hexdigest()==cert['input_sha256']
assert hashlib.sha256((HERE/'independent_checker.py').read_bytes()).hexdigest()==cert['checker_sha256']
a=data['a']; M=len(a)
assert data['C_exact']=='1000000' and data['m0']==2 and M==data['T']==12
assert len(rows)==data['core_records']==2
assert rows==[[35000,30000,6,8,1,3,8,3,11,12,5000],
             [37000,32000,3,8,1,6,8,6,11,12,5000]]
for d,e,pd,qd,pe,qe,c,s,i,r,t in rows:
    assert a[qd-1]-a[pd-1]==d and a[qe-1]-a[pe-1]==e
    assert d-e==t==a[r-1]-a[i-1]
    assert len({pd,qd,pe,qe,i,r})==6
    assert rank_conditions(c,s,i,r) and output_condition(c,t)
p,q,s,c=1,3,6,8
i,r=11,12
A=a[q-1]-a[p-1];B=a[s-1]-a[q-1];Cgap=a[c-1]-a[s-1]
Hquad=a[c-1]-a[p-1]
u=sum((F(1,k*k*(k-1)**2)-F(1,k*k*(k+1)**2))/(a[k-1]-a[0])**2
      for k in range(r,M+1))
assert str(u)==data['u_M_exact']=='1/676350675000000'
# The type-1 record contributes AC only; type-2 contributes AC+BH.
# There is no plus record in this complete certified core bank.
assert rows[0][0]*rows[0][1]==A*Cgap
assert rows[1][0]*rows[1][1]==A*Cgap+B*Hquad
g=[a[l]-a[l-1] for l in range(1,M)]
x=[int(q<=l<s) for l in range(1,M)]
y=[int(p<=l<c) for l in range(1,M)]
assert sum(g[l]*x[l] for l in range(M-1))==B
assert sum(g[l]*y[l] for l in range(M-1))==Hquad
K=[[u*F(x[l]*y[m]+y[l]*x[m],2) for m in range(M-1)] for l in range(M-1)]
z=[F(0)]*(M-1);z[0]=2;z[2]=-1
def quad(v):
    return sum((v[l]*K[l][m]*v[m] for l in range(M-1) for m in range(M-1)),F(0))
actual=quad(g);negative=quad(z)
assert K[0][0]==0 and K[0][2]==u/2 and K[2][2]==u
assert K[0][2]**2>K[0][0]*K[2][2]
assert K[0][0]*K[2][2]-K[0][2]**2==-u*u/4
assert negative==-u<0
assert actual==B*Hquad*u==F(134,676350675)>0
assert actual+2*A*Cgap*u==F(data['profile_exact']['9'])==F(data['profile_exact']['10'])
assert all(gap>0 for gap in g) and all(entry>=0 for row in K for entry in row)
result={
 'status':'CERTIFIED_PSD_AND_ENTRYWISE_SCHWARZ_COUNTEREXAMPLE',
 'C_exact':data['C_exact'],'m0':data['m0'],'M':M,'T':data['T'],
 'a':a,'core_records':rows,'old_quad_ranks':[p,q,s,c],
 'g_actual':g,'x_indicator':x,'y_indicator':y,'g_indexing':'1..M-1',
 'cut_interval':[9,10],'w_genuine_exact':str(u),
 'why_w_is_one_price':'Only the type-2 minus record contributes BH; the other record contributes AC. No plus record is present.',
 'K_exact':[[str(v) for v in row] for row in K],
 'K_11_exact':str(K[0][0]),'K_13_exact':str(K[0][2]),'K_33_exact':str(K[2][2]),
 'principal_1_3_determinant_exact':str(-u*u/4),
 'negative_test_vector':list(map(str,z)),
 'z_T_K_z_exact':str(negative),
 'g_dot_x_exact':B,'g_dot_y_exact':Hquad,
 'actual_g_T_K_g_exact':str(actual),'actual_Q_BH_exact':str(B*Hquad*u),
 'entrywise_kernel_nonnegative':True,'actual_gap_vector_strictly_positive':True,
 'squared_Schwarz_lhs_exact':str(K[0][2]**2),'squared_Schwarz_rhs_exact':'0',
 'alpha_M_plus_1_preserved':True,'unknown_comparisons':0,
 'scope':'One certified existing actual fixed-cap history refutes universal PSD or diagonal-Schwarz claims for the specified symmetrized BH gap kernel. The actual positive gap vector has positive quadratic form. No uniform norm, Q1 or copositivity claim is refuted.',
 'source_sha256':{str(path.relative_to(HERE)):hashlib.sha256(path.read_bytes()).hexdigest()
                  for path in [canonical,records_path,certificate_path,HERE/'independent_checker.py',Path(__file__)]},
 'frozen_source_sha256':data['source_sha256']}
(TARGET/'BH_symmetric_gap_kernel_exact.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({key:result[key] for key in ['status','g_actual','K_11_exact','K_13_exact','K_33_exact',
      'z_T_K_z_exact','actual_g_T_K_g_exact','actual_Q_BH_exact']},indent=2))
