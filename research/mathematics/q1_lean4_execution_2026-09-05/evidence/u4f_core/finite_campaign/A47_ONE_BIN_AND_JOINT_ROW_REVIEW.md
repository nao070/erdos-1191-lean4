# A47: one actual old-label bin and its shared output use

Date: 2026-09-09. Status: PASS exact bounded reference and independent checks.
No new history, source pair, bin, full profile, or Lean run.

## Fixed data and the single-row correspondence

Reuse the independently certified C=1, m0=2, M=T=96 variant history.
Fix b=25, k=48, x=1, y=22, d=a22-a1=603, and first fix lower output
i=42, a42=2975. Reuse J25=33 as certified by A46. The sole bin is
h=9, [hJ,(h+1)J)=[297,330). For every source label e in this bin,

    a_r=d+a_i-e=3578-e,
    3248<a_r<=3281.

The half-open integer window has 33 integer positions, rather than a
closed interval of diameter 33. The actual future points through k48
intersect this window only at a43=3266.

All labels below are actual unique positive differences of the first
24 points. The complete bin contains 13 labels with sum e=4025.

| e | unique old pair (w,z) | mapped value 3578-e | actual r at i42 | extra old-source exclusion |
|---:|---|---:|---|---|
| 299 | (5,17) | 3279 | absent | none |
| 302 | (18,23) | 3276 | absent | none |
| 303 | (4,17) | 3275 | absent | none |
| 305 | (8,18) | 3273 | absent | none |
| 307 | (15,21) | 3271 | absent | none |
| 308 | (3,17) | 3270 | absent | none |
| 310 | (2,17) | 3268 | absent | none |
| 311 | (1,17) | 3267 | absent | shares x=1 |
| 312 | (10,19) | 3266 | 43 | none |
| 313 | (19,24) | 3265 | absent | none |
| 317 | (12,20) | 3261 | absent | none |
| 318 | (7,18) | 3260 | absent | none |
| 320 | (16,22) | 3258 | absent | shares y=22 |

The source exclusions leave 11 labels and sum e=3394. They are separate
flags from output absence: e311 and e320 fail both tests. No fake rank
is assigned to an absent output. Its rank-dependent strict gates are
NOT APPLICABLE, not UNKNOWN and not silently declared satisfied.

The sole usable label at i42 is e312, with original bank index 9681:

    [603,312,1,22,10,19,22,19,42,43,291].

It retains six distinct endpoints, all five original strict inequalities,
old quad (1,10,19,22), gaps (88,312,203), cut coverage 23,...,41, and
all original large-gap/A45/A46 selections. At this cut it has e>144,
t=291>33 and every old gap>33. Its k48 is central and near-span by the
already certified A44 inequalities. Strict/gap enclosures are copied
with source binding from the original saved record and independently
rechecked using the independent fixed-point log implementation.

Thus bin label mass 4025 is not fully available to this actual row:
used mass=312, unused mass=3713, exact used fraction=312/4025. Multiplying
by the fixed d603 gives allowance 2427075, actual row weight 188136,
and unused allowance 2238939. These are a finite counterexample to
automatic full utilization of the bin by this row, not a global bound
or an asymptotic deficit fraction.

## Same thirteen labels shared by all lower outputs

The only extension examines these same thirteen labels at the same
source pair, cut, and component. For each t=603-e, a forward endpoint
membership lookup and an independent reverse lookup recover its unique
actual output pair, if present in this finite M96 history. No new bin
or source pair is scanned.

| e | t | unique actual output pair in M96 | decision at b25,k48 |
|---:|---:|---|---|
| 299 | 304 | (24,27) | lower output not after cut |
| 302 | 301 | (39,41) | strict and full remainder PASS |
| 303 | 300 | absent | difference absent in this history |
| 305 | 298 | absent | difference absent in this history |
| 307 | 296 | (11,19) | lower output not after cut |
| 308 | 295 | absent | difference absent in this history |
| 310 | 293 | (6,17) | lower output not after cut |
| 311 | 292 | (17,22) | lower output not after cut |
| 312 | 291 | (42,43) | strict and full remainder PASS |
| 313 | 290 | (88,89) | upper output exceeds component48 |
| 317 | 286 | absent | difference absent in this history |
| 318 | 285 | (25,28) | lower output equals cut |
| 320 | 283 | (1,16) | lower output not after cut |

This disjoint failure partition has four absent output differences, six
lower outputs not after the cut, one late upper output, and two used
records. Source or six-endpoint failures are separately recorded and
may overlap these primary reasons. Gates outside the prescribed component
are not tested at another cut/component.

The added usable label is e302, with original bank index 9680:

    [603,302,1,22,18,23,23,22,39,41,301].

Its de=182106, old gaps (350,253,49), and original coverage 24,...,38.
Both used records pass all original gates and the A46 remainder. Their
full records match the existing A29 original pool exactly. Their strict
gate margins and all-large gaps have independent rational verification.
Joint use is therefore

    used labels={302,312}, sum used e=614,
    B=d*sum_bin e=2427075,
    Q=sum_actual_records de=370242,
    B-Q=2056833.

For the 22 possible lower-output rows i=26,...,47, only i39 and i42
have weights 182106 and 188136. Assigning the full same B independently
to every row would give the different quantity

    sum_i(B-row_used_i)=53025408,
    sum_i(B-row_used_i)-(B-Q)=50968575=21B.

This is an exact shared-budget identity, not merely a numerical warning.
The single shared bin is counted once in B-Q. Independent row resets
count it 22 times. Consequently a large single-row unused allowance
cannot be summed across rows as independent source-bank savings.

## Genuine prices and verification scope

All component statements above retain

    lambda48=kappa48/H48^2=1/1148518878296832.

The evidence separately records lambda48 times every component mass and
deficit. Each actual record also retains its distinct genuine full tail
u41^[96] or u43^[96], evaluated as sum_{j=r}^{96} kappa_j/H_j^2 and
independently as sum of (alpha_j-alpha_(j+1))/H_j^2. The terminal
alpha97 is preserved. The exact rational full tails are in the JSON;
they are not replaced by lambda48 or assigned to nonexistent outputs.
No full-horizon price is inferred for an unused label lacking an actual
eligible output.

The independent single-row checker scans only integers 297,...,329 and
uses old-value membership instead of the reference difference enumeration.
The joint checker performs only the thirteen authorized forward/reverse
output lookups, reuses the original pool, and uses two log/price formulas
for the two present records. All checks PASS; UNKNOWN=0. Existing fixed
all-rank cap/Sidon certification is reused by content hash, without a
new full-history check. No process or search is left running.

This finite result rejects full single-row use and independent addition
of row deficits. It supplies neither a uniform shared deficit fraction
nor the square-root harmonic norm. The next nonduplicate mathematical
action is to retain the actual common label window and incompatible
output geometry in a joint transport estimate; A48 identifies a weaker
rowwise packing relaxation that cannot improve the existing common bank.
Source, evidence, script and note hashes are in `A47_A48_review_manifest.json`.
