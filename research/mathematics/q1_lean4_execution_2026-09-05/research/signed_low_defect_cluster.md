# Four-point clustering when the relative eligible defect is small

2026-09-05. Author: /root/causal_telescoping, GPT-6 Astra Ultra.

**Status.** A small relative eligible-collision defect forces six distinct
endpoints arranged with four points in a short interval at the top.
Their three old top endpoints determine the remaining collision up to
two choices. Under one fixed eventual quadratic-logarithmic radius cap,
this gives a summable output-priced energy tail for relative thresholds
log(2r)^(-gamma), gamma>5/3, and a summable defect tail already for
gamma>1. These analytical cutoffs are not a Q1 proof.

The parent proposed a four-point interval of length 10 epsilon H* and
the injective count. Both are independently checked below, with an
improved interval length (9/2) epsilon H*. No numerical experiment,
finite parameter search, Lean run, or edit to an earlier note is used.
All prices below are actual OUTPUT prices.

The mathematical inputs are the exact formulas in
signed_output_energy_closure.md and the separation argument in
signed_eligible_separation_deficit.md. This note does not rely on a
frequency assertion for collision energy or on regularity of the radii.

## 1. The exact hypotheses and the first geometric bound

Fix an actual integer Sidon history, including repeated two-sum
uniqueness. An eligible active collision is a pair of disjoint
equal-sum triple multisets

~~~
U={ell,u,v}, V={n,x,y}, n>ell>max(u,v,x,y).
~~~

Repeated old slots are permitted initially. Put

~~~
t=n-ell, p=ell-u, q=ell-v, A=ell-x, B=ell-y,
s=p+q, A+B=s+t,
M=max(p,q,A,B), H*=t+M,
aut=aut(U)aut(V),
S=pq+AB+ts+t^2.
~~~

All five distances are strictly positive. Let DeltaY be the full
collision increment of the raw signed diagonal excess, and let

~~~
G_lambda=(1+lambda)DeltaY-8 H_lambda,  0<=lambda<=1,
~~~

where H_lambda is the eligible carrier total of |de|+lambda de.
The earlier exact formulas imply

~~~
G_lambda>=8(1+lambda)S/aut,
0<DeltaY<=16(H*)^2/aut.                             (1)
~~~

Call this collision epsilon-small when

~~~
0<epsilon<=1/64,
G_lambda<=epsilon(1+lambda)DeltaY.                  (2)
~~~

Combining (1)-(2), with the same orbit factor on both sides, gives

~~~
S<=2epsilon(H*)^2.                                 (3)
~~~

This deduction does not assume that the endpoints are distinct:
their distinctness will be a consequence.

## 2. A bootstrap gives a top interval of length (9/2)epsilon H*

First t^2<=S and epsilon<=1/64 imply t<=H*/4.
Also s>=H*-2t: if M is p or q, s>=M=H*-t; if M is A or B,
s+t>=M. Thus s>=H*/2. The term ts in (3) then gives

~~~
t<=4epsilon H*.                                    (4)
~~~

Both pair sums p+q and A+B are at least H*-2t, hence at least
3H*/4. Since each pair product is at most 2epsilon(H*)^2, each
pair's maximum is at least 3H*/8 and its minimum is at most

~~~
min(p,q), min(A,B)<=(16/3)epsilon H*<=H*/12.          (5)
~~~

These already prove the parent's 10epsilon interval claim.
For the useful sharper constant, observe that

~~~
S>=t(s+t)>=t(H*-t).
~~~

Equation (4) gives t<=H*/16, so (3) implies

~~~
t<=(32/15)epsilon H*.
~~~

It follows that both pair sums are at least

~~~
H*-2t >=[1-(64/15)epsilon]H* >=14H*/15.
~~~

Subtracting the initial minimum bound H*/12 in (5) shows that the
maximum in each pair is at least 17H*/20. Dividing the pair-product
bound by this maximum now proves

~~~
min(p,q), min(A,B)<=(40/17)epsilon H*,
t+min(p,q), t+min(A,B)
 <=(1144/255)epsilon H* <(9/2)epsilon H*.            (6)
~~~

The inequality 1144/255<9/2 is exact. Hence n, ell, the closer
old endpoint of U, and the closer old endpoint of V all belong to

~~~
[n-(9/2)epsilon H*, n].                            (7)
~~~

The more distant old endpoint of each triple is at distance at least
17H*/20 below n. In particular it is outside (7), since
(9/2)epsilon<=9/128<17/20.

Each pair's closer endpoint is unique: its distance below ell is at
most (40/17)epsilon H*<=5H*/136, whereas the other distance is at
least 17H*/20. Thus each multiset has three distinct entries.
The supports of U,V are disjoint by the actual Sidon collision
partition, so all SIX endpoints are distinct and aut=1.

There is also a two-point bottom cluster. Write v,y for the closer
old endpoints of U,V and u,x for the farther ones. Equal sums imply

~~~
u-x=n+y-ell-v=t+(ell-v)-(ell-y).
~~~

Its absolute value is at most t+max(ell-v,ell-y), hence at most
(9/2)epsilon H* by (6). Thus the two far points lie within this
same short length of the smallest collision endpoint. This latter
observation is not needed for the count below.

## 3. The injective actual-point count

Fix the newest actual rank r and write n=a_r,
H_r=a_r-a_1. Since H*<=H_r, every epsilon-small collision has its
three old top endpoints in

~~~
I_r=[a_r-(9/2)epsilon H_r,a_r],  k_r=|P_r intersect I_r|.
~~~

The three old top endpoints form an unordered three-element subset
of the k_r-1 points other than a_r. Its maximum is necessarily ell.
There are at most two assignments of the other two points to the
closer U endpoint v and closer V endpoint y.

For each such assignment, the far ordered endpoint difference is
fixed by

~~~
u-x=a_r+y-ell-v.                                   (8)
~~~

The right side is nonzero. Otherwise a_r+y=ell+v would be a repeated
two-sum equality on the actual Sidon prefix, impossible because
a_r exceeds the other three distinct top points. For a nonzero
integer difference, Sidon uniqueness supplies at most one ordered
endpoint pair (u,x). This remains valid for a negative difference
by reversing the ordered pair.

Consequently the top three-point set and its one of two assignments
determine at most one collision. They need not determine a valid
collision; that only weakens the upper count. There is no additional
factor for interchanging U,V, since the newest endpoint canonically
lies in V. No multiset multiplicity remains by Section 2. Therefore

~~~
# {epsilon-small collisions with newest rank r}
 <=2 binom(k_r-1,3).                               (9)
~~~

The local k_r points are an actual Sidon set in an interval of width
(9/2)epsilon H_r. Their distinct positive differences give

~~~
k_r(k_r-1)/2 <=(9/2)epsilon H_r,
k_r-1<=3sqrt(epsilon H_r).
~~~

If k_r<4 the count in (9) is zero. Otherwise
2binom(k_r-1,3)<=(k_r-1)^3/3. Thus uniformly,

~~~
# {epsilon-small collisions at r}
 <=9(epsilon H_r)^(3/2).                           (10)
~~~

In particular a collision satisfying (2) requires
epsilon H_r>=4/3, since its four distinct top points already have
six positive differences within an interval of width
(9/2)epsilon H_r. All these are actual spatial counts, without any
assumed relation between the top three old ranks and r.

## 4. Output-priced energy, carrier, and defect tails

For r>=2 let Q_r=r(r-1), and consider any nonnegative output prices satisfying

~~~
0<=omega_r<=w_r:=1/[Q_r^2 H_r^2].
~~~

Both w and the complete-history compatible u satisfy this condition.
At each rank r choose any 0<epsilon_r<=1/64. Let L_r be the set
of eligible actual collisions at that rank satisfying (2) with
epsilon=epsilon_r and the fixed lambda. Define

~~~
E_low,r=sum_(C in L_r) omega_r DeltaY(C),
H_low,r=sum_(C in L_r) omega_r H_lambda(C),
G_low,r=sum_(C in L_r) omega_r G_lambda(C).
~~~

All endpoints in L_r are distinct, so aut=1. Each collision has
DeltaY<=16H_r^2; combine this with (10) to obtain

~~~
E_low,r <=144 epsilon_r^(3/2) H_r^(3/2)/Q_r^2,
H_low,r <=18(1+lambda)epsilon_r^(3/2)H_r^(3/2)/Q_r^2,
G_low,r <=144(1+lambda)epsilon_r^(5/2)H_r^(3/2)/Q_r^2. (11)
~~~

The carrier bound uses H_lambda<=(1+lambda)DeltaY/8.
The last bound instead uses the defining upper inequality (2);
its extra epsilon factor must not be dropped.

Now assume one C>0 and one rank r0 for which

~~~
H_r<=C r^2 log(2r) for every r>=r0.                 (12)
~~~

For r>=max(2,r0), Q_r^2>=r^4/4. Equation (11) therefore gives

~~~
E_low,r <=576 C^(3/2)
             epsilon_r^(3/2)log(2r)^(3/2)/r,

H_low,r <=72(1+lambda)C^(3/2)
             epsilon_r^(3/2)log(2r)^(3/2)/r,

G_low,r <=576(1+lambda)C^(3/2)
             epsilon_r^(5/2)log(2r)^(3/2)/r.         (13)
~~~

The finite initial segment has finite cost. The chosen prices are
never replaced by a fresh terminal price, and every collision has
exactly one newest stage. Hence no extra sum over retirement times
or source records is introduced.

## 5. Two different summability thresholds

Take epsilon_r=log(2r)^(-gamma) after an onset large enough that
epsilon_r<=1/64. Initial values may be handled separately or capped
at 1/64. From (13),

~~~
gamma>5/3
 => sum_r E_low,r<infinity and sum_r H_low,r<infinity,

gamma>1
 => sum_r G_low,r<infinity.                         (14)
~~~

For the first implication the logarithmic exponent in the denominator
is (3gamma-3)/2>1. For the second it is (5gamma-3)/2>1.
These follow from the usual positive integral comparison for
sum 1/[r(log(2r))^a], a>1.

Thus if a separate theorem proves divergence of the output-priced
eligible carrier, its divergence survives removal of the first
low-relative-defect set. If a separate theorem proves divergence of
the total defect, its divergence survives removal of the second set.
This note does not assume or prove either divergence as a substitute
for a demand-versus-capacity comparison.

The selection in (14) depends on an actual collision's relative
defect, not on a guessed typical geometry. A small relative defect
forces clustering; the actual Sidon packing bound then limits how
many such collisions can exist at that rank.

## 6. What remains outside these cutoffs

The complementary eligible collisions satisfy
G_lambda>epsilon_r(1+lambda)DeltaY. This inequality retains a factor
epsilon_r tending to zero. Divergence of their weighted energy alone
does not imply divergence of their weighted defect. Nor does a
divergent defect alone prove that actual moment demands exceed the
smaller eligible capacity.

In particular, the first bounded-margin criterion involving
eligible capacity minus the actual packing optimum in
signed_output_energy_closure.md remains a separate question. The
energy-budget margin also contains the full geometric defect and
must not be confused with that smaller eligible margin. Any
independently established divergence of the geometric defect may
rule out a bounded energy-budget margin without resolving the
eligible margin or original Q1.

The proved contribution here is the distinct six-endpoint cluster,
the injective count, and the two output-priced summable removals
under one fixed eventual cap. No earlier source was modified.
