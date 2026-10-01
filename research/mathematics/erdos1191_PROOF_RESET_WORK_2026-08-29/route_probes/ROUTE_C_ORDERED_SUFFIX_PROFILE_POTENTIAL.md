# Route C: bounded chronological dyadic-suffix profile potential

Date: 2026-08-31 (Asia/Tokyo)  
Status: `HUMAN_PROOF_AUDITED_STORAGE_COLUMN_LOCAL_INEQUALITY_OPEN`

## 1. Definition

Let `n=2^L` with `L>=2`, and let `h_1,...,h_n` be the positive consecutive
gaps of one completed dyadic shell.  Put

\[
 H=\sum_{i=1}^n h_i,\qquad p_i=h_i/H,
\]

and for `1<=m<n` define the chronological suffix mass

\[
 R_m=\sum_{i=n-m+1}^{n}p_i.
\]

The centered dyadic-suffix coordinate is

\[
 C_{\rm rt}
 =\frac1L\sum_{\ell=0}^{L-1}R_{2^\ell}
  -\frac{n-1}{nL},
\tag{1.1}
\]

and the normalized storage coordinate is

\[
 V_{\rm rt}=\frac{8C_{\rm rt}+3}{11}.
\tag{1.2}
\]

Unlike the scalar C119 variance coordinate, (1.1) retains chronological
order.  It is rational on integer gaps, invariant under common dilation, and
depends only on the completed current shell.  Thus it is nonanticipating at
the shell endpoint.

## 2. Uniform range

Every suffix in (1.1) is nonempty, so `R_(2^ell)>0`.  Hence

\[
 C_{\rm rt}>-\frac{n-1}{nL}.
\]

For `n=4` the number on the right has magnitude `3/8`.  For `n>=8`,
`L>=3` and

\[
 \frac{n-1}{nL}<\frac1L\le\frac13<\frac38.
\]

Therefore `C_rt>=-3/8`.  On the other side, the largest suffix in (1.1) has
only `n/2` gaps; positivity of the omitted prefix gives
`R_(2^ell)<1` for every term.  Their average is below one and the centering
constant is positive, so `C_rt<1`.  Substitution into (1.2) gives

\[
 0\le V_{\rm rt}<1.
\tag{2.1}
\]

This is a uniform bound over all dyadic shell sizes, not a fixture-only
observation.

## 3. Exact finite Abel control

For any nonnegative decreasing weights `q_a>=...>=q_b` and any sequence
`0<=V_k<=1`, finite summation by parts gives

\[
 \sum_{k=a}^{b}q_k(V_{k+1}-V_k)
 =q_bV_{b+1}-q_aV_a
  +\sum_{k=a+1}^{b}(q_{k-1}-q_k)V_k.
\tag{3.1}
\]

The positive terms on the right total at most `q_a`, and the only negative
term has magnitude at most `q_a`.  Consequently

\[
 \left|\sum_{k=a}^{b}q_k(V_{k+1}-V_k)\right|\le q_a.
\tag{3.2}
\]

Applying (3.2) to `V_rt` proves exactly the same finite Fejer--Abel storage
bound as for C119.  In particular, for `q_k=1/(k+1)`,

\[
 \left|\sum_{k=a}^{b}
 \frac{V_{{\rm rt},k+1}-V_{{\rm rt},k}}{k+1}\right|
 \le\frac1{a+1}.
\tag{3.3}
\]

No critical-cap estimate is needed for this global bounded-telescope fact.
It still does not supply the open local C058 margin inequality.

## 4. Exact order-sensitive fixture values

Using the chronological old-shell and new-shell gaps gives:

| row | `V_rt,2` | `V_rt,3` | `Delta V_rt` |
|---|---:|---:|---:|
| C118 | `1074/2431` | `10786/18249` | `601940/4033029` |
| C120 | `20/43` | `323/1353` | `-13171/58179` |
| C123 permutation | `496/2365` | `805/2706` | `51059/581790` |

The C120 and C123 rows have the same old-gap and new-gap multisets, so the
permutation-invariant C119 scalar `Delta V` is identical on them.  Their
chronological suffix increments differ in both magnitude and sign.  Thus
`V_rt` captures load-bearing information that scalar concentration discards.

These rational values were independently recomputed directly from (1.1).
They are finite calibration, not a proof that one coefficient multiplying
`V_rt` separates every legal history.

## 5. Exact current two-column constraints

Write `C` for the coefficient of `V_rt`.  Under the finite calibration
assumptions `epsilon,A>=0` and `e_2=0`, the registered C118, C120, and C123
dual rows yield exact rational half-planes in `(B,C)`.  At the most permissive
choice `epsilon=A=0`, the clean C118 and C123 scalar restrictions reduce to

`B>1341/4000` and `B<4753/10000` when `C=0`.

The current three-row system has not been proved infeasible.  Two further
same-model permutations, with opposite or near-zero `Delta V_rt`, are the
minimal exact additions before solving the rational outer LP.  Positive
`e_2` would relax these finite rows, so an `e_2=0` contradiction would still
be only a calibration gate, not the asymptotic theorem.

## 6. Remaining phase and ownership gates

The phase base used by C120/C123 is adaptive and changes under some
same-multiset permutations.  The nonanticipating C103/C116 scale rule must be
frozen, or representative independence must be proved, before the resulting
coefficient bank can be used as a theorem statement.

After that, any surviving `(B,C)` vector must pass 32-mark or scalable
critical-compatible histories and be embedded in one global ledger assigning
all C103 initial, final, interior, birth, cutoff, shared-endpoint, and
scale-terminal rows exactly once.  The local signed transport/master
inequality remains C058, the sole primary bottleneck.  Q1, Q2, novelty, and
prize eligibility remain unresolved, and the global status stays
`UNRESOLVED_AT_HARD_LIMIT`.

## 7. C125 five-row bank outcome

Two further ordered permutations with
`Delta V_rt=113/26445` and `-12913/58179` have been exactified.  The resulting
five-row bank does not refute the chronological suffix column: the rational
vector `epsilon=A=1/1000`, `B=1/2`, `C=1/10`, `e_2=0` lies below every stored
dual upper by more than `1/10000`.

This is necessary-side survival only.  No primal construction proves the
local inequality for that vector.  The next clean diagnostic fixes one
permutation-invariant phase for C120/C123 before deciding whether to construct
primals or add the ordered quarter-mass vector.
