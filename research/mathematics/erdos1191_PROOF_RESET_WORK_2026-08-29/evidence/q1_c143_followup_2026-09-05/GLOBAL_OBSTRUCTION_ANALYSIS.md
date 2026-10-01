# Q1 after C143: finite-horizon target and rigorous localization barriers

Date: 2026-09-05. Author: independent mathematical audit agent.

Status: **Q1 remains unresolved.** This memo proves two scoped localization
obstructions and a finite-tree equivalence, and isolates the extra analytic
identifications a positive finite C143 bank does not supply. It does not claim
an arbitrary-history counterexample to the graph method or to Q1.

The canonical inputs read for this audit were `00_START_HERE_PROMPT.txt`,
`UPDATED_START_HERE.md`, `QUANTIFIER_AND_REDUCTION_AUDIT.md`, registry rows
C058, C113, C115--C121 and C138--C139, and the route-probe notes cited below.
The newer implementation inspected was
`/Users/USER/Downloads/C143_S32_S41_FULLROOT_EXACT_PHASE_2026-09-04_V2/c142/master.py`.
Recovery and independent replay of its bank are handled by the main audit;
this memo does not duplicate or assume the outcome of that replay.

## 1. Exactly what must ultimately be proved

An infinite integer Sidon set has an increasing enumeration
`a_1<a_2<...`, with every positive difference distinct. Q1 is

\[
 \forall A\quad \liminf_{x\to\infty} A(x)\sqrt{\log x/x}=0.
\]

The audited critical-cap equivalence says this is equivalent to the
nonexistence, for every finite `C>0`, of an infinite Sidon sequence satisfying

\[
 a_m\le C m^2\log(2m)\qquad(m\ge m_0).
 \tag{1}
\]

In particular a finite collection of successful optimization problems is
evidence about those finite inputs, irrespective of whether the collection
contains every phase of each input.

There is a useful exact finite reformulation which avoids treating
compatibility as an additional mysterious limiting step.

**Finite-tree theorem.** Q1 holds if and only if, for every pair of positive
integers `C,m_0`, there exists a finite `N>=m_0` such that no `N`-mark Sidon
sequence obeys (1) for every `m_0<=m<=N`.

**Proof.** It suffices to use integer `C`, because any finite real cap is
dominated by an integer cap. Fix `C,m_0` and set

\[
 b_i=\left\lfloor C\max(i,m_0)^2
                      \log(2\max(i,m_0))\right\rfloor.
\]

Consider the tree of all finite increasing positive-integer Sidon sequences
whose `i`th entry is at most `b_i`. Each node has finitely many children.
Any Sidon sequence of length at least `m_0` obeying (1) also belongs to this
tree: its earlier entries are bounded by its `m_0`th entry. If such sequences
exist to arbitrarily large lengths, the finitely branching tree has an
infinite path by König's lemma. That path obeys (1). Conversely an infinite
path supplies every finite length. This proves the equivalence. ∎

Thus changing finite rulers at every depth is not an obstruction to a
compactness argument **when both `C` and `m_0` remain fixed and the cap is
enforced at every intermediate rank**. It is an obstruction when these
uniform hypotheses are missing. The theorem does not make finite exhaustive
search practical and gives no computable bound `N(C,m_0)` by itself.

## 2. Horizon-dependent certificates are a legitimate escape

A uniform finite contradiction need not construct one infinite optimizer,
one online algorithm, or one horizon-consistent graph. The useful quantifier
order is

\[
 \forall C,m_0\ \exists\epsilon>0,K<\infty,J_0\
 \ \forall J\ge J_0\ \forall\text{ capped finite towers through }J+1\
 \ \exists\text{ a legal certificate for that whole tower}.
 \tag{2}
\]

The certificate may depend on `J` and on the entire tower being contradicted.
What must be uniform are its final constants and boundary/error estimates.
If its use relies on a martingale, conditional expectation, predictable
channel choice, or an already fixed causal identity, the hypotheses of that
identity still apply. But nonanticipation is not a standalone logical
requirement for every possible proof of Q1.

Here is a precise sufficient target, without silently assuming the missing
common master. For every tower in (2), produce one set of owner projections,
phasewise corrections, and an **exact same-source global identity** giving

\[
 0\le R_J=B_J-\sum_{k=k_0}^{J-r}\omega_{k,J}\Phi_k,
 \qquad B_J\le K,
 \qquad\omega_{k,J}=\left({J+1-k\over J+1}\right)^2,
 \tag{3}
\]

where `r` is fixed, `R_J` is proved nonnegative, all terms have their physical
normalization, and every initial, shared-endpoint, birth, cutoff, final and
scale-terminal source is included once. Together with

\[
 \sum_{k=k_0}^{J-r}\omega_{k,J}\Phi_k
       \ge\epsilon\log J-K'
 \tag{4}
\]

this excludes all sufficiently deep capped towers. Equations (3)--(4) are a
sufficient Route-C architecture, not a theorem claimed here and not a
necessary characterization of all possible proofs of Q1. In particular,
the existing positive centered-covariance lower bound is not itself (3).

A concrete way to establish (4), already supported by the C115/C119 scalar
algebra, is

\[
 \Phi_k\ge {\epsilon-A\eta_k-[V_{k+1}-V_k]\over k+1}-e_k,
 \quad
 \eta_k=\log{H_{k+1}\over4H_k},
 \quad |V_k|\le B,
 \tag{5}
\]

with `A,B` fixed, and a uniform upper bound on
`sum omega_{k,J} e_k`. One may replace `V` by a fixed absolutely summable
linear combination of uniformly bounded coordinates. C115 proves
`sum omega eta_k/(k+1)=O_C(1)` and
`sum omega/(k+1)=log J+O(1)`. Finite Abel gives

\[
 \left|\sum_{k=a}^{b}p_k(V_{k+1}-V_k)\right|
 \le 2B p_a
 \quad(p_a\ge\cdots\ge p_b\ge0).
\]

This proves (4) from (5). What remains unproved is the legal arbitrary-rank
margin estimate (5), or a direct proof of (4), **and** its insertion into
the single identity (3). A constant allowed to deteriorate with the horizon
does not suffice.

The C113 last-three-epoch excision extends in the same manner to any fixed
number `r`: the omitted weights sum to `O(r^3/J^2)`, while the critical-cap
bound for the epoch demand is `O_C(J)`. The loss is `O_C(r^3/J)`. Thus a
strict Fejér ratio restriction bounded away from one can be handled by
discarding a fixed terminal number of epochs, provided the complete
baseline/cutoff ledger is retained. Shared physical owners still need proof.

## 3. New obstruction: fixed-rank positive windows miss the harmonic mass

Use the canonical zero-based notation

\[
 0=a_0<\cdots<a_{2n-1},\quad
 h_i=a_i-a_{i-1},\quad H=a_{2n-1}-a_{n-1}.
\]

For `n<=i<j-1<=2n-2`, write

\[
 M=h_{i+1}+\cdots+h_{j-1},\quad u=h_i,\quad v=h_j,
\]

and recall the positive primitive and its exact original weight:

\[
 C_{ij}=\log{(M+u)(M+v)\over M(M+u+v)},\qquad
 \alpha_{ij}={(j-i)^2\over4n^2},\qquad
 W_n=\sum_{i,j}\alpha_{ij}C_{ij}.
 \tag{6}
\]

For a rank cutoff `2<=L<=n-1`, define `W_n^{<=L}` by retaining only
`j-i<=L` in (6).

**Bounded-rank theorem.** For every strictly increasing integer prefix,

\[
 W_n^{\le L}
 \le {L(L+1)(2L+1)\over24n}\log H.
 \tag{7}
\]

**Proof.** The integer middle span satisfies `M>=1`, and

\[
 1\le {(M+u)(M+v)\over M(M+u+v)}
      \le {M+u\over M}\le H.
\]

Thus `0<=C_{ij}<=log H`. There are at most `n` pairs at each distance `d`.
Sum `n d^2 log H/(4n^2)` over `2<=d<=L` and use
`sum_{d=1}^L d^2=L(L+1)(2L+1)/6`. ∎

Here `W_n` is specifically the **Wave19 inner sector with `n` gap indices
`n,...,2n-1`**, not the Wave13 new-birth triangle with one additional gap.
For dyadic `n>=16`, the audited Wave19 inner-birth floor gives

\[
 W_n\ge {n^2\over384 a_{2n-1}}.
\]

For completeness, section 5 of
`core_workspace/endpoint_variance/WAVE19_INNER_BIRTH_SATURATION_NO_GO_2026-08-29.md`
proves

\[
 E'_n={n(n-2)(n^2+4n-14)\over48},\qquad
 W_n\ge {E'_n\over8n^2H}.
\]

For `n>=16`, `2n^2-22n+28>=0` implies `E'_n>=n^4/48`, yielding the
displayed bound since `H<=a_{2n-1}`. The small cases `n=4,8` are not being
silently covered by that simplified constant and are irrelevant to the
asymptotic assertion.

Under the eventual cap `a_{2n-1}<=4Cn^2 log(4n)`, (7) therefore gives

\[
 {W_n^{\le L}\over W_n}
 \le {64C L(L+1)(2L+1)\over n}
      \log\bigl(4Cn^2\log(4n)\bigr)\log(4n).
 \tag{8}
\]

For fixed `C,L`, the right side tends to zero. More generally it tends to
zero whenever `L^3(log n)^2/n -> 0`.

There is a stronger dyadic consequence. At `n=2^k`, the cap gives
`log H=O_C(k)`, so (7) gives

\[
 W_{2^k}^{\le L}=O_{C,L}(k/2^k),\qquad
 \sum_{k\ge k_0}\omega_{k,J}W_{2^k}^{\le L}=O_{C,L,k_0}(1)
 \tag{8a}
\]

uniformly in `J`, because `0<=omega<=1` and `sum k/2^k<infinity`.
Meanwhile the full inner sector has

\[
 \sum_{k=k_0}^J\omega_{k,J}W_{2^k}
 \ge {\log J\over1536C\log2}-O_{C,k_0}(1).
 \tag{8b}
\]

Thus fixed-rank positive original-budget windows supply only a bounded total
on the entire Fejér history, while the target inner-sector signal is
harmonic. This corollary requires no geometric nondegeneracy assumption.

**Consequence for C116.** Any family of consecutive 16-mark windows contains
only primitives with gap-rank separation at most 14. If each original
positive primitive is charged at most once, even using **all** such windows
captures at most `W_n^{<=14}=o(W_n)`. Selecting a positive fraction of
mark-disjoint good windows cannot improve that bound. A uniformly positive
fraction of the original harmonic signal cannot be recovered by simply
pasting positive fixed-window primitive budgets.

This theorem is scoped to the original positive primitives and their
one-use capacities. It does not exclude a new signed identity, different
negative source, long-range correction, or a localization theorem with
additional transport that genuinely accounts for the missing interactions.
Scaling a local coefficient above its available global `alpha_ij` is not
such a theorem; it changes the ownership budget.

## 4. New exact support obstruction to literal fixed-window matrix paste

The direct physical matrix is `M_n=D^T B_n D`, with

\[
 (B_n)_{ij}=\begin{cases}
 0,&|i-j|\le1,\\
 -(i-j)^2/(8n^2),&|i-j|\ge2.
 \end{cases}
\]

For interior physical indices `1<=i<j<=n-1` with `j-i>=3`, direct mixed
differencing yields

\[
 (M_n)_{ij}={1\over4n^2}.
 \tag{9}
\]

Indeed, with `d=j-i`, the numerator is
`-2d^2+(d+1)^2+(d-1)^2=2`, divided by `8n^2`.

Every matrix supported within one consecutive window of at most `L+1`
physical coordinates has zero entries for `|i-j|>L`. Every finite sum of
such matrices has the same zero pattern, irrespective of the signs of the
summands, their coefficients, or how their windows overlap. By (9) it cannot
equal `M_n` once there are interior coordinates separated by more than
`max(L,2)`.

This is an exact algebraic obstruction to literal matrix pasting. It does
not prohibit domination on a restricted actual-state family or the addition
of roots/corrections connecting distant windows. Those additions are the
substantive new ingredient needed.

## 5. Fixed rank also lacks uniform geometric compactness

C116's refined good-window filter supplies normalized gaps only in

\[
 \left[{1\over57600C\log(4n)},\ {1\over2}\right].
\]

The lower endpoint tends to zero with rank. Thus the parameter region allowed
by these bounds has collapsed boundary points; the estimates do not exclude
degeneracies in a uniform closure of the actually realizable family. Exact coverage
of all phase chambers of one nondegenerate ruler, or even a finite family of
such rulers, does not give a uniform positive margin over that closure.
A compactness proof would need a closed normalized parameter class including
these limits and a lower-semicontinuous margin bounded strictly away from
the required threshold on the entire class. Neither property follows from
finite bank enumeration. The loss quantified in (8) is independent of this
geometric degeneration and already blocks the simple positive-window route.

## 6. Four-scale phase integration and the lower-cutoff residual

This identity uses the literal C143 `c142/master.py` normalization. Let
`K_T=T^{-1}1_[0,T)` and `h_T=K_T-K_{2T}`. For an epoch `e`, let

\[
 Q_e(T)=\langle M_e,\operatorname{Gram}
                    (\delta_{a_i}*K_T)\rangle.
\]

The audited box refinement identity gives
`<M_e,Gram(delta*h_T)>=Q_e(T)-Q_e(2T)`. The implemented channel at width
`T=mt` is

\[
 q_{i,m,t}={8\over m}
     (1_{[a_i,a_i+mt)}-1_{[a_i+mt,a_i+2mt)})
          =16t(\delta_{a_i}*h_{mt}).
\]

Define the integrated unweighted direct epoch demand using exactly the
implemented factor `m/128`:

\[
 d_e(t)=\sum_{m\in\{1,2,4,8\}}{m\over128}
                    \int q_{e,m,t}^T M_e q_{e,m,t}\,dx.
\]

Then a change of variable `T=mt` proves the exact identity

\[
 \int_b^{2b}{d_e(t)\over t^2}\,dt
   =2\int_b^{16b}Q_e(T)\,dT
      -\int_{2b}^{32b}Q_e(T)\,dT.
 \tag{10}
\]

If the epoch span is at most `16b`, so `Q_e` vanishes above `16b`, this is

\[
 W_e-\int_0^b Q_e(T)\,dT+\int_b^{2b}Q_e(T)\,dT.
 \tag{11}
\]

Thus vanishing upper same-atom terminal does not identify the four-scale
phase demand with the complete Wave mass. The lower-cutoff adjustment in
(11) remains, with its signed value. Formula (10), rather than (11), must
be used when an old epoch span exceeds the relevant cutoff. Fixed epoch
weights can be included by linearity.

The all-dyadic-scale version, with the lower cutoff below every active
primitive and the upper cutoff above support, does recover `W_e`. But a
certificate involving only four scales establishes its own truncated
quantity until the additional rows or a rigorously owned residual estimate
are supplied. The correct phase measure here is `dt/t^2`; replacing it by
`dt/t`, or integrating a minimax objective instead of the signed physical
margin, changes the quantity.

## 7. What is rigorously isolated now

The finite C143 bank can settle feasibility, full-root optimality and signed
phase integration for the histories, ranks, owner convention, scales and
weight ratios actually included. It cannot alone settle any of the
following necessary steps of the proposed Route-C implementation:

1. A uniform estimate for arbitrary capped histories and arbitrarily large
   rank. Positive fixed-window pasting is blocked by (7)--(9); a new
   long-range or signed mechanism is required.
2. Identification of the finite demand and price with the exact global
   source ledger, including the lower cutoff in (10), any nonzero upper
   terminal, shared physical owners and original Gothic sources used once.
3. A horizon-uniform net gain such as (4), with an actual opposite-sign
   master identity such as (3). A list of positive local margins is not that
   identity.

One can pursue these with a certificate chosen separately for each whole
finite tower, avoiding an unnecessary demand for one online optimizer.
Alternatively, a nonanticipating construction is acceptable if it proves
the required uniform statements. The exact ultimate obstruction is still
the absence of a proof excluding arbitrarily deep fixed-`C`, fixed-onset
capped Sidon trees; the finite-tree theorem states this without extrapolation.

## Sources within the project

- `QUANTIFIER_AND_REDUCTION_AUDIT.md`, sections 1--3 and C115/C116 update.
- `route_probes/ROUTE_C_CRITICAL_SPAN_POTENTIAL_AND_GOOD_WINDOWS.md`.
- `route_probes/ROUTE_C_BOUNDED_GAP_PROFILE_POTENTIAL.md`.
- `route_probes/ROUTE_C_ORDERED_SUFFIX_PROFILE_POTENTIAL.md`.
- `route_probes/ROUTE_C_CROSS_RATIO_BOX_DIPOLE_BRIDGE.md`, (1.1)--(1.2).
- `core_workspace/endpoint_variance/WAVE19_INNER_BIRTH_SATURATION_NO_GO_2026-08-29.md`, section 5.
- `route_probes/ROUTE_C_DIRECT_ORDERED_B_INTERVAL_HAAR.md`, (1.4), (1.6),
  (4.1)--(4.7).
- `route_probes/ROUTE_C_FEJER_TERMINAL_EXCISION.md`.
- `route_probes/ROUTE_C_CENTERED_MULTIBAND_HISTORY_CARRIER.md`, section 5.
- The literal newer C143 `c142/master.py` path given above.

The new arguments in sections 1, 3, 4 and 6 are elementary derivations from
the displayed formulas. They have not been entered into the claim registry
or promoted to Lean/Rocq status by this memo.

## Independent review of the terminal and cutoff calculations

The sibling `c143_terminal_audit.py` and `c143_cutoff_audit.py` were reviewed
against their formulas. No normalization or sign error was found in the
current versions read on 2026-09-05. In particular:

- `point_matrix_integer(e)` returns `K=8e^2 M_e`, so the unordered box pair
  coefficient in the cutoff checker is `K_ij/(4e^2)=2(M_e)_ij`.
- The primitive integral is exactly
  `integral_a^B (T-d)/T^2 dT=log(B/a)+d(1/B-1/a)`, with `a=max(A,d)`.
- For raw Haar signs, the autocorrelation is `2T-3d` for `0<=d<=T`,
  `d-2T` for `T<=d<=2T`, and zero afterwards. Therefore the terminal
  checker's unordered coefficient `16K_ij/(m^2 e^2)` includes the required
  symmetric factor of two and the square of `8/m`.
- Its cumulative Abel coefficient is `(2^(s+1)-1)/128`; adding the final
  `15U_4/128` leaves precisely `sum_s 2^s U_s/128`. The nonzero old
  terminal therefore has the displayed positive formal coefficient even
  though its physical integral happens to be negative on this fixture.
- The rational atanh series lower bound and geometric remainder upper
  bound have the correct sign. Sign-aware interval arithmetic and outward
  fences are used in the displayed comparisons.

The zero-tail checks have a direct interpretation. Writing `d_ij=b_j-b_i`,

\[
 Q_e(T)=\sum_{i<j}2(M_e)_{ij}{(T-d_{ij})_+\over T^2},
\]

and the two exact identities
`sum_{i<j}M_ij=0`, `sum_{i<j}M_ij d_ij=0` make this zero for `T>=H`.
Integration to `H` cancels both the `log H-1` term and the `d/H` term:

\[
 \int_0^H Q_e(T)\,dT
       =-\sum_{i<j}2(M_e)_{ij}\log d_{ij}=W_e.
 \tag{12}
\]

The last equality follows by expanding each positive cross ratio in (6)
into its four logarithms; its distance coefficients are exactly `-2M`.
This was also checked independently on the hash-pinned C143 ruler by
enumerating the positive primitives, without using `Q_integral` to obtain
their coefficients: all 105 epoch-16 and 465 epoch-32 cross ratios matched
the `-2M` coefficient dictionaries exactly. Their rational logarithm bounds
give precisely the same outward fences as the box integral checker:

| quantity | lower bound | upper bound |
|---|---:|---:|
| `W_16` | `103342097371/10^12` | `25835524343/(25*10^10)` |
| `W_32` | `6109364193/(5*10^10)` | `122187283861/10^12` |

The recovered fixture has `H_old=76869`, `H_new=4150`, `b=2075/8`.
Its complete-cutoff formula is

\[
 I_e=W_e-\int_0^bQ_e+\int_b^{2b}Q_e
                -2\int_{16b}^{\infty}Q_e+\int_{32b}^{\infty}Q_e.
 \tag{13}
\]

Thus the old epoch has substantial nonzero tails, and its four-scale
signed demand integral is negative despite `W_16>0`. The numerical values
below summarize rigorous rational intervals from the sibling artifacts:

| quantity | approximate value |
|---|---:|
| old same-atom terminal integral | `-0.007017838` |
| new same-atom terminal | identically zero |
| old four-scale demand integral | `-0.007230289` |
| new four-scale demand integral | `0.128883128` |
| integrated graph price | `0.19636233` |
| `2(W_16+W_32)-integrated price` | `0.25469642` |

The final comparison is strictly positive. Therefore this cutoff audit
does **not** produce a numerical no-go for the recovered fixture. It
quantifies the correction needed to interpret its four-scale signal and
eliminates an unverified identification `D=W`. The result remains a
fixed-fixture comparison; it supplies neither the missing global signed
identity (3) nor a proof paying every physical source on arbitrary towers.
