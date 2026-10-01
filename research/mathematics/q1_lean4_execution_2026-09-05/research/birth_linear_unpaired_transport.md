# Birth-linear unpaired transport: an exact all-rank reduction

Date: 2026-09-05. Author: `/root/lean_target`, GPT-6 Astra Ultra.

Status: the joint term from (R6) is reduced, with an explicit `O(N³)` error, to a six-endpoint kernel summed over actual equal-three-sum fibers. The cumulative signs of both the unpaired part and the full convolution are proved. The required lower bound for the remaining kernel sum is **not proved**. This is not a Q1 proof or a replacement by the already refuted general small-retirement-operator hypothesis. No new Lean declaration is introduced by this note.

Use the actual Sidon history and notation of [retirement_shadow_review.md](retirement_shadow_review.md): `P={a_1<...<a_N}`, `F=ΔP`, `q=binom(N,2)`, `H=a_N−a_1>0`, and

```
m_j=(Σ_(h<j)a_h)/(j−1),
z_(a_j−a_h)=(m_j−a_h)/H.
```

All sums below use actual integer positions and actual endpoint births. In particular `|z_d|≤1`, every birth class is centered, and `S=Σz_d²≤q`.

## 1. What the triangular indexing proves about U

The contribution born at stage `j` to the unpaired sum is exactly

```
U_j(x)=Σ_(i≤h<j) [(m_j−a_h)/H] 1[x=a_i+a_j−a_h].       (1)
```

Terms with `i=h` lie at `x=a_j` and sum to zero. For a cut `X<a_j`, put `t=a_j−X>0` and

```
c_h(t)=#{i≤h:a_i≤a_h−t}.
```

The sequence `c_h(t)` is nondecreasing in `h`. The endpoint restriction `i≤h` causes no exception, because `t>0` already implies `a_i<a_h`. Pair covariance gives the exact identity

```
Σ_(x≤X) U_j(x)
 = (1/H)Σ_(h<j)c_h(t)(m_j−a_h)
 = −1/((j−1)H) Σ_(h<k<j)(c_k(t)−c_h(t))(a_k−a_h)
 ≤ 0.                                                (2)
```

For `X≥a_j`, all the unpaired incidences have been included. Their sum is

```
Σ_x U_j(x)
 = (1/H)Σ_(h<j)h(m_j−a_h)
 = −1/((j−1)H)Σ_(h<k<j)(k−h)(a_k−a_h)≤0.              (3)
```

Consequently every prefix cumulative sum of each `U_j`, and of `U=Σ_jU_j`, is nonpositive. This is a summed statement; it is compatible with individual positive and negative values of `U_x`.

Each birth-class vector `z` is increasing as a function of its label value and has total zero. Thus its partial sums in increasing-label order are nonpositive. Translating and summing them over the nonnegative point measure `1_P` proves the same cumulative sign for the full convolution `f=1_P*z=V+U`:

```
Σ_(x≤X) f(x)≤0       for every X.                     (4)
```

These facts give nonnegative discrete antiderivatives `−Σ_(x≤X)U_x` and `−Σ_(x≤X)f_x`. They do not give an inner-product sign for `<f,U>`, an `L²` bound of order `N³`, or a sign for the cumulative sums of `V=f−U`. No such inference is used below.

## 2. The complete joint term differs from L−Ret by only O(N³)

Write `L(z)` and `Ret(z)` for the unordered born and retired weighted label-pair sums, respectively. Let

```
J_joint=A_delta+<V,U>+||U||²/2.
```

Using the reviewed identities (R5), together with `E=NS+2(L+Ret)`, gives exactly

```
J_joint = [L(z)−Ret(z)] + NS/2 − Q_orb/2 − F_fix.      (5)
```

Thus the difficult terms have been kept together. Applying only the already established estimates `0≤Q_orb≤2(N−1)S`, `|F_fix|≤Nq`, and `S≤q`, we obtain for `N≥2`

```
|J_joint−[L(z)−Ret(z)]|≤(3/2)Nq.                     (6)
```

For the lower direction specifically, the error is at most `(3N/2−1)q`. These are whole-history bounds; they are not pointwise estimates at a single physical position.

## 3. Equal-three-sum fibers isolate every term of potentially larger order

Every used label pair has a unique third output label, and the three positive labels satisfy `d+e=t`. Restoring their unique endpoints gives two unordered three-point multisets with equal sum. If two *distinct* triples of a common sum shared a point, cancellation would give two equal unordered two-point sums; the actual Sidon condition would make the triples identical. Therefore distinct triples in a common-sum fiber have disjoint supports. In particular there are at most `N` distinct triples in any fiber.

Separate the terms as follows:

- If the two triples are identical, there are at most `binom(N+2,3)≤N³` possible multisets.
- If one of two distinct triples has a repeated point, there are at most `N²` choices for that repeated triple (write it as `{a,a,b}`), and at most `N` choices for a distinct triple of the same sum. This bounds these pairs by `N³`.
- The remaining case consists of two disjoint triples with all six endpoints distinct.

For any fixed pair of triple multisets, there are at most six matchings of their slots. Each matching generates at most two used label pairs, so at most 12 used pairs arise from that multiset pair. Each signed weight has absolute value at most 1. All contributions in the first two cases therefore have combined absolute value at most `24N³`. The bound deliberately allows overcounting and requires no generic-position hypothesis.

## 4. Literal six-endpoint kernel, including the birth test

For disjoint triples `X,Y` of equal sum, with all six points distinct, choose the names so that the largest of the six points belongs to `X`. For each of the six bijections `π:X→Y`, take the three signed differences `x−π(x)`. They are nonzero and sum to zero. One has the opposite sign from the other two; its absolute value is the largest label `t`, and the other two label values `d,e` obey `t=d+e`.

Let `g(s)=z_s` for the actual label coefficients. Let `α` be the label of the matching edge incident to the largest point of the six.

- If `α=t`, its birth is later than the births of both short labels. Both used pairs are born, so this matching contributes

```
g(t)[g(d)+g(e)]
```

to `L−Ret`.

- Otherwise `α` is one of the short labels; write `β` for the other short label. The pair `{t,α}` is born and `{t,β}` is retired, so the contribution is

```
g(t)[g(α)−g(β)].
```

Define `K(X,Y)` as the sum of these six contributions. All labels and their means are taken from the same actual history. There is no artificial deletion, independent birth marking, or dropped sign.

The unique-endpoint property gives no duplicates in this six-distinct case: a used label pair recovers its output endpoints, hence all three matching edges and its pair of triples. Therefore

```
L(z)−Ret(z) = Σ_(X,Y six-distinct, equal-sum) K(X,Y) + D_deg,
|D_deg|≤24N³.
```

Combining with (6) yields the all-rank reduction

```
|J_joint−Σ_(X,Y six-distinct, equal-sum) K(X,Y)|≤25N³.  (7)
```

An equivalent finite classification has only five possible order types. Number the six endpoints increasingly from 1 to 6 and put 6 in `X`. The other two ranks in `X` are one of

```
{1,2}, {1,3}, {1,4}, {1,5}, {2,3}.
```

Every other choice makes the sorted coordinates of `X` componentwise greater than those of `Y`, contradicting equality of their sums. This classification alone supplies no sign for `K`.

## 5. A direct falsification of the tempting K≥0 subclaim

Consider the actual Sidon set

```
P={0,1,10,13,17,39},
```

or translate every point by 1 if positive points are desired. Its 15 positive differences are

```
1,10,13,17,39,9,12,16,38,3,7,29,4,26,22,
```

all distinct. The equal triples are `{0,1,39}` and `{10,13,17}`, both of sum 40. In this order type the largest point is paired to the unique long label for every matching, so none of this kernel's pairs retires.

The needed prefix means are

```
m_10=1/2,  m_13=11/3,  m_17=6,  m_39=41/5,
```

where the subscripts here name the endpoint values rather than their ranks. Summing the six matchings in Section 4 gives directly

```
K = (2/39²) [
      (41/5−10)(11/3+6−1)
     +(41/5−13)(1/2+6−1)
     +(41/5−17)(1/2+11/3−1)]
  = −2096/(15·39²) < 0.                             (8)
```

This exact small example tests the specific new subclaim `K(X,Y)≥0`. It is not an asymptotic extrapolation, a counterexample to a lower bound for the full sum, or a counterexample to the desired joint estimate. In particular it cannot justify discarding the other fibers or the `O(N³)` terms. The calculation explains why proving every fiber nonnegative would be an invalid shortcut.

## 6. Remaining obligation and handoff

The good-epoch energy is of scale `N⁴/log N`; the explicit error in (7) is smaller. Thus the remaining mathematical work is genuinely a joint, all-fiber lower bound for `ΣK`, using the actual prefix-mean constraints and the all-prefix cap. One sufficient outcome would be a negative part of smaller order than `N⁴/log N`; another would retain a positive fraction after combining with the full energy and the additional future-moment demand.

Neither (2)–(4) nor the six-endpoint classification proves that bound. The future moment lower bound strengthens the demand available in the final comparison, but it is not inserted as an assumed payment in (7). The general small norm bound for `C Rret C` is not reconsidered here; its dense actual-family obstruction remains valid with its previously stated scope.

The exact cumulative signs, joint identity, degeneracy bounds, and kernel reduction above are the concrete mathematical checkpoint. The asymptotic joint lower bound and original Q1 remain unresolved.
