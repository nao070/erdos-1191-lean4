# Independent review of common-clock Schur energy

2026-09-05. Reviewer: `/root/moment_evidence_audit`, GPT-6 Astra Ultra.

Result: no mathematical defect identified in the common-price pairing, proxy-summable sibling closure, equations (1)–(15), or the stated constants. The entire target was read. The individual deletion proofs in `three_clock_separation.md`, `clock_core_localization.md`, `near_retirement_incidence.md`, and `late_retirement_tail.md` were checked as counts against the proxy, rather than inferred merely from small signed products. The repeated-endpoint counting argument in `birth_linear_total_causal_sign.md` was also read. No finite computation, checker, or Lean command was rerun.

## Common horizon and the proxy closure

For a canonical numeric triple `0<x<y`, `z=x+y`, with three distinct actual birth clocks, both `{x,z}` and `{y,z}` have different source births. Each record's existing Born or retirement price is `w_M`, where M is the largest of the three clocks. Each appears in the existing finite-horizon sums exactly when `M<=T`. Thus the sibling involution preserves the actual horizon and price, including cases where the largest numeric label z is not latest-born.

The common proxy `pi=1/q_M^2` bounds each absolute product because its two permanent raw coefficients are bounded by `H_M`. This proxy is shared by both siblings. The following imported omissions indeed have finite **proxy** sums:

| Omitted predicate | Counting proof that survives replacement by pi |
|---|---|
| Any close pair of distinct clocks | At the larger chosen rank n, count at most four completions per chosen label pair and use `pi<=1/q_n^2`; this gives `16*sum 1/[n*(log n)^gamma]`. |
| Equal clocks on distinct labels | Count at most four records per same-class label pair, with `pi<=1/q_n^2`; the resulting square-rank series converges. |
| Repeated numeric label | There are `p-1` possible smaller labels x at rank p, each yielding at most one `{x,2x}` record; `pi<=1/q_p^2` gives the original convergent series. |
| Old-source or old-output cutoff | At source birth b the counts are at most `(b-1)q_(k_b)` or twice that number; `M>=b` gives `pi<=1/q_b^2`. |
| Small numeric output | Count at most `2(b-1)floor[b^2/(log b)^beta]` original source pairs at b, each with one output; again `pi<=1/q_b^2`. |
| Two-sided close source/output window | The actual star-intersection bound is at most `3q_(b-1)` records per pair of ranks; multiplying by the number of allowed ranks and `1/q_b^2` gives the same constants 12 and 6. |
| Far retirement | Here `M=r`, so pi is exactly `1/q_r^2<=16/r^4`; there are at most `b^3/2` original pairs per source birth b and no extra sum over their realization ranks. |
| Born non-six-endpoint records | In a source dyad N, all endpoints are in `P_(2N)`; the complete count is at most `13(2N)^3` and `pi<=1/q_N^2`. |
| Near-retirement repeated endpoints | In the source dyad, all endpoints are below the stated polylogarithmic lookahead `L_N`; the bound `12L_N^3/q_N^2` is dyadically summable. The far-retirement deletion is applied first. |

In particular the automatic Born records are bounded by their actual point-triple count, at most `binom(M,3)` in an M-point prefix. Their signed centered formula alone would not justify a proxy estimate, and is not what these proofs use. Nontrivial repeated triple collisions are bounded by at most `M^2` repeated triples, at most M partners each, six slot matchings, and two records per matching. This is an actual count before applying any coefficient estimate. No small coefficient or cancellation is needed for any row of the table.

Within the symmetrically separated set, let D be the records failing an older asymmetric core predicate. The cited finite proxy bounds give `sum_D pi<=C_*`. If a record fails to survive the paired intersection, either it lies in D or its sibling does. Since the sibling involution is a bijection preserving pi, the union has proxy sum at most `2C_*`. The extra deletion of surviving siblings costs at most one additional `C_*`. This proves (2), and it would not follow just from a bound on the discarded signed products. Symmetric separation also preserves both siblings. Every predicate is imposed on each sibling separately in the final paired core.

## Latest-clock cases, square, and mean defect

When z is latest, both records are Born. When x is latest, `{x,z}` is Born and `{y,z}` retires; the roles reverse when y is latest. This verifies the whole table and `B(S)+R(S)=w_M*g_z*(g_x+g_y)` with two products, each counted once and no extra factor two.

For the actual raw feature, `g_d=d-h_(tau(d))`, where `h_j=a_j-m_j`. Numeric additivity gives `g_x+g_y=g_z+Delta` with `Delta=h_(p_z)-h_(p_x)-h_(p_y)`. Completing the square proves (5), including its subtraction `Delta^2/4` and its alternative center `z-(h_(p_x)+h_(p_y)+h_(p_z))/2`.

The actual endpoint equation for x+y=z implies `a_(p_z)-a_(p_x)-a_(p_y)=a_(ell_z)-a_(ell_x)-a_(ell_y)`. Substituting this into the definition of Delta gives (6) with the displayed signs. The upper endpoints cancel, while the prefix means and lower endpoints remain. Reindexing this correction by its three birth classes yields (7). The weights restrict and repeat coefficients through actual incidences, so class centering does not cancel the resulting `L_j`.

If a summand L is latest, let O be the other summand. Since `g_z=g_L+g_O-Delta`, multiplying by `g_L-g_O` gives exactly (8). Separating the latest-z cases then proves the signs of `P_T` and `E_T^def` in (9). The label reindexing (10) uses the head birth for every edge weight, and edges strictly increase birth rank. It is an exact weighted incidence expression, with no proved nonnegative divergence or monotonicity of squared coefficients. It is not an uncharged telescoping boundary.

## Triple count and all remaining constants

At latest rank M a retained triple has one new label and two distinct old labels. Marking one old label gives `(M-1)q_(M-1)` possible new/marked-old pairs and at most two numeric completions for each. Each actual triple is encountered twice because either old label can be marked. Dividing these two factors proves `N_M<=(M-1)q_(M-1)` in (11). There is no uncounted independent choice of third birth rank.

All three `h_j` lie in `[0,H_M]`. Their one-plus/two-minus combination Delta lies in `[-2H_M,H_M]`; hence `|Delta|<=2H_M`, rather than needing a bound of three H. Thus `w_M*Delta^2/4<=1/q_M^2`. The exact rational factor is

```
(M-1)q_(M-1)/q_M^2=2(M-2)/M^2.
```

For integer horizons `T>=3`, its sum is at most `2*sum_(M=3..T)1/M<=2*log T`; smaller empty sums are handled directly. This proves (12). For the latest-z correction the product costs at most `2/q_M^2`; for a latest summand it costs at most `4/q_M^2`, because `|g_L-g_O|<=2H_M`. The uniform factor four and the same count therefore prove `|E_T^def|<=8*log T` in (13).

Summing the exact square identity proves (14). The proxy-controlled deletions give a bounded absolute error from the original B and R, so substituting their sum into the existing positive-bank causal Abel identity proves (15), with the original diagonal retained. This application concerns the original positive-bank coefficients; it makes no assertion about a signed-bank causal Abel identity.

The defect estimate is logarithmic, not uniformly finite, and is not controlled by the much weaker available productive divergence. The note makes this limitation explicit. Neither paired closure, the mean cancellation, nor increasing birth ranks proves the needed sign or subcritical bound for the defect and potential. The shared physical margin and original Q1 remain unresolved. No source correction was requested.

Reviewed source SHA-256: `df24fc76cdbf7d6864b11db153adcd104c583a5d8d2032d93a6978acfc2653d0`.

Principal imported source hashes: `three_clock_separation.md` = `7d8fb8dc6f08cf5324160f2acbf4edc75a95d50f6bdc89f4cb227a2b6b032b85`; `clock_core_localization.md` = `38fe3a9b361f60bd3312c07bf87781b04690c2078de69617e58e505e86b768a8`; `near_retirement_incidence.md` = `b832e9b8f5abbb374ed10f08170ded8b7db825830c6a7ecb1ad8451b0a31d155`; `late_retirement_tail.md` = `5dbcf37e0a7fd687a8371c5f71c04b11cab45992a622ebe31ebba15d469963ab`.
