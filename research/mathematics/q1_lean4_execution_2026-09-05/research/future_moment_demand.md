# A first-moment demand on the same physical difference budget

Date: 2026-09-05. Author: `/root`, GPT-6 Astra Ultra.
Status: supporting finite mathematical inequalities, not original Q1
or its Lean verification. The resulting demands must still be compared
with one actual shared envelope; separate envelopes are not added.

## 1. Exact support, including the forbidden locations

Let `F` be a finite nonempty subset of `{1,...,H}`, where `H` is a
positive integer. Put `q=|F|`. Let `z:F→R` satisfy

`sum_d z_d=0`, `S=sum_d z_d^2`, `mu=sum_d d z_d`.

Extend every label function by zero off `F`. Let `B` be an actual
integer Sidon set of `m>=1` points, whose smallest and largest points
are `b` and `b+L-1`, with `Delta B` disjoint from `F`. Define

`f_0(x)=sum_(a in B) 1_F(x-a)`,
`f_z(x)=sum_(a in B) z_(x-a)`.

Both functions are supported in the consecutive integer interval

`J={b+1,...,b+L+H-1}`, `T=|J|=L+H-1`.

At every `x` in `B` they vanish: a nonzero term would require a
positive difference of `B` to belong to `F`. Exactly `m-1` points
of `B` belong to `J`; the smallest point `b` does not. Therefore a
common support is

`Omega=J\B`, `D=|Omega|=L+H-m>0`.                  (1)

The strict positivity follows also from `sum f_0=mq>0`. All these
counts use the actual span of `B`, not an interval centered at a
conveniently chosen mean. The full-interval bound below may be used
if only an upper bound on that span is available.

The exact moments are

`sum f_0=mq`, `sum f_z=0`, `sum_x x f_z(x)=m mu`.   (2)

In the last identity the term involving `sum_(a in B)a` vanishes
because `sum z=0`.

## 2. Separate orthogonal channels give an additional positive energy

Write `c_Omega=D^(-1) sum_(x in Omega)x` and
`V_Omega=sum_(x in Omega)(x-c_Omega)^2`. If `mu!=0`, then
`V_Omega>0`: otherwise the common support has at most one point,
and the last two identities in (2) are incompatible.

Cauchy--Schwarz, applied separately to the two real channels, gives

`sum f_0^2 >= m^2 q^2/D`,
`sum f_z^2 >= m^2 mu^2/V_Omega` when `mu!=0`.       (3)

The second channel has zero mass. Its nonzero first moment is useful;
discarding it is not forced by the zero sum of the label coefficients.
For a bound not depending on the exact locations of the holes, let
`c_J=b+(L+H)/2`. Centering (2) at `c_J` instead gives, when `T>=2`,

`sum f_z^2 >= LB(B):=12m^2 mu^2/[T(T^2-1)]`.       (4)

Indeed `sum_(x in J)(x-c_J)^2=T(T^2-1)/12`, and replacing its
subset `Omega` by `J` only increases this squared-coordinate sum.
The optimal hole-aware bound in (3) is at least (4), since the mean
minimizes the sum of squared distances on `Omega`. If `mu=0`, define
the additional lower bound to be zero; no division by a vanishing
variance is needed. In the good-epoch application, `H>=binom(N,2)`
with `N>=4`, so `T>=2` automatically.

Choose `lambda>=0` with `W_de=1+lambda z_d z_e>=0` for every
`d,e` in `F`. The matrix `W=J+lambda zz^T` is PSD, has mass
`q^2`, and trace `q+lambda S`. For instance, `|z_d|<=1` and
`lambda=1/8` suffice. Its actual shadow energy has the two-channel
decomposition

`E_B(W)=sum_x [f_0(x)^2+lambda f_z(x)^2]`
`      >= m^2 q^2/D+lambda LB(B)`.                  (5)

The two Cauchy inequalities in (5) concern orthogonal feature
coordinates of the same matrix. They do not allocate separate physical
copies of any label pair.

## 3. The physical pair demand and its diagonal cost

Define the nonnegative physical kernel

`K_W(t)=sum_(d,e in F, d<e, e-d=t) W_de`, `t>0`.

Actual Sidon difference uniqueness in `B`, including repeated-sum
Sidonness, gives the exact expansion

`E_B(W)=m(q+lambda S)+2 sum_(t in Delta B) K_W(t)`. (6)

Combining (5)--(6) proves the new raw demand

`delta_mom(B,W)`
` = [m^2 q^2/D+lambda LB(B)-m(q+lambda S)]/2`
` <= sum_(t in Delta B) K_W(t)`.                   (7)

Thus its positive part is also bounded by the right side. The old
mass-only demand for the same matrix is exactly the expression in
(7) with `LB(B)=0`. The increase in raw demand is `lambda LB(B)/2`.
Both the old and the new demands retain the full diagonal term.
Their positive parts differ by this full amount whenever the old
raw demand is already nonnegative; this sign condition is not omitted.

For pairwise difference-disjoint compatible blocks `B_r`, (7) gives

`sum_r max(delta_mom(B_r,W),0)`
` <= sum_(t outside F) K_W(t)`
` = (q^2-q-lambda S)/2 - sum_(t in F) K_W(t)`.      (8)

The disjointness and compatibility are literal properties of blocks
belonging to the same actual Sidon history. Negative values of the
residual kernel `K_(zz^T)` are not removed separately: the kernel
being bounded in (8) is the nonnegative full `K_W`.

## 4. Literal prefix restrictions and the shared historical envelope

Fix one terminal history `P_N` and its linear coefficient vector

`z_(a_j-a_i)=(mean_(h<j) a_h-a_i)/H_N`.

At every old rank `n<=N`, let `F_n=Delta P_n`, `q_n=|F_n|`,
`S_n=sum_(d in F_n) z_d^2`, and use the literal restriction `W_n`.
Both class centering and the first moment hold exactly:

`sum_(d in F_n) z_d=0`,
`sum_(d in F_n) d z_d=H_N S_n`.                    (9)

The normalization on the right in (9) is the fixed terminal `H_N`,
not the smaller support width `H_n`. This distinction is necessary.
Apply (7) to each chosen compatible future block `B_r`, with old
rank `n_r`, actual length `L_r`, support width `H_(n_r)`, and moment
`mu_r=H_N S_(n_r)`. For the same family of actual disjoint pair sets,

`sum_r max(delta_mom(B_r,W_(n_r)),0)`
` <= sum_(t>0) max_r [1[t notin F_(n_r)]`
`                         1[t<=L_r-1] K_(W_(n_r))(t)]`.       (10)

The maximum of an empty family is zero. All sums have finite support.
To prove (10), sum (7) over the actual pair differences, use that
each physical `t` occurs for at most one chosen block, and then bound
its one eligible coefficient by the displayed maximum. The span mask
holds because an internal difference of `B_r` is at most `L_r-1`.

Thus the new moment terms enter the same exact physical envelope as
the existing mass-only demands. Equation (10) is not obtained by
summing an independent right side for every row. The old/cross/unused
accounting already proved for that envelope continues to apply.

## 5. The changed historical comparison for one terminal row

For `lambda=1/8`, let `X_z` be the causal mixed-birth cross energy
of the fixed centered feature. Its exact historical capacity change
is `C_hist(J)-C_hist(W)=X_z/8`. The mass-only baseline demand is
`delta_J=[m^2 q^2/D-mq]/2`. Equation (7) gives

`delta_mom(B,W)-delta_J=[LB(B)-mS]/16`.

Consequently the exact comparison between these two specified raw
lower bounds and the historical capacities is

`[C_hist(J)-delta_J]-[C_hist(W)-delta_mom(B,W)]`
`               =[2X_z+LB(B)-mS]/16`.             (11)

The term `LB(B)` is new relative to the previous comparison with
mass-only demand for `W`. It is nonnegative and can be of the same
asymptotic order as the old energy gain. Equation (11) still does
not assign a sign to `X_z`, and it does not establish that the
baseline gap on the left has a uniform summable surplus.

## 6. Size on epochs with a bounded one-block lookahead

Suppose `p` is even, `N=2p`, and one fixed `K>4` satisfies

`H_p>=2H_(p/2)`, `H_N<=K H_p`, `H_(2N)<=K H_N`.    (12)

The variance proof from `birth_linear_good_epoch.md`, with `K`
in place of eight, gives

`S>=eta q`, `eta=1/(128K^2)`, `mu=H_N S`.          (13)

Take the actual next block `B={a_(N+1),...,a_(2N)}`, so `m=N`.
Its length is at most `H_(2N)<=K H_N`, and
`T=L+H_N-1<=(K+1)H_N`. Equations (4), (12), and (13) imply

`LB(B)>=12N^2 S^2/[(K+1)^3 H_N]`
`      >=12eta^2 q^2/[(K+1)^3 C log(2N)]`          (14)

whenever `H_N<=C N^2 log(2N)`. We used
`T(T^2-1)<=T^3<=(K+1)^3 H_N^3`, with the correct inequality direction.

For `lambda=1/8`, the normalized increase in raw demand is therefore

`[delta_mom(B,W)-delta_mass(B,W)]/q^2`
`          >=3eta^2/[4(K+1)^3 C log(2N)]`.         (15)

The old raw demand for `W` is positive for all sufficiently large
such epochs. Indeed `S<=q` and `D<=T<=(K+1)H_N` give

`delta_mass(B,W)`
` >= (Nq/2)[(N-1)/(2C(K+1)log(2N))-9/8]`.        (16)

So (15) then applies to the difference of positive-part demands too.

The extended good-epoch argument is being proved separately in
`coherent_birth_linear_envelope.md`; for `K=32` it supplies a
divergent reciprocal-logarithm sum under one fixed eventual cap.
If that argument is used, the individually normalized increases in
(15) have divergent total size. Their physically shared expenditure
is still governed by (10); its right side has not been proved uniformly
bounded or beaten by these increases. Q1 and its final Lean verification
remain unresolved.
