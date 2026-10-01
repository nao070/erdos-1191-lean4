# Critical-envelope birth-shell falsification report

**Date:** 2026-08-28 (Asia/Tokyo)  
**Scope:** exact finite falsification and pattern search.  No finite survival
statement below is an asymptotic theorem.

## Outcome

The four natural signed-budget shortcuts H1--H4 already fail on the smallest
four-mark Golomb-ruler diameter.  Critical-envelope level monotonicity H5 also
fails at the next diameter.  The only tested statement that survived is H6,
net birth-shell nonnegativity.  H6 points in the wrong direction for the needed
upper bound and therefore does not resolve Problem #1191.

Definitions of H1--H6 and the exact shell partition are in
`critical_shell_candidates_2026-08-28.md`.

## Smallest exact witnesses

### H1--H4

Take

\[
A=(0,1,4,6),\qquad j_0=1,\quad J=2,\quad C=\tfrac12.
\]

This is a Golomb ruler.  Both critical-envelope checks are certified by exact
rational enclosures of `log(2)`:

\[
N_1=2\le m_1^2\log m_1,
\qquad
N_2=7\le m_2^2\log m_2.
\]

The level energies and functional are

\[
(E_1,E_2)=\left(\frac1{32},\frac3{112}\right),
\qquad \mathcal F_{1,2}=\frac{13}{224}.
\]

The exact shell table is

| shell | net `S` | diagonal `D` | off-diagonal `O` |
|---:|---:|---:|---:|
| 1 | `13/392` | `13/392` | `0` |
| 2 | `39/1568` | `25/1568` | `1/112` |

Thus H1 fails because `O_{2,2}>0`; H2 and H4 fail because
`S_{2,2}>D_{2,2}`; and H3 fails because

\[
S_{1,2}-S_{1,1}=\frac3{1568}>0.
\]

There is no four-mark Golomb ruler of diameter below 6, and the complete
diameter-6 enumeration has denominator `C(5,2)=10` and exactly two rulers.
The displayed ruler is lexicographically first, so the witness is smallest in
the declared ordering.

### H5

Take

\[
A=(0,4,6,7),\qquad C=1.
\]

Both dyadic prefixes satisfy the critical envelope, while

\[
E_1=\frac1{50},\qquad E_2=\frac{87}{4096},
\qquad E_2-E_1=\frac{127}{102400}>0.
\]

Hence normalized level energy need not decrease.  Exhaustion at diameter 6
finds no H5 failure, making this the first failure in the declared ordering.

## Exhaustive ranges

### Four marks

- Diameters: `6..40`.
- Normalized candidates: `9,870`.
- Branch-and-bound nodes: `18,670`.
- Accepted Golomb rulers: `8,406`.
- `C=1` compatible at both dyadic prefixes: `2,324`.
- Failure counts among those compatible rulers:
  `H1=373, H2=373, H3=2324, H4=373, H5=1, H6=0`.
- `C=1/2` compatible: `136`; counts
  `H1=69, H2=69, H3=136, H4=69, H5=0, H6=0`.

### Eight marks

- Diameters: `34..42`.
- Normalized candidate denominator: `22,706,280`.
- Branch-and-bound nodes: `1,263,643`.
- Accepted Golomb rulers: `5,198`.
- `C=1` compatible at all three dyadic prefixes: `3,841`.
- Failure counts:
  `H1=3841, H2=3841, H3=3841, H4=3841, H5=3734, H6=0`.

The range begins at 34, the first diameter in this enumeration with an
eight-mark ruler.  The certificate does not claim completeness outside the
stated fixed-diameter ranges.

## Seeded targeted searches

The dense randomized constructor always preserves distinct positive
differences.  All compatibility decisions use rational lower/upper bounds for
`log(2)`, never a floating-point threshold.

- 16 marks: seed `1216`, 40 attempts, 40 unique rulers, all `C=2`
  compatible.  The first 3 were retained and fully audited; all 3 refute
  H1--H5 and none refutes H6.
- 32 marks: seed `1223`, 10 attempts, 10 unique rulers, all `C=2`
  compatible.  The first 3 were retained and fully audited; all 3 refute
  H1--H5 and none refutes H6.

The JSON records every construction parameter, a SHA-256 digest of each full
generated ruler list, and every retained witness.  Only retained rulers are
included in the randomized failure counts.

## Independent oracle and surviving pattern

The implementation computes `K_N` through the four-endpoint formula.  The
oracle constructs literal cyclic arc sets and direct crossing-load vectors.
The certificate performed `8,424` full shell-decomposition comparisons and
`27` direct level-energy comparisons, with zero mismatches.

H6 says

\[
S_{s,J}\ge0.
\]

It survived every compatible certified ruler above.  An additional exact scan
of all `346,104` normalized eight-point integer sets of diameter `7..24`, even
without the Golomb condition, also found no negative shell.  That extra scan
has no independent oracle and is kept outside the main certificate.

The initial follow-up question was the stronger fixed-modulus statement

> For a left prefix `A_r` of `A_{2r}` and every
> `N>diam(A_{2r})`, is
> `Var_N C(A_{2r}) >= Var_N C(A_r)`?

**Subsequent exact result: this statement is false, even for Sidon sets.**  At
`N=40`, the left prefix `(0,20)` has variance `1/4`, while the Sidon extension
`(0,20,21,39)` has variance `99/400`.  More generally,
`(0,ceil(N/2),ceil(N/2)+1,N-1)` is a Sidon counterfamily for every `N>=40`.
An analytic argument proves that 40 is the globally smallest counterexample
modulus over every doubled-prefix size \(A_r\subset A_{2r}\).  General
non-doubling extensions can fail already at \(N=11\).  See
`FIXED_MODULUS_PREFIX_MONOTONICITY_COUNTEREXAMPLE_2026-08-28.md` and its dated
certificate.  Thus the finite survival of H6 cannot be upgraded through
fixed-modulus monotonicity.  Any successful `o(log J)` argument must group
interactions more finely or use a different long-range invariant.

## Reproduction

From `core_workspace/endpoint_variance`:

```bash
python -m unittest -v critical_shell_test.py
python critical_shell_certificate_2026_08_28.py
/tmp/erdos1191-pytest.gu2FvF/venv/bin/ruff check \
  critical_shell_search.py critical_shell_test.py \
  critical_shell_certificate_2026_08_28.py
```

The self-authenticating certificate is
`critical_shell_certificate_2026-08-28.json`; its internal canonical payload
hash is
`b3382d17c93b0048aa581ce009876570f57da2bd4adeaed1a33d163f970b0c2a`.
