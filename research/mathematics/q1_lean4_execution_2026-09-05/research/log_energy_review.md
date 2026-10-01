# Independent review of the prefix log-energy route

Date: 2026-09-05. Reviewed file: `research/log_energy_route.md`, read in full after its creation during this run.

**Verdict:** the exact split, Wave coefficient identity, asymptotic constants, and fixed-onset non-Sidon countermodel are correct under their stated hypotheses. The potentially singular limits can be justified by the detailed estimates below. This is an independent mathematical review of a scoped relaxation result, **not a proof of Q1 and not Lean verification**. Q1 remains unresolved.

## 1. The exact coefficient 1:-4

Use the source's definitions literally:

\[
L_n=\sum_{0\le i<j<n}\log(a_j-a_i),\quad
E_n=L_n/n^2-\log n,
\]

and let L_B be the pair-log sum over n<=i<j<2n and X_n the cross sum over 0<=i<n<=j<2n. Set E_B=L_B/n^2-log n and F_n=X_n/n^2-2log n. Pair partition gives

\[
4E_{2n}=E_n+E_B+F_n-4\log2.
\]

No asymptotic pair-count replacement is needed. The factor 4 is forced by the normalization (2n)^2. In particular, E_n-4E_(2n) is not an ordinary increment. For any finite weight sequence,

\[
\sum_{k=a}^b w_k(E_k-4E_{k+1})
=w_aE_a-4w_bE_{b+1}
 +\sum_{k=a+1}^b(w_k-4w_{k-1})E_k.
\]

The source's equations (2), (10), and (12) have consistent signs.

## 2. Wave and boundary coefficients

The source's Wave block contains b_0,...,b_n, while its new half B contains b_1,...,b_n. This distinction is retained correctly. Independently mixed-differencing the full quadratic B coefficients gives the main log coefficients in 4n^2 W:

* left-boundary distance b_j-b_0: 2j-1;
* right-boundary distance b_n-b_j: 2(n-j)-1 before the new-half sum is split off;
* full span H: -(n-1)^2;
* an internal pair: -2.

Writing the internal/right pairs as -2L_B changes the explicit right-boundary coefficient to 2(n-j)+1, exactly as in T_n. Restoring the omitted adjacent B entries contributes +1 on every two-gap span and -1 on each of its constituent gaps. Thus

\[
4n^2W_n=T_n-(n-1)^2\log H-2L_B+4n^2R_n,
\qquad E_B=A_n-2W_n+2R_n.
\]

Combining with the preceding split gives

\[
2W_n=E_n-4E_{2n}+A_n+F_n-4\log2+2R_n.
\]

The total coefficient in T_n is 2n(n-1); subtracting (n-1)^2 leaves n^2-1. This verifies the coefficient in the upper bound for A_n as well. A lower bound for E_(2n), rather than its cap upper bound, is needed when estimating the term -4E_(2n) from above.

## 3. The smooth prefix energy without a singular Riemann shortcut

Let f(j)=gamma j^2 log j, gamma>0, at all sufficiently large integer indices, and let s_j=ceil f(j), with a fixed strictly increasing initial segment. All statements below are unchanged by that finite initial choice. Its affected pair-log sum is O(n log n)=o(n^2), even under a crude bound.

For 1<=i<j,

\[
f(j)-f(i)=\gamma(j^2-i^2)\log j+\gamma i^2\log(j/i).
\]

The elementary inequality log t<=(t^2-1)/2 for t>=1 gives

\[
\gamma(j^2-i^2)\log j
\le f(j)-f(i)
\le\gamma(j^2-i^2)(\log j+1/2). \tag{A}
\]

For i=0, use the harmless auxiliary convention i^2 log i=0 and treat the actual initial mark separately. Therefore

\[
\log(f(j)-f(i))
=\log\gamma+\log(j^2-i^2)+\log\log j+\epsilon_{ij},
\quad0\le\epsilon_{ij}\le{1\over2\log j}. \tag{B}
\]

The normalized sum of these errors tends to zero: split j<sqrt(n) and j>=sqrt(n), obtaining O(1/n)+O(1/log n). Rounding changes a difference by less than 1. For large j the smallest smooth difference is at least c_gamma j log j, so even the crude per-endpoint rounding-error sum is O(1/log j). Its total is o(n^2). All logarithms are of positive differences after a fixed onset.

The apparent diagonal singularity can now be eliminated exactly:

\[
\prod_{i=0}^{j-1}(j^2-i^2)=j(2j-1)!.
\]

Stirling with error O(log(j+2)) gives

\[
\log[j(2j-1)!]=2j\log(2j)-2j+O(\log(j+2)).
\]

Summing and using the elementary integral estimate for sum j log j yields

\[
{1\over n^2}\sum_{i<j<n}\log(j^2-i^2)
=\log n+\log2-3/2+O(\log n/n). \tag{C}
\]

For the remaining slowly varying term,

\[
{1\over n^2}\sum_{j<n}j\log\log j
={1\over2}\log\log n+o(1). \tag{D}
\]

One direct proof of (D) subtracts log log n and splits the indices into j<sqrt(n), sqrt(n)<=j<delta*n, and delta*n<=j<n. The first part is o(1) after normalization; the second is O(delta^2), because log(log j/log n) is bounded there; and the last tends uniformly to zero for fixed delta>0. Let delta decrease to zero. The difference between sum j/n^2 and 1/2 contributes O(log log n/n).

There are exactly n(n-1)/2 pairs. Combining (B)-(D), including this exact gamma coefficient, gives

\[
\boxed{E_n={1\over2}\log\log n+{1\over2}\log\gamma
 +\log2-{3\over2}+o(1).}
\]

Thus the claimed constant is confirmed without interchanging a limit across an unbounded two-dimensional logarithmic integrand.

## 4. New-half and cross constants

The corresponding factorial products on the two subdomains are

\[
\prod_{i=n}^{j-1}(j^2-i^2)
={(j-n)!(2j-1)!\over(j+n-1)!}
\quad(n\le j<2n),
\]

and

\[
\prod_{i=0}^{n-1}(j^2-i^2)
={j(j+n-1)!\over(j-n)!}
\quad(n\le j<2n).
\]

These include the empty-product and 0! endpoint cases correctly. Stirling errors summed over n terms are O(n log n)=o(n^2); the leading factorial expressions reduce to ordinary Riemann sums of t log t, extended continuously by 0 at t=0. Hence no diagonal or corner logarithmic singularity is left uncontrolled.

Independent integral evaluation gives

\[
I=\log2-3/2,
\quad B=9\log2-(9/2)\log3-3/2,
\quad C=(9/2)\log3-2\log2-3.
\]

For example, use F(z)=z^2 log z/2-3z^2/4, with F(0)=0, to integrate log(x+y); translation handles log(y-x). They obey

\[
I+B+C=8\log2-6=4I+4\log2,
\]

which independently checks the constant and logarithmic terms in the exact dyadic split. The stated three asymptotics in equation (17) are correct.

## 5. Wave limit and uniform diagonal control

On a shell b_i=s_(n-1+i), all gaps h_i are uniformly comparable to n log n: there exist fixed positive c,C such that

\[
c n\log n\le h_i\le Cn\log n
\]

for all large n and all shell indices. This remains true after the controlled perturbation in section 6 below. Let R=C/c.

For d=j-i>=2, the middle span M is at least (d-1) times the minimum gap. Using log(1+t)<=t,

\[
0\le{d^2\over4n^2}
\log\left(1+{h_i h_j\over M(M+h_i+h_j)}\right)
\le {R^2\over n^2}. \tag{E}
\]

There are at most delta*n^2 pairs with d<=delta*n, so that strip contributes at most R^2 delta, uniformly in n. This is the needed uniform integrability statement, not merely a pointwise limit away from the diagonal.

Outside that strip, set x=1+i/n and y=1+j/n. The shift by one index is O(1/n). Uniformly there,

\[
{f(nx)\over\gamma n^2\log n}\longrightarrow x^2,
\qquad {f'(nx)\over2\gamma n\log n}\longrightarrow x,
\]

and the middle span stays uniformly bounded away from zero after normalization. The rescaled summand n^2 times the weighted primitive therefore tends uniformly to xy/(x+y)^2. The ceiling error is O(1) per gap and is negligible under the gap normalization. Ordinary Riemann summation on the strip complement, then (E) with delta decreasing to zero, proves

\[
W_n\longrightarrow\int_{1<x<y<2}{xy\over(x+y)^2}\,dx\,dy.
\]

For a separate evaluation, twice this integral is the integral of the same symmetric function over [1,2]^2. Integrating first in one variable and then using the antiderivative

\[
G(s)={s^2+4\over2}\log(s+2)-{s^2+1\over2}\log(s+1)-s/2
\]

gives G(2)-G(1)=9log2-5log3-1/2. Therefore

\[
\boxed{w_*={9\log2-5\log3\over2}-{1\over4}.}
\]

The integrand lies between 2/9 and 1/4 on the domain, whose area is 1/2, so positivity is independently immediate. The source's stated decimal is consistent but unnecessary for the proof.

## 6. The controlled 3AP perturbation and its quantifiers

The source modifies each sufficiently late block of three indices using

\[
t_r=\lceil f(3r)\rceil,\quad
d_r=\left\lceil{f(3r+2)-f(3r)\over2}\right\rceil,
\quad(a_{3r},a_{3r+1},a_{3r+2})=(t_r,t_r+d_r,t_r+2d_r).
\]

The first block endpoint differs from f by less than 1, and the last differs by less than 3. Thus gaps between successive three-index blocks are positive after a fixed onset. The midpoint error is O(log j) by the second derivative of f, so a_j=f(j)+O(log j). Within each block d_r>0, giving a genuine three-term arithmetic progression. Every tail contains such a block, so no tail is Sidon.

To check the stated error summation, consider a perturbed pair with large upper index j. If i>=j/2, the smooth difference is at least c j(j-i) log j, and the endpoint perturbation is O(log j). Thus its relative error is O(1/[j(j-i)]). If i<j/2, the relative error is O(1/j^2). Both are uniformly small after a fixed onset, allowing the same bounds for the logarithmic error. Summing first over i and then j gives

\[
O\left(\sum_{j\le n}{\log j\over j}\right)=O(\log^2 n)=o(n^2).
\]

The new-half and cross sums are subsets of this estimate through 2n, so their asymptotics survive as well. Shell gap perturbations are O(log n)=o(n log n), preserving (E) and the off-diagonal limit for W.

Accordingly there is one fixed onset after which the modified ruler simultaneously obeys a fixed critical cap and every whole-prefix factorial inequality. The latter follows because its E_n tends to positive infinity, whereas the normalized log-factorial threshold tends to -(1+log2)/2. These quantifiers are stronger than a sequence of moving-onset finite examples, but the resulting infinite ruler is explicitly non-Sidon.

Finally W_(2^k)->w_*>0 and the Fejer weight sum is J/3+O(1). A finite-head/tail epsilon split proves the weighted remainder is o(J), giving w_*J/3+o(J) exactly as claimed.

## 7. Scope of the reviewed conclusion

This establishes a countermodel to the relaxation consisting of the fixed-onset cap, whole-prefix factorial log lower bounds, and exact geometric split identities. It does not preserve actual difference uniqueness, nor stronger inequalities involving selected subsets or their arithmetic compatibility. No step in the reviewed note establishes or refutes Q1. No material sign error or unproved singular-limit exchange remains in the displayed arguments once the explicit estimates above are supplied.
