# Independent endpoint-batch entropy review

Result: **accepted after the label-1 wording correction**. Reviewer: `/root/moment_evidence_audit`. Date: 2026-09-05T07:25:27.210982+00:00. This is an independent mathematical source review; no Lean verification is claimed. The original note was not edited by this reviewer.

1. **Finite union bound (1).** A fixed k-point integer Sidon set has exactly k(k-1)/2 distinct positive differences, all at most D-1 when its points lie in [1,D]. Independent bank membership with marginals at most b makes their simultaneous inclusion probability at most b raised to that number. There are at most binom(D,k) candidate point sets, and binom(D,k)<=D^k. Neither independence between candidate witnesses nor independence of actual Sidon differences is used. For k>D the event is empty.

2. **Threshold and Borel–Cantelli (2).** For k=ceil(4 log D/lambda)+2, lambda(k-1)/2>=2 log D+lambda/2. Hence the exponent is at most -k log D, and at most -4(log D)^2/lambda. The larger-witness event reduces to a k-point subset. The probability bound is eventually at most D^-2 and is summable over integer widths. The first Borel–Cantelli lemma requires no independence between widths. It produces one probability-one event on which all sufficiently large widths exclude every such large witness.

3. **Actual endpoint batches (3)–(4).** For i<j<n, the two new labels a_n-a_i and a_n-a_j differ by a_j-a_i, an old positive difference at most D-1. This proves Delta G_n(D) subset F_(n-1)(D). Reflection x -> a_n-x preserves unordered sum uniqueness, so G_n(D) is Sidon. Distinct births use disjoint difference labels by the original sequence's Sidon property. Thus the actual batches partition F_p(D), each has fewer than k_D labels if the ambient bank excludes k_D-point witnesses, and their total is less than p*k_D. The definition starts with an empty first batch.

4. **Cap implication and quantifiers.** The first two sections of fixed_width_bank_density.md correctly supply M_floor(D^theta)(D)>=cD for each fixed theta in (1/2,1) under a single fixed-onset cap. The selected dyadic rank blocks use disjoint physical differences; their Cauchy estimates sum to a positive harmonic-log coefficient, while p/D tends to zero. Since D^theta*k_D/D tends to zero, (4) contradicts that conditional density. The probability-one clique event was established before considering any realization. On that event the deterministic argument excludes every endpoint realization with any fixed cap constants/onset; their size thresholds may depend on those constants. There is no illicit union over uncountably many preselected sequences.

5. **Coherent model and (5).** The original defective CDF gives Pr(beta_d finite)=1/10 independently for d>=2, while tau(1)=infinity deterministically. The parent's corrected text now states precisely independent membership with all marginals at most 1/10. Earlier banks are subsets of this one eventual bank. The terminal-height version repeats the finite union bound with D=H (F restricted to [1,H]); for H<=C*n^2*log(2n), log H=O_C(log n)=o(n), so n log H+lambda*n/2<=lambda*n^2/4 eventually. This proves the stated exp(-lambda*n^2/4) estimate.

The saved primary-paper text also supports the limited comparison: Theorem 2.1 counts finite Sidon sets, and Lemma 3.2 bounds finite extensions through independent sets in the graph whose edges satisfy a1+b1=a2+b2. Its PDF hash matches the quoted value. None of these cited results is needed for (1)–(5).

**Scope accepted:** almost-sure exclusion of endpoint realizations inside this independent eventual label bank. The argument gives no deterministic nonexistence theorem for actual capped Sidon histories, no transfer to their correlated banks, and no Q1 resolution. It does not depend on the coherent model's separate total-label-count defect.

Reviewed source SHA-256 values:

- `research/endpoint_batch_entropy_obstruction.md`: `0043ac67950f861802e950cef7866f917f6f68228d134d8b519bebb4b14ca47f`
- `research/coherent_birth_field.md`: `d1a82d52d0be897e009af7200d377b703bfa4968982769afbf83e782309cba18`
- `research/fixed_width_bank_density.md`: `95347fdf75202cc8fda4946fbbcd2205927822892a496ba2be5eb601ae819de5`
