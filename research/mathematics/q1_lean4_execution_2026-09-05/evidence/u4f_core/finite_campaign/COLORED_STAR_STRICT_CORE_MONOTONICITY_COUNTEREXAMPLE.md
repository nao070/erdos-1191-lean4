# Actual strict-core counterexample to effective-deficit monotonicity

2026-09-09. Certified finite counterexample, followed by complete exact
profile evaluation and independent verification on the SAME history.
This refutes saturated gate-adjusted monotonicity, including its
all-three-old-gaps-large version. It does not refute U4-F or Q1.

## The fixed campaign and the one executed candidate

C=100000000000000 and m0=2 were fixed before checking any sequence.
The authorized ceiling was 200 graph trials per t=64 or96; only ONE
t=64 candidate was actually constructed and tested. It succeeded on
that first check. No later t=64 trial and no t=96 trial was run.

The exact 156-point positive integer sequence and graph are in
`C100000000000000_m02_colored_star/candidate_t64_trial1.json`, SHA-256
`cb26b78d3c4768ea022cf734a44414cf27090ae90d0a5e2f65c03187cc1982e0`.

The old left points are 1 and 6000000001, so h=6000000000. The 64
right points occupy ranks3..66; the cut point is a_67=31442910617.
The final point is X=a_156=1000000000000. The right points were drawn
once from a fixed integer grid with bounded deterministic seeded jitter;
the full numeric data and seed 119120064 are saved, not inferred from
an abstract graph.

For a concrete graph description, label the lower 32 right points low_j
and upper 32 high_j, j=0..31. Let f be the successor in the 32-cycle

    0,2,4,...,30,31,29,...,1,0.

The +h class has low_j->high_j and high_j->low_f(j), one alternating
64-point directed cycle. Every downward jump is less than h. The -h
class has low_j->high_(j+8), j=0..23; every such upward jump exceeds h.
Every t_e=R_v-R_u+sign*h is positive, and all 88 outputs are distinct.
Append the 88 points X-t_e in increasing order, then X. A graph color
is not the same as a plus/minus BH matching: that classification is
determined by the sorted physical source endpoints.

The complete ACTUAL point set passes all 12,090 distinct-positive-
difference checks. Independent repeated two-sum enumeration, including
doubled endpoints, also passes. Every rank2..156 satisfies the original
same fixed cap, checked with two independent rational-log implementations.
The graph alone was never treated as a Sidon certificate.

## Exact counterexample at the original cut

Fix b=67,l=2,T=M=156. The old pair bank has S=2*64=128 distinct
integer sums. Before adding X there are m=88 future points; d=2 is
already saturated. Complete target reconstruction, with the ORIGINAL
strict gates, gives

    J_raw=88, J_core=71, (d-1)S/2=64,
    J_core / [(d-1)S/2] = 71/64 > 1.

The 17 excluded raw collisions fail the following gates: 14 far-output,
one old-partner, one short-top-lag, one short-coverage. All strict
comparisons are resolved; UNKNOWN=0. The retained 71 channels comprise
47 type-2 minus and24 plus matchings, counted once each. Type-1 minus
is AC-only and contributes no additional J_core.

The raw pair-bank/future-fiber reconstruction is independent of the
direct old-quadruple/two-output enumeration. They agree on every
new collision. A separate root reconstruction saved outside this
worker's directory agrees as well. Complete before/after counts are

| Quantity | Before rank156 | After rank156 |
|---|---:|---:|
| Triple mass | 11264 | 11392 |
| Single fibers | 11264 | 11216 |
| Double fibers | 0 | 88 |
| Raw collisions | 0 | 88 |
| Original BH core collisions | 0 | 71 |
| Raw deficit delta | 11264 | 11216 |
| Gate deletion E | 0 | 17 |
| Effective deficit delta+2E | 11264 | 11250 |

Thus Delta D_eff=-14 both by direct reconstruction and by
128-2*71=-14. The signed identity remains valid; its monotonicity
consequence is false. Unlike the earlier M11 raw example, these
offending collisions satisfy every original strict-core condition.

All71 also belong to the unchanged all-three-old-gaps-large remainder.
In fact the smallest global adjacent point gap in this history is 13184,
whereas c^2/log(c)^3 has a certified upper bound below186 for every
possible old birth4<=c<=154. Every old adjacent quadruple gap is a sum
of global adjacent gaps, so this also certifies the large-gap property
for the entire core. The exact rational certificate is saved separately.

## Complete same-history profile certification

After target certification, the UNCHANGED `reference_evaluator.evaluate`
and independent output-based `independent_checker.check` were run on
the same fixed156-point sequence. Both passed:

    Original strict core records: 2435.
    All-three-old-gaps-large core records: 2435.
    UNKNOWN strict comparisons: 0.

The canonical finite profile JSON is
`C100000000000000_m02_colored_star/C100000000000000_m02_colored_star_t64_M156.json`,
SHA-256 `9234ad0557a920d67144c5d190c2663084be18e9a8ec986fe9598b0b7250d157`.
Its companion record bank and independent PASS certificate retain all
actual records. Every rational P_b, I_j, genuine component price and
one-record cut coverage agrees. In particular the last price is

    u_156^[156]
      =(alpha_156-alpha_157)/H_156^2
      =1/23095496774953809006450023095496775.

The terminal alpha_157 is retained. No numerical-output reordering of
the actual price was used. The following decimal values are only
presentation approximations, not certified square-root enclosures:

    N(156,156) ~=0.00001033069026003723572692681037234946.

| j | Actual cuts | I_j, approximate | Actual sqrt harmonic block, approximate |
|---:|---|---:|---:|
| 1..4 | 2..31 | 0 exactly | 0 exactly |
| 5 | 32..63 | 3.7721427592764504e-11 | 3.9472634713811161e-6 |
| 6 | 64..127 | 6.6709559235584370e-11 | 6.1240708073392190e-6 |
| 7 | 128..155 | 4.9093598586608148e-13 | 2.5935598131690061e-7 |

Exact fractions for every block, including the actual last cut155,
are saved in the canonical JSON. Maximum cap usage is approximately
0.00001240460794390623794, at rank3, against the SAME fixed C=10^14.
The leading total-I interval is (c,i,r)=(38,71,72), cuts39..70; the next
two are (44,70,71), cuts45..69, and (43,68,71), cuts44..67. The complete
exact birth/output masses and interval ranking are saved.

## Evidence, scope and remaining mathematical task

- `colored_star_one_candidate.py`: one explicit graph/input, independent
  actual Sidon/cap and target count checks; no broad trial loop.
- `full_colored_star_t64_certification.py`: exact target before/after
  deficits, unchanged full evaluator/checker, and large-gap checks.
- The campaign directory holds the pre-trial manifest, exact candidate,
  `result.json`, full canonical profile/records/PASS certificate,
  `target_direct_deficit_and_large_gap.json`,
  `global_large_gap_short_certificate.json` and
  `full_profile_certification_summary.json`.
- Root-independent target evidence is
  `../colored_star_root_review.json`.

This is one actual finite fixed-cap counterexample to the universal
effective-monotonicity proposal. It gives no unbounded fixed-cap
profile family and no C=1 counterexample. A22 independently excludes
fixed-size left groups from arbitrarily late large-gap cut scales at
each fixed cap. Thus no asymptotic claim is drawn from this construction.
Full-profile certification remains finite computation, not a Lean proof
or a completed U4-F/Q1 goal.

The rejected monotonicity premise must not be reused. A remaining route
must control the signed changes quantitatively, using actual cap-sensitive
correlations and simultaneous cut/future dependence. All authorized
processes finished; no graph trial or full-profile checker remains running.
