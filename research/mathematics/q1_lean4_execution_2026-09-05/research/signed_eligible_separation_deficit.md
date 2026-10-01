# A spatial and rank separation deficit for eligible collisions

2026-09-05. Author: /root, GPT-6 Astra Ultra.

This is an analytical consequence of the exact eligible-collision formulas in
`signed_output_energy_closure.md`, independently expanded by the parent. It is
not an original-Q1 proof, a finite-computation certificate, or a Lean theorem.
The source/output clocks below are actual ranks in one complete integer Sidon
history. The quantitative defect supplements the existing single physical
budget; it does not create another payment budget.

## 1. Exact geometry and a separation estimate

Take an actual eligible collision of disjoint equal-sum triple multisets

```
U={ell,u,v}, V={n,x,y}, n>ell>max(u,v,x,y),
t=n-ell, p=ell-u, q=ell-v, A=ell-x, B=ell-y,
s=p+q, A+B=s+t, aut=aut(U)aut(V).
```

All five distances are strictly positive; repeated old slots are allowed.
The exact multiset normalization is unchanged. Put

```
L=min(p,q,A,B), M=max(p,q,A,B),
D*=t+L=n-max(u,v,x,y), H*=t+M=n-min(u,v,x,y).
```

Thus D* is the distance from the newest endpoint to the latest actual source
endpoint, and H* is the width of all six slots. Write H_lambda for the eligible
carrier sum of |de|+lambda de, where 0<=lambda<=1, and DeltaY for the full
collision contribution to the signed energy excess. The earlier exact formula
and its positive-part bound imply

```
G_lambda:=(1+lambda)DeltaY-8 H_lambda
 >=8(1+lambda)(pq+AB+ts+t^2)/aut.                 (1)
```

For completeness, the exact numerator before this weakening is
`8(1+lambda)(pq+AB+ts+3t^2)-32P`, with
`P=((A-p)(B-q))_+ +((A-q)(B-p))_+ <=t^2/2`.
It gives (1) because the retained coefficient of t^2 is
`8(1+3lambda)>=8(1+lambda)`.

At least one of pq and AB contains M, and its other factor is at least L.
Also s>=2L and s+t=A+B>=M; the latter holds for M in {p,q} as well,
since then s>=M. Consequently

```
pq+AB >= LM,
t(s+t) >= t(M+t+2L)/2,
pq+AB+ts+t^2 >= LM+t(M+t+2L)/2
                 >= (t+L)(t+M)/2 = D* H*/2.       (2)
```

The second inequality follows by averaging the two lower bounds
`s+t>=M` and `s+t>=t+2L`. The final difference in (2) is
`(LM+tL)/2>=0`. Combining (1)-(2) yields

```
G_lambda >=4(1+lambda) D* H*/aut.                 (3)
```

For any three real numbers in an interval of width H*, the sum of squared
deviations from their mean is at most 2(H*)^2/3. To verify the constant,
sort them as a<=b<=c, set h=c-a and z=b-a, and use
`sum centered squares=(h^2+z^2+(h-z)^2)/3 <=2h^2/3`.
Apply this separately to U and V, retaining their slots and multiplicities.
Since `DeltaY=12(sigma_U^2+sigma_V^2)/aut`, it follows that

```
0<DeltaY <=16(H*)^2/aut.
```

Together with (3), this proves the relative separation defect

```
G_lambda >=(1+lambda) D*/(4H*) DeltaY,
H_lambda <=(1+lambda)/8 [1-D*/(4H*)] DeltaY.       (4)
```

No asymptotic spacing, distributional regularity, radius cap, or finite test
enters this all-history collision inequality.

## 2. Actual rank separation under one fixed cap

Let r be the rank of n and b the latest rank of the four source endpoints.
Then D*=a_r-a_b and H*<=H_r=a_r-a_1. Write h=r-b>=2. The interval
from a_b to a_r contains h+1 actual Sidon points. Its h(h+1)/2 positive
pair differences are distinct integers no larger than D*. Therefore

```
D* >=h(h+1)/2,
G_lambda >=(1+lambda) h(h+1)/(8H_r) DeltaY.       (5)
```

If a single fixed eventual cap `H_r<=C r^2 log(2r)` is assumed, the
same collision at every rank beyond its one fixed onset satisfies

```
G_lambda >= (1+lambda)/(8C log(2r))
             * h(h+1)/r^2 * DeltaY.              (6)
```

In particular, for any fixed epsilon>0, collisions with h>=epsilon r
have a defect at least
`(1+lambda)epsilon^2 DeltaY/[8C log(2r)]`.
This concerns the newest-to-source rank gap, not only the gap between
the two output endpoints. The latter may be short while h is long.

## 3. The same weighted physical budget

Let E_r denote the set of eligible actual collisions whose newest endpoint
has rank r. For any finite nonnegative prices omega_r, summing (4) gives

```
sum_r omega_r H_(lambda,r)
 <=(1+lambda)/8 sum_r omega_r DeltaY_r
   -(1+lambda)/32
      sum_r omega_r sum_(C in E_r) [D*(C)/H*(C)] DeltaY(C).   (7)
```

Active collisions with no eligible output and the nonnegative Born-only
remainder contribute only to the first term on the right. Their omission
from the displayed subtraction weakens the bound in the valid direction.
With omega=u, the left side is exactly the eligible output-clock budget
already available to actual strictly future blocks. Thus its existing
demand comparison and finite-tail accounting can be strengthened by the
single subtraction in (7). No historical capacity or positive-part bound
is duplicated.

The current argument does not establish that a large proportion of the
weighted collision energy lies at a fixed fractional rank gap. Even if
that were established, (6) contains a factor 1/log(2r), so divergence of
the weighted energy alone would not prove divergence of this defect.
Neither that missing frequency statement nor a demand-versus-energy
contradiction is claimed. These are explicit remaining research questions,
not completion conditions for original Q1.
