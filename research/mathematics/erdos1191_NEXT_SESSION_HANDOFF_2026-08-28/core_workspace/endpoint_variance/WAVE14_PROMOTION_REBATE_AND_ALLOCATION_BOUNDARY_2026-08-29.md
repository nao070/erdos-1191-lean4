# Wave 14: the legal promotion rebate and the remaining signed allocation

Date: 2026-08-29 (Asia/Tokyo)  
Status: **rigorous next-scale rebate; no resolution of Erdős #1191**

This note connects the future-rank promotion theorem to the exact Wave 11
Abel bulk.  It identifies the part of the promotion premium which can be
inserted into an existing negative floor without overlap or a new allocation
theorem.  It also records the coefficient which remains unallocated.

The conclusion is deliberately limited.  The rebate is a genuine harmonic
term, but the current endpoint envelope is still much larger.  In particular,
none of the inequalities below proves `P17`, `P19`, Question 1, Question 2,
or a prize claim.

## 1. A frontier atom reappears in the next lower shell

Keep the Wave 13 terminal-suffix atom

\[
 d_{m,p}=D_{p,2m-1},\qquad 2\leq p\leq2m-2.
\tag{1}
\]

At epoch `2m`, the same interval is in the Wave 11 lower shell
`q=2m-1`.  Its interval length and negative Abel coefficient are

\[
 \ell_{m,p}=2m-p,
 \qquad
 v_{m,p}={2\ell_{m,p}+1\over4(2m)^2}
 ={4m-2p+1\over16m^2}.
\tag{2}
\]

Let

\[
 L_{m,p}=\binom{2m-p+1}{2},
 \qquad \rho_0=\rho_{2m}(d_{m,p}).
\tag{3}
\]

The marks inside the interval in (1) determine `L_(m,p)` distinct positive
subinterval differences, all at most `d_(m,p)`.  Global Golomb uniqueness and
integer spacing therefore give

\[
 L_{m,p}\leq\rho_0\leq\rho_\infty(d_{m,p})\leq d_{m,p}.
\tag{4}
\]

Consequently the following four-channel split is an exact identity, and
every term after the first is nonnegative:

\[
 \boxed{
 \log d_{m,p}
 =\log L_{m,p}
 +\log{\rho_0\over L_{m,p}}
 +\log{\rho_\infty(d_{m,p})\over\rho_0}
 +\log{d_{m,p}\over\rho_\infty(d_{m,p})}.}
\tag{5}
\]

Define the legally weighted promotion premium

\[
 \Phi_m=\sum_{p=2}^{2m-2}v_{m,p}
 \log{\rho_\infty(d_{m,p})\over\rho_{2m}(d_{m,p})}.
\tag{6}
\]

Termwise application of (5) to the next lower shell proves

\[
 \boxed{A_{2m}^{\rm low}\geq K_{2m}^{\rm low}+\Phi_m.}
\tag{7}
\]

This proof does not allocate the future witness pairs individually.  The
same future difference may promote several nested thresholds.  That causes
no problem for the simultaneous scalar rank inequalities in (4)--(7), but it
must not be reinterpreted as a bounded-overlap atom allocation.

## 2. Disjoint insertion into the Wave 11 floors

For `E_J={4,8,...,2^J}`, write

\[
 \Phi_{J-1}=\sum_{m\in E_{J-1}}\Phi_m.
\tag{8}
\]

The last epoch `2^J` is omitted because its suffix row does not enter the
lower shell until epoch `2^(J+1)`.  Summing (7) gives two valid strengthenings:

\[
 A_J\geq K_J^{\rm len}+\Phi_{J-1},
 \qquad
 A_J\geq K_J^{\rm mix}+\Phi_{J-1}.
\tag{9}
\]

For the mixed floor, this is disjoint because `K^mix` applies the triangular
floor to the lower shell and the global rearrangement only to the interior
bulk.  Hence, with

\[
 K_J^\star=\max\{K_J^{\rm len},K_J^{\rm mix}\},
\tag{10}
\]

one has

\[
 \boxed{A_J\geq K_J^\star+\Phi_{J-1}.}
\tag{11}
\]

Put

\[
 \widetilde G_J=A_J-K_J^\star-\Phi_{J-1}\geq0.
\tag{12}
\]

The exact Abel identity then becomes

\[
 \boxed{
 \sum_{m\in E_J}Y_m
 =(T_J-K_J^\star-\Phi_{J-1})-(\widetilde G_J+S_J).}
\tag{13}
\]

Equation (13) is an exact reorganization, not an upper estimate of the
required size.  The corresponding sufficient theorem would still have to
show

\[
 \widetilde G_J+S_J
 \geq T_J-K_J^\star-\Phi_{J-1}-o_C(\log J).
\tag{14}
\]

The known direct bound on the right-hand envelope remains
`O_C(J log J)`.

The premium in (6) must not be added blindly to the old Wave 10 globally
sorted floor `F_J`.  Its selected global rank may already incorporate some
of the same promotion.  Equations (7)--(11) avoid this double counting by
using the explicit next lower-shell copy.

## 3. The rebate is genuinely harmonic

The Wave 14 promotion theorem applies uniformly to the macroscopic suffix
`2<=p<=m`.  On any fixed eventual-`C` branch, for all sufficiently large
dyadic `m`, it gives

\[
 \log{\rho_\infty(d_{m,p})\over\rho_{2m}(d_{m,p})}
 \geq
 \log\left(1+{1\over64C\log d_{m,p}}\right).
\tag{15}
\]

The exact `v`-mass of this subfan is

\[
 V_m^{\rm macro}:=\sum_{p=2}^{m}v_{m,p}
 ={(m-1)(3m-1)\over16m^2}\longrightarrow{3\over16}.
\tag{16}
\]

The deliberately coarse displayed consequence of Wave 14,

\[
 \log{\rho_\infty(d_{m,p})\over\rho_{2m}(d_{m,p})}
 \geq{1\over512C\log m},
\tag{17}
\]

already yields

\[
 \Phi_m\geq{1\over3072C\log m}
\tag{18}
\]

eventually.  The sharper asymptotic constant follows directly from (15).
Uniformly over `2<=p<=m`,

\[
 \log d_{m,p}=(2+o_C(1))\log m,
\tag{19}
\]

because `binom(m+1,2)<=d_(m,p)<=4Cm^2 log(4m)`.  Combining (15),
(16), and `log(1+x)=x+O(x^2)` gives

\[
 \boxed{
 \Phi_m\geq
 \left({3\over2048}-o_C(1)\right){1\over C\log m}.}
\tag{20}
\]

An explicit, weaker eventual version is also available.  Once
`log d_(m,p)<=3log m`, `x=1/(64C log d_(m,p))<=1/3`, and
`V_m^macro>=1/6`, the inequality `log(1+x)>=3x/4` gives

\[
 \Phi_m\geq{1\over1536C\log m}.
\tag{21}
\]

Thus the legally insertable rebate is not sub-harmonic and is not
intrinsically constant-starved.  However, comparing (20) or (21) with the
separate Wave 13 lower bound for `Y_m` or `Z_m` does **not** prove
`Phi_m>=Y_m` or `Phi_m>=Z_m`: it would only compare two lower bounds.

## 4. The coefficient still lacking an allocation

The Wave 13 positive frontier coefficient is

\[
 u_{m,p}={12m-5-6p\over16m^2}
 \qquad(2\leq p\leq2m-3).
\tag{22}
\]

On the macroscopic subfan, its part not covered by the legal next-row copy is

\[
 \boxed{
 r_{m,p}:=u_{m,p}-v_{m,p}
 ={4m-2p-3\over8m^2}>0.}
\tag{23}
\]

Its exact mass is

\[
 \sum_{p=2}^{m}r_{m,p}
 ={(m-1)(3m-5)\over8m^2}\longrightarrow{3\over8}.
\tag{24}
\]

For completeness, the exceptional endpoint `p=2m-2` has residual
coefficient `3/(8m^2)` after comparison with its next lower-shell copy.

The remaining falsifiable task is therefore a signed allocation theorem for
the `r_(m,p)` channel: map a quantitatively sufficient part of its promotion
resource to unused negative interior-bulk or terminal-tail capacity, with a
proved bound on total reuse across atoms and epochs.  The same-epoch Gothic
bulk `mathfrak B_m` does not contain the next lower-shell copy in (2), so
(7) alone is not an upper bound for the Wave 13 frontier `X_m`.

This is the exact claim boundary.  Wave 14 proves future rank filling and a
legal harmonic rebate.  It does not prove the signed comparison which would
turn that resource into a contradiction to the Wave 13 frontier lower bound.
