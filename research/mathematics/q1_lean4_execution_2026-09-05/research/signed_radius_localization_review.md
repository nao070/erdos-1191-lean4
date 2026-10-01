# Independent review: signed source-radius localization

Date: 2026-09-05. Reviewer: /root/causal_telescoping,
GPT-6 Astra Ultra.

**Verdict: mathematical PASS for the stated finite identities and
conditional good-epoch bounds.** No source correction was needed.

Reviewed source:
research/signed_radius_localization.md

Reviewed SHA256:
f9cd27d8c90f595661de07f8889f1bf0dd3161cb7a32f319ee0b11f7e331d4c7

The full source was read and every displayed identity and constant
was independently rederived. Source hashing is metadata binding,
not a mathematical experiment. No finite sign test, previous
checker, or Lean verification was run.

## 1. Source cutoffs and the integrated group table

For x<y and z=x+y, the two positive signed source groups need
the source z and are absent below radius z. The negative group
needs only x,y and starts at y. It is Born exactly when the output
z is no later than the later of the two source clocks. Whenever
it is Born, that source clock is the full triple maximum M, so
alpha_M is the correct common price. This proves (2), including
the negative boundary with an output outside the source radius.

For doubled labels there is one negative pair {-x,x}, which starts
at radius x, and two positive pairs starting at 2x. This gives (3).
The formal equal-clock case is harmless and is correctly excluded
from actual positive birth stars by their earlier internal differences.

Integration gives de A_*(max(|d|,|e|)), so the unequal table is
exactly

~~~
2x[zA_*(z)-yA_*(y)],
2y[zA_*(z)-xA_*(y)],
2z^2 A_*(z),
2z^2 A_*(z)-2xyA_*(y).
~~~

The doubled table has the required coefficients four and one.
The formulas remain valid when z is beyond the finite upper
radius: its positive term vanishes while the boundary can remain.

Monotonicity of u A_*(u) implies zA_*(z)>=yA_*(y);
nonnegativity of A_* also gives yA_*(y)>=xA_*(y).
This proves both unique-small-label cases and the tied case.
For a doubled label it implies 2A_*(2x)>=A_*(x), sufficient
for the stated expression. The note properly distinguishes this
sufficient condition from any necessity for a full-bank sum.

For w(D)=D^p, 0<=p<1, the integral is
u^(p-1)/(1-p), with nondecreasing u A(u). The absolute-feature
background is a finite integral of outer products whenever the
stated entry integrals are finite, and its combination with the
odd residual is entrywise nonnegative for lambda in [0,1].
No PSD assertion for arbitrary source-stage weights is silently
needed: those arbitrary weights are used in the Born functional.

For dD/D, the first table entry is exactly -x^2/(yz).
The actual prefix {0,2,5,6} has positive differences 1,...,6
and gives clocks 4,2,3 for x=1,y=2,z=3. Positive-difference
uniqueness verifies its Sidon property, including repeated two-sums.
This checks the local clock witness analytically. The source
explicitly does not claim a negative full Born sum on this prefix.

## 2. Ordinary radius measure and finite completion

For dD, A(u)=1/u gives the signed minimum kernel and the exact
unequal group values 0, 2(y-x), 2z, 2y. The doubled values
are 2x and x. These verify (8)-(9), including the integrated
negative boundary intervals.

When D_*>=H, removing the infinite tail subtracts dd^T/D_*.
The omitted rank-one integral is exactly dd^T/D_*, so its
Born contribution is the unnormalized linear contribution divided
by D_* in every clock case. This verifies (10)-(11).

The finite uniform source background is D_*-max(u,v).
Adding the absolute-vector tail uv/D_* yields

~~~
D_*-max(u,v)+uv/D_*
 =min(u,v)+(D_*-u)(D_*-v)/D_*.
~~~

Both the residual and its required nonnegative background are
therefore priced exactly in (12). The stated extra rank-one mass
and trace are correct. The note does not integrate an unweighted
uniform background to infinity and then omit its divergence.

## 3. The permanent threshold carrier

The threshold feature sign(d)1[|d|>=r] is odd and nondecreasing
on the full signed line. Its outer-product integral is the signed
minimum kernel; the unsigned threshold gives the ordinary minimum.
At a finite terminal bank both vanish for r>H. This proves the
PSD and entrywise claims for (13)-(14), and supplies Born
positivity directly from the already reviewed signed theorem.

Every signed prefix is centered at every threshold. Thus the
background mass is M=int Q_r^2, both traces are A=int Q_r,
and the residual mass is zero. Cauchy gives M>=A^2/H;
the elementary bound Q_r<=Q gives M<=QA<=Q^2H.
The sorted-label finite sum has coefficient four because each
positive tail label has two signs. Equations (15)-(16) are correct.

The historical saving lambda(B_R+A/2) retains the full Born
functional and its exact diagonal, including same-birth retirement.
It does not claim a nonpositive residual on retired outputs.

## 4. Future demands and good-epoch constants

For an actual compatible block, the signed support length is
T=L+2H and all m block points are holes, so D=T-m. Each
odd threshold shadow has zero mass and first moment m mu_r.
Integrating the channelwise Cauchy inequalities gives (18);
the exact energy expansion gives (19). Combining with the single
historical saving leaves the diagonal (m-1)A/2 in (20).

An upper tail of the magnitudes has average at least A/Q.
Therefore I>=bar_d^2 M, as in (21).

For N=2p and the stated good shape, there are exactly
(p/2)*p=p^2/2 cross gaps from indices 1,...,p/2 to
p+1,...,2p. Each gap is at least H_p/2. They are all distinct
by Sidonness, and both signs double their contribution to A.
Consequently

~~~
A>=p^2 H_p/2>=N^2 H/(8K)>=QH/(8K).
~~~

This independently checks the factor in (22), hence kappa=1/256
when K=32. It implies I/M>=kappa^2 H^2 and A/M<=1/(kappa Q).

The support bound T<=(K+2)H then gives the first term of (24).
For the negative term, (N-1)/Q=1/N gives exactly
-lambda/(2kappa N). No diagonal has been lost.

For (25), M/A>=kappa Q and
D<=(K+2)C N^2 log(2N) imply

~~~
N M/(D A)>=kappa(N-1)/[(K+2)C log(2N)].
~~~

Substitution in the mass-only raw demand for W proves precisely
the displayed lower bound and eventual positivity. The positive-part
comparison is therefore valid beyond one fixed initial range.

## 5. Physical accounting and scope

Equation (26) is valid because the actual block difference sets
are disjoint. Each demanded physical label contributes once and
its normalized source coefficient is bounded by the displayed
maximum. The integration over thresholds supplies matrix features;
it does not allocate separate physical capacities.

The source correctly distinguishes permanent unnormalized entries
from normalization by the varying row masses M_i. It does not
replace their shared maximum by one fixed historical capacity
divided by an arbitrary common mass.

At lambda=1 the opposite-sign entries vanish. The two same-sign
blocks contribute four times the positive minimum kernel, and
M=4M(V_+), proving the exact normalized baseline comparison.
Old-label masks, actual spans, and maxima over the same row family
preserve that equality.

All these identities and conditional row bounds are supported.
The shared physical margin and original Q1 remain unresolved,
exactly as the source states.
