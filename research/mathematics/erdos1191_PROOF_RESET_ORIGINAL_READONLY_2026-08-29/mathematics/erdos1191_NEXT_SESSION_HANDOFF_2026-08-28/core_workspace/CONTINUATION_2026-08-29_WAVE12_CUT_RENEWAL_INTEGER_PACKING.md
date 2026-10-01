# Erdős #1191 continuation — Wave 12 cut-renewal integer packing

Date: 2026-08-29 (Asia/Tokyo)  
Canonical state: `core_workspace/`  
Global status: `UNRESOLVED_AT_HARD_LIMIT`

## 1. Read order and claim boundary

This file supersedes Wave 11 only as the statement of the next lemma.  It
preserves every earlier theorem, computation, counterexample, and scope
warning.  Read next:

1. `endpoint_variance/WAVE12_SIGNED_OFFDIAGONAL_SURVIVAL_ANALYSIS_2026-08-29.md`;
2. `endpoint_variance/WAVE12_CUT_RENEWAL_PROBE_2026-08-29.md`;
3. `research_sources/WAVE12_SIGNED_OFFDIAGONAL_LITERATURE_DELTA_2026-08-29.md`;
4. `proof_obligations.md`, especially P17 and P18.

Wave 12 proves a new exact renewal identity and two exact method boundaries.
It does not prove P15, P17, P18, Question 1, Question 2, or a prize claim.
Finite rulers and changing finite families are never promoted to one infinite
branch.

## 2. Preserved Wave 11 state

For one fixed infinite normalized Golomb ruler, let

```text
D_(p,q)=a_q-a_(p-1),
C_(i,j)=log(D_(i,j-1)D_(i+1,j)/(D_(i+1,j-1)D_(i,j)))>0,
Y_m=sum_(j=m)^(2m-1) sum_(i=1)^(j-2)
      ((j-i)/(2m))^2 C_(i,j).
```

Wave 11 proves the triangular interval floor
`K_m^len=2log m+O(1)` and the nonnegative identity

```text
T_m-K_m^len=Y_m+G_m^len+S_m.
```

Thus P17 is exactly `sum_(m in E_J)Y_m=o(log J)` on one fixed infinite
eventually-critical branch, where `E_J={4,8,...,2^J}`.

## 3. Wave 12 exact positive cut renewal

Define the positive future cut tail

```text
R_m=sum_(i=1)^(m-2) ((m-i)/(2m))^2 sum_(j=m)^infinity C_(i,j).
```

Define four nonnegative sectors:

```text
Z_m^ob=sum_(j=m)^(2m-1) sum_(i=1)^(m-2)
       ((j-i)^2-(m-i)^2)/(4m^2) C_(i,j),

Z_m^nb=sum_(j=m)^(2m-1) sum_(i=m-1)^(j-2)
       (j-i)^2/(4m^2) C_(i,j),

Z_m^of=sum_(j=2m)^infinity sum_(i=1)^(m-2)
       i(4m-3i)/(16m^2) C_(i,j),

Z_m^mf=sum_(j=2m)^infinity sum_(i=m-1)^(2m-2)
       (2m-i)^2/(16m^2) C_(i,j).
```

With `Z_m` their sum, coefficientwise comparison gives

```text
Y_m=R_m-R_(2m)+Z_m.
```

Consequently

```text
sum_(m in E_J)Y_m
  =R_4-R_(2^(J+1))+sum_(m in E_J)Z_m.
```

The four `Z` sectors fix the raw-tail overlap defect.  For each fixed pair,
the old-future weights are bounded by `i/(4m)` and sum geometrically; the
middle-future sector meets only boundedly many dyadic cuts; each birth sector
occurs once.  The remaining difficulty is the total mass of different pairs.

## 4. Exact next lemma: P18

> **Integer cut-renewal packing lemma.**  For every fixed `C>0` and every
> fixed infinite normalized integer Golomb ruler with
> `a_n<=C n^2 log(2n)` eventually, prove
> `sum_(m in E_J)Z_m=o_C(log J)`.

This is sufficient for P17 by the preceding telescope.  It is not claimed
equivalent: the terminal `R_(2^(J+1))` is positive and cannot be silently
discarded in the reverse direction.

The highest-value immediate work is to seek a bounded-overlap injection for
different pairs using integer unit spacing and crossing interval-sum
relations.  A product-tree formulation is useful only if it retains that
arithmetic and supplies a summably vanishing box profile on the same fixed
ray.

## 5. Closed shortcuts and mandatory adversaries

### 5.1 Full independent order data is insufficient

Let `K_J^inc` be the best weighted-log floor using simultaneously numerical
ranks, `D>=binom(ell+1,2)`, and the complete interval-containment order.
Wave 12 proves

```text
0<=K_J^inc-K_J^len<5|E_J|.
```

Do not spend the next wave on another optimization using only these three
inputs.  The theorem does not exclude crossing additive relations, integer
spacing between distinct interval sums, or survival-conditioned state.

### 5.2 Real relaxation is false

The real marks

```text
a_n=n^2+sqrt(2)n
```

have all positive differences distinct and quadratic growth, but

```text
Y_m -> (3/2)(log 2-1/2)>0.
```

This is not an integer counterexample to Erdős #1191.  It is a proof-design
gate: reject any proposed P18 proof that would remain valid over arbitrary
real Golomb rulers.

### 5.3 Other gates

- Work on one fixed `surv_C=infinity` branch; do not change the ruler with the
  terminal scale.
- Fixed-pair coefficient summability is already proved and is not the missing
  different-pair packing theorem.
- Preserve all four positive sectors and the terminal renewal tail.
- Finite tests may falsify a candidate but cannot prove infinite survival.
- The separate Route B must use a full product geometry; arbitrary pruning
  and unrestricted higher-product analogies have known obstructions.

## 6. Certified computation

From `core_workspace/endpoint_variance/` run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v \
  test_wave12_cut_renewal_probe.py
PYTHONDONTWRITEBYTECODE=1 python3 wave12_cut_renewal_probe.py \
  --source-certificate wave11_abel_repayment_certificate_2026-08-29.json \
  --output /tmp/wave12-cut-renewal.json
cmp wave12_cut_renewal_certificate_2026-08-29.json \
  /tmp/wave12-cut-renewal.json
```

The seven focused tests and deterministic certificate cover:

- independent rational-coefficient and exact formal-log renewal oracles;
- all 1,146 bounded eight-mark all-prefix-`C=1` rulers;
- the authenticated 64-mark fixture and an independent 128-mark ruler;
- 32,130 containment atoms through epoch 128;
- the exact per-epoch containment gain cap; and
- a labelled floating real-model calibration, never used for exact signs.

Certificate internal payload digest:
`fe0fd30cccaf2717d4c7dd2306772bc7dbcaea9bacf2b641d8e685d4999894a4`.

Certificate file SHA-256:
`e5645101d5150910de428b7184d504b1a9b90ac411c1b007be743e43e65aecc9`.

## 7. Literature boundary

The four requested connector families were used.  Consensus returned only a
quota failure and supplied no evidence.  Two adjacent current sources were
checked in primary text:

- Martikainen, `arXiv:2608.22628`, gives critical two-depth Journé packing and
  a Zygmund-boundary theorem.  It is a Route B geometric template, not a Sidon
  encoding or arithmetic box estimate.
- Chen--Fang, DOI `10.1016/j.jcta.2026.106239`, shadows a supplied Sidon
  counting function by a perfect difference set, but deletes input elements
  and inserts new ones.  It is not prescribed-prefix survival and does not
  improve the input density exponent.

No checked source proves P18.  This is a qualified targeted null, not a proof
of absence or novelty.

## 8. Stop condition for the next session

Continue until one of the following is achieved:

1. a complete proof of P18 with every multiplicity and tail audited;
2. a rigorous counterexample to P18 that still leaves P17 eligible, followed
   by a precise replacement target;
3. a complete Route B arithmetic embedding and summable box estimate; or
4. a new exact obstruction that strictly narrows the remaining mechanism.

Do not label the project resolved without a publication-grade proof or
disproof of Question 1 or Question 2 and an independent proof audit.
