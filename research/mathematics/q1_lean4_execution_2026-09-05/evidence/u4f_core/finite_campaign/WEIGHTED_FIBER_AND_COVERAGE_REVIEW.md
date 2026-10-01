# Weighted c-to-p bound and the size of the paired subclass

2026-09-09. A concrete continuation of WORKING_PROOF A07. All numerical
checks reuse the two independently certified M=96 actual histories with
fixed C=1,m0=2. No new history, evaluator, broad audit or Lean run.

## A weighted injection with an exact deficit

Fix one oriented repeated collision, and let its m realized c values
have older labels e_c=a_c-A=a_q-a_p, where

```
A=a_jplus+t_plus=a_jminus-t_minus,
p<q<c<i.
```

Positive-difference uniqueness makes c-to-p injective, because
a_c-a_q=A-a_p. The map c-to-q is also injective: if q is the same,
then a_c+a_p=A+a_q is one fixed two-sum; repeated-sum Sidon and the
order p<c determine both c and p.

Consequently the requested weighted inequality has an exact form:

```
sum_c e_c
 = sum_(p in actual image) (a_(i-1)-a_p)
   - sum_(q in actual image) (a_(i-1)-a_q).
```

The second sum is a positive actual deficit, rather than a new budget.
Since the q's are distinct and all q<=i-2, Sidon interval packing yields

```
sum_(q in image) (a_(i-1)-a_q)
 >= sum_(l=1..m) l(l+1)/2
  = binom(m+2,3).
```

Indeed the l-th smallest distance back from rank i-1 is at least the
width needed for l+1 Sidon points. Hence the valid stronger bound is

```
sum_c e_c
 <= sum_(p in actual image) (a_(i-1)-a_p) - binom(m+2,3).
```

One may also discard the detailed p image, still using its injectivity:
sum_p(a_p-a_1)>=binom(m+1,3). With H=H_(i-1), this gives

```
sum_c e_c <= mH-binom(m+1,3)-binom(m+2,3)
          = mH-m(m+1)(2m+1)/6.
```

The identity and both inequalities hold for arbitrary actual fibers,
without imposing a cap. They keep a genuine weight deficit, but do not
by themselves give H*sqrt(jminus). Their finite instantiations were
checked exactly on every oriented fiber in the two existing histories.

## Bounded test of the constant-one square-root candidate

The precise tested claim was

```
sum_c e_c <= H_(i-1)*sqrt(jminus).
```

All terms are nonnegative, so it was tested by the exact integer
comparison (sum e_c)^2<=H_(i-1)^2*jminus.

| Existing history | Oriented fibers checked | Failures | Largest ratio to the proposed right side, approximate |
|---|---:|---:|---:|
| Greedy M96 | 905 | 0 | 0.4806723138 |
| Variant M96 | 858 | 0 | 0.4721155955 |

For the greedy maximum, (jplus,jminus,i,rplus,rminus)=(21,39,62,63,66),
m=6, sum e=23378, H_(i-1)=7788. Its exact squared ratio is
136632721/591366204. The p-image upper sum is 45657; the exact q-image
deficit is 22279, much larger than the generic cubic lower bound 56.

For the variant maximum, the oriented key is (32,45,75,77,79),
m=9, sum e=40174, H_(i-1)=12685. Its exact squared ratio is
1613950276/7240915125. The p-image upper sum is 109746 and its
exact deficit is 69572, compared with the generic lower bound 165.

This bounded absence is not a proof for arbitrary capped histories.
The separately reviewed actual family in
`CAP_FREE_SQRT_FIBER_COUNTERFAMILY.md` disproves every absolute-constant
version without a common fixed cap. Its cap constants grow; it does not
settle the C=1,m0=2 version tested here or a constant allowed to depend
on the fixed cap.

## How much of the actual core is paired

A paired row here means that both the plus and minus records at fixed
(c,e,i) belong to the current strict-core record set. Each of its two
records is included once. Opposite companions outside the strict core
are not counted, and no assertion about their absence is made.

Let P_pair be the exact profile of this subset. Its record mass is the
one-copy sum of u_r^[96]de over those records. Its harmonic coverage is
I_pair=sum_b P_pair,b/b, retaining each record's actual cut interval.
The total mass and I use the complete strict core.

| Existing history | Paired records / core records | Paired record-mass fraction | Paired harmonic-I fraction | Relative change in N if paired records are removed |
|---|---:|---:|---:|---:|
| Greedy M96 | 4,304 / 194,966 | 3.584674% | 3.434243% | 1.655082% |
| Variant M96 | 4,308 / 200,243 | 4.130506% | 3.939832% | 1.912436% |

Mass and I fractions are stored as exact rational numbers; these displayed
percentages are approximate. The last column is

```
[N(P)-N(P-P_pair)]/N(P),
```

computed from exact rational profiles with 55-digit Decimal square roots.
It is an approximation, not a certified square-root enclosure. No false
identity N(P)=N(P_pair)+N(P-P_pair) is used.

Thus in these two observed histories the paired-core argument addresses
a small part of the profile. This is finite evidence about scope, not an
asymptotic theorem that pairing must always cover a small fraction. A
proof about paired fibers alone leaves unpaired core records to control.

## Evidence and next nonduplicate action

`weighted_fiber_and_paired_fraction_existing_M96.json` stores exact
profile coefficients for the paired subset, exact mass/I fractions,
top candidate fibers, all deficit checks, the source hashes, and both
the current WORKING_PROOF hash and the A07 section hash.

The new all-history content is the exact weighted injection and cubic
deficit. The square-root bound remains unproved with a common fixed cap;
finite calculations do not strengthen that status. The full core bound
and Q1 remain unresolved.

Next action: carry the useful endpoint-weight deficit into an estimate
for all actual output correlations, or supply a separate bound for the
unpaired core before treating a pairing estimate as a closing argument.
