# Route C: whole-stencil cross-width master

Date: 2026-08-30  
Status: `EXACT_FIXED_AGGREGATE_CROSS_WIDTH_REOPENING_GLOBAL_C058_OPEN`

This bundle certifies a fixed two-epoch, one-phase reopening of the signed
Route-C master.  Its mechanism is not the closed C067 positive-pair
allocation.  It replaces the complete Gothic ledger, once, by the aggregate
four-corner stencil identity and pays the resulting signed rows with a common
positive-semidefinite master that is block diagonal by epoch but couples
different widths inside each epoch.

The result is finite and exact.  It does not prove C058, either Erdős
question, an infinite compatible history, novelty, or prize eligibility.

## 1. Frozen fixture

The points and sampled widths are

\[
 a_k=k(k+100),\quad 0\le k\le15,
 \qquad T\in\{100,200,400,800\}.
\]

There are 52 physical Haar channels, 77 events, 76 positive-length cells,
eight epoch-width owners, and 608 exact owner-cell inequalities.  The shared
endpoint \(a_7\) belongs once to the past \(n=4\) coordinate block.

## 2. Whole signed stencil identity

For a source \(\gamma=(n,i,j)\), put

\[
 \alpha_\gamma={ (j-i)^2\over4n^2},\qquad
 M=a_{j-1}-a_i,
\]

and let \(u=a_i-a_{i-1}\), \(v=a_j-a_{j-1}\).  With

\[
 R_T(d)={(T-d)_+\over T^2},
\]

the complete four-corner stencil is

\[
 \psi_\gamma(T)=R_T(M)+R_T(M+u+v)
 -R_T(M+u)-R_T(M+v).
\]

All 24 sources satisfy

\[
 \psi_\gamma(100)=\psi_\gamma(1600)=0.
\]

The lower equality holds because every middle span is greater than 100.  At
1600 all four overlaps are in their affine ranges and cancel exactly.  Hence

\[
 C_\gamma
 =\sum_{T=100,200,400,800}
 2T\alpha_\gamma\bigl(\psi_\gamma(T)-\psi_\gamma(2T)\bigr)
 =\sum_{T=200,400,800}T\alpha_\gamma\psi_\gamma(T).
\]

The exact totals are

\[
 D_4={9\over128},\qquad
 D_8={1349\over10240},\qquad
 D={2069\over10240}.
\]

The primitive off-diagonal convention is \(-\alpha_\gamma/2\) in each
symmetric position.  Therefore its quadratic cross term is

\[
 2(-\alpha_\gamma/2)\langle e_iK_T,e_jK_T\rangle
 =\alpha_\gamma\psi_\gamma(T).
\]

The certificate checks all 46 identities

\[
 \lambda_{n,p,q}=2M_{p-n,q-n+1}
\]

and thus excludes an accidental extra factor of two.

For \(f_n(T)=TQ_n(T)\), every integrated owner band is

\[
 b_n(T)=2f_n(T)-f_n(2T).
\]

The complete ledger is:

| epoch | width | \(f_n(T)\) | \(b_n(T)\) |
|---:|---:|---:|---:|
| 4 | 100 | \(0\) | \(-9/160\) |
| 8 | 100 | \(0\) | \(-117/3200\) |
| 4 | 200 | \(9/160\) | \(63/640\) |
| 8 | 200 | \(117/3200\) | \(169/12800\) |
| 4 | 400 | \(9/640\) | \(9/320\) |
| 8 | 400 | \(767/12800\) | \(4331/51200\) |
| 4 | 800 | \(0\) | \(0\) |
| 8 | 800 | \(361/10240\) | \(361/5120\) |

In particular, the negative first bands are present in the 608 constraints;
they were not dropped as boundary errors.  The upper 1600 terminal is exactly
zero.

## 3. Aggregate ownership only

The 24 sources produce 96 corner occurrences.  They collapse to 42 nonzero
physical Gothic rows, 28 of which are reused with mixed signs.  For example,

\[
 (a_3,a_6):\qquad {1\over16}-{9\over64}=-{5\over64}.
\]

Accordingly, the certified construction owns each net Gothic row once.  It
does not claim that each primitive occurrence is an independent capacity.

The exact countercell is

\[
 (n,T,c)=(4,200,[709,725)).
\]

Here primitive \((5,7)\) contributes \(1/3200\), primitive \((4,7)\)
contributes \(-9/25600\), and the aggregate demand is \(-1/25600\).  The old
PSD witness supplies

\[
 x=-{49528467\over1690000000000}.
\]

Its aggregate slack is

\[
 x+{1\over25600}={8243579\over845000000000}>0,
\]

but its residual against the positive primitive is

\[
 x-{1\over3200}
 =-{577653467\over1690000000000}<0.
\]

This is an exact regression against primitivewise reinterpretation, not an
objection to the aggregate one-for-one Gothic replacement.

## 4. Epoch-block, cross-width PSD witness

Partition the 52 coordinates into the 20-coordinate \(n=4\) block and the
32-coordinate \(n=8\) block.  For

\[
 E_m=\begin{bmatrix}I_{m-1}\\-\mathbf1^T\end{bmatrix},
\]

the certificate embeds the stored integer matrices as

\[
 X_4={E_{20}\widehat Z_4E_{20}^T\over10^{14}},\qquad
 X_8={E_{32}\widehat Z_8E_{32}^T\over10^{14}},
 \qquad X=X_4\oplus X_8.
\]

Exact unpivoted LDL replay gives 19 and 31 positive pivots for the two
\(Z\) blocks.  Thus \(X\succeq0\), \(X\mathbf1=0\), and its cross-epoch
block is exactly zero.  Cross-width entries within each epoch are nonzero.

All 608 owner rows hold exactly.  There are 254 zero or structural slacks;
the minimum positive slack is

\[
 {41304919\over12500000000000}.
\]

The physical price and aggregate margin are

\[
 P={3900000000091\over10000000000000},
\]

\[
 \Phi=2D-P
 ={141015624909\over10000000000000}>0.
\]

This does not contradict the C106 no-go.  C106 closes the same PSD cone only
when it is paired with C067's smaller positive-pair gain.  The present gain
comes from replacing the full signed Gothic ledger.

## 5. Cross-width coupling is necessary on the fixture

Restrict instead to four independent 13-coordinate width blocks.  An exact
dual uses 380 positive owner-row weights: 152 at width 200, 152 at width 400,
76 at width 800, and none at width 100.  The four projected \(12\times12\)
slacks have 48 positive rational LDL pivots in total.  The resulting bound is

\[
 P\ge {843669938599\over2048000000000}.
\]

It exceeds \(2D\) by

\[
 {16069938599\over2048000000000}>0.
\]

Thus positive aggregate \(\Phi\) is impossible in the no-cross-width cone.
Cross-width coupling is the genuine finite mechanism exposed here; an
epoch-cross matrix block is not required on this fixture.

## 6. Exact Fejér-weight gate

The two epoch margins are

\[
 \Phi_4=-{290502965603\over25000000000000},\qquad
 \Phi_8={1286084055751\over50000000000000}.
\]

After normalizing \(w_4=1\) and writing \(r=w_8/w_4\), positivity is
equivalent to

\[
 r>{581005931206\over1286084055751}\approx0.451764.
\]

For the Fejér ratio \(r=((m-1)/m)^2\), every \(m\ge4\) succeeds.  The worst
such value is

\[
 \Phi(9/16)={2278661602463\over800000000000000}>0.
\]

The next terminal ratio fails:

\[
 \Phi(4/9)=-{1694343157\over9000000000000}<0.
\]

The audited \(j=3,4,J=12\) ratio \(81/100\) gives

\[
 \Phi(81/100)
 ={46072215395231\over5000000000000000}>0.
\]

Hence the finite design handles the interior \(m\ge4\) range, while the last
\(m=3,2,1\) epochs remain an explicit terminal problem.

## 7. Fixed old-witness directed-flow regression

For uniform current-to-past variables \(\tau_j\) on the left-interface
sources \((8,8,j)\), five exact tight rows force

\[
 \tau_{10}=\tau_{11}=\tau_{12}=\tau_{14}=\tau_{15}=0.
\]

The remaining source \((8,8,13)\) has zero sampled capacity.  This is a
fixed-old-\(X\), fixed-orientation result only.  No theorem is asserted about
the exploratory jointly reoptimized SDP.

## 8. Scope and next gates

The bundle proves only the frozen aggregate finite statement.  The following
remain open and are represented by literal `false` scope fields:

- a primitive-owned cover;
- a directed current-to-past source map;
- continuum logarithmic-phase integration;
- the \(m=3,2,1\) final-terminal closure;
- a global birth/final/terminal ownership ledger;
- a uniform arbitrary-history epoch template;
- C058, Questions 1 and 2, novelty, publication, or a prize claim.

The next falsifiable target is a phase-chamber and terminal certificate that
preserves the exact \(m\ge4\) weighted margin while separately closing the
last three Fejér epochs.

## 9. Replay

Run:

```bash
python3 ROUTE_C_WHOLE_STENCIL_CROSS_WIDTH_MASTER_test.py
python3 ROUTE_C_WHOLE_STENCIL_CROSS_WIDTH_MASTER_certificate.py \
  --verify ROUTE_C_WHOLE_STENCIL_CROSS_WIDTH_MASTER_certificate.json \
  --self-check
```

The committed payload SHA-256 is

```text
5879f3b774b8b044f01f6a7d529946d620478191b7a9ed8b7e246c6e16063e57
```
