# A37 independent review: the fixed-threshold allowance error

Date: 2026-09-09. Status: PASS as a uniform bound between two upper
allowances for the unchanged original core. No finite computation
or Lean build was needed for this hand proof.

Fix b>=3 and the original ell_b=floor(b^2/(log b)^5)+1. For each
v=min(k,T), use exactly the same actual past-plus-mixed forbidden
bank. Let F^1_bv(h) use available integers [1,H_b-1] and let
F^ell_bv(h) restrict that universe to [ell_b,H_b-1]. Both are sums
of the h largest nonnegative kernel weights 1-t/H_b, or all available
weights if fewer than h labels exist.

The larger universe adds at most ell_b-1 labels, each of weight at
most 1. Deleting these labels from any optimizing subset leaves a
feasible subset of the restricted universe. Thus, at every capacity,

    0<=F^1_bv(h)-F^ell_bv(h)<=ell_b-1.

This also holds if ell_b>=H_b, when the restricted universe is empty.
It does not require the newly allowed small labels to be actual
output differences.

Define the difference of the two original-price upper allowances by

    Delta U_b=S_b sum_{k=b+2}^M (kappa_k/H_k^2)
                 [F^1_b,min(k,T)(h_k)-F^ell_b,min(k,T)(h_k)],
    h_k=binom(min(k,T)-b,2).

Using H_k>=H_b, the variance bound, nonnegative components and the
unchanged finite tail gives

    Delta U_b <= (S_b/H_b^2)(ell_b-1)
                      (alpha_{b+2}-alpha_{M+1})
              <= [(b-1)^2/4] [b^2/(log b)^5]
                        /[(b+2)^2(b+1)^2]
              <= 1/[4(log b)^5].

The last inequality uses b(b-1)<=(b+2)(b+1). Empty component ranges
give zero directly. No terminal alpha is set to zero in an identity;
only a nonnegative tail term is discarded in an upper bound.

Since 1/[x(log x)^(5/2)] decreases for x>1,

    sum_{b=3}^{T-1} sqrt(Delta U_b)/b
      <= (1/2) integral_2^infinity dx/[x(log x)^(5/2)]
      =1/[3(log 2)^(3/2)].

This constant is absolute and applies to each finite actual history
without a cap or an extension premise. For k>T both allowances keep
their output bank at T while retaining the genuine price tail to M.

Consequently the square-root harmonic norms of these two nonnegative
allowances differ by at most the displayed constant, because
0<=sqrt(U^1_b)-sqrt(U^ell_b)<=sqrt(Delta U_b). This permits a fixed
auxiliary threshold in the allowance analysis. It does not redefine
the original core or claim that the allowance equals the actual
profile. The remaining gap between the allowance and actual records,
and the global square-root norm, are not evaluated here.

Source and companion review hashes are recorded in
A36_A38_review_manifest.json. The argument uses the existing actual
variance bound and finite alpha telescope with their original scope.
