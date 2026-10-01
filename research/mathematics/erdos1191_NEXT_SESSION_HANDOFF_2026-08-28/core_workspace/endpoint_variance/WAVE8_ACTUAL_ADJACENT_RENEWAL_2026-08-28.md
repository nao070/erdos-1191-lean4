# Wave 8 actual-adjacent renewal and the exact shell-H comparison

Date: 2026-08-28  
Status: two universal finite theorems and one exact covariance comparison;
the required infinite-history `o(log J)` innovation budget is still open.

## 1. Purpose and scope

Wave 7's cheap-child argument attached the tax `m-1` to every active dyadic
epoch, but old-child adjacent sets are nested.  This left debt 63 in the
authenticated 128-mark audit.  The present note removes the artificial
choice of a certified child bound: it records the *actual* largest newborn
internal adjacent gap and proves an exact renewal alternative.

The same calculation also evaluates the fixed adjoint matrix `H` on every
newborn-shell secant.  This keeps the signed off-diagonal term exactly and
shows that it cannot cancel the shell covariance.  These are rigorous local
advances, not a resolution of Erdős Problem #1191.

Throughout, `A=(a_0<a_1<...)` is normalized by `a_0=0` and every positive
difference `a_j-a_i` is distinct.  At a dyadic boundary `m -> 2m`, write

\[
 \tau_{m,k}=D_m^-+D_m^+ + k\max(\mu_m^-,\mu_m^+),
 \qquad 1\le k\le m,
\]

for the proved Wave 6 cross-antidiagonal activation threshold.

## 2. The hybrid actual-adjacent ledger

For every `(m,k)`, retain the `k` Wave 6 cross pairs

\[
 (m-1-t,m-1+k-t),\qquad 0\le t<k.
\tag{1}
\]

They have distinct positive differences at most `tau_(m,k)`.  For every
`m>=2`, add the newborn internal-adjacent family

\[
 I_m=\{(m,m+1),(m+1,m+2),\ldots,(2m-2,2m-1)\},
\tag{2}
\]

of demand `m-1`, and activate it at the *actual* threshold

\[
 \delta_m=\max_{m+1\le r\le2m-1}(a_r-a_{r-1}).
\tag{3}
\]

### Theorem 1 (hybrid capacity)

For every finite Golomb ruler and every real `T>=0`,

\[
 \boxed{
 \sum_{m,k:\,\tau_{m,k}\le T} k
 +\sum_{m\ge2:\,\delta_m\le T}(m-1)
 \le \lfloor T\rfloor .}
\tag{4}
\]

#### Proof

Every pair in (1) crosses its unique dyadic birth boundary.  Pairs from
different cross families are therefore disjoint.  Every pair in (2) has both
endpoints in the newborn block `[m,2m)`, so these pairs are disjoint across
dyadic epochs and from all selected cross pairs.  The Golomb property turns
distinct endpoint pairs into distinct positive integer differences.  When a
family is active, all its differences lie in `{1,...,floor(T)}`.  Counting
that set proves (4).  No growth envelope or extension hypothesis is used.

Expanding each demand into unit atoms, ordering their thresholds
`gamma_1<=...<=gamma_P`, and applying (4) at `gamma_r` gives `r<=gamma_r`.
Consequently the exact finite layer-cake corollary is

\[
 \sum_{m,k}\frac{k}{\tau_{m,k}}
 +\sum_{m\ge2}\frac{m-1}{\delta_m}
 \le H_P,
\tag{5}
\]

where `P` is the total selected demand.  The truncated version follows by
the same argument at every cutoff.

For `(0,1,4,6)`, the five selected differences are exactly `1,2,3,4,5`.
The four activation rows are

| threshold | cumulative demand | capacity margin |
|---:|---:|---:|
| `1` | 1 | 0 |
| `2` | 2 | 0 |
| `3` | 3 | 0 |
| `11/2` | 5 | 0 |

Thus the endpoint and rounding conventions are sharp.

## 3. Exact old-clear/new-pay renewal

Put

\[
 B_m^- = \mu_m^-+2D_m^-,\qquad
 B_m^+ = \mu_m^++2D_m^+,
 \qquad \tau_m=\tau_{m,1}.
\]

Every old internal adjacent gap is at most `B_m^-`, and every newborn
internal adjacent gap is at most `B_m^+`: each gap is the difference of two
successive discrepancy equations.  Moreover,

\[
 \boxed{\min(B_m^-,B_m^+)\le\tau_m.}
\tag{6}
\]

Indeed, if both certified bounds exceeded `tau_m`, the old inequality would
force `D_m^->D_m^+`, while the new inequality would force
`D_m^+>D_m^-`, a contradiction.

### Theorem 2 (renewal dichotomy)

At every nontrivial dyadic epoch, at least one of the following holds:

1. `delta_m<=tau_m`, so the current newborn internal family is already paid;
2. every old adjacent gap is at most `tau_m`, so every earlier dyadic
   internal-adjacent family and every earlier dyadic boundary gap is cleared.

This follows immediately from (6).  In the second case all earlier listed
gaps occur among indices `1,...,m-1`.

Neither alternative can be deleted.  Exact eight-mark Golomb witnesses are:

- old-clear only:
  `(0,76,413,471,595,1283,1424,1624)`, with
  `tau_4=2731/4`, old maximum `337`, and newborn maximum `688`;
- new-pay only:
  `(0,768,1064,1216,1303,1423,1676,1922)`, with
  `tau_4=1507/2`, old maximum `768`, and newborn maximum `253`.

Thus this is a genuine renewal alternative, not a disguised assertion that
one fixed orientation always works.

### Corollary 3 (single-debt renewal history)

Process the dyadic epochs in increasing order.  Pay `I_m` at its own
`tau_m` whenever `delta_m<=tau_m`.  Otherwise Theorem 2 first clears every
older internal family and then leaves only `I_m` outstanding.  It follows by
induction that

\[
 \boxed{\text{at most one internal-adjacent family is outstanding at any time.}}
\tag{7}
\]

Every outstanding family is paid at the next ancestry-clearing epoch.  If
there is no such epoch, every later newborn family is paid at birth, so at
most that single family can remain unpaid forever.  This statement uses one
fixed history and is therefore immune to the changing-terminal-window defect
of the Erdős--Turán counterexamples.

The exact 16-mark ruler

`(0,76,413,471,595,1283,1424,1624,1694,1925,2015,2016,2059,2188,2261,2333)`

exercises the nontrivial transition: the `m=4` family has actual threshold
`688` and is unpaid at birth, then the `m=8` ancestry clear pays it at
`tau_8=5983/8`.

On the authenticated 128-mark fixture, every epoch through `m=64` happens to
pay both actual sides, although only the old side is certified by the
discrepancy bounds.  At `m=64`,

\[
 \tau_{64,1}=1198199/32,\quad
 \max(\text{old internal gaps})=8567,\quad
 \delta_{64}=24962.
\]

This explains why the earlier *certified-set* debt 63 does not represent an
actual failure of adjacent payment on that finite fixture.  It remains a
valid warning against summing nested certified old halves.

## 4. The fixed-adjoint shell quadratic form

The Wave 3 adjoint majorant is

\[
 H=\begin{pmatrix}16/15&8/105\\8/105&4/35\end{pmatrix},
 \qquad z(u)=(u(1-u),u).
\]

For newborn ranks `1/2<=u,v<1`, direct factorization gives

\[
 \boxed{
 (z(u)-z(v))^{\mathsf T}H(z(u)-z(v))
 =(u-v)^2q(1-u-v),}
\tag{8}
\]

where

\[
 q(x)=\frac{16}{15}x^2+\frac{16}{105}x+\frac4{35}.
\]

On `-1<=x<=0`, the quadratic has its minimum at `x=-1/14`; hence

\[
 \boxed{\frac{16}{147}\le q(x)\le\frac{36}{35}.}
\tag{9}
\]

The lower constant is attained, for example, by `u=1/2`, `v=4/7`; the upper
constant is the closed-interval endpoint value at `x=-1`.

Using the pairwise covariance identity, every probability measure `sigma`
supported on the newborn ranks satisfies

\[
 \boxed{
 \frac{16}{147}\operatorname{Var}_{\sigma}U
 \le \langle H,\operatorname{Cov}_{\sigma}z\rangle
 \le \frac{36}{35}\operatorname{Var}_{\sigma}U.}
\tag{10}
\]

Therefore the shell-covariance piece of the actual innovation obeys

\[
 \frac{16G}{147N_{2m}}\operatorname{Var}_{\sigma_m}U
 \le
 \left\langle H,\frac{G}{N_{2m}}
       \operatorname{Cov}_{\sigma_m}z\right\rangle
 \le
 \frac{36G}{35N_{2m}}\operatorname{Var}_{\sigma_m}U.
\tag{11}
\]

This is a useful localization and a no-go: the signed off-diagonal entry of
`H` cannot make the newborn covariance asymptotically disappear.  Any proof
of the required upper budget must control the shell rank variance (and the
separate rank-one mean term), rather than hope for cancellation inside the
shell covariance itself.

## 5. What this does and does not settle

Theorem 2 converts every first-cross activation into a precise event:
current-new payment or complete adjacent ancestry clearing.  Theorem 1 puts
the actual newborn payments into the same global integer-capacity ledger,
without the nested-set overcount that caused the Wave 7 debt.  Corollary 3
reduces the entire historical adjacent overlap to at most one family, rather
than the growing certified-set debt.  Equation (10)
then identifies the scalar shell statistic that must be charged.

Three gaps remain:

1. `delta_m` may exceed `tau_m` on old-clear epochs, as the first eight-mark
   witness proves;
2. the harmonic bound (5) is only logarithmic and by itself does not imply
   `o(log J)` on one infinite critical branch;
3. neither (4) nor (9) yet controls the rank-one mixture term
   `(N_mG/N_(2m)^2)d_md_m^T`.

Accordingly, P13 is narrowed but not discharged.  The next admissible bridge
must use non-adjacent newborn differences on old-clear epochs, or prove that
such epochs have sub-logarithmic innovation in one infinite critical branch.

The subsequent exact `kappa`-atom decomposition makes this interface still
sharper.  Its negative adjacent shell atoms are only the cross-boundary gap
`h_m` and the last internal gap `h_(2m-1)`; the other members of `I_m` are
positive assets.  The two notions of debt are therefore related but not
identical.  Moreover, under
`N_(2m)<=K(2m)^2 log(2m)`, those two negative adjacent atoms have the global
dyadic bound `(13/5)K log 2`.  Thus the remaining nonsummable shell object is
the proper non-adjacent prefix/suffix fan, together with the separate
rank-one Abel fan.  See `WAVE8_Q_ATOM_DECOMPOSITION_2026-08-28.md`.

## 6. Independent verifier

The companion files are:

- `wave8_actual_adjacent_renewal.py`;
- `test_wave8_actual_adjacent_renewal.py`.

The focused suite checks exact family pairs and differences, every threshold
capacity row, the reciprocal harmonic inequality, both exclusive sides of
the renewal alternative, a later repayment event, the authenticated
64/128-mark data, the secant factorization, the sharp lower constant, and
invalid-input mutations.  It contains ten tests and uses only integer and
`Fraction` arithmetic.
