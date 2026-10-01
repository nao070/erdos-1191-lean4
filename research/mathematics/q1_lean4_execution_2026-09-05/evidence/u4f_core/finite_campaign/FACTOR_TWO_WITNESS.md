# A strict-core witness requiring both orientation cases

2026-09-09. Finite exact counterexample to a proposed intermediate
incidence sharpening; not a counterexample to Q1191-U4F-CORE-UNIFORM-01.

## Exact claim rejected

For fixed later source birth c, older positive difference e, and lower
output index i, there is at most one eligible six-distinct strict-core
record. This claim remains false if the upper output r is fixed as well.

Take the actual positive Sidon prefix

```
(1,2,4,8,13,21,31,45,66,81,97,123,148,182,204).
```

Set M=T=15, C=1, m0=2 and (c,s,i,r)=(10,9,14,15). The older
label is e=a9-a4=66-8=58. The two labels born at c are

```
d_plus  = a10-a1 = 81-1  = 80 > 58,
d_minus = a10-a8 = 81-45 = 36 < 58.
```

Both output differences equal

```
|80-58| = |36-58| = 22 = a15-a14 = 204-182.
```

The six endpoint sets are respectively {1,10,4,9,14,15} and
{8,10,4,9,14,15}, both of cardinality six. In the contract's numerical
orientation d>e, the two full rows are

```
columns = d,e,p(d),q(d),p(e),q(e),c,s,i,r,t
(80,58,1,10,4,9,10,9,14,15,22)
(58,36,4,9,8,10,10,9,14,15,22)
```

All strict core inequalities follow already from log(10)>23/10 and
log(15)>27/10, which the rational log enclosures independently certify:

```
9*(23/10)^2 > 10,
4*(23/10)^2 > 10,
1*(27/10)^3 > 15,
10*(23/10)  > 15,
22*(23/10)^3 > 100.
```

Every rank 2<=n<=15 satisfies H_n<=n^2, so the C=1,m0=2 cap follows
from log(2n)>1. The reference evaluator verifies all 105 positive
differences are distinct; the independent checker instead verifies all
120 repeated two-sums are distinct.

Both records cover precisely b=11,12,13, once each. With the genuine
partial price, kappa_15=1/188160 and

```
u_15^[15] = 1/7753885440.
```

Their respective record weights are 4640*u_15 and 2088*u_15. Each
retains its one price across that interval; the harmonic coverage is
1/11+1/12+1/13=431/1716. The two sign cases are physical records,
not duplicate representations of one unordered source pair.

## Verification and scope

`C1_m02_greedy_M15.json` contains the exact profile, genuine prices,
cap certificates, source SHA-256 values and all-cuts coverage checks.
Its `_records.json` contains all 87 core records. Its
`_independent_check.json` records successful separate output-endpoint
enumeration, integer fixed-point rigorous log bounds, and exact profile
agreement. Neither checker imports the other's enumeration or log code.

The valid two-case incidence bound is not disproved. A proposed factor-one
replacement is rigorously rejected. No conclusion about a common uniform
K, infinite extension, or original Q1 follows from this finite witness.

Next nonduplicate action: retain both orientations and seek information
from the correlation of different (c,e,i,r) fibers or actual physical
label weights; single-fiber uniqueness cannot supply the missing saving.
