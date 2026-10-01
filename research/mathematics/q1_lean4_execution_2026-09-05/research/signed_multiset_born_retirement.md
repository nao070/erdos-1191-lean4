# Exact signed retirement domination, including repeated endpoints

2026-09-05. Author: /root/moment_evidence_audit, GPT-6 Astra Ultra.

**Status.** Finite analytical theorem on every actual integer Sidon
prefix: the full raw-linear retired sum at output stage j is at most
twice the full Born sum at source stage j, with no repeated-endpoint
error. An automorphism-weighted matching count extends the previously
reviewed six-distinct formula exactly. This is unformalized mathematics;
no checker execution or Lean change was made. It sharpens the signed
energy comparison but does not settle the shared physical envelope or Q1.

The parent proposed this extension. This note independently derives
the orbit count and all clock cases. The linear-causal agent separately
checked several actual repeated-endpoint examples by hand. The reviewed
`signed_retirement_fibers.md` is preserved without alteration.

## 1. Fixed conventions and the canonical triple collision

Let `P_N={a_1<...<a_N}` be Sidon, including repeated two-sums.
Use the permanent feature `g(d)=d` on

~~~
Fhat_N=(Delta P_N) union (-(Delta P_N)),
H_N=a_N-a_1,       Q_N=|Fhat_N|=N(N-1).
~~~

Each nonzero signed label has a unique ordered pair of actual endpoints.
A used record is an unordered pair of distinct signed sources `{d,e}`
whose positive output `t=|d-e|` belongs to `Delta P_N`. Put
`b=max(tau(d),tau(e))` and `r=tau(t)`. The record is Born when
`r<=b` and retired when `r>b`. Same-birth sources are included.
Its raw contribution is `de`. Throughout,

~~~
B_j = sum of all Born records with source clock b=j,
R_j = sum of all retired records with output clock r=j.    (1)
~~~

Every used record lies in one canonical numeric Schur group
`x+y=z`, `0<x<=y`. Its three positive labels recover their unique
physical endpoint edges. Orient these edges to represent
`x+y-z=0`; the three positive endpoint slots form a multiset U and
the three negative endpoint slots form V. Then `sum U=sum V`.
Changing the zero-sum orientation merely interchanges U and V.
Thus every entire numeric group has one unordered pair of triple
multisets, even when it has repeated labels or endpoints.

If `U!=V`, their supports are disjoint. Indeed, a shared endpoint
could be canceled, and Sidon uniqueness of repeated two-sums would
then force the remaining multisets to coincide. This also forces
`U=V`, a contradiction.

Suppose the group has a retired record. Orient its sources as
`d=A-B>e=C-D` and its output as `d-e=n-m`. Then

~~~
                      A+D+m=B+C+n.                     (2)
~~~

All four source endpoints and m precede n. Consequently the newest
endpoint n occurs exactly once among these six slots, and the
corresponding U,V are distinct. This condition is intrinsic to the
whole numeric group. Conversely, if distinct disjoint U,V have their
newest endpoint n exactly once, place it in V. Every matching has
exactly one edge incident to n; its magnitude is the unique latest
label. This is the class to which the exact formulas below apply.

Groups with `U=V`, or with the newest endpoint repeated, have no
retirement by (2). All their records are Born. They will be retained
as a nonnegative remainder, not discarded as an error.

## 2. Labeled matchings and the exact stabilizer factor

Fix distinct disjoint equal-sum triple multisets U,V. Give all three
slots in each multiset distinct auxiliary labels, even when their point
values agree. There are exactly six bijections between these labeled
slot sets. A bijection gives a multiset of three oriented physical edges
from U to V, and their signed differences sum to zero. Since the
supports are disjoint, none of these differences is zero.

Define

~~~
aut(U)=product_u (multiplicity of u in U)!,
aut(V)=product_v (multiplicity of v in V)!,
A=aut(U)aut(V).
~~~

For a fixed physical matching pattern let `c_(u,v)` be the number of
copies of the edge `(u,v)`. Its number of labeled realizations is

~~~
                  A / product_(u,v) c_(u,v)!.           (3)
~~~

To see this directly, distribute the labeled U-slots of each value
among their prescribed V-values, giving
`product_u m_u! / product_(u,v)c_(u,v)!`; then assign the labeled
V-slots within each value, giving `product_v m_v!`.

Positive-difference uniqueness implies that equal edge magnitudes are
the same physical edge. Because U and V have disjoint supports, its
orientation cannot reverse in another slot of this matching. Therefore
the three magnitudes are either all distinct, or exactly two copies of
one edge occur. Three copies of one edge would have a nonzero sum and
are impossible. These cases give, respectively,

~~~
distinct numeric Schur labels:  multiplicity of pattern = A;
doubled relation x+x=2x:        multiplicity of pattern = A/2. (4)
~~~

Each physical pattern gives exactly one numeric Schur group. Different
patterns cannot give the same group: its label magnitudes recover its
three physical edges, including repetitions, and their orientation is
fixed by membership in the disjoint supports U and V. Conversely all
groups belonging to this collision arise this way. This proves the
required exhaustion and prevents duplication between collisions.

The distinct-label formal list has six unordered source-pair entries:

| Output | Two formal source-pair entries | Raw sum |
|---|---|---:|
| x | `{y,z}`, `{-z,-y}` | `2yz` |
| y | `{x,z}`, `{-z,-x}` | `2xz` |
| z | `{-x,y}`, `{-y,x}` | `-2xy` |

For `x=y`, this formal list contains each of the three actual pairs
`{x,2x}`, `{-2x,-x}`, `{-x,x}` exactly twice. It preserves the
Born/retired classification of each copy, since the underlying labels
and clocks are identical. Thus its formal B and R sums are twice the
actual sums. Combining this factor 2 with the matching multiplicity
`A/2` in (4) proves the exact rule

~~~
actual sum over groups in the collision
 = (sum over the six labeled matchings of formal sums) / A.  (5)
~~~

This rule applies separately to Born sums and retired sums. Dividing
by A alone without retaining the duplicated formal six-entry list
would be wrong in the doubled-label case.

## 3. Exact multiset formulas and domination

Assume n is the newest endpoint and occurs exactly once in V.
Write `V={x,y,n}` as a multiset and let s be the common triple sum.
Here endpoint letters x,y are point values, not the Schur magnitudes
used in Section 2. For one chosen slot `m in U`, write the two
remaining slots as u,v. Repeated point values are permitted.

There are two labeled matchings that pair n to this slot m. The formal
retired pairs supplied by those matchings are

~~~
{u-x,y-v},      {v-y,x-u},
{u-y,x-v},      {v-x,y-u}.
~~~

Their raw sum is
`2[(u+v)(x+y)-2uv-2xy]`. It is a formal sum: duplicate entries
are deliberately retained. Summing over the three slots m uses only
polynomial identities, so the six-distinct calculation remains valid
with multiplicities.

Set

~~~
c=n-s/3,
sigma_U^2=sum_(u in U, with multiplicity)(u-s/3)^2,
sigma_V^2=sum_(v in V, with multiplicity)(v-s/3)^2.
~~~

For each labeled matching its latest label has magnitude `n-m`.
Its formal Born sum is `2(n-m)^2`, whether that latest label is
the numerically smallest, middle or largest magnitude. In the doubled
case the repeated edge is old, so the unique latest label is `2x`;
the formal Born sum is `8x^2`, exactly twice the actual `4x^2`.
There are two labeled matchings for each slot m. Applying (5) gives

~~~
B(U,V) = 4 sum_(m in U, with multiplicity)(n-m)^2 / A
       = (4sigma_U^2+12c^2)/A,
R(U,V) = (2sigma_U^2+6sigma_V^2-12c^2)/A,
B(U,V)+R(U,V) = 6(sigma_U^2+sigma_V^2)/A.              (6)
~~~

Every Born record in this collision has source clock `rank(n)`;
every retired record has output clock `rank(n)`. The formulas have
not equated retired source clocks with this common clock.

Since n is the maximum of the multiset V, `c>0`. The other centered
values X,Y satisfy `X+Y=-c` and `X,Y<=c`. Hence
`-2c<=X,Y<=c`, which implies `sigma_V^2=X^2+Y^2+c^2<=6c^2`.
Multiplicity does not change this elementary inequality. Therefore

~~~
2B(U,V)-R(U,V)
 =6[sigma_U^2+6c^2-sigma_V^2]/A >=0.                  (7)
~~~

All repetitions have been included exactly. There is no exceptional
triple count and no absolute-value error in (7).

## 4. Born-only cases and the exact stage inequality

In a group with no retired records all its used records are Born.
For distinct Schur magnitudes their full raw sum is
`2(x^2+xy+y^2)>0`. For `x+x=2x` the three actual records have
total `3x^2>0`. Every Born record of any complete group has later
source clock equal to the maximum of its label clocks. Thus the
Born-only remainder at each source stage is nonnegative.

At stage j, partition all groups into collisions in (6) with newest
endpoint `a_j`, and the Born-only remainder. This gives exactly

~~~
B_j = sum_(active collisions with newest a_j) B(U,V) + B_j^0,
R_j = sum_(active collisions with newest a_j) R(U,V),
B_j^0>=0,
                         R_j<=2B_j.                   (8)
~~~

Both sides of (8) may involve many collisions. Its proof groups whole
numeric Schur groups, rather than selecting positive individual terms.
It is valid for every finite actual history, with all clock ties and
automatic configurations included.

For any nonnegative stage prices `omega_j`, with no monotonicity
assumption, (8) yields

~~~
sum_(j=2)^N omega_j R_j <= 2sum_(j=2)^N omega_j B_j.   (9)
~~~

The retirement price is the output-stage price. Pricing retirement at
its source stage instead gives a false statement, as the source-price
counterexample in `signed_retirement_fibers.md` already proves.

## 5. Exact signed-energy and Abel consequences

Write `B_(<=N)=sum_(j<=N)B_j`, `R_(<=N)=sum_(j<=N)R_j`, and

~~~
Z_N=sum_(d in Fhat_N)d^2,
E_N=sum_x [sum_(a in P_N)g_(Fhat_N)(x-a)]^2.
~~~

The full signed convolution expansion counts the diagonal `N Z_N`
and twice every used unordered signed pair. Thus

~~~
E_N=N Z_N+2B_(<=N)+2R_(<=N)
   <=N Z_N+6B_(<=N),
B_(<=N)>=(E_N-N Z_N)/6
         >=E_N/6-N^3H_N^2/6.                          (10)
~~~

For an exact increment, put `v_j=Z_j-Z_(j-1)`. Subtracting the full
signed identity at two consecutive prefixes gives

~~~
E_j-E_(j-1)=Dhat_j+2B_j+2R_j,
Dhat_j=Z_(j-1)+j v_j,
B_j>=[E_j-E_(j-1)-Dhat_j]/6.                          (11)
~~~

This derives the signed diagonal directly; it is not the previous
positive-bank diagonal. Multiplying by nonnegative prices gives

~~~
sum_(j=2)^N omega_j B_j
 >=[sum_(j=2)^N omega_j(E_j-E_(j-1))
                       -sum_(j=2)^N omega_j Dhat_j]/6. (12)
~~~

For the canonical prices `omega_j=1/(Q_j^2H_j^2)`, one has
`Z_(j-1)<=Q_(j-1)H_j^2` and `v_j<=2(j-1)H_j^2`, whence

~~~
omega_j Dhat_j <=2/j^2+1/[j(j-1)],
sum_(j>=2)omega_j Dhat_j <=2zeta(2)-1.                 (13)
~~~

There is no repeated-endpoint correction in (10)--(13). These
identities and inequalities can sharpen the separately proved
good-epoch and Abel estimates. They do not supply a physical-envelope
baseline margin, and no asymptotic closure is asserted here.

## 6. Manual checks of the orbit normalization

These are exact hand calculations, not new execution evidence.

For `P_3={0,1,3}`, let `U={1,1,1}`, `V={0,0,3}`. Here
`A=6*2=12`, `sigma_U^2=0`, `sigma_V^2=6`, and `c=2`.
All six labeled matchings give the same doubled group `1+1=2`.
Their multiplicity is `A/2=6`, so (5) yields
`B=4`, `R=-1`, in agreement with the three actual pairs.
The automatic group `1+2=3` is wholly Born and has total 14.
The full history therefore has Born 18 and retirement -1.

For `P_4={0,2,5,9}`, the six positive differences
`{2,3,4,5,7,9}` are distinct. Take `U={2,2,5}`, `V={0,0,9}`.
Then `A=4`, `sigma_U^2=6`, `sigma_V^2=54`, `c=6`.
Its two physical matching patterns give

| Numeric group | Labeled multiplicity | Actual B | Actual R |
|---|---:|---:|---:|
| `2+5=7` | 4 | 98 | -20 |
| `2+2=4` | 2 | 16 | -4 |

Thus `(B,R)=(114,-24)`, exactly (6). This single collision includes
both stabilizer sizes and makes the distinction in (4) visible.

The repeated fiber of the previously recorded six-point fixture also
checks the nondoubled case. For `P_6={0,13,29,35,37,40}`, take
`U={0,29,37}`, `V={13,13,40}`. Then `A=2`,
`sigma_U^2=758`, `sigma_V^2=486`, `c=18`. Its three distinct
numeric groups are `16+24=40`, `11+13=24`, `3+13=16`, with
`(B,R)` respectively `(3200,-768)`, `(242,624)`, `(18,416)`.
Their totals are `(3460,272)`, exactly (6). The older fixed checker
recorded retirement 272; it did not test this new Born/orbit theorem.

## 7. The coefficient is sharp for an individual collision

For every integer `t>=3`, the four-point set

~~~
P(t)={-2t+1,0,t-1,t}
~~~

is Sidon: its six positive differences are the distinct numbers
`1,t-1,t,2t-1,3t-2,3t-1`. Take
`U={0,0,0}`, `V={-2t+1,t-1,t}`. This collision has `A=6`
and its sole numeric Schur group is `(t-1)+t=2t-1`, whose unique
latest label is t. Directly, or from (6),

~~~
B(U,V)=2t^2,
R(U,V)=2(t-1)(2t-1),
R(U,V)/B(U,V)=2-3/t+1/t^2 -> 2.                       (14)
~~~

Consequently the coefficient 2 in the collision inequality cannot be
uniformly decreased. Extra Born-only groups may improve a full-stage
comparison; (14) makes no optimality claim about all of B_j. This is
a parameterized family of finite fixtures, not one cap-preserving
infinite history.

The parent also supplied a family showing sharpness within the
six-distinct class itself. For integer `L>=10`, set

~~~
P={0,2L-1,2L,2L+2,3L-2,3L+3},
U={2L-1,2L,2L+2},       V={0,3L-2,3L+3}.
~~~

The fifteen positive differences are exactly the four separated groups

~~~
{1,2,3,5},
L+{-4,-2,-1,1,3,4},
{2L-1,2L,2L+2},
{3L-2,3L+3}.
~~~

They are distinct for `L>=10`, proving Sidon. The common triple sum
is `6L+1`; direct centering gives

~~~
sigma_U^2=14/3,
c=L+8/3,
sigma_V^2=6L^2+2L+38/3.
~~~

Thus the unweighted six-distinct collision has

~~~
B=12L^2+64L+104,
R=24L^2-52L,
2B-R=180L+208,       R/B -> 2.                       (15)
~~~

These symbolic calculations independently verify the parent's family;
no numerical sweep was run. The same limitations apply: this proves
sharpness per collision, including the six-distinct core, without a
claim about full-stage optimality or an infinite capped history.
