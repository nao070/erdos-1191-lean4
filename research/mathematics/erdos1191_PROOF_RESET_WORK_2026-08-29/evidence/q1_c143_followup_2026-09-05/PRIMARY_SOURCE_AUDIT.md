# Primary-source audit for Q1, 2026-09-05

This is a bounded literature check, not a proof that all relevant literature has been found. No inspected source resolves Q1. The mathematical statements below were checked against primary arXiv pages and full HTML theorem statements during this audit.

## Exact question and access limitation

Write `A(x)=|A intersect [1,x]|`. Q1 asks whether every infinite integer Sidon set satisfies

`liminf_{x -> infinity} A(x) sqrt(log(x)/x) = 0`.

The [official problem page](https://www.erdosproblems.com/1191) and its [official history](https://www.erdosproblems.com/history/1191), as returned by the web search index, give precisely this question and label the problem OPEN. The indexed page says last edited 2026-04-06; its crawl is approximately two months old. Direct retrieval returned HTTP 403. Thus OPEN is the indexed official status, not a freshly retrieved live database status. The separate Q2 asks for one infinite Sidon set with positive liminf after multiplication by some positive power of log; that is a different quantifier and exponent question.

## O'Bryant I

[arXiv 2606.28651v3](https://arxiv.org/abs/2606.28651v3), revised 2026-07-26; [full text](https://arxiv.org/html/2606.28651v3).

Theorem 1: for every positive integer `g` and every `g`-Golomb ruler, with each positive difference represented at most `g` times,

`liminf A(n)/sqrt(n/log n) <= 2 sqrt(g)/sqrt(log 2)`.

Corollary 2: an infinite such ruler has `limsup a_n/(n^2 log n) >= log(2)/(2g)`. Neither bound gives the infinity required by the enumeration form of Q1. Theorem 3 constructs a ruler with `limsup A(n)/sqrt(n) >= sqrt(g/2)`; this is a limsup assertion. Its blocks use `q_{i+1}=q_i^3`, leaving large gaps. Section 5 asks about finer simultaneous prefix distributions. The proof uses block energy, a Sidon upper bound, and weighted Cauchy; it improves a constant, with no vanishing factor. The inspected bibliography lists Part III as in preparation, which does not certify its current publication status.

## O'Bryant II

[arXiv 2607.23795v1](https://arxiv.org/abs/2607.23795v1), submitted 2026-07-26; [full text](https://arxiv.org/html/2607.23795v1).

Theorem 1 holds for every positive even `h` and every `B_h` set (unordered `h`-term sums, repetitions allowed, are unique):

`liminf A(n)/(n/log n)^(1/h) <= [pi Gamma(1+h/2)^2 / (log(2) Gamma(1+1/h)^h)]^(1/h)`.

At `h=2`, `Gamma(2)=1` and `Gamma(3/2)=sqrt(pi)/2`, so this is exactly `2/sqrt(log 2)`, without improving the Q1 exponent or making the bound zero. Higher-even-`h` conclusions cannot be applied to an arbitrary Sidon set. The record contains v1 only; the HTML's internal date is 2026-08-24, so version metadata is preferable for identifying the inspected object.

## Additional directly relevant 2026 source

Christian Táfula, [arXiv 2607.20753v1](https://arxiv.org/abs/2607.20753v1), submitted 2026-07-22; [full text](https://arxiv.org/html/2607.20753v1).

Theorem 1.1(i), for `b=(c_1,-c_1,...,c_k,-c_k)` with all `c_i != 0`, states that `A(x)/(x/log x)^(1/(2k)) -> infinity` forces `x^-1 sum_{|n|<=x} r_{A,b}(n) -> infinity`, where representations use pairwise distinct coordinates. For a Sidon set and `b=(1,-1)`, each nonzero representation count is at most one, so this excludes divergent normalized density, not positive finite liminf. Part (ii) assumes the substantially stronger bound `A(x) >> x^(1/(2k))`. Theorem 1.2 is for `h>=3` and adds individual-gap hypotheses; these are not consequences supplied by the negation of Q1. Hence this paper supplies no missing zero-constant theorem. Its Fourier kernel/dyadic-block proof is a possible technique source, but the necessary critical-scale gain remains unproved.

## Exact remaining logical bridge (independent deduction)

Negating Q1 gives one infinite Sidon set and constants `c>0`, `X0` such that `A(x) >= c sqrt(x/log x)` for **all** `x>=X0`. A positive solution must contradict this for every `c>0`; an upper bound with a fixed positive constant leaves all smaller `c` untouched. In enumeration form, the negation is eventual `a_n <= C n^2 log n` for some finite `C`, whereas Q1 is equivalent to `limsup a_n/(n^2 log n)=infinity`.

Consequently a finite positive margin, even with exact complete phase coverage and a continuum of nearby weights, needs an additional theorem that applies to every hypothetical counterexample history/rank and combines its local gains without reusing a difference budget. No theorem checked above supplies that implication. A possible bridge would be a uniform, non-summable critical-scale surplus (or a rigorously compensating rank-dependent surplus), together with global charging and all-history validity. This is a proposed proof obligation, not a result established by these sources.

## Search scope and provenance

Queries covered official 1191 statements/history; arXiv infinite Sidon, thickness, log-scale results in 2026; O'Bryant Part III; and August/September infinite-Sidon updates. They surfaced the three audited papers and unrelated finite constructions. No applicable newer resolution was found in that bounded search; this does not establish absence. Local memory `MEMORY.md:98-100` only supplied navigation cues; the above three paper statements were rechecked live.
