# Route C: exact cross-kernel positivity gate

Date: 2026-08-29  
Status: `HUMAN_PROOF_AUDITED` finite analytic gate; Q1/Q2 unresolved

## 1. Exact expansion

Let `A` be a finite Sidon subset of `Z`, let `K_1,...,K_R` be finitely
supported real kernels, and put `u_r=1_A*K_r`.  For a symmetric real matrix
`H=(h_rs)`, define

`E_H=sum_(r,s) h_rs <u_r,u_s>`

and the combined correlation kernel

`C_H(d)=sum_(r,s) h_rs sum_x K_r(x)K_s(x+d)`.

Direct expansion and the symmetry of `H` give

`E_H=|A| C_H(0)+2 sum_(d in Delta(A)) C_H(d)`,                 (1)

where `Delta(A)` is the set of represented positive differences.  Because
`A` is Sidon, every such difference occurs once.

If `C_H(d)>=0` for every positive `d`, difference uniqueness may be used
without changing the inequality direction:

`E_H <= |A| C_H(0)+2 sum_(d>=1) C_H(d)`.                     (2)

Writing `m_r=sum_x K_r(x)`, the full correlation mass is

`sum_(d in Z) C_H(d)=m^T H m`.

Consequently (2) becomes the exact upper bound

`E_H <= m^T H m+(|A|-1)C_H(0)`.                             (3)

For probability kernels, `m=(1,...,1)`.  The diagonal choice
`H=diag(lambda_1,...,lambda_R)` recovers the upper-energy step in the
Hou--Zhao vector smoothing lemma.

## 2. Why positive semidefiniteness alone is insufficient

Take two point-mass probability kernels

`K_1=delta_0`, `K_2=delta_1`

and

`H=[[1,-1/2],[-1/2,1]]`.

The eigenvalues of `H` are `1/2` and `3/2`, so `H` is positive definite and
`E_H>=0` for every input.  Nevertheless

`C_H(1)=C_H(-1)=-1/2`, `C_H(0)=2`, and `1^T H 1=1`.

For the Sidon set `A={0,2}`, equation (1) gives `E_H=4`, whereas the
illegitimate PSD-only version of (3) would give `E_H<=3`.  The set simply
avoids the negative correlation shift.  Thus PSD controls the quadratic form
but does not authorize filling all unrepresented Sidon differences in the
upper bound.

This exact two-kernel counterexample is the smallest red-team fixture for any
cross-kernel Route C proposal.

## 3. Surviving Route C obligation

A genuine cross-scale or cross-kernel improvement must prove at least one of:

1. `C_H(d)>=0` at every nonzero integer shift;
2. a separately proved theorem forcing the actual difference set to pay for
   the negative shifts; or
3. an upper bound using `sum_d max(C_H(d),0)`, with a net asymptotic gain after
   that positive-part cost is included.

The first option matches the caveat in Hou--Zhao v2, Section 5.  It is not
enough to exhibit a PSD matrix, a smaller numerical objective, or a joint
boundary cover.  In addition, an application to #1191 must use one compatible
infinite history and change the asymptotic order; a finite `N^(1/4)`
second-order improvement is not Q1 progress.

## 4. Exact positive-part and zero-mass consequences

The exact positive-part completion and its zero-mass consequence are now
proved in `ROUTE_C_POSITIVE_PART_ZERO_MASS_NO_GO.md`.  In the notation above,

`E_H <= |A|C_H(0)+2 sum_(d>=1) max(C_H(d),0)`

`=m^T H m+(|A|-1)C_H(0)+2 sum_(d>=1) max(-C_H(d),0)`.

Thus option 3 above has an exact, unavoidable price.  If the kernels are
probability kernels, `H` is PSD, and `H 1=0`, the cost-free sign gate makes
the energy identically zero.  The minimal and arbitrary-point-mass
subclasses are certified separately.  These are scoped G2 closures; the
overlapping nonzero-mass class is addressed next, while actual difference-set
payment and geometry-sensitive compatible-history terms remain possible P4
inputs.

## 5. Overlap passes the sign gate but exposes a normalization problem

`ROUTE_C_OVERLAPPING_KERNEL_FEASIBILITY.md` proves that two overlapping
probability kernels can use a negative positive-definite cross coefficient,
keep `C_H(d)>=0` at every nonzero shift, and strictly reduce the pure legal
upper-energy expression.  Its smallest half-grid witness has ratio `4/7` at
cardinality two.  This is a genuine escape from the point-mass obstruction.

It is not yet a useful joint Sidon inequality.  A rational full-overlap
family drives the unnormalized energy ratio to zero only while total
correlation mass, zero-shift energy, and the small Gram eigenvalue all tend to
zero.  A surviving theorem must fix a joint boundary-cover or lower-energy
normalization and show a gain after that denominator is included.

## 6. Proof audit

Equation (1) follows by writing

`<u_r,u_s>=sum_(a,b in A) sum_x K_r(x)K_s(x+a-b)`

and grouping diagonal and positive/negative differences.  Symmetry of `H`
implies `C_H(-d)=C_H(d)`.  Tonelli is finite here.  Equation (3) follows from
the nonnegative-shift hypothesis and

`sum_d sum_x K_r(x)K_s(x+d)=(sum_x K_r(x))(sum_y K_s(y))`.

No asymptotic statement, literature novelty claim, or implication to Q1/Q2
is asserted.
