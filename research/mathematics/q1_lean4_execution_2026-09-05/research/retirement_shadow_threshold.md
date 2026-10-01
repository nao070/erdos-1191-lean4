# The exact threshold graph at one convolution position

Date: 2026-09-05. Author: `/root`, GPT-6 Astra Ultra.
Status: supporting mathematical identities. No original-Q1 resolution or
Lean verification is asserted. The signed sums below are retained.

Let `P={a_1<...<a_N}` be an actual integer Sidon set, including repeated
summands. Write `F=Delta P`, and let `tau(d)` be the upper endpoint rank
of its unique representation. A label pair `{d,e}` retires when
`t=|d-e|` belongs to `F` and `tau(t)>max(tau(d),tau(e))`.

## 1. A partial involution determined by actual endpoints

Fix an integer convolution position `x`. Its active resource indices are

`I_x={i: d_i=x-a_i belongs to F}`.

For each active index, write the unique actual difference as

`d_i=a_j-a_h`, with `h<j`, so that `a_i+a_j=x+a_h`.

If `a_j<x`, then `a_i>a_h`, and
`x-a_j=a_i-a_h` is another positive difference. Thus `j` is active,
its source upper endpoint is `i`, and the same lower endpoint is `h`.
The correspondence `sigma(i)=j` is an involution on these indices.
It can have two-element orbits and fixed points. At a fixed point,
`x=2a_i-a_h`; repeated-summand Sidonness does not prohibit this when
`x` is not a point of `P`.

If instead `a_j>=x`, the partner label is nonpositive and absent.
Such an index will be called unpaired. Its source birth rank `j` is
larger than every active resource rank `k`, because `a_k<x<=a_j`.
Consequently every pair incident to this unpaired index is born with
its difference already used. It has no retirement edges at this position.

For `x>a_N`, every active index is paired. For `x` in `P`, Sidon
two-sum uniqueness shows that all active labels form the single actual
birth class with upper endpoint `x`; again there are no retirement
edges. The argument for arbitrary `x` does not rely on either special
case.

## 2. The retirement graph is a threshold graph on the paired part

For distinct active resource indices `i,k`, the corresponding labels
satisfy `|d_i-d_k|=|a_i-a_k|`. The physical difference has birth rank
`max(i,k)`. Therefore the exact born-edge test is

`max(i,k) <= max(tau(d_i),tau(d_k))`.                 (1)

On the paired part, replace the two source births by `sigma(i)` and
`sigma(k)`. Order its involution orbits by their largest resource rank.
The following completely describes the retirement graph:

* For a two-element orbit `{i,j}`, `i<j`, its internal edge is born.
  Among its edges to all earlier orbits, the vertex with resource rank
  `i` has no retirement edges, while the vertex with resource rank `j`
  is adjacent by retirement to every earlier vertex.
* A fixed-point orbit has no retirement edges to earlier orbits.
* Unpaired vertices have no retirement edges to any active vertex.

For the first statement, all resource and source ranks in an earlier
orbit are strictly below `j`. The vertex of resource rank `i` has
source birth `j`, which makes (1) true; the vertex of resource rank `j`
has source birth `i`, which makes (1) false. For a fixed point, its
source and resource ranks agree, so (1) is true. This also proves the
internal-edge assertion and every claimed absence of edges.

Equivalently, on the paired part each two-element orbit adds a vertex
adjacent to all earlier vertices and then an isolated vertex. Each
fixed point adds an isolated vertex. This is a threshold graph in the
usual graph-theoretic sense. This description is exact, not a bound on
the number or signs of weighted retirements.

## 3. Exact weighted formula and the birth-linear specialization

For a real coefficient vector `z` on `F`, put `v_i=z_(x-a_i)`.
For an orbit `O`, let `T_<O` be the sum of `v_k` on all earlier paired
orbits, excluding unpaired vertices. The unordered weighted retirement
sum at this position is exactly

`R_x(z)=sum_({i,j} orbit, i<j) v_j T_<{i,j}`.        (2)

There is no factor two in (2); the zero-diagonal adjacency quadratic
form is `2 R_x(z)`. Each global retiring label pair occurs at exactly
one position `x`: if `d<e` and `e-d=a_k-a_i`, `i<k`, that position is
`x=a_k+d=a_i+e`. The uniqueness of positive differences proves that
there is no second position. Hence

`R_ret(z)=sum_x R_x(z)`.                           (3)

Now let `H=a_N-a_1`, `m_j=(sum_(h<j) a_h)/(j-1)`, and use the
specific carrier

`z_(a_j-a_h)=(m_j-a_h)/H`.

Each actual birth class has sum zero. For a two-element orbit `i<j`
with common lower endpoint `h`,

`v_i=(m_j-a_h)/H`, `v_j=(m_i-a_h)/H`,

`v_i-v_j=(m_j-m_i)/H > 0`.                         (4)

All these ranks are at least two, since `h<i<j`. The strict increase
of the preceding-point means proves the sign in (4). In particular,
writing `w_O=v_i+v_j` and `delta_O=(m_j-m_i)/H`, formula (2) becomes

`R_x(z)=1/2 sum_(two-point O) (w_O-delta_O) T_<O`.   (5)

Let a fixed-point orbit have `w_O=v_i`, and let `V_x` be the sum of
`v_i` on the entire paired part. Expanding the square of that sum gives
the alternate exact identity

`R_x(z) = (V_x^2-sum_O w_O^2)/4`
`         - (sum_(two-point O) delta_O T_<O)/2`
`         - (sum_(fixed-point O) w_O T_<O)/2`.       (6)

The means in (4) are increasing, but `T_<O` need not be nonnegative.
Neither correction in (6) has been assigned a sign. Unpaired vertices
are excluded from `V_x`, and replacing it by the full convolution
without accounting for their contribution would be invalid.

For clarity, individual paired coefficients can already be negative.
For the actual Sidon set `{0,10,11,30}`, at `x=31` the orbit on points
`11,30` has common lower point `10`. The preceding means are `5,7`,
so its two coefficients are `-3/30` and `-5/30`. Its six positive
differences are `1,10,11,19,20,30`, all distinct. This example refutes
pointwise coefficient positivity only; it has no retirement edge at
that position and says nothing about the sign of a total correction.

## 4. Connection to the current all-history route

The good-epoch construction in `birth_linear_good_epoch.md` uses
exactly this coefficient vector. `dyadic_good_epochs.md` derives its
eligible epochs from one fixed eventual cap; it does not independently
spend the same physical source at each epoch.

Equations (3), (5), and (6) give an endpoint-preserving way to examine
the retirement term for that particular linear carrier. A usable
summed bound on the signed prefix sums in (5), including fixed-point
and unpaired contributions when comparing with full convolution
energy, remains unproved. These identities are not a transfer theorem
and do not settle original Q1.

## 5. A positive injection for one of the scalar signs

There is nevertheless a weighted consequence that uses the monotonicity
in (4) without assigning a sign to any centered prefix sum. More
generally, let `u_(a_j-a_h)>=0` be nondecreasing in `j` for each fixed
lower endpoint `h`. For a retiring edge at `x` from the high-resource
vertex `j` of an orbit `{i<j}` to an earlier vertex `k`, replace that
high-resource vertex by the low-resource vertex `i`. The source label
`a_i-a_h` is replaced by `a_j-a_h`; the other label is unchanged.
Section 2 shows that the resulting edge is born with its difference
already used. Its weight is at least the source edge's weight:

`u_(a_j-a_h) u_(x-a_k) >= u_(a_i-a_h) u_(x-a_k)`.

This map is injective globally. A target pair has exactly one label
with latest source birth `j`; its other label has source birth less
than `j`. Its unique convolution position `x` follows from actual
difference injectivity. The resource index `i` of the latest-born label
and the unchanged other label can then be recovered, and replacing
the latest-born label by `x-a_j` recovers the original retiring pair.
Distinct positions or source edges cannot collide in this inversion.

All born edges outside the image have nonnegative weight. Consequently,
with unordered weighted pair sums throughout,

`L_born(u u^T) >= R_ret(u u^T)`,
`L_born(u u^T) >= (L_born(u u^T)+R_ret(u u^T))/2`.   (7)

For the linear carrier this applies to `u_t=1+t z`, `0<=t<=1`,
because its entries are nonnegative and its increase on a paired swap
is `t(m_j-m_i)/H`. Thus at least half of its own terminal weighted
old mask remains absent from the historical capacity. This is a
statement for the plus scalar sign. For `1-t z`, the comparison on
each image edge reverses, but the unmatched born edges still have
nonnegative weights; one cannot conclude a reversed inequality for
the two total sums.

The positive injection does not yet retain the terminal improvement
relative to `J`. To display exactly the remaining issue, put

`B_lin=sum_({d,e} born) (z_d+z_e)`.

At every prefix `u_t` has the same mass as the unit vector, and its
squared norm increases by `t^2 S`. If `X_z` is the centered mixed-birth
cross energy, so that `L_born(z z^T)=X_z-S/2`, the improvement in
historical capacity minus the same terminal raw demand is exactly

`I_hist(u_t)=t B_lin+t^2(X_z-mS/2)`.                (8)

The raw-demand term uses a compatible future block of size `m` and
the same positive interval denominator in both comparisons. Its mass
term cancels, but its diagonal term does not. The sign or an adequate
bound for `B_lin` is not established by (7). Averaging the two scalar
signs removes `B_lin`, but (7) then no longer has its demonstrated
monotonicity premise for both components. No such averaging shortcut
is used here.

Independent review: `/root/c143_mathematics` separately rederived
Sections 1--3, the endpoint inversion and weight comparison in (7),
and the retained linear and diagonal terms in (8). Its additional
orbit counts and signed-sum bounds are recorded in
`retirement_shadow_review.md`. These are mathematical reviews, not
Lean verification or a proof of Q1.
