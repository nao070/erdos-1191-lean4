import sys
from fractions import Fraction as F
from collections import defaultdict
sys.path.insert(0,'/Users/USER/Downloads/C143_S32_S41_FULLROOT_EXACT_PHASE_2026-09-04_V2')
from c142.master import point_matrix
for n in range(3,33):
 M=point_matrix(n);lhs={(i,j):-8*n*n*M[i][j] for i in range(n+1) for j in range(i+1,n+1)}
 rhs=defaultdict(F)
 for j in range(1,n):
  rhs[0,j]+=2*j-1;rhs[j,n]+=2*(n-j)+1
 rhs[0,n]-=(n-1)**2
 for i in range(1,n+1):
  for j in range(i+1,n+1):rhs[i,j]-=2
 for i in range(n-1):
  rhs[i,i+2]+=1;rhs[i,i+1]-=1;rhs[i+1,i+2]-=1
 assert all(lhs[k]==rhs[k] for k in lhs),(n,lhs,rhs)
print('exact_W_newhalf_log_coefficient_identity_ranks_3_through_32_PASS')
