# Wave 10: exact laminar tile LP and the W9-RLP zero-column obstruction

**Date:** 2026-08-29 (Asia/Tokyo)  
**Scope:** the Wave 9 hereditary rank-lag inequality, four-parameter tile
capacities, and the retained primitive cross-ratio/rank-variance objective  
**Status:** exact finite primal-dual certificate and a rigorous obstruction for
the tested relaxation; P15 and Erdős Problem #1191 remain open

## 1. Outcome

This probe implements the literal finite relaxation suggested at the end of
Wave 9. It produces two positive results and one decisive negative result.

1. A dynamic program checks `(W9-RLP)` for **every** subset of the audited
   dyadic epochs and **every** legal lag cutoff on the selected epochs. The
   compression is exact: at fixed total selected-difference count it keeps the
   smallest possible right-hand side.
2. Every observed genuine nonadjacent birth pair is placed in its Wave 9
   `(R,X,Y,Z)` tile. The per-epoch tile capacities and the cross-epoch numerical
   capacity define an integer LP. Each tile block has an explicit greedy primal
   and threshold dual, and the two values agree as exact fractions.
3. After the prefix moduli `N_(2m)` are fixed, every `(W9-RLP)` row has
   coefficient zero in every tile occupancy variable. Hence adjoining all such
   rows leaves the tile LP feasible set and optimum unchanged. The resulting
   exact dual is much too large and has no cross-epoch survival damping.

Thus the proposed LP architecture is incomplete in a precise sense. A useful
Wave 10 inequality must add a nonzero coupling between hereditary rank-lag
packing and either endpoint products, the primitive Abel state, or the exact
infinite-survival label. Merely putting the existing rows in one solver does not
create that coupling.

All LP and W9-RLP calculations are exact integer or `Fraction` arithmetic.
They make no infinite-branch inference.

## 2. Exhaustive all-subset W9-RLP audit

For each audited dyadic epoch `m`, let the cutoff variable take the values

\[
 q_m\in\{0,1,\ldots,m\}.
\]

Here `q_m=0` means that epoch `m` is omitted. Therefore every nonzero vector
`(q_m)` is exactly one choice of a nonempty epoch subset together with one legal
positive cutoff on each selected epoch. Put

\[
 M=\sum_m m q_m,
 \qquad
 R=\sum_m N_{2m}\frac{q_m(q_m+1)}2.
\]

The dynamic program stores, for every reachable `M`, the smallest `R`. Since
the other side of `(W9-RLP)` is only `M(M+1)/2`, this proves all selection
vectors at once:

\[
 \boxed{\frac{M(M+1)}2\le R.}
\tag{1}
\]

For the perfect four-mark ruler `(0,1,4,6)`, the five nonzero choices give
minimum slack `1`, while the largest pressure is `2/3`, attained at
`q_1=q_2=1`. The large exact audits below found no violation.

## 3. The support-conditioned tile primal

At an update `m -> L=2m`, retain every genuine nonadjacent birth pair

\[
 1\le i<j<L,\qquad j\ge m,\qquad j-i\ge2.
\]

Give it its unique dyadic bands

\[
 R\le j-i<2R,\quad
 X\le h_i<2X,\quad
 Y\le h_j<2Y,\quad
 Z\le D_{i,j}<2Z.
\]

For every observed epoch-tile support `(m,t)`, introduce an occupancy variable
`x_(m,t)`. The Wave 9 bounds give

\[
 0\le x_{m,t}\le c_{m,t},
 \qquad
 c_{m,t}=\min\left(A_XA_Y,Z,
 \left\lfloor\frac{2R^2N_L}{Z}\right\rfloor\right),
\tag{2}
\]

and global difference uniqueness gives

\[
 \sum_m x_{m,t}\le Z.
\tag{3}
\]

The exact scalar charge

\[
 E=\sum_{m,i,j}
 \frac{h_i h_j}{N_L^2}\left(\frac{j-i}{L}\right)^2
\tag{4}
\]

is simultaneously the rank-variance birth objective and the exact rational
lower component of the retained cross-ratio potential:

\[
 \left(\frac{D_{i,j}}{N_L}\right)^2
 \left(\frac{j-i}{L}\right)^2 C_{ij}
 \ge
 \frac{h_i h_j}{N_L^2}\left(\frac{j-i}{L}\right)^2.
\tag{5}
\]

For the fixed-`H` budget, one tile occupant has the rigorous upper coefficient

\[
 w_{m,t}=
 \frac{144}{35}\frac{R^2}{L^2}
 \frac{\min(4XY,Z^2)}{N_L^2}.
\tag{6}
\]

The finite primal is

\[
 \boxed{
 \max\sum_{m,t}w_{m,t}x_{m,t}
 \quad\text{subject to (2)--(3)}.}
\tag{P}
\]

It is support-conditioned: it includes the tile keys actually realized by the
fixture. Adding unrealized tile keys could only make the relaxation weaker.

## 4. Exact threshold dual

For each fixed tile key `t`, the only cross-epoch row is (3). Its dual block is

\[
 \boxed{
 \min\left(
 Z\lambda_t+\sum_m c_{m,t}\mu_{m,t}
 \right),
 \quad
 \lambda_t+\mu_{m,t}\ge w_{m,t},
 \quad\lambda_t,\mu_{m,t}\ge0.}
\tag{D}
\]

Sort the epochs by decreasing `w_(m,t)` and greedily fill `Z` units. If the
global row binds, take `lambda_t` equal to the last occupied coefficient and

\[
 \mu_{m,t}=\max(0,w_{m,t}-\lambda_t).
\]

If it does not bind, take `lambda_t=0` and `mu_(m,t)=w_(m,t)`. In both cases the
primal and dual values agree exactly. This is an explicit finite dual
certificate, not a numerical optimizer tolerance claim.

On `(0,1,4,6)`, the only nonadjacent genuine atom has

\[
 E=\frac1{98},\qquad B_H^{\rm genuine,nonadj}=\frac2{1715}.
\]

The corresponding scalar LP value is `16/49`, and the fixed-`H` LP value is

\[
 \frac{576}{1715}=288\,B_H^{\rm genuine,nonadj}.
\]

The relaxation is therefore already extremely loose at four marks.

## 5. Zero-column theorem

### Proposition

Fix one finite nested Golomb ruler and hence all prefix moduli `N_(2m)`. Adding
`(W9-RLP)` for every epoch subset and cutoff to `(P)` does not change its
feasible tile-occupancy set or its optimum.

### Proof

Every `(W9-RLP)` inequality is, after fixing the ruler,

\[
 \frac{(\sum_m mq_m)(\sum_m mq_m+1)}2
 \le
 \sum_m N_{2m}\frac{q_m(q_m+1)}2.
\]

It contains only the fixed integers `m`, `q_m`, and `N_(2m)`. Every coefficient
of every primal variable `x_(m,t)` is zero. Since the fixed ruler is Golomb, all
these constant inequalities are true. Their intersection with the feasible
set of `(P)` is therefore the original feasible set. `square`

This does not say that Ma--Yi/Shearer rank-lag information is useless. It says
that a new bridge inequality must make the endpoint-product or Abel variables
appear with a nonzero coefficient.

## 6. Minimal exact slack-damping no-go inside the finite critical envelope

Consider the four-mark rulers

\[
 A_s=(0,s,4s,6s),\qquad s=1,2,3,4.
\]

Every `A_s` is Golomb and satisfies every `C=1` prefix cap through four marks.
The exhaustive W9-RLP minimum slack is exactly `s`, attained on the first
epoch alone. However, the nonadjacent retained scalar objective is

\[
 E_s=\frac{s^2}{2(6s+1)^2},
\tag{7}
\]

and the exact fixed-`H` objective is

\[
 B_{H,s}=\frac{2s^2}{35(6s+1)^2}.
\tag{8}
\]

Both increase strictly with `s`. Thus even within this complete finite
`C=1` scope, more raw W9-RLP slack does not force a smaller cross-ratio or
rank-variance objective. A useful deficit must be normalized and coupled to
the surviving endpoint mass, not used as a free-standing penalty.

## 7. Certified fixture results

| Fixture | Tile horizon | Nonadjacent atoms | Tile variables / keys | All RLP choices audited | RLP violations | Exact `E` | Exact `B_H` | LP / actual `B_H` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| perfect four | 4 | 1 | 1 / 1 | 5 | 0 | 0.0102041 | 0.00116618 | 288.0 |
| authenticated Wave 6 | 64 | 1,891 | 791 / 766 | 151,469 | 0 | 0.158378 | 0.0303308 | 103.564 |
| authenticated Wave 6 | 128 | 7,875 | 1,749 / 1,575 | 9,845,549 | 0 | 0.198717 | 0.0370378 | 163.816 |
| scaled Erdős--Turán | 512 | 129,795 | 204 / 62 | 9,845,549 through 128 | 0 | 0.539231 | 0.0866622 | 363.799 |

Every realized tile obeyed its per-epoch capacity, every global tile key obeyed
the magnitude capacity, and every exact primal equalled its exact dual. On the
512-mark Erdős--Turán fixture, the last update alone has

\[
 E_{256}=\frac{21618283516118435}{277489947818196992}
 \approx0.0779065,
\]

and

\[
 B_{H,256}=
 \frac{6172805308522804513441}{477371507030600649277440}
 \approx0.0129308.
\]

This is still a changing finite window, not one infinite eventually critical
branch. Its role is to show exactly what the present relaxation fails to
exclude.

## 8. Consequence for the next analytic step

The finite solver did not find a dual with the architecture needed for
`o(log J)`. More strongly, it proves that no such gain can arise merely by
concatenating the existing W9-RLP and tile rows: their variable supports are
disjoint.

The next admissible constraint must contain both sides in one inequality. High
value forms include:

1. a survival-conditioned lower bound on the W9-RLP cost contributed by tiles
   with two large endpoint gaps;
2. a laminar Abel inequality in which repeated positive boundary coefficients
   force new strict-interior negative mass on later epochs;
3. a rank-lag packing row weighted by an endpoint product truncation, proved on
   the exact `surv_C=infinity` subtree.

Any such row must fail on the changing scaled Erdős--Turán windows for a reason
that explicitly uses incompatibility across unbounded history.

## 9. Reproduction and integrity

Executable files:

- `wave10_laminar_lp_probe.py`
- `test_wave10_laminar_lp_probe.py`
- `wave10_laminar_lp_certificate_2026-08-29.json`

Focused commands:

```text
python -m pytest -q -p no:cacheprovider test_wave10_laminar_lp_probe.py
ruff check wave10_laminar_lp_probe.py test_wave10_laminar_lp_probe.py
ruff format --check wave10_laminar_lp_probe.py test_wave10_laminar_lp_probe.py
python wave10_laminar_lp_probe.py
```

Certificate internal SHA-256:

```text
3434372738c33fa59a2b3ea8085e4dc06878f9d260c22fb853b09b1cb3092095
```

File SHA-256 values at sealing time:

```text
f64be9e875bbfccff6eb3063a3f9dfa9b18766c168c8a32674be7b15af72726d  wave10_laminar_lp_probe.py
29e79702fd2791a6abf7604c59572e663c51584e446548dda63412a575dc2d48  test_wave10_laminar_lp_probe.py
20871af80932262ee375d2599ffac080a97310836fb9edba557e02889f09ad88  wave10_laminar_lp_certificate_2026-08-29.json
```

The certificate records finite computation only. It does not infer
`surv_C=infinity`, prove P15, resolve Question 1 or Question 2, or authorize a
prize claim.
