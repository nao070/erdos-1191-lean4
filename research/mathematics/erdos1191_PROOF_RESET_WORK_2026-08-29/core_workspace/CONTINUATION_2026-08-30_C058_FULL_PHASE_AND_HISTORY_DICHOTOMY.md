# C058 continuation: full phase, formal ownership, and the history dichotomy

Date: 2026-08-30 (Asia/Tokyo)  
Global status: `UNRESOLVED_AT_HARD_LIMIT`  
Primary research priority: C058 only

This is the superseding Route-C continuation after registered claims
C111--C116.  It records a real fixed-history advance and a real obstruction
to the naive universal extension.  Neither is a solution of Erdős Problem
#1191.

## 1. What is now closed

### 1.1 Frozen finite transport algebra

Lean 4.33.0 verifies the discrete prefix/scale curl and the complete finite
two-dimensional Abel transport identity, including the initial prefix
boundary, final prefix boundary, every interior epoch coefficient, every
scale difference, the upper scale-terminal row, and the zero-horizon case.

Lean also verifies the finite signed primitive-to-net-row identity, arbitrary
owner-fiber partition, coordinate-row decomposition of a quadratic form, and
the exact Fejér inequalities used at `m=3` and `m>=4`.  The repaired pinned
Rocq MCP independently compiles the stabilized curl and ownership audits and
returns empty assumption lists.  These are finite algebra checks only.

### 1.2 Aggregate change of basis

Primitivewise nonnegative ownership is not a legal requirement.  Finite
distributivity permits the 96 signed four-corner occurrences to be aggregated
into their 42 nonzero net Gothic rows before payment.  The owner-fiber identity
then partitions the physical quadratic energy exactly.  On the frozen
fixture, 28 net rows contain mixed-sign reuse and all 46 `lambda=2M`
identities are checked.

This closes the *within-one-block* change-of-basis question.  It does not
choose a single owner for a row or physical endpoint appearing in two
adjacent epoch-pair blocks.

### 1.3 Complete fixed-history phase

For

\[
 a_k=k(k+100),\qquad0\le k\le15,
\]

epochs `n=4,8`, widths `t,2t,4t,8t`, every `t in [100,200]`, and every
Fejér ratio `r in [9/16,1]`, the exact C112 bundle supplies an epoch-block,
zero-row-sum rational Gram master with positive margin.  It covers all 108
open chambers and 109 endpoints with no phase gap.  Exact replay checks
66,528 open-chamber owner rows and 129,280 collapsed-endpoint rows.

The uniform polynomial bound is

\[
 t\Phi_r(t)\ge
 \mu={255996752651\over2560000000000}>0,
\]

and therefore the normalized full-phase average exceeds

\[
 {\mu\over200}
 ={255996752651\over512000000000000}>0.
\]

This replaces C110's isolated midpoint by a complete fixed-history phase.  It
does not extend to another history or arbitrary dyadic `n`.

### 1.4 Terminal Fejér excision

Conditional on a legal core rewrite through `K=J-3`, the master may be
switched off on the final three epochs and the complete baseline ledger kept
once.  Under the eventual-`C` cap, the omitted positive master margin is at
most

\[
 {7(1+\log_2H_J^*)\over(J+1)^2}=O_C(J^{-1})=o(1),
\]

and the retained Wave-16 terminal positive part is
`O_C(log J/J^2)=o(1)`.  The cutoff final band and upper scale-terminal row
remain explicit.  Thus `m=3,2,1` is not an independent asymptotic bottleneck;
the core and its global one-owner ledger must still be proved first.

## 2. What the lacunary dual rules out

For the exact 16-mark ruler `a_k=2^k-1` at `t=6096`, C114 gives a strict
dual obstruction inside the same four-width aggregate epoch-block PSD cone:

\[
 D_4=0,\qquad D_8={981\over16256},
\]

\[
 P_8\ge {370911\over2560000}>2D_8,
\]

and for every `rho in [9/16,1]`,

\[
 \Phi\le-{70791273\over5201920000}<0.
\]

The dual uses 308 nonnegative rational weights, 243 positive, and its exact
projected slack has 31 positive LDL pivots.

The infinite powers-of-two ruler is not eventual fixed-`C` critical.  Hence
this is not a counterexample to C058.  It proves, however, that Golomb
distinctness and the finite signed change of basis alone cannot imply a
geometry-free positive master theorem.  Some quantitative critical-history
geometry must enter.

## 3. Exploratory evidence, not registered theorem evidence

Numerical SDP stress tests at the worst ratio `9/16` found positive combined
margin across coarse phase samples on four authenticated dense/critical-near
16-mark histories, the fixed quadratic history, a Mian-Chowla prefix, several
random short Golomb rulers, and one bounded-span nested extreme.  The minimum
among 17 coarse samples on the four authenticated histories was approximately
`0.01717`.

A separate general-size exploratory program used near-arithmetic quadratic
Golomb fixtures and obtained positive numerical margins at the normalized
base phase:

- adjacent `n=8,16`: approximately `0.12767`;
- adjacent `n=16,32`: approximately `0.12322`.

These are floating conic optimizations, not exact certificates, not chamber
covers, and not registry claims.  They only support continuing the
history-sensitive route rather than abandoning it after C114.

## 4. The sharpened C058 target

For an adjacent dyadic compatible prefix pair, let
`Phi_j(theta)` denote the best legal aggregate owner-master margin at log
phase `theta`, with every physical row owned once.  The next useful theorem is
not pointwise positivity for every Golomb geometry.  It must have one of the
following equivalent amortized forms.

### Desired potential inequality

Construct a nonanticipating history potential `U_j`, an explicit `eta_C>0`,
and summable errors `epsilon_j` such that, for every sufficiently large epoch,

\[
 \int_0^1\Phi_j(\theta)\,d\theta
 \ge {\eta_C\over j+1}
 -(U_{j+1}-U_j)-\epsilon_j,
\tag{4.1}
\]

and the Fejér-weighted finite sum of the potential differences, including its
initial, cutoff-final, and scale-terminal rows, is `O_C(1)` or otherwise
strictly lower order than `log J`.

### Equivalent dichotomy

For each adjacent pair, either

1. the phase-integrated epoch-block master has the required positive margin;
   or
2. a quantified lacunarity/span-jump defect pays the negative part, and that
   defect is a signed increment of the same globally telescoping `U_j`.

The potential cannot be an informal discarded boundary term.  It must be
inserted into the complete C103 two-dimensional Abel identity with the
initial boundary, cutoff final band, interior coefficient differences, and
upper scale-terminal row visible.

## 5. Immediate mathematical program

1. Define a normalized gap-profile statistic forced by the eventual critical
   cap, using the new-block span and the distribution of gaps rather than
   Golomb distinctness alone.
2. Prove a stability lemma for the aggregate SDP: a sufficiently dense or
   nonlacunary profile has a phase-integrated margin bounded below uniformly
   at the required `1/(j+1)` scale.
3. For profiles outside that stability region, prove that their negative
   margin is dominated by a signed span-jump/gap-entropy increment that fits
   (4.1).
4. Extend the finite mechanism from the `n=4,8` prototype to arbitrary
   adjacent dyadic `n,2n`, preferably by a rank-block or continuum-kernel
   construction with explicit approximation error.
5. Choose one-time owners for shared physical endpoints and all cutoff,
   final, birth, and scale-terminal rows.  Then, and only then, apply C113 to
   discard the last three master blocks asymptotically.

Formalization remains subordinate: only freeze a new Lean statement after
one of these finite mathematical lemmas is stable.  Rocq is reserved for a
second audit of especially critical stabilized finite lemmas.

## 6. Exact claim boundary

Registered C111--C116 are finite algebra, fixed-history computation,
conditional asymptotic terminal bookkeeping, and a noncritical finite no-go.
They do not prove the history-sensitive inequality (4.1), an arbitrary
compatible history, a horizon-uniform master, C058, Q1, Q2, publication
novelty, or prize eligibility.  The global state remains exactly
`UNRESOLVED_AT_HARD_LIMIT`.

## C126 update: the common completed-shell phase does not close the scalar bank

C120 and C123 have now been replayed on the same completed-shell phase
`T=H_3/8=82`, `[82,164]`, `rho=9/16`.  The exact sources contain respectively
147 and 135 chambers, 294 and 270 epoch duals, 90,552 and 83,160 rational
weights, and 588 and 540 endpoint positive-definiteness checks.  Their
normalized upper fences are `<89/1000` and `<87/2000`.

Combining outward-rounded common-phase C123 and C121 fences leaves the clean
open window

`1341/4000 < B < 1133/2000`, width `37/160`.

The exact conclusion is stronger than this rounding statement: the verifier
directly checks that `B=1/2` is strictly above the exact C121 lower and below
both exact common-phase upper bounds.  It does not claim that the whole clean
window is feasible.

Hence the adaptive phase-base difference was not the sole reason that the
scalar bank survived.  Do not repeat the scalar phase-comparison search.

The immediate executable branch is now:

1. check the C125 rational vector against the common-phase C120/C123 rows;
2. if it remains below the exact dual uppers, construct complete-phase exact
   primals for the retained training rows;
3. on a failed row, introduce only the minimal ordered quarter-mass vector and
   re-solve the rational outer system;
4. stress a surviving construction at 32 marks or on a scalable
   critical-compatible family; and
5. prove that the phase selection and every owner/boundary row coexist in one
   nonanticipating C103 ledger.

The rule `T=H_3/8` is proved common only for this finite pair, not globally
admissible.  C058 remains the sole primary bottleneck and the global state
remains `UNRESOLVED_AT_HARD_LIMIT`.


## C127 update: the ordered candidate also survives the two stored common-phase duals

The first C126 follow-up is complete.  For

`epsilon=A=1/1000`, `B=1/2`, `C_rt=1/10`, `e_2=0`,

exact rational comparisons on `[82,164]` give stored-dual-objective margins
`>21/500` for C120 and `>7/1000` for C123.  These margins use the dual lower
enclosure minus the target upper enclosure, so the two stored certificates
definitely remain above the candidate.  This is not a primal witness.

Do not spend another cycle varying the scalar or common phase against the
same two duals.  Execute instead:

1. solve the complete-phase primal feasibility problem for this exact vector
   on C120 and C123, recording every chamber/epoch slack;
2. rationalize a feasible solution with exact endpoint and integral margins,
   or isolate the first certified infeasible chamber/epoch;
3. only after a certified failure, add the minimum ordered quarter-mass
   coordinate capable of changing that obstruction;
4. stress a surviving construction at 32 marks or on a scalable family; and
5. construct one global nonanticipating C103 phase/owner/boundary ledger.

C058 remains the sole primary bottleneck and the global state remains
`UNRESOLVED_AT_HARD_LIMIT`.

## C128 update: the fixed candidate cannot be paid pointwise on every chamber

The complete local-dual audit for the C125/C127 vector

`epsilon=A=1/1000`, `B=1/2`, `C_rt=1/10`, `e_2=0`

on the common phase `[82,164]`, `rho=9/16`, is now exact.  In the frozen
independent epoch-block, zero-row-sum PSD cone, the stored C123 local duals
separate exactly chambers `0,1,...,21`.  Chamber 0 is `[82,493/6]`; there the
target is `>9/250`, the normalized local-dual upper is `<39/2000`, and the
deficit is `>33/2000`.  A pointwise lower throughout that chamber would force
the same lower after positive `dt/t` averaging, so this exact local-average
separation refutes the fixed-target uniform per-chamber/all-phase pointwise
statement.

The C120 stored-local-dual separation count is zero, but that is not a primal
feasibility result.  C128 also does not make `[82,164]` physically impossible
and does not settle the complete-phase integrated primal problem.  A floating
integrated-primal screen is useful only as heuristic route-selection evidence
and is not part of the canonical proof claim.

Do not return to a chamberwise proof for this candidate.  Phase redistribution
is load-bearing.  Execute instead:

1. construct an exact phase-integrated rational primal bank for C120 and C123;
2. certify that later-chamber surplus pays the C123 chamber `0--21` deficits
   with exact integrated log sums;
3. retain every boundary, terminal, and one-time owner row in that bank;
4. if exact integration fails, isolate the aggregate obstruction before adding
   the minimum chronological coordinate; and
5. stress a surviving bank on scalable critical-compatible histories and one
   nonanticipating C103 ledger.

C058 remains the sole primary bottleneck.  Q1, Q2, arbitrary rank, global
phase admissibility, and the owner ledger remain open, and the global state
remains `UNRESOLVED_AT_HARD_LIMIT`.


## C129 update: selected phase redistribution works, but the full phase is still missing

C129 promotes the first exact integrated rational primal sub-bank for the
fixed C123 candidate.  Every selected bank contains the exact deficit block
`0,...,21`.  In the frozen C128 numerical ordering, adding the top six later
chambers gives negative raw margin.  Adding chamber `88` produces a sparse
29-chamber / 58-factor bank with raw margin `>1/15000` and normalized margin
`>99/1000000`.  The robust 32-chamber / 64-factor bank gives raw margin
`>143/400000` and normalized margin `>103/200000`.

The robust owner counts are `12,140 / 24,280 / 23,745`; all relevant
inequalities are strict.  Independent exact replay recomputed minimum owner
margin `333523392719/67812500000000000>0` and found no load-bearing defect.
Thus later-chamber surplus can pay the early deficit on this stated selected
bank.  Do not call it a complete phase witness or a universally minimal
surplus-cardinality result.

The next executable branch, C130, has a fixed acceptance contract:

1. exactify all 135 C123 phase records and 270 epoch factors;
2. add the missing 103 records / 206 factors—zero extension is impossible
   because chamber 22 already has positive demand `1/32`;
3. reproduce owner census totals `51,355 / 102,710 / 100,183`; and
4. certify that the complete exact aggregate raw margin is strictly positive.

After those four finite checks, do **not** infer C058.  The same construction
must still be placed in a separate globally admissible C103
phase/owner/boundary/Abel ledger, then stressed at arbitrary rank or on a
scalable critical-compatible history.  C058 remains the sole primary
bottleneck and the global state remains `UNRESOLVED_AT_HARD_LIMIT`.


## C130 update: the complete fixed-C123 common phase is exact

C130 satisfies the full finite C123 acceptance contract.  On `[82,164]`, for
the fixed candidate

`epsilon=A=1/1000`, `B=1/2`, `C_rt=1/10`, `e_2=0`,

all 135 chambers have both exact epoch factors.  The 270 rational Gram factors
have denominator `100000000`, exact ranks `9,...,25`, and rank sum 4288.  Exact
owner totals are `51,355 / 102,710 / 100,183`; structural-zero totals are
31,805 generic, 62,713 collapsed, and 31,805 interior.  The replay performs
10,395 state evaluations and 20,790 separate epoch owner recoveries.  Endpoint
objectives total 540 separate / 270 weighted, and interior objectives total
270 separate / 135 weighted.  Minimum active owner slack is
`1137298595103/235750000000000000>0`.

The exact complete-phase integral clears raw `>1/400` and normalized
`>91/25000`, with enclosure width `<1/10^26`.  Exactly 37 pieces
`0--26,31--35,59,60,77--79` are negative and 98 are positive.  Therefore keep
the complete integrated ledger; a per-chamber positivity requirement would
again destroy the mechanism.

Temporary floating solver output was discovery-only and has been stripped
from the canonical payload.  The accepted object is exact-only.  Nine focused
tests pass, 28 mutations are rejected, and the independent canonical audit
found no P1/P2 defect.

The next executable branch is now:

1. exactify the complete C120 common phase for this fixed vector, using the
   same exact Gram/owner/objective/log-integral gates;
2. record C120 and C123 only as a two-row finite primal bank—do not infer
   two-row sufficiency or every-row validity;
3. audit cross-row compatibility and representative independence; and
4. place the surviving mechanism in one global nonanticipating C103
   phase/owner/Abel ledger containing all boundary, terminal, cutoff,
   shared-endpoint, and one-time owner rows.

C130 proves no C120 witness, global ledger, local master, arbitrary-rank
theorem, C058, Q1, Q2, novelty, publication acceptance, or prize eligibility.
C058 remains the sole primary bottleneck and the global state remains exactly
`UNRESOLVED_AT_HARD_LIMIT`.


## C125 update: the first ordered two-column bank survives

The two selected Pareto rows are now exact.  Together they add 304 full-phase
chambers, 608 epoch duals, 187,264 rational weights, and 1,216 endpoint
positive-definiteness checks.  Their chronological suffix increments are
`113/26445` and `-12913/58179`.

Across C118, C120, C123, and these two rows, the rational vector

`epsilon=A=1/1000`, `B=1/2`, `C=1/10`, `e_2=0`

lies below every stored certified dual upper by more than `1/10000`.  Hence
the present necessary-side bank does not contradict it.  Do not read this as
a lower witness: exact primals for the vector have not been constructed.

The immediate branch is:

1. place C120 and C123 on the same permutation-invariant phase
   `T=H_3/8` and replay both exact duals;
2. if the candidate survives, attempt complete-phase rational primals for all
   training rows;
3. if a row fails or the primals cannot be made uniform, add the four ordered
   quarter-mass coordinates before any larger feature family;
4. stress only the surviving mechanism at 32 marks or on a scalable family;
5. retain every C103 boundary and one-time owner row in a single ledger.

C058 is still the sole primary bottleneck; global state remains
`UNRESOLVED_AT_HARD_LIMIT`.

## 7. C115--C116 sharpening of the potential target

The abstract `U_j` in (4.1) can now be replaced by an explicit signed span
column.  With

\[
 H_k=N_{2^{k+1}}-N_{2^k},
 \qquad
 \eta_k=\log{H_{k+1}\over4H_k},
\]

Sidon counting, the eventual cap, and exact finite Abel summation prove

\[
 \sum_k{\omega_{k,J}\over k+1}\eta_k=O_C(1)
\]

uniformly in the finite horizon.  The prefix-span analogue is also exact.
Positive-part variation is not controlled by the same scalar hypotheses.

Thus the load-bearing local target is now precisely

\[
 \Phi_k\ge {\epsilon_C\over k+1}
 -{A_C\over k+1}\log{H_{k+1}\over4H_k}-e_k,
\]

or its parity-paired analogue, with Fejér-weighted errors `O_C(1)` and the
complete C103 owner ledger.

C116 additionally shows that the existing nonanticipating schedule supplies
more than `17n/32-14` translated 16-mark shell windows of span at most
`8T_n`, with a linear mark-disjoint subfamily and scale ratio `2` or `4`.
This provides raw local geometry but not the localization/ownership theorem:
degenerate normalized shapes remain in its closure.  Full proofs and constants
are in `route_probes/ROUTE_C_CRITICAL_SPAN_POTENTIAL_AND_GOOD_WINDOWS.md`.

## 8. C117--C119 correction: eta is not a sufficient state variable

C117 first isolates the global-owner gate: two locally feasible rank-one PSD
blocks sharing one coordinate can require different owners, while a single
global coordinate map necessarily gives shares `(2,0)` or `(0,2)`.  Therefore
the owner system in (4.1) must be constructed globally; local feasibility and
PSD summation do not supply it automatically.

C118 then gives a finite `C=2`-envelope 16-mark Golomb fixture with

\[
 H_2=442,\qquad H_3=1659,\qquad
 \eta_2=\log(1659/1768)<0,
\]

but whose complete four-width independent epoch-block phase satisfies

\[
 \int_{1649/8}^{1649/4}\Phi(t)\frac{dt}{t}< -\frac1{40}.
\]

The strengthened rational log replay gives, for its normalized dual upper,

\[
 -\frac{81}{2000}<U<-\frac1{25}.
\]

The 87-chamber exact dual rules out the error-free finite bare-eta inequality
in that cone.  Its scope stops at `k=2`: no eventual critical infinite ray or
sufficiently-large-rank counterexample is claimed.

The normalized within-shell concentration

\[
 V_k=1-\frac{H_k^2}{2^k\sum_i h_{k,i}^2}
\]

satisfies `0<=V_k<1`.  For the Fejér-harmonic weights, exact Abel gives

\[
 \left|\sum_{k=k_0}^{K}\frac{\omega_{k,J}}{k+1}(V_{k+1}-V_k)\right|
 \le \frac1{k_0+1}.
\]

Here `0<=k_0<=K<=J`; this is the finite range on which the displayed
Fejér-harmonic weights are decreasing.

On the C118 fixture, `Delta V=3440812085/9234857208`; on the positive C112
quadratic fixture it is only `35936/36085005`.  This makes `V` a legal bounded
storage column, not a proved separator.  It is permutation-invariant, whereas
the physical Haar/owner model is ordered, so the likely robust state is a
small vector of bounded dyadic ordered interval concentrations.

The corrected local target is therefore

\[
 \overline\Phi_k\ge
 \frac{\epsilon_C-A_C\eta_k
 -\sum_rB_{C,r}(V^{(r)}_{k+1}-V^{(r)}_k)}{k+1}-e_k.
\]

The next executable experiment is to construct exact primal phase witnesses
for the C118 chamber bank, fit common coefficients only on a multi-fixture
training bank, replay the inequalities exactly on held-out histories, and
then move to 32 marks or a scalable critical-compatible family.  Every trial
must include the exact reverse-concentration row, same-multiset ordered
permutations, and one global owner ledger.  C058, Q1, Q2, novelty, and prize
eligibility remain open; the global state remains
`UNRESOLVED_AT_HARD_LIMIT`.

## 9. C120 correction: integrate the whole phase before comparing storage

The reverse-concentration row from section 8 has now been replayed exactly.
At `rho=9/16`, the full phase `553/8<=t<=553/4` splits into 161 exact
chambers.  Rational Gram primals on all chambers give

\[
 \frac{719}{10000}<\overline\Phi_2<\frac9{125},
\]

whereas the trial `epsilon=A=1/1000`, `B=1/3`, `e_2=0` has right side in
`(13/500,27/1000)`.  The exact full-phase gap is greater than `457/10000`.

This does not upgrade to a chamberwise inequality.  On the first chamber
`[553/8,277/4]`, eight exact dual pieces give normalized supremum
`<2601/100000`, below the same trial RHS by more than `207/1000000`.
Consequently all subsequent fitting and verification must compare the complete
`dt/t` phase integral.  Requiring every chamber to carry the storage payment
would discard a viable finite mechanism.

The first exact C118 full-phase primal bank has now been run.  Its 87 rational
factors give normalized feasible lower near `-0.04770218`; the prototype is
near `-0.04104430`, while the existing exact dual upper is near `-0.04014304`.
Thus the prototype sits inside the remaining primal--dual interval rather than
on either certified side.  The residual width is about `0.00755914`; the
largest localized gaps occur in chambers 49, 73, 74, 64, and 70, while chamber
1 resisted a second rationalization scheme.

The next decisive run is therefore to close this exact C118 window by a
stronger primal bank or a tighter rational dual, not to label the current
lower witness as a failure.  Only after that comparison is decided should the
search proceed to same-multiset ordered permutations and 32 marks, or augment
the scalar `V` by a bounded ordered multiscale profile.  In every branch, the
complete C103 boundaries and one-time global ownership remain mandatory.
C120 is finite calibration only and C058 remains open.


## C121 update: replace the C118 window task by an outer coefficient bank

The C118 prototype is no longer inside an unresolved certificate interval.
Reciprocal subdivision of the five dual-gap chambers supplies an exact
complete-phase upper below `-83/2000`, while the prototype RHS is strictly
larger.  In fact, on this fixed positive-`Delta V` row and current cone,
`epsilon,A>=0`, `e_2=0` imply the necessary condition

`B > 287434930599/860203021250 > 1/3`.

Therefore the former instruction to improve the same C118 primal bank is
retired.  The next executable branch is:

1. collect exact full-phase upper rows with positive and negative `Delta V`;
2. fit or refute a common coefficient vector with bounded ordered profile
   coordinates;
3. include same-multiset gap permutations so scalar concentration cannot hide
   order dependence;
4. stress the surviving cone at 32 marks or on a scalable
   critical-compatible family; and
5. construct one C103-complete owner/boundary ledger before any asymptotic use
   of C113.

The current negative-`Delta V` C120 upper gives only `B<0.9904`
approximately and does not contradict C121's lower threshold.  Larger scalar
`B`, larger cones, arbitrary rank, C058, Q1, and Q2 remain open.


## C122--C124 update: solve the ordered two-column bank next

C122 confirms exactly that the C121/C120 scalar barriers leave a nonempty
interval.  C123 exactifies one same-multiset ordered permutation over its
complete adaptive phase: 140 chambers, 280 epoch duals, 86,240 rational
weights, and 560 endpoint positive-definiteness checks.  The clean scalar
bank becomes

`1341/4000 < B < 4753/10000`,

so scalar storage is narrowed but not eliminated.

C124 freezes the first chronological column that is globally admissible at
the telescope level.  If `R_m` is the mass in the last `m` gaps of a positive
`n=2^L` shell, define

`C_rt=L^(-1) sum_(ell=0)^(L-1) R_(2^ell)-(n-1)/(nL)`

and `V_rt=(8 C_rt+3)/11`.  Then `0<=V_rt<1`, it is scale invariant and
nonanticipating at the completed shell endpoint, and the C119 finite Abel
bound applies unchanged.  Its exact increments on C118, C120, and C123 are
respectively `601940/4033029`, `-13171/58179`, and `51059/581790`.

The immediate executable branch is now:

1. exactify the two selected ordered permutations with near-zero and negative
   `Delta V_rt`;
2. replay all endpoint dual slacks and full `dt/t` integrals exactly;
3. solve the rational outer half-plane system for `(B,C)` with
   `epsilon,A>=0` first at `e_2=0`;
4. if it survives, seek exact primal phase witnesses and stress it at 32 marks
   or on a scalable critical-compatible family; and
5. only then embed it in one C103-complete global owner/boundary ledger.

The adaptive phase base is load-bearing: C120 uses `[553/8,553/4]`, while
C123 uses `[297/4,297/2]`.  Freeze the intended nonanticipating phase rule or
prove representative independence before interpreting the bank as a theorem.
C058 remains the sole primary bottleneck and the global state remains
`UNRESOLVED_AT_HARD_LIMIT`.

## C131 update: the complete fixed-C120 common phase is exact

C131 satisfies the full finite C120 acceptance contract on `[82,164]` for the
fixed candidate

`epsilon=A=1/1000`, `B=1/2`, `C_rt=1/10`, `e_2=0`.

All 147 chambers have both exact epoch factors, for 294 rational Gram factors
in the frozen independent epoch-4/epoch-8 zero-row-sum PSD aggregate cone.
Exact ranks sum to 3205.  Provenance is retained rather than flattened: the
first 115 chamber records reuse the pinned construction with scale `1/D^2`,
and the final 32 use the reduced scale `1/(D^2 midpoint)`.

The exact replay reports:

- 53,312 generic active and 37,240 generic zero rows;
- 106,624 generic endpoint inequalities;
- 104,080 collapsed active and 73,440 collapsed zero rows;
- 53,312 midpoint active and 37,240 midpoint zero rows; and
- minimum active slack `305733/87500000000000>0`.

Complete rational log integration clears raw `>21/1000` and normalized
`>3/100`, while the normalized value is also `<31/1000`; every relevant
enclosure width is `<1/10^26`.  All 147 integrated chamber pieces are
positive.  Preserve the distinction between a positive chamber integral and
a pointwise-in-phase lower bound.

C130 and C131 now give exact complete common-phase primals for the fixed C123
and C120 rows.  Record this only as a **two-row finite primal bank**.  The next
executable branch is:

1. audit cross-row compatibility and representative dependence;
2. prove that the completed-shell phase rule is nonanticipating and globally
   admissible;
3. place both finite witnesses in one C103 phase/owner/Abel ledger containing
   every boundary, terminal, cutoff, shared-endpoint, birth, and
   scale-terminal row exactly once; and
4. stress the surviving mechanism at 32 marks or on a scalable
   critical-compatible family before any arbitrary-rank promotion.

C131 proves no two-row sufficiency, every-row theorem, global ledger, local
master, arbitrary-rank theorem, C058, Q1, Q2, novelty, publication acceptance,
or prize eligibility.  C058 remains the sole primary bottleneck and the
global state remains exactly `UNRESOLVED_AT_HARD_LIMIT`.

C131 SHA-256 values: verifier
`5f7f1a1928e413ec8808279c57da99a401a01bb3a52a1fe8bca764bacf2c3a4a`;
certificate JSON
`6b28874a6c0ffe3d36a5ada27a3b466e0dbcd19447a2da0fb501b0ccc7df5afc`;
payload `5012236aa28d76867d94926a26d00ffacf602952e93358818594907f7ea7d477`;
factor bank
`bb8629e4248bc6467fe6617f319e74f42457350dd797e821e320a7dc8b0477e8`;
test `7a8d60b8fd8d500f75a56d26243dae946029ed6b644097d49e5d5f872a4c6f83`;
explanatory MD
`bdfbb75b19ef0ddb59b13b42cb51a22368418d0566bb75ff8d4e67a0dd24a214`.
Focused tests: `8`; mutation rejections: `4`.

## 2026-08-31 continuation delta: C132--C134

The two-row C130/C131 bank has now been stressed on an explicit 32-mark
finite Golomb fixture.  C132 proves that the naive affine local-bank paste
fails the natural epoch-16 owner audit and that exact phase alignment within
the same affine family forces a repeated difference.  This closes that paste,
not the joint Route-C mechanism.

C133 freezes the only admissible adjacent-epoch bookkeeping contract for the
next test: fourteen unique rows after the four shared `A16` occurrences are
netted, with all initial, final, and two upper terminal rows present.  The
identity is Lean-checked and independently replayed in exact Fraction
arithmetic.  Rank 15 remains live and is past-owned by epoch 8.

C134 shows that all 63 cross-half residual sources admit an exact signed
primitive and signed Gram representation, with ranks 15--18 and finite C103
boundary/terminal slots retained.  It simultaneously proves an exact
positive-Gram-only no-go.  Therefore the missing object is not an algebraic
source basis; it is a genuinely positive capacity master coupled to that
signed demand.

The immediate continuation is a fresh full-cell 32-mark joint LP/SDP on one
common nonanticipating physical phase, with all ranks 15--31, all 63 sources,
and all fourteen C133 rows.  Feasible and infeasible certificates must be
independently replayed.  Timeout, `unknown`, and `optimal_inaccurate` are not
mathematical claims.  Only after this finite gate may a rank-uniform
product-BMO/fixed-complexity promotion and C116 arbitrary-window argument be
attempted.

C058 remains OPEN and the global status remains
`UNRESOLVED_AT_HARD_LIMIT`.

## 2026-08-31 continuation delta: C135 frozen O0N1 separator

C135 exactly separates the frozen O0N1 row on the common phase `[82,164]`
for `rho=9/16`, the fixed ordered-suffix candidate, and the current independent
epoch-4/epoch-8 aggregate cone. The complete bank has 314 rational pieces,
628 epoch duals, 193,424 nonnegative weights, and 1,256 exact endpoint-PD
checks. Its clean complete-phase margin is greater than
`83737247/(2*10^11)>1/2500`. Do not replace this integrated test by a
chamberwise sign rule.

This makes O0N1 a counterexample to the explicit finite assertion that every
Golomb member of the frozen `4x8` cyclic same-multiset rotation bank satisfies
the same candidate lower bound. It does not establish a global failure of
representative independence. C130 for O0N0 is unchanged.

The earlier exact one-stored-dual-per-parent-chamber bank remains a valid bank,
but its `NO_SEPARATION` output was a false negative as an infeasibility
classifier. Subdivision supplied a stronger stored piecewise bank; no
optimality theorem for unsplit duals is claimed.

Continue with the C133/C134 joint ledger/capacity gate, while treating C135 as
a veto on the frozen universal rotation shortcut only. Cross-row compatibility,
one nonanticipating C103 owner ledger, arbitrary histories/ranks, C058, Q1,
Q2, and the main problem remain open. Status remains
`UNRESOLVED_AT_HARD_LIMIT`.

## 2026-08-31 continuation delta: C136 direct-owner graph witness

The fresh 32-mark test now has an exact positive answer only for its direct
owner subproblem. At `t=17745/32`, a 57-root rational graph-Laplacian satisfies
all 1,192 full-`M8`/full-`M16` owner-cell constraints, includes every C134
source, and has exact positive margin `2D-P`. This is not a paste of the C130
or C131 factors.

The finite-horizon Abel requirement is still missing. The same-fixture/phase
box-pair carrier instantiates the fourteen C133 rows, but an exact countercell
shows that it is not the direct-demand potential. Its nonzero upper terminals
belong only to that rejected carrier; the correct direct-`M` aggregate terminal
states vanish on this fixture. Therefore C136 must be read as `unweighted
direct-owner graph feasible; weighted fourteen-row payment unknown`.

The next gate is a non-circular weighted same-atom potential or genuinely
nonlocal phase-integrated charge map with all boundary/terminal owners. Only
after that exact finite gate may the nonanticipating phase and arbitrary-rank
program resume. C058 remains OPEN.

## 2026-08-31 continuation delta: C137 and weighted same-atom target

C137 exactly rules out all pointwise memoryless maps from the current graph
state to the one-sided box carrier. The surviving finite target is instead
the cumulative direct-`M` potential, whose adjacent prefix increments are
exactly `U8` and `U16`. C133 then supplies the fourteen-row expansion of the
weighted direct demand without a free potential variable.

The formal upper terminal rows remain present, but their aggregate direct-`M`
values are zero for this fixture. The current graph was optimized for the
unweighted sum and has strictly negative weighted `2D-P`. Reoptimize with
`w8=1,w16=9/16`; accept only an exact positive witness or an exact dual no-go.
Neither a numerical solver status nor the pointwise box-carrier no-go resolves
C058.

## 2026-08-31 continuation delta: C138 weighted same-atom success

C138 gives an exact positive answer to the corrected finite midpoint gate.
The cumulative potential is reconstructed from direct `M4/M8/M16` atoms, its
two increments are exactly `U8,U16`, and its fourteen C133 rows sum pointwise
to the weighted direct demand. Both terminal keys are present and evaluate
to zero. A fresh 57-root rational graph satisfies all 1,192 weighted owner
rows plus nonnegative pre8 ownership and has

`2D-P=296239592131/16716398592>0`.

The graph price is the single unweighted physical energy; epoch weights occur
only on the demand RHS. Fourteen formal rows are kept, but only five
integrated rows are nonzero, so this fixture does not test nonzero initial or
terminal history.

The immediate continuation is now phase continuation, not another midpoint
reoptimization: find the maximal exact chamber of the fixed witness, verify
collapsed endpoints and the piecewise-affine fourteen-row ledger, then seek a
complete factor-two phase bank. Nonanticipation, one global C103 owner ledger,
arbitrary histories/ranks, C058, Q1, and Q2 remain open.

## 2026-09-01 continuation delta: C139 fixed-Y chamber

The maximal connected feasible chamber of the frozen C138 graph Y is now
exactly [4425/8,555]. Both collapsed endpoints pass every retained weighted
owner and pre8 gate, while the immediately adjacent chambers fail with exact
negative slacks. The fourteen-row same-atom ledger remains exact across its
two internal topology crossings, but both terminal rows are still zero.

Do not call this complete phase coverage. Build a chamber-by-chamber exact
factor-two bank, certify every collapsed boundary and every adjacent failure,
and prove the witness/chamber choice is nonanticipating. Then stress nonzero
initial, cutoff, and terminal histories and seek the rank-uniform/global C103
promotion. C058, Q1, and Q2 remain open.
