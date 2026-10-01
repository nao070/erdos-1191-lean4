# Complete signed retirement fibers and a quantitative Born comparison

2026-09-05. Author: /root/moment_evidence_audit, GPT-6 Astra Ultra.

**Status.** Finite mathematical derivation on every actual integer Sidon
prefix. The complete six-endpoint retirement sum can be positive. Its
full raw-linear Born companion nevertheless satisfies `R_6 <= 2 B_6`,
with a common latest-endpoint price. Repeated-endpoint retirement has
an explicit absolute error, including a summable output-stage version.
These statements are analytical and unformalized. They do not establish
a shared-envelope margin or original Q1. No checker was rerun.

The parent proposed the centered retirement formula and then the Born
comparison. Both are independently derived here. The linear-causal agent
also independently checked the matchings, fixture arithmetic and clock
restriction. This note concerns the permanent signed feature `g(d)=d`;
it does not import the positive-bank causal diagonal or Abel identity.

## 1. Actual labels, records and clocks

Let `P_N={a_1<...<a_N}` be Sidon including repeated two-sums. Let
`F_N=Delta P_N`, `Fhat_N=F_N union (-F_N)`, `H_N=a_N-a_1`, and
`Q_N=|Fhat_N|=N(N-1)`. A nonzero signed label has a unique ordered
pair of actual endpoints. Its birth is the rank of the larger endpoint;
`tau(-d)=tau(d)`.

Every unordered pair of distinct signed sources `{d,e}` with
`t=|d-e| in F_N` is used. Write

~~~
b=max(tau(d),tau(e)),       r=tau(t).
~~~

It is Born if `r<=b`, and retired if `r>b`. Both definitions include
same-birth sources. A record contributes the raw product `de`.
The symbols `B_N,R_N` below sum all Born and retired records,
respectively, once each. A lower-case endpoint such as `n` denotes
the point value when it occurs inside a polynomial; `rank(n)` denotes
its birth rank. Stage indices use `j` or an explicitly indexed `a_j`.

Orient a retired record as `d>e`, and recover its unique endpoints:

~~~
d=A-B,       e=C-D,       d-e=n-m>0.
~~~

All four source endpoints precede `n`, and `m<n`. Therefore

~~~
                 A+D+m = B+C+n.                         (1)
~~~

The newest endpoint `n` occurs exactly once among these six slots.
Distinct equal-sum triple multisets in a Sidon set have disjoint
supports: cancel any shared point, then repeated two-sum uniqueness
forces the remaining multisets, and hence the triples, to coincide.
The two multisets in (1) cannot coincide, because only the right one
contains `n`. Thus every retirement corresponds to a nontrivial,
disjoint-support triple collision. Repetition within either triple
is allowed at this stage.

## 2. Exactly twelve retired records per six-endpoint collision

Take disjoint three-element sets of equal sum

~~~
U={u,v,m},       V={x,y,n},       sum U=sum V=s,
~~~

where `n` is the largest of all six endpoints. Fix `m in U` and
write the other two points as `u,v`. The output `n-m` is born at
`rank(n)`. The complete source list for this output is

~~~
{u-x,y-v},      {v-y,x-u},
{u-y,x-v},      {v-x,y-u}.                              (2)
~~~

The second and fourth pairs are the negative reflections of the
first and third. For example `(u-x)-(y-v)=n-m`; this ordering is
strictly positive, even if the individual source labels are negative.
Every source endpoint lies below `n`, so every record is retired.

Conversely, (1) recovers `m` and the four remaining slots. For a fixed
unordered collision and fixed `m`, choosing which point of `U\{m}`
occupies `A` and which point of `V\{n}` occupies `B` gives precisely
the four records (2). They are distinct: each signed label determines
its ordered endpoints, and an unordered source pair determines its
larger signed source. Different `m` give different positive outputs.
There are therefore exactly twelve records, without multiplicity from
swapping the sources, swapping triple names, or changing sign.

The sum at fixed `m` is

~~~
R_m=2[(u-x)(y-v)+(u-y)(x-v)]
   =2[(u+v)(x+y)-2uv-2xy].                             (3)
~~~

Each of the four records has later-source clock equal to the maximum
rank among the four points `u,v,x,y`. This can depend on `m`; the
individual source-label births need not agree. All twelve output
clocks are `rank(n)`.

## 3. Centered pair and complete-fiber formulas

Put `c=n-s/3` and `sigma_T^2=sum_(a in T)(a-s/3)^2`.
Writing `e_2(U)` for the second elementary symmetric sum,

~~~
R(U,V)=sum_(m in U)R_m
      =4s(s-n)-4e_2(U)-12xy
      =2 sigma_U^2+6 sigma_V^2-12c^2.                  (4)
~~~

An equivalent expression is
`2 sigma_U^2+3(x-y)^2-3c^2`. Neither expression has a universal
nonpositive sign.

Fix one sum `s` and list all distinct-point triples in its fiber as
`T_1,...,T_K`, ordered by their distinct maxima `n_1<...<n_K`.
The triples are pairwise disjoint by the cancellation argument in
Section 1. Every pair `i<r` has latest endpoint `n_r`. Summing (4)
over the entire fiber gives the exact unweighted formula

~~~
R_fiber=sum_(r=1)^K [
 (2K+4r-6) sigma_(T_r)^2
 -12(r-1)(n_r-s/3)^2 ].                               (5)
~~~

If retired records are priced by arbitrary real output-stage prices
`omega_j`, the exact weighted version is

~~~
R_fiber(omega)=sum_(r=1)^K omega_(rank(n_r)) [
 2 sum_(i<r) sigma_(T_i)^2
 +6(r-1)sigma_(T_r)^2
 -12(r-1)(n_r-s/3)^2 ].                               (6)
~~~

Factoring a price from (3) is valid at either its common source clock
or common output clock. Factoring a price across (4) or a bracket in
(6) requires the common output clock; source clocks need not agree.
For example reflection of the fixture below gives the Sidon set
`{0,3,5,11,27,40}` and collision
`{5,11,27}`, `{0,3,40}`. The term with `m=27` has source birth 4,
while those with `m=5,11` have source birth 5.

## 4. Six matchings give the full Born companion

There are six bijections from `U` to `V`. Each gives three disjoint
physical endpoint edges whose signed differences sum to zero. Their
absolute labels are nonzero and pairwise distinct: repeated absolute
labels on different edges would violate Sidon uniqueness. Hence they
form one numeric Schur relation `x+y=z` with `0<x<y`.

Different bijections cannot produce the same numeric Schur triple,
because its three positive labels recover the three physical edges,
which recover the matching. Conversely any used source pair and its
output belonging to this collision recover such a matching. Thus the
six numeric Schur groups exhaust all signed used records associated
with this collision, including its Born records.

For clarity, the complete six records for one numeric relation are

| Output | Sources | Raw total |
|---|---|---:|
| x | `{y,z}`, `{-z,-y}` | `2yz` |
| y | `{x,z}`, `{-z,-x}` | `2xz` |
| z | `{-x,y}`, `{-y,x}` | `-2xy` |

Only the edge incident to `n` has the latest birth in a six-endpoint
matching. The other two labels are older, even if their births tie.
Its two output records are retired; the other four are Born. The
latest label can be numerically smallest, middle, or largest. If its
magnitude is `t`, the full Born raw total in all three cases is
`2t^2`: respectively `2xz-2xy=2x^2`,
`2yz-2xy=2y^2`, or `2xz+2yz=2z^2`.

If `n` is matched to `m in U`, then `t=n-m`. The other two edges
can be matched in two ways. Therefore all six matchings supply exactly
24 Born records and twelve retired records, and

~~~
B(U,V)=4 sum_(m in U)(n-m)^2
      =4 sigma_U^2+12c^2,
B(U,V)+R(U,V)=6(sigma_U^2+sigma_V^2).                  (7)
~~~

The Born source clock is always `rank(n)`, the same as the retired
output clock. All 36 records therefore have a common price if each
record is priced at the latest clock of its two sources and output.

Since `n` is the maximum of `V`, its centered value `c` is positive.
Writing the other centered values as `X,Y`, we have
`X+Y=-c`, `X,Y<=c`, hence `-2c<=X,Y<=c`. The maximum of
`X^2+Y^2+c^2` on this segment is `6c^2`. Consequently

~~~
sigma_V^2<=6c^2,
R(U,V)<=2 B(U,V),
B(U,V)>=(B(U,V)+R(U,V))/3.                            (8)
~~~

These inequalities survive arbitrary nonnegative common latest-clock
prices. The full fiber Born and total identities are

~~~
B_fiber=sum_r [4(K-r)sigma_(T_r)^2
                  +12(r-1)(n_r-s/3)^2],
B_fiber+R_fiber=6(K-1)sum_r sigma_(T_r)^2,             (9)

B_fiber(omega)=sum_r omega_(rank(n_r)) [
 4sum_(i<r)sigma_(T_i)^2+12(r-1)(n_r-s/3)^2],
B_fiber(omega)+R_fiber(omega)
 =6sum_r omega_(rank(n_r)) [
       sum_(i<r)sigma_(T_i)^2+(r-1)sigma_(T_r)^2].      (10)
~~~

No analogue of (8) with retirement source-clock prices is asserted.
The fixture in Section 7 actually disproves that analogue.

## 5. An explicit absolute repeated-endpoint error

A triple multiset with repetition has the form `{a,a,b}`. There are
at most `N^2` such multisets, including `{a,a,a}`. Distinct triples
in any one equal-sum fiber have disjoint supports, so there are at
most `N` representations in that fiber. Every non-six retirement has
at least one repeated triple, because its two triple supports are
disjoint. Therefore at most `N^3` unordered triple collisions can
contribute non-six retirement. This is an upper count and may count
one collision twice.

At the slot level each collision has at most six endpoint matchings.
A matching supplies at most two retired signed pairs. Repeated labels
can only reduce this count: for a doubled numeric relation `x+x=2x`
there are three signed pairs in the full group, and at most one is
retired. Matches with zero edges supply no nonzero-label record.
Automatic collisions with identical triple multisets cannot retire,
by the unique latest endpoint argument in Section 1. It follows that

~~~
number of non-six retired records <=12N^3,
sum_(non-six retired {d,e}) |de| <=12N^3 H_N^2.        (11)
~~~

This bounds the sum of absolute products, not merely their signed sum.

There is a stronger stage estimate. At output birth `j`, the newest
endpoint is `a_j`. Its new triple `V` contains `a_j` exactly once.
If `V` has three distinct points, its old partner `U` must repeat;
there are at most `(j-1)^2` possible old repeated triples, and at most
one new `V` at the prescribed sum, since any two new representations
would share `a_j`. If `V` repeats, it has the form `{a,a,a_j}` with
`a<a_j`, giving at most `j-1` choices, each with at most `j-1` old
partners. Hence

~~~
sum_(non-six retired, r=j) |de|
                      <=24(j-1)^2 H_j^2.              (12)
~~~

In particular, with `omega_j=1/(Q_j^2 H_j^2)`,

~~~
sum_(non-six retired, r=j) omega_j |de| <=24/j^2,
sum_(j>=2)sum_(non-six retired, r=j) omega_j |de|
                      <=24(zeta(2)-1).                (13)
~~~

No cap, density hypothesis, monotonicity, or cancellation enters this
absolute summability assertion. It specifically uses output clocks.

## 6. Closure of the complement and a global finite consequence

The six-endpoint property is constant over an entire numeric Schur
group: its three physical magnitude-label edges are fixed, and the
zero-sum orientation fixes the two triple multisets up to interchange.
Thus deleting the six-endpoint groups leaves complete Schur groups,
including doubled-label and clock-tie cases. Their raw full Born sums
are nonnegative, as follows directly from the table in Section 4 and
the doubled-label list `{x,2x}`, `{-2x,-x}`, `{-x,x}`. When the
latest clock is tied, all six records are Born and their total is
`2(x^2+xy+y^2)>0`; for the doubled case the Born total is either
`4x^2` or `3x^2`. In every group all Born records have the same
latest source clock. Nonnegative prices preserve this fact.

Consequently `B_N>=B_6>=0`, and (8), (11) give

~~~
                   R_N<=2B_N+12N^3 H_N^2.             (14)
~~~

More precisely, if `B_j` denotes all Born records at source stage j
and `R_j` all retired records at output stage j, then

~~~
R_j<=2B_j+24(j-1)^2H_j^2,
sum_(j=2)^N omega_j R_j
 <=2sum_(j=2)^N omega_j B_j
                  +24sum_(j=2)^N 1/j^2               (15)
~~~

for the prices in (13). Here (8) is applied to complete six-endpoint
groups with latest endpoint `a_j`, and the non-six Born remainder at
that source stage is nonnegative. The first line is unweighted; the
second uses exactly the displayed normalization.

One fresh full signed convolution identity supplies a quantitative
energy consequence. Extend `g(d)=d` by zero outside `Fhat_N` and set

~~~
E_N=sum_x [sum_(a in P_N)g(x-a)]^2,
S_N=sum_(d in Fhat_N)d^2.
~~~

Expanding the square gives `N S_N` from equal smoothing points.
Every distinct point difference occurs exactly once in the actual
Sidon prefix. Its off-diagonal terms are precisely twice the sum of
all used unordered signed pairs. Therefore

~~~
E_N=N S_N+2B_N+2R_N,
B_N>=E_N/6-N S_N/6-4N^3H_N^2
   >=E_N/6-(25/6)N^3H_N^2.                            (16)
~~~

The last step uses `S_N<=Q_NH_N^2<=N^2H_N^2`. This is a new
signed-bank finite identity and inequality. The separate note
`signed_born_quantitative_gain.md` treats the good-epoch energy scale
and its weighted consequences. No unproved positive-bank increment
formula is needed for (16).

## 7. An actual positive retirement fiber and the source-clock failure

The actual Sidon set

~~~
P_6={0,13,29,35,37,40}
~~~

has positive differences
`{2,3,5,6,8,11,13,16,22,24,27,29,35,37,40}`, all distinct.
Its sole pair of distinct-point equal-sum triples is

~~~
U={13,29,35},       V={0,37,40},       s=77.
~~~

The twelve records in (2) are grouped as follows; `plus/minus` means
the displayed pair and its negative reflection.

| m | Two pairs, each with its negative reflection | Raw sum |
|---|---|---:|
| 13 | `{29,2}`, `{-8,-35}` | 676 |
| 29 | `{13,2}`, `{-24,-35}` | 1732 |
| 35 | `{13,8}`, `{-24,-29}` | 1600 |

Thus `R_6=4008>0`, while `B_6=4(27^2+11^2+5^2)=3500` and
`B_6+R_6=7508`. All retired core source births are 5 and output
births are 6; all core Born source births are 6. With the nonnegative
source-stage prices `beta_j=Q_j^-2`, the incorrectly source-priced
comparison fails numerically:

~~~
beta_5 R_6-2 beta_6 B_6
 =4008/400-7000/900=1009/450>0.                        (17)
~~~

This finite fact is consistent with (8) and (15), whose retired
price is the output-stage price.

The fixture has a stronger geometric feature: writing
`V={x,y,n}`, it satisfies `x<min U<=max U<y<n`. Under this ordering,
for each `m`, both unreflected product types are positive for every
odd feature `h` that is strictly positive on the used positive
magnitudes. They are

~~~
h(u-x)h(y-v)>0,
h(u-y)h(x-v)=h(y-u)h(v-x)>0.                          (18)
~~~

Their negative reflections have the same products. Thus this is also
a positive six-endpoint retirement core for that whole odd-positive
family. It does not extend the quantitative raw-linear inequality
(8) to arbitrary odd features, and it does not refute an asymptotic
retirement bound with finite error, a cap-sensitive estimate, or a
shared-envelope margin.

## 8. Saved finite evidence and its scope

The parent supplied the already executed, fixed-input files
`research/evidence/signed_retirement_six_fixed.py`, `.txt`,
`.stderr.txt`, and `.run.json`. This audit read their contents and
current hashes without executing the checker. The recorded instrumented
run used Python 3.14, observed return code 0, and ran from
`2026-09-05T10:01:10.786300+00:00` to
`2026-09-05T10:01:10.819199+00:00`. Its source before/after hashes
agree, and its captured complete stdout equals the saved stdout.

The checker verifies repeated-two-sum Sidon, directly enumerates every
retired pair, separates six-distinct records, and compares each distinct
triple collision's complete sum with (4). It records twelve core pairs,
their clocks, `R_6=4008`, repeated retirement 272, and total retirement
4280. It has no Born enumeration or assertions for (7)--(16); those are
proved analytically above. One fixed run does not prove the general
theorem. The executable's own binary hash was not recorded.

Recorded source SHA-256:
`0d1ae2c7ac01fdd1bda4a53ede78c612aeef2a767ea97f1e1e1a07b2da0c1177`.
Recorded stdout SHA-256:
`01fa47494c38b1e014c0eb131fce29ed689989ebe7c817122e1947df650fffd8`.
The saved stderr is empty, SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
