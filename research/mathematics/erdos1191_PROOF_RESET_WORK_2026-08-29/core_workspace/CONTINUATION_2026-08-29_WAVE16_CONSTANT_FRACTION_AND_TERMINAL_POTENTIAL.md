# Erdős Problem #1191 — Wave 16 constant-fraction promotion continuation

Date: 2026-08-29 (Asia/Tokyo)  
Canonical root: `core_workspace/`  
Claim status: **Questions 1 and 2 remain open; no prize claim is ready**

## 1. What Wave 16 changes

Wave 16 strengthens the future-rank route in two independent ways.

First, the spatial-bin witnesses from many disjoint future blocks can be
added.  For every macroscopic old difference, the future rank increase is a
fixed positive fraction of the difference, rather than only
`Omega_C(d/log d)`.

Second, the apparent `Theta(J)` terminal suffix obstruction in the Wave 15
unweighted shift was an artifact of isolating `mathfrak U_(2^J)`.  The exact
renewal tail, full-span term, and singleton absorb that suffix fan into a
nonnegative terminal potential.  The true terminal upper is
`O_C(log J)`.  A Fejer taper can make the raw horizon mismatch negligible
while preserving the harmonic lower signal.

The remaining obstruction is now narrower: promotion capacity inside the
next Gothic bulk is already used by the existing rank/length floor.  No
disjoint premium of the required strength has yet been proved.

## 2. Constant-fraction future-rank filling

Let an infinite normalized integer Golomb ruler satisfy

```text
a_n <= C n^2 log(2n)
```

eventually.  Let `d` be an old difference in a prefix of `L` marks with
`d>=L^2/8`.  For

```text
M_t=2^t L,  0<=t<=floor((log_2 L)/2),
```

put the marks with indices `[M_t,2M_t-1]` into half-open bins of width `d`.
Once

```text
sqrt(L) >= 128 C log(4 L^(3/2)),
```

the number of same-bin pairs in every block is strictly larger than

```text
d/(64 C log L).
```

The mark blocks are disjoint, and global Golomb uniqueness makes all pair
differences distinct across blocks and distinct from the old prefix.  Since
there are more than `(log L)/(2log 2)` blocks,

```text
rho_infinity(d)-rho_L(d) > d/(128 C log 2).
```

For the Wave 13 suffix

```text
d_(m,p)=D_(p,2m-1),  2<=p<=m,
```

use `L=2m`; the contained subinterval differences give
`d_(m,p)>=L^2/8`.  Therefore, with

```text
kappa_C=log(1+1/(128 C log 2)),
```

one has eventually and uniformly

```text
log(rho_infinity(d_(m,p))/rho_(2m)(d_(m,p))) >= kappa_C.
```

This improves the Wave 14 `Omega_C(1/log m)` promotion to a positive
constant per suffix atom.  In particular,

```text
full macroscopic u-promotion >= kappa_C/2,
legal next-shell Phi_m       >= kappa_C/6,
residual (u-v) resource      >= kappa_C/3
```

for all sufficiently large dyadic `m`.  Also

```text
log(d_(m,p)/rho_infinity(d_(m,p))) < log(128 C log 2),
```

unless the hypotheses already contradict `rho_infinity(d)<=d`.  Thus the
eventual-hole channel is uniformly `O_C(1)`.

## 3. Exact terminal renewal potential

At epoch `m`, let

```text
A=D_(1,2m-1),
c_m=(2m-1)^2/(16m^2),
v_(m,p)=(4m-2p+1)/(16m^2).
```

Exact summation by parts gives

```text
R_(2m)
 = c_m log A
   - sum_(p=2)^(2m-2) v_(m,p) log d_(m,p)
   - mathfrak e_m.
```

The coefficient checksums satisfy

```text
U_m+V_m=F_m+c_m=(m-1)^2/m^2.
```

Hence

```text
mathcal T_m
 = mathfrak F_m+mathfrak e_m+R_(2m)-mathfrak U_m
 = ((m-1)^2/m^2) log A
   -sum_p (u_(m,p)+v_(m,p))log d_(m,p)
 >=0,
```

because every suffix difference is at most `A` and the positive and negative
coefficient masses agree.  Substituting into the Wave 13 spectrum yields

```text
Z_m-R_(2m)=mathfrak P_m-mathfrak B_m-mathcal T_m.
```

The prefix and descendant coefficient masses agree row by row.  The
triangular interior floor and the eventual cap then give

```text
0 <= mathfrak P_m-mathfrak B_m
   <= (3/4)log log(4m)+O_C(1),
Z_m-R_(2m) <= (3/4)log log(4m)+O_C(1).
```

At `m=2^J`, the genuine terminal upper is therefore `O_C(log J)`, not the
raw `Theta(J)` estimate for `mathfrak U_m` alone.  This is still not the
required `o(log J)`.

## 4. Fejer horizon taper

For `m_k=2^k`, set

```text
omega_(k,J)=((J+1-k)/(J+1))^2.
```

Then

```text
sum_(k<=J) omega_(k,J)/k = log J+O(1),
omega_(J,J) mathfrak U_(2^J)=O_C(1/J).
```

The weighted renewal identity has nonpositive coefficients on every
intermediate and terminal `R` term.  Moreover `Delta_m<log 13`, so shifting
the Wave 15 adjacent allocation by one epoch costs only a telescoping `O(1)`
weight mismatch plus its summable small-value error.  The taper therefore
preserves the `Theta(log J)` new-birth lower signal while removing the raw
horizon mismatch.

This is a valid alternate contradiction route, not a proof of the unweighted
P17 statement.

## 5. Exact remaining theorem

The next Gothic bulk supports both the Wave 15 promotion allocation and the
old interior rank/length floor.  The current proof does not show that both
uses are disjoint.  A sufficient new statement would be a weighted or
unweighted inequality of the form

```text
mathfrak B_(2m)
 >= chosen_existing_floor + c Delta_m - epsilon_m,
```

with a quantitatively sufficient `c>0` and a cumulative error negligible
relative to `log J`.  Equivalently, one may allocate the constant-size
residual `u-v` promotion across birth epochs with bounded total reuse while
preserving the taper or the exact terminal potential.

The Wave 16 theorems remove the former standalone `Theta(J)` terminal
obstruction.  They do not remove coefficient-capacity overlap, do not prove
`P19`, `P20`, or `P21`, do not construct an eventually critical branch, and
do not resolve either Erdős question.

## 6. Primary artifacts

- `endpoint_variance/WAVE16_MULTISCALE_FUTURE_RANK_FILLING_2026-08-29.md`
- `endpoint_variance/WAVE16_TERMINAL_POTENTIAL_2026-08-29.md`
- `endpoint_variance/wave16_multiscale_future_rank.py`
- `endpoint_variance/wave16_multiscale_future_rank_certificate_2026-08-29.json`
- `endpoint_variance/test_wave16_multiscale_future_rank.py`
- `endpoint_variance/wave16_terminal_potential_certificate.py`
- `endpoint_variance/wave16_terminal_potential_certificate_2026-08-29.json`
- `endpoint_variance/test_wave16_terminal_potential_certificate.py`
- `research_sources/WAVE16_PERFECT_DIFFERENCE_COMPLETION_BOUNDARY_2026-08-29.md`

All finite certificates remain algebra or mechanism checks.  Their scope
flags do not infer a critical infinite branch, a signed global allocation,
Question 1, Question 2, or a prize claim.
