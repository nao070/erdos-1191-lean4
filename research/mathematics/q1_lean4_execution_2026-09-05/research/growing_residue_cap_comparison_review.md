# Independent parent review of growing residue information

2026-09-05. Source `growing_residue_cap_comparison.md`, final SHA-256
`dde8cec1ec969f61685d13e59a7df5197e3a1e7f2447e2911c9d0dd2d77c5af0`.
The parent read the entire source and independently reconstructed the
counting, moment, projection and complete-history price arguments.

**Verdict: PASS at the stated analytical scope.** No numerical or Lean run
was used. The growing coprime-family obstruction is an actual Sidon
transformation, with all capped infinite-history claims conditional. It
does not rule out the full adaptive integer-modulus interval or resolve Q1.

For (1), the positive gaps within one endpoint residue are distinct positive
multiples of q at most H, across all residue classes combined. Summing the
binomial counts proves the exact integer upper bound. The square-count,
support-count Cauchy lower bound and individual quadratic count bound follow
with their stated constants. No modular Sidon property is assumed.

For (2), ordered endpoint differences give the residue convolution, with
exactly N self-pairs removed in residue zero. Every other ordered pair has
a unique nonzero signed integer label. Counting integers in [-H,H] gives
the separate zero and nonzero class bounds. The common denominator in (3)
also bounds the zero class, so the support lower bound is valid. The fixed
cap substitutions in (4) have the correct directions. At q comparable to
N log(2N), both support estimates have linear scale, not uniform occupancy.

Expanding a-b and (a-b)^2 proves every term and sign of (5), including
the absence of a self-pair correction in these zero-weight expressions.
The ordered prefix formulas for E_c^(h) count each positive difference once.
Adding and subtracting the opposite residue gives (6), including the
self-opposite residue case: the two signed labels remain distinct, while
their odd contributions cancel. The four shadow convolutions (7) follow
by x=b+d and retain the actual residue first moments before squaring.

The actual-hole estimate is uniform in the future block span. Put x=l/q.
The number of block holes in any residue is at most 1+sqrt(2x) by the
actual same-residue Sidon gap count. The ambient residue count is at least
x+2H/q-1. Subtraction and x-sqrt(2x)>=-1/2 give D_s>=2H/q-5/2.
Since 2H>=n(n-1), the entire interval q<=n log(2n) has the claimed
growing lower bound even after its actual holes. Thus this information
range is not secretly singleton refinement on sufficiently late rows.

The refinement surplus (10) is the squared norm of the projection of
f-Proj_1 f onto the larger piecewise affine space. Its residue mass is
r_s and its centered first moment is t_s exactly as displayed: the
constant part cancels, and the removed linear part contributes beta V_s.
Orthogonality of mass and centered coordinate on each support proves the
sum of squares. Empty and singleton supports are treated without a zero
division. The original diagonal is subtracted once and the pair payment
is unchanged. Separate moduli therefore must retain the same constraints
(11), as the source explicitly requires.

For K consecutive sites the affine reproducing-kernel diagonal is maximized
at an endpoint. Its exact maximum is (4K-2)/(K(K+1))<4/K. A union of rho
progressions of spacing D contains at most rho(K/D+1) sites. For K>=D,
the selected squared affine norm is consequently at most 8rho/D times
the full norm. Removing holes inside that same support leaves at least
1-8rho/D of the norm. The variational projection formula then gives
8rho/(D-8rho) in (13), including truncated boundary periods and arbitrary
actual hole positions. This proof does not presume periodic symmetry
of the entire finite interval.

For the pure dilation 24A, every q coprime to 6 is coprime to 24. At
n>=5 the allowed q is at most n(n-1), whereas 2H_n(24A)>=24n(n-1).
Every ambient q-residue has at least 24 sites. Both shadows and all holes
lie in one progression of spacing 24 within that residue, so (13) gives
a half projection bound for each shadow and each actual row simultaneously.
Keeping the same diagonal subtraction yields (15). It holds for the whole
growing family, and hence any prime subfamily, without a claim about prime
counts or an adversarially selected row after optimization.

Early rows use only one fixed bank Fhat_4. If Eraw and Lraw denote their
and the late rows' actual pair expenditures, respectively, then
Eraw+Lraw<=Hcum and Eraw<=R0. The objective is at most Eraw+Lraw/2,
which proves Hcum/2+R0/2 in (16). Under the compatible layer prices,
the coefficients on this constant sum exactly to u_2. This checks the
single finite initial charge in (17); it is not incurred again for each
component or modulus. Normalized eligible capacity is exactly dilation
invariant, so the stated class-wide boundedness equivalence follows.

For the primitive transformation the gap residues 0,1,-1 modulo 72 are
disjoint and each type has distinct actual gaps. The unit gap proves gcd
one. Translation by one enforces the positive-integer convention without
changing any quantity used. For n>=8 the claimed upper bound
n log(2n)<=(n-1)(n-2) holds by the two elementary inequalities stated.
Every residue class therefore has at least 72 ambient sites. At most
three support progressions, with D=72, again give half loss. Early ranks
use only Fhat_7. The exact kappa shift ratio is at least 3/32, as in the
prior reviewed primitive transform, and all bulk eligible pairs retain
their strict order. Thus the 3/64 comparison in (18), with one fixed
initial cost, is correct.

The important limitation is preserved. The full interval of integer
moduli eventually contains multiples of the fixed dilation, for which
L/gcd(L,q) can be one. The within-residue leverage estimate then yields
no loss. Broad endpoint residue support and increasing modulus size alone
are insufficient, but an adaptive choice exploiting divisibility has not
been disproved. The source claims no universal capacity upper bound or
actual infinite fixed-cap counterexample.
