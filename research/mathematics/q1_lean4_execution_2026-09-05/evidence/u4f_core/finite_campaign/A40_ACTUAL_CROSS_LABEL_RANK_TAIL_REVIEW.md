# A40 independent review: actual cross labels pay a far-rank component tail

Date: 2026-09-09. Status: PASS as a hand theorem for the full unchanged
original core. The recovery injection has no missing orientation
factor. No new finite calculation or Lean build was performed.

## Physical record recovery at one component

Fix 3<=b<T<=M, component k>=b+2, n=b-1, v=min(k,T), m=v-b,
and H=H_b. Let D be the actual positive differences of the first n
points. Define the actual cross-label set

    X={a_j-a_l:1<=l<=b-1, b+1<=j<=v}.

All labels are positive. Actual Sidon positive-difference uniqueness
gives card X=n m and uniquely recovers its ordered endpoint pair from
each label. The cut point b is not in the old endpoint group here.

An original record has oriented positive source labels
d=a_y-a_x>e=a_z-a_w, with x<y, w<z<=b-1, and output
t=d-e=a_r-a_i, b<i<r<=v. Define

    U=a_r-a_y in X, V=a_i-a_x in X.

Direct algebra gives V-U=d-t=e>0. For a fixed e, knowledge of U
therefore determines V=U+e. The two actual cross labels recover
(y,r) and (x,i) uniquely. The source label e recovers (w,z)
uniquely. Thus U and e recover the entire original oriented record,
including both source pairs and the ordered output pair.

In particular the map record -> U is injective among records with
that fixed e. There is no additional sign, unordered-pair or matching
multiplicity: the larger source is already designated d>e, and the
recovered physical positive-difference endpoints have unique order.
Also U!=V since e>0, so there is no zero-difference exception. The
six-distinct and strict-core conditions merely select a subset of
these recoverable records; they do not enlarge the count.

Since d<=H and at most n m records have each fixed e,

    Q_bk=sum_original_core d e <= H n m sum_{e in D}e.

The actual old gap expansion, using Sidon to count each difference
once, is

    sum_{e in D}e
      =sum_{j=1}^{n-1}j(n-j)(a_{j+1}-a_j)
      <=floor(n^2/4) H_{b-1} <= n^2 H/4.

Consequently

    Q_bk <= n^3 m H^2/4.                         (1)

This bounds the full original de mass, not just the BH part. No
mixed label is required to lie below H. A39 shows precisely why
imposing that local eligibility restriction would invalidate an
otherwise useful actual-cross-label argument.

## Genuine far-rank components

Fix one real p>2/3 for the entire argument and define

    R_b=ceil(b(log b)^p)+1, b>=3.

Since log b>1, R_b>=b+2. Partition the original genuine component
sum by k>=R_b and k<R_b. If M<R_b the far part is zero. Otherwise,
using (1), H_k>=H_b and min(k,T)-b<=k-b,

    P_rankfar_b <= n^3/4 sum_{k=R_b}^M kappa_k(k-b).

For R=R_b the exact finite tail identity is

    sum_{k=R}^M kappa_k(k-b)
      =(R-b)alpha_R+sum_{k=R+1}^M alpha_k
                         -(M-b)alpha_{M+1}.       (2)

The terminal term is preserved in this identity. To upper-bound it,
(R-b)alpha_R<=1/(R-1)^3 and the existing alpha coefficient bound
gives sum_{k=R+1}^infinity alpha_k<=1/(3R^3). Therefore

    sum_{k=R}^M kappa_k(k-b)<=4/[3(R-1)^3].

Since R_b-1>=b(log b)^p and n<=b,

    P_rankfar_b <=1/[3(log b)^(3p)].               (3)

The decreasing-integral estimate with exponent 3p/2>1 now gives

    sum_{b=3}^{T-1}sqrt(P_rankfar_b)/b
       <=(log 2)^(1-3p/2)/[sqrt(3)(3p/2-1)].     (4)

The b2 core is empty. Equations (1)-(4) need no cap: the infinite
series is only a numerical upper bound for the finite actual sum.
For k>T the real output bank remains at T; replacing its size by
k-b occurs solely in an upper bound, and the genuine component tail
continues through M. No alpha_{M+1} is set to zero and no physical
record is copied into an independent budget.

## Remaining strip and scope

For the fixed choice p=3/4, the absolute far norm constant is
8/[sqrt(3)(log 2)^(1/8)]. The remaining original components satisfy

    k<R_b=ceil(b(log b)^(3/4))+1,
    equivalently k<=ceil(b(log b)^(3/4)).

This is a narrower rank strip than the earlier cap-derived A33 strip.
It remains a growing strip, and this theorem does not control its
full square-root harmonic norm. The nonnegative component partition
and sqrt triangle inequality show exactly how a uniform remaining
norm would combine with (4); no such estimate is presumed.

The result is noncircular actual Sidon input through full endpoint
recovery. It assumes no infinite capped history, Q1, or maximal prefix
length. It is not a final proof of CoreUniform or original Q1. The
parent's source sections and any later generic Lean scope require
their own bounded final readback.
