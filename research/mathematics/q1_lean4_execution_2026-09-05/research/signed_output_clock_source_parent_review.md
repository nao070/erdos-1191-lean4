# Parent independent review of the output-clock source

2026-09-05. Reviewer: /root, GPT-6 Astra Ultra.

The entire source was independently read, then its final replacement
of Section 4 and its per-collision sharpness wording were reread.
This review binds to `research/signed_output_clock_source.md`,
SHA-256
`b499cad5c00d89d106d6163c10f82beaff49c7c231332c987066fb31cf8cad81`.
All mathematical statements (1)--(28) are supported at their stated
scope. No numerical execution or Lean verification was performed
by this mathematical review.

## Exact absolute comparisons

The parent independently derived both strengthened absolute bounds.
For endpoint distances delta_i>0 and a+b=S=sum delta_i, the
two factors in g_ij cannot both be negative. In the positive case,
`ab(S-p-q)-S(a-p)(b-q)=a q(a-p)+b p(b-q)>=0`.
Summing the six ordered slot pairs gives the asserted bound on
their positive parts and then on their absolute sum. Substituting
`sigma_U^2=sum delta_i^2-S^2/3` proves exactly

```
2B-Rabs >= (6 sigma_U^2+4ab)/A >=0.
```

The earlier matching stabilizer and doubled-record cancellation
also hold for absolute values; no repeated endpoints are omitted.
The same cancellation gives the exact Born-absolute reindexing
`(2/A)sum_i(S-delta_i)(|a-delta_i|+|b-delta_i|)`.
The inner absolute sum is at most S on [0,S]. Cauchy then gives
Babs<=3B. Born-only complete groups satisfy the stronger 5/3
ratio, so both full stage bounds follow with the stated clocks.
The previous finite sharpness families establish coefficient two
per collision only, precisely as the final wording specifies.

## Fixed Gram source, its trace and finite output boundary

The actual autocorrelation m_k has diagonal k and offdiagonal
indicator of Fhat_k by Sidon uniqueness. Its restriction is a
Gram matrix. The entrywise tensor product in (5) is therefore
PSD; entrywise nonnegativity separately follows from
|de|+lambda de>=0. Summing the compatible components gives
u_max(b,r) at every ever-used output and zero at a never-used
output. The diagonal retains the additional factor k.

The partial-fraction identity for k*kappa_k*Q_k telescopes to
2*zeta(2)-1. It proves finite trace and convergence on each
finite bank, not finite global mass. For old source pairs whose
output appears after N, u_r<=u_(N+1)<=w_(N+1) and
sum|d|<=Q_N H_N. Their total contribution is therefore at most
(1+lambda)/2. This includes all finite-bank future outputs and
does not change the permanent source under extension.

The literal historical maximum is linear for a fixed nonnegative
source: each physical kernel increases until its output appears,
so it equals the single sum over b<r. Equations (9)--(13) then
follow by a disjoint Born/retired partition. The mass coefficient
10+6lambda is correct: twice (3+lambda) from Born and twice
(2+2lambda) from retirement. The lower mass bound follows
from Babs>=B>=0. Its divergence under the fixed cap is consistent
with the O(log N) upper bound.

## Actual future payments and the correction to the convolution idea

Expanding the masked energy gives sum_t m_B(t)m_k(t)C_g(t).
The parent's earlier tentative ordinary triple-convolution idea
would have confused an entrywise matrix product with an operator
product. Equation (14) correctly rules that out. When B is in
P_k, every nonzero actual difference of B has m_k(t)=1.
Only the diagonal changes, and the additional term cancels
exactly against the trace subtraction when computing pair demand.
No k-fold moment amplification is available.

For k>=e, restriction to old sources therefore agrees with the
ordinary carrier precisely on Delta B. This proves the payment
comparison by actual coefficients, without claiming a global
PSD or entrywise ordering for the ordinary carrier. Both old
shadows vanish at every future point, and the support length is
L+2H. Their masses and first moments give (17), with the full
m(1+lambda)Z diagonal. Positive-part payment uses entrywise
nonnegativity of the physical kernel.

In (18), each p_k(h) is zero or one because the actual block
difference sets are disjoint. It selects exactly the component
tails k>=e_i on old sources with b<=n_i. Summing those selected
components gives Aactual_i; the complement is the same source's
unspent part. Outputs after N remain in the complement. Thus
the equality retains every output and no label budget is copied.

## Quantitative half-block estimate and financing

At good n=2p, the p^2/2 positive cross gaps and their reflections
give A_n>=Q_n H_n/(8K) and Z_n>=Q_n H_n^2/(16K^2).
The half-block ending at e=3n/2 leaves the component interval
[e,2n), with no third lookahead requirement. Q_e/Q_n<=3 and
Q_(2n)/Q_n>4 give the exact tail constant 7/(144K^2).

For m=n/2, the mass demand lower coefficient is
c_tail*epsilon^2/[8(K+2)C log(2n)], and the subtracted trace
is at most 1/[4(n-1)]. The moment coefficient in (23) has
factor 3/[2(K+2)^3], as obtained directly from twelve times
m^2 in the first-moment energy. Both errors are dyadically
summable, and the already established good-index harmonic
divergence applies. The ordinary unit tail of the compatible
source has mass one; its odd correction is u_n, so (26) is
the correct half-block demand with its own full trace.

Adding theta*Psi to W' is an explicit addition of nonnegative
kernels. Its actual cost is included using linearity of this
fixed-source historical capacity, and the Born saving finances
it when theta(2+2lambda)<=lambda0. The boundary in (25) is
one finite-terminal constant, not a new charge for every row.
The same physical selected outputs pay the combined kernels
and yield (27).

Finally (28) is a LOWER bound on the old baseline margin.
Its right side diverges under the hypothetical cap; no upper
bound contradicting it has been established. This direction is
essential. The new source, absolute theorem and financed demands
remain supporting research. They do not prove original Q1 or
fulfill its final Lean completion gate.
