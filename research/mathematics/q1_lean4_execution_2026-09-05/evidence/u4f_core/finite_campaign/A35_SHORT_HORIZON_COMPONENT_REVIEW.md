# A35 independent hand review: a short output horizon and terminal cuts

Date: 2026-09-09. Status: PASS for the proposed bound, with a stronger
denominator available. The resulting short-horizon cut sum is bounded
here only by a nonuniform O_C,m0(log log T) majorant. No new finite
experiment, history, source-bank scan or Lean build was performed.

## Exact finite-price statement

Fix integers 2<=b<T<=M in an actual Sidon history. Let S_b be the
squared-difference sum of the first b-1 points and H_b the diameter
of the first b points. As before, Q_bk is the unpriced original
strict-core de sum at cut b through output r<=min(k,T). The actual
source/output inequality and nonnegative genuine components give

    P_b(M,T) = sum_{k=b+2}^M (kappa_k/H_k^2) Q_bk
      <= (S_b/H_b^2) sum_{k=b+2}^M kappa_k h_k,
    h_k=binom(min(k,T)-b,2).

This uses H_k>=H_b. No strict gate is enlarged in the definition of
P; only its upper bound drops restrictions. The variance bound is
S_b/H_b^2<=(b-1)^2/4. Put h_T=binom(T-b,2). The exact finite Abel
identity is

    sum_{k=b+2}^M kappa_k h_k
      = sum_{r=b+2}^T (r-b-1) alpha_r - h_T alpha_{M+1}.

The increment of h_k is r-b-1 at r<=T and is zero after T. Thus the
last term uses M+1, even when the output horizon is the smaller T.
Equivalently the components k>T retain the common tail
h_T(alpha_{T+1}-alpha_{M+1}). The convention alpha_{M+1}=0 is not used.

Since 0<=h_k<=h_T,

    sum_{k=b+2}^M kappa_k h_k
      <= h_T(alpha_{b+2}-alpha_{M+1})
      <= h_T alpha_{b+2}.

Consequently a stronger version of the proposed inequality holds:

    P_b(M,T) <= (b-1)^2 (T-b)(T-b-1)
                /[8 (b+2)^2 (b+1)^2].

In particular replacing (b+2)^2 in the denominator by b^2 gives
the requested valid bound. The stronger denominator follows from
alpha_{b+2}=1/[(b+2)^2(b+1)^2], so its shift must not be lost in
an equality. The inequality is valid for every T, without assuming
T<J_b. When T=b+1 the two sides and h_T are zero. Separately, A27's
weighted Abel bound gives the useful simultaneous ceiling

    P_b(M,T) <= (b-1)^2/(24b^2) < 1/24.

All these statements hold for every actual M>=T; no bound on the
length of an admissible prefix is assumed.

## Fixed terminal fractions can be paid uniformly

Fix 0<delta<1 and restrict to b>=delta T. The proposed (weaker)
bound implies

    sqrt(P_b)/b <= (T-b)/(sqrt(8)b^2)
                 <= (delta^(-1)-1)/(sqrt(8)b).

For B=max(2,ceil(delta T)), if B<=T-1,

    sum_{b=B}^{T-1} 1/b <= 1/B+log((T-1)/B)
                        <= 1/2+log(1/delta).

Thus terminal cuts have a uniform bound depending only on delta.
Using the simultaneous 1/24 ceiling gives the simpler constant
(1/2+log(1/delta))/sqrt(24). Empty cut ranges contribute zero.
Neither estimate makes delta depend on T and then discards that
dependence.

## Exact short-horizon support and the last failed inequality

Let J_b=ceil(4sqrt(H_b)), and restrict now to T<J_b. Because T is an
integer, the ceiling comparison is exactly equivalent to

    T<4sqrt(H_b), or H_b>T^2/16.

For b>=m0, the fixed cap therefore implies the necessary condition

    16 C b^2 log(2b)>T^2.                         (1)

This is an exact integer support restriction derived from the cap;
it is not sufficient for a given actual history to be short. The
function x^2 log(2x) is strictly increasing for x>=1, so the allowed
integer cuts in (1) form a terminal interval. Equivalently its first
cut is the least integer b>=max(2,m0) satisfying (1), if any b<T does.
Because b<T, it follows further that

    b>T/rho_T, rho_T=4sqrt(C log(2T)).             (2)

With B=max(2,m0,floor(T/rho_T)+1), the high-rank short cuts are a
subset of {B,...,T-1}. A nonempty such range necessarily has rho_T>1.
The original b<m0 cuts are bounded independently by
K_initial=(1/sqrt(24)) sum_{b=2}^{m0-1}1/b, interpreted as zero when
the range is empty. Applying the universal ceiling above and the
same harmonic integral gives

    sum_{b<T, T<J_b} sqrt(P_b(M,T))/b
      <= K_initial
          + [1/2+max(0,log rho_T)]/sqrt(24).       (3)

The right side is O_C,m0(log log T), not a uniform constant. The
specific failed final step would be to assert a constant bound for
the numerical sum of 1/b over the cap-allowed interval (1), or even
the looser interval (2). Shortness alone does not give b>=delta T
for a positive delta independent of T.

This failure is visible in the numerical support itself, without
postulating any actual capped history. For fixed C>0 and sufficiently
large T put B*=ceil(T/[2sqrt(C log T)]). Take T large enough that
B*>=sqrt(T), B*<=T/2, and its unrounded value is at least one. For
every integer b>=B*, b<T,

    16 C b^2 log(2b)
       >= 16 C [T^2/(4C log T)] [log T/2]
       = 2T^2 > T^2.

Hence these integer cuts satisfy the necessary cap support (1).
Moreover B*<=T/sqrt(C log T), so

    sum_{b=B*}^{T-1}1/b >= integral_{B*}^T dx/x
                         >= log(sqrt(C log T)).

This diverges as a numerical majorant. It is not a lower bound for
the actual core profile, and it does not assert simultaneous
realizability of these cuts, arbitrarily long capped prefixes, or
a counterexample to U4-F or Q1.

## Logical role and source binding

The component count is the same actual count used in A33. The finite
price formula is a bounded algebraic identity with the original
terminal alpha_{M+1}. The cap support uses the same J_b as A34 but
addresses the complementary horizon case. No full near norm, global
charging estimate or frozen K has been proved. The next nonduplicate
step must use additional actual endpoint/cut correlation inside the
growing logarithmic band, rather than replacing (3) by a constant.

The companion A35_short_horizon_review_manifest.json binds these
dependencies and this note. No frozen research source was edited.
