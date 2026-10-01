# Route C: critical span potential and good-window supply

Date: 2026-08-30  
Status: `HUMAN_PROOF_AUDITED_INPUT_FOR_C058_LOCAL_INEQUALITY`

This note proves two history-sensitive facts forced by the Sidon and
eventual-critical hypotheses.  The first gives the exact signed potential
whose Fejér-weighted increments telescope.  The second supplies linearly many
bounded-geometry 16-mark windows in every sufficiently large new shell.

Neither fact proves that the aggregate PSD margin is controlled by the
potential or localizes the C112 master to those windows.  Those are the new
C058 obligations.

All logarithms below are natural.

## 1. Dyadic span potential

Let

\[
 \mathcal N_k:=N_{2^k}=a_{2^k-1}+1,
 \qquad
 x_k:=\log\frac{\mathcal N_k}{4^k},
\]

and

\[
 \delta_k:=x_{k+1}-x_k
 =\log\frac{\mathcal N_{k+1}}{4\mathcal N_k}.
\]

Here `N_m` is the full `m`-mark prefix span plus one.  It is not the shell
span `H'_n=N_{2n}-N_n`.

Distinct positive differences give

\[
 \mathcal N_k\ge1+\binom{2^k}{2}\ge4^{k-1},
\]

so

\[
 x_k\ge-\log4.
\tag{1.1}
\]

Under the eventual-`C` cap,

\[
 \mathcal N_k\le C4^k\log(2^{k+1})
 =C4^k(k+1)\log2,
\]

and therefore

\[
 x_k\le\log(C(k+1)\log2).
\tag{1.2}
\]

## 2. Exact Fejér Abel identity

For `J>=K>=k_0>=1`, put

\[
 \omega_{k,J}=\left(\frac{J+1-k}{J+1}\right)^2,
 \qquad
 p_{k,J}=\frac{\omega_{k,J}}{k+1}.
\]

Finite summation by parts gives exactly

\[
\begin{aligned}
 \sum_{k=k_0}^{K}p_{k,J}\delta_k
={}&p_{K,J}x_{K+1}-p_{k_0,J}x_{k_0}\\
 &+\sum_{k=k_0+1}^{K}
 (p_{k-1,J}-p_{k,J})x_k.
\end{aligned}
\tag{2.1}
\]

Set

\[
 y_k=x_k+\log4,qquad
 A_0=\max(0,\log(4C\log2)).
\]

Then `0<=y_k<=A_0+log(k+1)`.  The sequence `p_{k,J}` is decreasing and

\[
 p_{k-1,J}-p_{k,J}
 ={\omega_{k-1,J}-\omega_{k,J}\over k}
 +{\omega_{k,J}\over k(k+1)}
 \le {4\over k^2}.
\tag{2.2}
\]

Shifting `x` to `y` leaves the left side of (2.1) unchanged.  The two endpoint
contributions together are at most `A_0+1` in absolute value, while

\[
 \sum_{k=k_0+1}^{K}
 (p_{k-1,J}-p_{k,J})y_k
 <8A_0+12.
\]

Consequently the explicit uniform estimate

\[
 \boxed{
 \left|\sum_{k=k_0}^{K}p_{k,J}\delta_k\right|
 <13+9A_0
 }
\tag{2.3}
\]

holds whenever the cap is valid through `K+1`.  The bound is independent of
`J` and `K`.  If `K=J-3`, the final endpoint is in fact
`O_C(log J/J^3)` because `omega_{J-3,J}=16/(J+1)^2`.

The usual Fejér harmonic estimate also gives

\[
 \sum_{k=k_0}^{J-3}p_{k,J}=\log J+O_{k_0}(1).
\tag{2.4}
\]

### Shell-span version

The same argument applies directly to the Wave shell span

\[
 H_k:=N_{2^{k+1}}-N_{2^k}
 =a_{2^{k+1}-1}-a_{2^k-1}.
\]

It is the sum of `2^k` distinct positive adjacent gaps, so

\[
 {4^k\over2}\le H_k
 \le4C4^k(k+2)\log2.
\]

Thus

\[
 z_k=\log(H_k/4^k),\qquad
 \eta_k=z_{k+1}-z_k
 =\log{H_{k+1}\over4H_k}
\]

has the same signed Fejér telescope:

\[
 \sum_{k=k_0}^{K}p_{k,J}\eta_k=O_C(1)
\tag{2.5}
\]

uniformly in the finite horizon.  Repeating (2.1)--(2.3) with
`z_k+log2` and `A_1=max(0,log(8C log2))` gives, for example, the safe explicit
bound `13+9A_1` after the harmless index shift in `log(k+2)`.

This version is geometrically preferable: `H_k` is exactly the full shell
span already present in the Gothic and terminal formulae.

## 3. Exact form of the missing local lemma

It is now enough to prove, for an explicit `epsilon_C>0` and `A_C<infinity`,
a phase-integrated legal owner-master bound of the form

\[
 \Phi_k
 \ge {\epsilon_C\over k+1}
 -{A_C\delta_k\over k+1}
 -e_k,
\tag{3.1}
\]

with Fejér-weighted `sum e_k=O_C(1)`.  Multiplying (3.1) by `omega_{k,J}` and
using (2.3)--(2.4) yields

\[
 \sum_k\omega_{k,J}\Phi_k
 \ge\epsilon_C\log J-O_C(1).
\]

For masters pairing `(k,k+1)`, the same proof is applied separately on the
two parities with `x_{k+2}-x_k` in place of `delta_k`.

The more geometry-aligned target replaces `delta_k` in (3.1) by
`eta_k=log(H_(k+1)/(4H_k))` and invokes (2.5).  The missing task is not the
scalar telescope; it is realizing this signed shell-span increment through
the actual cutoff, final, and scale-terminal owner rows.

Equation (3.1), including the legal global owner map and all C103 boundary
rows, is not proved here.

## 4. Why positive-part charging is insufficient

The scalar sequence

\[
 \mathcal N_k=
 \begin{cases}
 4^k,&k\text{ even},\\
 2\,4^k,&k\text{ odd}
 \end{cases}
\]

is strictly increasing: consecutive ratios alternate between `8` and `2`.
It obeys the Sidon-count scalar lower bound and every fixed eventual-`C` upper
cap.  Its increments alternate between `+log2` and `-log2`.  Hence

\[
 \sum_kp_{k,J}(\delta_k)_+
 ={\log2\over2}\log J+O(1),
\]

and the same is true for the negative variation.  Only the signed sum
telescopes.

This abstract span sequence is not claimed to be realized by a Sidon ray.  It
proves that the scalar lower/upper span bounds alone cannot justify replacing
`delta_k` in (3.1) by its positive part.  Any such stronger charge needs new
Golomb geometry.

## 5. Good 16-mark windows in a critical shell

First use the scale already selected by the centered critical schedule:

\[
 q_n=\operatorname{ceilpow2}(8C\log(4n)),
 \qquad T_n=2nq_n.
\]

The cap gives `H/T_n<=n/4`.  For the consecutive 15-gap window spans

\[
 W_r=\sum_{i=r}^{r+14}h_i,
\]

each shell gap occurs in at most 15 windows, whence

\[
 \sum_rW_r\le15H.
\]

For every `beta>0`, the number of windows with `W_r>beta T_n` is less than
`15n/(4 beta)`.  At `beta=8`, more than

\[
 {17n\over32}-14
\tag{5.1}
\]

translated 16-mark subrulers have span at most `8T_n`.  Choosing the largest
residue class of starting ranks modulo 16 leaves at least one sixteenth of
these windows pairwise mark-disjoint.  Moreover `T_(2n)/T_n` is `2` or `4`.

This exact containment uses the existing nonanticipating schedule, but its
normalized shape simplex still permits gaps tending to zero.

### Refined two-sided gap filter

Let

\[
 H=N_{2n}-N_n=\sum_{r=n}^{2n-1}h_r
\]

be the span of the `n` new gaps.  Choose

\[
 T\ge {120H\over n}.
\]

Adjacent gaps are distinct positive integers.  Therefore fewer than `n/60`
of them are below `n/60`.  Markov's inequality gives fewer than `n/60` gaps
above `T/2`.  Call both classes exceptional.

There are `n-14` consecutive 15-gap windows.  One exceptional gap belongs to
at most 15 of them, so at least

\[
 {n\over2}-14
\tag{5.2}
\]

windows have every gap in

\[
 [n/60,T/2]
\]

and total 15-gap span below `15T/2<8T`.  Greedy interval selection gives a
positive absolute multiple of `n` pairwise disjoint good windows.

Under the critical cap,

\[
 H\le4Cn^2\log(4n),
\]

so the deterministic dyadic choice

\[
 T_n=\operatorname{ceilpow2}(480Cn\log(4n))
\]

works, and

\[
 T_{2n}/T_n\in\{2,4\}.
\]

Every good normalized gap is at least

\[
 {1\over57600C\log(4n)}
\]

and at most `1/2`, while its 16-mark window has span below `8T_n`.

This does not freeze the affine chamber shape and does not make a local
16-mark window an `n=4,8` owner block inside the global Wave-19 matrix.  A new
localization/ownership theorem is required before the C112 master can be
placed on these windows.

## 6. Claim boundary

The signed prefix/shell span potentials (2.3), (2.5) and the good-window
supplies (5.1), (5.2) are rigorous inputs.  The load-bearing inequality (3.1),
localization of the fixed-phase master, control of degenerate normalized
window shapes, arbitrary dyadic-size construction, and one-time global
endpoint and terminal ownership remain open.  C058, Q1, Q2, novelty,
publication, and prize eligibility remain unresolved.
