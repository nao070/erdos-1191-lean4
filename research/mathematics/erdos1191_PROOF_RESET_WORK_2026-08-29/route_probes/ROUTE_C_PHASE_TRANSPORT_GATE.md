# Route C: continuum-phase capacity transport gate

Date: 2026-08-29  
Status: `EXACT_GRID_TRANSPORT_IDENTITY_NAIVE_ADJACENT_FLOW_SIGN_GATE_OPEN_BEYOND_GATE`

The box-dipole bridge reduces the remaining comparison to a two-dimensional
prefix/scale transport problem.  This note derives that transport identity
exactly and isolates the sign condition needed to realize the pointwise
capacity map by nonnegative adjacent-epoch retained bands.  The most direct
universal-capacity choice can violate the condition.  This is a scoped gate,
not a no-go for data-dependent allocation, longer transport, a genuinely
signed master, or Erdős Problem #1191.

## 1. Prefix-scale grid

Fix a logarithmic phase `theta in [0,1)` and put

\[
 T_r=2^{r+\theta},\qquad r\in\mathbb Z.
\]

Let `A_j` be nested spatial prefixes and define the centered low-pass energy

\[
 C_{j,r}=C_{T_r}(A_j).
\]

There are two exact edge differences:

\[
 O_{j,r}=C_{j,r}-C_{j,r+1},
 \qquad
 \Delta_{j,r}=C_{j,r}-C_{j-1,r}.
 \tag{1.1}
\]

The first is a retained dyadic band on one prefix.  The second is the
centered first-use correlation when the prefix grows.  Direct cancellation
around each grid cell gives

\[
 \boxed{
 \Delta_{j,r}-\Delta_{j,r+1}
 =O_{j,r}-O_{j-1,r}.}
 \tag{1.2}
\]

This curl identity is algebraic; it uses no positivity or Sidon hypothesis.

## 2. Exact scale summation by parts

Let `c_(j,r)>=0` be supported on a common finite interval `L<=r<=U`, and put

\[
 s_{j,r}=\sum_{t=L}^r c_{j,t}.
 \tag{2.1}
\]

Summation by parts and (1.2) give

\[
\begin{aligned}
 \sum_{r=L}^U c_{j,r}\Delta_{j,r}
 ={}&\sum_{r=L}^Us_{j,r}
       (\Delta_{j,r}-\Delta_{j,r+1})
       +s_{j,U}\Delta_{j,U+1}\\
 ={}&\sum_{r=L}^Us_{j,r}(O_{j,r}-O_{j-1,r})
       +s_{j,U}\Delta_{j,U+1}.
\end{aligned}
 \tag{2.2}
\]

For the box correlations, `Delta_(j,r)` tends to zero at both scale ends, so
the infinite version follows by a justified limit whenever the weighted
sums converge.  Keeping (2.2) finite is safer because it exposes the scale
terminal term.

Now take epochs `j_0<=j<=J` with nonnegative weights `w_j`.  Reindexing the
second term of (2.2) gives the full finite-horizon identity

\[
\begin{aligned}
 \sum_{j=j_0}^Jw_j\sum_{r=L}^Uc_{j,r}\Delta_{j,r}
={}&\sum_{r=L}^U\Bigg[
 w_Js_{J,r}O_{J,r}-w_{j_0}s_{j_0,r}O_{j_0-1,r}\\
 &\quad+\sum_{j=j_0}^{J-1}
 (w_js_{j,r}-w_{j+1}s_{j+1,r})O_{j,r}\Bigg]\\
 &+\sum_{j=j_0}^Jw_js_{j,U}\Delta_{j,U+1}.
\end{aligned}
 \tag{2.3}
\]

Thus the interior retained-band coefficient is exactly

\[
 \boxed{b_{j,r}=w_js_{j,r}-w_{j+1}s_{j+1,r}.}
 \tag{2.4}
\]

If the available finite master permits only nonnegative mixtures of retained
band gains, then

\[
 b_{j,r}\ge0\quad\text{for every interior }(j,r)
 \tag{2.5}
\]

is the exact sign gate for this adjacent-epoch realization.  A negative
`b_(j,r)` is not a contradiction; it is an additional signed band that must
be paid rather than silently dropped.

## 3. Coefficients supplied by the pointwise box-dipole map

For Wave epoch `n_j`, the proved pointwise estimate is

\[
 Q_{n_j}(T)\le {\widetilde\Delta_{j,T}\over2n_j^2}.
 \tag{3.1}
\]

Multiplying by `T_r`, summing in `r`, and then averaging in `theta` is the
natural attempt to combine (3.1) with the exact log-phase formula.  If
`R_j(theta)` is the last sampled scale at or below a chosen finite horizon,
the resulting universal capacity coefficients are

\[
 c_{j,r}={2^{r+\theta}\over2n_j^2}
          {\bf1}_{r\le R_j(\theta)}.
 \tag{3.2}
\]

Taking the lower endpoint to minus infinity, the geometric sum is exact:

\[
 \boxed{s_{j,r}
 ={2^{\min(r,R_j)+\theta}\over n_j^2}.}
 \tag{3.3}
\]

For consecutive dyadic epochs `n_(j+1)=2n_j`, (2.4) is nonnegative exactly
when

\[
 \boxed{
 2^{\min(r,R_{j+1})-\min(r,R_j)}
 \le4{w_j\over w_{j+1}}.}
 \tag{3.4}
\]

When `w_j>=w_(j+1)`, a horizon increase of at most two dyadic bands is always
safe.  A larger increase is not automatically safe.  For example, with
equal weights and `R_(j+1)=R_j+3`, taking `r>=R_(j+1)` gives

\[
 b_{j,r}={2^{R_j+\theta}\over n_j^2}
 -{2^{R_j+3+\theta}\over4n_j^2}
 =-{2^{R_j+\theta}\over n_j^2}<0.
 \tag{3.5}
\]

An eventual critical cap bounds each suffix horizon above, and distinct
positive gaps bound it below, but those facts do not force consecutive
actual suffix horizons to grow by at most four.  Therefore the direct
universal-capacity transposition cannot assume (2.5).

## 4. Exact LP exposed by the gate

For a finite horizon, a legal continuation can now be stated as a concrete
transport problem.  It must choose nonnegative scale/pair allocations
`c_(j,r)` satisfying

\[
 \sum_r2^{r+\theta}Q_{n_j}(2^{r+\theta})
 \le\sum_r c_{j,r}\Delta_{j,r},
 \tag{4.1}
\]

with `c_(j,r)` bounded by the proved interval capacities, while arranging

\[
 w_js_{j,r}-w_{j+1}s_{j+1,r}\ge0
 \tag{4.2}
\]

or paying every violation inside the same signed master.  Pair-level
constraints must use the exact strict-interior `lambda=beta` ownership and
may not reuse `mathfrak B_n`.  The initial band, final band, and scale-terminal
terms displayed in (2.3) are explicit LP boundary rows, not `O(1)` by fiat.

The universal choice (3.2) is only one feasible upper envelope and can be
too crude.  The following remain logically available:

- data-dependent fractional allocation below the pointwise capacity;
- transport across more than one epoch;
- signed coefficients justified by a larger positive-semidefinite master;
- adaptive or randomized phase followed by an exact expectation argument;
- cancellation with the already-owned nonpositive Gothic boundary terms.

## 5. Claim boundary

The proved advance is the exact grid identity (2.3) and its coefficient gate
(3.4).  The refuted shortcut is:

> insert the full pointwise capacity envelope, transpose it through adjacent
> epochs, and assume all retained-band coefficients remain nonnegative.

No claim is made that every allocation violates the gate.  C058, a legal
phase-integrated signed rewrite, one compatible infinite history, Questions
1 and 2, publication novelty, and every prize claim remain open.
