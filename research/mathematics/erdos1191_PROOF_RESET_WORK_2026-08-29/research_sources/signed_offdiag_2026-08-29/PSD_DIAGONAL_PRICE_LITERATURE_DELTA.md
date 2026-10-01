# Weighted PSD diagonal-price literature delta

Search date: 2026-08-30 (Asia/Tokyo)  
Evidence label: `TARGETED_PRIMARY_SOURCE_QUALIFIED_SYNTHESIS`

## Exact interface searched

For a symmetric entrywise nonnegative matrix `A` with zero diagonal and
positive weights `g_i`, the Route-C coefficient completion reduces to

\[
 \min_d\left\{\sum_i g_i d_i:
       \operatorname{Diag}(d)-\frac A2\succeq0\right\}.
 \tag{1}
\]

Writing `s_i=sqrt(g_i)`, the project uses the explicit primal candidate

\[
 d_i^*=\frac{(As)_i}{2s_i}
 \tag{2}
\]

and the dual

\[
 \max\left\{\frac12\langle A,X\rangle:
       X\succeq0,\ \operatorname{diag}X=g\right\}.
 \tag{3}
\]

The slack has the edge-square representation

\[
 z^T\left(\operatorname{Diag}(d^*)-\frac A2\right)z
 =\frac12\sum_{i<j}A_{ij}s_i s_j
   \left(\frac{z_i}{s_i}-\frac{z_j}{s_j}\right)^2,
 \tag{4}
\]

while `X^*=ss^T` is dual feasible.  Since every feasible `X` satisfies
`X_(ij)<=sqrt(g_i g_j)` and `A_(ij)>=0`, the rank-one point is optimal and

\[
 \min (1)=\sum_{i<j}A_{ij}\sqrt{g_i g_j}.
 \tag{5}
\]

The search asked which parts of (1)--(5), and which parts of the surrounding
box-dipole logarithmic-energy realization, are already standard.

The user-requested Exa, Firecrawl, Consensus, and SciSpace routes were used
for discovery.  Consensus had exhausted its monthly quota in this pass.
Discovery snippets were not used as theorem evidence; the items below link
to primary proceedings, publisher, or arXiv records.

## Closest primary sources and the known ingredients

### Lee--Seung: diagonal majorant and edge-square proof

Daniel D. Lee and H. Sebastian Seung,
*Algorithms for Non-negative Matrix Factorization*, NeurIPS 13 (2000),
[official proceedings record](https://proceedings.neurips.cc/paper/2000/hash/f9d1152547c0bde01830b7e8bd60024c-Abstract.html),
[official paper PDF](https://proceedings.neurips.cc/paper_files/paper/2000/file/f9d1152547c0bde01830b7e8bd60024c-Paper.pdf).

Their auxiliary-function proof uses the diagonal matrix
`K_(aa)=(W^TWh)_a/h_a` and proves `K-W^TW` positive semidefinite by the same
weighted pair-square expansion as (4).  This is a direct precedent for the
diagonal-majorant construction and its edgewise certificate.  The paper does
not formulate the weighted SDP (1), its elliptope dual, or the Route-C
box-dipole application.

### Boman--Chen--Parekh--Toledo: factor width two

Erik G. Boman, Doron Chen, Ojas Parekh, and Sivan Toledo,
*On Factor Width and Symmetric H-Matrices*, Linear Algebra and its
Applications 405 (2005),
[DOI 10.1016/j.laa.2005.03.029](https://doi.org/10.1016/j.laa.2005.03.029).

They identify symmetric matrices of factor width at most two with symmetric
`H+` matrices, equivalently the generalized diagonally dominant PSD class in
the terminology used later in optimization.  The slack in (4) is explicitly
a sum of PSD rank-one matrices supported on two coordinates, hence lies in
this established factor-width-two architecture.  Their classification does
not by itself give the weighted minimum (5).

### Laurent--Poljak: the elliptope

Monique Laurent and Svatopluk Poljak,
*On a Positive Semidefinite Relaxation of the Cut Polytope*, Linear Algebra
and its Applications 223--224 (1995),
[DOI 10.1016/0024-3795(95)00271-R](https://doi.org/10.1016/0024-3795(95)00271-R).

This is a primary source for the elliptope
`{Y positive semidefinite: diag(Y)=1}` and its rank-one cut points.  Under
`X=Diag(s) Y Diag(s)`, the feasible set in (3) is a diagonally scaled
elliptope.  For the entrywise nonnegative objective in (3), the all-ones
rank-one point saturates the elementary bounds `Y_(ij)<=1`.  That last
one-line optimization is the specialization used here; it should not be
attributed as a theorem stated in Laurent--Poljak.

### Bacry--Muzy: logarithm from interval-cone overlap

Emmanuel Bacry and Jean-François Muzy,
*Log-Infinitely Divisible Multifractal Processes*, Communications in
Mathematical Physics 236 (2003),
[DOI 10.1007/s00220-003-0827-3](https://doi.org/10.1007/s00220-003-0827-3),
[arXiv:cond-mat/0207094](https://arxiv.org/abs/cond-mat/0207094).

Their time-scale cone construction with control measure `dt dl/l^2`
computes the overlap covariance explicitly: it has a logarithmic middle
regime and a finite-cutoff linear correction/terminal plateau.  This is a
close primary precedent for the Route-C uniform-box scale integral and its
finite-horizon `log(H/d)+d/H-1` correction.  It does not contain the Wave
rank-dipole coefficient SDP or a Sidon ownership ledger.

### Frerick--Müller--Thomaser: Fourier logarithmic energy

Leonhard Frerick, Jürgen Müller, and Tobias Thomaser,
*A Fourier Integral Formula for Logarithmic Energy*, Potential Analysis
(2024),
[DOI 10.1007/s11118-024-10125-9](https://doi.org/10.1007/s11118-024-10125-9),
[arXiv:2209.05439](https://arxiv.org/abs/2209.05439).

They prove a Fourier representation for logarithmic energy of signed or
complex measures, with the total-mass correction made explicit.  The
zero-mass specialization is the closest spectral precedent for separated
dipoles.  Atomic dipole self-energy is singular, so the project relies on
its own elementary finite mutual-interaction box calculation rather than
invoking a finite-self-energy corollary outside its hypotheses.

## Limited synthesis used in Route C

The following ingredients are known and are not claimed as new:

1. the Lee--Seung type diagonal majorant and edge-square/Laplacian proof;
2. the factor-width-two interpretation of an edge-supported PSD sum;
3. the scaled-elliptope dual feasible set and rank-one cut points;
4. logarithmic kernels from continuous box/cone scale overlap; and
5. Fourier logarithmic energy for zero-mass signed probes.

The present Route-C memo combines them in one narrow application: the
nonnegative active Wave graph makes the weighted diagonal-completion SDP
collapse to the explicit rank-one dual solution, and that exact coefficient
price is then compared with the finite-horizon Gothic ownership budget of
the box-dipole representation.

We did not locate the complete weighted statement in this application.  This
is only a dated, targeted retrieval result.  It is not a claim that the
weighted SDP identity is new, not a theorem of absence, and not publication
or prize evidence.  Any potentially new contribution would have to survive
specialist review and, for Erdős Problem #1191, would still require a legal
actual-Gram or signed cross-epoch payment on one compatible history.  The
global problem remains unresolved.
