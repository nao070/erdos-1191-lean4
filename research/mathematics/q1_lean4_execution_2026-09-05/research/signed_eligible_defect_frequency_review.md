# Independent review of full eligible-defect divergence

2026-09-05. Reviewer: /root/causal_telescoping, GPT-6 Astra Ultra.

**Verdict: PASS for all six sections and equations (1)-(16).**
The all-group matching identity, the fiber potential and its diagonal,
the good-prefix count, the fixed-price Abel argument, and the distinction
between the two margins were independently derived. No mathematical
correction is required.

Reviewed final source: signed_eligible_defect_frequency.md.
SHA-256:

~~~
292ce3b077858c742921bd59fe5d24c46a7aa35d630fad0e6e92f28d6ac9d3cd
~~~

The full mathematical note was read. The author corrected the textual
join "Equation (1)+then" before the final freeze; its corrected line was
then read, and the final 12,661-byte source and hash were independently
measured. The correction changes no equation or quantifier.

This is an analytical review. No previous successful checker, finite
parameter test, Lean execution, or other formal verification was rerun.
The source note was not edited by this reviewer.

## 1. The potential and its relation to the actual defect

For a three-point multiset sorted as x<=y<=z, put p=z-x and q=z-y.
The variance formula is
sigma^2=2(p^2+q^2-pq)/3. Thus
Ptop=pq<=(3/2)sigma^2 is equivalent to (p-q)^2>=0.
It includes repeated largest or smallest slots.

In an eligible collision, with the notation of the source,

~~~
Ptop(U)+Ptop(V)
 =pq+Aold Bold+ts+2t^2.
~~~

The already derived defect lower bound has twice the coefficient and
only one t^2. Subtracting the claimed right side of (2) leaves
4(1+lambda)[pq+Aold Bold+ts]/aut>=0. Thus the coefficient 4 is valid.

If there is no eligible output, its entire contribution to G is
(1+lambda)DeltaY. The full matching identity below and the variance
bound for Ptop give even the stronger coefficient 8. Hence the same
coefficient 4 applies to every distinct equal-sum multiset pair,
without a newest-distinctness assumption.

## 2. Full six-matching energy, including a repeated newest endpoint

The auxiliary matching edge values d1,d2,d3 sum to zero and are
nonzero, because the two multiset supports are disjoint. Their
formal full signed Schur-pair sum is sum_i d_i^2. For distinct
magnitudes this is 2yz+2xz-2xy with z=x+y. In the doubled case,
the formal list has twice the actual pair list, exactly as required
by the existing orbit normalization.

Each ordered U-to-V edge occurs in two of the six matchings. If both
triple sums are s0, the total matching square sum is

~~~
2sum_(u,v)(u-v)^2
 =6sum_U u^2+6sum_V v^2-4s0^2
 =6(sigma_U^2+sigma_V^2).
~~~

Dividing by aut(U)aut(V) uses the same physical-pattern multiplicity:
aut realizations for distinct edges, and aut/2 realizations for a
repeated edge together with a doubled formal Schur list. Thus the
actual full raw product sum is 6 variance-sum/aut; its contribution
to Y is twice that, as in (4).

This argument does not distinguish which endpoint is newest. If
the newest endpoint occurs twice or three times, at least two
matching labels have that newest birth. Every source pair in the
full Schur list therefore has newest source birth, and every
output is already present. All its records are Born at that stage.
No hidden retirement or eligible term is lost.

Every full Schur group first becomes entirely present at its latest
endpoint stage. With a unique latest endpoint, its Born source
stage and retired output stage agree with that stage. With a
repeated latest endpoint, all records are Born there. This verifies
that summing the complete collision energy over pairs belongs to
the actual cumulative stage defect.

The existing exact partition gives unique physical edge
representations and their unordered endpoint-multiset collision.
Distinct equal-sum multisets are disjoint by actual Sidon
cancellation. The U=V groups are correctly excluded from the
nontrivial-pair formula and retained only as a nonnegative automatic
Born-only remainder. They are not counted by an invalid orbit rule.

## 3. The fiber identity has no missing factor of two

Let w(U)=1/aut(U), S_s=sum_U w(U), and
P_s=sum_U w(U)Ptop(U) in one sum fiber. Expanding S_s P_s and
removing its single diagonal leaves

~~~
sum_(unordered distinct {U,V})
 w(U)w(V)[Ptop(U)+Ptop(V)].
~~~

This proves (5) with no additional 1/2. Each term has the same
nonnegative potential and the actual full-collision normalization.

There are 6/aut(U) ordered realizations of a multiset U, so
sum_U w(U)=N^3/6 exactly. Since w<=1 and Ptop<=H^2, the diagonal
is at most N^3H^2/6. This includes repeated triples explicitly.

The possible integer triple sums number at most 3H+1.
Since P_s<=H^2S_s, Cauchy gives

~~~
sum_s S_sP_s
 >=sum_s P_s^2/H^2
 >=Ptot^2/[H^2(3H+1)].
~~~

Substitution yields (7), including its finite diagonal coefficient.
No frequency or shape hypothesis was needed for this finite theorem.

## 4. The actual good-prefix lower bound

At a good N divisible by four, the upper-half point lies at least
H_(N/2)/2>=H_N/(2K) above each point of the lower quarter.
Consequently each selected triple contributes at least
H_N^2/(4K^2) to Ptop.

For each fixed upper-half point, the total multiset weight of two
lower-quarter slots is

~~~
binom(N/4,2)+(N/4)/2=(N/4)^2/2.
~~~

The repeated lower slot has weight 1/2; omitting it would not give
the same exact constant at all these ranks. Multiplying by N/2
upper-half choices yields N^3/64 weighted triples and hence
beta=1/(256K^2)=2^-18 for K=32.

The support inequality 3H+1<=4H changes (7) into

~~~
Gcum_N>=(1+lambda)[beta^2N^6H-(2/3)N^3H^2].
~~~

Multiplying by w_N gives the exact negative term
2N/[3(N-1)^2]. For the positive term,
N^6/Q_N^2>=N^2 and the one eventual cap give precisely
beta^2/[C log(2N)]. This proves (10)-(11) with the correct
inequality directions.

## 5. The fixed-price divergence and optional rate

The complete stage defect is nonnegative, including ineligible and
automatic contributions. Hence Gcum is nondecreasing. Since
u_n-u_(n+1)=kappa_n/H_n^2, the finite Abel formula (12) is exact,
with its nonnegative terminal term retained.

On each disjoint good interval [N,2N), H_n<=K H_N and
alpha_N-alpha_(2N)>=15alpha_N/16. Its contribution is at least
15/[16K^2] times w_N Gcum_N. The dyadic negative errors in (11)
are summable, while the actual good-index reciprocal logarithms
diverge. This proves the weighted divergence at the true stage
prices, without transplanting a retired source price.

For direct w, w_(2N)/w_N<=1/16, so the same argument works with
interval factor 15/16. Its terminal term is again nonnegative.

For the optional rate, beta^2=2^-36 and
gamma_*=15/2^14. Their product is 15/2^50.
The good-index constant 1/6 changes this to 5/2^51. Since
N=2^(k+1), log(2N)=(k+2)log 2, which supplies the displayed
factor 1/log 2. Replacing 1/k by 1/(k+2) changes the sum by a
bounded amount. The range T>=2^(J+2) contains every required
window. Thus (15) has its stated constant and concerns log log J,
not log log T.

Only one cap C and one onset are used throughout. No asymptotic
radius profile or online choice of the complete-history u is
asserted. The estimates are uniform after division by 1+lambda
for lambda in [0,1].

## 6. The physical conclusion is a separation, not Q1 closure

The exact eligible-budget identity is

~~~
Elig_T=(1+lambda)Ycal_T(u)/8-Gcal_T(lambda,u)/8.
~~~

Thus the difference between the larger energy budget and eligible
capacity diverges under the cap. Because every permitted optimized
demand is at most that smaller capacity, the energy-minus-demand
margin diverges as well.

The raw prefix residual q_k=(1+lambda)Y_k/8-Pi_k is at least
Gcum_k/8. Its nonnegative weighted series therefore diverges by
the same windows. This invalidates the bounded LARGER energy
margin criterion; it does not assign a sign, boundedness, or
divergence to the smaller residual
r_k=eligible raw capacity-Pi_k.

No physical budget is spent again in making this subtraction.
A growing explicitly retained positive difference is not a
contradiction. The note correctly leaves the eligible allocation,
local projection remainder, and original Q1 unresolved.
