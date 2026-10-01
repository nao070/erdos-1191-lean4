# Common-clock Schur pairs and their exact mean-defect energy

2026-09-05. `/root/causal_telescoping`, GPT-6 Astra Ultra.

**Status.** Exact common-clock and paired-core identities for actual
numeric Schur triples. The earlier core can be made closed under Schur
pairing at uniformly bounded cost. A nonnegative square, its explicit
mean-defect subtraction, and a separate squared-coefficient transport
identity are derived. Their remaining costs have an actual logarithmic
upper bound, but not the required finite or subcritical bound. No Lean
declaration, numerical run, arbitrary-gap sign claim, or Q1 conclusion
is made.

The complete `three_clock_separation.md` was read. Its common-price
and symmetric separation statements are used together with the tail
proofs in `clock_core_localization.md`, `near_retirement_incidence.md`,
and `late_retirement_tail.md`. The present numeric pairing is not the
high-resource/low-resource endpoint injection of earlier notes.

## 1. One Schur triple, two records, one horizon and one price

Keep one actual increasing integer Sidon history, its difference
banks `F_n`, actual label birth `tau`, and permanent raw coefficients

```
g_(a_j-a_i)=m_j-a_i,
m_j=mean(a_1,...,a_(j-1)),
h_j=a_j-m_j,
g_d=d-h_(tau(d)),
w_n=1/(q_n^2 H_n^2),
q_n=binom(n,2),    H_n=a_n-a_1.
```

Take the canonical numeric Schur triple

```
0<x<y,   z=x+y,   x,y,z in F_infinity,
p_x=tau(x), p_y=tau(y), p_z=tau(z),
M=max(p_x,p_y,p_z).
```

In this note the three birth clocks are pairwise distinct. There
are exactly two relevant mixed source records:

```
P_x={x,z}, output y;     P_y={y,z}, output x.       (1)
```

Both source pairs have distinct births. Both records have the
same actual price `w_M`: a Born record is priced at its latest
source birth, and a retired one at its later output birth. These
are equal to `M` in the respective cases.

The finite horizon agrees as well. In the existing `B_T,R_T`,
a Born record appears by its source birth and a retirement by its
output birth. Each of (1) has therefore appeared if and only if
`M<=T`. No extra future record is included by pairing at horizon
`T`. This assertion uses all three actual label births, not just
the birth of the numeric largest label `z`.

The separation condition of `three_clock_separation.md` is symmetric
in the three labels and clocks. It thus keeps or discards both
records together. The repeated-label and repeated-clock cases were
already removed there at finite absolute cost.

## 2. Close an asymmetric earlier core under this pairing

The older source/output restrictions are not all symmetric. For
example, when `p_z=M`, the two records have the same source scale
but numeric outputs `y` and `x`. A cutoff lying between `x` and
`y` could discard just one record. One must not then use a two-record
identity for the surviving record alone.

The existing tail proofs give a stronger majorant that resolves
this issue. Define a record's proxy price

```
pi(P)=1/q_M^2.
```

Both siblings in (1) have exactly the same proxy, and each actual
absolute contribution is at most that proxy. For every omitted
predicate proved in the cited notes, its proxy sum is finite too.
This follows from their actual counting proofs, as follows:

* Close clocks and equal clocks: the proofs count chosen labels at
  a rank `n<=M` and use `pi(P)<=1/q_n^2`.
* Repeated numeric labels: there are `p-1` choices at the repeated
  label's birth `p`, with `pi(P)<=1/q_p^2`.
* Old-source, old-output, and small numeric-output cutoffs: the
  counts at source scale `b` use `pi(P)<=1/q_b^2`.
* The two-sided close source/output window uses the same source
  bound and the three-per-old-label star intersection count.
* The far retirement tail has `M=r` and
  `pi(P)=1/q_r^2<=16/r^4`; it is counted once per original source
  pair, exactly as in its existing proof.
* The Born non-six-endpoint deletion and the near-retirement
  repeated-endpoint deletion are counted in a source dyad `N`
  and use `pi(P)<=1/q_N^2`.

None of these finite counts relies on a small coefficient `g_d`
to produce its convergence. Replacing the bounded product by the
displayed proxy therefore preserves their proved constants.

Let `S_T` be the full symmetrically separated record set. Intersect
it with the earlier core to obtain `K_T`, and let `D_T^omit=S_T\K_T`.
The preceding proxy bounds give one constant `C_*`, independent
of the history and horizon, with

```
sum_(P in D_T^omit) pi(P) <= C_*.
```

Let `iota` interchange the two records (1), and define

```
K_T^pair={P in S_T: P in K_T and iota(P) in K_T}.
```

Since `iota` preserves both the horizon and proxy price,

```
S_T\K_T^pair subset D_T^omit union iota(D_T^omit),
sum_(P in S_T\K_T^pair) pi(P) <= 2C_*.            (2)
```

Thus closing the core by deleting surviving siblings costs at most
one additional `C_*`. This is an actual bounded deletion proof;
smallness of one signed product alone would not imply smallness
of its sibling. Adding the already proved symmetric separation
error also bounds the difference from the original `B_T,R_T`.

From now on let `S_T^pair` denote the set of canonical triples
whose two records survive. It is a fixed finite collection of actual
triples with `M<=T`. Write `B_T^pair,R_T^pair` for their record
sums. Both older asymmetric predicates hold for each sibling
separately; none is silently transferred from one record to the other.

## 3. All three latest-clock cases

For one retained Schur triple, the exact contributions are:

| Latest clock | Born contribution | Retirement contribution | Born minus retirement |
|---|---|---|---|
| `p_z=M` | `w_M g_z(g_x+g_y)` | `0` | `w_M g_z(g_x+g_y)` |
| `p_x=M` | `w_M g_x g_z` | `w_M g_y g_z` | `w_M g_z(g_x-g_y)` |
| `p_y=M` | `w_M g_y g_z` | `w_M g_x g_z` | `w_M g_z(g_y-g_x)` |

In particular the sum always retains **both** products:

```
B(S)+R(S)=w_M g_z(g_x+g_y).                       (3)
```

There is no factor two in (3). There are two different records,
each occurring once. Their signs are those of their actual raw
coefficients. The fact that `z` is numerically largest does not
say that it is the latest-born label.

## 4. Numeric additivity leaves one explicit birth-mean defect

For this triple put

```
Delta(S)=h_(p_z)-h_(p_x)-h_(p_y).
```

Using `x+y=z` and the literal identity `g_d=d-h_(tau(d))`,

```
g_x+g_y=g_z+Delta(S).                             (4)
```

Thus (3) has the exact square decomposition

```
B(S)+R(S)
 = w_M [g_z^2+g_z Delta(S)]
 = w_M [(g_z+Delta(S)/2)^2-Delta(S)^2/4].          (5)
```

The positive square is also
`[z-(h_(p_x)+h_(p_y)+h_(p_z))/2]^2`. The subtraction measures
the actual failure of the raw feature to be additive on this Schur
triple. It is not a diagonal source-pair term already paid in the
causal identity.

This is a real endpoint cancellation, but it stops at the mean defect.
To see its exact content, write the unique differences as

```
x=a_(p_x)-a_(ell_x),
y=a_(p_y)-a_(ell_y),
z=a_(p_z)-a_(ell_z).
```

Their realized Schur relation gives

```
a_(p_x)+a_(p_y)+a_(ell_z)
 =a_(p_z)+a_(ell_x)+a_(ell_y).
```

Consequently

```
Delta(S)=m_(p_x)+m_(p_y)-m_(p_z)
                           +a_(ell_z)-a_(ell_x)-a_(ell_y). (6)
```

The upper endpoints cancel. The remaining prefix means and lower
endpoints are still those of the same actual history. Neither a
mean over the six endpoints nor arbitrary freely chosen gaps can
replace them.

For example, summing the linear correction in (5) can be reindexed
exactly as

```
sum_S w_M g_z Delta(S) = sum_j h_j L_j,

L_j = sum_(S:p_z=j) w_M g_z
     -sum_(S:p_x=j) w_M g_z
     -sum_(S:p_y=j) w_M g_z.                      (7)
```

The irregular actual incidence weights in `L_j` are retained.
The class identity `sum_(d in G_j)g_d=0` does not set these
weighted sums to zero. No such extra cancellation is proved here.

## 5. Born minus retirement has a squared-coefficient transport term

If `z` is latest, its contribution to `B-R` is already the first
line of (5). If instead a summand `L` is latest and `O` is the
other summand, equation (4) gives

```
B(S)-R(S)
 = w_M g_z(g_L-g_O)
 = w_M [g_L^2-g_O^2-Delta(S)(g_L-g_O)].            (8)
```

Thus globally

```
B_T^pair-R_T^pair=P_T+E_T^def,

P_T = sum_(S:p_z=M) w_M g_z^2
      +sum_(S:latest summand L) w_M(g_L^2-g_O^2),

E_T^def = sum_(S:p_z=M) w_M Delta(S)g_z
        -sum_(S:latest summand L) w_M Delta(S)(g_L-g_O).   (9)
```

The potential part itself can be reindexed by physical labels.
Orient an edge from `O` to `L` for each latest-summand triple,
with its actual weight `w_M`. Then

```
P_T=sum_d kappa_T(d) g_d^2,

kappa_T(d)
 = sum_(S: latest label z=d) w_(tau(d))
   +sum_(edges with head d) w_(tau(d))
   -sum_(edges with tail d) w_(tau(head)).          (10)
```

These edges strictly increase birth rank, but their weighted incidence
need not have zero divergence at each physical label. No nonnegative
sign for `kappa_T(d)`, or monotonicity of `g_d^2` along these actual
edges, is supplied by class centering. Equation (10) is a retained
weighted endpoint potential, not a telescoping boundary whose sign
has been established.

## 6. An actual counting bound for the remaining defect cost

The remainders have a concrete all-history bound. Let `N_M` be the
number of retained canonical Schur triples with latest clock `M`.
Each has exactly one label in `G_M` and two distinct labels in
`F_(M-1)`. Choose the new label and one old label. The third label
is one of their sum or positive absolute difference, at most two
options. Each realized triple is encountered exactly twice when
choosing which of its two old labels to mark. Therefore

```
N_M <= (M-1)q_(M-1).                              (11)
```

No arbitrary third-label birth is summed. This count applies to
the actual retained triple collection and could be enlarged to
all pairwise-distinct-clock triples without invalidating the bound.

All `h_j` for the three clocks lie in `[0,H_M]`, so
`|Delta(S)|<=2H_M`. Hence, if

```
Q_T^def=(1/4)sum_(S in S_T^pair)w_M Delta(S)^2,
```

then

```
0<=Q_T^def
 <= sum_(S in S_T^pair) 1/q_M^2
 <= sum_(M=3..T) (M-1)q_(M-1)/q_M^2
 = 2sum_(M=3..T)(M-2)/M^2
 <= 2 log T.                                           (12)
```

The final bound follows from comparison of `sum_(M=3..T)1/M`
with the integral of `1/x`; small or empty horizons give zero
directly. Likewise `|g_d|<=H_M` and (9) give the safe bound

```
|E_T^def| <= 4sum_(S in S_T^pair)1/q_M^2 <= 8 log T.      (13)
```

The latest-`z` part actually uses at most twice the proxy per triple;
four is a uniform bound for both cases. These are genuine bounds
on actual incidences, independent of any freely prescribed gap or
coefficient vector. They are logarithmic, not uniformly summable.

Writing the nonnegative square sum in (5) as `G_T^Schur`, the exact
global common-clock identity is

```
B_T^pair+R_T^pair=G_T^Schur-Q_T^def,
G_T^Schur=sum_S w_M(g_z+Delta(S)/2)^2 >=0.          (14)
```

The existing causal Abel identity and the bounded deletions give

```
2G_T^Schur-2Q_T^def+D_T=A_T+O(1).                 (15)
```

The right side's productive divergence does not make `Q_T^def`
bounded, nor does (15) prove that the Born portion alone has a
positive share. The logarithmic upper bound (12) cannot be
automatically absorbed by the much weaker divergent lower bound
presently supplied on productive epochs. As a lower bound for
`B+R`, (12) is also weaker than the already available Abel identity;
its role is to isolate the exact mean-defect cost.

## 7. Remaining obligation

The common price permits both records to be combined without a
source-time weight exchange. All earlier asymmetric deletions can
be closed under this numeric pairing at bounded cost by (2).
The resulting actual core has the three latest-clock cases in §3,
the square-minus-defect identity (14), and the weighted potential
plus defect identity (9)–(10).

No needed sign or subcritical estimate for the defect and potential
terms is proved here. Even such a transport estimate would still
have to pay the one physical margin from the causal note. Neither
the paired truncation, the mean-defect cancellation (6), nor the
logarithmic remainder bound constitutes a proof of original Q1.
