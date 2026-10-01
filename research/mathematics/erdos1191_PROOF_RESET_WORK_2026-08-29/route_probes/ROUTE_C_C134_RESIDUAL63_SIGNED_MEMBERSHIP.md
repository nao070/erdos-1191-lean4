# Route C C134: residual-63 exact signed membership

Status:

`EXACT_C134_SIGNED_RESIDUAL_MEMBERSHIP_POSITIVE_GRAM_ONLY_NO_GO_C058_OPEN`

C134 canonically records the finite exact result below.  It adds no claim to C103 or C111 themselves and does not construct the physical 32-mark phase/history ledger required by C058.

## 1. Frozen target and ambient owner space

Use the natural epoch-16 prefix state

```text
global ranks 15,16,...,31  <->  local coordinates 0,1,...,16.
```

For `0<=i<=15`, put `d_i=e_i-e_(i+1)`.  The 63 cross-half sources are

```text
Gamma_cross={(i,j): 0<=i<=7, 8<=j<=15, j>=i+2}.
```

For `gamma=(i,j)`, define

```text
alpha_ij=(j-i)^2/1024,
P_ij=-alpha_ij/2 * (d_i d_j^T+d_j d_i^T).
```

The target is

```text
R16=sum_(Gamma_cross) P_ij
   =M16-(1/4)(M8_left+M8_right).
```

Both constructions are recomputed independently.  They agree exactly.  The
source count is `63`, the alpha mass is `4767/1024`, and `R16` has zero row
sums, zero diagonal, and 160 ordered/80 unordered nonzero off-diagonal
entries.

The one-time coordinate owner partition is

```text
past/shared-boundary owner: {rank 15},
current epoch-16 owner:     {ranks 16,...,31}.
```

For a symmetric matrix `X` and an owner projection `P_g`, the exact symmetric
owner share is

```text
Own_g(X)=sym(P_g X)=(P_g X+X P_g)/2.
```

The two owner shares sum to `X`; this is the matrix form of C111's one-time
coordinate-row ownership identity.  Lifting `X` to the pair of owner shares
is injective because their sum recovers `X`.

## 2. Exact primitive membership

The ambient matrix space is `Sym_0(Q^17)`, the symmetric zero-row-sum
matrices, with the owner lift above.  The exact right inverse `S` of the gap
difference matrix `D` gives the rational compression

```text
X -> S^T X S.
```

Under this compression each `P_ij` has its own `(i,j)` off-diagonal gap entry.
Exact Gaussian elimination therefore gives

```text
63 primitive columns:        rank 63
primitive columns plus R16:  rank 63.
```

The unique coefficients are all `1`.  Thus the entire residual, rather than a
direct sum of two half-banks, is present.

## 3. Exact signed Gram certificate

Polarization gives, source by source,

```text
P_ij = (alpha_ij/4) * [
          (d_i-d_j)(d_i-d_j)^T
        - (d_i+d_j)(d_i+d_j)^T ].
```

Moreover

```text
alpha_ij/4=((j-i)/64)^2.
```

Consequently there are two explicit rational Gram banks

```text
X_plus  = sum ((j-i)/64)^2 (d_i-d_j)(d_i-d_j)^T,
X_minus = sum ((j-i)/64)^2 (d_i+d_j)(d_i+d_j)^T,
R16=X_plus-X_minus.
```

Each bank has 63 rational factor columns, common denominator 64, exact factor
rank 15, is positive semidefinite, and has zero row sums.  Both traces equal
`4767/1024`, so their signed difference has trace zero.

Equivalently, bake the minus sign into the second generator family.  Then the
126 signed Gram columns have exact span rank 78, the augmented rank with
`R16` is also 78, and every conic coefficient `alpha_ij/4` is nonnegative.
This is an exact conic-membership certificate in a **signed** generator cone.
It is not a claim that `R16` itself is PSD.

All 63 primitive generators and all 126 signed Gram generators were lifted to
the two one-time owner shares and checked exactly.

## 4. C103 boundary and scale-terminal embedding

To test only algebraic C103 compatibility, every generator is embedded into
the smallest nonzero finite horizon `m=0,n=1`, with `w_0=c_0(L)=1`.  For a
matrix `X`, choose the matrix-valued potential

```text
C(0,L)   =-X/3,     C(1,L)   = 2X/3,
C(0,L+1) = 0,       C(1,L+1) = X/3.
```

Then

```text
prefix increment at L        = X,
initial boundary band_0(L)    =-X/3,
final boundary band_1(L)      = X/3,
upper scale-terminal increment= X/3,
```

and both exact C103 equations are retained:

```text
delta(L)-delta(L+1)=band_1(L)-band_0(L),
X = final - initial + upper scale terminal.
```

Thus neither initial, final, nor scale-terminal rows were deleted or set to
zero.  Every slot was owner-partitioned, for the target, all 63 primitives,
and all 126 signed Gram generators.

This establishes existence of a finite algebraic C103 lift.  The chosen
potential is an explicit test embedding; it is not the actual completed-shell
phase potential and therefore does not prove a nonanticipating global ledger.

## 5. Mandatory ranks 15--18 and exact no-go gates

The target rows for global ranks 15--18 were retained.  Each has nine nonzero
entries.  Useful exact entries are

| target row | other rank | entry |
|---:|---:|---:|
| 15 | 23 | `-1/32` |
| 16 | 23 | `15/2048` |
| 16 | 24 | `1/1024` |
| 17 | 23 | `13/2048` |
| 18 | 23 | `11/2048` |

Exactly 32 of the 63 sources touch the formerly omitted local coordinate
block 0--3 (global ranks 15--18); eight touch the shared rank 15.  The past
owner piece is nonzero, with owner-lift entry `(rank15,rank23)=-1/64`.

Three strict smaller-model conclusions follow.

1. **Positive Gram roots only are impossible.**  For
   `q=e_0+e_8`, every positive Gram root `zz^T` has value
   `(q dot z)^2>=0`, whereas

   ```text
   q^T R16 q=-1/16.
   ```

   The opposite vector `e_0-e_8` gives `+1/16`, so `R16` is indefinite.
   The negative signed Gram bank is essential.

2. **Dropping the shared rank-15 boundary is impossible.**  Any matrix
   supported only on current ranks 16--31 has entry `(0,8)=0`, while the
   target has `R16[0,8]=-1/32`; its past owner share has `-1/64`.

3. **Using only the mapped C123 support ranks 19--31 is impossible.**  Such a
   matrix has local entry `(1,8)=0`, while the target has `15/2048`.

These are exact no-go statements only for the named strict subcones.  They do
not extend the old direct-sum failure to signed cross-source generators or to
a freshly reoptimized full 32-mark master.

## 6. Exact C134 claim boundary

The 63-source residual is **not** blocked by finite rational generator
expressibility, one-time coordinate-row ownership, or the generic finite C103
algebra.  It has a compact exact signed primitive certificate and an exact
rational difference-of-PSD-Gram certificate with all ranks 15--18 present.

The result does not supply a positive capacity matrix.  It also does not test
the actual 32-mark Haar cells, common physical phase, owner inequalities,
cross-width coupling, adjacent-epoch reuse, birth/cutoff/shared-endpoint/final
rows, or arbitrary horizons.  Those are precisely the remaining C058 gates.

The next admissible experiment is therefore a fresh full 32-mark owner LP/SDP
on one common physical phase, using all ranks 15--31 and all 63 signed source
rows, while optimizing a genuinely PSD capacity Gram matrix and carrying the
actual C103 boundary-terminal ledger.  `C058`, `Q1`, and `Q2` remain open.

## 7. Reproduction

```bash
cd /Users/USER/Documents/ChatGPT/mathematics/erdos1191_PROOF_RESET_WORK_2026-08-29/route_probes
PYTHONDONTWRITEBYTECODE=1 python3 -B ROUTE_C_C134_RESIDUAL63_SIGNED_MEMBERSHIP_certificate.py --write
PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest -v ROUTE_C_C134_RESIDUAL63_SIGNED_MEMBERSHIP_test.py
PYTHONDONTWRITEBYTECODE=1 python3 -B ROUTE_C_C134_RESIDUAL63_SIGNED_MEMBERSHIP_independent_oracle.py
```

Expected terminal lines include

```text
C134_RESIDUAL63_EXACT_OK sources=63 mass=4767/1024 primitive_rank=63 signed_gram_rank=78 positive_only_separator=-1/16 ranks15_18=retained C103_rows=retained C058_open
INDEPENDENT_C134_RESIDUAL63_OK sources=63 mass=4767/1024 primitive_rank=63 signed_gram_rank=78 positive_only_separator=-1/16 boundary_rank15=-1/64 ranks15_18=retained C103_initial_final_terminal=retained C058_open
```

The independent oracle imports neither the main certificate module nor any
other canonical Python code.  It parses the JSON and independently rebuilds
the exact matrix, rank, Gram, owner, C103, separator, and dependency-hash
checks.
