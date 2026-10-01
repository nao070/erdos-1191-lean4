# Independent review of exact multiset retirement domination

Date: 2026-09-05. Reviewer: `/root/linear_causal_sign`, GPT-6 Astra Ultra.

**Verdict:** mathematical PASS for the full source
`signed_multiset_born_retirement.md`, including the orbit factors,
the doubled-label case, the exhaustive stage partition, all constants
in (10)--(13), and both sharpness families. No material correction is
requested. The exact raw-linear inequality is

```
R_j <= 2B_j,
```

where R_j uses retirement **output** stage j and B_j uses Born
**source** stage j. The repeated-endpoint error in the earlier
supporting estimate is unnecessary for this new theorem. No
source-clock retirement version or physical-envelope closure follows.

The complete source was read in tool chunk `af79cf`. Its final
bytes were hash-inspected at actual UTC time
`2026-09-05T10:30:51.297720+00:00`, tool chunk `9afd87`.
This review binds to the observed 14,187-byte source with SHA-256

```
324a0eb718acc0f7b5830bbd6723546e9963b457df7dc26256e5b0a1e85e8487
```

No source was edited, no numerical test or replay was run, and
no Lean verification is claimed. The earlier reviewed notes remain
unchanged and valid as weaker estimates.

## 1. The canonical collision and the newest endpoint

A numeric Schur group x+y=z fixes its three actual physical
positive-difference edges. Their zero-sum signed orientation
fixes the two triple multisets U,V up to exchange, even if
a label or endpoint repeats. Equal-sum distinct triples cannot
share an endpoint: cancelling a shared occurrence would reduce
to repeated two-sum equality and force the triples to coincide.

A retired record has the endpoint equality
`A+D+m=B+C+n`, with all source endpoints and m earlier than
n. Thus n occurs exactly once in these six slots. The two
multisets are distinct and disjoint in support. This property
is intrinsic to the whole numeric group because its three edges
are fixed.

Conversely, if distinct disjoint U,V have newest endpoint n
once, each matching has exactly one physical edge incident to
n. Its magnitude has the unique latest birth. Both other edges
are old. The matching therefore belongs to the class treated
by the source's exact formulas. A group with U=V or repeated
newest endpoint cannot have a retired record. Such groups must
remain in the Born-only remainder, as the source does.

## 2. The exact orbit factor, including its stabilizer

For a physical matching pattern with edge multiplicities c_(u,v),
first distribute the labeled U-slots among the prescribed target
values. This has

```
product_u m_u! / product_(u,v)c_(u,v)!
```

possibilities. Assigning the labeled V-slots then contributes
`product_v m_v!`. Hence the number of labeled realizations is
exactly `A/product c!`, with A=aut(U)aut(V). This is equation
(3), not an assumption that the action is free.

Sidon injectivity identifies equal absolute labels with the same
physical unordered endpoint edge. Because the two supports are
disjoint, that edge has only one orientation from U to V. The
three matched magnitudes therefore either are distinct, or have
one physical edge repeated twice. Three repetitions of the same
nonzero oriented edge cannot sum to zero.

The first case has stabilizer one and A labeled realizations.
In the second, two equal signed gaps d force the third signed
gap to be -2d. It is exactly a doubled numeric relation, with
stabilizer two and A/2 realizations. Different physical patterns
cannot give the same numeric group, because the labels recover
their physical edges, multiplicities, and the orientation fixed
by U,V. This verifies both exhaustion and uniqueness in (4).

The formal six-entry Schur list at x=y contains each actual
pair `{x,2x}`, `{-2x,-x}`, `{-x,x}` twice. Both copies have
the same classification. Therefore its formal B and R sums
are twice their actual values. For a doubled pattern,

```
(A/2 labeled realizations)*(2 times actual sum)/A
 = actual sum.
```

For a distinct-label pattern the corresponding calculation is
`A*(actual sum)/A`. Thus equation (5) is exact separately
for Born and retired sums. Dividing labeled matchings by A
without the doubled formal record multiplicity would indeed
give a wrong answer; the source retains the necessary factor.

## 3. The multiset formulas keep every occurrence

Pairing the unique n-slot with a chosen occurrence m in U
leaves two labeled matchings. Their four formal retirement
entries give
`2[(u+v)(x+y)-2uv-2xy]`, just as in the six-distinct case.
The polynomial sum over the three m occurrences therefore
remains valid when point values repeat.

The unique latest label has magnitude n-m. Its formal Born
sum is `2(n-m)^2`. In a doubled pattern the repeated edge
is old, so the latest magnitude is 2x; the formal value 8x^2
is twice the actual Born value 4x^2. Applying the exact orbit
rule gives all three identities in (6):

```
B=(4sigma_U^2+12c^2)/A,
R=(2sigma_U^2+6sigma_V^2-12c^2)/A,
B+R=6(sigma_U^2+sigma_V^2)/A.
```

All Born source clocks and retirement output clocks here
are rank(n). Retirement source clocks can be earlier and
need not be constant.

The centered coordinates of V other than c sum to -c and
are at most c. They lie in [-2c,c], so sigma_V^2<=6c^2
also with multiplicities. This proves exactly

```
2B-R=6[sigma_U^2+6c^2-sigma_V^2]/A>=0.
```

No absolute-value estimate or repeated-endpoint error has entered.

## 4. The stage partition is complete

Every group with a retirement is one of the active multiset
collisions above. At stage j these are precisely the collisions
whose newest endpoint is a_j. They supply all of R_j and
their full Born companions at source stage j.

Every other group at that latest stage is wholly Born. Its
total is `2(x^2+xy+y^2)` for distinct numeric labels, or
`3x^2` for a doubled group. These totals are nonnegative,
even though some individual source products are negative.
Thus the remainder B_j^0 in (8) is nonnegative and the
displayed decompositions count every group once. Automatic
collisions, repeated newest endpoints, and clock ties have
not been deleted.

Summing the exact collision domination proves R_j<=2B_j.
Multiplying by arbitrary nonnegative stage prices proves (9)
without a monotonicity assumption. These are output prices
on retirement. The previously checked source-clock
counterexample is unaffected.

## 5. Energy and diagonal constants

The complete signed convolution identity is
`E_N=N Z_N+2B_(<=N)+2R_(<=N)`. Applying the exact stage
bound gives `E_N<=N Z_N+6B_(<=N)` and hence (10).
The elementary Z_N<=Q_NH_N^2<=N^2H_N^2 gives its stated
final diagonal term `N^3H_N^2/6`.

Subtracting adjacent full identities gives the fresh signed
increment

```
Delta E_j=Z_(j-1)+j v_j+2B_j+2R_j.
```

The factor is j, not the positive-bank mixed-source coefficient
j-1. The stage inequality therefore proves (11)--(12) with
no additional error.

For the canonical price, the diagonal bound is

```
omega_j Dhat_j
 <=(3j-2)/[j^2(j-1)]
 =2/j^2+1/[j(j-1)].
```

Summing from j=2 gives `2(zeta(2)-1)+1=2zeta(2)-1`,
confirming (13). The source does not infer a bound on a
span-masked physical maximum from this diagonal estimate.

## 6. Independent repeated-endpoint checks

The mixed-stabilizer example `P={0,2,5,9}` was independently
checked by hand. Its six positive differences are distinct.
The collision U={2,2,5}, V={0,0,9} has A=4 and produces
the distinct-label group 2+5=7 with (B,R)=(98,-20), and
the doubled group 2+2=4 with (B,R)=(16,-4). Their labeled
multiplicities are four and two. The total (114,-24) matches
the formula and verifies the doubled correction inside a
collision that also has a free orbit.

The P_3 example U={1,1,1}, V={0,0,3} has A=12 and
six labeled realizations of the doubled group. Its actual
(B,R)=(4,-1), and the separate automatic group contributes
Born 14, giving full Born 18 and retirement -1 as stated.

The repeated fiber at sum 66 in the six-point fixture has
A=2 and three distinct numeric groups. Their respective
totals (3200,-768), (242,624), and (18,416) sum to
(3460,272). This independently matches its centered formula.
These are hand calculations, not new execution evidence.

## 7. Both sharpness families check out

For the four-point family with t>=3, the positive differences
are strictly ordered as

```
1<t-1<t<2t-1<3t-2<3t-1.
```

The set is therefore actual Sidon. Its active collision has
one numeric group `(t-1)+t=2t-1`, with clocks 3,4,2,
so the unique latest magnitude is t. This gives
`B=2t^2`, `R=2(t-1)(2t-1)`, and the ratio in (14).

For the six-distinct family, direct subtraction gives precisely
the source's fifteen labels. At L>=10 the first group ends
at 5 and the next starts at L-4>=6; its last label L+4
is less than 2L-1; and 2L+2 is less than 3L-2. Within
each group the labels are distinct. This proves Sidon for
every stated integer L, without a numerical sweep.

The common mean is `2L+1/3`. The three U offsets are
`-4/3,-1/3,5/3`, giving sigma_U^2=14/3. The V offsets
are `-2L-1/3,L-7/3,L+8/3`, giving
`sigma_V^2=6L^2+2L+38/3` and c=L+8/3. Substitution
then yields exactly

```
B=12L^2+64L+104,
R=24L^2-52L,
2B-R=180L+208.
```

The ratio tends to two. Thus coefficient two is sharp per
collision even within the six-distinct class. Both families
have fixed finite cardinality as their parameter grows.
The source correctly makes no optimality claim for an
entire stage or claim about a capped infinite history.

## 8. Accepted scope

The exact multiset count removes the repeated-endpoint error
from the raw-linear stage comparison and its energy consequence.
This is a genuine strengthening of the earlier reviewed estimate.
It does not prove the same comparison for retirement source
prices or arbitrary odd features, make retirement nonpositive,
transfer physical payments between PSD-ordered sources, or
settle the shared-envelope baseline margin. The earlier
finite examples and scope boundaries remain consistent.

Original Q1 and any signed-bank Lean formalization remain open.
