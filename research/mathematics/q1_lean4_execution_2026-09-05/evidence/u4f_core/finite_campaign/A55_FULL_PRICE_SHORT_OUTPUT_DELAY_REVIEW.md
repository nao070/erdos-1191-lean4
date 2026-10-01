# A55 independent review: full-price short upper-output delay

Date: 2026-09-09. Status: PASS, independent hand proof and one saved-record exact check. Ownership: finite_campaign only. No new history, full-profile evaluation, pool scan, model/toolchain change, Lean run or redelegation.

## Exact claim and unchanged objects

Fix q>2/3 once. For every actual finite integer Sidon history with original horizons T<=M, retain exactly the original strict-core physical records with birth c and

    r-c <= R_c := floor(c/(log c)^q).

Price a selected record by its full original de*u_r^[M], where u_r^[M]=sum_{k=r}^M (alpha_k-alpha_(k+1))/H_k^2 and alpha_k=1/[k^2(k-1)^2]. Each selected physical record retains its original covered cuts c+1,...,i-1. This is a subclass of the frozen profile; its definition does not depend on the covered cut or component. The original Sidon/strict gates are unchanged, and no cap is required for the proof below.

## Fresh-source count

Six distinct endpoints imply four distinct old endpoints. The greatest of their ranks c occurs in exactly one of the two source differences. For a fixed actual output pair c<i<r<=min(T,c+R_c), write t=a_r-a_i>0.

- If the fresh source is the larger d=a_c-a_x, there are at most c-1 choices of x. Then e=d-t is determined, and actual positive-difference uniqueness determines its source endpoints, if it exists.
- If the fresh source is the smaller e=a_c-a_w, there are at most c-1 choices of w. Then d=e+t is determined, with at most one source pair.

Every original record has exactly one of these descriptions. Invalid positivity, overlaps, unavailable endpoints and failed strict gates only delete possibilities. There are at most binom(R_c,2) possible future output pairs. Thus the number of selected records born at c is at most (c-1)R_c(R_c-1), and their total product is at most

    (c-1)R_c(R_c-1)H_c^2 <= c R_c^2 H_c^2.

If R_c=0 or1 there are no such records. The bound permits output endpoint pairs that do not exist; this is only a counting upper bound, not an assertion of realization or extension.

## Original price and birth mass

Every actual record has c+2<=r<=T<=M. Consequently H_(c+2) exists, and monotone widths plus the finite alpha telescope give

    u_r^[M] <= alpha_(c+2)/H_(c+2)^2 <= 1/(c^4 H_c^2).

The intermediate equality sum_{k=r}^M kappa_k=alpha_r-alpha_(M+1) retains the nonzero terminal alpha. Dropping its subtraction is an upper bound, never a reset of the genuine price. Hence total full original price born at c is

    E_c <= R_c^2/c^3 <= 1/[c(log c)^(2q)].

All strict six-distinct records have c>=4. No nonexistent longer history or diameter is used.

## Birth blocks, coverage and uniform square-root norm

For ell>=2 group births 2^ell<=c<2^(ell+1). Since sum_{c=2^ell}^{2^(ell+1)-1}1/c<=1,

    E_ell <= (ell log2)^(-2q).

For every physical record in this group its exact harmonic coverage is

    h_record=sum_{b=c+1}^{i-1}1/b
            <= (i-c-1)/c <= (r-c)/c
            <= (log c)^(-q) <= (ell log2)^(-q).

Retain this coverage before taking square roots. Exact once-per-record expansion gives

    I_ell=sum_b P_b^(ell)/b
         =sum_records de*u_r^[M]*h_record
         <= (ell log2)^(-3q).

Since c>=4, log c>1 and q>0, R_c<c; covered cuts lie in the integer interval 2^ell<b<2^(ell+2). Its harmonic weight W_ell is at most log4=2log2 (integrate1/x on [b-1,b] for the strict lower endpoint). Therefore Cauchy gives

    N_ell=sum_b sqrt(P_b^(ell))/b
          <= sqrt(2log2)/(ell log2)^(3q/2).

The original selected profile is the sum over birth groups. Pointwise sqrt subadditivity, followed by the convergent ell series, yields

    N_selected <= sqrt(2log2)/(log2)^(3q/2)
                  * sum_{ell>=2} ell^(-3q/2) < infinity.

For q=3/4, sum_{ell>=2}ell^(-9/8)<=integral_1^infinity x^(-9/8)dx=8, so

    N_selected <= 8 sqrt2/(log2)^(5/8).

The estimate uses actual source/output uniqueness and exact physical coverage, not independent cut budgets or bounded birth mass alone. It holds uniformly for all finite M,T. In particular the selected original price still includes k>T components. Fixed C,m0 and all-rank cap assumptions, if imposed, remain unchanged but are unused here.

## One existing finite record: complete original price is now paid

The only inspected record is the saved certified C=1,m0=2,M=T=96 witness

    [d,e,x,y,w,z,c,s,i,r,t]
    =[215,174,14,19,21,24,24,19,27,28,41].

Its six endpoint values are old186,401,540,714 and future1018,1059; de=37410. The original coverage is cuts25,26, with harmonic weight51/650. Two independent rational log implementations and integer fourth-power comparisons certify

    floor(24/(log24)^(3/4))=10,
    floor(25/(log25)^(3/4))=10.

Since r-c=4<=10, this whole original record is in A55. Since k-b=48-25=23>10, the component at k48,cut25 was not paid by the A43 cut-short condition. These are distinct selectors. A55 now pays every original component28..96 of this record, with its full unchanged u28^[96], not just lambda48=1/1148518878296832. alpha97=1/86713344 is retained. The exact full fraction, both log proofs, endpoint recovery and both original strict-gate checks are stored in A55_SAVED_WITNESS_EXACT.json. UNKNOWN0.

## Logical role and next action

This is a valid new full-record uniformly summable subclass, with a noncircular cap-free proof. It is not a bound for the complementary frozen profile, CoreUniform, Q1 or its negation. The remaining records must satisfy r-c>floor(c/log^(3/4)c) if this payment is adopted. No finite nonemptiness or nonexistence inference is made. The separately requested A56 review next tests whether small i-c can be paid even with unrestricted upper output r.

## Source binding

The frozen source meanings are reused from the already reviewed notes and certified data, not reconstructed from a global audit. SHA-256:

- `A42_SOURCE_PAIR_RANK_TAIL_REVIEW.md`: `1f8f530e53de783939ef396490e1fc13168c5babd344e2602bd4add395c9e350`
- `A43_SHORT_RANK_COMPONENT_REVIEW.md`: `29fcc131c926e1c7c2d24e4d11171213e603d8ef19bd5dec4300529324b3f02f`
- `A53_BIRTH_RELATIVE_COMPONENT_TAIL_REVIEW.md`: `befdce4b639afa97044cb66628797a00e60387dd2df53169585453a2f57db208`
- `A50_A54_final_review_manifest.json`: `41b65b36e33bf4ceb922da65676a95780be468fe10ee082257a8b5dee336e4b7`
- `A53_EXISTING_RESTART_WITNESS_EXACT.json`: `4922d09cc1962ef0d7a466baa3713210e24d863b4c6bff7c8a02d38eb749caa2`
- `A54_EXISTING_WITNESS_FLAG_EXACT.json`: `89dcbd66964618bac33a48adc3e4cf694e2b8f9c7e3b0f6011060f9404e71d9b`
- `C1_m02_dense_variant1_M96.json`: `d2b47d3902725a6d2a7f9283f9ade3bfa9c02cbe9c899d0ce08fe8bc0adbbb3e`
- `C1_m02_dense_variant1_M96_independent_check.json`: `970215ab400c0427c10f30ad44e2bd9db4b8f2cf91ded2a85205b1c160ac4083`
- `reference_evaluator.py`: `3c8339dca1d7e75a0e7e2ff4088c0deea13a39274ad53430df83362d65fd5756`
- `independent_checker.py`: `24673840329f7407395428f6cfda5706813c4f0e4b386723540aa62645c7a198`
