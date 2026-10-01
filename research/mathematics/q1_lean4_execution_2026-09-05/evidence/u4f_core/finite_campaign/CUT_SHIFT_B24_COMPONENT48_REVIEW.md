# A24: exact cut-shift identities and failed retirement domination

2026-09-09. All requested exact identities PASS. The proposed inequality
retirement>=birth is FALSE in the existing fixed C=1,m0=2 histories,
both as a universal count claim and as a BH-weight claim. This is one
cut transition at one genuine component, not an asymptotic or Q1 claim.

## The precise banks for cut24 to cut25

Only the two already-certified M=T=96 histories are used. Fix component
k=48 and l in{6,12,18}. In rank notation put

    L={1,...,l}, R={l+1,...,23}, F_common={26,...,48}.

For actual integer point values define the sum-count banks

    u=L*R*F_common,
    w_plus=L*{a_24}*F_common,
    w_minus=L*R*{a_25},
    v_before=u+w_minus, v_after=u+w_plus.

The stars here denote finite additive convolution. They are the actual
point banks, not independent scalar arrays. For each fixed added point,
Sidon two-sum uniqueness makes w_plus and w_minus zero-one; both were
checked directly. The common u can have multiplicity.

For C(v)=sum_z binom(v_z,2), zero-oneness gives EXACTLY

    C(v_before)=C(u)+sum_z u_z*w_minus,z,
    C(v_after)=C(u)+sum_z u_z*w_plus,z,
    Delta C_raw=sum_z u_z*(w_plus,z-w_minus,z).       (1)

No assumption of disjoint w_plus and w_minus supports is needed.
Their overlap counts are zero at l6 andl12 in both histories, but at
l18 they are2 for greedy and3 for variant. Those overlapping sites
have identical added/removed value1 and hence cancel in (1). All sites,
common multiplicities and associated added/removed triples are saved.

Write N_before=l(23-l)*24, N_after=l(24-l)*23 and
d_before=min(l,23-l,24), d_after=min(l,24-l,23). Then

| l | N_before | N_after | d_before | d_after | Capacity before | Capacity after |
|---:|---:|---:|---:|---:|---:|---:|
| 6 | 2448 | 2484 | 6 | 6 | 6120 | 6210 |
| 12 | 3168 | 3312 | 11 | 12 | 15840 | 18216 |
| 18 | 2160 | 2484 | 5 | 6 | 4320 | 6210 |

Capacity means (d-1)N/2. The raw deficit satisfies
delta=(d-1)N-2C_raw, so Delta delta=2 Delta capacity-2 Delta C_raw.
Both sides were computed exactly from the full actual counters:

| History | l | Raw C before | Raw C after | u dot w_plus | u dot w_minus | Delta C_raw | Delta delta |
|---|---:|---:|---:|---:|---:|---:|---:|
| Greedy | 6 | 489 | 509 | 62 | 42 | 20 | 140 |
| Greedy | 12 | 900 | 1010 | 187 | 77 | 110 | 4532 |
| Greedy | 18 | 353 | 497 | 173 | 29 | 144 | 3492 |
| Variant | 6 | 545 | 573 | 63 | 35 | 28 | 124 |
| Variant | 12 | 1003 | 1122 | 188 | 69 | 119 | 4514 |
| Variant | 18 | 416 | 576 | 189 | 29 | 160 | 3460 |

## Original strict-core boundary identity

Independently of the raw-counter calculation, the saved original
strict-core BH record banks were filtered by r<=48 and q<=l<s.
Only type-2 minus and type-3 plus records contribute BH; type-1 minus
is not counted again. A record is covered precisely when c<b<i.
Under b24->25, its membership can change only as follows:

    birth: c=24 and i>25;
    retirement: c<24 and i=25.

The empty coverage case c=24,i=25 belongs to neither boundary. Common
records keep their exact strict gates and weights. For the full core
or the same fixed all-three-old-gaps-large quadruple selection,

    C_core(25,l,48)-C_core(24,l,48)
      =birth_count-retirement_count.                (2)

Define R_l(b)=sum B*Hquad over those physical BH matching records.
This is the actual l-selected BH mass coefficient, not the diagonal
count times an invented typical width. The exact weighted identity is

    R_l(25)-R_l(24)=sum_birth B*Hquad-sum_retire B*Hquad. (3)

The two cuts use the SAME genuine component weight kappa_48/H_48^2:

    Greedy: 1/1250168711457792;
    Variant: 1/1148518878296832.

Multiplying all four terms of (3) by this coefficient gives the exact
priced component identity. No terminal alpha, output rank, diameter or
price is changed. Original strict gates for every boundary record were
rechecked independently, UNKNOWN=0. The earlier full independent
certificates bind each input history and original record bank.

## Exact failures of retirement>=birth

The following are UNPRICED BH coefficients, not Decimal approximations.

| History / selection | l | Birth count | Retirement count | Count change | Birth BH | Retirement BH | BH change |
|---|---:|---:|---:|---:|---:|---:|---:|
| Greedy / full core | 6 | 58 | 38 | 20 | 12195944 | 2081639 | 10114305 |
| Greedy / full core | 12 | 171 | 62 | 109 | 39608795 | 6112113 | 33496682 |
| Greedy / full core | 18 | 157 | 18 | 139 | 44304153 | 3114722 | 41189431 |
| Variant / full core | 6 | 58 | 31 | 27 | 9930693 | 1730269 | 8200424 |
| Variant / full core | 12 | 175 | 56 | 119 | 36454312 | 5037149 | 31417163 |
| Variant / full core | 18 | 173 | 18 | 155 | 40205665 | 2177883 | 38027782 |
| Greedy / large gaps | 6 | 7 | 14 | -7 | 1860295 | 696617 | 1163678 |
| Greedy / large gaps | 12 | 126 | 50 | 76 | 27948661 | 4742453 | 23206208 |
| Greedy / large gaps | 18 | 138 | 16 | 122 | 37061484 | 2618108 | 34443376 |
| Variant / large gaps | 6 | 3 | 5 | -2 | 571826 | 147453 | 424373 |
| Variant / large gaps | 12 | 135 | 45 | 90 | 26925618 | 3799727 | 23125891 |
| Variant / large gaps | 18 | 159 | 17 | 142 | 35197495 | 1963900 | 33233595 |

Thus count domination already fails in ten of the twelve specified
selected cases. BH-weight domination fails in ALL twelve. In the two
large-gap l6 cases, the record count DECREASES while the actual BH mass
INCREASES. Count domination alone therefore cannot justify weighted
domination even at this one component.

For completeness, the same saved rows also give the WHOLE BH coefficient
with no l filter; each physical matching is counted just once here:

| History / selection | Birth count | Retirement count | Count change | Birth BH | Retirement BH | BH change |
|---|---:|---:|---:|---:|---:|---:|
| Greedy / full core | 399 | 153 | 246 | 66881755 | 8171465 | 58710290 |
| Variant / full core | 423 | 128 | 295 | 61811319 | 7362010 | 54449309 |
| Greedy / large gaps | 329 | 116 | 213 | 54160707 | 6478282 | 47682425 |
| Variant / large gaps | 351 | 97 | 254 | 51233803 | 5687322 | 45546481 |

The separate l-filtered rows are not summed as independent budgets.
They are parallel tests of the specified l-dependent quantity.

## A small complete weighted counterexample within the existing variant

At l=6 in the large-gap selection, the COMPLETE three birth and five
retirement BH records are listed below. All refer to the same actual
certified variant M96 prefix; p,q,s,c are old ranks.

| Boundary | Old quadruple | BH type | (i,r) | B | Hquad | B*Hquad |
|---|---|---:|---|---:|---:|---:|
| Birth | (1,6,9,24) | 2 | (30,35) | 48 | 713 | 34224 |
| Birth | (1,6,18,24) | 3 | (32,35) | 332 | 713 | 236716 |
| Birth | (1,6,20,24) | 3 | (42,43) | 422 | 713 | 300886 |
| Retirement | (2,6,7,14) | 2 | (25,26) | 14 | 184 | 2576 |
| Retirement | (2,6,9,14) | 3 | (25,26) | 48 | 184 | 8832 |
| Retirement | (1,6,10,18) | 2 | (25,27) | 70 | 350 | 24500 |
| Retirement | (2,6,12,18) | 3 | (25,27) | 105 | 349 | 36645 |
| Retirement | (1,6,15,18) | 3 | (25,26) | 214 | 350 | 74900 |

The retained core count changes84->82, while R_l changes
5348845->5773218. Its strictly positive genuine priced increment is

    424373/1148518878296832.

The exact prefix through component48, all eight original11-column
record rows, strict selectors and source hashes are saved in the
compact witness JSON. A separate compact count witness contains all
16 greedy large-gap l18 retirements and17 certified births, already
sufficient to violate the unweighted candidate; the full result records
all138 births and the exact increase122.

## Scope and remaining task

`cut_shift_b24_component48.py` is the minimal actual-bank and record
check for the specified two histories, one component, one cut transition,
and three left-group sizes. `cut_shift_b24_component48_exact.json`
stores the full common/add/remove banks, overlap sites, capacities,
raw/core/effective deficits, exact priced and unpriced masses and every
boundary record. `cut_shift_b24_compact_counterexamples.json` holds the
smaller explicit witnesses. `cut_shift_b24_review_manifest.json` binds
the exact claim, scope and evidence hashes.

There was no broader cut scan, new history, full-horizon recomputation
or new Lean run. These results reject the proposed pointwise retirement
domination, including its large-gap weighted version. They do not prove
failure of a compensated or summed flux estimate and do not refute
uniform U4-F or Q1. Both the counter identity and weighted boundary
identity remain useful; the next estimate must keep unequal physical
BH weights and allow positive cutwise net birth.
