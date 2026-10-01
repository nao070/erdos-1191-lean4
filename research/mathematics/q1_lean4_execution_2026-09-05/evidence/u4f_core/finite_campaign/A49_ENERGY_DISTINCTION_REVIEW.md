# A49: difference third energy is not triple-sum second energy

Date: 2026-09-09. Independent bounded hand-proof review: PASS.
No external theorem search, finite campaign, profile scan, or Lean run.

## Definitions and exact difference-energy count

Let A be a finite set of n integers satisfying the usual Sidon condition,
including repeated-element two-sums. Define ordered representation counts

    r_minus(x)=#{(a,b) in A^2 : a-b=x},
    r_triple(s)=#{(a,b,c) in A^3 : a+b+c=s}.

Repetitions among coordinates of a triple are allowed. The two quantities
under review are, explicitly,

    E3=sum_x r_minus(x)^3,
    T3=sum_s r_triple(s)^2.

Here E3 counts triples of ordered pairs with a common difference; T3
counts ordered pairs of triples with a common sum. The review is of these
displayed definitions. The root researcher separately checked the E_k
notation in equation (5) of https://arxiv.org/pdf/2103.14670. This note
does not claim an independent PDF or hypothesis review of that paper.

One has r_minus(0)=n. Sidon positive-difference uniqueness gives exactly
n(n-1) nonzero signed difference labels, each of multiplicity one;
negative labels correspond to reversed pairs and are counted as distinct
labels. All other representation counts vanish. Therefore, exactly,

    E3=n^3+n(n-1)=n^3+n^2-n.

This step is unaffected by translation or by whether A contains zero.

## Triple-sum contribution of identical multisets

For each unordered three-element multiset of A, all permutations have
the same sum. Counting only pairs of ordered triples that are permutations
of this same multiset gives disjoint contributions:

| multiset type | number of multisets | permutations per multiset | contribution |
|---|---:|---:|---:|
| three distinct entries | binom(n,3) | 6 | 36 binom(n,3) |
| one entry twice and another once | n(n-1) | 3 | 9n(n-1) |
| one entry three times | n | 1 | n |

Different multisets may also have the same sum. Those add nonnegative
cross-contributions to T3 and do not invalidate this lower bound. Thus

    T3 >= 36 binom(n,3)+9n(n-1)+n
       = 6n^3-9n^2+4n.

The lower bound is not asserted to be an exact formula for every Sidon
set. Subtracting the exact E3 identity gives

    T3-E3 >= (6n^3-9n^2+4n)-(n^3+n^2-n)
           =5n^3-10n^2+5n
           =5n(n-1)^2.

For every n>=2 this is strictly positive, so E3 and T3 cannot be
identified. At n=0 or n=1 the difference is zero, and these degenerate
cases are excluded from the strict conclusion. All coefficients follow
from ordered-pair counting; there is no factor-of-six normalization
hidden in either definition.

## No absolute constant comparison T3<=K E3 for all finite integer Sidon sets

Use the actual Sidon construction already present in
`research/causal_fourier_rank_commutator.md`, section 5, equation (13).
That construction and its proof were independently read back for this
addition; no new history or finite experiment is generated. For each odd
prime p, let r_i be the least nonnegative residue of i^2 modulo p and set

    a_(i+1)=1+2pi+r_i,  0<=i<p.

The points are strictly increasing because consecutive increments are
at least 2p-(p-1)>0. For completeness, equality of two positive
differences first gives the same index gap d: the difference between
the two residue corrections has absolute value strictly less than 2p.
The equality then reduces modulo p to
d(2i+d)=d(2j+d). Here 0<d<p and p is odd, so i=j modulo p and hence
as indices in {0,...,p-1}. Thus the positive differences are unique,
including the repeated-two-sum consequence required for the E3 formula.

For this p-point actual Sidon set,

    H_p=2p(p-1)+1,
    3H_p+1=6p^2-6p+4<6p^2.

The ordered triple representation function has total mass p^3 and support
within an interval of at most 3H_p+1 integer positions. Finite Cauchy gives

    T3 >= p^6/(3H_p+1) > p^4/6.

The exact difference-energy formula gives
E3=p^3+p(p-1)<=2p^3. Consequently

    T3/E3 > p/12.

There are arbitrarily large odd primes, so no absolute constant K makes
T3<=K E3 true for every finite integer Sidon set. This is stronger than
the preceding strict inequality T3>E3: it rejects any fixed constant
substitution of these two energies in a bare-Sidon argument. The proof
uses actual endpoints and an actual Sidon family, not a scalar model.

The quantifier boundary is essential. This family has H2=2p+1. More
generally, for any fixed rank s>=2 present in the family,
H_s>=2p(s-1). Taking s=max(2,m0), these values eventually exceed any
fixed C s^2 log(2s). Thus this family does not preserve one fixed C,m0
all-prefix cap as p grows. Its terminal width O(p^2) does not repair
the intermediate-rank failure. The result is not a counterexample to
the frozen U4-F estimate, Q1, or a theorem restricted to that entire cap
contract. No profile or genuine-price conclusion is deduced from these
unpriced energies.

## Fixed cap does not establish the near-extremal Fourier error

The separate proposed Fourier input contains the term

    abs(|S|/sqrt(N)-1)

for an integer Sidon set S contained in [N]. Treating this as o(1)
requires near-extremal density |S|/sqrt(N)->1 (equivalently
N/|S|^2->1). That conclusion has not been established from the original
fixed-cap hypothesis H_n<=C n^2 log(2n).

Even taking the smallest natural ambient interval after translation,
N=H_n+1 and |S|=n, the cap yields only

    N/n^2 <= C log(2n)+1/n^2,
    n/sqrt(N) >= 1/sqrt(C log(2n)+1/n^2).

These estimates do not provide convergence to 1. Choosing a larger
ambient N would require separate control of that choice as well. This
review does not substitute a scalar diameter model for an actual Sidon
set, assert a counterexample family of arbitrarily long capped prefixes,
or prove formal logical independence from the complete unresolved
Sidon/cap contract. It records the exact missing density inference in
the proposed application. The paper's Fourier estimate or any other
external theorem is not otherwise evaluated here.

## Logical role, evidence scope, and next action

This is a noncircular finite counting obstruction to an energy
identification, an actual finite-family counterexample to any absolute
constant bare-Sidon energy comparison, and a limitation on an unproved
Fourier specialization.
It does not bound the remaining original core norm and does not refute
U4-F or Q1. The next mathematical action is to keep E3 and T3 distinct
and retain the actual density error unless an independently justified
estimate controls it in the required original geometry. No new theorem
should be imported under an o(1) assumption not established for that
geometry.

This bounded review is complete. No process, finite search, or build is
running or queued. The note, reused cap-contract source, and actual
Sidon-family source section are bound by content hash in
`A49_review_manifest.json`; no external PDF content hash is claimed by
this independent reviewer.
