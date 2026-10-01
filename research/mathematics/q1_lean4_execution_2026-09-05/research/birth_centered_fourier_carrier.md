# A Fourier carrier centered in every actual endpoint-birth class

Date: 2026-09-05. Author: `/root`, GPT-6 Astra Ultra.
Status: supporting all-rank mathematical theorem, not a resolution of Q1.
No Lean verification is asserted in this note. The historical-envelope
cross term remains to be controlled.

Let `P={a_1<...<a_p}` be an actual integer Sidon set, with repeated sums
included, and assume `p>=16`. Write `F=Delta P`, `q=binom(p,2)`,
`H=a_p-a_1`, and

\[
 G_j=\{a_j-a_i:1\le i<j\}\quad(2\le j\le p).
\]

The full difference bank partitions into these actual birth classes. In
particular, a label has one upper endpoint. The construction below uses
this incidence and not merely arbitrary nested subsets of `[1,H]`.

## 1. A quantile width leaving a positive fraction of later births

Put

\[
 r=\lfloor p/8\rfloor,\quad l=a_{r+1},\quad
 h=a_{p-2r},\quad D=h-l>0,\quad c=(l+h)/2.
\tag{1}
\]

The number of central points in `[l,h]` is `p-3r>=5p/8`.
For `|xi|<=1/D`, their phases relative to `c` have absolute value at
most `1/2`. The elementary bound `cos(1/2)>=1-(1/2)^2/2=7/8`
therefore gives

\[
 |\widehat P(\xi)|
 \ge\Re(e^{-ic\xi}\widehat P(\xi))
 \ge(7/8)(p-3r)-3r\ge11p/64\ge p/8,
 \quad \widehat P(\xi)=\sum_{a\in P}e^{ia\xi}.
\tag{2}
\]

The lower and upper tails are allowed to have arbitrary locations; each
tail point is bounded below by minus one in this calculation.

For each `j` from `p-r+1` through `p`, the old prefix `P_(j-1)` contains
both of these `r`-point sets:

\[
 \{a_1,...,a_r\},\qquad
 \{a_{p-2r+1},...,a_{p-r}\}.
\]

Every difference between these two sets is greater than `D`. There are
`r` such upper-endpoint birth stages, and `r>=p/16` for `p>=16`.

## 2. One frequency supplies a positive total of old-prefix variances

For real `theta`, define

\[
 V_j(\theta)=(j-1)
       -\frac{|\widehat P_{j-1}(\theta)|^2}{j-1}
 =\frac1{j-1}\sum_{i,k<j}
           (1-\cos(\theta(a_i-a_k)))\ge0.
\tag{3}
\]

Average over `0<=theta<=1/(2D)`, with normalized average denoted by
`Av`. For every gap larger than `D`,

\[
 \operatorname{Av}(1-\cos(\theta\,\mathrm{gap}))
 =1-\operatorname{sinc}(\mathrm{gap}/(2D))\ge1/48.
\tag{4}
\]

Here `sinc x=sin x/x`. The bound holds for every `x>=1/2`: for
`1/2<=x<=2`, integrate `1-cos y>=y^2/4` to get
`1-sinc x>=x^2/12>=1/48`; for `x>=2`, use `sin x<=1`.
Thus no small-angle approximation is used at an unbounded gap.

Using just the two sets in Section 1, for every selected `j`,

\[
 \operatorname{Av}V_j\ge\frac{2r^2}{48(j-1)}
                         \ge\frac{r^2}{24p}.
\]

Let `L={p-r+1,...,p}`. Sum over these `r` stages:

\[
 \operatorname{Av}\sum_{j\in L}V_j
 \ge\frac{r^3}{24p}\ge\frac{p^2}{98304}
 \ge\frac q{49152}=:\eta q.
\tag{5}
\]

Choose `theta` to maximize this late-stage sum on the compact frequency
interval. Continuity gives `sum_(j in L) V_j(theta)>=eta q`; the sum over
all stages is at least as large, since every variance is nonnegative.
This stronger choice is selected from `P` alone and preserves every
conclusion below. It also supports the signed cross-energy packet in
[birth_centered_transport.md](birth_centered_transport.md), Section 6.

## 3. Centering within each actual class, and its exact Fourier peak

For the unique label `d=a_j-a_i` with `i<j`, put

\[
 \mu_j=\frac1{j-1}\sum_{k<j}e^{i\theta(a_j-a_k)}
      =e^{i\theta a_j}
            \frac{\overline{\widehat P_{j-1}(\theta)}}{j-1},
 \qquad z_d=e^{i\theta d}-\mu_j,
 \qquad R_{de}=\Re(z_d\overline{z_e}).
\tag{6}
\]

The real matrix `R` is PSD of rank at most two. Also `|z_d|<=2`, and
the construction gives the exact identities

\[
 \sum_{d\in G_j}z_d=0,\qquad
 S_j:=\sum_{d\in G_j}|z_d|^2=V_j(\theta),
 \qquad S_R:=\operatorname{tr}R=\sum_jS_j.
\tag{7}
\]

Consequently `eta q<=S_R<=q`. In contrast with centering only at the
terminal bank, every literal prefix restriction is still centered:
`sum_(d in Delta P_n) z_d=0` for all `n<=p`.

There is also a real, nonnegative contribution at the negative selected
frequency from each birth class:

\[
 \begin{split}
 \sum_{d\in G_j}z_de^{-i\theta d}
 &=(j-1)-\mu_j\sum_{d\in G_j}e^{-i\theta d}\\
 &=(j-1)-\frac{|\widehat P_{j-1}(\theta)|^2}{j-1}=S_j.
 \end{split}
\tag{8}
\]

Writing `Z_n(xi)=sum_(d in Delta P_n) z_d exp(i d xi)`, we have

\[
 Z_n(-\theta)=\sum_{j\le n}S_j\ge0,
 \qquad Z_p(-\theta)=S_R\ge\eta q.
\tag{9}
\]

These central-frequency values are nondecreasing in the actual endpoint
order. Both the centering and (9) hold without choosing the features anew
at a prefix.

## 4. The same non-summable single-row guarantee survives the stronger constraint

Since `|Z_p'(xi)|<=2qH`, on the interval

\[
 I=[-\theta-\eta/(4H),-\theta+\eta/(4H)]
\]

we have `|Z_p(xi)|>=eta q/2`. Also `D<=H`, and hence every point of
this interval has absolute value at most `1/D`; (2) applies. As `D,H>=1`,
the interval is contained in `[-pi,pi]`. Its length is `eta/(2H)`.
The actual old convolution and Parseval give

\[
 \begin{split}
 E_P(R)&=\sum_x\left|\sum_{a\in P}z_{x-a}\right|^2
       =pS_R+2\sum_{t\in\Delta P}K_R(t)\\
 &=\frac1{2\pi}\int_{-\pi}^{\pi}
            |\widehat P(\xi)|^2|Z_p(\xi)|^2\,d\xi
 \ge\frac{\eta^3p^2q^2}{1024\pi H},
 \end{split}
\tag{10}
\]

where `K_R(t)=sum_(d<e,e-d=t) R_de`. All repeated-label fibers are
retained in this convolution expansion.

Set `W=J+R/8`. Its entries lie in `[1/2,3/2]`; it is PSD, and
`M(W)=q^2`, `q<=tr W<=9q/8`. For a compatible future block of size
`m` with the same positive interval denominator in both comparisons,
the exact terminal capacity-minus-raw-demand improvement is

\[
 I_m(W)=\frac1{16}\{E_P(R)-(p+m-1)S_R\}.
\]

Under `H<=C p^2 log(2p)`, with fixed `R_0>=1` and `p<=m<=R_0p`,
(10) and `S_R<=q` prove

\[
 \boxed{\quad
 \frac{I_m(W)}{q^2}
 \ge\frac{\eta^3}{16384\pi C\log(2p)}
      -\frac{R_0+1}{8(p-1)},\qquad \eta=1/49152.
 \quad}
\tag{11}
\]

The bound is positive eventually and its dyadic lower-bound series
diverges. This is a statement about individually normalized row
comparisons, not about repeatedly spending a physical source budget.

Let `x=Re z`, `y=Im z`. As in the earlier centered carrier,

\[
 W=\tfrac14\sum_{v\in\{1+x/2,1-x/2,1+y/2,1-y/2\}}vv^T.
\tag{12}
\]

Every vector in (12) is nonnegative and sums to `|G_j|` on every birth
class. It therefore sums to `q_n` on each literal prefix, and has
squared norm at most `5q_n/4` there. At the terminal prefix, choosing
one of these four vectors at the largest `m` in a fixed near-shell
range preserves the bound for all smaller `m` in that range. The proof
uses linearity and the nonnegative trace increment, exactly as in
[centered_spectral_gain.md](centered_spectral_gain.md).

For actual rank shells whose terminal rank also obeys the fixed cap,
the effective ratio `M/S>=4q/5` makes all four raw demands positive
eventually. Thus the same comparison applies to positive-part demands.

## 5. Which transport issue is removed, and which remains

This construction removes the intermediate-prefix mass error caused by
loss of centering. No `|sum_(F_n) z|^2` term occurs at any restriction.
It also gives the nondecreasing real values (9) at the selected frequency.
These are genuine additional compatibility properties of the carrier.

They do not imply that the squared Fourier amplitude increases at every
frequency. In particular the positive contribution from the interval in
(10) cannot be copied into the signed energy change at a birth stage
while its contribution outside that interval is discarded.

For a new class `G_n`, actual Sidon difference injectivity gives

\[
 \|1_{P_n}*z_{G_n}\|_2^2
 =(n-1)S_n+\left|\sum_{d\in G_n}z_d\right|^2
 =(n-1)S_n.
\tag{13}
\]

To see this, at convolution position `a_n` the coefficient is the sum
of the class weights; at every other position `a_n+(a_k-a_i)` the
nonzero difference has unique endpoints, and each input weight occurs
exactly `n-1` times. The zero-sum term vanishes by (7).

Thus the diagonal and new-class energy do not by themselves provide a
large extra positive source. The cross term between old labels and new
labels remains essential. Equivalently the fixed-weight historical
capacity-minus-demand gain is the row gain (11) minus the signed
retirement correction, as in
[weighted_birth_envelope.md](weighted_birth_envelope.md).

No bound on that correction under the full fixed-onset cap has been
proved here. No original-Q1 theorem or counterexample, and no final
Lean clean build or axiom audit, is supplied by this supporting result.
