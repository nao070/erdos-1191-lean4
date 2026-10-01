# Prefix logarithmic energy: exact split, Wave sign, and relaxation countermodel

Date: 2026-09-05. Status: **exact identities and an obstruction to one proposed
use of Sidon uniqueness; Q1 remains unresolved**.

The tested route replaces all positive-difference uniqueness at a prefix by
the single lower bound that their logarithmic sum is at least the logarithm
of a factorial, combines it with the critical cap, and retains the exact
old/new/cross split. These ingredients are insufficient: an explicit
non-Sidon integer ruler satisfies all of them from one fixed onset, while
its Wave mass stays bounded below at every large epoch. The obstruction
does not rule out using additional arithmetic information about the actual
differences, or stronger subset/transport inequalities.

## 1. Definitions and the exact dyadic split

For an increasing integer ruler `a_0<a_1<...`, write

\[
 L_n=\sum_{0\le i<j<n}\log(a_j-a_i),\qquad
 E_n={L_n\over n^2}-\log n.
 \tag{1}
\]

At a fixed split, let `A={a_0,...,a_(n−1)}` and
`B={a_n,...,a_(2n−1)}`. Let `L_B` be the unweighted pair-log sum inside `B`
and define

\[
 E_B={L_B\over n^2}-\log n,\qquad
 X_n=\sum_{0\le i<n\le j<2n}\log(a_j-a_i),\qquad
 F_n={X_n\over n^2}-2\log n.
\]

Partitioning the pairs, without an estimate or omitted cross term, gives

\[
 L_{2n}=L_n+L_B+X_n,
 \qquad
 \boxed{4E_{2n}=E_n+E_B+F_n-4\log2.}
 \tag{2}
\]

The subtraction `log n` in (1) is retained literally. Replacing the number
of pairs by `n²/2` before deriving (2) would conceal finite normalization
terms.

## 2. What Sidon uniqueness and the critical cap actually give

Let `m_n=n(n−1)/2`. If the ruler is Sidon, its `m_n` positive differences
are distinct positive integers. Sorting them therefore proves

\[
 L_n\ge\log(m_n!),\qquad
 E_n\ge-{1+\log2\over2}-O(\log n/n).
 \tag{3}
\]

Suppose the prefix diameter satisfies
`a_(n−1)−a_0≤C n² log(2n)` from one fixed onset. Bounding each logarithm
above by the logarithm of this diameter gives

\[
 E_n\le {n-1\over2n}\log(Cn^2\log(2n))-\log n
       ={1\over2}\log\log n+{1\over2}\log C+o(1).
 \tag{4}
\]

The one-sided distinction matters: (3) has only a constant leading lower
bound; (4) is an upper bound growing like `log log n`. A term `−E_n` can use
(3) for an upper estimate, but cannot use (4) in that direction.

On dyadic ranks `n=2^k`, these bounds imply
`−O(1)≤E_(2^k)≤(1/2)log(k+1)+O_C(1)`. The C115 weighted Abel argument
therefore controls signed increments of this energy when they are weighted
by `omega_(k,J)/(k+1)`. It does not establish a comparison of those
increments to `W_(2^k)`.

## 3. Exact appearance of the rank-weighted Wave mass

The Wave epoch at `n` uses the `n+1` points

\[
 b_j=a_{n-1+j}\quad(0\le j\le n),\qquad
 h_i=b_{i+1}-b_i\quad(0\le i<n),\qquad H=b_n-b_0.
\]

Thus the old/new shared point is `b_0`, while the new half in (2) is
`B={b_1,...,b_n}`. Let `M_n=D^T B_n D` be the literal C143 matrix with
gap coefficient `−(i−j)²/(8n²)` at separations at least two and zero
otherwise. The existing cross-ratio expansion gives

\[
 W_n=-2\sum_{0\le i<j\le n}(M_n)_{ij}\log(b_j-b_i).
 \tag{5}
\]

Define the boundary logarithmic sum and adjacent correction

\[
 T_n=\sum_{j=1}^{n-1}
 \bigl[(2j-1)\log(b_j-b_0)
 +(2(n-j)+1)\log(b_n-b_j)\bigr],
 \tag{6}
\]

\[
 R_n={1\over4n^2}\sum_{i=0}^{n-2}
           \log{h_i+h_{i+1}\over h_i h_{i+1}},\qquad
 A_n={T_n-(n-1)^2\log H\over2n^2}-\log n.
 \tag{7}
\]

Direct mixed differencing of the quadratic gap coefficients yields

\[
 \boxed{4n^2W_n=T_n-(n-1)^2\log H-2L_B+4n^2R_n,}
 \tag{8}
\]

and hence

\[
 \boxed{E_B=A_n-2W_n+2R_n.}
 \tag{9}
\]

For clarity, the logarithmic coefficient identity underlying (8) is
entirely finite. In `4n²W_n`, the main terms have coefficients
`2j−1` on `(b_j−b_0)`, `2(n−j)+1` on `(b_n−b_j)`,
`−(n−1)²` on `H`, and `−2` on each pair of `B`. The correction adds `+1`
on every two-gap span and `−1` on each of its two constituent gaps. These
coefficients equal `−8n²(M_n)_(ij)` individually.

An exact Fraction/integer comparison against the literal `point_matrix(n)`
checked every pair coefficient for all `3≤n≤32`, with exit code zero.
This is a sanity check; mixed differencing proves the displayed identity
at arbitrary rank.

Substituting (9) into the complete split (2) gives the requested
opposite-sign occurrence of `W_n`:

\[
 \boxed{2W_n=E_n-4E_{2n}+A_n+F_n-4\log2+2R_n.}
 \tag{10}
\]

It is an identity, not yet a capacity inequality.

### The adjacent term is harmless; the large coefficients are not

For integer positive gaps,
`1/H≤(h_i+h_(i+1))/(h_i h_(i+1))≤2`. Thus

\[
 |R_n|\le {n-1\over4n^2}\max(\log H,\log2),
\]

which is summable on a critical-cap dyadic tower. On the other hand,
the total coefficient of the logs in `T_n` is `2n(n−1)`, so simply bounding
them by `log H` gives

\[
 A_n\le {n^2-1\over2n^2}\log H-\log n
       \le {1\over2}\log\log n+O_C(1).
 \tag{11}
\]

Similarly `F_n≤log log n+O_C(1)`. To upper-bound (10), the negative term
`−4E_(2n)` needs a lower bound. The factorial estimate (3) does not cancel
the `log log n` allowed by (11) and the cross term. Subtracting their
matching *upper* asymptotics would be an invalid sign reversal.

There is also no ordinary telescope in `E_n−4E_(2n)`. If `E_k` temporarily
denotes `E_(2^k)`, then exactly

\[
 \sum_{k=a}^b\omega_k(E_k-4E_{k+1})
 =\omega_aE_a-4\omega_bE_{b+1}
 +\sum_{k=a+1}^b(\omega_k-4\omega_{k-1})E_k.
 \tag{12}
\]

The interior coefficient is approximately `−3omega_k`, not a small Abel
increment. Renormalizing by `4^−k` would telescope, but it would also make
the original harmonic Wave sector summable and lose the intended signal.

## 4. Smooth capped rulers retain the logarithmic excess

Fix `gamma>0` and let
`f(j)=gamma j² log j` for large positive integer `j`. Consider first
`s_j=ceil(f(j))`, with any fixed initial increasing segment. Then

\[
 \boxed{E_n={1\over2}\log\log n+{1\over2}\log\gamma
              +\log2-{3\over2}+o(1).}
 \tag{13}
\]

This confirms the proposed constant without ignoring the logarithmic
singularity near equal indices.

**Proof.** For `0≤i<j`, ignoring a fixed initial segment,

\[
 (j^2-i^2)\log j
 \le j^2\log j-i^2\log i
 \le(j^2-i^2)(\log j+1/2).
 \tag{14}
\]

The upper bound uses `i² log(j/i)≤(j²−i²)/2`. Rounding contributes an
asymptotically negligible total logarithmic error. Thus the pair logarithm
equals `log gamma+log(j²−i²)+log log j+O(1/log j)` uniformly for large `j`.

The singular-looking part has an exact product evaluation:

\[
 \prod_{i=0}^{j-1}(j^2-i^2)=j(2j-1)!.
 \tag{15}
\]

Stirling's estimate summed over `j<n` consequently gives

\[
 {1\over n^2}\sum_{i<j<n}\log(j^2-i^2)
 =\log n+\log2-{3\over2}+O(\log n/n).
 \tag{16}
\]

Also `n^−2 Σ_(j<n) j log log j=(1/2)log log n+o(1)` and
`n^−2 Σ_(j<n) j/log j=o(1)`. These prove (13). Equivalently the continuum
constant is
`∫_(0<x<y<1)log(y²−x²) dxdy=log2−3/2`; (15) handles its singular boundary
directly rather than assuming bounded Riemann integrands. ∎

### Keeping the cross block does not remove that excess

On the same smooth sequence, the three block quantities have the exact
leading forms

\[
\begin{aligned}
 E_n&={1\over2}\log\log n+{1\over2}\log\gamma+I+o(1),\\
 E_B&={1\over2}\log\log n+{1\over2}\log\gamma+B+o(1),\\
 F_n&=\log\log n+\log\gamma+C+o(1),
\end{aligned}
 \tag{17}
\]

where

\[
 I=\log2-3/2,\qquad
 B=9\log2-(9/2)\log3-3/2,\qquad
 C=(9/2)\log3-2\log2-3.
 \tag{18}
\]

Here `B=∫_(1<x<y<2)log(y²−x²) dxdy` and
`C=∫_(0<x<1<y<2)log(y²−x²) dxdy`. They can be evaluated by splitting
`log(y²−x²)=log(y−x)+log(y+x)`; the first part has the usual integrable
diagonal singularity. Equation (15), or the same factorial products on
subintervals, justifies the corresponding sum asymptotics.

The identity `I+B+C=8 log2−6=4I+4 log2` makes (17) satisfy (2) exactly to
leading order. In particular, the `1/2 log log n` of `E_(2n)` survives the
full cross-block identity. No cross term was dropped to produce it.

The independent reviewer supplied explicit product identities for both
subblocks, so no singular Riemann-limit assertion is needed there either:

\[
 \prod_{i=n}^{j-1}(j^2-i^2)
 ={(j-n)!(2j-1)!\over(j+n-1)!},\qquad
 \prod_{i=0}^{n-1}(j^2-i^2)
 ={j(j+n-1)!\over(j-n)!}\quad(j\ge n).
 \tag{18a}
\]

Applying the same Stirling bounds to these finite products gives the
constants `B,C` in (18), with the rounding and slowly varying `log log j`
errors already controlled as in (14)--(16).

## 5. A nonvanishing Wave mass in the same relaxation

For the smooth shell at ranks `n,...,2n−1`,

\[
 \boxed{W_n\longrightarrow
 w_*:=\int_{1<x<y<2}{xy\over(x+y)^2}\,dx\,dy
 ={9\log2-5\log3\over2}-{1\over4}
 \approx0.12263159>0.}
 \tag{19}
\]

To justify the limit, the shell gaps are uniformly comparable to `n log n`.
For separation `d≥2`, `log(1+u v/(M(M+u+v)))≤u v/M²` bounds each weighted
primitive by `K/n²`, with one constant `K` on the shell. The contribution
from `d≤delta n` is therefore `O(delta)`. Away from that diagonal strip,
the normalized function `f(nx)/(n² log n)` and its derivative converge
uniformly to `gamma x²` and `2 gamma x`, so each rescaled primitive tends
uniformly to `xy/(x+y)²`. Ordinary Riemann summation there, followed by
`delta→0`, proves (19). Rounding has no effect on these uniform estimates.

For an elementary evaluation of the last integral, integrating first in
`x` gives
`y log(2y/(y+1))−y/2+y/(y+1)`. Its integral from `1` to `2` is the
displayed value. The integrand is at least `2/9` on the triangular domain,
so strict positivity requires no decimal estimate.

## 6. A fully explicit non-Sidon countermodel to the factorial relaxation

One should not assert Sidon or non-Sidon status of the unmodified rounded
smooth sequence without proof. A controlled perturbation makes the latter
status explicit while preserving every asymptotic above.

For each sufficiently large integer `r`, set

\[
 t_r=\lceil f(3r)\rceil,\qquad
 d_r=\left\lceil{f(3r+2)-f(3r)\over2}\right\rceil,
\]

and define

\[
 a_{3r}=t_r,\quad a_{3r+1}=t_r+d_r,\quad a_{3r+2}=t_r+2d_r.
 \tag{20}
\]

Choose an arbitrary fixed increasing initial segment below the first such
block. The ruler is eventually strictly increasing between blocks because
`f(j+1)−f(j)` is of order `j log j`, while the rounding errors at block ends
are bounded. Within every block it contains a nontrivial three-term
arithmetic progression, so every tail has repeated positive differences and
is **not Sidon**.

Taylor's formula gives `a_j=f(j)+O(log j)`; at the middle of a block the
error is controlled by `f''(j)=O(log j)`. These errors preserve (13),
(17), and (19). For example, for `i≥j/2` the relative change in a pair
difference is `O(1/(j(j−i)))`; for `i<j/2` it is `O(1/j²)`. Summing their
logarithmic errors contributes `O(log² n)=o(n²)`. On a large shell the
gap perturbations are `O(log n)=o(n log n)`, which preserves the dominated
primitive estimates used for (19).

This explicit ruler has all of the following properties from one fixed
onset:

1. a critical cap `a_j≤C j² log(2j)` for a fixed finite `C`;
2. the exact old/new/cross identity (2) and all actual cross-ratio geometry;
3. the **entire-prefix factorial inequality** `L_n≥log((n(n−1)/2)!)` for
   every sufficiently large `n`, since (13) tends to positive infinity
   after subtracting the constant lower envelope in (3); and
4. `W_n→w_*>0`.

Thus the cap, every sufficiently large whole-prefix log-factorial lower
bound, and the complete cross-block identities do **not** imply a bounded
Fejér Wave sum. Indeed,

\[
 \sum_{k=k_0}^J\omega_{k,J}W_{2^k}
 ={w_*\over3}J+o(J),
 \qquad
 \omega_{k,J}=\left({J+1-k\over J+1}\right)^2.
 \tag{21}
\]

This is a rigorous countermodel to that relaxation, not a counterexample
to Q1. It identifies exactly what was lost: the factorial logarithmic sum
does not retain actual uniqueness of the represented integer differences.

## 7. What a surviving logarithmic-energy proof must add

Equation (10) really places `W_n` with a favorable negative sign inside
the new-half energy. The failure is not a missing algebraic sign. It is the
absence of an arithmetic estimate for the coupled boundary/cross expression
`A_n+F_n` that uses more than its separate cap bounds and the whole-prefix
factorial floor. Keeping cross terms symbolically does not supply that
estimate, as the exact countermodel shows.

A viable continuation would have to use new information that fails on (20):
for example, simultaneous subset constraints on actual difference labels,
an injective assignment retaining their additive interval structure, or a
conditional cross-block entropy defect forced by the *same* global Sidon
history. A lemma deduced only from (2)--(4) and finite cross-ratio identities
cannot close the proposed capacity. No such stronger arithmetic inequality
is proved in this note.

## Verification and review provenance

The parent task independently rederived (8)--(10) and the constants in
(18). A separate mathematical agent independently reviewed the moment
coefficients, exact product identities, all logarithmic singularity/error
estimates, the three-term-progression perturbation, and the Wave limit; it
reported no material gap or sign error. Its written review is
`log_energy_review.md` in this research directory.

The previously executed exact coefficient check and floating sanity check
were subsequently saved as `verify_log_energy_coefficients.py` and
`log_energy_smooth_sanity.py`. The actual retained outputs, exit codes,
original executables, and distinction between original execution and later
source preservation are in `log_energy_checks_provenance.md`. No rerun was
claimed from saving those files. The exact proofs above do not depend on
the floating diagnostics.
