# 2026-08-28 endpoint-variance continuation

The new exact result is in `endpoint_variance/ENDPOINT_IMBALANCE_THEOREM.md`.
It proves that offset-energy variance is the cyclic H^{-1} energy of the short-pair endpoint imbalance, characterizes all zero modes as Eulerian residue graphs, and certifies a homometric Sidon-ruler separation of 6/7.

Verification: `cd endpoint_variance && python -m unittest -v test_endpoint_variance.py && python certificate.py`.

Additional exact result: in the complete-prefix diameter regime, the endpoint imbalance has squared norm `m(m^2-1)/3`, giving `Var(E_N) >= m(m^2-1)/(12N)`.

Sharp strengthening: for `diam(A)<N`, mandatory split levels force `Var(E_N) >= m(m^2-1)(m^2+11)/(180N)`, sharp for consecutive points at `N=m`.

## Anti-Eulerian continuation in this package

The endpoint theorem was independently audited.  The half-open convention,
forward-difference sign, `1/N^2` Fourier normalization, componentwise cycle
decomposition, diameter algebra, mandatory-level formula, and homometric
values all passed.  The unrestricted equality family is non-Sidon for
`m>=3`; Sidon sharpness is still open.

`endpoint_variance/MULTISCALE_ARC_KERNEL_AND_OBSTRUCTIONS_2026-08-28.md`
now gives the exact cyclic-arc covariance and resistance formulas and the
ordered pair--pair expansion with prefix-birth and short-pair indicators.  For
`m_j=2^j`, `N_j=D_{m_j}+1`, and weights `m_j^-3`, a critical envelope forces

```text
F_J >= (1+o(1)) log(J)/(360 C log(2)).
```

The required signed off-diagonal upper budget `F_J=o(log J)` is not proved.
Exact modular cycles, sign reversal under modulus doubling, a dominant-gap
family, and a sparse infinite Sidon construction rule out the simplest
positivity, monotonicity, and unconditional-budget variants.

Target D was also completed as certified finite computation.  The exact
enumerator covers `2<=m<=7`, `m-1<=D<=25`, and `N=D+1,D+2,D+3`; it inspected
245,505 candidates and agrees with an independent direct-block oracle in all
294 checks.  These finite minima do not imply an asymptotic theorem.

**Global status remains:** `UNRESOLVED_AT_HARD_LIMIT`.
