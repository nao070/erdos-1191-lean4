from itertools import combinations_with_replacement
checks=0
for e in range(3,25):
 N=e+1
 for u,v,w in combinations_with_replacement(range(N+1),3):
  q=[0]*u+[-1]*(v-u)+[1]*(w-v)+[0]*(N-w)
  d=[q[i]-q[i+1] for i in range(e)]
  nz=[(i,x) for i,x in enumerate(d) if x]
  F=-sum((j-i)**2*x*y for z,(i,x) in enumerate(nz) for j,y in nz[z+1:] if j-i>=2)
  s0=sum(d);s1=sum(i*x for i,x in enumerate(d));s2=sum(i*i*x for i,x in enumerate(d))
  adj=sum(d[i]*d[i+1] for i in range(e-1));L=sum(x*x for x in d)
  tr=sum(q[i]==-1 and q[i+1]==1 for i in range(1,e-1))
  assert F==s1*s1-s0*s2+adj
  assert adj<=0 and s1*s1-s0*s2>=0
  assert 3*F+2*L>=0 and F+4*tr>=0
  if F<0:
   assert q[0]==q[-1]==0
   a=q.count(-1);b=q.count(1)
   assert (a,b) in ((1,1),(1,2),(2,1)) and F in (-4,-1)
  checks+=1
print('exact_actual_state_pattern_checks',checks)
N=64;epochs=(4,8,16,32);towerchecks=0
for u,v,w in combinations_with_replacement(range(N+1),3):
 q=[0]*u+[-1]*(v-u)+[1]*(w-v)+[0]*(N-w)
 d=[q[i]-q[i+1] for i in range(N-1)]
 energies=[]
 for e in epochs:
  dd=d[e-1:2*e-1]
  s0=sum(dd);s1=sum(i*x for i,x in enumerate(dd));s2=sum(i*i*x for i,x in enumerate(dd))
  en=s1*s1-s0*s2
  assert 0<=en<=2*e*e
  energies.append(en)
 assert sum(en!=0 for en in energies)<=1
 towerchecks+=1
print('exact_whole_tower_pattern_checks',towerchecks)
