# Wave 8: Hegyvári's finite consecutive-sum construction and the missing infinite bridge

## Status boundary

This note gives an exact finite Golomb-ruler translation of Hegyvári's 1986
construction, a proof of its affine variants, a sharp splicing criterion, and
deterministic finite searches.  It does **not** construct a nested infinite
Sidon sequence with an all-prefix `O(n^2 polylog n)` coordinate bound, and it
does **not** resolve Erdős Problem #1191.

The primary source was read at the article itself:

- N. Hegyvári, *On consecutive sums in sequences*, Acta Mathematica
  Hungarica 48 (1986), 193--200,
  [DOI 10.1007/BF01949064](https://doi.org/10.1007/BF01949064),
  [official archived volume PDF](https://real-j.mtak.hu/7472/1/MTA_ActaMathHung_48.pdf).

The construction is equations (1.2)--(1.3) on pages 193--194.  The translating
problem is treated on pages 195--197.  This note rederives every claim it uses;
no OCR transcription is treated as a proof.

## 1. Exact finite construction

Let `p` be an odd prime, write `[x]_p` for the representative in
`{0,...,p-1}`, and define `p` positive gaps by

```text
a_(i+1) = 2p + [(i+1)^2]_p - [i^2]_p,       0 <= i < p.
```

With `s_0=0` and `s_t=sum_(i=1)^t a_i`, telescoping gives

```text
s_t = 2pt + [t^2]_p,                         0 <= t <= p.
```

Thus the gap sequence corresponds to the finite Golomb ruler

```text
S_p = {2pt+[t^2]_p : 0 <= t <= p}.
```

It has exactly

```text
p+1 marks,  p gaps,  diameter s_p=2p^2,
p+1 <= a_i <= 3p-1.
```

Consequently, whenever `3p<=n`, all `p` gaps lie in `[1,n]`.  Choosing a prime
`p=(1/3+o(1))n` gives Hegyvári's finite lower constant `1/3`.  This is a
different statement from producing one nested choice for every `p`.

### Direct Golomb proof

The following slightly more general family is useful.  Choose

```text
alpha != 0 (mod p), beta, gamma, c (mod p), and u >= 0,
r_t = [alpha(c+t)^2 + beta(c+t) + gamma]_p,
L = 2p+u,
x_t = Lt+r_t-r_0,                             0 <= t <= p.
```

Every gap is at least

```text
L-(p-1)=p+u+1>0,
```

so the marks increase.  Suppose two positive differences are equal:

```text
x_v-x_w = x_y-x_z,
d=v-w, e=y-z.
```

Each residue difference is in `[-(p-1),p-1]`; hence

```text
L(d-e) = (r_y-r_z)-(r_v-r_w).
```

The right side has absolute value at most `2p-2<L`, so `d=e`.  If `d=p`, both
pairs are the unique full-span pair.  If `1<=d<p`, reduction modulo `p` gives

```text
alpha*d*(v+w-y-z) = 0 (mod p).
```

Since `v=w+d` and `y=z+d`, oddness of `p` gives `w=z (mod p)`.  Both indices
lie in `[0,p-d]`, so `w=z` as integers, then `v=y`.  All positive differences
are therefore unique.

This proves, without relying on a named construction, that:

- nonzero quadratic coefficient, arbitrary linear/constant coefficients, and
  every cyclic rotation preserve the finite Golomb property;
- adding `u` to every gap preserves it;
- every complete `p`-gap variant has the coefficient-independent diameter
  `p(2p+u)`.

There is a second universal internal difference.  The congruence

```text
r_(i+1)-r_i = alpha*(2(c+i)+1)+beta = 0 (mod p)
```

has exactly one solution `i` modulo `p`.  Since both residues use the same
standard representative at that index, the corresponding gap is exactly
`L=2p+u`.  Hence every affine/rotated full block contains both universal
differences

```text
L  and  pL.
```

The exhaustive intersections in the certificate show that these are the only
universal positive differences for the audited samples; only their inclusion,
not that sample-based exclusivity, is used as a theorem.

More generally the affine family has a forced multiple skeleton.  For every
`1<=d<p`, the congruence `r_(i+d)=r_i (mod p)` has one cyclic solution.  If its
pair does not cross the index boundary, the block contains `dL`; if it crosses,
the reversed pair has length `p-d` and the block contains `(p-d)L`.  Hence

```text
for every 1<=d<p, at least one of dL and (p-d)L is present.
```

Thus changing affine coefficients rearranges a rigid collection of exact
multiples; it does not make the internal difference set generic.

Cyclic rotation adds `2*alpha*c` to the linear coefficient and changes the
constant coefficient, so the exhaustive `(alpha,beta,gamma)` sweep in the
verifier already contains every rotation.

## 2. The exact finite upper-counting inequality

Hegyvári's upper argument also has a clean local Golomb formulation.  Let
`h_1,...,h_k` be positive gaps, each at most `n`, whose interval sums are all
distinct.  Retain only interval lengths `1,...,t`.  Their number is

```text
K = tk-t(t-1)/2.
```

As distinct positive integers, their total is at least `K(K+1)/2`.  A fixed
gap occurs in at most `1+2+...+t=t(t+1)/2` retained intervals.  The length-one
sums show that the gaps themselves are distinct, hence

```text
sum h_i <= n+(n-1)+...+(n-k+1) = k(2n-k+1)/2.
```

Therefore the exact inequality is

```text
K(K+1)/2 <= t(t+1) k(2n-k+1)/4.              (H)
```

For fixed `t`, if `k/n -> rho`, the leading terms in (H) give

```text
rho <= 2(t+1)/(3t+1).
```

Letting `t` tend to infinity gives the finite upper constant `2/3`.  Since
every contiguous gap window of an infinite Golomb ruler also has distinct
interval sums, (H) applies to every such window.  It only forces a linear-size
maximum gap in a long window, so by itself it is much too weak to close the
critical logarithmic #1191 problem.

### What the paper's "translating problem" actually says

Section 2 starts with a strictly increasing finite gap list
`A={a_1<...<a_k}` and replaces **every** gap by `a_i+t`.  Equal interval sums
of the same length are already impossible by monotonicity; equal sums of
different lengths exclude only finitely many values of `t`, so some uniform
translation works.  For the special list `A={1,2,...,k}`, Theorem 2 prints the
quantitative bounds

```text
(1+o(1)) k^2/25 < t_A(k) < k^2/4.
```

This is not an old-prefix extension: the `i`-th partial sum is changed by
`i*t`, so all prior positive marks move.  The theorem therefore cannot be
invoked to preserve a fixed Sidon prefix.  Its quadratic translation scale is
also a warning that uniform gap translation can be expensive.

## 3. Exact splicing criterion

Let `A={a_i}` and `B={b_j}` be normalized finite Golomb rulers.  Translate the
whole second block to `T+B`, to the right of `A`.

### Necessary condition, independent of `T`

If an internal difference is shared,

```text
b_j-b_i = a_v-a_u,
```

then for every translation `T`,

```text
(T+b_j)-a_v = (T+b_i)-a_u.
```

Two distinct mixed pairs collide.  Thus

```text
Delta(A) intersect Delta(B) = empty                         (S)
```

is necessary for **every** separated concatenation, no matter how far the new
block is shifted.

### Sufficient condition with an explicit shift

Let `M=max A`, `R=max B`.  If (S) holds, mixed differences are mutually
distinct: an equality between two of them would imply an equality between an
internal difference of `A` and one of `B`.  Choose

```text
T = M+max(M,R)+1.
```

Then every mixed difference is greater than both `M` and `R`, so it cannot
equal an internal difference.  Hence `A union (T+B)` is a Golomb ruler.

Therefore (S) is necessary and sufficient for the existence of a sufficiently
large separated shift.  Translation in physical space cannot cure a shared
internal difference.

## 4. What can be guaranteed for an arbitrary finite old prefix

Let `A` have diameter `M`, and take a Hegyvári block of prime size `p`.  Its
smallest positive difference is at least its smallest gap, namely
`p+u+1`.  Choosing

```text
u >= max(0,M-p)
```

makes every internal block difference larger than `M`; condition (S) is then
automatic.  The explicit shift above gives a valid finite extension of every
old ruler.

This is a genuine sufficient finite splicing theorem, but its quantitative
cost misses #1191.  When `M>=p` and the smallest guaranteed choice `u=M-p` is
used, the block diameter is

```text
R=p(M+p),
```

and the safely spliced ruler has endpoint

```text
M+2p(M+p)+1.
```

For an old `m`-mark critical prefix with `M` of order `m^2 polylog(m)` and a
new block with `p` comparable to `m`, this is of cubic rather than quadratic
order.  Worse, the safe construction places its first new mark near `pM`, so
it violates an all-prefix critical bound immediately.  Taking `p>M` avoids
old differences without `u`, but the first `m` new gaps are then already too
large.  These are finite-extension mechanisms, not a critical infinite tower.

## 5. Universal obstruction to a fixed finite menu

Every affine/rotated full block with fixed `(p,u)` contains the universal base
gap and full-span differences

```text
2p+u  and  p(2p+u).
```

Any finite list of prescribed positive distances can be embedded in a finite
Golomb ruler.  Inductively, if the current ruler has diameter `M` and a new
distance `d` is not already present, put `x=M+max(M,d)+1` and append the pair

```text
x, x+d.
```

All new-to-old differences exceed `max(M,d)`; the two new fans could overlap
only if `d` were already an old difference.  Thus neither an old difference
nor the newly prescribed difference can collide, and the induction remains
Golomb.

It follows that for every finite menu of `(p,u)` values there is a finite old
ruler containing every corresponding universal span.  No affine choice,
rotation, or physical translation from that menu can be spliced to this old
ruler.  In particular, two separated copies of complete Hegyvári blocks with
the same `(p,u)` cannot be concatenated: their distinct endpoint pairs repeat
the full-span difference.  (This does not concern two descriptions of
overlapping subsets that share the very same endpoint pair.)

This obstruction concerns arbitrary finite old rulers.  The constructed
blocker need not lie on an infinite critical branch, so it does not refute a
survival-conditioned theorem tailored to #1191.

## 6. Deterministic exhaustive results

The verifier exhausts all normalized old Golomb rulers in the stated finite
boxes and every distinct affine Hegyvári variant.  Counts include endpoints
*at most* the displayed cap.

| old marks | endpoint cap | new `p` | tested `u` | old rulers | compatible at `u=0` | compatible in range | still incompatible |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 16 | 3 | 0..3 | 354 | 68 | 196 | 158 |
| 4 | 20 | 5 | 0..2 | 802 | 232 | 452 | 350 |
| 5 | 25 | 5 | 0..3 | 4,618 | 166 | 1,060 | 3,558 |

Extending to the elementary magnitude-guaranteed ranges covers every ruler.
The exact largest minimum translations are:

| old box | guaranteed tested range | largest minimum `u` | witness old ruler |
|---|---:|---:|---|
| 4 marks, endpoint <=16, `p=3` | 0..13 | 11 | `(0,3,10,16)` |
| 4 marks, endpoint <=20, `p=5` | 0..15 | 11 | `(0,3,14,19)` |
| 5 marks, endpoint <=25, `p=5` | 0..20 | 17 | `(0,2,10,22,25)` |

Untranslated two-block searches were also negative for all variants in three
small prime transitions:

| first original block | second prime | distinct second variants | least-common-difference histogram |
|---:|---:|---:|---|
| 3 | 5 | 60 | `6:20, 7:20, 11:20` |
| 5 | 7 | 168 | `9:56, 10:42, 11:70` |
| 7 | 11 | 660 | `12:110, 13:132, 14:154, 15:110, 16:66, 17:88` |

These are exhaustive finite statements, not an asymptotic theorem.  Allowing
gap translation produces deterministic positive finite splices.  The first
compatible translations found by the fixed enumeration order were

```text
3 -> 5:   u=2,   safe-spliced endpoint 139
5 -> 7:   u=18,  safe-spliced endpoint 499
7 -> 11:  u=34,  safe-spliced endpoint 1331
11 -> 13: u=94,  safe-spliced endpoint 3363.
```

The endpoints use the proved safe shift and are not claimed optimal.  The
growth of these sample translations is evidence about this finite algorithm
only; it is not an asymptotic lower bound.

An exact search also joined the end of the first block directly to the start
of the second (so the common endpoint is counted once).  The first examples in
the same deterministic coefficient order were:

```text
3 -> 5:   u=2,   parameters (2,0,2),   9 marks, endpoint 78
5 -> 7:   u=18,  parameters (1,3,0),  13 marks, endpoint 274
7 -> 11:  u=50,  parameters (4,4,8),  19 marks, endpoint 890
11 -> 13: u=106, parameters (2,10,11), 25 marks, endpoint 1958.
```

These prove that two-block concatenation is sometimes possible; they do not
give a nested sequence or a uniform translation bound.  Direct endpoint
joining has additional mixed-versus-internal collision constraints, so the
internal-difference criterion alone is not sufficient for this tighter join.

For `p=5` and `u=0,1,2,3`, the universal spans are `50,55,60,65`.  The exact
old ruler

```text
(0,50,106,161,323,383,767,832)
```

is Golomb and contains all four spans, so it blocks all affine and cyclic
variants throughout that translation range.

## 7. Consequence for the #1191 program

Hegyvári supplies an excellent finite parabola block and a useful exact local
inequality.  It does not supply the missing nesting mechanism:

1. the terminal `p` changes with the prime, and the blocks are not nested;
2. physical separation cannot repair repeated internal differences;
3. a finite parameter menu is defeated by a finite prescribed-difference
   blocker;
4. the unconditional magnitude-avoidance splice costs order `pM` and destroys
   the desired all-prefix scale.

The remaining potentially useful target is narrower and survival-conditioned:

> For an old prefix lying on one infinite critical branch, prove that an
> adaptive affine Hegyvári block (possibly after deleting a quantitatively
> small set of marks) has internal difference set disjoint from the old prefix,
> and can be inserted with small enough spacer to preserve every intermediate
> coordinate bound.

Nothing in the primary paper or in the finite computations proves that
statement.  Its key missing ingredient is a structural bound on intersections
between the old difference set and the affine parabola-block difference sets;
arbitrary-prefix counting alone is insufficient.

## 8. Reproduction

Files:

- `wave8_hegyvari_bridge.py`
- `test_wave8_hegyvari_bridge.py`
- `wave8_hegyvari_bridge_certificate_2026-08-28.json`

Commands run from this directory:

```text
uv run --no-project --with pytest python -m pytest -q test_wave8_hegyvari_bridge.py
uvx ruff check wave8_hegyvari_bridge.py test_wave8_hegyvari_bridge.py
uvx ruff format --check wave8_hegyvari_bridge.py test_wave8_hegyvari_bridge.py
python3 wave8_hegyvari_bridge.py --output wave8_hegyvari_bridge_certificate_2026-08-28.json
```

At sealing time the focused test suite had `13 passed`.  The generated JSON
certificate's SHA-256 was
`69c10953c856e0c4ccf46e734ed7d4adda84207ab61617caacf1812f20159ce6`.
The hash must be recomputed after any edit or regeneration.
