# Verified Research Report on Erdős Problem #1191

**STATUS: UNRESOLVED_AT_HARD_LIMIT**

> **Translation note.** This is a faithful English translation of the supplied Japanese research report. Mathematical notation, quantifiers, proof structure, and claim strength have been preserved. Technical terminology and bibliographic titles were cross-checked against current primary/preprint sources. No unresolved claim has been upgraded to a theorem.

This investigation adopted the stated success conditions and audit criteria, in particular: **finite computation is not to be treated as a resolution**; liminf/limsup statements must be distinguished rigorously from statements quantified over **all sufficiently large** \(x\); and in block constructions, **cross-scale difference collisions** must be checked completely. Primary literature and preprints through 2026 were searched, independent lemma proofs were developed, and finite computations were used for falsification and sanity checks. Nevertheless, the final theorem-strength gap required to settle Q1 and Q2 completely remains. The present execution environment does not provide asynchronous long-running autonomous research, and a single response also has practical limits on web retrieval; accordingly, only audited results are returned here, with the problem left unresolved.

## Strongest Verified Results

The most important achievements are: (i) an **exact translation of Q1 and Q2 into growth statements for the enumeration \(a_n\)**, with the logical relation between the two questions fully organized; and (ii) a proof that the quadratic deletion loss \(\binom m2\) in O'Bryant's separated-block pasting lemma is **worst-case sharp** if one assumes only the Sidon property and separation of the blocks.

In Erdős's 1980 paper on combinatorial number theory, after stating for a \(B_2\)-sequence that

\[
\limsup_{n\to\infty}\frac{a_n}{n^2\log n}>0,
\]

he asks whether this limsup is infinite, and also asks whether there exists a \(B_2\)-sequence satisfying

\[
a_n<c_1n^2(\log n)^{c_2}
\]

for all \(n\). He then offers \$1000 for “clearing up the problems” arising from these statements. Thus the modern Q1/Q2 formulation correctly isolates the two central issues in the original problem. [Erdős 1980]

**Exact \(A(x)\)–\(a_n\) conversion.** Let \(A=\{a_1<a_2<\cdots\}\) be an infinite Sidon set, and define

\[
L(A):=\liminf_{x\to\infty}A(x)\sqrt{\frac{\log x}{x}},
\qquad
R(A):=\limsup_{n\to\infty}\frac{a_n}{n^2\log n}.
\]

O'Bryant's 2026 theorem implies \(R(A)\ge \log 2/2>0\) in the Sidon case. [O'Bryant 2026] Moreover, in the extended real numbers,

\[
\boxed{
R(A)<\infty\quad\Longrightarrow\quad
L(A)^2=\frac{2}{R(A)}
}
\]

and

\[
\boxed{
L(A)=0
\quad\Longleftrightarrow\quad
R(A)=\infty.
}
\]

Therefore Q1 is **exactly equivalent** to

\[
\boxed{
\forall A\text{ infinite Sidon},\qquad
\limsup_{n\to\infty}\frac{a_n}{n^2\log n}=\infty.
}
\]

**Proof.** By the Sidon property, the positive differences among the first \(n\) terms,

\[
a_j-a_i\qquad(1\le i<j\le n),
\]

are all distinct. Hence

\[
\binom n2\le a_n-a_1<a_n.
\tag{1}
\]

On the other hand,

\[
f(x)=\sqrt{\frac{\log x}{x}}
\]

is decreasing for \(x>e\). If \(a_n\le x<a_{n+1}\), then \(A(x)=n\), so

\[
L(A)
=
\liminf_{n\to\infty}
n\sqrt{\frac{\log a_{n+1}}{a_{n+1}}}
=
\liminf_{n\to\infty}
n\sqrt{\frac{\log a_n}{a_n}},
\]

where the last equality follows from shifting the index by one and using \((n-1)/n\to1\). Therefore

\[
L(A)^2
=
\liminf_{n\to\infty}
\frac{n^2\log a_n}{a_n}.
\tag{2}
\]

Set

\[
R_n:=\frac{a_n}{n^2\log n}.
\]

If \(0<R(A)<\infty\), then (1) together with \(a_n\le Cn^2\log n\) gives

\[
\frac{\log a_n}{\log n}\longrightarrow2.
\]

Hence

\[
\frac{n^2\log a_n}{a_n}
=
\frac{\log a_n/\log n}{R_n},
\]

and therefore

\[
L(A)^2
=
\frac{2}{\limsup R_n}
=
\frac{2}{R(A)}.
\tag{3}
\]

If instead \(R(A)=\infty\), choose a subsequence for which \(R_{n_j}\to\infty\). Along this subsequence,

\[
\frac{n_j^2\log a_{n_j}}{a_{n_j}}
=
\frac{
2+\dfrac{\log\log n_j}{\log n_j}
+\dfrac{\log R_{n_j}}{\log n_j}
}{
R_{n_j}
}
\longrightarrow0,
\]

because \(\log t/t\to0\). Equation (2) gives \(L(A)=0\). The converse follows immediately from (3). This proves the equivalence, including the quantifiers.

**Exact sequence formulation of Q2.** For fixed \(c>0\),

\[
\liminf_{x\to\infty}
\frac{A(x)(\log x)^c}{\sqrt x}>0
\tag{4}
\]

is equivalent to

\[
\boxed{
a_n=O\!\left(n^2(\log n)^{2c}\right).
}
\tag{5}
\]

Consequently,

\[
\boxed{
\text{Q2}
\Longleftrightarrow
\exists \beta>0,\ \exists\text{ an infinite Sidon set }A:
\quad
a_n=O\!\left(n^2(\log n)^\beta\right).
}
\tag{6}
\]

Up to absorbing finitely many initial terms into the constant, this is the same problem as Erdős's formula (6) from 1980. [Erdős 1980]

Indeed, (4) implies that for all sufficiently large \(n\),

\[
n\ge \delta\frac{\sqrt{a_n}}{(\log a_n)^c},
\]

and hence

\[
a_n\le \delta^{-2}n^2(\log a_n)^{2c}.
\tag{7}
\]

For large \(y\), \((\log y)^{2c}\le y^{1/2}\), so (7) first yields \(a_n=O(n^4)\), hence \(\log a_n=O(\log n)\). Substituting this back into (7) gives (5).

Conversely, suppose

\[
a_n\le Kn^2(\log n)^\beta,
\]

and put \(n=A(x)\). Then

\[
a_n\le x<a_{n+1}
\le K(n+1)^2(\log(n+1))^\beta.
\]

Since \(n\le x\), we also have \(\log(n+1)\ll\log x\). Therefore

\[
A(x)=n
\gg \frac{\sqrt x}{(\log x)^{\beta/2}},
\]

which is (4) with \(c=\beta/2\).

The logical relationship between Q1 and Q2 is therefore completely determined.

| Statement | Rigorous consequence |
|---|---|
| Q1 is false | There exists \(A\) with \(L(A)>0\). Hence Q2 is true with \(c=\tfrac12\). |
| Q2 is true with \(c=\tfrac12\) | Then \(L(A)>0\), so Q1 is false. |
| Q2 is false | Q1 must be true. |
| Q1 is true and Q2 is true | This is logically possible, but the exponent in Q2 must satisfy \(c>\tfrac12\). |

O'Bryant further proves, for \(g=1\), that

\[
L(A)\le \frac{2}{\sqrt{\log2}}.
\]

Therefore a Q2 witness with \(c<1/2\) is impossible. Indeed, along a subsequence \(x_j\) realizing the relevant upper bound,

\[
\frac{A(x_j)(\log x_j)^c}{\sqrt{x_j}}
\ll(\log x_j)^{c-1/2}\to0.
\]

The equivalent sequence-form corollary of O'Bryant is

\[
\limsup_{n\to\infty}\frac{a_n}{n^2\log n}
\ge\frac{\log2}{2}.
\]

The constants agree exactly. [O'Bryant 2026]

## The Precise Remaining Gap

Version 3 of O'Bryant's 2026 preprint, revised on 26 July 2026, proves for every \(g\)-Golomb ruler that

\[
\liminf_{x\to\infty}
\frac{A(x)}{\sqrt{x/\log x}}
\le
\frac{2\sqrt g}{\sqrt{\log2}},
\]

with \(g=1\) giving the Sidon case relevant here. The proof estimates the block energy

\[
E=\sum_\ell F_\ell^2
\]

for the counts \(F_\ell\) in blocks of length \(N\), bounding it above using difference multiplicities and below using a weighted Cauchy–Schwarz inequality. O'Bryant states that this one-scale energy/Cauchy argument has essentially been fully optimized and explicitly points to averaging across multiple scales, martingale/reverse-martingale structure, and entropy as possible sources of further improvement. [O'Bryant 2026]

Thus, on the universal side, the remaining proof obligation is not a mere improvement of the constant. One must prove

\[
\boxed{
\forall C>0,\ \forall\text{ infinite Sidon }A,\ 
\exists^\infty n:\quad
a_n>Cn^2\log n.
}
\tag{8}
\]

Equivalently, one needs a **multiscale gain that can make the effective constant arbitrarily large**.

On the constructive side, Cilleruelo's explicit discrete-logarithm construction achieves

\[
A(x)=x^{\sqrt2-1+o(1)},
\]

and O'Bryant's 2026 paper also records this as the current benchmark for an infinite Sidon set. [Cilleruelo 2014; O'Bryant 2026] Since

\[
\frac12-(\sqrt2-1)
=
\frac32-\sqrt2
=
0.085786\ldots,
\]

this is not merely a missing logarithmic factor relative to Q2. For every fixed \(c\),

\[
\frac{x^{\sqrt2-1+o(1)}}{\sqrt{x}/(\log x)^c}
=
x^{-(3/2-\sqrt2)+o(1)}(\log x)^c
\longrightarrow0.
\]

Thus the constructive route requires a genuinely new **power-exponent breakthrough**.

The obstruction can be located even more precisely inside Cilleruelo's proof. In the deletion argument, ignoring polynomial factors, the number of bad primes at level \(k\) satisfies

\[
|\mathcal B_k|
\lesssim
2^{\left(\frac{2c}{1-c}-1\right)k^2},
\]

whereas the available prime block has size

\[
|\mathcal P_k|
\asymp
\frac{2^{ck^2}}{k^2}.
\]

To keep the bad set at most comparable in size, one therefore needs

\[
\frac{2c}{1-c}-1\le c.
\]

The boundary equation is

\[
c^2+2c-1=0,
\]

so

\[
c=\sqrt2-1.
\]

This is exactly the exponent produced by the published construction. [Cilleruelo 2014] At the target value \(c=1/2\), the bad-set exponent is \(1\), whereas the available-prime exponent is \(1/2\). Thus the existing counting argument is too large by a factor on the scale of \(2^{k^2/2}\). This route therefore also requires an **exponential saving in the collision count**, not merely the polishing of logarithmic factors.

The possibilities for a complete resolution can consequently be compressed into the following three cases.

| Resolution type | Required theorem-strength step |
|---|---|
| Q1 true, Q2 false | Prove universally that \(a_n\neq O(n^2(\log n)^\beta)\) for every fixed \(\beta\). |
| Q1 true, Q2 true | Prove (8), while also constructing a Sidon set with \(a_n=O(n^2(\log n)^\beta)\) for some \(\beta>1\). |
| Q1 false, Q2 true | Construct a critical Sidon set with \(a_n=O(n^2\log n)\), equivalently \(A(x)\gg\sqrt{x/\log x}\) for all sufficiently large \(x\). |

The fourth logical possibility, Q1 false and Q2 false, is ruled out by the exact equivalences established above.

## Approach Registry

| Status | Approach | What was actually obtained | Exact reason for stopping |
|---|---|---|---|
| **PROVED** | Quantifier-preserving conversion \(A(x)\leftrightarrow a_n\) | Q1 \(\Longleftrightarrow R(A)=\infty\); Q2 \(\Longleftrightarrow\) polylogarithmic upper growth of \(a_n\) | Complete |
| **BLOCKED** | One-scale block energy / Cauchy–Schwarz | Universal constant \(2/\sqrt{\log2}\) | Produces only a fixed constant; Q1 requires an unbounded gain. [O'Bryant 2026] |
| **ACTIVE** | Multiscale entropy / reverse martingale | O'Bryant explicitly identifies a conditional-expectation structure | No theorem yet combines energies across scales without double-counting the same differences. [O'Bryant 2026] |
| **BLOCKED** | Separated finite-block pasting | O'Bryant Lemma 9 combines blocks after deleting at most \(\binom m2\) points when \(g=1\) | The present report proves that this quadratic loss is worst-case sharp as a black-box statement. [O'Bryant 2026] |
| **BLOCKED** | Ruzsa/Cilleruelo discrete-logarithm digits | \(x^{\sqrt2-1+o(1)}\) | The bad-collision exponent saturates exactly at \(\sqrt2-1\). [Cilleruelo 2014] |
| **BLOCKED** | Build \(B_2[g]\) first, then thin to \(B_2[1]\) | Cilleruelo: \(a_n\le2g\,n^{2+1/g}\) | Every fixed \(g>1\) still leaves a power gap; no density-preserving \(g\to1\) reduction is known. [Cilleruelo 2017] |
| **BLOCKED** | Compactness / diagonal limit | Compactness of Sidon and \(B_2[g]\) sets is useful for maximizing several extremal functionals | A finite extremizer need not possess a compatible dense prefix; an all-scale liminf condition requires a separate extension theorem. [Riblet–Schehr 2026] |
| **ACTIVE** | Entropy / combinatorial large sieve | Super-polylogarithmic savings for structured Sidon problems | The current theorem assumes algebraic splitting coming from squares, norm forms, etc.; it does not directly apply to arbitrary \(A\subset\mathbb N\). [Croot–Mao–Pohoata–Sheffer–Yip 2026] |
| **ACTIVE** | Zero-sum Fourier / dyadic blocks | Táfula recovers the classical critical threshold in the case involving \((1,-1)\) | It rules out \(A(x)/\sqrt{x/\log x}\to\infty\), but does not rule out a fixed positive liminf. [Táfula 2026] |
| **ABANDONED** | Independent Bernoulli selection + naive alteration | At critical density, the expected number of conflicts greatly exceeds the expected number of selected points | A one-conflict-one-deletion first-moment argument cannot preserve the desired density. |

Táfula's 2026 theorem was examined in particular detail. For a matched-even zero-sum vector

\[
\mathbf b=(c_1,-c_1,\dots,c_k,-c_k),
\]

it proves that if

\[
\frac{A(x)}{(x/\log x)^{1/(2k)}}\to\infty,
\]

then

\[
\frac1x\sum_{|n|\le x}r_{A,\mathbf b}(n)\to\infty.
\]

Its proof sums nonnegative Fourier integrals over dyadic blocks in the index set. When \(k=1\) and \(\mathbf b=(1,-1)\), the number of difference representations for a Sidon set is bounded, so the theorem recovers the classical finite-liminf density restriction. However, it does **not** contradict the negation of Q1, namely the possibility that the set stays dense at every sufficiently large scale by a fixed positive constant multiple of \(\sqrt{x/\log x}\). [Táfula 2026]

The 2026 combinatorial large sieve of Croot, Mao, Pohoata, Sheffer, and Yip supplies a new mechanism structurally close to Q1: local branching among residue classes creates many modular collisions, while a global bounded-multiplicity condition controls how many such collisions can actually occur. For Sidon subsets of the squares it yields

\[
|A|
\le
N\exp\!\left(
-c\frac{\log N}{\log\log N}
\right),
\]

a super-polylogarithmic saving, and the paper also develops an entropic version of the method. The load-bearing hypothesis, however, is the **algebraic splitting** arising from squares or norm forms. It is not presently available for an arbitrary Sidon subset of the integers. [Croot–Mao–Pohoata–Sheffer–Yip 2026]

## Counterexamples and Computational Checks

First, the idea that Sidon-ness is automatically preserved by placing blocks “sufficiently far apart” is already false in the smallest example:

\[
V=\{0,1\},\qquad W=\{T,T+1\}.
\]

Each block is Sidon individually, but the positive difference \(1\) occurs in both. Hence \(V\cup W\) is not Sidon for any \(T\). Making the separation arbitrarily large does nothing to eliminate collisions between **internal differences** of the two blocks.

More substantially, the following lemma was proved independently in this investigation.

**Sharpness Lemma for the Quadratic Deletion Loss.**  
Let \(V\subset\mathbb Z\) be any finite Sidon set with \(m\ge2\) elements, and let its set of positive differences be

\[
D(V)=\{d_1,\dots,d_e\},
\qquad
e=\binom m2.
\]

Then there exists a finite Sidon set \(W\) with \(2e\) elements, translatable arbitrarily far to the right, such that the forbidden-pair graph associated with

\[
D(W)\cap D(V)
\]

is exactly a matching of \(e\) pairwise vertex-disjoint edges. Consequently, every \(W^*\subseteq W\) satisfying

\[
D(W^*)\cap D(V)=\varnothing
\]

obeys

\[
|W^*|\le e,
\]

so at least

\[
\boxed{\binom m2}
\]

points must be deleted from \(W\).

This shows that the guarantee in O'Bryant's Lemma 9 for \(g=1\),

\[
|W^*|\ge |W|-\binom{|V|}{2},
\]

**cannot be improved uniformly from the information that \(V\) and \(W\) are Sidon and sufficiently separated alone**. [O'Bryant 2026]

**Proof.** Let \(D=\max_i d_i\), and choose an integer \(B>4D+4\). For \(1\le i\le e\), put

\[
x_i=B^i,
\]

and define

\[
W_0=\{x_i,\ x_i+d_i:1\le i\le e\}.
\]

The difference between the two points in the same \(i\)-block is \(d_i\), and these differences are all distinct.

For distinct blocks with \(j>i\), every positive cross-block difference has the form

\[
B^j-B^i+\varepsilon d_j-\eta d_i,
\qquad
\varepsilon,\eta\in\{0,1\}.
\tag{9}
\]

First, the base differences \(B^j-B^i\) are all distinct. Indeed,

\[
B^j-B^i=B^i(B^{j-i}-1)
\]

is divisible by \(B^i\) but not by \(B^{i+1}\). Thus equality of two base differences first forces \(i=i'\), and then \(j=j'\).

Moreover, any two distinct base differences are multiples of \(B\), so their absolute difference is at least \(B\). By contrast, the difference between two perturbation terms in (9) has absolute value at most \(2D\). Since \(B>4D\), two expressions of the form (9) attached to different base differences cannot coincide.

For a fixed pair \((j,i)\), the four perturbations are

\[
0,\quad d_j,\quad -d_i,\quad d_j-d_i.
\]

Because \(d_i,d_j>0\) and \(d_i\ne d_j\), these four values are distinct.

Finally, every cross-block difference is greater than

\[
B^2-B-D>D,
\]

so it cannot equal any within-block difference \(d_k\le D\). Therefore all positive differences in \(W_0\) are distinct, and \(W_0\) is Sidon.

Furthermore, the only differences of \(W_0\) that lie in \(D(V)\) are exactly

\[
(x_i+d_i)-x_i=d_i.
\]

Hence the forbidden graph is precisely the matching

\[
\{x_i,x_i+d_i\},
\qquad i=1,\dots,e.
\]

To destroy every edge of this matching, at least one endpoint of each edge must be removed. Thus at least \(e=\binom m2\) points must be deleted.

Finally, translating \(W_0\) by \(T\), and setting \(W=T+W_0\), preserves all internal differences. Since \(T\) can be arbitrarily large, one can also satisfy the separation hypothesis in O'Bryant's Lemma 9,

\[
W_1-V_2\ge\max\{V_2,\operatorname{diam}W\}.
\]

This completes the proof.

The lemma does not solve #1191, but it gives an important **search-space reduction**. A black-box constructive strategy of the form “take an arbitrary dense finite Sidon block, place it far away, and delete only a few points” has a principled limitation. Any successful pasting theorem must exploit **additional algebraic structure, randomness, or variable dilation** in the candidate blocks, and must seek a large independent set in the forbidden-difference graph rather than controlling only its edge count.

The lemma was also sanity-checked by finite computation. Taking

\[
V=\{0,1,4,10\},
\qquad
D(V)=\{1,3,4,6,9,10\},
\]

and \(B=41\), the construction gives a 12-point set \(W_0\). Exhaustive checking of all positive differences found no duplicates, and the only differences lying in \(D(V)\) were the six prescribed disjoint pairs. This computation is not a substitute for the proof; it is a finite audit intended to detect indexing or sign errors.

**Check of naive random alteration.**  
Select each integer in \([N]\) independently with probability

\[
p=N^{-1/2}(\log N)^{-c}.
\]

Then

\[
\mathbb E|S|
=
Np
=
\frac{\sqrt N}{(\log N)^c}.
\]

On the other hand, there are \(\Theta(N^3)\) nontrivial equations

\[
a+b=c+d
\]

with four distinct integers, so the expected number of conflicts is

\[
\Theta(N^3p^4)
=
\Theta\!\left(
\frac{N}{(\log N)^{4c}}
\right).
\]

The ratio of the expected number of conflicts to the expected number of selected points is

\[
\Theta\!\left(
\frac{\sqrt N}{(\log N)^{3c}}
\right)\to\infty.
\]

Therefore the naive first-moment scheme “choose independently, then delete one point from each conflict” does not preserve the critical polylogarithmic density. This does **not** rule out a random greedy process, a local-lemma argument, a container method, or a construction in which conflicts are highly concentrated.

## Literature Audit: Current Frontier

The following ledger records the principal sources whose statements and assumptions were checked against primary sources or author preprints.

| Primary source | Precisely useful content | Proof mechanism | Assessment for #1191 |
|---|---|---|---|
| Erdős, 1980 | \(\limsup a_n/(n^2\log n)>0\); asks whether the limsup is \(\infty\); asks for a sequence with polylogarithmic upper growth | Classical Sidon-density argument | **Original source of the problem itself.** |
| Cilleruelo, *Infinite Sidon sequences* | Explicit construction with \(A(x)=x^{\sqrt2-1+o(1)}\) | Mixed-radix digits + discrete logarithms + bad-prime deletion | **Constructive frontier.** The collision-count barrier is \(\sqrt2-1\). |
| O'Bryant, arXiv:2606.28651v3 | For a \(g\)-Golomb ruler, \(L\le2\sqrt g/\sqrt{\log2}\); equivalently \(\limsup a_n/(n^2\log n)\ge\log2/(2g)\) | Block energy + weighted Cauchy–Schwarz | **Most direct recent improvement found on the universal side.** It does not make the Q1 constant zero. |
| O'Bryant, Lemma 9 | Combines separated \(V,W\) after deleting at most \(g\binom{|V|}{2}\) elements | Delete overlaps between old and new internal differences | Concrete entry point for cross-scale construction; for \(g=1\), the quadratic loss is worst-case sharp by the lemma proved in this report. |
| Táfula, 2026 | Zero-sum linear forms; in particular the vector \((1,-1)\) reproduces the classical critical \(x/\log x\) threshold | Dyadic index blocks + nonnegative Fourier integral | A multiscale/Fourier candidate, but the current statement yields only a finite liminf constant. |
| Cilleruelo, *A greedy algorithm for \(B_h[g]\) sequences* | \(a_n\le2g\,n^{h+(h-1)/g}\) | Greedy construction with bounded representation multiplicity | For \(h=2\), the exponent is \(2+1/g\), arbitrarily close to \(2\), but \(g>1\) and no reduction to Sidon with comparable density is known. |
| Fabian–Rué–Spiegel | Strong infinite Sidon and \(B_h\) constructions | Cilleruelo-type construction + deletion | Provides additional separation robustness, but at \(\alpha=0\) does not cross the exponent frontier. |
| Croot–Mao–Pohoata–Sheffer–Yip, 2026 | Super-polylogarithmic saving for Sidon sets on squares; entropic large sieve | Modular splitting + collision entropy | **Promising new universal-side mechanism**, but the present hypotheses are much more structured than an arbitrary integer Sidon set. |
| Riblet–Schehr, 2025/26 | Compactness of Sidon and \(B_2[g]\) sets; existence of extremizers for certain functionals | Compactness | Does not give a compatible dense extension, so it cannot transfer a finite extremizer directly to Q2's all-scale liminf condition. |
| Niu, 2026 | Strengthens Pilatte-type asymptotic Sidon-basis constructions using function-field convolution estimates | Ruzsa/Pilatte skeleton + deep Sawin-type analytic input | Not a density theorem, but adjacent evidence that strong analytic input can be combined with a Ruzsa-type algebraic skeleton. |

Táfula's paper first appeared as a preprint in July 2026 and was subsequently published in *Monatshefte für Mathematik*. The matched-even case of Theorem 1.1 was checked not merely at the citation level but at the level of proof mechanism. The proof sums representation lower bounds obtained from disjoint dyadic blocks

\[
\{a_{2^m+1},\ldots,a_{2^{m+1}}\}
\]

and uses nonnegativity of the Fourier integrand. This decomposition is genuinely different from O'Bryant's interval-block energy method, so combining the two remains conceptually interesting. At present, however, both mechanisms yield only a **finite constant at the same critical scale**; no additional divergence has been identified that would exclude every positive liminf. [Táfula 2026; O'Bryant 2026]

The compactness route requires a separate caution. The Sidon property itself is defined by finitely forbidden configurations and is therefore highly compatible with pointwise or diagonal limits. But Q2 requires

\[
A(x)\ge C\frac{\sqrt x}{(\log x)^c}
\qquad
\text{for every sufficiently large }x.
\]

This condition is not preserved merely by taking a large finite Sidon extremizer at one terminal scale. If the mass of a finite set drifts to the right, a diagonal limit can become sparse on every fixed initial interval. Thus a compactness argument would first need a **nested feasibility theorem** of the form “every existing prefix admits a dense extension,” rather than merely the existence of a dense finite set. No such missing extension theorem has been proved here.

## Highest-Value Next Directions

To avoid rewriting the same missing lemma in different notation, the next research wave should **change the underlying mechanism**.

| Priority | Direction | Why this is not merely a restatement of a previous failure | First concrete milestone to prove |
|---|---|---|---|
| Highest | **Multiscale difference entropy** | O'Bryant uses \(L^2\)-energy at one partition scale; Croot et al. use entropy/collision accounting across many moduli. This would accumulate information across scales. | Prove an inequality bounding the sum of entropy deficits across several nested partitions by the global Sidon difference budget, without double-counting the same difference pairs. |
| Highest | **Forbidden-difference graph of algebraic finite Sidon blocks** | Black-box deletion is quadratically sharp, but Singer/Bose/Cilleruelo blocks possess extra structure. | Average over affine/dilation parameters and quantify whether the graph induced by the old difference set \(D(V)\) has an independent set of size \((1-o(1))|W|\), or loses only polylogarithmically. |
| High | **Deep arithmetic saving in Cilleruelo's collision count** | The barrier is now quantitative rather than a vague “density deficit”: a saving on the scale \(2^{k^2/2}\) is required. | At \(c=1/2\), reduce the bad-prime count from the current \(2^{k^2}\)-scale to at most \(2^{(1/2+o(1))k^2}\) via a new bilinear or convolution estimate. |
| High | **Dynamic random greedy Sidon process** | Naive Bernoulli alteration fails, but random greedy selection avoids forbidden differences dynamically, so the conflict structure is fundamentally different. | Control pseudorandomness of the forbidden set and survival probability of available integers up to the \(n^2\operatorname{polylog}n\) scale. |
| Medium-high | **Táfula Fourier blocks × O'Bryant shifted blocks** | One decomposition is dyadic in the index, the other is shifted in physical space; they are not the same partition. | Determine whether the multiplicity with which the two local lower bounds count the same differences can be uniformly controlled while producing a lower bound that grows with the number of scales. |

The first direction is the most concrete on the universal side. In O'Bryant's proof,

\[
F_\ell
=
A(t^*+\ell N)-A(t^*+(\ell-1)N)
\]

can be interpreted as the conditional expectation of the indicator of the set with respect to the \(\sigma\)-algebra generated by a partition into intervals of length \(N\). O'Bryant also notes that near-equality in the Cauchy–Schwarz step requires the \(F_\ell\) to be approximately proportional to a particular weight profile, with no evident reason for such smoothness to persist across scales. [O'Bryant 2026] The promising target is therefore **not** to repeat the same Cauchy–Schwarz estimate independently at many scales, but to link **entropy increment/decrement for nested conditional expectations** to uniqueness of differences.

On the constructive side, the quadratic-sharpness lemma proved here significantly narrows the search target. Rather than attempting a better deletion theorem for arbitrary \(W\), it is more informative to study the forbidden-difference graph

\[
H_{V,W}:
\quad
ww'\in E(H)
\Longleftrightarrow
|w-w'|\in D(V)
\]

along the affine parameter space of Bose/Singer/discrete-logarithm blocks. Edge count alone is not the relevant statistic. O'Bryant's deletion argument effectively uses a vertex-cover upper bound obtained by deleting one endpoint per forbidden edge, whereas the quantity of real interest is

\[
\alpha(H_{V,W}),
\]

the independence number of the graph. The matching counterexample constructed here shows that for arbitrary \(W\), one can have \(\alpha=|W|/2\). It has not been proved that the same worst case persists throughout the affine orbit of an algebraic block.

The next requirement on the Cilleruelo route is likewise clear. There is little value in trying to move the published divisor-counting/deletion proof mechanically from \(c=0.4142\ldots\) to \(0.49\). At \(c=1/2\), the argument is short by an exponential factor corresponding to an exponent saving of \(1/2\). Pilatte-type Sidon-basis constructions, together with Niu's 2026 use of deep function-field convolution estimates, show that it is at least possible in principle to combine a Ruzsa-type algebraic skeleton with much stronger analytic input. [Pilatte 2024; Niu 2026] To transfer such technology to #1191, one would need a new estimate that averages a family of divisor/congruence constraints arising from **repeated pair-sum collisions**, rather than controlling basis representations.

## Formalization Status

A complete solution has not been obtained, so Q1 and Q2 as a whole cannot yet be closed as Lean theorems. However, the reductions and obstruction lemma proved in this investigation do not depend on any unresolved theorem-strength assumption and are independently formalizable results.

The dependency structure is as follows.

```text
Sidon sum uniqueness
        │
        ▼
positive-difference uniqueness
        │
        ├──────────────► binom(n,2) ≤ a_n-a_1
        │                         │
        │                         ▼
        │                 log(a_n)/log(n) → 2
        │                         │
        ▼                         ▼
A(x) constant on [a_n,a_{n+1}) ─► Q1 enumeration equivalence
                                  │
                                  ▼
                  L(A)=0 ↔ limsup a_n/(n² log n)=∞

eventual positive liminf
        │
        ├──► a_n ≤ C n²(log a_n)^(2c)
        │                   │
        │                   ▼
        │             log a_n = O(log n)
        │                   │
        ▼                   ▼
Q2 ↔ a_n=O(n²(log n)^β), β=2c
```

The dependency DAG for the pasting obstruction is even more finite and combinatorial.

```text
D(V) has e=binom(m,2) distinct differences
                    │
                    ▼
       choose B>4 max D(V)
                    │
                    ▼
 W={B^i, B^i+d_i : 1≤i≤e}
          │                  │
          ▼                  ▼
base differences unique   perturbations separated
          └────────┬─────────┘
                   ▼
                 W Sidon
                   │
                   ▼
forbidden graph = e-edge matching
                   │
                   ▼
 every compatible W* deletes at least e points
```

The first finite statement to formalize in Lean should conceptually be

\[
\texttt{quadratic\_pasting\_loss\_sharp}:
\]

> For every finite Sidon set \(V\subset\mathbb Z\) with \(|V|=m\ge2\), there exists a finite Sidon set \(W\) with \(|W|=2\binom m2\) such that every \(W^*\subseteq W\) whose positive-difference set is disjoint from that of \(V\) satisfies \(|W^*|\le\binom m2\).

This statement contains no limiting argument or real analysis; it is entirely finite, involving finite sets, integer differences, and a matching. It is therefore the most robust first target for formalization.

Next one can formalize

\[
\texttt{q2\_iff\_polylog\_enumeration\_growth}
\]

as

\[
\left[
\liminf_{x\to\infty}
\frac{A(x)(\log x)^c}{\sqrt x}>0
\right]
\Longleftrightarrow
\left[
a_n=O(n^2(\log n)^{2c})
\right].
\]

This requires standard analysis concerning eventual inequalities and \(\log y=o(y^\varepsilon)\).

Finally, one can target

\[
\texttt{q1\_iff\_enumeration\_limsup\_infinite}
\]

in the form

\[
\liminf_{x\to\infty}
A(x)\sqrt{\frac{\log x}{x}}=0
\Longleftrightarrow
\limsup_{n\to\infty}
\frac{a_n}{n^2\log n}=\infty.
\]

The most fragile part here is the passage from the step-function intervals of \(A(x)\) to the enumeration \(a_n\), together with the treatment of an extended-real limsup. These points were audited explicitly above.

The final audit conclusion is clear. None of O'Bryant's universal theorem, Cilleruelo/Ruzsa-type constructions, Táfula's Fourier theorem, \(B_2[g]\) constructions, compactness, or entropy/large-sieve methods currently yields a theorem that completely settles Q1 or Q2. Conversely, the exact \(A(x)\)–\(a_n\) equivalence, the polylogarithmic-growth equivalence for Q2, and the worst-case sharpness of the quadratic deletion loss in separated pasting are independent of unresolved lemmas and substantially narrow both the quantifier structure and the constructive bottleneck of any candidate solution route. Therefore, **Erdős Problem #1191 cannot be classified as resolved on the basis of this investigation, and there is no mathematical justification here for marking it RESOLVED**.

## References and Terminology Sources

The following entries were used to verify English terminology, paper titles, and the literature statements referenced above.

1. **Erdős, Paul.** “A survey of problems in combinatorial number theory.” *Annals of Discrete Mathematics* **6** (1980), 89–115. Erdős Problem #1191 summary and provenance: https://www.erdosproblems.com/1191

2. **Cilleruelo, Javier.** “Infinite Sidon sequences.” *Advances in Mathematics* **255** (2014), 474–486. Preprint: https://arxiv.org/abs/1209.0326

3. **O'Bryant, Kevin.** “On the Thickness of Infinite Generalized Sidon Sets, I.” arXiv:2606.28651v3 (2026). https://arxiv.org/abs/2606.28651

4. **Táfula, Christian.** “Infinite Sidon-type sets for zero-sum linear forms.” *Monatshefte für Mathematik* (2026). DOI: 10.1007/s00605-026-02211-4. Preprint: https://arxiv.org/abs/2607.20753

5. **Cilleruelo, Javier.** “A greedy algorithm for \(B_h[g]\) sequences.” *Journal of Combinatorial Theory, Series A* **150** (2017), 323–327. Preprint: https://arxiv.org/abs/1601.00928

6. **Fabian, David; Rué, Juanjo; Spiegel, Christoph.** “On strong infinite Sidon and \(B_h\) sets and random sets of integers.” *Journal of Combinatorial Theory, Series A* **182** (2021), Article 105460. Preprint: https://arxiv.org/abs/1911.13275

7. **Croot, Ernie; Mao, Junzhe; Pohoata, Cosmin; Sheffer, Adam; Yip, Chi Hoi.** “A combinatorial large sieve for Sidon sets, distances, and norm forms.” arXiv:2606.17487 (2026). https://arxiv.org/abs/2606.17487

8. **Riblet, Robin; Schehr, Titien.** “Existence of a Sidon set for the distinct distance constant.” *Acta Mathematica Hungarica* (2026). DOI: 10.1007/s10474-026-01604-z. Preprint: https://arxiv.org/abs/2505.20851

9. **Niu, Wei.** “An asymptotic Sidon basis of order \(3-\eta\).” arXiv:2607.11351v2 (2026). https://arxiv.org/abs/2607.11351

10. **Pilatte, Cédric.** “A solution to the Erdős–Sárközy–Sós problem on asymptotic Sidon bases of order 3.” *Compositio Mathematica* **160** (2024), 1418–1432. DOI: 10.1112/S0010437X24007140.

11. **Ruzsa, Imre Z.** “An infinite Sidon sequence.” *Journal of Number Theory* **68** (1998), 63–71. DOI: 10.1006/jnth.1997.2192.
