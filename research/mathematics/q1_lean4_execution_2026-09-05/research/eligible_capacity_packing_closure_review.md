# Independent parent review of the lattice and residue packing analysis

2026-09-05. Source `eligible_capacity_packing_closure.md`, final SHA-256
`1bbe91da5091f59c1ecaf32cd70a8e48fd22bc7e174dd09c2831614d41e34964`.
The parent read the full draft, independently reconstructed its arguments,
then read the final added positive translation, finite-modulus corollary,
and explicit component embedding. The finite-modulus corollary was suggested
by the parent and independently checked by the author before inclusion.

**Result: PASS at the stated analytical scope.** No computation or Lean
run was needed. No capped infinite history has been constructed. The
universal implications on capped classes remain conditional, and original
Q1 is unresolved.

## Sampling and the original frozen packing

Centering an affine test at LM/2 diagonalizes both counting-measure norms
in the constant and linear coordinates. Summing the squares of the M+1
lattice positions gives L^2 M(M+1)(M+2)/12. Subtracting this from the full
integer-interval variance gives L M(L-1)(L M^2-2)/12 for the complement.
The constant counts are M+1 and (L-1)M. The two coefficient ratios give
the uniform lower factor 2(L-1)/5 for M>=3 and L>=2, with the linear
factor attaining the limiting worst case M=3,L=2. The displayed weaker
inequality is sufficient even when the removed lattice holes are not
symmetric, because no nonlattice point is removed.

For any nonzero residue, convexity of the squared affine function on each
adjacent lattice interval bounds its sum by the lattice sum. The endpoint
weights are at most one; each interior weight is exactly one. Combining
at most rho residues and Cauchy with the affine variational formula gives
theta=5rho/[2(L-1)]. This is a bound for the complete two-dimensional
projection, including its cross term on the nonsymmetric punctured domain.

The actual future shadows vanish on the block itself by Sidon uniqueness.
For a dilated row its support interval has M>=3, since the old radius and
block span are both positive integers. Its holes are lattice nodes and
the shadows use one residue. Applying the norm bound to both shadows
retains the single diagonal subtraction; thus J<=theta Praw minus the
nonnegative remaining diagonal. Taking positive parts preserves
J^+<=theta Praw. Summing the actual per-pair constraints proves the bound
for the entire finite optimum, not only for individual disjoint rows.

The weighted margin identity uses u_N r_N plus the finite layer sum. Its
coefficients are nonnegative. Substitution of the row bound therefore gives
the displayed fraction of actual eligible capacity. On dilation the raw
carrier scales by L^2 and its complete-history price by L^-2; output and
birth ranks are unchanged. This proves exact normalized capacity invariance,
including the infinite price tail.

Consequently bounded residual on every member of a dilation-closed class
implies bounded eligible capacity, by applying the residual bound to 6P.
The converse follows from nonnegativity. Neither implication needs one
constant uniform over histories. For the class defined by existence of
some fixed eventual cap, dilation merely changes that fixed constant.
Together with the prior cap-forced divergent demand, a universal residual
bound would contradict the existence of such a history. This is a closing
implication, not a proof of its missing premise or a constructed counterexample.

## Primitive transformation and the price shift

For P={0,1,L a2,L a3,...}, the three gap types have residues 0,1,-1.
Each type has distinct gaps and the residue types do not meet for L>=3.
This verifies actual Sidonicity including repeated two-sums. The presence
of the unit gap verifies gcd one. Translation of the whole set by one
enforces positive integers without changing any claimed geometric quantity.

For old n>=3 the shadows use only three residues; theta<=1/2 at L>=16.
At n=2 the only potential source-pair output is 2, whereas every actual
future difference is a multiple of L, so the raw pair payment is zero.
This separately handles the spectator row instead of applying the
three-residue argument at a nonmultiple radius.

The exact coefficient formula is
kappa_l=4/[l(l-1)^2(l+1)^2]. Its shifted ratio is the one in (12).
Clearing denominators in its 3/32 lower bound gives
(l-2)(29l^2+14l-16)>=0 for l>=2. Reindexing the entire compatible tail
with H_(l+1)(P)=L H_l(A) proves the stated u-price comparison. Every
eligible bulk pair keeps its strict birth/lower/upper order after the
common rank shift, and all extra pairs have nonnegative weight. Hence
both finite inequalities (13), including the 3/64 margin constant, follow.
The cap and shifted onset are preserved with a new fixed constant; no
finite moving-onset construction is substituted for an infinite history.

## Same-source residue refinement and its exact limitation

The two shadow moments in (14) follow by writing x=b+d before summing.
For the even feature the first moment is b|d|+d|d|; for the odd feature
it is bd+d^2. This verifies all four residue convolutions. In particular
the odd mass and even first source moment need not vanish separately in
each residue. Combining them before squaring is essential and is done.

The supports Omega_s are disjoint. The global affine subspace embeds in
their piecewise affine subspace, so its projection norm cannot decrease.
Singleton and empty supports are treated without dividing by zero. The
orthogonal residual identity uses one combined diagonal subtraction and
the unchanged actual pair payment. At q=L a fully dilated history reduces
exactly to the original affine projection with its L^2 feature scaling.

Rows with different q share identical physical pair masks; selecting their
best objective or listing fractional copies is equivalent under the same
constraints. For a fixed finite family, choose L divisible by all q and
at least six times their maximum. The only active q-residue then has
relative lattice spacing L/q>=6. The same sampling theorem gives the
uniform half-loss for every permitted q and hence their maximum. This
extends the fixed-packing obstruction without granting separate budgets.

If q exceeds the full shadow interval width, all residue pieces are
singletons and the projection equals the actual shadow. For every output
with positive eligible payment, i>=3, so n=i-1 is an allowed old rank.
Its two-point block has exactly that output and all its eligible source
pairs. Different outputs have disjoint pair masks by actual output
uniqueness. These rows recover all raw eligible capacity with coefficient
one each, proving (18). This unconditional identity explains why a zero
residual for unrestricted residue data has no Q1 closing implication.

## Distinct masked source and retained clocks

The mask D_q is the Gram of residue indicators. Schur multiplication with
the existing K and the two-feature W preserves PSD and nonnegative entries.
Its unit diagonal leaves the trace unchanged. Zero embedding outside each
actual component bank ensures that summation starts at max(b,r), giving
the exact fixed-q coefficient (20). A never-used output has zero entry
in every finite K component.

For a monochromatic actual block its internal outputs are all divisible
by q, so the masked and original matrices agree on the entries actually
paid. There is no such equality for an arbitrary multicolored block.
Different monochromatic blocks still have disjoint actual positive
differences. Fractions over moduli within a component sum to at most one,
which proves the matrix entry and trace domination in (21). Their fixed
complete-history choices do not license independent terminal re-selection.
When the modulus varies by component the pure u_r factor need not survive;
the source correctly refrains from importing unmodified collision
cancellation formulas in that case.

The final obligations are therefore stated accurately: a genuine capacity
upper bound or a nontrivial cap-based comparison for restricted data is
still required. The finite transforms, exact residue identities, and
concrete masked Gram sources do not supply that global argument.
