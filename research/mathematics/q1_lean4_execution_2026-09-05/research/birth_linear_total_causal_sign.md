# The actual birth-linear total: direct fibers and feasible gaps

Date: 2026-09-05. Owner: `/root/linear_causal_sign`, GPT-6 Astra Ultra.

Status: an exact direct formula for the **full causal total** is proved
below, including the automatic contribution and a bounded repeated-point
error. Two fixed rational checks verify the formula by independent
enumerations. A tempting relaxation to freely chosen nonnegative gaps is
falsified. Neither a universal `X_z >= -O(N^3)` theorem nor an actual
Sidon family with supercubic negative `X_z` is obtained. The fixed-onset
cap/good-epoch version and original Q1 remain unresolved. No Lean file
was changed and no Lean verification is asserted.

The complete assigned notes `birth_linear_good_epoch.md`,
`retirement_shadow_review.md`, `birth_linear_unpaired_transport.md`,
`birth_linear_born_term.md`, and `future_moment_demand.md` were read.
The supporting causal identities in `birth_centered_transport.md` were
also read. This note does not revisit the false arbitrary centered
retirement-operator bound or replace the quadratic total by `B_lin`.

## 1. The quantity being estimated

Let `P={a_1<...<a_N}` be actual integer Sidon, including repeated
two-sums. Put `H=a_N-a_1>0`, `F=Delta P`, `q=binom(N,2)`, and

```
m_j = (sum_(i<j) a_i)/(j-1),
z_jh = z_(a_j-a_h) = (m_j-a_h)/H,        h<j,
S = sum_(h<j) z_jh^2.
```

Every actual birth class sums to zero, and `|z_jh|<=1`, `S<=q`.
A used source pair `{d,e}` is born precisely when the birth rank of
`|d-e|` is at most the maximum source birth. Define

```
L(z) = sum_({d,e} born) z_d z_e,
X_z = L(z)+S/2.
```

The same-birth contribution to `L` is exactly `-S/2`. Consequently

```
X_z = sum_({d,e} born, different source births) z_d z_e.   (1)
```

This is the actual causal total. The coefficients on the common bank
are the ones of the specified history, not freely selected centered
vectors. All statements below retain every mixed-birth Born pair.

## 2. The automatic contribution has an exact positive square part

A used pair, its output label, and their unique endpoints give two
unordered triples with equal sum. If the triples coincide, the three
oriented differences form a directed three-cycle. For `h<i<j`, its
two used source pairs are the pair sharing lower endpoint `h` and
the pair sharing upper endpoint `j`; both are born. Conversely these
are all the automatic pairs, by endpoint uniqueness.

The second type has the same source birth, so cancels in (1). The
entire automatic part of `X_z` is therefore exactly

```
X_auto = sum_(h<i<j) z_ih z_jh
       = (1/2) sum_h C_h^2 - S/2,
C_h    = sum_(j>h) z_jh.                                  (2)
```

In particular `X_auto >= -S/2 >= -q/2`. This is a bound on this
entire part, rather than a claim that every sharing-lower-endpoint
product is positive. The positive column squares in (2) may themselves
have order `N^3` and need not be discarded in a sharper argument.

## 3. A direct three-term kernel for every six-distinct collision

Let `T,U` be two distinct triples of distinct points, with all six
endpoints distinct and common sum `s`. Name them so that `U` contains
the largest endpoint `a_n` among the six. Define

```
Phi(T,U)
 = (1/H^2) sum_(a_j in T)
       (2m_n-s+a_j)
       sum_(a_h in U\{a_n}, h<j) (m_j-a_h).                (3)
```

Formula (3) is the complete mixed-birth Born contribution of this
unordered collision. In particular it is a kernel for `X_z`, not
the previously defined `K(T,U)` for `L-Ret`.
An empty inner sum is zero; in particular no undefined `m_1` is used.

Here is the endpoint verification. A mixed-birth pair with new source
`a_n-a_i` and old source `a_j-a_h`, `h<j<n`, is born if and only if
its two source labels overlap after translation by two points of
`P_n`. Write those smoothing points as `a_k,a_l`. The equality is

```
a_k+a_j-a_h = a_l+a_n-a_i,
T={a_i,a_j,a_k},       U={a_h,a_l,a_n}.                     (4)
```

The actual output difference gives the unique ordered pair `(k,l)`;
there is no additional copy of the source pair. Conversely, given
the six-distinct `T,U`, choose `a_j in T`, choose `a_h in U\{a_n}`
with `h<j`, and choose either `a_i in T\{a_j}`. The two remaining
points are the unique `a_k,a_l` in (4). This produces positive source
labels of distinct birth, with their output already in `F_n`, hence
an actual mixed-birth Born pair. All endpoints and the chosen source
pair recover the choices, so there is no duplication.

For fixed `j,h`, the sum over the two choices of `i` is

```
sum_(a_i in T\{a_j}) (m_n-a_i) = 2m_n-s+a_j.
```

Multiplying by `(m_j-a_h)/H^2` proves (3). It also proves that
there are at most 12 records in this kernel and `|Phi|<=12`.

## 4. The exact full-total reduction and its error

Distinct triples of a common sum cannot share a point: cancellation
would contradict repeated-summand Sidon two-sum uniqueness. Thus
distinct triples in one fiber have disjoint supports.

The remaining nonautomatic case is a collision where at least one
triple has a repeated point. There are at most `N^2` possible repeated
triples, by writing one as `{a,a,b}`. Each has at most `N` distinct
partners of the same sum, by disjointness of supports. This bounds
the number of unordered collisions by `N^3`, allowing overcounting.
Matching their three slots gives at most six matchings, with at most
two used source pairs per matching. Repeated slots only reduce the
number. Every product has absolute value at most one.

Combining this observation, (2), and (3) gives the exact identity

```
X_z = (1/2)sum_h C_h^2 - S/2
       + sum_(T,U six-distinct, equal-sum) Phi(T,U) + D_rep,
|D_rep| <= 12N^3.                                         (5)
```

All fibers in the displayed sum are retained. A lower bound of order
`-N^3` for that sum would suffice for the requested full-total bound.
No such lower bound is proved here.

There is a useful exact way to keep a whole fiber together. Order its
distinct triples by their largest rank. Before its new triple `U`
with largest endpoint `a_n`, let `J_old` be the union of the endpoints
of its earlier completed triples. These endpoints occur exactly once.
Summing (3) over every older triple in this fiber yields

```
(1/H^2) sum_(j in J_old)
    (2m_n-s+a_j) sum_(a_h in U\{a_n}, h<j)(m_j-a_h).        (6)
```

Thus a full-fiber argument may use a single causal endpoint sum,
without estimating its triple pairs separately. Reconstructing (6)
as a nonnegative square minus a total `O(N^3)` diagonal remains an
unproved possibility. Disjoint endpoint membership alone does not
supply that sign.

## 5. The actual cut representation and the feasibility restriction

For `1<=k<N`, define the class-centered cut coefficient by

```
v^k_jh = 0                         if j<=k,
         (j-1-k)/(j-1)             if j>k and h<=k,
         -k/(j-1)                 if j>k and h>k.
```

With `delta_k=a_(k+1)-a_k>0`, summing the coordinate gaps gives
the exact identity

```
H z_jh = sum_k delta_k v^k_jh.                             (7)
```

Let `A_cross` be the symmetric adjacency of the actual mixed-birth
Born graph and put

```
K_kl = (1/2)(v^k)^T A_cross v^l.
```

Then

```
H^2 X_z = delta^T K delta.                                (8)
```

The symmetry in this definition matters: for an unordered mixed
pair its contribution to `K_kl` is
`(v^k_d v^l_e+v^l_d v^k_e)/2`.

The graph and the gaps cannot be varied independently. Every recorded
three-sum equality `T=U` imposes the necessary linear equation

```
sum_k [#{a_i in T:i>k}-#{a_i in U:i>k}] delta_k = 0.        (9)
```

Preserving the exact graph additionally excludes unrecorded equalities
and preserves difference uniqueness. Hence a negative quadratic value
at an arbitrary nonnegative gap vector is not an actual Sidon example
for that graph.

The exact six-point calculation in the evidence file gives
`K_1,3=-37/240` for `P={0,1,10,13,17,39}`, disproving entrywise
nonnegativity. Its complete matrix is

```
113/40   7/24   -37/240   1/15   0
 7/24   13/15    7/60    1/30   0
-37/240  7/60   13/20    1/10   0
 1/15    1/30    1/10      0    0
   0       0       0       0    0
```

For this particular graph the whole form is nevertheless nonnegative
on nonnegative gaps: absorb its sole negative cross term with
`2 delta_1 delta_3 <= delta_1^2+delta_3^2`. The remaining coefficients
of `delta_1^2` and `delta_3^2` are respectively `641/240` and
`119/240`; all other terms have nonnegative coefficients. This checks
an entire finite graph family, not a universal assertion.

Even copositivity without the graph feasibility constraint fails.
For the fixed 32-point fixture from `born_dead_spectral_route.md`,
the exact entries are

```
K_1,1  = 222731046444694206217/743389490296252800,
K_1,30 = -284130964889/316674458100,
K_30,30= 0.
```

The nonnegative relaxed vector with `delta_1=1`,
`delta_30=K_1,1/(-2K_1,30)+1`, and all other gaps zero therefore has
quadratic value `2K_1,30<0`. But the actual graph contains

```
a_2+a_4+a_32 = a_1+a_15+a_29 = 1533.
```

At the proposed relaxed scores the two sides differ by
`1+delta_30>0`. It violates (9). It is therefore explicitly excluded
as an actual negative-total example or an asymptotic obstruction.

## 6. Exact fixed checks and what they establish

Reproducible standard-library code and its complete observed stdout:

- `research/evidence/birth_linear_total_causal_sign_exact.py`
- `research/evidence/birth_linear_total_causal_sign_exact.txt`
- `research/evidence/birth_linear_total_causal_sign_exact.run.json`

Executed through `exec_command` with `python3`; exit code **0**.
The evidence script uses only `Fraction` arithmetic. It checks
positive-difference injectivity and every class zero sum, independently
enumerates physical Born pairs and unordered equal-three-sum fibers,
and verifies (1), (2), (5), the aggregate of (3) over all six-distinct
fiber pairs, and the cited cut entries. It checks
two named preexisting fixtures, not a parameter family or a sweep.
The `.run.json` is a later provenance record transcribed from retained
tool results, with their command, cwd, chunk identifiers, exit codes,
and complete stdout readback. Historical start/end times and source
hashes were not recorded; they remain null. Its current file hashes
were computed when that record was written. No source-unchanged gate
or rerun is claimed by that retrospective record.

For the six-point fixture it obtains

```
X_auto = 1493/9126,
D_rep  = -214/22815,
sum Phi= -2096/22815,
X_z    = 569/9126 > 0.
```

Thus the known negative six-distinct fiber is retained and does not
make the full total negative. The repeated-point part is retained too.
For the 32-point fixture it obtains

```
X_z = 63519376895998932344045509/352214070504135681441600 > 0,
number of six-distinct triple pairs = 3374.
```

Every one of these 3374 pairs is used in that aggregate comparison;
the script does not make 3374 separate per-pair equality assertions.
These positive finite totals do not prove a lower bound at untested
ranks. A preliminary floating-point matrix diagnostic on the same
32-point fixture was used only to identify the cut entries subsequently
certified exactly; none of its eigenvalue output is a certificate here.

## 7. Conditional use with the actual future-moment demand

For the carrier `W=J+zz^T/8`, the already proved comparison in
`future_moment_demand.md` is, with the same actual interval denominator
and the full diagonal loss,

```
[C_hist(J)-delta_J]-[C_hist(W)-delta_mom(B,W)]
             = [2X_z+LB(B)-mS]/16.                        (10)
```

If a new argument proved `X_z>=-C_0 N^3`, then (10) would give

```
comparison >= LB(B)/16 - [2C_0 N^3+m q]/16.                (11)
```

On the extended good epochs with bounded lookahead in the cited note,
`m=N` and `LB(B)>=c q^2/log(2N)` for a fixed `c>0`. Thus (11) would
eventually be positive. This is a conditional comparison within one
actual historical capacity, not permission to add independently chosen
capacities across epochs. Its missing input is precisely the full-total
lower bound; the positive moment demand does not supply that input.

The direct formula (5), the endpoint partition (6), and the actual gap
constraint (9) are the resulting analytic checkpoint. No full-total
asymptotic sign or original-Q1 conclusion has been established.
