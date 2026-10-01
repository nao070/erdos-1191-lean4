# Independent review of the productive triple-potential source

2026-09-05, 14:04:42 UTC. Reviewer: `/root/moment_evidence_audit`, inherited
GPT-6 Astra Ultra. Read the entire source and independently rederived
equations (1)–(20), including the complete-history tail and the component
allocation over the longer physical horizon.

Final reviewed source: `research/triple_potential_productive_source.md`,
SHA-256 `f9be618684b2ed933b480f4107c0ccdbddffd309339e7d63db831d511cf920ff`.
The earlier `c1d6eaba09e6433ebedaacdb717d303eb326d2b656f84f4b81f8e86dc4b489e5`
version was read in full. The author then applied the sole requested domain
clarification in §4: `k≥n≥2` and a nonempty block. The final bytes were read
back. No mathematical formula changed.

**Verdict:** the Gram source, trace and tail bounds, defect financing,
long-horizon demand, and shared-bank allocation are valid at their stated
scope. No material mathematical correction is needed. This is an analytical
review; no finite computation, prior-test replay, Lean build, axiom audit,
kernel replay, or edit to the author's source was performed by this reviewer.
The smaller eligible-capacity-minus-demand residual and Q1 remain unresolved.

## Fiber potential, Gram construction, and convergence

In (1), a triple with a repeated largest slot has zero potential. A unique
largest slot and distinct smaller slots has two ordered square terms, while
two equal smaller slots has one. The prefactor `1/2` therefore gives exactly
the weights `1` and `1/2`; no triple multiplicity is lost.

The finite feature `R_k(s)=sqrt(S_k(s)P_k^top(s))` has squared norm `L_k`.
Its translates define precisely the matrix in (2), including the factor
`Q_k²H_k²` in the denominator. The matrix is Gram and entrywise nonnegative,
and is zero when either label index is outside the component bank. There is
no output mask in this construction.

Distinct equal-sum actual Sidon triples have disjoint supports. In the three
multiplicity types, `1/aut(U)≤|support(U)|/3`, so each fiber has weight at most
`k/3`. The full weighted triple count is `k³/6`, from the `6/aut(U)` ordered
realizations. These yield `L_k≤k⁴H_k²/18` as in (3).

The full-defect input was also checked at its exact fiber grouping: the
unordered distinct-pair potential is `S_k P_k^top` minus the single diagonal
`sum_U w(U)²Ptop(U)`. The latter is at most `k³H_k²/6`. This proves (4),
including repeated newest endpoints and the nonnegative automatic remainder;
no diagonal is discarded without its explicit allowance.

Each component diagonal is `L_k/(Q_k²H_k²)`. With `Q_k` labels, its trace is
`L_k/(Q_kH_k²)≤k²/9`, while its full matrix mass is at most `L_k/H_k²`.
For the exact sums (5), the identities

\[
 \kappa_k k^2=\frac1{(k-1)^2}-\frac1{(k+1)^2},
\]

and

\[
 \kappa_k k^3=
 \frac1{(k-1)^2}+\frac1{(k+1)^2}+\frac2{k^2-1}
\]

give `5/4` and `2 zeta(2)+1/4`. Hence total trace is at most `5/36`.

On the restriction to the earlier `Q_N` labels, a future component contributes
mass at most `Q_N² k⁴/(18Q_k²)`. For `k>N`, the ratio `k/(k-1)` is at most
`(N+1)/N`; summing its fixed coefficient tail gives exactly
`(N-1)²/(18N²)≤1/18`. This verifies (6), proves finite convergence of the
complete future tail on each restriction, and justifies passing the PSD and
nonnegative properties to the permanent source. Entries are not renormalized
when a terminal prefix changes.

## Defect financing and one combined source

For a permanent nonnegative source, the physical historical maximum selects
each source pair precisely when its output is unused at its later source
birth. Thus its historical capacity is bounded by half the full matrix mass.
This upper bound includes never-used outputs and outputs beyond the terminal
rank; it is not an eligible-only truncation disguised as historical capacity.

The interior component defect cost in (4) is at most the exact layer sum
`Gcal_N`, because the omitted future components have the nonnegative terminal
value `Gcum_N`. The finite error cost is `D_3/6` and the tail cost is `1/18`.
After dividing mass by two, the constant becomes

\[
 D_3/12+1/36=\zeta(2)/6+7/144.
\]

This checks both lines of (7). Adding `(1+lambda)Theta` to the unchanged
`Psi_lambda` gives one PSD nonnegative source. The exact old eligible deficit
`-Gcal_N/8` and the cost upper bound cancel in the valid direction, proving
(9). This is an upper financing inequality, not an identity identifying all
new payments with all geometric defect.

## Tensor demand and the fixed component across cells

For (10), the unnormalized tensor shadow has total mass
`mQ_n sum_s R_k(s)` and exact diagonal contribution `mQ_n L_k`. Its first
coordinate is supported on the actual interval minus the block holes;
Sidon difference uniqueness makes it vanish at every block point. The second
coordinate has at most `3H_k+2H_n+1` possible sites. Cauchy on this rectangle
and division by the exact Gram normalization yield (10) with its factor two.
The clarified conditions `k≥n≥2` and a nonempty block ensure the displayed
normalizations and hole-support denominator are well-defined.

The nearby half-block comparison has the stated weaker reciprocal-log-square
scale: `sum R_k≥Ptot_N/H_k`, the good-window radius bounds control both tensor
support lengths, and the weighted trace loss has order `1/N`. Reciprocal-log
divergence of good windows alone does not make that weaker estimate diverge.

For the longer allocation, translating the history's first point to zero is
legitimate: all radii and physical labels are unchanged, and the fiber
translation only shifts the dummy Gram index. With `D=H_k`, each integer cell
contains `D` possible sites and is strictly after the old component bank.
Its feature shadows have support length at most `3D`; mass projection over
the first coordinate, summed over the feature coordinate, gives exactly

\[
 J_j=\tfrac12\{m_j^2 M_k/(3D)-m_jT_k\}.
\]

The actual off-diagonal pair expansion has no missing multiplicity because
the block's positive differences are unique. For empty cells the demand is
zero. For singleton cells it cannot be positive, since their actual pair
payment is zero. Keeping positive parts therefore has the stated valid lower
bound after summation.

Different cells have disjoint actual point sets. Equal positive differences
in two cells would contradict Sidon uniqueness, so their difference sets are
disjoint. Consequently every fixed pair entry of this same `A_k` pays at
most one cell, regardless of the number of later cells considered. This is
the essential shared-bank step in the proof.

## Hardy estimate, constants, and finite horizon

For the translated counting function, integer spacing gives
`A(X)+1≤X+2`. Its next endpoint exceeds `X` and obeys the one fixed eventual
cap. Substitution into that cap gives
`A(X)≥sqrt(X/[C log(2X+4)])-1`. The cell count is exactly
`F_j=A((j+1)D)-k`. Enlarging the logarithm and decreasing the numerator
produces (12) in the stated direction. For sufficiently large `k`, the same
fixed onset applies simultaneously to every cell used.

The continuous step-function Hardy argument is valid on each finite horizon:
the boundary term at zero vanishes, and the terminal integration-by-parts
term is nonpositive. Cauchy gives `integral(F/x)²≤4 sum m_j²`. Integrating on
`[j,j+1]`, where `F(x)≥F_j`, proves (13).

On `ceil(k^(1/2))≤j<floor(k^(3/2))`, the Sidon lower radius bound and the
fixed cap make the square root in (12) uniformly more than twice `k+1`
eventually. Squaring the resulting half-root lower bound and applying Hardy
gives the coefficient `D/(16C)` in (14). The radius satisfies
`log D=2 log k+O_C(log log k)`. The corresponding integral has value

\[
 \log\!\left(\frac{2+3/2}{2+1/2}\right)+o(1)=\log(7/5)+o(1).
\]

Discrete-to-integral errors, floors, and ceilings are negligible uniformly
under those fixed bounds. No radius derivative or asymptotic equivalence to
the cap is assumed.

The unconditional Sidon count `A(X)≤sqrt(2X)+1` makes the total points in
these cells `O_C(k^(7/4)sqrt(log k))`. A uniform ratio
`T_k/M_k=O(log k/k²)` therefore makes their whole diagonal cost
`O(k^(-1/4)(log k)^(3/2)) M_k=o(M_k)`. The leading demand before absorbing
errors is `M_k log(7/5)/(96C)`; retaining half proves the stated `192C`
denominator in (15).

The physical terminal coordinate is `(floor(k^(3/2))+1)H_k`, and its actual
rank is bounded by the same point-count estimate. Every allocation therefore
has a finite terminal horizon. The eventual constants depend on the fixed
cap and the uniform trace-to-mass constants, not on separately chosen cell
or window onsets.

## Good windows and the final residual

The translates of `R_k` have aggregate mass `Q_k sum R_k` and support length
at most `5H_k+1`. Cauchy proves the component lower mass in §6. With the actual
weighted good-triple lower bound `Ptot_N≥beta N³H_N²`, the inequalities
`R_k≥P_k^top/H_k`, `H_k≤K H_N`, and `5H_k+1≤6H_k` give exactly

\[
 M_k\ge\frac{\beta^2N^6}{6K^5H_N}.
\]

The trace-to-mass ratio in (16) is consequently uniform over all sufficiently
late good windows. The coefficient tail
`sum_(N≤k<2N) kappa_k≥15/(16Q_N²)` gives the constant
`5 beta²/(32K^5 C)` in (17). Multiplying by (15) gives the `6144K^5 C²`
denominator in (18).

Distinct dyadic windows have disjoint component indices. Within each
component the cells spend each physical pair entry at most once; across
components, overlapping physical labels use different additive summands of
the same permanent `Theta` entry. This proves feasibility without requiring
output disjointness between different components or renewing a budget.
At a finite terminal prefix only completed rows are counted; increasing the
prefix eventually includes every row from every fixed finite window.
Nonnegative sums and good-window reciprocal-log divergence then prove the
claimed nonsummable actual future demands.

The additive demands for `Psi_lambda` and `(1+lambda)Theta` pay distinct
additive portions of `Omega_lambda`, establishing (19). The exact residual
split (20) retains both nonnegative unused-budget terms. A divergent amount
paid by the additional source is therefore not a negative copy of the old
uncontrolled residual.

Finally, for each fixed `0<epsilon<1`, replacing the physical cell exponents
by `epsilon` and `2-epsilon` gives the logarithmic ratio stated in §7, while
the diagonal error tends to zero because its polynomial factor is
`k^(-epsilon/2)`. The limit as epsilon tends to zero is only a comparison of
fixed-exponent bounds; it cannot be repeated independently on one component.
The available fraction still depends on the arbitrary fixed cap constant
`C`. These limitations, the uncontrolled smaller residual, and the unresolved
original Q1 are correctly stated.
