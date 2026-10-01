# Final independent consistency review of WORKING_PROOF A16-A19

2026-09-09. Verdict: PASS for the mathematical statements and logical
scope of all four saved sections. No new finite search, M96 re-evaluation,
source change outside this worker's owned directory, or Lean rebuild was
performed. The final section text and hashes are pinned in
`A16_A19_review_source_manifest.json`.

## A16: symmetric kernel, without an unwarranted PSD inference

The bilinear identity Q_BH=sum_h w_h(g dot x_h)(g dot y_h)=g^T K g
counts type-2 minus and type-3 plus BH terms once, with their actual
gates and genuine prices. Because x is the middle subinterval of y,
the diagonal is sum_h x_h(l)w_h. Symmetry and entrywise positivity
do not imply PSD. The complete A14 M12 kernel's K11=0,K13=w/2,K33=w
and negative direction 2e1-e3 agree with the saved exact matrix.
Its actual positive gaps give 134/676350675, also matching the saved
BH channel. No negative physical mass is claimed.

## A17: exact tripartite count and a nonsummable pointwise bound

All three coordinate projections of a Sidon triple-sum fiber are
injective because the other two coordinates lie in disjoint rank sets.
Thus v_z<=min(l,n-l,m_k), with total l(n-l)m_k. An unordered collision
gives exactly one plus or type-2 minus BH matching; the type-1 minus
term is AC and must not double that count. The strict core is the
specified subset, not the entire raw collision set.

The recorded component identity uses F_k through min(k,T) and preserves
all k>T price components. The capacity count has its factor 1/2, and
l(n-l)min(l,n-l,m_k)<=n^3/8 gives n^3/16 after it. The finite Abel
telescope retains -(M-b)alpha_(M+1), yielding the valid
Q_BH<=n^3/(48b^3)<1/48. As recorded, that majorant tends to a positive
constant and does not establish the required square-root harmonic sum.

## A18: all losses share the actual cuts and component prices

The exact identity 2C_all=(d-1)N-delta and E=C_all-C_core give
Q_BH=U-Gamma-Gate-O with the displayed coefficients H_b/2,H_b,1.
The outer-width sum includes each selected BH matching with its
original coverage and upper-output gate; multiplying it out as a
component sum is legitimate finite interchange of nonnegative terms.
For a restricted quadruple collection, E must include every raw
collision outside that same collection, exactly as the saved text does.

All four numeric table rows match the previously saved independent
b24/k48/T96 component checks. The capacities, deficits, gate deletions,
outer losses and residual BH coefficients have no transcription error.
Their percentages remain explicitly finite observations.

The scalar lower bound 1/(1024*3^9)=1/20155392 agrees with the independent
factor count: H_b/2>=b^2/8, at least b components, at least b/8 old-gap
indices, and component weight >=16/(3^9 b^9). The triangular scalar
sequence fails positive-difference Sidon at its fourth point. Its
nondecaying majorant is not asserted to be an actual core mass or a
fixed-cap Sidon counterfamily.

## A19: raw and gate-adjusted increments have different obligations

Fix b,l and one old-quadruple collection independent of the component
index k; both the whole core and the all-large-old-gap selection meet
this condition. Let S=l(n-l), m=k-b and k+1<=T. The actual pair-sum
bank has zero-one coefficients. Hence the new shifted bank creates
J=sum_z v_z w_z collisions with old triples, and creates no collisions
between two different new triples. The finite expansion gives

    Delta delta=(d'-d)Sm+(d'-1)S-2J.

Every existing physical core record keeps its own strict tests when
k increases. The selected old quadruples are unchanged, and the newly
counted core outputs have upper rank exactly k+1. Therefore

    C_core(k+1)-C_core(k)=J_core, 0<=J_core<=J.

From D_eff=delta+2E=(d-1)Sm-2C_core one obtains EXACTLY

    Delta D_eff=(d'-d)Sm+(d'-1)S-2J_core.

No price term belongs in this unpriced count increment; the original
prices are subsequently supplied by the common coefficients in A18.
For k>=T the future set, raw and core counts, and both deficits stop
changing, while the genuine components continue. This is consistent
with the two-horizon limit rather than an implicit T=M restriction.

Before saturation m<min(l,n-l), so d=m,d'=m+1 and v_z<=m imply
J_core<=J<=mS. Consequently both deficits are nondecreasing in this
proved range: their increments are 2mS-2J or 2mS-2J_core.
After saturation the exact effective nondecrease condition is

    J_core<=(d-1)S/2.

This condition remains an UNPROVED candidate. It is not deduced from
J_core<=J, and it is not rejected by the existing raw counterexample.

In the certified M11 instance, the full original core is empty both
before and after the last addition. The exact values are

| Quantity | Before | After | Change |
|---|---:|---:|---:|
| m | 4 | 5 | 1 |
| d | 2 | 2 | 0 |
| S | 6 | 6 | 0 |
| C_all | 0 | 4 | 4 |
| C_core | 0 | 0 | 0 |
| E | 0 | 4 | 4 |
| delta | 24 | 22 | -2 |
| D_eff=delta+2E | 24 | 30 | +6 |

Thus J=4 but J_core=0. The four new raw collisions all fail the old-birth
upper-output gate of the strict core. The M11 witness refutes raw
monotonicity only, exactly as A19 states. Nor would effective monotonicity
alone imply a sufficiently strong weighted/cut summability estimate.

## Readback of the existing pinned Lean evidence

I read `../LEAN_VERIFICATION_04.json` and the corresponding c04 type/axiom
log. The recorded target-dependency compile, module compile and audit
all have exit code 0. All NINE source, toolchain and log hashes in that
manifest match the currently saved files. There are 18 supporting
declarations; the new three are:

- `mem_tripartiteFiber`: the finite fiber's membership characterization.
- `tripartiteFiber_card_le_min`: the exact bound for disjoint finite
  subsets of an actual `Erdos1191Q1.Sidon` set, using the literal predicate.
- `fiber_deficit_increment`: the generic finite algebraic identity with
  the hypothesis w_z^2=w_z.

Their logged transitive axioms are only `propext`, `Classical.choice`
and `Quot.sound`. No custom axiom appears. This was a readback of
already completed pinned checks, not a new build or a global audit.

The BH/core collision correspondence, full 1/48 estimate, complete
profile-deficit instantiation, gate-adjusted global potential inequality,
uniform U4-F constant and literal Q1 remain outside those supporting
Lean declarations. The status text in A17/A19 correctly preserves this
boundary. No completed master goal or final Q1 verification is claimed.

## Final source binding

Final `research/u4f_core/WORKING_PROOF.md` SHA-256:
`171807b9727b1b3cddce87594439a752b7db109856e27fe0a2325b960046ca75`.

- A16: `2dc6c4bc3f67ed61fcaaebc39cac253fee190ca88f835fcbc612f5f614c7a3e6`
- A17: `306723f8f8488d697d855f99267c0d3c2f64f4ae297c1d4d1d95bebcefc97e50`
- A18: `b91f1623132f59ec1a2f465ec428ed799b4c4771be2c87735f3f9d6a8de05506`
- A19: `244b954b1f13adc7649469a5ba10ff368d6c0d5d4f0c5bea45ab32eeca2e92dc`

The manifest saves the exact final sections, all binding hashes and the
Lean readback scope. The remaining mathematical action is a justified
post-saturation estimate on actual J_core or another compensated
potential strong enough for A18's weighted norm; the candidate is not
an assumption and does not replace the unchanged frozen theorem.
