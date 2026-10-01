# Route C C135: frozen D1 O0N1 complete-phase dual no-go

Status:

`EXACT_FROZEN_D1_O0N1_COMPLETE_PHASE_DUAL_SEPARATOR_C058_OPEN`

## 1. Exact claim

For only the frozen D1 O0N1 16-mark Golomb row

```text
(0,22,60,83,154,284,494,513,558,649,715,818,927,1038,1107,1169),
```

the common phase `[82,164]`, `rho=9/16`, coefficients

```text
(epsilon,A,B,C_rt,e2)=(1/1000,1/1000,1/2,1/10,0),
```

and the current 52-coordinate independent epoch-4/epoch-8 zero-row-sum
PSD aggregate cone, an exact 314-piece complete-phase separating dual
satisfies

```text
U^+ < T^-.
```

This is a narrowly scoped finite no-go. It is not a statement about a larger
cone, another rotation, another coefficient vector, or another phase rule.

## 2. Frozen fixture and target

The gap data are

```text
prefix:       (22,38,23)
old O0:       (71,130,210,19)
new canonical:(62,45,91,66,103,109,111,69)
new N1:       (45,91,66,103,109,111,69,62).
```

All 120 positive differences of the resulting 16 marks are distinct. Exact
reconstruction gives

```text
H2=430, H3=656,
Delta V=-443620417/1928247678,
Vrt_old=496/2365,
Vrt_new=118/451,
Delta Vrt=5034/96965.
```

The frozen target is

```text
T=(epsilon-A*log(82/215)-B*Delta V-C_rt*Delta Vrt)/3-e2
 =q+log(215/82)/3000,
q=2072411952219457/56091760829181000.
```

The logarithms are enclosed by a 30-term rational atanh series. No floating
solver status, floating objective, or approximate eigenvalue is accepted as
evidence.

## 3. Exact partition and dual bank

The canonical O0N1 event partition has 134 parent chambers. A frozen list of
60 parent chambers is divided into four equal rational `t`-subintervals;
the other 74 are retained whole. Thus

```text
60*4+74=314 complete phase pieces.
```

The exact bank contains 628 epoch duals, each with 308 nonnegative integer
weights, for 193,424 weights in total. The only denominators are `100000`
and `100000000`; support sizes range from 183 to 307. Every dual is replayed
from the current C126 exact model. Both endpoints of every piece pass exact
fraction-free Bareiss positive-definiteness, giving 1,256 endpoint checks.

All 480 epoch duals on subdivided parent chambers strictly improve the
corresponding stored parent objective. The 148 epoch duals on unselected
chambers are inherited exactly. The regenerated rational partition has
SHA-256

```text
a71fc17672166167bc379e8c5bc060649d8187dd760cc0d0a1dfdc5e49fa9ca1.
```

## 4. Complete-phase separation

Classification is performed only after summing the exact log-integral
enclosures over all 314 pieces and normalizing by an exact enclosure of
`log(2)`. Piecewise signs are used only to orient interval multiplication;
there is no chamberwise positivity or sign acceptance criterion.

The clean exact fences are

```text
U^+ < 36849435771/1000000000000
    < 18634061003/500000000000
    < T^-,

T^- - U^+ > 83737247/200000000000 > 1/2500.
```

The independent replay reproduces the exact hashes

```text
normalized refined interval: a00860e08252ac6106e6fec4190a1e843f8d9be3d559c471ea160004343c08b7
target interval:             c0c8dff6dad73696ecbef46168112f2ac0cd23ab831857e2c7489973a0c1ab65
separator margin:            391b05b51ab82272dc7da5e1d31116a2f436ea8e757c8409e9670ff78c593783
```

## 5. Earlier NO_SEPARATION false negative

The preserved parent bank has one stored constant dual vector for each of the
134 original combinatorial chambers. Its full exact replay again gives

```text
1887/1000000 < U^- - T^+ < 1888/1000000.
```

That `STORED_DUAL_NO_SEPARATION` outcome was a false negative as an
infeasibility classifier: the exact stored vectors were feasible, but that
particular stored construction lacked enough piecewise expressivity to expose
the separator. The refined bank improves the parent-normalized-lower versus
refined-normalized-upper comparison by more than

```text
461159269/200000000000.
```

This does not prove that every optimally chosen unsplit dual would fail. The
earlier result was never a primal-feasibility certificate.

## 6. Finite universal consequence

Define the isolated **D1 rotation hypothesis** to be:

> Every Golomb member of the specified frozen `4x8` cyclic old/new
> same-multiset rotation bank satisfies the frozen candidate complete-phase
> lower bound in the setup of Section 1.

By weak duality, the exact O0N1 separator refutes its frozen candidate lower
bound. Therefore this universal finite D1 rotation hypothesis is false.
Equivalently, the C130-type O0N0 feasibility result does not transfer to every
Golomb-retained cyclic rotation under this exact frozen setup. C130 itself is
unchanged and remains valid within its own stated scope.

This local name is unrelated to the repository's Q2 DAG node `D1` and the
approach-registry label `D1`.

## 7. Claim boundary

C135 does not claim any of the following:

- Route C is false;
- C130 or C131 is invalid;
- arbitrary representative independence is globally false;
- the common phase rule is globally admissible;
- cross-row compatibility or a global C103 owner ledger is constructed;
- arbitrary history or arbitrary rank is handled;
- C058, Q1, or Q2 is false or resolved;
- Erdős Problem #1191 is resolved.

`FINAL_STATUS.txt` remains `UNRESOLVED_AT_HARD_LIMIT`.

## 8. Preserved artifacts and replay

The discovery artifacts are preserved byte-for-byte:

```text
refined source SHA-256:
2949602baa0cb68aa3131bcb003fa2ac35156743bb2202e9a02f906ccf960c6b
refined internal SHA-256:
8c19def256d58813a22220d80fe1ec96fcd5da1a3cb580381e5fee70fb38310d
parent source SHA-256:
93efb6b9846800f4025d72bd79536cc052f46f750e706b2966efa90928002912
parent internal SHA-256:
325d1c4e5556ab654a21c698583628478e750c61859622140a414ac0228aac43
```

Reproduce from `route_probes/`:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B ROUTE_C_C135_D1_O0N1_COMPLETE_PHASE_DUAL_NO_GO_certificate.py
PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest -v ROUTE_C_C135_D1_O0N1_COMPLETE_PHASE_DUAL_NO_GO_test.py
PYTHONDONTWRITEBYTECODE=1 python3 -B ROUTE_C_C135_D1_O0N1_COMPLETE_PHASE_DUAL_NO_GO_independent_oracle.py
```

The focused suite has 10 tests and rejects rehashed scope/fixture upgrades,
partition mutations, malformed or changed exact dual data, provenance drift,
and a controlled doubled-weight mutation whose two endpoint slacks are both
non-PD. The independent oracle does not import the C135 verifier and contains
no `/private/tmp` dependency or removable `assert` gate.
