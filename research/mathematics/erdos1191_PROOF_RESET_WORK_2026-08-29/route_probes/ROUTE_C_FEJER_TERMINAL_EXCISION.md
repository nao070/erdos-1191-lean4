# Route C: Fejér terminal excision

Status: `HUMAN_PROOF_AUDITED`, conditional on a legal core rewrite.  This
removes the numerical `m=3,2,1` gate from the asymptotic C058 target; it does
not construct the arbitrary-history core master or its global owner ledger.

## Statement

Let `n_k=2^k` and

\[
 \omega_{k,J}=\left(\frac{J+1-k}{J+1}\right)^2.
\]

Suppose a legal aggregate core rewrite is used only through `K=J-3`, and the
complete baseline Gothic/terminal ledger is retained once on the last three
epochs.  Under the canonical eventual-`C` cap

\[
 N_m\le C m^2\log(2m),
\]

the possible loss from not using the positive-margin core master at
`k=J-2,J-1,J` is `O_C(J^{-1})=o(1)`.  The complete retained Wave-16 terminal
potential on these epochs contributes only
`O_C(\log J/J^2)=o(1)` on its positive side.  Thus a contradiction with a
positive multiple of `log J` does not require a positive whole-stencil margin
at Fejér ratios `4/9`, `1/4`, or `0`.

This is an asymptotic excision statement.  It does not produce an exact
zero-error inequality for each finite `J`.

## Proof of the master-loss bound

For one epoch let

\[
 D_n(\theta)=\sum_r T_r Q_n(T_r).
\]

The strict-interior positive coefficient mass is exactly

\[
 \sum_{\gamma\in\Gamma_n}\beta_\gamma
 =\frac{(n-1)^2}{4n^2}<\frac14.
\]

The dyadic harmonic estimate gives

\[
 \sum_rT_rR_{T_r}(d)
 \le 1+\log_2(H'_n/d)
 \le 1+\log_2H'_n,
\]

and hence

\[
 D_n(\theta)<\frac14(1+\log_2H'_n).
\]

Every PSD price satisfies `P_n>=0`, so for
`\Phi_n=2D_n-P_n`,

\[
 (\Phi_n)_+\le2D_n.
\]

The final three Fejér weights sum to

\[
 \frac{9+4+1}{(J+1)^2}=\frac{14}{(J+1)^2}.
\]

Consequently

\[
 \sum_{k=J-2}^{J}\omega_{k,J}(\Phi_{n_k})_+
 \le \frac{7(1+\log_2H_J^*)}{(J+1)^2}.
\]

The eventual cap implies

\[
 H'_n\le N_{2n}\le4Cn^2\log(4n),
\]

so the displayed loss is `O_C(J^{-1})=o(1)`.

For reference, applying the frozen C107 witness at the excluded ratios really
does fail:

\[
 \Phi(4/9)=-\frac{1694343157}{9000000000000},
\]

\[
 \Phi(1/4)=-\frac{1037939669073}{200000000000000},\qquad
 \Phi(0)=-\frac{290502965603}{25000000000000}.
\]

Turning that rewrite off is therefore the correct asymptotic operation; these
negative fixture values need not be repaired.

## Exact finite cutoff identity

Set `K=J-3` and set the transport coefficient `c^0_{k,r}` to zero for
`k>K`.  With the notation of the finite prefix/scale transport kernel, the
exact identity is

\[
\begin{aligned}
\sum_{k=k_0}^{J}w_k\sum_{r=L}^{U}c^0_{k,r}\Delta_{k,r}
={}&\sum_{r=L}^{U}\Big[
 w_Ks_{K,r}O_{K,r}
 -w_{k_0}s_{k_0,r}O_{k_0-1,r}\\
&+\sum_{k=k_0}^{K-1}
 (w_ks_{k,r}-w_{k+1}s_{k+1,r})O_{k,r}
\Big]\\
&+\sum_{k=k_0}^{K}w_ks_{k,U}\Delta_{k,U+1}.
\end{aligned}
\]

Thus the initial prefix boundary, cutoff final band, every interior
coefficient-difference row, and upper scale-terminal row must all be retained.
The one-variable scale Abel endpoints are

\[
 -T_LQ_L+T_{U+1}Q_{U+1};
\]

they vanish only when the chosen endpoints lie outside the support.

## Retained terminal potential

The last-three-epoch baseline must keep the complete Wave-16 identity, not
only its birth term:

\[
 \mathcal T_n=\mathfrak F_n+\mathfrak e_n+R_{2n}-\mathfrak U_n\ge0,
\qquad
 Z_n-R_{2n}=\mathfrak P_n-\mathfrak B_n-\mathcal T_n.
\]

Its existing bound

\[
 (Z_n-R_{2n})_+
 \le \frac34\log\log(4n)+O_C(1)
\]

has final-three Fejér contribution `O_C(\log J/J^2)=o(1)`.

## Ownership and remaining obstruction

Each net Gothic row must belong to exactly one of the core master or retained
baseline.  Pairing core epochs as

\[
 (k_0,k_0+1),(k_0+2,k_0+3),\ldots
\]

through `k<=J-3` uses only `m>=4` ratios and leaves at most three terminal
vertices.  This matching settles only Gothic-row duplication.  It does not
settle the one-owner rule for physical diagonal/carrier endpoints shared by
adjacent pairs.

The live C058 obligations are therefore the arbitrary-history/full-phase core
master, one-time ownership of shared endpoints, and payment of the explicit
cutoff/final/scale-terminal rows above.  No conclusion about C058, Q1, Q2,
novelty, or a prize follows from this memo alone.
