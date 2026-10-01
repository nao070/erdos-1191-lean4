# Congruence and entropy route: exact bounds, a zero criterion, and its scope

Date: 2026-09-05. Owner: `/root/global_route`. Independent mathematical work;
other agents' files have not been edited. Model settings have not been changed.

**Status: Q1 remains unresolved.** This note proves a quantitative sufficient
condition for the zero conclusion, using actual uniqueness of every positive
difference. It also proves that this condition cannot be forced from a single
finite prefix's Sidon property and critical cardinality alone. The missing step
is a consequence of the *fixed-onset, all-prefix* cap and compatible history.
There is no Lean verification claim for the new statements in this file.

All logarithms are natural. A finite Sidon set here allows diagonal sums and is
equivalently a set for which each nonzero ordered difference has at most one
representation. Write `[N]={1,...,N}`.

## 1. Primary theorem checked, including its additional hypotheses

Croot, Mao, Pohoata, Sheffer and Yip, *A combinatorial large sieve for Sidon
sets, distances, and norm forms*, arXiv:2606.17487v2, 24 June 2026,
[Theorem 1.1 and Section 2.1](https://arxiv.org/html/2606.17487v2#S1.SS1):
if a finite Sidon set `B ⊂ [N]` has `|B mod p| ≤ αp` for every prime, where
`0<α<1`, then for `0<δ<1/4`,

    |B| ≪_(α,δ) sqrt(N)
          exp(-(1/4-δ) log(1/α) log(N)/log log(N)).

The constant depends on α and δ. Thus substituting an N-dependent α directly
into the displayed asymptotic theorem is not justified. Its proof uses a
product of small primes and difference injectivity. The missing-residue
hypothesis is additional; the theorem does not assert it for arbitrary Sidon
sets. It concerns each finite B. Applying it to infinite A requires proving
the hypothesis for relevant prefixes, or a stronger hypothesis on A itself.

The exact calculations below eliminate unspecified α-dependent constants and
restrict the necessary primes to a chosen finite set. The Shannon extension,
varying-deficit threshold, and finite counterexamples are derived here.

## 2. One modulus: no repeated charge to a difference

Let `B ⊂ [N]` be nonempty and Sidon, `n=|B|`, `q≥1`, and

    ν_q = |B mod q|,
    n_r = |{b in B : b ≡ r mod q}|.

The exact number of ordered distinct same-residue pairs is

    sum_r n_r(n_r-1).

Every such positive difference is a different member of
`{q,2q,...,floor((N-1)/q)q}`. Consequently

    n²/ν_q - n ≤ sum_r n_r² - n ≤ 2 floor((N-1)/q).            (2.1)

The first inequality is Cauchy--Schwarz on the occupied classes. Solving the
quadratic, and then using `sqrt(u+v)≤sqrt(u)+sqrt(v)`, gives

    n ≤ [ν_q + sqrt(ν_q² + 8ν_q floor((N-1)/q))]/2
      ≤ ν_q + sqrt(2ν_q N/q).                                 (2.2)

No condition such as `n≥2ν_q` is required. This matters when the modulus is
large. Dropping the first term of (2.2) without controlling it is invalid.

For any finite collection of moduli with nonnegative weights `w_q`, the exact
same-residue count can instead be summed using

    W(d) = sum_q w_q 1[q divides d].

Difference uniqueness gives

    sum_(b>b', b,b' in B) W(b-b') ≤ sum_(d=1)^(N-1) W(d).       (2.3)

Thus a difference divisible by several chosen moduli has the same weight on
both sides. There is no uncharged CRT multiplicity. The useful gain below is
the loss of occupied CRT classes, rather than counting one difference once
for each prime while retaining a one-copy upper bound.

## 3. CRT and a quantitative sufficient condition for zero

For distinct primes in a finite set `P`, put

    q = product_(p in P) p,
    ρ_p = |B mod p|/p,
    Γ_0(P) = sum_(p in P) -log(ρ_p).

CRT injects `B mod q` into the product of its marginal residue supports, so
`ν_q ≤ q exp(-Γ_0)`. Inserting this into (2.2),

    n ≤ q exp(-Γ_0) + sqrt(2N exp(-Γ_0)).                      (3.1)

In particular, if `q≤sqrt(N)/log N`,

    n sqrt(log N/N)
      ≤ 1/sqrt(log N) + sqrt(2 exp(log log N - Γ_0)).          (3.2)

This is an exact inequality for `N>1` and any chosen P satisfying the modulus
condition. Therefore the following conditional implication is proved:

> If an infinite Sidon A admits arbitrarily large N and prime sets P_N with
> product at most `sqrt(N)/log N` and
> `Γ_0(A∩[N],P_N)-log log N → +∞`, then
> `liminf_(N→∞) |A∩[N]| sqrt(log N/N)=0`.

Only the selected primes for that finite prefix occur in the hypothesis.
The prime sets may vary with N. The statement does not require infinite A
itself to omit a residue at any fixed prime.

### 3.1 An explicit vanishing omission fraction

Let `L=log N`, `l=log L`, and, for sufficiently large N, choose

    t_N = floor((L-2l)/(2 log(2L)))

distinct primes from `[L,2L]`. Such a selection is possible for all sufficiently
large N: the prime number theorem gives `(1+o(1))L/log L` primes in this
interval, whereas `t_N=(1/2+o(1))L/log L`. By construction

    q ≤ (2L)^t_N ≤ sqrt(N)/log N.

Suppose that, for each selected prime,

    |(A∩[N]) mod p|/p ≤ 1-ε_N,
    ε_N ≥ (2+η)(log log N)²/log N,

where η is any fixed positive number. Then

    Γ_0 ≥ t_N [-log(1-ε_N)] ≥ t_N ε_N
        ≥ (1+η/2+o(1)) log log N.

Equation (3.2) proves

    |A∩[N]| sqrt(log N/N)
      ≤ (log N)^(-1/2) + (log N)^(-η/4+o(1)).                 (3.3)

In particular the right side tends to zero. The first term in (3.3) must be
retained when η is large; an unconditional bound solely by the second term
was not established. This proves the proposed quantitative improvement
under its explicit local omission condition, with no α-dependent constants.

Uniform ε_N at every selected prime is more than necessary: their logarithmic
deficits only need to have sum exceeding `log log N` by a quantity tending
to infinity. A product over all primes is not required.

### 3.2 A condition expressed using the infinite profinite support

If `δ_A(q)=|A mod q|/q`, (2.2), applied at `N=q²`, shows

    |A∩[q²]| sqrt(log(q²)/q²)
      ≤ [δ_A(q)+sqrt(2δ_A(q))] sqrt(2 log q).

Hence `δ_A(q_j) log q_j →0` along some unbounded moduli is another sufficient
condition for Q1's zero conclusion. This is not a property of all infinite
Sidon sets: Section 7 constructs one whose support modulo every q is full.

## 4. Shannon deficit works even when every class is occupied

Let X be uniform on the finite set B. Write H for Shannon entropy, and define

    Γ_H(P) = sum_(p in P) [log p - H(X mod p)].

All summands are nonnegative. Also `Γ_H≥Γ_0`, since entropy is at most the
logarithm of support size. CRT and entropy subadditivity imply

    H(X mod q) ≤ sum_(p in P) H(X mod p) = log q - Γ_H.

For any probability vector π, Jensen's inequality for log gives

    log(sum_r π_r²) ≥ sum_r π_r log π_r = -H(π).

Apply this to `π_r=n_r/n`. Combining it with the same pointwise difference
budget used in (2.1),

    n² exp(Γ_H)/q - n ≤ 2 floor((N-1)/q).

Consequently

    n ≤ q exp(-Γ_H) + sqrt(2N exp(-Γ_H)).                      (4.1)

Thus every assertion in Section 3 remains valid with Γ_H in place of Γ_0.
This includes distributions having full support but uneven class masses.
No false subadditivity assertion about collision/Rényi-2 entropy is used:
the proof passes through Shannon entropy and then Jensen.

### 4.1 A necessary residue constraint on any hypothetical critical set

Suppose a particular prefix has

    n sqrt(log N/N) ≥ c > 0.

For sufficiently large N, any prime set with `q≤sqrt(N)/log N` satisfies,
by (4.1),

    c/2 ≤ sqrt(2 exp(log log N - Γ_H)),
    Γ_H ≤ log log N + log(8/c²).                              (4.2)

A uniform positive critical lower bound therefore forces a uniform upper
budget for marginal entropy deficits over every admissible prime product.
To obtain a contradiction one must force a larger deficit from some further
feature of the all-prefix history. The inequalities so far prove the upper
budget; they do not prove that it is exceeded.

## 5. A genuine finite Sidon counterexample to automatic marginal deficit

The following is an existence proof, not a numerical experiment. It preserves
the pointwise Sidon condition. It proves that neither Γ_0 nor Γ_H can be
forced large from a *single prefix* having critical cardinality.

### 5.1 A near-extremal finite Sidon starting set

Take arbitrarily large prime powers Q, let `N=Q²-1`, and choose a primitive
element θ of the field with Q² elements. For each t in the subfield with Q
elements, let d_t in `{0,...,N-1}` be determined by

    θ^(d_t) = θ+t.

There are Q different such d_t. If two pair sums of their exponents agree
modulo N, multiplication and comparison of the coefficients of `1,θ` give

    t_1+t_2=t_3+t_4,     t_1 t_2=t_3 t_4.

The two unordered pairs are therefore equal, as the roots with multiplicity
of the same monic quadratic. Thus

    S={d_t+1 : t in F_Q} ⊂ [N],    |S|=Q,

is a Sidon set, including for diagonal sums. This is the usual finite-field
Bose--Chowla construction, with its needed Sidon verification given above.

### 5.2 A verified primary distribution estimate

Kolountzakis, *On the uniform distribution in residue classes of dense sets
of integers with distinct sums*,
[arXiv:math/9808061, Theorem 2](https://arxiv.org/pdf/math/9808061), gives, in
the case `|S|≥sqrt N` and `m=o(sqrt N)`,

    [sum_(r mod m) (|S_r|-|S|/m)²]^(1/2)
        ≤ C N^(3/8) m^(-1/4).                                (5.1)

Here C is absolute. This is the first branch of the stated theorem; it also
allows negative `sqrt N-|S|`. For our S, this branch applies since `|S|=Q`.
In particular every residue modulo every `m≤2log N` is occupied for large N:
the error in each class divided by `|S|/m` is at most
`O(N^(-1/8)m^(3/4))=o(1)` uniformly in that range.

**Norm/range audit requested by the parent:** the original PDF's printed
page 2, Theorem 2, equation (4), bounds the norm with subscript 2, not merely
one residue's error. The norm is explicitly defined on that same page as
`||f||_p=(sum_(x in Z_m)|f(x)|^p)^(1/p)`. The page also specifies that C is
an absolute constant. Thus squaring (5.1) bounds the *sum* over residues;
no extra factor m is to be inserted. One can take the theorem's deficit
parameter `ℓ=0`, since `Q≥sqrt(Q²-1)`. Its modulus assumption is
`m=o(sqrt N)`. The proof, printed pages 4--5, uses the small quantity
`m^(1/2)N^(-1/4)` and absolute constants. Over
`m≤sqrt N/log N` this quantity is at most `1/sqrt(log N)`, so all requisite
smallness estimates hold with one sufficiently large N threshold uniformly
over the range. Equation (5.6) uses precisely this L2 version and range.

### 5.3 Deterministic full-support thinning

Choose from S one representative of every residue of every integer modulus
`2≤m≤floor(2log N)`. The union R of all representatives has

    |R| ≤ sum_(m≤2log N) m = O((log N)²).

For large N this is less than `n=floor(sqrt(N/log N))`. Extend R inside S to
a set B of exactly n elements. Then B is Sidon, its normalized cardinality
`n sqrt(log N/N)` tends to 1, and

    |B mod m|=m          for every m≤2log N.

Thus all the Γ_0 statistics in the prime annulus of Section 3.1 are exactly
zero. This alone refutes a universal finite-density-to-omission implication.

### 5.4 Entropy deficits can simultaneously tend to zero

A stronger thinning argument handles Γ_H. Let M=|S|, and choose an n-element
subset B uniformly among all such subsets of S. For each modulus m let
u_r=|S_r|/M and define the chi-square discrepancy from the uniform distribution

    χ_m(S)=m sum_r (u_r-1/m)².

For B use its empirical probabilities `|B_r|/n`. Hypergeometric variance gives
the exact expectation

    E χ_m(B) = a(m-1)+(1-a)χ_m(S),
    a=(M-n)/(n(M-1)).                                        (5.2)

Indeed the individual variance is
`n u_r(1-u_r)(M-n)/(M-1)`; summing it proves (5.2). In particular

    E χ_m(B) ≤ m/n + χ_m(S).

Squaring (5.1) and multiplying by `m/M²` yields

    χ_m(S) ≪ N^(-1/4) sqrt m.

For `R_N=floor(2log N)` we therefore have

    E sum_(m=2)^R_N χ_m(B)
      ≤ C₀ [R_N²/n + N^(-1/4) R_N^(3/2)]
      =: E_N = o(1/log N),                                  (5.3)

where C₀ is a sufficiently large absolute constant, fixed independently
of N. This fixes the constant in E_N before using the averaging argument.

There is an actual n-element subset B for which this nonnegative sum is at
most E_N. For any probability π on m points its relative entropy to uniform
obeys

    log m-H(π)=sum_r π_r log(mπ_r)
      ≤ log(m sum_r π_r²)=log(1+χ(π))≤χ(π),                  (5.4)

again by Jensen. Therefore this B satisfies

    sum_(p≤2log N) [log p-H(B mod p)] ≤ E_N=o(1).              (5.5)

It even has full support for every `m≤R_N`: missing a class would force its
entropy deficit to be at least `log(m/(m-1))≥1/m≥1/R_N`, contrary to (5.3)
and (5.4) for large N. Here `H(B mod p)` means the entropy of the residue of
a uniform element of B, as before.

This establishes exact finite Sidon counterexamples to the candidate claim
that critical cardinality alone forces
`Γ_H≥log log N+ω(1)`, or even any fixed positive marginal deficit in the
indicated prime range.

**Scope:** these B depend on N. Their intermediate sorted prefixes were not
shown to obey `a_j≤Cj²log(2j)` from one fixed onset, and they do not form one
nested infinite set. Accordingly this does not refute Q1 or an inverse
statement using mutually compatible extensions across the entire tower.

### 5.5 Even an adaptively selected large modulus has insufficient deficit

The obstruction extends beyond the small-prime marginal statistics. Keep the
same S, and let B be **any** subset of size `n=floor(sqrt(N/log N))`. Put
`θ=n/M=(1+o(1))/sqrt(log N)`. For every

    1≤q≤sqrt(N)/log N,

the quantitative estimate (5.1) remains applicable, since this entire range
is `o(sqrt N)`. It gives, uniformly in q,

    χ_q(S) ≪ N^(-1/4) sqrt q ≪ 1/sqrt(log N) ≪ θ.             (5.6)

Let U be uniform on S, let E indicate membership in B, and let Y=U mod q.
Write u for the law of Y, π for its law conditioned on E=1, and v for the
uniform law on q classes. Entropy chain rules give

    θ D(π||v)+(1-θ)D(Law(Y|E=0)||v)
       = D(u||v)+I(Y;E) ≤ D(u||v)+h(θ),

where `h(θ)=-θ logθ-(1-θ)log(1-θ)`. Thus (5.4) and (5.6) imply

    Γ_joint(B,q) := log q-H(B mod q)
       ≤ χ_q(S)/θ+h(θ)/θ
       ≤ (1/2)log log N+O(1).                                (5.7)

The constant is uniform in B and q in the specified range. In particular
it permits choosing q after inspecting B. For a squarefree q with prime
set P, entropy subadditivity gives `Γ_H(B,P)≤Γ_joint(B,q)`. Even this stronger
joint statistic stays a factor of two below the sufficient logarithmic
threshold for these genuine finite Sidon sets.

This is not an artifact of replacing collision entropy by Shannon entropy.
For π and u as above we have `π_r≤u_r/θ`. Let

    R_q(B)=q sum_r π_r².

Then, writing `χ=χ_q(S)`, Cauchy--Schwarz and Young's inequality yield

    θR_q(B) ≤ q sum_r π_r u_r
             ≤ 1+sqrt(R_q(B)χ)
             ≤ 1+(θ/2)R_q(B)+χ/(2θ).

Consequently, simultaneously for every allowed q,

    R_q(B) ≤ 2/θ+χ_q(S)/θ² ≪ sqrt(log N),
    log R_q(B) ≤ (1/2)log log N+O(1).                         (5.8)

Thus the actual collision counts in all these moduli also retain a
`sqrt(log N)` factor of slack relative to the `log N` factor needed to
contradict critical cardinality. This is a strengthened *finite-prefix*
counterexample; it still has no fixed-onset nested cap assertion.

## 6. Why the finite counterexample leaves a precise new target

A sufficient all-history lemma would be the following (currently unproved):

> Under a fixed-onset bound `a_j≤Cj²log(2j)` for an infinite Sidon sequence,
> there are arbitrarily large N and selected prime products
> `q_N≤sqrt(N)/log N` for which the marginal entropy deficit of `A∩[N]`
> exceeds `log log N` by a quantity tending to infinity.

Equation (4.1) would immediately close the contradiction. A support deficit
at the explicit rate in Section 3.1 is a stronger sufficient alternative.
Section 5 shows that a proof of this lemma must use the compatible history
assumption materially; a one-prefix inverse statement is false. No proof of
this additional all-history lemma has been obtained in this note.

## 7. Infinite Sidon sets need not have any omitted profinite class

For completeness, even omission somewhere in the infinite support does not
follow merely from infinitude and Sidon. Construct an increasing sequence
recursively, with

    a_j > 2 a_(j-1),
    a_j ≡ j mod lcm(1,2,...,j).

At every step there are arbitrarily large integers in the required class.
The new sums `a_j+a_i` exceed every old sum and are pairwise different; the
new diagonal sum `2a_j` exceeds them. Thus this is an infinite Sidon sequence.
For every fixed q and every j≥q we have `a_j≡j mod q`. Its first n terms
therefore have `n/q+O(q)` representatives in each residue, and the infinite
set has full support modulo every q.

The construction grows at least exponentially and violates the critical cap.
It verifies only the exact boundary of a purported unconditional residue
omission lemma. It is consistent with Q1.

## 8. Verification and handoff record

- Primary statements read directly: arXiv:2606.17487v2, Theorem 1.1 and
  Section 2.1; arXiv:math/9808061, Theorem 2 and its quantitative first branch.
- Equations (2.1)--(4.2), the finite-field Sidon argument, and the thinning
  expectation (5.2) were derived algebraically here. No solver status or
  finite numerical experiment is substituted for their proofs.
- No new numerical script was executed for this note; hence there is no
  numerical execution claim or unsaved execution cell.
- New conditional zero criteria and actual finite Sidon counterexamples are
  distinct from the still-unproved all-history implication in Section 6.
- No implication from an α-dependent asymptotic constant to varying α is
  used. The varying-α bound is supplied by the explicit finite inequalities.
- Q1 remains unresolved; this file is not a proof/refutation of Q1 and is
  not a Lean certification of the original statement.
