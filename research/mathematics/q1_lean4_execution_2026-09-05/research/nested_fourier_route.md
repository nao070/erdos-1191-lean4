# Nested Fourier identities and the retained arithmetic information

2026-09-05. Parent-authored research note. The original Q1 is unresolved.
These are direct finite identities and one elementary almost-everywhere
consequence. They have not been Lean-verified. No numerical experiment or
external oracle is used in their proofs.

## 1. Exact quartic information of one entire Sidon history

Let a_1<a_2<... be an actual infinite positive integer Sidon sequence, and use Haar
probability measure on T=R/Z. Put e(t)=exp(2 pi i t). For finitely supported
complex coefficient vectors u,v,w,z define F_u(t)=sum_i u_i e(a_i t).
Character orthogonality and the Sidon property including repeated summands give

    integral F_u F_v conjugate(F_w F_z)
      = <u,w><v,z> + <u,z><v,w>
        - sum_i u_i v_i conjugate(w_i z_i).                 (1)

Here <u,w>=sum_i u_i conjugate(w_i), linear in the first entry.
Indeed the integral selects a_i+a_j=a_k+a_l. The two possible ordered
matches are (i,j)=(k,l) and (i,j)=(l,k). Their intersection consists exactly
of i=j=k=l, which is subtracted once. There are no omitted diagonal solutions.

In particular, with F_n=sum_(i<=n)e(a_i t) and X_n=|F_n|^2-n,

    integral X_n = 0,
    integral X_n X_m = min(n,m)(min(n,m)-1).                (2)

An alternative proof of (2) uses all signed nonzero differences. The common
frequencies in X_n and X_m are precisely those with both endpoints in the
smaller prefix. Their number is min(n,m)(min(n,m)-1).

Consequently the actual birth increments Z_n=X_n-X_(n-1), n>=2, satisfy

    integral Z_n Z_m = 2(n-1) 1_(n=m).                     (3)

These are orthogonal increments of trigonometric polynomials. No martingale
conditional-expectation assertion follows from (3), and none is made here.
Their frequency support is inherited from a_n, but the covariance identities
themselves contain no upper bound on a_n. All these formulas refer to the
same infinite history, rather than unrelated finite examples.

## 2. A genuine quadratic strong law, and its exact limitation

Define the increasing nonnegative potential

    V_N(t)=sum_(n=1)^N |F_n(t)|^2/[n(n+1)].

Its expectation is H_(N+1)-1. Equations (2) give exactly

    Var(V_N)
      = sum_(n=1)^N (n-1)/[n(n+1)^2]
        +2 sum_(n=1)^(N-1) [(n-1)/(n+1)]
             [1/(n+1)-1/(N+1)]
      <= 1+2 log(N+1).                                    (4)

For the diagonal bound use (n-1)/(n+1)<=1 and the telescoping sum
sum 1/[n(n+1)]<=1. For the off-diagonal bound discard the nonpositive
last term and use (n-1)/(n+1)<=1 and
sum_(n=1)^(N-1)1/(n+1)<=log N.

It follows that

    V_N(t)/log N --> 1 for Haar-almost every t.             (5)

Proof: take N_k=floor(exp(k^2)). By Chebyshev and (4), for every fixed
positive epsilon the measures of
|V_(N_k)-E V_(N_k)|>epsilon log N_k are summable in k. Apply the first
Borel--Cantelli lemma, then intersect the conclusions for epsilon=1/j.
Since E V_(N_k)/log N_k tends to 1, the result holds on this subsequence.
For N_k<=N<=N_(k+1), monotonicity squeezes V_N between the adjacent values;
log N_(k+1)/log N_k tends to 1. This proves (5) for every integer N tending
to infinity, outside one null set. No independence assertion is needed.

This is a valid statement for arbitrary infinite Sidon sequences, but it
does not give the original density conclusion. For example, under a fixed
cap a_N<=C N^2 log(2N), on the arc

    |t| <= 1/[12 C N^2 log(2N)]

all F_n for n<=N have real part at least (sqrt(3)/2)n. Thus

    V_N(t) >= (3/4)(N+1-H_(N+1)).                         (6)

These arcs shrink to the exceptional point 0, so (6) does not contradict
the almost-everywhere assertion (5). Even the fourth-power calculation at
this one coherent arc has scale 1/log N: the width times the square of the
lower bound in (6) is of that order. The upper variance in (4) has scale
log N. There is no contradiction between these estimates. This observation
limits this specific inference; it is not an impossibility theorem about
Fourier methods in general.

## 3. The next mixed integral is exactly the shared label budget

Let P be a finite old prefix, let F be any finite set of its positive
differences, and take real u_d>=0 supported on F. Put

    h(t)=sum_(d in F) u_d e(dt),
    U=sum_d u_d, S=sum_d u_d^2,
    K(s)=sum_d u_(d+s) u_d, s>0,

extending u by zero outside F. F need not itself be Sidon: all contributions
to a fiber K(s) are retained. For any actual future block B disjoint from P,
of size m, character orthogonality gives

    integral |h|^2 |F_B|^2 - m S
       = 2 sum_(s in Delta B) K(s).                        (7)

The unique positive differences of B are essential to the coefficient one
on the right. Now suppose all the mutually disjoint B_j belong to the same
Sidon history with P. Their internal positive difference sets are pairwise
disjoint and avoid Delta P. Since K is nonnegative,

    sum_j [integral |h|^2 |F_(B_j)|^2 - |B_j| S]
       <= U^2-S-2 sum_(s in Delta P) K(s).                  (8)

Here 2 sum_(s>0) K(s)=U^2-S is the expansion of the square of U after
removing its diagonal. Thus (8) is precisely the cumulative budget (13)
in difference_extension_route.md before the Cauchy lower bound is inserted.
Writing the same quantity as a higher-degree integral does not create an
additional source of budget. Cross-block labels omitted on the right are
nonnegative unused costs, as recorded by that note's exact partition (14).

For complex u the equality (7) instead uses Re K(s), which need not be
nonnegative. One cannot retain (8) while discarding the other fibers without
proving the necessary sign or an independent bound for those fibers.

## 4. Primary-source check and the remaining mathematical target

One Exa call requested numResults=100 with the query recorded in
evidence/goal2_fourier_search.json; it returned 100 title entries. Relevant
primary material was then read directly. Ortega--Prendiville,
*Extremal Sidon Sets are Fourier Uniform, with Applications to Partition
Regularity*, arXiv:2110.13447v1, Theorem 1.2, gives an error controlled by
sqrt(N) times the square root of the deficit from extremal cardinality and
an inverse power of N. At cardinality about sqrt(N/log N), this does not
give a small error relative to the cardinality. Its near-extremal
equidistribution conclusion cannot simply be imposed on a critical prefix.
Source: https://arxiv.org/pdf/2110.13447 .

The exact formulas above show where a new argument must enter this route:
either a bound using the actual positions of the frequencies across all
prefixes that is stronger than (2)--(4), or a controlled family of kernels
in (7) whose total charge improves on resetting (8) at each old-prefix
size. The latter is being studied independently in growing_label_budget.md.
Neither improvement is proved in this note, and (5) is not substituted for
the original Q1. The actual final Lean theorem proving Q1 or its negation
does not yet exist.

Independent review: `/root/global_route` rederived the quartic diagonal
subtraction, all factors in (2)--(4), the Borel--Cantelli subsequence and
monotonic interpolation in (5), and the signs and factors in (7)--(8).
It reported agreement on 2026-09-05. For (6) the positive-integer hypothesis
of the original Q1 is now explicit in the opening definition.
