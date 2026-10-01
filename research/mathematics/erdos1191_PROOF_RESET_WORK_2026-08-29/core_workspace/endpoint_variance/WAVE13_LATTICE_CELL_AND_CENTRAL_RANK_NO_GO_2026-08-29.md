# Wave 13 lattice cells and central-rank no-go diagnostics

Date: 2026-08-29  
Scope: exact identities and finite diagnostics; no asymptotic obstruction is
claimed beyond the stated theorems

## 1. Integer lattice decomposition of one cross ratio

Write the adjacent gaps as `g_k=a_k-a_(k-1)`.  For a cell `(i,j)` with
`j-i>=2`, put

```text
x = a_(j-1)-a_i,
u = g_i,
v = g_j.
```

Then

```text
C_(i,j)=log((x+u)(x+v)/(x(x+u+v))).
```

For positive integer `n`, define

```text
kappa_n=log((n+1)^2/(n(n+2)))>0.
```

Two discrete telescopes give the exact integer-cell identity

```text
C_(i,j)=sum_(s=0)^(u-1) sum_(t=0)^(v-1) kappa_(x+s+t).       (1)
```

Indeed, the summand is the mixed unit difference of `-log n`; summing first
in `t` and then in `s` leaves precisely the four boundary logarithms above.
Thus, for any finite nonnegative coefficient family `q_(i,j)`,

```text
sum q_(i,j) C_(i,j) = sum_(n>=1) M_n kappa_n,

M_n=sum q_(i,j) #{(s,t): 0<=s<u, 0<=t<v, x+s+t=n}.          (2)
```

Formula (2) exposes exactly where integer unit spacing enters.  It does not
by itself bound the occupancy profile `M_n`.

## 2. Exact central-crossing path theorem

Let

```text
S_(k,r)=a_(k+r)-a_k
```

be the sum of `r` consecutive gaps.  The two central differences of the cell
`(i,j)`, with `r=j-i`, are

```text
B=D_(i,j-1)=S_(i-1,r),
C=D_(i+1,j)=S_(i,r).
```

Therefore cells of fixed `r` are exactly the consecutive edges

```text
S_(0,r)--S_(1,r)--...--S_(N-r,r).                           (3)
```

Every interval difference of a Golomb ruler is unique.  Hence vertices from
different pairs `(k,r)` are distinct, including across different `r`.
Consequently the graph obtained by mapping every cell to its unordered
central pair `{B,C}` is a disjoint union of paths.  The map from cells to
edges is injective and every difference vertex has degree at most two.

This is a valid bounded-incidence fact.  The next examples show that central
magnitude spacing alone is too weak a weight for those path edges.

## 3. Exact bounded witnesses against central-hole charges

The complete bounded scope contains all 1,468 normalized eight-mark Golomb
rulers with terminal mark at most `40`; 1,146 of them obey every `C=1` prefix
cap.

### 3.1 Consecutive central values already occur at minimum diameter 34

In that complete scope, the minimum terminal diameter at which a relevant
Wave 12 birth cell has consecutive central values is `34`.  A lexicographically
first witness at that diameter is

```text
(0,1,4,9,15,22,32,34),  m=4,  (i,j)=(1,7).
```

Here

```text
(x,B,C,x+u+v)=(31,32,33,34),
q_(i,j)=27/64,
C_(i,j)=log(32*33/(31*34))=log(528/527).
```

Because `32` and `33` are consecutive integers, they are also adjacent in
the numerical rank order of all differences.  Thus a charge that requires
an unused integer, or even another difference rank, strictly between `B`
and `C` fails in this finite scope.

### 3.2 A large cell can still have adjacent central ranks

The all-prefix-`C=1` ruler

```text
(0,1,7,10,22,24,35,40),  m=4,  (i,j)=(4,6)
```

has

```text
(x,B,C,x+u+v)=(2,14,13,25),
q_(i,j)=1/16,
C_(i,j)=log(14*13/(2*25))=log(91/25).
```

The central values `13,14` are consecutive integers and adjacent ranks, but

```text
C_(i,j)/|log(B/C)|
  =log(91/25)/log(14/13)
  =17.43380157493304... .
```

So the literal pointwise candidate `C_(i,j)<=|log(B/C)|` is false.

The authenticated 64-mark Hall fixture makes the same finite warning more
pronounced.  At `m=32`, cell `(57,59)` has coefficient `1/1024` and

```text
(x,B,C,x+u+v)=(406,804,805,1203),
C_(57,59)=log(15410/11629),
C_(57,59)/log(805/804)=226.47852367606455... .
```

This does not disprove every constant-weighted central-edge theorem.  It says
only that path degree and central rank adjacency, without the outer/inner
curvature, do not supply the needed pointwise payment.

## 4. Finite lattice-occupancy diagnostics

For a finite ruler with `n` marks, the following diagnostic sums the four
nonnegative Wave 12 sector coefficients over every dyadic `m` with `2m<=n`,
truncating future right endpoints at `n-1`, and then forms `M_n` in (2).
The exact maximum occupancies were:

| finite ruler | magnitude attaining maximum | `max M_n` |
|---|---:|---:|
| `(0,3,14,22,23,27,29,39)` | 24 | `63/16 = 3.9375` |
| authenticated Hall 64 | 13,487 | `6679145/4096 = 1630.650634765625` |
| Erdős--Turán 128, `p=257` | 43,662 | `77742955/8192 = 9490.106811523438` |

Hence the simplest candidate `M_n<=1` is already false in the exhaustive
eight-mark regime, and raw maximum occupancy grows across these two longer
fixtures.  These are finite, terminal-dependent diagnostics.  They do not
prove that any occupancy statistic grows on one infinite eventual-`C` branch.

## 5. Finite actual-rank-floor diagnostics for the frontier spectrum

For the exact Wave 13 spectrum `Z_m=sum c_(p,q) log D_(p,q)`, define

```text
P_m       = sum_(c>0) c log D,
L_m       = sum_(c<0) (-c) log binom(ell+1,2),
R_m^rank  = sum_(c<0) (-c) log max{binom(ell+1,2), rank_(2m)(D)}.
```

Here `rank_(2m)` is the actual numerical rank among all differences of the
first `2m` marks.  The rank envelope is `U_m^rank=P_m-R_m^rank`; the rank
premium over the length floor is `R_m^rank-L_m`.  Natural-log projections
are:

| fixture | `m` | exact `Z_m` | rank envelope | rank premium |
|---|---:|---:|---:|---:|
| Hall 64 | 4 | 0.157456 | 1.708981 | 0.649628 |
|  | 8 | 0.218809 | 2.413590 | 0.933093 |
|  | 16 | 0.240089 | 2.961431 | 1.142667 |
|  | 32 | 0.264755 | 3.122966 | 1.250248 |
| E--T 128 | 4 | 0.253319 | 4.080870 | 0.541762 |
|  | 8 | 0.309203 | 4.820039 | 0.828752 |
|  | 16 | 0.350219 | 4.657357 | 0.983331 |
|  | 32 | 0.360120 | 3.971898 | 1.120455 |
|  | 64 | 0.367966 | 3.081265 | 1.199930 |

Thus actual finite ranks improve the length floor, but the resulting
envelopes remain much larger than the exact frontier values on these
fixtures.  This table is neither an optimization theorem nor an asymptotic
no-go result.  It only discourages treating unstructured numerical rank as
the missing payment without a new cross-epoch argument.

## 6. Safe next use

The path decomposition (3) is the reusable exact result: central crossing
edges have degree at most two.  A viable charge can use that carrier only if
it retains an outer/inner or lattice-curvature weight capable of handling the
adjacent-rank witnesses above.  Formula (2) offers another exact carrier, but
its occupancy must be controlled by a survival-conditioned arithmetic
statement; a uniform pointwise occupancy cap is unavailable.

Nothing in this memo proves P15, P17, an upper bound for P18, either question
of Erdős #1191, or a prize claim.
