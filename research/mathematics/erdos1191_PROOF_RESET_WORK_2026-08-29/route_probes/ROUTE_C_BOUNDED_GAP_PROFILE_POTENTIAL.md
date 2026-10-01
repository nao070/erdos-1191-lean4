# Route C: bounded normalized gap-profile potential

Date: 2026-08-31  
Status: `HUMAN_PROOF_AUDITED_STORAGE_COLUMN_LOCAL_INEQUALITY_OPEN`

C118 shows that the normalized total shell-span increment `eta_k` forgets
load-bearing within-shell shape.  This note introduces the smallest exact
bounded shape column suggested by the obstruction and proves that its signed
Fejér increments telescope at uniformly bounded cost.  The local
phase-margin inequality involving this column is still open.

## 1. A bounded scale-free shell concentration

For one shell of `n` positive consecutive gaps `h_1,...,h_n`, write

\[
 H=\sum_{i=1}^n h_i,
 \qquad Q=\sum_{i=1}^n h_i^2,
\]

and define

\[
 V(h_1,\ldots,h_n)=1-\frac{H^2}{nQ}.
\tag{1.1}
\]

Cauchy--Schwarz gives `H^2<=nQ`, while positivity gives `H^2/(nQ)>0`.
Therefore

\[
 0\le V<1.
\tag{1.2}
\]

The value is invariant under common dilation of every gap and uses only the
current finite prefix.  If `CV^2` denotes the squared coefficient of variation
of the shell gaps, then

\[
 V=\frac{CV^2}{1+CV^2}.
\]

Thus (1.1) is zero exactly for an equal-gap profile and approaches one as the
mass concentrates.  It compares shells of different cardinalities without an
unbounded factor of `n`.

For the dyadic shell at scale `k`, use the `n=2^k` gaps between ranks `2^k-1`
and `2^(k+1)-1` and denote (1.1) by `V_k`.

## 2. Exact finite Fejér--Abel telescope

Let `p_a>=p_(a+1)>=...>=p_b>=0` and let every `V_k` lie in `[0,1]`.  Exact
finite summation by parts gives

\[
 \sum_{k=a}^{b}p_k(V_{k+1}-V_k)
 =p_bV_{b+1}-p_aV_a
  +\sum_{k=a+1}^{b}(p_{k-1}-p_k)V_k.
\tag{2.1}
\]

The positive-coefficient part on the right of (2.1) lies between zero and

\[
 p_b+\sum_{k=a+1}^{b}(p_{k-1}-p_k)=p_a.
\]

The subtracted term `p_a V_a` also lies in `[0,p_a]`.  Hence the sharp uniform
bound

\[
 \left|\sum_{k=a}^{b}p_k(V_{k+1}-V_k)\right|\le p_a
\tag{2.2}
\]

holds for every finite horizon.

For the C115 weights

\[
 p_{k,J}=\frac1{k+1}
 \left(\frac{J+1-k}{J+1}\right)^2,
\]

on the finite range `0<=a<=k<=b<=J`, the sequence is nonnegative and
decreasing, and `p_(a,J)<=1/(a+1)`.
Consequently

\[
 \left|\sum_{k=a}^{b}
 \frac{\omega_{k,J}}{k+1}(V_{k+1}-V_k)\right|
 \le\frac1{a+1}.
\tag{2.3}
\]

Unlike the logarithmic span potential, (2.3) requires neither a critical cap
nor an `O_C(log k)` endpoint estimate.  Any fixed finite nonnegative linear
combination of bounded profile coordinates has the same property after
scaling the right side by the sum of its coefficients.

## 3. Exact calibration on the three certified fixtures

The following values use precisely the past four gaps and current eight gaps
of the C112, C114, and C118 fixtures.

| fixture | `V_2` | `V_3` | `V_3-V_2` |
|---|---:|---:|---:|
| C118 eta-negative | `1271/5028` | `4594463/7346744` | `3440812085/9234857208` |
| C112 quadratic | `1/2421` | `21/14905` | `35936/36085005` |
| C114 powers of two | `23/68` | `1291/2056` | `10125/34952` |

Numerically, the increments are approximately `0.372590`, `0.000996`, and
`0.289683`.  Thus (1.1) detects a large concentration increase in both known
negative geometries while changing by only about `10^-3` in the certified
positive quadratic phase.

The same comparison for the mass in the largest quarter of each shell gives
increments

\[
 \frac{76701}{244426}\approx0.313800,
 \quad
 \frac{147}{26840}\approx0.005477,
 \quad
 \frac{56}{255}\approx0.219608,
\]

respectively.  This supports a multiscale concentration vector, but it is only
finite calibration, not a universal separation theorem.

## 4. Necessary coefficient imposed by C118

Suppose the repaired `k=2` target is

\[
 \overline\Phi_2\ge
 \frac{\epsilon-A\eta_2-B(V_3-V_2)}{3},
 \qquad \epsilon,A,B\ge0.
\tag{4.1}
\]

C118 proves `overline Phi_2<-1/40` in the stated cone and has `eta_2<0`.
Therefore a necessary condition for (4.1) not to contradict that exact upper
bound is

\[
 B(V_3-V_2)>\epsilon+A|\eta_2|+\frac3{40}.
\tag{4.2}
\]

Even at `epsilon=A=0`, (4.2) requires

\[
 B>\frac{3463071453}{17204060425}
 \approx0.201294.
\tag{4.3}
\]

The strengthened C118 replay also proves that the **normalized** dual upper
`U` obeys

\[
 -\frac{81}{2000}<U<-\frac1{25}.
\tag{4.4}
\]

Using the upper endpoint in (4.4) strengthens (4.2) to

\[
 B(V_3-V_2)>epsilon+A|\eta_2|+\frac3{25}.
\tag{4.5}
\]

At `epsilon=A=0`, this requires

\[
 B>\frac{27704571624}{86020302125}
 \approx0.322070.
\tag{4.6}
\]

As an exact finite calibration, the trial
`epsilon=A=1/1000`, `B=1/3`, `e_2=0` is not excluded by C118: its required
lower value is strictly below `-41/1000`, while (4.4) puts `U` strictly above
`-81/2000`.  On C112, the same trial requires less than
`27229385925821/64953009000000000`, whereas the certified positive margin is
`255996752651/512000000000000`; their exact difference is
`2686313784890824859/33255940608000000000000>0`.

These are necessary-side and finite-witness calibrations only.  C118 supplies
a dual upper bound, not a matching primal lower bound for (4.1), and the
trial constants are not asymptotic theorem constants.

## 5. Why one scalar is not yet a theorem

The finite table is encouraging but insufficient for three independent
reasons:

1. C118 is a `k=2` fixture and is not an eventual critical infinite history.
2. The scalar (1.1) is invariant under permutation of the gaps, whereas the
   ordered Haar cells and owner rows can depend on their positions.
3. A valid local inequality needs a constructive lower bound on the best
   phase margin and one legal global owner ledger; neither follows from the
   bounded telescope.

A more robust profile column is a finite dyadic vector of ordered interval
concentrations.  For example, at depth `r` take the largest mass of a
contiguous dyadic block of `n/2^r` gaps, divided by `H`, and combine these
coordinates with summable fixed weights.  Every coordinate lies in `[0,1]`,
so (2.2) applies coordinatewise, while the vector retains positional and
multiscale information lost by (1.1).

### 5.1 Reverse-profile and permutation stress fixtures

The exact Golomb ruler

`(0,22,60,83,102,173,303,513,616,727,772,881,972,1041,1103,1169)`

has 120 distinct positive differences, satisfies the same three finite
`C=2` envelope rows, and has

\[
 H_2=430,\qquad H_3=656,\qquad
 \exp(\eta_2)=\frac{82}{215},\qquad
 \Delta V=-\frac{443620417}{1928247678}.
\]

It is the first exact reverse-concentration row that a storage theorem must
repay.  C120 now replaces the earlier midpoint-only observation by a complete
exact phase computation at `rho=9/16`: 161 rational chamberwise Gram factors
give

`719/10000 < overline Phi_2 < 9/125`,

while the trial right-hand side lies in `(13/500,27/1000)` and the certified
gap is greater than `457/10000`.  This survival is genuinely phase-integrated.
On chamber 0 alone, an independent exact dual gives an average upper below
`2601/100000`, strictly below the same trial right-hand side by more than
`207/1000000`.  Thus C120 supports complete-phase redistribution but refutes
a pointwise or per-chamber reading of the trial.

A follow-up disposable exact primal bank for C118 now supplies 87 rational
factors with 1,573 columns and verifies all 53,592 open owner rows plus 104,784
endpoint owner rows.  Its normalized feasible witness lies in

`(-47703/1000000,-47702/1000000)`,

whereas the prototype RHS lies in
`(-41045/1000000,-41044/1000000)` and the existing exact dual upper is about
`-0.04014304`.  Thus the prototype lies strictly inside the remaining
primal--dual window: this search neither certifies it nor refutes it.  The
residual gap is about `0.00755914`, concentrated most strongly in chambers
49, 73, 74, 64, and 70; chamber 1 also resisted a second exact rationalization
scheme.  These `/tmp` artifacts are diagnostic and are not a registered
certificate.

A disposable search returned exact within-shell permutation candidates of the
C118 gap multisets that keep
`eta`, (1.1), Gini, maximum-gap, sorted-tail, and entropy values fixed while
an order-sensitive centered dyadic-tail increment changes sign, from about
`+0.14925` to `-3951736/12099087`.  This shows why the next bank must test both
permutation-invariant concentration and bounded ordered coordinates; the
permutation list and floating midpoint margins are not yet canonical
certificates and remain discovery data only.

## 6. Smallest next exact experiment

The next computation should not merely fit coefficients to the three rows
above.  It should:

1. close the remaining exact C118 primal--dual window around the prototype,
   either by a stronger rational primal bank or a tighter rational dual,
   beginning with chambers 49, 73, 74, 64, 70, and the chamber-1
   rationalization boundary;
2. compute `eta`, (1.1), and a small ordered dyadic concentration vector on a
   bank containing C112, C118, the reverse-profile fixture, same-multiset
   permutations, and a Mian--Chowla prefix;
3. solve a small rational outer LP for common `epsilon,A,B_r`, with held-out
   fixtures and strict slack;
4. replay every selected primal/dual endpoint and the full log-phase integral
   exactly, without requiring a false chamberwise lower bound; and
5. only after the 16-mark bank survives, repeat at 32 marks or on a scalable
   critical-compatible family.

The desired theorem remains a nonanticipating storage/dissipation inequality

\[
 \overline\Phi_k\ge
 \frac{\epsilon_C-A_C\eta_k
 -\sum_r B_{C,r}(V^{(r)}_{k+1}-V^{(r)}_k)}{k+1}-e_k,
\tag{6.1}
\]

with the complete C103 boundaries and a single global owner system.  Equations
(1.2)--(2.3) certify only that the new storage column is admissible in the
global Fejér telescope.  C120 adds one exact held-out full-phase calibration,
not a proof that the scalar `V` works uniformly.  Neither result proves (6.1),
C058, either Erdős question, novelty, or prize eligibility.


## C121 superseding update

The C118 prototype is no longer unresolved inside the old
fixed-primal/pointwise-dual window.  The exact reciprocal-subdivision
certificate in `ROUTE_C_C118_SUBDIVIDED_STORAGE_NO_GO.md` proves a normalized
complete-phase upper below `-83/2000`.  On that fixed positive-`Delta V`
row and current cone, `epsilon,A>=0`, `e_2=0` force

`B > 287434930599/860203021250 > 1/3`.

Thus the prototype `B=1/3` and the box `0<=B<=1/3` fail there.  The bounded
telescope proved in this document remains valid; what C121 closes is only its
first scalar coefficient calibration on one finite row.  The next experiment
is a multi-fixture complete-phase outer coefficient bank with both signs of
`Delta V`, ordered profile coordinates, permutations, larger rank, and one
global C103 owner ledger.

## C122--C124 superseding update

The two-row scalar bank and one exact same-multiset permutation have now been
completed.  They leave the clean nonempty interval

`1341/4000 < B < 4753/10000`.

Thus the C119 scalar remains a useful bounded column but does not separate the
current finite rows by itself.  The ordered successor is now frozen in
`ROUTE_C_ORDERED_SUFFIX_PROFILE_POTENTIAL.md`.  Its chronological suffix
coordinate lies in `[0,1)` for every positive dyadic shell and has the same
finite Abel control, while its exact increments on the same-multiset C120 and
C123 rows have opposite signs.  The next outer bank is therefore genuinely
two-dimensional in `(B,C)`.

The C120/C123 adaptive phase intervals differ under permutation.  Any theorem
use must first freeze the intended nonanticipating phase-base rule or prove
representative independence.  C058 remains open.
