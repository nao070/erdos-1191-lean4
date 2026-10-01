# Q1 の原定式化と整数定式化の同値証明

ここで証明するのは**定式化の同値性**であり、Q1 の肯定・否定ではない。
Lean の主宣言は `Erdos1191Q1.original_iff_integerSquared` である。

A を任意の自然数の集合とし、

\[
C_A(x)=\#\{a\in A:1\le a\le x\},\qquad
F_A(x)=C_A(x)\sqrt{\log x/x}
\]

とする。漸近議論では常に \(x\ge2\) を用いる。正整数 Sidon 集合という仮定は、
この同値証明自体には不要である。

## 数え上げと極限の意味

自然数 a が \(1\le a\) を満たすとき、実数 x の符号にかかわらず

\[
a\le\lfloor x\rfloor_{\mathbb N}\iff a\le x
\]

である。ただし非正の x の自然数床は 0 とする。従って、有限集合
\(A\cap[1,\lfloor x\rfloor_{\mathbb N}]\) による実装は上の数え上げと完全に一致する。
これは `mem_countingSet_real` が全実数 x について確認する。

下極限は拡張実数で取り、\(+\infty\) の場合を保持する。実数型の条件付き完備性による
上限の全域化で、上に有界でない集合の上限を 0 と読むことはしない。
\(F_A(x)\ge0\) より、

\[
\liminf_{x\to\infty}F_A(x)=0
\iff
\forall\eta>0\ \forall B\in\mathbb R\ \exists x\ge B:\ F_A(x)<\eta.
\]

右から左では、非負性が下極限の下界 0 を与える。任意の正の拡張実数 y に対して
\(0<\eta<y\) となる実数 \(\eta\) を選ぶと、任意に大きい x で \(F_A(x)<y\) なので
下極限は y 以下である。従って 0 以下でもある。左から右は、下極限より大きい
任意の \(\eta\) 未満の値が任意に遅く現れるという下極限の性質による。
Lean 宣言は `original_iff_frequently`。

## 平方根を除く

\(x\ge2\) なら \(\log x/x\ge0\) であるから、

\[
F_A(x)^2=C_A(x)^2\log x/x.
\]

任意の \(\varepsilon>0\) に対して上の頻出条件を
\(\eta=\sqrt\varepsilon\) に適用し、x を \(\max(B,2)\) 以後に取れば
\(C_A(x)^2\log x<\varepsilon x\) を得る。逆に任意の \(\eta>0\) に対して
\(\varepsilon=\eta^2\) を用いれば、非負性から \(F_A(x)<\eta\) が従う。
Lean 宣言は `normalized_sq` と `original_iff_realSquared`。

## 実数 cutoff から整数 cutoff へ

任意の \(\varepsilon>0\) と \(M\in\mathbb N\) を固定する。
実数の平方条件を \(\varepsilon/2\) に適用し、

\[
x\ge\max(M,2),\qquad C_A(x)^2\log x<(\varepsilon/2)x
\]

を満たす x を取る。\(N=\lfloor x\rfloor_{\mathbb N}\) とおくと、

\[
N\ge\max(M,2),\quad C_A(N)=C_A(x),\quad
\log N\le\log x,\quad x<N+1\le2N.
\]

よって

\[
C_A(N)^2\log N
\le C_A(x)^2\log x
<(\varepsilon/2)x
<\varepsilon N.
\]

## 整数 cutoff から実数 cutoff へ

任意の \(\varepsilon>0\) と実数 B に対し、整数条件で
\(M=\lceil B\rceil_{\mathbb N}\) と取る。得られる整数 N は
\(N\ge\max(B,2)\) を実数の順序でも満たし、実数 cutoff として同じ不等式を満たす。
この両方向が `realSquared_iff_integerSquared` であり、前節との合成が全同値である。

## 否定形と入力条件の非空性

整数条件の量化を古典論理で否定すると、ちょうど

\[
\exists\varepsilon>0\ \exists M\ge2\ \forall N\ge M:\
\varepsilon N\le C_A(N)^2\log N
\]

となる。従って Q1 の否定には、これを満たす**実在する正整数の無限 Sidon 集合**が
必要十分である。Lean 宣言は `not_original_iff` と `not_q1_iff`。
この同値性だけでは、そのような集合の存在も非存在も証明していない。

入力条件は同時に実現できる。\(A=\{3^n:n\in\mathbb N\}\) は正で無限である。
\(i<j\) なら \(2\cdot3^i<3^j\)。従って
\(i\le j,\ k\le l\) と並べた和
\(3^i+3^j=3^k+3^l\) では、\(j<l\) も \(l<j\) もこの不等式に反する。
ゆえに \(j=l\)、消去して \(i=k\) である。重複する添字を含めて unordered sums
は一意となる。Lean 宣言 `admissible_exists` がこの例を確認する。
