# Independent review of the fixed signed causal source

Date: 2026-09-05. Reviewer: `/root/linear_causal_sign`, GPT-6 Astra Ultra.

Source: `signed_causal_source.md`, authored by
`/root/causal_telescoping`.

**Verdict:** the source's equations (1)--(28), including the added
(14a)--(14b), are mathematically supported within their stated scopes.
No material correction is requested. This review independently
checks the permanent source, the negative full-prefix certificate,
the distinct compatible infinite-tail source, its actual block
allocation and unused-capacity identity, the good-epoch constants,
and both capacity-divergence bounds. It does not transfer the
compatible source's future payments to the requested source or
establish the remaining global margin bound.

The complete source, including (14a)--(14b), was read in tool chunk
`4750e9`. The author then confirmed the final version. At actual
UTC observation time `2026-09-05T09:58:11.108191+00:00`, this
reviewer read the source bytes, computed their hash, and re-read the
added comparison passage in tool chunk `543c45`. The observed final
source is 17,565 bytes and 521 lines, with SHA-256

```
8806a3f6f5f5cc7964a43d34b64c014c1fddcc09182ab6db65a31da2e11d772d
```

This review binds to that version. These were source inspections,
not numerical tests. No evidence script, Lean command, or test was
run, and the reviewed source was not edited.

## 1. The requested permanent source is PSD and nonnegative

Both sequences `alpha_n=Q_n^-2` and `w_n=alpha_n/H_n^2` strictly
decrease. For a finite prefix, the coefficient at a pair with
maximum birth b in the nested-prefix decomposition is exactly

```
sum_(k=b..N-1)(c_k-c_(k+1))+c_N=c_b.
```

This verifies the PSD decompositions for V and U. Since both
signed magnitudes at birth b are at most H_b, each entry obeys
`|U_de|<=V_de`, proving `(1-lambda)V<=W<=(1+lambda)V`
entrywise for 0<=lambda<=1. These conclusions include diagonal
entries and pairs of equal source birth.

The row-centering claim for U is valid, not merely its total-mass
claim. For a fixed d of birth i, the labels with birth at most i
share coefficient w_i and have signed sum zero. Each later whole
birth class also has signed sum zero with its own fixed coefficient.
Summing a row over any complete prefix therefore gives zero.

The exact stratum identities are

```
Q_b-Q_(b-1)=2(b-1),
(Q_b^2-Q_(b-1)^2)/Q_b^2=4(1/b-1/b^2).
```

They give the source's exact mass `M_N=4(h_N^(1)-h_N^(2))`.
Also

```
1/[b^2(b-1)]=1/(b-1)-1/b-1/b^2,
```

which proves the stated trace formula and its limit. At rank two,
both V and U have trace contribution 1/2; every subsequent U
diagonal is bounded by the corresponding V diagonal. Thus
`1/2<=s_N<=t_N` and `tr W_N=t_N+lambda s_N` are correct.
The matrix mass is M_N itself, not its square.

## 2. Historical capacity uses the full signed lifetime partition

For a fixed nonnegative matrix A, the correlation at one physical
output grows with source availability until the old-output mask
switches off. Its historical maximum therefore counts precisely
the pairs with source birth b strictly less than output birth r,
including r=infinity. This proves equation (5) and all its factors.
Pairs with equal source births may have b<r and are retained.

The requested U has coefficient `w_b d e`; the reviewed signed
Schur theorem allows every nonnegative price w_b. It therefore
gives a nonnegative **full** Born sum. Combining that with the
zero mass and trace s_N gives the one saving

```
C_N(V)-C_N(W)=lambda[s_N/2+L_N(U)].
```

The source does not use the positive-bank new/new cancellation,
does not claim that every signed same-birth output is already old,
and does not repeat this one saving for each future row.

## 3. The negative full-prefix certificate is an analytic obstruction

The common signed support has length `T=L+2H_N` and contains all
m forbidden block points, so `D=T-m`. The PSD feature channels
of V have total vector mass whose squared norm is M_N. Those of
U are individually centered, with first-moment squared norm
`J_N=d^T U_N d`. Hilbert-space Cauchy therefore gives equation
(9), with denominator `T(T^2-1)` in its moment contribution.

Partitioning the ordered terms of `d^T U_N d` by maximum source
birth yields

```
J_N=sum_b w_b (Z_b^2-Z_(b-1)^2).
```

For every term in stratum b, `d^2e^2<=H_b^4`. Hence
`J_N<=H_N^2 M_N`, as stated. For m=N the actual integer block
length satisfies L>=N, so

```
D>=2H_N>=Q_N,
T(T^2-1)>=8H_N^3.
```

These yield the separate upper bounds

```
N^2 M_N/D <= N M_N/(N-1),
12lambda N^2 J_N/[T(T^2-1)] <= 3lambda N M_N/(N-1).
```

The trace is at least `(1+lambda)/2`. Substitution gives exactly
equation (11). Since M_N is logarithmic while the subtracted
trace term is linear in N, that specified certificate is eventually
negative. This conclusion needs no growth cap and is not merely
a finite numerical observation. It concerns this lower certificate;
it does not say that the actual nonnegative shadow energy is
negative or exclude all stronger demand inequalities.

## 4. PSD layer differences are not nonnegative physical layers

The kth combined layer of the requested source has PSD form
`kappa_k J+lambda(w_k-w_(k+1))d_kd_k^T`. Nevertheless, at
lambda=1 and the actual pair `{-H_k,H_k}` its entry is

```
-alpha_(k+1)[1-H_k^2/H_(k+1)^2] < 0.
```

The strict inequality follows from strict growth of the actual
diameter. Thus equation (12) correctly blocks independent physical
payment from these particular layers. PSD guarantees nonnegative
quadratic energy, but does not give a nonnegative physical
correlation kernel after the pair expansion and diagonal subtraction.

## 5. The compatible infinite-tail alternative and U minus U-prime

For the second construction,
`u_b=sum_(k>=b)kappa_k/H_k^2` is positive and at most w_b.
Each finite restriction of the infinite sum converges absolutely
entrywise, and each component is PSD and entrywise nonnegative.
Its uniform part telescopes to exactly V. This proves (13), its
mass and trace statements, and the saving (14).

The source honestly uses the complete infinite history to determine
u_b. It is a fixed compatible choice after that history is fixed,
not an online rule from P_b alone. Replacing the infinite tail by
a new normalization at successive terminal ranks would produce
different matrices and is not this construction.

For the added identity, direct subtraction gives

```
(w_k-w_(k+1))-kappa_k/H_k^2
 =alpha_(k+1)[H_k^-2-H_(k+1)^-2] >= 0.
```

Both original coefficient sequences vanish at infinity. Summing
over k>=b therefore yields w_b-u_b and proves (14a) on every
finite restriction, including its infinite tail. The difference
U-U' is PSD and centered. Its entries are
`(w_b-u_b)d e`, so the full Born theorem applies to the
nonnegative price w_b-u_b and gives (14b).

This difference is **not** entrywise nonnegative: it has negative
entries at opposite-sign sources. Thus the ordering `U>=U'` in
the PSD sense, and even the favorable historical comparison
`C_N(W)<=C_N(W')`, do not establish that W pays the future
tail demands proved for W'. The future pair sum is
`[energy-m*trace]/2`, and the extra PSD part changes both energy
and trace. Equations (14a)--(14b) do not resolve that comparison.

For the separate sign construction, the coefficients are genuinely
birth determined. At lambda=1 every positive source pair has two
reflected contributions of size `2alpha_b`, so its total physical
weight is `4alpha_b=1/q_b^2`. Opposite-sign contributions vanish.
The stated identity with the earlier positive-bank causal unit
source is therefore exact, rather than a new baseline gain.

## 6. Actual future payment and the exact unspent identity

Restricting the compatible layers k>=n to the old bank gives

```
alpha_n J +lambda u_n d_n d_n^T
 =alpha_n[J+lambda gamma_n z_nz_n^T].
```

Its mass is one and its trace is
`1/Q_n+lambda gamma_n S_n/Q_n^2`. Its complement inside W'_n
is a sum of PSD, entrywise nonnegative layers with k<n. Thus it
is a literal physical subsource. This verifies (15) and the exact
raw demands in (16).

An actual block after old rank n_i has all its difference labels
outside F_(n_i), and its differences are at most L_i-1. Its
positive-part demand is paid by the nonnegative tail kernel on
those actual differences. Pairwise disjoint difference sets ensure
each physical output is charged by at most one block. Taking the
one maximum and then enlarging the subsource gives every step
of (17), with the actual old and span masks retained.

For the unspent identity, a component-k source pair can be spent
by block i exactly when its output lies in Delta B_i and
`b<=n_i<=k`. Such an output has retirement birth
`r>n_i>=b`. Because the actual block difference sets are disjoint,
the integer p_k(e) in (18) is either zero or one. Conversely,
expanding each actual tail payment A_i counts precisely those
component pairs selected by p_k(e). Hence

```
sum_i A_i
 =sum_k kappa_k sum_(historically eligible component pairs)
                              v_k(e)p_k(e).
```

The historical capacity is the same sum with p_k(e) replaced by
one. Subtracting these and then adding the exact demand slacks
`A_i-(d_i^lambda)^+` proves (18). All summands are nonnegative,
so the infinite component tail restricted to the finite terminal
bank causes no interchange problem. Pairs whose output is not
selected, or is not used by the terminal horizon, remain in the
unspent term. This is genuine single-budget accounting; a layer
may appear in several rows but cannot be spent twice on the same
physical output.

## 7. The lookahead coefficient and demand constants are correct

Retaining terms n<=k<2n in the actual infinite tail gives

```
gamma_n >= (H_n/H_(2n))^2 [1-alpha_(2n)/alpha_n].
```

Here `Q_n/Q_(2n)=(n-1)/[2(2n-1)]<1/4`, so the squared
alpha ratio is less than 1/16. The good lookahead
`H_(2n)<=32H_n` therefore proves
`gamma_n>=15/(16*32^2)`, exactly the source's gamma_*.

The signed raw moment bound `S_n>=2^-17 Q_n`, the actual next
block length L<=32H_n, and T<=34H_n give the positive term
in (21). In its negative term, use gamma_n<=1 and S_n<=Q_n:

```
lambda gamma_n n S_n/(2Q_n^2)
 <=lambda/[2(n-1)].
```

This is the **mS** subtraction in the future tail demand. The
historical saving has not been credited to each row, so replacing
it here by `(m-1)S` would be unjustified. The source retains the
correct mS term.

The full mass-only demand after the larger trace cost is bounded
below by `n^2/(68H_n)-(1+lambda)/[2(n-1)]`. The fixed cap
makes this eventually positive, verifying (22) and the use of
positive parts. The existing good dyadic frequency theorem then
gives divergent total gain in (21), while its negative dyadic
error is summable. The future blocks at distinct selected dyadic
old ranks are actual disjoint point blocks, hence also have
disjoint physical difference sets.

## 8. Both stated historical capacities really diverge

For any finite positive F of size q, the ordered positive Schur
count A is at most `q(q-1)/2`: for the kth smallest output z,
there are at most k-1 possible first summands. The signed pair
partition counts exactly 3A used unordered pairs, including
three for each doubled relation. Subtracting from
`binom(2q,2)=2q^2-q` proves (23).

Applying that current-unused lower bound at each actual prefix
layer is valid: an output unused at that layer's prefix was not
Born when its sources became available, so the pair is included
in its later historical capacity. Summing the nonnegative layer
coefficients gives `C_N(V)>=M_N/8+t_N/4`, equation (24).

The linear-feature bound (25) also checks out. At lambda=1 only
opposite-sign pairs with both magnitudes above H/2 can have
weight less than 1/2; there are h^2 such pairs. If h<=7q/10,
removing all these potential exceptions from (23) leaves the
stated lower bound q^2/200.

If h>7q/10, there are h(h-1) same-sign high-source pairs.
Their outputs lie strictly below H/2. At most l=q-h old output
labels can occur there, and each output can be represented at
most h-1 times per sign. Thus at least
`(h-1)(3h-2q)` pairs remain unused. Since h>=2,
`h-1>=h/2>7q/20` and `3h-2q>q/10`, giving more than
`7q^2/200` unused pairs of weight at least one. The weaker
unified bound `q^2/200=Q^2/800` is therefore valid.
Linearity under the fixed current-output mask covers every
0<=lambda<=1. The q=1 exception is correctly retained.

For W', every layer k<N can be treated at its own actual prefix,
and the entire tail k>=N combines with effective parameter
lambda gamma_N in [0,1]. The omitted rank-two component has
mass at most `alpha_2 Q_2^2=1`. Equation (26) follows:
`C_N(W')>=(M_N-1)/800`. Because M_N diverges logarithmically,
both capacities are unbounded. These are lower bounds on the
unspanned fixed-source historical capacities, not on arbitrary
span-masked selected-row maxima.

## 9. The remaining margin has not been paid

Both margins in section 9 are nonnegative by the actual single-
source allocation, using lambda=0 for the background case.
Subtracting their definitions gives exactly

```
M_0-M_lambda
 =lambda[tr U'_N/2+L_N(U')]+G_N.
```

If the proposed estimate (28) held while G_N diverged, it would
contradict this identity and M_lambda>=0. It is therefore a
valid sufficient closing target. The source does not prove it.
The divergence of capacity alone is not a proof that the margin
M_0 diverges, nor a bound comparing that margin with G_N.

Finally, replacing the fixed historical capacity by the smaller
span-masked maximum in (17) would remove the hypotheses used in
the exact saving (14). A new comparison of those actual maxima
would be required. Neither full Born positivity nor the PSD
identity (14a) supplies that missing comparison or transfers
future payments from W' to W.

The review therefore supports the source's finite and conditional
supporting results, with the global margin obligation intact.
Original Q1 and any signed-source Lean formalization remain open.
