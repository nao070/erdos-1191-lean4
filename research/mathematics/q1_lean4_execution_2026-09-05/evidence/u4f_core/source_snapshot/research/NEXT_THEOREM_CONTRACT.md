# Erdős Problem #1191 Q1 — Critical-path mathematical audit

Checkpoint: 2026-09-09, Asia/Tokyo.
Audit scope: existing mathematical dependencies, bounded falsification, and one
theorem statement. No proof search for the selected theorem was performed.

Decisions:

- Original-Q1 fidelity: **PASS**.
- Gate 0, six-endpoint localization: **PASS**, as a mathematical reduction,
  not as a bound on the remaining core and not as Lean verification.
- Principal high-level bottleneck: **PARTIALLY**. The shared global comparison
  is the common unresolved task, but the wording alone does not specify an
  inequality that closes Q1. In U4-F, a uniform core-profile bound does close
  the mathematical route; boundedness of an arbitrary residual in U4-E/R/G
  does not have that implication without an additional comparison.
- Selected route: **U4-F**.
- One frozen theorem: **Q1191-U4F-CORE-UNIFORM-01**.
- The theorem's status is **NEEDS-PROOF**. Original Q1 remains unresolved.

## 1. Primary state and source identity

The four pre-flight files were read completely before the underlying audit.
They have been preserved byte-for-byte. Their SHA-256 values are:

| File in research/ | SHA-256 |
|---|---|
| PROBLEM_CONTRACT.md | 4e83f03b5aa95557ce4d7e387503f02da2553c54ec47356477b7e9dc69702fd7 |
| STATE.md | 15c52bb3b600a90f5e58efb7155299a4d5f22b578df37c94585847ce7e0cdd7b |
| LEAN_CLAIM_LEDGER.md | 6a3f8c427e78d026e0076093c71e124aec816875b9bb2b46ca01c24c7a807d0e |
| UNRESOLVED_CORE.md | 458a509f0398bbf90ae6b5cf7c8525a4bd3ac386a1fa844a7e3eabb19d69fb33 |

Below, E means q1_lean4_execution_2026-09-05. The actual underlying files
inspected, with the portions used, were:

| Source | Portion and purpose |
|---|---|
| E/lean/Q1/Target.lean | Complete; literal target, positivity, Sidon, normalization |
| E/lean/Q1/Equivalence.lean | Final equivalence and negation declarations |
| E/lean/Q1/SidonTripleFiber.lean | Complete; exact boundary of formalization debt |
| E/research/future_covariance_rank_localization.md | Complete; Gate 0 |
| E/research/causal_fourier_rank_commutator.md | Complete; covariance identity, upper bound, raw no-go |
| E/research/causal_fourier_rank_commutator_review.md | Complete; source-bound earlier analytical review |
| E/research/signed_clock_deficit_global.md | Complete; eligibility, source/output clocks, top-lag counts |
| E/research/clock_core_localization.md | Complete; earlier counts and their different weights |
| E/research/near_retirement_incidence.md | Complete; endpoint incidence and physical packing |
| E/research/late_retirement_tail.md | Complete; source count and scalar-tail limitation |
| E/research/signed_retirement_fibers.md | Complete; all repeated classes, raw stage bound, symmetry |
| E/research/causal_fourier_coefficient_route.md | Complete; actual coefficient identity and source pricing |
| E/research/nested_fourier_route.md | Complete; quartic identity and the absence of a martingale claim |
| E/research/dyadic_good_epochs.md | Complete; fixed-cap lower radius, onset and divergent good supply |
| E/research/coherent_birth_linear_envelope.md | Section 1 and its Sidon application; two-step lookahead |
| E/research/signed_output_clock_source.md | Sections 2 and 5–7; fixed Gram source, trace cancellation, good-block demand |
| E/research/signed_output_clock_source_parent_review.md | Source, payment, and quantitative half-block review |
| E/research/signed_output_energy_closure.md | Eligibility and sections 5–8; actual payment, packing, retained residuals |
| E/research/signed_output_energy_closure_review.md | Complete; explicit analytical verification and scope limits |
| E/research/physical_envelope_allocation_dual.md | Complete; U4-E and actual feasible allocation |
| E/research/eligible_capacity_packing_closure.md | Complete; lattice loss, same-source residue repair, all-q tautology |
| E/research/growing_residue_cap_comparison.md | Complete; full adaptive range versus coprime-family obstruction |
| E/research/coherent_defect_source.md | Complete; Gamma financing, demand, additive residual |
| E/evidence/goal12_pause_checkpoint.json | Provisional source identity and paused snapshot |
| E/evidence/goal11_reviewed_research.json | Review bindings, separate formal scopes, unresolved obligations |
| E/RESEARCH_STATUS.md | Route pointers and verification scope |
| erdos1191_PROOF_RESET_WORK_2026-08-29/evidence/q1_c143_followup_2026-09-05/C143_TO_Q1_REPORT.md | Section 5 and adjacent no-go explanation; finite-tree and global certificate obligations |

The source frozen for Gate 0 has SHA-256
ece5508f9210916db86462ad6dabbb8b07cc9a9902fcedc47dfdfea8ee6d30c0.
The commutator source has SHA-256
3e410eef809aaef4469d7b5de69836ac48a725d7d9ac8d5bec791326a07e8b74.
The raw repeated-stage input has SHA-256
af256edc1cd1812a9069823b906f89328de6fb85aec6e087a7ff6a4a851cc8c9.
The two-lookahead source has SHA-256
0b9327dbed49d7086238954e9cb5d120b6864cb59bbb2597c8d6c2763bf35d00.
The output-clock source has SHA-256
b499cad5c00d89d106d6163c10f82beaff49c7c231332c987066fb31cf8cad81.

No external theorem was needed to settle Gate 0 or to select the next
statement. The Carleson/literature discussion in the coefficient note is not
an input to the selected theorem's implication to Q1. No literature search,
new Lean build, or replay of the large C143 experiment was performed.

## 2. Original-Q1 fidelity: PASS

For a positive infinite Sidon set A, put
\[
C_A(x)=\#(A\cap[1,x]),\qquad
\operatorname{Original}(A):
\liminf_{x\to\infty} C_A(x)\sqrt{\log x/x}=0.
\]
Here log is natural and the count includes both endpoints. Sidon means
\[
a+b=c+d\ \Longrightarrow\
(a=c\land b=d)\ \lor\ (a=d\land b=c)
\]
for all four members of A, with repetitions allowed. The target is exactly
\[
\forall A\subseteq\mathbb N_{>0},\
 A\text{ infinite and Sidon}\ \Longrightarrow\operatorname{Original}(A).
\]
It remains Erdos1191Q1.Q1 in Lean. The extended-real liminf prevents an
infinite lower limit from being identified with zero.

The verified negation is existence of one such A and fixed epsilon>0,
M0>=2 such that
\[
\forall N\ge M_0,\quad \epsilon N\le C_A(N)^2\log N.
\]
Neither a subsequence nor a horizon-dependent epsilon is allowed.

For the increasing enumeration a_n, this negation is equivalent to existence
of one eventual cap a_n<=C n^2 log(2n), with C and the onset fixed.
The cap inversion is a mathematical step, not a Lean theorem in this project:
at N=a_(m+1)-1 the eventual lower bound gives
N/log N<=m^2/epsilon; monotonicity of x/log x for x>e gives
a_(m+1)=O_epsilon(m^2 log(2m)). Conversely, a fixed enumeration cap,
applied at a_m<=N<a_(m+1), gives an eventual positive lower bound since
log N>=log m and
m^2 log m/[(m+1)^2 log(2m+2)] is bounded below away from zero.
All changes of constants/onsets are made once.

The chosen theorem uses the diameter H_n=a_n-a_1. A point cap implies the
same diameter cap. Conversely a diameter cap implies a point cap, for
example with constant C+a_1 beyond the same onset. Thus existence of an
infinite diametrically capped history is also equivalent to the negation.
This changes constants in the bridge, not the target. The chosen estimate
is translation invariant and its constant may not depend on a_1.

| Quantifier item | Audited requirement |
|---|---|
| C and onset m0 | Fixed before the history and both horizons |
| Uniform bound K | May depend on C,m0 and the already fixed localization parameters only |
| History | Every actual positive integer Sidon history/prefix satisfying the stated cap |
| Rank/component horizons | Arbitrary; K may depend on neither |
| Initial ranks | No cap silently imposed below m0; finite initial-cut costs are uniformly bounded |
| Hidden regularity | No asymptotic equality, derivative law, random model, primitive gcd, density uniformity, or extendibility-to-a-capped-history assumption |
| Finite/infinite bridge | Required explicitly; finite evidence alone is insufficient |

For completeness, the finite-tree equivalence also retains the early ranks.
Normalize translation to a_1=1. Every prefix reaching m0 has all its first
m0 entries bounded by 1+C m0^2 log(2m0). There are finitely many such initial
prefixes. Subsequent capped levels are finitely branching. Arbitrarily long
capped prefixes therefore give an infinite capped branch by König's lemma.
One must first restrict to these extendible initial prefixes; the uncapped
raw early-level tree need not be finitely branching.

## 3. Gate 0: independent mathematical audit of all six deletions

Use the original complete-history quantities
\[
Q_n=n(n-1),\quad \alpha_n=Q_n^{-2},\quad
\kappa_n=\alpha_n-\alpha_{n+1}>0,\quad
u_r=\sum_{k=r}^\infty\frac{\kappa_k}{H_k^2}.
\]
For an unordered pair of distinct positive difference labels h={d,e},
let c=max(tau(d),tau(e)), s=min(tau(d),tau(e)). An eligible output has
its unique actual endpoints t=|d-e|=a_r-a_i with c<i<r.
Its weight is v_h=u_r de>=0. Source birth s is not a point value.

The exact covariance profile is
\[
P_b(T)=\sum_{\substack{h\ {\rm eligible}\\r(h)\le T}}
 v_h\,{\bf1}_{c(h)<b<i(h)},\qquad
N_T(P)=\sum_{b=2}^{T-1}\frac{\sqrt{P_b(T)}}b.
\]
This follows directly by expanding K_(b-1)^+(a_r-a_i). Each positive
source pair occurs once in that kernel. Sidon injectivity gives one output
endpoint pair, but does not make different source pairs with the same output
unique. All such source pairs remain in the sum.

### Common estimates, including their constants

Since H_k>=H_r>=H_c for k>=r,
\[
u_rde\le\alpha_r\le4/r^4,\qquad
u_rde\le4/b^4\quad(c<b<i<r).
\]
Two positive labels born at the same c have an old output: their difference
is a difference between two endpoints before c. Hence eligible pairs have
s<c. There are at most
(c-1) binom(c-1,2)<=c^3/2 source pairs at c, counted once over all future
outputs. The output may never occur, which only reduces the sum.

At a fixed b, bound u_r by alpha_b/H_b^2 and sum over distinct used
positive source pairs in F_(b-1). Their total de is at most half the
square of their label sum. Thus P_b<=1/8, uniformly in history and horizon.
Every finite collection of initial b therefore costs at most
(1/sqrt(8)) sum 1/b. This absorbs only parameter-dependent initial
thresholds, never a history-dependent unbounded interval.

### Six omitted classes

| Class omitted | Rechecked estimate for sufficiently large b | Summability threshold |
|---|---|---|
| Far upper output: r>=c(log c)^A | P_b<=2 sum_(3<=c<b) c^3/max(b,c(log c)^A)^4 = O_A((1+log log b)/(log b)^(4A)) | A>1/2 |
| Short coverage: i-c<=c/(log c)^gamma | P_b<=4 ceil(2^gamma b/(log b)^gamma)^2/b^2 | gamma>1 |
| Short top lag: r-i<=r/(log r)^delta | P_b<=2b^2 sum_(r>b) 1/[r^3(log r)^delta]<=1/(log b)^delta | delta>2 |
| Old partner: s<=c/(log c)^eta | P_b<=2/b^2+2^(2eta-1)/(log b)^(2eta) | eta>1 |
| Small actual output: t<=c^2/(log c)^beta | P_b<=2/b^2+2^(beta+1)/(log b)^beta | beta>2 |
| Repeated endpoint | P_b<=24 sum_(r>b)r^-2<=24/b | No cap or logarithmic threshold |

The assertion in the final column is convergence of sum_b sqrt(P_b)/b,
not merely convergence of total pair mass.

Details that matter for this audit:

1. For the far class put L=(log b/2)^A. Eventually 1<=L<=sqrt(b).
   Split c at b/L. Below it use sum c^3<=x^4. Above it c>sqrt(b),
   so (log c)^A>=L and the remaining sum is at most
   (1+log L)/L^4. Taking square roots requires 2A>1.
2. For fixed c<i and old positive label e, write d=a_c-a_j, j<c.
   If d>e, then a_r+a_j=a_c+a_i-e. Repeated-sum Sidon gives one
   unordered pair, and r>i>c>j fixes its orientation. If d<e, then
   a_r-a_j=a_i-a_c+e>0 and positive-difference uniqueness gives one
   ordered pair. These are disjoint sign cases. Thus
   I_(c,i)<=2 binom(c-1,2), over all future r together, and its weighted
   mass is at most 2 binom(c-1,2)alpha_c<=1/c^2.
   Short coverage implies c>b/2 eventually and puts both clocks within
   ceil(2^gamma b/(log b)^gamma) of b. This proves the second row.
3. For a fixed positive t, the graph on positive source labels with
   edge difference t has degree at most two. Summing
   de<=(d^2+e^2)/2 proves K_(b-1)^+(t)<=b^2 H_b^2/2.
   There are at most r/(log r)^delta possible short-top lower endpoints.
   The price remains u_r<=4/(r^4 H_b^2). Integral comparison gives
   the third row with the stated coefficient.
4. The old-partner count is at most c^3/[2(log c)^(2eta)].
   The small-output count is at most 2c^3/(log c)^beta, because each
   new d and integer t have at most the two partners d-t,d+t.
   Split c at sqrt(b); the low range costs at most 2/b^2, while
   sum_(c<b)c^3<b^4/4 gives the displayed high-range constants.
   No centered birth-linear coefficient or q=binom(n,2) price is imported.
5. For repeated endpoints, orient signed retirement by d>e and write
   d=A-B, e=C-D, d-e=a_r-a_i. Then
   A+D+a_i=B+C+a_r. The newest endpoint a_r occurs exactly once.
   Cancellation plus repeated-sum Sidon makes distinct equal-sum triple
   multisets support-disjoint. Identical triple multisets cannot retire.
   If the new triple is distinct, the old triple must repeat: at most
   (r-1)^2 choices, with at most one new partner sharing a_r at a given
   sum. If the new triple repeats it is {a,a,a_r}: at most r-1 choices,
   with at most r-1 old partners. Each collision has at most six
   matchings and two retired signed records per matching. This includes
   every repeated class and bounds the absolute raw product by
   24(r-1)^2 H_r^2. The positive-source records form a subset.
   Multiplication by u_r<=alpha_r/H_r^2 gives 24/r^2.
   Doubled labels and zero-edge exclusions do not increase this upper
   count. No inverse-automorphism identification is needed for this loose bound.

For any fixed permissible parameters, let core retain the complement of
all six classes, with their strict inequalities. A record in several
omitted classes may occur in several upper bounds; this is a finite union
bound for nonnegative errors, not additional spendable capacity. Since
sqrt(x+y)-sqrt(x)<=sqrt(y),
\[
0\le N_T(P)-N_T(P^{\rm core})
\le B_{A,\gamma,\delta,\eta,\beta}<\infty.
\]
The bound is independent of C, m0, history and T.

All localization statements also follow with their stated strictness:
on a covered cut, r<c(log c)^A and c<b<i<r imply
b/(log b)^A<c<b<i<r<b(log b)^A. The actual numeric output obeys
t<=H_c, and Sidon packing between its two endpoints gives
(r-i)(r-i+1)/2<=t. The cap adds t<=C c^2 log(2c) only for c>=m0.
It does not bound a_i-a_c by t.
The exact dyadic coverage is
ell_N(c,i)=sum_(N<=b<2N,c<b<i)1/b, with total at most log(i/c).
It is not a fresh budget in each dyadic block.

**Gate 0 verdict: PASS.** Every substantive implication needed for the
finite-error reduction is justified. Its profile bound remains unproved.
The old source note is preserved; its previously provisional reduction is
classified as MATH-REVIEWED by this audit, not retroactively as Lean-verified.

## 4. Dependencies, backwards from Q1

Classification used here is exactly:
A = Lean-verified supporting theorem; B = mathematically proved/reviewed,
not Lean-formalized; C = exact finite computation; D = provisional;
E = rejected; F = unproved bridge.

| Class | Critical-path assignment |
|---|---|
| A | Target equivalence/negation theorems, positive-difference injectivity, finite envelope/accounting. The definition Q1 itself is checked syntax, not a proved theorem. |
| B | Cap inversion and finite-tree equivalence; two-lookahead good epochs; actual source/payment and quartic/commutator identities; raw incidence/repeated-stage estimates; Gate 0 reduction; finite-component limit argument. |
| C | The bounded actual-configuration enumeration in Section 8. Rational identities/counts are exact; the displayed square roots are numerical presentations only. Historical C143 is not a dependency of this route. |
| D | No provisional assertion is used. The localization note entered this audit as D; only its audited reduction is promoted to B. |
| E | Proposed raw O(T^3 H_T^2) bound; independent-label or point-Fourier-truncation substitutions; automatic cancellation of additive residuals. The valid proofs of their obstructions are B. |
| F | The boxed core bound; a successful global closure through another route; the final formal chain. The multiset normalization bridge is F as formalization debt, not the selected mathematical blocker. |

~~~text
Literal original Q1
  ↑ B: negation/enumeration-cap inversion + A: exact target equivalences
Absence of every fixed-cap infinite actual Sidon history
  ↑ contradiction: uniformly bounded eligible capacity vs divergent demands
  ├─ B: cap -> two-lookahead good epochs -> disjoint half-block demands diverge
  └─ B: commutator bound -> capacity <= constant + 4 sqrt(2/3) N_T(P)
                ↑ B: audited finite-error localization
      uniformly bounded N_T(core), for the same history and all T
                ↑ B: monotone passage from genuine finite component sums
      Q1191-U4F-CORE-UNIFORM-01                         [F: NEEDS-PROOF]

Supporting infrastructure:
  A: Sidon difference injectivity and finite one-copy accounting
  B: actual Fourier quartic identity, source pricing, local moment lower bound
  C: bounded actual-configuration checks (diagnostics; no upward proof arrow)
~~~

Missing implications and their necessity:

| Obligation | Status | Logical role |
|---|---|---|
| Uniform core-profile bound in Section 6 | F | Selected U4-F sufficient formulation; not a step every proof must use |
| Convert its finite component statement to the same infinite source | B, justified in Section 7 | Required for this finite formulation only |
| Insert the profile bound into the capacity inequality and contradict divergent actual demand | B, justified in Section 7 | Required endgame for U4-F; no second unknown margin estimate |
| Establish some valid contradiction to every fixed-cap actual history | F until the selected theorem or an alternative closes it | Necessary for every current affirmative cap route |
| Formalize the actual mathematical dependencies and derive literal Q1 in Lean | F | Required for the project's formal completion |
| Identify orderedCard/6 with the inverse-aut multiset mass | F as a Lean bridge | Formalization debt for the multiset branch; not used by the loose repeated-stage bound or the Fourier endgame here |

The finite accounting already verified in Lean is not being reproved.
The Fourier source/profile identities and good-block mathematics remain B,
even though some finite algebra and injectivity inputs have Lean proofs.
The 54-name ledger is supporting evidence, not a final theorem chain.
The later 138-name inventory does not close any F entry above.

## 5. Adversarial bottleneck test and route comparison

The original same-source capacity counts each eligible physical source pair
once. Numeric output uniqueness identifies that output's endpoints, not a
unique source pair. The covariance P_b can contain the same pair at many
cuts, exactly on c<b<i. Cauchy uses these overlaps analytically; they are
not separate allowances. A theorem on independent labels would not apply.

At lambda=0 all carrier entries are nonnegative. The commutator calculation
retains the quartic diagonal and its finite bound, the fresh opposite-sign
class, and the boundary commutator. Endpoint energies E_1 and E_T vanish
for the stated reasons; the terminal u_T term in V_b is retained.
The actual demand retains its entire trace subtraction.
The exact unused-capacity identity retains gate, membership, output-price
and projection losses. We do not need to bound these losses separately
when the entire eligible capacity is bounded above.

Historical outputs beyond T cannot pay a block contained in P_T; excluding
them defines the eligible budget and does not assert that the historical
source tail is zero. Component truncation in the theorem below is a genuine
partial sum, with an explicit monotone limit. No source price is replaced
by an output price or vice versa.

One source belongs to one history. Uniformity concerns the bound over all
such histories; no physical ledger is shared between different histories.

| Route | Strongest available upstream input | First unproved implication | Distance if that implication is proved | Provisional input? | No-go / limitation | Cap sensitivity and falsifiability |
|---|---|---|---|---|---|---|
| U4-F | Exact causal coefficient/commutator identities; finite diagonal; audited six-class reduction; divergent actual half-block demands | Uniform bound on the actual core square-root profile | Finite-component limit, two proved comparisons, contradiction; then formalization | None after Gate 0 for selected statement | Raw O(T^3 H_T^2) false; ordinary point Fourier truncation does not describe gap-birth order | Exactly quantified in Section 6; all cap dependence explicit; finite profiles computable, but finitely many values cannot refute existence of an unspecified K |
| U4-E | Exact finite allocation dual I_max=inf_alpha[L+ell sum(d-rho)_+]; constructive actual-block allocation with I_max<=M(0) | Cap forces I_max>M(0) at some horizon of each hypothetical history | This exact strict surplus would give contradiction immediately; mere positive improvement still leaves the full baseline margin | Finite dual itself has none; no proved asymptotic surplus | Actual allocation witnesses nonnegative margin at every finite instance; tiny improvement is insufficient | A cap-sensitive strict surplus must be stated over a specified row family; current record does not isolate a simpler quantitative criterion |
| U4-R | Exact residue moments/projection gain and shared pair constraints; coarse-support bounds | Additional cap-based comparison using all integer q in [n,n log(2n)] | A bounded or improved repaired residual alone need not contradict anything; a coercive comparison/contradiction remains | No provisional count needed; closing comparison is F | Fixed/coprime families have lattice loss; arbitrary q above the support width gives exact energy and zero residual tautologically | Full adaptive comparison has not been specified with a proved contradiction threshold; individual finite LP values are testable |
| U4-G | Rank-one Gamma for full defect, finite financing error, divergent permitted Gamma demand | Joint capacity/demand inequality for Psi+(1+lambda)Gamma | A sufficiently strong joint surplus would close; financing alone leaves two nonnegative residuals | Direct Gamma construction avoids needing the provisional core or ordered/multiset bridge | Additive residuals remain additive; full defect cannot be spent twice; entrywise domination is not PSD subtraction | Current fraction depends on arbitrary C; no uniform relative gap closing the sum is proved or sharply isolated |

**Verdict on the general bottleneck wording: PARTIALLY.** It correctly points
to uniform global comparison, but is too broad to identify a closing theorem.
U4-F has an explicit bound whose proof would leave no equally major
mathematical implication open. U4-E needs a full strict surplus, U4-R needs
an additional non-tautological comparison, and U4-G needs a joint inequality.
Those are alternatives, not cumulative prerequisites for U4-F.

U4-F is selected for that audited implication to Q1, not for recency.
This is no claim that its unproved estimate is easy or likely to succeed.

## 6. ONE NEXT THEOREM: Q1191-U4F-CORE-UNIFORM-01

Name: **Uniform finite-component bound for the actual six-endpoint core**.

Fix the localization parameters once:
\[
(A,\gamma,\delta,\eta,\beta)=(1,2,3,2,3).
\]
These are choices of an equivalent finite-error reduction, not additional
assumptions on the Sidon history.

### Definitions

Given an integer M>=2 and positive integers a_1<...<a_M, let
\[
P_n=\{a_1,\ldots,a_n\},\quad H_n=a_n-a_1,\quad
F_n=\{a_j-a_i:1\le i<j\le n\}\quad(2\le n\le M).
\]
Assume P_M is Sidon in the repeated-sum sense specified in Section 2.
Every d in F_M then has unique endpoint indices
(p(d),q(d)), p(d)<q(d), with d=a_(q(d))-a_(p(d)).
Set tau(d)=q(d).

Define, for every integer k>=2, alpha_k=1/[k^2(k-1)^2] and
kappa_k=alpha_k-alpha_(k+1). For 2<=r<=M define the **genuine partial
component price**
\[
u_r^{[M]}=\sum_{k=r}^{M}\frac{\kappa_k}{H_k^2}.
\]
In particular alpha_(M+1) is not reset to zero, and u_M^[M] is
kappa_M/H_M^2, not alpha_M/H_M^2.

For integers 2<=T<=M, let R_core(M,T) be the set of unordered pairs
h={d,e} of distinct positive labels in F_M with all the following
properties. Orient them numerically as d>e and set
\[
t=d-e,\quad c=\max(\tau(d),\tau(e)),\quad
s=\min(\tau(d),\tau(e)).
\]
Require t in F_M, write (i,r)=(p(t),q(t)), and require
\[
3\le c<i<r\le T.
\]
Require all six endpoint indices
p(d),q(d),p(e),q(e),i,r to be distinct, and require
\[
\begin{aligned}
s&>\frac{c}{(\log c)^2},&
i-c&>\frac{c}{(\log c)^2},\\
r-i&>\frac{r}{(\log r)^3},&
r&<c\log c,&
t&>\frac{c^2}{(\log c)^3}.
\end{aligned}
\]
Every one of these conditions is part of the record definition. The
logarithms have positive arguments greater than one. No point values are
substituted for the rank s, and t remains an integer physical difference.

For every integer cut b with 2<=b<T define
\[
P_b^{\rm core}(M,T)=
\sum_{h=\{d,e\}\in R_{\rm core}(M,T)}
u_{r(h)}^{[M]}de\,
{\bf1}_{\,c(h)<b<i(h)}.
\]
The cuts comprise the full integer range; none are selected or discarded.
The same record retains its single price across its exact interval of cuts.
Empty record sets and empty sums have value zero.

### Complete quantified proposition

\[
\boxed{
\begin{gathered}
\forall C\in\mathbb R_{>0}\ \forall m_0\in\mathbb N,\ m_0\ge2,\quad
\exists K\in\mathbb R_{\ge0},\\
\forall M\in\mathbb N,\ M\ge2,\quad
\forall (a_1,\ldots,a_M)\in\mathbb N_{>0}^M:\\
\left[
a_1<\cdots<a_M,\quad P_M\text{ is Sidon},\quad
\forall n\in\mathbb N,\ m_0\le n\le M
\Rightarrow H_n\le Cn^2\log(2n)
\right]\\
\Longrightarrow\quad
\forall T\in\mathbb N,\ 2\le T\le M,\qquad
\sum_{b=2}^{T-1}\frac{\sqrt{P_b^{\rm core}(M,T)}}b\le K.
\end{gathered}}
\]

K may depend only on C and m0; the five numerical localization parameters
are already fixed. It may not depend on M,T, any point a_j, the particular
history, a choice of cuts, or a later extension. The cap is required at
every intermediate rank from m0 through M, not only at T or M.
When M<m0 its range is empty; those bounded-length prefixes are still
included and are uniformly handled by P_b<=1/8.
There is no hypothesis that a finite prefix extends to an infinite
history satisfying the cap. No blocks, LP optimizers, random variables,
or independent-label models are free parameters in this theorem.

### Existing inputs and their status

| Input | Status |
|---|---|
| Literal target, integer equivalence, exact negation | LEAN-VERIFIED |
| Positive-difference injectivity, finite one-copy envelope/accounting | LEAN-VERIFIED supporting results |
| Actual quartic and causal coefficient identities | MATH-REVIEWED |
| Rank commutator and capacity upper bound | MATH-REVIEWED |
| Raw repeated-endpoint bound and actual incidence counts | MATH-REVIEWED |
| Six-class finite-error localization | MATH-REVIEWED by Gate 0 in this audit |
| Two-lookahead epochs and actual half-block demand divergence | MATH-REVIEWED |
| Finite-component-to-complete-source passage below | MATH-REVIEWED elementary limit argument in this audit |
| The boxed uniform inequality | NEEDS-PROOF |
| Final Lean chain and literal Q1 theorem | NEEDS-PROOF |

No PROVISIONAL statement is assumed. The numbered theorem is a U4-F
sufficient formulation, not a requirement that every proof of Q1 use Fourier
profiles. Its qualitative existential-K form is in fact logically equivalent
to Q1 via the finite-tree argument in Section 9; this audit does not claim
that freezing it has made a weaker unsolved problem available.

## 7. Exact downstream implication, if the theorem is proved

First, the finite-component version of Gate 0 and of the commutator bound
is legitimate. Its weights are decreasing and satisfy
u_r^[M]<=alpha_r/H_r^2. All deletion proofs above use these bounds and
actual finite incidences. The commutator proof uses a finite positive Abel
measure with its terminal u_T^[M] term, so its algebra and constants also
hold. Alternatively a finite Sidon prefix can be extended to an arbitrary
infinite integer Sidon history for the unconditional upper bounds, without
assuming that extension has a cap.

Now suppose an infinite actual Sidon history has one fixed diameter cap
C,m0. For each fixed output horizon T, its genuine component partial sums
increase to the original complete-history u_r as M tends to infinity.
For r<=T,
\[
0\le u_r-u_r^{[M]}
\le\frac{\alpha_{M+1}}{H_{M+1}^2}\longrightarrow0.
\]
The finite record set through T is stable under extension, by unique actual
endpoints. Thus the finite sum of square roots converges to the original
N_T(core). The theorem's same K bounds every M>=T, so
N_T(core)<=K for every T. Gate 0 then gives N_T(P)<=K+B, with the
single absolute finite error B=B_(1,2,3,2,3).

Choose lambda=0 in the existing source. Define its actual eligible capacity
without using a multiset quotient:
\[
\operatorname{Elig}_T=
\sum_{\substack{\{d,e\}\subset F_M\cup(-F_M),\ d\ne e\\
 |d-e|=a_r-a_i,\ \max(\tau(|d|),\tau(|e|))<i<r\le T}}
 u_r |de|.
\]
For T fixed, M may be any M>=T; source labels in a contributing record
already occur before i, so this definition is independent of M.
Here u is the complete-history price, not its finite partial price.

The reviewed commutator inequality yields
\[
\operatorname{Elig}_T\le C_0+4\sqrt{2/3}\,N_T(P)
\le C_0+4\sqrt{2/3}(K+B),
\]
where
\[
C_0=\frac{4(\zeta(3/2)-1)}{3\sqrt2}
       +\frac{\zeta(2)-\zeta(3)}3.
\]
The opposite-sign and fresh repeated contributions at lambda=0 are included
in this inequality even though P_b uses positive source labels only.

The independent lower side uses K0=32, good dyadic old ranks n=2p,
and actual half-blocks B_n={a_(n+1),...,a_(3n/2)}:
\[
H_p\ge2H_{p/2},\qquad H_n\le K_0H_p,\qquad
H_{2n}\le K_0H_n.
\]
The two-lookahead lemma gives a divergent sum of 1/log(2n) over these
good ranks. With epsilon0=1/(8K0) and c_tail=7/(144K0^2), the existing
mass-only raw demand satisfies
\[
\delta_n(0)\ge
\frac{c_{\rm tail}\epsilon_0^2}{8(K_0+2)C\log(2n)}
-\frac1{4(n-1)}.
\]
The error has a finite sum on dyadic n; hence sufficiently late positive
demands have divergent sum. These half-blocks are pairwise disjoint as
actual point blocks. Sidon uniqueness makes their internal differences
disjoint, and the existing source payment gives
\[
\sum_{\substack{n\ {\rm selected}\\3n/2\le T}}
\max(\delta_n(0),0)\le\operatorname{Elig}_T.
\]
This contradicts the upper constant as T grows.

Consequently no fixed-cap infinite actual Sidon history exists. Section 2
then gives literal original Q1. The remaining work after a mathematical
proof of the boxed estimate is formalizing the dependencies actually used,
constructing the literal Lean Q1 proof, and completing the required release
and axiom/dependency checks. There is no additional unproved global
allocation or Gamma/Psi margin estimate on this selected path.

## 8. Bounded pre-freeze falsification

One read-only falsifier was used, with delegation depth one. It performed
only bounded exact enumeration and supplied the following results; no
source/evidence files were modified and no extra agents were created.
These are category C evidence for the finite checks. They are not a
verification of the theorem's uniform K.

### Enumerated inputs and exact checks

All 5,369 subsets with minimum 1, maximum at most 24 and size 2–6 satisfying
repeated-sum Sidon were covered, together with these eight fixtures:

~~~text
(1,14,30,36,38,41)
(1,4,6,12,28,41)
(1,2,4,8,13,21,31)
(1,2,4,8,13,21,31,45)
(1,2,4,8,13,21,31,45,66)
(1,2,4,8,13,21,31,45,66,81)
(1,2,4,8,13,21,31,45,66,81,97)
(1,2,4,8,13,21,31,45,66,81,97,123)
~~~

The first two are positive translations of the source's six-point fixture
and reflection. The last six are deterministic greedy prefixes.
Across the 5,377 histories, the exact enumeration covered 48,578 signed
retired records: 42,362 non-six and 6,216 six-distinct, together with
12,280 eligible triple collisions and 2,140 positive eligible records.

No counterexample was found to the fixed-(c,i,e,sign) uniqueness, the
I_(c,i) bound, disjoint triple-multiset classification, the twelve-record
six-endpoint factor, the absolute raw repeated-stage bound, or the
source-record/covariance identity. The last identity was compared
coefficientwise in independently named output prices, not only at one
chosen set of weights.

The maximum observed I_(c,i)/[2 binom(c-1,2)] was 2/3 at (c,i)=(4,5)
for (1,5,7,10,17,18). The maximum observed raw-stage/bound ratio was
1781/173400 at r=6 for (1,3,8,14,17,18).

### The frozen core and component prices

Only the greedy fixtures of length 10,11,12 had nonempty cores:

| M | Core records | Maximum over T<=M of N_T(core), approximate |
|---|---:|---:|
| 10 | 5 | 0.0004225141216053640546 |
| 11 | 9 | 0.0008006811536594995428 |
| 12 | 20 | 0.0012010780282121734720 |

All three have
max_(2<=n<=M) H_n/[n^2 log(2n)] approximately
0.2776352673700936014, attained at n=9.
For M=T=12 the nonzero exact coefficients are

~~~text
P_7  = 42967789 / 23906323584000
P_8  = 16592136787 / 1577817356544000
P_9  = 24872453269 / 2524507770470400
P_10 = 993 / 152181458
~~~

Reproduction procedure: recursively append each admissible integer through
24, then add the eight fixtures. Build the unique endpoint dictionary for
positive differences, enumerate unordered signed pairs and retrieve outputs
by exact integer lookup. Compare the stated coefficient identities and raw
bounds using integer/rational arithmetic. For the core inequalities, write
n=2^s q, 1<=q<2, and use forty rational terms of
log q=2 sum_(j>=0) z^(2j+1)/(2j+1), z=(q-1)/(q+1).
The omitted tail is bounded by 2z^81/[81(1-z^2)]; use the same enclosure
for log 2. Every tested strict comparison was resolved by these enclosures.
Prices and profile coefficients were exact rational numbers; displayed
square roots and cap ratios used 45-digit Decimal evaluation.

### Boundary and adversarial interpretation

- T=2 has no cuts and gives zero; no H_1 denominator is used.
- c=b and i=b are excluded. A source/output record with i=c+1 covers
  no cut and contributes zero, not an exceptional allowance.
- Same-birth positive sources have an old output. All repeated-endpoint
  cases are included in Gate 0's absolute class; they are absent from core.
- No signed product is replaced by its positive part in an identity.
  The core has d,e>0; the signed carrier's other cases are controlled by
  the reviewed lambda=0 commutator inequality.
- Empty/singleton blocks are not parameters of the selected theorem.
  The lower-side half-blocks have m=n/2>=2 at their stated late dyadic ranks.
- A terminal output r=T remains at its actual partial price. The M>=T
  component horizon is independent of T, and constants cannot depend on it.
- Translation by 101 was checked on all eight fixtures. Dilation by 2,3,10
  preserves the full profile exactly and scales the cap constant by the
  dilation. The absolute t cutoff makes core membership non-invariant in
  general; unchanged membership in these tests is not a general theorem.
- The raw finite no-go family x_i=2pi+(i^2 mod p), translated by 1,
  is not a falsifier at a common fixed cap/onset: for m0=2 its H_2=2p+1
  already forces C>=(2p+1)/(4 log 4). Moving m0 with p is also forbidden.
- A finite number of profile values, however large, cannot refute
  existence of an unspecified K(C,m0). Such a refutation needs an
  unbounded family with the same C,m0, not refitting them at each horizon.

No counterexample to the frozen statement was obtained. No uniform bound
was established by these checks.

## 9. If the theorem is false: exact consequence

Negating the boxed proposition gives one fixed C>0,m0>=2 and, for every
K, an actual capped finite prefix and T<=M whose core profile exceeds K.
Since P_b<=1/8, unbounded profile values force unbounded T and M.
After normalizing a_1=1, the finite-tree argument in Section 2 then
produces one infinite actual Sidon history with the same diameter cap.
That is a counterexample to original Q1 by the cap/negation bridge.

Thus a rigorous falsification of this particular uniform finite theorem
would do more than eliminate U4-F: it would refute Q1, and no affirmative
route U4-E/U4-R/U4-G could then succeed. This is different from the existing
raw-bound counterfamilies, which eliminate only a route-specific intermediate
estimate and do not keep a common cap and onset.

Conversely, if Q1 is true, every fixed C,m0 admits a finite maximum capped
prefix length by the same finite-tree argument. The bound P_b<=1/8 then
provides some finite K(C,m0); prefixes shorter than m0 are also bounded.
Hence the qualitative existential-K theorem is equivalent to Q1. This is
explicitly a concrete Fourier formulation of the remaining original
difficulty, not an assertion of progress from a new assumption.

## 10. Next exact proof-search action — for a later turn only

Start from the boxed Q1191-U4F-CORE-UNIFORM-01 statement and the exact
dyadic coverage formula
\[
I_N^{\rm core}(M,T)=
\sum_{h\in R_{\rm core}(M,T)}
u_{r(h)}^{[M]}de\,\ell_N(c(h),i(h)),
\quad
\ell_N(c,i)=\sum_{\substack{N\le b<2N\\c<b<i}}\frac1b.
\]
The actual within-block Cauchy bound is
\[
\sum_{N\le b<2N}\frac{\sqrt{P_b^{\rm core}(M,T)}}b
\le\sqrt{(\log2+1/N)\,I_N^{\rm core}(M,T)},
\]
with cuts outside 2<=b<T interpreted as zero. Preserve the same physical
records, two horizons, fixed cap/onset and all strict core conditions.
The next run's proof or falsification must address the boxed bound itself;
this sufficient Cauchy inequality is not a second frozen theorem.
Do not replace coverage by independent copies or use the false raw
T^3 H_T^2 saving.

The orderedCard/6 multiset identification can be formalized in a separate
later formalization effort. It is not the next mathematical theorem here.
No proof attempt for Q1191-U4F-CORE-UNIFORM-01 was begun in this audit.
