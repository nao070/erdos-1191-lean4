# A66: exact failure of a shared fresh-source boundary budget

Date: 2026-09-09. Status: independent finite PASS; the proposed inequality
beta_x <= h^2 is FALSE in the specified actual residual data.

Scope is exactly the 125 A65-unpaid records of the certified C=1,m0=2,
M=T=96 history, b=25,k=48,c=24. No new history, cut, component horizon,
original core enumeration, logarithm comparison, or full profile was run.
The existing original strict and residual certification is reused by
content hash. This task performs only exact integer/rational operations
on those physical rows and reconstructs their current graph components.

For fresh lower rank x, let h=a24-a_x. Each old g and fresh h occurs at
most once in this physical bank. The computed quantity is

    beta_x = sum_(saved records with this x) g*max(h-g,0).

Every one of the 23 possible fresh ranks is recorded, including empty
ones. All 14 strict violations and every contributing original record
are saved in A66_BOUNDARY_EXACT.json. Their fresh ranks are
1,2,3,4,7,8,9,10,12,13,14,15,16,18. The ratios beta_x/h^2 and
beta_x/(h^2/4) are exact rationals, not floating-point classifications.

## Largest violation in the prescribed bank

At x=10, a10=89 and h=714-89=625. Its ten actual old g labels give:

| Original bank index | g | Output ranks i,r | g(h-g) |
| --- | ---: | --- | ---: |
| 10211 | 159 | 36,39 | 74,094 |
| 10214 | 191 | 43,45 | 82,894 |
| 10216 | 212 | 39,42 | 87,556 |
| 10217 | 214 | 44,45 | 87,954 |
| 10218 | 227 | 37,39 | 90,346 |
| 10226 | 281 | 46,48 | 96,664 |
| 10230 | 302 | 37,38 | 97,546 |
| 10231 | 311 | 42,44 | 97,654 |
| 10244 | 416 | 47,48 | 86,944 |
| 10245 | 420 | 45,46 | 86,100 |

Thus beta_10=887,752, whereas h^2=390,625. The exact ratios are
887752/390625 and 3551008/390625 respectively. The excess over h^2
is 497,127. Each individual edge nevertheless satisfies
4*g*max(h-g,0) <= h^2. Its valid single-edge parabola bound does not
provide the proposed common budget after summing different old g.

## Actual post-A64 paths and the shared x13

The 125 rows form 87 nonempty old-g cells and 117 path components:
110 of length 1, six of length 2, and one of length 3. No cycle occurs
in this specified bank. Components were reconstructed after the A64
deletion, rather than assuming that old components remain connected.

For every actual path the signed boundary B was computed both as
sum sigma*t and from its two boundary vertices. The exact product
identity sum gh=L*g^2+g*B holds. The totals are

    sum_paths g*max(B,0) = sum_x beta_x = 8,716,524,
    sum_records g^2 = 15,887,484,
    sum_records g*(h-g) = 6,034,555,
    sum_records gh = 21,922,039.

Here the positive edge-to-path cancellation is zero. Both positive
boundary totals are 8716524/21922039 of the actual residual product
mass. Equality between them is a fact of this finite bank, not a
general replacement of a signed path boundary by its positive edges.
The pre-A64 mass was 22,127,899; the deleted record contributed 205,860.

The g=163 path 36->38->40 has B=630, g*B=102,690, and product
mass 155,828. The g=214 path on vertices 42,44,45,47 has B=1065,
g*B=227,910, and product mass 365,298. Both are retained intact.

Their shared fresh rank x13 has h=714-160=554. Across all its eight
actual old g labels, beta_13=573,314 > 306,916=h^2. Its contributors
are g=163,214,231,253,280,305,349,399, with respective positive
charges 63,733;72,760;74,613;76,153;76,720;75,945;71,545;61,845.
In particular the two retained cells contribute through the same
physical fresh source, and cannot each reset a shared h^2 budget.

## Price and verification scope

The unchanged genuine coefficient is
lambda48=1/1,148,518,878,296,832. The positive boundary component
mass is 726377/95709906524736, and the original residual component
mass is 21922039/1148518878296832. Original full u_r^[96] tails are
not replaced by this coefficient or reset; this task totals one fixed
component only. The boundary quantities are proposed charging terms,
not independently spendable physical records.

The reference read the saved physical rows once and constructed graphs
by edge traversal. A separate checker imported no evaluator: it computed
charges as max(gh-g^2,0), reconstructed components by vertex union-find,
and obtained signed boundaries directly from endpoint coefficients.
Both programs exited 0, all exact totals agree, and no UNKNOWN arose.
All source hashes and output hashes are in A66_BOUNDARY_MANIFEST.json.

This rejects the stated common-boundary-budget candidate in a fixed-cap
actual residual example. It does not prove that every constant multiple
of h^2 fails, supply an asymptotic lower bound, or refute CoreUniform/Q1.
No Lean theorem or full core norm is claimed. The bounded task is
complete, and no process remains running.
