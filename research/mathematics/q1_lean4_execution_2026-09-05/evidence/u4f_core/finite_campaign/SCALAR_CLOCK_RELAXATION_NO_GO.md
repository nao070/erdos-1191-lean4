# No-go for the explicitly listed scalar relaxation

2026-09-09. Independent adversarial review of the main researcher's
proposed abstract-record construction. This is **not an actual Sidon
family**, not a strict-core record family under the complete contract,
and not a counterexample to the frozen theorem or Q1.

## Exact claim and verdict

The listed scalar core inequalities, diameter cap, source count at each c,
and incidence counts at each (c,s), (c,i), (c,r), and (i,r), together with genuine
partial component prices and one interval per abstract record, do **not**
imply a uniform square-root profile bound. The construction below gives
a rigorous counterexample to that implication.

The phrase "listed scalar inequalities" is essential. The corrected
principal construction below retains the true birth-pair count at fixed
(c,s), addressing a flaw in the originally proposed fixed-s model.
It does not show that every possible refinement involving scalar birth
clocks or actual labels fails. The original flaw is recorded at the end.

## Construction, with exact onset

Let N be a power of two, N>=64. For the block at scale N choose integers

```
N <= c < 9N/8,
5N/4 <= i < 11N/8,
3N/2 <= r < 13N/8.
```

For every such (c,i,r), introduce precisely N/16 artificial records,
indexed by a distinct record identifier (N,c,i,r,l), 0<=l<N/16.
Each receives

```
s=3N/4+l,
d=3N^2/4,  e=N^2/4,  t=d-e=N^2/2.
```

Use one scalar diameter sequence H_1=0, H_k=k^2 for k>=2. For a single
global component horizon M use exactly

```
alpha_k = 1/[k^2(k-1)^2],
kappa_k = alpha_k-alpha_(k+1),
u_r^[M] = sum_(k=r..M) kappa_k/k^4.
```

Nothing resets alpha_(M+1), and no record is split into new copies at
different cuts. Each record contributes its one weight u_r^[M]de on its
full interval c<b<i.

The construction uses repeated numerical labels and has no actual point
endpoint equations. Record identifiers distinguish artificial records;
they must not be mistaken for distinct physical unordered source pairs.

## The requested scalar conditions all hold

Since log N>=log64>4 and c>=N, one has (using only log N>3 below)

```
s >= 3N/4 > c/2 > c/(log c)^2,
i-c > N/8 > c/(log c)^2,
r-i > N/8 > r/(log r)^3,
r < 13N/8 < 3N < c log c,
t=N^2/2 > c^2/(log c)^3.
```

For the second inequality use c<9N/8 and (log c)^2>9. For the third,
use r<13N/8 and (log r)^3>27>13. For the last,
c^2/(log c)^3 < (81/64)N^2/27 = 3N^2/64.
The lower log estimate can be justified directly by
log2=2(1/3+(1/3)^3/3+...)>2/3, hence log64>4.

All other specified scalar checks hold:

```
3 <= c < i < r,
2 < s < 13N/16 < c,
0 < e < d <= H_c,
t <= H_c,
0 < r-i <= 3N/8-1,
(r-i)(r-i+1)/2 < 9N^2/128 < t,
H_k=k^2 <= k^2 log(2k)  (k>=2).
```

Thus the scalar diameter cap has the same C=1,m0=2 at every rank and
at every scale. If six different formal endpoint indices are desired as
a cardinality-only check, (1,c,2,s,i,r) are distinct. This observation
does not assert their declared labels equal actual point differences.

There are N/8 values of each of c,i,r and N/16 multiplicity. At any
single scale, the exact counts are:

| Fixed clocks | Constructed count | Requested upper bound |
|---|---:|---:|
| c | N^3/1024 | c^3/2 |
| (c,s) | N^2/64 | (c-1)(s-1) |
| (c,i) | N^2/128 | 2 binom(c-1,2) |
| (c,r) | N^2/128 | 2 binom(c-1,2) |
| (i,r) | N^2/128 | binom(i-1,2) |

The first comparison follows from c>=N. The (c,s) count is just the
number of choices of i,r, because l is determined by s; its comparison
uses c-1>=N/2 and s-1>=N/2. For the next two,
(c-1)(c-2)>=(N-1)(N-2)>=N^2/4. For the last, i>=5N/4 and N>=64
imply i-2>=N, so binom(i-1,2)>=N^2/2. These estimates leave ample
room and prove every row with the stated onset.

The c, s, i, and r ranges are separately disjoint at different dyadic
scales. Consequently those same fixed-clock counts are unchanged when
all scales through the global horizon are combined.

## Genuine price lower bound and linear divergence in block count

Assume M>=2N. All the records in this scale have r<13N/8. Algebra gives

```
kappa_k/k^4 = 4/[k^5(k^2-1)^2] >= 4/k^9.
```

The integer range 13N/8<=k<=2N contains 3N/8+1 terms, all available
in the genuine partial price. Therefore

```
u_r^[M] >= (3N/8) * 4/(2N)^9 = 3/(1024N^8).
```

There are exactly N^4/8192 records in the scale, and de=3N^4/16.
Every one covers every integer cut in

```
B_N={b : 9N/8 <= b < 5N/4}.
```

Consequently the abstract profile satisfies

```
P_b(M,M) >= (N^4/8192)*(3/(1024N^8))*(3N^4/16)
          = 9/2^27                         (b in B_N).
```

The cut set has N/8 members and b<5N/4 throughout, so
sum_(b in B_N)1/b >= 1/10. Its physical logarithmic width is the fixed
positive number log(10/9). Hence this single scale contributes at least

```
sum_(b in B_N) sqrt(P_b)/b >= 3/(81920 sqrt(2)).
```

Now take all N=2^j, 6<=j<=J, and one global horizon M=2^(J+1).
There are L=J-5 scales, their B_N are disjoint, and the same genuine
price lower bound holds at every scale under that one M. Thus

```
N_abstract(M,M) >= 3L/(81920 sqrt(2)) -> infinity.
```

Within-block exact coverage and Cauchy are not contradicted. Each of
these blocks instead has I_j >= 9/(10*2^27), so these listed scalar
constraints cannot imply summable dyadic square-root masses either.

## Precisely which genuine information has been discarded

The following actual-history conditions do not hold here and are not
among the hypotheses of this no-go:

* Numeric difference labels have unique actual endpoints and a unique
  source birth. The construction deliberately reuses the same d,e at
  many births, endpoints and record identifiers.
* An unordered physical source pair has at most one actual output, with
  its unique endpoint pair. Artificial record identifiers do not satisfy
  this property.
* The true fixed-(c,e,i,sign) uniqueness is violated: all constructed
  later labels have d>e and the same numerical e, with N^2/128 records
  at fixed (c,e,i). This already exceeds one at N=64.
* The graph on genuine numerical labels with edges separated by a
  fixed t has degree at most two. A bound on the number of abstract
  records per (i,r) is not a substitute for that graph property.

The valid conclusion therefore rejects a proof of uniform N based only
on the specifically verified scalar conditions. It does not reject a
proof retaining one of these further constraints and does not supply an
actual finite or infinite Sidon counterexample.

No Lean theorem or actual-Sidon finite computation is claimed for this
construction. The proof is an exact hand argument with the explicit
onset and constants above. The original contract and genuine-price
definitions are those identified by the source hashes in this directory's
certified actual-profile JSON files.

Next nonduplicate action: retain the actual fixed-label/output
correlation and determine whether its weighted aggregate rules out such
multiscale profiles. The corrected model already retains the scalar
fixed-(c,s) count; introducing that count alone cannot close the proof.

## Review history: flaw in the originally proposed fixed-s model

The original proposal assigned s=floor(3c/4) to every record at a fixed c.
It satisfied the original list of scalar tests with onset N>=32, but
violated the additional true count
#(records at fixed c,s)<=(c-1)(s-1). At c=N it assigned N^3/1024 records
to s=3N/4; for dyadic N>=1024 this exceeds
(N-1)(3N/4-1)<3N^2/4.

The principal model above corrects that issue by setting s=3N/4+l,
with exactly one earlier birth for each multiplicity index. This leaves
the total record count, prices, coverage, profile lower bound and all
other scalar constraints unchanged, while making the count at (c,s)
equal to N^2/64. The clean onset has been set to N>=64. The correction
does not repair actual numeric-label uniqueness or endpoint realization.
