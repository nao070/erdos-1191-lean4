# Wave 3 continuation: positive gap multiscale and birth obstructions

**Date:** 2026-08-28  
**Global status:** `UNRESOLVED_AT_HARD_LIMIT`

## Rigorous advances

1. At the diameter modulus, endpoint variance has the exact sign-free formula

   \[
   V_m=N_m^{-2}\sum_{k<\ell}h_kh_\ell
   (\ell-k)^2(m-k-\ell)^2.
   \]

2. For every Sidon ruler with \(m=8q\ge16\),

   \[
   V_m\ge\frac{9D_mq^5(q-1)}{16N_m^2}
   \ge\frac{9m^6}{16\,777\,216N_m}.
   \]

3. Under a hypothetical critical envelope
   \(N_m\ll_Cm^2\log m\), the positive dyadic functional

   \[
   \mathcal G_J=\sum_jV_{m_j}/m_j^4
   \]

   is at least a positive constant times \(\log J\).

4. The same functional has an exact nonnegative birth-pair kernel.  Its
   unconditional shell estimate is only
   \(\mathcal G_J\le(4/3)\log N_J=O(J)\).

5. The normalized gap measure has an exact positive matrix dynamics.  With
   \(f(u)=u(1-u)\), \(z=(f,u)\), and
   \(\mathcal M_m=N_m\operatorname{Cov}_{\nu_m}z\),

   \[
   \mathcal M_{2m}=B\mathcal M_mB^{\mathsf T}+Q_m,
   \qquad B=\begin{pmatrix}1/4&1/4\\0&1/2\end{pmatrix},
   \qquad Q_m\succeq0.
   \]

   Selecting the largest \(3m/4\) distinct adjacent gaps and aging them over
   two dyadic steps gives, for \(M=4m\ge16\),

   \[
   \frac{V_M}{M^4}\ge
   \frac{9M^2-256}{1\,048\,576N_M}.
   \]

   Under \(N_M\le2CM^2\log M\), this is
   \((9-256/M^2)/(2\,097\,152C\log M)\), sixteen times the
   direct eight-block constant.  See
   `endpoint_variance/GAP_MEASURE_DYNAMICS_AND_TWO_STEP_LOWER_BOUND_2026-08-28.md`.

6. The missing upper problem has an exact adjoint-Lyapunov form.  With
   `R_j=M_j/N_j`, `G_j=<E,R_j>`, and backward weights
   `H_j=E+(N_j/N_(j+1))B^T H_(j+1)B`,

   \[
   \sum_{j\le J}G_j
   =\langle H_1,R_1\rangle
   +\sum_{j\le J}\langle H_{j+1},Q_j/N_{j+1}\rangle.
   \]

   The universal majorant is
   `H=((16/15,8/105),(8/105,4/35))`.  An exact critical abstract orbit has
   arbitrary PSD innovations but `G_j=1/72`, so recursion, PSD, and critical
   growth alone allow linear accumulation.  This orbit is not claimed to be a
   compatible Golomb birth process.  Consequently the remaining estimate
   must use the arithmetic structure of the actual innovations.

7. A three-rank lift preserves the Sidon property and forces
   \(V_m/m^4\ge1/2304\) in one birth shell, even at diameter \(O(m^2)\).
   Thus no uniform pointwise `o(1)` bound follows from one isolated Sidon
   ruler and its quadratic diameter.  This rank-lift example alone does not
   exclude compatible bounded-depth hypotheses; the separate construction in
   the next item does.

8. A separate Erdős--Turán family closes the purely local fixed-depth route.
   For every fixed `L`, arbitrarily large finite Sidon rulers have their last
   `L+1` dyadic prefixes inside one `C=1` critical envelope, while

   \[
   \operatorname{Var}_{\nu_M}f\to1/180,
   \quad Q_{m,00}/N_M\to1/360,
   \quad L_m\to19/3840.
   \]

   The born diagonal is `O(M^-2)`, so the signed born off-diagonal shell also
   stays positive.  This refutes uniform finite-window `o(1/j)` lemmas based
   only on those prefixes and their local compatibility.  It does not refute
   a hypothesis of embeddability in one infinite globally critical sequence
   or an unbounded-history amortization theorem.

9. For cyclic interval loads, the exact q-cover projection is

   \[
   q^2V_{qN}=V_N(R_N)+\mathcal I_{N,q},\qquad\mathcal I_{N,q}\ge0.
   \]

   It produces a genuine frozen-edge martingale.  Complete loads fail because
   newborn edges can cancel old residual arcs exactly; `{0,1,4}` is the
   minimal example.

## Falsification outcome

The exact critical-shell search refutes five natural shortcuts H1--H5 on
four-mark Golomb rulers.  Net shell nonnegativity H6 survived the certified
finite ranges, including all stated four- and eight-mark ranges and seeded
16/32-mark witnesses, but is not a theorem and would not give the missing
upper bound even if true.

## Precise remaining target

Prove, using compatibility across unboundedly many nested Sidon prefixes,

\[
\mathcal G_J=o(\log J)
\]

under the critical envelope, or find a different global functional with the
same forced lower accumulation and a provable smaller Sidon budget.  The exact
matrix update may be used, but the proof must bound its innovations or charge
long-range signed gap interactions.  A fixed ordered interaction has tail at
most \(4/(15m_s^4)\), and the crude absolute charge is now only \(O(1)\) per
shell; turning this \(O(J)\) bound into \(o(\log J)\) is the precise bottleneck.
Local positivity, scalar martingales, and distinct-difference Bessel
heuristics are rigorously insufficient.

## Verification

The Wave 3 code uses exact rational arithmetic.  Run the package-level
`integrity/run_all_checks.sh`; current test counts, certificate hashes, and
the extracted-package audit are recorded in `HANDOFF_MANIFEST.md` and the
dated integrity report.  These are algebra and finite-search audits only.
