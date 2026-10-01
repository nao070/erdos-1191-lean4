# Wave 19 / P28: arbitrary-transport residual floor

Date: 2026-08-29 (Asia/Tokyo)  
Status: **finite universal transport lemma proved; the signed whole-cut bridge
remains open; P28 and Erdős #1191 remain unresolved**

## 1. Claim boundary

This note closes one narrow P28 question.  Even if the cut-valid full-row mass
is transported by an arbitrary feasible, energy-aware matrix rather than by a
constant row quotient, a definite part of the inner-new-birth sector survives.
For every dyadic `n>=64`, every increasing integer Golomb prefix, and every
feasible transport defined below, the surviving cross-ratio energy is at least

\[
 \boxed{\mathcal E_n^{\rm res}(t)
        \ge {n^2\over 2^{25}H'_n}.}
\tag{1.1}
\]

This is a universal residual theorem, not a contradiction.  In particular,
the note does **not** prove that the negative renewal cut or the Wave 16
terminal potential pays (1.1).  It does not prove P28, answer either question
of Erdős Problem #1191, construct an infinite branch, establish novelty, or
support a prize claim.

## 2. Inner sector and feasible transports

Retain the Wave 19 notation

\[
 G'_n=\{n,n+1,\ldots,2n-1\},\qquad
 H'_n=\sum_{r=n}^{2n-1}h_r=A-a_{n-1},
\tag{2.1}
\]

and

\[
 \mathcal W_n
 =\sum_{j=n+2}^{2n-1}\sum_{i=n}^{j-2}
   w_{ij}C_{ij},\qquad
 w_{ij}:={(j-i)^2\over4n^2}.
\tag{2.2}
\]

On the inner Gothic rows `n+1<=p<=2n-2`, the exact atom capacities are

\[
 \beta_{p,q}=
 \begin{cases}
  1/n^2,&q=p,\\
  1/(4n^2),&q=p+1,\\
  1/(2n^2),&q\ge p+2,
 \end{cases}
 \qquad p\le q\le2n-2.
\tag{2.3}
\]

The cut-valid residual row mass `bar r=u-v` is

\[
 \bar r_p=
 \begin{cases}
 (4n-2p-3)/(8n^2),&n+1\le p\le2n-3,\\
 3/(8n^2),&p=2n-2.
 \end{cases}
\tag{2.4}
\]

A feasible full-row transport is any family `t_(p,q)` satisfying

\[
 0\le t_{p,q}\le\beta_{p,q},\qquad
 \sum_{q=p}^{2n-2}t_{p,q}=\bar r_p.
\tag{2.5}
\]

It induces on an inner pair `n<=i<j<=2n-1`, `j-i>=2`, the coefficient

\[
 K_t(i,j)=\sum_{p=i+1}^{j-1}\sum_{q=p}^{j-1}t_{p,q}.
\tag{2.6}
\]

Put

\[
 a_{ij}:=w_{ij}-K_t(i,j),\qquad
 \mathcal E_n^{\rm res}(t)
 :=\sum_{j=n+2}^{2n-1}\sum_{i=n}^{j-2}a_{ij}C_{ij}.
\tag{2.7}
\]

## 3. Exact beta-rectangle capacity

For a row with `z` cells remaining in the rectangle, direct summation of
(2.3) gives

\[
 b_z=
 \begin{cases}
 1/n^2,&z=1,\\
 (2z+1)/(4n^2),&z\ge2.
 \end{cases}
\tag{3.1}
\]

Writing `d=j-i`, the complete beta capacity of the rectangle in (2.6) is

\[
 \sum_{p=i+1}^{j-1}\sum_{q=p}^{j-1}\beta_{p,q}
 =\sum_{z=1}^{d-1}b_z
 ={d^2\over4n^2}=w_{ij}.
\tag{3.2}
\]

Consequently every feasible transport obeys

\[
 0\le K_t(i,j)\le w_{ij},\qquad a_{ij}\ge0.
\tag{3.3}
\]

This is pointwise and does not assume that `t` is a row quotient.

## 4. A transport-independent row-sum bound

For every inner row, including the exceptional last row,

\[
 \boxed{\bar r_p\le {2n-p\over4n^2}.}
\tag{4.1}
\]

For `p<=2n-3`, the difference between the right side and (2.4) is exactly
`3/(8n^2)`.  At `p=2n-2`, the demand is `3/(8n^2)`, the right side is
`4/(8n^2)`, and the slack is `1/(8n^2)`.  Thus the exceptional row has not
been silently put into the generic formula.

Write `i=n+x`, `j=n+y`, and `d=y-x`.  Equations (2.5) and (4.1) give

\[
 \begin{aligned}
 K_t(i,j)
 &\le\sum_{p=i+1}^{j-1}\bar r_p\\
 &\le{(d-1)(2n-x-y)\over8n^2}.
 \end{aligned}
\tag{4.2}
\]

After division by `w_ij`,

\[
 {K_t(i,j)\over w_{ij}}
 \le{(d-1)(2n-x-y)\over2d^2}
 <{2n-x-y\over2d}.
\tag{4.3}
\]

The first inequality is valid for every feasible transport, including a
transport selected after inspecting all cross-ratio energies.

## 5. Good partners for every inner gap

Assume now that `n` is dyadic and `n>=64`.  For every coordinate
`x in {0,...,n-1}`, choose exactly `N=n/64` partners as follows:

\[
 P_x=
 \begin{cases}
 \{63n/64,\ldots,n-1\},&x\le7n/8,\\
 \{0,\ldots,n/64-1\},&x>7n/8.
 \end{cases}
\tag{5.1}
\]

Every selected pair has distance at least `7n/64`.  In the first case, the
loose envelope in (4.3) is at most

\[
 {2n-(7n/8)-(63n/64)\over
  2((63n/64)-(7n/8))}={9\over14}.
\tag{5.2}
\]

In the second case, the strict endpoint inequalities in (5.1) give

\[
 {2n-x-y\over2(x-y)}<{71\over110}.
\tag{5.3}
\]

Both constants are below `3/4`.  Hence every selected partner satisfies

\[
 a_{ij}\ge{w_{ij}\over4}
 \ge {1\over4}{(7n/64)^2\over4n^2}
 ={49\over65536}>{1\over2048}.
\tag{5.4}
\]

The deliberately weakened coefficient `1/2048` is convenient for the next
integer count.

## 6. Symmetrization and the energy floor

All adjacent gaps of an integer Golomb ruler are distinct positive integers:
equality `h_r=h_s` for `r!=s` would repeat a positive difference.  Therefore
the sum of the `N=n/64` partner gaps at any fixed vertex is at least

\[
 1+2+\cdots+N={N(N+1)\over2}\ge {n^2\over8192}.
\tag{6.1}
\]

Define the residual weighted neighbor sum

\[
 Q_i^{\rm res}:=\sum_{\substack{j\in G'_n\\|j-i|\ge2}}
                    a_{\min(i,j),\max(i,j)}h_j.
\tag{6.2}
\]

The good partners and (6.1) imply, at every inner vertex,

\[
 Q_i^{\rm res}\ge {1\over2048}{n^2\over8192}
 ={n^2\over2^{24}}.
\tag{6.3}
\]

Now symmetrize once, with no atom duplicated in the final unordered sum:

\[
 \begin{aligned}
 2\sum_{i<j}a_{ij}h_ih_j
 &=\sum_i h_iQ_i^{\rm res}\\
 &\ge {n^2\over2^{24}}\sum_i h_i
 ={n^2H'_n\over2^{24}}.
 \end{aligned}
\tag{6.4}
\]

The Wave 9 product floor gives

\[
 C_{ij}\ge{h_ih_j\over D_{ij}^2}
           \ge{h_ih_j\over(H'_n)^2}
\tag{6.5}
\]

for every inner pair.  Combining (3.3), (6.4), and (6.5) proves (1.1):

\[
 \boxed{
 \mathcal E_n^{\rm res}(t)
 \ge{1\over(H'_n)^2}\sum_{i<j}a_{ij}h_ih_j
 \ge{n^2\over2^{25}H'_n}.}
\tag{6.6}
\]

This proof uses each unordered `C_ij` atom once.  The directed good-partner
sets are used only to lower-bound the two endpoint neighbor sums whose factor
of two is then removed by the exact symmetrization identity.

## 7. Energy-correlated transports do not evade the floor

Changing the order of summation gives the exact covered energy

\[
 \sum_{i<j}K_t(i,j)C_{ij}
 =\sum_{p=n+1}^{2n-2}\sum_{q=p}^{2n-2}t_{p,q}L_{p,q},
\tag{7.1}
\]

where

\[
 L_{p,q}=\sum_{i=n}^{p-1}\sum_{j=q+1}^{2n-1}C_{ij}.
\tag{7.2}
\]

Since every `C_ij>=0`, `L_(p,q)` is nonincreasing in `q`.  Thus, for a fixed
row and fixed cross-ratio data, the left-greedy filling of the boxes
`0<=t_(p,q)<=beta_(p,q)` maximizes (7.1).  This observation distinguishes
energy-correlated coverage from a uniform coefficient argument.  Nevertheless,
(4.2)--(6.6) use only the row sums and capacities and therefore apply to the
left-greedy maximizer and to every other feasible transport.  No adaptive
choice of `t` evades (6.6).

## 8. The corner `1/3` obstruction is weaker but exact

For the corner `(i,j)=(2n-4,2n-1)`, the rectangle contains the complete last
two rows.  Hence every feasible transport has

\[
 K_t(2n-4,2n-1)
 ={3\over8n^2}+{3\over8n^2}
 ={3\over4n^2}.
\tag{8.1}
\]

Since the full coefficient is `9/(4n^2)`, its exact coverage ratio is `1/3`
and its residual coefficient is `3/(2n^2)`.  This proves that uniform
coefficient coverage strictly above `1/3` is impossible.  By itself it says
nothing about where the energy `C_ij` is concentrated.  The good-partner and
symmetrization argument is the additional ingredient which gives the
energy-correlated universal floor.

## 9. Eventual-`C` and Fejér corollaries

On a hypothetical eventual-`C` branch, for all sufficiently large `m`,

\[
 a_m<Cm^2\log m.
\tag{9.1}
\]

At `m=2n-1`, this gives

\[
 H'_n<A=a_{2n-1}<4Cn^2\log(4n).
\tag{9.2}
\]

Therefore (6.6) implies, for all sufficiently large dyadic `n`,

\[
 \boxed{
 \mathcal E_n^{\rm res}(t)
 >{1\over2^{27}C\log(4n)}.}
\tag{9.3}
\]

For `n=2^k` and the Wave 16 weights

\[
 \omega_{k,J}=\left({J+1-k\over J+1}\right)^2,
\tag{9.4}
\]

the exact harmonic expansion gives

\[
 \sum_{k=k_0}^J{\omega_{k,J}\over k+2}
 =\log J+O_{k_0}(1).
\tag{9.5}
\]

Thus every sequence of feasible transports on an extant eventual-`C` branch
satisfies

\[
 \boxed{
 \liminf_{J\to\infty}
 {\sum_{k=k_0}^J\omega_{k,J}
       \mathcal E_{2^k}^{\rm res}(t)\over\log J}
 \ge {1\over2^{27}C\log2}.}
\tag{9.6}
\]

The statement is conditional on such a branch; it does not assert that one
exists.

## 10. Cut ownership and the remaining signed inequality

The transport demand in (2.4) is exactly `bar r=u-v`.  The `v` coefficient
belongs to the next negative renewal cut.  Extracting the raw `v` fan as an
additional positive resource while retaining that cut would spend it twice
and is forbidden.

There are two legitimate signed organizations.  They may be combined only
through the complete balancing identity already recorded in the companion
adaptive-row-cap memo, not by superimposing selected favorable pieces.

1. In the Wave 12 identity

   \[
    Y_n=R_n-R_{2n}+Z_n,
   \tag{10.1}
   \]

   the whole cuts can remain intact.  Their primitive supports do not overlap
   the inner residual: `R_n` has `i<=n-2`, the inner residual has
   `i>=n,j<=2n-1`, and `R_(2n)` has `j>=2n`.  This makes a *global signed
   inequality* involving the whole cuts a legal target, but support
   disjointness alone supplies no comparison.

2. The Wave 16 terminal potential is the alternative regrouping

   \[
    \mathcal T_n=\mathfrak F_n+\mathfrak e_n+R_{2n}-\mathfrak U_n\ge0,
    \qquad
    Z_n-R_{2n}=\mathfrak P_n-\mathfrak B_n-\mathcal T_n.
   \tag{10.2}
   \]

   Because `T_n` itself contains both `U_n` and `R_(2n)`, one cannot spend a
   part of the `U` rows and then cite `T_n>=0` in isolation.  The companion
   adaptive-row-cap identity (8.5) does supply the required complete ledger:
   it retains `T_n` and the transport simultaneously, while the balancing
   `Qad`, `Pair`, and cap-surplus bracket accounts for every Gothic and cut
   coefficient exactly once.  Thus `T_n` is a legally available negative
   carrier *inside that identity*; no inequality showing that it pays the
   residual is presently known.

After Fejér summation, the whole-cut identity has the exact favorable terms

\[
 \begin{aligned}
 \sum_{k=k_0}^J\omega_{k,J}(R_{2^k}-R_{2^{k+1}})
 ={}&\omega_{k_0,J}R_{2^{k_0}}\\
 &-\sum_{k=k_0+1}^J
   (\omega_{k-1,J}-\omega_{k,J})R_{2^k}\\
 &-\omega_{J,J}R_{2^{J+1}}.
 \end{aligned}
\tag{10.3}
\]

In the balanced adaptive ledger, the exact remaining signed quantity is

\[
 \boxed{
 \mathcal G_n=R_n+P_n^{\rm coef}\log A-K_n^{\rm int}-\mathcal T_n
 -\Theta_n^{\rm full}-{1\over4}\mathcal D_n^{\rm pre},}
\tag{10.4}
\]

where `Pcoef_n=3(n-1)^2/(4n^2)`.  The smallest honest next obligation is the
already isolated strict Fejér inequality

\[
 \boxed{
 \limsup_{J\to\infty}
 {\sum_{k=k_0}^J\omega_{k,J}\mathcal G_{2^k}\over\log J}
 <{1\over3072C\log2}.}
\tag{10.5}
\]

A cleaner stronger target is

\[
 \sum_{k=k_0}^J\omega_{k,J}(\mathcal G_{2^k})_+
 =o_{C,\mathbf a}(\log J).
\tag{10.6}
\]

Neither (10.5) nor (10.6) is proved here.  Equation (9.6) shows that changing
the transport alone cannot remove the residual-energy contribution; the
needed progress must be a genuine cancellation or domination inside the
signed whole-cut/terminal ledger.

## 11. Exact certificate

The companion certificate uses only exact `fractions.Fraction` arithmetic at
`n=64,128,256`.  It verifies:

- the beta row and rectangle identities, representing every inner pair;
- the row-sum upper bound with the exceptional final row separate;
- a literal left-greedy feasible transport and every beta cell bound;
- every directed good-partner inequality;
- the distinct-gap and symmetrization constants;
- the transport-independent corner ratio `1/3`;
- payoff-support nesting behind the energy-aware left-greedy maximizer; and
- explicit scope flags recording that the signed cut inequality and P28 are
  still open.

The represented pointwise rectangle counts are `1953`, `8001`, and `32385`;
the directed partner counts are `64`, `256`, and `1024` respectively.

Replay with

```bash
cd core_workspace/endpoint_variance
PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider \
  test_wave19_p28_transport_residual_floor_certificate.py
PYTHONDONTWRITEBYTECODE=1 python \
  wave19_p28_transport_residual_floor_certificate.py
PYTHONDONTWRITEBYTECODE=1 python \
  wave19_p28_transport_residual_floor_certificate.py --check
```

Files:

- `wave19_p28_transport_residual_floor_certificate.py`;
- `test_wave19_p28_transport_residual_floor_certificate.py`;
- `wave19_p28_transport_residual_floor_certificate_2026-08-29.json`.
