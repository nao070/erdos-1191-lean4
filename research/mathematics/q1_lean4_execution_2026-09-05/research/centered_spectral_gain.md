# A centered Fourier carrier with a non-summable single-row guarantee

Date: 2026-09-05. Owner: `/root/lean_target`.

Status: Q1 remains unresolved. This note proves a new single-row improvement
of order at least `1/log(2p)`, including the increased diagonal cost. Its
dyadic lower-bound series diverges. It does **not** turn those local gains
into savings on the common physical-label envelope or an all-history
contradiction. The full old label bank and a prefix-dependent frequency
selection are explicit hypotheses of the construction.

The parent independently checked the quantile counts, global sinc bound,
frequency window, Parseval constant, and nonnegative rank-one decomposition.
The proofs are included below; agreement is not substituted for a proof.
No theorem in this note is claimed to have been checked by Lean.

## 1. The baseline and what is being improved

Use the notation of [matrix_transport_route.md](matrix_transport_route.md).
Let

\[
 P=\{a_1<\cdots<a_p\},\quad p\ge16,\quad
 F=\Delta P,\quad q=\binom p2,\quad H=a_p-a_1.        \tag{1}
\]

`P` is an actual integer Sidon set, with repeated summands included in the
Sidon definition. Thus all its positive difference labels have unique
endpoints. The full bank `F`, rather than an arbitrary chosen subset, is
used in the counting argument below. Translate `P` when convenient; none
of the quantities in the argument changes.

For symmetric PSD `W` on `F`, retain

\[
 M=\mathbf1^TW\mathbf1,\quad S=\operatorname{tr}W,
 \quad K_W(t)=\sum_{d<e,\ e-d=t}W_{de},\quad
 T_P(W)=\sum_{t\in\Delta P}K_W(t).                   \tag{2}
\]

When `W` is entrywise nonnegative, its available old-masked row capacity is
`C_P(W)=(M-S)/2-T_P(W)`. For a compatible actual future block of size `m`,
integer interval length `L`, and positive denominator `D_B=L+H-m`, define
the raw demand `d_B(W)=(m^2 M/D_B-mS)/2`.

For a centered PSD correction `R1=0` and `W=J+lambda R`, where `J=11^T`,
the mass stays `q^2`. The exact reduction of capacity minus raw demand is

\[
\begin{split}
 I_m(W)
 &:=[C_P-d_B](J)-[C_P-d_B](W)\\
 &=\frac\lambda2\{2T_P(R)-(m-1)S(R)\}\\
 &=\frac\lambda2\{E_P(R)-(p+m-1)S(R)\},\qquad
 E_P(R)=pS(R)+2T_P(R).                               \tag{3}
\end{split}
\]

All diagonal costs appear in (3). Its value does not depend on the future
interval denominator, because the compared carriers have the same mass.
The earlier affine carrier is the mean of `u^+(u^+)^T` and `u^-(u^-)^T`,
where `u^±_d=1±(d-mean(F))/H>=0`. The PSD formulation does not hide this
nonnegative rank-one representation.

## 2. A quantile width that controls the old Fourier amplitude

Put

\[
 r=\lfloor p/8\rfloor,\quad
 l=a_{r+1},\quad h=a_{p-r},\quad D=h-l>0,\quad c=(l+h)/2.
                                                               \tag{4}
\]

There are `n=p-2r>=3p/4` central points in `[l,h]` and at most `p/4`
points outside it. For the Fourier polynomial
`P_hat(xi)=sum_(a in P) exp(i a xi)`, if `|xi|<=2/D`, then central
points have `|xi(a-c)|<=1`. Since `cos(1)>1/2`,

\[
\begin{split}
 |\widehat P(\xi)|
 &\ge\Re(e^{-ic\xi}\widehat P(\xi))\\
 &\ge n/2-(p-n)\ge p/8
 \qquad(|\xi|\le2/D).                              \tag{5}
\end{split}
\]

This uses a majority cluster only. Arbitrarily distant tail points can
contribute at worst minus one each, so they cannot cancel (5).

Two unweighted subsets of the full difference bank are quantitatively large:

\[
 F_{\rm short}=\{d\in F:d\le D/2\},\quad
 F_{\rm long}=\{d\in F:d\ge D\},\qquad
 |F_{\rm short}|\ge p^2/16,\quad |F_{\rm long}|\ge p^2/256.       \tag{6}
\]

To prove the short-label estimate, split the central interval at its
midpoint into two sets of respective point counts `n_1,n_2`. Every pair
inside one half gives a different positive label of size at most `D/2`.
The number of these pairs is

\[
 \binom{n_1}2+\binom{n_2}2
 \ge n^2/4-n/2
 \ge9p^2/64-p/2\ge p^2/16 \quad(p\ge16).            \tag{7}
\]

For long labels, the bottom `r` and top `r` points give `r^2` distinct
differences larger than `D`. Since `p>=16` implies
`r>=p/8-1>=p/16`, this proves the second estimate. Sidon injectivity is
used in both counts; counts of endpoint pairs have not been silently
replaced by counts of possibly repeated labels.

## 3. Selecting a frequency with centered label variance bounded below

For `0<=theta<=1/D`, set

\[
 \mu(\theta)=q^{-1}\sum_{d\in F}e^{i\theta d},\quad
 \sigma^2(\theta)=1-|\mu(\theta)|^2
 =q^{-2}\sum_{d,e\in F}(1-\cos(\theta(d-e))).         \tag{8}
\]

The elementary global bound needed here is

\[
 1-\frac{\sin x}{x}\ge\frac1{48}\qquad(x\ge1/2).     \tag{9}
\]

For `1/2<=x<=2`, Taylor's theorem gives
`1-cos y >= y^2/2-y^4/24 >= y^2/4` for `0<=y<=x`.
Integrating and dividing by `x` gives `1-sin(x)/x>=x^2/12>=1/48`.
For `x>=2`, use `sin x<=1` to obtain `1-sin(x)/x>=1-1/x>=1/2`.
This treats the entire unbounded range; no small-angle approximation is
being applied to an arbitrarily large difference.

Each short/long ordered pair has `|d-e|>=D/2`. Averaging its term in (8)
over `[0,1/D]` gives `1-sinc((d-e)/D)>=1/48`. Every remaining term is
nonnegative. Since `q<=p^2/2`, (6) yields

\[
 D\int_0^{1/D}\sigma^2(\theta)\,d\theta
 \ge\frac{2|F_{\rm short}||F_{\rm long}|}{48q^2}
 \ge\frac1{24576}=:\eta.                            \tag{10}
\]

By continuity, some `theta` in this compact interval satisfies
`sigma^2(theta)>=eta`. The frequency can be chosen from `P` alone by
maximizing this explicit continuous function. It uses no future shell or
future owner of a physical difference label.

Fix such a frequency and put

\[
 z_d=e^{i\theta d}-\mu(\theta),\quad
 R_{de}=\Re(z_d\overline{z_e}).                       \tag{11}
\]

This is a real PSD matrix of rank at most two, with
`R1=0`, `|z_d|<=2`, and

\[
 \eta q\le S(R)=\sum_d|z_d|^2=q\sigma^2(\theta)\le q. \tag{12}
\]

## 4. A low-frequency packet gives the energy bound

Let `Z_theta(xi)=sum_(d in F) z_d exp(i d xi)`. At the negative selected
frequency there is the exact identity

\[
 Z_\theta(-\theta)=q(1-|\mu(\theta)|^2)
                   =q\sigma^2(\theta)\ge\eta q.      \tag{13}
\]

Because `F` is contained in `[1,H]` and `|z_d|<=2`,
`|Z_theta'(xi)|<=2qH` at every real frequency. Set

\[
 a=\eta/(4H),\qquad I=[-\theta-a,-\theta+a].          \tag{14}
\]

On this whole interval, (13) and the derivative bound give
`|Z_theta(xi)|>=eta q/2`. Also `D<=H`, so
`|xi|<=1/D+eta/(4H)<=2/D`; (5) applies. Since `D,H>=1`, the interval
lies inside `[-pi,pi]`, and its length is exactly `eta/(2H)`.

For the integer convolution `f(x)=sum_(a in P) z_(x-a)`, Parseval therefore
gives

\[
\begin{split}
 E_P(R)=\sum_x|f(x)|^2
 &=\frac1{2\pi}\int_{-\pi}^{\pi}
       |\widehat P(\xi)|^2|Z_\theta(\xi)|^2\,d\xi\\
 &\ge\frac1{2\pi}\frac\eta{2H}\frac{p^2}{64}
                         \frac{\eta^2q^2}4
 =\boxed{\frac{\eta^3p^2q^2}{1024\pi H}}.
                                                               \tag{15}
\end{split}
\]

The equality with `p S(R)+2T_P(R)` follows by expanding the same convolution
and using the unique old positive differences. Thus (15) is an estimate
on the actual old adjacency, with no feasible-graph replacement.

In particular, if `A_P` is that adjacency and `Pi` is orthogonal projection
onto `1^perp`, then its centered spectrum satisfies

\[
 \lambda_{\max}(\Pi A_P\Pi|_{\mathbf1^\perp})
 \ge\frac{E_P(R)}{S(R)}-p
 \ge\frac{\eta^3p^2q}{1024\pi H}-p.                 \tag{16}
\]

The first inequality is the Rayleigh principle applied to the two real
components of `z`; at least one component attains their trace-weighted
average. Under the critical cap this is a lower bound of order
`p^2/log p` minus `p`, improving the earlier `p^2/log^3 p` guarantee.

## 5. Nonnegative carriers and the exact non-summable row rate

Take

\[
 W=J+R/8.                                           \tag{17}
\]

It is PSD, entrywise at least `1/2`, and has
`M=q^2`, `q<=S<=9q/8`. More explicitly, if `x=Re z` and `y=Im z`, then

\[
 W=\frac14\sum_{v\in\{1+x/2,1-x/2,1+y/2,1-y/2\}}vv^T.         \tag{18}
\]

All four vectors are entrywise nonnegative, each sums to `q`, and each
has squared norm between `q` and `5q/4`. Equation (18) follows by expanding
both opposite-sign pairs. Thus this construction can be used within the
original nonnegative scalar-carrier formulation as well.

Equations (3), (12), and (15), with `lambda=1/8`, imply

\[
 \boxed{\quad
 \frac{I_m(W)}{q^2}
 \ge\frac{\eta^3p^2}{16384\pi H}
          -\frac{p+m-1}{16q}.
 \quad}                                             \tag{19}
\]

For fixed `C>0`, fixed `R_0>=1`, and `p<=m<=R_0p`, assume the actual old
prefix satisfies `H<=C p^2 log(2p)`. Then

\[
 \frac{I_m(W)}{q^2}
 \ge\frac{\eta^3}{16384\pi C\log(2p)}
       -\frac{R_0+1}{8(p-1)}.                        \tag{20}
\]

The positive constant is deliberately conservative. It is independent of
the prefix and its size. For all sufficiently large qualifying prefixes,
(20) is a positive guarantee of order `1/log(2p)`.

Since the row-gap expression is linear in `W`, at least one of the four
scalar carriers in (18) attains at least the average improvement (19).
This choice can be made simultaneously for a fixed near-shell range:
choose a maximizing carrier at the largest integer `m_max` of that range.
Each carrier has `S(vv^T)-q>=0`, so its improvement is nonincreasing in `m`.
The selected carrier therefore has at least that same lower gain for all
`m<=m_max`. No future interval geometry enters this four-way choice.

For positivity of the demands themselves, take the actual rank shell
`B={a_(m+1),...,a_(2m)}` and impose the same cap at rank `2m`.
Its denominator satisfies
`D_B/m <= 4C m log(4m)+C p^2 log(2p)/m = O_(C,R_0)(p log p)`.
Each scalar carrier in (18) has `M/S>=4q/5`, so all four raw demands,
as well as the matrix demand, are positive eventually. The comparison is
then also a comparison of the corresponding positive-part demands.

At dyadic `p=2^k`, the explicit series on the right of (20) is

\[
 \frac{\eta^3}{16384\pi C\log2}\frac1{k+1}
      -\frac{R_0+1}{8(2^k-1)}.                       \tag{21}
\]

Its sum diverges to positive infinity. This improves the summable
`k^(-5)` row guarantee from the affine-moment construction. It is a
statement about individually normalized row comparisons; it is not a
claim that the same physical source may be credited this many times.

## 6. Exact finite checks with a rational unit-circle phase

The [standard-library checker](evidence/centered_fourier_exact_checks.py)
uses the same 17-point old prefix and its exact 17-point greedy continuation
as the previous note. It contains and verifies all 34 points, including
unordered sums with repeated summands. Its
[execution log](evidence/centered_fourier_exact_checks.log) and
[source-hash provenance](evidence/centered_fourier_exact_checks.run.json)
record the successful run. No floating-point trigonometry is used.

Here `D=248`, `H=335`, `q=136`, and the phase is chosen as
`theta=2 arctan(1/(2D))`. The unit complex number has the exact rational form

\[
 e^{i\theta}=\frac{(2D)^2-1+4Di}{(2D)^2+1}.          \tag{22}
\]

Gaussian-integer powers put all centered features over one common integer
denominator. Every assertion about signs, traces, kernels, demands, and
improvements is checked with exact integers or `Fraction`; decimal values
below are displays only. The selected phase variance is approximately
`0.133868`, well above `eta`.

| Carrier | Available capacity | Positive raw demand | Row-gap improvement |
|---|---:|---:|---:|
| Uniform | 4026 | 444.4024 | baseline |
| `1-Re(z)/2` | 4118.2763 | 431.5480 | -105.1308 |
| `1+Re(z)/2` | 3901.8341 | 431.5480 | 111.3114 |
| `1-Im(z)/2` | 3870.7896 | 418.5690 | 129.3770 |
| `1+Im(z)/2` | 4106.9931 | 418.5690 | -106.8265 |

The matrix improvement is the exact average of the four scalar improvements,
approximately `7.1828 > 0`. The best scalar improvement is approximately
`129.3770 > 0`. Their exact rational numerators and denominators are saved
in the log. Actual internal expenditures exceed each displayed demand.
This is a finite validation of the formulas and construction, not evidence
from which the asymptotic estimate is inferred.

## 7. What the spectral improvement does not settle

The frequency in (10) and the four-way scalar selection can vary with the
old prefix. On a fixed row, capacity is linear in `W`; on the common source,
the cost is `sum_t max_j G_j(t)`. The matrix average and the four-way
selection do not commute with those maxima in the direction needed to
claim a saving against the uniform full-history envelope.

The original exact transport identity still contains both changed weights
on old relations and genuinely new relation pairs. There is no bound here
on its positive injection term. Moreover the local guarantee is proved
relative to the uniform full bank. It has not been proved as a repeatable
hazard for every already conditioned productive weight vector; the
unweighted quantile counts in (6) alone would not establish such a claim.

Even the diverging row-improvement series (21) can coexist with a larger
positive baseline row slack or with maxima attained at other epochs.
Neither effect has been bounded away under the fixed-onset cap. Establishing
that coupling remains necessary before any contradiction with an actual
Sidon history, and before a resolution of Q1, can be claimed.
