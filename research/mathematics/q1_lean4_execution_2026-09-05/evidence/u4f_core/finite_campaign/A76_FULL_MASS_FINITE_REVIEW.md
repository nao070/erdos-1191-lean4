# A76 independent finite full-product certificate review

Status: PASS_INDEPENDENT_TWO_ORIENTATION_FULL_MASS_CERTIFICATES. The independent checker exited 0. No all-theta optimality claim is made.

## Independent reconstruction

The checker uses only the Python standard library, imports no reference implementation, and runs no optimizer. It reconstructs the two saved actual histories/cells, all actual old positive sources, fresh labels with source endpoints excluded, and both orientations of every supplied original record.

For the older physical source (w,z) and fresh lower endpoint x, the common-node identity is

    g+f_q-f_j=h_actual>0,
    a_w+f_j=a_z+f_q+a_x-a_c.

Fresh-larger records use q=r-b,j=i-b; fresh-smaller records use q=i-b,j=r-b. Thus the full node matrix has every future column j!=q, with the j=q column zero. Restricting columns to j<q would omit the second orientation.

The checker directly confirms every supplied record's original integer endpoint arithmetic, six distinct endpoints, cut c<b<i<r<=min(k,T), source birth, orientation, and actual positive-difference recovery. It checks physical (w,z,x) uniqueness across all nodes and orientations, and row/column/fresh-coordinate injectivity at every actual node. Positive-difference uniqueness of both supplied histories and old/future mixed-sum uniqueness are also checked directly. These checks enumerate no new core record set.

For each physical source it reconstructs

    S_g=g*sum_(x<c; x!=w,z) (a_c-a_x).

The total source bank is checked a second way as U*G minus the two excluded endpoint products for every old source. For each matrix entry it independently finds the least allowed fresh hmin>=y=g+f_q-f_j>0 and forms

    W_scaled=max(d*g*y-p*g*hmin,0), theta=p/d.

Dummy, same-future, nonpositive-y, and missing-fresh entries are zero. On actual records hmin=y=h_actual, and each residual equals (d-p)*g*h_actual exactly.

All 3,312 node assignment certificates at theta=0,1/2,1 pass all 1,917,648 integer dual inequalities. Every assignment is a permutation with objective equal to both its claimed value and the complete dual sum. All actual node residuals are bounded by these exact node optima. The matrices are padded to max(z-1,m), retaining all m future columns; positive assignment entries therefore describe a feasible partial matching after dummy/zero entries are removed.

## Exact two-cell results

C=1,m0=2,M=T=96,c=24,b=25,k=48:

- Input scope: the same 125 already certified A65-unpaid residual records. This is not an enumeration of all original core records of M96.
- Fresh-larger: 106 records, original product mass 18,533,368.
- Fresh-smaller: 19 records, original product mass 3,388,671.
- Full original product mass of this subset: Q=21,922,039.
- Source bank: 634,824,292.
- Exact allowances at theta=0,1/2,1: 212998214, 840549483/2, 634824292.
- Original component coefficient: lambda48=1/1148518878296832.

C=2^67,m0=2,c=24,b=25,k=M=T=50:

- Input scope: the single original strict-core record from the existing independently certified whole-M50 profile. Its original strict/residual/cap certification is reused by hash; the profile generator is not rerun.
- Fresh-larger: one record; fresh-smaller: zero.
- Q=319014718988636095646352980968623575040.
- Source bank=1591346439643469596457552815054114237739600.
- Exact allowances at theta=0,1/2,1:

    2604576907803905178252676165836593156992820,
    1420455659290029060643662558763142175622036,
    1591346439643469596457552815054114237739600.

- Original component coefficient: lambda50=1/25527428477350911764427016026213912381273457594050.

Every displayed allowance bounds the corresponding actual Q. Only the minimum among the three tested theta values is certified; no minimum over a continuum or source-dependent penalty vectors is claimed.

## Logical and runtime boundary

The full-product wording means that both source orientations contribute their complete original product g*h=de, rather than only their positive boundary term. In the C1 finite check it still refers to the stated selected 125-row subset. The general A76 hand theorem applies to an original strict-core subset without enumerating hypothetical records into it.

Existing original strict gates, residual selectors, all-rank cap certificates, and whole-profile completeness where relevant are reused from bound artifacts. The new integer computations have UNKNOWN=0; this review does not assert new interval comparisons were performed.

Any later genuine-price summation must preserve v=min(k,T), selectors inside the component sum, all k>T components, and the original nonzero alpha_(M+1). The certificate assigns no original output price to an auxiliary matching edge that lacks an original record. It creates no independent per-cut or per-component source budget.

No new history, core-profile scan, A72 generator run, reference import, optimizer, Lean build, or root mathematical-source edit was performed. The checker completed; no process remains running. Full uniform norm, frozen U4F, and Q1 remain unresolved.

## SHA-256 binding

- A76_FULL_MASS_EXACT.json: 352bba86f180deb757fd46501e9be5c1aeb7862a5fddd6c9e52f47dcd9842082.
- A76_FULL_MASS_CHECKER.py: 0504837fd7e365a03ef59c02933e13ee2eb9f0a81ec53843adb58f4d85f8a4bb.
- A76_FULL_MASS_CHECK.json: 7052a16aa119832134fb81f3685a7927766daf1973b9469d3474033197dbbc90.
- A76_FULL_MASS_REVIEW.md: 3e34f1cfd0f149a7915c470cf77284147efc2f85152ff0d604253868551539a2.

The check JSON binds all input/source/history/record hashes and records every reconstructed actual row, source-bank term, node result, and exact component value. The concurrently maintained root proof and ledger were not edited.
