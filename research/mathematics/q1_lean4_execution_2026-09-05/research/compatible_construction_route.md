# Compatible algebraic integer construction: an exact tower obstruction

Status: Q1 remains unresolved. This note constructs a genuine infinite integer
Sidon sequence and proves that this particular construction fails the required
fixed-onset bound. It also refutes a compressed version by an explicit repeated
sum. It does not prove that all compatible constructions fail, and supplies no
Lean proof of Q1. The arguments below are analytic and algebraic; no parameter
search was used. Author: `/root/global_route`, GPT-6 Astra Ultra.

The counterexample sought would have an increasing enumeration satisfying

\[
 a_n\le C n^2\log(2n)\qquad(n\ge n_0)
\tag{1}
\]

for fixed finite constants. Dense endpoints of a sequence of finite sets are
insufficient. Our previous complete-residue construction gives actual nested
Sidon prefixes, but selects very large new representatives. The concrete
replacement tested here is a field graph with a basis compatible across a tower.
It does not additionally assert the dyadic complete-residue property.

## 1. One precisely defined candidate

Fix an odd prime p. Inside an algebraic closure of F_p use the tower

\[
 K_k=\mathbb F_{p^{2^k}},\qquad K=\bigcup_{k\ge0}K_k.
\]

Choose an F_p-basis e_0,e_1,... of K such that the first d=2^k basis
vectors span K_k. Such a basis exists by extending a basis at each finite
extension. For t in K, write t=sum t_i e_i and t^2=sum u_i e_i, with
t_i,u_i in {0,...,p-1}. Both coefficient sequences have finite support.

For an integer B>=p define

\[
 E_B(t)=\sum_{i\ge0}\bigl(t_i B^{2i}+u_i B^{2i+1}\bigr),
 \qquad A_B=\{1+E_B(t):t\in K\}.
\tag{2}
\]

All terms are positive integers. The first-coordinate digits make E_B
injective. If t is in K_k, so is t^2, hence E_B(t)<B^{2d}. Conversely,
if t is outside K_k, some t_i with i>=d is nonzero, hence E_B(t)>=B^{2d}.
Consequently exactly p^d elements of A_B are at most B^{2d}. In particular
these finite field sets really are prefixes of the integer ordering; no old
integer is rescaled when the tower extends.

## 2. Guarded encoding is genuinely Sidon, including repeated summands

Take B>=2p-1. Every digit of a sum of two encodings is at most 2p-2<B,
so equality of two integer sums implies equality of all coordinate sums.
Reducing the coordinate equations modulo p gives

\[
 t+v=s+w,\qquad t^2+v^2=s^2+w^2.
\]

Since 2 is invertible, these imply tv=sw. Thus the two pairs are the
roots, with multiplicity, of the same monic quadratic. More explicitly,
substitution gives (t-s)(t-w)=0 in the field K, so the unordered pairs
are equal. The shift by 1 in (2) cancels from two-sum equations.

This proves the full integer Sidon property, including comparisons involving
2(1+E_B(t)). It is not merely uniqueness of sums of distinct elements.

At completed levels this construction already pays a guard penalty. The
squares span each K_k over F_p because

\[
 z=((z+1)/2)^2-((z-1)/2)^2.
\]

The last coordinate functional is therefore nonzero on some square. Hence,
for n=p^d, a_n>=B^{2d-1}+1, and

\[
 \frac{a_n}{n^2\log(2n)}
 \ge \frac{B^{2d-1}}{p^{2d}\log(2p^d)}\longrightarrow\infty
 \quad(B>p).
\tag{3}
\]

There is a stronger obstruction between levels which persists even if all
guard overhead is hypothetically removed.

## 3. Exact count between field levels: the cubic growth bottleneck

Put d=2^k, q=p^d. Consider the quadratic extension

\[
 \mathbb F_{q^2}=\mathbb F_q(\alpha),\qquad
 \alpha^2=D\in\mathbb F_q,
\]

where D is a nonsquare. Let V_r be the span of the first r basis vectors,
with r=d+s and 0<=s<=d. Since V_r contains F_q, there is an s-dimensional
F_p-subspace W of F_q for which

\[
 V_r=\mathbb F_q\oplus\alpha W.
\tag{4}
\]

This holds for **any** basis extending the old field basis: take the image
of V_r in the quotient F_(q^2)/F_q and identify that quotient with F_q
by the alpha coefficient. No multiplicative closure of W is assumed.

Because the digits in (2) are nonnegative and less than B,

\[
 1+E_B(t)\le B^{2r}
 \quad\Longleftrightarrow\quad t\in V_r\text{ and }t^2\in V_r.
\tag{5}
\]

An element from a later field cannot evade this condition: its input
coordinates already fail to lie in V_r. Write t=a+b alpha. The first
condition in (5) is b in W. The alpha coefficient of t^2 is 2ab, so the
second condition is 2ab in W. If b=0, all q values of a work. For each
of the p^s-1 nonzero b in W, multiplication by 2b is a bijection on F_q,
and exactly p^s values of a work. We obtain the exact formula

\[
 \boxed{A_B(B^{2(d+s)})=q+p^{2s}-p^s.}
\tag{6}
\]

In particular, for k>=1 take s=d/2. With X_k=B^{3d},

\[
 A_B(X_k)=2q-\sqrt q,
\qquad
 A_B(X_k)\sqrt{\frac{\log X_k}{X_k}}
 \le 2\sqrt{3d\log B}
       \left(\frac{p}{B^{3/2}}\right)^d
 \longrightarrow0.
\tag{7}
\]

This holds for every B>=p. At the exact rank

\[
 n_k=2q-\sqrt q+1\le2q,
\]

the next element is greater than X_k, so

\[
 \frac{a_{n_k}}{n_k^2\log(2n_k)}
 >\frac{B^{3d}}{4p^{2d}\log(4p^d)}\longrightarrow\infty.
\tag{8}
\]

Thus even the formally compressed B=p version has a_n larger than a
constant multiple of n^3 along these intermediate ranks. Successful
carry repair alone would not turn this field tower into a Q1 counterexample.

This obstruction is an exact count of real encoded points. It is stronger
than observing that field cardinalities jump, or checking only the endpoints.
It is independent of the choices of W and of the compatible basis.

## 4. Compression B=p also creates an explicit diagonal collision

Already over the prime field p=7, the degree-one encoding is

\[
 E_7(t)=t+7[t^2]_7\qquad(0\le t<7).
\]

Four relevant values are

\[
 E_7(1)=8,\quad E_7(4)=18,\quad E_7(6)=13,
 \qquad 8+18=13+13.
\tag{9}
\]

After the positivity shift, this is 9+19=14+14. The low digit 6+6
causes a carry into the square-coordinate digit. In F_7^2 the corresponding
graph sums are different: the square coordinates are 3 and 2 modulo 7.
Therefore finite-field Sidonness does not justify the carry-permitting
integer encoding. This particular compressed candidate is refuted outright.

## 5. Characteristic two: the diagonal issue can be resolved, but the
same growth problem remains

For completeness, the analogous APN-looking proposal can be checked without
assuming that an additive F_2 graph is Sidon in the integer sense. Use
K=union F_(2^(2^k)), graph (t,t^3), binary coordinates, the same interleaving,
and B>=3. Integer pair sums are carry-free.

If t+v=s+w=h is nonzero, characteristic two gives

\[
 t^3+v^3=h^3+h\,tv,
\]

so the two field coordinate equations determine tv=sw and the unordered
pair. If h=0, both pairs are diagonal. The integer equation is then
2E_B(t)=2E_B(s), which, by integer injectivity, gives t=s. Off-diagonal
pairs cannot have h=0. This proves that the **guarded integer lift** is
Sidon, despite all diagonal sums of the field graph being zero.

For the intermediate count, write the quadratic extension using
alpha^2+alpha=D and again V_(d+s)=F_q+alpha W. The alpha coefficient of
(a+b alpha)^3 is

\[
 ba^2+b^2a+(D+1)b^3.
\]

For b=0 there are q inputs. For each nonzero b in W and each target in W,
the displayed polynomial is a nonzero quadratic in a, so there are at
most two inputs. Consequently

\[
 A_B(B^{2(d+s)})\le q+2(2^s-1)2^s.
\tag{10}
\]

At s=d/2 this is at most 3q, at integer height B^{3d}. The same calculation
as (7) proves a zero normalized subsequence, even formally at B=2. Thus
switching to this cubic map in characteristic two does not repair the
intermediate-rank failure. The proof does not confuse additive field
diagonals with integer diagonals.

## 6. Narrow primary-source check and what digit logarithms change

Primary sources read on 2026-09-05:

* Javier Cilleruelo, [Infinite Sidon sequences, arXiv:1209.0326v2,
  §§2.1–2.4](https://arxiv.org/pdf/1209.0326).
* Juan Pablo Maldonado Lopez, [A remark on Ruzsa's construction of an
  infinite Sidon set, arXiv:1103.5732v3,
  §3 and Lemma 3.1](https://arxiv.org/pdf/1103.5732).

Cilleruelo uses mixed radices 4q_j, with 2^(2j-1)<q_j<=2^(2j+1),
and active digits q_j+1<=x_j<=2q_j-1 satisfying g_j^(x_j)=p mod q_j.
The prime-label length is set by p about 2^(ck^2). Guarding recovers
both digit sums and the multiset of active lengths. His no-deletion and
deletion constructions have exponents (3-sqrt(5))/2 and sqrt(2)-1.
Maldonado's presentation of the Ruzsa variant instead truncates scaled
Gaussian-prime arguments, reverses expanding binary blocks, and separates
them by guard bits. These mechanisms address mixed-length comparisons;
they are not compatible embeddings of complete finite fields.

The following calculations are independent tests of a proposed boundary
modification, not stronger conclusions asserted by either source.

### 6.1 Merely setting c=1/2 still loses the critical logarithm

Define a formal version of Cilleruelo's digit construction with all prime
labels through 2^(k^2/2-3) assigned lengths at most k. Exclude any label
equal to a modulus prime, so all logarithms used are defined; this exclusion
can only lower counts. Do not assume that the resulting set is Sidon.

Put Q_k=product_(j<=k) q_j and R_k=4^k Q_k. At X_k=R_k-1, every code
of length at least k+1 is greater than X_k, since its leading active digit
is nonzero. Thus, even if every available label gave a distinct code,

\[
 A(X_k)\le 2^{k^2/2},\qquad
 2^{k^2+2k}<R_k\le2^{k^2+4k}.
\]

It follows directly that

\[
 A(X_k)\sqrt{\log X_k/X_k}=O(k2^{-k})\longrightarrow0.
\tag{11}
\]

This is a growth refutation of that exact boundary modification, independent
of the unproved Sidon property. It needs neither the prime number theorem
nor a bound on the number of deletions.

### 6.2 What a quantitative logarithmic repair would have to prove

With prime labels and integer height R, the desired number of labels is
of order sqrt(R/log R). The prime number theorem then requires a prime
cutoff P of order sqrt(R log R), not merely sqrt R. In the guarded digit
scheme R=4^k Q, this would require

\[
 P^2\asymp 4^k Q\log R.
\tag{12}
\]

At this range, the usual same-level certificate
Q divides p_1p_2-p_3p_4 together with |p_1p_2-p_3p_4|<Q is unavailable.
This does not itself prove a collision; exact digit equalities are stronger
than their modular consequences. It identifies a specific extra collision
estimate needed by this proposed repair.

There is also a separate mixed-length issue. In the exponent variables
L_i=k_i^2 of the original construction, its two elementary modular tests
leave the necessary interval

\[
 (1-c)L_1<L_2<\frac{c}{1-c}L_1.
\tag{13}
\]

For c approaching 1/2 this has positive width, from roughly L_1/2 to L_1.
The known deletion estimate balances its exponential cost at sqrt(2)-1;
its formal exponent difference is

\[
 \frac{2c}{1-c}-1-c,
\]

which equals 1/2 at c=1/2. An upper bound becoming too large is not a
lower bound on actual bad tuples, so no impossibility theorem for every
logarithmic construction is asserted here.

## 7. Exact outcome and a narrower remaining construction problem

The guarded odd-characteristic tower is a verified actual infinite integer
Sidon set. Formula (6) gives an exact intermediate density obstruction for
any compatible basis in that tower. Its unguarded p=7 version fails Sidonness
by (9); even hypothetical carry repair leaves (7). The guarded binary cubic
variant is also Sidon, but (10) yields the analogous obstruction.

A successor to these candidates must change more than the base or the field
characteristic. It must provide at least on the order of sqrt(X/log X)
compatible integer points at every intermediate height. For a quadratic
field tower, (6) shows that the graph condition itself supplies only order q
points at height corresponding to three old-field coordinate blocks.
Additional points must therefore change the graph or its encoding, while
remaining compatible with **every** old two-sum equation.

Taking a large fixed p makes log_p(2p-1) closer to 1, but leaves
the exponent-three obstruction even at B=p. Letting the characteristic
vary between stages is not a repair within this tower: fields of distinct
characteristics do not embed into a common field by compatible unital field
maps. Such a change would instead need a new argument for mixed-stage sums.

For a prime-log alternative, the concrete unresolved requirement is to
control exact digit collisions at the range (12), simultaneously for old
and new lengths in (13), while retaining a positive proportion of the
critical number of labels at every height. No such lemma is proved here.
Neither a fixed-onset bound (1) nor a counterexample to Q1 has been obtained.

Independent review: `/root/c143_mathematics` read Sections 1--5 and
confirmed the arbitrary-compatible-basis quotient argument, exact count
(6), positivity shift and intermediate rank in (8), guarded diagonal sums,
and the characteristic-two coefficient/root count. Section 6's literature
comparison was outside that review's scope.
