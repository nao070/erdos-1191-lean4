import numpy as np,math
I=math.log(2)-1.5
B=9*math.log(2)-4.5*math.log(3)-1.5
C=4.5*math.log(3)-2*math.log(2)-3
wstar=(9*math.log(2)-5*math.log(3))/2-.25
for n in (128,512,2048):
 a=np.arange(2*n+6,dtype=np.int64)
 def f(j):return j*j*math.log(j)
 for j in range(6,len(a)-2,3):
  t=math.ceil(f(j));d=math.ceil((f(j+2)-f(j))/2)
  a[j:j+3]=(t,t+d,t+2*d)
 assert np.all(np.diff(a[:2*n])>0)
 def energy(v):return sum(np.log(v[j]-v[:j]).sum() for j in range(1,len(v)))
 LA=energy(a[:n]);LB=energy(a[n:2*n]);X=sum(np.log(a[n:2*n]-x).sum() for x in a[:n]);Ltotal=energy(a[:2*n])
 b=a[n-1:2*n];h=np.diff(b);W=0.
 for i in range(n-2):
  js=np.arange(i+2,n);mid=b[js]-b[i+1];outer=b[js+1]-b[i]
  W+=np.sum((js-i)**2/(4*n*n)*np.log1p(h[i]*h[js]/(mid.astype(float)*outer)))
 print({'n':n,'old_constant_error':LA/n**2-math.log(n)-.5*math.log(math.log(n))-I,'new_constant_error':LB/n**2-math.log(n)-.5*math.log(math.log(n))-B,'cross_constant_error':X/n**2-2*math.log(n)-math.log(math.log(n))-C,'W':W,'W_limit':wstar,'split_error':Ltotal-LA-LB-X,'factorial_floor_slack_per_n2':(LA-math.lgamma(n*(n-1)//2+1))/n**2})
