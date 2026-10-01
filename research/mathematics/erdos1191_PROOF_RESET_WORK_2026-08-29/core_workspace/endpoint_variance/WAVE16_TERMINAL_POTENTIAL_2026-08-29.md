# Wave 16: terminal renewal absorption and a Fejer horizon taper

Date: 2026-08-29 (Asia/Tokyo)  
Status: **exact terminal-potential theorem and weighted horizon repair; the
disjoint-floor premium remains open**

Wave 15 found an adjacent-epoch allocation of the marginal promotion
`Delta_m` into the literal next Gothic bulk `mathfrak B_(2m)`.  Two issues
remained:

1. that literal bulk was already used by the Wave 10--11 lower floors; and
2. reindexing an unweighted finite horizon appeared to leave the terminal
   fan `mathfrak U_M=Theta(log M)=Theta(J)`.

This note proves that the second issue is not intrinsic.  The terminal
renewal tail, full-span term, and singleton absorb the whole terminal suffix
fan into a nonnegative potential.  The resulting terminal upper is only
`O_C(log log M)=O_C(log J)`.  A separate Fejer-type taper removes even the
adjacent-allocation horizon mismatch while preserving the harmonic lower
signal.  Neither argument supplies a premium over the already-used bulk
floor, so P17, P19, and Erdős Problem #1191 remain open.

Throughout, use the Wave 13 notation

\[
 Z_m=\mathfrak P_m+\mathfrak U_m-
     \mathfrak B_m-\mathfrak F_m-\mathfrak e_m
\tag{1}
\]

and the Wave 12 renewal identity

\[
 Y_m=R_m-R_{2m}+Z_m.
\tag{2}
\]

## 1. Adjacent-epoch coefficient audit

For the suffix atom

\[
 d_{m,p}=D_{p,2m-1},\qquad 2\le p\le2m-2,
\]

write `u_(m,p)` for its coefficient in `mathfrak U_m`.  Its copy in the
Wave 11 lower row of epoch `2m` has coefficient

\[
 v_{m,p}={4m-2p+1\over16m^2}.
\tag{3}
\]

The exact masses are

\[
 U_m={12m^2-28m+19\over16m^2},\qquad
 V_m:=\sum_{p=2}^{2m-2}v_{m,p}
 ={4m^2-4m-3\over16m^2}.
\tag{4}
\]

The mass of the next Gothic interior bulk is

\[
 B_{2m}={3(2m-1)^2\over16m^2}.
\tag{5}
\]

Consequently

\[
 \boxed{B_{2m}-U_m={m-1\over m^2}>0.}
\tag{6}
\]

Thus there is no coefficient-mass deficit in pairing a suffix fan with the
next interior bulk.  Wave 15's obstruction is instead about logarithmic
values and reuse of coefficient capacity already committed to a floor.

## 2. Exact terminal renewal potential

Put

\[
 A=D_{1,2m-1},\qquad
 c_m={ (2m-1)^2\over16m^2}.
\]

The finite boundary form for the next cut is

\[
 R_{2m}=\sum_{i=1}^{2m-2}{(2m-i)^2\over16m^2}
 \left(\log D_{i,2m-1}-\log D_{i+1,2m-1}\right).
\tag{7}
\]

Summation by parts in `i` gives the exact expansion

\[
 \boxed{
 R_{2m}=c_m\log A
 -\sum_{p=2}^{2m-2}v_{m,p}\log d_{m,p}
 -\mathfrak e_m.}
\tag{8}
\]

Indeed, the coefficient difference is

\[
 {(2m-p+1)^2-(2m-p)^2\over16m^2}=v_{m,p},
\]

and the last coefficient is `1/(4m^2)`, exactly the coefficient in
`mathfrak e_m`.

The coefficient checksums satisfy

\[
 U_m+V_m=F_m+c_m={ (m-1)^2\over m^2},
\tag{9}
\]

where `F_m=(12m^2-28m+15)/(16m^2)`.  Define

\[
 \begin{aligned}
 \mathcal T_m
 &:={}
 \mathfrak F_m+\mathfrak e_m+R_{2m}-\mathfrak U_m\\
 &={ (m-1)^2\over m^2}\log A
 -\sum_{p=2}^{2m-2}(u_{m,p}+v_{m,p})\log d_{m,p}.
 \end{aligned}
\tag{10}
\]

Every `d_(m,p)<=A`, and the two coefficient masses in the last line of
(10) agree by (9).  Hence

\[
 \boxed{\mathcal T_m\ge0.}
\tag{11}
\]

Substitution into (1) gives the exact terminal identity

\[
 \boxed{
 Z_m-R_{2m}=\mathfrak P_m-\mathfrak B_m-\mathcal T_m.}
\tag{12}
\]

This is the missing sign audit behind the apparent Wave 15 terminal fan.
The quantity `mathfrak U_m` must not be treated alone at the last horizon:
its full-span, singleton, and renewal-tail partners absorb it into the
nonnegative `mathcal T_m`.

## 3. Size of the true terminal residual

For a fixed `q`, `m<=q<=2m-2`, the coefficient of the prefix
`log D_(1,q)` is

\[
 c_{m,q}={2q-1\over4m^2}.
\]

The coefficients of all descendants in the corresponding `q`-row of
`mathfrak B_m` have the same total mass:

\[
 {q-3\over2m^2}+{1\over4m^2}+{1\over m^2}
 ={2q-1\over4m^2}.
\tag{13}
\]

Since every descendant is at most its prefix,

\[
 \mathfrak P_m-\mathfrak B_m\ge0.
\tag{14}
\]

For the upper direction, the Wave 11 interior triangular floor gives

\[
 \mathfrak B_m\ge K_m^{\rm int}
 ={3\over2}\log m+O(1),
\tag{15}
\]

while the common mass in (13), summed over `q`, is

\[
 B_m={3(m-1)^2\over4m^2}={3\over4}+O(m^{-1}).
\]

On an eventual-`C` branch,

\[
 \log A\le2\log m+\log\log(4m)+O_C(1).
\]

It follows from (12)--(15) that

\[
 \boxed{
 Z_m-R_{2m}
 \le \mathfrak P_m-\mathfrak B_m
 \le {3\over4}\log\log(4m)+O_C(1).}
\tag{16}
\]

At `m=M=2^J`, this is `O_C(log J)`, rather than the `Theta(J)` bound
obtained from `mathfrak U_M` alone.  Equation (16) does not give
`o(log J)`; the remaining terminal object is the scale-free prefix versus
descendant product, not the raw suffix fan.

## 4. A Fejer taper removes the allocation horizon mismatch

Let `m_k=2^k` and, for a horizon `J`, define decreasing weights

\[
 \omega_{k,J}=\left({J+1-k\over J+1}\right)^2,
 \qquad k_0\le k\le J.
\tag{17}
\]

They retain the harmonic scale:

\[
 \sum_{k=k_0}^J{\omega_{k,J}\over k}
 =\log J+O_{k_0}(1).
\tag{18}
\]

This follows by expanding
`omega/k=1/k-2/(J+1)+k/(J+1)^2`.  On the other hand,
`omega_(J,J)=1/(J+1)^2`; under the critical cap,

\[
 \omega_{J,J}\mathfrak U_{2^J}=O_C(J^{-1}).
\tag{19}
\]

The renewal telescoping also has the favorable sign.  From (2),

\[
\begin{aligned}
 \sum_{k=k_0}^J\omega_{k,J}Y_{m_k}
 ={}&\omega_{k_0,J}R_{m_{k_0}}
 +\sum_{k=k_0+1}^J
   (\omega_{k,J}-\omega_{k-1,J})R_{m_k}\\
 &-\omega_{J,J}R_{m_{J+1}}
 +\sum_{k=k_0}^J\omega_{k,J}Z_{m_k}.
\end{aligned}
\tag{20}
\]

All middle coefficients and the terminal coefficient in (20) are
nonpositive because the weights decrease and every `R` is nonnegative.

There is also no material loss when reindexing the Wave 15 adjacent
promotion allocations.  Its finite increment satisfies uniformly

\[
 \Delta_m\le\log13.
\tag{21}
\]

To prove (21), note that

\[
 K_p\le {4m-1\choose2}-{2m\choose2}=6m^2-5m+1,
 \qquad
 r_p\ge {m(m+1)\over2},
\]

so `K_p/r_p<12`; the total macroscopic `u`-mass is less than one.
If `E_m=O(m^{-2})` denotes the explicit summable Wave 15 small-value
error, then

\[
\begin{aligned}
 \omega_{k,J}\Delta_{m_k}
 \le{}&\omega_{k+1,J}\mathfrak B_{m_{k+1}}
 +(\omega_{k,J}-\omega_{k+1,J})\log13\\
 &+\omega_{k+1,J}E_{m_k}.
\end{aligned}
\tag{22}
\]

After summing (22), the weight-mismatch and error contributions are only
`O(1)`: the weight differences telescope and the dyadic errors are summable.
The main weighted bulk term remains explicit and is not being bounded by
`O(1)` here.  The unpaired terminal increment is at most
`log(13)/(J+1)^2`.

Thus a horizon-dependent decreasing taper simultaneously

- preserves a `Theta(log J)` harmonic lower signal;
- makes the raw terminal fan negligible;
- makes the adjacent-allocation weight mismatch `O(1)`; and
- gives favorable signs to all renewal boundary terms.

This is a valid alternate weighted route to a contradiction.  It is not a
proof of the unweighted P17 statement.

## 5. The obstruction which remains

Wave 15 uses literal `beta log D` capacity from `mathfrak B_(2m)` to pay
`Delta_m`.  The same coefficient capacity also supports
`K_(2m)^int`, the Wave 10 sorted floor, or another Abel lower floor.  Neither
the terminal potential (10) nor the taper (17) proves the disjoint premium

\[
 \mathfrak B_{2m}
 \ge K_{2m}^{\rm int}+\Delta_m-\epsilon_m
\tag{23}
\]

with a cumulatively negligible error.  More generally, the weighted route
still needs

\[
 \sum_{k=k_0}^{J-1}\omega_{k+1,J}
   \bigl(\mathfrak B_{m_{k+1}}-\text{chosen residual floor}\bigr)
 \ge
 \sum_{k=k_0}^{J-1}\omega_{k,J}\Delta_{m_k}
 -o(\log J).
\tag{24}
\]

This is now the exact bottleneck.  The `Theta(J)` terminal fan and the
finite-horizon reindexing error are not independent obstructions; the
coefficient-capacity overlap in (23)--(24) is.

No finite fixture, weighted identity, or terminal cancellation in this note
is promoted to an infinite critical branch or to a solution of either
Erdős question.

## 6. Exact algebra certificate

The deterministic audit files are

- `wave16_terminal_potential_certificate.py`;
- `test_wave16_terminal_potential_certificate.py`;
- `wave16_terminal_potential_certificate_2026-08-29.json`.

They check with `Fraction`, for every dyadic `m=4,...,2048`, the `U`, `V`,
`F`, cut-full, and next-bulk mass formulas, every coefficient in (8), the
singleton cancellation, (9), (13), and the rational inequality behind
`Delta_m<log 13`.  They also check the exact Fejer harmonic expansion,
decreasing weights, and renewal signs through horizon 256.  The committed
certificate replays byte-for-byte.  The focused verification was

```text
3 tests passed
Ruff check: clean
Ruff format: clean
```

Its scope flags explicitly keep the disjoint-floor premium, P19, both Erdős
questions, and prize readiness false.
