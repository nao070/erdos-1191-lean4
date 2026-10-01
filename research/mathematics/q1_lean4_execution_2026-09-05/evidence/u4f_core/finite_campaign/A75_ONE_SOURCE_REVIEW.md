# A75 source-dependent penalty: independent review and certificate

Status: PASS. The hand extension is valid, and the independent finite checker exited 0. The certified strict improvement is confined to the prescribed C=1,m0=2,M=T=96,c=24,b=25,k=48 cell.

## One-copy hand argument

For each actual older physical difference g=a_z-a_w, choose one theta_g in [0,1], shared across all future nodes of the fixed component. Put

    B_g=sum_(x<c; x!=w,z) g*(a_c-a_x-g)_+.

Retain the A74 candidate hmin for each positive-boundary edge: among actual fresh h_x with x distinct from w,z and h_x>=g+t, choose the least, or exclude the edge if no such x exists. Define its residual weight as

    W_gtheta=max(g*t-theta_g*g*(hmin-g),0).

For an actual positive-boundary record, hmin=h_actual=g+t, so W_gtheta=(1-theta_g)*g*t. The actual physical source (w,z,x) determines t and then its unique actual output pair. Thus it is used once across all right nodes, and its theta_g part is charged once to theta_g*B_g. The actual edges at each right node are a matching by literal Sidon and the original six-endpoint conditions. Summing gives

    Beta <= sum_g theta_g*B_g + sum_nodes maximum_matching(W_gtheta).

Nonnegativity of theta_g permits adding unused source terms to the auxiliary bank. The proof does not price those missing records. Dependence on the physical source g is allowed; silently choosing a different penalty for each occurrence of the same source at different future nodes would require a separate justification. No uniform cross-cut budget is provided here.

## Prescribed finite certificate

Only the actual old pair (w,z)=(1,16), with g=284-1=283, receives theta_g=1/1000; every other source penalty is zero. Excluding fresh x=1,16 gives

    B_g=1,463,959.

The checker independently reconstructs the 23 changed right-node matrices (z=16,q=1,...,23). For w=1 their scaled entries are

    max(1000*g*t-g*(hmin-g),0),

and other eligible entries are 1000*g*t. Ineligible or dummy entries are zero. All 6,155 integer dual inequalities pass. Every supplied assignment is a permutation with exactly the certified objective, and its value equals the complete dual sum.

The other 506 node values are reused from the hash-bound independent A74 theta-zero certificate, which had already certified the global scalar minimum. The new checker matches every original node value to that independent result; it does not rerun the reference optimizer or rebuild the unchanged certificate.

Exact totals are

    unchanged node sum = 74,543,883,
    previous changed node sum = 5,787,629,
    new changed node sum, scaled by 1000 = 5,785,452,730,

    new upper bound = 80330799689/1000,
    previous minimum over every scalar theta = 80,331,512,
    strict improvement = 712311/1000 > 0.

Thus the single prescribed nonconstant source-penalty vector strictly improves every scalar theta on this cell. It is not asserted to be the minimum over all source-dependent vectors.

Direct arithmetic on the same 125 already certified A65-unpaid rows reconstructs 106 positive-boundary records and Beta=8,716,524. Their node matching capacities and physical source uniqueness pass, and all actual node residuals are below the certified allowances. The selected source g=283 has zero actual positive charge in this retained subset. The improvement therefore does not claim a newly priced actual record or an actual decrease in Beta; it reduces an auxiliary upper allowance.

## Scope and prices

The checker uses only standard-library arithmetic and saved sources. It performs no reference import, new history, original core enumeration, strict-gate re-evaluation, full-profile calculation, optimizer run, or Lean build. Existing original strict gates, fixed-cap certificates, and residual memberships are reused by hash. UNKNOWN=0 for this exact check.

The hand inequality applies at the actual fixed v=min(k,T), preserving selectors. Subsequent genuine-price summation must use the same lambda_k and retain k>T components and alpha_(M+1). No source or node budget can be independently reset across cuts by this argument. It bounds Beta; it does not yet establish a full original mass estimate, uniform square-root harmonic norm, frozen U4F theorem, or Q1.

## SHA-256 binding

- `A75_ONE_SOURCE_PENALTY_EXACT.json`: `7f88b57203c6923600026a0049f2df6ba2ed445d2e580d1abefffe32c3f7e19a`
- `A75_ONE_SOURCE_CHECKER.py`: `f88872cfb840f4af871c0e3156c1849321653d18afb4b88fbd2c8de74dd091cd`
- `A75_ONE_SOURCE_CHECK.json`: `29fe09a50d7ea768a7aa63511631cdaebc99b68fb75a4ab10e4bcaabfae900ff`
- Reused `A74_PARAMETRIC_DUAL_EXACT.json`: `7d32e6598f38cb0ad8917076ce5a77feda28b9ed187b4fe72c8e3b2879a37c7a`
- Reused `A74_PARAMETRIC_DUAL_CHECK.json`: `04aa0fa904bd873a01e7ccea7bb9590ad2bc943fd31817d97ab3eaf775daf727`
- Hand proof `A74_SOURCE_DUAL_REVIEW.md`: `d7c62f0badb11eb796ee28ab29a64d557a96624dde38193f563ce23f6222ce56`

The check JSON records all additional source/history/record hashes, all 23 changed-node results, and the source cost by actual fresh rank. Root-owned proof, ledger, and Lean files were not edited. No process remains running from this check.
