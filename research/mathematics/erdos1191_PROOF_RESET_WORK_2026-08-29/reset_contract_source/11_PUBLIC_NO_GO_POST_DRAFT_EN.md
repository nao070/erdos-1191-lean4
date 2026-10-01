# Draft for external mathematical review — do not post before independent audit

## A harmonic obstruction to a proposed multiscale route for Erdős Problem #1191

We have been studying a dyadic Abel/cut-renewal approach to Question 1 of Erdős Problem #1191. The problem remains open; this note reports a method correction and several conditional/no-go statements, not a solution.

Let `0=a_0<a_1<...` be an integer Golomb ruler and let `m` be dyadic. In the cut-renewal decomposition, the new-birth sector is

`Z_m^nb = sum_{j=m}^{2m-1} sum_{i=m-1}^{j-2} ((j-i)^2/(4m^2)) C_ij`,

with the usual positive cross-ratio coefficient `C_ij`.

Using only positivity, integer spacing, and distinctness of adjacent gaps, we obtain the finite bound

`Z_m^nb >= E_m/(8m^2 H_m) >= m^2/(384 H_m)`,

where `H_m=a_{2m-1}-a_{m-2}` and

`E_m=m(m-2)(m^2+8m+6)/48`.

Consequently, on any hypothetical fixed infinite branch satisfying

`a_n <= C n^2 log(2n)` eventually,

one has for all sufficiently large dyadic `m`

`Y_m >= Z_m^nb > 1/(1536 C log(4m))`

and the same lower bound for `Z_m`. Thus the dyadic sums of both `Y_m` and `Z_m` are `Omega_C(log J)`.

This changes the logical status of two proposed intermediate statements. Their universal forms,

`sum_{m in E_J}Y_m=o_C(log J)` and `sum_{m in E_J}Z_m=o_C(log J)`

for every fixed `C` and every fixed branch satisfying the critical cap, are each equivalent to Question 1: if Question 1 is true the quantified branch class is empty, while either statement contradicts the displayed harmonic floor if a critical branch exists.

The exact finite telescope is

`sum Y_m = R_4 - R_{2^{J+1}} + sum Z_m`.

Therefore a valid continuation must keep the terminal term. Proving `sum Z_m=o(log J)` separately discards the only channel that can absorb the harmonic new-birth mass and jumps directly to a target-equivalent contradiction.

We also have several narrower method obstructions and finite counterexamples, but we do not claim that they exclude all multiscale approaches. Current open questions for this route are:

1. Is there an exact finite-horizon terminal potential that controls the terminal suffix fan without borrowing from future epochs?
2. Can future-rank promotion be assigned as a genuinely disjoint premium over the existing Abel/rearrangement floors, with atomwise ownership?
3. Is a different architecture—averaging over block sizes, a reverse martingale, entropy, or an inverse theorem for near-extremizers—more natural?

Before public posting, attach a concise proof, exact index conventions, an independent checker for the finite identities, and a Lean formalization of the harmonic theorem and the quantifier equivalence. We welcome references to existing results that subsume these statements.
