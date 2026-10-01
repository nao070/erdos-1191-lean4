# Independent review of the completed-fiber Gram reduction

2026-09-05. Reviewer: `/root/causal_telescoping`, GPT-6 Astra Ultra.
Ownership: this review; the reviewed source and its checker were not
edited or rerun.

**Result: PASS.** The complete mathematical argument, in particular
equations (14), (16), and (19), is supported by independent derivation.
The actual Sidon assumptions, diagonal constants, and retained signed
terms are correct. The saved instrumented execution record matches its
current source and output files. This is a mathematical and artifact
review; it is not a new execution of the mathematical checker, a Lean
verification, an estimate on the signed corrections, or original Q1.

Reviewed source: `completed_fiber_gram_route.md`, SHA256

```
fd0354333b8a60d6a7380cf7dca48012b069b0dacad9352df37df698d4e74f94
```

The complete preceding `birth_linear_total_causal_sign.md` was also
read to audit the inputs to source equation (19).

## 1. Actual fibers and the ambient operator

If two different triples of one sum shared a point, canceling one
common occurrence would give an equality of two-sums. Sidonness with
repeated summands would force the remaining unordered pairs to agree,
and hence the triples to agree. Thus different same-sum triples have
disjoint supports. For distinct-point triples this gives `3R<=N`,
distinct maximum ranks, and a legitimate ordering by those ranks.
This is an actual consequence of the original history, not an
independently specified collision graph.

All ambient means `m_j` remain those of the original prefix. The
convention `m_1=a_1` leaves the first row of `Q` zero and adds no
label. Every other row sums to zero because it is exactly one actual
birth class divided by the common terminal diameter. The inequalities
`0<=b_i<=1`, `|Q_ji|<=1`, and the strict increase of `t_i=x_i+mu_i`
follow directly from the point order and the nondecreasing means.

The direct endpoint formula in the preceding note becomes
`v_(r-1)^T(diag(x)+lambda_r I)Q nu_r`: the original multiplier
`(a_j+2m_(n_r)-s)/H` is exactly `x_j+lambda_r`. Endpoints in an
earlier completed triple lie below `n_r`, so including all of `nu_r`
inside `Q nu_r` contributes nothing from its maximum endpoint.
This verifies source equation (2), including its orientation.

The representation (4) is exact, since `mu_h+b_h=x_h`. Its two
displayed parts are each nondecreasing in the ambient index, while
their difference need not be. Thus the covariance discussion retains
both signed contributions correctly.

## 2. The finite Gram identity and the four-term decomposition

For `i<j`,

```
mu_i+mu_j-min(t_i,t_j)=mu_j-x_i=Q_ji;
```

on the diagonal it equals `-b_i`. This proves source equation (5).
On a zero-mass vector the two mean rank-one terms vanish. Shifting
every `t_i` by `-t_1` changes the minimum kernel by a constant
matrix, also annihilated by zero mass. The interval representation
then proves (6), including the minus sign before `Gamma` and the
diagonal `sum b_i u_i^2`. No probabilistic assumption is used.

For the complete-fiber bridge, each coordinate belongs to exactly
one triple. At step `r`, its coefficient is `1-r/R` on the first
`r` triples and `-r/R` on the others. This independently proves
every norm in (9). Both the mass and the `x` moment vanish, because
each triple has mass three and zero `x` moment. The endpoints
`xi_0=xi_R=0` are essential in the subsequent summation by parts.

For a symmetric `S_r` and skew `J_r`, polarization gives source
equation (15). Summing its symmetric part produces

```
(1/4) sum_(r<R) xi_r^T(S_r-S_(r+1))xi_r
 = -(1/4) sum_(r<R) Delta_r xi_r^T(Q+Q^T)xi_r.
```

Applying (6) gives precisely the nonnegative Gram term and the
second diagonal term in (11). The first diagonal term comes from
the squared increment in (15).

For the terms with one copy of `e`, the coefficient on `xi_r` is

```
A_(r+1)+(r-1)A_r^T-r A_(r+1)^T
 = J_(r+1)-(r-1)Delta_r Q^T.
```

This confirms the two different rank offsets and the transpose in
(12)–(13). The two-copy terms are exactly
`sum_r(r-1)e^T A_r e`. Combining the pieces proves (14), with
all factors of one half and one quarter as stated. `R=1` gives
zero on both sides and needs no exception beyond empty sums.

## 3. Constants and the full-total cubic remainder

The bound on entries of `S_r` is three, not six: `Q` is strictly
triangular, so only one of `A_r,A_r^T` contributes at each
off-diagonal position. Therefore the first diagonal term has total
absolute value at most

```
(3/4) sum_r ||d_r||_1^2 <= 27R.
```

The second is at most
`(1/4)*2*(3R/4)=3R/8`, using the entire mean variation at most
two. Their sum is `27.375R<=28R`, proving (16).
Every distinct-point triple is in exactly one complete sum fiber,
so summing gives exactly the counting premise of (17).

The coarser bound (18) is also valid: its four pieces are bounded
by `13.5R^2`, `13.5R^2`, `13.5R^2`, and `9R^2`, respectively.
The sum is `49.5R^2<50R^2`. It has no cubic consequence after
summing the fibers; the source correctly distinguishes this from
the diagonal estimate.

For (19), the preceding note's repeated-point accounting is valid.
There are at most `N^2` repeated triples `{a,a,b}`. Distinct
same-sum partners have disjoint supports, even with repeated slots,
so there are at most `N` partners per repeated triple. Six slot
matchings with at most two used records each give an absolute
product bound of `12N^3`. Allowing duplicate descriptions only
enlarges this upper bound. Automatic pairs and six-distinct pairs
are already separated in the preceding identity.

The remaining old diagonal is `S/2<=q/2`. Consequently

```
|E_N| <= 12N^3+28 binom(N,3)+q/2 <= 17N^3  (N>=2).
```

For example, the last inequality follows already from
`28 binom(N,3)<=14N^3/3` and `q/2<=N^3/8` for `N>=2`.
This verifies (19). It provides no sign for the explicitly retained
sum of `Circ_s+Mean_s`.

## 4. Exact-check scope and saved provenance

The checker, recorded stdout, empty stderr, and complete instrumented
JSON were read. The mathematical checker was not rerun.
Its literal fixture lists and `combinations` enumeration do select
the complete fibers of sums 40 and 1533 stated in the source.
It uses `Fraction` arithmetic throughout the mathematical comparisons.

The script checks difference uniqueness, disjoint supports, the bridge's
zero moments and exact squared norms, the Gram identity on the bridge
vectors actually used, the endpoint formula, the four-term equality,
Gram nonnegativity, and the bound `28R`. The analytic `l1` formulas
in source (9) were independently proved above; they are not separately
asserted as `l1` checks in the script. The finite Gram tests do not
assert the identity on every possible vector. Those facts come from
the analytic proof, rather than extrapolation from the two fixtures.

A read-only metadata audit checked current SHA256 values and exact
stream bytes against the saved JSON. It passed without executing
`completed_fiber_gram_exact.py`. In particular:

```
checker source:
4ffa49d47e9f80a5a9a219c316cb5f08deb804b3cd2f1b00b376df86316cd400

saved run JSON:
6fbf23522fba11fa3d327d262b4deb6a32463399e0b4a1afb0902bdd19153a31
```

The current checker hash equals both recorded pre- and post-run
hashes. The stdout and stderr bytes match both their recorded hashes
and their embedded complete strings. The saved record reports the
stated executable, timestamps, return code zero, and a passed source
gate. The original enclosing tool chunk is historical provenance
reported by the source; this reviewer did not recreate that past
tool event. Nothing in this review is a claim of a new mathematical
execution.

## 5. Scope and subsequent reindexing

The source is a sound reduction, with its signed correction estimate
still open. It neither replaces actual fiber feasibility by a free
matrix nor allocates separate capacities to the fibers.
An additional exact reindexing of the skew correction is saved in
`completed_fiber_skew_reindex.md`. It removes the bridge variables
and records what cancellation actually follows after all fibers are
assembled; it does not prove the remaining cubic lower bound.
