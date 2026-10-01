import sys,json,copy,time
from pathlib import Path
p=Path(__file__).parent;sys.path.insert(0,str(p));import c143_full_pricing_replay as a
import numpy as np
start=time.monotonic();b=json.loads(a.BANK.read_text());m=a.Model(b);c=b['children'][0];L,R=a.pf(c['left']),a.pf(c['right']);parent=b['geometry_parents'][0];cells,D=m.geometry(a.pf(parent['left']),a.pf(parent['right']));passed=[]
def rejects(name,f):
 try:f()
 except (AssertionError,ValueError,IndexError):passed.append(name)
 else:raise AssertionError('mutation accepted: '+name)
for name,mutate in [
 ('negative primal weight',lambda B:B['support'][0].__setitem__(2,'-1/1')),
 ('out of universe support',lambda B:B['support'][0].__setitem__(1,m.m)),
 ('duplicate selected gate',lambda B:B['selected_gate_indices'].__setitem__(1,B['selected_gate_indices'][0])),
 ('dual list length mismatch',lambda B:B['dual_affines'].pop()),
 ('stored objective false',lambda B:B['primal_objective'].__setitem__('intercept','0/1')),
 ('dual affine false',lambda B:B['dual_affines'][0].__setitem__('intercept','-1000000000/1'))]:
 B=copy.deepcopy(c['basis']);mutate(B);rejects(name,lambda:m.verify_basis(cells,D,B,L,R))
for name,change in [
 ('child coverage missing',lambda z:z['children'].pop(0)),
 ('geometry breakpoint false',lambda z:z['geometry_parents'][0].__setitem__('left','1/1')),
 ('integral record duplicated',lambda z:z['integral']['records'].__setitem__(1,z['integral']['records'][0])),
 ('endpoint phase false',lambda z:z['geometry_endpoints'][0].__setitem__('phase','1/1'))]:
 z=copy.deepcopy(b);change(z);rejects(name,lambda:a.coverage(z,m))
rejects('unsafe int64 bound',lambda:a.exact_weighted_cross(np.array([[1<<62]],dtype=np.int64),np.array([[8]],dtype=np.int64),[1]))
res={'status':'ADVERSARIAL_REJECTIONS_PASS','rejected_mutations':passed,'elapsed_seconds':time.monotonic()-start};(p/'c143_full_pricing_replay.adversarial.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
