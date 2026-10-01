# Independent parent review of the proposed triple-source remainders

2026-09-05. Reviewed source `triple_source_remainder_analysis.md`, SHA-256
`6476aca5330fa7a368b40872650994290c97f2456899cb73f9fccb67c68eb775`.
The input productive source is bound to its final SHA-256
`f9be618684b2ed933b480f4107c0ccdbddffd309339e7d63db831d511cf920ff`.

**Result: PASS for the two stated analytic obstructions.** The parent
independently reconstructed the formulas and the finite actual endpoint
example. This was a proof review, with no new search, numerical run, or
Lean execution. It is not a proof that every full-defect representation
fails, and not a result resolving original Q1.

The vector r(s) has squared norm S(s)P(s); coordinates from different
sums are disjoint because each triple multiset has exactly one sum.
Its translated Gram is therefore L/(Q^2 H^2) times the identity. Collapsing
each vector to its scalar norm preserves diagonal norms while introducing
nonzero off-diagonal correlations. The displayed difference D-A then has
zero diagonal and a negative off-diagonal entry, so its two-by-two
principal block is indefinite. A positive debit theta A from any scaled
diagonal reserve still has a negative off-diagonal entry. These are
failures of the specified PSD-and-entrywise-nonnegative remainder, not
failures of scalar mass financing.

For the alternative reserve gamma J, the vector e_d-e_e lies in the
nullspace of J. Its quadratic form against the proposed remainder is
minus the squared distance of two distinct translates of R, with the
correct Q^2 H^2 denominator. The distance is positive: a nonzero finite
support cannot be invariant under a nonzero integer translation. This
proves the claimed obstruction for every gamma, without requiring a
uniform scalar bound or an arbitrary off-history Gram example.

The parent recomputed the entire P3={0,1,3} table. At sum 3 the otherwise
zero-potential triple {1,1,1} must remain in S(3), giving S=2/3, P=9/2
and R^2=3. Together with sums 1,4,5 this gives L=41/4. The only nonzero
correlation at displacement 4 is R(1)R(5)=1/2. Thus the diagonal is
41/1296, the selected off-diagonal is 1/648, the principal-block
eigenvalues are +/-1/648, and the gamma J test is -13/216.

The ten positive differences of P5={0,1,3,10,14} are exactly the ten
distinct numbers listed in the source. This verifies actual Sidonicity,
including the repeated two-sum condition through difference uniqueness.
The sources -1 and 3 have later birth 3, whereas their output 4 has
actual endpoint ranks 4 and 5. The same is true of the other two old
pairs {-3,1} and {-2,2}. Their common coefficient sums to the actual
two-point block payment 1/216. Multiplying by kappa_3 changes no sign.

Translation by one gives the positive example {1,2,4,11,15}. Its widths,
signed labels, birth ranks, and correlations of triple fibers are
unchanged; the fiber coordinates themselves shift by three. This
explicitly connects the finite example to the positivity convention of
the original problem.

The important limit is stated correctly. D is the canonical orthogonal
realization of the scalar norm L; it has not been established as a
matrix representation of all geometry defect G. Similarly gamma J is
one proposed coherent reserve. The finite obstructions rule out these
two proposed debits, while leaving other full-G representations and
joint allocation inequalities open. They do not invalidate the prior
Theta cost bound or supply an infinite capped Sidon counterexample.
