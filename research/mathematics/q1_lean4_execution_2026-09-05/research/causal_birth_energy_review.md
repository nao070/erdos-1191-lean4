# Independent review of causal birth energy telescoping

Result: **no mathematical defect identified in the finite identities or the stated conditional divergence/reduction**. Reviewer: `/root/moment_evidence_audit`. Date: 2026-09-05T07:31:33.165678+00:00. The complete target note was read and its equations were independently rederived. No numerical experiment, previous computation, or Lean build/check was rerun. Original Q1 and the required Lean proof remain unresolved.

The coefficient rename to alpha/α is present in the recorded source; it separates scalar matrix weights from actual endpoints a_n.

## 1. Actual clocks and Abel bookkeeping

For a birth class j, summing `(a_j-a_i)(mean(P_(j-1))-a_i)` cancels the a_j term and gives v_j. Hence every prefix has coefficient sum zero and first label moment S_n. Each coefficient is fixed when its physical difference is born. The bounds v_j<=(j-1)H_j² and S_n<=q_n H_n² hold for these raw, unnormalized coefficients.

The new-star convolution has a zero coefficient at a_n, because the class is centered. All other positions are `a_n+a_k-a_i`, k!=i; positive and negative differences have unique ordered endpoints. Each source coefficient occurs n-1 times. Therefore `||k_n||²=(n-1)v_n`, while `||h_n||²=S_(n-1)`. Expansion proves (2). For mixed old/new source labels the cross inner product counts exactly one overlap when their output is in F_n; the old/new-point cross term counts exactly one pair retiring at n. Neither x_n nor rho_n requires another factor of two. The factor two enters only the norm expansion.

Summing the diagonal terms gives `(N-1)S_N`; same-birth pairs contribute `-v_j/2`, so (3) agrees with the direct final-energy expansion. Abel summation of `E_n-E_(n-1)` gives (4), using E_1=0. The two clocks in (5) are essential: x_n carries the maximum source birth b, while rho_n carries output retirement r.

## 2. Uniform bounds and the divergent Abel interior

For `w_n=(q_n²H_n²)^(-1)`, both q_n and H_n increase. The diagonal estimate is

`w_n D_n <= [q_(n-1)+(n-1)²]/q_n² = 8/n² - 2/[n(n-1)]`.

Summing from n=2 gives `8(zeta(2)-1)-2=8zeta(2)-10`, proving (7)–(8). Young's inequality gives `E_N<=N²S_N`; division yields `w_NE_N<=N²/q_N=2N/(N-1)<=4`, proving (9). Both bounds include the correct diagonal; no energy increment has been assumed nonnegative.

For every n in [N,2N], the zero total and raw first moment n*S_n imply

`(n*S_n)² <= E_n * H_n(4H_n²-1)/6 <= E_n*(2H_n³/3)`.

The carrier has exactly the stated enclosing 2H_n integer positions. Monotonicity of S_n, together with (10), gives (11); monotonicity of E_n is unnecessary. Since `q_(2N)>4q_N` and `H_(2N)>=H_N`, the weight drop on [N,2N] is at least `(15/16)w_N`. Multiplication gives exactly `45 eta² N²/(32 K³ H_N)` in (12).

The good-epoch input was checked in `coherent_birth_linear_envelope.md` sections 1–2: its lookahead lemma supplies the divergent reciprocal-log selection, and the same variance argument with diameter ratio 32 gives eta=2^-17. The selected old ranks are dyadic, so [N,2N) intervals are disjoint. A diameter cap suffices: actual Sidon labels give H_n>=q_n, furnishing the lower dyadic growth used there. Thus the Abel interior is monotone in the terminal horizon and has a divergent lower bound. Adding its nonnegative bounded endpoint proves (13), even though A_T itself need not be monotone. From (4) and (8), only B_T+R_T is forced to diverge.

## 3. Source/retirement commutator

The decreasing-tail decomposition in (14) proves PSD of Z_N and gives `t_N=sum_j w_j v_j`. In its final convolution, all source pairs have coefficient w_b. The same-birth cancellation reduces the diagonal N*t_N to (N-1)*t_N, and the remaining terms are B_N plus retirements weighted at b.

Subtracting the causal Abel identity leaves twice the signed retirement lag and the exact age charge. The coefficient of each v_j in the diagonal difference is

`(N-j)w_j - sum_(n=j+1..N)w_n = sum_(n=j+1..N)(w_j-w_n)`.

This proves (15), including every replication age. Expanding the two tail decompositions gives (16). Positivity of the two energies separately yields no sign for their difference, and the positive coefficients w_b-w_r do not change that limitation for signed g_d*g_e.

## 4. One source matrix, its mass, trace, and real demand

Use `α_n=q_n^-2`. Both V_N and Z_N have nonnegative-coefficient nested outer-product decompositions. Since `|g_d|,|g_e|<=H_b`, `W=V+lambda Z` has entries between `(1-lambda)α_b` and `(1+lambda)α_b` for fixed `0<lambda<=1`. These entries remain unchanged when the history extends. Complete birth-class centering proves zero row sums of the residual on every complete prefix.

Here matrix mass means **M(X)=1^T X 1**. For a scalar carrier u this equals `(sum u)²` only when X=u*u^T. V_N is a mixture of rank-one matrices; its M is not a scalar coefficient sum to be squared again. Its exact increment is `1-(q_(n-1)/q_n)²=4/n-4/n²`, proving (18). For the trace,

`1/[n²(n-1)] = 1/(n-1)-1/n-1/n²`.

The resulting sum is 2-zeta(2). Also w_n*v_n<=4/[n²(n-1)], proving all of (19).

The full historical maximum uses all prefix states with the old-label mask and no extra future-span mask. For a fixed nonnegative matrix, each fiber is largest just before retirement, or at the terminal prefix if unretired. The associated pair functional is linear. On the signed residual, its total strict-upper-triangle sum is -t_N/2, while the born-used sum is B_N-t_N/2. Their difference is -B_N, proving (20) with the correct sign. This applies linearity to the difference of the two full nonnegative matrices; it asserts no separate nonnegative residual budget.

For a compatible N-point future block, the actual mass-only raw demand is

`delta_0 = [N² M(V_N)/(L+H_N-N) - N tr V_N]/2`.

Because L>=N, H_N>=q_N, tr V_N>=1, and N²/q_N<=4, its upper bound is `[4M(V_N)-N]/2`, eventually negative. Taking a positive part then supplies zero demand from this estimate. The bounded trace therefore does not supply a free bounded historical margin, nor does the diverging matrix mass itself prove diverging masked capacity. A moment/allocation substitute needs a separate actual-demand proof.

## 5. Terminal rows and the conditional closing estimate

For any finite selection of terminal rows, interchanging finite sums gives the tail weights theta_n in (21). Applying the energy-increment identity with those weights gives (22) exactly; repeated terminal ranks simply add their coefficients. In general theta_n is not w_n. Thus the direct-weight divergence cannot be inserted into the previously studied current-row maximum without a new argument controlling its overlap and span costs.

With actual demands separately paid by their corresponding historical envelopes, (20) gives `M_0-M_W=lambda*B_N+Delta_D`. Since M_W>=0 and lambda>0, `B_N<=(M_0-Delta_D)/lambda`; substitution in (4) proves (23). If (24) held with one fixed epsilon>0, fixed positive lambda, and a uniform O(1) along unbounded horizons of the same capped history, then `epsilon*A_N<=D_N/2+O(1)`, contradicting (8) and (13). The note explicitly leaves (24), retirement control, and the physical margin unproved. A retirement-only estimate would force an increasing source improvement without paying that remaining margin.

Scope accepted: finite weighted identities and matrix realization, a uniform diagonal bound, and conditional Abel divergence under the stated full-history cap/good-epoch assumptions. The reduction neither proves a deterministic cap contradiction nor resolves Q1. No hidden payment hypothesis is presented as an established actual demand.

Reviewed target SHA-256: `4caf4ee5f8dc123cfb0024c9f305703580cb1c9d976a72df146baacfc5350fe2`.

Principal supporting sources read: `birth_centered_transport.md` section 2; `weighted_birth_envelope.md` sections 1–2; `birth_linear_good_epoch.md`; `coherent_birth_linear_envelope.md` sections 1–2 and its current-row/mixture conclusions; `future_moment_demand.md` sections 1–3. Relevant endpoint/shadow definitions were also compared with the retirement and Born-term notes. Existing source text was preserved.
