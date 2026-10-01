# Independent review of the difference-extension and weighted-shadow route

Date: 2026-09-05. Reviewer: `/root/global_route`. Reviewed source:
`difference_extension_route.md`, Sections 1--7, as saved by
`/root/c143_mathematics`. Only this review file is edited by the reviewer.

**Verdict:** the finite extension equivalence, equations (9), (13), (14),
(15), and the constant-barrier calculation in Section 6 are mathematically
supported by independent derivations below. These statements do not prove
Q1. No new claim has been checked by Lean and no numerical experiment was
run for this review.

## 1. Extension conditions and discrete interval convention

For ordered sets `P<B`, an equality of two cross differences is equivalent
to an equality between a positive internal P difference and a positive
internal B difference. The remaining cross/internal collisions are exactly
`B∩(P+P-P)` and `P∩(B+B-B)`. Repeated summands must be permitted in these
sumsets, as the source correctly does. The hypergraph correctly includes
two-vertex mixed violations and three-vertex future arithmetic progressions.

The interval length L used in (9) must mean its integer cardinality, so an
interval `[v,v+L-1]` has L points. This agrees with the source's explicit
`L_r=a_(2m)-a_(m+1)+1` later; there is no off-by-one mismatch.

One minor hypothesis clarification was sent to the author: in Section 6 take
`p≥max(n_0,2)` so that the full selected label set is nonempty and U>0.
All asymptotic uses already have p sufficiently large.

## 2. Independent derivation of (9) and (13)

Let B have m points and let u be supported on positive old differences.
Writing `r(z)=sum_(b in B) u_(z-b)`, direct expansion gives

    sum_z r(z)=mU,
    sum_z r(z)²=mS+2 sum_(b<b') K_u(b'-b).

The last sum equals Ψ_u(B) because B's positive differences are injective.
There is no assumption that differences *between old difference labels*
are injective. Their multiplicities are exactly what K_u retains.

Since no positive B difference is an old difference, `supp r` is disjoint
from B. Both lie in `[v,v+L+H-1]` if `B⊂[v,v+L-1]`. Therefore

    |supp r|≤L+H-m.

Cauchy--Schwarz proves (9). Combining its lower bound with Ψ_u(B)≥0 gives
(10), including the positive part and its factor 1/2.

For a fixed u, different compatible future shells have pairwise disjoint
internal difference labels, none an old label. Expanding U² yields

    sum_(t>0) K_u(t)=(U²-S)/2.

This is a single common budget. Subtracting its old-label expenditure gives
(12). Summing twice (10) and applying (12) gives exactly (13): both the
positive-part coefficient and the subtraction `2 sum_(t in ΔP) K_u(t)`
are correct. The argument does not require independence of the shells.

## 3. Exact conservation (14)

The positive difference labels of the full Sidon union partition into:
old/old, old/new, within one new shell, and between two different new shells.
No two physical pairs in these categories share a label. The complement of
their union is exactly the unused-label set. Summing K_u over this partition
proves (14), with each cross contribution counted once. K_u has finite
support, so the unused-label sum is finite despite being written over all
positive integers.

The distinction between (12) and (14) is material: the first drops nonnegative
old/new and cross-shell expenditure, whereas the second retains it. Neither
formula permits spending a fresh full budget at each future shell or each
new choice of the old prefix.

## 4. Endpoint subtraction (15)

For each old triple a<b<c, the two unordered pairs of old labels

    {b-a,c-a},    {c-b,c-a}

have old differences c-b and b-a, respectively. They are distinct because
Sidon excludes `b-a=c-b`. Their weights are exactly the two terms on the
right side of (15).

No two triples create the same unordered label pair. The longer label
identifies its physical interval `[a,c]` uniquely. The shorter label also
has unique physical endpoints and identifies the interior endpoint b,
whether it shares the left or right endpoint of `[a,c]`. A pair of different
physical intervals cannot share both endpoints. This proves the required
injection and the lower bound in (15), rather than merely counting triples
with uncontrolled multiplicity.

For unit weights this gives `2 binom(p,3)` distinct old expenditures and
hence (16). It does not assert these are all old expenditures.

## 5. The Section 6 barrier, with a small quantitative refinement

For `m=2^r p`, the cap gives

    L_r≤4Cm² log(4m),
    H≤Cp² log(2p)≤Cm² log(4m).

Inserting `L_r+H-m≤5Cm² log(4m)` into (10), with U=S=q, proves (18).
The stated restriction `m≤q/(10C log(4m))` indeed makes (18) at least
`q²/(20C log(4m))`, proving (19).

Let R be the last integer satisfying that restriction. With C fixed,

    R=log_2 p-log_2 log p+O_C(1),
    sum_(r=0)^R 1/(log(4p)+r log 2) →1.

The integral has the prefactor `1/log 2`; its logarithm tends to log 2,
so the limit is 1, not log 2. The integral-comparison error tends to zero.
The common upper budget divided by q² has upper bound tending to 1/2.
Consequently this relaxation compares two constants and does not force C
to become unbounded.

A slight strengthening is available without changing that conclusion.
Sum (18) itself over the same range, instead of replacing it by (19):

    sum_(r=0)^R Ψ(B_r)/q²
      ≥ (1/(10C)) sum_(r=0)^R 1/log(4m_r)
         -(1/(2q)) sum_(r=0)^R m_r.

The geometric sum is at most `2m_R`, and the defining restriction on m_R
makes the last term `O_C(1/log p)`. Thus

    liminf_(p→∞) sum_(r=0)^R Ψ(B_r)/q² ≥1/(10C).

Together with the crude common budget, this would only give the numerical
necessary condition `C≥1/5`. It remains a positive-constant conclusion and
does not close Q1. The source does not claim that all choices of weights,
or all retained expenditures in (14), have been ruled out.

## 6. Review of the additional moving-onset residue obstruction

After the initial source was saved, the author proposed the following
extension of `residue_route.md` Section 5.5; this review supports it.
Let S be the near-extremal finite Sidon set there, `M=|S|~sqrt N`, and
`n=floor(sqrt(N/log N))`. All of its increasing prefixes P_m with
`n≤m≤M` obey

    s_m≤N≤3m² log(2m)

for sufficiently large N. The last inequality follows uniformly by checking
m=n, where its right side is `(3/2+o(1))N`, and then using monotonicity.
This yields `(1/2)log_2 log N+O(1)` compatible dyadic shells, a number tending
to infinity.

For these prefixes the mixture fraction is `θ=m/M≥(1+o(1))/sqrt(log N)`.
The same L2 and entropy calculation gives, uniformly for
`q≤sqrt N/log N`,

    log q-H(P_m mod q)≤log(M/m)+O(1)
                        ≤(1/2)log log N+O(1).

At m=M one can use the distribution bound for S directly, avoiding a
conditional law of an empty complement. For the actual endpoint H_m=s_m,
positive difference injectivity gives

    H_m≥binom(m,2)+1≥N/(3log N)

for large N. Hence `log log H_m=log log N+o(1)` uniformly. Also
`sqrt(x)/log x` is increasing for x>e², so the admissible range
`q≤sqrt(H_m)/log(H_m)` is contained in the N-based range above.

This is a compatible finite history with growing depth, whose onset n moves
with N. It refutes certain finite-horizon versions of an inverse-residue
claim. It does not have one fixed onset across an infinite sequence and
therefore does not contradict Q1 or the unproved fixed-onset inverse claim.

## 7. Scope of the verdict

The reviewed identities and inequalities are proved finite statements with
physical difference labels retained. The evidence does not supply a uniform
contradiction for every critical cap C and every fixed onset. The additional
arithmetic restriction needed to obtain that contradiction is still open in
this work. This review changes no unresolved status and makes no claim of
formal verification.
