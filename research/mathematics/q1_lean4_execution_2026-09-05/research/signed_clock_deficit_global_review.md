# Independent review of eligible far-clock transport

2026-09-05. Reviewer: /root/causal_telescoping, GPT-6 Astra Ultra.

**Verdict: PASS within the explicitly stated analytical scope.**
All eight sections and equations (1)-(17) of
signed_clock_deficit_global.md were read in full and independently
rederived. No mathematical correction is required. The source remains
unchanged. A scope clarification for the word "full" in Section 7 and
an independently derived stronger variant are recorded below.

Reviewed source SHA-256:

~~~
e39045c8a212250a2505ac1df5995c6cd3ed7bab546dfdd8fda0039bc6716051
~~~

The final source bytes were separately measured after the full read:
15,519 bytes. This review uses hand algebra and current source inspection.
It did not rerun a finite experiment, a previous successful checker,
Lean, or any other formal verification.

## 1. Actual eligibility and orbit normalization

For an actual output a_r-a_i, a strictly future block against an old
bank n can pay a source pair of birth b only when b<=n<i. Thus b<i<r
is the exact availability condition. It is stronger than retirement.

Within the full active equal-three-sum collision U,V, the four formal
records opposite m in U have latest source endpoint
max(U without m,V without newest). Their output is newest-m.
Consequently eligibility forces m to be the unique second-largest
endpoint, in the opposite triple from the newest endpoint. If a
second occurrence of m remains among the source endpoints, eligibility
fails. This checks the clock ties and repeated-slot boundary.

All four eligible formal records have one common source clock and
one common output clock. The divisor aut(U)aut(V) is the existing
full multiset orbit divisor. For a doubled numeric Schur list, the
formal-pair duplication and the smaller orbit multiplicity cancel
together; eligibility and both clocks are unchanged by that operation.
The note does not claim a new formal proof of that orbit partition.

## 2. Stronger geometry and the absolute half-B bound

In the note's notation, p,q,a,bgeo>t, P=p+q, S=P+t=a+bgeo.
The elementary inequality (a-t)(bgeo-t)>=0 gives a bgeo>=tP.
Substituting in the exact R formula and using P^2<=2(p^2+q^2)
proves its bound R<=(3/2)B and G>=B/2, with the displayed factors.

For the eligible subtotal, the positive-product bound applies with
third distance t, giving (g1)_+,(g2)_+<=a bgeo t/S. Direct expansion
g1+g2=2a bgeo-(p^2+q^2)-Pt then yields

~~~
|g1|+|g2|
 <=p^2+q^2+Pt-2a bgeo(1-2t/S)
 <=p^2+q^2+Pt(3t-P)/(P+t)
 =p^2+q^2+t^2-t(P-t)^2/(P+t).
~~~

The substitution direction is valid because 1-2t/S>0. Multiplying
by 2/aut proves the absolute correction in (5), including its factor
2. In particular K<=B/2. No sign of the raw rho is assumed.

## 3. Price-ratio grouping and the finite early-source charge

The eligible absolute sum has output price c_r while the full Born
group is born at r. Thus H_out<=B(c)/2 and the retained deficit
2B(c)-H_out is at least (3/2)B(c). When c_b<=4c_r, the full grouped
term c_b K-2c_r B is nonpositive. Dropping those groups, and retaining
the other nonnegative Born remainders with their negative sign,
proves (7). The argument does not drop inconvenient signed records.

For c=w or u, c_b |de|<=alpha_b. The sum over the finitely many
unordered source pairs of birth at most b0 is therefore at most
[M_b0(V)-tr V_b0]/2. Each such pair realizes at most one physical
output. Its eventual retirement time cannot create repeated costs.

## 4. The displayed actual P7 family

The first five points {0,1,8,10,100} have exactly the ten distinct
listed gaps and no gap 3. For L>=204, all L-a and L+3-a exceed
100. A cross-family equality would require old gap 3, and the
remaining new gap is 3. This verifies Sidonness without a finite run.

The equal-sum triples and the four source pairs are exact:
their products are -2,-2,70,70, hence rho=136 and K=144.
All sources are born by rank 4, while the output endpoints have ranks
6 and 7. The spectator 100 does not change those source births.

The Born value is
4[(L+2)^2+(L-7)^2+3^2]=8L^2-40L+248.
The difference of the two stated priced quantities has numerator
1188L^2+323928L-622908 over the positive stated denominator.
It is positive on the prescribed L range.

The spectator extension can be made by repeatedly choosing a new
point more than twice the old diameter, retaining distinct new gaps
and excluding 3. This is a finite extension argument. As stated in
the source, it does not supply a capped infinite counterexample or
invalidate the uniform finite-early-source bound.

## 5. Exact lower-endpoint telescoping

A fixed eligible record occurs in the inner sum of (10) precisely
for b<=n<i. The output belongs to Delta(P_T without P_n) exactly
when both of its actual endpoints occur after n. Its accumulated
coefficient is therefore c_b-c_i.

Every pair in k_(i-1)^abs(a_r-a_i) has b<i<r and is eligible.
Multiplication by c_i-c_r gives the remaining coefficient. This
proves Pre+Post exactly, with each record counted once in the final
commutator. The overlapping suffixes represent a telescoping price
difference, not repeated independent capacities.

For either the even absolute feature or the odd raw feature, the
suffix convolution identity has the diagonal (T-n)Z_n and the
factor 1/2 in front of the off-diagonal energy. The full signed
version is consequently exact, with its actual suffix and source
bank retained.

## 6. Both short-lag thresholds and their constants

The fixed-output graph has degree at most two. Summing
2|de|<=d^2+e^2 yields k_(i-1)^abs(t)<=Z_(i-1), with factor one.
This is the correct unordered-pair normalization.

For u, the price inequality and Q_(i-1)<=(i-1)^2 give
2L_i(L_i+1)/[i^2(i-1)]. For i>=3 this is bounded by the two terms
with coefficient 3 in (13); their summability threshold is gamma>1/2.
No radius cap is used for this u estimate.

For w, the additional radius-change coefficient is 2/i^2.
On N<=i<2N, reindexing actual increments of log H gives the factor
8 in (15). Each increment is crossed by at most
floor[2N/(log N)^gamma]^2 admissible pairs. The involved radii lie
between H_N and H_(4N). Finitely many initial indices cause no
uniform-in-terminal issue.

With one eventual cap and H_N>=N^2/4, the ratio is at most
64C log(8N), giving exactly the convergent dyadic series displayed.
This verifies the onset quantifier and the separate capped scope
of the w estimate.

For Section 7, the displayed theorem concerns the total nonnegative
ELIGIBLE capacity on short top-endpoint lags. At one output,
u_r k_(i-1)^abs<=u_r Z_(i-1)<=1/Q_r.
There are at most floor[r/(log r)^gamma] actual endpoint pairs at
upper rank r in the cutoff. Thus its series is
(1+lambda)sum 1/[(r-1)(log r)^gamma], requiring gamma>1.
This is a capacity bound, not merely a difference-of-prices bound;
the gamma>1/2 threshold cannot be substituted.

The author confirmed that "full" in that section's heading/status
means total eligible capacity, as opposed to a commutator. The body
and displayed statement explicitly retain eligibility.

There is also a valid stronger variant, independently checked here:
all HISTORICAL retired pairs at that output have b<r and lie in
Fhat_(r-1), so replacing k_(i-1)^abs by k_(r-1)^abs gives the same
upper bound (1+lambda)/Q_r. Therefore the same gamma>1 series
controls all historical retired Psi entries on those actual labels,
including ineligible ones. This strengthening is not retroactively
attributed to the displayed proof in the frozen source.

## 7. Remaining scope and final bound

Combining exact Pre+Post with the retained deficit gives (17).
Its O(1) is unconditional for u and uses the one cap for w.
It does not bound the full signed source-priced excess, because
ineligible signed terms have not received a sign.

The h+1 actual points between ranks i and r give
h(h+1)/2 distinct positive differences in their actual span.
That span is at most 2H_b for any source pair, or H_b for a
positive product. The resulting capped bound
h<=2sqrt(C)b sqrt(log(2b)) has the stated constants.

Finally, the crude suffix bound gives
2kappa_n Q_n H_n=8H_n/[(n-1)(n+1)^2]
<=16C log(2n)/n. Its O(log^2 T) accumulation is an upper bound,
not evidence that the true remainder diverges. The stronger old
physical O(log T) bound still does not prove a constant after the
same deficit is subtracted.

The saved note correctly leaves the future-suffix/far-top-lag
comparison open. Its finite algebra, exact clock accounting, and
summable removals do not settle original Q1, do not duplicate a
physical budget, and do not provide new Lean verification.
