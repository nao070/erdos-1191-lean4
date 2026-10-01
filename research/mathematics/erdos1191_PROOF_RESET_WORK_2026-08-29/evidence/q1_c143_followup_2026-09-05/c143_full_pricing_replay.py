#!/usr/bin/env python3
"""Independent exact C143 replay, with integer-only bounded digit matrix products.
No optimization solver, floating-point comparisons or package mutations are used.
"""
import argparse, collections, functools, hashlib, importlib.util, json, math, sys, time, traceback
from fractions import Fraction as F
from pathlib import Path
import numpy as np
sys.set_int_max_str_digits(0)
BASE=1<<20
SRC=Path('/Users/USER/Downloads/C143_S32_S41_FULLROOT_EXACT_PHASE_2026-09-04_V2')
BANK=SRC/'runs/pilot_s32_n16_r1/C143_BANK.json'
def ft(x):
 x=F(x);return f'{x.numerator}/{x.denominator}'
def pf(x):
 y=F(x);assert ft(y)==x;return y
def aff(x):return tuple(pf(x[k]) for k in ('intercept','slope'))
def av(x,t):return x[0]+x[1]*t
def sha(x):return hashlib.sha256(x).hexdigest()
def canon(x):return sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def scaled(v):
 den=math.lcm(*(x.denominator for x in v));return den,[x.numerator*(den//x.denominator) for x in v]
def exact_weighted_cross(P,S,weights):
 """Return sum_g weights[g] P[g,i] S[g,j], exactly as Python ints.
 Signed digits each have abs <2^20; below bound certifies every int64
 multiply and accumulated matrix entry stays strictly below 2^63.
 """
 n,m=S.shape; assert P.shape==S.shape and len(weights)==n
 bound=n*(BASE-1)*int(np.max(np.abs(P),initial=0))*int(np.max(np.abs(S),initial=0))
 assert bound < (1<<62), ('int64 bound',bound)
 out=np.zeros((m,m),dtype=object);remain=list(weights);power=1
 while any(remain):
  digit=[(abs(v)%BASE)*(1 if v>=0 else -1) for v in remain]
  remain=[(abs(v)//BASE)*(1 if v>=0 else -1) for v in remain]
  mat=(P.T*np.array(digit,dtype=np.int64))@S
  out += mat.astype(object)*power
  power*=BASE
 return out

def root_coeffs(C,ii,jj):
 d=np.diag(C);return (d[ii]+d[jj]-C[ii,jj]-C[jj,ii]).tolist()

class Model:
 def __init__(self,b):
  self.n=b['n'];self.w=pf(b['new_weight']);self.points=b['points'];n=self.n
  self.ch=[(r,m,self.points[r]) for m in (1,2,4,8) for r in range(n-1,4*n)]
  self.m=len(self.ch);self.owners=[(e,m) for m in (1,2,4,8) for e in (n,2*n)]
  idx={(r,m):i for i,(r,m,o) in enumerate(self.ch)}
  self.direct=[[idx[(r,m)] for r in range(n-1,2*n)] if e==n else [idx[(r,m)] for r in range(2*n-1,4*n)] for e,m in self.owners]
  self.group=[([i for i,(r,m,o) in enumerate(self.ch) if r==n-1])]+[[idx[(r,m)] for r in range(n,2*n)] if e==n else [idx[(r,m)] for r in range(2*n,4*n)] for e,m in self.owners]
  self.which=[None]*self.m
  for g,inds in enumerate(self.group):
   for i in inds:assert self.which[i] is None;self.which[i]=g
  assert None not in self.which
  self.lines=sorted({(o,s*m) for r,m,o in self.ch for s in (0,1,2)})
  H=self.points[4*n-1]-self.points[2*n-1];lo,hi=F(H,16),F(H,8);br={lo,hi}
  for i,(a,b) in enumerate(self.lines):
   for aa,bb in self.lines[i+1:]:
    if b!=bb:
     t=F(aa-a,b-bb)
     if lo<t<hi:br.add(t)
  self.br=sorted(br);self.ii,self.jj=np.triu_indices(self.m,1)
 @functools.lru_cache(maxsize=50000)
 def demands(self,st):
  ds=[]
  for oi,(e,m) in enumerate(self.owners):
   q=[st[i] for i in self.direct[oi]];nz=[(a,q[a]-q[a+1]) for a in range(e) if q[a]!=q[a+1]]
   num=sum(-2*(c-a)**2*va*vc for z,(a,va) in enumerate(nz) for c,vc in nz[z+1:] if c-a>1)
   ds.append(F(m*num,1024*e*e)*(1 if e==self.n else self.w))
  return tuple(ds)
 def geometry(self,L,R=None):
  t=L if R is None else (L+R)/2;tn,td=t.numerator,t.denominator
  ordered=sorted(self.lines,key=lambda x:(x[0]*td+x[1]*tn,x))
  if R is None:
   ordered=sorted({a*td+b*tn for a,b in ordered})
   pairs=[(a,0,aa,0) for a,aa in zip(ordered,ordered[1:])]
  else:pairs=[(a,b,aa,bb) for (a,b),(aa,bb) in zip(ordered,ordered[1:])]
  cells=[];D=[F(0),F(0)]
  for a,b,aa,bb in pairs:
   # Interior x=(a+aa+(b+bb)t)/2; endpoint a,aa are scaled integers.
   xn=a+aa if R is None else (a+aa)*td+(b+bb)*tn
   st=tuple((8//m)*((0<=xn-2*o*td<2*m*tn)-(2*m*tn<=xn-2*o*td<4*m*tn)) for r,m,o in self.ch)
   wi,ws=(F(aa-a,td),0) if R is None else (aa-a,bb-b)
   ds=self.demands(st);rhs=(F(0),)+tuple(max(F(0),d) for d in ds)
   de=sum(ds,F(0));D[0]+=wi*de;D[1]+=ws*de
   cells.append((wi,ws,st,rhs))
  return cells,tuple(D)
 def all_objective(self,cells):
  S=np.array([c[2] for c in cells],dtype=np.int64);out=[]
  for k in (0,1):
   den,weights=scaled([F(c[k]) for c in cells]);C=exact_weighted_cross(S,S,weights)
   out.append((den,root_coeffs(C,self.ii,self.jj)))
  return out
 def fullprice(self,cells,sel,ys,obj,L,R):
  S=np.array([cells[g//9][2] for g in sel],dtype=np.int64)
  P=np.zeros_like(S)
  for z,g in enumerate(sel):P[z,self.group[g%9]]=S[z,self.group[g%9]]
  nums=[];dens=[]
  for k in (0,1):
   yd,yw=scaled([y[k] for y in ys]);C=exact_weighted_cross(P,S,yw);dual=root_coeffs(C,self.ii,self.jj)
   od,on=obj[k];dens.append(od*yd);nums.append([o*yd-d*od for o,d in zip(on,dual)])
  mins=[]
  for t in (L,) if L==R else (L,R):
   vals=[a*dens[1]*t.denominator+c*dens[0]*t.numerator for a,c in zip(*nums)]
   mn=min(vals);assert mn>=0,('negative all-root reduced cost',ft(t),mn)
   mins.append(mn)
  return len(self.ii)*len(mins)
 def verify_basis(self,cells,D,B,L,R):
  support=B['support'];roots=[(i,j) for i,j,w in support];assert len(set(roots))==len(roots)
  assert all(type(i) is int and type(j) is int and 0<=i<j<self.m for i,j in roots)
  ws=[pf(w) for i,j,w in support];assert all(w>0 for w in ws)
  xd,xw=scaled(ws);sel=B['selected_gate_indices'];ys=[aff(y) for y in B['dual_affines']]
  assert len(sel)==len(ys)==len(set(sel)) and all(type(g) is int and 0<=g<9*len(cells) for g in sel)
  assert all(av(y,L)>=0 and av(y,R)>=0 for y in ys)
  pobj=[F(0),F(0)];mins=[]
  for wi,ww,st,rhs in cells:
   shares=[0]*9;energy=0
   for (i,j),w in zip(roots,xw):
    z=w*(st[i]-st[j]);energy+=z*(st[i]-st[j]);shares[self.which[i]]+=z*st[i];shares[self.which[j]]-=z*st[j]
   for lhs,r in zip(shares,rhs):
    assert lhs*r.denominator>=r.numerator*xd,('primal gate',lhs,xd,ft(r));mins.append(F(lhs,xd)-r)
   pobj[0]+=wi*energy/xd if isinstance(wi,F) else F(wi*energy,xd)
   pobj[1]+=F(ww*energy,xd)
  dobj=tuple(sum((cells[g//9][3][g%9]*y[k] for g,y in zip(sel,ys)),F(0)) for k in (0,1))
  assert tuple(pobj)==dobj==aff(B['primal_objective'])==aff(B['dual_objective'])
  assert min(mins)==pf(B['minimum_primal_slack'])
  assert B['exact_primal_feasible'] is True and B['exact_primal_dual_equal'] is True
  return tuple(pobj),sel,ys

def audit_primary(b):
 run=BANK.parent;sm=json.loads((run/'SOURCE_SHA256.json').read_text())
 assert all(sha((SRC/r).read_bytes())==h for r,h in sm.items())
 pm=json.loads((SRC/'C143_PACKAGE_SHA256SUMS.json').read_text())['files'];assert all(sha((SRC/r).read_bytes())==h for r,h in pm.items())
 assert json.loads((run/'RUN_CONFIG.json').read_text())==b['run_meta']['run_config']
 assert canon(sm)==b['run_meta']['run_config']['config']['source_manifest_sha256']
 counts={}
 for d,k,bk,ik in [('checkpoint','certified_child','children','child_id'),('checkpoint_endpoints','geometry_endpoint','geometry_endpoints','endpoint_id')]:
  assert json.loads((run/d/'state.json').read_text())=={'pending':[]}
  rows=[json.loads(x) for x in (run/d/'results.jsonl').read_text().splitlines()];a={x[k][ik]:x[k] for x in rows};bb={x[ik]:x for x in b[bk]}
  assert len(a)==len(rows)==len(bb) and a==bb
  counts[d]=dict(collections.Counter(x['status'] for x in rows))
 return {'package_hashes_verified':len(pm),'saved_source_hashes_verified':len(sm),'checkpoint_status_counts':counts,'saved_oracle_files_present':[x.name for x in run.glob('*') if any(s in x.name for s in ('ORACLE','SUMMARY','PASS'))]}

def coverage(b,m):
 ps=b['geometry_parents'];cs=b['children'];es=b['geometry_endpoints'];assert len(m.br)==b['phase_breakpoint_count']==len(ps)+1==len(es)
 for i,p in enumerate(ps):
  assert p['index']==i and p['parent_id']==f"{b['case_id']}/g{i:06d}" and (pf(p['left']),pf(p['right']))==tuple(m.br[i:i+2])
  assert p['endpoint_hash']==sha((p['left']+'|'+p['right']).encode())
 by=collections.defaultdict(list)
 assert len({c['child_id'] for c in cs})==len(cs)
 for c in cs:by[c['parent_id']].append(c)
 assert set(by)=={p['parent_id'] for p in ps}
 for p in ps:
  cur=pf(p['left'])
  for c in sorted(by[p['parent_id']],key=lambda c:pf(c['left'])):
   L,R,S=map(pf,[c['left'],c['right'],c['sample']]);assert cur==L<R<=pf(p['right']) and L<=S<=R;cur=R
  assert cur==pf(p['right'])
 for i,(e,t) in enumerate(zip(es,m.br)):
  assert e['endpoint_id']==f"{b['case_id']}/e{i:06d}" and e['endpoint_index']==i and pf(e['phase'])==t and e['status']=='FULLROOT_ENDPOINT_CERTIFIED'
 ir=b['integral']['records'];assert len(ir)==len(cs) and len({r['child_id'] for r in ir})==len(ir)
 irm={r['child_id']:r for r in ir}
 assert set(irm)=={c['child_id'] for c in cs}
 for c in cs:assert all(irm[c['child_id']][k]==c[k] for k in ('left','right'))
 return by,irm

def logbound(q,n):
 assert q>=1 and n>=1;z=(q-1)/(q+1);lo=sum((2*z**(2*k+1)/F(2*k+1) for k in range(n)),F(0));return lo,lo+2*z**(2*n+1)/(F(2*n+1)*(1-z*z))

def run(a):
 start=time.monotonic();raw=BANK.read_bytes();b=json.loads(raw);assert b['schema']=='erdos1191.c143.parametric_fullroot_phase_bank.v3'
 assert canon({k:v for k,v in b.items() if k!='integrity'})==b['integrity']['canonical_payload_sha256']
 for k in ('C058_proved','Q1_resolved','Q2_resolved','uniform_over_all_C116_histories','history_independent_eta_proved','single_phase_global_witness_proved','nonanticipating_global_ledger_proved'):assert b['scope'][k] is False
 target=[x for x in json.loads((SRC/'source_run/TARGET_FIXTURES_FROM_OVERNIGHT.json').read_text()) if x['task_id']==b['case_id']];assert len(target)==1;tr=target[0]
 assert tr['points']==b['points'] and tr['n']==b['n'] and F(tr['new_weight'])==pf(b['new_weight'])
 assert tr['history_sha256']==b['history_sha256']==sha(json.dumps(b['points'],separators=(',',':')).encode())
 out={'started_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'bank':str(BANK),'bank_bytes':len(raw),'bank_sha256':sha(raw),'python':sys.version,'numpy':np.__version__,'mode':a.mode,'argv':sys.argv,'primary':audit_primary(b)}
 print('PRIMARY_AUDIT_OK',json.dumps(out['primary']),flush=True)
 m=Model(b);by,irm=coverage(b,m);total=[F(0),F(0)];children=ends=full=0;minmargin=None;lastmargin=None
 for pi,p in enumerate(b['geometry_parents']):
  if a.limit and pi>=a.limit:break
  lastmargin=None
  cells,D=m.geometry(pf(p['left']),pf(p['right']));obj=m.all_objective(cells) if a.mode=='full' else None
  for c in by[p['parent_id']]:
   L,R=pf(c['left']),pf(c['right']);pobj,sel,ys=m.verify_basis(cells,D,c['basis'],L,R);margin=tuple(2*d-v for d,v in zip(D,pobj));assert margin==aff(c['margin_affine'])
   vals=[av(margin,t) for t in (L,R)];assert min(vals)>0;minmargin=min(vals) if minmargin is None else min(minmargin,*vals)
   if lastmargin is not None:assert lastmargin==vals[0]
   lastmargin=vals[1]
   if a.mode=='full':full+=m.fullprice(cells,sel,ys,obj,L,R)
   ir=irm[c['child_id']];beta,alpha=margin;rat=beta*(1/L-1/R)
   if alpha:
    ll,lu=logbound(R/L,ir['log_terms']);lo,hi=(rat+alpha*ll,rat+alpha*lu) if alpha>0 else (rat+alpha*lu,rat+alpha*ll)
   else:lo=hi=rat
   assert (lo,hi)==(pf(ir['lower']),pf(ir['upper']));total[0]+=lo;total[1]+=hi;children+=1
  for ei in ([pi] if pi+1<len(b['geometry_parents']) else [pi,pi+1]):
   ep=b['geometry_endpoints'][ei];t=pf(ep['phase']);ec,eD=m.geometry(t);pobj,sel,ys=m.verify_basis(ec,eD,ep['basis'],t,t)
   assert pobj[1]==0 and pf(ep['D_exact'])==eD[0] and pf(ep['margin'])==2*eD[0]-pobj[0]>0
   if a.mode=='full':full+=m.fullprice(ec,sel,ys,m.all_objective(ec),t,t)
   ends+=1
  if pi%10==0 or pi+1==len(b['geometry_parents']):print('PROGRESS',json.dumps({'parents':pi+1,'children':children,'endpoints':ends,'all_root_checks':full,'elapsed_seconds':round(time.monotonic()-start,3)}),flush=True)
 if not a.limit:
  assert tuple(total)==(pf(b['integral']['lower']),pf(b['integral']['upper'])) and total[0]>0
  assert children==len(b['children']) and ends==len(b['geometry_endpoints'])
 out.update(status=('PARTIAL_' if a.limit else '')+('C143_INDEPENDENT_EXACT_FULL_PRICING_OK' if a.mode=='full' else 'C143_INDEPENDENT_EXACT_PRIMAL_AND_MARGIN_OK'),children_checked=children,endpoints_checked=ends,full_root_endpoint_checks=full,min_pointwise_child_margin=ft(minmargin),aggregate_lower=ft(total[0]),aggregate_upper=ft(total[1]),elapsed_seconds=time.monotonic()-start,exit_code=0,scope=b['scope'])
 Path(a.output).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n');print('RESULT',json.dumps({k:v for k,v in out.items() if k not in ('aggregate_lower','aggregate_upper','primary')}),flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['primal','full'],default='full');ap.add_argument('--limit',type=int);ap.add_argument('--output',required=True);a=ap.parse_args()
 try:run(a)
 except Exception:
  traceback.print_exc();Path(a.output).write_text(json.dumps({'status':'FAILED','exit_code':1,'argv':sys.argv,'traceback':traceback.format_exc()},indent=2)+'\n');sys.exit(1)
