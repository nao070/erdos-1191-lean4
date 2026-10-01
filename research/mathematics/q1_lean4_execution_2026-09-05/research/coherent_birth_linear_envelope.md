# Coherent birth-linear rows and one physical envelope

Date: 2026-09-05. Owner: `/root/global_route`, GPT-6 Astra Ultra.
Status: proved lookahead lemma, exact coupled finite accounting, and a
closed obstruction to a free trace-class budget. Original Q1 remains
unresolved. No new Lean theorem or execution is claimed.

The inputs read for this investigation were `growing_label_budget.md`,
`envelope_selection_route.md` §§5–6, `lean/Q1/PhysicalLabelEnvelope.lean`,
`birth_linear_good_epoch.md`, `retirement_shadow_threshold.md`, and
the complete new `future_moment_demand.md`. The latter's moment/support
proof and constants were independently checked and supported. The Lean
file establishes finite physical-label accounting, not an asymptotic
bound on its envelope; merely reading it is not a fresh build claim.

## 1. Two-step lookahead good epochs

Assume one strictly increasing sequence `H_k>0` satisfies

\[
 c4^k\le H_k\le Ck4^k\quad(k\ge k_0),\qquad
 k_0\ge1,\quad C\ge c>0.
\]

Set `A=C/c≥1`, `s_k=H_k/4^k`, and
`r_k=H_k/H_(k−1)` for `k≥k_0+1`. Define

\[
 {\cal G}_2=\{k\ge k_0+1:r_k\ge2,\quad
                        r_{k+1}\le32,\quad r_{k+2}\le32\}.
                                                               \tag{1}
\]

**Lookahead lemma.** If `[a,b]∩G_2=∅` with `a≥k_0+1`, then

\[
 b-a+1\le\log_2(A(a-1))+2\log_2(A(b+2))
          \le3\log_2(A(b+2)).                    \tag{2}
\]

**Proof.** If all ratios in `[a,b]` are less than two, the shrinking
argument gives `b−a+1≤log_2(A(a−1))`. Otherwise let `j_0` be the
first index with `r_(j_0)≥2`. The initial shrinking part has length
at most `log_2(A(a−1))`.

Whenever `j_i≤b` is a trigger with `r_(j_i)≥2`, failure of (1)
forces one of the next two ratios to exceed 32. Choose such an index
`j_(i+1)∈{j_i+1,j_i+2}` and continue until the first `j_ell>b`.
Then `j_ell≤b+2`. Every intervening ratio is greater than one, since
`H` is strictly increasing. Consequently each jump satisfies

\[
 \frac{s_{j_{i+1}}}{s_{j_i}}
 =\frac{H_{j_{i+1}}/H_{j_i}}{4^{j_{i+1}-j_i}}
 >\frac{32}{16}=2.
\]

Thus `c2^ell<s_(j_ell)≤C(b+2)`, so
`ell<log_2(A(b+2))`. Also `b−j_0+1≤j_ell−j_0≤2ell`.
Adding the initial part proves (2). The first trigger and both possible
right-hand lookahead endpoints are counted explicitly. ∎

For `M≥k_0+1`, put

\[
 L_M=\lfloor3\log_2(A(2M+1))\rfloor+1.
\]

Every interval of this length inside `[M,2M−1]` contains a good
index, by (2). Hence

\[
 |{\cal G}_2\cap[M,2M-1]|\ge\lfloor M/L_M\rfloor,
\qquad
 \sum_{k\in{\cal G}_2\cap[M,2M-1]}\frac1k
 \ge\frac1{2L_M}-\frac1{2M}.                     \tag{3}
\]

For `M=2^j`, `L_M≤3j+d` with one fixed
`d=3 log_2(3A)+1`. Sum (3) over disjoint such blocks and compare
`Σ1/(3j+d)` with its integral. This proves

\[
 \boxed{\quad
 \sum_{\substack{k\in{\cal G}_2\\k\le J}}\frac1k
       \ge\frac16\log\log J-O_{A,k_0}(1),\qquad
 \sum_{k\in{\cal G}_2}\frac1k=\infty.
 \quad}                                          \tag{4}
\]

All sufficiently large real `J` are covered by the complete
power-of-two blocks below `J`. Formula (2) also yields gaps
`O_(A)(log k)`. In particular the varying upper bound `Ck` has not
been treated as constant within a gap.

For an infinite integer Sidon sequence with the fixed eventual cap
`a_n≤C_0 n² log(2n)`, set `H_k=a_(2^k)−a_1`.
The distinct positive differences give `H_k≥4^k/4`; the cap gives
`H_k≤2C_0 log2·k4^k` beyond one fixed onset. Thus the hypotheses
apply with `c=1/4` and `C=max(c,2C_0 log2)`.

## 2. The genuinely new future demand is non-summable individually

For a good `k`, let `p=2^k`, `N=2p`, and write
`h(n)=a_n−a_1`, `H=h(N)`, `q=binom(N,2)`. Then

\[
 h(p)\ge2h(p/2),\quad H\le32h(p),\quad
                         h(2N)\le32H.            \tag{5}
\]

Use the birth-linear coefficients

\[
 g_{a_j-a_i}=\frac1{j-1}\sum_{u<j}a_u-a_i,
 \qquad z_d=g_d/H,\qquad S=\sum_{d\in F_N}z_d^2.
\]

The reviewed variance proof, with 32 in place of eight, gives

\[
 \eta q\le S\le q,\qquad\eta=1/(128\cdot32^2)=2^{-17},
 \qquad \sum_d dz_d=HS.                          \tag{6}
\]

Let `B_k={a_(N+1),...,a_(2N)}`, so `m=N`. Its actual interval
length `L≤h(2N)≤32H`, and `T=L+H−1≤33H`. The first-moment
future-energy lower bound is therefore

\[
 B_k^{\rm mom}:=\frac{12N^2H^2S^2}{T(T^2-1)}
       \ge\frac{12N^2S^2}{33^3H}.                \tag{7}
\]

Use the full nonnegative PSD matrix `W_k=J+zzᵀ/8`. If `D_k=L+H−N`
is the hole-corrected interval capacity, define raw demands

\[
 \delta_k^0=\frac12\left(\frac{N^2q^2}{D_k}-Nq\right),
 \qquad
 \delta_k^W=\delta_k^0+\frac{B_k^{\rm mom}-NS}{16}.       \tag{8}
\]

These are paid by the same physical kernels as in the parent note.
Relative to the **mass-only demand for `W_k`**, the new demand
increase is `B_k^mom/16`, with no subtraction of `NS` a second time.
Relative to the **unit baseline**, the increment is the second term
in (8), which retains that diagonal cost.

If `H≤C_*N² log(2N)` with fixed `C_*`, then

\[
 \frac{\delta_k^W-\delta_k^0}{q^2}
 \ge\frac{3\eta^2}{4\cdot33^3 C_*\log(2N)}
                  -\frac1{8(N-1)}.              \tag{9}
\]

The mass-only demand for `W_k` is positive for all sufficiently large
good epochs: the lower bound is
`(Nq/2)[(N−1)/(66 C_* log(2N))−9/8]`. We may discard one
fixed finite initial range, so all demands compared below are
nonnegative and positive-part bookkeeping does not change (8).

By (4), the sum over good `k` of the lower bounds in (9) diverges:
`log(2N)=(k+2)log2`, whereas `Σ_k1/(2^(k+1)−1)<∞`.
This is a statement about individually normalized demands, not a sum
of independently reusable capacities.

For later reference, the individual normalized **terminal margin
improvement** includes both old and future moments. If `E_k` is
the old convolution energy, it is exactly

\[
 \Gamma_k=\frac{E_k+B_k^{\rm mom}-(2N-1)S}{16q^2}.
                                                               \tag{10}
\]

Since `E_k≥(3/2)N²S²/H`, these `Γ_k` also have divergent sum,
with a lower bound
`η²(3/2+12/33³)/(16 C_* log(2N))−1/[4(N−1)]`.
The word terminal in (10) is essential.

## 3. What coherence buys in a mixture of prefix matrices

Fix a finite terminal history containing all selected old prefixes.
For ranks `N_k`, put `q_k=binom(N_k,2)`, `H_k=h(N_k)`, and
`g_k=g 1_(F_(N_k))`. Given finite nonnegative coefficients `β_k`,
consider the matrix on the final physical label bank

\[
 {cal W}_\beta=
  \sum_k\frac{\beta_k}{q_k^2}
       \left[J_{F_{N_k}}+\frac{g_kg_k^\top}{8H_k^2}\right].
                                                               \tag{11}
\]

Its residual is PSD and centered in every actual birth class. For
`b=max(τ(d),τ(e))`, its residual entry is exactly

\[
 \frac{g_dg_e}{8}
       \sum_{k:N_k\ge b}\frac{\beta_k}{q_k^2H_k^2}.           \tag{12}
\]

Thus the block coefficient is a tail depending on the later source
birth. Its PSD property comes from the sum of actual nested outer
products, not from an assumed sign of individual entries.

For a literal restriction to `F_n`, let `v_k=min(n,N_k)` and
`V_v=Σ_(d∈F_v)g_d²`. Its exact mass and trace are

\[
 M({\cal W}_\beta|_{F_n})
       =\sum_k\beta_k\frac{q_{v_k}^2}{q_k^2},\qquad
 \operatorname{tr}({\cal W}_\beta|_{F_n})
       =\sum_k\frac{\beta_k}{q_k^2}
             \left(q_{v_k}+\frac{V_{v_k}}{8H_k^2}\right).
                                                               \tag{13}
\]

At the final bank the mass is `Σβ_k`, while the trace is at most
`(9/8)Σβ_k/q_k`. For unit coefficients on dyadic prefixes this
trace is uniformly bounded, although the mass grows with the number
of selected prefixes. A trace-class infinite positive operator can
therefore arise without a finite quadratic form on the constant
vector; that vector is not in the infinite label-space `ℓ²`.

Every summand in (11) has the two nonnegative scalar decompositions
`1±g_k/(sqrt(8)H_k)` on its own support. Thus it remains compatible
with the nonnegative-kernel budget. Formula (13) records the mass
and diagonal charges which a nested PSD-tail construction must pay.

## 4. One explicit coefficient choice, with the actual maximum retained

Select any finite collection `K` of sufficiently large good indices.
Use its actual disjoint future blocks `B_k` from §2. In the general
coefficient notation this choice is diagonal in the old/future indices:
the old row `k` is used only for `B_k`, with coefficient `q_k^{-2}`.
This is a current-row envelope, not the previously closed choice that
freezes every old kernel with a stationary coefficient at all later
shells.

For `t>0`, define full available row kernels

\[
 a_k(t)=\frac{1[t\notin F_{N_k}]}{q_k^2}
                \#\{d,d+t\in F_{N_k}\},\qquad
 r_k(t)=\frac{1[t\notin F_{N_k}]}{8q_k^2H_k^2}
                \sum_{d,d+t\in F_{N_k}}g_dg_{d+t}.           \tag{14}
\]

Here `a_k≥0` and `|r_k|≤a_k/8`, so `a_k+r_k≥0`.
The repeated use of `r` as an index-ratio symbol in §1 ends there;
in (14) it denotes this residual kernel only.

To keep the actual future-span mask, put `σ_k(t)=1[t≤L_k−1]` and

\[
 G_k^0=\sigma_ka_k,\quad G_k^W=\sigma_k(a_k+r_k),\qquad
 \mu_v(t)=\max_{k\in K}G_k^v(t),\quad C_v=\sum_t\mu_v(t).
                                                               \tag{15}
\]

For an empty selected family use zero maxima. All supports are finite.
On every actual label in `ΔB_k`, both masks are exact, and Sidon
difference injectivity makes these sets pairwise disjoint. Thus

\[
 D_v:=\sum_{k\in K}\delta_k^v/q_k^2\le C_v
                           \qquad(v=0,W).        \tag{16}
\]

This is the same one-copy physical inequality proved by
`growing_prefix_interval_envelope` in `PhysicalLabelEnvelope.lean`;
for `W` its local premise is now the additional two-channel moment
demand. That new premise is mathematically proved in the parent note,
not already a Lean theorem merely because the envelope bridge exists.

For clarity every unused contribution is retained. Let `T_0` contain
the finite support of all kernels, and let `V` be the positive
difference set of one actual terminal history containing the blocks.
Write `Dset=union_(k∈K)ΔB_k`. Then exactly

\[
 \begin{split}
 C_v-D_v={}&
 \sum_k\left[\sum_{t\in\Delta B_k}G_k^v(t)
                                      -\delta_k^v/q_k^2\right]\\
 &+\sum_{t\in(T_0\cap V)\setminus Dset}\mu_v(t)
   +\sum_{t\in T_0\setminus V}\mu_v(t)\\
 &+\sum_k\sum_{t\in\Delta B_k\cap T_0}
                                  [\mu_v(t)-G_k^v(t)].       \tag{17}
 \end{split}
\]

The second line includes every old, cross-shell, and other used label,
and every label unused at that actual terminal horizon. The first
line is the true local shadow surplus; the last is envelope slack.
Each term is nonnegative. No additional width or epoch copies of
the physical labels are introduced.

## 5. The exact coupling between individual gains and the envelope

Define the overlap reduction caused by taking a maximum,

\[
 O_v=\sum_k\sum_tG_k^v(t)-C_v\ge0,
 \qquad M_v=C_v-D_v\ge0.                         \tag{18}
\]

Define also the signed span correction

\[
 Z_k^{\rm span}=\sum_{t>L_k-1}r_k(t).
\]

The local **span-masked** margin improvement is
`Γ_k+Z_k^span`: removing the same span from both capacities changes
their difference by the removed residual sum. Subtracting the two
identities in (18) therefore gives the exact coupled formula

\[
 \boxed{\quad
 M_0-M_W=\sum_{k\in K}(\Gamma_k+Z_k^{\rm span})
                       +(O_W-O_0).
 \quad}                                          \tag{19}
\]

In particular the actual Sidon history must obey

\[
 \boxed{\quad
 \sum_{k\in K}\Gamma_k
 \le M_0+(O_0-O_W)-\sum_k Z_k^{\rm span}.
 \quad}                                          \tag{20}
\]

This is one concrete joint inequality for the specified coherent
coefficients, demands, and physical maximum. It preserves both the
new future moment and the whole baseline margin (17). If the span
mask is suppressed in a deliberately larger valid envelope, (19)–(20)
hold with `Z_k^span=0` and with the corresponding new `C_v,O_v,M_v`.
This alternative does not claim an unpriced gain from the actual span.

There is one useful unconditional stability bound, proved pointwise:

\[
 \frac78 O_0\le O_W\le\frac98 O_0.               \tag{21}
\]

For a finite nonnegative vector `(b_k)`, its overlap is
`Σb_k−max b_k=min_j Σ_(k≠j)b_k`. If every entry is multiplied
by a factor in `[7/8,9/8]`, the same bounds hold for this minimum.
Apply this observation at each `t` using
`(7/8)G_k^0≤G_k^W≤(9/8)G_k^0`, then sum. This proof also covers
zero entries and a one-element family.

Thus (20) yields the valid but weaker bound
`ΣΓ_k≤M_0+O_0/8−ΣZ_k^span`. Neither `O_0` nor `M_0` is
known to be bounded in the number of good epochs. The matrix tail
identity (12) has not supplied a sign for `O_W−O_0` or for the
span correction. The exact target sufficient for this selection is

\[
 M_0+(O_0-O_W)-\sum_k Z_k^{\rm span}
                 =o\!\left(\sum_{k\in K}\Gamma_k\right)
                                                               \tag{22}
\]

along increasing finite good-epoch families. Even a bounded right
side would suffice. Equation (22) is **not proved here**.

## 6. A coherent trace-class mixture does not give a free finite budget

The natural alternative is to use the single static matrix (11) and
restrict it at every history rank. Because every full matrix entry is
nonnegative, each component's physical correlation increases until
the target label is used and is zero under the mask thereafter. All
components have the same last eligible rank for that target. Hence
the full-history envelope of this matrix is exactly linear:

\[
 C_{\rm hist}({\cal W}_\beta)
       =\sum_k\frac{\beta_k}{q_k^2}
                           C_{\rm hist}^{N_k}(W_k).           \tag{23}
\]

After its support stops growing at `N_k`, a component cannot acquire
a larger eligible correlation. Formula (23) is the literal maximum
identity, not an estimate that discards the shared maximum.

This closes the assertion that the coherent residual's bounded trace
would automatically produce a bounded physical source. For the
actual infinite Sidon sequence `a_n=10^n`, the previously proved
classification in `growing_label_budget.md` §3.1 gives

\[
 C_{\rm hist}^{N}(J)
       =\binom{q_N}{2}-2\binom N3,
 \qquad C_{\rm hist}^{N}(J)/q_N^2\longrightarrow1/2.
\]

Since `W_k≥(7/8)J` entrywise, unit coefficients on dyadic prefixes
give from (23)

\[
 C_{\rm hist}({\cal W}_{1})\ge\frac7{16}|K|-O(1),
 \qquad \operatorname{tr}{\cal W}_{1}
                    \le\frac98\sum_k1/q_k=O(1).              \tag{24}
\]

No new finite search or repetition of the old example is needed:
the new conclusion is specifically that **this same birth-linear,
class-centered, coherent PSD-tail construction** still has finite
trace and unbounded physical capacity. The positions `10^n` violate
the cap and need not be good epochs. Thus (24) refutes only a
Sidon/coherence/trace-only argument, not (22) with its full cap and
good-epoch hypotheses.

Imposing `Σβ_k<∞` repairs the total mass but also makes the sum of
the guaranteed `β_k/log N_k` improvements finite. A free static
matrix mixture is therefore not the required endgame. This does not
rule out the genuinely changing current-row maximum (15), whose
precise outstanding obligation is (22).

## 7. Mathematical outcome of this bounded investigation

The new lookahead lemma is proved and supplies infinitely many
epochs with divergent reciprocal-log weight. The future moment
increases on their actual next blocks are proved, non-summable
individually, and paid by the same physical kernels. The coherent
nested residual has the exact tail, mass, and trace formulas
(11)–(13). The current-row physical envelope obeys the exact
coupling (19), including every old/cross/unused cost in (17).

The automatic trace-class-budget candidate is closed by (23)–(24).
The cap-dependent endgame (22) is unresolved; a finite bound for its
right side is not inferred from the divergence of the left side,
positive semidefiniteness, or class centering. The fixed-horizon
matrices used in this note do not constitute a proof of original Q1.
