# Wave 7 exact adversarial probe of band-renewal improvements

**Date:** 2026-08-28  
**Status:** two natural strengthenings are refuted by exact finite witnesses;
one stronger threshold tax is proved only through eight marks and survives the
larger authenticated finite sample.  No unbounded theorem, infinite extension,
or resolution of Erdős Problem #1191 is claimed.

## 1. Three falsifiable candidates

Use the Wave 6 thresholds

\[
\tau_{m,k}=D_m^-+D_m^++k\max(\mu_m^-,\mu_m^+)
\]

and their cumulative weight

\[
S(T)=\sum_{m,k}k\,1_{\{\tau_{m,k}\leq T\}}.
\]

The Wave 6 theorem is (S(T)\leq\lfloor T\rfloor).  The probe tested:

1. **RH, local renewal holes.**  If an integer interval (K) contains
   actual Wave 6 anti-diagonal differences from (E(K)\geq2) epochs, then
   
   \[
   C(K)+E(K)-1\leq |K|.
   \]

2. **EST, epoch-size threshold tax.**  With
   
   \[
   P(T)=\sum_{m:\tau_{m,1}\leq T}(m-1),
   \]
   assert
   
   \[
   \boxed{S(T)+P(T)\leq\lfloor T\rfloor.}\tag{EST}
   \]

3. **HT, direct harmonic epoch tax.**  At an activation threshold (T),
   with (W=S(T)), assert
   
   \[
   H_W-\sum_{\tau_{m,k}\leq T}{k\over\tau_{m,k}}
   \geq {E(T)-1\over\lceil T\rceil}.
   \]

All interval scans use inclusive integer width and all scores use integers or
`Fraction`; there is no floating-point decision.

## 2. RH is false

Every fixed-ruler RH scan is complete: an interval with occupied differences
may be shrunk to its extreme occupied values without losing an atom, so both
endpoints can be restricted to the finite set of actual differences.

The first authenticated Wave 6 64-mark ruler has consecutive selected values

```text
21  from epoch 8, anti-diagonal 1
22  from epoch 4, anti-diagonal 1
```

in `[21,22]`.  Thus width (=2), occupancy (=2), and (E=2), giving

\[
2-2-(2-1)=-1.
\]

The independent Wave 6 Hall counterexample gives another refutation in
`[382,383]`, from epochs 8 and 16.  Therefore a hole per renewal cannot be
deduced from local numerical-band overlap.

## 3. HT is false

On each of the six authenticated Wave 6 rulers, the first two unit
activations occur at thresholds (1) and (3).  At (T=3),

\[
H_2=\frac32,
\qquad
\sum_{\tau\leq3}{k\over\tau}=1+\frac13=\frac43,
\qquad
{E-1\over\lceil T\rceil}=\frac13.
\]

Hence the HT margin is

\[
\frac32-\frac43-\frac13=-\frac16.
\]

The failure is exact and already occurs at two epochs.

## 4. EST: complete four- and eight-mark result

### Four marks

The exact \(C=1\) caps leave 1,672 normalized four-mark Golomb rulers.  The
enumeration is exhaustive in that scope.  None violates EST; exactly two
attain equality:

```text
(0,1,4,6)
(0,2,5,6)
```

The (C=1) enumeration is larger than what is needed for a universal
four-mark statement.  A failure at the first m=2 activation forces
tau_(2,1) < 3, hence a_1 <= 4 and a_3-a_1 <= 5.  A failure at the
second activation forces tau_(2,2) < 5 and lies in the same bounded region.
There are exactly nine normalized Golomb rulers there; a separate cap-free
enumeration finds no negative margin.  Thus EST holds for every normalized
four-mark Golomb ruler, without an early (C=1) assumption.

### Why a bounded eight-mark enumeration is complete

Consider the first \(m=4\) activation.  Put

\[
M_4=\max(N_4/4,(N_8-N_4)/4).
\]

If it violates EST, then even the upper bounds \(S\leq4+1\) and \(P\leq4\)
force

\[
\lfloor\tau_{4,1}\rfloor\leq8.
\]

Because \(\tau_{4,1}\geq M_4\), this implies the two cap-free bounds

\[
a_3\leq34,
\qquad
a_7-a_3\leq35.
\]

The probe enumerated every extension of every normalized four-mark Golomb
parent inside this forced region:

```text
bounded four-mark parents:             4,934
candidate eight-mark rulers audited: 3,341,161
Golomb-extension search nodes:        37,423,576
minimum 4*tau_(4,1):                  44
minimum-threshold ruler:              (0,2,5,6,15,22,33,41)
```

Thus the actual minimum in the only possible failure region is
\(\tau_{4,1}=11\), already above the required 9.

This also closes later m=4 activations analytically.  An eight-mark
Golomb ruler has 28 distinct positive differences in
`[1,a_7]`, so N_8=a_7+1 >= 29, and therefore

\[
M_4\geq N_8/8\geq29/8.
\]

Once tau_(4,1) >= 9, the four thresholds satisfy the lower bounds

\[
9, 9+29/8, 9+2(29/8), 9+3(29/8).
\]

Their floors are at least 9,12,16,19, while the corresponding worst-case
values of S+P are only 9,11,14,18.  Before m=4 activates, the universal
four-mark result applies.  Consequently:

> **Finite theorem.** EST holds for every normalized eight-mark Golomb ruler,
> with no diameter or prefix-cap assumption.

This is a rigorously closed finite theorem, not an induction step.

## 5. Larger authenticated and transformed rulers

The Wave 6 arithmetic certificate was authenticated by file SHA-256

```text
573098370f4def5593230bdacb8f9488325eaf67b0e7949c8adb606e1e71e15d
```

and internal hash

```text
16a5e07165c767fe714f1044ae4c7c490265428e746653cfe40c385f0e9e671a.
```

The exact scorer audited:

- the 64-mark Hall counterexample;
- all six authenticated Wave 6 64-mark rulers;
- the authenticated Wave 6 128-mark ruler;
- every single adjacent-gap transposition of each authenticated 64-mark
  ruler, retaining only variants that independently re-pass Golomb uniqueness
  and every (C=1) prefix cap.

There are 23 retained swap variants, distributed `(1,1,2,6,9,4)` across the
six parents.  Mutation generation is exhaustive only inside this stated
single-swap class.  Across the 31 fixed and transformed rulers, the minimum
EST margins when at least (2,3,4,5,6,7) epochs are active are respectively

```text
0, 30, 153, 584, 2099, 36608.
```

The 64/128-point witnesses and their mutations were originally selected by
heuristic searches.  Scoring each fixed output is complete, but this is not
an exhaustive enumeration of all rulers at those sizes.

## 6. Cheap-child-half lemma and the exact overlap debt

For an active epoch, every old internal adjacent difference is at most

\[
B_m^-=\mu_m^-+2D_m^-,
\]

and every new internal adjacent difference is at most

\[
B_m^+=\mu_m^++2D_m^+.
\]

At (T=\tau_{m,1}=D_m^-+D_m^++\max(\mu_m^-,\mu_m^+)), at least one of
(B_m^-,B_m^+) is at most (T).  Otherwise, subtracting the common
discrepancy terms from the two strict reverse inequalities and adding gives

\[
\mu_m^-+\mu_m^+>2\max(\mu_m^-,\mu_m^+),
\]

which is impossible.

This promising local observation does **not** prove EST.  The certified gap
index sets are

\[
O_m=\{1,\ldots,m-1\},
\qquad
N_m=\{m+1,\ldots,2m-1\}.
\]

The (N_m) are disjoint across dyadic epochs, but the (O_m) are nested.
Moreover, (O_m) contains the smaller dyadic boundary gaps already counted
as the (k=1) atoms of (S(T)).

The 128-mark fixture makes this debt explicit.  At

\[
T=1198199/32,
\]

epochs (1,2,4,8,16,32,64) are active.  Epoch 64 is forced to use its old
half at this threshold; the earlier epochs have both choices.  The exact
figures are

```text
EST tax P(T):                         120
largest distinct cheap-adjacent union: 63
overlap among cheap halves:             57
overlap with already counted boundaries: 6
genuinely new adjacent charge:           57
total tax debt still unpaid:             63
```

Thus the local child-half lemma certifies only 57 new differences here, not
the full EST tax 120.  The exact missing statement is a **debt-repayment
lemma**: repeated old-cheap orientations must supply at least the remaining
63 unused non-adjacent differences below (T), or an equal amount of
integer-capacity slack.  Pure set matching of the adjacent halves cannot do
this because of their nesting.

## 7. What EST would and would not imply

Conditionally assume EST for an unbounded dyadic family.  Layer-cake
integration gives the exact strengthened endpoint budget

\[
\sum_{\substack{m,k\\\tau_{m,k}\leq X}}{k\over\tau_{m,k}}
+
\sum_{\substack{m\\\tau_{m,1}\leq X}}{m-1\over\tau_{m,1}}
\leq 1+\log X.
\]

So EST would add a real positive global charge.  It still would **not by
itself** imply that the first sum is (o(\log X)).  That conclusion needs the
second sum to consume ((1-o(1))\log X).  EST supplies no lower bound of that
kind.  For the critical heuristic scale
tau_(2^j,1) asymptotic to 2^j*j, its terms are only of order 1/j; through
level (J) their total is order (log J), whereas (log X) is order
(J).  This comparison is scale analysis, not an existence claim.

Therefore even a proof of EST would require a further link between its charge,
the signed reset epochs, and the innovation quantity before it could close the
hard endpoint.  The immediate rigorous next target is the finite/infinite
debt-repayment inequality identified above.

## 8. Reproducibility and scope

Owned files:

- `wave7_band_renewal_probe.py` — exact scorers, transformations, and bounded
  enumeration;
- `wave7_band_renewal_certificate.py` — deterministic certificate generator;
- `wave7_band_renewal_certificate_2026-08-28.json` — authenticated outputs;
- `test_wave7_band_renewal_probe.py` — focused regression and complete replay;
- this note.

Generate the certificate with

```text
PYTHONPATH=core_workspace/endpoint_variance \
python core_workspace/endpoint_variance/wave7_band_renewal_certificate.py
```

The committed certificate internal SHA-256 is

```text
7fdfeda650d71f4ea7cbe0771eac6b3ecf8619ec4ac69bbfc4684fc710d3a2ef.
```

Every positive result is explicitly limited to its enumerated or authenticated
finite scope.  No finite ruler here is asserted to have an infinite critical
extension.
