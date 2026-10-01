# Route C: exact epochwise-owned cross-scale no-saving certificate

Date: 2026-08-30  
Status: `EXACT_FIXED_EPOCHWISE_OWNERSHIP_NO_SAVING_C058_OPEN`

This note repairs the main scope defect of the preceding 14-channel
common-cell sum-cover experiment: the two epoch demands are now kept in
separate rows.  Two exact, genuinely epochwise formulations are audited on
the same fixed rational fixture.  Neither formulation uses a cross-scale root,
and neither improves on the sum of the separately optimized same-scale covers.

This is a finite no-saving result for two specified ownership conventions.  It
does not prove that every possible signed transport fails, and it does not
prove C058, Question 1, Question 2, novelty, or eligibility for a prize.

## 1. Frozen fixture and physical price

Use the 14 normalized Haar channels from the previous certificate: five
`n=4,T=200` channels and nine `n=8,S=800` channels on

\[
 a_k=k(k+100),\qquad 0\le k\le15.
\]

The duplicate origin `a_7=749` remains two distinct channel identities because
the widths and normalizations differ.  Their common refinement has 40
positive-length cells.  For every unordered pair `e=(i,j)`,

\[
 R_{c,e}=(z_{c,i}-z_{c,j})^2,
 \qquad
 p_e=\sum_c |c|R_{c,e}.
\]

There are 91 physical root identities, including 45 cross-scale roots.  Every
owner copy below is charged the full physical price `p_e`; a single price is
never credited as the full square in both epoch rows.

The separated demands are

\[
 D_{4,c}=z_{c,0:5}^{\mathsf T}M_4z_{c,0:5},\qquad
 D_{8,c}=z_{c,5:14}^{\mathsf T}M_8z_{c,5:14}.
\]

## 2. Maximal nonnegative global ownership relaxation

For each root `e`, give each epoch its own nonnegative, cell-independent owner
coefficient `x_e^(4),x_e^(8)`.  The exact LP is

\[
 \min\sum_e p_e\bigl(x_e^{(4)}+x_e^{(8)}\bigr)
\]

subject to the 80 separate cell rows

\[
 \sum_eR_{c,e}x_e^{(4)}\ge D_{4,c},\qquad
 \sum_eR_{c,e}x_e^{(8)}\ge D_{8,c}.
\]

This has 182 root-owner variables.  It is a relaxation of every
cell-independent nonnegative fractional assignment because every physical
root, including every foreign same-scale and cross-scale root, may be assigned
to either epoch.  The three aggregate columns `J4`, `J8`, and `J_all` are also
audited for both owners at their complete physical prices, giving 188 tested
nonnegative owner variables in total.

The exact values are

\[
 E_4={29\over200},\qquad
 E_8={59841\over512000},\qquad
 \boxed{E_{\rm owner}={134081\over512000}.}
\]

Thus

\[
 E_{\rm owner}-(E_4+E_8)=0,
\]

while its gap above the weaker combined sum-cover is

\[
 {134081\over512000}-{1555757\over6144000}
 =\boxed{{10643\over1228800}}>0.
\]

An exact optimal primal uses only

\[
 x^{(4)}_{0,2}=x^{(4)}_{2,4}={1\over40}
\]

and

\[
 x^{(8)}_{5,6}=x^{(8)}_{12,13}={13\over512},\qquad
 x^{(8)}_{5,7}=x^{(8)}_{11,13}={131\over2560}.
\]

All 90 owner-labelled cross-scale copies are zero.  Exact dual witnesses make
that exclusion strict:

\[
 \min_e\bigl(p_e-\langle y^{(4)},R_e\rangle\bigr)={169\over300},
 \qquad
 \min_e\bigl(p_e-\langle y^{(8)},R_e\rangle\bigr)={817\over500}
\]

over the 45 cross-scale roots.  The closest foreign same-scale margins are
`691/2400` for the small owner and `321/200` for the large owner.  Every tested
aggregate margin is also strict.

## 3. Canonical signed coordinate-row split

For a cross root with small coordinate `i` and large coordinate `j`, split its
root-matrix quadratic form by coordinate rows:

\[
 R^4_{c,ij}=z_{c,i}(z_{c,i}-z_{c,j}),\qquad
 R^8_{c,ij}=z_{c,j}(z_{c,j}-z_{c,i}).
\]

This is signed but conservative on every cell:

\[
 R^4_{c,ij}+R^8_{c,ij}=(z_{c,i}-z_{c,j})^2.
\]

Within-scale roots stay wholly in their own epoch.  A single physical
coefficient `w_e` is charged once at `p_e`, and the two owner rows receive the
two displayed signed shares.  Nine cross-root cell entries are negative; for
example, on `[749,816)` the root `(3,5)` contributes

\[
 R^4={1\over800},\qquad R^8=-{1\over1600},\qquad
 R^4+R^8={1\over1600}.
\]

Exact primal-dual replay of all 80 rows and 91 columns again gives

\[
 \boxed{E_{\rm row}={134081\over512000}}
\]

with the same six positive within-scale roots and no cross-scale root.  The
minimum cross-scale dual margin is

\[
 \boxed{{237\over500}}>0
\]

at `(2,7)`.  The three coordinate-row aggregate margins are respectively
`121/50`, `18919/1000`, and `114167/6000`.

## 4. Why the earlier saving is not epochwise ownership

On the earlier sum-cover's tight cell `[749,816)`, its positive weights give

\[
 D_4={1\over3200},\quad P_4={271\over1024000},\quad
 D_8=0,\quad P_8={49\over1024000}.
\]

The separate slacks are `-49/1024000` and `+49/1024000`; only their sum is
zero.  Allowing an arbitrary nonnegative allocation of every physical column
separately on every cell is therefore exactly equivalent to the weaker
sum-cover.  It is not a global ownership law.

## 5. Consequence for C058

The exact fixed-fixture conclusion is:

1. arbitrary cellwise reassignment merely reproduces the weak sum-cover;
2. maximal cell-independent nonnegative ownership yields no saving;
3. the canonical conservative signed coordinate-row split also yields no
   saving;
4. cross-scale roots are strictly excluded in both genuine epochwise optima.

This identifies a real modeling boundary but leaves C058 open.  A surviving
master inequality needs an explicit source-to-sink owner flow, whole signed
Abel/Gothic rows, single ownership of boundary and terminal terms, and the net
quantity

\[
 G_{\rm off}^{\rm owned}-(P_{\rm phys}-D)-\operatorname{terminal}^{\rm owned},
\]

not just a cheaper summed cover.  The subsequent four-owner, 26-channel gate
is now recorded in `ROUTE_C_FOUR_OWNER_CROSS_SCALE_LP.md`; it again excludes
all nonnegative cross-scale roots, with one of its four named owners inactive.
The surviving finite test therefore needs whole signed coordinate rows or a
larger PSD block, plus an explicit directed source-to-sink ownership map.

Replay with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest -v \
  ROUTE_C_EPOCHWISE_OWNED_CROSS_SCALE_LP_test.py
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  ROUTE_C_EPOCHWISE_OWNED_CROSS_SCALE_LP_certificate.py \
  --verify ROUTE_C_EPOCHWISE_OWNED_CROSS_SCALE_LP_certificate.json --self-check
```

The committed JSON is a one-line canonical replay artifact.  Its semantic
payload SHA-256 is
`fe41d6979d86cea7d58fddf2a80a9c3b205e0fb424ac4a3ae5de2f5a9141c890`.
