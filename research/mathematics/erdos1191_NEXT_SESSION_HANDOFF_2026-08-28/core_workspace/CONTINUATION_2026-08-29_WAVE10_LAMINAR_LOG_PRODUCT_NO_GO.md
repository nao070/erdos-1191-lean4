# Erdős Problem #1191 — Wave 10 laminar log-product continuation

**Date:** 2026-08-29 (Asia/Tokyo)  
**Status:** rigorous weighted incomplete-difference-triangle inequalities,
exact Abel-spectrum asymptotics, certified finite LP obstruction, and a
current primary-source audit; P15 and Erdős Problem #1191 remain open  
**Prize status:** no claim is ready

## 1. What Wave 10 changes

Wave 9 reduced the positive birth budget to the scalar position variances

\[
 {4\over49}\sum_{k=1}^{J+1}V_{2^k}
 \leq B_H(J)\leq
 {36\over35}\sum_{k=1}^{J+1}V_{2^k},
 \qquad V_n=\operatorname {Var}_{\nu_n}(u),
\]

and isolated a long-rank, two-large-endpoint core.  It proposed combining the
hereditary rank-lag inequality `(W9-RLP)`, the four-parameter tile capacities,
and the primitive cross-ratio Abel state in one laminar relaxation.

Wave 10 carries out the strongest direct version of that proposal.  It proves
new hereditary weighted inequalities and a fixed-location kernel tail, but it
also proves two exact obstructions:

1. after the prefix moduli are fixed, the existing W9-RLP rows have zero
   coefficients on every tile-occupancy variable, so merely adjoining those
   rows cannot improve the tile LP;
2. even the simultaneous weighted log-product inequality for every negative
   Abel bulk difference supplies only a `7/4` logarithmic main term, leaving a
   sharp `1/4` main-term deficit before the secondary `log log` slack.

Thus the missing theorem must couple survival, endpoint products, and
interval consistency in a single inequality.  Global integer distinctness by
itself has now been used to its quantified leading-order limit in this route.

## 2. Arbitrary-weight hereditary incomplete-DTS inequality

Let `A={0=a_0<a_1<...}` be one integer Golomb branch and
`h_i=a_i-a_(i-1)`.  For a finite set `E` of dyadic epochs, select any finite
family `T_m` of intervals

\[
 d_{m,j,s}=a_j-a_{j-s}=\sum_{t=j-s+1}^j h_t,
 \qquad m\leq j<2m,
\]

and attach weights `lambda_(m,j,s)>=0`.  Define

\[
 L_{m,t}=\sum_{(j,s)\in T_m:\ t\in[j-s+1,j]}\lambda_{m,j,s},
 \qquad \Gamma_m=\max_t L_{m,t}.
\]

If all selected weights are rearranged as
`beta_1>=...>=beta_M>=0`, then

\[
 \boxed{
 \sum_{r=1}^M r\beta_r
 \leq \sum_{m\in E}\sum_{(j,s)\in T_m}
          \lambda_{m,j,s}d_{m,j,s}
 \leq \sum_{m\in E}N_{2m}\Gamma_m.}
 \tag{W10-LWIDT}
\]

The first inequality follows by arranging the globally distinct positive
integer differences increasingly; the second follows by expanding each
interval into gaps and bounding its load by `Gamma_m`.  Both inequalities
survive deletion of arbitrary epochs or edges.  Taking unit weights on all
lags `s<=q_m` gives W9-RLP exactly.

A complementary product formulation is also valid.  For
`M_E=sum_(m in E)m q_m`,

\[
 \boxed{
 \prod_{m\in E}\prod_{s=1}^{q_m}\prod_{j=m}^{2m-1}
 (a_j-a_{j-s})\geq M_E!.}
 \tag{W10-HLP}
\]

More generally, for distinct positive integers `d_t` and nonnegative weights
`lambda_t`,

\[
 \sum_t\lambda_t\log d_t
 \geq\sum_{r=1}^M\lambda_r^\downarrow\log r.
 \tag{W10-WR}
\]

For rational weights this is an exact integer product inequality after
clearing denominators.

## 3. Fixed-location endpoint-product kernel tail

Put `D_(i,j)=sum_(r=i)^j h_r`.  For every positive gap vector of total length
`A` and every cut `t`, Wave 10 proves

\[
 \boxed{
 \sum_{i<j:\ i\leq t\leq j}{h_i h_j\over D_{i,j}}
 \leq\left(\log2+{1\over e}\right)A.}
 \tag{W10-CUT}
\]

The strictly crossing rectangles integrate under `(u+v)^(-1)` and cost at
most `A log 2`; intervals ending at the cut cost at most `A/e`.

For the normalized birth kernel at `L=2m`, this yields

\[
 \Lambda_{L,t}< {\log2+1/e\over N_L},
 \qquad
 \sup_t\sum_{k\geq K}\Lambda_{2^{k+1},t}
 \leq {4\over3}(\log2+1/e)4^{-K}.
 \tag{W10-TAIL}
\]

Hence no fixed old gap location can carry a persistent obstruction.  Any
non-vanishing mass must migrate with the advancing frontier.  Integrating
this local estimate over all gaps still gives only `O(1)` per epoch, so it is
not P15.

## 4. Exact dyadic Abel spectrum

For `n=2m`, `g=2m-1`, `w_r=r^2/(4m^2)`, and

\[
 C_{ij}=\log {D_{i,j-1}D_{i+1,j}\over D_{i+1,j-1}D_{i,j}},
 \qquad
 Y_m=\sum_{j=m}^{g}\sum_{i=1}^{j-2}w_{j-i}C_{ij},
\]

put `theta_m=((m-1)/m)^2`.  The exact Abel expansion contains:

- a positive left-prefix fan of total mass `theta_m`;
- a positive terminal-suffix fan of total mass `theta_m`;
- the negative full span with mass `theta_m`;
- a negative non-full bulk
  `I_m={(p,q): p>=2, m-1<=q<=2m-2}` of total mass `theta_m`.

After multiplication by `4m^2`, the decreasing bulk coefficient multiset is

- one copy of `2 ell+1` for `ell=2,...,m-2`;
- `m` copies of `4`;
- `(m-1)(3m-8)/2` copies of `2`;
- `m-1` copies of `1`.

Its cardinality is `m(3m-5)/2` and its scaled mass is `4(m-1)^2`.
The right-endpoint bands `[m-1,2m-2]` are disjoint across dyadic epochs, so
all associated differences are globally distinct on one branch.

## 5. Global bulk rearrangement and the `7/4` law

For any finite dyadic epoch set `E`, sort all absolute bulk coefficients as
`beta_1^E>=...>=beta_M^E`.  Then

\[
 \boxed{
 \sum_{m\in E}\sum_{(p,q)\in I_m}
  \beta_{m,p,q}\log D_{p,q}
 \geq F_E:=\sum_{r=1}^{M}\beta_r^E\log r.}
 \tag{W10-BULK}
\]

This is hereditary under arbitrary deletions.  It is stronger than applying
a separate factorial inequality at each epoch.

The exact coefficient spectrum nevertheless gives, uniformly over all finite
dyadic `E`,

\[
 \boxed{F_E={7\over4}\sum_{m\in E}\log m+O(|E|).}
 \tag{W10-7/4}
\]

The ramp contributes `(1/4)log m+O(1)` and the weight-two block contributes
`(3/2)log m+O(1)`.  A global threshold count
`#{beta>=tau}<4/tau` supplies the matching upper bound, so cross-epoch sorting
does not repair the leading coefficient.

Bounding both positive fans by the full span gives the valid certificate

\[
 \sum_{m\in E}Y_m
 \leq U_E:=\sum_{m\in E}\theta_m\log a_{2m-1}-F_E.
 \tag{W10-CERT}
\]

On one eventually `C`-critical branch,

\[
 {1\over4}\sum_{m\in E}\log m-O(|E|)
 \leq U_E\leq
 {1\over4}\sum_{m\in E}\log m
 +O_C\!\left(\sum_{m\in E}\log\log(4m)+|E|\right).
\]

For `E={4,8,...,2^J}` this is

\[
 U_E={\log2\over8}J^2+O_C(J\log J).
\]

This statement concerns the strength of the certificate, not the actual
size of `sum Y_m`.  It rigorously closes the route that uses only the exposed
Abel signs plus global distinct-positive-integer rearrangement.  The leading
missing quarter is localized to the lower-shell fan `q=m-1`.

## 6. Exact finite LP obstruction

The Wave 10 probe exhausts W9-RLP for every epoch subset and every lag cutoff
through 128 marks by exact dynamic programming: 9,845,549 selection vectors,
with zero violations.  It also solves the support-conditioned tile LP by an
exact greedy primal and threshold dual.

After a ruler and its moduli `N_(2m)` are fixed, every W9-RLP inequality is a
constant inequality in `m,q_m,N_(2m)`.  Every tile occupancy variable has
coefficient zero.  Therefore:

> Adding all existing W9-RLP rows to the current tile LP leaves its feasible
> occupancy set and optimum unchanged.

On the 512-mark scaled Erdős--Turán fixture, 129,795 genuine nonadjacent atoms
produce 204 support variables and 62 tile keys; every capacity holds and
every primal equals its exact dual.  Yet the fixed-`H` LP is about `363.799`
times the realized exact objective.  The last epoch has exact scalar charge

\[
 {21618283516118435\over277489947818196992}\approx0.0779065
\]

and exact fixed-`H` charge

\[
 {6172805308522804513441\over477371507030600649277440}
 \approx0.0129308.
\]

The four-mark dilation family `(0,s,4s,6s)`, `s=1,2,3,4`, further shows that
larger raw RLP slack can coexist with a larger retained objective inside the
complete finite `C=1` scope.  These are finite no-go certificates, not an
infinite construction.

## 7. Current literature interface

The 2026-08-29 primary-source delta found no theorem that closes P15.  It did
isolate one conditional black-box route:

- the endpoint-limited tile weight is proportional to `R^2XY`, within the
  three-factor tensor range of the tri-tree embedding theorem;
- the difference-limited tile weight is proportional to `R^2Z^2`, within the
  two-factor tensor range of the bi-tree theorem.

The relevant positive sources are the bi-tree product-weight embedding
theorem (arXiv:1906.11150, Theorem 2.3) and the tri-tree theorem
(arXiv:2001.02373, Theorem 1.3; published DOI `10.4171/RMI/1378`).  This route
still requires a positive-measure encoding of the P15 atoms and a box constant
that is `o(1)`.  Squaring the Hardy potential creates cross terms not controlled
by W9-RLP.

Naively pruning empty cells is invalid: arXiv:1903.02478, Theorem 1.11 gives a
pruned-bi-tree box/Carleson counterexample.  A direct four-parameter black box
is also unavailable; arXiv:2108.04789 disproves a proposed small-energy
majorization used by the straightforward `T^4` proof route, while
arXiv:2109.00021 records a surviving interpolation loss.  These are method
obstructions, not a theorem that every four-tree embedding is impossible.
Ding's 2026 rank-weighted Sidon theorem is correct but
its discrepancy is not small at P15 density and it does not control
`h_i h_j Phi_(ij)`.

This is a qualified null, not an absence or novelty theorem.  Overall search
saturation remains false; Consensus was quota-blocked until 2026-09-01.

## 8. Highest-value sufficient next targets

The exact unresolved obligation remains P15 itself.  The following are two
sufficient candidate architectures; they have not been proved equivalent to
each other or necessary for every possible proof of P15.

### Route A: survival premium for the lower-shell fan

For `E_J={4,8,...,2^J}`, let `A_J` be the actual negative-bulk log mass,
`Q_J` the exact positive-fan log mass, and
`T_J=sum_(m in E_J)theta_m log a_(2m-1)`.  Put

\[
 P_J=A_J-F_{E_J},\qquad S_J=2T_J-Q_J\geq0,
 \qquad U_{E_J}=T_J-F_{E_J}.
\]

The exact Abel algebra is

\[
 \sum_{m\in E_J}Y_m=U_{E_J}-P_J-S_J.
 \tag{W10-REPAY}
\]

Therefore a sufficient Route A theorem is: on one fixed infinite eventually
`C`-critical Golomb branch, find `epsilon_J>=0` with
`epsilon_J=o(log J)` such that

\[
 P_J+S_J\geq U_{E_J}-\epsilon_J,
 \quad\text{equivalently}\quad
 0\leq U_{E_J}-P_J-S_J\leq\epsilon_J.
 \tag{W10-NEXT-A}
\]

The stronger statement `P_J>=U_(E_J)-epsilon_J` would suffice by paying
everything from the bulk.  If one tries to obtain that premium from the
lower-shell fan alone, one must first prove a valid global allocation: the
floor `F_E` is sorted simultaneously across all coefficient classes and
epochs and has no canonical fanwise decomposition.  Any such theorem must use
more than global integer distinctness, because `(W10-7/4)` already computes
the leading-order limit of that information.

### Route B: tensor-box encoding

After splitting the endpoint- and difference-limited regimes, encode each
survival-conditioned epoch block on a full bi-tree or tri-tree with tensor
weight and arbitrary positive measure.  Prove that the exact core is
dominated by the Hardy embedding energy and that every one-box constant is
`o(1)` with enough summability to give a total `o(log J)` bound.

Either sufficient route must contain a nonzero coupling between the primitive
endpoint-product/Abel variables and the hereditary rank-lag/survival data.
Finite LP concatenation, static tile occupancy, and another independent
factorial rearrangement are no longer admissible substitutes.

## 9. Verification boundary

The Wave 10 executable audits are:

- `endpoint_variance/wave10_laminar_triangle_check.py` and 13 tests;
- `endpoint_variance/wave10_log_product_packing.py` and 13 tests;
- `endpoint_variance/wave10_laminar_lp_probe.py` and 4 tests;
- `endpoint_variance/wave10_laminar_lp_certificate_2026-08-29.json`.

The combined focused Wave 10 suite passes 30 tests; Ruff check and format are
clean.  The finite LP certificate regenerates byte-identically and has internal
SHA-256
`3434372738c33fa59a2b3ea8085e4dc06878f9d260c22fb853b09b1cb3092095`.

No finite fixture is promoted to `surv_C=infinity`.  No checked source or
project theorem proves P15, Question 1, or Question 2.  The public problem
record still requires a fresh external check before any claim, and an
independent expert proof audit remains mandatory.

**Current status:** `UNRESOLVED_AT_HARD_LIMIT`.
