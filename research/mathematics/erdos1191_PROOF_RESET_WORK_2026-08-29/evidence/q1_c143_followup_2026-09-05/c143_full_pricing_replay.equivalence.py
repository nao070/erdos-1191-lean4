import importlib.util,sys,json,time,random
from pathlib import Path
from fractions import Fraction as F
p=Path(__file__).parent
sys.path.insert(0,str(p))
import c143_full_pricing_replay as a
import numpy as np
spec=importlib.util.spec_from_file_location('original',a.SRC/'oracle/c143_independent_oracle.py');o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
start=time.monotonic();b=json.loads(a.BANK.read_text());m=a.Model(b);old=o.Model(b['points'],b['n'],a.pf(b['new_weight']));checks={}
rng=random.Random(143)
for n,dim in [(1,3),(7,8),(25,13)]:
 P=np.array([[rng.randrange(-8,9) for j in range(dim)] for i in range(n)],dtype=np.int64);S=np.array([[rng.randrange(-8,9) for j in range(dim)] for i in range(n)],dtype=np.int64)
 weights=[rng.randrange(-(1<<140),1<<140) for i in range(n)]
 got=a.exact_weighted_cross(P,S,weights)
 for i in range(dim):
  for j in range(dim):assert got[i,j]==sum(weights[k]*int(P[k,i])*int(S[k,j]) for k in range(n))
checks['signed_140bit_cross_entries_against_python']=3*0+9+64+169
L,R=a.pf(b['geometry_parents'][0]['left']),a.pf(b['geometry_parents'][0]['right']);cells,D=m.geometry(L,R)
for ci in (0,1,10,50,100,200,len(cells)-1):
 wi,ws,st,rhs=cells[ci]
 ds=m.demands(st)
 for k,owner in enumerate(old.owners):assert ds[k]==old.weights[owner[0]]*old.demand(owner,st)
checks['owner_demands_against_original_dense_fraction']=56
ordered=tuple(sorted(old.lines(),key=lambda z:(z[0]+z[1]*(L+R)/2,z)))
for ci,((x,y),(xx,yy)) in enumerate(zip(ordered,ordered[1:])):
 t=(L+R)/2;assert cells[ci][2]==old.state(((x+y*t)+(xx+yy*t))/2,t)
checks['all_geometry_cell_states_against_original']=len(cells)
cc=[(F(wi),F(ws),st) for wi,ws,st,rhs in cells];gates=[(ci,tuple(m.group[k]),rhs[k]) for ci,(wi,ws,st,rhs) in enumerate(cells) for k in range(9)]
c=b['children'][0];l,r=a.pf(c['left']),a.pf(c['right']);roots,x,sel,ys,pobj=o.verify_basis_at(cc,gates,c['basis'],l,r)
newobj,newsel,newys=m.verify_basis(cells,D,c['basis'],l,r);assert pobj==newobj
checks['complete_original_fraction_primal_dual_basis_replays']=1
oc=m.all_objective(cells)
for t in (l,r):
 den,nums=o._objective_scaled_all_roots(cc,t,m.m)
 assert all(F(v,den)==F(ai,oc[0][0])+F(bi,oc[1][0])*t for v,ai,bi in zip(nums,oc[0][1],oc[1][1]))
 ok,minnum,dd,count=o._exact_full_pricing_integer(cc,gates,sel,ys,t,m.m)
 assert ok;checks['original_integer_full_root_checks']=checks.get('original_integer_full_root_checks',0)+count
assert m.fullprice(cells,newsel,newys,oc,l,r)==2*len(m.ii)
checks['all_objective_coefficients_against_original_integer']=2*len(m.ii)
res={'status':'EXACT_REPLAY_EQUIVALENCE_CHECKS_PASS','checks':checks,'elapsed_seconds':time.monotonic()-start,'scope':'Arithmetic and representative bank cross-check only; global bank replay separate.'}
(p/'c143_full_pricing_replay.equivalence.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
