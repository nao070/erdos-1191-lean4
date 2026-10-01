# Reindexing the completed-fiber skew correction by actual endpoints

2026-09-05. `/root/causal_telescoping`, GPT-6 Astra Ultra.

**Status.** Exact finite algebraic reindexing, following the independently
reviewed `completed_fiber_gram_route.md`. It removes the bridge and
fiber-average vectors from the skew term. The remaining endpoint weights
are explicit signed sums over the actual completed fibers. Their cubic
bound or required sign is not proved. No computation was rerun, no free
graph was substituted, and original Q1 remains unresolved.

## 1. Eliminate the bridge from the skew term

Fix one complete nonempty fiber of `R` distinct-point triples in the
notation of the reviewed source. Set

```
K=Q-Q^T,
J_base=diag(x)Q-Q^T diag(x),
J_r=J_base+lambda_r K,
Delta_r=lambda_(r+1)-lambda_r >=0.
```

The matrix `Q` is actually common to all fibers: its nonzero entries
are `(m_j-a_i)/H`. Only the center used in `x,lambda` depends on the
fiber. Throughout this note, the terminal history and complete fibers
are fixed once.

Expanding `xi_(r-1)=v_(r-1)-(r-1)e` and `d_r=nu_r-e` in the
source's skew expression, and using the skew symmetry to cancel
`e^T J_r e`, gives

```
Circ_s
 = (1/2) sum_(u<v) nu_u^T J_v nu_v
   -(1/2) sum_(r<R)(r-1)Delta_r xi_r^T K e.        (1)
```

For clarity, the coefficient from all terms involving one `e` is

```
(1/2) sum_i nu_i^T
  [sum_(r=i..R-1) J_(r+1)+(i-1)J_i] e.
```

The bracket equals
`(R-1)J_R-sum_(r=i..R-1)(r-1)(J_(r+1)-J_r)`.
The `J_R` term vanishes after summing `nu_i=Re`; the remaining
term proves (1). This keeps the original rank offset `r-1`.

There is a second exact simplification:

```
xi_r^T K e = v_r^T K e
 = (1/R) sum_(u<=r<v) nu_u^T K nu_v.              (2)
```

Indeed `e^T K e=0`, and the terms with both endpoints among the
first `r` triples give `v_r^T K v_r=0`. Substitute (2) into (1)
and interchange the finite sums. For `u<v` define

```
gamma_(u,v)
 = lambda_v-(1/R)sum_(r=u..v-1)(r-1)Delta_r.
```

Then the bridge-free identity is

```
Circ_s = (1/2) sum_(u<v)
          nu_u^T [J_base+gamma_(u,v) K] nu_v.      (3)
```

In particular

```
lambda_u <= gamma_(u,v) <= lambda_v.              (4)
```

The removed coefficient is nonnegative and at most
`lambda_v-lambda_u`. When the `lambda_r` are constant, all bridge
corrections cancel exactly and (3) is just the chronological skew
pair sum for that constant operator. It need not be zero.

The coefficients in (3) depend on the entire completed fiber through
`R` and its intermediate completion ranks. This is a fixed-horizon
identity, not an online assignment that remains unchanged when later
triples are added to that same fiber.

## 2. Reindex all fibers into one ambient endpoint-pair sum

Let the triple maxima in fiber `s` be `n_1<...<n_R`. For `u<v` put

```
theta_(s;u,v)
 = m_(n_v)-(1/R) sum_(r=u..v-1)
                         (r-1)(m_(n_(r+1))-m_(n_r)).
```

Thus `gamma_(u,v)=2(theta_(s;u,v)-s/3)/H`, and (4) says

```
m_(n_u) <= theta_(s;u,v) <= m_(n_v).               (5)
```

For an ambient endpoint `i` belonging to this fiber, write `rho_s(i)`
for its unique completed-triple index. Disjointness makes that index
unambiguous. For two endpoints in different triples of this fiber, set

```
epsilon_s(i,j)=sign(rho_s(i)-rho_s(j)).
```

For `i<j`, the lower triangular entry of the operator in (3) is

```
[J_base+gamma K]_(j,i)
 = (x_j+gamma) Q_(j,i)
 = [(a_j+2theta_(s;u,v)-s)/H] [(m_j-a_i)/H].       (6)
```

Its transposed entry has the opposite sign. Write `u_s(i,j)` and
`v_s(i,j)` for the smaller and larger of the two completion indices.
Define the following weight on each actual endpoint pair `i<j`:

```
L_ij = sum_(s: i,j belong to different triples of fiber s)
       epsilon_s(i,j)
       [a_j+2theta_(s;u_s(i,j),v_s(i,j))-s].
```

Summing (3) over every complete fiber gives the exact global identity

```
sum_s Circ_s = (1/(2H^2)) sum_(i<j) (m_j-a_i) L_ij.        (7)
```

Every endpoint pair occurs with precisely its actual fiber incidences.
There is no independent copy of a physical difference budget in (7).
By Sidonness a fiber contains at most one triple through a fixed
endpoint, so each summand in `L_ij` has one specified pair of triples.
Equivalently those incidences are actual four-other-endpoint relations

```
a_i+a_p+a_q = a_j+a_r+a_t,
```

with six distinct endpoints and the actual completion orders. No such
relation is inserted merely because an abstract weight is desired.

## 3. The automatic global cancellation is only the total divergence

There is a useful exact check on any proposed cancellation of the
oriented endpoint incidences. Ignore their nonconstant scalar weights
temporarily and define their endpoint divergence

```
D_i = sum_(s containing i)
      sum_(j in that fiber, rho_s(j)!=rho_s(i)) epsilon_s(i,j).
```

For an endpoint in triple number `r` of a fiber of size `R`, there
are `3(r-1)` earlier endpoints and `3(R-r)` later endpoints. Hence

```
D_i = 3 sum_(s containing i) [2rho_s(i)-R_s-1],
sum_i D_i=0.                                             (8)
```

The second equality is ordinary antisymmetric cancellation. It only
removes a constant endpoint potential. It does not imply `D_i=0`
at individual endpoints. For the actual largest endpoint,

```
D_N = 3 sum_(s containing N) (R_s-1) >=0.          (9)
```

It is strictly positive whenever that endpoint belongs to a nontrivial
completed fiber. Thus completeness and Sidonness do not themselves
make this endpoint flow balanced. Such an incidence already occurs
in the source's displayed sum-40 fiber with largest endpoint 39;
no new example search or computation is needed for that observation.

The weights in (7) additionally involve prefix means, actual sums,
and the intermediate completion drift in `theta`. Neither the
constant-potential cancellation in (8) nor completion of every fiber
removes those weights. Equations (7)–(9) do not exclude a subtler
identity coupling `Circ_s` with the Gram or mean terms; they show
exactly what the direct endpoint reindexing does and does not cancel.

## 4. A compatible simplification of the combined signed correction

If the skew and fiber-mean corrections are kept together, (1) also
combines their drift operators:

```
Circ_s+Mean_s
 = (1/2)sum_(u<v) nu_u^T J_v nu_v
   +sum_r(r-1)e^T A_r e
   -(1/2)sum_(r<R)(r-1)Delta_r xi_r^T(Q+Q^T)e.     (10)
```

Here `K+2Q^T=Q+Q^T` proves the last line. This is an exact
symmetric-drift reformulation, not a positive square: `e` has mass
three, so the zero-mass quadratic Gram identity cannot be applied
to this mixed bilinear expression as if both arguments were the
same centered vector.

The source's global nonnegative Gram and column-square terms and its
cubic error remain intact. No bound of order `-N^3` for (7), (10),
or their sum over the actual fibers is established here.
