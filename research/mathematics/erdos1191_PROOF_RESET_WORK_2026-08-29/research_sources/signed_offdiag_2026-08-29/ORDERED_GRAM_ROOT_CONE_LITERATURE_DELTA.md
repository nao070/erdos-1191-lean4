# Ordered-Gram root-cone literature delta

Search date: 2026-08-30 (Asia/Tokyo)  
Evidence label: `TARGETED_PRIMARY_SOURCE_QUALIFIED_SYNTHESIS`

## Interface searched

The new Route-C calculation starts with consecutive gap intervals

\[
V_i=[a_{i-1},a_i),\qquad U_i=V_i+T,
\]

and the box-convolved gap dipoles

\[
T f_i={\bf1}_{V_i}-{\bf1}_{U_i}.
\]

Because both the `V` family and the `U` family are disjoint, the actual Gram
matrix has the exact grounded-Laplacian decomposition

\[
G_T=\operatorname{Diag}(\rho)
 +\sum_{i<j}\psi_{ij}(e_i-e_j)(e_i-e_j)^T,
\qquad \rho_i\ge0.
\]

The Wave coefficient is a squared rank distance,
`alpha_(i,j)=(j-i)^2/(4n^2)`.  Therefore the linear ramp
`eta_i=(i-c)/(2n)` satisfies

\[
\eta^TG_T\eta-Q_n(T)
=\sum_i\rho_i\eta_i^2
+{1\over4n^2}\sum_i\psi_{i,i+1}(T)\ge0.
\]

Exa, Firecrawl, and SciSpace were queried for the conjunction of ordered
interval-indicator differences, an SDDM/grounded-Laplacian Gram matrix, the
Wave/Sidon application, and the rank-ramp comparison.  Consensus had already
exhausted its monthly quota.  Discovery results were filtered against primary
publisher or arXiv records; no discovery snippet is treated as theorem
evidence.

## Known general ingredients

I. J. Schoenberg, *Metric Spaces and Positive Definite Functions*,
Transactions of the American Mathematical Society 44 (1938), 522--536,
[AMS primary PDF](https://www.ams.org/tran/1938-044-03/S0002-9947-1938-1501980-0/S0002-9947-1938-1501980-0.pdf).
Schoenberg's negative-type framework is the classical general setting behind
squared Euclidean distances.  In the present finite calculation the relevant
specialization is elementary: `(j-i)^2` is exactly the square of the
one-dimensional rank embedding, so no deep embedding theorem is needed.

Daniel A. Spielman and Shang-Hua Teng, *Nearly-Linear Time Algorithms for
Preconditioning and Solving Symmetric, Diagonally Dominant Linear Systems*,
SIAM Journal on Matrix Analysis and Applications 35 (2014), 835--885,
[DOI 10.1137/090771430](https://doi.org/10.1137/090771430).
This is a primary reference for the standard SDD/graph-Laplacian
architecture.  The Route-C decomposition is an exact application-specific
factorization, not a new definition of SDDM matrices.

David Durfee, John Peebles, Richard Peng, and Anup B. Rao,
*Determinant-Preserving Sparsification of SDDM Matrices with Applications to
Counting and Sampling Spanning Trees*, SIAM Journal on Computing 49 (2020),
[DOI 10.1137/18M1165979](https://doi.org/10.1137/18M1165979),
[arXiv:1705.00985](https://arxiv.org/abs/1705.00985).
Their work explicitly uses the equivalence between SDDM matrices and
Laplacian minors.  It supplies context for the grounded-Laplacian language,
not the ordered overlap identity or the Sidon/Wave ramp formula.

## Qualified boundary

The searches did not locate a primary source containing the complete
application-specific conjunction above.  In particular, they did not locate
the exact cellwise identity

\[
Q_n(T)=\sum_{j\ge i+2}\alpha_{ij}
 \|T^{-1}{\bf1}_{U_i\cap V_j}\|_2^2
\]

together with its finite-horizon Gothic ownership problem.  This is a
qualified retrieval null, not an absence theorem and not a novelty claim.
The matrix vocabulary, graph-Laplacian factorization pattern, squared-distance
negative type, and Dirichlet-form evaluation are known general ingredients.
Only the exact synthesis in this application is being recorded, and it still
does not supply the signed cross-epoch/common-history theorem required for
Erdős Problem #1191.
