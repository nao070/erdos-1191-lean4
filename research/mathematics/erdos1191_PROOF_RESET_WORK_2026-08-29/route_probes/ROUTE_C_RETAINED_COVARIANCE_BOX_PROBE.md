# Route C: exact retained-covariance box probe

Date: 2026-08-29  
Global status: `UNRESOLVED_AT_HARD_LIMIT`  
Scope: exact finite identities and a bounded enumeration of primitive Golomb
rulers. **No compatible infinite-history theorem, Question 1 result, Question
2 result, current-best result, global optimum, or novelty claim is made.**

This memo instantiates the rank-one target in
`ROUTE_C_TWO_SCALE_BRIDGE_AND_COEFFICIENT_NO_GO.md` for uniform boxes.  The
canonical replay is `retained_covariance_box_probe.py`; its JSON and tests use
only exact `Fraction` arithmetic after deterministic floating active-set
discovery.

## 1. Exact finite convention

Let

\[
A\subset\{0,\ldots,N-1\},\qquad \min A=0,\quad\max A=N-1,
\]

and let `A` be a Golomb ruler.  Here `N` is the ambient interval length, not
the largest mark.  For a positive integer `T`, put

\[
 K_T(x)={1\over T}{\bf1}_{0\le x<T},\qquad
 K_{2T}(x)={1\over2T}{\bf1}_{0\le x<2T}.
\]

The exact convolution range is

\[
0\le x\le (N-1)+(2T-1)=N+2T-2,
\]

so it has exactly `N+2T-1` sites.  A boundary vector
`z(x)=(z_1(x),z_2(x))` is legal when, for every ambient position
`0<=a<N`,

\[
 {1\over T}\sum_{y=0}^{T-1}z_1(a+y)
 +{1\over2T}\sum_{y=0}^{2T-1}z_2(a+y)\ge1.
\tag{1.1}
\]

The endpoint is not cosmetic.  Deleting the last site from the constant
cover lowers the last row from `1` to

\[
1-{1\over4T}<1.
\]

The replay and tests verify this off-by-one value exactly.

## 2. Box/Haar identities

Translation by `T` is denoted by `tau_T`.  The dyadic split is

\[
K_{2T}={K_T+\tau_TK_T\over2}.
\tag{2.1}
\]

Hence the contrast `h_T=K_T-K_{2T}` is

\[
h_T(x)=
\begin{cases}
 1/(2T),&0\le x<T,\\
-1/(2T),&T\le x<2T,\\
0,&\text{otherwise}.
\end{cases}
\tag{2.2}
\]

Its exact nonnegative-shift correlation is

\[
\rho_T(d)=\sum_xh_T(x)h_T(x+d)=
\begin{cases}
(2T-3d)/(4T^2),&0\le d\le T,\\
(d-2T)/(4T^2),&T\le d<2T,\\
0,&d\ge2T.
\end{cases}
\tag{2.3}
\]

For `f=1_A`, define

\[
V_T(A):=\|f*K_T-f*K_{2T}\|_2^2=\|f*h_T\|_2^2.
\]

Direct expansion gives the exact Golomb-ruler formula

\[
\boxed{V_T(A)=|A|\rho_T(0)
+2\sum_{a<b\in A}\rho_T(b-a).}
\tag{2.4}
\]

Because a Golomb ruler uses each positive shift at most once, its worst
possible negative contribution is obtained by filling every shift at which
`rho_T(d)<0`.  If `q=floor(2T/3)`, that exact negative budget is

\[
S_T^-:=\sum_{d\ge1}\min\{0,\rho_T(d)\}
={(T-q)(T-3q-3)-T(T-1)\over8T^2}.
\tag{2.5}
\]

Checking the three residue classes of `T mod 3` gives

\[
S_T^-\ge-{3\over16}\qquad(T\ge2),
\tag{2.6}
\]

with equality at `T=2`.  Therefore

\[
\boxed{V_T(A)\ge {|A|\over2T}+2S_T^-.}
\tag{2.7}
\]

In particular, for a dyadic `k`-mark prefix and the nonanticipating choice
`T=k`,

\[
\boxed{V_k(A)\ge{1\over8}.}
\tag{2.8}
\]

For `k=1` this is checked directly (`V_1=1/2`); for `k>=2`, (2.6)--(2.7)
give `1/2-3/8=1/8`.

Equation (2.1) and the parallelogram law also give

\[
\boxed{\|f*K_T\|_2^2=\|f*K_{2T}\|_2^2+V_T(A).}
\tag{2.9}
\]

Therefore, for every finite set `A`,

\[
\sum_{r=0}^{R}V_{2^r}(A)
+\|f*K_{2^{R+1}}\|_2^2=|A|.
\tag{2.10}
\]

Since

\[
\|f*K_L\|_2^2\le\|f\|_1^2\|K_L\|_2^2={|A|^2\over L},
\]

the tail tends to zero and

\[
\boxed{\sum_{r\ge0}V_{2^r}(A)=|A|.}
\tag{2.11}
\]

The diagonal contribution to `V_T` is `|A|/(2T)`.  Center it by defining

\[
O_T(A):=V_T(A)-{|A|\over2T}.
\tag{2.12}
\]

For `M=2^(R+1)`, subtracting the geometric diagonal sum from (2.10) yields

\[
\boxed{
\sum_{r=0}^R O_{2^r}(A)
={|A|\over M}-\|\mathbf1_A*K_M\|_2^2
=-2\sum_{\substack{d\in\Delta(A)\\d<M}}{M-d\over M^2}\le0.}
\tag{2.13}
\]

Equivalently, each nonzero lag has the exact finite identity

\[
\boxed{
\sum_{r=0}^R\langle h_{2^r},\tau_dh_{2^r}\rangle
=-{(M-d)_+\over M^2}.}
\tag{2.14}
\]

Both right sides tend to zero, so

\[
\sum_{r\ge0}O_{2^r}(A)=0.
\tag{2.15}
\]

Thus the full covariance deficits have the exact budget (2.11), but their
easy positive total is diagonal Parseval mass.  The centered signed
off-diagonal resource sums to zero.  The proof is the parallelogram identity;
it does **not** assume that convolved translates have disjoint supports.
These identities concern one fixed finite prefix and do not by themselves
provide the single-owner cross-prefix ledger required by the bridge
obligation.

## 3. Same-fixed-cover gain

Fix `lambda=1/2` and

\[
D={1\over2}I,
\qquad
H_\theta=\begin{pmatrix}1/2-\theta&\theta\\
\theta&1/2-\theta\end{pmatrix},
\qquad0<\theta<1/4.
\]

Then

\[
H_\theta=D-\theta(1,-1)^T(1,-1),
\qquad
\kappa={\theta\over1-4\theta}.
\]

For one fixed feasible `z`, define

\[
B_D=2\sum_x(z_1(x)^2+z_2(x)^2),
\qquad
Q=4\sum_x(z_1(x)-z_2(x))^2.
\]

Sherman--Morrison gives `B_H=B_D+kappa Q`.  The legal diagonal fill is

\[
U_D=1+{3(|A|-1)\over4T}.
\]

The exact same-cover comparison is

\[
\boxed{
G=\theta B_DV_T-\kappa Q U_D+\kappa\theta QV_T
=B_DU_D-B_H(U_D-\theta V_T).}
\tag{3.1}
\]

No difference of two separately optimized products is called `G` here.

Three cover classes are replayed:

1. `simple_gamma`: `z(x)=(1/2,1/2)` on all `N+2T-1` sites.  It has
   `B_D=N+2T-1` and `Q=0`.
2. `D_optimal`: minimize `B_D` subject to (1.1), then hold this exact `z`
   fixed in (3.1).
3. `H_optimal`: minimize `B_H` subject to (1.1), then hold this exact `z`
   fixed in (3.1).

For `M=D` or `H_theta`, the optimized problem is

\[
\min_z z^T(I\otimes M^{-1})z\quad\text{subject to }Az\ge\mathbf1,
\]

with exact dual

\[
\max_{y\ge0}\left(\mathbf1^Ty
-{1\over4}y^TA(I\otimes M)A^Ty\right).
\]

Every accepted optimizer verifies exact cover, dual positivity,
stationarity, complementarity, and primal--dual equality.  Floating point
only guesses the active rows.

For reference, the optional combined-fill correlation is

\[
C_\theta(d)={1\over2}R_{T,T}(d)
+{1\over2}R_{2T,2T}(d)-\theta\rho_T(d).
\tag{3.2}
\]

Every enumerated record passes `C_theta(d)>=0` at every nonzero shift, although
the retained-square use of (3.1) does not require this gate.

## 4. Bounded exact enumeration

The enumeration contains every primitive (`gcd=1`) normalized Golomb ruler
with `2<=|A|<=5` and largest mark at most `12`.  The exact counts are

| marks | rulers |
|---:|---:|
| 2 | 1 |
| 3 | 44 |
| 4 | 112 |
| 5 | 18 |

For each of the 175 rulers it checks

\[
T\in\{1,2,3,4\},\qquad
\theta\in\{1/16,1/8,3/16\},
\]

giving 2,100 exact records per cover class.

| fixed cover | `G>0` | `G=0` | `G<0` |
|---|---:|---:|---:|
| simple gamma | 2100 | 0 | 0 |
| `D`-optimal | 1368 | 0 | 732 |
| `H_theta`-optimal | 2086 | 0 | 14 |

The simple result is structural: `Q=0`, so

\[
G=\theta(N+2T-1)V_T(A)>0
\]

for every nonempty finite `A`.  Positivity of `V_T` follows because the
product of the two nonzero finite convolution polynomials `1_A` and `h_T`
cannot vanish identically.  This is a reproducible finite positive pattern,
not an infinite bridge theorem.

For the dyadic choice `T=k=|A|`, (2.8) strengthens this to the uniform exact
finite bound

\[
\boxed{{G\over N}
=\theta{N+2T-1\over N}V_T(A)
\ge\theta V_T(A)\ge{\theta\over8}.}
\tag{4.1}
\]

At the tested `theta=1/8`, this is `G/N>=1/64`.  The centered identity
(2.13) is the essential warning: (4.1) includes the diagonal `|A|/(2T)`
budget and therefore is not yet a net signed off-diagonal carrier.

The most negative normalized `D`-optimal record is

\[
A=(0,1),\quad T=4,\quad\theta=3/16,
\]

with

\[
B_D={256\over43},\quad Q={6656\over1849},\quad
V={13\over32},\quad U_D={19\over16},
\]

and

\[
G=-{18837\over7396},\qquad {G\over N}=-{18837\over14792}.
\]

The most negative normalized `H_theta`-optimal record is

\[
A=(0,1),\quad T=4,\quad\theta=1/16,
\qquad {G\over N}=-{3250\over109561}.
\]

These signs show that optimizing a boundary metric does not automatically
make the retained-covariance comparison favorable.

## 5. Concrete nonanticipating dyadic-prefix rules

Every four-mark ruler supplies the nested `1,2,4`-mark prefixes.  Consider
the explicit rule

\[
\Pi_{\rm cover}:\quad T=1,quad\theta=1/8,
\]

with the named cover class recomputed using only the current prefix and its
ambient length.  This is nonanticipating within the finite test.

Across all 112 compatible chains:

| rule | all three tested prefixes have `G>0` | chains with a nonpositive prefix |
|---|---:|---:|
| simple gamma | 112 | 0 |
| `D`-optimal | 0 | 112 |
| `H_theta`-optimal | 112 | 0 |

For the `D`-optimal rule, stage signs are:

| prefix size | positive | negative |
|---:|---:|---:|
| 1 | 0 | 112 |
| 2 | 84 | 28 |
| 4 | 112 | 0 |

The lexicographically first chain is `A=(0,1,3,7)`, where

\[
G_1=-{1\over8},\qquad
G_2=-{13\over98},\qquad
G_4={280961\over277207}.
\]

This falsifies only the assertion that this displayed `D`-optimal rule has
positive `G` at every dyadic prefix.  A finite early failure does not refute
the weighted harmonic obligation with an additive constant, and the two
finite surviving rules do not prove it.

The separate nonanticipating rule `T=k`, `theta=1/8`, simple gamma also
passes all 112 chains and, unlike a mere enumeration, satisfies the analytic
bounds

\[
V_k\ge1/8,\qquad G/N\ge1/64
\]

at every dyadic prefix.  Again, (2.13) shows why this full-`V` positivity is
not automatically an off-diagonal harmonic resource.

## 6. Where the dyadic Haar energy sits

For the representative compatible chain `(0,1,3,7)`, the exact values at
`T=1,2,4,8` are

| prefix | `V_1,V_2,V_4,V_8` | tail at width 16 | total |
|---:|---|---:|---:|
| 1 mark | `1/2, 1/4, 1/8, 1/16` | `1/16` | 1 |
| 2 marks | `1/2, 5/8, 13/32, 29/128` | `31/128` | 2 |
| 4 marks | `3/2, 3/4, 15/32, 59/128` | `105/128` | 4 |

The JSON also records exact minimum, mean, and maximum `V_T/|A|` at every
one of these widths and prefix sizes across all 112 chains.  The distribution
moves with the prefix, while (2.11) fixes its total for each individual
prefix.  Turning that finite budget into the required cross-prefix harmonic
deficit remains the missing theorem.

### Exact two-dimensional prefix/scale ownership

Let `A_j` be the first `j` marks of one finite compatible chain and put

\[
E_{j,r}:=\|\mathbf1_{A_j}*K_{2^r}\|_2^2,
\qquad
V_{j,r}:=E_{j,r}-E_{j,r+1}.
\]

With `A_0` empty, define the prefix-owner cell

\[
\Omega^V_{j,r}:=V_{j,r}-V_{j-1,r}.
\tag{6.1}
\]

For `M=2^(R+1)`, double telescoping gives the exact one-owner identity

\[
\boxed{
\sum_{r=0}^R\Omega^V_{j,r}
+(E_{j,R+1}-E_{j-1,R+1})=1.}
\tag{6.2}
\]

Thus each newly added mark owns exactly one unit after the terminal scale is
included.  Centering gives

\[
\Omega^O_{j,r}:=Delta_j
\left(V_{j,r}-{j\over2^{r+1}}\right)
\]

and

\[
\boxed{
\sum_{r=0}^R\Omega^O_{j,r}
={1\over M}-(E_{j,R+1}-E_{j-1,R+1})\longrightarrow0.}
\tag{6.3}
\]

For arbitrary rational weights `w_(j,r)`, prefix Abel/Fubini reindexing is

\[
\boxed{
\sum_{j=1}^J\sum_{r=0}^R w_{j,r}V_{j,r}
=\sum_{i=1}^J\sum_{r=0}^R
\Omega^V_{i,r}\left(\sum_{j=i}^Jw_{j,r}\right),}
\tag{6.4}
\]

and the same identity holds with `V,Omega^V` replaced by `O,Omega^O`.
The replay verifies (6.2)--(6.4) exactly on the representative chain and
stores both ownership matrices in the JSON.  This provides a correct
two-dimensional accounting language.  It does not supply favorable signs
for the centered owner cells.

## 7. Replay and claim boundary

```bash
PYTHONDONTWRITEBYTECODE=1 python3 retained_covariance_box_probe.py \
  --verify retained_covariance_box_certificate.json --self-check

PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v \
  test_retained_covariance_box_probe.py
```

The replay recomputes the full bounded enumeration, checks byte-canonical
JSON and its payload hash, and rejects semantic mutations of the boundary
endpoint, Haar shift/normalization, signs, enumeration scope, telescoping
identity, and Q1/Q2/history claims.

## 8. Registry-ready claims

| ID | Evidence/status | Exact claim | Explicit non-claim |
|---|---|---|---|
| `RC-BOX-HAAR-TELESCOPE` | `PROJECT_INTERNAL_THEOREM`, exact replay | Equations (2.3)--(2.15) give the exact box/Haar correlation, `V_T` lower bound, dyadic Pythagorean identity, total full-`V` budget `sum_r V_(2^r)=|A|`, and centered identity `sum_r O_(2^r)=0`. | The positive full-`V` budget contains diagonal Parseval mass; no net off-diagonal harmonic lower bound. |
| `RC-BOX-PREFIX-SCALE-ABEL` | `PROJECT_INTERNAL_THEOREM`, exact replay | Equations (6.1)--(6.4) give exact prefix-owner cells, terminal-scale ownership, and rational two-dimensional Abel reindexing for both full and centered covariance. | No favorable sign theorem for centered owner cells. |
| `RC-BOX-FINITE-SIGN-ENUM` | `COMPUTER_EXACT`, bounded scope | On 175 primitive rulers, four widths, and three rational theta values, the exact sign counts are `2100/0/0`, `1368/0/732`, and `2086/0/14` for simple, `D`-optimal, and `H_theta`-optimal fixed covers respectively. | No global optimization or extrapolation beyond the stated box. |
| `RC-BOX-D-PI-PREFIX-FAIL` | `COMPUTER_EXACT`, scoped counterexample | The rule `T=1`, `theta=1/8`, current-prefix `D`-optimal cover fails `G>0` at the one-mark prefix of every one of the 112 tested `1,2,4` chains; `(0,1,3,7)` gives `(-1/8,-13/98,280961/277207)`. | Does not refute the Section 8 weighted obligation with its additive constant, or any other rule. |
| `RC-BOX-SIMPLE-POSITIVE` | `PROJECT_INTERNAL_THEOREM` plus finite replay | The constant cover has `Q=0` and therefore `G=theta(N+2T-1)V_T(A)>0` for every nonempty finite `A`; all 2,100 records pass. | Positivity alone is not a compatible-history theorem and does not resolve Q1/Q2. |
| `RC-BOX-T-EQUALS-K-BOUND` | `PROJECT_INTERNAL_THEOREM` plus exact replay | On every dyadic `k`-mark Golomb prefix, `T=k` and the simple cover give `V_k>=1/8` and `G/N>=theta/8`; the `theta=1/8` replay gives `G/N>=1/64`. | This lower bound includes diagonal mass and is not a centered signed deficit. |

Question 1 and Question 2 remain unresolved.
