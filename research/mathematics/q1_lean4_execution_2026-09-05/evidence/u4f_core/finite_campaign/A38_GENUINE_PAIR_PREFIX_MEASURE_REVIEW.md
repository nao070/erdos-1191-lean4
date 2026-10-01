# A38 independent review: one genuine-price pair measure

Date: 2026-09-09. Status: PASS for the finite representation below,
with the eligible-cut domain made explicit. This is a hand proof;
it includes no new search, profile evaluation or Lean verification.

Fix the auxiliary threshold 1, an actual pair c=a_f-a_p>0, and
f<=T<=M. Define the eligible-cut set

    E_c={b:p<=b<f and H_b>c}.

If this set is empty, every cut sum below is zero and no L is needed.
Otherwise put L=min E_c. Strict increase of the actual diameter gives
E_c={L,...,f-1}. The restriction b<f is essential in defining L:
min{b>=p:H_b>c} alone can equal f even when no mixed cut is eligible.
Since H_1=0<c, any nonempty eligible set automatically has L>=2.

For b in E_c let phi_b(c)=1-c/H_b>0 and use A36's canonical deletion
penalty p_b(h). For each v>=f put

    rho_b,v=p_b(binom(v-b,2))/phi_b(c).

A36 proves 0<=rho_b,v<=1 and its cut-nonincreasing property at every
fixed v. The crucial component coefficient
lambda_k=kappa_k/H_k^2 is the same actual positive number at all cuts.
Define

    Pi_b(c)=sum_{k=f}^M lambda_k p_b(binom(min(k,T)-b,2)),
    A_b=Pi_b(c)/phi_b(c)
       =sum_{k=f}^M lambda_k rho_b,min(k,T).

Because min(k,T)>=f for all these components, the same fixed-v theorem
applies to each summand. Finite nonnegative summation therefore gives

    A_{b+1}<=A_b, 0<=A_b<=sum_{k=f}^M lambda_k=u_f^[M].

The common tail for k>T stays present. This is the original genuine
u_f, not alpha_f/H_f^2 and not a tail with alpha_{M+1}=0.

Define an actual nonnegative finite measure on the eligible cut range:

    delta_t=A_t-A_{t+1}   for L<=t<f-1,
    delta_{f-1}=A_{f-1}.

Then, by finite telescoping,

    sum_{t=L}^{f-1}delta_t=A_L<=u_f^[M],
    A_b=sum_{t=b}^{f-1}delta_t.

For any given nonnegative cut weights w_b, finite interchange yields
the exact prefix-interval representation

    sum_{b=L}^{f-1}w_b A_b
      =sum_{t=L}^{f-1}delta_t sum_{b=L}^t w_b.     (1)

The terminal definition of delta encodes the finite cut range; it
does not replace a physical price or assert a deletion at the cut f.
For the specific choice w_b=S_b phi_b(c)/b, equation (1) becomes

    sum_{b=L}^{f-1} S_b Pi_b(c)/b
      =sum_{t=L}^{f-1}delta_t
                    sum_{b=L}^t S_b phi_b(c)/b.

Thus the original genuine harmonic loss for this one physical pair
has one common prefix measure of total mass at most u_f. There is no
claim that S_b Pi_b(c) is nonincreasing; A36 already supplies concrete
counterexamples to analogous source-weighted monotonicity. The raw
normalization and the common component prices are both necessary.

This is a linear harmonic identity. It does not bound the sum of
square roots of the original profile, the prefix weights on the right,
or the comparison between all-pair losses and their common baseline
upper bound. Summing independent per-pair allowances without that
comparison would leave the same global gap. A37 permits threshold-1
allowance analysis up to a uniformly paid error while keeping the
actual strict core unchanged. U4-F and original Q1 remain open.

The source bindings and the A36/A37 dependencies are recorded in
A36_A38_review_manifest.json.
