#!/usr/bin/env python3
"""Specified existing cell only: b25,k48,c23/24, all named residual selectors."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter,defaultdict
from functools import lru_cache
import hashlib,json
from reference_evaluator import log_bounds,strict_positive,rank_core,physical_core

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
sp=HERE/'C1_m02_dense_variant1_M96.json';cp=HERE/'C1_m02_dense_variant1_M96_independent_check.json'
pp=HERE/'A29_forbidden_output_packing_four_cells_exact.json'
data=json.loads(sp.read_text());cert=json.loads(cp.read_text());prior=json.loads(pp.read_text())
assert cert['status']=='PASS' and cert['input_sha256']==sha(sp)
assert prior['source_sha256'][sp.name]==sha(sp)
assert sha(pp)=='8a08d2ecd2e6a1317d4d6699ad98dff971e578325211759afbae849a9c3354fb'
assert data['C_exact']=='1' and data['m0']==2 and data['M']==data['T']==96
a=[None]+data['a'];b=25;k=48;M=T=96;births=(23,24)
rank_by_value={v:j for j,v in enumerate(data['a'],1)}
cell=next(v for v in prior['cells'] if v['b']==b and v['k']==k)
original={int(j):prior['original_core_record_pool'][str(j)] for j in cell['original_core_bank_indices'] if prior['original_core_record_pool'][str(j)][6] in births}
assert all(row[6]<b<row[8]<row[9]<=k for row in original.values())
@lru_cache(None)
def log(n):return log_bounds(n)

def flags(row):
 d,e,x,y,w,z,c,s,i,r,t=row
 lo,hi=log(b);cl,ch=log(c)
 quad=sorted([x,y,w,z]);gaps=[a[j]-a[h] for h,j in zip(quad,quad[1:])]
 vals={'A46_above_cut_short':((k-b)**4*lo**3,(k-b)**4*hi**3,b**4),
  'A46_below_cut_far':(b**8*lo**5,b**8*hi**5,(k-1)**8),
  'A46_near_cut_span':((a[b]-a[1])*lo**2,(a[b]-a[1])*hi**2,a[k]-a[1]),
  'A46_large_smaller_source':(e**4*lo**5,e**4*hi**5,b**8),
  'A46_large_output':(t*t*lo**5,t*t*hi**5,b**4),
  'A46_source_birth_support':(16*s**8*lo**9,16*s**8*hi**9,b**8),
  'A53_near_birth_rank':(c**8*cl**5,c**8*ch**5,(k-1)**8),
  'A54_near_birth_span':((a[c]-a[1])*cl**2,(a[c]-a[1])*ch**2,a[k]-a[1])}
 for j,gap in enumerate(gaps,1):vals['A46_large_gap_'+str(j)]=(gap*gap*lo**5,gap*gap*hi**5,b**4)
 delay=(i-c)**2*min(c,r-c)
 vals['A57_reverse_delay_product']=(delay**4*cl**9,delay**4*ch**9,c**12)
 ff={name:strict_positive(*v) for name,v in vals.items()}
 if y==c:g,h,new_x,old_pair,sigma=e,d,x,[w,z],1
 else:
  assert z==c
  g,h,new_x,old_pair,sigma=d,e,w,[x,y],-1
 K=a[c]-g;mirror_value=2*K-a[new_x];mirror_rank=rank_by_value.get(mirror_value)
 if mirror_rank is not None and not mirror_rank<c:mirror_rank=None
 ff['A61_no_old_mirror']=mirror_rank is None
 return ff,{'g':g,'h':h,'fresh_x':new_x,'old_pair':old_pair,'sigma':sigma,'K':K,
   'mirror_value':mirror_value,'mirror_rank':mirror_rank,'old_quad':quad,'old_gaps':gaps,'delay_product_integer':delay},vals

stages=['A46','A53','A54','A57','A61'];counts={str(c):{'original_core':0,**{z:0 for z in stages}} for c in births}
rows=[];survivors=[];unknown=[]
for index,row in sorted(original.items()):
 d,e,x,y,w,z,c,s,i,r,t=row
 assert len({x,y,w,z,i,r})==6
 assert d==a[y]-a[x] and e==a[z]-a[w] and t==d-e==a[r]-a[i]>0
 assert rank_core(c,s,i,r) is True and physical_core(c,t) is True
 ff,info,vals=flags(row);counts[str(c)]['original_core']+=1
 entry={'original_bank_index':index,'record':row,'flags':ff,**info}
 alive=True
 for stage in stages:
  stage_values=[value for name,value in ff.items() if name.startswith(stage+'_')]
  if None in stage_values:unknown.append({'original_bank_index':index,'stage':stage})
  alive=alive and all(value is True for value in stage_values)
  if alive:counts[str(c)][stage]+=1
 if alive:
  cl,ch=log(c);rl,rh=log(r)
  margins={'older_birth':(s*cl**2-c,s*ch**2-c),
   'birth_output_gap':((i-c)*cl**2-c,(i-c)*ch**2-c),
   'output_top_gap':((r-i)*rl**3-r,(r-i)*rh**3-r),
   'upper_rank':(c*cl-r,c*ch-r),'physical_output':(t*cl**3-c*c,t*ch**3-c*c)}
  assert all(z[0]>0 for z in margins.values())
  entry['strict_margin_intervals']={n:list(map(str,v)) for n,v in margins.items()}
  entry['selector_margin_intervals']={n:[str(v[0]-v[2]),str(v[1]-v[2])] for n,v in vals.items()}
  entry['de']=d*e
  entry['original_covered_cut_interval']=[c+1,i-1]
  entry['source_values']=[a[j] for j in [x,y,w,z]];entry['output_values']=[a[i],a[r]]
  survivors.append(entry)
 rows.append(entry)
lam=Q(4,k*(k*k-1)**2*(a[k]-a[1])**2)
@lru_cache(None)
def tail(r):return sum((Q(4,j*(j*j-1)**2*(a[j]-a[1])**2) for j in range(r,M+1)),Q(0))
groups=defaultdict(list)
for entry in survivors:
 c=entry['record'][6];groups[(c,entry['g'])].append(entry)
 entry['lambda48_mass_exact']=str(entry['de']*lam)
 entry['original_u_r_96_exact']=str(tail(entry['record'][9]))
 entry['original_full_record_price_exact']=str(entry['de']*tail(entry['record'][9]))
graphs=[]
for (c,g),edges in sorted(groups.items()):
 by_vertex=defaultdict(list)
 for j,edge in enumerate(edges):
  for vertex in edge['record'][8:10]:by_vertex[vertex].append(j)
 assert max(map(len,by_vertex.values()))<=2
 assert len({x['fresh_x'] for x in edges})==len(edges)
 remaining=set(range(len(edges)));components=[]
 while remaining:
  pending=[min(remaining)];comp=set()
  while pending:
   j=pending.pop()
   if j in comp:continue
   comp.add(j)
   for vertex in edges[j]['record'][8:10]:pending.extend(h for h in by_vertex[vertex] if h not in comp)
  remaining-=comp
  vertices=sorted({v for j in comp for v in edges[j]['record'][8:10]})
  degree={v:sum(j in comp for j in by_vertex[v]) for v in vertices}
  kind='cycle' if all(d==2 for d in degree.values()) else 'path'
  assert kind=='cycle' or sum(d==1 for d in degree.values())==2
  boundary=sum(edges[j]['sigma']*edges[j]['record'][10] for j in comp)
  products=sum(edges[j]['de'] for j in comp)
  assert products==g*g*len(comp)+g*boundary
  components.append({'kind':kind,'edge_count':len(comp),'vertices':vertices,
   'bank_indices':[edges[j]['original_bank_index'] for j in sorted(comp)],'boundary_exact':boundary,'sum_products':products})
 graphs.append({'c':c,'g':g,'old_pair':edges[0]['old_pair'],'edge_count':len(edges),'vertices':sorted(by_vertex),
  'max_degree':max(map(len,by_vertex.values())),'bank_indices':[x['original_bank_index'] for x in edges],'components':components,
  'sum_products':sum(x['de'] for x in edges),'lambda48_mass_exact':str(sum(x['de'] for x in edges)*lam)})

out={'date':'2026-09-09','attempt':'A62_PRESCRIBED_CELLS','status':'EXACT_REFERENCE_COMPLETE' if not unknown else 'UNKNOWN_COMPARISONS_REMAIN',
 'C_exact':'1','m0':2,'M':M,'T':T,'b':b,'k':k,'births':list(births),'input':sp.name,
 'pool_source':pp.name,'pool_cell_indices_count':len(cell['original_core_bank_indices']),
 'stage_counts':counts,'original_prescribed_rows':rows,'survivors':survivors,'nonempty_graph_cells':graphs,
 'summary':{'original_prescribed_records':len(rows),'survivor_records':len(survivors),'nonempty_fixed_c_g_cells':len(graphs),
   'path_components':sum(x['kind']=='path' for g in graphs for x in g['components']),
   'cycle_components':sum(x['kind']=='cycle' for g in graphs for x in g['components']),
   'unpriced_mass':sum(x['de'] for x in survivors),'genuine_component_mass_exact':str(sum(x['de'] for x in survivors)*lam)},
 'lambda48_exact':str(lam),'log_intervals_exact':{str(n):list(map(str,log(n))) for n in sorted({23,24,25}|{x['record'][9] for x in survivors})},
 'unknown_comparisons':unknown,
 'source_sha256':{p.name:sha(p) for p in [sp,cp,pp,HERE/'reference_evaluator.py',Path(__file__)]},
 'scope':'Only b25,k48,c23/24 in one existing certified C1,m02 M96. A46.6,A53,A54,A57 reverse delay,A61 mirror deletion retained. No new history, full profile, other cut/component/birth, or proof of general forest/cycle absence. Original u_r is metadata only: survivor at k48 need not survive all original components.'}
(HERE/'A62_CELL_EXACT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'stage_counts':counts,'summary':out['summary'],'graph_cells':[(g['c'],g['g'],g['edge_count'],[(x['kind'],x['edge_count']) for x in g['components']]) for g in graphs],'unknown':len(unknown)},indent=2))
