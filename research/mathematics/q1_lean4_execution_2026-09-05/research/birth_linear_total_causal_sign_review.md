# Independent review of the birth-linear full causal total

Result: **the mathematical identities and stated conditional implication are accepted; the full-total asymptotic lower bound remains open**. Reviewer: `/root/moment_evidence_audit`. Date: 2026-09-05T07:40:50.767314+00:00. The complete note and complete exact checker were read. The successful fixture checker was not rerun, and no Lean verification is claimed. Original Q1 is unresolved.

## 1. The target and automatic part

The target is `X_z=L(z)+S/2`, where L is the quadratic sum over all source pairs whose output is already available when both source labels have been born: `tau(|d-e|)<=max(tau(d),tau(e))`. Birth-class centering makes the same-birth part exactly `-S/2`; therefore X_z is precisely the quadratic mixed-birth Born total (1). It is neither `L-Ret` nor the linear statistic `B_lin=sum(z_d+z_e)`. Retiring mixed pairs are not silently included with a minus sign.

A coincident three-term multiset relation with three nonzero oriented edges is a directed three-cycle. For h<i<j, its two used source pairs share the lower endpoint h or the upper endpoint j. The latter has equal source births and cancels from X_z. The former contributes `z_ih*z_jh`. Summing each lower-endpoint column gives exactly `(sum_h C_h²-S)/2`, proving (2). Its lower bound is `-q/2`. No sign is assumed for each individual product.

## 2. Direct six-distinct fibers

The endpoint equation (4) is correct. Given a mixed-birth source pair, its larger birth n determines the new source `a_n-a_i`; the old source is `a_j-a_h`. The actual signed output difference fixes the ordered smoothing endpoints k,l uniquely by Sidon difference injectivity. This assigns exactly one unordered equal-three-sum collision.

For six distinct endpoints, the largest endpoint a_n must be a source upper endpoint for a Born record; if it occurred only as an output endpoint, that record would retire later than both sources. Thus the orientation with a_n in U and all of T earlier loses no Born record. Conversely, choose j in T, h in U without a_n with h<j, and either i in T without a_j. The remaining endpoints k,l satisfy (4), all source labels are positive, the two source births differ, and the output is already available. The pair and its unique endpoints recover these choices, proving absence of duplication.

Summing `m_n-a_i` over the two choices gives `2m_n-s+a_j`, which proves (3). There are at most 3*2*2=12 records and every normalized product has magnitude at most one. For a complete fiber, distinct triples have disjoint supports; their older endpoints therefore occur exactly once in J_old, justifying the regrouping (6). Neither formula supplies a sign for the summed fiber.

## 3. Repeated-point error and full reduction

Distinct equal-sum triple multisets cannot share a point: cancelling one copy would give equal two-sum multisets, forcing the original triples identical by repeated-summand Sidonness. There are at most N² repeated-point triple multisets, represented as {a,a,b}, and at most N distinct partners for each, since all supports within that fiber are disjoint. Hence at most N³ unordered collisions need be retained, with harmless overcounting.

A matching of the three slots has at most six choices. Its three signed edge lengths sum to zero; after excluding zero edges, one absolute length equals the sum of the other two. At most the two pairs involving the largest length give source-pair records. Repeated slots or equal lengths only reduce the number. Thus at most twelve records per collision suffice and `|D_rep|<=12N³` is valid. Combining all three disjoint categories proves (5), including its error constant. A lower bound `sum Phi>=-O(N³)` would imply the desired full-total bound, but none is proved.

## 4. Cut representation and feasible gaps

The coefficient of delta_k in the old mean is the proportion of old ranks greater than k. Subtracting the coefficient of a_h yields exactly the three cases of v^k in (7). There is no contribution from the newborn endpoint to its own class coefficients. The symmetric adjacency convention consequently gives `H²X_z=delta^T K delta` with the factor 1/2 in (8); the checker uses the same convention.

Equation (9) follows by expanding every endpoint as `a_1+sum_(k<i)delta_k`; the translation term cancels. It is a necessary constraint, not a complete characterization of a valid fixed graph. Positivity of all actual gaps, retained three-sum equations, excluded unrecorded equalities, and difference uniqueness must all be respected.

For the six-point matrix the sole negative cross coefficient is -37/240. Absorbing `-2(37/240)delta_1*delta_3` into the two squares leaves 641/240 and 119/240, exactly as stated. This proves copositivity of that fixed form, not a universal form property.

For the 32-point selected entries, writing a=K_11 and b=K_1,30<0 gives the relaxed value `a+2b*(a/(-2b)+1)=2b<0`. The displayed actual relation has gap coefficient +1 at cuts 1 and 30, so its violation is exactly `1+delta_30>0`. The relaxed vector already allows zero gaps and additionally violates a required equality; it is not an actual Sidon negative-total example. This distinction is correctly preserved.

## 5. Actual demand implication

The historical capacity change for `W=J+zz^T/8` is X_z/8. The actual moment raw-demand increase relative to J is `(LB(B)-mS)/16`, with the same denominator and complete diagonal charge. Adding these proves (10). If the unproved full-total bound `X_z>=-C_0N³` held, `S<=q` gives (11) with both error terms and their factors intact.

On the stated extended good epochs, `m=N` and `LB(B)>=c q²/log(2N)` with fixed c>0; this dominates `2C_0N³+Nq` eventually. The identity is a raw-demand comparison; any replacement by positive parts uses the separate eventual positivity in the cited good-epoch argument. It establishes neither repeated spending across epochs nor the missing full-total bound.

## 6. Exact-check scope and provenance

The script uses Python's standard-library `Fraction`, integer endpoint arithmetic, and two fixed fixtures. Its source checks all positive differences for distinctness and each class sum for zero. It directly enumerates physical mixed-born pairs, separates automatic/repeated/six-distinct cases, and independently enumerates unordered distinct-triple fibers. It compares the **aggregate** direct-fiber sum with the six-distinct physical-pair sum. All 3374 pairs in the 32-point fixture enter that aggregate; there are not 3374 separate per-pair equality assertions. The parent's current note explicitly states this distinction.

The six-point full cut matrix is computed, and its quadratic value at the actual gaps is compared with H²X_z. Only the selected three entries needed for the 32-point relaxed obstruction are computed there. The script's observed repeated-error assertion is a fixed-fixture check; the universal 12N³ bound comes from the mathematical argument above. No floating diagnostic output is used as a certificate. Static inspection found no floating literals, and the displayed exact decompositions are arithmetically consistent.

The author supplied a retrospective record from retained tool results, saved as `research/evidence/birth_linear_total_causal_sign_exact.run.json`. It records the original redirected command `python3 research/evidence/birth_linear_total_causal_sign_exact.py > research/evidence/birth_linear_total_causal_sign_exact.txt`, the correct working directory, chunk `0166c3`, reported exit code 0 and elapsed time 0.735349167 seconds. Chunk `0949c6` records the subsequent complete stdout readback. I independently verified that the current stdout exactly matches that retained readback and that current script/stdout hashes match the post-run observations.

**Binding limitation:** the original run has no recorded start/end UTC, executable resolution, or before/after source hashes. Those fields remain null and no source-unchanged gate is claimed. Thus the record supports the retained successful execution/readback report and current-file consistency; it does not cryptographically establish that today's script bytes are exactly the historical executed bytes. No rerun was performed to manufacture stronger provenance. The proof review above is independent of the finite output.

The accepted checkpoint is the direct full-total decomposition, its feasible-gap restriction, and a conditional use of the future-moment demand. Neither `X_z>=-O(N³)` nor an actual supercubic negative family, a fixed-onset cap contradiction, or Q1 has been established.

Current reviewed SHA-256 values:

- `research/birth_linear_total_causal_sign.md`: `c0052d708ea744f149316da624d85f02ff2eb5ceca4f13785b3c43582418b1dc`
- `research/evidence/birth_linear_total_causal_sign_exact.py`: `e897bb67ef9da4f28449b4b81b2f81ded9cc542c68a8790608d3e9b1d26820bb`
- `research/evidence/birth_linear_total_causal_sign_exact.txt`: `1ffdb5dcf55ef124deb3fbbe96d483ca5a3278110ef4aae8440911264a541a13`
- `research/evidence/birth_linear_total_causal_sign_exact.run.json`: `e182c6ca2128e58c7f94810748a9bd0950dee971448b5d6278b37fbb9a33abf2`
