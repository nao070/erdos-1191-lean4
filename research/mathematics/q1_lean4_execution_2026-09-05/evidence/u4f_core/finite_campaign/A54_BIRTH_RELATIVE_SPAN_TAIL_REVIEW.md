# A54: a uniformly paid diameter tail relative to source birth

Date: 2026-09-09. Independent hand-proof review: PASS.

Fix q>1 and an original strict record of birth c>=4. Select components
whose actual width obeys H_k>=H_c(log c)^q. Its selected contribution is

    de sum_{k=r}^{M} 1[H_k>=H_c(log c)^q] kappa_k/H_k^2.

If no such component exists the contribution is zero. There is no
assumption that a threshold rank exists or that the history extends.
For every selected component its denominator is at least
H_c^2(log c)^(2q). Original causal endpoints give r>=c+2. Therefore

    selected price <= de*alpha_(c+2)/[H_c^2(log c)^(2q)]
                   <= de/[c^4 H_c^2(log c)^(2q)].

The first step bounds an actual finite kappa sum by
alpha_(c+2)-alpha_(M+1)<=alpha_(c+2). It does not reset the terminal
term or change either horizon. Components k>T remain selected by their
actual widths and original prices.

Using A53's independent actual Sidon bound
sum_{birth c}de<=DeltaF_c<=c^3H_c^2/4 gives birth price mass at most
1/[4c(log c)^(2q)]. For a dyadic birth block c in[2^ell,2^(ell+1)),
ell>=2, the once-per-physical-record price mass satisfies

    E_ell<=1/[4(ell log2)^(2q)].

The same original strict support as A53 is
2^ell<b<2^(ell+1)(ell+1)log2. Its integer harmonic sum is at most
log(2(ell+1)log2). Thus

    N_selected <= 1/[2(log2)^q]
       *sum_{ell=2}^infinity log(2(ell+1)log2)/ell^q < infinity.

Convergence requires q>1. All records are priced once and retain their
original cut intervals. The numerical infinite series bounds finite
M,T histories uniformly. No cap is used for this subclass theorem.

## Stronger remaining geometry and removal of late activation

Fix q=2. Since c<b implies
H_c(log c)^2 < H_b(log b)^2, this birth-span paid class contains the
previous A33 cut-span paid class. A remaining component satisfies

    H_k<H_c(log c)^2,

which automatically implies the cut-near condition of A46.6 for every
covered cut. Likewise A53's remaining k<L(c), with p=5/8, implies
k<L(b) for every covered b. Hence neither of A52's common increasing
conditions causes a post-birth activation in the new remainder.

At a fixed component, filter the actual source-pair bank by these two
static birth predicates before assigning its auxiliary weight de.
The birth c and H_c are determined by the source pair itself, so these
predicates do not change as the cut moves. On b>=max(4,m0), all other
displayed threshold predicates move only toward retirement, as proved
in A52. Every selected record therefore enters only at its source birth
(if eligible then) and may later retire. Actual source-pair injection
shows that a newly selected price is covered by the new filtered bank
weight. Consequently this filtered raw bank minus selected Q is
nonnegative and nondecreasing, without rebasing at a later common a_k.

This component statement may be summed with fixed genuine lambda_k.
It does not assert monotonicity of a cut-normalized ratio, does not give
unused labels genuine output prices, and does not move any remaining
component-dependent indicator outside its k sum. The initial cut/source
exceptions remain separately paid under the existing contract. Passing
the displayed necessary conditions is not a claim that every historically
paid subclass is characterized by those conditions alone.

## The one saved restart witness

Only the same A53 bank-index1487 witness is checked against this new
condition. Its source birth c24 has H_c=713, while H48=4248. Independent
rational log enclosures verify 4248<713(log24)^2. Thus that one record
at cut25/component48 remains after A54 as well as A53/A46. No further
record, cut, source or bin is searched. This establishes finite
nonemptiness only, not a profile lower bound across scales.

A54 supplies a new uniform subclass norm and a useful potential with
no post-birth activation for the displayed remainder. The total remaining
norm, CoreUniform, Q1 and final Lean closure are still unproved. These
are independently reviewed hand arguments; source hashes and the
single-witness flag are in `A51_A54_review_manifest.json`.
