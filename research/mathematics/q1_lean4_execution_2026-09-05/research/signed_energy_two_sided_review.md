# Independent review of two-sided retirement and raw-energy monotonicity

2026-09-05. Reviewer: `/root/linear_causal_sign`, GPT-6 Astra Ultra.

**Verdict:** mathematical PASS for equations (1)--(13) of
`signed_energy_two_sided.md`. No correction is requested. For the actual
raw signed feature, the full output-stage retirement lies in
[-B_j/4,2B_j], the raw energy increases strictly, and its exact diagonal
excess is nondecreasing. The physical-margin and source-clock caveats
are necessary and correctly retained.

The complete source was read in tool chunk `407a65`. Its observed
9,834-byte final source was bound at actual UTC time
`2026-09-05T11:18:00.799505+00:00`, tool chunk `73f403`, to SHA256

```
1364dd87dc4290f50e3a7367500c1059519beba24eb076202c1a559c87d6dcb2
```

This is an independent analytical review. No numerical test, saved-test
rerun, Lean execution, or new formal verification was performed. Only
review files were written; the source and prior evidence were preserved.

## 1. Collision lower bound and stage normalization

With X+Y=-c, the identity
sigma_V^2=(3/2)c^2+(1/2)(X-Y)^2 immediately gives

```
R(U,V)+B(U,V)/4
 =[3sigma_U^2+6sigma_V^2-9c^2]/A
 =3[sigma_U^2+(x-y)^2]/A>=0.
```

This uses the previously reviewed exact automorphism-weighted collision
formulas. Repeated slots and doubled numeric labels are already included;
no additional distinctness hypothesis is inserted. In particular x=y is
permitted. The hand example U={1,1,1}, V={0,0,3} has A=12 and
(B,R)=(4,-1), so equality in the lower collision bound is possible.
The source correctly does not call this equality for the full stage.

The exact stage partition adds a nonnegative Born-only remainder B_j^0.
Its lower-bound effect has the correct direction:
-sum_active B(U,V)/4 >= -B_j/4. The upper bound also persists after
adding B_j^0. Thus the full inequality -B_j/4<=R_j<=2B_j includes
all automatic groups, source-birth ties, and repeated-label groups.
Here B_j is priced at source stage j and R_j at output stage j.

## 2. Actual energy and diagonal excess

Each used pair first contributes when all its sources and its output are
present. Its first stage is b when Born and r when retired. Therefore
the full pair expansion and increment are exactly

```
E_N=N Z_N+2sum_(j<=N)(B_j+R_j),
Delta E_j=Z_(j-1)+j v_j+2(B_j+R_j).
```

The diagonal difference Dhat_j=Z_(j-1)+j v_j is correct; no positive-bank
mixed-source diagonal is imported. Since B_j>=0 and B_j+R_j lies
between (3/4)B_j and 3B_j, the two increment bounds in (6) follow.
The actual new signed birth class has 2(j-1) nonzero labels, so v_j>0
and Dhat_j>0 at every j>=2. Thus E_j is strictly increasing.

Subtracting the same exact diagonal gives

```
Y_N=E_N-N Z_N,
(3/2)B_j<=Delta Y_j<=6B_j.
```

With Y_1=0, summation proves (7), including Y_N>=0 and monotonicity
of Y_N. These conclusions concern the raw feature d on the growing
actual bank, not a radius-normalized energy or arbitrary odd feature.

## 3. Weighted identities and bounded diagonal

Multiplying the stage inequalities by any nonnegative omega_j proves
all comparisons in (8); decreasing prices are not needed for that step.
For decreasing prices, finite summation by parts with E_1=Y_1=0 gives
both identities in (9), with the stated terminal term and interior
coefficients. The second line is the Abel expression of the exact
diagonal excess, so all of its summands are nonnegative.

For omega=w the direct estimate is

```
omega_j Dhat_j<=2/j^2+1/[j(j-1)].
```

Its sum from j=2 is 2zeta(2)-1. The compatible u satisfies
0<=u_j<=w_j, hence has the same diagonal upper bound. Applying these
facts to (8) proves (10) and the equivalence of the indicated weighted
Born and energy divergences. All u entries remain fixed from one complete
history. No retired source price is substituted for an output price.

## 4. Current-row residual has the stated scope

The centered source vector has total mass zero and square sum Z_N.
Its unordered offdiagonal raw product sum is therefore -Z_N/2.
The sum on all currently used output labels is B_(<=N)+R_(<=N)=Y_N/2.
Subtracting proves the exact current-unused identity (11).

For the single normalized row z=d/H_N, the kernel difference between
J and J+lambda zz^T is -lambda/H_N^2 times that same raw correlation.
Thus its current capacity saving is exactly
lambda(Z_N+Y_N)/(2H_N^2). Inserting the two Y_N bounds gives the
constants 3/4 and 3 in (13). Both kernels are PSD and entrywise
nonnegative for 0<=lambda<=1. This computation keeps one row, one
normalization, and one current-unused mask throughout.

It does not assign a sign to a source-clock-weighted matrix evaluated
against a later terminal-unused set, nor does it pass through a maximum
of rows or a future-span mask. The note states these limitations
explicitly. The unresolved commutator term is not settled by (11).

## 5. Earlier wording and retained proof scope

The previous quantitative proof did not require energy monotonicity, but
its aside that E_n need not be monotone was incorrect for this actual
raw source. The new theorem supplies the stronger correct conclusion.
The revised statement that the earlier Abel lower-bound argument does
not require monotonicity is accurate; its proof and constants survive.
The separate quantitative review receives a follow-up binding while
retaining its original source hash and the history of that review.

This new note establishes finite analytical stage and energy results.
It neither formalizes the Sidon orbit partition in Lean nor proves the
remaining shared physical capacity-minus-demand estimate or original Q1.
