# Wave 19 sparse-spike cooldown boundary

**Research date:** 2026-08-29  
**Status:** **[COMPUTATIONAL - CERTIFIED FINITE]**, with exact integer and
rational checks for every Golomb and prefix-cap claim below.

This memo certifies a finite nested construction only. It does **not** produce
one infinite branch, refute P23, answer either question in Erdős Problem #1191,
or solve Erdős Problem #1191. The displayed values of the descendant-jump
functional (J_n^{(5/2)}) are high-precision transcendental projections. They
are not used in any Golomb or cap decision.

## 1. Conventions

All rulers are normalized increasing integer tuples

\[
0=a_0<a_1<\cdots<a_{m-1}.
\]

Write

\[
\Delta^+(A)=\{a_j-a_i:0\le i<j<m\}.
\]

The package's (C=32) prefix convention is

\[
N_m=a_{m-1}+1
 \le \left\lfloor 2C m^2\log m\right\rfloor
 =\left\lfloor64m^2\log m\right\rfloor.
\tag{1.1}
\]

It is useful to name the largest terminal permitted at mark count (m):

\[
U_m:=\left\lfloor64m^2\log m\right\rfloor-1.
\tag{1.2}
\]

Every logarithm in this memo is natural.

## 2. Exact (32+95+1) construction

### 2.1 The 32-mark root

The root is

```text
A32 = (
  0,15,32,44,58,74,85,200,202,205,223,224,233,269,273,1418,
  1425,1431,1479,1514,1534,1571,1657,1696,1790,1798,1850,
  1912,1984,2047,2072,7096
).
```

Its (\binom{32}{2}=496) positive differences are distinct.

### 2.2 The scaled 95-mark Erdős-Turán-type block

For (0\le j<95), define

\[
b_j=7\bigl(346j+(63j^2\bmod173)\bigr).
\tag{2.1}
\]

Thus (b_0=0), the first four marks are

\[
(0,2863,5397,7602),
\]

and

\[
b_{94}=228557=:W.
\]

The exact finite audit finds all (\binom{95}{2}=4465) positive differences
distinct. No asymptotic or full-field conclusion is needed here.

### 2.3 Separated union

Set

\[
T=235654=7096+228557+1
\]

and

\[
P_{127}=A_{32}\mathbin{\dot\cup}(T+B_{95}).
\tag{2.2}
\]

This has 127 marks and terminal

\[
T+W=464211.
\]

The difference partition is exact:

| sector | count |
|---|---:|
| inside (A_{32}) | 496 |
| inside (T+B_{95}) | 4,465 |
| cross block | (32\cdot95=3,040) |
| total | (8,001=\binom{127}{2}) |

The two internal spectra are disjoint. A cross difference has the form

\[
T+b-a.
\]

If two such differences agree, then a nonzero equality would give a common
positive internal difference of (A_{32}) and (B_{95}), which the exact
audit excludes. Hence the 3,040 cross differences are distinct. In addition,

\[
\max(\text{internal differences})=228557,
\qquad
\min(\text{cross differences})=T-7096=228558.
\]

Therefore cross and internal spectra are disjoint, and (P_{127}) is Golomb.

### 2.4 Primary and reserve terminal spikes

Append either

\[
X_{\rm primary}=5087721
\quad\text{or}\quad
X_{\rm reserve}=1271930.
\tag{2.3}
\]

Both exceed (2\cdot464211=928422). The separation lemma in Section 4
therefore proves that both 128-mark tuples are Golomb. Direct enumeration also
finds exactly

\[
\binom{128}{2}=8128
\]

distinct positive differences in each tuple.

## 3. Exact certification of every prefix cap

Binary floating point is not used to decide (1.1). For a rational
(1\le y\le2), put

\[
z={y-1\over y+1}.
\]

For every positive integer (K),

\[
L_K(y)=2\sum_{k=0}^{K-1}{z^{2k+1}\over2k+1}
 \le \log y
\]

and the positive tail satisfies

\[
0\le\log y-L_K(y)
\le {2z^{2K+1}\over(2K+1)(1-z^2)}.
\tag{3.1}
\]

Write each integer (m\ge2) as (m=2^r y), with (1\le y<2). Applying
(3.1) to (2) and (y) gives rational lower and upper bounds for
(\log m=r\log2+\log y). The certificate multiplies both bounds by
(64m^2) and increases (K) until their integer floors agree. That common
integer is the certified value of (\lfloor64m^2\log m\rfloor).

Every prefix from (m=2) through (m=128) passes for both terminal choices.
The primary terminal saturates the last cap exactly:

\[
5087721+1
=5087722
=\left\lfloor64\cdot128^2\log128\right\rfloor.
\tag{3.2}
\]

For the reserve terminal, the first-next-prefix cap is

\[
\left\lfloor64\cdot129^2\log129\right\rfloor=5175816,
\]

so its recorded next-prefix slack is exactly

\[
5175816-(1271930+1)=3903885.
\tag{3.3}
\]

## 4. Extension and maximal-terminal lemmas

### Lemma 4.1: exact one-point forbidden shadow

Let (A) be a finite Golomb ruler and let (x>\max A). Then

\[
A\cup\{x\}\text{ is Golomb}
\quad\Longleftrightarrow\quad
x\notin A+\Delta^+(A).
\tag{4.1}
\]

**Proof.** The new differences (x-a), (a\in A), are pairwise distinct.
The only possible collision is therefore (x-a=d) for an old difference
(d\in\Delta^+(A)), equivalently (x=a+d\in A+\Delta^+(A)). \(\square\)

### Corollary 4.2: separated terminal

If (A) is normalized with terminal (H), then every old difference is at
most (H). If (x>2H), every new difference is at least
(x-H>H). Hence (A\cup\{x\}) is Golomb.

### Corollary 4.3: exact cap maximum for a fixed core

For a fixed ((m-1))-mark normalized Golomb core with terminal (H), if

\[
U_m>2H,
\tag{4.2}
\]

then (U_m) is legal by Corollary 4.2. It is also the largest legal terminal
under (1.1), because no integer larger than (U_m) satisfies the cap. Thus
maximality over the complete legal domain is proved without classifying the
lower candidates.

## 5. The descendant-jump functional

For (2\le p\le n) and (n\le q\le2n-2), define

\[
D_{p,q}=a_q-a_{p-1},
\qquad
d_{n,p}=a_{2n-1}-a_{p-1},
\]

\[
L_{n,p}=\binom{2n-p+1}{2},
\qquad
c_n={(n-1)(3n-4)\over2},
\]

\[
r_{n,p}={4n-2p-3\over8n^2},
\]

and

\[
\beta_{n,p,q}=
\begin{cases}
1/n^2,&p=q,\\
1/(4n^2),&p=q-1,\\
1/(2n^2),&p\le q-2,
\end{cases}
\qquad
w_{n,p}=\sum_{q=n}^{2n-2}\beta_{n,p,q}.
\]

The audited Wave 18 functional is

\[
J_n^{(h)}=
\sum_{p=2}^n{r_{n,p}\over w_{n,p}}
\sum_{q=n}^{2n-2}\beta_{n,p,q}
\log_+\!\left(
 {d_{n,p}c_n\over e^hL_{n,p}D_{p,q}}
\right).
\tag{5.1}
\]

At (h=5/2), Decimal precision 80 gives:

| finite prefix | (n) | (J_n^{(5/2)}) |
|---|---:|---:|
| primary 128 | 4 | 0.00207857666134448790116808217985169... |
| primary 128 | 8 | 0.06999594179639167333554727545726496... |
| primary 128 | 16 | 0.02824820609231238026097147132079141... |
| primary 128 | 32 | 0 |
| primary 128 | 64 | 0.31393714841781551906475165119399590... |
| reserve 128 | 64 | 0.06891061854425407828425688515323626... |
| primary optimized 256 | 128 | 0.01272516844381263848423096161164741... |
| reserve optimized 256 | 128 | 0.30918607717778162040642138337083231... |
| reserve cooldown, optimized 512 | 256 | 0.00570953372166603339834664256385869... |

The originally supplied binary64 values agree within (10^{-15}). Equation
(5.1) contains logarithms and (e^{5/2}), so these rows are projections, not
exact rational identities.

## 6. Complete one-step scans and deterministic 255-mark cores

For a fixed prefix, (4.1) lets the code construct the complete forbidden set
inside the next legal domain instead of checking every candidate against
every pair repeatedly.

At the 128-to-129 step:

| prefix | legal-domain size | forbidden | allowed | first allowed |
|---|---:|---:|---:|---:|
| primary | 88,094 | 3,249 | 84,845 | 5,087,755 |
| reserve | 3,903,885 | 8,128 | 3,895,757 | 1,271,964 |

These two rows classify the complete next-prefix integer domains and are
exhaustive for the fixed 128-mark inputs.

For each later mark count through 255, the deterministic search chooses the
smallest legal integer under (1.1). Every candidate below the chosen mark is
tested, so each local first-legal choice is exhaustive for its fixed prefix.
Alternative earlier choices are not explored, so the branch search is not
globally exhaustive and proves no optimum.

The resulting 255-mark core terminals are

\[
H_{255}^{\rm primary}=5192189,
\qquad
H_{255}^{\rm reserve}=1376398.
\tag{6.1}
\]

A continuation that also takes the first legal mark at count 256 ends at
5,192,370 and 1,376,579 respectively. Both are exact 256-mark Golomb rulers,
but they do not maximize the final terminal.

## 7. Exhaustive terminal optimization at 256 marks

The exact cap maximum is

\[
U_{256}=23258158.
\tag{7.1}
\]

For the primary 255-core,

\[
A+\Delta^+(A)\le H+\max\Delta^+(A)
=2H=10384378<U_{256}.
\]

For the reserve 255-core,

\[
2H=2752796<U_{256}.
\]

Thus (U_{256}) has zero blockers for both cores and is the exact largest
legal 256th mark. The candidate-domain sizes are 18,065,969 and 21,881,760.
Only the top candidate needs examination for maximality; the lower domains
are intentionally not classified.

The two optimized 256-mark tuples each have all 32,640 positive differences
distinct and satisfy every (C=32) prefix cap. The reserve version has the
larger displayed (J_{128}^{(5/2)}), so it is the finite input selected for
the cooldown experiment. This selection criterion is projection-only; the
Golomb and cap certification does not depend on it.

## 8. Cooldown necessity boundary

The word *cooldown* means inserting first-legal marks while the cap grows,
before attempting another terminal chosen at the full cap.

### Theorem 8.1: a second separated cap spike cannot be immediate

Suppose a normalized nested branch has already selected the cap maximum

\[
H_{256}=U_{256}=23258158.
\]

At a later mark count (M), every continuation core has terminal
(H_{M-1}\ge U_{256}). To certify the next cap maximum (U_M) by the same
spectral separation argument, one needs

\[
U_M>2H_{M-1}\ge2U_{256}=46516316.
\tag{8.1}
\]

The exact caps give

\[
U_{257}=23456698<46516316
\]

and, more sharply,

\[
U_{352}=46497749<46516316<U_{353}=46784940.
\tag{8.2}
\]

Since (U_M) is increasing, no continuation can reuse the sufficient
(x>2H) separation proof for a second cap-maximal spike at any
(257\le M\le352). At least 96 intermediate marks are therefore necessary
before that particular proof mechanism can possibly return.

This is **not** a theorem that (U_M) is illegal for all (M\le352). It is a
sharp obstruction only to the universal high/low spectral separation proof.
Other arithmetic cancellations inside (A+\Delta^+(A)) are not excluded.

### The certified cooldown path

Starting from the reserve optimized 256-prefix, the deterministic first-legal
rule is run for mark counts 257 through 511. It succeeds with

\[
H_{511}=24032260.
\]

The search tests 774,102 candidates in total. Its largest local scan is
15,707 candidates at mark count 456. The fixed 511-mark output has all

\[
\binom{511}{2}=130305
\]

positive differences distinct and passes every prefix cap. This is an exact
finite witness, but the discovery branch is not globally exhaustive.

On this actual path, the separation inequality first becomes available at
mark count 354:

\[
U_{354}=47073074
>2\cdot23426060=46852120.
\]

The construction continues to 512 because the target boundary is the dyadic
transition (256\to512), not because 354 is impossible.

At the dyadic endpoint,

\[
U_{512}=104661718,
\qquad
2H_{511}=48064520,
\]

with separation margin

\[
104661718-48064520=56597198.
\]

Corollary 4.3 therefore proves that (104661718) is the exact largest legal
512th mark for this fixed 511-core. The resulting 512-mark ruler has all

\[
\binom{512}{2}=130816
\]

positive differences distinct and satisfies every (C=32) prefix cap.

## 9. Completeness and claim boundaries

The following statements are exhaustive:

1. Every pair difference of every displayed fixed witness is enumerated.
2. Every prefix cap is decided by exact rational logarithm enclosures.
3. The primary and reserve 128-to-129 domains are completely classified.
4. Each first-legal choice is minimal for the fixed prefix reaching it.
5. The terminal choices (U_{256}) and (U_{512}) are the largest legal
   terminals for their fixed 255- and 511-mark cores.

The following statements are not exhaustive:

1. The greedy search does not explore alternative branches to 255 or 511.
2. No smallest-span, largest-(J), or globally optimal ruler is claimed.
3. The lower candidate domains at the optimized 256 and 512 stages are not
   classified because the legal cap maximum already proves maximality.
4. No compatible tower exists here beyond the displayed finite 512-prefix.
5. The finite values of (J_n^{(5/2)}) do not refute the tapered asymptotic
   assertion P23.

Accordingly, this is a **finite nested witness only**. There is **no infinite
branch**, **no P23 refutation**, and **no solution of Erdős Problem #1191**.

## 10. Authentication hashes

For a tuple of integers, `marks SHA` and `difference SHA` mean SHA-256 of
comma-separated base-ten integers with no trailing newline. Difference tuples
are sorted increasingly and retain every enumerated pair entry before the
distinctness check.

| object | marks SHA-256 | sorted-difference SHA-256 |
|---|---|---|
| 32-mark root | `453085605c07dea071c2c5e1bb8d9d90e6a3886a0f3ed1665ef0e84f18586e68` | `882e53653e3733ad3e5fbdf05b61b7177fd0835b1efe433961c0d52a27d30a04` |
| scaled ET 95-block | `9f2d5b77e2c9335aeba714d701d95ac5c9154797c824a0dfa859555c46a2f90d` | `e803edf53e8f67e50429e82b52b491a3d03228653faa46a0102aab8f8e3e68c3` |
| separated 127-union | `d9ac3a565ae01382d40e7c13d3a377ead67522164c3102af69fda3d9c53afbe8` | `20c9b39f25e220d35b31c12c40beb96598e5df527e203e780c5683f891d7c7db` |
| primary 128 | `ec7965ccb5c05c0cfcf68900153f09f37ca39f94f9601f0b2b67c29cfacaf373` | `dfd2b62ff0b1494727177b26f1ffb61108ff077a0ffbeb627dea072a255c4ff3` |
| reserve 128 | `972b1ca7bff4a1425405f934ea776cbca5066673145acc434ac5eb43f068b4a7` | `e1b90baa94d7822da894824976c316cebf106fa797bc78e4ad4677d0be7d2f7d` |
| primary first-legal 256 | `b250a53ef2532e4e45f0aeed8021b97b7c37c1180b57088da8d557179091adb8` | `2696e033857455359f03f9b7639ded516695ebe2dff4aa1263a04b90ebe1c0e0` |
| reserve first-legal 256 | `10145a6470d236b806f9a60dae26bc7e1b52277d690bbec4c7097997319f1530` | `945f61374b962b1903b7f553afd3e236c9fce02d6a80cb194b12499064bfa897` |
| primary optimized 256 | `4254c6af1ddc0d30e472ec42353b1f7cc9a4fe279e9eaf5bdfd1b25e128643c7` | `470771223038ada2c60858096d0aa9cab6bc97eee8d49811055540254e0cbe28` |
| reserve optimized 256 | `c81e6a65e3164d7da3cf6c70b2c587ab8e4c309c0221c94cf9266a0fcceab4c6` | `21344b8e7e0f337e31f5407fd6ab7d7e5ed9ed3ab3442473b3400846a55cb52c` |
| reserve cooldown 511 | `7817c391cb7a33540dcba164805e88411132cf5fa0f4ccff8313e0da13a0e36b` | `ff3b462cf0bd4c47faba92562d9b71b26e01b9af0ebe28d2fbd724e8924e8ab3` |
| optimized 512 | `9721cbfaa645e96e73283b37d7c476d4a9286799ac2197da40ed1cac79b2ae63` | `cdad53cb4928712573069e30708d7d354f76302cdb355329a9711759ebb6a7f4` |

The deterministic JSON certificate has internal canonical-payload SHA-256

```text
db785aed118ee4d075655354d254319fe7b789f14cbccdfce45fa4418b57703c
```

and complete file SHA-256

```text
90e1e4b53624e40e239bb28947544884a122eaf68eecb7081e416e294ab0acb8
```

The executable artifacts used for replay have SHA-256 values

```text
15034edbfef6a887bd094886511762c5268439afc8bf61087fdb1ee77a737ac2  wave19_sparse_spike_certificate.py
14f0821c69e809e75bcde4c6c30da880cb93142392d36afbe7797fbfe7d681a2  wave19_sparse_spike_search.py
d4e117114ad1fd59aa63622c7eeeafd3b02914c5ebb62332a6f9fd0dc3d25b4e  wave19_sparse_spike_test.py
```

## 11. Deterministic replay

From `core_workspace/endpoint_variance/`, run

```bash
python3 wave19_sparse_spike_certificate.py
python3 -m unittest -v wave19_sparse_spike_test.py
```

The isolated suite reports 13 passing tests and 23 passing subtests. The CLI
rebuilds `wave19_sparse_spike_certificate_2026-08-29.json`; its replay test
requires byte-for-byte equality with the committed certificate, and its
internal canonical hash is independently recomputed after removing the
`certificate_sha256` field.

Primary artifacts:

- `wave19_sparse_spike_certificate.py`
- `wave19_sparse_spike_search.py`
- `wave19_sparse_spike_test.py`
- `wave19_sparse_spike_certificate_2026-08-29.json`
