# Wave 8: exact cross-epoch pair telescope

Date: 2026-08-28  
Scope: the cumulative dyadic sum of the exact signed pair identity (14)  
Status: **rigorous structural theorem and rigorous no-go; Problem #1191 remains open**

## 1. Outcome

The negative old-pair terms in (14) do not create a hidden long-history
cancellation.  Keeping every one of them gives the following results.

| Statement | Status | Conclusion |
|---|---|---|
| Exact coefficient of one pair under constant `H` | **PROVED** | Birth charge minus every later old-pair subtraction is given by (6). |
| Sign after the Lyapunov telescope | **PROVED** | It is a sum of positive `E`-atoms with positive scalar weights. |
| Uniform retention for arbitrary increasing moduli | **PROVED** | At least one half of every raw birth charge survives; (10) gives the sharper ratio-dependent bound. |
| Global regrouping | **PROVED** | The whole fixed-`H` innovation sum is between one half and one times the globally unique birth-pair budget. |
| Exact finite-horizon adjoints | **PROVED** | The signed pair sum is exactly the positive future state-energy tail (17). |
| Constant-ratio and critical-ratio limits | **PROVED, conditional on the stated ratio hypothesis** | The three distinct kernels are `H_rho`, `H_(rho^2)`, and `F_rho`; at `rho=1/4` the retention is at least `4/5`. |
| Old-pair cancellation as the missing `o(log J)` mechanism | **REFUTED** | It can save at most a constant factor, never an unbounded factor. |
| `B_H(J)=o(log J)` on one infinite eventually critical Sidon branch | **OPEN** | Neither finite tests nor the critical upper envelope alone proves this. |

Thus this note gives both a sharper positive global upper envelope and a
no-go.  It does **not** resolve Erdős Problem #1191 and makes no prize claim.

## 2. Notation and the exact local coefficient

Let

\[
 0=a_0<a_1<\cdots,
 \qquad h_0=1,
 \qquad h_i=a_i-a_{i-1}\quad(i\geq1),
 \qquad N_L=a_{L-1}+1.
\tag{1}
\]

For a state with `L` marks, put

\[
 z_L(i)=z(i/L),\qquad z(u)=\binom{u(1-u)}u,
 \qquad K^{(L)}_{ij}
 =(z_L(j)-z_L(i))(z_L(j)-z_L(i))^{\mathsf T}.
\tag{2}
\]

At the update `m -> 2m`, identity (14) is

\[
 \frac{Q_m}{N_{2m}}
 =\frac1{N_{2m}^2}
   \sum_{\substack{i<j<2m\\j\geq m}}h_ih_jK^{(2m)}_{ij}
 -\frac{N_{2m}-N_m}{N_mN_{2m}^2}
   \sum_{i<j<m}h_ih_jK^{(2m)}_{ij}.
\tag{3}
\]

Fix one index pair `p=(i,j)`.  It is born at the unique dyadic epoch

\[
 b=2^{\lfloor\log_2j\rfloor},\qquad b\leq j<2b.
\tag{4}
\]

Write `L_t=2^(t+1)b`, `n_t=N_(L_t)`, and, through the chosen finite
horizon,

\[
 K_t=K^{(L_t)}_{ij},\qquad
 \phi_t=\langle H,K_t\rangle,\qquad
 e_t=\langle E,K_t\rangle.
\tag{5}
\]

The factor `h_i h_j` is suppressed until the global regrouping.  Reading
(3) at the birth epoch and every later epoch gives its exact coefficient

\[
 \boxed{
 c_p(T)=\frac{\phi_0}{n_0^2}
 -\sum_{t=1}^{T}
 \frac{n_t-n_{t-1}}{n_{t-1}n_t^2}\,\phi_t.}
\tag{6}
\]

There is no missing factor of `N`, `G`, or `N'`: the birth coefficient is
`1/n_0^2`, and at age `t` the old-pair coefficient is exactly
`-(n_t-n_(t-1))/(n_(t-1)n_t^2)`.

## 3. Constant `H`: a positive telescope and the half-retention theorem

The exact identities

\[
 z(u/2)=Bz(u),\qquad
 B=\begin{pmatrix}1/4&1/4\\0&1/2\end{pmatrix},\qquad
 H-B^{\mathsf T}HB=E
\tag{7}
\]

give

\[
 K_{t+1}=BK_tB^{\mathsf T},
 \qquad \phi_t-\phi_{t+1}=e_t\geq0.
\tag{8}
\]

Set

\[
 \alpha_t=\frac{n_t-n_{t-1}}{n_{t-1}n_t^2},
 \qquad
 w_r=\frac1{n_0^2}-\sum_{t=1}^{r}\alpha_t,
 \qquad w_0=\frac1{n_0^2}.
\tag{9}
\]

### Theorem 1 (arbitrary increasing moduli)

For every strictly increasing positive sequence `n_0<...<n_T`,

\[
 \boxed{
 c_p(T)=\sum_{r=0}^{T-1}w_re_r+w_T\phi_T.}
\tag{10}
\]

All terms on the right are nonnegative.  Moreover,

\[
 \boxed{
 \frac12\frac{\phi_0}{n_0^2}
 \leq c_p(T)\leq\frac{\phi_0}{n_0^2}.}
\tag{11}
\]

If every future modulus ratio satisfies

\[
 \rho_t:=\frac{n_{t-1}}{n_t}\leq r\leq1,
\tag{12}
\]

then the sharper bound is

\[
 \boxed{
 c_p(T)\geq\frac1{1+r}\frac{\phi_0}{n_0^2}.}
\tag{13}
\]

#### Proof

The exact factorization

\[
 \alpha_t
 =\frac{\rho_t}{1+\rho_t}
 \left(\frac1{n_{t-1}^2}-\frac1{n_t^2}\right)
\tag{14}
\]

shows that `alpha_t>=0`.  Since `rho_t/(1+rho_t)<=1/2`, telescoping the
reciprocal squares gives

\[
 0\leq\sum_{t=1}^{r}\alpha_t
 \leq\frac12\left(\frac1{n_0^2}-\frac1{n_r^2}\right)
 <\frac1{2n_0^2}.
\tag{15}
\]

Thus every `w_r` lies between `1/(2n_0^2)` and `1/n_0^2`.  Expanding
`phi_t=e_t+...+e_(T-1)+phi_T` in (6) gives (10), and comparison with
`phi_0=e_0+...+e_(T-1)+phi_T` gives (11).  Under (12), replace `1/2` in
(15) by `r/(1+r)` to obtain (13).  `square`

The terminal correction retained by (15) is actually positive:

\[
 w_r\geq
 \frac1{(1+r)n_0^2}+\frac{r}{(1+r)n_r^2}.
\tag{16}
\]

## 4. Global theorem and the sharper unique-difference envelope

Let the terminal number of marks be a power of two and sum (3) over every
complete dyadic update.  Define the raw birth budget

\[
 \mathcal B_H(M)=
 \sum_{\substack{0\leq i<j<M}}
 h_ih_j\,
 \frac{\langle H,K^{(2b(j))}_{ij}\rangle}{N_{2b(j)}^2}.
\tag{17}
\]

Each pair occurs positively exactly once, at its birth, and negatively at
every later update.  Summing Theorem 1 pair by pair proves

\[
 \boxed{
 \frac12\mathcal B_H(M)
 \leq
 \sum_{\substack{m<M\\m\ \mathrm{dyadic}}}
 \left\langle H,\frac{Q_m}{N_{2m}}\right\rangle
 \leq\mathcal B_H(M).}
\tag{18}
\]

This identity and comparison are algebraic; they do not require the Sidon
condition.  On a Golomb ruler, they have an additional arithmetic meaning.
For `1<=i<j`, set

\[
 D_{i,j}=\sum_{k=i}^{j}h_k=a_j-a_{i-1}.
\tag{19}
\]

Then `h_i h_j<=D_(i,j)^2/4`.  The right endpoint `j` lies in exactly one
newborn block, so all endpoint pairs in the following sum are globally
disjoint; Golomb uniqueness makes their numerical differences distinct:

\[
 \boxed{
 \begin{aligned}
 \mathcal B_H(M)\leq{}&
 \frac14\sum_{\substack{m<M\\m\ \mathrm{dyadic}}}
 \frac1{N_{2m}^2}
 \sum_{\substack{1\leq i<j<2m\\j\geq m}}
 \Phi^{(2m)}_{ij}D_{i,j}^2\\
 &+\sum_{\substack{m<M\\m\ \mathrm{dyadic}}}
 \frac1{N_{2m}^2}\sum_{j=m}^{2m-1}h_j\Phi^{(2m)}_{0j}.
 \end{aligned}}
\tag{20}
\]

The last row is the familiar artificial `h_0=1` boundary.  Using
`Phi_(0j)<=23/105`, `sum_(j in S)h_j<=N_(2m)`, and the Golomb lower bound
`N_(2m)>=m^2`, its entire infinite dyadic sum is at most

\[
 \frac{23}{105}\sum_{k\geq0}4^{-k}=\frac{92}{315}.
\tag{21}
\]

Equation (20) sharpens the earlier positive envelope (25) on within-shell
pairs: its coefficient is `1/(4N_(2m)^2)`, rather than
`1/(4G_mN_(2m))`.  Cross-pair coefficients agree.  The improvement comes
directly from retaining the short identity (14) before discarding its old
negative part.

However, (18) is also a no-go.  Cross-epoch old-pair cancellation can reduce
the raw birth budget by at most a factor two.  If `M_J=2^(J+1)` and
`mathcal B_H[J]:=mathcal B_H(M_J)` denotes the budget through dyadic epoch
`m_J=2^J`, then consequently

\[
 \sum_{j\leq J}\left\langle H,Q_{2^j}/N_{2^{j+1}}\right\rangle
 =o(\log J)
 \quad\Longleftrightarrow\quad
 \mathcal B_H[J]=o(\log J)
\tag{22}
\]

up to the harmless choice of dyadic starting scale and the fixed factor two.
Any successful proof must therefore control the positive birth budget itself
using infinite-history Sidon arithmetic.  It cannot obtain the missing
little-`o` merely by waiting for the old negative terms in (14).

## 5. Exact finite-horizon adjoints: cancellation is persistence

The constant matrix `H` is only a uniform majorant.  The exact adjoint has a
different telescope.

Consider the closed list of states `0,...,T`, including the terminal state in
the observable sum.  Set

\[
 A_T=E,\qquad
 A_r=E+\frac{n_r}{n_{r+1}}B^{\mathsf T}A_{r+1}B
 \quad(0\leq r<T).
\tag{23}
\]

This is exactly the canonical convention
`H_(J+1)=0`, `H_j=E+rho_j B^T H_(j+1)B`, with the extra zero state omitted:
the last displayed state consequently carries weight `E`.  If the last
listed adjoint is instead set to zero, that state is not part of the
observable sum.  Confusing these two conventions creates an apparent
one-term discrepancy.

Pull every matrix to the pair's birth grid:

\[
 C_r=\frac{(B^{\mathsf T})^rA_rB^r}{n_r},
 \qquad E_r=(B^{\mathsf T})^rEB^r.
\tag{24}
\]

The recurrence (23) becomes

\[
 \boxed{C_r=\frac{E_r}{n_r}+C_{r+1}.}
\tag{25}
\]

The pair's birth matrix coefficient is `C_0/n_0`.  Its old subtraction at
the next update is

\[
 \left(\frac1{n_r}-\frac1{n_{r+1}}\right)C_{r+1}.
\tag{26}
\]

Using (25) successively yields the exact matrix identity

\[
 \boxed{
 \frac{C_0}{n_0}
 -\sum_{r=0}^{T-1}
 \left(\frac1{n_r}-\frac1{n_{r+1}}\right)C_{r+1}
 =\sum_{r=0}^{T}\frac{E_r}{n_r^2}.}
\tag{27}
\]

Pairing (27) with the birth-grid rank-one matrix and restoring `h_i h_j`
shows:

> Under exact finite-horizon adjoints, the positive birth term plus every
> later negative old-pair term equals the sum of the same pair's positive
> `E`-energy in every future state.

Thus the exact cancellation reconstructs persistence in the original state
sum.  It is not a new upper budget.

## 6. Constant ratios and the critical `rho=1/4` regime

For `0<=q<=1`, define

\[
 H_q=E+qB^{\mathsf T}H_qB.
\tag{28}
\]

Exact solution gives

\[
 H_q=
 \begin{pmatrix}
 \dfrac{16}{16-q}&
 \dfrac{8q}{(16-q)(8-q)}\\[2mm]
 \dfrac{8q}{(16-q)(8-q)}&
 \dfrac{q\left(\frac14\frac{16}{16-q}
 +\frac{8q}{(16-q)(8-q)}\right)}{4-q}
 \end{pmatrix}.
\tag{29}
\]

Suppose `n_r/n_(r+1)=rho` exactly.  Three matrices must not be conflated.

1. The infinite-horizon exact adjoint at one state is `H_rho`.
2. The positive future tail of one born pair is

   \[
   \frac1{n_0^2}\sum_{r\geq0}\rho^{2r}
   (B^{\mathsf T})^rEB^r
   =\frac{H_{\rho^2}}{n_0^2}.
   \tag{30}
   \]

3. The constant-`H` birth term after every old-pair subtraction has effective
   kernel

   \[
   \boxed{
   F_\rho=\frac{H+\rho H_{\rho^2}}{1+\rho}.}
   \tag{31}
   \]

In particular,

\[
 \frac1{1+\rho}H\preceq F_\rho\preceq H.
\tag{32}
\]

At the regular critical ratio `rho=1/4`,

\[
 H_{1/4}=
 \begin{pmatrix}64/63&32/1953\\32/1953&176/9765\end{pmatrix},
\qquad
 H_{1/16}=
 \begin{pmatrix}256/255&128/32385\\128/32385&2752/680085\end{pmatrix},
\tag{33}
\]

and

\[
 F_{1/4}=\frac45H+\frac15H_{1/16}
 =\begin{pmatrix}
 448/425&23328/377825\\
 23328/377825&313648/3400425
 \end{pmatrix}
 \succeq\frac45H.
\tag{34}
\]

Because

\[
 B^r=
 \begin{pmatrix}
 4^{-r}&2^{-r}-4^{-r}\\0&2^{-r}
 \end{pmatrix},
\tag{35}
\]

the transported pair kernel is `O(4^-r)`.  At constant ratio `rho`, both
the old-subtraction tail and the exact positive state tail therefore decay
as `O((rho^2/4)^r)`.  At `rho=1/4` this is `O(64^-r)`.

If an actual branch satisfies the additional regularity

\[
 N_m/N_{2m}\longrightarrow1/4,
\tag{36}
\]

then late-born pairs retain at least `4/5-o(1)` of their constant-`H` birth
charge.  An eventual upper cap `N_m<=C m^2 log m` by itself does **not** imply
(36); no ratio limit is inferred from the critical cap alone.

## 7. Exact verification

`wave8_pair_telescope.py` implements (3), (6), (10), (18), (23), (27),
(29), and (31) with `fractions.Fraction`.  The tests independently compare
the pair regrouping with the matrix update and compare the exact-adjoint
innovation sum with the direct state-functional sum.

For the perfect four-mark ruler `(0,1,4,6)`, pair `(0,1)` gives

\[
 \text{birth}=\frac1{35},\qquad
 \text{later negative}=\frac{29}{10976},\qquad
 \text{net}=\frac{1423}{54880},
\tag{37}
\]

so its retention is `1423/1568`.  Under exact adjoints, the same pair gives

\[
 \text{signed innovation coefficient}
 =\text{positive state tail}=\frac{205}{12544}.
\tag{38}
\]

Summing all six pairs gives

\[
 \sum I_m=\frac{2253}{54880},\qquad
 \mathcal B_H=\frac{1199}{27440},\qquad
 \text{exact-adjoint sum}=\frac5{224}.
\tag{39}
\]

The full exact audits also pass on the independent 64-mark fixture and the
hash-authenticated 128-mark Wave 6 fixture:

| fixture | pairs | fixed-`H` sum | raw birth sum | minimum pair retention | exact-adjoint/state sum |
|---|---:|---:|---:|---:|---:|
| 64 marks | 2,016 | 0.0631358057 | 0.0664819248 | `286851781/355511025` | 0.0336808584 |
| 128 marks | 8,128 | 0.0766108062 | 0.0816844471 | `15576406729/18573056089` | 0.0439860190 |

The decimals in the table are for readability only; every asserted equality
and inequality is tested as an exact rational identity.

Reproduction from the package root:

```bash
uv run --with pytest pytest -q -p no:cacheprovider \
  core_workspace/endpoint_variance/test_wave8_pair_telescope.py
uvx ruff check \
  core_workspace/endpoint_variance/wave8_pair_telescope.py \
  core_workspace/endpoint_variance/test_wave8_pair_telescope.py
```

Observed result: `8 passed`; Ruff reports `All checks passed!`.

## 8. Consequence for the main problem

The pair telescope removes one ambiguity from P13:

- keeping the negative old-pair terms does improve the positive birth upper
  envelope, including the within-shell normalization;
- the improvement is bounded by a universal factor two, and by only
  `5/4+o(1)` under the regular critical ratio;
- exact horizon adjoints turn the same algebra into the positive state tail,
  not into a disappearing debt.

Therefore the surviving target is precisely a theorem forcing
`mathcal B_H(J)=o(log J)` on one infinite eventually critical Sidon branch,
or another genuinely global argument that bypasses this innovation route.
Finite survival, a finite critical ruler, or the upper critical envelope
alone does not establish that statement.
