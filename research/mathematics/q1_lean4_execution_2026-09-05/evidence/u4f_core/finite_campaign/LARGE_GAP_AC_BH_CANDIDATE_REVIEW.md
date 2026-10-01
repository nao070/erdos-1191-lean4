# Large-gap AC/BH comparison: a cut counterexample, dyadic status open

2026-09-09. Exact adversarial tests using prefixes of the two existing
certified chains, always with C=1,m0=2. No new history or size campaign.

Restrict the unchanged core to old quadruples whose three adjacent gaps
A,B,Cgap all exceed c^2/(log c)^3. Use the exact profiles

```
Q_AC=sum_quad AC(G_(minus,q)+G_(minus,s)),
Q_BH=sum_quad BH(G_(minus,s)+G_(plus,s)).
```

The proposed pointwise inequality Q_AC(b)<=Q_BH(b) is **false** for
an actual capped prefix. The weaker proposed dyadic inequality is not
refuted by the checks here and remains unproved.

## The aggregate cut counterexample

Take the existing variant chain's first 12 points:

```
(1,2,4,9,13,19,33,46,67,89,105,124), M=T=12.
```

The reference evaluator and independent output-endpoint checker both
verify this same prefix: 22 full-core records, exact prices and profile,
positive-difference/repeated-two-sum Sidon, every intermediate-rank
C=1,m0=2 cap, and all strict comparisons with UNKNOWN=0. This was a
targeted recheck of an existing prefix, not a newly generated history.

Exactly six of its core records meet the large-three-gap condition.
Their complete decomposition is:

| Old quadruple | Matching type | Actual output (i,r) | Covered cuts | AC coefficient | BH coefficient |
|---|---:|---|---|---:|---:|
| (1,4,6,7) | 3 | (9,10) | 8 | 0 | 320 |
| (1,4,6,8) | 1 | (11,12) | 9,10 | 216 | 0 |
| (1,4,6,8) | 2 | (11,12) | 9,10 | 216 | 450 |
| (1,4,6,8) | 3 | (10,12) | 9 | 0 | 450 |
| (3,6,7,9) | 1 | (11,12) | 10 | 510 | 0 |
| (3,6,7,9) | 2 | (11,12) | 10 | 510 | 882 |

All coefficients in a row use its actual output price. At b=10 only
output rank 12 contributes. With the genuine price

```
u12^[12]=kappa12/123^2=1/928118763,
```

the complete large-gap profiles, not just one selected quadruple, obey

```
Q_AC(10)=1452*u12^[12]=4/2556801,
Q_BH(10)=1332*u12^[12]=148/103124307,
Q_AC(10)-Q_BH(10)=120*u12^[12]=40/309372921>0.
```

Thus the constant-one pointwise comparison is rigorously rejected under
the actual fixed cap. This small-rank witness does not rule out an
eventual comparison after an independently fixed initial threshold, a
different multiplicative constant, or a genuinely global comparison.

## Individual-quad failures and why they are distinct

Within that prefix, the quadruple (3,6,7,9) has actual point values
(4,19,33,67), hence A=15,B=14,Cgap=34,H=63. The certified integer
threshold at c=9 is floor(81/(log9)^3)=7, so all three gaps are large.
Its minus output t=19 has endpoints (11,12); its plus output 49 is absent
from the prefix's entire positive difference bank. Both minus matchings
are strict core with six distinct endpoints. Therefore

```
Q_AC,quad(10)=1020*u12^[12],
Q_BH,quad(10)=882*u12^[12],
excess=138*u12^[12]=46/309372921>0.
```

This is the earliest M=T individual-quad violation in the existing variant
chain among its prefixes through M96. For the greedy chain the earliest
such violation is M=T=14, b=10, old quadruple (2,5,6,9), point values
(2,13,21,66), gaps (11,8,45), AC=495 and BH=512. Its two minus records
have output (13,14). The plus output occurs only at rank 15 and is absent
from T=14. Thus its excess is

```
(990-512)*u14^[14]=956/8720159175>0,
u14^[14]=2/8720159175.
```

The full greedy M14 large-gap profile nevertheless satisfies Q_AC<=Q_BH
at every cut: other quadruples compensate for this individual failure.
That demonstrates why one must not infer aggregate failure from an
individual-quad failure. The variant aggregate failure above was checked
by a separate complete six-record sum.

Minimality here is only within the two already-given chains with M=T;
it is not a claim about all possible Sidon prefixes.

## Dyadic tests and their precise scope

For the variant M12 counterexample, the actual j=3 block is 8<=b<12.
Its exact integrated difference is

```
I_AC-I_BH=-40*(u10^[12]+u12^[12])
         =-84176539/215620551020160<0.
```

So this example does not refute the dyadic comparison. The tests were
then extended over every existing prefix M=T=2,...,96 in both chains,
with all actual truncated dyadic blocks. All 450 block/horizon cases per
chain passed (900 in total). No violating block exists in this checked
range, so there is no violating-block square-root contribution to report.
No all-history dyadic inequality follows from this finite absence.

These checks preserve the genuine price at each M. If W_(j,r) is the
exact harmonic coefficient of output-r records on block j, then

```
I_j(M)=I_j(M-1)+(kappa_M/H_M^2)*sum_(r<=M)W_(j,r).
```

This finite interchange of sums was used to scan the saved records
without generating or re-enumerating histories. The endpoint M96 values
agree exactly with the earlier direct profile summation. Comparisons
with T<M are not claimed by this M=T scan.

For completeness, both M96 terminal profiles themselves pass the cut
candidate. Their largest nonzero cut ratios Q_AC/Q_BH are approximately
0.3760240253 (greedy, b=13) and 0.6155931053 (variant, b=10).
Passing at M96 did not imply passing at smaller genuine horizons.

## Evidence and unresolved work

* `large_gap_AC_BH_aggregate_candidate_existing_M96.json`: exact terminal
  profiles, cut comparisons and block values.
* `large_gap_individual_quad_counterexamples_existing_prefixes.json`:
  exact earliest per-chain individual witnesses and bounded minimality.
* `large_gap_aggregate_target_prefix_checks.json`: complete record tables,
  exact aggregate cut counterexample and comparison block values.
* `large_gap_dyadic_candidate_all_existing_prefixes.json`: every scanned
  horizon, all block outcomes and the exact finite-price update scope.
* `C1_m02_dense_variant1_M12_independent_check.json`: independent small
  prefix verification bound to its input and checker by SHA-256.

The pointwise and individual constant-one claims are rejected; the dyadic
claim remains an unproved candidate. These are intermediate comparisons,
not the frozen uniform-core theorem. Q1 and its final Lean chain remain
unresolved. Next action: pursue an independently justified block or joint
profile estimate, retaining actual output eligibility and genuine prices.
