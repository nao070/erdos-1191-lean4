# Persistent forward shadows and an arithmetic inverse target

2026-09-05. Owner: `/root/global_route`; only this new file is edited.
The original Erdős #1191 Q1 remains unresolved. These are analytic proofs
and explicitly marked inverse targets, not a Lean proof or a counterexample
to Q1. No numerical experiment is used.

The input is one actual infinite positive integer Sidon sequence
`a_1<a_2<...`, with diagonal sums included in the Sidon condition. Put
`P_p={a_1,...,a_p}` and let ΔP_p be its distinct positive difference labels.
Whenever a critical cap is assumed, it is one pair of fixed constants

    a_p≤Cp² log(2p)  for every p≥p_0.                         (1)

The finite moving-onset counterexamples in the earlier notes are not
repeated here as purported counterexamples to (1).

## 1. An exact forward update with permanent certificates

Define the new forward shadow at stage p by

    S_p=a_p+ΔP_p,
    S_≤n=union_(p≤n) S_p.

It has `|S_p|=binom(p,2)`. More importantly,

    S_p∩A=empty                                               (2)

for the entire infinite sequence A, not merely its present prefix. Indeed
`x=a_p+(a_j-a_i)` with `i<j≤p` is greater than a_p. If x were a later point
of A, its difference with a_p would repeat the physical label `a_j-a_i`.
Thus every member of S_p is permanently excluded with identified old
endpoints, and `S_≤n` is a monotone growing set.

For every x>a_p there is also the exact update

    x∈P_p+P_p-P_p
      iff x∈(P_(p-1)+P_(p-1)-P_(p-1)) union S_p.             (3)

To check the new terms, a_p can be a positive summand or the subtracted
summand. If it is subtracted, two old positive summands give a value below
a_p. If it is a positive summand, the other positive summand must exceed
the subtracted point, giving `a_p+d` for an old positive difference d.
The case with two copies of a_p gives `d=a_p-a_i` and is included in S_p.

Consequently a candidate larger than the current prefix can be followed
through every stage using the *same first certificate*, rather than resetting
its exclusion history at each scale.

## 2. The exact forest attached to one physical candidate

Fix a positive integer x and let

    Y_x={x-a : a∈A, a<x}.

This is a finite positive integer Sidon set, by translation and reflection.
Occurrences `x∈S_p` correspond exactly to unordered Schur relations

    u+v=w,    u,v,w∈Y_x,    u≤v.                              (4)

Here the larger of the two original positive summands is a_p; thus the
maximal original rank is part of the witness. There is at most one witness
at any given stage p, since `x-a_p` has unique difference endpoints.

Construct a directed graph on Y_x by putting an edge from each distinct
input of (4) to its output w. A diagonal relation `2u=w` contributes one
graph edge, with a recorded diagonal mark.

**Forest theorem.** Every vertex has outdegree at most one and indegree at
most two. Every edge strictly increases its numerical value. The underlying
undirected graph is a forest.

Proof: a specified output has a unique unordered summand pair by Sidon.
If the same input u occurred in `u+v=w` and `u+v'=w'`, the equal positive
differences `w-v=w'-v'=u` force `(w,v)=(w',v')`. Thus its output edge is
unique. To exclude an undirected cycle, take its smallest numerical vertex.
Both incident cycle edges would point away from it, contradicting outdegree
at most one.

If there are n vertices, c components (including isolated vertices), T
relations, and D diagonal relations, the exact edge count gives

    2T-D=n-c.                                                (5)

In particular, the bound `T≤(n-1)/2` is valid only after excluding diagonal
relations and discarding isolated vertices appropriately. With diagonals,
`Y={1,2,4,...,2^(n-1)}` is Sidon and has n-1 Schur relations, all diagonal.

Nor are different witnesses vertex-disjoint. For the actual Sidon set

    A_0={6,10,16,17,19},

its ten positive differences are
`{1,2,3,4,6,7,9,10,11,13}`, while

    20=19+17-16=16+10-6.

The point 16 is used in opposite roles. The corresponding gap relations are
`1+3=4` and `4+10=14`. The forest, rather than a matching, is the correct
representation structure.

For an actual future point `x∈A`, (2) says that the entire past gap set Y_x
is sum-free: its forest has no edges. This is the exact survivor condition.

## 3. A cap-dependent bound on the lifetime of one certificate location

If `x∈S_p`, then

    a_p<x≤2a_p-a_1,     hence x/2<a_p<x.                     (6)

For all sufficiently large x, all such p exceed the fixed onset p_0. Since
positive increasing integers satisfy p≤a_p<x, (1) implies

    p>sqrt(x/(2C log(2x))).                                  (7)

On the other hand, unique positive differences give
`p(p-1)/2≤a_p-a_1<x`, so

    p≤sqrt(2x)+1.                                            (8)

Thus all stages at which this *same x* acquires further certificates belong
to a rank interval whose endpoint ratio is `O_C(sqrt(log x))`. The number
of rank-dyadic epochs intersecting that interval is at most

    (1/2)log_2 log x+O_C(1).                                 (9)

This uses the fixed cap on every relevant stage and the actual difference
injectivity. A certificate location is permanent once excluded, but its
possible new witnesses are confined to the physical band `a_p∈(x/2,x)`.
These are different notions of duration. In particular an argument that
charges a positive amount at x at every subsequent dyadic rank, merely
because the certificate remains valid, charges beyond the possible new
witnesses described by (9).

## 4. Strong forced reuse, with the first witness retained

For x∈S_≤n let `τ(x)=min{p:x∈S_p}`. This definition is fixed once and for
all along the infinite history. Let

    r_n(x)=|{p≤n:x∈S_p}|,
    M_n=sum_x r_n(x)=sum_(p≤n) binom(p,2)=binom(n+1,3).        (10)

All these physical locations lie below `2a_n`. Under (1),

    |S_≤n|≤2Cn² log(2n),
    M_n=(n³-n)/6.                                           (11)

There are exactly `M_n-|S_≤n|` occurrences after a location's first witness.
Thus their proportion is at least

    1-(12C+o(1)) log(2n)/n.                                 (12)

This is a diverging-multiplicity structural requirement: almost all new
shadow occurrences must reuse already excluded physical locations. It is
not a proof that their forests have a large connected component.

One can retain the age of the *same first certificate* quantitatively.
For every positive integer L, the number of occurrences `(p,x)` with
`p-τ(x)<L` is at most `L|S_≤n|`: at most L distinct stages are possible for
each x. For sufficiently large n choose

    L_n=floor(n/(32C log(2n))).

Then the number of these young occurrences is at most n³/16, whereas
`M_n≥n³/8`. Hence at least half of all occurrences through stage n have

    p-τ(x)≥L_n.                                             (13)

The labels in their first witness were born at least `~n/(32C log n)` ranks
earlier. This is an actual history statement, with τ not reassigned at later
cutoffs. It concerns age measured in individual ranks; it must not be
upgraded to a comparable number of rank-dyadic epochs.

An equivalent information statement is also exact. Choose an occurrence
`(p,d)`, where `p≤n` and `d∈ΔP_p`, uniformly from the M_n possibilities,
and set X=a_p+d. Given (p,X), the label d is determined. Therefore

    H(p|X)=H(p,d|X)=log M_n-H(X)
          ≥log M_n-log(2a_n)
          ≥log n-log log(2n)-log(12C)+o(1).                 (14)

This large conditional entropy records substantial reuse of candidate
locations. It does **not** imply that the residues of A have small entropy:
the random variable is a forward-shadow occurrence, not a uniform element
of A. No data-processing or inverse-sieve implication between those two
different distributions has been proved.

The elementary counting estimates (11)--(14) also hold for a single finite
Sidon prefix with the same endpoint bound. Their simultaneous use with one
τ and the lifetime restriction (9) retains additional bookkeeping, but a
contradiction from that bookkeeping is still missing. They are not presented
as an inverse theorem already distinguishing fixed from moving onset.

## 5. Packing efficiency: a concrete necessary condition from the parent

The parent proposed the following formulation; its finite proof is checked
here. Let α(P) be the supremal upper density of a set T⊂Z avoiding all
distances in ΔP. Equivalently the translates `P+t`, t∈T, are disjoint.
Consequently

    α(P)≤1/|P|.                                             (15)

Take an actual future block `B={a_(p+1),...,a_(2p)}`. Let
`H=diam P_p`, `D=diam B`, and set `Q=D+H+1`. Then

    T=B+QZ

avoids ΔP_p. Distances within one copy are legal by Sidon. Between copies
they are at least `Q-D=H+1`. This periodic packing has density p/Q, so (1)
gives, for all sufficiently large p,

    α(P_p)≥p/[5Cp² log(4p)+1].                              (16)

In terms of the coverage efficiency `e_p=pα(P_p)`, the whole history must
satisfy

    1/[5C log(4p)+p^(-2)]≤e_p≤1.                            (17)

This is much weaker than near-tiling. A near-equality inverse theorem whose
hypothesis is `e_p=1-o(1)` cannot be applied at the lower bound (17).

One quantitatively sufficient inverse target is a *net* decrease along
dyadic prefixes that forces `e_(2^k)=o(1/k)` under (1). For example, an
eventual inequality

    e_(2^(k+1))≤e_(2^k) exp(-(1+η)/(k+1)),    η>0,           (18)

would suffice: its product is `O(k^(-1-η))`, contradicting (17). Equation
(18) is an **unproved candidate**, not a theorem. Efficiency itself need
not decrease: α(P_p) is decreasing as the forbidden bank grows, but the
normalizing factor p increases. Negative net losses cannot be discarded.

## 6. A true infinite counterexample to a span-free inverse claim

The cap in (18) would have to do real work. Infinitude, complete compatibility,
and permanent avoidance by themselves permit `e_(2^k)=1` at every k.

Construct an infinite positive Sidon sequence as follows. Start with a_1=1.
Suppose its first p=2^k points are a complete residue system modulo p. They
occupy exactly one of the two lifts of each such residue modulo 2p. Fill the
p missing residues modulo 2p, once each, by selecting new integers in those
classes successively, always larger than twice the present maximum.

Each extension preserves Sidon: all its new sums exceed all old sums, the
new sums with different old points differ, and its new diagonal sum exceeds
those. At the end of the stage the first 2p points are a complete residue
system modulo 2p. Thus the construction continues indefinitely.

For every dyadic p the translates

    P_p+pZ

partition Z. Hence `α(P_p)=1/p` and `e_p=1` exactly. Every actual later point
still avoids the past forward shadows by (2); no finite-prefix replacement
has been made in this example.

However `a_n>2a_(n-1)` throughout, so it violates (1) for every fixed C.
This refutes any proposed deduction of (18) from compatible history and
Sidon alone, and identifies the necessary modification: the inverse estimate
must retain a quantitative bound on the physical height at every stage.
The example is not a counterexample to the cap-dependent candidate or Q1.

## 7. Literature scope and the remaining arithmetic connection

A narrow primary-source check found two related but inapplicable shortcuts:

- Natalchenko--Sagdeev, [*Packing density of sets with only two non-mixed
  gaps*](https://arxiv.org/html/2407.01101v1), describes the equivalence
  between packing translates and avoiding a difference set. Its explicit
  density formulas concern special two-gap sets, not arbitrary Sidon prefix
  banks. The packing proof needed here is provided in Section 5.
- Thornburgh, [*Uniform exclude distributions of Sidon
  sets*](https://arxiv.org/html/2407.11783v1), studies characteristic-two
  groups and APN graphs. This does not supply an inverse theorem for ordered
  positive integer prefixes. Opposite signs and the order-oriented forest
  in Section 2 cannot be discarded by importing that setting's conventions.

The new proved structure is the permanent forward update, its exact Schur
forest, the cap-dependent witness lifetime, and the quantitative reuse/age
constraints. A possible next connection is to combine these forests across
different physical locations x and successive value bands to force a
height-sensitive loss in (17), or the residue entropy deficit from
`residue_route.md`. At present no bound makes either loss follow. In
particular high shadow multiplicity alone gives (14), not the needed
entropy statement about A.

The root has independently confirmed the forest argument and its diagonal
caveat. The sibling's growing-label budget work separately retains six-point
relations and birth/death charges. Neither review closes the missing
height-sensitive inverse implication. Q1 remains unresolved and no Lean
completion is claimed.
