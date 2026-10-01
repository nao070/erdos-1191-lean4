# Route C probe — why linear multi-`N` averaging cannot improve the best scale

Date: 2026-08-29  
Evidence: `HUMAN_PROOF_AUDITED` algebraic method no-go  
Progress grade: `G2` closure of one precisely named method class

## The method class

At scale `N_i`, suppose an argument supplies nonnegative energy `E_i`, an
upper budget `u_i`, and a density lower coefficient `c_i>0` such that

`c_i*tau^2 <= E_i <= u_i`.

This abstracts using the existing Sidon pair budget and the existing
scale-wise weighted Cauchy lower bound.  Allow any finite family of scales,
any nonnegative weights `lambda_i`, and even grant a common shift for which
all weighted energies can be summed.

## Exact convexity theorem

If `sum_i lambda_i*c_i>0`, then summing the displayed inequalities gives

`tau^2 <= (sum_i lambda_i*u_i)/(sum_i lambda_i*c_i)`.

Put

`alpha_i=lambda_i*c_i/(sum_j lambda_j*c_j)`.

The right side is exactly

`sum_i alpha_i*(u_i/c_i)`,

where `alpha_i>=0` and `sum_i alpha_i=1`.  Hence

`(sum lambda*u)/(sum lambda*c) >= min_(i:lambda_i>0) u_i/c_i`.

No nonnegative linear average of the old independent one-scale upper and
lower inequalities can beat the best constituent one-scale constant.

## Scope

This does not rule out O'Bryant's multi-`N` suggestion.  It rules out only
the implementation “take the existing inequality at several scales and add
them with nonnegative weights.”  A successful multi-scale theorem must add
at least one term absent from the constituent inequalities, for example:

- a negative cross-scale covariance in the Sidon upper budget;
- orthogonality of martingale differences giving an additional square sum;
- an entropy chain-rule deficit which is positive unless all conditional
  profiles are simultaneously extremal; or
- an inverse theorem proving that the near-Cauchy profiles required at two
  or more nested scales are arithmetically incompatible for a Sidon set.

The theorem is non-vacuous and independent of the existence of an infinite
critical branch.  It is a closure of a method class, not a proof of Q1 or
Q2.

