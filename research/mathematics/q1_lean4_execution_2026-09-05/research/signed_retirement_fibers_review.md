# Independent review of complete signed retirement fibers

Date: 2026-09-05. Reviewer: `/root/linear_causal_sign`, GPT-6 Astra Ultra.

Source: `signed_retirement_fibers.md`, authored by
`/root/moment_evidence_audit`.

**Verdict:** mathematical PASS within the stated scopes. The complete
record partition, all complete-fiber identities, Born companion,
repeated-endpoint bounds and stage constants, complement closure,
energy consequence, and exact six-point counterexample are supported.
No material correction was requested. The author resolved one wording
ambiguity by distinguishing a record's later-source clock from the
births of its individual labels.

The complete pre-clarification source was read in tool chunk `e814f5`.
After the author confirmed the sole wording update, the revised passage
and actual source hash were read in tool chunk `c59de7`, at UTC
`2026-09-05T10:18:25.184388+00:00`. This review binds to final SHA-256

```
af256edc1cd1812a9069823b906f89328de6fb85aec6e087a7ff6a4a851cc8c9
```

This was an independent mathematical and read-only source review.
No checker was run or rerun, no source file was edited by this
reviewer, and no Lean verification is claimed.

## 1. Recovery of all retirement records and their multiplicity

Orient a retired pair by d>e and write its unique signed endpoints
as `d=A-B`, `e=C-D`. Its output is `n-m`, where n is newer than
all four source endpoints and m<n. Thus the equality
`A+D+m=B+C+n` has n in precisely one slot. The two triple
multisets cannot coincide. If they shared any point, cancelling
it and applying repeated two-sum uniqueness would force them to
coincide. Hence their supports are disjoint, with repetitions
allowed only inside one side.

For distinct triples `U={u,v,m}`, `V={x,y,n}`, the four source
pairs at output n-m are exactly

```
{u-x,y-v}, {v-y,x-u}, {u-y,x-v}, {v-x,y-u}.
```

The two pairs of negative reflections have equal products. Every
source label has a unique ordered endpoint pair. Combined with
the unique larger signed source in an unordered pair, this proves
that the four records are distinct. The three choices of m give
different outputs, so the total is exactly twelve. These records
are all retired, including any equal-birth sources.

Their common later-source clock for a fixed m is the maximum
rank of u,v,x,y, which may change with m. All twelve retirement
output clocks are rank(n). The final source's clarified wording
states this correctly and does not equate individual label births.

Expanding the products gives exactly

```
R_m=2[(u+v)(x+y)-2uv-2xy].
```

Summing over m and using equal sum s yields
`R=4s(s-n)-4e_2(U)-12xy`. Substituting the centered square
sums verifies both equivalent centered forms in equation (4).

## 2. Complete fibers and the exhaustive Born companion

In a complete fixed-sum fiber, distinct triples have disjoint
supports and hence different maxima. In the unweighted retirement
sum, the variance of triple T_r receives coefficient 2 from
each of its K-r later partners and coefficient 6 from each of
its r-1 earlier partners. Their sum is `2K+4r-6`, proving (5).
Keeping each later maximum's price instead gives exactly (6),
for arbitrary real prices as an identity.

Each of the six bijections U to V consists of three disjoint
physical endpoint edges. Orient them from one triple to the other;
their signed differences sum to zero. Their absolute labels are
nonzero and distinct: repeated magnitudes would identify two
different endpoint pairs, violating Sidon difference uniqueness.
The labels therefore form a numeric Schur triple with unequal
summands. Different bijections give different numeric Schur
triples because the positive labels recover the physical edges
and therefore the matching.

This argument rules out both duplicate groups and a missed
doubled-label degeneracy in the six-distinct core. The six groups
exhaust all used records of that collision. Exactly one label in
each group is born at n, namely the edge incident to n. Each
group consequently has two retired records and four Born records.
The entire collision has twelve retired and 24 Born records.

If n is matched to m, its magnitude is n-m. Regardless of whether
that label is numerically smallest, middle, or largest, its
Schur group's full raw Born sum is `2(n-m)^2`. There are two
matchings for each m. Therefore

```
B=4sum_(m in U)(n-m)^2=4sigma_U^2+12c^2,
B+R=6(sigma_U^2+sigma_V^2),  c=n-s/3.
```

Since the other centered V coordinates sum to -c and are at most
c, their squared sum together with c^2 is at most 6c^2. Thus

```
2B-R=6[sigma_U^2+6c^2-sigma_V^2] >= 0.
```

This verifies (7)--(8). The prices must be nonnegative for the
inequality. The common clock is the Born source clock and the
retirement **output** clock, both rank(n).

Summing B over the fiber gives coefficient `4(K-r)` on each
old-triple variance and `12(r-1)` on its maximum square. Adding
the retirement formula cancels those maximum-square terms and
leaves `6(K-1)` on every variance. This proves (9). Keeping
the price of each later maximum yields the two exact sums in
(10). No source-clock replacement is used.

## 3. Repeated endpoints: absolute and stage bounds

There are at most N^2 repeated triple multisets `{a,a,b}`.
Every fixed-sum fiber contains at most N distinct representations,
because their supports are disjoint. A non-six retirement must
have a repeated triple on at least one side. Hence the count of
candidate collisions is at most N^3, allowing harmless double
counting when both sides repeat.

At most six slot matchings describe one such collision, and each
has at most two retired signed pairs. Repeated slots can cause
overcounting or doubled labels; they cannot increase the bound.
A doubled numeric relation has at most one retired pair. Thus
the total number of non-six retired records is at most 12N^3.
Bounding each absolute product by H_N^2 proves (11), as an
absolute-product bound.

At output birth j, the newest endpoint a_j occurs once. The two
cases used for (12) exhaust the non-six possibilities:

* If the new triple is distinct, its old partner repeats. There
  are at most `(j-1)^2` such old triples, each permitting at most
  one new representation at that sum, by the shared-a_j
  cancellation argument.
* If the new triple repeats, it is `{a,a,a_j}` with a<a_j.
  There are j-1 choices and at most j-1 old partners per sum.

This gives at most `2(j-1)^2` collisions. Equivalently, each
collision has at most three choices of an old endpoint occurrence
matched to a_j, two matchings of the remaining slots, and two
signed reflections. The factor twelve remains valid when some
occurrences describe the same physical record. Therefore

```
sum_(non-six, output birth j)|de| <=24(j-1)^2 H_j^2.
```

Multiplication by `1/(Q_j^2 H_j^2)` cancels both H_j^2 and
(j-1)^2, leaving exactly `24/j^2`. This proves (12)--(13),
including absolute summability without a cap assumption. The
argument is specifically indexed by output birth.

## 4. Complement closure and the global consequences

The three physical edges of a numeric Schur group are fixed.
Their zero-sum orientation fixes the two endpoint triple
multisets up to exchange. Thus the six-distinct property belongs
to an entire numeric group, not merely to selected source pairs.
Deleting the complete six-distinct groups leaves complete numeric
Schur groups. Their full raw Born sums are nonnegative in every
latest-clock and doubled-label case.

The non-six Born remainder is therefore nonnegative, also after
nonnegative source-stage weighting. This justifies replacing the
core Born sum by the full Born sum in (14)--(15). In particular
the stage inequality has retirement output j on its left and
Born source stage j on its right. The absolute repeated error is
then the one already proved; no extra record is omitted.

The full convolution expansion is
`E_N=N S_N+2B_N+2R_N`. Combining it with
`R_N<=2B_N+12N^3H_N^2` gives

```
B_N>=E_N/6-N S_N/6-4N^3H_N^2.
```

Since S_N<=Q_N H_N^2<=N^2H_N^2, the final coefficient is
`4+1/6=25/6`, confirming (16). This is a new full signed
identity; the positive-bank mixed-source diagonal has not been
used.

## 5. Independent arithmetic for the actual fixture

The fifteen positive differences of
`{0,13,29,35,37,40}` are exactly the distinct values listed in
the source. Directly listing the twenty distinct-point triple
sums gives

```
42,48,50,53,64,66,69,72,75,77,
77,79,82,85,88,90,101,104,106,112.
```

Thus 77 is the sole distinct-point triple collision. For that
collision the four-pair sums at m=13,29,35 are respectively
676, 1732, and 1600, totaling R_6=4008. The Born companion is
`4(27^2+11^2+5^2)=3500`, so B_6+R_6=7508 and R_6>B_6.

Every core retired pair has source birth 5 and output birth 6.
Every core Born pair has source birth 6. Therefore the source-
clock replacement really fails for beta_j=Q_j^-2:

```
beta_5 R_6-2beta_6 B_6
 =501/50-70/9=1009/450 > 0.
```

This is consistent with the correctly output-priced theorem.
The geometric ordering `0<U<37<40` makes both unreflected
product types same-sign for every m. Their products and their
reflections are strictly positive for any odd feature that is
strictly positive on these positive magnitudes. That observation
does not extend the quantitative raw-linear factor-two theorem
to arbitrary features.

As an additional arithmetic check, the full retirement products
on outputs 3,5,11,27,40 are respectively
416,1600,2356,676,-768. Their total is 4280, with non-six
remainder 272. These values were checked directly from the old
positive labels; no program was executed for this review.

The saved instrumented run record was read in tool chunk `88979a`.
It records the same twelve core pairs, clocks, core and full totals,
return code zero, and captured complete stdout/stderr. Reading
that record is not a fresh execution. Its fixed check does not
assert the general Born companion, complete-fiber, or error
inequalities; those are supported by the analytical arguments
above. No larger sign or asymptotic claim follows from the fixture.

## 6. Scope of the accepted result

The positive retirement core disproves unqualified nonpositivity,
while the matching identity supplies a valid quantitative Born
comparison with the correct shared clock. The stage error is
absolutely summable under the displayed output-clock weights.
These are genuine finite and weighted supporting estimates.

They do not give a source-clock retirement comparison, a
nonpositive retirement kernel, a payment transfer between
different PSD sources, or a bound on the shared physical-envelope
margin. The separate quantitative Born analysis must retain those
distinctions. Original Q1 and signed-bank Lean formalization
remain unresolved.
