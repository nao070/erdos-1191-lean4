# A78 independent common-fiber kernel review

Status: PASS. The exact unfiltered kernel and its selected-record interpretation are valid. The proposed length-product upper bound and natural PSD completion have a certified counterexample among actual original strict-core records. Those records are paid by A53, so this does not refute such a bound on the later surviving remainder.

## Actual fibers and support separation

Fix the cut b and component k, use old ranks 1,...,b-1 and actual future ranks b+1,...,min(k,T), and form the fibers of a_u+a_v+f_q with u<v. If two distinct triples in a fiber shared a point, cancellation would give equal remaining two-sums. Literal Sidon makes the remaining unordered pairs equal; old/future separation and u<v then make the original index triples equal. Hence distinct fiber triples have six disjoint endpoints, distinct future coordinates, and disjoint old pairs.

The fiber-size bound min(floor((b-1)/2),m) follows from this separation. It supplies no uniform norm estimate by itself.

## Independent algebra for the kernel

Let the two old intervals have endpoints x0<x1 and y0<y1, lengths L=x1-x0 and J=y1-y0. Write delta=(x0+x1)-(y0+y1). The common fiber equation gives |delta|=t, the positive actual future difference.

There are two cross-source matchings. Their signed endpoint products are

    (x0-y0)(x1-y1)=[delta^2-(L-J)^2]/4,
    (x0-y1)(x1-y0)=[delta^2-(L+J)^2]/4.

Exactly when one such signed product is negative, its two signed differences have opposite signs. Their positive magnitudes are actual old source labels whose difference is |delta|=t, and their positive product is the negative of that signed product. The source matching contributes once in this case and contributes zero otherwise. Thus the total is exactly

    K(L,J,t)=([(L+J)^2-t^2]_+ + [(L-J)^2-t^2]_+)/4.

Distinct old endpoints exclude a zero cross difference. Sidon and distinct future points exclude t=0 and equality of distinct positive source labels. The actual integer inputs also make the displayed numerator divisible by four.

Ordering the four old points as p<q<s<c, with adjacent physical gaps A,B,C and span H=A+B+C, gives:

- Interlaced intervals (p,s),(q,c): t=A+C and K=BH.
- Nested intervals (p,c),(q,s): t=|C-A| and K=BH+2AC.
- Separated intervals (p,q),(s,c): t=A+2B+C>H and K=0.

In the nested case the two original source products are AC and AC+BH; they are separate physical records. Unique output difference does not identify their different source pairs.

## Bijection and strict filtering

An original oriented record d=a_y-a_x>e=a_z-a_w with output i<r satisfies

    a_y+a_w+a_i=a_x+a_z+a_r.

This specifies its unique unordered pair of fiber triples, sorting each old pair internally. Conversely, the positive cross-source matchings above reconstruct the eligible original source/output records for that pair. This gives the unfiltered identity across every birth below the cut. Birth c=3, if included in the sum's notation, contributes zero because four distinct old source endpoints are required.

The unfiltered kernel drops the original strict-log and residual selectors. For the original selected mass each reconstructed physical record must retain its own gate; in particular the two nested records can have different smaller source birth ranks. Multiplication by an independent common gate for both would be unjustified. The sum with these individual selectors is an exact selected kernel between zero and K.

No record or cut interval is duplicated by reindexing through fiber pairs. Genuine-price summation uses the original lambda_k, the same v=min(k,T), selectors inside the component sum, and every k>T tail. The proof changes neither u_r^[M] nor alpha_(M+1).

## Independent fixed-component arithmetic

The two prescribed actual domains were reconstructed directly from their saved point inputs, including every old pair below b=25 and every future point in the indicated component window. All fiber pairs were compared with the saved certificate, and every K was independently checked against the two direct signed cross-source products above. This is not a full-profile or strict-core re-enumeration.

For C1,m0=2,M=T=96,b=25,k=48:

- 6,348 mixed triples, 1,947 nontrivial fibers, largest fiber size 5.
- 4,098 fiber pairs: 1,247 nested, 1,499 interlaced, 1,352 separated.
- 3,993 represented unfiltered positive-source records.
- Exact unfiltered product total 257,942,228.

For the existing C=2^67,m0=2,M=T=50,b=25,k=50 input:

- 6,900 mixed triples and one nontrivial fiber of size two.
- One interlaced fiber pair and one represented unfiltered record.
- Exact product total 319014718988636095646352980968623575040.

The enlarged all-birth domains differ from the single-birth A77 domains and the selected A76 record subsets. The calculation does not newly certify every unfiltered record's strict gates.

## Actual strict-core length-product and PSD counterexample

In the unchanged C1 history, fiber sum S=1035 contains old pairs (1,12),(3,5) with actual future ranks 26,27:

    old values 1,4,13,124; future values 910,1018,
    1+124+910=4+13+1018=1035,
    L=123, J=9, t=108.

The adjacent old gaps are A=3,B=9,C=111. Therefore

    K=BH+2AC=1107+666=1773 > 1107=LJ.

The two original records are

    [111,3,5,12,1,3,12,3,26,27,108],
    [120,12,3,12,1,5,12,5,26,27,108].

They occur exactly once at zero-based indices 427 and 516 of the saved original core bank. All endpoint arithmetic and all five original strict comparisons were independently rechecked using both existing rational logarithm interval methods. Every lower margin is strictly positive, with UNKNOWN=0. Their products are 333 and 1440; each original cut interval is [13,25], so both cover cut 25.

The natural symmetric completion has diagonal K(L,L,0)=L^2. Its actual two-point matrix is

    [[15129,1773],[1773,81]],

with determinant -1,918,080. The vector (3,-41) has quadratic value -163,836. This disproves PSD of that completion. Its diagonal is an auxiliary kernel convention, not an assertion that a self-pair is an original physical record.

Both records have the same original positive u_27^[96]; hence 1773*u_27 remains strictly larger than 1107*u_27. The evidence stores that complete genuine tail, their full prices, lambda48=1/1148518878296832, and the nonzero alpha97. No price is reset or attached to a missing record.

The same two logarithm methods certify

    21 < 12*(log 12)^(5/8) < 22,
    A53 L(12)=ceil(12*(log 12)^(5/8))+1=23.

Thus component 48 is in the A53 paid class. Since the actual upper output rank is 27>=23, the full original tails of both records are also in that paid class. This witness refutes the shortcut on actual original core, but supplies no counterexample on the current fully localized residual.

## Scope and binding

No new history, full-profile rerun, A72 generator invocation, optimizer, Lean build, or root-source edit was performed. Existing fixed-cap certification was reused by hash. Only these two prescribed witness records received fresh strict interval checks. The kernel computation and independent checks completed with no remaining process.

The positive nested correction must be retained. The actual joint fiber structure and fixed cap still need an analytical estimate; no selected square-root harmonic uniform norm, frozen U4F, or Q1 result follows.

- Reviewed WORKING_PROOF whole SHA: `e4925e81dcc54899a87e19ebf691c1ab8ff970ee2c17e7b3e7d12891665f8889`.
- A78 section SHA: `70f2fc1003a6dcdca1d6084680f0fb995fe496bdce2e7694f78825b346519d00`.
- `A78_COMMON_FIBER_KERNEL.json`: `4ba427024fa1c2431a793e7d46be9ee3b1fde556ccea4fe5cb48edcd07755e9a`.
- `A78_INDEPENDENT_CHECK.json`: `b8831ee9a770c2087c32115c158384f62fb0a43fc79ac4713c9296a237e36e01`.

The independent JSON binds the actual inputs, original core bank, logarithm helpers, and relevant preceding certificates. It stores both strict-margin methods and all exact witness prices. The proof binding is the reviewed snapshot; the root researcher owns subsequent integration.
