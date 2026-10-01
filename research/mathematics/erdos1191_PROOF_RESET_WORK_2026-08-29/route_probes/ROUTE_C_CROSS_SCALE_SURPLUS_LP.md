# Route C: exact 14-channel cross-scale surplus LP

Date: 2026-08-30  
Status: `EXACT_FIXED_FIXTURE_SHARING_SAVING_CROSS_ROOTS_STRICTLY_EXCLUDED_DEMAND_EQUALITY_FALSE_C058_OPEN`

This note solves one finite rational LP on the fixed 16-mark Golomb fixture.
It finds a strict saving relative to optimizing the two same-scale covers
separately, but the saving is **not** produced by a cross-scale root.  An exact
dual gives every cross-scale root positive reduced cost.  The optimal price is
also strictly above integrated signed demand.

The constraint here covers the **sum** of the two epoch demands on each common
cell.  That is weaker than requiring a separate cover inequality for each
epoch.  Consequently this fixture is a diagnostic for surplus sharing, not a
paid common-history ledger and not a proof of C058, Question 1, or Question 2.

## 1. Fixed normalized model

Let

\[
 a_k=k(k+100),\qquad 0\le k\le15.
\]

Use the five `n=4` channels at width `T=200` and the nine `n=8` channels at
width `S=800`:

\[
 \phi_{T,k}(x)={g_T(x-a_{3+k})\over\sqrt{2T}},\quad0\le k\le4,
 \qquad
 \phi_{S,k}(x)={g_S(x-a_{7+k})\over\sqrt{2S}},\quad0\le k\le8.
\]

Here `sqrt(2T)=20` and `sqrt(2S)=40`, so every common-cell state is rational.
The two channels based at `a_7=749` remain distinct; one belongs to each scale.
There are 14 channels, 41 distinct finite events, 40 positive-length cells,
two zero exterior cells, and

\[
 {14\choose2}=91
\]

graph-root columns, of which `5*9=45` are cross-scale.

On a common cell `c`, write the channel vector as `z_c`.  The target is

\[
 \boxed{
 D_c=z_{c,0:5}^{\mathsf T}M_4z_{c,0:5}
     +z_{c,5:14}^{\mathsf T}M_8z_{c,5:14}.}
 \tag{1}
\]

Thus (1) is precisely

\[
 {v_{4,c}^{\mathsf T}M_4v_{4,c}\over400}
 +{v_{8,c}^{\mathsf T}M_8v_{8,c}\over1600}.
\]

For root `e=(i,j)`, put

\[
 R_{c,e}=(z_{c,i}-z_{c,j})^2,
 \qquad
 p_e=\sum_c |c|R_{c,e}
     =\|\phi_i-\phi_j\|_2^2.
\]

Every `p_e` is checked both by complete cell summation and by the oriented
mixed-Haar formula

\[
 p_{ij}=2-{A_{t_i,t_j}(b_j-b_i)\over\sqrt{t_it_j}}.
 \tag{2}
\]

The root LP and its cell dual are

\[
 \min_{w\ge0}\sum_ep_ew_e,
 \qquad
 \sum_eR_{c,e}w_e\ge D_c,
 \tag{3}
\]

\[
 \max_{y\ge0}\sum_cy_cD_c,
 \qquad
 \sum_cy_cR_{c,e}\le p_e.
 \tag{4}
\]

The certificate also appends the normalized aggregate columns `J4`, `J8`, and
`J_all`, each with its exact integrated price.  None is free.

## 2. Exact optimum

One exact primal optimum has the following positive root weights; all omitted
weights, including all 45 cross-scale roots, are zero.

| root | weight |
|---|---:|
| `(0,1)` | `13/30720` |
| `(0,2)` | `3971/153600` |
| `(2,4)` | `191/9600` |
| `(3,4)` | `13/7680` |
| `(5,6)` | `49/640` |
| `(6,7)` | `131/2560` |
| `(11,13)` | `131/2560` |
| `(12,13)` | `13/512` |

An exact dual optimum is supported on eight cells:

| cell | dual weight |
|---|---:|
| `[525,616)` | `698/5` |
| `[636,709)` | `1426/15` |
| `[749,816)` | `418/5` |
| `[864,925)` | `2186/15` |
| `[1596,1664)` | `3086/45` |
| `[1664,1725)` | `2086/15` |
| `[2349,2396)` | `381/2` |
| `[2396,2464)` | `12743/90` |

Every one of the 40 primal cell inequalities and every one of the 91 dual root
constraints is replayed with `Fraction`.  Complementary slackness holds and
the exact gap is zero:

\[
 \boxed{E^*={1555757\over6144000}.}
 \tag{5}
\]

The integrated signed demand is

\[
 \mathcal D={63\over640}+{361\over5120}={173\over1024},
\]

so equality with demand is impossible in this class:

\[
 \boxed{E^*-\mathcal D={517757\over6144000}>0.}
 \tag{6}
\]

The separate optima at the correct widths are

\[
 E_{4,200}^{\rm sep}={29\over200},
 \qquad
 E_{8,800}^{\rm sep}={59841\over512000}.
\]

Therefore the common-cell sum-cover has the strict saving

\[
 \boxed{
 E_{4,200}^{\rm sep}+E_{8,800}^{\rm sep}-E^*
 ={10643\over1228800}>0.}
 \tag{7}
\]

## 3. What causes the saving

The saving in (7) is surplus sharing, not a positive cross edge.  On the tight
cell `[749,816)`, the exact decomposition is

\[
 D_{4,200}={1\over3200},\qquad D_{8,800}=0,
\]

\[
 P_{4,200}={271\over1024000},\qquad
 P_{8,800}={49\over1024000},\qquad P_{\rm cross}=0.
\]

The two within-scale corrections sum exactly to `1/3200`.  In other words,
an `S=800` correction row that is surplus relative to its own zero demand pays
the small deficit in the `T=200` row under the combined inequality (3).

Moreover, the exact dual is **strict** on all 45 cross roots.  The smallest
margin occurs at `(2,6)`:

\[
 p_{2,6}={861\over400},\qquad
 \text{dual load}={7811\over4000},\qquad
 \boxed{\text{margin}={799\over4000}>0.}
\]

Complementary slackness therefore forces every cross-root coefficient to be
zero in every optimum exposed by this dual.  Adding the exactly priced
aggregate columns also changes nothing:

| column | physical cost | dual load | margin |
|---|---:|---:|---:|
| `J4` | `3` | `107/150` | `343/150` |
| `J8` | `688/25` | `8441/1000` | `19079/1000` |
| `J_all` | `702/25` | `25277/3000` | `58963/3000` |

All three optimal aggregate coefficients are zero.

## 4. Exact conclusion and boundary

This fixture proves only the following:

1. A common-cell cover of the **sum** of the `n=4,T=200` and `n=8,S=800`
   direct demands is cheaper than the sum of their separately optimized
   root covers.
2. The optimum remains strictly above integrated demand.
3. Genuine cross-scale roots and all explicitly priced aggregate columns are
   strictly inactive at the exact optimum.

It does **not** prove the same saving under separate epochwise inequalities.
It does not provide a common-history recurrence, an active-scale or terminal
rule, a phase-uniform bound, a singly owned payment source, C058, either Erdős
question, publication novelty, or a prize claim.  The 26-channel/four-demand
variant is not part of this certificate.

Replay with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v \
  ROUTE_C_CROSS_SCALE_SURPLUS_LP_test.py
PYTHONDONTWRITEBYTECODE=1 python3 \
  ROUTE_C_CROSS_SCALE_SURPLUS_LP_certificate.py \
  --verify ROUTE_C_CROSS_SCALE_SURPLUS_LP_certificate.json --self-check
```
