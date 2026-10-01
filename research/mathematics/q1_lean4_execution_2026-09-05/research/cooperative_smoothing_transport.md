# Cooperative smoothing and the causal cross-energy budget

Date: 2026-09-05. Owner: `/root/global_route`, GPT-6 Astra Ultra.
Status: bounded analytic investigation, with exact operator identities
and an explicit remaining inequality. Original Q1 remains unresolved.
No numerical search or Lean verification is claimed.

## 1. Primary lemma actually read

Jianfeng Hou and Hongbin Zhao, *Vector-valued smoothing for finite Sidon
sets*, [arXiv:2607.01169v1](https://arxiv.org/html/2607.01169v1),
1 July 2026, Lemma 2.1 and its complete proof were read directly.
The published setup uses symmetric probability kernels, nonnegative
mixing coefficients of total mass one, and real boundary weights. Only
the weighted combination of kernel/weight pairs must cover each input
location. Individual pairs need not cover it.

The operative proof step is Hilbert-space Cauchy–Schwarz applied after
this combined pointwise cover. The upper energy estimate separately uses
nonnegative kernel autocorrelations and unique Sidon differences. Thus
the proof does not provide positivity for an arbitrary bilinear cross
term. The finite coefficient and the rational certificate are not
recomputed here; neither is needed below.

Here is the elementary operator version of that proof, stated separately
because the kernels below need not have its block structure or symmetry.
For finitely supported real nonnegative probability kernels `K_r`, let

\[
 ({\cal T}f)_r=\sqrt{\lambda_r}(f*K_r),\qquad
 \lambda_r\ge0,\quad\sum_r\lambda_r=1.
\]

If real square-summable weights `Q_r` satisfy

\[
 M(x):=\sum_r\lambda_r\sum_sK_r(s)Q_r(x+s)\ge1
       \quad(x\in I),\qquad
 N_Q:=\sum_r\lambda_r\|Q_r\|_2^2,                \tag{1}
\]

then for every `B ⊂ I` with `|B|=m`,

\[
 m\le\sum_r\lambda_r\langle 1_B*K_r,Q_r\rangle,
 \qquad
 \|{\cal T}1_B\|_2^2\ge m^2/N_Q.                \tag{2}
\]

Indeed, sum (1) over `B`, interchange the finite sums, and apply
Cauchy–Schwarz in the weighted direct sum. No unmentioned sign of
`Q_r` is needed. Positivity of `1_B` is essential to the first step.
This proof establishes (2) for these more general kernels; it does not
claim their use is a literal instance of the source's symmetric finite
certificate.

For a complex centered input `z`, a cover `M≥1` does not bound a
nonzero linear functional of `z`: multiplying its inequalities by the
complex coefficients is invalid, and `Σz=0` in the intended application.
A phase-matched dual test can instead bound a squared norm. Such a norm
bound still has to be transported through its old/new cross terms.

## 2. The causal operator and the quantity to retain

Let `P_n={a_1<...<a_n}` be an actual integer Sidon prefix, `F_n=ΔP_n`,
and `G_n=F_n\F_(n−1)`. Fix one terminal prefix `p` and one phase, and
use exactly the features from `birth_centered_transport.md`:

\[
 z_{a_j-a_i}=e^{i\theta(a_j-a_i)}
       -\frac1{j-1}\sum_{h<j}e^{i\theta(a_j-a_h)}.
\]

Thus `Σ_(d∈G_j)z_d=0`, `|z_d|≤2`. Put
`q=|F_p|=binom(p,2)`, `S_j=Σ_(G_j)|z_d|²`, and `S=Σ_j S_j≤q`.
All restrictions below are literal restrictions of this one terminally
fixed feature, without reselecting its phase.

Define input/output operators and their increments by

\[
 L_nf=1_{P_n}*f,\quad
 v_n=L_nz_{F_{n-1}},\quad g_n=L_nz_{G_n},\quad
 X=\sum_{n=2}^p\Re\langle v_n,g_n\rangle.          \tag{3}
\]

Write `R_de=Re(z_d conjugate(z_e))` and `W=J+R/8`. The already
proved exact budget comparison is

\[
 C_{\rm hist}(J)-C_{\rm hist}(W)=X/8.             \tag{4}
\]

For a terminal future block of size `m`, keeping the same raw
denominator in the two comparisons, the retained gain is

\[
 I_m^{\rm hist}=X/8-mS/16.                        \tag{5}
\]

In Fourier variables,

\[
 A(\xi)=\sum_n|\widehat P_n(\xi)|^2
       \Re\{Z_{F_{n-1}}(\xi)\overline{Z_{G_n}(\xi)}\},
 \qquad X=(2\pi)^{-1}\int_{-\pi}^{\pi}A.          \tag{6}
\]

The positive interval packet in the transport note has size at least
`η⁴ p²q²/(2²² π H)`, where `H=diam(P_p)` and `η=1/49152`.
Equation (6) still includes its signed complement. This investigation
does not discard that complement.

## 3. A valid cooperative cover using the four positive carriers

On the terminal bank `F=F_p`, take the four nonnegative functions

\[
 u_1=1+\Re z/2,\quad u_2=1-\Re z/2,\quad
 u_3=1+\Im z/2,\quad u_4=1-\Im z/2.              \tag{7}
\]

Every `u_r` has mass `q`, and has mass `q_n` on every full prefix bank.
With equal probabilities `λ_r=1/4`,

\[
 \frac14\sum_ru_r(d)u_r(e)=W_{de},\qquad
 \frac14\sum_r\sum_d u_r(d)^2=q+S/8.             \tag{8}
\]

Apply (1)–(2) with `K_r=u_r/q`. A *cooperative* cover is allowed:
only their mixture must majorize one on the allowed future locations.
For actual Sidon `B`, unique physical differences give exactly

\[
 q^2\|{\cal T}1_B\|_2^2
   =m(q+S/8)+2\sum_{t\in\Delta B}K_W(t),
 \qquad K_W(t)=\sum_{d,d+t\in F}W_{d,d+t}.        \tag{9}
\]

Consequently the raw lower demand is

\[
 D_W(Q)=\frac12\left(\frac{m^2q^2}{N_Q}
                              -m(q+S/8)\right). \tag{10}
\]

If `B` is compatible with the old ruler, then `ΔB∩F=∅`; this
condition is used on the same physical labels `t` in (9). The cover
does not create four separate label budgets.

In detail, for each `r` the unnormalized correlation of the restriction
`u_r 1_(F_n)` increases with `n` because all its coefficients are
nonnegative. For a fixed physical `t`, its eligibility indicator is
`1[t∉F_n]`. Every channel therefore attains its eligible maximum at
the same last eligible prefix. It follows that

\[
 \sum_t\max_n\left[1_{t\notin F_n}
       \frac14\sum_r K_{u_r1_{F_n}}(t)\right]
 =\frac14\sum_r\sum_t\max_n
       [1_{t\notin F_n}K_{u_r1_{F_n}}(t)].        \tag{11}
\]

This explains exactly why channel averaging preserves the historical
budget here. It does not justify summing independent maxima over
different terminal widths, different phases, or unrelated time weights.

For a baseline `J` cover with squared norm `N_J`, the corresponding
raw demand is `D_J=½(m²q²/N_J−mq)`. Combining (4) and (10) gives the
exact cooperative historical comparison

\[
 \boxed{\ (C_{\rm hist}(J)-D_J)
       -(C_{\rm hist}(W)-D_W(Q))
 =\frac X8+\frac{m^2q^2}{2}
            \left(\frac1{N_Q}-\frac1{N_J}\right)
          -\frac{mS}{16}.\ }                    \tag{12}
\]

Thus cooperation really offers an additional term: a smaller cover
norm increases the demand. Its sign is not assumed; different kernel
families need not have the same optimum cover norm. Setting `N_Q=N_J`
recovers (5). Equations (10)–(12) compare **raw** demands. Replacing
them by their positive parts requires a new piecewise comparison and
is not silently used here.

## 4. Smoothing the causal outputs changes the cross form

A second attempted application is to smooth the outputs in (3).
Let `T` be the convolution direct-sum operator from §1, set `B=T*T`,
and let

\[
 c(t)=\sum_r\lambda_r\sum_sK_r(s)K_r(s+t),\qquad
 \rho(\xi)=\sum_r\lambda_r|\widehat K_r(\xi)|^2.
\]

Here `c` is nonnegative and even, `Σ_t c(t)=1`, and `0≤ρ≤1`.
The smoothed cross energy is

\[
 X_c=\sum_n\Re\langle Tv_n,Tg_n\rangle
       =(2\pi)^{-1}\int\rho(\xi)A(\xi)\,d\xi.   \tag{13}
\]

For old `d∈F_(n−1)` and new `e∈G_n`, its exact coefficient is

\[
 X_c=\sum_n\sum_{d,e}\Re(z_d\overline{z_e})
               H_n^c(e-d),\qquad
 H_n^c(t)=n c(t)+\sum_{s\in F_n}[c(t-s)+c(t+s)].   \tag{14}
\]

To see (14), expand the two convolutions: the smoothing-point
difference `a-b` contributes `c(t−(a-b))`. Sidonness makes each
nonzero signed difference occur once, while zero has multiplicity `n`.
For `c=δ_0` the old/new labels are distinct and this is the original
membership test `|e-d|∈F_n`. For general `c`, physical labels `s`
near `e-d` are mixed, and the zero-difference term `n c(e-d)` also
appears. The original historical capacity (4) prices the membership
test, not these new coefficients. Keeping (4) while substituting (13)
would change the source budget without paying for that change.

Modulating kernels can move a Fourier multiplier toward `−θ`, but
then their physical autocorrelation is complex; the nonnegative
autocorrelation upper bound in the source lemma cannot be retained
unchanged. An orthogonal Fourier projection onto the positive packet
also bounds a modified cross form, not the one in (4).

The smoothed energy transport itself remains exact. With
`f_n=L_n z_(F_n)`, `h_n=δ_(a_n)*z_(F_(n−1))`, and
`R_n^c=Re⟨Tf_(n−1),Th_n⟩`,

\[
 \|Tf_n\|^2-\|Tf_{n-1}\|^2
   =\|Tz_{F_{n-1}}\|^2+\|Tg_n\|^2
                              +2R_n^c+2X_n^c.    \tag{15}
\]

Since `T` is a contraction and actual birth-class centering gives
`||g_n||²=(n−1)S_n`, its nonnegative diagonal cost obeys

\[
 \sum_n\left(\|Tz_{F_{n-1}}\|^2+\|Tg_n\|^2\right)
 \le\sum_n[S(F_{n-1})+(n-1)S_n]=(p-1)S.          \tag{16}
\]

This useful reduction of the diagonal does not identify `R_n^c` with
the original retirement functional, or remove the coefficient change
in (14).

## 5. Exact price of returning from a filtered packet

For any contraction multiplier `0≤ρ≤1`, define

\[
 V_\perp=\sum_n\|(I-B)^{1/2}v_n\|^2,\qquad
 G_\perp=\sum_n\|(I-B)^{1/2}g_n\|^2.
\]

The operator identity and direct-sum Cauchy–Schwarz give

\[
 X-X_c=\sum_n\Re\langle(I-B)^{1/2}v_n,
                                    (I-B)^{1/2}g_n\rangle,
 \qquad X\ge X_c-\sqrt{V_\perp G_\perp}.         \tag{17}
\]

Available elementary bounds are

\[
 G_\perp\le\sum_n(n-1)S_n\le(p-1)S,\qquad
 V_\perp\le\sum_n n^2S(F_{n-1})\le p^3S.        \tag{18}
\]

The second bound uses `||1_(P_n)*f||_2≤n||f||_2`.
Their resulting loss is `O(p²S)=O(p⁴)`, larger than the packet
`q²/log p` under the critical cap. A sufficient new estimate would be
`V_perp G_perp=o(q⁴/log² p)` for a packet-retaining filter. For example,
when only `G_perp=O(p³)` is known, the sufficient condition
`V_perp=o(p⁵/log² p)` would supply the missing logarithmic saving.
No such estimate is established by the cover lemma, and none is
asserted here.

## 6. The precise remaining cooperative inequality

There are two distinct ways the new cover could help, neither supplied
by the cited lemma alone:

1. Retain the original physical budget and prove, for admissible
   cooperative covers and the actual selected features,

\[
 X+4m^2q^2\left(\frac1{N_Q}-\frac1{N_J}\right)
      -\frac{mS}{2}
       \ \ge\ c_C\frac{q^2}{\log(2p)}             \tag{19}
\]

   with one positive constant on the required fixed-onset capped
   histories. By (12), this is exactly eight times the desired retained
   gain. Its cover improvement might compensate a negative frequency
   complement, but doing so requires a joint estimate involving `X`.
   A separate valid cover, without (19), does not do it.

2. Retain a filtered packet, and prove an adequate complement estimate
   in (17), or explicitly reprice all shifted coefficients in (14)
   by one shared physical source measure. Positivity of the filtered
   packet and the diagonal bound (16) alone do not suffice.

This bounded investigation ends at (19) and (17). It neither proves
these missing inequalities nor gives a critical-cap counterexample to
them. It does establish that cooperative covering can be incorporated
without duplicating physical budgets, and identifies the exact extra
term it buys. The published finite Sidon bound is not being substituted
for the original infinite Q1 obligation.
