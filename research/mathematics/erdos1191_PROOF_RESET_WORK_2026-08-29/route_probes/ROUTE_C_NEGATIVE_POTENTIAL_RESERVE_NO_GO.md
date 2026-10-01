# Route C: isolated negative-potential reserve payment no-go

Date: 2026-08-30  
Status: `EXACT_SCALE_PHASE_INTEGRATED_RESERVE_NO_GO_CONSTANT_FRACTION_PSD_MARGINAL_PAIR_PRICE_NO_GO`

This note tests whether the unused positive finite-potential budget from the
pair-owned allocation can be reinterpreted as a nonnegative reserve which pays
the active coefficient-PSD price, the signless pair-lift diagonal price, or the
finite scale terminal.  It cannot do so universally.  The failure already
occurs at one scale and one phase of an eight-mark Golomb ruler, persists after
the exact continuum-phase integral, and becomes arbitrarily severe for the
coefficient-PSD, marginal-only, and integrated pair-lift prices on an explicit
Golomb family.

The scope is deliberately narrow.  The result rules out only using the
**magnitude** of the negative-`lambda` finite-horizon potential as an isolated
nonnegative payment.  It does not rule out retaining the negative rows with
their exact signed kernels inside the ordered Gram coupling, using cross-epoch
or cross-phase cancellation, or embedding all rows in a larger master.  It
does not resolve C058, either question in Erdős Problem #1191, publication
novelty, or a prize claim.

## 1. Exact reserve identity

Fix one Wave epoch and put `H=D_(n,2n-1)`.  Separate the finite-horizon scale
density into its positive strict-interior and negative-boundary parts:

\[
 P_n^+(T)=\sum_{\gamma}\beta_\gamma R_T(d_\gamma),
 \qquad
 N_n(T)=\sum_{\lambda_{p,q}<0}(-\lambda_{p,q})R_T(D_{p,q}).
 \tag{1.1}
\]

The superscript in `P_n^+` is essential: this is the positive-potential
density, not the coefficient-PSD price denoted below by `P_n^{PSD}`.  The
mixed-difference identity is

\[
 Q_n(T)=P_n^+(T)-N_n(T),\qquad 0\le Q_n(T)\le P_n^+(T).
 \tag{1.2}
\]

Let

\[
 \mathcal G_n=\sum_\gamma\beta_\gamma F_H(d_\gamma),
 \qquad
 \mathcal U_n=\mathcal G_n-\mathcal W_n.
\]

Then the unused positive budget is exactly the negative-potential magnitude:

\[
 \boxed{
 \mathcal U_n
 =\sum_{\lambda_{p,q}<0}(-\lambda_{p,q})F_H(D_{p,q})
 =\int_0^H N_n(T)\,dT.}
 \tag{1.3}
\]

For `T_r=2^(r+theta)`, the logarithmic change of variables also gives

\[
 \boxed{
 (\log2)\int_0^1\sum_{r:T_r\le H}T_rN_n(T_r)\,d\theta
 =\mathcal U_n.}
 \tag{1.4}
\]

Thus `T_r N_n(T_r)` is the exact phasewise unused capacity.  Equations
(1.3)--(1.4) grant the isolated-reserve proposal its strongest natural
interpretation; the counterexamples below still defeat it.

## 2. Minimal Wave-order exact fixture and one-scale failure

Take `n=4` and

\[
 A=(0,2,5,16,22,23,31,35).
 \tag{2.1}
\]

Its 28 positive differences are

\[
\begin{split}
&1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,\
&22,23,26,29,30,31,33,35,
\end{split}
\tag{2.2}
\]

so it is a Golomb ruler.  Its current gaps and horizon are

\[
 (h_4,h_5,h_6,h_7)=(6,1,8,4),\qquad H=19.
 \tag{2.3}
\]

The positive owners and absolute negative rows are

\[
 \begin{array}{c|ccc}
 d_\gamma&1&8&9\\ \hline
 \beta_\gamma&1/16&1/16&1/64
 \end{array}
 \tag{2.4}
\]

and

\[
 \begin{array}{c|cccc}
 D&7&15&12&13\\ \hline
 -\lambda&1/16&5/64&1/16&5/64.
 \end{array}
 \tag{2.5}
\]

At `T=2`, every negative row is inactive, while only the owner at distance
one and the Wave edge `(4,6)` are active.  Directly,

\[
 N_4(2)=0,qquad P_4^+(2)=Q_4(2)={1\over64}.
 \tag{2.6}
\]

For the active edge, `g_4(2)=g_6(2)=1` and `alpha_(4,6)=1/16`.  Hence

\[
 P_4^{\rm PSD}(2)={1\over16},qquad V_4(2)={1\over32},
 \tag{2.7}
\]

where `V_4` is the ordered-strip marginal price.  This realizes the exact
hierarchy

\[
 Q_4(2)={1\over64}<V_4(2)={P_4^{\rm PSD}(2)\over2}.
\]

The proportional pair allocation has

\[
 x={1\over32},\qquad v=2R_2(1)={1\over2},\qquad a={x\over v}={1\over16}.
\]

Its full signless-completion price attributable to this scale, including the
tail accounting, is

\[
 {2a\over T}={1\over16},
 \tag{2.8}
\]

against unused capacity `T N_4(T)=0`.  Therefore the isolated reserve cannot
pay any positive pointwise fraction of the PSD, marginal, or pair-lift price.

## 3. One complete phase: even the finite terminal is too large

Choose the log phase whose last dyadic width at most `H=19` is `U=10`.  The
active grid is

\[
 \ldots,{5\over4},{5\over2},5,10,qquad 20>H.
\]

The quotient `q(T)=Q_4(T)/P_4^+(T)` equals one at the first three displayed
widths and `11/15` at `T=10`.  The nonzero owner coefficients are

\[
\begin{array}{c|ccc|c}
T&a_{d=1}&a_{d=8}&a_{d=9}&T N_4(T)\\ \hline
5/4&5/128&0&0&0\\
5/2&5/64&0&0&0\\
5&5/32&0&0&0\\
10&11/48&11/48&11/192&3/160.
\end{array}
\tag{3.1}
\]

Thus

\[
 (s_1,s_8,s_9)=\left({193\over384},{11\over48},{11\over192}\right),
 \qquad \sum s={101\over128}.
 \tag{3.2}
\]

The complete phasewise unused reserve is only

\[
 \mathcal U_{4,\theta}=\sum_rT_rN_4(T_r)={3\over160}.
 \tag{3.3}
\]

In contrast, the pair-lift signless price, terminal diagonal price, and
terminal off-diagonal row are respectively

\[
 \mathcal D_{4,\theta}
 =2\sum_{\gamma,r}{a_{\gamma,r}\over T_r}
 ={93\over320},
 \tag{3.4}
\]

\[
 \mathcal T^{\rm diag}_{4,\theta}
 ={1\over U}\sum_\gamma s_{\gamma,U}
 ={101\over1280},
 \tag{3.5}
\]

\[
 \mathcal T^{\rm off}_{4,\theta}
 =\sum_\gamma s_{\gamma,U}\,2R_{2U}(d_\gamma)
 ={331\over5120}.
 \tag{3.6}
\]

Their exact ratios to (3.3) are

\[
 {\mathcal D_{4,\theta}\over\mathcal U_{4,\theta}}={31\over2},
 \qquad
 {\mathcal T^{\rm diag}_{4,\theta}\over\mathcal U_{4,\theta}}={101\over24},
 \qquad
 {\mathcal T^{\rm off}_{4,\theta}\over\mathcal U_{4,\theta}}={331\over96}.
 \tag{3.7}
\]

This is a phasewise obstruction to the terminal itself, not merely to its
diagonal PSD completion.

## 4. Integrated separations

For the fixture (2.1), the exact reserve is

\[
\begin{split}
 \mathcal U_4={}&{1\over16}\log{19\over7}
 +{5\over64}\log{19\over15}
 +{1\over16}\log{19\over12}
 +{5\over64}\log{19\over13}-{63\over608}.
\end{split}
\tag{4.1}
\]

For `x>1`, set `z=(x-1)/(x+1)`.  The exact atanh bounds

\[
 2z<\log x<2\left(z+{z^3\over3(1-z^2)}\right)
 \tag{4.2}
\]

give

\[
 \boxed{
 \mathcal U_4
 <{75853397\over2099365632}
 \approx0.03613158.}
 \tag{4.3}
\]

The actual value is about `0.03562590140`; decimals are not used in any
separation below.

### 4.1 Active coefficient-PSD price

The exact C069 price is

\[
 \Pi_4={1\over8}\log6+{109\over416}
 -{23\sqrt3\over240}+{5\sqrt6\over152}
 \approx0.4005762825.
 \tag{4.4}
\]

A shorter rational proof of failure uses only the `(4,6)` Wave atom:

\[
 \Pi_4\ge2\mathcal W_4
 \ge {1\over8}\log{21\over5}
 >{2\over13}.
 \tag{4.5}
\]

Combining (4.3)--(4.5),

\[
 {2\over13}-{75853397\over2099365632}
 ={19009687\over161489664}>0.
 \tag{4.6}
\]

Numerically `Pi_4/U_4` is about `11.24396`.

### 4.2 Integrated pair-lift signless price

Let `B(T)` be the sum of the active positive `beta` coefficients and
`q(T)=Q_4(T)/P_4^+(T)`.  The continuum-phase form of the exact price (3.4) is

\[
 \mathcal D_4
 :=(\log2)\int_0^1\mathcal D_{4,\theta}\,d\theta
 =\int_0^H {B(T)q(T)\over T}\,dT.
 \tag{4.7}
\]

On `1<T<7`, `N_4(T)=0`, `q(T)=1`, and `B(T)=1/16`.  Therefore

\[
 \mathcal D_4\ge {1\over16}\log7>{3\over32},
 \tag{4.8}
\]

and

\[
 {3\over32}-{75853397\over2099365632}
 ={120962131\over2099365632}>0.
 \tag{4.9}
\]

For reference, exact integration of the rational pieces gives

\[
\begin{split}
\mathcal D_4={}&{1\over16}\log7
-{3\over8}\log{8\over7}+{3\over8}\log{7\over6}
+{1\over36}\log{9\over8}+{5\over144}\log{9\over7}\\
&+{17\over320}\log{4\over3}+{1\over40}\log{7\over4}
-{31\over320}\log{13\over12}+{9\over80}\log{8\over7}\\
&-{3\over10}\log{15\over13}+{19\over80}\log{5\over4}
-{171\over320}\log{19\over15}+{63\over160}\log{7\over5},
\end{split}
\tag{4.10}
\]

which is about `0.1941232428`, or `5.44894` times the reserve.

### 4.3 Integrated finite terminal

As the phase varies, the last width `U(theta)` runs log-uniformly over
`[19/2,19]`.  Normalize the off-diagonal terminal by

\[
 \mathcal T_4^{\rm off}
 :=(\log2)\int_0^1
 \sum_\gamma s_{\gamma,U(\theta)}
 v_{\gamma,U(\theta)+1}\,d\theta.
 \tag{4.11}
\]

For an allocation at `T=U/2^m`, its contribution to the integrand after the
logarithmic change of variables is

\[
 {\beta_\gamma q(U/2^m)\over2^{m+2}}
 {2U-d_\gamma\over U^2}\,dU.
 \tag{4.12}
\]

On every linearity interval, `q` is a ratio of affine functions whose exact
derivative numerator is nonpositive.  Split `[19/2,19]` at every integer.
Replace `q(U/2^m)` by its right-end value and each logarithm by the lower
bound in (4.2).  The ten exact rational contributions are

\[
\begin{array}{c|c}
U\text{ interval}&\text{lower contribution}\\ \hline
[19/2,10]&2501/758784\\
[10,11]&21529/3548160\\
[11,12]&8609/1554432\\
[12,13]&4841/998400\\
[13,14]&91603/22643712\\
[14,15]&45203/13511680\\
[15,16]&50943/19554304\\
[16,17]&50273/18382848\\
[17,18]&318499/142571520\\
[18,19]&6167/3151872.
\end{array}
\tag{4.13}
\]

Their sum gives

\[
 \mathcal T_4^{\rm off}
 >{48804306505243169\over1330823143467417600}
 >\mathcal U_4,
 \tag{4.14}
\]

with the exact separated margin

\[
 {719563809873569\over1330823143467417600}>0.
 \tag{4.15}
\]

The direct exact-log value is about `0.03827132077`.  The terminal diagonal
price is termwise larger because

\[
 2R_{2U}(d)={1\over U}-{d\over2U^2}<{1\over U};
\]

its exact-log value is about `0.04438246020`.  Thus the integrated reserve
cannot pay either terminal quantity.

## 5. No constant-fraction payment of the PSD, marginal, or pair-lift price

For every integer `L>=26`, define

\[
 A_L=(0,2,5,16,L+16,L+17,L+25,3L+25).
 \tag{5.1}
\]

The affine positive differences split by their coefficient of `L`:

\[
\begin{array}{c|l}
0&1,2,3,5,8,9,11,14,16\\
1&0,1,9,11,12,14,15,16,17,20,23,25\\
2&0,8,9\\
3&9,20,23,25.
\end{array}
\tag{5.2}
\]

Each row has distinct constants.  At `L=26`, the margins between consecutive
rows are `10,1,26`, and these margins increase thereafter.  Hence every
`A_L` is a Golomb ruler.  Its current gaps and horizon are

\[
 (L,1,8,2L),\qquad H_L=3L+9.
\]

The four negative distances are `L+1,L+9,2L+8,2L+9`, with coefficients
`1/16,5/64,1/16,5/64`, respectively.  Since

\[
 F_H(d)=\log{H\over d}-1+{d\over H},
\]

the reserve is exactly

\[
\begin{aligned}
 \mathcal U_L={}&{1\over16}F_{H_L}(L+1)
 +{5\over64}F_{H_L}(L+9)\\
 &+{1\over16}F_{H_L}(2L+8)
 +{5\over64}F_{H_L}(2L+9).
\end{aligned}
\]

Here `H_L/(L+1),H_L/(L+9)` tend to `3`, the other two horizon ratios tend
to `3/2`, and the corresponding `d/H_L` ratios tend to `1/3,1/3,2/3,2/3`.
Thus the logarithmic part tends to `(9/64) log(9/2)`, while the `-1+d/H_L`
part tends to `-9/64`.  Consequently

\[
 \mathcal U_L\longrightarrow
 {9\over64}\left(\log{9\over2}-1\right)<\infty.
 \tag{5.3}
\]

For `9<T<L+1`, all three positive owners are active and every negative row is
inactive.  Hence

\[
 \mathcal D_L\ge {9\over64}\log{L+1\over9}\longrightarrow\infty.
 \tag{5.4}
\]

There is an equally direct ordered-marginal lower bound.  For `9<T<L`, edge
`(4,7)` is active because

\[
 M_{4,7}=1+8=9<T<D_{4,7}=H_L=3L+9.
\]

Moreover `h_4=L` and `h_7=2L`, so

\[
 \mu_4(T)={g_4(T)\over2}={1\over T},
 \qquad
 \nu_7(T)={g_7(T)\over2}={1\over T}.
\]

In the transport dual for `V_L(T)`, set `y_(4,7)=1/T` and every other load to
zero.  The only nonzero row sum is `1/T=mu_4`, the only nonzero column sum is
`1/T=nu_7`, and all remaining sums are zero.  Thus every dual capacity
constraint is met.  Since `alpha_(4,7)=9/64`, its objective value is
`9/(64T)`, and

\[
 V_L(T)\ge {9\over64T}.
\]

Consequently the integrated marginal-only price obeys

\[
 \mathcal V_L:=\int_0^\infty V_L(T)\,dT
 \ge {9\over64}\log{L\over9}\longrightarrow\infty.
 \tag{5.5}
\]

The long edge `(4,7)` has cross ratio

\[
 \exp C_{4,7}(L)
 ={(L+9)(2L+9)\over9(3L+9)}.
\]

Therefore

\[
 \Pi_L\ge2\mathcal W_L
 \ge {9\over32}\log{(L+9)(2L+9)\over9(3L+9)}
 \longrightarrow\infty.
 \tag{5.6}
\]

Equations (5.3)--(5.6) prove

\[
 {\mathcal U_L\over\mathcal D_L}\to0,
 \qquad
 {\mathcal U_L\over\mathcal V_L}\to0,
 \qquad
 {\mathcal U_L\over\Pi_L}\to0.
 \tag{5.7}
\]

Thus no positive universal fraction of any of these three integrated prices
can be paid by the isolated reserve.  Equation (5.7) makes no
constant-fraction claim about the terminal; for that component, (3.7) and
(4.14) prove failure only of full payment.

## 6. Relation to the ordered-Gram marginal price

The hierarchy from the ordered-strip memo is

\[
 Q_n(T)\le V_n(T)\le {P_n^{\rm PSD}(T)\over2}.
\]

Equation (2.7) is exactly consistent with it.  On the separate C070 fixture,
the ordered-marginal memo proves `G_4<V_4`.  Since
`U_4=G_4-W_4<G_4`, the isolated unused reserve fails to pay that marginal
price a fortiori.  None of these scalar comparisons excludes using the exact
intersection masses `|R_i intersect L_j|` together with the signed negative
rows in one master.

## 7. Exact replay and scope

The companion files

- `negative_potential_reserve_certificate.py`,
- `negative_potential_reserve_certificate.json`, and
- `test_negative_potential_reserve_certificate.py`

replay all 28 Golomb differences, the exact negative and positive rows, the
`T=2` zero-reserve fixture, every coefficient in the `U=10` phase, the three
integrated rational separations, piecewise monotonicity of `q`, and the affine
difference proof for (5.1).  The focused suite passes **13 tests** and rejects
**12 semantic mutations**.  Deterministic payload SHA-256:

`b102f5345497519321b04695c4f8cde068b08367530cfef215a16dc4f86927f0`

Companion-file SHA-256 values after final replay:

- `negative_potential_reserve_certificate.py`:
  `433732651af98b58cdf39dcc6bca4a02aa499967356c1f2e23f61ee6e7c2e9a2`
- `test_negative_potential_reserve_certificate.py`:
  `8af2817efdd2cb23ec9bfe2640580683164380fbdb9ad057965f736a07854963`
- `negative_potential_reserve_certificate.json`:
  `d198c93d6a6f677fdcd06ad93aafe90bb586c91e56aabd12c16eaa31e9137400`

From this directory, run

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v \
  test_negative_potential_reserve_certificate.py
PYTHONDONTWRITEBYTECODE=1 python3 negative_potential_reserve_certificate.py \
  --verify negative_potential_reserve_certificate.json --self-check
```

The certificate keeps every surviving scope flag false.  In particular it
does not promote finite exact arithmetic into an infinite-branch theorem and
does not claim that the exact signed negative rows, ordered Gram intersection
route, cross-epoch payments, or larger masters are impossible.
