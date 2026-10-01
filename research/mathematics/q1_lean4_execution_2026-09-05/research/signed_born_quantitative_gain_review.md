# Independent review of quantitative full signed Born growth

Date: 2026-09-05. Reviewer: `/root/linear_causal_sign`, GPT-6 Astra Ultra.

**Verdict:** mathematical PASS for equations (1)--(28) and their
stated consequences in `signed_born_quantitative_gain.md`. No material
correction is requested. The two weighted Born divergences and the
new full-signed energy Abel argument are supported. They prove a
divergent historical saving for the specified fixed sources, while
leaving the physical capacity-minus-demand margin unresolved.

The complete source was read in tool chunk `80259c`. Its final bytes
were hash-inspected in tool chunk `d382ef` at actual UTC time
`2026-09-05T10:25:13.406733+00:00`. This review binds to the observed
17,368-byte source with SHA-256

```
0f666e5935112ad2c58c273da44932efd9a66a15bea4385b74ef8299ec535b83
```

The companion fiber identities and error bounds have also been
independently reviewed in `signed_retirement_fibers_review.md`.
No source was edited, no numerical checker was run or rerun, and
no Lean verification is claimed.

## 1. Full signed energy, core accounting and the finite error

The raw feature is the permanent signed function g(d)=d on the
actual bank. Expanding its convolution with the old point prefix
gives diagonal N Z_N and twice the full used-pair correlation.
The exact identity is therefore

```
E_N=N Z_N+2B_N+2R_N.
```

It includes every same-birth signed pair according to its actual
Born or retirement clock. There is no positive-bank new/new
cancellation in this identity.

The six-endpoint property is constant across an entire numeric
Schur group, so the non-six complement retains full groups. Its
Born sum is nonnegative by the full signed theorem. The six
matchings of two distinct disjoint equal-sum triples give 24
Born and twelve retired records, with

```
B_fiber=4sigma_U^2+12n'^2,
B_fiber+R_fiber=6(sigma_U^2+sigma_V^2).
```

The bound sigma_V^2<=6n'^2 gives R_fiber<=2B_fiber. The
source correctly retains a possibly positive retirement term
and uses the common Born source / retirement output clock.

The repeated-triple count N^2, at most N partners per sum, and
at most twelve retired records per collision give the absolute
error `12N^3H_N^2`. Repeated slots can only cause overcounting
in this argument. Thus the full energy is bounded above by
`N Z_N+6B_N+24N^3H_N^2`, proving (8). The source does not
discard individual signed Born records to obtain this bound.

## 2. The energy moment and all good-prefix constants

For smoothing by P_N itself the signed convolution is supported
on `[a_1-H_N,a_1+2H_N]`, of integer length T_N=3H_N+1.
It has total mass zero and first moment N Z_N. Centering at
`a_1+H_N/2` gives the exact coordinate-square denominator
`T_N(T_N^2-1)/12`. The source correctly makes no claim that
the shadow vanishes at the old points.

For integer H_N>=1,

```
T_N(T_N^2-1)=27H_N^3+27H_N^2+6H_N<=60H_N^3.
```

Hence `E_N>=N^2Z_N^2/(5H_N^3)`. Combining it with (8),
the two bounds on Z_N, and the fixed cap gives exactly

```
w_N B_N >= eta^2/[30 C_cap log(2N)]
               -1/[6(N-1)]-4N/(N-1)^2.
```

The stated absolute error bound follows from
`1/[6(N-1)]<=1/(3N)` and
`4N/(N-1)^2<=16/N`, so their sum is at most 49/(3N).

The improved eta is also correct. The first p/2 points and the
last p points contribute p^2/2 distinct positive cross gaps of
size at least H_p/2. Including both signs gives
`Z_N>=p^2H_p^2/4`. Since N=2p and H_N<=32H_p, this is
at least `Q_NH_N^2/(16*32^2)`, proving eta=2^-14.
Both this choice and the weaker cited eta=2^-17 may be used,
provided the same choice is maintained in subsequent constants.

## 3. Monotone cumulative Born mass and its own Abel identity

Every full numeric Schur group's Born records appear at the same
maximum source clock. Their total is nonnegative. An old source
pair whose output appears later becomes retired, never newly
Born. These facts prove ell_b>=0 and the monotonicity of B_N.
This is monotonicity of the **Born cumulative sum**, not of the
convolution energy.

For every decreasing nonnegative c_b, telescoping gives exactly

```
sum_(b=2..T)c_b ell_b
 =c_T B_T+sum_(b=2..T-1)(c_b-c_(b+1))B_b.
```

Every term on the right is nonnegative. On a good dyadic interval
[N,2N), B_b>=B_N and `w_(2N)/w_N<1/16`. Disjointness of
these intervals therefore proves (18), retaining the original
birth price on each Born record. The lower bounds from (12)
sum to infinity because the good reciprocal-log sum diverges,
while the error sums absolutely over dyadic ranks.

The optional rate (19) has the correct coefficient:

```
(15/16)*(eta^2/(30 C_cap log 2))*(1/6)
 =eta^2/(192 C_cap log 2).
```

The condition T>=2^(J+2) includes all required good intervals
with exponent k<=J. Replacing 1/k by 1/(k+2) changes the sum
by a bounded amount. The rate is log log J in the exponent
bound J; it is not log log T. The source makes this distinction
explicitly.

## 4. The fixed complete-history tail price

For the compatible source, the coefficient difference is exactly
`u_b-u_(b+1)=kappa_b/H_b^2`. On a good interval, H_b<=H_(2N)
and B_b>=B_N. Summing kappa_b gives alpha_N-alpha_(2N),
and the lookahead H_(2N)<=32H_N yields the factor
`15/(16*32^2)` in (21). The same disjoint-interval argument
then proves divergence in (22).

The proof does not require uniform comparability u_b~w_b at
every rank. It also does not turn u_b into an online rule:
u_b depends on the fixed complete history, and its old entries
are never recomputed with a new terminal cutoff. The source
retains this quantifier boundary.

## 5. The fresh signed energy increment and its diagonal cost

Subtracting the full identity E_n=nZ_n+2B_n+2R_n at adjacent
prefixes gives

```
Delta E_n=Z_(n-1)+n v_n+2ell_n+2rho_n.
```

The retirement increment rho_n consists precisely of records
whose **output** birth is n. The diagonal coefficient is n,
not the older positive-bank coefficient n-1. This directly
verifies the newly derived Dhat_n.

The estimates on Z_(n-1) and v_n give

```
w_n Dhat_n <=(3n-2)/[n^2(n-1)]
            =1/(n-1)-1/n+2/n^2.
```

Summing proves the bound 2zeta(2)-1 in (24). Young's inequality
with the point indicator in l1 gives
`E_N<=N^2Z_N<=N^2Q_NH_N^2`, and therefore
`w_NE_N<=N/(N-1)<=2`. This uses no monotonicity of E_N.

Finite summation by parts with E_1=0 proves exactly (26).
The non-six output-stage estimate is at most
`24(n-1)^2H_n^2`, so its canonical weighted cost is at most
24/n^2. Combining this with the complete core and the nonnegative
Born remainder gives

```
R_T^out(w)<=2B_T(w)+24sum_(n=2..T)1/n^2.
```

Inserting it in the signed energy identity yields

```
A_T(w)<=6B_T(w)+50zeta(2)-49,
```

because `(2zeta(2)-1)+48(zeta(2)-1)=50zeta(2)-49`.
All prices on retired records here are output prices. A source-
clock retirement price has not been substituted.

## 6. Energy Abel divergence without energy monotonicity

On N<=n<2N, the raw label-square sums are monotone,
`Z_n>=Z_N`, and the good lookahead gives H_n<=H_(2N).
The first-moment lower bound therefore holds throughout the
window:

```
E_n>=N^2Z_N^2/(5H_(2N)^3)
    >=eta^2N^2Q_N^2H_N/(5*32^3).
```

Multiplying this uniform lower bound by the sum of nonnegative
Abel coefficients, `w_N-w_(2N)>=15w_N/16`, gives

```
3eta^2N^2/(16*32^3H_N)
 >=3eta^2/[16*32^3C_cap log(2N)],
```

which is exactly (28). The good-window contributions diverge
and the terminal boundary stays bounded. Thus the second route
to weighted Born divergence is valid without an unproved
monotonicity assumption on E_n.

## 7. Scope of the historical saving

The historical capacity identities for the fixed direct and
compatible sources identify their savings with
`lambda[trace/2+B_T(w)]` and
`lambda[trace/2+B_T(u)]`, respectively. For fixed lambda>0,
the proved divergences make these savings diverge under the one
fixed-onset capped-history hypothesis.

This strengthens an already nonnegative saving. It does not
upper-bound the remaining source capacity, compare that
capacity to all actual demands, transfer payments between the
two sources, or commute a saving through a span-masked maximum.
The unchanged physical-margin obligation is still required for
Q1. The separate potential multiset refinement is not assumed
or needed in the reviewed source; the explicit repeated error
has been retained throughout this audit.

## 8. Follow-up binding after the raw-energy monotonicity correction

2026-09-05. This is a new observation of corrected source bytes, not
a claim that the earlier review read them. The original source hash,
read times, and review text above are retained as the historical snapshot.

The current source has 17,363 bytes and SHA256

```
6e463ac1b8e24c9d950a81550b4c91bd0df18c0eb75a8aab2739d613f0628ddb
```

Its corrected passage was inspected in chunks `73f403` and `8ff09c`.
At actual UTC time `2026-09-05T11:22:55.076285+00:00`, read-only
checksum inspection in chunk `d738d4` independently verified that
reversing the author's exact passage replacement recovers the prior
reviewed SHA256 `0f666e5935112ad2c58c273da44932efd9a66a15bea4385b74ef8299ec535b83`.
There was exactly one occurrence of the replacement block. This binds
the unchanged remainder, including every equation, to the earlier review.

For exact provenance, the old block was:

```
For clarity, E_n need not be monotone. Its Abel interior nevertheless
diverges under the same good-shape assumptions, without assuming
monotonicity. On N<=n<2N, squares give Z_n>=Z_N and the actual
```

The new block is:

```
The following Abel lower-bound argument does not require monotonicity
of E_n. Its Abel interior diverges under the same good-shape assumptions.
On N<=n<2N, squares give Z_n>=Z_N and the actual
```

An initial attempted reversal omitted the change from a space to a
newline before `On N<=n<2N`; that incomplete reconstruction did not
match the prior hash. The exact replacement above does match. No
source-unchanged claim is based on the unsuccessful reconstruction.

The old aside that E_n need not be monotone is incorrect for this actual
raw signed source. The earlier review supported the inequalities and
their proof but did not flag that aside. This follow-up corrects that
scope issue explicitly. The newly independently reviewed
`signed_energy_two_sided.md`, SHA256
`1364dd87dc4290f50e3a7367500c1059519beba24eb076202c1a559c87d6dcb2`, proves

```
-B_j/4<=R_j<=2B_j,
Dhat_j+(3/2)B_j<=E_j-E_(j-1)<=Dhat_j+6B_j.
```

Since Dhat_j>0, actual E_j increases strictly. Its diagonal excess
E_j-jZ_j is nondecreasing as well. The statement in Section 3 above
distinguishing the Born cumulative sum from the convolution energy
describes the object used in that particular proof; it must not be
read as denying the newly proved energy monotonicity. Likewise the
earlier Abel proof remains valid without using that property.

**Updated verdict:** PASS for the corrected quantitative source. Its
equations (1)--(28), constants, explicit-error estimates, and divergence
conclusions are unchanged and retain their reviewed scope. The new
monotonicity theorem is analytical, not a newly executed finite check
or a Lean theorem asserted by this review. No test, replay, or Lean
command was rerun. Original Q1 and the shared physical-margin estimate
remain unresolved.
