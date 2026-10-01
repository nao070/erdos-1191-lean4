# Erdős Problem #1191 — 統合研究状況・重複整理・次の証明目標

**監査日:** 2026-08-29（Asia/Tokyo）  
**総合状態:** `UNRESOLVED_AT_HARD_LIMIT`  
**公開状態:** Open、賞金 USD 1,000

> **2026-08-28 handoff correction:** 今回は添付ZIPが実際にマウントされ、endpoint-varianceのコード・tests・certificatesを再実行した。15 unit testsと合計42,615 exact checksが通過した。2つ目のZIP内28ファイルは全て1つ目の `core_workspace/endpoint_variance/` とSHA-256一致した。元の内部 `SHA256SUMS` は自己自身をhash対象に含めたため1件だけ不一致となるが、他のpayloadは通過した。詳細はパッケージの `MATHEMATICAL_AUDIT_NOTES_2026-08-28.md` と `integrity/` を参照。

> **2026-08-28 continuation:** endpoint theorem は独立再導出を通過した。
> Wave 1 では cyclic-arc covariance の正確な pair--pair kernel と
> resistance 表現を得て、臨界dyadic functionalの強制下界
> `F_J >= (1+o(1)) log J/(360 C log 2)` を証明した。しかし必要な
> density-compatible signed upper budget `F_J=o(log J)` は未証明である。
> 正値性・単調性・無条件raw-budget版は明示反例で排除された。
> Wave 2 では `m<=7, D<=25` のGolomb rulerを完全列挙し、有限最小値を
> 独立oracleで照合した。この有限計算は漸近結論ではない。したがって
> 総合状態は引き続き `UNRESOLVED_AT_HARD_LIMIT` である。

> **2026-08-28 continuation, Wave 3:** diameter modulus
> `N_m=D_m+1` では、gap weights `h_k` と levels
> `x_m(k)=k(m-k)` により
> `V_m=N_m^-2 sum_{k<l} h_k h_l (x_m(k)-x_m(l))^2` という完全に正の
> 恒等式を得た。Sidon 条件から `m=8q>=16` について
> `V_m >= 9m^6/(16,777,216 N_m)` を証明した。従って臨界包絡の下で
> 新しい汎関数 `G_J=sum_j V_{m_j}/m_j^4` は `Omega_C(log J)` となる。
> これは従来の `m^-3` 重みから一冪の改善である。反面、三段 rank lift
> により単一 birth shell が `V_m/m^4>=1/2304` を持ち得るため、必要な
> `G_J=o(log J)` 上界は、孤立した一つのSidon rulerと二次直径だけから
> 導くpointwise `o(1)` 評価からは出ない。互換prefixを仮定する
> 有界深度補題まではこの有限族で排除されない。
> また exact q-cover projection identity を証明したが、新生辺一つが
> 古い分散を完全相殺する Sidon 反例 `{0,1,4}` があり、complete loads
> 自体の scalar martingale 化は不可能である。H1--H5 の自然な shell
> shortcut も4点 rulerで反証された。これらは厳密な部分進展であり、
> Q1/Q2はいずれも未解決である。

> **Wave 3 adversarial closure:** H6を導く候補だった同一modulusでの
> prefix分散単調性も偽である。倍加比較 `A_r subset A_2r` における
> 最小Sidon反例は
> `N=40, A_2={0,20}, A_4={0,20,21,39}` で、分散は
> `1/4 -> 99/400` と減少する。これは全ての倍加prefix sizeについて
> 40が最小であることまで解析的に証明され、3,354,793個のgap構成と61個の反例族
> instanceで監査された。また各差を独立Hilbert座標へ分ける方法は、
> 任意の重みでもcritical scaleごとに少なくとも`const/log m`の
> trace-synthesis costを持つため、必要な`o(log J)`予算を出せない。
> よって次の候補はstructured off-diagonal情報を保つ必要がある。

> **Wave 3 gap-measure dynamics:** 正規化gap測度
> `nu_m=N_m^-1 sum_(k<m) h_k delta_(k/m)` と
> `f(u)=u(1-u)` に対し、`Var C_(N_m)/m^4=Var_(nu_m) f` である。
> `m -> 2m` では `z=(f,u)` の共分散行列
> `M_m=N_m Cov_(nu_m)(z)` が、明示行列
> `B=((1/4,1/4),(0,1/2))` により
> `M_(2m)=B M_m B^T+Q_m`, `Q_m` positive semidefinite、という完全な
> cross-prefix更新を満たす。さらに隣接gapが相異なることだけから、
> `M=4m>=16` について
> `Var C_(N_M)/M^4 >= (9M^2-256)/(1,048,576 N_M)` を得た。
> 臨界包絡 `N_M<=2CM^2 log M` の下での係数は
> `(9-256/M^2)/(2,097,152 C log M)` で、従来の8-block定数の16倍である。
> 固定interactionの `M^-4` tailは `4/(15M_s^4)` まで下がり、粗い絶対値
> 損失は一shellあたり `O(1)` になった。それでも全体は `O(J)` であり、
> 必要な `o(log J)` signed/structural upper budget は未証明である。

> **Wave 3 innovation reduction:** normalized recursionを有限horizonで
> adjoint化し、`G_j=Var_(nu_j)f` の総和を、bounded initial termと
> `sum <H_(j+1),Q_j/N_(j+1)>` というPSD innovation総量へ完全に
> telescopingした。一定majorantは
> `H=((16/15,8/105),(8/105,4/35))` である。他方、critical growthを
> 満たし `G_j=1/72` が全尺度で続く明示的なabstract PSD orbitを構成
> した。これはGolomb birth shellから来るとは主張しないが、recursion、
> PSD、critical diameterだけに依存するuniformly controlled
> Lyapunov/trace/determinant上界を排除する。係数が爆発するformal
> forward telescopeは存在し得るが有用な終端予算を与えない。従って残る補題は、actual newborn-shell covarianceと
> rank-one mean innovationに対する**arithmetic innovation budget**である。

> **Wave 4 growing-depth / global-history refinement:** `M=2^J` の有限
> Erdős--Turán rulerでは、末尾の `floor(log_2 J)-1` 個のdyadic prefixが
> 全て同じ `C=1` 臨界包絡を満たしながら、gap varianceの和が
> `(log J)/(180 log 2)+O(1)`、隣接innovationが `1/360+o(1)` となる。
> 従って固定深さだけでなく、深さが `Theta(log J)=Theta(log log M)` に
> 増える局所履歴も不十分である。ただし各`J`で別の有限rulerを使うため、
> 一つの無限critical列ではない。

> 同時に、一つのglobal critical列に本当に使えるcross-block packingを
> 証明した。`M=qm`、古いprefixが `N_m<=K m^2 log m` のとき、正規化
> prefix直径のrank-grid discrepancy `epsilon_M` は
> `1/q-Km^2 log(m)/(binom(q,2)m^2+1)` 以上である。従って仮想的な
> global critical列では全ての十分大きいdyadic `M` で
> `epsilon_M=Omega(1/log M)`、すなわち直径profileのresetが必ず起こる。
> しかし、old--new difference帯域の占有率から`Q_00/N`を直接支払う
> 不等式は growing Erdős--Turán族で反証された。残る本命は異なる
> profile epoch間のcross differencesを使い、resetを無限に独立更新
> できないことを示す**flat-profile versus profile-reset amortization**で
> ある。32点までの有限nested searchも4遷移での単調減衰を反証した。
> Q1/Q2はいずれも未解決であり、賞金請求可能な状態ではない。

> **Wave 5 arithmetic reset-renewal refinement:** `M=qm` に対し、旧profile
> のchordを除いた非線形成分が
> `e_M(r)-(r/m)e_M(m)=(N_m/N_M)e_m(r)` と厳密に輸送されることを
> 証明した。global block packingはさらに、`q-1>=4K log m` ならresetの
> 場所と符号を `e_M(m)<=-1/(2q)` と固定する。dyadic endpoint-flat run
> は `O(log log m)` 世代に限られ、上向きnormalized-diameter変動を用いた
> 条件付きamortizationも得た。しかしcritical growthはその上向き変動を
> 制御しない。dyadic `C=1`、全prefix `N_n<12n^2 log n`、scalar capacity、
> exact PSD dynamicsを満たしながら全stepで `Q_00/N>=1/2048` となる
> infinite sawtooth gap profileを構成したため、profile/reset/PSDのみの
> 証明は排除された。このprofileは4点で差14が重複する明示的な非Sidon
> 例であり、Sidonの全contiguous-sum一意性を使う道は残る。計算側では
> 認証済み32点prefixを同じ`C=1`全prefix包絡のまま64点へ延長し、五つの
> dyadic transitionで `min Q_00/N>0.0037994` を保持した。64点以降は
> heuristicであり、無限延長や漸近結論ではない。次の厳密目標は複数の
> reset-to-flat cycleをまたぐcross differencesからrenewalを排除する
> **arithmetic reset-renewal exclusion** である。Q1/Q2は未解決である。

> **Wave 6 arithmetic band-renewal refinement:** birth-lag familyを整数差の
> inclusive hullでまとめると、任意の整数区間に完全に含まれる需要は
> 区間容量以下であるため、普遍Hall圧力は厳密に`Lambda<=1`となる。ただし
> 22個の既存fixtureで観測された`Lambda_NN<=1/(4 sqrt(n))`は一般則では
> ない。一つのC=1 Golomb rulerを64点までexact auditし、8→16、16→32、
> 32→64でそれぞれ`Lambda=9/14,17/28,45/118`、scaled値
> `2592/49,4624/49,259200/3481>1`を得た。全2,016差と全63 prefix包絡は
> 完全検証したが、拡張searchはheuristicであり、最小性・漸近性はない。
>
> newborn-shellとold--new anti-diagonalを複数epochで同じ整数帯域へ注入する
> Theorems A--Cを証明した。`H_m=D_m^-+D_m^+`、
> `M_m=max(mu_m^-,mu_m^+)`、`tau_(m,k)=H_m+kM_m`とすると、Theorem Dは
> `sum_(tau<=X) k/tau<=1+log X`、また任意の`epsilon>0`について
> `sum k/tau^(1+epsilon)<=(1+epsilon)/epsilon`を与える。これは一つの
> 無限Sidon列の全epochにも単調収束で延長できる厳密なglobal ledgerだが、
> endpoint `epsilon=0`では`O(log X)`に留まり、必要な`o(log J)`上界では
> ない。
>
> 計算側では別のseeded beamが既存64点witnessを128点へ延長した。最終mark
> は136,282で、8,128/8,128差が一意、2点から128点までの全127 prefixが
> `N_n<=floor(2n^2 log n)`を満たす。これは発見後のexact finite auditで
> あり、最適性・全探索・無限延長を主張しない。またresidue lift
> `A_L(B)={0,1,Lb_1,...}`はGolomb性を保ち、one-point forbidden shadowを
> 高々4剰余類へ閉じ込める。増大する有限互換windowでもshadow密度総和を
> `o(1)`、innovation総和を発散させられるため、普遍的な局所shadow-density
> chargeは反証された。従来のgeneric近接blockで観測された高密度shadowは
> tested modelの事実に過ぎない。
>
> Wave 6時点の単一目標は**global band-renewal self-improvement theorem**で
> あった。Wave 7は全pairのcomplete-birth ledgerまで完成し、そのpotential
> だけによるaffine innovation支配を反証した。従って現在の目標は、§11の
> **infinite-survival-conditioned debt-repayment theorem**である。一つの無限
> global critical Sidon列でoverlap debtを返済し、exact adjoint innovation
> sumを`o(log J)`へ改善する必要がある。限定一次文献監査でも、この
> compatible all-prefix towerまたはinnovation theoremは確認できなかった。
> これは限定付きnullであって不存在・新規性の証明ではない。総合状態は
> `UNRESOLVED_AT_HARD_LIMIT`、賞金請求可能な証明はまだない。

> **2026-08-28 continuation, Wave 8:** actual newborn-adjacent familyを
> Wave 6のcross-antidiagonal ledgerへ追加し、任意の閾値で両需要の合計が
> `floor(T)`以下となるglobal capacity theoremを証明した。さらに各dyadic
> epochでは「現在のnewborn familyが実際に支払われる」か「全ての古い
> adjacent ancestryがclearされる」かのどちらかが必ず起きる。従って一つの
> 固定history上で未払いinternal-adjacent familyは高々一つである。
>
> actual innovation `Q_m`はcommon grid上のpair energyとして完全展開された。
> newborn covarianceのsigned square expansionでは、負係数は二つのproper
> boundary fanだけで、strict bulkとfull-span cornerは全て正である。critical
> cap下では負のadjacent endpoint atomsのdyadic和は有限で、人工的な`h_0`
> boundary rowの全和も`92/315`以下である。残るshell障壁はnon-adjacent
> boundary fanであり、rank-one Abel fanも別に制御する必要がある。
>
> さらに全old-pair負項をepoch間で保持したexact pair telescopeを証明した。
> 各pairのnet coefficientはbirth chargeの少なくとも`1/2`を保持し、全体でも
> `B_H/2 <= sum <H,Q_m/N_(2m)> <= B_H`である。exact finite-horizon adjoint
> では同じ符号付き和が正のfuture `E`-energy tailへ一致する。従って
> old-pair cancellationだけで必要なlittle-oを得る道は閉じた。現在の単一
> 主目標は、一つの無限eventually-critical Golomb branch上でpositive birth
> budget `B_H(J)=o(log J)`を証明することである。
>
> 局所候補も敵対的に整理した。`U_global(T)/T>=I_m`は4点`C=1`例で反証され、
> latest-shell版はgenuine old-clear/new-unpaid 8点例で反証された。m>=4の
> global版は682点modified-greedy fixtureの全510活性化まで有限反例なしだが、
> 無限主張ではない。Hegyváriのfinite parabola block、affine variants、
> exact splicing criterionも監査した。任意有限prefixへの無条件spliceは
> 可能だが保証endpointがcritical regimeで立方化し、固定finite block menuは
> universal internal differencesで阻止される。従ってQ2のcompatible-prefix
> bridgeにもならない。550-recordの限定一次文献監査でも必要なpositive
> birth budget theoremまたはcompatible critical towerは確認できなかった。
> 総合状態は引き続き`UNRESOLVED_AT_HARD_LIMIT`で、賞金請求は不可である。

> **2026-08-29 continuation, Wave 9:** positive birth budgetをscalar化した。
> `nu_n=N_n^(-1)sum_(i<n)h_i delta_(i/n)`、
> `V_n=Var_(nu_n)(u)`とすると、全dyadic horizonで
> `(4/49)sum V_(2^k)<=B_H<=(36/35)sum V_(2^k)`。従ってP15は
> `sum_(k<=J)V_(2^k)=o(log J)`と定数因子内で同値で、shellとrank-oneを
> 別々に扱う必要がなくなった。一方、distinct genuine gapsだけで
> `V_n>=n^2/(512N_n)`なので、仮想critical branchは
> `B_H(J)>=(6272C log2)^(-1)log J+O_C(1)`を強制する。必要な反証機構は
> non-adjacent contiguous sumsのglobal uniquenessだけに絞られた。
>
> 任意のpositive gap vectorについてshort rankとsmall endpointを除くcore
> reductionを証明し、標準cutoffで除外総量を`O(log log J)`にした。残る
> long-rank/two-large-endpoint coreには`(R,X,Y,Z)`のexact tile boundがある。
> しかしscaled E–T familyではnumerical difference densityが0へ行っても
> local birth chargeが`1/2352`以上なので、local sparsity routeは閉じる。
> 4点1,672件とbounded 8点`C=1` 1,146件のcomplete probeはpointwise decay、
> literal harmonic schedule、static rank/magnitude injectionを反証した。
> 512点finite fixturesではmacroscopic coreがterminal chargeの`3/5`超を占める。
>
> genuine non-adjacent productにはpositive cross-ratio majorantを導入した。
> quadratic rank weightのAbel係数は完全に分類され、strict-interior gcd
> `delta_n^circ`と全difference一意性からscale-invariant factorial upper
> `S_n<=log(a_(n-1)/(delta_n^circ n^2))+1+log2+o(1)`を得た。retained
> `(D/N)^2` potentialはexact dyadic recursionを持つが、そのbirth sumは
> positive state sumの`3/4`から`1`倍で、terminal telescopeにはならない。
>
> 750-record、31-queryの限定一次文献deltaではMa--Yi Theorem 4.1とShearer
> DTS LPが最も近かった。それらからarbitrary epoch subsetsに有効な
> hereditary rank-lag inequality `(W9-RLP)`を導いたが、linear difference
> lengthしか制御せずproduct/kernel coreは未払い。従って次の単一目標は
> 一つの`surv_C=infinity` branch上のcore tileに対するsurvival-conditioned
> cross-epoch non-saturationである。Q1/Q2は未解決、賞金請求は不可。

> **2026-08-29 continuation, Wave 10:** Wave 9のlaminar案を実行した。
> 任意重み付きのincomplete-DTS inequality
> `sum r beta_r <= sum lambda*d <= sum N_(2m)Gamma_m`、hereditary
> factorial/product inequality、固定gap位置への将来kernel loadの
> `O(4^(-K))` tailを証明した。従って永続するmassは新しいfrontierへ
> 移動し続けなければならない。
>
> dyadic cross-ratio shellのnegative bulkを完全分類すると、全epochで
> right-endpoint bandsが互いに素であり、global weighted log-product
> rearrangementが使える。しかしその最適主項は一様に
> `F_E=(7/4)sum_(m in E)log m+O(|E|)`で、positive boundaryに対して
> `(1/4)sum log m`とsecondary `log log`が残る。これはactual shell massの
> lower boundではなく、plain distinct-integer Abel-spectrum certificateの
> 厳密な限界である。欠けるleading quarterはlower-shell fan `q=m-1`に局在する。
>
> exact finite LPでは、prefix moduli固定後のW9-RLP行が全tile変数に対して
> zero columnであり、単純併置はprimal/dualを変えない。128点までの
> 9,845,549 selectionを全監査し、tested tile blocksではexact primal=dual。
> したがってexact obligationはP15のままである。次の高価値な十分条件候補は、
> actual bulk premiumとpositive-boundary slackを合わせてcertificateを返済する
> `surv_C=infinity` theorem、または別のbi-/tri-tree tensor encodingでsummably
> vanishing box constantを証明すること。P15/Q1/Q2は未解決、賞金請求不可。

---

## 1. 問題と解決条件

無限Sidon集合を

\[
A=\{a_1<a_2<\cdots\}\subseteq\mathbb N,
\qquad A(x)=|A\cap[1,x]|
\]

とする。

### Q1 — 全Sidon集合に対するゼロliminf

\[
\liminf_{x\to\infty}A(x)\sqrt{\frac{\log x}{x}}=0
\]

は常に真か。

### Q2 — 全ての十分大きい尺度で濃いSidon集合

ある無限Sidon集合とある \(c>0\) が存在し、

\[
\liminf_{x\to\infty}\frac{A(x)(\log x)^c}{\sqrt{x}}>0
\]

となるか。

Q1とQ2は別々の目標であり、一方の解決が自動的に他方を解決するわけではない。

---

## 2. 必ず残すべき正確な同値変形

### 2.1 ギャップ端点への還元

\(A(x)=k\) となる \(a_k\) と \(a_{k+1}\) の間で、\(\sqrt{\log x/x}\) は十分大きい \(x\) について減少するため、

\[
\liminf_{x\to\infty}A(x)\sqrt{\frac{\log x}{x}}
=
\liminf_{k\to\infty}k\sqrt{\frac{\log a_{k+1}}{a_{k+1}}}.
\]

標準的な対数反転を加えると、Q1は次と同値である。

\[
\boxed{
\text{全ての無限Sidon列で }
\limsup_{n\to\infty}\frac{a_n}{n^2\log n}=\infty
}
\]

Q2は、ある \(d>0\) について

\[
\boxed{a_n=O\!\left(n^2(\log n)^d\right)}
\]

を満たす無限Sidon列の存在と同値である。元のQ2の記号では \(d=2c\)。

### 2.2 有限・互換接頭辞プロファイル

Sidon列を平行移動して、全ての正差が異なる正規化Golomb ruler

\[
0=b_0<b_1<b_2<\cdots
\]

とする。次を定義する。

\[
\Lambda_n(d):=
\min_{\substack{0=b_0<\cdots<b_n\\\text{Golomb ruler}}}
\max_{1\le k\le n}
\frac{b_k}{k^2(\log(2k))^d}.
\]

有限分岐木に対するKőnig型コンパクト性から、

\[
\boxed{\text{Q1が肯定的}\iff\Lambda_n(1)\to\infty}
\]

および

\[
\boxed{\text{Q2が肯定的}\iff
\exists d>0:\ \sup_n\Lambda_n(d)<\infty}
\]

が成り立つ。

この定式化は重要な誤りを防ぐ。各尺度で独立に濃い有限Sidon集合を作るだけでは不十分である。一つの一様な座標上界の下で、全接頭辞が互換でなければならない。

---

## 3. 現在までに確立していること

### 3.1 外部一次資料で確認できる厳密な結果

1. **Erdősの原問題。** 1980年のsurveyでErdősは、\(\limsup a_k/(k^2\log k)>0\) を証明し、このlimsupが無限大か、また \(a_k\le Ck^2(\log k)^d\) を全ての \(k\) で満たす \(B_2\)-列があるかを問い、関連問題の解明に1,000ドルを提示した。

2. **既知の最良の普遍定数。** Kevin O’Bryantの現行Part I、arXiv:2606.28651v3は、任意の \(g\)-Golomb rulerについて

   \[
   \liminf_{n\to\infty}
   \frac{|A\cap[0,n)|}{\sqrt{n/\log n}}
   \le \frac{2\sqrt g}{\sqrt{\log2}}
   \]

   を証明する。Sidon集合では \(g=1\) なので定数は
   \(2/\sqrt{\log2}\approx2.4022448\)。同値な列形式として

   \[
   \limsup_{n\to\infty}\frac{a_n}{n^2\log n}\ge\frac{\log2}{2}
   \]

   が得られる。これは定数改善であって、Q1のゼロ結論ではない。

3. **既知の最良構成指数。** Ruzsaは存在を証明し、Cillerueloは明示的に

   \[
   A(x)=x^{\sqrt2-1+o(1)}
   \]

   を満たす無限Sidon集合を構成した。列形式では

   \[
   a_n=n^{\sqrt2+1+o(1)}
   =n^{2.414213\ldots+o(1)}.
   \]

   Q2に必要なのは \(n^2\operatorname{polylog}(n)\) であり、依然として真の多項式指数差がある。

4. **2026年の隣接研究は#1191を閉じない。** O’Bryant Part IIは偶数次数の \(B_h\)-集合を扱い、\(h=2\) ではPart Iに帰着する。Táfulaのzero-sum linear formの研究も古典的有限定数型の密度制約を拡張するが、右辺をゼロにはしない。

5. **公開状態。** Erdős Problemsは#1191を依然Openとし、「有限計算のみでは解決できない」と明記している。

### 3.2 これまで報告された厳密有限計算

以下は漸近証明ではなく、校正・反証・構造発見用である。

1. \(\rho_n:=\Lambda_n(0)\) について、従来の独立検証器は \(n=21\) まで厳密値を報告した。特に \(n\le12\) では \(\rho_n=1\) だが、厳密な二次上界 \(b_k\le k^2\) は深さ13で不可能になる。

2. 特定のmodified greedy rulerは、

   \[
   b_k\le k^2\log_2(2k)
   \quad(1\le k\le680)
   \]

   を満たし、\(k=681\) まで全正差が重複しないことが厳密に検査されたと報告されている。従って自然対数による上記定義では

   \[
   \Lambda_1(1)=\cdots=\Lambda_{680}(1)=\frac1{\log2}.
   \]

3. \(k=681\) の失敗は**その構成だけ**の失敗である。全rulerに対するUNSATではなく、\(\Lambda_{681}(1)\) の下界でもない。

4. 数学的教訓は、問題に直接対応する有限プロファイルでさえ数百段にわたり自明な下限に張り付く点である。有限探索単独から漸近機構を推測するのは危険である。

### 3.3 残すべきproject-internal構造結果

1. **濃い平行移動ブロック接着は、実験した領域で阻害される** — `[COMPUTATIONAL / STRUCTURAL, NOT A THEOREM]`。

   添付ログのforbidden-position/difference-shadow実験では、濃い有限Sidonブロックに対する禁止位置密度がサイズ増加とともに1へ近づくことが報告されている。これは独立に作った濃いブロックを単純に平行移動して追加する戦略に対する強い反証的証拠である。

   **Wave 6 correction:** これは普遍的現象ではない。residue lift
   `A_L(B)={0,1,Lb_1,...}`では`A+Delta^+(A)`が高々4剰余類に入り、任意の
   長さ`H`の区間との交わりは`4 ceil(H/L)`以下である。従って高密度shadow
   はこのtested generic modelの観測としてのみ保持する。

   正しい解釈は次のとおり。

   - 検査した一般的なseparated-block方式を阻害する。
   - 代数的に協調したブロック、接頭辞全体の再設計、有限体塔、より強いalteration lemmaまでは排除しない。
   - \(F(V)\) の厳密な定義、全パラメータ、seed、raw outputを計算台帳に残す必要がある。

2. **O’Bryantのseparated-block deletion lemma** — `[RIGOROUS EXTERNAL]`。

   十分離した旧ruler \(V\) と新ruler \(W\) を統合するとき、最大

   \[
   g\binom{|V|}{2}
   \]

   個を \(W\) から除けば \(g\)-Golomb性を保てる。この方法は次ブロックを旧集合より圧倒的に大きくするlimsup構成には有効だが、Q2の全尺度polylog上界を直接与えない。

3. **アプローチ状態。** 

   - 単純な濃いblock gluing: `BLOCKED`。
   - Erdős/O’Bryant一尺度エネルギーの重み最適化: `CONSTANT-ONLY METHODとして飽和`。
   - 多尺度energy、martingale、entropy、全offset利用: `ACTIVE`。
   - 代数的に協調したnested construction: `ACTIVE`。
   - 有限プロファイル計算: `反証・予想生成用途としてACTIVE`。

---

## 4. 修正すべき矛盾・誤り・過剰主張

### 4.1 #1191ページの誤った関連リンク

#1191ページには「limsupについて#729を参照」とあるが、#729は階乗の整除性に関する無関係な問題である。Sidon集合のlimsupを扱う実際の関連問題は#329。

**措置:** #729をSidon関連文献として伝播しない。

### 4.2 古い衝突数計算の係数誤り

ブロック長 \(N\) について

\[
\sum_{d=1}^{N-1}(N-d)=\frac{N(N-1)}2.
\]

従ってoffset平均の**前**の総衝突数上界は

\[
g\frac{N(N-1)}2.
\]

\(N\) 個のoffsetで平均した**後**に初めて、あるoffsetで

\[
g\frac{N-1}{2}
\]

という上界を得る。平均前に後者を用いる導出は因子 \(N\) を落としている。

### 4.3 「681で失敗した」の過剰解釈

681での失敗は一つの構成に限定される。\(\Lambda_{681}(1)\) の不可能性でも、Q1の証拠でもない。

### 4.4 「有限の濃いブロックが無限問題を解く」という誤り

Singer、Bose–Chowlaなどの最適に近い有限集合を各尺度で作れても、cross-block differenceと接頭辞互換性を制御しなければQ2にならない。

### 4.5 「禁止密度が1に近いので全接着が不可能」という過剰主張

実験は一般的な平行移動方式への証拠であり、普遍的不可能定理ではない。公表可能な障害には、定量化された仮定・結論・証明が必要。

### 4.6 「O’Bryant 2026がQ1を解いた」という誤り

右辺は正の定数でありゼロではない。一尺度Cauchy/energyの定数は改善したが、Q1に必要な発散因子は得ていない。

### 4.7 非公開・未検証の証明主張

`arXiv:submit/...` しかない文書、公開preprintのないResearchGate upload、uniformityやdiagonalizationに未解決箇所がある導出を解決例として扱わない。

### 4.8 用語混同による除外

厳密な還元がない限り、次は核心台帳へ混ぜない。

- multiplicative Sidon sets
- 調和解析・コンパクト群のSidon sets
- random weighted Sidon sets
- prefix互換性を扱わない有限係数改善
- \(h=2,g=1\) に特殊化して新情報がない \(B_h[g]\) 一般化

---

## 5. 現在地から完全解決までの正確な壁

### 5.1 Q1の壁：cross-scale rigidity theorem

一尺度証明は、長さ \(N\) のブロックに分け、unique differenceからenergy上界、weighted Cauchyから下界を得る。重みの最適化だけでは定数しか変わらない。

Q1を証明するには、反対仮定

\[
a_n\le Cn^2\log n
\quad\text{for all sufficiently large }n
\]

の下で、各尺度のnear-extremizerが互いに整合できないことを示す必要がある。

有効な目標補題の候補は次。

1. **Multiscale energy gain:** 複数尺度のenergyの重み付き和に、unique-difference上界を最終的に上回る発散利得を与える。
2. **Stability incompatibility:** Cauchy近等号が強制するblock profile \(F_\ell\approx c(\ell\log(\ell N))^{-1/2}\) が、多数のnested/incommensurable scaleで同時成立できないことを定量化する。
3. **Martingale/entropy increment:** 入れ子区間分割に対する条件付き期待値のenergyまたはentropy増分が累積し、差分予算と矛盾することを示す。
4. **Cross-offset lower bound:** 平均後に一つのoffsetだけ選ぶ段階で捨てられるcovariance/consistencyを保持する。

### 5.2 Q2の壁：compatible extension/global construction theorem

ある固定 \(C,d>0\) について、任意の深さで

\[
b_k\le Ck^2(\log(2k))^d
\]

を満たす有限rulerの存在を示せば、コンパクト性で無限rulerを得る。欠けているのは終点密度ではなく接頭辞互換性。

有効な目標補題は例えば次。

> 任意の十分大きい許容接頭辞を拡張するか、有限範囲で再設計し、cross-scale differenceが失わせる候補点数を旧サイズの二次ではなく \(O(m\,\mathrm{polylog}\,m)\) に抑える。

候補構成は独立ブロックの平行移動ではなく、差を代数的に協調させる必要がある。

---

## 6. 次に行うべき高価値作業

### Priority A — survival-conditioned nonzero couplingを証明する

1. Wave 9のscalar equivalence
   `(4/49)sum V_(2^k)<=B_H<=(36/35)sum V_(2^k)`を出発点にし、matrix成分へ
   戻らない。
2. Wave 11のtermwise triangular floor
   `K_m^len=2log m+O(1)`とexact identity
   `T_m-K_m^len=Y_m+G_m^len+S_m`を最新の出発点にする。Wave 10の
   weighted incomplete-DTS、cut-kernel tail、global `7/4` spectrum lawは
   保存済み基礎だが、先頭`1/4`不足は解消済みである。
3. Route A/P17では、一つのfixed infinite eventual-`C` branch上で、ある
   `epsilon_J>=0`, `epsilon_J=o(log J)`について
   `G_J^len+S_J>=T_J-K_J^len-epsilon_J`を証明する。これはexactに
   `sum Y_m=o(log J)`と同値。`K^len`は項別floorなのでfanwise global
   allocationは不要であり、overlapする`K^mix`と加算してはならない。
4. Route Bでは、endpoint-limited `R^2XY`とdifference-limited `R^2Z^2`を
   full bi-/tri-treeのtensor weightへ正しく符号化し、arbitrary positive
   measureにsparsityを置く。one-box constantに必要なsummable/Dini-type
   profileをcontiguous-sum uniquenessとsurvivalから導く。Route Aとの
   同値性は未証明。
5. `surv_C(P)=infinity`を明示して、terminal-dependent E–T windowと有限
   extension depthを排除する。pruned-tree theoremをproduct theoremへ
   誤適用しない。
6. objectiveはexact `h_i h_j Phi_(ij)/N_(2m)^2`またはprimitive Abel stateを
   保持し、linear difference length、raw cardinality、独立factorial boundへ
   置換しない。
7. Wave 4--11の全反例とno-goで敵対検査し、finite dualを
   infinite-survival theoremへ昇格しない。

旧`computation/crossblock.py`修復と有限体構成探索はQ2の二次目標として
残すが、未添付artifactやgeneric blockでの高shadow密度をQ1の普遍的
上界として使ってはならない。

### Priority B — Q1用の明示的multiscale identity

尺度 \(N_j\)、重み \(\lambda_j\ge0\)、全offsetのblock count \(F^{(j,t)}_\ell\) に対して、境界項込みで

\[
\sum_j\lambda_j
\sum_{t=0}^{N_j-1}\sum_\ell
\binom{F^{(j,t)}_\ell}{2}
=
\sum_{\{a,b\}\subset A}
\sum_j\lambda_j\bigl(N_j-|a-b|\bigr)_+
\]

または正確な局所版を導く。

その上で、

1. 右辺kernelを最適化する。
2. 仮定した全尺度密度から下界を出す。
3. \(\log\log\)、反復対数、その他の発散利得が残るか判定する。
4. 有限kernel最適化のextremizerを計算する。
5. 利得が消える場合のstability theoremを定式化する。

これは一尺度重み変更ではなく、古典証明を直接多尺度化する。

### Priority C — Q2用の構造的互換構成

優先順は次。

1. nested/tower-compatible SingerまたはBose–Chowla
2. Cilleruelo mixed-radix discrete-log構成のadaptive scale化
3. codegreeを利用するconflict-hypergraph alteration/nibble
4. finite-field/function-field towerとtrace/norm互換性
5. cross-scale difference signatureを持つblock label
6. \(\Lambda_n(d)\) 上界下での接頭辞全体の有限最適化

全提案について、密度評価より先にcross-differenceの全分類を証明する。

### Priority D — 証明を直接導く計算

1. near-critical finite rulerでO’Bryant Cauchy defectとblock-profile shapeを多数尺度で測定する。
2. scale \(N\) のnear-extremizerが \(2N,3N,\lfloor N^{3/2}\rfloor\) でもnear-extremalか検査する。
3. dyadic partitionのmartingale energy・entropy incrementを測る。
4. SAT/CP-SATは構造・反例生成に限定する。
5. finite UNSATはfinite theoremとしてのみ記録し、一様補題なしに漸近主張へ上げない。

---

## 7. 歴史的・将来用の推奨構造（現パッケージ実体ではない）

以下は初期段階で提案されたaspirational layoutであり、現在のinventoryや
実在pathを表さない。現パッケージの正確な配置は`HANDOFF_MANIFEST.md`と
`FILE_INVENTORY.txt`を用いる。特に`NEXT_FULL_SOLUTION_PROMPT_EN.txt`と
`computation/` treeは本パッケージには存在しない。

```text
erdos1191-research/
├── 1191_MASTER_STATUS.md
├── NEXT_FULL_SOLUTION_PROMPT_EN.txt
├── research_log.md
├── approach_registry.md
├── proof_obligations.md
├── counterexamples.md
├── literature_ledger.md
├── computation/
│   ├── crossblock.py
│   ├── tests/
│   ├── manifests/
│   ├── raw_results/
│   └── certificates/
├── sources/
│   ├── primary/
│   └── metadata/
└── archive/
    ├── superseded_reports/
    ├── duplicate_exports/
    └── unverified_claims/
```

### 配置方針

- **Canonical:** master status、各ledger、コード、tests、manifest、certificate。
- **Supersededとしてarchive:** 内容をmasterへ統合済みの旧説明報告。
- **Duplicateとしてarchive:** hash一致する貼付Markdown/PDF/ZIP export。
- **Unverifiedとしてarchive:** 非公開submission token、未完成proof claim、未解消gapを含む計算。
- **削除しない:** raw output、counterexample、失敗アプローチ、source snapshot。

元添付が利用可能になったら、まずSHA-256で重複除去し、次にPDF/Markdownのmetadataや改行だけが異なるものをnormalized-text hashでまとめる。

---

## 8. Wave 0--2 時点の歴史的結論

このプロジェクトは次の4点で実質的に前進している。

1. 両問いを互換有限接頭辞問題へ正確に還元した。
2. 二次プロファイルとcritical-log envelopeを有限範囲で厳密に校正した。
3. 単純な濃いblock gluingに具体的障害を発見した。
4. 完全解決に欠けるものを明確化した。
   - Q1: cross-scale rigidity inequality
   - Q2: compatible algebraic extension/global construction theorem

しかし、どちらの問いも未解決である。この節が掲げたQ1の多尺度
energy/entropy theoremとQ2の代数的互換構成は上位方針として残るが、
運用上の現在の単一目標はWave 7で具体化した§11.5である。

---

## 9. 一次資料監査台帳

1. P. Erdős, *A Survey of Problems in Combinatorial Number Theory*, Annals of Discrete Mathematics 6 (1980), 89–115, printed p. 98.
2. I. Z. Ruzsa, *An Infinite Sidon Sequence*, Journal of Number Theory 68 (1998), 63–71, DOI 10.1006/jnth.1997.2192.
3. J. Cilleruelo, *Infinite Sidon Sequences*, Advances in Mathematics 255 (2014), 474–486, DOI 10.1016/j.aim.2014.01.011; arXiv:1209.0326.
4. K. O’Bryant, *A Complete Annotated Bibliography of Work Related to Sidon Sequences*, Electronic Journal of Combinatorics DS11 (2004), DOI 10.37236/32.
5. K. O’Bryant, *On the Thickness of Infinite Generalized Sidon Sets, I*, arXiv:2606.28651v3.
6. K. O’Bryant, *On the Thickness of Infinite Generalized Sidon Sets, II*, arXiv:2607.23795.
7. C. Táfula, *Infinite Sidon-type Sets for Zero-sum Linear Forms*, Monatshefte für Mathematik (2026), DOI 10.1007/s00605-026-02211-4; arXiv:2607.20753.
8. Erdős Problems #1191 and #329. #1191から#729への参照は誤り。
9. *Erdős Problem a Day*, #1191 working report, 2026-07-28 — 二次的な再現・監査資料として使用。

### 検索方法上の注記

通常検索、arXiv、Exa、SciSpace、Firecrawl、MathOverflow、EuDML、および他の指定DBへの公開index検索を実行した。Consensusは呼び出したが月間検索枠を使い切っており、証拠となる結果は得られなかった。今回の公開検索ではMathSciNet/zbMATHの直接結果ページを網羅的に取得できなかったため、決定的主張は原論文、journal metadata、Erdős原典で照合した。


---

## 10. 2026-08-28 endpoint-variance前進と現在の第一目標

### 10.1 Project-internal exact finite theorem

有限集合 `A` とmodulus `N` に対し、差 `b-a<N` のpairから residue multigraph

\[
a\bmod N\longrightarrow b\bmod N
\]

を作り、端点不均衡を

\[
\delta_N(r)=\operatorname{outdeg}(r)-\operatorname{indeg}(r)
\]

とする。translated `N`-block partitionのsame-block pair energy `E_N(r)` について、boundary loadの前進差分は厳密に `delta_N` であり、

\[
\operatorname{Var}_{r\bmod N}E_N(r)
=\|\delta_N\|_{H^{-1}(\mathbb Z/N\mathbb Z)}^2.
\]

ゼロ分散はshort-pair residue graphが各頂点でbalanced、すなわちEulerianであることと同値。`{0,1,N}` はexact two-edge zero modeである。

### 10.2 Diameter regime

`A={a_1<...<a_m}`、`diam(A)<N`、`g_k=a_{k+1}-a_k`なら、boundary loadはgap `(a_k,a_{k+1}]` 上で `k(m-k)`。よってexact gap-moment formulaが成り立ち、

\[
\sum_r\delta_N(r)^2=\frac{m(m^2-1)}3,
\]

さらにmandatory levelsから

\[
\operatorname{Var}E_N\ge
\frac{m(m^2-1)(m^2+11)}{180N}.
\]

critical prefix `N\asymp m^2\log m` では少なくとも `m^3/log m` のorderを強制する。

**Sharpnessの範囲に注意:** 等号例 `A={0,1,...,m-1}`, `N=m` は `m>=3` でSidonではない。従って一般有限集合としてsharpであり、Golomb ruler classでの最小値は未決定。

### 10.3 Difference spectrumからの分離

homometric Sidon rulers

\[
\{0,1,4,10,12,17\},\qquad
\{0,1,8,11,13,17\}
\]

は同じpositive-difference spectrumを持つが、`N=14` でvarianceが `79/28` と `55/28` に分離する。従ってendpoint varianceはdifference multiplicitiesだけに依存するglobal mean kernel barrierを越える。

### 10.4 残る壁

大きなprefix varianceを、多数のprefix・nested/incommensurable moduliで結ぶ**Sidon upper budget**が未証明。単一scaleでvarianceが大きいだけでは矛盾しない。現在の最強の下界は、隣接gapの相異性と二段階agingだけで得られる

\[
\frac{\operatorname{Var}C_{N_M}(A_M)}{M^4}
\ge \frac{9M^2-256}{1\,048\,576N_M},
\]

および臨界包絡下のdyadic和 `Omega_C(log J)` である。共分散行列更新は
正のcross-prefix invariantを与えるが、それ自身は上界を与えない。

これは現在も有効な上位目標だが、Wave 7の運用上の最重要目標は
§11.5の無限生存条件付きdebt-repayment定理へ具体化されている。

> critical envelope `a_m<=C m^2 log m` が強制するweighted multiscale endpoint varianceの下界と、global unique differencesから得られる上界が発散的に衝突する anti-Eulerian multiscale lemma を証明する。

候補は covariance-matrix innovations の総量制御、quartic pair-pair kernelの
符号付きshell相殺、nested-modulus cycle packing、martingale/entropy
increment、および contiguous-gap uniqueness を使う長距離chargeである。

### 10.5 Reproducibility status

endpoint-variance artifactsは本パッケージで再現可能。旧ledgerが参照する `computation/crossblock.py` 等は添付に存在しないため、旧block-gluing実験は `[COMPUTATIONAL — REPORTED, ARTIFACTS MISSING]` として扱う。

---

## 11. Wave 7 完全出生台帳・無限生存境界

### 11.1 現在の最強arithmetical ledger

dyadic epoch `m`のold--new全lag `1<=k<2m`とnewborn内部pairを合わせると、
terminal `M=2^J` prefixの全`binom(M,2)` pairを出生epochごとにちょうど一度
分割する。family `F`の需要、rank lag、上側閾値を`q_F,ell_F,gamma_F`と
すると、rank floorとの結合により

\[
\sum_{\ell_F\ge K}q_F1_{\{\gamma_F\le T\}}
\le\max(0,\lfloor T\rfloor-K(K+1)/2+1)
\]

および

\[
\boxed{\sum_F q_F\ell_F/\gamma_F^2\le8\sqrt2}
\]

を得る。これは一つの無限Golomb履歴上で総和可能な正確なpotentialである。

### 11.2 有限窓no-goと量化境界

`p=1423`の512点Erdős--Turán rulerでは厳密に
`Q_(256),00/N_512>W_2(256)`。さらにterminalごとに変わるrecent windows
ではadjoint innovationが`R/360+o(R)`と発散する一方、`sum W_2=o(1)`。
従って固定定数affine支配は成立しない。ただし各terminalでprimeとprefixが
変わるため、一つの無限critical履歴を仮定する定理は反証されない。

正の有理数`C`とfinite prefix `P`に対し、同じcritical cap内のGolomb拡張木
の高さを`surv_C(P)`と定義する。有限分岐König補題により
`surv_C(P)=infinity`は、同じ`P`が一つの無限eventual-C-critical Golomb列に
属することと同値。これが次の定理で使う正確な非局所ラベルである。

### 11.3 renewal probeと残るdebt

- local renewal-hole RHは`[21,22]`（別epoch二点）でmargin `-1`となり反証。
- direct harmonic tax HTはthreshold 3でmargin `-1/6`となり反証。
- epoch-size tax ESTは全normalized 8点Golomb rulerまで無条件に成立。
  forced failure regionでは4,934 parent、3,341,161 ruler、37,423,576 nodeを
  完全列挙した。64/128点認証fixtureと23 single-swap変形でも生存するが、
  その大サイズ範囲は非網羅。
- 128点fixture、`T=1198199/32`ではEST tax 120に対しgenuinely new adjacent
  chargeは57だけで、未払いdebtは63。nested old halvesの重なりを
  non-adjacent差またはcapacity slackで返済する定理が未証明。

### 11.4 gluingと文献境界

O'Bryant Lemma 9を最悪削除数`binom(n,2)`だけでblack-box反復すると、最初の
new prefixが`Omega(n^4)`へ跳び、固定critical envelopeを最終的に破る。
`C=1`では全`n>=8`で解析的に閉じる。これはstructured low-conflict blockや
新しいmixed-difference gluingを排除しない。

Wave 7文献監査はOpenAlex/Crossref/arXivの14成功roundから316重複除去recordを
保持し、採用定理は一次資料本文で照合した。該当するcritical all-prefix tower
またはinnovation budgetは確認できなかったが、これは限定検索のqualified null。
Consensusは30/30 quota、SciSpaceは隣接結果と壊れた重複metadata、Firecrawlは
generic listingのみという制限を記録した。

### 11.5 現在の単一主目標

一つの無限critical Golomb列で`surv_C=infinity`を明示的に使い、old-cheap
renewalのoverlap debtを未使用non-adjacent差または同等の整数capacityで返済し、
そのchargeがactual newborn-shell/mixing innovationを量的に支配することを証明して

\[
\sum_{j\le J}\langle H,Q_j/N_{2m_j}\rangle=o(\log J)
\]

を得る。Q2の副経路は、一様座標capを満たすfinite rulerを任意深さで実現し、
König補題で無限枝を得ることである。どちらも未証明。現在statusは
`UNRESOLVED_AT_HARD_LIMIT`で、賞金請求は不可。

---

## 12. Wave 8 正の出生予算への最終縮約

### 12.1 adjacent debtの解消範囲

actual newborn internal familyとWave 6 cross familyは全epochでpair-disjointで、
同一thresholdの総需要は整数capacity以下。各epochではactual-new payまたは
old-ancestry clearが必ず起きるので、一つのhistory上の未払いinternal familyは
高々一つである。exact shell square expansionの負adjacent atomsは二つのendpoint
gapだけで、critical cap下の全dyadic和は有限。従ってWave 7のnested adjacent
debtは主障壁ではなくなった。

### 12.2 actual innovationの残るatoms

`Q_m`は全newborn-right pairの正項とall-old pairの負項に正確に分解される。
shell covarianceの負係数はproper left-prefix/right-suffix fanだけで、strict
bulkとfull spanは正である。rank-one termは別のAbel boundary fanを持つ。
positive square envelopeでは全genuine atomがglobally uniqueなnon-adjacent
Golomb differenceとなり、人工`h_0` rowの総和は`92/315`以下。ただしdifference
の二乗momentをsublogarithmicにする定理は未証明。

### 12.3 pair telescopeと新しい単一主目標

各pairのbirth termから全将来のold-pair負項を引いてもbirth chargeの半分以上が
残る。従ってpositive birth budgetを`B_H(J)`とすると

\[
\boxed{
\frac12B_H(J)
\le\sum_{j\le J}\langle H,Q_j/N_{2m_j}\rangle
\le B_H(J).}
\]

exact finite-horizon adjointでもsigned sumは正のfuture `E`-energy tailに一致する。
よってcancellation routeは定数因子を超えて改善できない。現在の単一主目標は

\[
\boxed{B_H(J)=o(\log J)}
\]

を、一つの無限eventually-critical Golomb列について証明すること。必要なのは
全contiguous-sum一意性を使うmagnitude/rank-lag二変数のbounded-overlap chargeで
ある。local `U/T`、latest-shell density、raw non-adjacent count、rank-one対shell
定数比較には反例がある。

### 12.4 Q2と文献境界

Hegyvári有限parabola blockはaffine variantsを含めGolombだが、separated splice
はinternal difference spectraのdisjointnessと同値。任意prefixへの無条件splice
はcritical scaleで立方endpointを与え、fixed finite menuはuniversal spansを持つ
old rulerで阻止できる。従ってcompatible all-prefix constructionは未解決。

Wave 8限定監査は550重複除去recordを保持し、Exa、Firecrawl、SciSpace、
Consensusの制限を明記した。必要なpositive birth budgetまたはcritical towerは
確認できなかったが、検索saturationは未達でありqualified nullのみ。Q1/Q2とも
未解決、statusは`UNRESOLVED_AT_HARD_LIMIT`、賞金請求は不可。

---

## 13. Wave 9 scalar rank varianceとsurvival-conditioned core

### 13.1 exact scalar equivalence

`nu_n=N_n^(-1)sum_(i<n)h_i delta_(i/n)`、`V_n=Var_(nu_n)(u)`とする。
一step scalar birthは

\[
R_m=V_{2m}-{1\over4}\left({N_m\over N_{2m}}\right)^2V_m
\]

で、fixed-`H` kernelのscalar factorは`16/147`から`36/35`。従って

\[
\boxed{{4\over49}\sum_{k=1}^{J+1}V_{2^k}
\le B_H(J)\le{36\over35}\sum_{k=1}^{J+1}V_{2^k}.}
\]

これはalgebraicでGolomb性を使わない。Golomb性からは逆に、distinct genuine
adjacent gapsだけで`V_n>=n^2/(512N_n)`を得る。critical cap下ではP15に必要な
upperと明示`Omega_C(log J)` lowerが衝突するため、non-adjacent contiguous-sum
uniquenessが唯一の不足情報である。

### 13.2 coreとfinite no-go

`theta_j^2=eta_j=1/(j log j)`により、short-rankまたはsmall-endpoint atomsは
全体で`O(log log J)`。残るcoreはlong rank、two large endpoints、globally
unique interval differenceを同時に持つ。`(R,X,Y,Z)` tileにはendpoint-band、
integer magnitude capacity、interval-overlapのexact min boundがあるが、local
summationではlogarithmic slackが消えない。

complete finite probeは4点1,672件、bounded 8点`C=1` 1,146件を監査し、
pointwise decay、literal harmonic schedule、static 2-variable cell injectionを
反証。long finite fixturesではmacroscopic core shareが`3/5`超。これらは
infinite survivalを証明しない。

### 13.3 primitive cross ratio

non-adjacent gapsに

\[
C_{ij}=\log{(M+h_i)(M+h_j)\over M(M+h_i+h_j)}
\]

を割り当てると`h_i h_j/D_ij^2<=C_ij`。quadratic-rank sumはexact Abel
formulaを持ち、interior coefficientsは全てnegative。strict-interior gcd
`delta_n^circ=gcd(h_2,...,h_(n-2))`でprimitive化し、distinct differencesへ
rearrangement inequalityを使うと

\[
S_n\le\left({n-2\over n}\right)^2
\log{a_{n-1}\over\delta_n^\circ}-{I_{\min}\over n^2}
=\log{a_{n-1}\over\delta_n^\circ n^2}+1+\log2+o(1).
\]

`delta_n^circ`は固定branch上でeventually stable。ただしcritical capではこの
state boundは`O(log log n)`に留まる。`(D/N)^2`を保持したpotentialもexact
dyadic recursionを持つが、birth sumはpositive state sumに定数因子で同値。

### 13.4 literature interfaceと次の定理

Wave 9 stateは750 records、31 queries。Ma--Yi/Shearerから任意のfinite epoch
set `E`について

\[
{M_E(M_E+1)\over2}\le
\sum_{m\in E}N_{2m}{q_m(q_m+1)\over2},\qquad
M_E=\sum_{m\in E}m q_m
\]

を導いた。これはone nested branch上で厳密だがlinear-only。次の単一目標は
`surv_C=infinity`を条件とするlong-rank/two-large-endpoint coreの
cross-epoch non-saturation。laminar weighted incomplete-DTS LPのuniform dual
または同値なprimitive cross-ratio Carleson theoremが必要。未証明であり、
statusは`UNRESOLVED_AT_HARD_LIMIT`、賞金請求不可。

---

## 14. Wave 10 laminar log-product lawとfrontier obstruction

### 14.1 weighted incomplete-DTSとcut kernel

任意のfinite dyadic epoch setと任意のweighted interval familyについて

\[
\sum_r r\beta_r\leq\sum\lambda_{m,j,s}(a_j-a_{j-s})
\leq\sum_m N_{2m}\Gamma_m
\]

を証明した。W9-RLPはunit lag rectangleの場合。全選択差の積は`M!`以上で、
rational weightなら分母を払ったexact integer product certificateになる。

さらに任意のgap cut `t`で

\[
\sum_{i<j,\ i\leq t\leq j}{h_i h_j\over D_{i,j}}
\leq(\log2+1/e)a_g
\]

なので、固定位置へのfuture dyadic loadは`O(4^(-K))`。これはmassをmoving
frontierへ局在させるが、全gapへ積分すると一epoch `O(1)`でありP15ではない。

### 14.2 global Abel spectrumの最適主項

negative non-full bulkのright endpointsは各dyadic `m`で`[m-1,2m-2]`。
従って全epochの対応差はglobalにdistinct。係数multisetを全体でsortした
rearrangement floor `F_E`は

\[
F_E={7\over4}\sum_{m\in E}\log m+O(|E|)
\]

である。threshold count `#{beta>=tau}<4/tau`がglobal upperを与え、各shell
floorの和がlowerを与える。critical cap後の表示certificateは連続dyadic
`K` epochsで`Theta(K^2)`のleading termを残す。これはactual energyが
`Theta(K^2)`という主張ではない。

### 14.3 finite LPと文献境界

all-subset/all-cutoff W9-RLP DPは128点まで9,845,549 choicesをexactに監査し、
違反0。tile LPは全tested blockでexact primal=dual。しかしfixed modulus後の
W9-RLPはtile variablesにzero coefficientsなので、両制約の単純併置は
optimumを変えない。

一次文献ではfull bi-/tri-tree上のtensor-product weightに対する
box-to-embedding theoremが最も近い。P15 atomのpositive-measure encodingと
vanishing box estimateは未証明。pruned sub-bi-treeとT^4の既知障害は
naive pruning/direct four-parameter extensionを許さない。qualified nullのみ。

### 14.4 exact next target

`A_J,Q_J,T_J,F_E`を上の定義とし、`P_J=A_J-F_E`,
`S_J=2T_J-Q_J>=0`, `U_E=T_J-F_E`と置くと、exactに
`sum Y_m=U_E-P_J-S_J`。一つの`surv_C=infinity` branch上で
`0<=U_E-P_J-S_J<=epsilon_J`, `epsilon_J=o(log J)`を証明することが
Abel routeの十分条件である。bulk-onlyまたはlower-shell-only repaymentは
さらに強い候補で、必要条件とは未証明。別の十分条件候補としてfull
product-tree encodingとsummably vanishing box constantを証明してもよい。
両routeは同値とは未証明だが、どちらもendpoint/Abel variablesと
rank-lag/survival dataを同一不等式でnonzeroに結合しなければならない。

30 focused tests、Ruff、exact certificate replayは通過。P15、Q1、Q2、
賞金請求は未解決。

---

## 15. Wave 11 triangular interval floor と secondary survival frontier

### 15.1 missing leading quarter の完全回収

**[RIGOROUS — SELF-CONTAINED]** Golomb ruler の隣接gap自体が互いに異なる
正整数なので、長さ `ell=q-p+1` の任意interval差について

\[
D_{p,q}\geq1+2+\cdots+\ell={\ell(\ell+1)\over2}
\]

が成り立つ。これをexact Abel bulk係数へ項別適用したfloor
`K_m^len`は

\[
K_m^{\rm low}={1\over2}\log m+O(1),\qquad
K_m^{\rm int}={3\over2}\log m+O(1),\qquad
K_m^{\rm len}=2\log m+O(1).
\]

従ってWave 10のglobal rearrangement floor `F_E`との差は
`K_E^len-F_E=(1/4)sum_(m in E)log m+O(|E|)`であり、先頭`1/4`の
不足は無条件かつ局所的に回収された。lower shellだけに長さfloorを使い、
残る`q>=m`だけをglobal sortする別のdisjoint certificate `K^mix`も同じ
主項を持つが、両certificateを重複加算してはいけない。

### 15.2 exact three-channel identity

**[RIGOROUS — SELF-CONTAINED]**
`G_m^len=A_m-K_m^len>=0`とおくと、境界slack `S_m>=0`およびcross-ratio
energy `Y_m>=0`に対し

\[
T_m-K_m^{\rm len}=Y_m+G_m^{\rm len}+S_m
\]

が各epochでexactに成り立つ。従って

\[
\sum_{m\in E_J}Y_m=(T_J-K_J^{\rm len})-(G_J^{\rm len}+S_J).
\]

complete dyadic bulk triangleについては、数値hole、係数/rank permutation、
containment-rank surplusもすべて非負項としてexactに分解済みである。

**[CONDITIONAL]** 一つのfixed infinite eventually-`C`-critical branch上で
直接得られるのは

\[
0\leq\sum Y_m\leq T_J-K_J^{\rm len}=O_C(J\log J)
\]

までである。Wave 10の表示certificateの`O_C(J^2)`主項は消えたが、P15に
必要な`o(log J)`には届かない。

### 15.3 exact obstruction と文献境界

**[RIGOROUS — SELF-CONTAINED]** lower-shell residualはpositive future
cross-ratio tailにexactに等しい。しかし固定pair `(i,j)`はdyadic epoch和で
`Theta(log(j/i))`回重なるので、一つのbirth atomへのuniform same-pair charge
は不可能である。

**[COMPUTATIONAL — CERTIFIED FINITE]** 全1,146個の8-mark all-prefix-`C=1`
rulerでbulk-only、boundary-only、all-hole-only、lower-hole-quarter、
zero-residualの各literal候補は全件失敗した。changing Erdős--Turán familyでも
new floor後の比は正の定数帯に留まる。これはlocal mechanismの反証であり、
一つの無限枝上のaggregate theoremの反証ではない。

**[LITERATURE STATUS — PUBLIC RECORD ONLY]** 26 scripted scholarly requests、
351 deduplicated papers、Exa、Firecrawl、SciSpaceの横断監査では、要求する
nested secondary repayment theoremは確認できなかった。within-lengthの
shifted-factorial改善のtriangular floorからの増分は一shell
`O(m^(-1/2))`だけで、dyadic総和`O(1)`。2025 finite-diameter theoremの
`O(m^(-1/2))`は`2log m`主項に対する下位補正であり、total-diameterだけでは
cross-length/survival stateを持たない。overall saturationはfalseなので、
これはqualified nullでありnovelty claimではない。

### 15.4 exact next target

P17として、一つのfixed infinite eventual-`C` branch上で

\[
G_J^{\rm len}+S_J\geq T_J-K_J^{\rm len}-\epsilon_J,
\qquad \epsilon_J=o(\log J)
\]

を証明する。これは`0<=sum Y_m<=epsilon_J=o(log J)`と同値である。必要なのは
cross-length allocation、future-tail telescope、または真にsurvival-conditioned
なstateであり、別のwithin-length sort、global diameter、finite windowではない。
別routeとしてfull bi-/tri-tree positive-measure encodingとsummably vanishing
product-box profileも残るが、Route Aとの同値性は未証明。

Wave 11 focused testsは独立再実行で7件通過。P15、P17、Question 1、
Question 2、賞金請求は未解決。総合状態は`UNRESOLVED_AT_HARD_LIMIT`。

## 16. 2026-08-29 continuation — Wave 12 cut renewal と整数格子境界

### 16.1 positive cut-renewal theorem

**[RIGOROUS — SELF-CONTAINED]** Wave 11 の positive future tail

\[
R_m=\sum_{i=1}^{m-2}\left({m-i\over2m}\right)^2
          \sum_{j=m}^{\infty}C_{ij}
\]

を用いると、4つの明示的非負sector
`Z_m^ob,Z_m^nb,Z_m^of,Z_m^mf`の和`Z_m`について

\[
Y_m=R_m-R_{2m}+Z_m
\]

が各`C_(i,j)`の係数比較だけでexactに成り立つ。従って

\[
\sum_{m\in E_J}Y_m
=R_4-R_{2^{J+1}}+\sum_{m\in E_J}Z_m.
\]

各fixed pairに対する`Z`係数のdyadic和は一様有界であり、Wave 11のraw
tailで現れた`Theta(log(j/i))` overlapは解消された。これは重要な改善だが、
異なるpairs全体のcross-ratio massをまだ制御していない。

### 16.2 rank + length + full containment の限界

**[RIGOROUS — SELF-CONTAINED]** numerical rank、triangular length floor、
全interval-containment posetを同時に満たすlinear extensionの中で最良の
floorを`K_J^inc`とする。epoch順、同一epoch内length順の明示的extensionと
exact atom count `B(m)=2m^2-5m+2<2m^2`から

\[
0\leq K_J^{\rm inc}-K_J^{\rm len}<5|E_J|
\]

を得た。従って、この3種類の独立ordering情報を全部使っても、secondary
`sum log log m` repaymentには足りない。このno-goはcrossing intervalの
加法関係、整数unit spacing、またはsurvival couplingを排除しない。

### 16.3 real Golomb countermodel と必要な算術

**[RIGOROUS — SELF-CONTAINED]** real marks
`a_n=n^2+sqrt(2)n`は全正差が相異なりquadratic growthを持つが、

\[
Y_m\longrightarrow {3\over2}(\log2-1/2)>0.
\]

従って、abstractなdifference uniqueness、order、quadratic growth、exact
cross-ratio algebraだけではP17は出ない。この例は**非整数**であり、
Erdős #1191への反例ではない。次の証明は整数unit spacingまたはそれと同値な
arithmetic packingを明示的に使わなければならない。

### 16.4 certified computation と文献境界

**[COMPUTATIONAL — CERTIFIED FINITE]** 独立なrational coefficient oracleと
formal-log oracleがrenewal identityを照合した。focused suiteは7 testsを通し、
certificateは全1,146個の8-mark all-prefix-`C=1` rulers、64-mark fixture、
独立128-mark ruler、epoch 128までの32,130 containment atomsを監査した。
certificate file SHA-256は
`e5645101d5150910de428b7184d504b1a9b90ac411c1b007be743e43e65aecc9`。
これは有限代数検査であり`surv_C=infinity`の証明ではない。

**[LITERATURE STATUS — QUALIFIED NULL]** Exa、Firecrawl、SciSpace、
Consensus（quota blocked）、arXiv primary textを使ったdeltaでは、fixed-ray
integer renewal packing theoremは確認できなかった。Martikainen
`arXiv:2608.22628`はcritical two-depth product packingの鋭いRoute B template
だがSidon encodingを持たない。Chen--Fang
`10.1016/j.jcta.2026.106239`はSidon setを密度を保つperfect difference setへ
変換するが、input elementsの削除とnew elementsの挿入を行うためprescribed
prefix survivalではなく、Q2へ使うには既にQ2密度のinputが必要になる。
qualified nullはabsence/novelty claimではない。

### 16.5 historical Wave 12 target（Wave 13で再分類）

P18として、一つのfixed infinite eventually-`C` **integer** Golomb branch上で

\[
\sum_{m\in E_J}Z_m=o_C(\log J)
\]

を証明することをWave 12では次の十分条件とした。これによりP17が従う。priorityはdifferent-pair integer packing、
crossing interval-sum relations、または同じ算術を保持するfull product-tree
encodingとしたが、次節のWave 13 theoremにより、このP18はQ1と同値な
contradiction statementへ再分類された。P15、P17、P18、Question 1、Question 2、賞金請求は未解決。
総合状態は`UNRESOLVED_AT_HARD_LIMIT`。

## 17. 2026-08-29 continuation — Wave 13 harmonic barrier と signed frontier

### 17.1 integer new-birth の普遍的下界

**[RIGOROUS — SELF-CONTAINED]** dyadic `m>=4`について、suffix gap集合
`G_m={m-1,...,2m-1}`と

\[
H_m=\sum_{r=m-1}^{2m-1}h_r=a_{2m-1}-a_{m-2}
\]

を置く。`G_m`は正確に`m+1`個の互いに異なる正整数gapを持つ。各
`k in G_m`から距離`r`以上にあるgapの個数をlayerごとに数え、

\[
E_m=\sum_{r=2}^{m/2}(2r-1)
 { (m+2-2r)(m+3-2r)\over2}
 ={m(m-2)(m^2+8m+6)\over48}\ge {m^4\over48}
\]

を得る。product floor
`C_(i,j)>=h_i h_j/D_(i,j)^2`と`D_(i,j)<=H_m`を組み合わせると、Wave 12の
new-birth sectorについて

\[
\boxed{
Y_m\ge Z_m^{\rm nb},\qquad
Z_m\ge Z_m^{\rm nb}
\ge {E_m\over8m^2H_m}
\ge {m^2\over384H_m}.}
\]

これは有限prefixごとの無条件整数定理であり、無限branchの存在を仮定しない。

### 17.2 critical branchを仮定したharmonic barrier

**[CONDITIONAL]** 一つのfixed infinite branchがeventually
`a_n<=C n^2 log(2n)`を満たすなら、十分大きいdyadic `m`で

\[
Y_m,Z_m>{1\over1536C\log(4m)}.
\]

従って

\[
\liminf_{J\to\infty}{\sum_{m\in E_J}Y_m\over\log J},
\quad
\liminf_{J\to\infty}{\sum_{m\in E_J}Z_m\over\log J}
\ge {1\over1536C\log2}.
\]

このため、全`C>0`と全fixed branchを量化したP17の`sum Y=o(log J)`、
P18の`sum Z=o(log J)`は、どちらもQuestion 1と論理的に同値である。
Q1が真なら仮定を満たすbranchがなくvacuousであり、いずれかのlittle-ohを
証明した状態でQ1が偽なら、反例branchが上のharmonic lower boundと矛盾する。
これはQ1の証明ではなく、P17/P18を「より易しい中間補題」と見なせないことを
示すexact reductionである。

### 17.3 terminal tailを残したexact signed target

Wave 12のtelescoping identityから、P17のcancellation-faithfulな形は

\[
\boxed{
\sum_{m\in E_J}Z_m-R_{2^{J+1}}=o_C(\log J)}
\]

である。`R_4`はfixed constantとしてlittle-ohへ吸収される。`sum Z`自体には
harmonic lower boundがあるため、hypothetical critical branch上でP17を扱うなら
terminal `R`がその質量を吸収しなければならない。ただし`sum Y`にも同じ下界が
あるので、このsigned assertionを全branchについて証明すること自体がQ1の証明と
同値であり、ここでは未証明である。

### 17.4 exact frontier spectrum

**[RIGOROUS — SELF-CONTAINED]**
`endpoint_variance/WAVE13_FRONTIER_SPECTRUM_AND_SIGNED_REPAYMENT_2026-08-29.md`
は各epochで

\[
Z_m=\mathfrak P_m+\mathfrak U_m-
    \mathfrak B_m-\mathfrak F_m-\mathfrak e_m
\]

という有限interval-log spectrumをexactに導出した。prefix/full-span channelは

\[
0\le Z_m\le X_m+\varepsilon_m,\qquad
X_m=\mathfrak U_m-\mathfrak B_m,qquad
\varepsilon_m={4m-3\over16m^2}\log a_{2m-1}
\]

とone-sidedに除去でき、critical cap下で`sum epsilon_m<infinity`である。一方、
new-birth barrierにより

\[
\sum_{m\in E_J}X_m
\ge {\log J\over1536C\log2}-O_{C,\mathbf a}(1).
\]

従ってterminal suffix fanはinterior descendantsをharmonic量だけ上回る。
within-epoch positive packingでfrontierをsmallにする方針は閉じ、必要なのは
この下界と矛盾するgenuinely cross-epoch arithmetic upperか、terminal tailを
保持するsigned cancellationである。

### 17.5 lattice-cell / central-rank no-go

**[RIGOROUS IDENTITY + CERTIFIED FINITE DIAGNOSTICS]** cross ratioには

\[
C_{ij}=\sum_{s=0}^{h_i-1}\sum_{t=0}^{h_j-1}
\log{(M+s+t+1)^2\over(M+s+t)(M+s+t+2)},
\quad M=D_{i+1,j-1},
\]

というexact positive integer-cell expansionがある。しかしGolomb uniquenessが
直接制御するのは4 corner differencesであり、internal levels `M+s+t`ではない。
実際、cell occupancy `M_n<=1`は完全8-mark scopeですでに偽で、64/128-mark
fixturesではraw maximumも大きくなる。

fixed rank-distance `r`のcentral differencesは互いに頂点を共有しないpathをなし、
各difference vertexのdegreeは高々2である。しかし完全8-mark scopeにはcentral valuesが連続整数
かつadjacent ranksとなるcellがあり、literal
`C_(i,j)<=|log(B/C)|`も反例を持つ。従ってpath degree、central hole、adjacent-rank
だけのpointwise chargeは不可である。actual-rank floorの表はfinite diagnosticであり、
asymptotic no-goとは主張しない。Wave 12のrank+length+full-containment theoremも
gainが一epoch定数未満に留まる。次のchargeはouter/inner curvatureまたは
survival-conditioned lattice multiplicityを保持しなければならない。

### 17.6 certified scope と claim boundary

Wave 13 harmonic probeは5 focused tests、Ruff、deterministic replayを通過し、
全1,146個の8-mark all-prefix-`C=1` rulersでfailure 0、64/128-mark fixturesを
exact rational arithmeticで監査した。certificate file SHA-256は
`8d23fe9955bc7027ba1af31770deb0f731d964717f26dd86f309f0ba5f43d63c`。
finite diagnosticsはinfinite eventual-critical branchを作らず、Q1またはQ2を
解決しない。P15、P17、P18、signed target、Question 1、Question 2、賞金請求は
すべて未解決であり、総合状態は`UNRESOLVED_AT_HARD_LIMIT`のままである。
