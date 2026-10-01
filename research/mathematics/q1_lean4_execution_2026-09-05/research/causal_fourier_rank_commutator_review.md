# Independent review of the output-rank commutator

2026-09-05. Reviewer: /root/causal_telescoping, GPT-6 Astra Ultra.

**Verdict: supported, with no material correction requested.**
The reviewer read the whole authored source and independently
rederived equations (1)--(16), including the finite actual Sidon
family and every displayed constant. This is an analytic review,
not a test run or a Lean verification.

Reviewed source: research/causal_fourier_rank_commutator.md.
SHA-256:
3e410eef809aaef4469d7b5de69836ac48a725d7d9ac8d5bec791326a07e8b74.

The full source was read in tool output 940194. The same hash was
then measured in output 5d022f; the adjoining clock observation was
2026-09-05 14:54:51 UTC. The source was not edited. Only this new
review file was created; no earlier evidence or successful check
was rerun.

## 1. Exact output weights and the fresh source star

For b<i,j<=T, its coefficient in the positive Abel expansion is
u_T+sum_(r=max(i,j)..T-1)(u_r-u_(r+1))=u_max(i,j).
Thus source equation (1) is exact, V_b is pointwise nonnegative,
and its constant coefficient is m_b. Every positive or negative
actual future output has coefficient u_r at its true upper
endpoint, rather than at the source rank or a reset terminal price.

The phase z^(a_b) in g_b drops from its absolute square. Every
nonconstant frequency of |g_b|^2 is a difference of two endpoints
strictly before b. The actual suffix differences have both
endpoints after b. Sidon uniqueness excludes their intersection.
Equivalently the weighted old/future point supports are disjoint
in the B2 quartic identity. This proves (2), including all fresh
diagonal terms. It justifies removal of the fresh same-sign
eligible contribution and no broader source class.

## 2. Signed pair normalization and the repeated fresh class

Writing h_b=h_(b-1)+g_b in the same-sign positive-frequency
kernel gives the factor 2(1+lambda)X_b after integration against
the symmetric V_b. The analytic square gives
2(1-lambda)Y_b+(1-lambda)Z_b. Thus (3) has the correct factors.
In particular the symmetric future polynomial does not supply
an extra factor two in the analytic opposite-sign term.

The unique latest source birth prevents duplication in (3),
although many suffixes contain the same physical output.
All gap and V_b coefficients are real and nonnegative, so the
three integrals are real and nonnegative. The fresh analytic
square includes doubled labels and same-birth opposite-sign
pairs, which cannot be removed with the fresh same-sign star.

Both bounds on sum Z_b are valid. The first uses distinct
future output labels and u_r<=alpha_b/H_b^2. For the sharper
bound, positivity of V_b gives

~~~
Z_b<=integral |g_b|^2V_b=m_b s_b
   <=(b-1)/(3b^3).
~~~

Summing from b=2 yields exactly [zeta(2)-zeta(3)]/3, as in (4).
The weaker intermediate bound m_b s_b<=1/(3b^2) displayed later
in the source is not the bound used for this sharper constant.

## 3. The two exact commutators

Removing a_b from the suffix leaves its diagonal u_b and the two
cross terms in (5). Since |h_(b-1)|^2 has equal positive and
negative autocorrelation coefficients, both cross terms contribute
L_b, proving (6). Expanding h_b and then subtracting the old
measure gives exactly

~~~
E_b-E_(b-1)=2X_b+m_b s_b-u_b S_(b-1)-2L_b.
~~~

Both endpoint energies vanish. Reordering the finite nonnegative
diagonal sum gives
sum_b m_b s_b=sum_r u_r sum_(b<r)s_b
=sum_r u_r S_(r-1).
Consequently the commutator retains sum X_b=sum L_b; it does not
cancel the causal quantity.

For h^2 the constant coefficient and all negative frequencies
are absent. Exactly one nonconstant term of (5) therefore
contributes, giving (8) with no factor two in its final term.
Its two endpoint energies also vanish. These identities require
no martingale assertion or numerical ordering of gap births.

## 4. Cauchy constants and the correlated profile

Each actual suffix output enters the absolute-square integral
in both orientations, so the covariance identity (9) has the
factor 2P_b. Weighted Cauchy against the same nonnegative V_b
bounds both X_b and Y_b by
sqrt(m_b s_b[m_b S_(b-1)+2P_b]).
Their two prefactors sum to four for every 0<=lambda<=1.
Splitting the square root proves (10).

The pointwise price comparison

~~~
1/[r^2(r-1)^2]
 <=[(r-1)^(-3)-r^(-3)]/3
~~~

follows after clearing denominators from
3r(r-1)<=3r^2-3r+1. Summing it gives the source bound for m_b.
Using s_b<=(b-1)H_b^2 and
S_(b-1)<=(b-1)(b-2)H_b^2/2 then proves

~~~
m_b sqrt(s_b S_(b-1))
 <=1/(3sqrt(2)b^(3/2)),
sqrt(2m_b s_b P_b)
 <=sqrt(2/3)sqrt(P_b)/b.
~~~

Thus both constants in (11) and its finite diagonal C_lambda
are supported without using the cap.

The source correctly states that P_b are overlapping covariance
quantities, not independent allocated budgets. The trivial
P_b<=1/8 is also valid: actual output uniqueness bounds the
unweighted positive autocorrelation sum by the square of the old
positive-feature mass divided by two, and u_r<=w_b on the suffix.
No summability of the remaining square-root series follows.

## 5. The actual finite quadratic family and its exact limitation

For x_i=2pi+(i^2 mod p), equality of two positive differences
forces the integer index gaps to coincide: otherwise their 2p
multiples differ by at least 2p while the two residue corrections
differ by strictly less than 2p. Reduction modulo p then gives
2d(i-j)=0. Since p is odd and 0<d<p, the starting indices agree.
This proves actual distinct positive differences and hence full
Sidon two-sum uniqueness, including repeated summands. The
translation by 1 makes the displayed history positive.

For n=(p-1)/2 and p>=5, the source estimates follow from

~~~
x_j-x_i>=p(j-i),    n>=2p/5,    H_n<p^2,
sum_(i<j<n)(j-i)=n(n^2-1)/6.
~~~

Since n>=2, n(n^2-1)/6>=n^3/8. Therefore
U>=p^4/125 and S<=p^6/8, as in (14).

The positive-gap shadow is supported in an integer interval
with at most x_(p-1)+x_(n-1)-x_n sites, strictly less than 2p^2.
This count already includes the endpoint convention: the least
positive source label is at least one. Since m>=p/2, its squared
mass divided by that support size is at least p^8/125000.
The diagonal mS is at most p^7/8. The exact off-diagonal
energy factor is two, proving (15).

All these old-source/future-block pairs are eligible for the
strict triangular functional. At lambda=1 its same-sign factor
is four, giving A_p^1>=p^8/62500-p^7/4. The threshold p>=31250
is exactly what makes this at least p^8/125000. Finally
H_p^2<4p^4 gives the ratio lower bound p/500000 in (16).

This is a realizable analytic family disproving the proposed
uniform raw O(T^3H_T^2) estimate. It uses one actual old-half/
future-half block, not repeated payments. It does not construct
an infinite capped history, contradict Q1, or replace the actual
complete-history prices by independently chosen terminal prices.

## 6. Remaining scope

The new uniform finite diagonal and the exact covariance
reduction are genuine consequences. The proof obligation is a
new estimate of the correlated profile in (11), or an equivalent
order-sensitive estimate retaining (6)--(9), under one actual
history and the one fixed cap.

No such estimate or original-Q1 conclusion is established by
the reviewed source. No formal theorem or numerical execution
is claimed by this review.
