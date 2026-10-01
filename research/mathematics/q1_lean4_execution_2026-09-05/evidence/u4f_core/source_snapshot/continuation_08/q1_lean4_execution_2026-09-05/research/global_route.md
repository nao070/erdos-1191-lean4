# Independent global route: exact difference-counting barrier

Date: 2026-09-05. Status: **Q1 unresolved; the theorems below concern a relaxation.**

This file is owned by the independent global-route agent. Existing C143 evidence was read only. No claim below has been entered into the canonical claim registry or checked by Lean. The purpose is to decide which global mechanisms can still reach Q1, not to treat an obstruction as a resolution.

## 1. Contract and source checks

The target is the original Q1: every infinite Sidon set of positive integers has

\[
\liminf_{x\to\infty} A(x)\sqrt{\log x/x}=0.
\]

The supplied `MASTER_PROMPT.md`, `TARGET_SPEC.md`, `C143_TO_Q1_REPORT.md`, and `GLOBAL_OBSTRUCTION_ANALYSIS.md` were read. In particular, the fixed-window obstruction is restricted to original positive one-use budgets; it does not prohibit all multiscale arguments. The bank and its independent replay are handled by the parent agent, not rerun here.

Primary material checked live:

* Kevin O'Bryant, *On the Thickness of Infinite Generalized Sidon Sets, I*, arXiv:2606.28651v3, version label 26 July 2026, https://arxiv.org/html/2606.28651v3 . The HTML title block also displays 24 August 2026; these dates are not silently identified. Theorem 1 gives a positive universal constant. Section 3.1 explicitly raises infinite binomial energy, reverse-martingale, and entropy possibilities without proving them.
* Christian Táfula, *Infinite Sidon-type sets for zero-sum linear forms*, arXiv:2607.20753v1, 22 July 2026, https://arxiv.org/html/2607.20753v1 . The matched-even theorem assumes a ratio tending to infinity; it does not convert a fixed positive lower ratio into a contradiction.
* David Conlon, Jacob Fox, Benny Sudakov, *Short proofs of some extremal results III*, Random Structures & Algorithms 57 (2020), 958–982, DOI 10.1002/rsa.20953, https://people.math.ethz.ch/~sudakovb/essays-in-combinatorics3.pdf . Section 4 gives an analogous finite-constant bound for minimum degrees of infinite K_{s,t}-free graphs. For s=2 it has the same logarithmic scale, so its stated conclusion does not settle Q1.

The following analytic calculation is derived here. An earlier project memory recorded numerical evidence for its constant and expressly left the asymptotic calculation unproved. The proof below supplies that calculation, with a sharper all-monotone-kernel consequence. It is not a novel theorem claim against the literature.

## 2. Exact asymptotic for the smooth integer model

Fix a real gamma>0. Discard finitely many initial indices if necessary to make

\[
s_n=\lceil\gamma n^2\log n\rceil,\qquad n\ge2,
\]

strictly increasing. This discarding changes the pair count below by O(sqrt(D/log D)), hence by o(D). Define the count **with multiplicity**

\[
F_\gamma(D)=\#\{(i,j):2\le i<j,\ 0<s_j-s_i\le D\}.
\]

**Theorem.** As D tends to infinity through positive reals,

\[
F_\gamma(D)\sim {\log2\over2\gamma}D. \tag{1}
\]

**Proof.** Put f(t)=gamma t^2 log t on t>=2 and first count real differences f(j)-f(i). Call their cumulative count G(D). Its finite value follows from f(j)-f(j-1) tending to infinity. Ceiling changes a difference by less than one, so

\[
G(D-1)\le F_\gamma(D)\le G(D+1). \tag{2}
\]

It therefore suffices to calculate G. Fix eta in (0,1/4), and write m_j(D) for the number of i<j counted at endpoint j. In the middle range

\[
D^{1/2+\eta}\le j\le D^{1-\eta},
\]

any admissible k=j-i satisfies k/j=o(1), uniformly: first f(j)-f(j/2)>D for all these j and large D, then the mean value theorem gives k<=D/f'(j/2)=O(D/(j log j)). Consequently f'(j-k)/f'(j)=1+o(1) uniformly. The real interval of admissible k has length D/f'(j)(1+o(1)), whence

\[
m_j(D)={D\over2\gamma j\log j}(1+o(1))+O(1). \tag{3}
\]

The total O(1) error is O(D^(1-eta))=o(D). Integral comparison therefore gives

\[
{1\over D}\sum_{D^{1/2+\eta}\le j\le D^{1-\eta}}m_j(D)
\longrightarrow {1\over2\gamma}
\log {1-\eta\over1/2+\eta}. \tag{4}
\]

We bound both omitted ranges rather than assume they are negligible. Choose a fixed B large enough in terms of gamma, and put L=B sqrt(D/log D). Endpoints j<L contribute at most L^2/2=O(D/log D). For every j>=L and large D, f(j)-f(j/2)>D, because

\[
f(j)-f(j/2)=\gamma j^2\left({3\over4}\log j+{1\over4}\log2\right).
\]

Thus any contributing i is greater than j/2. Since f'(j/2)>=(gamma/2)j log j for all sufficiently large j,

\[
m_j(D)\le {2D\over\gamma j\log j}. \tag{5}
\]

The adjacent-gap bound f(j)-f(j-1)<=D also forces j<=K_gamma D/log D for a fixed K_gamma. Apply (5) on the two remaining ranges. Dividing by D, their limsup is at most

\[
{2\over\gamma}\left(
\log{1/2+\eta\over1/2}+\log{1\over1-\eta}
\right). \tag{6}
\]

This tends to zero as eta decreases to zero. Equation (4), the nonnegativity of the remainders, and (6) squeeze G(D)/D to (log 2)/(2 gamma). Equation (2) proves (1). All bounds involve the infinite sequence; this is not an extrapolation from a finite run. QED.

Finite removal used at the start is harmless because pairs involving any one removed mark have count at most #{j:s_j<=D+O(1)}=O(sqrt(D/log D)).

The counting function S_gamma(x) satisfies

\[
S_\gamma(x)\sqrt{\log x/x}\longrightarrow\sqrt{2/\gamma}. \tag{7}
\]

Indeed log(s_n)/log n tends to 2 and s_(n+1)/s_n tends to 1, which first gives the limit at s_n and then throughout every gap.

## 3. Sharp triangular threshold and all decreasing kernels

For integer N define the total shifted-block triangular energy

\[
P_\gamma(N)=\sum_{i<j}(N-(s_j-s_i))_+.
\]

The exact identity P_gamma(N)=sum_(D=1)^(N-1) F_gamma(D), followed by (1), yields

\[
P_\gamma(N)\sim {\log2\over4\gamma}N^2,
\qquad
{P_\gamma(N)\over\binom N2}\longrightarrow {\log2\over2\gamma}. \tag{8}
\]

Thus the threshold gamma=log(2)/2 seen in the old finite experiment is the exact asymptotic threshold of this relaxation. Equality at the threshold does not settle the sign of lower-order errors.

More strongly, assume gamma>log(2)/2. By (1), F_gamma(D)<=D for every D>=D_0 for some finite D_0. Take a tail T of the smooth integer sequence whose successive gaps all exceed D_0. Then its cumulative difference count is zero below D_0 and at most F_gamma(D)<=D above D_0. Therefore

\[
F_T(D)\le D\quad\hbox{for every positive integer }D. \tag{9}
\]

For every finitely supported nonnegative **nonincreasing** weight w on the positive integers, let mu_D=w(D)-w(D+1)>=0. Finite summation gives

\[
\sum_{i<j} w(t_j-t_i)
=\sum_D\mu_D F_T(D)
\le\sum_D\mu_D D
=\sum_{d\ge1}w(d). \tag{10}
\]

So one positive-critical-density integer model satisfies simultaneously the budget inequalities for **all** such decreasing difference kernels. This covers arbitrary nonnegative sums or limits of the usual threshold and triangular kernels, with the limits justified by monotone convergence. It does not cover nonmonotone kernels, rank-dependent ownership, signed covariance identities, or pointwise r(d)<=1. Those retain information discarded here.

Equation (10) does not assert T is Sidon. Its Sidon status is not used or settled. Treating (10) as Sidonicity would erase the central difficulty.

For an explicit demonstration that the full system (9) does not imply Sidonicity even after positivity and infinitude are imposed, take P={1,3,11,13}. Its difference multiset is {2,2,8,10,10,12}, so F_P(D)<=D for every integer D, although 1+13=3+11. Since c=log(2)/(2 gamma)<1 and S_gamma(D+13)=o(D), choose D_0 sufficiently large that

\[
F_\gamma(D)+4S_\gamma(D+13)+6\le D\quad(D\ge D_0).
\]

Choose T with first mark greater than D_0+13 and all its gaps greater than D_0. Then P union T obeys (9): below D_0 only P contributes, and above D_0 the displayed bound controls internal, cross, and P pairs. It is an infinite non-Sidon set, has the positive limit (7), and satisfies every inequality (10). This is a counterexample to the **relaxed implication**, never a counterexample to Q1.

## 4. Other mechanisms examined, and why their stated versions do not close Q1

1. **Make the whole positive-difference set sparse.** The assertion that every infinite Sidon set has a difference set of density zero is false. A sparse infinite Sidon set can represent every positive difference: given a finite ruler, take its least missing d and add x,x+d with x sufficiently large and avoiding finitely many forbidden equalities. The new differences x-a and x+d-a are mutually distinct because d was missing from the old difference set; all remaining bad equalities exclude only finitely many x. Iteration supplies an infinite perfect difference set. This elementary construction gives no critical density bound and therefore does not settle Q1 in either direction.
2. **Pass to the sum graph and invoke an infinite C4-free theorem.** The primary Conlon–Fox–Sudakov conclusion retains a positive constant on precisely the square-root/logarithm scale. The existing theorem therefore does not supply the required vanishing factor. Translation structure would need an additional argument.
3. **Avoid all old differences when extending a finite prefix.** If disjoint sets P,B have Sidon union, the cross sums p+b are all distinct, so |P||B|<=diam(P+B)+1. With both counts of size sqrt(X/log X), this uses only O(X/log X) of an interval of length O(X). This particular packing estimate leaves a logarithmic factor and cannot by itself force the desired contradiction.
4. **Average over all long-distance cutoff scales.** Equations (9)–(10) show rigorously that an argument using only positive combinations of decreasing difference kernels cannot improve the positive constant to zero. A useful replacement must retain pointwise collision information or arithmetic/rank correlations before averaging it away.

The productive remaining target on this route is an inequality that converts global coherence of r_A(d) in {0,1} and d_ik=d_ij+d_jk into a loss beyond (9). No such inequality is proved in this file, and no uniform cap has been excluded.
