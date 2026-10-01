# Paired orientations: repeated collision, multiplicity, and tail count

2026-09-09. Independent adversarial review of concrete identities and
counts proposed by the main researcher. Only previously certified M=25
and M=96 records were reused; no new campaign or Lean execution.

## Exact identity and what the collision forgets

At fixed later source birth c, older positive difference e, and lower
output i, suppose both strict-core orientations occur:

```
d_plus  = a_c-a_jplus > e,
t_plus  = d_plus-e = a_rplus-a_i,

d_minus = a_c-a_jminus < e,
t_minus = e-d_minus = a_rminus-a_i.
```

Eliminating a_c and e gives exactly

```
a_jminus + 2a_i = a_jplus + a_rplus + a_rminus,
a_jminus-a_jplus = t_plus+t_minus > 0.
```

Thus jplus<jminus<c<i<min(rplus,rminus). The collision has a repeated
point on the left. Both original records individually have six distinct
endpoints, so this repeated collision is a derived object, not one of the
original repeated-endpoint records already removed by Gate 0.

For a fixed oriented collision define

```
A = a_jplus+t_plus = a_jminus-t_minus,
e_c = a_c-A,
B_M = t_plus*u_rplus^[M]-t_minus*u_rminus^[M].
```

The paired compensation excess is D_c(M)=e_c*B_M. Therefore its sign
is the same for all realized c belonging to that oriented collision.
Positive rows do not cancel one another when grouped by this collision;
their total is B_M times the sum of their actual older labels e_c.

## Two useful injections, neither giving a constant bound

The clock ordering immediately allows at most i-jminus-1 values of c.
There is also an actual positive-difference injection into older endpoints.
Write e_c=a_q-a_p with p<q<c. Then

```
a_c-a_q = A-a_p > 0.
```

If two rows share p, positive-difference uniqueness forces the same
(q,c). Consequently c maps injectively into p. Also
a_p<A<a_jminus, and six-distinctness gives p!=jplus. Hence

```
# {realized c for this oriented collision}
 <= min(i-jminus-1, #{p : a_p<A and p!=jplus})
 <= min(i-jminus-1, jminus-2).
```

These are valid rank-dependent bounds. They do not furnish an absolute
constant. The finite examples below refute uniqueness and several small
proposed constants; they do not disprove every possible absolute bound.

## Actual multiple-c witnesses, including positive excess

The already certified greedy M=25 prefix has the fixed repeated collision

```
a16+2a22 = a1+a24+a23 = 1438.
```

Both c=17 and c=18 occur, with the same oriented outputs rplus=24,
rminus=23 and the same lower output i=22:

| c | Older e and its endpoints | d_plus | d_minus |
|---:|---|---:|---:|
| 17 | 107=a15-a11 | 289=a17-a1 | 38=a17-a16 |
| 18 | 178=a14-a3 | 360=a18-a1 | 109=a18-a16 |

The four records are all strict core with six distinct endpoints. At
M=25,T=24 their compensation excesses are positive:

```
D_c17 = 200502708371698175071/28627944104873943851933340000,
D_c18 = 166773280795150818517/14313972052436971925966670000
      = (178/107)*D_c17.
```

For a larger example entirely within the already certified M=96 greedy
history, the oriented collision

```
(jminus,jplus,i,rminus,rplus)=(44,24,72,73,77)
```

has nine distinct c values with positive exact excess:

```
c = 45,46,49,50,52,53,54,61,64,
e = 364,565,1346,1418,1810,1865,2318,4356,5297.
```

The corresponding collision of point values is

```
3591+2*11876 = 775+12034+14534 = 27343.
```

Grouping all already-certified paired records gave:

| Existing history | Paired rows | Unoriented repeated collisions | Largest number of distinct c | Largest number of distinct c with positive excess |
|---|---:|---:|---:|---:|
| Greedy M96 | 2,152 | 582 | 13 | 9 |
| Variant M96 | 2,154 | 567 | 12 | 9 |

An unoriented collision forgets which of its two output ranks is rplus.
The exact positive examples above retain that orientation. All signs in
the grouping were determined by Fraction arithmetic with genuine M96
prices. The underlying records, Sidon assumptions, all-rank fixed caps
and strict conditions were already independently certified.

`paired_orientation_repeated_collision_existing_M96.json` stores the
selected records, exact excesses, multiplicities and original source
hashes. Finite observed multiplicities do not show unbounded multiplicity.

## Exact count for positive common-tail increments

Consider paired rows with rplus>rminus and put R=rplus. Fix jminus<i<R.
The repeated-collision identity becomes

```
a_jplus+a_rminus = a_jminus+2a_i-a_R.
```

Repeated-sum Sidon gives at most one unordered actual point pair on the
left. The strict order jplus<i<rminus chooses its orientation uniquely.
For this pair and a chosen c, the value e_c=a_c-A is determined, and
positive-difference uniqueness determines its older endpoints if it is
an actual label. Thus the number of such rows with maximum output R is
at most

```
sum_(1<=jminus<i<R) (i-jminus-1) = binom(R-1,3).
```

This counts the remaining free c exactly as an intermediate clock:
each summand enumerates jminus<c<i. Further strict-core requirements and
the endpoint injection above can only reduce this upper count.

When component k is added, an old row with R<k has common price increase
kappa_k/H_k^2 at both output ranks. Its compensation excess increases by

```
(kappa_k/H_k^2)*e*(a_rplus-a_rminus) > 0.
```

For rplus<rminus this common-tail increment is negative, and for equal
outputs it is zero. A positive-part excess increases by no more than
the positive increment above. Define J_k to sum these positive common-tail
increments over the old rows R<k,rplus>rminus.

The exact hockey-stick count for those old rows is

```
sum_(R<k) binom(R-1,3) = binom(k-1,4) <= binom(k,4).
```

Both e and a_rplus-a_rminus are at most H_k. Consequently the main
researcher's stated majorant is valid:

```
0 <= J_k <= kappa_k*binom(k,4)
         = (k-2)(k-3)/[6(k-1)(k+1)^2] ~ 1/(6k).
```

The slightly sharper old-row count yields, for k>=5,

```
J_k <= kappa_k*binom(k-1,4)
     = (k-2)(k-3)(k-4)/[6k(k-1)(k+1)^2] ~ 1/(6k).
```

Both displayed majorants have divergent sums. This proves neither that
the actual J_k sum diverges nor that no better bound exists. It identifies
the precise remaining factor: charging each derived repeated collision
only once would incorrectly remove its genuine source-birth multiplicity.

This argument controls common-tail increments of old paired-row excesses.
Newly appearing rows at their output ranks and the full square-root
coverage profile require separate treatment. No cap was needed for the
count or these tail inequalities, and none of them establishes uniform N.

## Logical status and next action

The repeated-triple identity, two injections, fixed-R count and exact
tail majorants are hand-proved here. Multiple-c witnesses and their
positive exact excesses come from independently certified finite actual
histories. No arbitrary-rank constant multiplicity bound, summable
weighted tail, frozen core bound, or Q1 conclusion has been obtained.

Next nonduplicate action: estimate the weighted quantity
sum e*(a_rplus-a_rminus) over actual rows before replacing each summand
by H_k^2, retaining the unique older endpoints and the c-to-p injection.
The unweighted repeated-collision count alone leaves the harmonic loss.
