# Independent review of final A20-A23 and the fixed-cap support bound

2026-09-09. Verdict: PASS for the mathematical claims, finite evidence
and logical scope of final WORKING_PROOF A20-A23. Final source hashes
and exact sections are stored in `A20_A23_final_review_manifest.json`.
The previously reviewed A16-A19 section bytes remain unchanged.

## A20: historical finite test and necessary graph constraints

The two C=1 M96 record-bank scans, 82,335 saturated cells per history,
and exact worst ratios3/8 and1/3 match the saved independent results.
They remain true finite statements after the later C=10^14 counterexample;
they did not and do not prove a universal margin.

The elementary bound v_old(z)<=d-1 at a newly occupied site gives
J_core<=J<=(d-1)S, with precisely the missing factor two recorded.
The compensation formula with R_new=J-J_core is algebraically correct.
The new colored-star example has R_new=17 but needs at least
J-(d-1)S/2=88-64=24, so its actual compensation fails by7 collisions,
producing an effective increment of -14.

For an actual two-point left group, same-sign shared source/target
would repeat an old right-point difference among future points. Hence
each sign class has in-degree and out-degree at most one. A double-
signed ordered edge produces a future difference2h; two distinct such
edges would give distinct endpoint pairs for that same positive
difference. At most one is possible. These are necessary conditions
only, just as A20 states; the complete actual Sidon test is decisive.

## A21: the integer monotone relaxation is valid but not realizable evidence

Let S=l(n-l), d=min(l,n-l,m), and B=(d-1)Sm/2. For m>=1, B is
nonnegative and nondecreasing; B(0)=0 separately. It is an integer:
if d is odd, d-1 is even; if d is even, at least one factor of Sm is
even, since d equals one of l,n-l,m. No fractional capacity is rounded
prematurely.

With C_*=floor(B/2),

    2B-2C_*=2ceil(B/2),

so both the abstract count and effective deficit are nondecreasing.
After saturation d is one of the two old side sizes; therefore
Delta B=(d-1)S/2 is an integer. For an integer increment a>=0,
floor((B+a)/2)-floor(B/2)<=a, giving the displayed saturated bound.
At the pre-saturation transition Delta B=mS, so the abstract arrays
are also consistent with the elementary pre-saturation increment bound.

The relaxed U profile is H_b sum price*g_l*B, whereas V replaces B by
floor(B/2). On the retained b>=16,2b<=k<=3b,l interval, every B>=2;
floor(B/2)>=B/4 proves V>=U_retained/4. Thus the constant
1/(4096*3^9)=1/80621568 is correct, including the common component
prices and original terminal subtraction convention.

These are abstract integer counts attached to the non-Sidon triangular
diameter sequence. They do not assert simultaneous realization by
actual fibers, gates or old widths. This is a no-go for deriving the
weighted norm solely from the listed scalar/capacity/monotonicity
conditions, not an actual Sidon/profile/Q1 counterexample. A23 now
separately rejects monotonicity itself; A21's strength test remains valid.

## A22: exact exclusion of a short left group under the fixed cap

For a remaining record, A=a_q-a_p>c^2/log(c)^3. If q>=m0,

    A<=H_q<=C q^2 log(2q)<=2C q^2 log(c),

because q<=c and 2q<=c^2 for c>=3. Taking positive square roots gives
q>c/(sqrt(2C)log(c)^2). Original coverage and the original far-output
gate give b<r<c log(c)<c log(b), hence c>b/log(b). Combining the
strict inequalities gives the stated

    q>b/(sqrt(2C)log(b)^3).

The q<m0 exception is handled without assuming a capped extension.
For B0=C*m0^2*log(2m0), c0=max(m0,3,ceil((B0+1)^2)) ensures that
when c>=c0, the rank m0 already exists and A<=H_m0<=B0. But
log(c)<sqrt(c) gives c^2/log(c)^3>sqrt(c)>=B0+1, a contradiction.
For c<c0, the increasing function c log(c) and the original strict
gate instead imply b<c0 log(c0). Thus b>=ceil(c0 log(c0)) excludes
the exceptional old partner. All thresholds depend only on fixed C,m0.

Since every diagonal channel requires q<=l<s, the claimed zero-support
region l<=b/(sqrt(2C)log(b)^3) follows exactly for sufficiently late b.
It is a statement about the all-three-old-gaps-large remainder, not a
redefinition of core. The same old/output support test holds in each
genuine component, including k>T. The threshold grows without bound
with b, so a fixed left size such as l=2 is confined to finitely many
cut scales at each fixed cap. No mass bound on the surviving balanced
region is thereby proved.

## A23: independent target and complete-profile consistency

The exact candidate input hash, one-trial scope, actual t64/M156 data,
J_raw88,J_core71=47minus+24plus, all71 large gaps, and the before/after
fiber table match the worker's independent exact reconstruction and
`../colored_star_root_review.json`. The new point changes raw delta
by -48 and gate deletion by+17; D_eff changes by-48+34=-14.

The unchanged complete evaluator and independent output-centric checker
subsequently pass on that same history: 2435 core records, all2435
large-gap, UNKNOWN0, exact rational profiles/I/coverage/genuine prices,
and every original fixed-C rank cap. The saved canonical profile hash
and exact u156 in A23 match the output. The block decimals, N, maximum
cap usage and leading three coverage intervals are faithful rounded
presentations and are explicitly not certified square-root enclosures.

A short additional independent large-gap certificate uses the global
minimum adjacent point gap13184 and the rational upper bound below186
for every old threshold c^2/log(c)^3 through c=154. This confirms the
all2435 large-gap statement without another profile evaluation.

The current status is that saturated gate-adjusted monotonicity is
FALSE in general, including the large-gap version. Earlier A19/A20
unproved-candidate language records the earlier stage and is explicitly
superseded by A23 and the current frontier. No C=1, asymptotic fixed-cap,
uniform-K or Q1 refutation is asserted. The signed increment identity
remains valid. No extra graph trials, t96 history or new Lean run was
performed, and the complete checker process has exited successfully.

## Final source binding and restart obligation

Final WORKING_PROOF SHA-256:
`e0ee7a37f94a7c2da35ceb82ad399bf0af1bb81c3dc18f7b2722d34dd9b4b493`.

- A20: `7b1e669475e7f1181902e39515cfc113d9d392dec771e64ab67a4e4c1285ac76`
- A21: `10c4898473785937ea4cb8c0dfca0ac79fd4bb4a1644de084c35ea0788734e41`
- A22: `378546fd9fc52037261d6f3eecd2ea9cae429f550e960971d13ab7998509c160`
- A23: `046e546b6636e907c247f813916174a29ce7babc6328b59e45ef847f78c24b37`

The remaining problem is a quantitative signed/compensated estimate
using actual fixed-cap correlations in the surviving group/cut region.
Effective-deficit monotonicity must not be reused as a premise. The
finite counterexample and complete finite profile are not the frozen
uniform theorem, and the original Q1/Lean final closure remains absent.
