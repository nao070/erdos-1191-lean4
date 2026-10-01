# Erdős Problem #1191 に対する検証済み研究報告

**STATUS: UNRESOLVED_AT_HARD_LIMIT**

本調査では、提示された成功条件・監査基準、特に「有限計算を解決と見なさない」「liminf/limsup と全十分大きな \(x\) の量化を厳密に区別する」「ブロック構成では cross-scale difference collision を完全に検証する」という基準を採用した。fileciteturn0file0　一次文献と 2026 年の最新プレプリントまで検索し、独立の補題証明と有限計算による反証試験を行ったが、Q1・Q2 の完全決着に必要な最後の theorem-strength gap は残った。本実行環境は非同期の長時間自律研究を提供せず、単一応答内のウェブ探索にも実際の呼び出し上限があるため、ここで未解決状態として監査済み成果のみを返す。

## 最強の検証済み結果

最も重要な成果は、Q1・Q2 を \(a_n\) の成長に**正確に**変換し、両問題の論理関係を完全に整理したこと、および O'Bryant の separated-block pasting lemma に現れる二次的削除損失 \(\binom m2\) が、Sidon 性とブロック分離だけを仮定する限り**最悪の場合に厳密に鋭い**ことを証明したことである。

Erdős の 1980 年原論文では、\(B_2\)-sequence について

\[
\limsup_{n\to\infty}\frac{a_n}{n^2\log n}>0
\]

を述べた直後に、この limsup が \(\infty\) かを問い、さらに

\[
a_n<c_1n^2(\log n)^{c_2}
\]

を全 \(n\) で満たす \(B_2\)-sequence が存在するかを問い、「(5) と (6) から生じる問題を解決する」ことに \$1000 を提示している。したがって現代の Q1/Q2 は、原問題の二つの核心を正しく抽出している。citeturn9view0turn10view0

**正確な \(A(x)\)-\(a_n\) 変換。**　無限 Sidon 集合 \(A=\{a_1<a_2<\cdots\}\) に対して

\[
L(A):=\liminf_{x\to\infty}A(x)\sqrt{\frac{\log x}{x}},
\qquad
R(A):=\limsup_{n\to\infty}\frac{a_n}{n^2\log n}
\]

とおく。2026 年の O'Bryant の定理から \(R(A)\ge \log 2/2>0\) である。citeturn21view0 さらに、拡張実数として

\[
\boxed{
R(A)<\infty\quad\Longrightarrow\quad
L(A)^2=\frac{2}{R(A)}
}
\]

であり、

\[
\boxed{
L(A)=0
\quad\Longleftrightarrow\quad
R(A)=\infty.
}
\]

したがって Q1 は**完全に同値**な形で

\[
\boxed{
\forall A\text{ infinite Sidon},\qquad
\limsup_{n\to\infty}\frac{a_n}{n^2\log n}=\infty
}
\]

と書ける。

証明する。Sidon 性から最初の \(n\) 項の正の差

\[
a_j-a_i\qquad(1\le i<j\le n)
\]

は全て異なるので、

\[
\binom n2\le a_n-a_1<a_n.
\tag{1}
\]

一方、

\[
f(x)=\sqrt{\frac{\log x}{x}}
\]

は \(x>e\) で単調減少する。\(a_n\le x<a_{n+1}\) では \(A(x)=n\) だから、

\[
L(A)
=
\liminf_{n\to\infty}
n\sqrt{\frac{\log a_{n+1}}{a_{n+1}}}
=
\liminf_{n\to\infty}
n\sqrt{\frac{\log a_n}{a_n}},
\]

最後の等号は添字を一つずらした際の \((n-1)/n\to1\) による。したがって

\[
L(A)^2
=
\liminf_{n\to\infty}
\frac{n^2\log a_n}{a_n}.
\tag{2}
\]

ここで

\[
R_n:=\frac{a_n}{n^2\log n}.
\]

もし \(0<R(A)<\infty\) なら、(1) と \(a_n\le Cn^2\log n\) から

\[
\frac{\log a_n}{\log n}\longrightarrow2.
\]

従って

\[
\frac{n^2\log a_n}{a_n}
=
\frac{\log a_n/\log n}{R_n},
\]

なので

\[
L(A)^2
=
\frac{2}{\limsup R_n}
=
\frac{2}{R(A)}.
\tag{3}
\]

他方 \(R(A)=\infty\) なら \(R_{n_j}\to\infty\) となる部分列を取れる。この部分列では

\[
\frac{n_j^2\log a_{n_j}}{a_{n_j}}
=
\frac{
2+\dfrac{\log\log n_j}{\log n_j}
+\dfrac{\log R_{n_j}}{\log n_j}
}{
R_{n_j}
}
\longrightarrow0,
\]

なぜなら \(\log t/t\to0\) だからである。(2) より \(L(A)=0\)。逆向きは (3) から直ちに従う。これで量化を含めて同値性が証明された。

**Q2 の正確な列形式。**　固定 \(c>0\) について

\[
\liminf_{x\to\infty}
\frac{A(x)(\log x)^c}{\sqrt x}>0
\tag{4}
\]

であることと、

\[
\boxed{
a_n=O\!\left(n^2(\log n)^{2c}\right)
}
\tag{5}
\]

であることは同値である。従って

\[
\boxed{
\text{Q2}
\Longleftrightarrow
\exists \beta>0,\ \exists\text{ infinite Sidon }A:
\quad
a_n=O\!\left(n^2(\log n)^\beta\right).
}
\tag{6}
\]

これは Erdős の 1980 年の式 (6) と、有限個の初期項を定数に吸収する違いを除き同じ問題である。citeturn9view0turn10view0

実際、(4) から十分大きな \(n\) について

\[
n\ge \delta\frac{\sqrt{a_n}}{(\log a_n)^c},
\]

従って

\[
a_n\le \delta^{-2}n^2(\log a_n)^{2c}.
\tag{7}
\]

大きな \(y\) では \((\log y)^{2c}\le y^{1/2}\) なので、(7) はまず \(a_n=O(n^4)\)、従って \(\log a_n=O(\log n)\) を与える。これを (7) に戻せば (5) になる。

逆に \(a_n\le Kn^2(\log n)^\beta\) とし、\(n=A(x)\) とおけば

\[
a_n\le x<a_{n+1}
\le K(n+1)^2(\log(n+1))^\beta.
\]

また \(n\le x\) なので \(\log(n+1)\ll\log x\)。従って

\[
A(x)=n
\gg \frac{\sqrt x}{(\log x)^{\beta/2}},
\]

すなわち (4) が \(c=\beta/2\) で成立する。

ここから Q1/Q2 の論理関係は完全に決まる。

| 命題 | 厳密な帰結 |
|---|---|
| Q1 が偽 | ある \(A\) で \(L(A)>0\)。したがって Q2 は \(c=\tfrac12\) で真 |
| Q2 が \(c=\tfrac12\) で真 | \(L(A)>0\) なので Q1 は偽 |
| Q2 が偽 | Q1 は必ず真 |
| Q1 が真かつ Q2 が真 | 論理的には可能だが、Q2 の指数は \(c>\tfrac12\) でなければならない |

さらに O'Bryant は \(g=1\) について

\[
L(A)\le \frac{2}{\sqrt{\log2}}
\]

を証明しているので、Q2 の witness に \(c<1/2\) はあり得ない。実際、その上界を実現する部分列 \(x_j\) 上で

\[
\frac{A(x_j)(\log x_j)^c}{\sqrt{x_j}}
\ll(\log x_j)^{c-1/2}\to0.
\]

O'Bryant の同値な corollary は

\[
\limsup_{n\to\infty}\frac{a_n}{n^2\log n}
\ge\frac{\log2}{2}.
\]

定数まで正確に一致する。citeturn20view0turn21view0

## 厳密に残るギャップ

2026 年 7 月 26 日改訂の O'Bryant v3 は、任意の \(g\)-Golomb ruler に対し

\[
\liminf_{x\to\infty}
\frac{A(x)}{\sqrt{x/\log x}}
\le
\frac{2\sqrt g}{\sqrt{\log2}}
\]

を証明し、\(g=1\) が本問題の Sidon case である。証明は長さ \(N\) のブロック数 \(F_\ell\) の energy

\[
E=\sum_\ell F_\ell^2
\]

を、差の重複度から上から、weighted Cauchy から下から評価するものになっている。著者自身、この一段階の energy/Cauchy 論法は十分最適化したと考える一方、複数スケールでの平均、reverse martingale、entropy を改善源として明示している。citeturn21view0turn22view0

したがって universal side の残る証明義務は、単なる定数改善ではなく

\[
\boxed{
\forall C>0,\ \forall\text{ infinite Sidon }A,\ 
\exists^\infty n:\quad
a_n>Cn^2\log n
}
\tag{8}
\]

を示すこと、すなわち固定定数を**任意に大きくする multiscale gain** を得ることである。

construction side では、Cilleruelo の explicit discrete-log construction が

\[
A(x)=x^{\sqrt2-1+o(1)}
\]

を達成し、O'Bryant も 2026 年にこれを infinite Sidon set の記録として記載している。citeturn25view0turn21view0　ここで

\[
\frac12-(\sqrt2-1)
=
\frac32-\sqrt2
=
0.085786\ldots,
\]

なので、これは Q2 に対して単なる対数因子の不足ではない。任意の固定 \(c\) について

\[
\frac{x^{\sqrt2-1+o(1)}}{\sqrt{x}/(\log x)^c}
=
x^{-(3/2-\sqrt2)+o(1)}(\log x)^c
\longrightarrow0.
\]

従って construction route には genuine power-exponent breakthrough が必要である。

特に Cilleruelo の proof 内部では障害をさらに正確に特定できる。彼の deletion argument では、level \(k\) の bad primes に対して多項式因子を無視すると

\[
|\mathcal B_k|
\lesssim
2^{\left(\frac{2c}{1-c}-1\right)k^2},
\]

一方で利用可能な prime block は

\[
|\mathcal P_k|
\asymp
\frac{2^{ck^2}}{k^2}.
\]

したがって bad set を同程度以下にするには

\[
\frac{2c}{1-c}-1\le c.
\]

境界方程式は

\[
c^2+2c-1=0,
\]

従って

\[
c=\sqrt2-1.
\]

これが published construction の指数を正確に生む。citeturn32view0　目標 \(c=1/2\) では bad-set exponent が \(1\)、available-prime exponent が \(1/2\) になり、既存 counting は \(2^{k^2/2}\) 級も過大である。したがってこの route も「対数因子を研磨すればよい」のではなく、collision count に**指数的な新しい節約**が必要である。

完全決着のために残る選択肢は、結局次の三類型に圧縮される。

| 決着型 | 必要な theorem-strength step |
|---|---|
| Q1 真、Q2 偽 | 全ての固定 \(\beta\) について \(a_n\neq O(n^2(\log n)^\beta)\) を universal に証明 |
| Q1 真、Q2 真 | (8) を証明し、同時にある \(\beta>1\) で \(a_n=O(n^2(\log n)^\beta)\) の Sidon 構成 |
| Q1 偽、Q2 真 | critical construction \(a_n=O(n^2\log n)\)、同値に \(A(x)\gg\sqrt{x/\log x}\) を全十分大きな \(x\) で構成 |

Q1 偽かつ Q2 偽という第四の可能性は、上の厳密な論理変換によって排除される。

## アプローチ・レジストリ

| 状態 | アプローチ | 実際に得られたもの | 正確な停止理由 |
|---|---|---|---|
| **PROVED** | \(A(x)\leftrightarrow a_n\) の量化変換 | Q1 の \(R(A)=\infty\) との同値、Q2 の polylog growth との同値 | 完了 |
| **BLOCKED** | 一段階 block energy / Cauchy | \(2/\sqrt{\log2}\) の universal constant | 固定定数しか生成せず、Q1 には unbounded gain が必要。citeturn21view0turn22view0 |
| **ACTIVE** | multiscale entropy / reverse martingale | O'Bryant 自身が conditional-expectation 構造を指摘 | 異なるスケールの energy を重複計数せず加算する定理が未取得。citeturn22view0 |
| **BLOCKED** | separated finite-block pasting | O'Bryant Lemma 9 により \(\le\binom m2\) 削除で結合 | 本調査でこの二次損失が black-box として最悪時に鋭いことを証明。citeturn22view0turn22view1 |
| **BLOCKED** | Ruzsa/Cilleruelo discrete-log digits | \(x^{\sqrt2-1+o(1)}\) | bad-collision exponent が厳密に \(\sqrt2-1\) で飽和。citeturn31view0turn32view0 |
| **BLOCKED** | \(B_2[g]\) を先に構成し \(B_2[1]\) に thinning | Cilleruelo: \(a_n\le2g\,n^{2+1/g}\) | 固定 \(g>1\) は依然 power gap。密度保存的 \(g\to1\) reduction がない。citeturn30view0 |
| **BLOCKED** | compactness / diagonal limit | Sidon sets の compactness は種々の extremal functional の最大化に有効 | finite extremizer が dense な compatible prefix を持つことは保証しない。all-scale liminf は別の extension theorem を要求する。citeturn15academia3turn17search5 |
| **ACTIVE** | entropy / combinatorial large sieve | structured Sidon problems では super-polylog saving | 現定理は squares・norm forms 等の代数的 splitting を仮定し、任意の \(A\subset\mathbb N\) には直接適用できない。citeturn24view1 |
| **ACTIVE** | zero-sum Fourier / dyadic blocks | Táfula は \((1,-1)\) を含む zero-sum form で古典的 critical threshold を再導出 | \(A(x)/\sqrt{x/\log x}\to\infty\) は排除するが、正の固定 liminf を排除しない。citeturn16view0 |
| **ABANDONED** | 独立 Bernoulli + 単純 alteration | critical-density で conflict 数の期待値が点数を大幅に上回る | one-conflict-one-deletion の first-moment 論法では密度を保持できない |

Táfula の 2026 年定理は特に吟味した。matched-even zero-sum vector

\[
\mathbf b=(c_1,-c_1,\dots,c_k,-c_k)
\]

について

\[
\frac{A(x)}{(x/\log x)^{1/(2k)}}\to\infty
\]

なら

\[
\frac1x\sum_{|n|\le x}r_{A,\mathbf b}(n)\to\infty
\]

とするもので、証明は各 dyadic index block 上の非負 Fourier integral を足し合わせる。\(k=1,\mathbf b=(1,-1)\) では Sidon の差表現数が bounded なので classical finite-liminf theorem を回収するが、「正の定数倍で全スケール dense」という Q1 の否定仮定とは矛盾しない。citeturn16view0

Croot–Mao–Pohoata–Sheffer–Yip の 2026 年 combinatorial large sieve は、局所的な合同類 branching が大量の modular collisions を作る一方、global bounded multiplicity がそれを制限するという、Q1 に構造的に近い新機構である。実際、squares の Sidon subset には

\[
|A|
\le
N\exp\!\left(
-c\frac{\log N}{\log\log N}
\right)
\]

という super-polylogarithmic saving を出し、さらに entropic version も構築している。しかし load-bearing hypothesis は「squares や norm forms に由来する algebraic splitting」であり、任意の整数 Sidon set にそのまま移すことはできない。citeturn24view1

## 反例と計算検証

まず、ブロックを「十分遠く離せば」Sidon 性が自動的に保たれるという考えは、最小例ですでに偽である。

\[
V=\{0,1\},\qquad W=\{T,T+1\}.
\]

どちらも個別には Sidon だが、\(1\) という正の差が両方に現れるため \(V\cup W\) は任意の \(T\) で Sidon ではない。距離を巨大にすることは internal-difference collision を全く解決しない。

より本質的に、本調査では次を独立に証明した。

**二次削除損失の鋭さ補題。**  
\(V\subset\mathbb Z\) を \(m\ge2\) 個の元を持つ任意の有限 Sidon set とする。その正の差の集合を

\[
D(V)=\{d_1,\dots,d_e\},
\qquad
e=\binom m2,
\]

とする。このとき、任意に遠くへ平行移動できる \(2e\) 元の有限 Sidon set \(W\) が存在して、次を満たす。

\[
D(W)\cap D(V)
\]

に対応する forbidden-pair graph は、ちょうど \(e\) 本の互いに頂点素な辺からなる matching である。従って

\[
D(W^*)\cap D(V)=\varnothing
\]

を満たす任意の \(W^*\subseteq W\) は

\[
|W^*|\le e
\]

であり、少なくとも

\[
\boxed{\binom m2}
\]

個を \(W\) から削除しなければならない。

これは \(g=1\) に対する O'Bryant Lemma 9 の

\[
|W^*|\ge |W|-\binom{|V|}{2}
\]

という保証が、**\(V,W\) が Sidon で十分離れているという情報だけからは一様に改善できない**ことを示す。citeturn22view0turn22view1

**証明。**  
\(D=\max_i d_i\) とし、整数 \(B>4D+4\) を取る。各 \(1\le i\le e\) に

\[
x_i=B^i
\]

と置き、

\[
W_0=\{x_i,\ x_i+d_i:1\le i\le e\}
\]

と定める。

同一の \(i\) に属する二点の差は \(d_i\) であり、これらは全て異なる。

異なる block \(j>i\) の間の正の差は必ず

\[
B^j-B^i+\varepsilon d_j-\eta d_i,
\qquad
\varepsilon,\eta\in\{0,1\}
\tag{9}
\]

の形をしている。まず base differences \(B^j-B^i\) は全て異なる。実際

\[
B^j-B^i=B^i(B^{j-i}-1)
\]

は \(B^i\) では割れるが \(B^{i+1}\) では割れないので、二つの base difference が等しければまず \(i=i'\)、続いて \(j=j'\) が従う。

また相異なる base differences はいずれも \(B\) の倍数なので、その差の絶対値は少なくとも \(B\)。一方 (9) の perturbation の差は絶対値 \(2D\) 以下である。\(B>4D\) より、異なる base differences に属する二つの (9) が一致することはない。

同じ \((j,i)\) 内では perturbation は

\[
0,\quad d_j,\quad -d_i,\quad d_j-d_i
\]

の四つである。\(d_i,d_j>0\) かつ \(d_i\ne d_j\) より、これらも相異なる。

最後に cross-block difference は \(B^2-B-D>D\) なので、\(d_k\le D\) である within-block difference と一致しない。従って \(W_0\) の全ての正の差は相異なり、\(W_0\) は Sidon である。

しかも \(D(V)\) に属する \(W_0\) の差は、ちょうど

\[
(x_i+d_i)-x_i=d_i
\]

だけである。したがって forbidden graph は

\[
\{x_i,x_i+d_i\},
\qquad i=1,\dots,e
\]

という \(e\)-edge matching そのものになる。その全ての辺を破壊するには少なくとも各辺から一頂点、合計 \(e=\binom m2\) 点を削除する必要がある。

最後に \(W_0\) を \(T\) だけ平行移動して \(W=T+W_0\) とすれば internal differences は変化しない。\(T\) は任意に大きくできるため、O'Bryant Lemma 9 の

\[
W_1-V_2\ge\max\{V_2,\operatorname{diam}W\}
\]

も満たせる。証明完了。

この補題は #1191 を解かないが、重要な search-space reduction である。すなわち、construction side で「任意の dense finite Sidon block を遠くへ置き、少数点だけ捨てる」という black-box strategy には原理的な限界がある。成功する pasting theorem は、候補ブロックの**追加の代数構造・ランダム性・可変 dilation** を使い、forbidden-difference graph の edge count ではなく大きな independent set を直接作る必要がある。

有限計算でもこの補題を sanity-check した。

\[
V=\{0,1,4,10\},
\qquad
D(V)=\{1,3,4,6,9,10\},
\]

として \(B=41\) を取り、上の方法で 12 点の \(W_0\) を構成した。全ての正の差を総当たりで検査したところ重複はなく、\(D(V)\) と一致する差は指定された 6 本の disjoint pair に限られた。これは証明の代替ではなく、添字・符号ミスを検出するための有限監査である。

**単純 random alteration の検査。**  
有限区間 \([N]\) から各整数を独立確率

\[
p=N^{-1/2}(\log N)^{-c}
\]

で選ぶと、

\[
\mathbb E|S|
=
Np
=
\frac{\sqrt N}{(\log N)^c}.
\]

一方、四つの相異なる整数による非自明な

\[
a+b=c+d
\]

は \(\Theta(N^3)\) 個存在するので、その期待 conflict 数は

\[
\Theta(N^3p^4)
=
\Theta\!\left(
\frac{N}{(\log N)^{4c}}
\right).
\]

点数との比は

\[
\Theta\!\left(
\frac{\sqrt N}{(\log N)^{3c}}
\right)\to\infty.
\]

従って「独立に選ぶ→各 conflict から一点ずつ削除する」という naive first-moment alteration は critical polylog density を保持しない。ただし、これは random greedy process、local lemma、container、あるいは conflicts を高度に集中させる構成を排除するものではない。

## 文献調査の到達点

以下は、実際に一次ソースまたは著者プレプリントで statement と仮定を確認した主要 ledger である。

| 一次文献 | 正確に有用な内容 | 証明機構 | #1191 への適用判定 |
|---|---|---|---|
| Erdős, 1980 | \(\limsup a_n/(n^2\log n)>0\)、limsup \(=\infty?\)、polylog upper-growth sequence の存在問題 | 古典 Sidon density argument | **問題そのものの原典**。citeturn9view0turn10view0 |
| Cilleruelo, *Infinite Sidon sequences* | explicit \(A(x)=x^{\sqrt2-1+o(1)}\) | mixed-radix digits + discrete logarithm + bad-prime deletion | **construction frontier**。collision-count barrier は \(\sqrt2-1\)。citeturn25view0turn31view0turn32view0 |
| O'Bryant, arXiv:2606.28651v3 | \(g\)-Golomb ruler に \(L\le2\sqrt g/\sqrt{\log2}\)、列形式 \(\limsup a_n/(n^2\log n)\ge\log2/(2g)\) | block energy + weighted Cauchy | **現在確認できた universal side の最も直接的改善**。Q1 の zero には届かない。citeturn20view0turn21view0 |
| O'Bryant Lemma 9 | separated \(V,W\) を \(\le g\binom{|V|}{2}\) 削除して結合 | old/new internal-difference overlap の削除 | cross-scale construction の具体的入口。ただし \(g=1\) の二次損失は本調査の補題で worst-case sharp。citeturn22view0turn22view1 |
| Táfula, 2026 | zero-sum form、特に \((1,-1)\) で critical \(x/\log x\) threshold | dyadic index blocks + nonnegative Fourier integral | multiscale/Fourier 候補だが現 statement は有限 liminf 定数まで。citeturn16view0 |
| Cilleruelo, *A greedy algorithm for \(B_h[g]\)* | \(a_n\le2g\,n^{h+(h-1)/g}\) | greedy bounded-representation construction | \(h=2\) で \(2+1/g\)。任意に \(2\) に近づけられるが \(g>1\) であり、Sidon への reduction が欠落。citeturn30view0 |
| Fabian–Rué–Spiegel | robust/strong infinite Sidon・\(B_h\) constructions | Cilleruelo 型 construction + deletion | extra separation robustness は得るが \(\alpha=0\) で exponent frontier を超えない。citeturn19academia3 |
| Croot–Mao–Pohoata–Sheffer–Yip, 2026 | squares 上の Sidon set に super-polylog saving、entropic large sieve | modular splitting + collision entropy | **新しい universal-side mechanism として有望**だが、現仮定は任意の整数集合より強い。citeturn24view1 |
| Riblet–Schehr, 2025/26 | Sidon sets/\(B_2[g]\) の compactness を用いた extremizer existence | compactness | compatible dense extension は得られず、Q2 の liminf condition を有限 extremizer から移せない。citeturn15academia3 |
| Niu, 2026 | Pilatte 型 Sidon asymptotic-basis construction を function-field convolution で強化 | Ruzsa/Pilatte skeleton + Sawin 型深い解析入力 | density theorem ではないが、**Ruzsa 型 algebraic skeleton に強い解析的 sieve を組み合わせられる**ことを示す隣接技術。citeturn17search1 |

Táfula の論文は 2026 年 7 月 22 日プレプリントとして現れ、matched-even case の Theorem 1.1 は、単なる citation ではなく proof mechanism まで確認した。証明は disjoint dyadic blocks

\[
\{a_{2^m+1},\ldots,a_{2^{m+1}}\}
\]

から得る representation lower bounds を足し合わせ、Fourier integrand の非負性を利用する。これは O'Bryant の interval-block energy とは異なるため、両者を組み合わせる価値はあるが、現状では両方とも同じ critical scale で「有限定数」を生成し、任意の正の liminf を排除する追加の divergence は確認できなかった。citeturn16view0

一方、compactness route は慎重に区別する必要がある。Sidon property 自体は有限 forbidden configuration なので pointwise/diagonal limit と非常に相性がよい。しかし Q2 が必要とする

\[
A(x)\ge C\frac{\sqrt x}{(\log x)^c}
\qquad
\text{for every sufficiently large }x
\]

は、単一終端スケールで大きい finite Sidon extremizer を取るだけでは保存されない。有限集合の質量を右へ移せば、任意の固定初期区間では diagonal limit が疎になり得る。したがって compactness を使うなら、その前に「dense finite set の存在」ではなく「任意の既存 prefix を保った dense extension」のような nested feasibility theorem が必要になる。この missing theorem は現在証明されていない。

## 最も価値の高い次方向

現時点で再び同じ欠落補題を別記号で書かないためには、次の研究波は**機構そのものを変える**べきである。

| 優先 | 方向 | なぜ既存失敗の言い換えではないか | 最初に証明すべき具体的 milestone |
|---|---|---|---|
| 最高 | **multiscale difference entropy** | O'Bryant は一つの partition scale の \(L^2\)-energy。Croot 等は多 moduli の entropy/collision accounting。情報量を scale 間で累積する新機構 | 同一 difference pair を二重計数せず、複数 nested partitions の entropy deficits の和を global Sidon budget で上から抑える inequality |
| 最高 | **algebraic finite Sidon block の forbidden-difference graph** | black-box deletion が二次的に sharp でも、Singer/Bose/Cilleruelo block には追加構造がある | affine/dilation parameter を平均して、old difference set \(D(V)\) が誘導する graph に \((1-o(1))|W|\) あるいは polylog-loss の independent set が存在するかを定量化 |
| 高 | **Cilleruelo collision count への深い arithmetic saving** | 現在の barrier を「密度不足」と曖昧にせず、必要な saving が \(2^{k^2/2}\) 級と判明している | \(c=1/2\) で bad-prime count を current \(2^{k^2}\) scale から \(2^{(1/2+o(1))k^2}\) 以下へ下げる新しい bilinear/convolution estimate |
| 高 | **dynamic random greedy Sidon process** | naive Bernoulli alteration は失敗したが、random greedy は forbidden differences を逐次避けるため conflict concentration が全く異なる | 時刻 \(t\) までの forbidden set の pseudorandomness と available integers の survival probability を \(n^2\operatorname{polylog}n\) scale まで制御 |
| 中高 | **Táfula Fourier blocks × O'Bryant shifted blocks** | 一方は index-dyadic、他方は physical-space shifted partition で、同じ decomposition ではない | 二種類の local lower bound が同一差を数える multiplicity を一様に制御しながら、scale 数に応じて増大する lower bound を作れるか検証 |

最初の方向が universal side では最も具体的である。O'Bryant の proof では

\[
F_\ell
=
A(t^*+\ell N)-A(t^*+(\ell-1)N)
\]

が、集合の indicator を長さ \(N\) の区間 partition が生成する \(\sigma\)-algebraへ conditional expectation したものと解釈できることを著者自身が指摘している。さらに Cauchy が equality に近いのは \(F_\ell\) が特定の weight profile に比例するときだけであり、その smoothness を強制する理由はないとも述べる。citeturn22view0　したがって promising target は「各 scale で同じ Cauchy を繰り返す」ことではなく、nested conditional expectations の**entropy increment/decrement**を差の一意性と結ぶことである。

construction side では、本調査の quadratic-sharpness lemma により search target がかなり絞られた。一般の \(W\) を使う deletion theorem の改善を追うより、

\[
H_{V,W}:
\quad
ww'\in E(H)
\Longleftrightarrow
|w-w'|\in D(V)
\]

という forbidden-difference graph を、Bose/Singer/discrete-log block の affine parameter に沿って解析する方が情報量が多い。必要なのは edge 数だけではない。O'Bryant の deletion は「一辺につき一点削除」という vertex-cover upper bound を使うが、実際に重要なのは

\[
\alpha(H_{V,W}),
\]

すなわち大 independent set の大きさである。今回の matching counterexample は一般 \(W\) では \(\alpha=|W|/2\) まで落ちることを示したが、algebraic \(W\) の affine orbit 全体について同じ worst case が起こるとはまだ証明されていない。

Cilleruelo route についても、次に必要なものは明瞭である。published proof の divisor-counting/deletion のまま \(c\) を \(0.4142\ldots\) から \(0.49\) へ動かす作業には意味が薄い。\(c=1/2\) では指数レベルで \(1/2\) の saving が不足する。Pilatte 系の Sidon-basis constructions と、その 2026 年の Niu による function-field convolution の利用は、Ruzsa 型 algebraic skeleton に通常より強い解析入力を結合すること自体は可能だと示している。citeturn17search1　#1191 に転用するには「basis representation」を制御する代わりに「repeated pair-sum collision」の divisor/congruence family を平均する新しい estimate が必要になる。

## 形式化状況

完全解決は得られていないため、Q1/Q2 全体を Lean theorem として閉じる段階には達していない。ただし今回証明した reduction と obstruction lemma は theorem-strength の未解決仮定を含まず、形式化可能な独立成果である。

形式化の依存関係は次のように整理できる。

```text
Sidon sum uniqueness
        │
        ▼
positive-difference uniqueness
        │
        ├──────────────► binom(n,2) ≤ a_n-a_1
        │                         │
        │                         ▼
        │                 log(a_n)/log(n) → 2
        │                         │
        ▼                         ▼
A(x) constant on [a_n,a_{n+1}) ─► Q1 enumeration equivalence
                                  │
                                  ▼
                  L(A)=0 ↔ limsup a_n/(n² log n)=∞

eventual positive liminf
        │
        ├──► a_n ≤ C n²(log a_n)^(2c)
        │                   │
        │                   ▼
        │             log a_n = O(log n)
        │                   │
        ▼                   ▼
Q2 ↔ a_n=O(n²(log n)^β), β=2c
```

pasting obstruction の dependency DAG はさらに有限的である。

```text
D(V) has e=binom(m,2) distinct differences
                    │
                    ▼
       choose B>4 max D(V)
                    │
                    ▼
 W={B^i, B^i+d_i : 1≤i≤e}
          │                  │
          ▼                  ▼
base differences unique   perturbations separated
          └────────┬─────────┘
                   ▼
                 W Sidon
                   │
                   ▼
forbidden graph = e-edge matching
                   │
                   ▼
 every compatible W* deletes at least e points
```

Lean 化で最初に狙うべき有限 statement は、概念的には次である。

\[
\texttt{quadratic\_pasting\_loss\_sharp}:
\]

> 任意の有限 Sidon set \(V\subset\mathbb Z\), \(|V|=m\ge2\) に対し、有限 Sidon set \(W\) が存在して \(|W|=2\binom m2\) かつ、\(V\) の正差を一つも持たない \(W^*\subseteq W\) は \(|W^*|\le\binom m2\) を満たす。

これは極限・解析を一切含まず、有限集合、整数差、matching だけで完結するので formalization の最初の対象として最も堅い。

次に

\[
\texttt{q2\_iff\_polylog\_enumeration\_growth}
\]

として

\[
\left[
\liminf_{x\to\infty}
\frac{A(x)(\log x)^c}{\sqrt x}>0
\right]
\Longleftrightarrow
\left[
a_n=O(n^2(\log n)^{2c})
\right]
\]

を形式化できる。ここでは eventual inequalities と \(\log y=o(y^\varepsilon)\) の標準解析が必要になる。

最後に

\[
\texttt{q1\_iff\_enumeration\_limsup\_infinite}
\]

として

\[
\liminf_{x\to\infty}
A(x)\sqrt{\frac{\log x}{x}}=0
\Longleftrightarrow
\limsup_{n\to\infty}
\frac{a_n}{n^2\log n}=\infty
\]

を目標とする。この部分で最も壊れやすいのは、\(A(x)\) の step-function intervals から \(a_n\) への liminf 移行と、extended-real limsup の扱いである。本調査ではこれらを上で明示的に監査した。

最終監査の結論は明確である。O'Bryant の universal theorem、Cilleruelo/Ruzsa 型 construction、Táfula の Fourier theorem、\(B_2[g]\) constructions、compactness、entropy/large-sieve のいずれからも、現時点で Q1/Q2 の完全決着を導く theorem は得られていない。反対に、本調査で証明した \(A(x)\)-\(a_n\) の正確な同値性、Q2 の polylog-growth 同値性、および separated-pasting の quadratic-loss sharpness は未解決補題に依存せず、候補解決 route の量化条件と construction bottleneck を厳密に狭めている。したがって **Erdős Problem #1191 は本研究実行では解決済みとは判定できず、RESOLVED とする数学的根拠はない**。