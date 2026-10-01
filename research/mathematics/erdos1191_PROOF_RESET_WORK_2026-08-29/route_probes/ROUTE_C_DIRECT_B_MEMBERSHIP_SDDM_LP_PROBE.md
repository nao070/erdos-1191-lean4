# Route C: direct-`B` actual-cell membership SDDM LP

**Status:** exact finite primal/dual certificate; useful local construction;
no uniform multiscale payment theorem.

This note executes the finite target left open in Section 9 of
`ROUTE_C_DIRECT_ORDERED_B_INTERVAL_HAAR.md`.  We fix `mu=1` and restrict the
repair to the graph-Laplacian/SDDM cone

\[
 C=\sum_{0\le i<j\le n}w_{ij}(e_i-e_j)(e_i-e_j)^{\mathsf T},
 \qquad w_{ij}\ge0.
 \tag{1}
\]

Thus `C` is positive semidefinite, has nonpositive off-diagonal entries, and
annihilates `1`.  It is generally singular; **positive definiteness is not
claimed**.

The result is constructive.  A positive state-dependent correction is
feasible and has an exact **coefficient-trace LP objective** on the stated
fixtures.  What is not yet supplied is an already owned disjoint resource
that pays this coefficient price uniformly over all epochs, scales, and log
phases.  The C083 block-count expression is not treated as a competing
feasible point here: C081 already shows that an aggregate `J` channel alone
fails on zero-sum Haar states.

## 1. Exact finite LP and its dual

For each actual half-open Haar cell `c`, put

\[
 v_c=2T\bigl((K_T-K_{2T})(x_c-b_i)\bigr)_i,
 \qquad m_c=v_c^{\mathsf T}Mv_c,
 \qquad s_c=\mathbf1^{\mathsf T}v_c.
\]

Every entry of `v_c` lies in `{-1,0,1}`.  Since the only discontinuities are
`b_i`, `b_i+T`, and `b_i+2T`, sorting these endpoints enumerates every state
exactly.  The two zero exterior cells are retained rather than silently
dropped.

For one block the primal constraint is

\[
 \sum_{i<j}w_{ij}(v_{c,i}-v_{c,j})^2+\kappa s_c^2\ge m_c.
 \tag{2}
\]

For nonnegative cell multipliers `y_c`, the dual constraints are

\[
 \sum_c y_c(v_{c,i}-v_{c,j})^2\le2
 \quad(i<j),
 \tag{3}
\]

and

\[
 \sum_c y_cs_c^2\le c_\kappa,
 \tag{4}
\]

where `c_kappa=0` for LP A and `c_kappa=n+1=5` for LP B.  The dual objective
is `sum_c y_c m_c`.  The numbers `y_c` below are abstract LP multipliers;
they are **not** physical cell lengths or measures.

## 2. Complete `n=4`, `T=200` cell enumeration

Use the five physical block points

\[
 (b_0,b_1,b_2,b_3,b_4)=(309,416,525,636,749).
\]

The direct matrix is

\[
M=\begin{pmatrix}
0&0&-1/32&-5/128&9/128\\
0&0&1/32&1/128&-5/128\\
-1/32&1/32&0&1/32&-1/32\\
-5/128&1/128&1/32&0&0\\
9/128&-5/128&-1/32&0&0
\end{pmatrix}.
\tag{5}
\]

There are 15 distinct finite endpoints, 14 finite cells, and two zero
exterior cells.  The last two columns give the exact primal slack for the
solutions in Sections 3 and 4.

| actual cell | `v_c` | `s_c` | `m_c` | LP A slack | LP B slack |
|---|---:|---:|---:|---:|---:|
| `[-inf,309)` | `(0,0,0,0,0)` | 0 | 0 | 0 | 0 |
| `[309,416)` | `(1,0,0,0,0)` | 1 | 0 | 3/32 | 1/40 |
| `[416,509)` | `(1,1,0,0,0)` | 2 | 0 | 13/32 | 1/40 |
| `[509,525)` | `(-1,1,0,0,0)` | 0 | 0 | 1/32 | 1/40 |
| `[525,616)` | `(-1,1,1,0,0)` | 1 | 1/8 | 0 | 0 |
| `[616,636)` | `(-1,-1,1,0,0)` | -1 | 0 | 1/8 | 1/8 |
| `[636,709)` | `(-1,-1,1,1,0)` | 0 | 1/8 | 0 | 0 |
| `[709,725)` | `(0,-1,1,1,0)` | 1 | -1/64 | 15/64 | 21/320 |
| `[725,749)` | `(0,-1,-1,1,0)` | -1 | -1/64 | 15/64 | 21/320 |
| `[749,816)` | `(0,-1,-1,1,1)` | 0 | 1/8 | 0 | 0 |
| `[816,836)` | `(0,0,-1,1,1)` | 1 | 0 | 1/8 | 1/8 |
| `[836,925)` | `(0,0,-1,-1,1)` | -1 | 1/8 | 0 | 0 |
| `[925,949)` | `(0,0,0,-1,1)` | 0 | 0 | 1/32 | 1/40 |
| `[949,1036)` | `(0,0,0,-1,-1)` | -2 | 0 | 13/32 | 1/40 |
| `[1036,1149)` | `(0,0,0,0,-1)` | -1 | 0 | 3/32 | 1/40 |
| `[1149,+inf)` | `(0,0,0,0,0)` | 0 | 0 | 0 | 0 |

In particular, `[636,709)` and `[749,816)` both have `s_c=0` and
`m_c=1/8`.  The aggregate term `kappa J` vanishes on them, so a nonzero
root correction is genuinely necessary.

## 3. LP A: minimize `trace(C)` with free `kappa`

The exact primal point is

\[
 w_{13}=\frac1{32},\qquad \kappa=\frac3{32},
 \qquad w_{ij}=0\ \text{otherwise}.
 \tag{6}
\]

The table above checks every primal constraint.  Its objective is

\[
 \operatorname{tr}C=2\sum_{i<j}w_{ij}=\frac1{16}.
 \tag{7}
\]

For the dual, take only

\[
 y_{[749,816)}=\frac12.
 \tag{8}
\]

That state is `(0,-1,-1,1,1)`, so every edge load is at most `2`; the
`(1,3)`, `(1,4)`, `(2,3)`, and `(2,4)` loads are exactly `2`.  Its aggregate
load is zero.  The dual value is

\[
 \frac12\cdot\frac18=\frac1{16}.
 \tag{9}
\]

Primal and dual feasibility plus (7)--(9) prove

\[
 \boxed{\min\operatorname{tr}C=\frac1{16}.}
 \tag{10}
\]

Thus the zero-sum cells do not merely show `C != 0`; they force the exact
positive coefficient-trace minimum `1/16` within this root-SDDM-plus-`J`
model at this one fixture, one `T`, and `mu=1`.  The algebraically normalized
coefficient price `trace(C)/(2T)` is `1/6400`.

## 4. LP B: minimize the total trace

Now charge the aggregate channel at its actual trace:

\[
 \operatorname{tr}(C+\kappa J)=2\sum_{i<j}w_{ij}+5\kappa.
 \tag{11}
\]

An exact primal solution is

\[
 w_{02}=w_{24}=\frac1{40},\qquad \kappa=0,
 \qquad w_{ij}=0\ \text{otherwise}.
 \tag{12}
\]

For the dual, take

\[
 y_{[525,616)}=y_{[836,925)}=\frac25.
 \tag{13}
\]

In pair order

\[
(01,02,03,04,12,13,14,23,24,34),
\]

the exact edge-load vector is

\[
 \left(\frac85,2,\frac45,\frac45,\frac25,
 \frac45,\frac45,\frac25,2,\frac85\right)\le(2,\ldots,2).
 \tag{14}
\]

The aggregate load is `4/5 <= 5`.  The dual value is

\[
 \frac25\cdot\frac18+\frac25\cdot\frac18=\frac1{10},
 \tag{15}
\]

equal to the primal trace.  Hence

\[
 \boxed{\min\operatorname{tr}(C+\kappa J)=\frac1{10}.}
 \tag{16}
\]

The algebraically normalized coefficient price is `1/4000`.  Notice that the
optimum found here uses no aggregate baseline at all; the optimal displayed
state-sensitive correction is a two-edge graph Laplacian.

These divisions by `2T` are only the normalization proposed for the
coefficient trace in the finite target.  They are **not** asserted to equal
the physical integrated Haar-energy cost of `C`.  For a root shift, the
exact integrated Haar factor depends on the displacement; after the same
`2T` rescaling it can be as large as `3`, whereas the root's trace coefficient
is `2`.  Any eventual payment ledger must calculate those shift costs rather
than silently identify them with `trace(C)/(2T)`.

## 5. A substantive two-consecutive-epoch common-scale fixture

To prevent an inactive-next-epoch artifact, use the exact 16-mark Golomb
fixture

\[
 a_k=k(k+100),\qquad 0\le k\le15,
 \tag{17}
\]

namely

\[
 (0,101,204,309,416,525,636,749,864,981,1100,1221,
 1344,1469,1596,1725).
\]

The certificate exhaustively checks that all 120 positive differences are
distinct.  This is a finite fixture check, not a general theorem about (17).
At common width `T=200`, embed

\[
 M_4\quad\text{on }\{a_3,\ldots,a_7\},
 \qquad
 M_8\quad\text{on }\{a_7,\ldots,a_{15}\}.
\]

The 13 union points have 40 actual cells including the two exteriors.  The
two epochs are both genuinely active:

- `M_4` is nonzero on 7 cells and positive on 5;
- `M_8` is nonzero on 15 cells and positive on 5.

The five positive `M_8` cells are

\[
 [981,1036),\ [1036,1064),\ [1100,1149),\
 [1725,1744),\ [1796,1869),
\]

each with demand `1/32`.  Thus this is not merely a shared-coordinate
embedding replay.

Cell-length integration supplies a second, independent activity gate.  Since
`v=2T h_T`, exact summation of `|c| m_c/(2T)^2` gives

\[
 \int h^{\mathsf T}M_4h=\frac{63}{256000}>0,
 \qquad
 \int h^{\mathsf T}M_8h=\frac{169}{5120000}>0,
 \tag{18}
\]

and their sum is `1429/5120000`.  Both epochs therefore have positive
integrated signed Haar-band demand, not merely a positive pointwise cell.

Charge the two aggregate channels at traces `5*kappa_4` and `9*kappa_8`.
An exact primal point is

\[
\begin{aligned}
 w_{02}&=\frac{45}{1792},&
 w_{24}&=\frac{11}{448},\\
 w_{46}&=\frac3{1792},&
 w_{10,12}&=\frac1{128},\\
 \kappa_4&=0,&\kappa_8&=0.
\end{aligned}
\tag{19}
\]

All other roots vanish.  The union-coordinate points relevant to (19) are
`b_0=309`, `b_2=525`, the shared `b_4=749`, `b_6=981`,
`b_10=1469`, and `b_12=1725`.

The exact dual is

\[
 y_{[636,709)}=\frac37,\qquad
 y_{[836,864)}=\frac27,\qquad
 y_{[1100,1149)}=\frac37,\qquad
 y_{[1725,1744)}=\frac12.
\tag{20}
\]

The first two multipliers witness positive `M_4` rows; the last two witness
positive `M_8` rows.  Exhaustive rational verification gives every one of
the 78 edge loads at most `2`, with equality on every positive root in
(19).  The two aggregate loads are respectively

\[
 \frac57\le5,\qquad \frac27\le9.
\]

The dual objective is

\[
 \frac37\frac18+\frac27\frac18
 +\frac37\frac1{32}+\frac12\frac1{32}
 =\underbrace{\frac{40}{448}}_{M_4}
  +\underbrace{\frac{13}{448}}_{M_8}
 =\frac{53}{448}.
 \tag{21}
\]

The trace of (19) is also `53/448`.  Therefore

\[
 \boxed{
 \min\bigl(\operatorname{tr}C+5\kappa_4+9\kappa_8\bigr)
 =\frac{53}{448}}
 \tag{22}
\]

for this exact two-active-epoch/common-scale LP.

The direct `M_4` and `M_8` physical-pair supports are disjoint and their
diagonals vanish.  The aggregate coefficients in (19) are zero, so no shared
`J` diagonal is used twice.  For accounting, the correction diagonal at the
shared physical point `a_7=749` is recorded once in the **single global
matrix `C`**.  Its coefficient is

\[
 C_{44}=w_{24}+w_{46}=\frac{47}{1792},
\]

and it is counted exactly once in `trace(C)`.

This is single global accounting, **not** a paid capacity owner.  No Gothic,
birth, cross-epoch, or external reserve budget has yet been assigned to pay
this diagonal or the other root coefficients.

## 6. Interpretation and strict scope

What this probe establishes is narrower, but positive:

1. the C081 zero-aggregate obstruction can be repaired by a finite
   membership-sensitive SDDM graph Laplacian on the exact `n=4` cell set;
2. both natural trace objectives have exact rational optima and exact LP
   duals;
3. one explicitly stated consecutive `n=4/n=8` common-scale fixture also
   admits an exact shared-coordinate correction with both epochs active.

It does **not** establish any of the following:

- a uniform correction for arbitrary Golomb rulers;
- one correction compatible with all dyadic scales or all log phases;
- an integrated-energy optimum, or a lower bound for arbitrary PSD,
  indefinite, or signed repairs;
- an allocation of the trace price to a disjoint, already-owned positive or
  signed capacity;
- a Gothic rewrite, a cross-scale ownership theorem, or an external budget
  owner;
- the cross-scale/common-history lemma C058;
- Q1, Q2, or Erdős Problem #1191;
- publication novelty or prize eligibility.

In particular, (10), (16), and (22) are coefficient-trace theorems inside
the stated root-SDDM-plus-`J` class at fixed fixtures, fixed `T`, and `mu=1`;
they are not physical integrated-energy optima or a publication-ready
resolution.  Their value is that they replace the vague instruction "add
positive membership slack" by exact coefficient prices, sparse active roots,
and dual witnesses that a future common ledger must reproduce or dominate.

## 7. Reproducibility

The committed bundle is

- `direct_b_membership_sddm_lp_certificate.py`;
- `direct_b_membership_sddm_lp_certificate.json`;
- `test_direct_b_membership_sddm_lp_certificate.py`.

The certificate has no nonstandard runtime dependency.  A floating LP solver
was used only to discover candidate active sets; every accepted number was
rationalized and then independently checked with `fractions.Fraction`.
Generation, semantic replay, literal raw-byte replay, complementary
slackness, scope gates, and mutation rejection are exercised by the test
suite.
