# A41 independent cap corollary for all-large paths

Date: 2026-09-09. Status: PASS hand proof, with the count/weight
distinction below. No further finite calculation was used.

Restrict the unchanged original strict core to records whose three
adjacent old physical gaps all exceed c_birth^2/(log c_birth)^3.
Every positive source difference, including the smaller fixed label e,
is a sum of at least one of these gaps. Hence

    e>c_birth^2/(log c_birth)^3.

The original rank gate gives r<c_birth log c_birth and a covered cut
has r>b>c_birth. Since log c_birth<log b, this implies
c_birth>b/log b, and therefore

    e>b^2/(log b)^5, e>=ell_b=floor(b^2/(log b)^5)+1.

Each strict output difference also satisfies t>=ell_b by the existing
unchanged core threshold. A41's path argument consequently gives

    L<=H_{b-1}/(e+ell_b).

For b>=max(3,m0), the original cap at b yields

    L<=C b^2 log(2b)/(2ell_b)
       <(C/2)log(2b)(log b)^5=:D_b.              (1)

Only the cap at the actual cut rank is used; the strict inequality
follows from ell_b>b^2/(log b)^5. No path or prefix extension is
assumed.

As a cardinal statement, a disjoint path family with lengths at most
D_b has at most D_b/(D_b+1) times as many edges as ambient vertices,
by summing L<=(D_b/(D_b+1))(L+1) over its paths (isolates are harmless).
Thus the guaranteed cardinal deficit is at least 1/(D_b+1), of order
log^(-6)b for fixed C at large b. This is a count deficit; translating
it into a de-weighted saving requires additional actual information.
It is not automatically a proportional improvement to Q_bk.

The polylogarithmic length bound alone does not control the number of
paths, their weighted spans or the remaining square-root harmonic
norm. In particular it does not supersede A42's existing pointwise
source/output minimum by a new uniform norm theorem. The original
core, cap, physical records and genuine prices remain unchanged.
