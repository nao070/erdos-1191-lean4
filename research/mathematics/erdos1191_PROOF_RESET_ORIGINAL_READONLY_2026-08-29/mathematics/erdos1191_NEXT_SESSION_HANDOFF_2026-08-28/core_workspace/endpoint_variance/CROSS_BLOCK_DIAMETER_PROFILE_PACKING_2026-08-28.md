# Cross-block packing and forced diameter-profile resets

**Date:** 2026-08-28  
**Status:** rigorous global-history restriction and rigorous no-go for a
natural innovation charge.  It does not prove the missing `o(log J)` budget
and does not resolve Erdős Problem #1191.

## 1. Diameter profile

Let

\[
A_M=\{a_0<a_1<\cdots<a_{M-1}\}
\]

be a finite Sidon ruler.  Put

\[
N_0=0,
\qquad
N_r=a_{r-1}-a_0+1\quad(1\le r\le M),
\qquad N=N_M,
\]

and define the shifted rank-grid discrepancy

\[
\varepsilon_M=
\max_{0\le r\le M}
\left|\frac{N_r}{N}-\frac rM\right|.
\tag{1}
\]

This is deliberately called a *diameter-profile* discrepancy, not the graph
divergence `delta_N` used elsewhere in the project.  If
`Delta_M=d_K(nu_M,lambda)` is the Kolmogorov discrepancy of the diameter-gap
measure from Lebesgue measure, then the left and right limits at the rank grid
give the exact formula

\[
\Delta_M=
\max_{1\le r\le M}
\max\left\{|e_r|,\left|e_r+\frac1M\right|\right\},
\qquad e_r=\frac{N_r}{N}-\frac rM.
\tag{2}
\]

Consequently

\[
\boxed{
\varepsilon_M\le\Delta_M\le\varepsilon_M+\frac1M.
}
\tag{2a}
\]

The grid shift remains important: on `[(r-1)/M,r/M)` the cumulative gap mass
is `N_r/N`, and the two interval endpoints produce the two terms in (2).

## 2. A weighted cross-band packing lemma

Let `I` and `J` be two disjoint consecutive rank intervals, with every index
of `I` before every index of `J`.  The cross spectrum

\[
\Delta(J,I)=\{a_j-a_i:i\in I,\ j\in J\}
\]

contains exactly `|I||J|` integers and lies in

\[
K(I,J)=
[a_{\min J}-a_{\max I},\ a_{\max J}-a_{\min I}].
\]

The containing band has the exact integer length

\[
|K(I,J)|=\operatorname{span}(I)+\operatorname{span}(J)+1,
\]

so Sidon uniqueness gives

\[
|I||J|\le
\operatorname{span}(I)+\operatorname{span}(J)+1.
\tag{3}
\]

More generally, let `(I_alpha,J_alpha)` be any family whose ordered rank
rectangles `I_alpha x J_alpha` are pairwise disjoint, and let
`w_alpha>=0`.  All actual differences represented by these rectangles are
distinct.  Charging an occupied integer by the weight of its unique rectangle
therefore proves the exact weighted inequality

\[
\boxed{
\sum_\alpha w_\alpha |I_\alpha||J_\alpha|
\le
\sum_{d=1}^{N-1}
\max_{\alpha:\ d\in K(I_\alpha,J_\alpha)}w_\alpha .
}
\tag{4}
\]

The constant in (4) is one.

### Dyadic-tree corollary

Take the complete dyadic rank tree on `M=2^J` marks.  If an internal node
`v` has two children of `m_v` marks and its full rank interval has span `D_v`,
then the child-to-child spectra partition all positive differences, once
each.  Order the internal nodes so that

\[
D_{v_1}\le D_{v_2}\le\cdots
\]

and put `S_r=sum_(i<=r)m_(v_i)^2`.  The first `r` spectra consist of `S_r`
distinct positive integers, each at most `D_(v_r)`, hence
`D_(v_r)>=S_r`.  Consequently

\[
\boxed{
\sum_v\frac{m_v^2}{D_v}
\le
\sum_r\frac{S_r-S_{r-1}}{S_r}
\le 1+\log\binom M2 .
}
\tag{5}
\]

This is a genuine cross-prefix Carleson packing estimate, but its size is
`O(log M)=O(J)`, not the required `o(log J)`.

## 3. Same-rank-lag collision bands

Let `M=qm` and partition the ranks into `q` consecutive `m`-mark blocks

\[
B_t=\{tm,\ldots,(t+1)m-1\},
\qquad 0\le t<q.
\]

Write

\[
e_r=\frac{N_r}{N}-\frac rM,
\qquad |e_r|\le\varepsilon_M.
\]

Fix a block lag `1<=d<q`.  The exact smallest and largest differences from
`B_t` to `B_(t+d)` are

\[
L_{t,d}=N\left(
\frac{d-1}{q}+\frac1M
+e_{(t+d)m+1}-e_{(t+1)m}
\right),
\tag{6}
\]

\[
U_{t,d}=N\left(
\frac{d+1}{q}-\frac1M
+e_{(t+d+1)m}-e_{tm+1}
\right).
\tag{7}
\]

As `t` varies, the `(q-d)m^2` underlying rank pairs are disjoint, so all their
differences are distinct.  They lie between the global minimum of (6) and the
global maximum of (7).  Counting all integers in that band gives

\[
\boxed{
(q-d)m^2\le N\left[
\frac2q-\frac2M
+\max_t(e_{(t+d+1)m}-e_{tm+1})
-\min_t(e_{(t+d)m+1}-e_{(t+1)m})
\right]+1.
}
\tag{8}
\]

In particular,

\[
\boxed{
(q-d)m^2\le
N\left(\frac2q-\frac2M+4\varepsilon_M\right)+1.
}
\tag{9}
\]

Thus, when the diameter profile is nearly rank-uniform, all cross spectra of
one block lag are forced into a common short integer band.

Equation (9) alone does **not** force a positive discrepancy at the terminal
critical scale.  Solving it for `epsilon_M` gives

\[
\varepsilon_M\ge
\frac{(q-d)m^2-1}{4N}
-\frac1{2q}+\frac1{2M},
\]

whose right side can be negative when `N` has order `M^2 log M`.  This is not
just a weakness of constants.  Put `X=ceil(M log M)`, choose a prime
`X<=p<2X`, and use the `M`-mark Erdős--Turán ruler
`b_i=2pi+(i^2 mod p)`.  Then

\[
M^2\log M\le N_M\le5M^2\log M,
\qquad \varepsilon_M\le\frac2M,
\]

while every exact fixed-rank-lag spectrum lies in a band of width below
`2p`.  What fails is the old-prefix hypothesis below: for
`m=M/q`, the ratio `N_m/(m^2 log m)` grows at least on the order of `q`.
Thus the genuine global-history content comes from coupling a terminal prefix
to an *old prefix of the same critical sequence*, not from (9) in isolation.

## 4. A global critical sequence must reset its diameter profile

All differences between distinct `m`-mark blocks give the independent packing
bound

\[
N-1\ge\binom q2m^2.
\tag{10}
\]

Assume only that the first block satisfies

\[
N_m\le K m^2\log m.
\tag{11}
\]

No upper bound on `N_M` is used.  From (1),

\[
\frac{N_m}{N}\ge\frac1q-\varepsilon_M.
\]

If `theta=q epsilon_M<1`, combine this inequality with (10) and (11) to get

\[
\boxed{
q-1+\frac{2}{qm^2}
\le\frac{2K\log m}{1-\theta}.
}
\tag{12}
\]

For example, `epsilon_M<=1/(4q)` implies

\[
q-1\le\frac{8K}{3}\log m.
\tag{13}
\]

For `q=2^r`, near-uniformity can therefore persist backwards for at most

\[
r\le
\log_2\left(1+\frac{8K}{3}\log m\right)
=O_K(\log\log m)
\tag{14}
\]

dyadic generations.  In the canonical project envelope
`N_m<=2C m^2 log m`, one has `K=2C`.

Without assuming that `theta<1`, (10) also gives the unconditional exact
lower bound

\[
\boxed{
\varepsilon_M\ge
\frac1q-
\frac{K m^2\log m}{\binom q2m^2+1}.
}
\tag{15}
\]

Now suppose one infinite Sidon sequence satisfies (11) for every sufficiently
large prefix.  Let `M` be a sufficiently large power of two, let `q` be the
least power of two at least `1+4K log M`, and put `m=M/q`.  Then (15) yields

\[
\boxed{
\varepsilon_M>
\frac{1}{4(1+4K\log M)}.
}
\tag{16}
\]

Together with (2a), this shows that the diameter-gap measures of a hypothetical
global critical sequence cannot be uniform to `o(1/log M)`.  This is a real
unbounded-history consequence, but it is a discrepancy *lower* bound and does
not control `Var_nu(f)` from above.

## 5. Why cross-band occupancy cannot pay for innovation

Use the growing Erdős--Turán window

\[
b_i=2pi+(i^2\bmod p),
\qquad M\le p<2M,
\]

from `GROWING_DEPTH_ERDOS_TURAN_NO_GO_2026-08-28.md`.  Its last
`L+1`, `L=floor(log_2 J)-2`, dyadic prefixes share the `C=1` critical
envelope and satisfy uniformly

\[
\frac{(Q_n)_{00}}{N_{2n}}=\frac1{360}+o(1).
\tag{17}
\]

For a transition from `n` to `2n`, its `n^2` old--new differences lie in a
band of exact length

\[
W_n=(b_{n-1}-b_0)+(b_{2n-1}-b_n)+1.
\]

Writing `b_i=2pi+r_i`, `0<=r_i<p`, gives, for `n>=3`,

\[
W_n\ge4pn-5p+2\ge2pn.
\]

At terminal offset `ell`, where `2n=M/2^ell`,

\[
\frac{n^2}{W_n}\le\frac n{2p}\le2^{-\ell-2}.
\]

Therefore

\[
\boxed{
\sum_{\ell=0}^{L-1}\frac{n_\ell^2}{W_{n_\ell}}<\frac12,
\qquad
\sum_{\ell=0}^{L-1}
\frac{(Q_{n_\ell})_{00}}{N_{2n_\ell}}
=\frac L{360}+o(1).
}
\tag{18}
\]

For any fixed constants `A,B`, (18) refutes the natural estimate

\[
\sum_n\frac{(Q_n)_{00}}{N_{2n}}
\le A+B\sum_n
\frac{|\text{old--new cross spectrum}|}
     {|\text{its containing band}|}.
\tag{19}
\]

It also refutes its pointwise vanishing analogue at the back of these growing
windows.  This is an actual finite Sidon obstruction, not an infinite
globally critical counterexample.

Covariance moments alone are weaker still.  The nested integer profile
`a_k=k^2` has limiting gap density `2u`, ratio `N_m/N_(2m)->1/4`, and

\[
R=\begin{pmatrix}1/180&-1/90\\-1/90&1/18\end{pmatrix},
\]

\[
R-\frac14BRB^{\mathsf T}
=\begin{pmatrix}19/3840&-1/80\\-1/80&5/96\end{pmatrix}\succ0,
\]

with determinant `187/1843200`.  Thus a nested quadratic-growth integer gap
profile can sustain a positive innovation.  The squares are not Sidon—for
example, `5^2-1^2=7^2-5^2=24`—which isolates the missing arithmetic input.

Even within the Sidon class, a discrepancy lower bound has the wrong
direction for the desired variance upper bound.  For `H>=2`,

\[
A_H=(0,H,H+1,2H+3)
\]

is a Golomb ruler with

\[
\varepsilon_4=d_K(\nu_4,\lambda)=\frac14,
\qquad
\operatorname{Var}_{\nu_4}f
=\frac{5H+9}{256(H+2)^2}\longrightarrow0.
\tag{20}
\]

Moreover, the homometric Sidon rulers `(0,1,3,7)` and `(0,1,5,7)` have the
same old two-mark prefix, the same `epsilon=Delta=1/4`, and the same diameter
ratio `1/4`, but their normalized innovations are respectively

\[
\begin{pmatrix}51/16384&37/4096\\37/4096&67/1024\end{pmatrix},
\qquad
\begin{pmatrix}67/16384&37/4096\\37/4096&51/1024\end{pmatrix}.
\tag{21}
\]

Thus scalar diameter-profile discrepancy does not determine even a single
actual `Q` transition.  Its forced lower bound must be augmented by the
location, sign, persistence, and cross-epoch arithmetic of the resets.

## 6. Surviving target

The next viable statement is a global **flat-profile versus profile-reset**
lemma.  At a mesoscopic partition `q` comparable to `log M`:

1. if the block-boundary errors in (8) have small same-lag oscillation, many
   distinct cross differences are compressed into a common band, but the
   one-epoch inequality alone may still be numerically vacuous;
2. if they have large oscillation, those profile resets must be charged across
   successive scales to a global potential; and
3. a contradiction or summable charge must therefore compare overlapping
   bands and cross differences from *different* flat epochs, not merely the
   occupancy of each old--new band.

The growing Erdős--Turán family proves that only `O(log log M)` recent dyadic
scales cannot suffice.  The square profile proves that covariance moments
without Sidon arithmetic cannot suffice.  What remains unproved is that
nonflat resets cannot renew independently for all time in one globally
critical Sidon sequence.
