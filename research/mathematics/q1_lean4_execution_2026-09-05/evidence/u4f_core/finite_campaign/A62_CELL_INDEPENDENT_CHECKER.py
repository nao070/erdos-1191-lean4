#!/usr/bin/env python3
"""Independent actual endpoint reconstruction only at b25,k48,c23/24."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict,Counter
from functools import lru_cache
import hashlib,json
from independent_checker import log_fixed,SCALE,decide,rank_conditions,output_condition
HERE=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rp=HERE/'A62_CELL_EXACT.json';ref=json.loads(rp.read_text());sp=HERE/ref['input'];data=json.loads(sp.read_text())
assert sha(sp)==ref['source_sha256'][sp.name]
assert data['C_exact']=='1' and data['m0']==2 and data['M']==data['T']==96
a=[None]+data['a'];b,k,M,T=25,48,96,96;births=(23,24);unknown=[]
oldmaps={}
for c in births:
 mp={}
 for u in range(1,c):
  for v in range(u+1,c):
   d=a[v]-a[u];assert d not in mp;mp[d]=(u,v)
 oldmaps[c]=mp
# Enumerate only prescribed future pairs and fresh x, then recover the old partner.
# This does not depend on the saved record-pool candidate list.
raw=set();lookups=0
for c in births:
 for fresh in range(1,c):
  h=a[c]-a[fresh]
  for i in range(b+1,k):
   for r in range(i+1,k+1):
    t=a[r]-a[i]
    for sigma,g in [(1,h-t),(-1,h+t)]:
     lookups+=1
     pair=oldmaps[c].get(g)
     if pair is None:continue
     u,v=pair
     if len({fresh,c,u,v,i,r})!=6:continue
     if sigma==1:row=(h,g,fresh,c,u,v,c,v,i,r,t)
     else:row=(g,h,u,v,fresh,c,c,v,i,r,t)
     try:good=rank_conditions(c,v,i,r) and output_condition(c,t)
     except ArithmeticError:
      unknown.append({'kind':'original_strict','record':row});continue
     if good:raw.add(row)
expected={tuple(x['record']):x for x in ref['original_prescribed_rows']}
assert raw==set(expected),'Prescribed original-core pool mismatch'

@lru_cache(None)
def logs(n):
 lo,hi=log_fixed(n);return Q(lo,SCALE),Q(hi,SCALE)
def classify(row):
 d,e,x,y,w,z,c,s,i,r,t=row
 lo,hi=logs(b);cl,ch=logs(c)
 quad=sorted([x,y,w,z]);gaps=[a[v]-a[u] for u,v in zip(quad,quad[1:])]
 # Expressions independently use scaled rational log bounds; none use floats.
 vals={
 'A46_above_cut_short':((k-b)**4*lo**3,(k-b)**4*hi**3,b**4),
 'A46_below_cut_far':(lo**5,hi**5,Q((k-1)**8,b**8)),
 'A46_near_cut_span':(lo**2,hi**2,Q(a[k]-a[1],a[b]-a[1])),
 'A46_large_smaller_source':(lo**5,hi**5,Q(b**8,e**4)),
 'A46_large_output':(lo**5,hi**5,Q(b**4,t*t)),
 'A46_source_birth_support':(lo**9,hi**9,Q(b**8,16*s**8)),
 'A53_near_birth_rank':(cl**5,ch**5,Q((k-1)**8,c**8)),
 'A54_near_birth_span':(cl**2,ch**2,Q(a[k]-a[1],a[c]-a[1]))}
 for j,gap in enumerate(gaps,1):vals['A46_large_gap_'+str(j)]=(lo**5,hi**5,Q(b**4,gap*gap))
 A=(i-c)**2*min(c,r-c)
 vals['A57_reverse_delay_product']=(cl**9,ch**9,Q(c**12,A**4))
 ff={}
 for name,expr in vals.items():
  try:ff[name]=decide(*expr)
  except ArithmeticError:
   ff[name]=None;unknown.append({'kind':name,'record':row})
 if y==c:g,h,fresh,oldpair,sigma=e,d,x,[w,z],1
 else:g,h,fresh,oldpair,sigma=d,e,w,[x,y],-1
 mirrors=[j for j in range(1,c) if a[j]+a[fresh]==2*(a[c]-g)]
 assert len(mirrors)<=1
 ff['A61_no_old_mirror']=not mirrors
 return ff,(g,h,fresh,oldpair,sigma),vals
surv=[];margins={};stage_counts={str(c):{'original_core':0,'A46':0,'A53':0,'A54':0,'A57':0,'A61':0} for c in births}
for row in sorted(raw):
 ff,info,expr=classify(row);saved=expected[row]
 assert ff==saved['flags'],'selector mismatch'
 c=row[6];stage_counts[str(c)]['original_core']+=1
 alive=True
 for stage in ['A46','A53','A54','A57','A61']:
  alive=alive and all(x is True for name,x in ff.items() if name.startswith(stage+'_'))
  if alive:stage_counts[str(c)][stage]+=1
 if alive:
  g,h,fresh,oldpair,sigma=info
  assert (g,h,fresh,oldpair,sigma)==(saved['g'],saved['h'],saved['fresh_x'],saved['old_pair'],saved['sigma'])
  surv.append((row,info))
  margins[str(saved['original_bank_index'])]={name:[str(v[0]-v[2]),str(v[1]-v[2])] for name,v in expr.items()}
assert stage_counts==ref['stage_counts']
assert {row for row,info in surv}=={tuple(x['record']) for x in ref['survivors']}
# Independently check every survivor's original full tail and component coefficient.
def alpha(j):return Q(1,j*j*(j-1)**2)
@lru_cache(None)
def u(r):return sum(((alpha(j)-alpha(j+1))/(a[j]-a[1])**2 for j in range(r,M+1)),Q(0))
lam=(alpha(k)-alpha(k+1))/(a[k]-a[1])**2
assert str(lam)==ref['lambda48_exact']
for row,info in surv:
 saved=expected[row];assert Q(saved['original_u_r_96_exact'])==u(row[9])
 assert Q(saved['lambda48_mass_exact'])==row[0]*row[1]*lam
# Vertex-based connected components, independent of reference edge traversal.
groups=defaultdict(list)
for row,info in surv:groups[(row[6],info[0])].append((row,info))
checks=[];hist=Counter();through_witnesses=[]
for (c,g),edges in sorted(groups.items()):
 adj=defaultdict(list);color_in=defaultdict(list);color_out=defaultdict(list)
 for j,(row,info) in enumerate(edges):
  i,r=row[8:10];sigma=info[4]
  adj[i].append((r,j));adj[r].append((i,j));color_out[(i,sigma)].append(j);color_in[(r,sigma)].append(j)
 assert max(map(len,adj.values()))<=2
 assert all(len(v)<=1 for v in color_in.values()) and all(len(v)<=1 for v in color_out.values())
 assert len({info[2] for row,info in edges})==len(edges)
 unseen=set(adj);components=[]
 while unseen:
  todo=[min(unseen)];vertices=set()
  while todo:
   v=todo.pop()
   if v in vertices:continue
   vertices.add(v);todo.extend(w for w,j in adj[v] if w not in vertices)
  unseen-=vertices;ids=sorted({j for v in vertices for w,j in adj[v]})
  ends=sorted(v for v in vertices if len(adj[v])==1)
  cycle=not ends;assert cycle or len(ends)==2
  kind='cycle' if cycle else 'path';hist[(kind,len(ids))]+=1
  mass=sum(edges[j][0][0]*edges[j][0][1] for j in ids)
  B=sum(edges[j][1][4]*edges[j][0][10] for j in ids)
  assert mass==g*g*len(ids)+g*B
  if cycle:assert B==0
  else:assert abs(B)==abs(a[ends[1]]-a[ends[0]])
  indices=sorted(expected[edges[j][0]]['original_bank_index'] for j in ids)
  components.append({'kind':kind,'edge_count':len(ids),'vertices':sorted(vertices),'bank_indices':indices,'boundary':B,'mass':mass})
 for v in sorted(adj):
  for sigma in [-1,1]:
   if (v,sigma) in color_in and (v,sigma) in color_out:
    j1=color_in[(v,sigma)][0];j2=color_out[(v,sigma)][0]
    through_witnesses.append({'c':c,'g':g,'shared_future_vertex':v,'sigma':sigma,
       'records':[list(edges[j1][0]),list(edges[j2][0])],
       'bank_indices':[expected[edges[j1][0]]['original_bank_index'],expected[edges[j2][0]]['original_bank_index']]})
 actual=next(x for x in ref['nonempty_graph_cells'] if x['c']==c and x['g']==g)
 assert {(x['kind'],tuple(x['bank_indices']),x['boundary'],x['mass']) for x in components}=={(x['kind'],tuple(sorted(x['bank_indices'])),x['boundary_exact'],x['sum_products']) for x in actual['components']}
 checks.append({'c':c,'g':g,'edge_count':len(edges),'components':components})
assert not unknown
out={'date':'2026-09-09','attempt':'A62_PRESCRIBED_CELLS','status':'PASS_INDEPENDENT_ACTUAL_ENDPOINT_AND_INTERVAL_CHECK',
 'C_exact':'1','m0':2,'M':M,'T':T,'b':b,'k':k,'births':list(births),
 'reconstruction':'For each prescribed c and fresh endpoint x<c, enumerate only actual output pairs26<=i<r<=48; recover older g=h-t orh+t through actual old difference maps. Independent strict predicates and fixed-point rational logs; no reference evaluator imported.',
 'older_label_lookups':lookups,'stage_counts':stage_counts,
 'physical_g_domains':{str(c):{'old_label_count':len(oldmaps[c]),'nonempty_cells':sum(cc==c for cc,g in groups),'empty_g_labels':[g for g in sorted(oldmaps[c]) if (c,g) not in groups]} for c in births},
 'graph_checks':checks,'component_length_histogram':{kind+':'+str(length):count for (kind,length),count in sorted(hist.items())},
 'first_same_color_two_edge_through_path':through_witnesses[0] if through_witnesses else None,
 'same_color_through_junctions':len(through_witnesses),
 'independent_selector_margin_intervals':margins,
 'independent_log_intervals':{str(n):list(map(str,logs(n))) for n in sorted({23,24,25}|{row[9] for row,info in surv})},
 'source_sha256':{p.name:sha(p) for p in [rp,sp,HERE/'independent_checker.py',Path(__file__)]},
 'survivor_count':len(surv),'unpriced_mass':sum(row[0]*row[1] for row,info in surv),
 'genuine_component_mass_exact':str(sum(row[0]*row[1] for row,info in surv)*lam),
 'unknown_comparisons':unknown,
 'scope':'Only prescribed existing two births, one cut and one genuine component. No full profile or new history. Cycle absence is finite only. A same-color chain, if present, is an actual counterexample to matching in precisely this surviving cell; no frozen-norm conclusion.'}
(HERE/'A62_CELL_INDEPENDENT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({name:out[name] for name in ['status','older_label_lookups','survivor_count','component_length_histogram','first_same_color_two_edge_through_path','same_color_through_junctions','unpriced_mass','genuine_component_mass_exact']},indent=2))
