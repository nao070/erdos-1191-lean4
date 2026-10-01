# Independent mathematical review of the output-correlation bound

2026-09-09. This reviews the main researcher's proposed inequality,
separately from finite profile certification. No Lean verification.

## Verdict and precise range

The following chain is valid for n=b-1>=3; its cap conclusion needs
n>=m0. Initial cuts outside that range remain covered by the established
uniform bound P_b<=1/8. C and m0 remain fixed.

Write x_j=a_j-a_1 (1<=j<=n), H=x_n, D=F_n, and S=sum_(d in D)d^2.
Positive difference injectivity makes this S equal to the sum over point
pairs. For each fixed positive output t, the graph on D with edges
{e,e+t} has degree at most two. Applying
e(e+t)<=([e^2+(e+t)^2]/2) and then the degree bound yields K_D(t)<=S.
For output rank r, the lower endpoints after b number r-b-1. Therefore

```
P_b^core(M,M)
 <= S sum_(r=b+2..M) (r-b-1) u_r^[M]
 <= (S/H^2) sum_(r=b+2..infinity) (r-b-1) alpha_r
 <= (S/(3H^2)) sum_(t=b+1..infinity) t^-3
 <= S/(6b^2H^2).
```

The genuine finite price is used in the first line. The second line
uses only u_r^[M]<=alpha_r/H^2. The third uses
alpha_r<=[(r-1)^-3-r^-3]/3 with linear-weight summation by parts;
the lower index t=b+1 is correct. The last compares the decreasing
positive series to its integral from b to infinity.

Exact pairwise variance gives

```
S = n sum_j x_j^2 - (sum_j x_j)^2
  = n^2H^2/4 - n sum_j x_j(H-x_j) - (sum_j x_j-nH/2)^2.
```

Packing positive differences among the first j points and last n-j+1
points implies

```
x_j >= j(j-1)/2,
H-x_j >= (n-j)(n-j+1)/2.
```

The exact sum of the smaller of these rank lower bounds equals
n(n^2-4)/24 for even n and n(n^2-1)/24 for odd n. Thus uniformly

```
sum_j min(x_j,H-x_j) >= n(n^2-4)/24.
```

Since max(x_j,H-x_j)>=H/2, it follows that

```
sum_j x_j(H-x_j) >= H n(n^2-4)/48,
S/H^2 <= n^2/4 [1-(n^2-4)/(12H)].
```

Combining, and then using H<=Cn^2 log(2n) with the correct inequality
direction, gives

```
P_b^core(M,M)
 <= n^2/(24b^2) [1-(n^2-4)/(12H)]
 <= n^2/(24b^2) [1-(1-4/n^2)/(12C log(2n))].
```

No independence of output records, cap-onset change, or artificial
terminal price occurs in this proof. The moment identity and packing
indeed use the actual Sidon geometry. The odd-n improvement above is
available if desired but does not change the obstruction below.

## Where this attempt fails to close the core bound

The displayed final bound tends to 1/24 as b grows. Summing its square
root divided by b diverges. It consequently yields a valid improvement
over the coarse constant 1/8 and a cap-sensitive correction, but no
summable I_j or uniformly bounded N follows from this estimate alone.

The losses are concrete: (1) each output correlation graph is replaced
by its degree-two envelope S, discarding the actual simultaneous set of
future outputs; (2) all future prices are independently enlarged to
alpha_r/H^2; (3) the negative variance-square term is dropped; and
(4) one-dimensional packing is reduced to its smallest possible endpoint
distances. The first two losses do not retain a mechanism to charge
different outputs or scales to a single scarce resource.

Next nonduplicate action: bound the weighted aggregate of actual output
correlations before applying K_D(t)<=S, retaining the shared label bank
and the exact changes in H_r across output ranks.

## Finite corroboration, with its separate scope

`output_correlation_bound_finite_review.json` checks every cut
4<=b<=95 on the two already-generated M=96 histories. It certifies by
rational arithmetic the full chain

```
P <= S * actual future-price sum <= S/(6b^2H^2)
  <= packing bound <= rational upper enclosure of the C=1 cap bound.
```

The largest approximate P/(S * actual future-price sum) is 0.1031183
(greedy, b=13) and 0.1119679 (variant, b=14). The largest P/cap-bound
ratio is 0.00112705 (greedy, b=23) and 0.00119204 (variant, b=14).
These ratios describe finite slack and are not universal constants.
All original mathematical source hashes are saved in each input profile.
