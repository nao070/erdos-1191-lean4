# Wave 16: multiscale future-rank filling

Date: 2026-08-29 (Asia/Tokyo)  
Status: **rigorous constant-fraction rank filling; disjoint signed bulk allocation remains open**

Wave 14 used one future block to show that a macroscopic old difference gains
at least `d/(64 C log d)` future ranks on a hypothetical eventual-`C`
branch.  The same spatial-bin argument can be applied to many disjoint
future blocks.  Global Golomb uniqueness makes all of their witness
differences distinct, so their contributions add rather than merely repeat
the same lower bound.

The resulting gain is a fixed positive fraction of `d`, depending only on
`C`.  Consequently the Wave 14 promotion logarithm is bounded below by a
positive constant per suffix atom, not only by `1/log m`.  This is a genuine
strengthening, but it is still a positive rank resource.  No signed
allocation or terminal cancellation required for Erdős Problem #1191 is
proved here.

Throughout, let

\[
 0=a_0<a_1<a_2<\cdots
\]

be one fixed normalized integer Golomb ruler, and suppose that

\[
 a_n\leq Cn^2\log(2n)
\tag{1}
\]

for every sufficiently large `n`.

## 1. Disjoint multiscale blocks

Let `L` be sufficiently large that (1) holds from index `L` onward.  Let
`d` be a positive difference already present among the first `L` marks, and
assume

\[
 d\geq {L^2\over8}.
\tag{2}
\]

Put

\[
 T=\left\lfloor {1\over2}\log_2 L\right\rfloor,
 \qquad M_t=2^tL\quad(0\leq t\leq T),
\tag{3}
\]

and use the pairwise disjoint mark blocks

\[
 V_t=\{a_{M_t},a_{M_t+1},\ldots,a_{2M_t-1}\}.
\tag{4}
\]

Each block has `M_t` marks, and `M_t<=L^(3/2)`.  Partition the line into
half-open bins of width `d`, and let `B_t` be the number of bins occupied by
`V_t`.  Since `d<=a_(L-1)<=a_(2M_t-1)`,

\[
 \begin{aligned}
 B_t
 &\leq \left\lfloor {a_{2M_t-1}\over d}\right\rfloor+1\\
 &\leq {2a_{2M_t-1}\over d}
 <{8CM_t^2\log(4M_t)\over d}.
 \end{aligned}
\tag{5}
\]

Assume the explicit floor-safe side condition

\[
 \boxed{\sqrt L\geq128C\log(4L^{3/2}).}
\tag{6}
\]

Equations (2), (3), and (6) give, uniformly in `t`,

\[
 16CM_t\log(4M_t)
 \leq16CL^{3/2}\log(4L^{3/2})
 \leq {L^2\over8}
 \leq d.
\tag{7}
\]

Combining (5) and (7) yields `M_t>=2B_t`.

If the occupied-bin populations are `x_q`, the number `S_t` of same-bin
pairs in `V_t` therefore satisfies

\[
 \begin{aligned}
 S_t
 &=\sum_q\binom{x_q}{2}
 =\frac12\left(\sum_qx_q^2-M_t\right)\\
 &\geq\frac12\left({M_t^2\over B_t}-M_t\right)
 \geq {M_t^2\over4B_t}
 >{d\over32C\log(4M_t)}.
 \end{aligned}
\tag{8}
\]

For `L>=16`, one has
`log(4M_t)<=log(4L^(3/2))<=2log L`, and hence

\[
 \boxed{S_t>{d\over64C\log L}.}
\tag{9}
\]

Every pair counted by `S_t` has positive integer difference strictly less
than `d`.  The blocks in (4) are disjoint, and global Golomb uniqueness says
that no two different pairs anywhere in the ruler have the same positive
difference.  Thus:

- witnesses from different `t` are numerically distinct;
- none is a difference of the old `L`-mark prefix; and
- all are counted by `rho_infinity(d)-rho_L(d)`.

No selection compatibility issue remains.

## 2. Constant-fraction future-rank theorem

There are `T+1>(log L)/(2log 2)` blocks in (3).  Summing (9) proves the
following.

### Theorem 2.1 (multiscale future-rank filling)

Under (1), (2), and (6),

\[
 \boxed{
 \rho_\infty(d)-\rho_L(d)
 >{d\over128C\log2}.}
\tag{10}
\]

This is an infinite-branch theorem obtained from a finite collection of
future blocks depending on `L`.  It does not infer an infinite branch from
finite rulers.

The constant is deliberately conservative.  Extending the block family
closer to the largest scale allowed by `16CM log(4M)<=d` improves it, but
the fixed half-logarithmic family already removes the `1/log d` loss and
keeps every floor and endpoint explicit.

## 3. Application to the Wave 13 suffix fan

For a dyadic source epoch `m`, put

\[
 d_{m,p}=D_{p,2m-1}=a_{2m-1}-a_{p-1},
 \qquad 2\leq p\leq m.
\tag{11}
\]

Use `L=2m`.  The interval in (11) contains `2m-p+1>=m+1` marks, whose
pairwise differences are distinct positive integers at most `d_(m,p)`.
Therefore

\[
 d_{m,p}\geq\binom{m+1}{2}\geq{(2m)^2\over8}={L^2\over8}.
\tag{12}
\]

For every sufficiently large `m`, the side condition (6) holds.  Theorem
2.1 applies simultaneously to the complete macroscopic subfan.

Write

\[
 \kappa_C:=\log\left(1+{1\over128C\log2}\right)>0.
\tag{13}
\]

Integer distinctness gives `rho_(2m)(d)<=d`, so (10) implies

\[
 \boxed{
 \log{\rho_\infty(d_{m,p})\over\rho_{2m}(d_{m,p})}
 \geq\kappa_C
 \qquad(2\leq p\leq m).}
\tag{14}
\]

This replaces Wave 14's coarse `1/(512C log m)` lower bound by a positive
constant depending only on `C`.

The exact macroscopic Wave 14 coefficient masses now give three immediate
corollaries.  For `m>=20`,

\[
 \sum_{p=2}^{m}u_{m,p}
 ={(m-1)(9m-11)\over16m^2}\geq\frac12,
\]

and hence the full `u`-weighted promotion satisfies

\[
 \sum_{p=2}^{m}u_{m,p}
 \log{\rho_\infty(d_{m,p})\over\rho_{2m}(d_{m,p})}
 \geq {\kappa_C\over2}.
\tag{15}
\]

For the legal next-lower-shell coefficient `v_(m,p)`, its macroscopic mass
is at least `1/6` for `m>=12`, so

\[
 \boxed{\Phi_m\geq{\kappa_C\over6}.}
\tag{16}
\]

Finally, the unallocated residual coefficient `u-v` has mass at least
`1/3` for `m>=24`, giving the positive resource

\[
 \boxed{
 \Theta_m:=\sum_{p=2}^{m}(u_{m,p}-v_{m,p})
 \log{\rho_\infty(d_{m,p})\over\rho_{2m}(d_{m,p})}
 \geq{\kappa_C\over3}.}
\tag{17}
\]

In particular, the already legal Wave 14 insertion strengthens to

\[
 A_J\geq K_J^\star+{\kappa_C\over6}J-O_{C,\mathbf a}(1),
\tag{18}
\]

after harmless adjustment for the finite initial epochs and the missing
terminal source row.  The `J` in (18) denotes the number-scale endpoint in
`E_J={4,8,...,2^J}`; changing the finite starting index changes only the
constant.

## 4. The eventual-hole channel is uniformly bounded

Theorem 2.1 also gives

\[
 \rho_\infty(d_{m,p})>{d_{m,p}\over128C\log2}.
\tag{19}
\]

If `128C log 2<=1`, the strict inequality (19) contradicts the elementary upper bound
`rho_infinity(d)<=d`, so no branch satisfying all the hypotheses exists.
Otherwise,

\[
 \boxed{
 0\leq\log{d_{m,p}\over\rho_\infty(d_{m,p})}
 <\log(128C\log2).}
\tag{20}
\]

Thus the eventual numerical-hole part of every macroscopic suffix atom is
`O_C(1)`, uniformly in `m` and `p`.  This removes a possible `log log m`
loss from that particular channel.

## 5. Exact claim boundary

Equations (10), (14), and (20) are stronger than the Wave 14 one-block
promotion bounds.  They say that the future difference set fills a fixed
fraction of every macroscopic old suffix threshold on a hypothetical
eventually critical branch.

They do **not** prove a signed upper for
`X_m=mathfrak U_m-mathfrak B_m`.  In particular:

- `Phi_m` in (16) is already a legal lower-shell floor improvement, but its
  linear-in-`J` cumulative size does not by itself control the remaining
  endpoint envelope;
- `Theta_m` in (17) is positive and still has no disjoint negative carrier;
- the Wave 15 local allocation spends full next-bulk atom values and cannot
  be added again to an existing floor; and
- the isolated terminal `mathfrak U_(2^J)` fan appears only if the exact
  renewal tail is omitted.  The companion terminal-potential memo absorbs
  that fan, but it does not create disjoint next-bulk capacity.

Accordingly, `P19`, `P20`, `P21`, Questions 1 and 2, and the prize claim
remain open.  The next exact task is to combine constant-fraction rank filling
with a genuinely disjoint global rank/length floor, or an equivalent
bounded-reuse carrier for the residual promotion.
