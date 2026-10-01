# A34 independent hand review: deferred deletion penalties

Date: 2026-09-09. Status: PASS for the fixed-cut identities and the
explicitly conditional genuine-price corollary below. No uniform
cross-cut charging estimate follows from these identities alone.

## One canonical deletion

Fix b, H=H_b and ell, and let
U_0={ell,...,H-1} minus Delta(first b points). Set phi(t)=1-t/H>0
on this universe. List eligible actual mixed labels c_i once each,
ordered first by the future endpoint's rank f_i, then by the past
endpoint's rank. Sidon difference uniqueness makes this a list with
no repeats, disjoint from the past difference bank. Thus each c_i
really belongs to U_{i-1}, where U_i=U_0 minus {c_1,...,c_i}.

Let N_i=card U_{i-1}, let r_i be c_i's 1-based ascending rank in
U_{i-1}, and write the corresponding nonincreasing positive weights
w_1,...,w_{N_i}. For nonnegative integer h put

    p_i(h)=F_{U_{i-1}}(h)-F_{U_i}(h).

The exact formula is

    p_i(h)=0                           if h<r_i,
    p_i(h)=w_{r_i}-w_{h+1}              if h>=r_i,

where w_{h+1}=0 whenever h>=N_i. If h<N_i and the deleted label is
selected, the new optimum replaces it by the old (h+1)-st label.
If h>=N_i, both optima include all available labels, and the loss
is exactly phi(c_i). This proof includes h=0, deletion at the final
rank, and the boundary h=N_i.

Consequently 0<=p_i(h)<=phi(c_i), p_i is nondecreasing in h, and
p_i(h)=phi(c_i) whenever h>=N_i. N_i and r_i refer to the sequential
pre-deletion bank, not the bank before the entire batch of labels
with equal future birth. Each same-birth deletion must use its own
updated bank.

## Simultaneous capacity growth and new deletions

At future horizon v let d_v count deleted labels with f_i<=v,
h_v=binom(v-b,2), and U_v denote the bank after those deletions.
Here U_v uses a horizon subscript, whereas U_i above uses a deletion
index. Telescoping at the same capacity gives the exact identity

    F_{U_0}(h_v)-F_{U_v}(h_v)
        = sum_{i<=d_v} p_i(h_v).

For v to v+1, put m=v-b, h=h_v, h'=h+m. Define baseline capacity
gain A_0=F_{U_0}(h')-F_{U_0}(h), actual capacity gain
A=F_{U_v}(h')-F_{U_v}(h), and new deletion loss
R=F_{U_v}(h')-F_{U_{v+1}}(h'). Then

    g=A_0-A=sum_{i<=d_v}[p_i(h')-p_i(h)]>=0,
    R=sum_{d_v<i<=d_{v+1}}p_i(h')>=0,
    Delta F_joint=A_0-g-R.

If the actual future kernel increment is J, the deficit E=F_joint-L
satisfies exactly

    Delta E=A_0-g-R-J=A-R-J.

This matches A32's exact finite checks. The total loss from the fixed
baseline has increment g+R>=0, but that fact alone does not imply
monotonicity of E, since the new actual kernel J must also be paid.
An immediate loss R=0 can therefore coexist with a positive mixed
label weight; its penalty may grow at later capacities. A finite
horizon need not reach the rank or full-payment threshold, so eventual
full payment must not be asserted without an explicit condition.

## Genuine component prices and a conditional lower bound

For both horizons retain v_k=min(k,T), h_k=binom(v_k-b,2), and
lambda_k=kappa_k/H_k^2. Finite sums may be rearranged exactly:

    sum_{k=b+1}^M lambda_k
       [F_{U_0}(h_k)-F_{U_{v_k}}(h_k)]
      = sum_{i:f_i<=T} sum_{k=f_i}^M lambda_k p_i(h_k).

For k>T the label catalog and capacity are frozen at T while genuine
prices continue through M. In particular alpha_{M+1} is not replaced
by zero and no terminal component is altered.

For one eligible label define

    d_i=min{m>=0:binom(m,2)>=N_i}, k_i=b+d_i.

Assume explicitly T>=k_i and f_i<=T<=M. Put r_i^*=max(f_i,k_i),
so r_i^*<=T. For every k>=r_i^*, min(k,T)-b>=d_i and hence
h_k>=N_i. Therefore p_i(h_k)=phi(c_i), giving

    Pi_i=sum_{k=f_i}^M lambda_k p_i(h_k)
       >=phi(c_i) sum_{k=r_i^*}^M lambda_k
       =phi(c_i) u_{r_i^*}^{[M]}.

Only preceding nonnegative penalties were discarded. The auxiliary
index r_i^* is a component threshold; it does not change any original
physical output rank. Without T>=k_i this full-tail bound has not
been proved and must not be used. Empty initial banks produce no
eligible labels, so no exceptional nonexistent deletion is needed.

## A simultaneous actual-prefix threshold and the near connection

For b>=8 put H=H_b and J_b=ceil(4 sqrt(H)). Every actual eligible
mixed label c=a_f-a_p<H with p<=b satisfies

    H_f=c+H_p<2H.

Integer Sidon packing H_f>=f(f-1)/2 gives
f<1+2sqrt(H)<=J_b. Thus all eligible mixed labels in any given
actual horizon have birth at most J_b. Also H>=b(b-1)/2>=b^2/4,
so b<=2sqrt(H) and J_b-b>=2sqrt(H). Consequently

    binom(J_b-b,2)>=2H-sqrt(H)>=H>=N_i.

The quadratic is increasing on the relevant interval, and H>=1.
If explicitly T>=J_b (hence J_b<=M), every eligible mixed label
has appeared and every sequential deletion penalty has reached its
full phi weight by J_b. The eligible forbidden bank stays fixed
thereafter, including components k>T. This is conditional on the
given finite horizon containing J_b; it assumes no extension exists.

Suppose additionally b>=max(10,m0,C) and log b>=150C. The cut cap,
C<=b, and log(2b)<=b give H<=C b^2 log(2b)<=b^4. Since
J_b<=5sqrt(H) and J_b>=b>=m0, the cap at the actual rank J_b yields

    H_{J_b}<=25 C H log(10sqrt(H))
            <=75 C H log b
            <=(1/2)H(log b)^2 < H(log b)^2.

Here log(10sqrt(H))<=log 10+2log b<=3log b uses b>=10.
The cap at J_b is legitimate only together with T>=J_b<=M.
Monotonicity of the actual diameter gives H_k<=H_{J_b} for k<=J_b,
so all these components are in A33's p=2 near class. Thus, when
the stated size and horizon conditions hold, all mixed deletion
penalties at this cut become full before any far component appears.
This does not pay the remaining near component norm or compare
payments across different cuts. The short-horizon case T<J_b is
not covered by this simultaneous-threshold corollary.

## Logical scope and next missing estimate

All identities hold at one fixed cut. The same physical mixed
difference can be present at other cuts, where H, ell, the baseline
bank and deletion ranks differ. These repetitions cannot be charged
as independent budgets. Likewise repeated appearances at different
components carry the original genuine price decomposition, rather
than independent record copies.

A32 supplies actual finite evidence rejecting immediate full payment;
the present proof supplies the exact deferred alternative. It gives
no bound on summing those payments over cuts, no proof that a finite
T always reaches full payment, and no uniform U4-F or Q1 conclusion.
The remaining task is a common physical-record estimate for the
cross-cut weighted sum. No additional finite campaign or Lean build
was run for this review. Source/evidence hashes are in the companion
A32_A34_review_manifest.json.
