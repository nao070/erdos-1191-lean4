# Wave 19 P28: exact `Gmix` self-cancellation no-go

Date: 2026-08-29  
Status: **HUMAN_PROOF_AUDITED + exact Fraction certificate; bare-`Gmix`
route closed, P28 and Erdős #1191 unresolved**

## 1. Exact claim and narrow boundary

Let `n` be an integer epoch and use the cut-valid mixed transport

\[
 t={8t^0+t^R\over9}
\]

from the mixed right-greedy audit.  For every `n>=2048`, the already-defined
functional

\[
 \mathcal G_n^{\rm mix}
 =R_n+P_n^{\rm coef}\log A-K_n^{\rm int}-\mathcal T_n
 -\Theta_n^{\rm full}-{1\over3}\mathcal D_n^{\rm pre}
\]

satisfies the strict finite-prefix inequality

\[
 \boxed{\mathcal G_n^{\rm mix}>{1\over2}Y_n+{1\over40}.}
\tag{1.1}
\]

Consequently, for every fixed integer `k_0>=11`,

\[
 \sum_{k=k_0}^{J}\omega_{k,J}\mathcal G_{2^k}^{\rm mix}
 >{J\over120}+O_{k_0}(1),
 \qquad
 \omega_{k,J}=\left({J+1-k\over J+1}\right)^2,
\tag{1.2}
\]

and, once `J+1>=2k_0`, the explicit bound

\[
 \boxed{
 \sum_{k=k_0}^{J}\omega_{k,J}\mathcal G_{2^k}^{\rm mix}
 \ge {J\over960}}
\tag{1.3}
\]

holds.  Thus the normalized weighted functional tends to `+infinity`, not to
a number below `1/(3072C log 2)`.

This closes only the **bare `Gmix` upper target as a standalone method**.  It
does not prove that an eventual-`C` infinite branch exists, does not disprove
Question 1, and does not prove Question 1, Question 2, P28, novelty, or any
prize claim.

## 2. Imported proved identities and inequalities

The proof uses the following already-audited statements.  They hold for every
integer Golomb prefix in their stated ranges.

1. The mixed transport is feasible for every `n>=4` and obeys

   \[
   S_{t,n}\le {1\over2}Y_n,
   \qquad
   E_{t,n}^{\rm rank}\le {2\over3}\mathcal D_n^{\rm pre}.
   \tag{2.1}
   \]

2. With the actual-rank split,

   \[
   Q_n^{\rm ad}:=\mathcal S_n^{\rm rank}+S_{t,n}
   +E_{t,n}^{\rm rank}-\Theta_n^{\rm exc}\ge0.
   \tag{2.2}
   \]

3. The pairing slack and birth energy are nonnegative:

   \[
   \mathcal P_n^{\rm pair}\ge0,\qquad Y_n\ge0.
   \tag{2.3}
   \]

4. The hostile rewrite and the cap split are exact:

   \[
   \mathcal G_n^{\rm mix}
   =Y_n+D_n+\mathcal S_n^{\rm rank}+\mathcal P_n^{\rm pair}
   -\Theta_n^{\rm full}+{2\over3}\mathcal D_n^{\rm pre},
   \qquad
   \Theta_n^{\rm full}=\Theta_n^{\rm cap}+\Theta_n^{\rm exc}.
   \tag{2.4}
   \]

No item above assigns a new owner.  In particular, (2.4) is a numerical
identity, not permission to spend a bracket that was dropped earlier.

## 3. The exact five-slack identity

Subtract `Y_n/2` from (2.4), insert `-S_{t,n}+S_{t,n}` and
`-E_{t,n}^{rank}+E_{t,n}^{rank}`, and use (2.2).  Coefficient by coefficient,

\[
\begin{aligned}
 \mathcal G_n^{\rm mix}-{1\over2}Y_n
 ={}&\left({1\over2}Y_n-S_{t,n}\right)
 +(D_n-\Theta_n^{\rm cap})
 +\mathcal P_n^{\rm pair}\\
 &+Q_n^{\rm ad}
 +\left({2\over3}\mathcal D_n^{\rm pre}
              -E_{t,n}^{\rm rank}\right).
\end{aligned}
\tag{3.1}
\]

The certificate checks (3.1) in the literal formal basis

```text
D, Dpre, Pair, Srank, S_t, E_rank, ThetaCap, ThetaExc, Y.
```

The coefficient vector on both sides after cancellation is exactly

```text
D:1, Dpre:2/3, Pair:1, Srank:1,
ThetaCap:-1, ThetaExc:-1, Y:1/2.
```

The first, third, fourth, and fifth summands in (3.1) are nonnegative by
(2.1)--(2.3).  The second summand has a uniform strictly positive floor.

## 4. Exact current-cap gap from epoch 2048

The adaptive-cap theorem gives the current-index bound

\[
 \Theta_n^{\rm cap}\le\mathcal C_n^{\rm det}
 <b+{a\over n},
 \qquad
 b={8336738101\over10^{10}},\quad
 a={3009853\over10^7}.
\tag{4.1}
\]

Wave 17 gives

\[
 D_n\ge f(n):=\delta_0-{18(1+\log n)\over n},
 \qquad
 \delta_0={3\over2}+{3\over4}\log3-2\log2.
\tag{4.2}
\]

The positive atanh series with a rational tail bound proves, independently
of floating point,

\[
 \log2<{693147181\over10^9},
 \qquad
 \log3>{1098612288\over10^9}.
\tag{4.3}
\]

Using these deliberately coarse rational bounds at `n=2048` gives

\[
 f(2048)-\left(b+{a\over2048}\right)
 >{143573826923\over5120000000000}
 ={1\over40}
  +{15573826923\over5120000000000}
 >{1\over40}.
\tag{4.4}
\]

For real `n>1`,

\[
 f'(n)={18\log n\over n^2}>0,
 \qquad
 \left(b+{a\over n}\right)'=-{a\over n^2}<0.
\tag{4.5}
\]

Therefore (4.4) propagates to every integer `n>=2048`, and the strict cap
inequality in (4.1) yields

\[
 \boxed{D_n-\Theta_n^{\rm cap}>{1\over40}.}
\tag{4.6}
\]

For comparison, the preceding cap used in the unreindexed ledger satisfies
`Theta_(n/2)^cap<b+2a/n`; the same independent onset calculation leaves

\[
 {142821363673\over5120000000000}>{1\over40}.
\tag{4.7}
\]

Thus neither the current nor the preceding rank-cap surplus is small.  This
is a structural obstruction, not a numerical threshold accident.

Combining (3.1), (4.6), and the four nonnegative terms proves (1.1).

## 5. Exact Fejér lower bound

Fix `k_0>=11` and put `M=J+1-k_0`.  Directly reindexing the squares gives

\[
 \sum_{k=k_0}^{J}\omega_{k,J}
 ={1\over(J+1)^2}\sum_{r=1}^{M}r^2
 ={M(M+1)(2M+1)\over6(J+1)^2}
 ={J\over3}+O_{k_0}(1).
\tag{5.1}
\]

Since `Y_(2^k)>=0`, (1.1) and (5.1) imply (1.2).  If
`J+1>=2k_0`, then `M>=(J+1)/2`, and

\[
 \sum_{r=1}^{M}r^2\ge {M^3\over3}
 \ge{(J+1)^3\over24}.
\]

Hence the weight sum is at least `(J+1)/24>J/24`, proving (1.3).  In
particular,

\[
 \lim_{J\to\infty}
 {\sum_{k=k_0}^{J}\omega_{k,J}\mathcal G_{2^k}^{\rm mix}
  \over\log J}=+\infty.
\tag{5.2}
\]

Because `Gmix_(2^k)>1/40` for `k>=11`, replacing it by its positive part does
not alter this eventual lower bound.  Both the old strict-threshold target
and its stronger positive-part `o(log J)` form are therefore impossible on
any extant branch.

The quantifier matters: if Question 1 is true, the class of eventual-`C`
branches is empty.  Equation (5.2) says that **conditional on such a branch,
bare `Gmix` cannot be the small functional used to contradict it**.  It does
not establish whether that class is empty.

## 6. What survives when the old bracket is retained

Before the one-step cap reindexing, define the diagnostic quantity obtained
by replacing `Theta_n^cap` with `Theta_(n/2)^cap` in (2.4).  The same literal
coefficient calculation gives

\[
\begin{aligned}
 \mathcal G_n^{\rm pre}-{1\over2}Y_n
 ={}&\left({1\over2}Y_n-S_{t,n}\right)
 +(D_n-\Theta_{n/2}^{\rm cap})
 +\mathcal P_n^{\rm pair}+Q_n^{\rm ad}\\
 &+\left({2\over3}\mathcal D_n^{\rm pre}
              -E_{t,n}^{\rm rank}\right).
\end{aligned}
\tag{6.1}
\]

The original exact ledger owns

\[
 H_n^{\rm old}:=(D_n-\Theta_{n/2}^{\rm cap})
                  +\mathcal P_n^{\rm pair}+Q_n^{\rm ad}
\]

once, with favorable negative sign.  Retaining that bracket rather than
dropping it removes precisely the middle three terms of (6.1), but it leaves

\[
 \boxed{
 X_n+P_n:=\left({1\over2}Y_n-S_{t,n}\right)
 +\left({2\over3}\mathcal D_n^{\rm pre}
              -E_{t,n}^{\rm rank}\right)\ge0.}
\tag{6.2}
\]

This is the smallest honest residual exposed by the present algebra.  Calling
`X_n+P_n` by another name is G0.  A next route must supply a separately owned
negative cross-scale carrier for (6.2), prove a genuine atomwise premium, or
change the global architecture.  `D-ThetaCap`, `Pair`, `Qad`, raw `v`, and the
already used endpoint/cross bounds cannot be counted a second time.

## 7. Progress grade and route disposition

The result is graded **G2, route-obligation closure**:

- it proves a uniform asymptotic-order obstruction to the proposed bare
  functional;
- it closes the strict-threshold and positive-part `Gmix` programs;
- it does not provide sublogarithmic control or a new contradiction, so it is
  not G3;
- it does not resolve either Erdős question, so it is not G4.

The kill rule is immediate: any Route A/B proposal whose claimed remainder is
algebraically (6.2), or (6.2) plus already dropped nonnegative slacks, receives
G0 and is not promoted.  Any proposal that borrows the terminal fan, raw `v`,
or future capacity without a signed finite-horizon potential is rejected for
ownership or horizon failure.

## 8. Reproducible certificate

The companion artifacts are:

- `wave19_p28_gmix_no_go_certificate.py`;
- `test_wave19_p28_gmix_no_go_certificate.py`;
- `wave19_p28_gmix_no_go_certificate_2026-08-29.json`.

They audit the nine formal basis coefficients, all five slack terms, the
current and preceding onset margins, dyadic monotonicity probes, exact Fejér
sums, adversarial coefficient mutations, invalid domains, scope flags,
self-hash, and deterministic byte replay.  Every proof comparison is a
`fractions.Fraction`; decimal projections are not used as theorem evidence.

Focused verification commands:

```bash
PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider \
  test_wave19_p28_gmix_no_go_certificate.py
ruff check wave19_p28_gmix_no_go_certificate.py \
  test_wave19_p28_gmix_no_go_certificate.py
python -m py_compile wave19_p28_gmix_no_go_certificate.py \
  test_wave19_p28_gmix_no_go_certificate.py
python wave19_p28_gmix_no_go_certificate.py --output /tmp/gmix-a.json
python wave19_p28_gmix_no_go_certificate.py --output /tmp/gmix-b.json
cmp /tmp/gmix-a.json /tmp/gmix-b.json
```

These are finite algebra and rational-envelope checks supporting the proof
above.  They are not a computation-only extrapolation to an infinite branch.
