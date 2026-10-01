# Erdős #1191 U4-F — 最初の数学的攻撃の補足
日付: 2026-09-09
基礎資料: 添付「Erdős Problem #1191 Q1 — Critical-path mathematical audit」。
以下は定義から導く初等的簡約と攻撃方針。原Q1の証明ではない。
今回、下流の原研究ファイル一式やLean buildを再検証したものではない。

## 1. 記号
S(M,T)=Σ_{b=2}^{T-1} sqrt(P_b^core(M,T))/b。
価格は凍結されたgenuine partial component price u_r^[M]を使う。

## 2. 固定Mでのoutput horizon単調性
T≤T'≤MならR_core(M,T)⊆R_core(M,T')。
既存recordの価格u_r^[M]はTに依存せず、各項は非負。
したがって各既存cutでP_b^core(M,T)≤P_b^core(M,T')。
新しいcutの寄与も非負であるからS(M,T)≤S(M,T')。

従って、凍結命題を証明することは、同じC,m0、同じ履歴量化の下で
S(M,M)≤K(C,m0)を全Mについて証明することと同値。
ただし無限sourceへの接続では「固定Tの後にM→∞」を保持する。
単調性は、有限価格をterminal-reset価格へ変更してよいことを意味しない。

## 3. 同じ無限または有限履歴の延長に沿う単調性
M'≥Mで最初のM点を保った延長なら、古いrecordの端点・core条件は不変。
u_r^[M']≥u_r^[M]であり、新recordも非負なのでS(M',M')≥S(M,M)。
これは異なる履歴を比較する定理ではない。

## 4. 一様な初等上界とその限界
固定cut bに寄与する正sourceラベルはF_(b-1)に入る。
u_r^[M]≤alpha_b/H_b²、および
Σ_{unordered distinct d,e∈F_(b-1)} de ≤ (Σ_d d)²/2
を使うと
P_b^core(M,T) ≤ (b-2)²/(8b²) ≤ 1/8。
従ってS(M,T)≤(1/√8)Σ_{b=2}^{T-1}1/b=O(log T)。
これはM,Tから独立なKを与えず、凍結命題を解決しない。

## 5. 正確なdyadic massと十分条件
j≥1についてB_j(M)={b:2^j≤b<min(2^(j+1),M)}とし、
I_j(M)=Σ_{b∈B_j}P_b^core(M,M)/b、
W_j(M)=Σ_{b∈B_j}1/b、
Q_j(M)=Σ_{b∈B_j}sqrt(P_b^core(M,M))/bと置く。

有限和の交換から
I_j(M)=Σ_{h∈R_core(M,M)} u_r^[M] d e ell_j(c,i;M)、
ell_j(c,i;M)=Σ_{b∈B_j, c<b<i}1/b
が正確に成立する。同じrecordを異なる物理予算へ複製しない。

加重Cauchyから
Q_j(M)≤sqrt(W_j(M) I_j(M))、
W_j(M)≤log 2+2^(-j)。
従って
S(M,M)≤Σ_j sqrt((log 2+2^(-j)) I_j(M))。

例えば、全てのcap履歴に対し
I_j(M)≤A(C,m0)/(1+j)^(2+eta), eta>0
を証明できれば凍結命題の十分条件になる。
このrateは未証明の攻撃候補であり、必要条件ではない。
rateが偽でも凍結命題が偽とは限らない。
ΣI_j<∞だけでは不十分である。I_j=1/j²ならΣI_jは収束するが
Σsqrt(I_j)=Σ1/jは発散する。

## 6. エラーと成功の判定
- 素のO(log M)上界: 確認用baseline。新しい一様上界ではない。
- より強いrateへの有限反例: そのrateを棄却。Q1反証ではない。
- 固定C,m0の下でprofileが非有界になる族の証明: 凍結命題の否定。
- 凍結命題の数学的証明: 下流接続と形式化へ進む。まだ最終Lean完了ではない。
- 原Q1の数学的閉包と固定環境の最終Lean検証: master goalの受理対象。

## 7. M=12基準例の今回の独立有限再計算
点列: (1,2,4,8,13,21,31,45,66,81,97,123)。
core数: 20。
P7  = 42967789/23906323584000
P8  = 16592136787/1577817356544000
P9  = 24872453269/2524507770470400
P10 = 993/152181458
その他のcutは0。
S(12,12) ≈ 0.0012010780282121734719572456912311897844。

整数の差辞書・有理数価格・有理数log区間でcoreのstrict条件を再確認した。
logはn=2^s q、1≤q<2、z=(q-1)/(q+1)として
log q=2Σ_{j≥0}z^(2j+1)/(2j+1)
の40項と残差上界2z^81/[81(1-z²)]を使用。
全比較が決まりUNKNOWN=0。4つの有理数係数は添付の値と完全一致。
表示した平方根の和のみDecimalによる近似。
この一つのfixtureの再計算であり、5377例の再実行、Gate 0全体、
一様定理、Lean証明を検証したという意味ではない。

## 8. 手順を支える公式運用資料
Codex goal: https://developers.openai.com/codex/use-cases/follow-goals
Codex commands: https://developers.openai.com/codex/cli/slash-commands
Codex subagents: https://developers.openai.com/codex/multi-agent
Codex MCP: https://developers.openai.com/codex/mcp/
Lean Comparator: https://github.com/leanprover/comparator
上記は運用資料であり、本補足の数学的主張の証明根拠ではない。
