# Erdős Problem #1191 — quantifier and reduction audit

Date: 2026-08-30 (Asia/Tokyo)  
Global status: `UNRESOLVED_AT_HARD_LIMIT`

## 1. Target statements and conventions

Let `A subset N` be infinite and additive Sidon, let

`A(x)=|A cap [1,x]|`,

and write its increasing enumeration as `a_1<a_2<...`.  Equivalently, the
positive differences `a_j-a_i`, `i<j`, occur at most once.

Question 1 is the closed sentence

`forall infinite Sidon A, liminf_(x->infinity) A(x)*sqrt(log x/x)=0`.

Question 2 is the closed sentence

`exists infinite Sidon A, exists c>0,`
`liminf_(x->infinity) A(x)*(log x)^c/sqrt(x)>0`.

The two questions are logically separate.

For `C>0`, let `B_C` be the class of fixed infinite integer Golomb/Sidon
enumerations for which

`exists N, forall n>=N, a_n<=C*n^2*log(2n)`.

The order of quantifiers matters.  A statement about `B_C` always means one
fixed compatible infinite branch, not a ruler chosen anew at each terminal
scale.

## 2. Critical-cap equivalence

The established natural-language reduction is

`Q1 <=> forall C>0, B_C is empty`.

More explicitly, failure of Q1 supplies one fixed `A` and one `delta>0`
such that `A(x)*sqrt(log x/x)>=delta` eventually.  Evaluating at enumeration
points and performing the elementary logarithmic inversion gives a finite
`C` and an eventual cap.  Conversely, an eventual cap controls each interval
`a_n<=x<a_(n+1)` and gives a positive eventual lower bound for the normalized
counting function.  The inversion constants must remain explicit in Lean;
this equivalence is currently `HUMAN_PROOF_AUDITED`, not yet
`FORMAL_THEOREM`.

## 3. Vacuity lemma for counterexample-branch targets

Fix properties `L_C(a)` defined only for `a in B_C`, and put

`UL := forall C>0, forall a in B_C, L_C(a)`.

If the already proved conditional theory gives

`forall C>0, forall a in B_C, not L_C(a)`,

then

`UL <=> forall C>0, B_C is empty <=> Q1`.

The forward implication uses the conditional incompatibility.  The reverse
implication is vacuous truth.  Thus a universal asymptotic estimate over
hypothetical critical branches is not automatically an intermediate lemma;
when it contradicts a proved branch lower bound, its closed universal form
is exactly target-equivalent.

## 4. Audit of historical targets

### P17 and P18

For fixed `C` and `a in B_C`, the statements were respectively

`sum_(m in E_J) Y_m=o(log J)` and
`sum_(m in E_J) Z_m=o(log J)`.

Wave 13 proves on every such branch

`Y_m,Z_m>1/(1536*C*log(4m))`

for all sufficiently large dyadic `m`.  Both sums therefore have a positive
`log J` lower coefficient.  Hence their universal forms are
`TARGET_EQUIVALENT` to Q1, not strict intermediate lemmas.  Q1 makes the
branch class empty; either universal target plus the lower bound implies Q1.

### P24, P25, P26, and P27

These are increasingly precise signed or positive-part rewrites of the same
counterexample-branch contradiction.  P25 and P26 differ by the nonnegative
dyadically summable `Pair_n`; P27 proves the untouched inner-birth floor

`R_n^sharp>=R_n^prof>=W_n>=n^2/(384*a_(2n-1))`.

On `B_C` this again supplies a forbidden harmonic lower coefficient.  Their
closed universal upper targets are therefore `TARGET_EQUIVALENT`; the P26/27
standalone smallness route is additionally closed by its own saturation
theorem.  The finite-window versions are not vacuous, but the particular
unchanged P26/27 bounds are refuted whenever the window contains the proved
inner-birth floor.

## 5. New audit: the bare mixed functional is impossible

For the verified mixed transport, the exact ownership identity is

`Gmix_n-Y_n/2`
`=(Y_n/2-S_(t,n))+(D_n-Theta_n^cap)+Pair_n+Q_n^ad`
` +(2*Dpre_n/3-E_(t,n)^rank)`.

Every displayed term is nonnegative.  The five owners are distinct:

- `Y/2-S_t`: unused cross-energy coefficient;
- `D-Theta^cap`: rank-floor surplus minus the current adaptive cap;
- `Pair`: rearrangement pairing slack;
- `Q^ad=Srank+S_t+E^rank-Theta^exc`: actual-rank carrier slack;
- `2Dpre/3-E^rank`: mixed endpoint slack.

The current-index deterministic envelopes give, for every `n>=2048`,

`D_n-Theta_n^cap>1/40`.

With `omega_(k,J)=((J+1-k)/(J+1))^2` and fixed `k0=11`,

`sum_(k=k0)^J omega_(k,J)`
`=M(M+1)(2M+1)/(6(J+1)^2)=J/3+O_(k0)(1)`,

where `M=J+1-k0`.  Consequently

`sum omega Gmix>=J/120+O(1)`

and the quotient by `log J` tends to positive infinity.  Therefore both the
strict `1/(3072*C*log 2)` upper target and
`sum omega (Gmix)_+=o(log J)` are `REFUTED` on every extant branch.  As a
closed universal statement over all counterexample branches, either is also
`TARGET_EQUIVALENT` by vacuity.  This closes the bare-`Gmix` route; it does
not prove or refute Q1.

The following subtractions do not create a new mechanism:

`Gmix-[(D-Theta^cap)+Pair+Q^ad+(2Dpre/3-E^rank)]`
`=Y-S_t>=Y/2`,

and subtracting `Y/2-S_t` as well leaves exactly `Y/2`.  Re-inserting the
old favourable bracket or centering `Gmix` is therefore a self-cancellation
rewrite, not progress.

## 6. P28 disposition

The abstract P28 idea — relocate an inner-birth atom through an independently
owned negative cut while retaining the finite terminal boundary — is not
logically refuted.  The particular mixed `Gmix` implementation is refuted as
an upper target.  No currently proved P28 statement is a strict weakening of
Q1.

A replacement may be called an `INTERMEDIATE_LEMMA` only if it is stated on
a nonempty finite class, for example:

> For all sufficiently large dyadic windows `[2^L,2^(2L)]`, for every
> compatible finite Golomb tower satisfying an explicit cap throughout the
> window, an atomwise, singly owned negative carrier `N_n` obeys a uniform
> signed inequality with an explicit finite terminal term and a residual
> strictly below the harmonic signal.

This formulation is not made vacuous by Q1: cap-respecting finite towers can
exist even if no infinite tower does.  Q1 therefore need not imply it.  A
proof could still imply Q1 after compactness/iteration, but it would contain
new finite information rather than merely renaming the target residual.

No such `N_n` has been constructed.  It must be disjoint from `D`, `Pair`,
`Q^ad`, the Gothic bulk already used, and the renewal cut.  Setting `N` equal
to any of those existing brackets is forbidden duplicate ownership.

## 7. Implication DAG

```text
Q1
 <=> forall C, B_C=empty
 <=> universal P17
 <=> universal P18
 <=> universal saturated P26/P27 upper target
 <=> universal bare-Gmix upper target

centered multiband carrier theorem (proved conditionally on each finite cap window)
  + continuous box-dipole and finite-horizon Gothic capacity map (proved)
  + continuum log-phase identity (proved; finite-phase replacement refuted)
  + exact finite prefix/scale transport identity (proved;
      universally saturated adjacent nonnegative shortcut can fail)
  + exact pair-owned proportional allocation and birth-supported lift (proved)
  + every phasewise scalar family satisfying equations (4.3)--(4.5) (refuted)
  + exact active coefficient-PSD price Pi_n>=2W_n (proved)
  + payment from isolated positive same-epoch F_H sector (refuted)
  + actual ordered-Gram realization or signed/cross-epoch/larger-master payment
      of the exact diagonal and terminal price from a disjoint reserve (not proved)
  + legal signed rewrite of already-owned Gothic beta capacity (not proved)
  + established harmonic lower bound
  + uniform passage from all finite windows to one branch
  -----------------------------------------------> Q1

Q2 construction obligations D1+D2+D3+D4 --------> Q2
```

The equivalences on the first line use vacuity plus a proved conditional
lower/no-go statement; none constitutes a proof of Q1.

## 8. Hypothetical-model test

- P17/P18/P26/P27/bare-`Gmix` smallness: no model can satisfy the stated
  branch hypothesis and the conclusion together, because the existing
  lower/no-go theorem contradicts it.  Classification: `TARGET_EQUIVALENT`,
  and for bare `Gmix`, `REFUTED_AS_INTERMEDIATE`.
- Centered multiband carrier theorem: its finite-window identities are now
  proved and can hold on nonempty finite cap-respecting Golomb towers while
  Q1 remains undecided.  Classification: `STRICT_COMPONENT_THEOREM`, not
  `TARGET_EQUIVALENT`.
- Box-dipole/Gothic map: the continuum identity, pointwise capacity bound,
  finite-horizon coefficient match, and log-phase average are also
  `STRICT_COMPONENT_THEOREM`s.  They can all hold on finite towers without
  deciding Q1.  Their positive `beta` atoms are already Gothic-owned, so the
  absent phase-integrated signed rewrite remains a
  `CANDIDATE_STRICT_INTERMEDIATE`; adding the map as a second payment is
  invalid.
- Fixed-prefix no-go: the ET family changes with `k`.  It refutes a universal
  ordinary fixed-prefix domination but is neither an infinite counterexample
  to Q1 nor evidence against a compatible-history telescope.  Classification:
  `CONDITIONAL_NO_GO` at its stated finite-family quantifiers.
- Phase-transport gate: on finite nested prefixes, positive weights, one
  common phase, and a finite epoch/scale rectangle, the curl, two Abel
  identities, all boundary rows, and the coefficient gate are
  `STRICT_COMPONENT_THEOREM`s.  The `b=-62/121` fixture refutes only the
  universally saturated adjacent-epoch nonnegative-coefficient shortcut.
  At the C066 stage this left pair-dependent allocation open; C067 solves the
  strict-interior owner class below.  Longer transport, a signed master, and
  C058 remain open; no infinite-branch or Q1 inference follows.
- Pair-owned allocation and birth lift: for every finite Wave epoch in the
  canonical dyadic spatial-prefix chain and its stated strict-interior owner class, the proportional LP, owner-preserving
  phase budget, residual negative-potential identity, prebirth-zero row, and
  finite terminal are `STRICT_COMPONENT_THEOREM`s.  They remove the aggregate
  adjacent sign gate only after retaining the physical pair label.  They do
  not pay the signless-completion diagonal price, place the bands in the full
  Gothic master, or imply an infinite-branch theorem.
- Scalar fractional fallback: only for the displayed nested Sidon prefixes at
  `n_-=4`, `n_+=8` and the fixed ratio `w_-/w_+=100/81`, the fixture refutes
  every measurable phasewise scalar coefficient family satisfying the envelope,
  demand, horizon, and adjacent nonnegative-gate hypotheses of equations
  (4.3)--(4.5) in the pair-owned memo.  Classification:
  `CONDITIONAL_NO_GO`.  The quantifiers do not cover owner-resolved variables,
  cross-phase cancellation, signed coefficients, extra capacity, different
  weights, or a larger master.
- Active coefficient-PSD price: for every finite Wave epoch and `T>0`, after
  retaining exactly the active tent edges, the primal/dual identity for
  `P_n(T)` and the bounds `P_n(T)>=2Q_n(T)`, `Pi_n>=2W_n` are
  `STRICT_COMPONENT_THEOREM`s.  This is coefficient-matrix PSD, a stronger
  requirement than positivity on the actual ordered box-dipole Gram matrix;
  no Gram-restricted obstruction follows.
- Positive same-epoch payment: the exact `n=4` Golomb fixture proves
  `G_4<2W_4<=Pi_4`, including the direct-domination sign convention because
  its active graph is bipartite.  Classification: `CONDITIONAL_NO_GO` for
  paying the coefficient-PSD lift solely from the isolated positive
  same-epoch `lambda=beta` `F_H` sector.  Nonpositive Gothic rows,
  signed/cross-epoch reserves, the actual Gram restriction, and larger masters
  remain outside its scope.
- Actual ordered-root cone and ramp theorem: C071--C072 prove, for every
  finite ordered prefix and fixed `T>0`, the exact labeled-root decomposition
  of its box-dipole Gram matrix, `<B,G_T>=Q_n(T)`, and the rank-ramp
  domination with its optimal shift.  These are
  `STRICT_COMPONENT_THEOREM`s.  They neither quantify over a compatible
  infinite history nor supply the opposite-sign common master needed for Q1.
- Ordered-root extension gates: C073 proves only that an ungated ramp,
  automatic signed-band cone inheritance, and a zero-slack PSD Schur
  cross-coupling do not supply that master.  Classification:
  `CONDITIONAL_NO_GO`, not a refutation of direct labeled-cell signed use.
- Marginal transport: C074 universally proves
  `Q_n(T)<=V_n(T)<=P_n^PSD(T)/2` at fixed scale.  C075 exhibits one exact
  finite Golomb prefix with `G_4<V_4`.  The theorem is a
  `STRICT_COMPONENT_THEOREM`; the payment failure is `CONDITIONAL_NO_GO` for
  marginal-only, positive same-epoch payment.  Neither result quantifies over
  the exact intersection coupling on an infinite branch.
- Isolated negative-potential reserve: C076 disproves full scalar payment on
  exact finite scale/phase/integrated fixtures, and C077 disproves any
  positive universal fraction of the integrated pair, marginal, and PSD
  prices along the finite family `A_L`.  These are scoped
  `CONDITIONAL_NO_GO`s.  They do not replace the magnitude by the original
  signed rows, and do not quantify against cross-epoch/cross-phase or larger
  masters.
- Fixed-three-channel ramp insertion: C078 quantifies over the linear
  cellwise insertion into that architectural carrier and its isolated
  positive same-epoch Gothic payment source.  Its `A_L` family gives a
  `(9/128)log L+O(1)` gap.  It does not quantify over a direct indefinite
  labeled-cell `B` rewrite, disjoint reserve, or a larger
  membership-sensitive master.  Classification: `CONDITIONAL_NO_GO`.
- Direct physical-point interval/Gothic theorem: C079 quantifies over every
  finite ordered Wave block and fixed `T>0`.  The `M=D^tBD` interval formula,
  sharp count domination, `M1=0`, `diag M=0`, and `2M=lambda` are
  `STRICT_COMPONENT_THEOREM`s.  Consecutive direct-pair disjointness does not
  quantify away the shared positive-baseline endpoint diagonal.
- Terminal-free Haar-Abel bridge: C080 holds for every finite canonical block,
  log phase, and active endpoints chosen outside the compact support.  It is
  a `STRICT_COMPONENT_THEOREM` giving a signed common coordinate rewrite,
  not a sign or capacity theorem and not an infinite-history telescope.
- Direct-Haar sign/aggregate shortcut: C081's two finite fixtures establish
  both signed-band signs, and its actual cell `[636,709)` defeats every
  `kappa J-mu M` with `mu>0`.  Classification: `CONDITIONAL_NO_GO` only for
  fixed-sign and aggregate-`J` pointwise domination; positive membership
  corrections and cross-epoch signed cells remain outside its quantifiers.
- Zero-slack repairs: C082 quantifies over scalar covers on every binary
  interval state and root-restricted Schur blocks nonnegative on every
  `(t e_i,y)` with unrestricted external `y`.  Singleton zero slack forces
  the scalar row and cross block to vanish.  Classification:
  `CONDITIONAL_NO_GO`, not a no-go for constrained actual-state coupling with
  positive slack.
- Count-baseline payment: C083 uses the finite family `A_L` to separate the
  sharp count baseline's `11/64` log coefficient from the positive
  same-epoch Gothic coefficient `9/64`, with an exact finite gap at
  `L=2^24`.  Classification: `CONDITIONAL_NO_GO` only for that baseline and
  payment source.
- One-epoch membership correction: C084 quantifies only over the 16 complete
  actual cells of the fixed `n=4`, `T=200`, `mu=1` block and only over the
  stated nonnegative root-SDDM-plus-`J` coefficient variables.  Its exact
  optima `1/16` and `1/10` are `COMPUTATIONAL_FINITE`; they do not quantify
  over arbitrary blocks, scales, general PSD/indefinite repairs, or physical
  integrated-energy cost.
- Two-epoch membership correction: C085 quantifies only over the stated
  16-mark finite Golomb fixture, consecutive `n=4/n=8` blocks, common
  `T=200`, 40 union cells, and the same coefficient class.  The exact
  optimum `53/448`, positive activity of both epochs, and one global record
  of `C_(4,4)=47/1792` are `COMPUTATIONAL_FINITE`.  Global accounting does
  not quantify a Gothic, birth, cross-epoch, or external payment owner.
- Physical root cost: C086 quantifies over every `T>0`, `d>=0` for the stated
  half-open Haar root and proves the exact three-piece `chi_T(d)`.  This is a
  `HUMAN_PROOF_AUDITED` component theorem, but it supplies no payment source.
- Physical joint savings: C087 quantifies only over the stated `mu=1`
  two-epoch `T=200` and three-epoch `T=2000` finite fixtures and only inside
  the root-SDDM-plus-`J` physical LP.  The exact savings `103/5600` and
  `11251/448000` are `COMPUTATIONAL_FINITE`; they do not quantify over other
  scales, continuum phase, or one compatible infinite history.
- Fixed sparse reuse/changing family: C088 tests only the literal `T=2000`
  sparse weights at `T=2500`, where one cell has slack `-5/32`, and fixed
  `a_k=k(k+C)`, where one repeated-difference identity holds.  Classification:
  `CONDITIONAL_NO_GO` only for that reuse and family, not for scale-adaptive
  weights or a genuine recurrence on one fixed history.
- Q2 finite dense ruler: isolated finite rulers can exist while Q2 remains
  false.  Without compatible prefixes, cross-stage uniqueness, and an
  all-scale lower bound, classification is only `COMPUTATIONAL_FINITE`.

## 9. Promotion decision

There is currently no theorem entitled to the phrases “one remaining
lemma”, “last step”, or “single bottleneck”.  The scalar aggregation and
positive same-epoch coefficient-PSD payment fallbacks are stopped at their
precisely quantified theorem-level no-gos.  The direct physical-pair Gothic
rewrite and terminal-free signed Haar bridge are now component theorems.
C084--C087 certify fixed-fixture corrections, exact physical root costs, and
finite joint savings; C088 blocks only a literal recurrence.  Route C still
requires a finite-horizon scale-adaptive actual-cell cover and, on every
capped compatible finite tower,

`G_off-P-terminals >= epsilon_C log((J+1)/(j0+1))-K_C`.

The cell-length dual gives `P>=weighted W`, so feasibility/joint saving alone
does not promote.  Only cover excess with explicit one-for-one `2M=lambda`
cancellation may be charged.  Continuum phase, exact mixed-scale energy,
singly owned payments, and every birth/past-scale/active-gate/terminal/final
row remain mandatory.
C058, Question 1,
Question 2, complete proof, publication novelty, and every prize claim remain
unresolved.  The research continues only through the four independently
specified routes in `ROUTE_PORTFOLIO.md` and the Lean proof kernel.

## 10. C089--C096 quantifier boundary

- C089 is universal only over finite ordered Haar **state shapes** and
  nonnegative root-Laplacian covers required to work on all of them.  Its
  coefficient-mass optimality is not physical-price, active-scale, or
  compatible-history optimality.
- C090 concerns the same universal star without an active gate.  It does not
  quantify over membership-adaptive or signed gated covers.
- C091 quantifies over every two positive widths and real shift.  C092
  quantifies over every finite family of translated Haar channels, but assumes
  the actual-cell inequalities.  It rules out below-demand pricing, not
  cross-scale reduction of separate-cover surplus.
- C093 is an exact abstract shared-interface state theorem.  C094 is only the
  named fixed roots and weights on one finite `n=4/n=8` Golomb tower at
  `T=200,250`; neither is a no-go for wider or scale-adaptive roots.
- C095 covers all open optimality chambers on one fixed history and actual
  breakpoint optima only at `T=216,220`.  The other isolated breakpoint
  optima, other histories, arbitrary depth, and any infinite recurrence are
  excluded.
- C096 is a fixed-fixture/class lower obstruction to zero same-scale phase
  excess.  It does not quantify over signed cross-scale or externally paid
  masters.

The phrase “C058 is the sole primary bottleneck” records research priority.
It does not authorize “last step”, “one remaining lemma”, problem resolution,
novelty, publication, or prize language.

## 11. C097--C098 quantifier boundary

- C097 concerns exactly one fixed `a_k=k(k+100)` history, the 14
  scale-labelled `n=4,T=200` and `n=8,S=800` channels, and one common-cell
  inequality covering the **sum** of the two demands.  Its strict saving over
  separate optima is not an epochwise-cover, signed-master, phase-uniform, or
  compatible-infinite-history theorem.
- C098 concerns only the optimal face of that C097 LP.  Its exact dual
  strictly excludes all 45 cross-scale roots and the three specified
  aggregate columns on this fixture.  It is not a universal no-go for
  cross-scale roots at another ratio, history, ownership convention, or
  signed formulation.
- The C097 sum-cover can fill one scale's cell deficit using a same-root
  correction from the other scale.  That is precisely why the constraint is
  too weak to certify the separately owned rows required by C058.

Thus the next finite falsification target is an epochwise or signed-owned
cross-scale surplus LP.  No C058 or global quantifier is discharged.

## 12. C099--C110-era quantifier boundary

The paragraph immediately above is superseded as an experiment request: the
epochwise and signed-owner finite probes have now been run.  Their
quantifiers remain sharply bounded.

- C099--C100 quantify only over the fixed 14-channel two-owner fixture and
  the two stated ownership formulations.  “No saving” is not a theorem about
  another signed split, width family, or history.
- C101--C102 quantify only over the fixed 26-channel four-owner fixture and
  its nonnegative root cone.  Strict exclusion of all 676 cross columns does
  not extend to general PSD, indefinite, primitive, or phase-dependent
  corrections.
- C103 quantifies over arbitrary *finite algebraic arrays* satisfying its
  stated additive hypotheses.  Lean verifies all boundary and terminal terms
  in that identity; it does not verify the C058 inequalities, Gothic
  ownership, or any Sidon asymptotic.
- C104--C106 quantify over the fixed 52 coordinates, eight canonical signed
  owner groups, and the stated graph or zero-row-sum PSD cones.  The exact PSD
  no-go additionally freezes the C067 positive-pair allocation and terminal
  convention.  It has no force against the later complete signed-stencil
  replacement.

The newest whole-stencil results are registered as C107--C110.  Their exact
domain is:

`a_k=k(k+100), 0<=k<=15`, epochs `4,8`, one dyadic phase with widths
`100,200,400,800`, terminal width `1600`, 52 coordinates, eight aggregate
owners, and 608 owner-cell inequalities.

Within that domain the full signed Gothic row is replaced one-for-one, the
epoch-block PSD witness has

`P=3900000000091/10000000000000`

and

`Phi=141015624909/10000000000000>0`.

“Epoch-block” is essential: the witness has zero cross-epoch block.  Its
cross-width terms are necessary only relative to the smaller cone of four
independent 13-coordinate width blocks, whose exact dual lower bound is
`843669938599/2048000000000`, exceeding `2D` by
`16069938599/2048000000000`.

The Fejér conclusion is also conditional on this fixture.  Positivity holds
when `w_8/w_4>581005931206/1286084055751`.  The bound `9/16` proves the
displayed weighted statement for `m>=4`; the `m=3` value `4/9` fails.  No
quantifier over the final small epochs is discharged.

Aggregate ownership is weaker than primitive ownership.  On
`(n,T,c)=(4,200,[709,725))`, the aggregate demand `-1/25600` is covered even
though the positive primitive `(5,7)` contributes `1/3200` and is not covered
by the old owner share separately.  Hence neither the 608 aggregate rows nor
the zero terminal of each four-corner stencil implies a primitive-to-source
map.  The fixed-`X` cascade is likewise a no-go only for that matrix and that
uniform directed orientation.

The rational midpoint `t=4835/48` quantifies over one additional phase point:
616 aggregate rows, price `951134501701/3000000000000`, and margin
`246690436855133/2901000000000000`.  It does not quantify over either adjacent
phase chamber, an interval of `t`, or the continuum phase integral.

Therefore none of the following has been proved: primitive-owned cover,
directed current-to-past flow, the full small-epoch and finite-horizon
boundary ledger, a uniform phase template, a compatible infinite history,
C058, either Erdős question, novelty, publication, or prize eligibility.

## Quantifier refresh after C111--C114

- C111 quantifies over generic finite sums and owner maps.  Its Route-C
  instantiation is one finite block; it does not quantify over overlapping
  epoch-pair selections.
- C112 quantifies over the full continuum `t in [100,200]` and
  `r in [9/16,1]`, but only on one 16-mark history and epochs `n=4,8`.
- C113 quantifies over arbitrary large finite horizons under an eventual-`C`
  cap, but is conditional on a pre-existing legal core through `J-3` and is
  asymptotic rather than an exact finite-`J` zero-error inequality.
- C114 quantifies over one lacunary 16-mark fixture and the stated PSD cone.
  Its infinite continuation is not fixed-`C` critical, so it is not a C058
  counterexample.

No registered claim quantifies over every compatible critical history or
arbitrary dyadic `n`.  The next admissible reduction is a history-sensitive
phase-margin/span-potential inequality with every C103 boundary term retained.

- C115 quantifies over every actual dyadic prefix/shell span after the
  eventual-`C` onset and every finite Fejér horizon; it proves only the signed
  scalar telescope, not the local PSD margin inequality.
- C116 quantifies over every sufficiently large critical Sidon shell and
  supplies linearly many controlled 16-mark windows; it does not identify a
  Wave owner block, freeze normalized shape, or transfer the C112 factors.

The exact remaining quantified statement is the arbitrary-history,
arbitrary-dyadic-size legal margin inequality with signed shell-span increment
and global one-time boundary ownership.
