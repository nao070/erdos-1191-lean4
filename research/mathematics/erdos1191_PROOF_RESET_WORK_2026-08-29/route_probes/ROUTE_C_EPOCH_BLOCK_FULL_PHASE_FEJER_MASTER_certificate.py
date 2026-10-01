#!/usr/bin/env python3
"""Exact full-phase epoch-block Fejer master on one fixed history.

The embedded rational Gram factors were discovered numerically, but every
claim replayed here uses ``fractions.Fraction`` only.  This is a finite fixed
aggregate statement, not C058 or an infinite-history theorem.
"""

from __future__ import annotations

import argparse
import base64
import copy
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import sys
from typing import Callable, Mapping, Sequence
import zlib

import direct_b_membership_sddm_lp_certificate as membership
import ROUTE_C_WHOLE_STENCIL_CROSS_WIDTH_MASTER_certificate as whole


SCHEMA = "erdos1191.route_c_epoch_block_full_phase_fejer_master.v1"
STATUS = "EXACT_FIXED_FULL_PHASE_FEJER_MASTER_GLOBAL_C058_OPEN"
HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = (
    HERE / "ROUTE_C_EPOCH_BLOCK_FULL_PHASE_FEJER_MASTER_certificate.json"
)

POINTS = tuple(k * (k + 100) for k in range(16))
MULTIPLIERS = (1, 2, 4, 8)
CHANNELS = tuple(
    (rank, multiplier, POINTS[rank])
    for multiplier in MULTIPLIERS
    for rank in range(3, 16)
)
OWNER_ORDER = tuple(
    (n, multiplier) for multiplier in MULTIPLIERS for n in (4, 8)
)
PHASE_LEFT = F(100)
PHASE_RIGHT = F(200)
FEJER_RATIO_MIN = F(9, 16)
FEJER_RATIO_MAX = F(1)

EXPECTED_WHOLE_STENCIL_PAYLOAD = (
    "5879f3b774b8b044f01f6a7d529946d620478191b7a9ed8b7e246c6e16063e57"
)

# Filled only after an independent gap-free exact manifest replay.  The
# decoded object contains one closed-chamber epoch-block Gram factor for each
# of the 108 chambers.
FACTOR_MANIFEST_RAW_SHA256 = "45060f68702057a81718ca452502c9f3cdd322edc07c9884583d802f5e18e49c"
FACTOR_MANIFEST_B85 = (
    "c-oA;-Hv3ra-{n%eI0?l_)qFp1mPefB6BpDkp#@lxf+~zKeW$Q)=sWqcbA0S=<3RhSU;rG+}zy!|Nim("
    "_mBU0eEzTh{l~xj>;L`!!yo^0-2Qm}*Z=%~|KmUP-~aWVdbr(dO}Be&^_J7P#awU4<^Ovtw=%{p9P<Z9"
    "xYbbJe&$|syxn`ApAgIK9$LP|-rs&K>LY4xw|gt$7Dv35V_bjg-){eU5BZos6l1-Gs1Kc=SLav1eO_(z"
    "Yg3&ctFIg>&JTURxK`%ZhLXxH<$eoee(XIQ<^B5ZA;tNrq0NtLecn}>7f}1|3d^|V+-~{kw>0uCr1pMw"
    "QJ)y|{PJG&{MRslX{5~sj&|J2e9ZTp=Re{oTyA{(!II}i-)kH5r}cq);P=ut*EjU!<_*ukoj2RUam$;x"
    "7V5mq(C78X7@ICuk3Ed?{;22knvXh%F|Q)kq2JYIw)TGCHD}$#ytb0lyx!P#KcmOZb<SJ4^FeVw$XHsq"
    "?Uv1a8@H@4&GQ+~7oK9$!f2a23i_ORUvnXp`R9DhMaIp&{b)Mor^ZtB1hgbem~SDazJ1;E6N1)txz(nX"
    "n{TaeA86DY3AOSD>)b2{@9OPw#zPxruHVY;Yr3BK@LS%z_Q0*Qp1A13W2o8?$L3OhTuq!ybgs_1gtY|b"
    "pS2HCnQwb}bn~?bR;R96%T{k|-ehJ&%&+fnt2$+^uQ<0!yrr(MV&TqpGdJ7ME3f?LTh=Aa1r(3DRpNZ&"
    "b7S38Tdy~SxtH|eVQA6B^V{cUoDXt7ou8jOA89!1e71Trdgu3AxUMuGw|+DCH3ZC0iu2Bc?rgpwJq<0>"
    "KD6ME5N`?+KUYW7_xAZ4S&vSOFV3|;ik?y&dTX(*k6ZT`60b+WYhFqmY%e{}`Dx?l6=`RT`NHQejr!p_"
    "UwzQC(N@#`UaqFiTMb!TG<IEknoCxzXa1w>y^R?J?mq*|3}l(t80L~D=mo`@gNHhwZ^%OdyY%H2;tW&s"
    "D(-W6+%wT*Xp1EF)vaB2TGEEp!zr21))#80%`FggGm7CqV%I!pqJn8?I!xwkXotSxP*~PcFyr{orJr?6"
    "b4zx;pLsL$nb#RT6JMg+X!E7jk}peses*G2<dNp0(K1nV&g<iGOp3>RKlgU9HF#$ImLn@P-D+JH^58(?"
    "RG6V~eq7co8C`!)dc{ef)7J12M)sq-Cq0;SC_3amICcle&AiB5)_uTU3It7s`!qvDQn1kTxhG!Ry0jbD"
    "F#n?Jz2vBqD=U=D6&CorpKmVd17{#nIEmVGRWP6oz3-@hPg?u)UdQDD6y2Tz)qD{->vbnR<g7(fDtoY}"
    "v2JM{_(f}CF2qu`Fv`uLlyJJ7<z2Ua8*@E#y6KqHvC#<lGnAyCr_$W-^9Q3M*}dvuoqM3`T3EH(r7>yK"
    "weU0eX1&>d=mC_XwG{Kb;aaqm!#oRai7*&@t?Rm)Ur^`s%*Tv-^Y@w#AVuPmh-W|dMb~0ut$rV<QQ>-C"
    "&)nqqc`9<;ET4UFCG&HW&x08h=1<1C0_XJ(ZGWw!64x_9e^a|w;JnjJ7z}*nj4Vw%J<sF%Hn+{c{oC!2"
    "*XMu!*MI!?|NQtr|21)7JovxcA73BO`5*qDfB*R3|Nh6n{82;r_$ul3`s%s2R=+;JQhLtK^!507%xBtO"
    "&qw)6kFSrBOZl8Xb9{W{@tWWJHQHDC<Mzk@{QUYq^OM4H{3Fai{;!Y!{2%#`f2sbr{>Q)c`EURIzx}&@"
    "rXS@W{g40e_5+`W3qDQ28^5OcZ04DCydUIk#_^(sqYyX|W!M0$tQgj^9$Rvdj+=8f5|H$kYSnR}^E2+@"
    "DY!=9DbAIVX27mXz&<}u%VchsxyORS{k+h4Y~X1Hp6aZg2c2H5-esygcsj2<be+3;?RCDw*mv-6t_T8X"
    "o_i+iw&MmoXBMc=kiiv%`B9_h&DS1L@lelEXMG~fl=A+ZCthYdPPCo^KvEkuZ7xs;t2dB>VVdV@*}<uN"
    "=#>dDRE|*v<ry~m`&aj&D;sm8l{ScMotOE3-$|!OY(8Y?FR{aBbSaz5tU+r^KR-AA+>d#8nNep((vRkp"
    "0hS6p`Tf4xobwc{0wa;Y*5|s23dry9G|tB};oe->-RI=|k}}F3o$_21nC4*<hj8RByQzx#C4hN|+F9>x"
    "hfX=PCe&5*s#PK8nD^7Pmfm-bR(Tg_ONVe>R@AS(jlV{xiiye^K}<IV{~5p&AZq#5ppdCGJpb!_P!U|v"
    "8`$%{F8{lZg9t`Qgkmy)`Gn^(N`hBMS+~<Tzg}P|vubq19Gdfm&;NV@s59F0ETVV+UC4BT-Wl_6f}THt"
    "@7$!v+z8;T!f{p%mug_UFOPl3@vLlCXeFGV9kqq}(8)GW_<q!NbttCH3k^CO=hgC}=KjsV3PIcX%+?1k"
    "EIW@#;jjwK1}D!@$XA9nVCvCu_6Ff(Qc@zoM334t!ZG7#Z0ux?N_i%7pCNIE$XlCxvMCci6#e455d@za"
    "Shfg-%{Mx8KOyu3c#!Agnm{;T@M*sl5SZSXj?Q`F3D)Z>-@ZYwk*uH|igBH+f3A9EM12NXfvO+Jh&H7X"
    "w;2kQGAVZp-}p3<9WRGZCPC>!9`m$|Is|6wtHfZQ-b9qSRN4g(-9e-?id0h{6Z_rtfaX33D?ZH~+#pb="
    "`_l#w0yH@*a?U-_!m{2v5Thl3zb?G!s1Qn1=B>~;Ux>EXkH@LMh>2`n`%egazE-VRa`>P<pHd1Jc*+I@"
    "krZcZ9Mnl+SBGZ^m(+{>s1?N10WB*;w5DZ4MpEhmQ2n_L+F;&lRhTF`nhfevB;{1>{P_gtf@li(Gs4Yf"
    "o+<!!UT4<XP{^KYujR6(1qF%6^E~K|HY{;=>GHHH$?4o<hgM-Y&#sB_byxG|=MlaHqpEw3fQlORJ!3wq"
    "Tswc(aTSANQePfdj!91?K;7uE&Ty85J-M8@!xJzv&H#TwsCrKG_XRez_mYynLgpG4&S}280CEJBXeSc*"
    "6ar(`9qDXVHuv*Zh^I5}n(LvkG*3Ec#^AY%L<Hq%66YsGZDcw_modXInX?vTpO|B4`Oi%}57$0^8=*e("
    "gsA25QO5K0t2`cB>W}BMe;wtS9&zTFW7Ox@vwck<{|Y7KXM4`~b=2G+AIIlE5vtMWUnA5yf2OVoHC_>_"
    "p1fj!xDO@TiaKuyb*`m(DL10@40d_Lam{C$PMYEXjLkqA-w^~yT2Yc9z%l{mOiBKPK_$zZ2U7@RkW<zT"
    "%$N~XKPDzvC^nFBhPr{!1koUDCnj!wrdZsxL5p*X2A1ADu$zyu_>M6EsdEh}vO;L~3IMo%+z5^W)hwxE"
    "?F^Z1NB!{%A}~b!1rTGr-*SPY5e39y84uB)I}kmOr};ogF!iZACgTpIPAn;6OJ{NBOz7;@_70Uqx6YU}"
    "Z@U2CW2%6HO;SU`*p)OFLTcbd-=-tnX^6!v#)ND2wjr6L?wFvMGdo_~&^)krcwehvZfiIzh?ykLaK~Jy"
    "3~4%F5&=FdQ%x<WElSl2yUzvOx_J6<Ywx$igHzTAJf7Dv7r21xQ8pkoay<45fhJfu12><Vcd4D(VMVzX"
    "ppvUlYW_P8wLysTboD62aO%ws$NZl^Svfqa77c%#pjJ<Ne&xylb9R=wMk5P)zJ}ajJcoblzHXPSTbj=+"
    "Q7{oC2)cfNXpHM=HW#ZNgJL->s(9A9u|xo+<(TP0SBHpMJ!bu*>#Fqn3jb+M@9rX1=g~FKzM-qR3sK*@"
    "&VV4YqAk?jojg`mf{-~EkMBqXjLHLSGp=Oy9U3RY%!!IoYBYbLM5vY@8(2y3A+T%~Z=U-iLBrwCCD#4;"
    ";6DF2F9F2shgOX5InB8P5Xp+C5^<+an4QEChe8CZpm8Br1FcJfpk!LG6dYB^KL=qPHaM&VmI+jS0}()r"
    "QxJ)YOc7BrZ-2ROB@Xl2sqAE@I2ojOXvZhhv_HS1!t0L;4jzh)N$~{U5ngcazj<Gm_W-YH3U%JDpqWmR"
    "e4&3+GJPn70ZXa1nU6?5IrB%=4A&aQ8K8)modX3(8@1}{S;ebk!F0-K?&Nb(c|@X|Fk^utjpApI3M4IF"
    "@M(uPWN88u=h3Ez9Q&E_DX?GGwlX;?g<upm_W?m&d8}!nDrer+0jQaEoKGgZ=o6y&D!&YBH9w!g{H@Ni"
    "6Y5P6`SS#y8><yPE}^lB&{tfi{7-3mobRf_<Wz1a>P%m_CK%PZ-RA;?eS!0uhfy(_m^s6Go{OrERiUCr"
    "L-M&ON&s63dWi+qW?JG#66e&!*UYQZKALYwz>{23Cq|@BH^XhZz|(_T81OU+5)}#}M9r}73s^JZ(ZF#U"
    "iKZa}EqFoVkdFnM>xwDK97^k|0l5I`!7b<mE2Q@FTXRi9_9Y%ybg5w+&U6R3IO|-U=hg25)c6!K&5!gI"
    "pQ(R^`mC?6O6-?7<@os=k5}oB`Z?k&K3|Wo35(0Kr;pd8g;(nT1gHj|e+^LE(f`p_fSOi-N^YOwE9R=!"
    "whWuHX`X8sYMY=pe|il(-;qH<qs|jHrsfxyHV{Yni^`Cg1*PX<hphxgBD|80zwWGcBP*DoLevOhQS^ce"
    "=$lIu?KRJSZ8}b7f^XeaXbY7l192BT=K~slp+N|g0OytVxkze!2P{d&!+DU@^PYqDzy>J=D)B*EEvU3g"
    "60cBnY-;VK(r_siJWir^>`;}6zCiAvs{LK%Y~_`kw|DSDL~uk%i%uz1g@U(tNZzSqaz<JItFC8kKzD0r"
    "B`zy`-^o}**;2kbg>@|G<ctcdW1BmOOPts*t6CJBIqLqtG%Cl5fzvTpNup*HS0Hk(Zh%1&cV4v4Aznw^"
    "*ZIq#Dvx+Lv5i`NyHul+pF;=)ov56Y8*Vf>z&3Lp4fZ^!)|={vM@BXf6S9#4B`NN$wh;b?Nfq%sFIAKk"
    "6?8o{==z0J5+D>AptGm>bj-T0q0}WW^^4prLFqm_;MoH4ItVP1jp)Gqu??~@^$jgWnoqp&bcBKv%*$FW"
    "p9j-TtExC7VL=Y+Y|*^#&(EG;t_nD%ZmwtUb(q6y3f2{hpUYC!*7*%VcS{MW7<!ieebk5L_*7nbvv_2v"
    "cG@@>bo@e+!r}A_;}Rg|ybcKgl#7CeBK@|M>%^oBZgnb~2p9x1rEAi@>8qAXlqrFf!gVqus;JuGnsnCn"
    "WnH4=f^iHI82PpXrL%VYB3k>kINRsZHWy5CeM6P18w9|N6n&+PTrBEJhP$D!7DEQO38o*48Vht&LR`AY"
    "jtLsXU^R%gq*9Jj{RO0V&R*!E07}i^M6%D$SL^(rDawUSZ33MNQxJSYFH~4FFJ%b@qUi6PvfX@9ZLTk+"
    "es}G%0q|^#yhP|Sk3;+edWb3@q|K#2PF$@Uy3~Co*a{g8n3RWWKNLM;_#A;h0q_;7ioi!Vp$pULA$nJI"
    "40#@fhHD+}-Xu3WPF`4vmRB6*{G<K6rmXC1E+-bpe6QyHbkHi9gr=BVXnAW*MILdps+hP8Eu30ZbgZht"
    "%=L5;jm!(VH7ha*irqQH-KR_?UtW|KAyLb{w+x!s^VMSzrc@Ntll*xTAn<sI-4#Y@yjzt+iqwBG`-B>+"
    "qNyo0ott;=NpVNyJE@?N7~w?iX(qsz9ewUTm9S0;5;3QBYhuDugn^GwyguoCbo(4tb8j~oeic>HlDN*>"
    "15kVaKs_bDo<mFd;0#+%Pr>0s!Axm|@R^9Wp=Z@85b}=ZI{96II#>N`Ok{J6FiL#Z{;VG<eavs3k1T%G"
    "i6<WEBYZyR+8z2s&ySDsOkW{9XMR5Z2~Z6_|E9(t#<j+u7l7IjRVbh1SaL$Ot3V$}5UGsw{ECXz$EKPt"
    "959bvs<8wWG^fWqA}TrtssXQlFju&M{3lp&STq#0LnZqu8-8y_YLq~URI->^Nn^`$k-{TzJHQ+Kxoz%f"
    "9-)ZOpi!akOZpR4Y7Kx(DlNe*%KXe-9a;}0s(97OtB{k0(%-+GrxK$W+N|StUV|3gj=9S^`Ga`kJm43Q"
    "JB73rsOpTP29Kz%N~O8E&Zu-_Za<OE^CeBZ$D2y;KS~jis{S2PbHcsM8+-rJ9HGYBj6o`jrQsauUHS|l"
    "%mRUmxMG$h1KK1#+N2FhQ8|UN30X+r074XP&Fox_uyuu$dPCVp;z4400wi5pujTImp$b4jl3!_}(7#B7"
    "EI`>7IvQs2P!R#a(XA+l(0MqQ`BIYW-?-iiN8t%87efrz*eM12`5S2DNUn4y&o`EROi2errcf?N;rxm5"
    "jR(s&#R&VPYT(b0z7gIVB}hOm_`Y%JCsbH+!+BKbmXL`S(Xl-IWGN6UHLi*}g<`7SI&Vs_M0p^~v*5A5"
    "J@9W7$f;LRnjr$1dnezPx`r}7ktW7+N~0U(;CwPoPhhO%l*mWW7y4kUmL+ekx52$noY0p<7t(BEKPe<6"
    "lYso1sfEryVfRYq?pW_&{*HKJa5&Ff94n%!TfHh+px3m8I+p?h&d7+gnC4fu6$!%EsPtJ-L$oqZ5y}j?"
    "L6D;@Psar)V7KaK*~h>3sPnBbgnlpdQsPdPHqOYb|G9KJ7ai|pspF1QZ^4~Pa?p#_$x_hG7hYE(2LMob"
    "Lv+|(kT#YsdRpLj#%6_t7B3|X$pX!j_jHn#S-ezr;XvwxbV0Mo&kt&=(L75+hpUq>lfYgej&_R5W<oz`"
    "FTHXp6+@{+5yL-1B=C3U8&O11bdEdkKpS{aimPa`;;OT(>U4+_?`ku`Cl)QNtkk%W3Qi<;xff&?67HyC"
    "tavyq`nH7R=i5-&xC=Y0DkF(2b$V6d^QmH3<P)kZ>QyzqqEL=d=q09yO37|1T};p_aMq2m^FbyOs)fxU"
    "(O{^5+0hP$%An`zG!qmh`MUgYtZXI4G~I-AuE6e#<VYr0=WCnGcfoXdAZkQtlH46JoPR;?L-wfJxD*WL"
    "CmUTL<(I&Ep7JE<6F~L@`BE1fG&Akr1cM_TGa96?7(eDy3HAB$IBIz1XZ!k0ujhm?_3LBekI+BL>s4!b"
    "ex|SIF<#}FUZZ^dD5nGTeu2TV1B3A>|A;FXEDIPEK9AI+CF4KdG_T()GKQOpA&8wI{(j2}R=SoNdU>|H"
    "-cW73z8Vpu%|t>yKk~k%T@;ll3rbZkCFY?6CBMVVWZk!!NEB8ureO!h;JFE5ZC;`^MLR)hAoz=yoG-4Q"
    "O33?;Y#Z?G6`?hmdZBk<qcdb%r#zo0gkXenKppr-xe=O`HkQLRQQy|C9qiPdH>KhVlf%mN9mJASuFr#s"
    "Y885fUAImwak$SRi^-29$|1d1n&*z@#|=j3Hclwy5I4OcLCT-0d0SJtCL2BCo*UGu-JPmZkBRY5MV1cq"
    "x^G=i%sVIuG1kiA9)b!K)akj=;Kt<2HEYywRExisp8gsNN^m&i)=lUc2IkDu^8&Y3M+*wQghoo1m7;+X"
    "oh6*+a5g}6p;A@y6-qgMD6r`aSw8o!C_V$B%6D`w-P~|-ssCyf7A_E01Im9c%d>dAs1$@if{1Yeccfuz"
    "X^OYv6>%xDPB@il<D&saT7uwymcvw5yyz+?ViiSCFQI5sZ84(-7R$Ba#2PAubWm2(T&Gh309;vg+=zA#"
    "VZRd#gLFu|z(VWMo99DC{2OU#NCnM}x}G326ScD?!Ko%6n{-HpO4~PBy!S#a26(&PL*Y~bqWPNjTT%G6"
    "8I}C(RD{eb6uHe?xYVd^#EAuavc#DQUfuj;P|31Qrq|}7KW{&+dZW8!bobQznaNEg3oByuOQVL!pNlFH"
    "oyDN#kP}{)R25V>2Y$wSF`a;VdaYE%r8|>S`dOJ-GWNOJ+bJ!#240-0U|$ZXK?IuHvFuqT%n~CKb6tF+"
    "6fISq)#qxVNnr)Cf}^xTYMm**p~e%J=-{yS3^a2l_xN4gQ_Be;AJtV`+ARyDdO@`)x)4cTQ8_S*>ZA%k"
    "k=QChrOQ#QGZMr=W`@E)i{~zh?b^c1>+3)glGD1>i<IKjJL8rvDBPW0b1%%V(fO==%wo#9JW^T_6Raoc"
    "X@lKWREj{Q60J?tVIM9+8~D|Z#G8kycGV=18I%>yd#_YSFH#gZULAI3H0TqAW^<svEe+6t7^p~55WOf}"
    "J1DbE$eg~h-Ot1r*-f=HBkLkjee!j}6WrY@Et<!%`VX{;l2dV&C8d1e%9QhwkcZy|e&wToeT|;J>f`GO"
    "AFt0`pP@X)E6*cfeC77}n%UHGJYMmUU+t@;&-xKRK9Bw}SAO}y0vgo)HSlZkxR$Bw0{q~u2GC}1t6?O+"
    "!E;hnyQR+gp*X<4IfIKLI7w5XWTXP+ebZ{LG_l;^wE}7e6n1+C&^l>pnvRMLtI+)Yc2Em>iFu<n^Xzor"
    ")o#I~1XJxo*sXY+MVw7PMy1P3(&u<mfEUHmFV!NA4mq0yD1I38xZeQJC<-DcNUa1@0mD(>f3#DpRyjWx"
    "ivLQI!v=g&bf3Fe#SXNMKB@8!N=rT-Rf-o*mnu(;zz+HKZw8oJM0Ed3+Nk{Q6d%x+;Tw<wa?rRz-Pr~E"
    "gJxCIaZaxJNVd>ViW=pzK{XIzicKfZ$=|93Vw6>=bA*k=a-JN@Gg=!i>(JO)MFWP7kARCpkO=h3&*MOc"
    "+|mBF!A9Lc`nDT|Wp_%ibx)qWz*&*FRh8s<r)w3dyEfaX&rn6~CoWTw>c>s_FoKd3G&zdvQwnI8>Mx>-"
    ">}GV%Vd2l4-d<h`k5pxqwyC+3Msr~k@|x(%Zdj#$2pNSYPc@v57vd#{6&&$W!>KyDEs<7Y53y~gj1JOz"
    "t@s9)4Ap<6w!?XzC++ucg!1!)#i;QHRM-%zKzgA|h$xYkh;TM}kh0LXP~3%24>`Fjk`R@7f7bJ<nkyTk"
    ";Km7ew!U`J&yu5G1fuhu=vb!<MxD}knLp57a$g0XNx)yLCabouN2H_1%})u%_5y;1XQjPJ5KGD*bheg3"
    "w9dS*W7!9HZDngtMduWKM^yQ-D-@|UWb|wAj5w;fxN4ze90^F9%K_nBSTr|xD`rT(75b_Rk{$IEvca{V"
    "DzUGs0C$OnR^K4>uMPs}Xi1Rc%D;(%c9)rWb{E*&w>Cktniwv3fM$}SCylMVZWT1T7PrhFF6e(o88>$g"
    "8!UvQneUNc;GS1mOo`Eb8IpMsG~nHX>@W(9v*KM{NyMsTsOT6-DwC2`NxU(^npg;Dop~<Fm8(zZmFqnV"
    ">1JA<C4NvJ)Dq`%bHzOeOJng4f&Owk+1hkQYDO!2_Fo@|MbYjO0`8`_Mw2Er?r_ncFdiha7b%;&*!PH{"
    "eALT&LJ>ebJ-pUc^ROol4fu<?Ma{rcfMrZ9s*NP5T=v5ih@U~ViXR4?id$AgTpd=YL78-Y$|}7Vb0{$E"
    "HjD1^os<yCmsv$5%+N4j#qV}=zw+l?%+HVX`ii+8kFV!v{LGJu;Ey_YUh1FEc~xJZ<N3<R$Mf^!Irrb!"
    "vppUkHRacjN-y~BuQA@-w%1B;TcwBroUT|Pj$h9uwoT2e0yPSU2QnjszPmOB`az<|m?X-)5^Ihf(6JJR"
    "4r?qKXkiLrTk!L7#{qt-aCY3yVTB2*u4YMbBH`PVt_Lq0w&G-mSk~`YR4QQL9R)wDokrhwrVO2N!z4m?"
    "(VH5~ra?oJex;|Bb0Pwj5H=W(x|tU2T-K~rDWp~r_xFQ`Bq+*nz$CSvMf6RXSLz_GX}n78pHVj-8CA<i"
    "n~{fDA6L&)-(oyM3dNX%)JNF3Z0OPwt^3vs=%}61F_yfS{xwBF(H;_3bhU@?TJXv0Rqy~6sephb#s=aQ"
    ">qivkn+td|4z#%IPN@i&uw0?{Hwk9eBj>+FcxnZuh)Fi2=veK&1<iK9YGSy%x%;%t$UF`NT4d*~tu&a|"
    "G(rPpr9<i~axQ^j?UB3$NJ)6~;vyo7W}SvJ8bn#KUd?j4Vu0BQsU&iSSk)>92`%a{vGZ_~Y8Px+64{w6"
    "nIl;X;wnjwvuVqVI=QeZiZ=#Z$fT<?0Z$SsY3$KVq7`f4FhzYeIUVa6qSzzgl5H!16068_!OFz3p6Ag%"
    "LMkCA`!TU^?7NayhG!ym6GeKa1p@?`(@d!DPECvhRskBV!NY1fM3`0YNo1HBU}e{IZIz(Vf(siWOKQ!k"
    "CI$MvSBnhXCM0yIURmx`nju(Hl5toGwP?>szoR?i;8EzG0^<T^h5PeZdLe1n;Dd!wZDL~bRkg~{=DAuf"
    "V5HDq)67j-X>d<iu62omFGe4^xQ=m}w`3BFnVlS`@~*G`J<3i4dshX(pnB?zkm;-o7AoI$Wvawrb@fAJ"
    "YL)g1kSMdLnJJq#pULj!MUZAu0wEVyTip!90Kiq+8Wf@`J`?bZ4X*`?-u5UeX>A%B!TmU?9PY`b7~<n2"
    "4R=NKi_Va)q@rC@)aYx|saV|;#d}mdpWEz`AOY@38_-AHIegRvAZXK9c}PbmFZFbky~ButS=l1IvFv|}"
    "?lvr{s&fW4NLAzyNv#WaY%;F=rAU)8PhI;QIW20s9DC&`!p;*j(5~>im}+9C86rMZ5APF6y&jM8dG!1-"
    ";^WaKj?Q1t)Lt`$eZ<eN=d(W^`H{!OJ0CO0f3}|mQ}EITQ?(!c$MLQIxL+|9t&C0RXQoclh;4|oSlf4e"
    "n2{Z#F*%!iKiX+a6)j6GszP8MTc<rOPbxc!hg&RC-q%dO1*+P_RH`@TDD*G5_X=K?=H0eEgAb5ghC04O"
    "<=%JYy&{T)3V>Vw8ddjWi>SI(5U9<pIzAEA27j=Rit=%e_LyBO-YDV%p+h}@iEWp}dDI=pMbwrb1ys9@"
    "-6lxf@q1Z$ncfR8)f9H!b?Xd-6lzWwxTmCYmKitQGgN+1n^fd24YlkBqtc9*<!cvdP&9DacmWwv)p8=L"
    "`L)We_lOE8=W>!NBp|BIk_(A<*_G;_egmrKwVh%#RyGC#=vdr#p`$APwQ^1rjcvzRFNYBo<S3?`b=8Sc"
    "e<Kv#l7ahqGT`~S7V|7LqkXejomy{h&dbI@?f_mmGErF^ht2gFQ3{I7sMxRF2+<CT_!`P6MAF81ng!$q"
    "NlJl5X^qx(C0s$B{6Y0>yf4}!m{K-|DjhHfq1sPV(U?x_$mpJrl{JjA14;*KyJiz1p6vj@2{NtspsZQ{"
    "3rL+U)JhU_HTNrBn<T{S+IK_^$CPJa0Ar@Xd{Ok*!?c=cP6@R$p0QnU0^!VDooi&chqDZ7QEMYdDd)`s"
    "{B_V@weZT;lYGPG_uP=%CBQ2b_FB|Q$u>+0Ulbmsggl6WMMtgzOawyNYFw(v4S^-b1oRChg^S#mriV&H"
    "wX!c&)G!Ln$RkuxvYK|TstcUL%p$tqi<f$5*F}=3E1VK29WDi^Xa6SVgO$(zyL1;6<cHXX%mhoxeI+Rs"
    "HB?!qYu!uXyNgJr3lqI&)H5xTR~0wx=C?PX!vH%r6~nW?ubye+!mv$<oo$dSx)hxuF%{O3UW<u)`l>u4"
    "3V=jXs!kY=v(ywEa-?^;a69rE)+?k`jzv%sDZoESGv*?*km-^nRj4K8B*ad1HR_z99<*$Tc{N%@I$x+1"
    "Mq~`QG@A3w7ekj|d8-osZuxn|t}T&@pfrhVWR*-dBO64E0{Jx~u-YQe^h&@O`?{Gn{Vt?xJ*1EN@o_vu"
    "f9Yw=taI+`2|?qL;%A%h`tfYX^J`|#=_|gDuM)!7<MEaHqvqG+N5^bjI%c<!s-<`>MUE9x4U${sGm=Cp"
    "+ub<@a!TZK2B<p?;M-DUCnUR~Et74#P#rsWHsl0FQPu9wG?{PxDX2l5DWq5`C0Uz#6f{%7VW|(xY6FFd"
    "_p4OxXK4G{TusN<rWK(m9JCltzi+Cg@`u}8Vw9ZD_E-@X4g2EUcFs3qu8U}TVvp>!=d;`t%^(F;wum?m"
    "s1Dfswp&E!r8KxI54g6{x5ZL?9%ZjqhmEQggg2L%sMjn1DLm6kr8I3{<8fH`t6(c1m1ITJ#=g8z0>}t|"
    "1MS(_3FQ_<M+tK|7*u*Lx1B`qj!UZcwCxw&dxvKK9Zg{x+?8qG5mrP&#I|)ZryNzN9wwVJ3(SqbcKB18"
    "Z2<)u{Tr-`tsaU+%Ri5u8<v+!W5gMX<WNLL%s!T)=-rNYSkk-hC4DY2Tl|PRV=gUcs?;3*ygN&_yJPo$"
    "))lUGQ*i`zli2j0V=I_+G@QRcDJ9}TEi}@W0%2)S!c}m!D!LbJmtD{n1>u6gX`9TVlFlexdH~9CcH^cJ"
    "`ma{<K&fEZ@LY%0MNy|>3|4&BQU~-q6Cb#b=eQJ`sI6M+ezSa;vo6|K4(GCklcOm~-kFigQG=|&U!<Kz"
    "bgMq#&KVQoq+;?3N+*ESd`?Znj-l#MBg!!B?Wv_9m3x8wFKf|{6Ish6(KB4Iv%3ko3T~9;vF3_vhn@E1"
    "PG&>IVsRqZCsAQqSUi~^Vc@6|PNo$tW2vHgA`MOX%1?nWan-P^F$8He@K6>LFa43?63h4VS1#IdDP@rZ"
    "vzG-(1E6EPG+}|CsX9gI%D30mMV)4usgjjc(O{^MoK#LN$R*L3)Yz`wk*faFbc$4`RlC55pL4mjUig7i"
    "0EK=-)wp@1$`?s5FCE)O%G-uIlQ)f0Fa{56h^EBWn-~Z>t6n1h1QDmrfDdfMWB~d<=Ww|VE61q}*qi?@"
    "#!O{*(uuHCRTF8_(TwO-J{QYPL0qV6tV%(Z>!FuQb-#lkIEhF1UKQEhj&`Y?4_BIemIA+(tDY>n1nF7!"
    "jB|<ocJ1$#U+MEzANBR<sXk+WgwNN<e4>xXc)mU-+?xM)45|5!@Oo+ChF5#E33!j=+0&2OAAsqvLDf7%"
    "-kh8-qee)mnK7XzZ>_JgacWQk9F<%aGZN80ZSV6C+*_-&P#m&__8Vtf%(jUW+8TC}PRG_lE!}Jw45<Z2"
    "y6Z=ri?dqSskBt<b9=NNI78#+z{#nDHSF9{f*M8#40b=<5qN7`f(oksj=+)FGYD22vq5^m@6lYEja?6F"
    "qwj?@2?w#fv^}}AflV1rQA)5rI2T4(5O-&Pl=2|tvqC?t$lg^DlQ3Df;~6Jls(AIjceUQgYrE!55IVCu"
    "71FVrW`d4i?=H4%`y!nzW2cgeP546EYRvGh#NSP<(X<-uwlVl^$o_2$w($Xsr}x@0%ct7w&Rm64R!=Gw"
    "ieIonn?kF7yaDb~XW0_rkcr9W+v#s=$VuQbakt64cH+`F*loYv>CV(7g}9+)XBs4;N7z+fyaG<LDA=|~"
    "ELJnp{@$de!v`6)OLfV3_59CHcrdk-`;<<4Of=>3STC5~Al}v9ekSf{=12xslr>K2A$`!H+95*>0$EkQ"
    "IEGOfM^&f_A$8Rjv4f4}k^zIJ>99VX^OAWg$q79jV67mDrjAy8!KyTOXJ)XmjV%Tg+)q+PwN#ozb>a%T"
    "p2j*2xzr&C+6zk30a*rKUKDhUoLMqLaBXdA#H*6%C7z%RCu*THn8Q}bt0W&4xT{NtslI%Q<&|-mdn@tM"
    "c|qy#piYSu3p9jnO^Rbly10bN2WC*8C^oOTyEz8DfyLiSOiBjZ$wBS<WT(Bu{tfsA*Gspa*px!ex%J?d"
    "uY^z$30w6ziLq)Bn<e(qxHu|>58gMYO?P|mN2SSRSXhf*VZOv_17pPfX}t{_O+{BN&rv)_K2>H|y3}RU"
    "C7%}Vf>Rbb;gvF3E?<ZvYFWkAcM^9}xjJw+y0&Wid7Qq=>XPo4y)iQmAJ>+pXURa7WtC(J-;$=p8;e0j"
    "OPZjN(J5!<U6(cCgBob!VykplkV;u-CkBeEhs}>KvOcj~>Rw<bRK!%U9MHYPqDv(OD~(p&D^72%wxhIu"
    "YU*J&!-~D5J7NjBiXQoNXk`9G@Wh<k1riJ2!U&OaqbtaiJe7hdHjQ;KPqIUbO0X4~EIM`Blh4(uF(Y7~"
    "<E=tGf0lMXBN|;4fOr09tQS`sEgT{H_x=g)Q3Y7LuCd<7g!<h|tHukAYLdY#y@0in{CQ}O`}w--*^RBS"
    "D=JqrnoF(w)#jN+J7b2)-)~3F?f8uKL!K`3#!Dah^%x&2o_;;sGv}{-e5S9*SJteGbUepvJU-Qsnc8dK"
    "@{j5&i1csF^K!mYf#EWMB(nPyKBGI>`-a4U`vfxDd>C)bUEwg(HkgpJV9l{bWgJ1}^aa0j)YR=vGJ!wb"
    "3_ORapj_R2oGse$fLG_z+zD+n-%YjAh`~xEL`mn-#?DL)dle6R0GVLezODM&jiG%rGe|SWMocF%vAH9T"
    "(v}cm-57W9Z0#UP#{iuTJH>nz=h3K-W>=-Vm4_QwI%1#=<+VG4B<Z^vx=NnZC=;f0Ntr;|IBF-Hprz_b"
    "6za0{PdV>IZx!wNpeOKjs~60zd7GhdKDliOvkB@yn>TqMirJJWPO}EHm1EPc5t=7oK%2Qf`Q6m_KFo%0"
    "G`U9<de$jS@LzW-N;|*+kI>v;*R-jSW0ljJu~j@Rg5!ospV@RjC#a;8{KjrMm0b(47M%nc6oT%p!Ftud"
    "fvxC{8?sbgi_AgoMqxXXpZz%59&@rQnA=p#_M9}~Li^8(ayq$?d-X_3>3q~nm~7GySY0YJ#V4m?Yqup9"
    ")713&c!aFjHJsg2(#_D-N4*a2F<vKP6l;6F&D@pDaIQ<8fcHRNwkO>JZXxBeDb&+YZ|~xuax_NDKjO&z"
    "ogT+&_0K?%JKcTSKzG$q-(B3wIH#~#Tvn`NQQ=!aVD;SUOoL%a+X1@J57ES<v$TLq*ZDxD^;2h`Z2idS"
    "f?%&6Eo9x+`qHF`YChrO_=b|6`lp^!W}{sC9+kxfH-_Cf{fl*(;QdxFUW3IZ-wd9?>CrU(;ih%ci-m?i"
    "U6-)umadZK8Fiqdeo_QUYnjUP-7@7^yYP1up>zh&DQOSHcwD{QkWJj=ilIYH1bZ}be_M2J!#=@s5W>hX"
    "V&}>%C28v81uQV#Or5R7_iEhS<=TW|0eQB%HS1coKV6(?#%yi?)&*f#g-j)4T6~ekDq{y`7wP-lhy)=m"
    "*T2;jP>R0LNriO2AE#8#(`TVr!b&mgI88KTV1n#8#~_d5J&_&B%Q~G!c&w4l;Rzxq&?KVA2ov<R-h?;="
    "L3nHc=l+pnp}NYgalA~NgOHM~pPte%(r`VP*8D|fMN@*bB6bDFh^nf!A!ub~;_+I&j+PA20_WNcGmQk$"
    "$)Xy6pN@E??nPMxCyl(%nT~o2xc^=jh&~A->PV+n_s+Z@Gl#*hxa$BsZ9|#QvkTNairmoriWr-=966_n"
    "B~pWOQ0lXMM89W)3Td3jTqeJ*2h1P&bDlHL@OnJcG0&n@KYMJSd45ay>UD0^dD*di9Od~6nyFY{Wuk$P"
    "&-8e;pKf}f(Z5ElGxYu=ToCJJAW5-8L(R|%Re4j)E9X2>h$U)J8<Q0k4#jlZ;dj@lF<+mSoV~Mg9o`Q4"
    "$c#@)9)4rDoK&}kOZiSnvx_m5By$@=S8dX6HjCd=oVBgP?nf~Yw}_enHA&+_w=Ez2IC~A0gj*vVHb_78"
    "UaifMBn;Y6$?cXW=G##}krU9mlsCh*E7oZuE?|}E-7oFWy#10MjEiRh8?Cl6v-xEhN2;tCf+#BF4U?``"
    "QdekQ&Zl02?b1e4*rJ^UsL#vgkCZp}edC8PQPX+gstS{>Ti)saf)1SwG3QS0NGchRjRqhWlPCy+lWVdE"
    "R%&l=i+)}`itcLT+0@gv4ZhVGh0tfBq@>ujc?LPUV^@3}K8)$Ko!))F+XxuFLo=Oh$u?z*jH04R%HVnC"
    "D%)?C)rDcoH}?ddmdG|)&~8jv>5YqG_9l?6tp_zNn3i3JabN4&zlMtggCH6`ot9jCNM$&VV4>Y=&*Qen"
    "0FR?#ckXUiti?~EmrGf++27yZ$;U}U<Cw{S*!2WO+z$gu8?<fuIjg;Mts7pu+_^@i;Ud=?67hJd!DI+_"
    "8_Ti@B5Rb+%-tYT${^PB_X;U_eH%6`C|$9K7_MLI(it!b_r0jiq=2Nm7b8NZZ8Gu${VRqX;nEC&*fX9}"
    "dSz*p&iO~4J;>yk^^PMZ+Tt0yokc;q>LJleah$ufL1JVeb6I&PYhs<{5%a9Qh+VrSA|}K<vBWXc8_UCB"
    "$_1@MJY~!TrFfGeWMhH_$Gc{z&lj}HBBftV+EH#9i`KN_Ehs**na{Xzd?=W#+)zJ@5THy$%Q@Zrtq0^z"
    "<t-rIOTkJ4mDJ>B8IQHi8gPSW5xkcA{VJVJ8SW<w*VVClFrr71&8{tT?0b!3Szkg=RZiF8+ru6_f}9ZU"
    "gWM_JY$ei`X{WLuD`)4rj!M;ga{N|@wspE>llwDGJvdAjnkMA5mC+XDMz73b7^A8~(wZ1pHA^##_aAe7"
    "&LImc-plyzxaDqM49u>@6n3^<iPnC0c{?v;PPK*=s@Wa?A3FAbRy8Y~hBO`9uLFn^nMx|^D%qyIuKDZ8"
    "=THGwX#|8+B$^TgSGa^36)v5@GAe_RI%m(Qnb<Rn^u^aPq8MDNMeKgIEbCrm3TdH7Up;9unH+DzooVK}"
    "3X^fNCu!w140s%h+QAJzij^0-{*$zcsv_6lCR&dV8M!>#Aw#HFpK0erN*{AMr&sNt^VL5-!}xkV^4I6%"
    "<MSxx*^bX=ewOig_SYl+9Q54&cF^-YGyjn<uyq|%!Wtl15s!QhrF<73x_Mq94!5wK0f_iMTK>e6Ym@9+"
    "S5U8u^O8hSn)kMyp^S&h*|h7OSvJmeDo#ncl`+kwCuB2w1FSl?kCGGmwsxk_m`tNRkTi(6x9wMm$jk;E"
    "Xva4~-wqpg2_;+m5X>sY%}iu^3d;9*7ny-F(04Ng5Q8(FhQsRe5Vua$cl7EOG|B=Eg0pP;qp9bgvc-VV"
    "EvnbP9y@D26@jChMG<XD3b1Q^$;^@!mzt<a2)Bp01AZ`GN$jkfbtr7czUxqCQnvg^BOuiiY4T2pkR8Dk"
    "o3LtOGTxfBpXeV2I@W|r3U97m_U%MRI-FB=f0l=PSkAv$-&EpgmdVL|*J$N8ok!)I9IwJUZlXzZc;y1M"
    "$rWHc$h%7>rDp)~pUg-{+zP>{;yzN&4M;|9Erua!0G8yI$5v6S#arwqKGaGWu#3#QDnY?CqjwDKIELrP"
    "#qoD;Ipr+x1{|2ro@$F6`)&1(Qag@@jMK1>3$PAf<drUVtk`&bo1=trc<}r=`$v`6a9GN}juI5mRi!=H"
    "J+q$Hb8>v*kS~3`daaEZPN{>tVLj@E`N$+fD~&aOe$?;w=5S6>CQlOpJ~#GQo&SVLw6P}A8f5;>eFTbZ"
    "l)zWr!$c`+iB{P)ROGo-=~afHs$H*x=RAumpA$cnVN0w<$FSrQD+5p0lBg}1BAxWu_~B8`DIeEf#Dpw}"
    "_loF9xz9++ObK<0a+$yk=oS|}R7s)I>)DjJe?W!ja8W#K#E=HMiQ8uiClW24^lL*aj?;{P#H;X^tGyDA"
    "{!6aEZtmcLACcrlNUSjLTNju;=T52GN)0A;m!wFyAPukpvdDl|osM`&%O?B+rrnhzRiwJF0)tAjopE({"
    "3z+663ns_kgJ(p32wIV#uJ(6yzXUtE5Ju<jss|Qj?o<=Iei<I`sVfW{rd3-pZP@OZ?s$UX1x!mxXqS&f"
    "LPjA~S$o2lV43_a8(+lUfy}9r*?Ta7z;s<e<qV@D3G=BrFSKF<JTs3iSJuqpvyZ?*We#+l4Y?|fZOpc$"
    "_E;~IVd6;(M`mjQmRT6IO5N6GxR}ww9L&8@Qj1F`QWECurAu^C7^)-F#G@8?*~)lUw1+@bU0KbDhJDZ3"
    "?e++zx3=I;dP-j1cyw7x%C=qB!6LsUPX?fZ961`7xF^&`%6)2dYhY|3J}7;u3c^UpC!*of$P8MRD~-rG"
    "(J>Y;;(LOSyOipgzo&rnfh{!T)i&lS{M$Z?c^=5G4>fo{U&mLS!ETh+o_!pTXa4;9n8Eik50GPm=6ZaN"
    "NByc33B0}@YSDN+{|TfGl79i|w)NPl;Z0||j#IIRt9y(*B`B4#V}QA7K{@dPJEX_-R@}~Tm=0mv0*=Bf"
    "(t9uOr<k@_5Qi3Mn|cn++08^z+vhlKIg~iYt;iCu83FgfWM1@7JH)LCM^ybYtlM=Q)UWbC-Y}ebIG0d?"
    "%R3=OI)>Xo=#KYz$xwFvOt2!|Hl2WU91Y42Q@RtF_#=YDUIo4E`+xA-(P78a79iMBx)I|AM|xWmQT2=)"
    ";RVqlLB|xS?=RN;-&jFNLW4JRgCm9F+Sbx(%80^TA)lQj_pqgW)hZ`@9AJXA!uP)Evr|_B&)J%A4l7zk"
    ";)b8EhewY_VL&U84yvYUpG1i^Bs0UFgC6UYc27w)yG9r)9*t=JW8>k}sIg1D*+|j{obOKNlPtxOZYK`-"
    "TLtjApY=C!ng;MldLf=C5bigOvn?1hYJ{`)7Rs)Xj@p^#Yh-4r<F2yvMba26-H;x4pg&1?36Imiww|;d"
    "-q}uL!%iLC(XgVe^Nj{0VRAmF?TYHfSc;M2eNmd<J9hr`WE6b&HRyyH&-5<#WnD1$H8p!QLIRU!Qu!zJ"
    "ub=^+LS(Dp_?*vKn#%vxd$^XQXhRBE(z@KwWU=CAL(Y}!yh^+p)DWs-v|T30Iez*Qgac+mII*i^{rFz@"
    "vJX&`_(lHPth(gM;DRhjbvwbHFm72Vn&|OKk}DRIQ5fhnqLhhBLrEZhc9DC0CPEVrMr-y%_k73G{=2NE"
    "4s=kt0e)BkamPwBSeiaAoEsMEOk72aNCQYeXMLExEQ<?0y%UmGAmC8uC>gHSGLr9nY1@$8-)9HNKNa`$"
    "bvH+<Pr%bEm#s?6sxu;Ht>GVH6;1S5Wrdn}5o(gB54O&Y#p+S!cXt|GM}XrorRzdv8-#JIyLN3ve>sxx"
    ";T+OvX@Z(1PthS8PH#S~&V>ne`a#8Ci(_~MOFX`ljY7P>jKWiO-d0MIs8tT*yLGPPwo2TUgW>NJIG>XF"
    "b<dKhOqE#`yj(<RCjRFk0kbL`TH{D3d9oJt3I_iJ8r`asEG9%qSlfgc-!DF=$q@nyy+#{pf~PSTxtRWE"
    "i6TXbpYv3R;eosiyLblm{Vdpd2u@`tyO58`=}M%TiGZhR9;@MbqaZ2Hd%h=hek^vK5aW9`wS3sFBMH%3"
    "Xab}B(wL<LN1<`x>!>tiX3av8*OM@C#>}_b9Av@S%)PMhy$s;T*#Y5p<g7vV=*ySXO%`lY#i6!POh=B4"
    "@-@>HT|{K5konuw2-`6MS3SPw(tL>yIRx4BT&G`cgpcQh<@NRXk}KOd@{vA1Mo%B}VxNzPR>6-xHDlwy"
    "#?Le8z3C^))lezht@}<ZK-1i^veWW@J9T-8c^tR0ll+QHBkCYLW7u5UR;u-Sky6M<Cbb<1kct5#l7j0I"
    "9r!y3au35)mc`KAc#!Dr2G7_cmK?J>A!TCQ26RJ5s2NBbleO|E-kJEj$b48|ucR%8vKyJ5&ef$Ns7}VT"
    "b5Bax)R;legrFFAyl|rpsDJ0CJg7c)bT30q=-HOOE}#V58aK7?DGhhZwy2(u-FHVZ#)U~ZjR_bBQ6}x|"
    "s1&*xa3dB&4Ks&Fm+m^hJTDieFU4gB$?Rq!HL-sfoL~l{a7c9DJWdQtnx`97)THQRH%b@kN=O@Ul+nCG"
    "9dv2?(nbCx=BT3-Kx95Ppwo3gDqQjsEN*Gq3Br$xZc(=((V4Q7&^Ad~#>cYI2(MQQe{di5ucZ^|T=bq!"
    ">#OpCm6zSg9G9xGUl0c~-l;mi%GR(h*S?tN-wikP_7(t`d~uHI$j8k#kQbJu@?*gyC44N?pr|~rxC*{}"
    "FqC+>Jj~lyFAsvqb>62yA;$&1lieK~>C|1T9<&O5s8o3{qDJ9$Mgc14RoGE#c^MotTz#T_-}8Qv2vsZn"
    ")`=wov!{iPht(naQ18b4MoRF@`s&Qm_LNjr1;@$c-;2HMw9J=|^Te%2I<qU1Y#C3YhV(G66s|~(!Lx`L"
    "BOQx^RXN)G>9+FULAIkZMv+`eTFK`B6cZdYEfY)Z<k>|VYh=Q|ea$Sute$3(*7mfs7giuv_5$HMg{RPe"
    ";3l!&g6soy_GpA>OkOznK8WP(s}BtsE42pIq=T#U=XeUNK-!Wfq<l{H8CFMd`S_Pb{ANUjr`3}yN>VzX"
    "hZ`vY{7sXPZ=|_K-ZL-0yaX{YGA~pL3Qo3&z-Q7r1m^5IgyU*-U*HsZw?0**NNU%%#XDX5*?YC1l8PAZ"
    "7EK0bde2Xg2Ge|y2znm<Desb-t3r{qRTsohN{k&@vjHx}F?tR#&00*|=ysiPf4C<OkwWpb?<kIXJvj9J"
    "%#zVwKy}L?Ozej$LRoxPSL@Z(E!?KtDBuBzQeG+v{4=bbx<F=6FZ5`Q!$TESa3~%O6_$i5;mN8w>X^vM"
    "S2WSf`)gojTf<7$=B#+BRjQ|wd3dm^vYmS;FVCx^upW3lTyeqcNT91BSS!r<)ERoM;*q`LVpgfe^I{ms"
    "H7>1wxQAuI<HGT&m!`9R408qRTo1Zl5yxx81xA)63O89*>2yw%s;i<*7(aGcD20eXJ-iVOA{O3wV{~b<"
    "eiJc=_K<1X7|)tMo~gXj*VpTK){mUNWUBWlUtb@iy~ZJO@<YDlNBexfJ{yJ);iq(?@1+~#Ct@CNh<P2|"
    "gVPER8M#tGr?V4XxM^AwpV7@9`66lhZZDItL#2j%mgREZ(QJ}RVJkucFTA_$k;99J;v-><BQvM1W|k?)"
    "nhqt@scKMf8z`({6~PSa5zkJz?T|{mD)pj=rBL@xcb=_LJ)uaQ6s}AK!r?ouYZ#ww@omNOxb5gY2tdJa"
    "sx^!nJ9gc4UFTn8@@n(?Py4arm;f<`B+KSrx9(THgTpgE^-7fUJawkO?Ckrqi+XbOJ_W28if;8Bhf78x"
    "sqybuw`>gY*n8vWbEx*6Mm44X_p~c<3?e!{f?dVJp*Pw$J$+eq@`U3}_fg-~?z)*OM4vEU?EyKRnZ#p1"
    "Qc7yvgiAu=St$7`+o4LQid@GD7~76-J2g^nr$wPXcXd~)Ahyj+$wa$&v7nNvITS+b-;lcrQ`DGF_?!%("
    "am`y&V0DSZLejG`L$_*k7f~q(lm0Wc098H3m#=)0%2?vO7$qqXMn~+003A{<rQ+ijbp-_SmC@G|0YA5s"
    "wN#=(OAcPwz^SE9<Z<7_58IU;+6@^0p(E-|HlUKU?fYc1^z9@gB%^|OT+t5`Y0+okQcU-2@GKsD@WX{w"
    "70n&b;dC8`O;=>kv6Fs{D+c|Z6{bomMjU<IT<lE8?IKml-;Sq2V6R&TW5Z}X%4ZC}<SniIa)OdM)=h?="
    "*$D?d&OZS(Lqo-xE3snMo!|o<NK9(FuUpS54mUE|W5O7N9N^mlHC<2jnOMNbYgwTz#cxY8Yuqzt__&Tx"
    "5PVU~7~z!B^c}{0HJuBm`wAWwGrgcSllgA!0>&tf<@yt*khxIPv&u|NLZ`L+9Q3f99BR8)(-L_U&16Zc"
    "Vt_3@DbcMv<;piRY>n4NQ?T%fu3xPmEALm39np-UA&6M#Ghj5h7wohoSXEIfcQxr(RB$;P_&nk^3ji)Z"
    "A8F4>wvkjC2|u4qnWIQo<J)BuXu)ybOQ%5dLWT)V<YM~UpJa2wfE22q0zT58vy&jl+r==VXoJf{EqLDB"
    "I9nxDe~H9gjlExlaj8-hRvJR5QB_STB>WlakwsWFQ=RoDEVvBjT49dV(M0>?xRlQmVjLn*KjAYnBudby"
    "F>zd>u&mRNR##47MM?5jd!I9T^<t?>Z;=`2aB_l;f?83<%x!{K_kKdVQ`VbP;PCB6vVJ}+It|dp{i}#@"
    "#L@@uEM98%F6PmELB|8W&FD6=`czZ*OpDdBnTX+mHE~#@BVL4!p(j1D54{)Z_xa}j`uu$K*H`H?`af#="
    "eD+>uup3W#`ad5@Sh`K5aiq`ijN$ouwc0<P&rm*Mdi9^^dHg+kPWqwC$n$U+i$wC_4kZTHrF2Q>&S=<N"
    "5WAm!n^-i~yyNZ&+llo{1&6xV22y6d>2M~uoa1T+3!8R8hBc}Mvok|Fx}mx_dEe-cP1C5Lik!1!@3a+0"
    "YnFGmCt^I^$`Am)V=(lG48rw@lTJBpKcQXDgL1yq>4t1AZLnH8Oz%oNuUwrRal=;MHNjV@ux-#yHty^k"
    "a4t-zxuG0wqE(GM@MkhX%?o9m+Txw&U6!2D<?SG|$*4HlcVn|yMp0@v+0W?S&xV+`vHA!eb&1l2L4l+e"
    "TY(Jr)Y%eD9~|#Jl)Cg}d>jUPJLsf+v!89uWKCN%11O=6>1{Lhv<5Joh^;Ij?-8x__!ECT3Cz)iu`}pA"
    "+}NMVR*D7;%w1dam_;~(O(SPzbllKps!U+?DYlz9&=?M`GG?_w4-EtDuT{s9Nq(pRbhI-pJ(#6m#I!m`"
    "Xu#K4x^Nq}#mzgN<PB6C#9shTF9Dl3NZ)*B82pWq;#akvP!qxdHU85`LF2&HO71k=ik2@a<ZB`+U!qnB"
    "y@g{5=0uNVZ;|h+<~h;{^`4samU1Z?1Ska+Sm=vQcthbOGB?bMqYw8x^Ys93YpBW7c&729-)3#W?lmgB"
    "=11Y|uy0;ibSbieojl|`=<($Zq;t+I#7=E>sEoL`sbGg_KX}xj_C1zxSHm!@pOfcdVCX8pER)gVT>FZp"
    "<$6FXVW7w5oR}6Z|ES%iqo4g^R5XF2NURgj$Q>@Q`19u0SfN&$)8Un{4`#LL9cbFUPM0a{XxlSnOoATi"
    "81kEOT-|`P&28@zm0?qX)kF0;G~(4xJq<iyll@xdZzHs-tOIfmE3?(%Mtxfnt_^Ge(dBhOk*phNj-(^`"
    "l1YkGPPkE*)3^*Rj&cKO>2rFYGKzJHPC_?mh8Vu1tJIZi&p8v=BSXt{-sz^wX?BVyuuhA%_OnydP@?zU"
    "MBlk18VD4`ER<i90##mVUXVIO>R`Id<m0IeTNNVsDhTd&YuaISn{^d1FL|vb6jgf)4W-n~%rt1b7OQ-8"
    "q_vfimXdv*x7hwsJJ5k9Su?eSQ|{hIzxs!tsd}KLv3ur-9)ynCr96}PYgO+XIRT^!!v;?kf2bEmTDY<T"
    "keb?Lm3!yrGtn%FmS(!}MRNSn@sjP+rxXsiK-v1}Rd^)QrOY&+Oh4y0bn8_dZPIa_b8a7Y^+M@QdA1@A"
    "iZ^<r$7KuQE|;MIk~$+pN7ZJDTw@ju)JCY6sYEKC*(jNS;qg#7VFAb{2&IL&hVr|>IzIb+16{MQK0j+2"
    "&&N1EKR=4Bna7dqgo~dauh+-NT-(q2PQFTdJU&wokLS@|A3v<yzCrWfK<jY45!091SPnYb9XZJp{ZK2t"
    "`x->NRuUqnz_h$gPnVpoJ(fyKU)`fSB3bi*8vPH)x1&$qiY3xvzD5WqoD!n28R9@e*iCYHuCqpK+Koq&"
    "*8%lU%i2V!mCe`zjWL0HlTJtuR+hExn;=!GuQVh}h?tpZy+MGE;5Zi{UsHFM`cgNe?CZCIJ?V7xWVv_f"
    "i*Z-NLql^YRp4ft;jTB15nRJl!F3?w*dN=@cv#TKR@?SGl)j|zL^&1DQZg4Jv$UEq?(7>>F>2?CLRsmE"
    "1=~8}73&G{g{HizV`Y1pq%b2{P%7Vlh^M^chCPQRYos#$P&vD+dTUKb%a$e{Ma^*tj;VXOc|dPRrhqp_"
    "$E2ihr|YU0OLl+(qFiXMd%oaiBAO7L1RWhB&*M}lj@SrB7<kk)G8N>c7ZAqZH1Vm}LVu9n6di7Ait;e+"
    "1sa6Yq0BUJp*yv>JdfCDoq3n-{Bm}8(^!CXJ=lkC$Q8L=WI;9*N7ze_gOYc~A$x<a@YO~{^gx{qFvU@c"
    "3$3kam)<ngDR%}zVT40PJE-35sgTD~7aAN6J-gA~<{6UTzyquP!9RXhko5qClJ(FT1Qj~lMHD7wnhR{o"
    "zZmsE5)w6a?nXni$f;G_jNJguYv~lFN-ZA+(oKZ*rK{Fr+i072+)|lNGy_dKP2$P7*LAFNkqkQ}&}(FR"
    "JWdbW3dtO6s8=-wQvht=hTQJVCNJkMBRrXrBatq;?C!v4L6apbmk=RluNvbstSMwJOsm?fXzlw|P*ge6"
    "QvmSMz;Ww9SvSE?W0L%JUWRlsd~m3C@t|do-n<d6d~i?YJN;F*e&Scs2Z){^Ak<b3D9{xGQ;`lQ&Vt)<"
    "j5g3$G(6(!GI`(^8lCy^=w;T$;yW#~XUx8|Qg(NdD2ozm#s^G7cWsDOH^cBnK_?v)=^VFarH9~tS}Qa&"
    "{zm5z0QU?jDyUazvCCRVYn)35gLIgh2l1JBFsZl~C_;$M?L988;<Bo$^fyp9X6kMD)~Z~j;E91-N{G5w"
    "wB1$ZqocKTj&E8zFKLabDhjm2lPx`8eb|qe5YiT)V8KEa6<3ZEsLT^fc;3#5D%8&Jze<n~CL7~gA~I3`"
    "!>z&U{BaQ)QKX^VRdn8nvey@SV8QysO#RND{-R2q+o}>P5|%tCxBD!}SGs^RU5VkJGo2Z&8)>R8INA1j"
    "()~7oeZ2aFqC-X_Behrj44>n8#OEtNLwQXc8QbgmmC_^U<MkL{kMa5XjP3K|GsRc@;pAp$`ZrE)A-uuY"
    "arGXqE(WMTfz{sT^k*q6q68d0AykgC8;NDT3gt`J1As|8^415-*;G>*d%PpulIKK6N2GR&jCY@?2(NOi"
    "az;(PEE`%*S|**l6g9NF`q+2>f$=&<_w{tPj%BY#_CeUs;jn?yQQePe)h1^1i;}<+HEc%N-rP2?x@r=B"
    "L9@28d4}$RpJ32(QW1XJgJ!RN8e#*}nGt#HEG>c_T%ug;cJClCIbp&3qZCJDs+vtrwK~<Yq5th3pYnH!"
    "rb@-y<JQG5dANC^{FJgM292GNCPQj7d_XY|TJW7yXX==;tt9>}<>Pzy)w@M8XDf0xHBlvWaPt7@dpXUp"
    "oetcOCzfuq5P$<gINH#XrqovUe%u}qg+q}Rl3iCyteeFi-ILnXUe)n+OPgZGm2y&6im{SB?6rh$9)Wv-"
    "lx{j?Dkm<jho_iHb%zdVos*_K!xr2!p0Vi_q?}1bHrxd<)!X=ntW=~V*o|0Csp;f0DOZP2_RJPLd{Pty"
    "b{N3+w*aK00UC6;7Y6yY-f6IOc)_gfS#6D0ze!DH16F(m_SK?S6)eqUL0rCF!f1($*u%wls&AZ{(u(!*"
    "&E+C&&XBSHT!d01cXb&Es-)97d!E;1J`|-c_7t#Z$a#@1L>%AUhBWM-SXaGc)TkGUczgO5XoqBDq+ftF"
    "r;F{!O$rJG8vx>4^T@5<-pG1v|3qZtwFMUONN7fKgs@Z`vN^|UW>TtD=2@vzgE?m&)EHOwZ*>1tILC*G"
    "&@C2YV{pTC)NrxT(`lV?5KbAfIw(f-9a(#;7@;|HR``>4_q0UG;hfeDsP5&`vShyX@Vy5#qxH1*Vj#In"
    "J8g022#~kYJ$7b}ln;=9ApD#uj<TZVPO#56T2;W}IF|BE<WF3NEd+^I#AB=IjhMVjAasONpcva)`!BzY"
    "L4ya(*6I$nlASVYF5Z$qNA*JFz~Et<Kv27_!Dbx4a;WtVXakgN2N{5@tF1{Y9NzgdY6<nKvQOsn;B}@P"
    ")NL!cKCOQ58PcVyy3!6CYcUs1xWEHgG7~WtPAwrfsha4A$C=AJMSM-ko?{|mc?fUq$F7)oa!bS82&oXQ"
    "r1!On=x*^*W(bLg(+zal!P872(k^38)HTo<3Leh}s~oNImxZc#ZCGc+sq^JVxv_#-y15(9AVwfIYl}+$"
    "ee>b;`SJM5&-5|#!}j^=_0@HhJ?HWKRYU#!JRTqAc-8h1+r+7@eD=rdRli;;Mx~#SHT(u-jaSGT*CB5~"
    "Eh3aKHvpz_>gs8~^RKe|fW*FSW~o7~>6E)|rK$5YDQ7E*ds>g3hk^1DT%v<SVYV>|8-yw26lnl(<*6RN"
    "{ytv;neYwyN{_eJccj$4ogFR_+X(r*?_8|}?p0{gg3~E<?ASp3i)T<_bE?$0bxIg+IH7<>HxSLxTUIxK"
    "PCU3Y>KNR$%efMHZ=SP0vwXZccAaI+gABv<QIlNvwwuR?&jaoOci~9fFH+chGS}1I_-;*#3Vs{2i+GN<"
    "AgevCWx}?HG3DbN8km(WS9=-9orYOVAW~=%6K)ov8)i2@m~rz=Y9^NzHx&BLEJZ1KP5oP&V}Gg8>Q3$}"
    "z;k?`|ABe8abw=bD0;N&ayPNzL*A-Qn43mv+?p_kK*T+QRed-&<{P?G%##OpJ}0pKY7N8}g{tPI^W&Gr"
    "15Izz_Nl3!0n?$hy&|3}3-cN@i9JcLUw4xM<tZ$#2SUo84%No;o5_-rO-nd4j2e<O4yEie;N~8fdE0~W"
    "cY_3_{!LS%GzCy^$lHYC=S!xaeMRxunGHs%#M7rHdr;GG1n3v$Q0Ln?nG+8JR>dF?osg@qOLrKR2Z$-R"
    "Txbx@*;Z99v~xfE9+_c;y9+Q~=e=i}Uy3IMtHy63YzWjlxu}X27X;Dj_tn08VsU9mZW%YBbcguFr2PjB"
    "3F`hRr;{|60JtVoCR1ohN4w(qZz%_c5e;tuJvdB3mS{UaQL0;}Aq!>81ePjD@NCP~R)*GGJ=6Y;g#&hH"
    "S+uWW+=y2L=A^eOc*xEkKx+jMnC|YGDe=uSj@d%2n7aqdC%e9mRf`KTi{Mk`Z@U<?SdYU^{l_Wv{>kKb"
    "iwEQ~hqY`y+rlx;B@C>trgs{3BZ6iuEKkchRTc%nqr1=F+!HIqsDkn-x^l%Z>0t=Nhq2lbS9jdd$x&}U"
    "-eBlCz32!$)=sKuSJ)QLnks`|3lp4U#x+yZN?-|o{uWY61}L6GkW^@*s~V^OpcClA+6He4<uOXc_+hP("
    "Ond3NoQenGDW!Fbp3o@axV&}#$=JfRF9rDTE<;T$MTn9`rKQ#LSf_ZFompp04YtKH_c|3Xv<Jt_92zvF"
    "BU=!o!~(}>DdEH`t$AURCIX_=g=K2w>9AK|gAl%ecsK8AE7WQ}{@Y-w<n}!?B_3<DAf>DVho9)Srq7{("
    "#N6ee6sPrzY(m8^foecNqUkQ0@E~@qBAL@lCBfaho)!-L`7<22Yd_1N8!-Q{IA7ZC>fW%5ABb!pqA_Jz"
    "P3Q7CZOyu$bXd@nv6I2m9>;=S#&5Uu<@R`dOaMP)`eUZpuUbBfI$68O=DDOFeJ=LL{HE9EXZ@UCIQlC+"
    "TX{Sl`S|MjCytLlaeUw7`1FS3*RglxA!xwev<E-B8D4f;^+Y0t#Vnf^eTn-y(X-Z?!1u0?pH(C#cGv=="
    "Z|z#YMSa!P)Wm_i(-_#PisA$vn8QM#cPOtaWVBt1eNuKHlM-b>@q{l#IxCJFQ!yEzm+vHz;jee~s%<>Q"
    "JW|dR8+@#UjqxvZGp)z8yD=EP?+D^bRaS|tFzt9B6ZE6)%-wq$H$ltDu(t7CE#RI>y9oAkOmyE>7mR0M"
    "#pD}=t;o)muc-X5US8B#dL!l7^5U>(;LE7?1ttNMwi~n}ju{J1)a;7FV+R$fdAn>J4@!iE>}WS+FrS9M"
    "hBv`YM_biNu>Zamen01JhaFOmLR6JPd#8h~oQ7UIwi!P1V59&IH9Y>f^Fya=Qx6i0hKAhXsQWq6hiAW$"
    "%<<MWX=kU<5U~!xL9eF5d>Wfh*r2qPj(P?2uIYg^JZ;n=jmfu}`L;Eni5!13L7J*?qgtfSa}6x5G|@1{"
    "bdm94jauz+L$8WO2Tbd|g?8;*zqzF)v~TCyhP_KSgSvXnnalKSLSc^Ht&m0pD_Pc9=~#D()58<()#{mo"
    "ni)p+yjo@7X)ZKtan8zQB1^V^nq9L!1bR_xwo?)sL_B#80-j?>JI5k~vIIpHZ=$+9Njw>zP|7)$3#HT*"
    "P-6q@wn0#h9ibCG-ec`FBHhE}I2C)e1a&M7hP3xHvi-yY^m#FSE2*xS3yl&Gboc@HzFKo33K5v$IKPu>"
    "XI$RSZh8sIR}HdIIfVjSUVz>0KO3CXtcA7l{lf5og}j(A7Rbmc2y6?N*<&6*sS(6lJBg952RWz=x-|XM"
    "w7^ebrrMAP8+j^<V0P<fyID{1IvG(wuAq;Z7k>&%3e9~K7S~SMe_pJNhG}}HD2q!5=JKltHAaU_`n@ya"
    "TFuAiyepC@ZSb0wa~PIh3byd837rmmn=I&Pn3)@cuUAl=kF#%69jKyzxJ=F35t+SMSw_WV(lX`!5eEmx"
    "lG}P7L&$X?pZ2atI^uYrIQvAAWf!D0y+^=d<=}%%B0AHa7;B(ZGawok<=`Rnmwln-7UY3fn)QgDje^<+"
    ">Cy_WEqC#vrMv4K1lhA^iqaEsDPdt(ryj|Y?Ul)eC=6DZ^_0k_(i+qlyewI2p^Q4?FtLWkBjX-=^3rv9"
    "kxF733w7A7fC`wCTo1!d>j~fS#aFj_hax|0(qOqe^Fe>E#ew?^X5W~?3a+`qT@Ox^c?uPx3%aJT+3X3M"
    ")c!!bX#u6vf|cok?K9c?U3C3Q<@tE_=jYIf@$l+1P5ubN*pKj4K3=hF6w2%K_&7eF&&Q`4;=WoK&#$>Q"
    "bNt!z2Xg)!i@A{B(Dgc^PuoseRb)VW#_i%A%?*!<rVPk1<DJo)txCz=imNnREh$N9b$#qkBkR5Fr}kos"
    "LM^wPM;Z05_X!L6HnewW`lnd7x0kRSnqhce5?fCV4LnCJs<W1vvH6?`vTH{R)}V11lNVoPQNLh^2)sm#"
    "ErmESBOB3lJ)2>JL`Y~B!_FRr8fEydjNR#c9s9W_^w<}Z2hru$cTK|)esPTA$26-dZ>M+LHe1v7=Gz!b"
    "0s2mJLLw_AXuyCdFr;)lG~A}PR2$We4^NQuZaTHrQ{r^Q9!pBxU5g^R=XefRkcfq0qOI;2V>5)F{?HNq"
    "Ks#*A4t44wPh^BxWH^N={!NFZBt=BC#xO`T1UqvQtWc{!R+gt;0&AzXdGN6xOkq|<o33=6q{@-DMji=b"
    "2mS#gVD-w;RJrNR_36RnWTnp%(rxZ4Sh=Z_zM{lvk)l%^+jd)eQ4STM?Rp~Ov;WP!lfXbPJOF~JYEDuR"
    "Qdp1JHqODo7;B))W8*i6h@Owj&}irp{mW_bme0mmJnG);1>l|3+nGFVJ9%U?wg8v;#L2qTahfyRHzqQM"
    ";Z`}wmfhi2PfrHpOvK~7dyWNcG%5e$V1S(fleeQ}q(CEdcsOArvF_K2b=9Nc1F<++ze$cK%G4b=S4m|a"
    "r=#ZGFpx$FewC@?YuRkrgO;ofYdD)8$Sa8VwVa|h@=PB5Ll0sz;3DNc!2fl1Nr*JM*|@TM=c8cOb$N98"
    "MV%`KUB}5evJuUu=M2fyijP`ldpJ%|S*ME+(L8R1&fPTO=BnxK$s^&S`nZw;Q5bfER@uYmAZ?vF)9^`h"
    "8T2^eMZ)g8;fQpxJiCiOE*LF}Dx_&!Z9q1WSpXxDH`3D{b@&B~%g6+E3}cD0X1%o9;$BamBZah*P7xPw"
    "4?^5)?@2H%nZ9>~g#T(HEk4Hu5j_I!;sfY@+QT!wW&O@nY?`ofv!V&@$2Jn>@9FJsv!T_toz)hGQsveD"
    "qz)5SR9ng3$T0A5O^63Qsd~+M1XK&tV5n*ooP~8rxlg-$SjELn4++$~nBuB3-F)~$SKK95f6LQb5swPG"
    "eo1VztSh}|*vCtRj|J~u(Q>&_%o?V+IN&gk5{#@%tWT64qGVVlp&zF}laya#WOw4=aAmP0^Ad-R%CRk<"
    "dxQNzdq`ZEC6ewQ@cs#y5X!qur1t46FpgC|9i0-B<1#XX<43}>JB{@j+sw3@3eIcJhl>NsK(Hug?gTSA"
    "MSIH*9L?_W+xqFp*O<%iH6zr_R^rI>(SFV4^fAWAI9?-#_SHVabFSRy>*!6ol;iU&e~j`}>0=?W^KZcH"
    "@&>chMU0~9s4{2WX;Fe?CF-Pqrzml^ntxxn(=eojoEeb2b>h~30z$|Bn)yZ}{AR3zXGk$XAemh#yOC>*"
    "4%4*u;hgLE6YB|u)j<D!&@p8e@y{F`v?8^_l1Kg+LdR|5kUW(IwWcFi+xb_^e{T$@>_RSimk&gMPjGf#"
    "{dn?rX1E)}Q$ES0il%Dwy|yk9b=D~wNA0Yg=>)x)(dSe_;D=}P&b6<ZzPQomX-VOh{B=+Yo+H%BayTJ&"
    "FL8#)hF&ZS6zW;m-87hR*b@sv88x`-$azP&$ANXU@UCQIR7Y7#J0wjH6oXvsdl@~jZs*-cnjsUV8T~yY"
    "B;~CR-?BXVlJVJqcGyT%Xa$_XQYivsl$jEc$Dgp&I{1di4xrsuVLbPpne{MiHTBdyC~lJ@hZcQ2XpR)r"
    "x*7}8ZW5&m-w=57?CFshui`JBsDFv1ar7N_;6522>R7Bdx~~?!7QMq14Cnj8c$!q?W>B=eLxz%ddA>0("
    "gqdpJP}U-kRfdKC0($vEdLH};Grb`fnsja!(Y4XTDRBm2@P?S%wcibANR1dC-<){Dq5^Yr)vzxoGExdj"
    "Zc{vm%O8wb)dOj#l({U~Q8fvPlbUSaB?QK?0C7*n+2!Jw!Kc~`N$Pfu7ST+?)0&8$=4G^U_k9famN0@*"
    "fE~xZNHf)y6}a1#DxfYCmD*5@fDF+okL!$A?3yVVX${Ci7w3#<6KWi<F7<+jhqkNYSU}>GC4DHsaiu!H"
    "*JnN@`V{!Ax6#5eQ<iUQ<&8Os!Mcn@MO<ATO0vSKZduYFDg)onMX+^R%E@z*N$60tT$S|7?E*c&Y?$MA"
    "4u@e<EX4j#GZj?az0#>7GYhPZg0ZIr(3fcy$yOAH>mtFU1ErgAbHhQoRh5l3Rt3!S(l5aQQwPIvV}SNs"
    "1~7)p#EoY9pr4bZD%O%(g-DT2k1hHv<}8o~dq|-$dh|?366Y02H<1{*9lusg#xXZCTV>e#g>-5$(2&X~"
    "E3@JGM|{YY4g~w1+c_(i3+Y~M_zciv8PF}JsX}7v!)1syvE^(O(Y6-jK(j`K=Zk4g^XYo1s&k(m=PdJt"
    "pDc|p(Pi1CfB?Ji7PPs)nQ#E;R94ENFvdBGbX{OrL96BUu$_B=wQHvu?b3+QJe3xC+v!DC=!vxJq}Z>v"
    "cEL8rHo~H-^O^B2x$_?I1@=6bSk|%dp7BooOW-ZjPLaZ|ZVwrd(CXBW-?!0tejUe0ijpvV=C3ND-4XLk"
    "b>NR9J;TJ)$5)xix%cr*H9roqR56Z^&+z&26GfNbK+*LLMX&P&as9ko)V-mz_}lGYN$fozoPJ=}{l$Ps"
    "L91KXTexXip$<NLqTIrEBr&sx7!iR6A5@*UaLLmTLi(qLM%dbuNgC%N3z8;O>+|;$Iu7O(1{dOO;<KF<"
    "6A!xJU~W&|D(zsj@UcLbyk*ocoVIMfB7l8|Xx|e}f;w)ep_Ut2uxf=Su?@}JE9pb9n-4dzMVysnJ<@1x"
    "P+E_?9bq2b4j)u1V&dw(?{vPw3g;d?@{n}P1>@aonQx>qbu7tJP(C+h*L#V(STHrCm>F6-ZFx32XNWEI"
    "+U<MhamqUgEm9_6q2)>xlbXtQ8cai^qX`TesSsVH*v{wyk7$^#OfIc8+kIs6_v&HB=3&2D=_9v2fL5A_"
    "RuWqX4W5lh+!=9rmgBcbvI%D5s`)P3XAn}6gAtS5B>l}t+r6fKR&F%Sfu6I2SiLnvxtP;wk4Y!Sq(Ocm"
    "d0f{@tC@7l?o9xOdS-fMfXY}NHLZMBVZb-x2BL~fhYICXShyFQdGne0-l?+NmX5Zri)rlv$j#^A0GRP)"
    "8I;mHqqv{PB{O_s{go_r&z)>8&2uWP%AHORLhRquPPL>=cq2ZHM_(rl!yT%BFj*6!NQkv0CwOE?#wBgB"
    "xfydPMCBgYmU1cv9JkeZn$eQ1B@M$7$4tu-9yXBn>l7h5nGz7wx0i{zv3i>6uq1%tOG_{ZCuYDB{Mc+s"
    "e$Fj<)L5%)4O^g`f)<wVrw6d%9k(Jm#2Sd1p%^`TUA7Y6y`-wNdjK$Vmsj(LZuEm=A&q6nDF=+@>`4=I"
    "x~R^mfyvqKY?bUzgc@?ia9Xrqivp1KvZf(_gMyb_saefr!Pn2;Pv@8l45HSN*Go1T(8%IHxlZ&{p~4fy"
    "#R-$7$&4e(eigbjARkzTlA(j5E55HZS!%)`?X8jt6Y!YldXY+qfX*GeJ%U@y|FjZzpTg>#>bcf7_LhVl"
    "i;SSy6EqYj=5)2=Qj?`8hP#ViU65Er89+-$b!qUxxEsHzXsLQNiq;T9l}E-oq<)3b4KsH26nmNjePrZ<"
    "M7ve5R3e$h!S>^?<M?M6Dp}rf4z^h6JAFL*dBS~m8>MhhNv5!w;<!#lmnJ4FAD8Bso$g9$_N@d1<X*3K"
    "9?YFrWd+f$)4_nVHkxZ-)X%Ru+|k-;l?YC3T_WPZ9_z%KXn{18J$VMEbeYl(iDhQEYU*px?I8o2LBd_&"
    "CdmtM3*_cC1LvI6@Vj98;~C4Big;g9vh5PSdaR!_N`B1E@mZhcBadf3K9i;m#<`~RXPz;s&+t>*D?NUK"
    ">G~UBy1jwv>u^DQc@Ljzj3NlfrcO=sDJf+5W<Yj63&Zt<!QfOl=e`|Os8o;n#;M|n6~nggs^X}vf*2-<"
    "JpNpE&_yzDow_)M6bON|u_X3f)nlHx^NHRh_zk=AwRCaVN_TTx%7FVG&K?72Dz(AWO}Sy_Zgw;6jA{yY"
    "aF3<`N%LC7<Q!{pSuuy5?_WA?1aHivXS+~R-ciC9h9aNh!1C$0BT!Y>YR!9M24#&_-nCZV2lf=GMb!Qi"
    "G$<*gom|7G$H3Y)lwTBN+o@C}(xV^zPAx3b6`i+s9%8DKidfn8_~7=$onsw2mFNJB2Ql*5O`qq6?}ZU%"
    "%w1rTWeH=er-^z-y%-@90OEB>!7tsxVahC^l5e7iQrNW0M$LMe!Iat2g$WMweb_ZQ1l;BkqIAy-IZ!-o"
    "J-wGY0*BWP|0iR8{)gH>E(a_|Vqq9%0`ZEuOwbEq@M4e0JOZ5~9GLx^c&?1YxUF|=jqk8EDAvZ+aAqb@"
    "Z=PFfd#P9@G`meGcXNx?#I&ICa&d3>HVenM4y+>}Ewo<nU+SenQAxPu<wy=7vK(p}V}fu6xfpNQa>sQM"
    "jO<7kP?KsB{kVviVTv+U8`>6BbWltfF4-@-mU2^;rj{(V?A~SksYlt(rM^|zlpm_K^Moj9&#Px&)Bd)i"
    "P0KLknGq!_4pvB1kNQ2qXS~qb2!ynW`ut(UxV<`t!&zuP$bx4fDyq90$b&*=YP9O+f^zCaU56^@BQnI5"
    "coQZ7(En)fv&;aJg&Dz9p4yJsSzFCk4~{`M7I}1<8gPXf;Mh1k&4Q$@B4Wx8PAgLrd5{x031z6@N9u!V"
    "iJg%<vw7Mzze}1ThNaB}zp4{9i-KX5^Tl^b9FqA>5!xLg$?#zyH5%QlmozE3L8rL!2Nf%Bc?E6q9Ur8N"
    "^dqVo%H`9Pidr~YDWd*K=56=2D>zduILIfNQPMNh96`hsL==15h3jZKIIvFZsC-Y)H>qC&RuY<MbZIta"
    "{!VizF@|YwHIWM}+1CPQm4qUnF3c^=mK3=&KRC&O>-kxewNjg&yQD6s+9(c?a>;}TerO%al!E)U=zdVE"
    "NM+XLcPp}oUCcu;zja(Qs1FT!Jl!d=n^P?zudTn$lK~m$<T<%Lm`9_dFEGY#EKEt%s!F<(4A&MV2c+*Y"
    "9t<#1VLG*XF%!WtMPhxAh(bfv$LY_D&#pw*A^a|komtJ}b4=hm|Nrsz`T6Q!^SM4to*7Q+uk;#nSuW+H"
    "&mWs>x=j2$gTYb8D}3cw`w3&)Z`gdi&B%_IiGSM4u>X;`uLCab{ButaN@*$jEp2T%+F9gn{0pYjJ7!b~"
    "H*zuju`R`^X@?i21xAKvZL*WSooY3zc%}khV)6pVR@wkXdI{AIf`|aPv>WuT<zvq#4=I(qb1&QeJ2n3*"
    "u7v|XJZ-yoF3rsxu7{kwK-saa@pN2}Sc<U}Z7UB}jZpkRz`n92GlPH9co&cr#nWGLKBaBPpQ<ta+oZw1"
    "(A$BDIMI`#cPYCh4*`s9L<OOos3Uj=(YJH=2EYcqg7WF86_0eztKO(i1j7__v*J57sj|b*J~-5-m8Jen"
    "&`GIo+WC^r>qMFpX|pR?8-EwKTW0sYXrhG+mb9<$=CU-qm4yyphb`e4J2Q&|-(TE{DnBV^DQq<*9VHN1"
    "7$go(UN!#>C5uhNx05Hs@$i;}rq_h}we_gbrFU9GWO{xXf5!p6pdyTkzkx22e>4H8Jp{ezzqzA$UBFkg"
    ")2!_?f{5S2{0D0DrV7@Yv@m{$AMD}g;jEFe6MJSA|72gc@H4zH3PexegHgGy#}(>O)W&CW!nw<vHRYxQ"
    "Ij*L;jZq$oclbgvJ^&RSdIt@ny(AFo!nE-qP8-=~mhtqSM%S9x{7V#)*aCQx?37Vy<tgsy7YEe?1L0V)"
    "t(u3fg<vWm*lifsz_o=dH74EK59bCWYvG1K+YCOdL|B@Y(QF`utum9~Jf%?*iOb$URiCG?r)DIOdMT_%"
    "CwA+M<L@IO)iYXQNtZB)BvrwSeyP~j@5b#|;1yYl2Xjv;vUpJ9WyrZRTiXY*n`BQ)|D-i7dMADD(4?)w"
    "rXjXfq>*QWHN?Gg++W=*wLgPyiAmVmTG51rN8l-W+GnemE@fsXqSL@v7&t27X!V%!sJ7{JN$`}8%A!Ul"
    "1-K>QV5BeAR=PkL253aMUh57bv$CuJVG4nUowjvKt-$Z`eZaCgdf@zme6B)|Wvs)5vWIuz;%~ci4@RZR"
    "hL@CrO1?Pm$&*9eY*DbF1!Z`C43ub$7ik?s>fG@6%~B!~M{y8|qoKsry1)VxF|b)De=PQ?#2^W+b+;A4"
    "s>)3sMuZvAudYQ{*HkQ=W9Y(VfS?^ILU*0P?H_bDNJXj>yPVRdb%?cqu@7y8;?dJ_JsdN7xcgC7zM=h7"
    "t(45KS8MlaUXXn>T;SRWB_fiW0n`dYceY>63`OxAA(2@5w}<hCuU8SOEsy^7NMDc7{CecC)L!HDar9n3"
    "YJYyj{B=Ah=zcwpQ2HZ(i1z+^)}Eg~fo=Z{VEZ=8I$lQcDM`Zygl?j-t*f(ZP}-}KrQ|bh%jL{ZSKe-y"
    "$?j2@Z$~~1$2idkyj3iHTZ8V^6asi6pZcNgB<s;l4+W1_@Yu4j6H(3(NfI2m-{OkoX0X}0-R-_3Pnjca"
    "4VN|KH=$D;DC+2&+4TD*x`Zm7?8T#|c9zwib~x~fBU+E09bcx$fgcfS9y&H^+M-)`U&HP=>k~22cO(Cj"
    ")RCSXs8<{g$IW+mE0MA(HH`Tqz3jXB=Wch&>AM^hPTSR8jv$6Kcp?}fh#Wlah~y}`EUCDbR3aW&MC~LL"
    "NGvP151moT)^Tp`DKX%*sIw#Ltj_8`P(gA_%GczXS&G@Hu_dTTn|)L1>J{XGsBKy!acsW-oN+D%Ri%rn"
    "9cqp0yUF109<m*`PTi8dP5#<mf_J3uVn&wIAIoZxs%{-Z$0$Eb*1~r>sajZpkGMFf%co7cGgKcUt!Qyp"
    "Sv}a#@24!fx|}CZtM86$noGgh;ZjZ&qa&E#&hDq`#(7LV)U3C9C^nBGJpFla&5%M52vaQOyVPkIF$u|r"
    "`&C7HgiygU&2eG+4@)-Bxt)xPkb+>M5k!#bqD0hE8c5{zP!u4t&wE$H()!FpJAI_112OrkM@ZnpEI+K("
    "BA1Sfj?0%~h8?D5|JqI)sc<==wf7>f5FRxL+Q*M9sBlSsI(Ntwl83V!l~I#5-OjlMOdU8bjl=4~6gL{q"
    "88^hR#K=C})H-f|>um3K9szVcnASy7Lwg+hwRmBGnIWQ!X8GoCFoM>%o#x0It9wy?tD13Oh^ttjRyDP-"
    "*%M?v^hKHX{;O|5B$*_6Nd|b<eJqKTSvCrYZeK${7v%ThT5gE;MO~7YfP-7pS7F;i{~6kJoDEp^<KkAV"
    "3>E1T1&|P6{rb0^3bvW~VryA7t@=jI&x4(VPaeTIEc3^5EA$^?lg=TpmOq5ZK_-(x^pzZtD*+vvcgDN0"
    "%aU%Ib0mw%m?w6*xXmR~5^#nRRwZ8;B*@y4jO{y;HXaXl5UR_0_UCYka3Sug2B9$*hGechl?U+<8QyE2"
    "1*;<s<H=P-WQd$6o1}vzgw|q}W@nys8DE4B3)_I|(T)h0)V!3ine7+eTEUDGvIKMOwAE^M4P<w$HJ}vT"
    "W9WU*4;l2bMWdw{82v2bn7hny8y1+A=4JH<>n-yMNuGM)y1i}0B^M2}(j}d?;>9p;CEzgGO!fkZo>YZN"
    "bwAC8qSiS>Hh+qr^+FDpKP8d_QrlB6E7@1#kXIviiIF;`5)t*v(5!;@pfzR`&bt)h``aV1zaAre&Ya<E"
    "!pF~<-F+SDsJ+an`86@ySM6W*b9}_-NBS)FRoY{Gj^p_mpO0K7PXCFze`5r8e4Eo3`~OebnP5kfV@dKt"
    "^w)+RI1bnQA7M;I;gJL!SsC+Yx;ncug7n1<_7_#r*Ps&zqa}8Gr<w@Sn><e>244)74>dOrEn&^dG)I)f"
    "kHY<C^v$2s`#ei-!9z_yr16S`eiA-LA2?dnlsR^Jj1%rz8N-qif!k-ZbV|@xY{z{jCA8xc#L&Z8?<t8z"
    "!@Mlv$V*7%KbW+{j99|{pan91+SibAjTIZ?jersND5uVv)M5CG25Vr!=%<p~oBLpYDdPm8qS8UoqK#B#"
    "isRc;{Z~4I2f?T{2c<<e<fL;PRNqz*-tP-3sh-7S97%3^dSsY+o;Bq;@;HG&lCo%3M#nO*q<X5%2Pe7a"
    "40yJ^LP{;1U=tonYy2Z6My{S@9HkqN@CWRK?mT$f(GUDS^AA<&s4%EnNyZbJIwk{AMH!+fstqP$KlN@7"
    "BI`s7YlITX$~`6oEn8=l2m!NC<T}&pSXsAgXDCt68(0UO0>LA|PUuHlN4CY&N3aXHNu8WcQtz_Hqoi`("
    "8_Fzz>r4Uw6So(7MgiC0x!A*b8D%D6NT{&kY=yAZfQn(9>@SWpm~Jt7<d+G!Mz2V_R67L=aFn2wK*3Il"
    ";KImYCas6SW$sd8P>!HjbBOijODGA?8T4H7db>GN1N2W`t9gf@R0kh4$_Q&+spSF-<<-^@<PjuQkI9xZ"
    "7&LhWv`b)Ky5d?FVp143ou>>foH1nqWd<DJ+P((z3Mu<_8Yyp;&_KSOxEk8M8x-R|Q`H77`Gdf*aP%H+"
    "$yFs3ZU)gs2IUDQW6BVwZM%<etDDT8WXMCh=S@fCqR`cVfhlfj>LMoR*|VkTv@_(Ba2z!qYpRALc~$0H"
    "AebEyYtXbQ^J_5tL)BB!(#{Z8eKx-Oy6L^KIy!Xu!ubF-!ck<Mgcb}J)N~o8Fz#=67mLqOR}wDpW9cdr"
    "seq--MQ5~Z3zGf5rCC0qFGUI-UA59aY_Ey+eby>HITLHlh$V92vijw*KP%G=M+cr=eNphR(Q`}A^=`|`"
    "c6%cqVzMf<2Dfy4ItY-?zHR5$w8=*{8ny;Rvm+yvjg?19*M|n<f`Tghm_DRPztpvZOnJElOL24?ih3sh"
    "+P_8}|EYSPL-)5yIpiP+;II_Zs)ERTam~wUbILLj$dh%cttEs^>3MB$lIi6!HbKgTtW;(5<kX`-(w?G$"
    "hjtWOTD7D?{6169Ja>>2pfX$+5kdf|mu$gqMWLn!zWkkEqzwnb@p1Xq8LVO@h}kC%n(q$rx)Hmgren!m"
    "XU>nzsp9#pI?a>vDrlKQ0jv`CJ1hHO3B&qjMNo3<@ZcNzCi{I_{B7O+89&SC_xn#(=JHQT_amUlkkG!{"
    "&-MLYKR(|-?gOQj&(y{ktzTbX<LfKje{Y1Z`2DNyj@Mt*-7f)yaSs@TILXcryKV@FGDe#J&P+gG>WRXD"
    "m78?~nNm!)j#5$_`wVpeGA2(7&VDNyh{}w^t)<SV(ZN~gY^+&J6D<4a@dVx?ePgbrv09(7UmDj0FrWjI"
    "I!WL0tV_-4TN?SVv+s-f=+|oiqspA<l!I7?Y%pzNQ8innbu#~D9@H`$$8=2+{-YlG1kJ4}BOxjn)fnki"
    "CTo8I(p|G|&7Ji4ET`|8R0F3j-Om|93J#KUvx+o8cRe;A<p&UniW<j2xd7z}+mB)$nWiP2NP1EP%!oA|"
    "8y#IO6{WpuhK%Zx>A@@3d(hP-(kIh>d|u{c9%USo(W80iY{T>$&rL^vb0Uk*yV@CQv?C9Nm}+7Vsve~k"
    "j8aMmpQ~zujOBl*&MNRedi>vsB>p^3flK!8>So2I8`nQ0Ww0<f3~5MoY8xQu{;asC^l{4_yf4h#q#J>*"
    "4h-4BD2FG(cLiQ+$4L#wy8nS_ghvd{-j#e=pK0Az63g9=gOf^(LCT)hOb3yQYkgF)JZ~{sV6R%2$^r2p"
    "!0Hhu4=quWVNhDuy!A=99^T?nH@hXakMP>#lxQNt1p6cnwyEU_-vw*GX-NgKjHFz2FBQf!@doDzA8LFt"
    "_R$x{I`<cfM1VDl5ikMpTV}7QuGE>i-qa&9C8Do&6PL7$XoH~u^wcbqGhKf6@*>W0URwDAoydyIwOyR6"
    "Yu!V7`ylr~9c_Yi_skmL(@ixef0Aj+=r*iy1z<`U8ckL@sUJocx2#h`rF9)E??UoK^SaR=D4ISJqA@0A"
    "WMiO8v|ZnvDuR(rMEwENi;Ms*Iqt{IKCO<HF)<c?;5L-mFw?%4w>84{K{{M;>%}2;pH7HK?B-2tOqfXv"
    "0jppj*hMe9%<D-TE@|LaV}MxX;$U+6b|S^AKi5Ey-*u4oo;J;ejzBeGk#uY1+?_UejP$nJEkk{7TI7of"
    "a*P5gW_sbvbG2J*O9jWi(b`)>4q8vWgT}E^2*$iJgFEsc2psSu>0p6ezzEDJBip947mQX!yTF;xAVa1m"
    "e7G_}Y)~kJ+AJy!xS$7ulh`LkzFwQ22h<g-j{b(AThbhjg6>~YW^KJnRH7KZQHmkeTnTY|*Y}twenWHU"
    "7I)7m$HM*nA)#?)4h+Y*PM+%PdW{@1aED-FBrLZd0FD&ZbzOQnLktsVLy+L6YUBjKMO$HsiBuY{D)9S-"
    "G>Z6(<EL4o<(RaDK!C?|{cAGDeb0Tj_v`CDe$>zY^-;&?{Zqtm{tBah$NEu4W&eq)-^%CL72dD>@&5Di"
    "ewT9f<N94bhrcMFU&0R4b;#!iPr=kigVlZr4^c%2?T!0bF6v_(GD7-5x~dcRay{?x5&06>g?y_Yg`7I#"
    "Njhx-l0;AaWY2SjhU701-*tLr%<B5|Z4?hdUdxFJzQ$A;BUN=lpVsiYeFhi>9vX0tT0a}w*s!NJ^Ed#j"
    "^n;E?gIF@Qb*?ZqKXm|Xt#M;_3rp_r@0^ZkVzvmaGA~Vp?RCr)Oi*(R4_5{!yrGv#tTVF}eWGe%9%l!u"
    "VVR?{Dg5Fj3+*U#r*UWE*r{-XCOxNuSPgh|tT^{^n=ZnG-bN=mo32FmY4D`%<%)J$uS2RyRji}!bP+}#"
    "h*x{=WDS`-J4#Vw=zvuxF!SAy?}o~^5)B|>YhhY<Kfuy~TVZ#~NCqTfVY!>7dM2OC<)ML?hR)QC@sLu_"
    "Xo;wB36?ABkXVlP0{I^zQ1dF6NsZ{#+fn$gtEXW38~PA(0s4I$|NqARGZII19jwT3?X1pcjeo{~?JRT_"
    "0l_*+v^yE3ZCaK<#mJNgYY<HZi1H8sOT*Qr7|Q(#o`t%CKh(WxH#|(H{5^OedrV`^3H2v)FCy?9v+z4H"
    "<f7xXo}vUtAM-{%VO#n|?S@n{H;Yt@3u;Wt+6brRgsV(=!faF{!v+HHnDJ}NEdAOxJal2JT3zTX$&mGr"
    "9^#J`A@>KW<-B7S%9!7X-3yoMnzAaCjW*GvnD}#am6e(cIj0`ji$H@$IJs^|HWf)<8E+QxWXEjQ7XSeE"
    "Og+E{p+PolQRQ$nYE`hh^QAZf-VP}_;oZc6jTXKDfRAgitrhWvJezC581rtd{EVP?+Y-<*2k0BgfQHrZ"
    "yNb{Q6rjz0S8ju8Qc(aw1nrG%0Jd5yI_7?jB^&fRsLY)|+sM7hMy2SE4QtY@NxwmM3#X?hQe5dGCGxEn"
    "LjC$u^e4;QE~|bb%Tz<%k)4yxFr)8D=;C6rH420@s`-U149jJS$W$jQe#3=dFu};yTwO|G9U^hV=k;g)"
    "VRBt)r%jphLdiIn$3~*>tcJ|0cKA-P#aGWIT?GS6XD=^f>Bk>6CU^~Tu0>ZX(P)deHEl6EF;SC};p7nk"
    "IN8FuJ6bOhjoY$e%Arl#kcmAJ5>FDGJFn=(px2yO{bh&O=rIGS@k$;u-UnWJL7Xet*x^Agf3<6_d9c5X"
    "n|(Do4_)6~G?B!&usV@AWng2ub;Eqp!SG7zDDG=N7Rp7g98H~9W`V?nx}w!Kmw_Q&;{?%s9WR-7mHfjP"
    "yZcV^{SG%&H;tw1u1w07l$@R^=MuwR_OJTP!clWsTeI}(WuhX*L{ecH<w#2Gu28j%#`U=%%XNsL1+CJ?"
    "ljzBoyh(AGXxp#;*8}$VyQ%x?A0M@TUitm|GyZ%u(WQI){7E18MfLrizrNGQ-7MVaNqzsh^4$V`e3tx^"
    "uKM*m=q1K8?qlf?USbqe*gAv=qI)ttaszMjnva;?99=p=q(`h6D%-5xOPI0TsUH)WqfZZq5Fmfd=Xs{X"
    "<8+|wNA_Y>|7&gCd=>gYE}pNv{waD#7$d?zyoD297i__BRM8uV)R^+A#?kD!|1oxvD+-6<&>@uSaKuSa"
    "wGOnMJA|UB_C8<d!G0I;s^hsHm$#>c9v(@>h?PV)Q%P^F<#oyu=kK#wf#n-&wv70tTIEQYQF)}nx0AR("
    "tJ32W=B~s}LYIGN5faPzNzSm?`|X(cEn>oDD`%Zl*|UVb*Eu6(?qBdg9KM&*pQ2Za?+cGy`IofJz=FWq"
    "TRXYpX{xSSO4f&z@FEf$TSh&02!#$I&ncKK!{cP_?a_&e(U?%L_u3WC3!i2sLX-@{^)XM6L!!{zEOE5}"
    "DE2#^DB9$}#YQ@pR@Vsp9-GAX4<U=}6sCxpft$e9|09#!h(-P*o4Ki1qZ!-V8WUZnmkbaTk@MuNG2AL^"
    "Xs{mbJmZE1rw_yKh-^j!^SfF`vA~^51sJ&ik;7u#T3;?3H*-@+u`4qTTSJqyfiF;hAwB4h<8?ZkQTi*v"
    "OfYFEU&Cw?ky<D9HQP_Q><Q!aWRf!F09=uIqA77heEY3%GtCY6q%*GQ$1QGkHsX4R!U+tWeO#W60G=^I"
    "e=_f)u8+#B0145njoy5?6u)l=1UqHz_dq_00YsA*;c!CslNhLYJu%jgUd?voq078ceK@^TCa!Uv<fD4G"
    "p)OQ9^@fD<8F^W!xp%DD<-x2tof?!nNkhQ^)<YpLTeP;~qiTCb&ZBOwEC_^rxxC=mc@P0XfKwa0-K^Bn"
    "HfhovtTRgYi+V(MAF3)KQ4Pt$8S`R%j}>Aj>~Axnu*u5767&wTubEZTPn#QIb@7UDr5Z;~fN=`eXze?w"
    "N47*$=R<w#aH8awq0Lzah{d5Dl~G-oI%Mgz$&TrQ2N>M(+dHeNI$RtcnArF3%ao8kE`l}t4+9~)E0Q5i"
    "e&$09!DM++obLCs_xWkg0*aG3sXrayJp1yvJu9O-fC`;FIDtziWSXOtHI0(YB}bVh2$$X|py?R)zUcz!"
    "t1_HrRY(MRP-xrL#@R5eB1HAG*)w$t4%U;y1NV6d;dy<lt2SJBkhbO7pA<_L2mo}eXu|5cOcXI2D|`}y"
    "EvxU-CD7+U-<!N;RgyeANfP!$7*HOzO{ok(SX^wHA$<3+pIB6-IX~e5VGFY6(-!XoXJ(rggw|u;H$t_p"
    "R~1v<UBg-CKb{Kq-4hQ#*j&<Wu@mZTr|~L$DNNhZeaVQ$blD7iT@x{PU*`wazE|?SKe+;OmU%G39lNf*"
    ";xu>)?P4ZR`tu!e!w~1RSt&As7Xe;d(b9Dk(7k$-oplQp@D<hrMkZO?mgHbiz*2%fP}O<6XS%<vzwK|v"
    "_s4sDzaL^>cNLhz=lk94++Dy=`S~gN^ZV<)f5)$%ucj2s>+|zHUmwDXeYWc(OMLaazxkIS%lqU1)!@7&"
    "S*9(?GEK7wMh;|Eha!jT%k15mk#Z;*)rVSmsqPjO&tanL^1kyA0mj66eh=qj#M%1}6K>-XD|26s#rEYO"
    "9n*mcu0d90ND4nKgi~^e$_7-{_+9iiH(Jv_n;AWSRU7Nv;iejgL36Y(DG+z3g@KCHehO^?+sTH|;dA%P"
    "YiBmID^{3Ms!|yNjqxv}#R;Dk2!(Gs9P>wu{e=w!B7fs?Xg58!l@Ct`y9BooBM#v^Qt?Tn*sD)OiL_7M"
    "D@9C9l*<HPWbz75b+e8hf(q?oRZh@#0CH=9eQ^@#Hr2!~_JcE{#_*()-Ip||$#_f$Vjt8dBX6d`g?ik5"
    "NRX+z!I}%L>`>dDIvYb$q*~P(4$LZzgI3F<y{yd;rhMwBcAZxr$@z=P*%+*DAK^#>C)<MIf=VZMg6Y`x"
    "4#054rBd|ui6p*`HgCdIIl0MiZ{!61hqg%vj&lj3lL*S&{;yT<&1iz<V6I4)G-rZdHFFGpo%ZIBNCp*W"
    "{y}*4GiaQqX_^X|LE}R~u$kRB<aN`Ds~Dm!CY)}?Nii#eoHlqC_XU6${6Htk*ZH*iT{hVKmtAGr6o3_I"
    "Mji~NJljN&(Mo-zfbVqmmF_p#*}6t~jy7%bM8H5zRaIkW=2BL|u{3xOV#s8d4`}ECC}>(D1N;eG7E}k<"
    "uNln*#aj^`q3$rgg1MpcqK$r=8ZQuX%WP`c^O4EhMYZ_komT{)bad;Q&88Zd*ONV*QM)M0kX?!v!pmP!"
    "<4gI^^4mV#GHY=Pg8N~+CvT%(R28aQ|Nb_B={Xgr?i=J{|5+!izzCW?|FI1;^5t#Ckw&}QR5jk8cOiWz"
    "6u{-OuCrQRHS0F@Tz{BMeagi^ifA5_!&ch|zte1~j%;r<19`fv0$0totz*@SqqMi3ST#N7(BzQSE#bp<"
    "XmqLEHbp*36t@o<C-^MV>a5W--y34Ewa(>jjG0X+&^<UxJ{Ujwd7Okg+q61@aH(ba+Wl&w)W(zKeP54E"
    "DdaRI6!e1jwd!YRe7vjA&NQ&j2=T50H8lR;eYmoNLJgF5mSqz0TT!!OUu$_shZda57$U&TYl;~gt}nN&"
    "E2gkaos!X}=FF?#APy%u8S`qZ&&Gxq2phipXg)dBQnV(nFGTCCs>DplCVoL~cKy;AUD%mby_YTLH?TL$"
    "b^z)|CH90WC`o9xJjnnzO_7#VEVlh!C^_Mx>zW=5VniS+Aow_J^|uDR;>^y$V=t7cTNJWHkJ;ZjO?~lw"
    "puuE=0>VNUtIu}NCrDVGh+pr$`TAAuXbb%ckC}<uW#R-iL8wpWVvtrWttP0XBPSK?&Nwagwt9~L1eWOA"
    "DeF)JOjXLTAF4<E_j9LJFRamP1#(iyU;B&S?<;3~#_#L13*Os4?}Pk3-5u0dy1qW&+fVpzt>=(GzSH-8"
    "yQGh=@$*%`O8lws-{ZHxIOe};Q(lrl)0zZ|&!632H^E=exqb>dF|Vevq%|b;wY0*UBa>f&KO2rBbi!2p"
    "dm@1L`@wW%LAGbLr>b~9dJgq-@NO^}&LQJUKj9!jBr`Gd>{2`7QyykygA@e9A#se*%UG_Xl#J^e<ZGCG"
    "iV*WDXpzAp(|70!@Ny2T3FpWmMB&NL6TBVP4dfem04x7Q=bRY-MuU{0q?2JeHI5;jbo7cAXFQ8<S2amI"
    "Y-1QAQ-tW@rg|q`hd)+F{)6VbKaz6!M;^)W&OG+QH8_Iglx80#gU*s6rHEbI4~b(tfRzcslqNET!#N$2"
    "H60YLDS3hoQvoWs>$p9b5UPYqtb0#qztzi!DVVa^6%vJ_F^ebf{)0tJx)^;3RZ<8j4yOjomX#LFQ_Mtf"
    "NR4ysvR0pi&eZ2W>_7M}g{J3$Kf6wZ?uMYae+b$^tfTt3ZkL0id@ubUV{b(6uND(U!aK2t3FrC0-K&)S"
    "-!oC<ujM5ujqU`Mj)I8g!&nDjW)ck?5Yhnav7qU&qczrn9MQqy@)pkADZ>RU`VH&)Kr?XKHS}^KV5qc~"
    "{m&6O*YXX6i&x;30NF14V4Vpbr3~4&Q^7@x%kCz~1?54eGIL9bbXJTekOfVc+il%(j_+PQDVGJ**@kyH"
    "a;eDzb8yqP>Q1wBGCP5@ay_ZeAJqsTH$#GftP85*Ls}t*#ZODz-w(1x7jG&RB6v_;&jBR_R<f98%6eN_"
    "+fnfxAiW8Sm*uHVhgS$j|7j4lG#`YU4ZcFvJ+d3qDYEh`MrmxtuExZV;WQ$xdMd#x_u=ZWCbqQ;{CH+C"
    ">5FUAC!$w1CU$}trR8{<wp-ojhN#+Pda<e(tD!L|&D$cspum|tPPpj~l*COjpn8VA7Zf*Scy(?D0RK^+"
    "VAl1$JdDYg%`;jMg(8!{q3D2UkI2^gm3@;c>fr5VvMuI8Cbh@>%Pvro08|*GPOcH6V`~5l<zw2}UeP$_"
    "hobGYNyS>D@(n)r7KktfZ(>m5I@A-~OAulzz(K4oqTb6ilV`-tS%pCimsMfIE5W)vE+f&mu{vzk;0UCb"
    "f?zg8AWj_HmLw+oAyaIm`a1uGi+C3(>pQD6t&?7kVHn_J&lY^!_Jes{k0;56X7p18FH!ScxQx8YmGux|"
    "&z2blI3if<nZbAD(cEUN&^n<RP1v5)DwslknLg$gOiv@umbI820W1q-Q#L<#jbSj?&z+54is?hVozBL1"
    "7)Nxisqw6a3Gr<jTYKrn`bT#|Zk%6XzruoXREgV#NgGzffCWvIqE!uIgefg5cb1b889!k-C8H`{%iWc<"
    "V2%lJ2@F2176&GlhH@eS!dv6~0&H#~LwX?1R?=EsKbp{31Fd|J|Bw9C`1AgLx3cA{zh8Gx{}rzH_p8MB"
    "kA9`^&!6}4bvGQJAKzc^_lMVd`nvAY;_I%r%GbCr_utJ&IlDyePwiLp@e-h#)&NyB2@GU<EfWz9v;4J4"
    "Vk?@TJHNs~eNZXs=+t^pNzXVp#xY)K9uK<kHC2o?9w+^dZ{x$}z-F3tSiMwJM01$MwFZKxTuZb+`T9q^"
    "6;HLBy0Gq0N#+Ju4>K*}B)qv_m;_96vN<~Jgbz~JubVSMa;qjb9zJA5QE#?1=|OY~F->h!^=7=h(~Mg@"
    "wjK<@lUtA3)EqjG`<Z69!0_#-#^cn3c0o>_>9dlnr|U$DXVd@%2wgwcoMY$FW;}xfDud<v@!S(azE?Tc"
    "%R~pas~x*rbf@?QRiC1RK;Qg&u_DjWWJChsO1??Ej$$wi&}HG9(r0hL4*6)(5Au}9)_wo_G6P)>Uw75x"
    "n|W*NQq~4P^saxgV>hOUlDW3oc!dA$!U$CEUO|LKU*cTkAm2YbhsP?Sp(AMCHV~A&Qs3N|(12hUek=d#"
    "?Z&{pUYpa={RsAIKjPl62uGmaBEFTaPtr-{Mu!jL?Ioi!I+%eg$pIjieucUHT&89BLotmRE9j??rqWUL"
    "fVah{t)hbPTC3ISv>7oMCYy10*KjzRfOP@X4_4i&EZClZtoCIwcJu@ZKDvem$MRBLWt)EK4H`bXXLOIo"
    "!VSdV(xwH%kRxL~p1jyq**GFTTxqh!B$fM4z&KEF8rzkl4Q8)<>^Wi+^24Y(9Exc;5Kwii78gw;)=opJ"
    "K+>u&^daBDUTPY;%(GQ~sDq48_b?~7i^fY8M_yDRY6gcnv?|?zwOSW4ExXrRr)ydzrKY+F3EWfy%Ra&k"
    "d_|yIzl8eft^K3J)#o(aNrm-})nS2Xbe1RdjMB|8jBtGym#2zK<fwf|B#j&BmiIhkZf5F+=zJ93p?06u"
    "`b9aa`%L~?eFjX$nWQ`W6$+7rWD0}TKg7N%MNz+IK9@LSm7)=k*C^I;tzVXYwxKn3$~r@Kx^9~}8o68>"
    "hDv3rQd`kThWM1&_^-_@#FdU)9H}LXH2Tc}+><!rp{MZ%p(h76T1F1QvfIzq|FCIS<ZvwJHH~bSbRhbp"
    "*lGVTUL&Uciy$hT$wi<~(1(_F1C0AUGGJRe@M+DqQkNbK^pliPAp?zCKHMk)Y&Wt36C~HZO;5p613<8A"
    "7GJUOQ|57-RKpDLnuZC-C*}=7)s<gKQT&X!G5x>L=yR{{oUe|>gltLcSR;@p6>WmEZ*=neqE8?c^==a&"
    "#N;#w3eZ5czQS9SA1LsJ#*b<)hXb>iMQ~?F%Kovhos62RrrpCdV`yOQEBdhIfHg3(PY{moQO+5+n_P=d"
    "2pn5RJ!TSTQLx~~4pxBRRYb*OqjP9omPs<ohAQh!kb*Cp&Wn2~?n&g90s17YW*d=QTsYz2vM+~FH%=?N"
    "v;=!Y@Lg0jGwjlBTWxvG1e?UhCGsR~nt*hPym2sNnOj<A1{A8FI$E^COeiVzuf|F2R2<abr;3H~J?{4E"
    "eT?{3zwX+#eSGEm-9Gx~`{(!PSG~{N&yV-;{w~kq&v*X%x*u)#Y4CNQ=pT!kto}=<6n}S0FX^~xPsb%M"
    "Kn?J;N0Lr*%-VvJBZ7l5;>p4AuhnO69A7C=FKQ!xsAgL-O)|j`)E4t-XGY#Oj}x!swb(pJt)i>*2z!J>"
    "Johuy_K_eEIc#%Gi|A<|VXJG>OhRQ&8Gb$=i|CG;L&HMtmD|xwQNfX;BxbUD6t#Kj^JWP%kfd><M|oNU"
    "jE=^NXUui(l{nUsCbO)tp7Q97xG!igicu~Jf0z#HLb_WX|ALF$w{;4K5M4HYBnv;R_jWYxX`>Knm-<uB"
    "Z&CZPTOa^b=YG-`7Lf+Gavghd=B|lZZPcQKb^PILZo1^N>IV&PYny7=^B3I_FOqzL>cKg&<$&V~=7A<{"
    "=1ZTd)6<$plDkB?ThZ(~I^^GC)s$_*nEcY$kTpPz<$uSD#W=xD@&rnRquQQIGF&SQ6EkB>n159<0>H+&"
    ")q!O6RR<+Y6@HM&)B)Qx^iN$K!>YnXFu=2!@s^~UTxByASPXW=EMbr5Nq^!fA%q5tQ6Jr4jOLi!EeSnn"
    "ZK>fdbH<Pu5n`HvZ@<E-G@Ug%gXWrMRWs7Yz}eRDD{u5Hdi(IKw8W(kQ?oR2$GpXLOsfH-S}ajo?$1gO"
    "8)iTjMU=h`1{&B-b!BO~Z<yy^Q%Dt7Qa!IUaD6gHjKL5(2tDL)%1^i)?7|{M&T*67T)6qqY7q$(V&C{#"
    "xUU5Szz?Kvnle`iz?E#<)ddtCEJ3_Lmce;Al3@^sy;wJ_(IJD&4Orw73<|MQ3m9!w*jg!hvYBz1ZW}Q}"
    "gOHN8RPJGk^S6<C<As>A8ItolIHD^0g0(ac5D1VTYA<d%suD@fSmV5E%b|~CPv1tCQZ~W!Wl5&#akL*i"
    "=Piv^CpmSB*u`v!m^JFPSzCG+qkFH)&`+ZQUvvzQfjgL#qbEq&SQ^tAf=?BB6Rg*Q9_aoG@><YKn;~R0"
    "=N<a4i3G6VM}F;>EnoN7Oe#iVQ=c^nOGHIvk_>Cz!b&Xavr}{OC-s3n#4lRDaW%@!=;TsCu2XEJlX?(i"
    ")(VGZ%xVOLoqUuLmlJ;8nj5}toT@p05HqTVr&SEMM&W+acBSqB=r(&hJ#Au~F)<-wr(zG8*6%?zI|@6!"
    "TX^AP4k4X@wC9wtw$*#&p_A3~=uLDOoK2;BT<<-zU$auh>59sg!M936gJxVWVfU&Ki6I=89z_OWXj262"
    "<a%kmT_CZ$C~m5}%EfPk#H7O>U(}vCvOA+KM$@C1_v9P9Kb38{kJWpqE2B2ll9zU%1l<)<5euyaB#!%M"
    "=fAJTzpwK7_46Le_xQ>mU+wDSr?#IIztY$HeFA^f@9+9ku8)$-*T+X_-~Ebrd4AnLsFmNfc>4>s)l0%}"
    "+7f<e#*J;^q|rPMFeguj9@ZS2Y{8Xw+*)L4LLh6%7)i&;vd$fvCW#(3&F}T>@VJ~oN#zlM2^`WEu40k6"
    "Hf$n9wv&m$Gd2PJslJH+DW|T3)|C`g`C3W%6~^ZH`iS)n_)MESGa!`*2r0~p;6f+F**Ao9maDT~gQv&Y"
    "JC5VquF!#WF$R^<Bes84O&M10QD`>R^wg)^--fByItXPsi1{E&!aQ&8pC&Y%kKwRG2o8W!*u63Damsm5"
    "lvox|qFPfwWNOA&g`A$zILp+Fpzz8%QuB%7q}Az!6K3|60vnxLAYEEHvzLIiG0>#vqm(ZZA?o#$ehayp"
    "2d<eOCoYaOfhf<B&#5(Sz``j7Bu~lJ6z_5BN91{K#b#GM)S(8JRR6<9;hjZzDxntT)BQU6f8|9|r2`^+"
    "QGj+Tcw_NPQiT{xt4{sv{_5Tc|0uOMZPxuqo2!WO7GEw!EkkIwZ2Q=}8`_t!OySo)I)8M1zzfX9Y80zN"
    "Cl<wr&g4=paTg+*x93F-wNPwMbQDNOLJRBFg_$|q&FXOhF(tN`63v+wstbsqk)J@tGE-l)uBWMZ$%0Gd"
    "D={_G%js^7#`6)6$#QIsh<?0!RXR%PeMoHTX(peJ6}e>xv;<cgaZm$Xc_L^FH2kFp*Fd;nC(&fOn(mpP"
    "!>Kr1>qHr#ixncXYr-z)-qnizur~2*ytN%x>FFsv;w|k_rfh$cyUDPp^x<ImwTyoKsn{k5Y&EHY!_!xF"
    "IVvS8_PNXeWfTw&T1k6Oh+U!dos2R9&YJRc;Cqz4BtXf~s?aFay}Hz>adrG8qL`Pnl%7<d`OF}yXyoR&"
    "S%wiL<!iafge5y{+#x2q*y}Y#Wq1wiwIYutl*=>8K#!<)In(FOuEJ$V+}d2V;(+60W!ZnXLmd&vq?;`O"
    "N#%uVW7{u(^YZ0rYg4#QwkWt^CJj$*>66JO&=8$&y?BJZqqDdL>_~28YxjBmu|)|h08B@@343gcnlE43"
    "i%|}Rw&@TN%#8Nrcx!<d4Oxb$%o1uvLw8LYEvlfC(U(yt;S~g^F0#7@UK_#I8FVYcQ^^^Ag=20F^BT`E"
    "lmeMBiR-wD^9cpSS0@dn{>J+)Q-CsE;7ajhrmg^FH18=dVk^J#di}|GOziN(%t28PoSav?9#CACxPF`M"
    "YY#u{qno9&M8{8{k$Y?WOc;EK@W55VsAWZTknt^HDBEX^vNAD!gF02t{<4mP?{g-I)Ki|30~)0^b0k8t"
    "a!`u>UUpPr;81(xnM;cyKPnBO8vIl?P68#Nxd$8{bCVFlJV7Ig^gXOmDa4WT6_Xuu_aXXn9z#Vg>T;x="
    "zxRfng>y%erg|FRtgCcMCtv|wf3KQ)zt7e8YkarQtEa2Ie=6*?{(Ow`)v~M`{k^A;{&_c^pP}EKNc{Qg"
    "<?0{(BgvrhyZ`8aqndh2VoqBU^Q1((BxOa^uj5!e*|QO>AhHD@oP;R4(wX2X=S8jHDcB56s}E7dU@K%~"
    "lyD5_ZPpY#ieckvKPmroNM+7GywtET@Z_y6Ch$m+mzyV<hfFU$F=v6T_bQcOO6Q<3kNAnf!<wYyA{_G1"
    "w6LISHD$!Hq15Q7&;ml#nB~OTvGl{A^HMiWn3PWb9M3BO1g5xy36|#`4yX7K)eX^B3!f()9_VY;URe)W"
    "J#F=_{^!&PbXUvI!3s*;(*WC>UFnB3!DY95a1WsuG0SjVW-ZF6GY-F)*n(nY4fH3SM&o!ziWNDNX_3YX"
    "$^S2eD(FK5H3@2f@ZoXdcr~cTyjpF7BE?ZYF2~e%Bv#W^0>aEzw;u^znnJebN4j2c)|#px>1n_9M#0j3"
    "uv7?x#<QATW6(5p(MOQ_%=1#ghR&lK#NS`80aiYAw#Y-Gr~bNvNixria0Uee?&aVCM4cK8QLUlHY-JP9"
    "e)NPW<3UX{f0X=P!q(EVXNjKgN3WC#P$d3=4N+9vIQo`{r{Q!ZI~ylXYV8^NJ5e%A+jJLx0_W**A(f3T"
    "0>YV{AiX}OH9HMTACZOt?X>v(*~ROqTjD{VHQ}T3`6HUwGuSZvV&l%HKu~pCLDguWOYz~D6YlWw)|M_s"
    "V5O*ujY>Y&?Gd9yh2%!T-*@1XFWoD9=$6ez*AbZs0_xUDuUeJq<YwMZJEk^{&76LoM$3zcE!lO=&dI4S"
    ")=BBAkQ!baj&;nSplA(|+yrLR&ytmCdQyW+y1&EqM!*+SOec&E4{4^QKI|gd7NiyhjHk7v+Q>qUU+inI"
    "b2adr&H9FMyJ%Cyr^_E>A~J&zwl_k9Qwg3+TBb{|)rq>(Cq*T7?HUTxpWmFRNmAi`YcQT5+-TJrDFP)~"
    "&mwcpH4((cge;(SYcfW(8$|^f1|?m9{TZYKn)Cs4_4l3qM^{!ZEUhZF<^CW+Y_1RPBWtT-BOn!`H2`na"
    "`oz`ena}w$yCfZ!@3`8EBAppZe}?a?bxMz$%cBUm&*1CzK)<U*#A9F@;`)u0WYVUG;Gl9VNQ10^6P|NG"
    "yjG144p`Dngoi<=Qzj@$p4fFn*Zp{{ob-Jvj5VB4qPA0-SIr^1g@giA1(8OCd7!zdE)T@>TXejdVQ4`|"
    "kHg{zmQup%MSE4W%1XJs-0=<J=TK{bctZ7WW9O-EI&R!DPjqxJP>=J)d3Pj9qH2!f2$<jXxQt_$Go8oG"
    "aBp5SYEdXSP3(26E_K)y6pKPTp``|uQX3{10@=e~7v!mbeSLp?e~u!Bj?xiFFXJnGl<<CE&F|wU<ga{v"
    "d@JapzJLDols?A&pYQSKelhRA3-Z6nXudnD|La>pzJ)Zq$Jer3^&h9}DUgk!g)vF2xlBDv|F#fdF)VDP"
    "#8M|ugpPI#9fwm*(a#@-#K?Max!3q-FLA;k!LK2WQfG_#*@ya7x?>)&8hsb%NWK<GDRHf&=R*jtQySyE"
    "vZ#|{=8j$hv3Ol4lQK6Pr=lg49^mvN)d|CotX(+1NmV&ozBP4DbEO%Y_g<&Qrl)@j^3f-C;=tL`nRd5I"
    "JQ`qpdGc8ghVN!Nm428!bfR6HEC_y@V+;u<he}C(+FS%%1K@=vKfX@667ljIp4<#$N);jAPGKmTxOvA)"
    "89lHjow_CA?X&|JWD;wzFk1cBjQ|REWa2EE#-WW>jc(GH%!%0$znD+<6-{H(^qB}I(M*y!`KWPw50i;i"
    "z9p3x;m}$gM)Ps;H~iuvr8#haOtR84wdcR~dWv$MDg3Vim&WnB`rmYJYeTRpNo`H|g?3t?`u>IKZ5pP_"
    "=CclO;GROTbviGvOTErpd|DbP8#XSYLo-aayx8H`-OHfAuCQ}*gFA!i=HO{DWpgu4G;S~t3t@HTW4dDv"
    "4V&4?%YYRY;LlZ^11mXhx56>9&FjA3>$UTQD9HN6wLFlGdFM?F?y7bZk|$!pvo}#)OcHGsI3c3M0PDz9"
    "9uG`8SDd?E+lh+PRHqPq$%_z9EDVbpvO|I99PR15UB3cyNXV}*Bpb<?8Z_+=(5Bi3kf>I{XmiH&oe7)r"
    "Ll`L7aJ;A-z)|zn>5wdr&Cuw~Coz-L->)XTDexINQqN(o=(Ki;2z_hbDlFiED327T2J_L8)DH)*Y@yrM"
    "GhpA#_|>P^BG7oE&ySnLAu*E=JT3(c(vm_}b=J}jQ(ES?6G6qUB@jS-pM3^o2D(;flW$Y#>JgcKjbz{t"
    "{L+vuC;^sPJz?&}38X=gWa-e5q@h>F5VGJ&nnSA!<8W)4sw2dW#n4Q8dA=u2^d#p?@Cv(8#%*4t4`9gY"
    "x^_qPv?H+qg6n92;R9{faN_9lYxJ?G!ezaJayKyw=*45Av3!3?7$-D$j^?oShr57Ty~>M~uA!{=>d3X6"
    "VdKFpD>gHOj1mQFQzD^onnK)2IyDT<YXY@@@6(}-qlojrR`vv*&8QmQUBgOi11<+z17BkPb6&*GkI{oG"
    "t&2h6Qx7&8YKyF2uaWp^px#<M$Gb>gJ1L0CD6FGHcYL|`X!B593Q3Ph8x1qOqXKb_GtDcS?I6>NUcyV9"
    "T}5B^eS5&j!jK}I%C(v)Qo;0I-6G)f(wuP64_lGV^I*?#w4<ZxF7gt9CPES=3#C>SWY0!tUsFIx5il)W"
    "bQ7_|322+hO{WYZR`sP(LxaX;-!%c(UW@Pc_oz#fIo!h15}<*~)z_5CDcbSGzmC!P{`$IGmAmu!`Klj3"
    "^)r0r`1M)eb9yg7@ArW@?g}^E&zt^pf4D_uU--Na)*L?S&v*PCqv5{dKehoQ#Q$qs^RXvYUo(icJ5giU"
    "ko3wwVyMZRw&abor5@v;!<%mu`GkN-96ZWE2BQOQNkzSmG*a|+xLJy4a@4M`Kakmjo*>uEpi2jJKDxSL"
    "nIL(mF&;Xj=wNcKT!R&gDdi*12Y?=dO;#F8#uLV&HDc-@&C-|*m*9AYV_)XQw<ek1!6BJD4efQvJfVgG"
    "?)Y`wr$EPxmhXfo8}4y3O~f&6J<$ky@*vt__ktwfN&$^|Kq{T&Qk=g`>`gxml;fvu1z$`cWR{0qh+Z$e"
    ";-f5#9L&wInrmG=PP+hoFa;bQhij8CE*;`B@O&rP>#13qmYH>2?d%Q64p+mf9gL|yeC4xAhxMi?QzYi&"
    "<nq8co>>l6KXZlkICUL3l+xUWYQ?PjqyA@5#a*30z06_L8dZl-ho@J1(fc4s9~hS7lj8L2Z<^j3pEm0I"
    "!`KbB=}9W6o$#!{_DG0beGjX3OB*2dX~0kM%tD%mF?9dYxF+l}Fa>6zF(d2Q5S-X3m#~DpYeYgUPqjhx"
    "c#b+ec^VH~^FEdL$OAoqWQN8FhX)%^g3EtG<JO2>LB%5P5A*XN2q0izj_8N-8e^v<$omo<JcHF}hd;&`"
    "P>#zt3mQJ^j|>JfeFkFU*duJ<E+yMm9Uw}VC%t=291<WS(MsY=T*`yswos7`Q>U?rEYVRF+<Cum#F%D*"
    "gTm4Xwp48#*GE7Q!1{LY|AJ@th!duwA8RW~-78Jv_$J84I7=xUl=lefbZi`R<{HCm=rWmE>QjOmg&+Yc"
    "P1%yY>tsR4uBOR6c=Te7oXWw;68?4YA=^rM=8j&WKb^w?7>}BWbr+;@rkHFBc>u#+`ZT`-k__upw%E+g"
    "#TRf$sPVe1l}<UA@@CRjD`<WBeSNAciBAjaBU;<F$P`nt9!z^%nQlZ&F-Z%PV;EZHUz?>C^uMZ6YsIQ<"
    "Db#XO?|2ZjSjP<Ud7CvaXSx<uB)O_fVe0m~6Jhxn%vSXJD0s_kpBC-$I)Fwhilsj5wvJS_cEgyCEG1Ri"
    "Ixwj8NMY3fm14%81}lUqgzfGGKLT^q;S|Ds^I_3#v2a|o!iD4z=zDlYI_CWFVcTLtJUo{9ejLbE!5Sw("
    "qwt~v32y~ht;XA9T{<|X)8oWO24H#0fO?n-IV&aL(Nmq>j`VQ%Lri<%ieY&jls@1k&Am99f1v@2XvdiX"
    "rfcew*4%no{)TcqSfM&0QfyPN*wxqo^a|r8uk`ZC(O8sT_GIapq{(}%%B;@wgBT$M6*Db`ZwJqJlxd8!"
    "{r9*b1}Ir#DXLbH?HCu-z-v`VXI^+Q4gD4_63xByeD91ddA>+^diOAYtpQ5ud&uHlzk7cFu0MU;_5S#5"
    "KOeFQr@O=Z%HN~CUq2Es^}ArGBmUfP>8pRXG5#t0UC^JZ{@>WvtE7GBkoSb`ZV%l9&mw@{amw0le0eyp"
    "owtI3ryUHz9Pcg9JVeWP4v`93VzJ@uWa|FdPP20Be+JvCVsP~1uoQ7b)#dwrx|`!Ey-!brYDwFhqtMc!"
    "4osIJTazdyL0XFAC`qsO2(aWHX$J3&1AHoWZ)+%6%a|k$a*EEJDju87mE#O5I%JxcNiUaENjV82#bfPX"
    "C-zfu>VMD|@sxHE)Yw~JXD5?52JNsJA<3tCRjf(A=H_eE*B`<mQsVwxC}_eOk0e}&F9qu%)fwr^IJ`*E"
    "XR7{<8^n2gKQj8Eu4ejISR6JZ>9zGd`9!b?O6`;h$dqxRju6k)zf|Fp27m;?xo|?Q!p(^mO=!6WQlnk}"
    "TKtm%t*w5#aI>7UUbJ4Ba_$Rw)c|wyUtta||NWmk2njX6#{Tmk7Og)@4%hwNSf$?=AnaD*UGIO?_mmGA"
    "5@DJO;{MZFI2fM<xOMG!?iUv6In+L7laiKQha)CTeI+C3{&DNhK^lx+rnOmGiQrx=LUvg8{<t*dEfK&E"
    "6G&HI9eqrMzPld%z`CmkDrRYF)csobQe7mi%(0+xgY-yLCjlE<r?}~o>Ff_gmF#`)fvGm=9L7Wi=eG@x"
    "2skHVwoEg44?y!TkN3iy6V&3q%?7J;42eFSl4G+r_Tqg<>c_{K`pxH=pb1u$8h~cv`b^hB$8D0FXo6@i"
    "qARZal{G#6nlV{{(Q|bOxRA@i(Ke{^fBOlP=Mcw?C&VJ%$;5&Tuivzq0tU)3ur4Oh1_q3R1F76<d!TQA"
    "?wb*@Fj<kBf>%i6xY!8#a~zh-OqABx6_HFJ0(~Xh1xTFkLv!OblLgT1?IYb%NdrrTs0uWYoQHrjdXwWJ"
    "oO&)jqSIYJt(7hcI0oaaa7jj@pu8OHY}Vk)1n$NhQ&>NFU#P9IDwY)&n)KL>1P3zJj-0owD3kZxX=jYY"
    "R?A!~MRsDHDInvi<no;%^*$P|B>0-C<g_20*1(`pwB$tr!%W6-z8M4aAgM2qzR6Xy2pW^tN={J6`;o^S"
    "!0Ca7NWGXIywnpZg8Rz4WTJ!5okmJYt=ncN6Y+hcrB*6zvn_&E97>Kw1A*rw+PH2u)cqT($xq@Jm{(j@"
    "t~$=2PE%)?+-N?s5|#y_T9=MInT*n=KRIzK0UJ+@VX}(x6t<g$j7k#(M+bQt+7#$F_ZMRUgp{Y(wS*bj"
    "1gF6OAbrrAh$KBT;b;evVHx*p&+H2?<<#~ScFUz$x@l5|R0zq1<XFE)kArk~N;@ul*dH(U6~UTXXlMfi"
    ">R`iQcP#X?_xMx#k!|Z$B+H=DUt5pJiU!-em~Q;0t_@1iI6bZcM<Ni|q78i|_Zz!r>wz*k3fV8E;9skq"
    "e(tYJxpwXS{>QtQ`24BkKFjZt{{8-4Kk4JjU!VCiw6AjCTJih4y!Y$pE4|-W+<guG-Z;=z{Kv+jjqrbU"
    "YdyB;Zua2u>4~-BC!b1oOrJS=ZZPL!hid$dWhcz0NU>$b;Gt+1;J~Dj#x6Ad3#g`~sbK>|o~E_>Fx3BJ"
    "1*2~CZt!HiE+~Q!)Yb94v0s0lzGldIVQO>JSxEGlXl8C)Hh?<W#sTLU?K{qY^5_Gg#v=#GX|DLWuWRnn"
    "N;ySg+!tcSPocr3M2oSWr0D1ZEi{!tk7sXjM8#{dF6Ojh4Noy)?8ogADn;E>1BaP9w062Ch+ZFMO1!LS"
    "PsiSa^wo*Ujn-|aLj*_wkC(%6NVhp?ciA`&e^jCXCoxbuv_MgGG?Z(YqLhJ($X)Gt?f;^AYBQ*Yg}XO!"
    "{cvH1fCT?}fM-YKmScjtpa7t;Y9bI<lZ_+7R!vX$?&^}`E3yOW<NAv%xnIJgxCoERgtbQZ7jbPtBC7|Q"
    "4YvtPz}Z`NLjzP*x5L^2s3KwW>>M#VfaoX|myW-e3Dtwxj?>MCWb)0MlSx-)aW)6W!OjnfQ#8$H1I@f*"
    "q|KH<S);Nw%$&1gQsVvM+e@&oQ0~+<DDX_}OHVFgKn$`jP6G8m7Cj$v()Wkt_e%k{thBWf8>;_dEnG92"
    "oIQu-BFjDEahIT~+TABF1-ip#dD!0tVBNGviT{x?QH_=fTB^0hNDo_HY-}@BAYfRnGe1Tj%$w~#VG$6!"
    "{GVmf-Gde%Tey~@>(({uvohW$j>pvyiyI~|9hA&VuyUMj&hUak|2tVr68FH{1`5jcUU2NER4{Op$nV_S"
    "9VD@XsQ8%(KkNxnN!Xmrx$e0L@+R}NvuXg8fpW@GVZ5FD%#K^BNeobd+8?Y@N6u)b6rA);VviaY<(=NO"
    "1V;~JM}uoZhTvQ0nV46QQa&JY!VvOsnhLM28=7hkQwAQ^b$|9bDhF=yL=NtCnieS0&mz_T9<8&k>UOF>"
    "^72Tb{;zq)TzdfjXJiw>Gc6}E4-n>AXso;miI8qsZjdCf64~|HWJqgSM<B^a^^bB&{{FbN#dt<00#l}K"
    "W4{zXYj*P{dcV9wbAyd9`hG&N0+QiRRdh^ay)!fpA~J*#tu9%*64S;BN6ssNB(b8li@0b<7?2$48l=<A"
    "&=__(9=kwX(YCuZ9llzPG(dP|ofK-;F*UbSXHvY#bABeO$hG<xcqYxIt@;b8h;l)Xp}8d46-(_e^P*?0"
    "oMl<xb#_{{-=6BIe4Q2#q8|ri71Sl%N2l&KeQGN_&a$@4`I*lV?E|l&sS=ov#|l8wiXPoZ(lVDlW2>_&"
    "Awuh=#L<)W4X&2vJw@UwNz-&qRhdg;WMK36i-)^IzTeJ!{`o9-Z}-)k087_Lxjw({s`kDn+WlDnzWQCr"
    "^;+7;$5*;b$t*fv`Ds`Cr}}qY{~wEo`y$=tMmcU?hdJYVkYq!bIS&3&S8fIQ7m7AgKT<grdKn9x@gfXb"
    "({;))5Chy81CN$d&FA9Zaeit&aj_s0JSb%fm-52`B?dF&1p1W49AzJO2<oLnRB>!Z)p(OTS=Id*%=KU^"
    "JmVs2dCGqd#Gw14<RW*-^q445R=0<^X)f#gZdM+gvFYuQI&lA+`<YHst>_P+EaRyLv|XIraH@`Ad4yNB"
    "3VYZ(gE4s+X!15r`mK=vq_o0GQqX)lS)|d8cGpZD-UWu3!^?E;7JC__xlAn&H8nzI&m}CD$nsP6gElJ2"
    "2v$Ij!|ZCR98x=cLF~AJH+s&*Q>3S}0hx^@I`0d^14@N<TDr{OtgO;2Aw_PX9_>0pi-KFnZmC8$ACa+@"
    "gOWHheJ`=V`AOk_14)A&cx;mOI0i!F(V%aPW$|X>>U7hq;AI_ywUFuR`jlXtl-)F`it1nh^k`>hv_?<b"
    "l{RL0viH+Ej$zB~4~A?T&0|m!_d1cM(+L}?1$OO>D)6T<R-&GfOzf3>AbCFUdm*FELT4kODR+FPoRU%X"
    "SaY0}78mufDl<BWP$K(z<~Xo#Zr9-Ong{V5!6;Y_w4}}H*G?Q5=5<d09#=VH_z<imiEAv{{b1nPWmhoV"
    "bm1YrX(3g1rO&CZK^A$9XUr~ya&juw=jJ^T0O>c46xEN)Z@Vjz+~nn_3o`Q{q>Egi+U#qa<XH#tt}##i"
    "PH@xNH&b|XP_opa-C5&Hjcd>XN;Xn?@8eEA#XykdZ+O#~=<Fn0E2L?=Ws}tWj55=2@!`?9K^v~w3F6Jc"
    "v`+m*aS~T1Z_>3M#ogl#r9z&v`k(O})g$QrU3^o2IiM}kmO^x6+RfAKzNG4of$biky7D#+I<u-QGc$E%"
    "<}xbd^7O{lYksl;LZoxs3h(>X4kEVd3?QBCjmSt%%Y_i)HhAZhK#|fge!l&&EDT*}+ti(6!zQ{Rufbb#"
    "3eBIwyKSlL=&Go3+ckw@pzLCkych=Qa&+AfEj8uB58>%>$;+LI?HiT+`piuccZPG4v>0RG#Ll~Oa-)5}"
    "`g&_*M+HVZp2;h-W4FB#%e<mWh)L-tK6tPt!~7d7k!14LmKdkCQ<inq3(<mczN@4{gNe;;&0MkAztL)F"
    "I6KGg=r9e^XUG~}dTd9Zy=hwEA(;-i+GoeM#&xp@o!mj*O7g}MX;L(Zwy=c#U3=@<%*aCG%BXs-HG;UD"
    "mq+Ki2rFPZyU89EM6bGe(%Y+Gf{``a{onqz=;x>B{;oUoyVj5T_0jGxbSOS1e*MJOzVFKW=OcfPpP!#A"
    ")zAC6-`=m!yIcGD%=P{Am*|JG`oDa}Exc%c(ra8=EPv!aeyW`^x`5G5E(Qfzn>_tPoz;z<1s2N4{6utT"
    "_G8q-KsB32564k#aSZc(=C*N6IMc+46z%Q_l$|UGs!igTK|+Rmax@y>kM3*cDl>%A6OPH*zt`RbfnRgg"
    "c^`2{)zA1NUhQ_*7mpwgM&mShxeQz2AhgrRSb>5>3vL6rtfM%I`y{e*u+i9^aXeOm`ZUeArl``JANBNA"
    "^DZt&*9Xf+Q!1w_9XlC(dn&a;D9zE_(Vip$sBRK;p91ItA7-|i^zv;jF+n~p5}Jzd_6&h<x`t9a+0fB9"
    ">4f9}Yj+c@#^#*c{9Gnz9_pi~_k-$(7AKSaD@3a`9OGYWZ?29S5sItRuSfW3x&G1ps58=k5km<7k)1aE"
    "zG0XB{9%#CIeg#Z)21K?Gw~z8?cry2GDYnhh+Br)^(UwKC9-Xr56bi+tdNU0(4#yS{s2gSKlBYAEzWBu"
    "LG8ugoMxyS2+c=bRtZdN=4%L6EaeS+D*mIF6_KCOmsfbdCYB7iuT`q)oZ2FD)s<D}@>Y5~|IVp=TUBhs"
    "!!TxGkX{U5GLqnmX>)$-5JXs@+miuco^+>`wh3W)SWDMHx6Bj+P2%Od>${s%Pc{dP;k3YM*z!MGJna)U"
    "Q=rD`T8_|x>VuJ26=HL=25A{!2Uf1?lY_8uPn^M+w9~X$@in84`XrO5rIR=pbazzuK6_CVgNHt}ZTE{E"
    "lYb$mX&Yl})cTySczFiXCkZa*aI-NHhQCi99OGnLy_x-~j+UWN87?7zM{jka#%vjVc8s#B1Tgmw>)N6("
    "D8h9}+mS{blSDXnZ7)-2p2MB)iDwIj>q*+sPnU@L_wvIgwr3e5%n|;3!lk8gZtD&p5nx?RSz{zBZw+)W"
    "*>oNIwi)CD*#(uf2Sr?UqbVQl*~h1}`u;3t)98qfM3+so?Zxs9!ztpn<5HxUkXVsaTNN8JzXwZ#q=|U+"
    "72=frbCAx+Q<a#squwwjgra08;M~`|Cx0|i-PycPs7ObX5?14aiv4Vj6+bkf6)GxaiB?}O@1zmsr2oL~"
    "V+3wrv>8fhU)NTzY1WRm%GyBCgsi(}4!5XCYs-VshDO15iZ^(Vn!oroh+|tp(?QwWOe4sQkK;j#UGRx("
    "7p<!Ou4NQGnk~P2G+$$&QWWJ)R^9LSUbx0VacKH_;qjHns&oJ9x>L2XC3uWyhJ_#^AQ7WMCg>>hQqr&s"
    "8n%e)TO??1hR1o{pTl-q%8;Sa0&PcUD!@_e6|Gd2Wqnd;wo|xik)4Bvy4$-n@86;};;xGJsgjGUi=bW7"
    "ZUmimiQV}z8|>7&P0~f`pM3+wA3EKr#ng(P*D(LB`-dq8zGS&79P0<UH||>dAeaz~eZkZ<r>TnTx<DVZ"
    "VG=Ma|GmBW{-g2pbG-k2zu)EL_-x-IHuSsm8sB%(^x5iney`st{>1#<K7Kyx_`E(YdZPQ^|4xW@JM$mG"
    "XZ<QKVxv7G8oQ3BMAvu*9A4MSn4qHq-KL2VoB{b%j9$!vlDkif=lV(6eOHx;3U!#N<IYz+73%~DmTOXr"
    "<gk!1?6v2Cq}NS2ec0oE=y^&uQ4#HC#ZnayV|+$Ok7RUS^`?;Mp(E>bJmqe_?rZn{_AFp>NDs^%=G!6k"
    "W5$(bKGAv0&VWCNqF_$JP}PW<^w>k1fO-ic2Lm19Ko`K;B_0|SneQ@q6&ReJY{k(|!*ruxOn25Tq4O#o"
    "^+r0&hgD7r;o8ih|LhwK4N8ujV3?oAp*z8Ro&$>sXd`67^n-`s{uG68<uxKL2?Sjqvde=goiXF48}vL<"
    "KDKyXIH(*FFG*~Z!0Fu&_7+dm$tKDY_9ia6dL5e{RiRpWJ_u?HI;xK;gi%Y?{=|r3d(~s@XmR;9D+iGB"
    "hR(D&8+|yd{IRBJh3xzq$G9V)i>R)V$gLI;4D4d?mFXTT*l^hsdr-aK^9~9a*2h4~P${5^(}oV@V2bV&"
    "2xLz4zI^~oRrM`a{sy;E8d5dHQ}Z*@S)=_hc|yp4SB&JZbx+{?j4L7o7Q|m#h#x|QM-@R<50Pn#Y54x@"
    "h@E0>;l+qZ`K=69mES6cu+?Ri-z!}bn=GU0fL{WMQxaE+rxu%`zJ>>=T*U#|9m*xQ0;Y!e)J^~P^J*8V"
    "FNVF}WsX9g1<b|$UbYE0T!4z)lCoD{^pHE6OCv7|i-J6pA**+k4<8Q5@%16+ReGeSH`O;9v}px*Y<tj9"
    "pso7*1iJ}(ZUjvwdAm4CQ3Z9Um*_cc)i?7uT2J*mZQA8#G?NE!zpHPE{|-}~PM1feP;_>z_e-k)P=uAC"
    "-I`vBo-Wd(sV;mL$Rt{?Oxt3N4*o1@<Ak|{j%wg#bY$*$t-jIuBu7#>9x_c`8Y+^!=*K9Bu!9&8?ucMm"
    "PfTJE4gCJ&eEd9VM1pCK{k}XE)%k@+Z!N`|9%Ne16*y*zzmx5WHsM-JwYB`V&VNj>r*v?6R)16JzmlHV"
    "jK$1{<r-Y&H#K>Oja(dn_WK;y{oJDx2B83?2@Hq|mR7u!uHU-Cp45F3KcO)bm{v_QB}-*=uc!PAUZ|w>"
    "Pdv+89#1)y&SdVI9M_#gb}3;>t?$;$b0(qzSHT(T%sOjtDg0HvX5@fP7k?_NTrkN5QxNO0G|hpkYRoQI"
    "k~U#H+HR@hw7(w;;%nll68TpWYGZ@)hQ*9di!26NJ)U;-Jf6-Ly~D8-RarfppVFEEM71pq?N8SssMcs3"
    "l?GrDjl`$Up{BJhy6z?^a?~GJ+Q{G5-uDS~U(h*xkDu#1{#@nj^Zl;6KTG}j9I^l0H$*PE{<M$#^N640"
    "`)*%8zQ68c<E}$$O8?Z}uB!j{x?$w}qVy>Tr4O7a-49%3<D@~xSk}WIc`U(R<$!WzS3#F5p16u0#P2U^"
    "5<QWwiK2Keat?)9?1q&ZQKFOMP}TvsANbcNmv5bC{6e$ZjjGtG{%;8bk@^|SK$>&(%g6Vr><)dx)s4GC"
    "4AuIHSCrZ$3eEK(0O=S{p<6z`G?i1WHpTIWqI<j<Z>dSfg^TR`DKg1~+7n?%xl>I?i4o=ugo6%d(-{;`"
    "5dGk&ODjDK>L`scPNnaxp6HPy=w=y~j^B57v<rD?`iERk*$TxR*Yb}#S6J?GDyF43Q?3ZwsTO$9wNojt"
    ")4CzgWVx?LX<fIk|5V+{k?r^AuctcSS37l~6pQGkGKeZ7K@S!3yoL&+*{Y`*#n-`N@XSDG1~jA|;L=Rt"
    "`rm+|BuD=nt!91`|Iz%~)iTqlmP~4ha2o@ZdQQx>U<GR5=B`qYPF<qhQ|nZa&@Be7QhD$c$rHJRDY)(="
    "PoAS(E@d(#^F;j8F3N1YgD~DuuoZjQ1ahAY`v<d;Eg4<6ff_WjIEAn9o}GCgQ9rAGQ4~(9?YY4mCIvEW"
    "28@4K+gtjmsG9e4!RBU7gJ&#m+<5<zw}we8b@Y$9lnIbKN5qULTslr!6|e^h49!roIkq5%$wB<BtEg~U"
    "gC#)L7i!!lb5(RY<PK9M-+<?L9TOHLu)~0^q0!s#Pv=6x7aaNpg8X5wi_eC-J%S?*uuSsV#w-ahgJPe6"
    "hgL>oOS!GtOt;X30!qq#`YQp9Dqmf@Hf@grSS_yCTo{8|M<kEeb@x6#x+9|X=WTt(<dFa5SB5y91$%0y"
    "9G<#7q*_f9%}72Ns((g$nUy>Px*!%CV2bH_cpsnHZ<m*PTm73KZK}7ydpO;j2e!>li@K-rE*Wh<xOD`P"
    "&NJztuKB$)Gdj)|DKtOvxRHB&W($R}mfN~aRc$Bc{5?;BZA5lN>{r;s1jx+7y@f|wc8xl<16KHq73YZ{"
    "2!&iSMn_m5*X%O^Gp;=FAlVe*Y2%MEj$126U_07h@W@!80)0k#=r&E}p~%;lsQEIH*?lj!y+LpSkv;7&"
    "F14ou>690l1C|l(_p{GUsi`1lHcyw<bZecxN!NR&#foaErKf|EoOyUHkNCSdQZQ&CaGY_sSUwJc;Bzgi"
    "neJ<1Un%-cSdv+vh&BOtoGQMT+pH&v!F7&6;{7vkO5R4)`ciJIn#YYtBC<x94aInG>;U!LSif~awIZgg"
    "p>io{DVf=KwM+OYZTRn>^VhM$pYPYld;I*mOU;k(`*Hp8RlYvnNBT<j<0Jlj)UWz+w;A#K>al$$1v{6I"
    "ulMVIS@(hb{YzQzQu@EtJ$<~Wd$wF*9;@IlRW~919;Yy&#@@E|XNVrr@Z~Tgmg9g7NO_m(+iN}yKJ^r~"
    "NL~+0<;9)nvkXkELd10bb_l~I8O)5d=tTK{DYujVt-40f8m@lOzvGSNxO4}u;L30g%OXi$DwIBzQ385~"
    ")ob!c`R_KkJ&zr|#&A?1;aUjlSu|({P#BK(N(%1C;1m}k2?Ym7E!G~`oYCs`Xe#Q-c_2ly(Ma%}3HXfT"
    "lo$+MX@sW{&?B1zy(y5^V2HmTfa5J46MK`Rizb~z&xm|*Jp|`B;{pus%+=T*J+0C|X9$=uyd{u4vH5{$"
    "Odt{?Zmkt-KH5~Flry2#(-d^Vqn*a)49gl=MD;9*F-<uQu7eKk!ns8V8Q)`%rwjo-b~~lYP-#h!Te^Dw"
    "FPLYT;+oYg`w!0N`orB>|2>t+MEk$!fu_Y)4~I@#*rw`9=w+%CiPs3y``?tAT+n@@Z{n59ni>s;-y9*("
    "H|!KX#y9t`rcuA`7=EcZ9dm^`&f_}gTsy;>klaO7Cn<>xWF@;?YE-Kve{dYcl?EwvUyEFPta@;0auk?A"
    "w)DwTdBi}q8|L;3Z;cu-RNS#`L8?;K$Xp?{_WfpcQX(e1?~%6FK*3X57t|gx!w4jRK<s$1JF86~G{SZ!"
    "@7`EH@<6(+KVi)fP+<()#-fX0n|xsK?b<zTJQ+J7YR@wqEp!tbRjnwzGcP-=fAryDo`BJADU1EY86SDA"
    "-mwRW9LLH_@*L*On&;O(V}KUhU&%AaPL^&5G-y?E|LB-`xN~idwqbF!B+}C*NV(47LfhL1211-dtJQ?)"
    "E{~KOiO_Yru7c+?rk;kr!w``?D$J;vprUAV;qkcC89}deW`_p=gKQ+`Mx?KoWl|W;?q|dXD}vEwLo98G"
    "Jsi#FShEP`w{f#gMTqI#_w_Lvj$KaluvQB^00MSsJsCoG5>NL+AUhc)<W&$}n*$$}KTK|w=b3(J(e)^u"
    "w`}tRN^wU*cm6L3Gx|)OWxw^QfhR92S+$K1GJUEmee!~vZi2Q>4#^Lj9$=$7Jc9!Glv*d2qOT)e2?A1b"
    "tcVFeMZ2fe4R%vXZ`)@7_DC=YyWh3vkmxJKgTNKPh8cUqDJ1V3&;~U4LIZJeZIE7=7OAH;9Z*G=aMlRj"
    "H%*f-AjMVmmNkATJeHbSiF$7qkm+0_zBl!2*XUc5EZO$d=&RC}JIfbY+0wv}P~!zp-U?A9VTMTdQQYrx"
    "r1cZl6Oijvbw#w=jJ!wf{qzN=x{Rs9s5934nY*Ji{i#^d*(D{?eSQ7))I5B>w-7$c&-cg2xAgj-y?>>T"
    "^qJnjzw^g;>33gz-;Ces`u<7Z*Iiirg!tKhzP~@e@BZtzVucd@KOD06lj8s4R>yDgyj+k*d!(5_-w$Go"
    "2g)mA4lV?rfXPov6zwH4mUs<XP^=y1@KPE&twK^W<+vZT>Z<H4<DbKff~Dp)#;G{3N2eI!RPhv})Iiod"
    "1pY1AqH~xAM_zo4fAW5`$ZqARRdLUpho{02)rF|ZCj+nUw{AdQoeQ3D*3@`qEi6K?1;};xp)XOb%NUXM"
    "QaQ3NIk_S;>*zc{ub~d3<A)xxnGqZqYyBrr^>$W)Ji1TWhHy=qg+nD>&EB>Er+8eDaz4(?lf&5YI1U-{"
    "$Du2rqs*5ne(KwEWT$_cnM3#0w5ZT}YyFoF`k+Xn5dp`ngPTS{HT80ynO7eOtjkfgJ?e=Q#o?mSq1K%w"
    "r8Q6-C-K%rI3Dg&h+vvip1d+qCX`NDIoM*cUQHqX2N&o1N1p#8l)s)rb1UOlM0heahq8L;pWB+(HUHJ0"
    "4xsK@`Nuy*(EL{SP(aoH@sDv}{n^2@V<nBfWQa}DPq)4vAlD?~?LZ(4^!Z~CJ++n}LqRq}$I5ITwhusM"
    "oANo5bI^FbeI?xJ7js^y48u6^f(VtRQnuaaL4g53TYnFqSc0xC;8wsxxx@)OR;sNe$$wgkX8G*uePux3"
    "VbRNT>a>V3gO<{AD(V1;7^=|dHqum+t5p+UTHMq(!&5>O^GQJS#`%Nxea%-eI5$`Y<5eNTsM%HACk(6Y"
    "v?9=@$44})W&zxaCV!av8T+p4cdGg~n@@2Ls9WKyidS;>)oC99p$XfnUWImLRSlN?WWRa}K6H;zsDPSx"
    "OjGHj+G51@Iso6J`FHS~R+bxmmU>f&@3!nB=NQCbB?a1S2|`syM=6cz>y;R{_Y^wW2uiir`prJEnRKxC"
    "j*n*Gm@FKfY@><*VulXrXpVr7%J$-@k)%|VoJ{98@1&u$q)=W>bw0TRYuSd-0}`uqpUWFqwi-6r4y|r*"
    "e%j0tF!LL0h@&BvZ{05K_JsX=LE=fE6_eL8_(_D9MN0x$X!GhR95XjR=+yPSSA5=t#H+nc!>JtncRcXq"
    "(oWm5%oAi>EGdz5R>Gv*1uTnkL$d<QAq=}f-_c8RJhKHK7QFv9t6+z(GvNcyburC|kz)tHumJorDxYG5"
    "jo1%Px<c4*6}*<%@h;@ou7cTQG>pnF6c7nYJZt%-slbmr6oKIbPTq$Cg8~iN+Ol!wB%)_Q6czXZYI(8="
    "{17p=i0q6SU$+E2#T?jx3?n>X`y|Xp`)a`NqrB+|WDQ19B@%)eblbDY>mN52e{OlJ;L}V|y$h~oP>B?u"
    "W<D#ig<W35;MwIE(Z(mOwd4KatC4f#s#Pq6p=@p+NxBk%#1i}8HWgp#eZ03Z-pj}5Pk8_MY3+kt;h&%T"
    "5c}z$cVAIHzVp}5N6X`@{``y&#V&o_?eo`lef-l@xLx?Kkgs~ZXmQqrVFRuDq_0ZZcnW_~(U^6~axZ%$"
    "eekL_5{32slL3DUrcx4pwwRU^BV9*|B}A30O|K~74(%jMP#KNQJ<L=pe(=G`t2Q1!umClTe|vbXR{_`X"
    "wASqH5(@M<b<Nj538Orx-VR6_J>wa0=z&r_r#ZDc_aig8xX66M`k9BaH#35wc;k7k6-~?MPtR*x9;}=V"
    "@}B_Yc@;4M_DbCXN)P!%I<;hVwmSVy;}NKU;rNF12@l}r&X6Re^Ix*Z%=C=SKP^md(d*Z&hmy^RneSO5"
    "h%*GVP_gj<&`2^7)0g9^HF2YA!eC)*bkO~<u}G6g1=%g>$#&47p_a{8e(GwZfYgvAo&Km;cpM;%#+3gP"
    "4kmhx+Qe4|et*;OM|7@Zuj3(jRgO}$`;MpiYXjwIlpdeUW^00viF1;I7uYOS+QW{yw4a+DEKEFpEBUcn"
    "0q6fM5Q_Xy+9Qqs2@;DmBLoZ_LIx)5zs}9T(g~1DoZTi}Z~NoM0RgkW%1f6OW_&>OkLX*Ep^ieY?0(!z"
    "x>WaU1ojngX*McIj^b<9^PhHZZI%3c+1KzU(;E2jU?CFusVTh8U$(ux@N^fmQ+e30y}x~ZD*E6X8<v&z"
    "%TI`J&ri3ne(5)>h2H3#;&ZXId}p>?YvfLkC6nUz2^2ycU^4anisMVkv*B#3;k!B>+MS)!tnE2p%VD|M"
    "_<RuRR=?7nU!y0x1$Ea9*LrZrczYX28{R%yO&Bj_8Ts#tZ$@-gGwY|kSU@#USB(pQQTGGZjFz07#HL~y"
    "t7|RQtkoyJP?b-RtFWN}YiYfZ<oM16;8}^P!36=8V%E29<wYxCYgMrMyP~e3L+uo?d+<%rh}#fnp@$(5"
    "X_chL(=jH$1wiQQw8-$*O(*bRT}1i~QI&o7H$OcFbqavM!|Kda9lT1sNfR)!!a`PC0n+mkCx2D1Ta!m|"
    "pd?z8KobI7S&<B33V9P(S!K*<K6?BnU~WNlEex8A)J;Vm5Z36qMPfK+I42HGwGQsRWw^=pqum?(gFm_9"
    "@Lz4OkKx)_meNQHXc^_{PEt?la1Gt~2PYS<`5ytS8VnL1Ur9?$*cQBm>?qVd(9KuBo=VT9_0+jHWJc|>"
    "Nd8x8RUj5=JsXYDd2@v_w=49^OY@}(5Q~yNe3980r)3M{I*ses!thawkx1HyXtaSo>%P|7Os9B|;MZ!}"
    "fM>iT&v_)VYBWbW;o{uC{9Xki4y1=5XfH|!SaNyV2C;6(&5p|*N~A}d!AQ1hpw~~*9HqQCmrADEqC^|^"
    "O0)dIZ`>?x(ucO?y1DD7B+g&}5U)KXJHx8B5<+@>9&KXTsU(p<L8@h3*kPT(nueBodNQm_249;&N8`=b"
    "MrEx#^b?~{56FdR_2l?sU~R<jT@jFUzwIX7c<baBx`9^jJ_s6`W?K)}mj){9BB+A>QMUTs*TXY>Zw+V8"
    ";9F_+1Tu)?-Zscv-K+lUH}*S9MJ-`716k5)Fa98FR1Jy{2E<b1-?n;Je}BIZh4A(L^L{s+A0MrMeSH0V"
    "-u>M8{Qij7R~cXLF~7IZ_wW0xyZ=!CXyfYNC8qD6U#<&xaerF9_D`#q{%Q3}DgT$ZR&UL7rd<JX?(kq8"
    "Kd&v2eBRM|1g17?Q0Jdwuaa=1@E^%y)2U|HObud?w&&49wo_n1otQypQV?!Ws`kkOzr2&~6H4}|2Od%D"
    "eljC{&6vASy<Uo@4XXxM6PB-h7FPYk1O~9};M?5|tPN;(HUx^>d~z&T+=HY98;BRi2@sX30Inxi9V1#h"
    "rg=d*nB4e)vD$;b>(uH&a6vba;}jT&bbzkT_DSn@C3-rxCSRvkFASVrNC%X7)Q^UMY=<JUymq-f$i|4h"
    "{zxWrm+d~*(WfKtR?lVTFqAi!7gebo(;1vF%mh_yP?>8>I-+T@usNgjE~ZL7w|W3dJOm3);*$cYoucMc"
    "Xkhcyxm&evOyPiiibO_32VwBr)R@*#&S?*xNU7oxQzS!CJ@oAH@)r$_g4)3Z-!zWd;zgZaq0_q$)IsN2"
    "PVzJbeA%X}0}~}uDp&ZcwbtY;txwTEJ=ctzTWbC=u~I@krDrn4+RGKEP^%Za|6MueOw9kE)*$Q4=%(=8"
    "S;ZG3R;3*pe_r6KVXNrh9_3HFm0x>3nnHTfGXME^Lo>to5YIi<PV}LlpZyvwk6ZfG;${sZRq#*GJA2A`"
    "*;kxowg)^(=3fxSAK__>UrInBiDa3!{Y`5UydSO)c(gCaZo$8L-=`u9Yl+$z7o%p6{l(QPP$sxCvYNq4"
    "$+KFNF5_KRe<^+BRgm>usv=23G~&ldUba4mD?TB73J9m@5t8AZn$(wTN`w|Hb2h$K8a){6-FT|ERg1--"
    "Oe*&Kma5Nf86<mEE<rD<ZH;CDn8>3+CqV>Es}Z%vi)9%Oc|#D%M(60GkhD&heo7IxwQb@!^28DUOh8wY"
    "s%J<Gs8wsa)<q@a!TaO42ib_;=tC!J>1B=nb?upPq9*V?<14?ygmn2w@RC;(Z*|;(+AOV^h~8o#S<3ay"
    "#g13rlzW;OBseAdk4p?uy%UHR!P2CwuLBd~{4Ke=^uSlaXoHJ3{eV~dwHsWd1yp#PF4+4z6#~bm?+fSN"
    "rma#F7%%fD1KMT2Z&(O3t8Z03SqB#{;>byG)}`l|Q6+KXXOJIxdF&5~KPwua0KYAGDaJ!Rftn3<%fL(U"
    "9b^R8EF!T&OXi=4sYm&J0XtvUgAPZtONB@p6N^crVnU8v^lWu1Ok+6~h<>X^_Nq=HO!4<+*}M*Q3&b3f"
    "^xpvakl~H4{QKisSB$LGFr#;F5yGp;GqgQqZE-l9F4zg#`K(%#SF|`JdG!sZtZh~Ij~zS(711Y!OPyN-"
    ";<VGs36+vbsnG%D><nF-t~?#MQvBs>ce*66xD}?8aP#5bY{2L2(c0QChXjP@7XTN+_dkFxn*Om^4zLxm"
    "o5~&OB%6JxC5?Mr>D0>(CTegWyB`J`(<GgqnFGD5`X-@JV!OZXamshC;j4X=&!!*=4M~3bPkH~j%J?il"
    ";q$xXkMbR~>H2ElAD1jn@Asej`uh0k-}Rp!$L-6h$N9C+x{Hn->QvV7YR-KITTe*c39DN4#aHYho;##t"
    "s%}E5rXGhi;7MqgWht`NwEJ;))Sl7d=Vr;lql4l(^#^kT3EMiDl2pwfdFgR9P1LQgi_3O~!{Q`O$^=|x"
    "(Uh1loOEXdmobv?M1@4G*DgoTA2__iyK#S<J{7SVY!rMmxN00K{aEn50y1-U*zkVg*yT{V8xao<Uk%3z"
    "pPGE+hBoo#gcpT0PHrc2s5Hivd<|#Z(JoUp)srmV$w^|))?=5$d0LIQPEQMGJy|^HOoNAh9+C=1)8olR"
    "MF6zVY7Jx}dA{)^Ve|X3i(Z{KL3770Cp<OyL&BVfY2mfYL6v+NJw_=aR&YBZuGDa5i6t@nRvp4A<kRkn"
    "Sq(Dm2(i7%lJGD4tUirdodN>U_3>xArGz1aiX3j($+z}kR#!1iRG9+wYzbGbN6u8gyBs_T?6WZOm;Vg4"
    "d%AEA9-K6la}#&FjU#55bvX1##?G>oVVg5vBDJmClm0KQ9mMnRf$j}&d23(XGth8Z7Py6JxXDN~Almi3"
    "xNnf+&*;B4lf-zuLbpP_6UvHOZ3I#_2Lcm0lS${`p@nxNF9NlKg6KY2J?AU#5>Ti!3f#a@Qpqq|pWa0%"
    "b}0NI!Q8!n-ii)&7md&@wKXW^WJ$emwwC)w<F;jmF?|aEbQg0-JO@f^QUq~ML8z1F3=>_iy7b=GW6?8b"
    "Nx6cl9cUZy2`jB_Xk4=gAS+|bd@7ZUGGi*wc3c#*W%DJ4=aFQ1&AeeaBpV$6`}M5}9hihPH%(^F5r)=g"
    "cOjEd3VAaY8v4QBfdWm`D&D+XKC&3LU={1DbzBE|Nr_K_+~bgoYSQI$dYa-zo2v8@JvlLn7;{FKc5QJT"
    "WKv5Hj6N=@rZX$)@`$a^S@Q}3wPxC*cg^mSh^`!6+MsZ;r@i9_9v<N|iN&dci`Z7eP}<hLTxc@sC}@j^"
    "BcnY0!d)0!UiX_^c}^PQbAlhDJ{|)|1ckcgF~DJQ9xN*gCQ^x#Ru8O1#NGXD+XEZjQqO8%SD{2Nkr8^1"
    "i$d7Bv+Wl(Lvk-d0wT>Bcg-5|p=x8`^9ZdyqrRzG9Gg5e6I*YRmSF<H48b8o>oU@O^Ug83@0D$Wz=jY3"
    "g%cam7D=?7V23S*bq~)5RizWCc->X%*Q?z}ecJ(Pod8jr53FeVkR{(wg#thV^>p<ufIu@y3DW~-0<jdC"
    "A|!G@=VqN<-y4hZY%HS9H;G(!T}2Gh^R@xx<Dnvk;^5H_tD|J#m~vK@(lJXE*@)j%NfC9jG~x$(v+7+#"
    "_2uf)4f$*=Iy$;6a0hBp$sC`JMf>aJ$yfevUw46YA4ui<>!Zf^-agvhw7h@x_*LJ>PrnrX_u1Y*f3EM("
    "`#rvok92?i{iA*NU&tzYhErqlJDsl8T_;!8Xlk|Y@)829AdKr!f+YuphdFa)G;wkbKM4Ak?T->($8kBW"
    "SxjHA7RwX!nrc2a7#dpyN6x?DfIS%KFZ&SY-klBKA@#x8i?kr7x9Am)0~R*~gv`|&UoXM0c&g-z{qS{8"
    "fJ`Y4<5Y9KA&$@hqp@;6K)fDcEji;2hj}nMd{y7smG?}GLUGIl=9r+yx!wM(7tuMLD)*#|)e%~LMpq-L"
    "US8$!V?{jKVV}2yY!BT<A!Z(9S3;P3)I=gn2+j6n2X2f>g?#;pF0`s;#yES?eD($n43EPe2F7@Tq#OWc"
    "(RSVH(TZ9IRbxkNF*HoKY#JO@up0-n5#cb&nOwO2i*K?+!rs(NJ1~w_Y&|S5ZNboigSxMwxvBl!UZgyo"
    "&3eiPXDA#f7Slp3-=X%D3UqVk&B^00S8KHuTAfhlxq0$~MSaHI26X*_f+GAsE&iE_a&l?}T&Uz#l%?`-"
    "c`b#5>0_?THCilnP7@XELWIwvOA%8x7?Q(mv-_C|g_%NmiE^n9#3?q7CGLbgL)`RL*1F*qHNPLe#q%@l"
    "5680~YRkM1#gN3DL7zEMpMhlom|LB(D?-*^U_=W-Vq_*uS5Ic!DC(-DvrNgN3N1G(=>77PqI5gsw|WSA"
    "z5{_Z8bW|0bH7UWwX#7JGcTP$P@hMJ!@NVNoi34nzvUSUuVJS3B+7gbDy=khFLeVVm6@3V1>X};K2p7Z"
    "3Bc~dD!hQ5f{_Q<N+dRu2S=^0Jq~N^Rdbg1V-le?03w2}x?9*@Q7}SS?4d9qAqlNO?j(dC3*lDCvG<cE"
    "u`_wr!J9xjvkO4<wHfuL)D22T!s8DImZ=8`)5M9dE06vZzy+2+h+Sk%K+;#9O6d{THZ|+aVcH_gNyuE^"
    "9h|O7-u>m8swUVXGsii3u~c!R(9m1m&+n~+yC~z5{or~!Ga{@LcT{$YwC;PgriqUyc9;K=z`ii!C^vr>"
    ">;C4TJ`IWya7z8alBK&I-ZnAd$i!%O(x7%2nUs<wLk|&fy5h!*U0)jr#YzX6Q39#qLNs38@$l=8glsl&"
    "(|WGxOadPk^IR*e&VlYOm!tQ-%mfkB%s$&GYnxPGBwbZ^d0?(yJQ&o_QM2@@B3B^v`>DUahivKiGy5_="
    "cX(E}5t3Gy=OYRP>Ea3<4l?mz!xv#wp|9R{eH^x%Lf6%7vuO1b1Hw=zy065Ns-07jP%K8Tl$30Z3??EU"
    "OC+F-@p9lMLq%nMaM^d)hnbUF0{U&*!zPOf0nCU<_AQ8I-gZWOvj(bXJ&_HV6blq8U88aDhM`FjwiHk*"
    "hr+NvP5&JA9c7T|MeT12C=c58*Gq`IL;U{E<LCW;>VJN|_xkxBe?Hzn@AjbO@P5D5>*ub9`qx+c4&OO^"
    "w7a4B`TD%Ond|!9E4U3f^a{UtTRpdz9mE!79SC&}q)ws(CHCp4q!>>f&Na&9l%DM?T5%179c;3!;{@DS"
    "CylxOjmcCx4Bl1yh*PgCXgEbS<Wnz`ofG<i)S+!iIj{kIFX~C|g97>Azl6k9<l0&^apafdD#F^NHtbD<"
    "BK=55h?V>=*F;eOe&{uw?KM=&Qlpi*%zSMYNQJTEay)Th*U`K%<8zwRhY4ua;IEwG1BdQd9a+u$z{Df;"
    "q`on_Qqs=*x*5*8J~&6vODG!%NU-M8G4)eML!J&8o@Cc^kj~!Z(5j$FfcVDorLjajHdPR{tHZa<O;fpe"
    "2-1kj$vn*P2jnaDhe!S!VzBN7euMr~Pbe~WAld7FS3DQm?tVt~X6&4BDRr>LdgvvYR7(HgK-Q+2T503l"
    "BRU*5ce^`rzScuu9FuccF^%gk;v3p{nSbVAn)xGbuR1jp97%m~$odogtQeJ@`kSYAG5pmw;+XVTo}wqz"
    "RGYRazCE#AkNScIdmwqLGpkQ)i+oUA<+*vV?rD#$Gx+@}&00r^tUx+{40rz6EH1^)ee1dK!ypV<pM6Nn"
    "Gx2JAsEBV;H13l$Vy!}EGDh^{eJXB9K~DIgm!&)Z6$x|~i52AXx~-z3Um>rWxXulzu=3TVcYv1_UT8<;"
    "0m96+blC<i+dxb!Ss&O9SO#Tko)AB^?-jEM2`P0s*x9>D<)I@m;l_r(CfP}!h{&bl0$h&cxj3&_Xs|3&"
    "KDv($WA?zP_JDN{;)TzjU5Ti<C|S!Y1k<=$7?aD?EZJ+ybWZ@mU*pti!9g5`#$Y}WK4Qfa{l!XFS1Dfp"
    "_yZcDtnImJAZg2)&bvLFm`=^0)R!Yo*DOyUYlv*Ca^CQ&XQV6NIhiNSOBu&|$-4mMBuXHVT7n>|(<Jd*"
    "w{9t3VOw2{Ngc5LUo}>69wdlynG)L;ISFzO*n7rr&E&t~Aar;)xz7v9rp?!B?5B$iZnDAo%oD7ynUdH?"
    "Ns7lN9(5lv1c>PM;ZTlk<3W%JdmG2|CG`Mc8CloCyNNF$Y4Yf^;R+}^q{k*)hRN9`SCY^!YLpW#Co8TX"
    "B4Mu6-_<uLHfyGcc{3vSK?#h9OuOtzka1br157~afoFbXoD$^9Vm+Y?a&F{mdZb@@<1&=24BCAm4@-FM"
    "UEB)&3+Izs!^tJj&%`_!ATRK0X?lRy#WclHgiNTgGUE7mZ7FmXbyglM6o5I)w@T;hD6abp+JMANf3G=-"
    "!mmyGn0AotWR^!bFSU^dTAehc?}vJT1>`D&XYQ0uuVen5F%v*obCPt&z`rUE3*Ni}dck77rkd5!)~4Ze"
    "D{SCy??D1E&M;{z!zng-Mmn!wI(zC)Lkn3CYEXm2nC<?#HiThD%xy)I207}Fdt{LXG+9fTyq<MQXZ?NE"
    "*#U!(MutzQ{`VCr5Oo4?T>d(Ayu^5=^mAV?U)Oj1xW5HehV^^Y&wStb?W4D!{8e)KF5ls+r;ocS`}(f+"
    "KK||l`j=MAEzo~xwMu>Qqm(UlJd|Jc_BG=f>xqFIW|yIv+?A$k;L#3Z5Ute^N-6@Ik$O3CsjNPIL${pS"
    "R~=`>>c}-{(yc1mT|9WSNnZ6#2_mE%bNQgyVm=q_nKI0pdHSI$4Z2k=b`6lnj9oZsj{FoWMl8GCFX5Ql"
    "ksSajVD=ajmU`G5JRhWzemLwfAIfHeS!#G@)B-RnM^ThVDfbocR0h5~RUY}!A_|$v32&?#Nlb@e#HV+)"
    "lG4_mGS_x8sK~{kn}{O~!l*Wc$L$J(Q)V5}E3dE@f4?Tj$qMs{pA)QZw1fX*b~Z?X2Ljc)+X0_T2A+py"
    "qT^L_FgHCx%@`#&j}9(E3~D|ZPdw#pV@kb{{>6T>$H1N^ZIJ3qFobl19cx#lQX(;}sTvHFT+ZONQs-kz"
    "<1yxkk9_)w98Sgf1K>O|5gab3Zs~3m2A!|UpNZ8yE)oZ@8{WI7?-ZHsf3paNeedCq<z(xb+_R+3P_lae"
    "^RurB2e-)VhvF~O^!iA3D~6^i*wnHr#M%>@JYI1LkLSx<f5pr1e*Dp%ZEkXG0Y(GxgiBLAwn*6SnpiIr"
    "4ccyH3BO)LI(>lKYv5;>wQh|D5Htrwhv~@KKy%RT*oo&qz2@(6#*C+*uOPm7e&)B7|5590wN32P2c0Jh"
    "foIYt`mj4korK!cRXHc_b;Y}rHiV!4n>6VQ{Ftq7k3bdp7T_k7b*}{BubAJ*n&oY=R=>$dWF$o6oBC~Y"
    "szlrS1?WWHs-Wg*<Y+6FMF*HDHnxHTl;40*7##js_TPU1eR=+vI)it{%OCQb0r%Gq8{-lA{M%`&CnXNs"
    "_O13^`TGKT^A<Ovh9_?pGrkQ55qW1SPU0e$%C--9Ai)YwCgj!l=Ra0aRy5L(o#<1z@x}+Zzm(`V19VGd"
    "y}0VMG~0;03n8@hu6O&i`x3q3BAn=biTHQ_I!G+#4E|Q{2Za1VYJk?rJPGHNr5E44CU9!y`o8#R^L**e"
    "|HB!x3zK-nG@l!q25Xa}N@!{L<?U3#Z#J_J97ODWZQFgk@CoU&=R?WMVn;7r+Xx{do2ikTc#Rk@xwsx^"
    "3plS(wJaY(L8Y#7B3>3{$@38`uqmK7D0E@bnF{k*Tl$H#gg!K{7*vq*&9Aq(js-@J`nd`mei-k(B;=SJ"
    "VO+<3nrK!~fm*IB`(SA>b?(gVQNYRD;``vNlb2URF%7`DBi2{d*}P%XR!p62;56^+JVh-VTRpohf)!s*"
    "J6hX(+4a0oCfSt^3o=;R?i$Bdpv>dl(09E|^Q4Yf?5_(`t(=P9&z^MT-_$MLbZ5y~lHOL~&tv>a(}_^Q"
    "{j|tyFoHf(uol_2@0cf$5v|qo`kF6(%^QOCsD65`>+xsI6UT_sX^KNIYTll49Ywabz;d1xEzuv<L!hOt"
    "<Qr%_W9~Ltssujh%~jR)N7T+shsumhpU%2oRf3sh(yVBpln;)UEq@@mZ}NRvjm3{;K0Z?2I6@LWaVtgS"
    "3z-Z)^$mwdk8>7vJ4gtr=fY;+N<<TIBeTX=Aj3>tU7BqP)`lI5{6t(ED0K}<Ts8{&;+Q_o(VF9-@?M!e"
    "=FN%|cpe*iG``%AxI;Q|kW7pe97!(|*H~9GVI*UU#8SfEBL!dqtISiNI{iY^CXp!+%&af4s^SROpThug"
    "%RoB*djRZ}j3hA$o+k{~YQ+9_DvB>Fy-T$qTbzIi!%i!;`OP^d{#MHK+mXPw#O={lbozkUqtwazXj0lu"
    "R}Q&K&eR0Sqmd4S+a*x;jgTS<naO|Ff<=Qna&fol!Z$Azn=E*wb7u?Q*?X<0GvR31eB^RuU=(ez+8$E("
    "^}vXR7fC~px$kY}2mEevP(H><_mnzp;2u>Q$-mkr%6f!ov!!Q;cdwUixl*f?xRb1m#p~8oIzYL_ISg=i"
    "LR?At$m2Y?BY0C&E)K*FSZBQw27#Cl(F3H>aPz6oyVcz&+FdnrQ0r{?LmOgMsiE)|&o<*g6@4LZr)2r}"
    "??aQbQnEd=FjZ(&&s>qY7i{GBYubZS@D~SCygdIWy^}c;yAEwN!s=j}nS2_W>r>DG$rIiGN7<WTNse1d"
    "yBl&pKQV*L$#MTnc(l(hBLi@%rFXidmQ-00?i_#%8*RT$yK={At9Vh^8O|dNCk|ZTFg@D3;OOxh+Cr5f"
    "25v4mf-oYbOyf^jw)eC8+Px8_W`Y&pNI~gyPHXKOj6<?gQ^2pYBr-R`y{fk|e?9sgGP<7-%j|Nsxcb7{"
    "-uIel{}w$hwHD10tgLc6C|;sFjCSj+kyp<sxkyo*3U3mo>C6i*XXW^_a<oB(vx4BQQjHuBU9A(p;{GON"
    "XE5<o;b$wQHOa}JhKiQ4j%q?4t)uW?6(^HX^yyEp+S=^G7gTzM`;d=_>jmQKh1`QR@KL~`P+F_jBwaEJ"
    "pFl69f2qf2>LF_e>_Xg@ri~H_<BmsI)I`Z@YD5OS$XR<dPXNOGq=kcssqc@Wh(jFg)9e&7JMNI<5%j**"
    "Bd-V*Zbj^rYLH7LofpAmiH8KO+_l#3wV3cCFDaIjR$Z#$C8#<j&1&1y*YMd!m6Kiuyf>t%o~{Dh*jtP%"
    "ssf^<4Z{*`>{Lsfs52G>@wyU?%PxYEUDx5a`bR+Ml*wK;hZviNM-8-!)HF!KMEcGuWf$d2Bm{{Kw)0&7"
    "Yh>23>aH)7JSO7?swLnQs;O<2l$WM*l)MJpU9acC`lp?A^55Au@sDATty0^Uy1yW3+Z3-SNw2iAg69Y~"
    "D0$!6BLqI5=!<#Uk)93c-Dt<8Re3!rX&^-^P2rB-r-A-%Oya2NmE7{+bh?@D<!E$tDyz;B2&%WFC`}Qu"
    "|8oIjOTT}XE}nNBfAh~@wa(u^fBaI$R{lMH{r&S>3b9|me&+G>_n%+KwO^J$Khw|h=hu0ypx<2S{Xe+U"
    "%QvPY&#@P`Tzk!G9!alAmA@8Rk>SUa+XL=2x!oEE#(1bavAa?)G@F|q#qnfcC&Mhq*z4f>Yl?YPgY_fE"
    "<gECUs@3%Y{B=hZY_)4@wN725>_dbY=B;Di{pe?e0)GmRl=XcEdqE~t%H^>$kld^TN23E(>LV)vc&`n!"
    "d#b6A>_LzGIkIqEb(!;%<zb$oOR$iMsXnD={|(D330NZD`wSuZCk|@?QzZ$8&R6rgpVwREA$E%KA&BC9"
    "xQKY;y$fj1oEYgIBBs79B+d8)gPg_jk7>`+;-+y&)@K@I(}Q6sS5rVfrSxo#ODPYJc(&!<)m$>&Gp;;`"
    "F5@o3|0w=jS@QisW=1}-l0DJifMBJuZ7bhe(Th$s_$L~<bw_zfkRF8p2%95dPKThDp0n$UOZ0|gc^qH("
    "B;U&C01QF!t1Ic0)ch2_MkMw~%=-w)ffb)MVMQ#*L4y7D9A)^h|GQmAqM87=r44yK(Fj^AMkG(|i_e#x"
    "{E44gLY1{RtlQ`-0A2Eda}-A|AI(1igf#C>l=X)7(_MABf3k0+L&B=HLP-9H<-Gtf=IHhMh;~ly${bOI"
    "zTQTD#JJI&`td5>f0ZxJp|3a*=%@pX1ppgJnOifaxs}v|T6p(c?Dm~1YNiR|j+FmIG{sF3u(qDPX8dA#"
    "`+d>N+`v&X&x)IOGN<aYF&RWWpHLl3$`D)w_%vL@rhkF)J5AiQFA(3~aeJTw9LzW8Gw#P@CjlH&5Ra~|"
    "SYJcr{L|xK{l09P!nfoeU?4Qdq%@Q-9we{O;Elq+s1v$5f@Pc?X4Ou=Z#Dq!e`emDM&(~p+=m`52k_1}"
    "&1N~+*w;Q~|GDOeEWL8%bf-NpZw6HD2yQ*^`(;lMGdHC<>H}Uk%#6fcX%-o*1BhRCCs5$nmyF@nb{2x0"
    "rw6)7C9GKDWd<muvJq1+bmrtm-hrhW|8n%X7I{-3Yh;d7^jxJZa8+d$V<lkprLxum*?p>~r`q@L#=UNF"
    "!Q-az!lzx*88_Xj==$xI7ND}~Jq*3eHs1ZrMf2TzP4Vu5kxTN4>+eOu`!WoHsOw}PYA_!5v?W$|G_fwz"
    "CTxofB6r^UV)2iXbM|68Y8;^7_!So5r+g*O!)FwJJ!IkX1vm{E7$*@fD2)wl6%fI{zm0rnzeQy=Q1j!H"
    "4S@$3ee*3|i<>|=t>~<-g5!=|e`xNh_iuZ2x#zkTJSkg=XYJsZ1iG10WML$6epQ76_iNOoNUm66=6syx"
    "$BCnYB*AuU^mfkuqp`M)8<{TwyjzjEuIovlt{~_GzJw=<2+PGQ84C(oPKNz`2EfR@KI!htMUONJOhoY>"
    "n$~W)4)NlgzOZ$sa3H^0KK9*5xE}%GuQ<n=+DRL|RpQ}FaeE58u)yGR?<z7m154uOVuxSy53iq<@}L)p"
    "gwlfah;{Xo>Cn1G)Wgt{!{UOLN>I+nuO=Xfk<snSx?(`rc|E!7wvBFnZ{Xx}p1rC-Hl1v<Sk`nR;3YQI"
    "$@TgqUrUrBL=87<#To`t=(y#+r2_P?22Nj}?>?Pj->udJDLDmF>M_xAewo0<B^9p-`YL+d!94-$w(79{"
    "ie}457^{|ghz=O9-61@n<mdoYEz^vvU)OGeY$A@80Cks6KTZaEEq~N#P4jLve5i81CgBAu6iSs4d|8KB"
    ")AgLIWq?s0!o_<!z^alnIfKnLSajM6=H`Iv?NEJybegU;O4_U|uOiUj%Lh-AL$fS`dmWocpLAU^*}3#$"
    "KwncHv30l@T7x^A?!-`wxufvEcQ~BRNaeI{+I03vd^_#RS~P{lG?7ZyUKC;q*@0{8L}lc4ZOUFEYG~he"
    "n1+pfFUMM1fE0dBfwv4ixV=%!<~7)YFC{f)Aqa0G5vLx4>z%hcvq_tZ!ghS-=f~+7luVcHIX)hgLgGwj"
    "p#776!ne<n*}9SbSGPMmc$CL(X)iUEPml--VzO1yj#eTo7R<s<Cyc!gJXfHkz>1N=m|C}EmabTJM+=HW"
    "M?#Ied~5Dn`O}sYyIm32(LYsdilB!bvPAH#<MT;55shBj#O`90)q|mPyegAUH<F$NR_h;R?@n{aD9QJM"
    "jFqkKeG(EeQZ%jmd8=bhB^1M3utL~%u1BUh7Yd63=8d&YlV+rhHC$zI>Esa--vCUxHNTKFj4%7zf2mke"
    "3CdYGqqFL6GYru$P6yH5))yu{G&@9#)pR*@4AZ;#>0U7E2@^5H<zDwF53>*^`EZ)1YNvP|hfDmB>l|y5"
    "o!vBvB&U+Io6AsBMo?ltK3p(bQpodSiAQnG)Z_H9;V86iyS@fz$#IoKKwKfFD_uU+pJi>3a1%J*fuaEb"
    "nh#q?VnM}Yna3&wD9XgA?K1JqHUg}9`wr5%m@?}&@$#r@>Xd{+7M&jaJ^aWz9>6r{TgdY=wfDH;J)Jg7"
    "U4L&~33GfT8KI>lP(~IxbdypG*pbxRPSgpvVp*MXJLt?p)<P||#h0;XNrSsa_^d+_y_lt9zG|+q>9)j="
    "Q$qObi5YTGL5j7#;ZhtaBtOdMsM~h$rsfg}6TD(Bd~Z>LU*;xM#N}n;!52<iGQ~tXB5tRDVz6!1e{}*{"
    "r}gOqGS^Sl?bi)s1wju)ZUFMeU0Rh36vI(m@+JmZYhHD?rakvf<`b~#h0B*(K?H@O&E!ApL~kM2K{$|Q"
    "hB-b$ev@BQ`RN)vdv^C)vqNy5WedJMoN>jw%E{HCw1Lz6iJ)hZiwfdH$WaG6HI>|$hmomH`^;v)E!ysp"
    "bW2H4qqe2sM6U#@ao0xupN%8GuHT&V?_cfcBmZoFN1N9IeEiHm|NcG4pI<-D-+!*XCjIQk-}&cv|M|0("
    "ALsSD|DL7)`jx+RR>GA07doYlPvc1Y$l_AMXi^BfUY93}$D8Sm(kRXu<v&DmVWgJZ$9cA5#2!Flb_8l;"
    "y&_wA^4vL&0ZSyfSXkK^&WGms=<{VebF*Rw?R$u5(n}&*x7vM*&GWGgQ+W~?%`;I~XiU;${;Px@LTxm~"
    "awK`+nbMua_12YX*s%H&>N|W^817BOqnV$))+b>*9@Xhyx$a_m_KaxvfORGRrdrGOM1EwCN4h4kDfuJl"
    "=c^WS+FD3Y8Jp&#7ryExrJ+fCSz_VO=`lq&S~fA4Di6;|OYNx|RhC>r3f~An-UPRh<M?R=L4bFR6zPc9"
    "ax9g|Q%#HmHmiker<4bRCi2rmDV@(7URDS5p|+a(z>$zgRZgp&5cJAMee|aW6iK)AfZN2SiT-R4u6;GL"
    "Xv`|~8+S<!S~?ziNJpPz>eVsVaVnpI+G?_46F&MEn*tx*ADv@DxZTo98F!w~!O=R>!KM(2No2pqnB)9E"
    "=@gFAKq*lZxm!L`uom@I9z7X>>;E5Y%KbOT#%2U$?iA<OvHkpJMf-HTZ~EX$>dKY;N2^E*+G1<%MAG$2"
    "p&YLt1VpkNF&l3`cOoTy`wZpNuJZ2_{39}I+TAKP!f4gJ5%2fbl_{bMGlW6MxpOGxU$;ySYUw|_RrvQ6"
    "cg`cIiDacd&Y8KD#{i~JuGO)yB!$wN8Lo`{A50?Vsy9BM+U1b>v4xt<<>LB#V*yAR$oxCn{L+W)@mtEq"
    "+w}OYtUu|2hp>{W1SXj{)#oid%BXm^8RaG|#+Fw-1DlSYIXAg<AjONPDd+KVCCp{`4=1~W>Z|uBbB3KD"
    "0E6f2iAJK^E5-LOuRTd4(z}Hn=I76m%|D&^f8O=jZ4EZ71Sx>@{k4W-Wk08Ug86cl>B1Q4lPByUkZ+CW"
    "ZoeumygWU+aYLS7wxU-5E~ikvXhB<D7V~xb1_p&uEYMzmhyh|=^5*Mw><${c3i!vBbOySfS8@hT=8IH7"
    "LzRG;2E~>$sTsABz8<Rgnza6&_g5=-28kG*&45qxiTN>5V{2$%>+vQ#X;(sDj+E&1yZWz}Lr^@!&1ov0"
    "zcw+v!nR&F$(Q}0ZQz)Inqp&2wK3rEwOGRqpiG4NReK3+RdJN%dSkMm0~|o6#mb(2lH%nFOrNG)*SoK1"
    "ea1Ut6NGprZKFEku2Cm1Qm1egg#n7!f6W%gh2XW&?!EFsuB9)=yZaqNkB%L$>`s~t)+@?zMCb5(NBV1c"
    "l6e2Y6jfoqa>Iw=6A9#pPS&icTeDOR??H7%4d(UK!T?jo@%akYAgU-_o$+ggJuT>gyE7Y5JnG%d!M9+D"
    "UqHqVP@&)+`IrY2H2HboR}cvxL0iHRlzJeUB--wQGsDFI@<6@M*yOx$tQ_sN*qk~yo01%^j#TOK_U1u`"
    "`i>G?F>o)W6~LN-UOU6Wh6|O4_m5>2<IXD<SJLEIY3J^NqP<B@Fxyke%r7g?<^W=c>zyvHGyt`>Jj1;j"
    "2Y=B~T98Vltu&zdO-Rj2r?bF@kUB9|<CxP5-Kyd*Ai-rR`%IQxylW#03i$epf{?N+@&&s&%OrE_5Htzp"
    "`SdbWKL#B~hdGzNGTzb<v9i@5oz&yzGs-gXPp7EZ1Ty0}fhDgSJFCYe7uT$cV)SEk8ZfyY_q`yEUuh=H"
    "Pq`pl{p78cPM7mW*{ew+$id}Sn}u<K=IL+`ciY~h+NwD2!EsB-VSxaoo#w(S7hL`@1``0OXHq|zm3K9J"
    "G+#ys>c4Pj$WT<)!H~C|7ppjn6wg<4Xp;I{zK>;%);h?9Y)<`J(iPe2n$V3GnnApZb91(zB*aIAoP1w+"
    "V%7lORS3om%M@hl>R3VmkesEX&vTFxnTe>^k$d^mHfkupDo}o^x5T6xT)!T$4fYqcp-2dt#ZHIop4l0p"
    "V{OmA&T{CMs!OdSRU#|izI8Wzx+Hv)yiW(C)96iQnRqA)=4>MR4!F2K!|2Q~$mjS&S2eVqv>>!1*MD{L"
    "2ZPhQMPc#o+*3d=B2hlco4SJ}bQeN6EA40vGEE&Z1rfYdJ~%lGB}KPYWvrA!mVBS+WQE5RXU8k`QAB$u"
    "_iXc}>ZvENoYp=wMv*6CBCBt{DtRzbKxD5{uC1lsWkx^gG6gz-y&FtZ9Pb&{CD;g}H|qKz39rr~@hb=d"
    "E3pDE?4q#H;5>JEQk!?7hfwM2S{It}4%41XcRNONhqe1Gay>XsXi@wriF~tez4FB}dRM&X5y_V+LL1*0"
    "K5A}Tsjs%3)(L=p56lN7c{M{)b0~zVeKcS4Fwj<ieIsc@<+9<s=S5;$9m+N$&Q7$EMhKVg_AoA{tuM27"
    "HA(2sdG$}qEYSqfO?xRdrhIfQxzjI8JuE6IQ3ztP#-8Ub)q!TcQbKs*_Q8n8rkd7<pfxSjRF<9-4g7Sc"
    "Ib6KQ0=p*2B!TCJ;9)(cNmeGO%3r_Oub7O{tBQ!WziU@JiJe!tl=fzn$N99C5xdpqX%Y9-V}rp^mEEZz"
    "tZdf-O}Dd`>!E_N)9WS61x3+nMp<8}LuPM;BgDGN0HJD6<scU53$ezC#}{FTmds2k5BZ$7b}*n4K3n8R"
    "DSe;*n1~o3n(2G>oaug&hn+WOg>bt}DUl`V)zzaTL<(|fU<>=Myuj`OzccCi!4L%wSkZ_p(0^?bIijFP"
    ")3S68vMbipx%U_r6^=05{9oCN>)Q2^fB(+q$C3W@Kk4VMK70T1^ZZqg_UlKz9?oBXdYjkU^Y_<vWyc}*"
    "r2qNzGnZ@W{$>Ul|AQIinqB^1+SrS}vKKlj2`&{Ys%X9T6b)R^2_ObLkx~>w<{y%7kVA>jOpeEXbc2ZX"
    "iiSI=F&L#|Ja&mVH%^nWqJ^k6ew4}MhU0m#@l$;vPgIBbMkz_?rEJ!-)u+n%>wk0{xg_w|2A_QlIxdOy"
    "yk4(HKF55bY<Q$0Z6#Ph8l0bjU(6+L4LvZd<%e{vOnHi1=@i>1*<T&c5y9k1U}3D&X3zIi2V&Gp(7e%H"
    "MW?Iq(7f24angf<PU0!j<CEiLI+$NJPjpw0fP1yTg|Qd?L*vx=K%dYvm91uJ&Y(;rbw9BZQRX-!tMg5s"
    "WGVTntkL1}r@H{I*FmzOc|L{&A9tS{^q&rW4-b08HcsXp1U47}^C-_`M@dKUh`Q`ZbDrwnucaFoIH;yH"
    "JGDPPnD2V{keT>&so9K^9@4c@X-uYnJ-ty`J;!6Ih}boB%l2`haw?CHvS}c)=x|2TDpmgPnBe&Zg`tG`"
    "Y$pW%);a@P{Yi5C|8s@x$r&N=2R5oC7=8cezlzs6Xr(O^EBqL3`yHRIko@HeX}c@LxUm4O67uEO#smCA"
    "ZI4h0?`%f>rsV&hY$4mBEuokO&9uoy_OP<bR*67jFy$LlS-wUcMVX_LkZLeM|GuY521EYuy0?@kB&a1K"
    "ZeA&TgBx+++ZmpXTyFez1%!<SryGs?;8ogvImSPL|3fh<NKX$`a}*L_Un<)(iK;XcXv5gDJUX`dBrwPk"
    "d0b1-mj4>Tv&gr#U6V7ymgXxAD`^;^9=k{dPFL5rhK_TUG#Z;tk=Nr5D_kafa@n~3D|h@_-9<n)n}3sq"
    "Pd@#8tpxe~K4-_!6o)}^DBT0SY+`<8U#Yr_#e)tx;xp}4*ERZkifI+SBZKRbwtSg48N7ai+%KGVAhw3}"
    "N>A_gpF6QN%Ydl(*ulSBgs#`(y~BohREzQBM51mBvFyTj+5SXA6yf`?spHN{0_dxuy?hlL*Xr$>SmVF4"
    "Z%nzVogS}3-qN2Oo}+u_oGdH5al~!oHcQeQS=DgD4JyRG1Y*DVxPthKU(A5}*VTs*yK*laZ=509W7WwX"
    "YcoC&p2CEormtGd2-E@F@BAT-^m7kan2{lPr;zC#J#F|}WHSPOB3cV^uG!-C!;P%(J^a2X;MFAC8iwwa"
    "oooh$ky-iO$i(|5G4D3KIHJ-ygHtN54~x$T+`mctn<7oD?a4btIpwe%pnx8T|7+UA4H6F#Em%Br8LR=!"
    "e~kx1Y4jRjDfd7mt4h(QVXw7#yu3D$Vz%+Nz*si{K_!Vpb^Puw%i?q@TgFY0!_7b<#VUd!MTVRauA=+L"
    "P8jLJyR=~CCqak;7PQMCc6C_FhTI$`E(rT@sk8fwZsX1xA8#3T2M&Let3P;Q+>f@R13~u{y4rD(3>K63"
    "T)7w$zf71BKjcHNBe#XmY#*5S+5NG8XH&#`t&BJ@N2UbJ%Kya37kzeR)nvDJdryU=P~$CWE7?zZZ2hUX"
    "M19`3S1=SJb3K^*mL>>RZ$F%Xw;CPJHV=l)HM;hVgh6FERR8$J{qb(a3=W7}tS?>mvxWH9t7WiRXZ{3;"
    "M5a~QUUTRS0bICpkWSlJQ@7hhe}YSX&wB=WS6bF2&)!ljOjAH{tK#_#&2J07W666vsB3^MpoK_xC`Yy4"
    "mK&aMr*`ig7%@=8EPfwa7x@Bip4MvTiiuUT3C?=bUT-kk&Jwjtv_RFqBZ<~!XOL_pV_F!C1J>KzIleHa"
    "YLU=Ioz!nTb7-ApGUD@hNch5FdP1tL;XDYyJ0-};bi}nn_Ir)mOuU?2UAn7h4?*2f&=gKK;<(yQ>-ueX"
    "%LnsI4&@*=m$gOg&?`0BiAs3eTKK2duO}8%HP#||YqrAsdf5&%>UmiPJ9#I@LAW)OWUAyq1j5Af?m>k`"
    "Dn6gRiqrF1CS9wwi0J%hx!G{sSVm^J=BQ@=KBzQ|#&i=3@pzAs%@zRulSs4X1CYm)PBeL5_bZ&Da69d@"
    "`-`W@0>N?u45&6#OyqPo%IGU$HW+otwwf*^g<#jpVtU+dnagIH)V(2vyPEkDkF{jBqJi8*_Z<N2FZn7I"
    "-Q#k@LkV=u>XXQ*-K7A|f4aZ#O_{fL)i=NjQBbP})`lNxsp-QYCo1)O=ef=y`L#AgUCUl_yJBX|P^&<u"
    "XK|t`4-|blu#=ibAOkrM#873sxY?hNyiqR)mRd}eDh00QOaX6*P}%IqEimxY-7M}v#A-2!&|K+z{Y*Ml"
    "+-$A+6A;IBW7JtI=xoJd&tZs9tWD-(QlY5mrx231<3o&<umG{Q>kW47mIG*<day|<&Zt<#x20ZCrHeaq"
    "2&+OKn@+=#fK(=^q$d*@H=WRSJ-SYWT2Jp2$yb(up?O13&<W1DKg>O}vJG|DGU1kU^_3>my4|+Q_38q)"
    "h(4JLq4Id^y5Smq;JK`QjI_TL7&a&=xFJ35Q{6qpf~@kj4ijKks~W`=$XAKTABS<x>m}G$BkGg;5ewlU"
    "J(0*n{Wl397NHm82&B0hI`66*a(o;!x2DVuQ-Za7yO;k39!2&;*`r+$wkE(7E%+`GZke26Pk4Ij3!U!@"
    "PRkpaC!<YrmafhyL{(`*IfbC109dA*yO#;#7EjP*&~i>KWh`wKuqAwJR68cDk5!9gl}!Aa7Tie~b*78q"
    "=XyF@t9E%Sg-{Zpa+js3j#TpK^P_1b21z~YWb7#e2jf}|8|B()+oCA=Z3#RPT2uQVJs_EA{j{`2SGm)0"
    "R1Ga`dR;rk?0rD5YYkowxLJ0elWy?A%jdQ%egak&8QgoV|100}w_nR-{*nIlajn|<XZzLq@BH)U^<Pr{"
    "`zP0HWw_S0{HGkf{p_>-$?5mc`X`OQ`C9mX{Nr0prTjOy$ozDRjD>H>w<$-yH6gg=L8i_eVDeTBDKvE("
    "`LVZI5B+IZtkR%ned?Xi@eg@0CnM*4KE(aNx0q}e5|P;zF~5B>0LSTIxi@`GA|uXEcZX^Y;4cz8(7Sn7"
    "JD!5XuFt3CgcqgK-1G<(OJ}dv9oYmOHuYc#khdt(0<_;!e|4txY@`wW)$$SSVSW<s7rbz8<<RHTnc#u$"
    "a37<PQ(|8wDxjEs%*Wub=EFe4^#ULJ<ZWP0v*paKy3zpTrzkOM-7RX-+6Fi>9vLg=*pD*`C|w=&R1@=7"
    "pG=x&nSfcPaw+NQ8es%WkSO`^Z`TZvAAW3cH8=K#EUWYwC>fq^ILXe`9afjsJobwqDlB*x3(~Ik%&%cz"
    "EeYOQ(@E1;S=BjT8l8hwkmBk(Aw#7-#;v*3UgvVnHOVz)_2CL3zH?nk&FGO*fCdjfrX+B)J9iU+Mk8N;"
    "avkY=P7XH1G^qYqZ6*Jgf{_xDkfD<OBwC`)=e$EE-k%{@+4y{Vt^ir7ma$VU7Q==dbVbBD(FWIopQY?v"
    "OS{F@Q5^Z0z*WDvppSl&9y$H5;vg(h%&!g8PubRnFBCQHR7*(C+ZWyOAGwyWrEK9hZ+I3CrOxr!fstsT"
    ")f)0uP+)Fo{Z0NQ1Pod0e{A7g4F(2eb8Mqo2lFct;F3dsU3Z5B8Ql?R5^O=*dS9aIBt_T2f23Plz`kF-"
    "DA##y7qBTvNL{FW(-hj#m2N?l4|E13K3?mI0ip(|Tz_Y*o)q&{vb&gvlACv%Sex<x8hKb&*tWFCS+H>W"
    "4ah+sF->lfIY&gcI*6*6T-^Uyz^AuSiZG(rXFh%Z7Qb~jQlLQXdvw%0Kw|ok`7UW=1m6Kx>W`331nIK%"
    ";+myP!MODD!HvD+r@w7{<Fc+U&ReWsyeM>Mb}3J1Eo+HF7ySr{{N=1&A%7Ai_$!6sh-341jb_wX3<p?s"
    "8YH+<O9_pE{(3hsklZwYrdGO$9&kw45ZxaB3iHD(gR$iNXF8hhht0cDtHN?)6S&(Zx)Ja-tJ)NmKm|ok"
    "VxE)Bcu6ClfPaZjh7ukV(lmE#Ob>$X{BkGd4@PJZH04;;klyO})Fc62vj<UIXUf|>Fn%SwY{2*t3}aY7"
    "O8*L>TEJ0S7EFI+z#qK~TX2F72lGW_4{Gb%)R%WbzczRj*8rzl9}d@1th9=NC_gQH_R2DSN(i-c8!UM3"
    "rl69qblResQQh<UfNRiDGAoAD&AySMI8@rb61>`V<%EXTb)}l-uF}8qn{+cA%b}TtB{obFk0Ubd1A(1i"
    "y&skHTL|}u1CCZl73T{}%!^arbd$-n$SVk|XwZ767?~&`r6BwYeKl95NLdtOF8EbA2pCh{$<q?NkTZV2"
    "Bx8*;hjHH}6*v&3=}ke8g6j&M^t4Dv(HV$#t9p`s+KfGRVP<tXb-lcV%)lEB_Ul#NcT^DW=}Hi-$|b_W"
    "#=825DDelQNJQL9wjGF*d0BF3lZ#MTfZdT%4+q?55YM?H;?o^M#8rzZN{-mD{%mh#p=hQ<V|L);>Kde#"
    "(G+OdvfU6JjS1#uaupZ$nfh?w%a;((d_S+MnpjV}Pz5Ms4O7F&oThN=W_I9GY0;M`pJj(sKIfq<V`HT{"
    "J$w@+pXs%2X8Vp!%#>__(d)wc4L@Asde@DQxi%#s_QN?1S^!IrNUL%lyD6DKb5n6Ma%!4wWb3-j`iYUK"
    "xjUNzCYA86as*XDxDd98R6yk8CSY>W&JE0rFP3eQoyMYss}famZjDPW?x>M}C+y6D=`Y~xt;jlsPH7Ny"
    "h0WL+mIeHwhh&hq=CxOvORo`9IIq*ebV&<M18%QXBwyGyaLV;Px)ymN-z+M%Q+!+fr;VLH6`AEny#YPD"
    "#zx6%n*&EZK?2I@O7L<vP;I2w#yKC(rVE*t3UPI!B-=v^15@K3ok|d84=0@dgTZ)FG~J~wYatMMLN35K"
    "W$ZgR2_$!^uUq`}i%FPq=FRCWmo%7chD(+RfBTMVIFdl}4>tPjI;p{-2>av~l-ODB?6j|lT^q?krO|r6"
    "C`Qc3=%I&-a}2xQK@SX|u6(?uzvqOCv+kRhShwnMQ!~Z8OJTdV+X8$-*fnup2cdb{1*W_Am)AvW8&NE%"
    "+h|B=-IYD>vV?glLn2`+sI)sV-H;J)J-(j&Wuh27iDK}e926!VZ6Ufl?$6oC_;K>mb!!?<A3U<7D%_oO"
    "z4&!o3sbOA8htvPw`D&Vm)C6I?33el4w|<!2DypS#jvt&e_TL1IALTiRcnV8gJQ;wQ~R<zW!1H$0yh)3"
    "66M=vUZsd7uX}6&2B7n<@gldWkRPSn0i(2v)<jDd(kyW{B)5c@gN!&)F?p-0&rVHI8k8QEL&i*oPAzKS"
    "lIPs2nZ#pHrp0rbQ9Jb$#GnbG+BVKcnvOO?;oACVVWHg*zotL9r=sIu8OX8ByXV`jmDeERob6B)<5jWE"
    "opvJ-_T@x>N^+MK+(_AQdD8W0dVOJGX}HU-F=NkFn=B**NT0&irs=q(wdlkky}HmvhtuiB8zu$Rh<XDc"
    "{jr(R%fKN+z;+iYt}#czs4>O53>if$Qkr%P$HJ0bgjBR2AjaPN>pNozEfmy6WOQ+NT<GQ<=7Og?^J@Cp"
    "5gT`mh|a&>-npme>I>TEX2=+R`kHPStlA-hwCu@W;@>(bG+zYM5w2SDY>HU>a@5@{R-^AuWKRToT_@c0"
    "ctuyzss@Y@FJ8%F+?9Qn^W*{l)QPlR&f-nG$OMYe^L6NCR0$j$*GE%gP+8-6@^Bg7bxaWsq)Dc@=>W&F"
    "-jzI#|Cy8N*SdNAs^9HLk<aO9Wwu|n_1=D@^Y?M)KcoNt^P~O!^Yh1#aim|rjw8+Af3925>hJL_!OL{Z"
    "f8k`VmF54Hjgy%RCo}J~BpblY>(=~K>M_{uRli4k%k_`d2bdSFj`mWCfC;#LGQn^Qik1<LM;espW9_?u"
    "=yxL!7;-tW0zMcBY+gUZN+mMo!Mj1<M50t&uD_I=8vD@gG6kli(Ie$ibn;XDkPMT0_*nk!b$@UM;V@(;"
    "kcrJjLC*~$Le42TA+{7xLORD&Kf8Vzu2TSS9SBm+&zDd<@KI6eMN80oZ87?ST(~oYFiY&l0s5gjBwOt_"
    "t^sJkz@m750`gC-0s1=98x9t+M@q&gd{695BYh3;xp`~RqxF8%i`b0oLX-!_O53HUAkGuoPN8T%DLQXJ"
    "jIEtM1Br8v<B1-Wa}YB<IL@}P+#?VQFO0W*#)@zzpHG!LT5Po56&K`q<bC*%+B+q~YQ?px4o`k=L1ATA"
    "^%)4T!wViR5EXO<5-6+v3(-J(dLXqs4%7=Rj&n+%c%<M;LahMBO*TPRPHcU!8*QgA1GY6{vnSq&1v$4D"
    "=J;Y{wn~!vvRdxRcam;`CWw&tJ{DU*0aQ~snmy!Gxv{!L{{2VB)^IdWdfh10@nHA(DypxaAAor05NDsx"
    "yjXun2`MY6cu7IbtRGPyBg25SkG^;FAO#+Tg=McsNN%Gk0o&>X_*!OTkdf#SMwweS!l)T`BZvGoxE$ZF"
    "&<N)TX-wA{d&LfCB+THB$kE81K2+f9yiZ_pwgBW+4^J<t@=-A8tPfBl@t?FUj*;ib2WVz-X7Cf~E*f9X"
    "nXkaNOOz^<$agyT($+k_kgxao#cgcu9%lfX@fh~7o3t%k>zwpx=qpsmG4-)Fb7=2w?M_KkNrdp1)%Bil"
    "chjKPm*A(iI`+O&%38E+kIkrTD@2Br!eh|le6@5&WNZ72=^^ZOW2Igiy7ppP<tw|b?Qu7L6K53tfRJxO"
    "bx|U;j1(ij_ByQ?<}}CYZsXaIl^dA*{*gMdOTJr-?K;CU+OKILPK1AVTQc055^-YZzOb=eC8rc!zf}#)"
    "fsCg$Cy0vrud0Mba0hwvtH_*WnP_0I(L&-<hPju|AUwL)lx+G<=~Vrb!0O|R#HzSOG~_Obh7M@&pgb7E"
    "?zocfA$^hd1}l8+EoV@E+PYpVd_mhiCWZ4Az7L74x8s=^NBw`yEw+;MybIvTkmD+%B&YwYyUoGL@hj1$"
    "|4kxU?RwQNAq_^kZH41+4z$T(P;XKUu8C(~yvG;hUn2=f^A+B$b1O+McYCwLgvOo1kk)SR=0rbgLpb-n"
    "?sVgg?J0!b2%tNIM#&K_)joJ`*RW&1fEBgnZHHtLTN8IS>?a^m>%41?S8~gQfR1II*QZlp#p1B6y(yxi"
    "^!(cp<`ryiwO|lx(#4;dT&rXwog5H-8#M4o4O`bltj&PD%lcfPRu^(FK@iYM4c8x_;0D^&s8?yXVVM{W"
    "B;x`F$43;K<O-E8LXw^ZpSIU3FGop;KtE8fD9NcIqt9yxm2}oTXhhp^sI3l~;$YDC$C#!5bgFBLN(0^5"
    "w)H#X!b0O+`wfW_;Izf9vpStrQdquiX@p%RX$xtzMmV`R*ld6>j7CfFdc($-iGbIXqmWnxiEXuypX)qO"
    "|7itKE2$C~fPKx3GO_~3Gl$DO+(|!;ovzG~%8XL6+QU4cY_@W-O^XiK>XB@7<awj(kPZa_UfGv<V~@Fh"
    "ebv%l&LH0wD)~AFtGLV0b;Z#Ia;93Za7M@<ds;=zD}dM$acLpx`Ct1P<Z8v;$2cct1o>9mJ|2})_2nbq"
    "S5c4a!PZ#S`c;>k9o|JXfV2rKMI_`C_)6?xE8biX@|L-;hRKGBxBVL_Sj~dpgw^Ic46SQ}0)T3Sf<-pk"
    "xZ?upwO9l@Cn5tD$FF}Vd*R#YoV$g}z+poGaqV65Iv0X^zC9JkiISA2hKU2&`yV7L1I2Fl19R1yFxXUu"
    "fy)-DMP(TQu=VwHbM1H9qW&0Ry5}0q5_wz9Ay{Is4|nDWBwvRghYxk<IYZn)pfr0E2wkdqZke2FLloOM"
    "<Dst3mEuJ^H`kAt2)S~ESR^0>Nioz*E@{wiGZ0av&K>o1I((?*a99vAvj(^wmdcCgZB&~Op2XZum|NdX"
    "fEZ;f${GwUUOn^668$yN%BaI>0si&L(3UsrJ`$RazD*gfF*w`ZX^wsrlB%~zDc|CNm_B+988Q;!3HJj("
    "t3<2oXO_(YB;6(PQrCx&2#B7#Nv-y3R?|5Oasu8<VN2cL$)d*O*LDr%Lu>5bifJd1BUDl@k)yPrNY@^P"
    "Jw+mXrXWTwKV<{-?phMIhyEm066Y6SQwQGA7xwfkC2L*X-@v`{G8B70!+xOy`LauARW9r8QDK8U70_kE"
    "GXMc|UQ6fl`Bh!h!eXNnkO%ys6fez{TcG!G`#tFqYev;AqDfmTTLP%dLg@$3ri0Mg33Zm@{%m9pXIIr!"
    "V0zW7c={fn5lWxenwgx;&X+rMiwr!(&Mqc*Ms58ljmd6Yc>CUtBU1d{NDDdQf16J^C?Gd2)K1BZ5gHsZ"
    ";m1M@<U|UeOVs&_Cu<j<ixQ)xlAd}j>WFKhrirBlG(|2}^?$@5qMhv6l)CCyA^oizN_+=?iYnb*$D6B%"
    "l%v@b88$@P4d_IjyN>y3eiExx$lDhXS73PTwK@IBG;^EFV`a_MB+)MGy-e<JC^6x%AB^qIphP*}Wu0&_"
    "85K>xv+@=aTwI0Z+0@M)1^X&80Vpc%1RDr|KV=@Ii`X)hC>aw(-JlxtYAgV@eV4O)j4eQ*Sv<OmyRR*p"
    "6Zfv7DxR`rp0BUKP6we_QGc`_37OPEtFb3#bovtsK3C)VjhgkBH>>G&R?Mm7AfjNDtVP3H?@Vq<IBi-B"
    "8+hzdx`}Z<=s7x(S4f5-KlJSRf97g_{P@-X{3*ZN@we5V?eEX}_nMP_|C;$nne+GW<M*Gxzpo$oXSQnr"
    "`29Ei{BvC6%ir<q@2_js|HsvshWT&h^=JDiuRqtkGGy-6qO#+z_^2iSC$dHn8Uyw6cxc$jGrCFMBIp{S"
    "PY()v_EaH8TI1ve&5x;2Ugo=9Wq0xBL$p|G7FZ*fEj`jH*F=T88x<|#St4%Jho<wvKr?h0Q$JpHgki1c"
    "BU^(NsQH>8e0p&Ayp>P-b~IilQ<qrEem-4f9K4zer$3`p`93eSn}ysUhS)f_=W93!ZPz^Fthr(P<>y^F"
    "yzXU8?6yKZT<lErvk?AHZ)YJR@*z=;ZWHRqq~DNz^SNk+naz#qs+$vyx<<KtMUO$D2~2Q3lj_`#Cv%aW"
    "D0EEK<`v;1=^;_8rdTey9a^nB7}BFrN|cl)S1a~YZl6pgCi&}g65z$@k)uGF#}ie9B}^0)GSTG7-6u~K"
    "i8+$Kh_xhUw>}d!)2=N1peSd`!+Tr^MJ<djSs{!L?|<^lXu%$YWVU!wG-qgNdmw6(=Frajdft(M|H0w&"
    "oyo}I1`&8HEdIS`PR#(dp-Sij`OGgXk$v^?%*6kd`w8FEdWhGVw{zybSDiboDc{ZGANgeCpUdF>RR6)A"
    "@kOm{XkYtk+DI-=V^L`9FG+T&+}#f!SD@UnTrB|q<NvhHR9MCJEF6XL*WJKO3G4`Iv}rfE+T_#U_Jq08"
    "O6N@#MLW#=D2Rz@l5u}rF3?`oTKwxv_NhZZ_IT|=ECQ=uF1NRTVL7tf>M}@@%7ojc<%3Qax40x-6U}z!"
    ";3_ojU<J%J=hv1mZU}&|@M0XjF1DEhGmvqDOc<=ym(5?NJ8W<zwJp2BK{?!v6xsXOoW+{-4~)Dg$LQY$"
    "&;*aHr^gbVA-;Mk#NY*RdM^i$ytovhaE=K4_<;XfTsYNX07z&sw?EaPBhXJf)2gkZ>8Rk{twExChCW&_"
    "o($i3Hw^Li?OEN?qH!a{g%4CX4SZizm|I`B>cqyRTvtZHFMuIdvdl=GYOm!-HM}qyhN-wuJ<!YZfwu`y"
    "yj=m4LW(Fs_^w5?9gJKSOirDqH$u5S3KUC=mz6`?a1j4$faJc^+gLP$8q6+hnfofxFk{qgGhi|%`|fos"
    "#3UgZ^hO9?fx*+jzufhcE~3iy#jn&HuC@ZXDd<k(?o%vrjsBw*aF$7#He~yI&@^TzU!NbTcbwi!wq-%i"
    "3<E;EjjJKVsf^lUPSeFT0>oC8kxD3DXLN>ZSUErH<L%yQPONI~{%ChU(fCM=A})&J1>pyspb}W)HGHl?"
    "ui8P-jV|$l^{*8^kH|sC)9IM^x*zfFN_Mjr)!5s+Sz9i##_FJhw-cw@xPOSsGu?U{aRB(p;}@BC+EaTx"
    "z-zt{Ppw^M2d1>^FF40N3DMZT1E~8=0@_i2I6Y~*LnUG!SX4*Av<HQ_T3pInqp4asLy^HsMPk^RdP`JR"
    "v+f>>LrjVkV;cMC=SmnIO71(+beC;~*}_1f2y-}g4>jUxe_25_rE+Air!*hn64DT=yu7(ZdQq_OqWMuz"
    "Rkkxjkx?JD;>DM?@VI#;UZ&2*T<ld;S53zP#Iq7Wt-Zqu3LJV1n~nNN+g)P0J|RLzDFM!4z~DSC8`00M"
    "X<IH8<Cihvg$K!F1dwyt@L%h$C7r57luhH}xYbrvhKLuA1bQlfDoAM;ig<mdwKkTA4wJa?TR!%T6tCR{"
    "hAGcEK-BRH<0_|1*wYF&YFlBlseV7Sjw!}iK?iwz1oWKfY}*f~U;&IsI*+k4^}RY~g6t%t*3BV5TKt>J"
    "Gge5L8>|KLboQ-57PF|!O5v5(b|<ZlDasi6v7@X&@XSO?@yd3a(#FfVSMylQqRew+Is@;7G}eKQ9tW)s"
    "J1?HY-UJ6D%+^)!<kPQX4tz6+G$U$e=e)<KyunpW8t-wpyrWcTx2<N~aNPhu&E`;tEDRdcgvk1emV3R<"
    "iB}_?$6a>pF^325{Ky4W{N?pAu?$SM{1#$>&7CNH^hre~f^Bl7rUZRs8-mLbkxpdmTtD&JV`N_7eq(c}"
    "yM>-i!gAh~KGGDr9t{q;r>zXgAxTCzS$>mi7s6DtnQ&-(ujvk3X%zW#{Um!ncDC>x{TU(=3eGdFZ_*OU"
    "IwA+u+|tfe_ke8Yh=w=aFwVUCoc-Jt-^a@j2?v(qwvuGs;CWhl-q&6oAwI$-^`3*!H0HE&(-_PCt(ETj"
    "5jw$XNzm8|>MA^xt5C}hg;HmV)YUyG<b9iVIb1=@-C4YRycV(wvq^U<yt1GA198wogVp39(u|_MVEl2$"
    "sUT2&zP|bTDptkdtY?Xa?~@0j*gUb`hf~}}H_+ZFO!4cGP1CQoBOVtV40=3fO<|#MbZ*@gA~482DM(Z4"
    "OeBlU3|e)Q(lP`iZj~B%VB$jWGf1C2oE>^ClpnVNjfla@j3lbq`wY6j*OZZMHo6mSUi$O`f3COBlb&Nc"
    "H^wy?TESbPw>{MIVY(6ty-tlv{wuNyB@ajFsqt87W|s@3j6M5LJT{|9Bb`xXGmlY}=B^8Jb;g{SYuz&#"
    "f7{Vn)Xyz_^ZcqU(rbhkyg(wzSe7Pz2D?M_oc6lA6=+fhTxn1iL+N2)4>moWl&5z`)CQ;V#08_q?chVN"
    "4wk{hfNq%Jmull>LdLyJCKF4TK)B96r9`PJT}YR12xvSnVy|o$8<GX;Un(X+X(fuF$u#&xn;cabZ9!})"
    "QWb54><8Fz)}lSEO0Fx)K7SuITFKpK<ea=-wwtHE$U(FMe2OM|`S2{vZh}^GT?faL<jYaR^;{~|Zty|Q"
    "{Z5wV?+r{hRU-qyj5A3`U3k>poh~}YahqSJ8VbawU5mIFMc=2oNIqM~MUDD}<5>}32SnS6VpUpIT}LaN"
    "0fiDnLWx8Ia~X@sP!VzY%>Q$>O#ab-_c>eb<M+=W*KGSYi^3n}XDR9DwW9y|ef+3@B<#OdwfW<hni;O;"
    "tNi$ze~mxC|4}t&Vg6gS%u(9^8!K0Hef=ftEJqljoK>vW25!!$=Jf7uNha$IM)`n$Cni;*&MJLAOvE23"
    "c{fL|yL5IfWc9J&8}S9Ikijb@l;EMmqxy)7-jk(8oA`gQJwzQELq+v`^!a6_3#!xc%Q%y3pN{}O<*pJ-"
    "DJsw0@>5Gq3PDEir~m*u=2IPq6d{qG=0f#c&-uVx0J9x#V+mE~c|L~4Q7VHUM9hx;bE7{M15HQC7DRO{"
    "6HlRN*LbF#N=T;ba!4YbPo@m})ln7-Np)XGdgN=|gvJI%0;V&vo)W)a!;N>WNUAK!eLN<eMH9B|+&T!I"
    "5A;fPyZ~A}TYI$aT$9HW9U|sI+5=<IDLpVD-HGm+K!+nPZGL}9FMCgX1Tu9{byg2{s`G(zC=ou>U|70}"
    "`m&bgC&tDyZ3&TdjKG+dA8z-xVPOy|CR!3I=={VLC4HySI1!a}Ybg}V_|zJeC4$BxG##XU%86IX|Lv`D"
    "N2i3sk@#OWWF4CY<Fw1cciJSJICs|Bf9RCSU#!7)I&n6O8+Po8U0W{>H*}*%?GFv~h_2_qkhM=!%h%uf"
    "Y*KNW(_M)H*ZW>;T-+264P)&8gRP2GsPWogg*#fT+ER1ok8fU_|52j$p#jXT0#>pz%3V@SoYz_rAJrA4"
    "4kRdv{D0VLwiw`mbLsNI(Lt+qn!5)@NWC1nqE2#KE9x;eQF8x4%M60+!dBz*uNAxOhNkZJjGzZy9ku$q"
    "N~qUcD1XBf(mzOtZ*@2Go3&=Q)tq;l&A%3xwjK9Rn3={GX!OXsQlxF!Gj76g>9$@btT+p5fI~$Lr3=;5"
    ")@(@<oBz_T%^%-l-)y`I9?k_d%28fJb9@io4v4wGKme|2N{_^N@w4LD050qL-V9R8a*&>7vl|Wk8XY=}"
    "!=qlYWoSPg@Xp$<4)PX!*D9AK-7uX|AYS5>e>zWRs~x5zCPf)<z~b^`?67SKmAaGhm2Ud7!*W%n!rSD8"
    "MF5?(#!svX=>sR4FSqeDC$#BqBbr!4R7!-~-7dJ$Web+ut246M9Y@7u&#>`zq1S0g5eOyKrd>xar{z+v"
    "(Sq}SgHF30bS(Ms)0|K{Uuzx$jnD8alGz)+lHznHVxqPx3+t}D!`8?jArr@mnOj>njuNtD(dX(&c5W6d"
    "T~%nR77--)@OIkGJ)}`JQ1A9**on0s;vCUXp^ctH%{-!rI3(QPo_4Pf>J&QYcy`SAbb!^8nplX=A<(8q"
    "V4<-7{+W(wf&;?pOVU@0mx$H*;?_SsvfVvBo+JAB;F+?6r>h=l{lU|fS;w)p%OY}eI_Zr!@`zk>`MG5("
    "P~9!Z+ckBa?lae6Bg1#BT=OBp_G<*2F$j9nd|vw8!-Npc3-WZ`y5rtt)z}h6j$r;=E1p72o}9d^`>=i1"
    "S3bYpoa4(~#qe6zv^>mv97s{q4#WT5jZoj``CH?!&|<xA=Uw}fKf=2vIbcX}NEyQy=Z!?D{@nN03DxT`"
    "C^GC=>{i?yCrjlTkXvG(!1eTmNI36ap>hVJuRML|58Y=?oX1AM7sqOz-2gK{mtb05;9b)1h?B^;>Mp;5"
    "q+O9}w~f<~Q(%-B9Lyc-aFv&Z>3ZN=w=Dx~+U(ACK<wQ`9c#fk^v3C=L}w+CzAX4^ixPx(pW!UE4a>ZS"
    "a|qXLHfg1$&VwU@3zI$a^dtRVr42ld)rJb**Gx)`ACHwx%-*NsIVOszSI<+(Ut8LjeVll2A}HL)3Pqte"
    "c{K%8yHdoV06|x#zQbDlx!~7443kC%o~*koN6a8Kh~F(hfc{REw})+5fv-*P*vaqcVY{m!C`DIk7c^Es"
    "HfsutkXRf&@7LuYjH-|#3j^kLKmjV|^znIB|Gsx!k8{%+bh4@?)*TLxL_g6?ery*w*_4ZAL&gKL6J2()"
    "&RY!hB^YIp1OKNn@%}FOfbp%~eCJf7q<@?m-A1*_x-}}5sN2C&EyBK@2w`x5`Xc4GaX@raA;YJ{+D8G8"
    "77UV^)(e<0H3$c?wc}*5>SzGwmT@OBGXT#kGPsqt$+SKC+FDbkQzaS+BMqGqDaC2lIe=q+bO{zm8Ty|M"
    "mzEX*&bNJRyxjdN%blQNdmu#6ajGKLnd>yKOVE{@<c}c3TNotsYIFhZO{3f0B3iW@HBJ^qX!97oei~_-"
    "1@wZ%2Vt@Lj8x!kxaSzR7(MCv#Zi}3b}bo8#D;Ds@|gALeyA><$FRkhGf}-34SDH5Q8c`Ti9oiBN)er1"
    "#!jMwcB81CXshcTn-#SyueOEo%B)NDZ>0o7!*;{EAdSH)0zvV4N+Wh{WTORDlL{INH3X)WZ^$PxmM+`5"
    "`;V?MW&}<@knpU2hswDhPftmX<0QvZ5{a}%Y&%v|_y-Aj7$w{%ePYpJlgXQrNq%<4QXVN9N3Q>*A&YZK"
    "q6@67LEZ!t7S9jNv-BGwg$h#iGpfyE9v+Vhn|zmOLCUqXb)Uf6@>$>13#c+i>5gQ5VvSuo0j~e5YBdjX"
    "%>HcXEXq+Cr6QQRDxqi>$WkCD7P^6ZrT2S`6qiub)(<KMNUT(cEgD|zVHP-}!RT%I3w(j5kyLE#hzB4%"
    "NNpG3yw!PMoPc+T(jd{(x_1|o4~{8Yf`91Z*#SuxOXgm$EyN5h+wL}mpLfL<{)G`%KKECjVZq&FspK0g"
    ";qBv9*J=pcs#=vbPQ#rL=r`$zhM6FFE@O=%a5Ha>oB+KdLzF6iIF|7Ge0o*#WamETN9tKjPSDg`3R&AU"
    "PFs+kR?&e4RgsTaqVMZHt$`yPi6FtUoR^w>J!tn!!~Zr!mpaK|l808)YNcTrq0C{(URxx-FJ^d8dM1=#"
    "cx`q6BR})=$DiXzzRtW|e9ZCt@6Xm}|CQRW^ke?`@#oJq2h?BXR~~<R`Z?OKd0pY_0nY8$S$>}FTNRC|"
    "m;cs9bAEKuTzkiNeg-`g`l8b^Oj_5UDkchPZ*oScvl1!B@rhzPJ$>eg<*FDS9^5Y>746h>c{;0~WB_F}"
    "$V9wP6WClI<l@?U?fz`H$kxf<pB#-T)t2o9OoS3ZU3@_IsIzi}Xh>}J+@zvKx%2p3n=96U{D53H7|l7X"
    "4oT)9>r?TMqzww79OSMYE>VB1wQo1^3M(LO@;IL@Ng?>TR#m<8HMW*dipDl|ot&=KU`DOeCqvVVv*p;{"
    "le~%76@79Bk&umEMR95@f#nga_n=XyD+k#C*1`TOaQD@0)!=NSUGf@!+k<1IOwaa+lZ!Is^7-Hbsq`u4"
    "<oOFNq@b{Q%*W_6VjhuzvOJE5Y(4Mb(sQC6KfIl_2ZH8QyC<jJf*gs!!1~F%M1QOxSdP|(3h3S+i)aui"
    "9vY!FUbw#P!4h?C-Gte=9|;}P;hy3Lf0r0YP2VDD3^R$Cf9T**g(O`|9K@ZIrPPj^|8GytJHpj<e|yv@"
    "Y#=)&E$OQZCU4<qt~YtNudK7ZyW*SOrGE6UIQUGbBOwP*$!8J1?+yqdG)6pDjv`y--~JWf?4QC4W<axD"
    "JDiZz_6Ydb#0nZWw=~sT=USZ|)qG9%&nm8{ZIvhglHd+Pq!2cLRJqT?GU#d*O?F4?Sdo5iS4i|Z1k*jT"
    "b??}P0I5N`(IV1>Fj97!0Hjavf$KUz&GWzNgVQJL@AJF9eu+Yh@Df;p``XUTB`RF#D4AjXFxj^icu<61"
    "<4^S4crenQmagm_9k}#*DqO+obgTD6zarD@MTpBQt$`QXPBW2z=S_~J^+INXCQ5uyifY=PTbJD18cj}t"
    "arNd<{j^urw0MUcn3N6KZ3YZIS(V2vAED!?9QPw~s+2VVZroi+b2EMG%+JJ`QgpRbM_$gY5kUbj$zfN+"
    "Vzv}*<BJ3!9aeq&?&v@=ky?crZON}{4q!9#m!pTLZ5_WvMU&=+*|fW7+@->0Eh(vACBT*b7!3711$hl)"
    "M})4wHDJsVMc2y;+YZNmwJ_~*_Wa;d#Fri<x!R&uqgoqRds<VY1#S!KPG&Z2KF9&aEt}AEf`5sg4hNeR"
    "z`?YzNDc;5NipTyWUO*gwj^v_folD=Tk62Z#zx;^BA^i?#Z7Sp4(AJ(aeVus=E2CIc7IQ~U5~3{@orQy"
    "_ka|Ymtkw&p>QZsf{gEjGjk5f{^ohG#w_71K*dzKHb@!kX7ZI&U|2Wo1g&b1!>T+E?6x@5O-w}fvN7rg"
    "J5l*lA~6vCW<soEz9jKGzdyUvfhM4FSdnirG5^#;NT^}L*>xohM9qNd>Qavmo*vZ|*<-c->rSVYo2_C_"
    "?sxXNLmJm)1{9Z3)lHLO@F<dwQ>yWOA;_<GFV~c4_}xLp_uhW4BQ0Jdn4ZiH#-hA6h(K%b2`KeK+ieaF"
    "Mk24QNs9>JqlK*m+7mmnqu~}Cng>ZYeK+gSePNK`F6U}}$_fQ1_(~FBVz`S1a{C32UN)nqDeNzrz}jJY"
    "=KEDU@N?Aey^!cZ0r#zM(5b@X@{Csi`BsXYEpLBgUqw^7#lLlgs{>n!NR+&}loQNq3nt&m9U0k88oPZz"
    "`4sj7Y2{c?E;<m^**^TD4Ar%|Wr0spBk`%NbaBQ;2~3!RC%Ef?%DL@LmC#FZY1a7q-GnjN;L*rucj^|F"
    "DC}c;eMa8aP15w$z3c=%Mn4^`b#w9-r`er1MH_|o4Gv7r&AscO7&>nGhbm6qVp+WMj5cyO@GvSp4wv-^"
    "$B>AjEvE<WO>+_%!d1F<U)9O1L=}D%E0D?r|0v~{t_oUDft{^<B!HrUI5^3q?sW>3sH`fRBYaDzPoS7c"
    "WNB%UZ?>FOtErme3J+;9^uI_n?~2=X)2S~<CY;!Zh(ql0T4|Hs>NT({A_@p|q;hE(1~xN>EobzZ-R-tT"
    "noSp?EqlEwaA+ekNlXfRlU}2-E!`uS0K62&&naF-Mk<L~+a3U$?#V#&B3gFV>viQ(tb{wblMP@>O%nf#"
    "@~$oDmmYz)Ab9}426=^1Ygm_`S2jby8UZPUKM8X1^K){V6C}DP1~#~+BX}c_OYh9n@ojBqBHh+Xz*H>D"
    "HIh#IqLsV`qkLPC!gC?<E_sJqROYz{c)~UdG1SYc*Gid(Ba+B<BiE}f?#)sjz1c^G_!z|%qHB}+o9b$Z"
    "fn%yFQMlvk<YpyT-E#aB_fOjMkp}G#)In7o5MvFcCHX{`j*<W*M3l?3Im^?w3rsZ2OX;aMK50kM@6-F%"
    "`-k`Sgo&D1wUmw{aZ9%A%d+UcHdN^rQ6iN2&`EY1!Rz`e6DoEEiyikhn;t3tyjZ7EywG2J3w>c@W3-A*"
    "bVL*0U2~Oko#_UkMbTRW1xhD9R{6Zccl0R8y*Jh~!wGbFbV8kqYn?J@tn3Wf1Lh<x!C~Ulb>;HlDFT)&"
    "H7axxduBP(o=xU;jSVbCnHC;kIv0{!Mc(_Kg84!x?nF5zRXq%V2{S>TAL%aW*01U0lw=^&O{HkO(@y;@"
    "dG#Q494C17+Y7|5j+Z;HtZ&f8DPytXZ?$pa1&^0PJI9t`Ky8d$>`(F%->1$^de(zsTx(8?b34W45jl<M"
    "%^MV}?plcs5p#V*JtGv@L}_&cgyiolJhblxI5?YB98E-?c0LCZlNnHs6}cu@79y5oCl1Q%^8@_hkR4l3"
    "t!sRcjWE#4+;hO@(fme;_1dMR>Z%elAqUOyJTR=z?%=D+N7)>`i6%WA;M6=ArOp_a&7!PZXt93|9d|Z|"
    "?!q`&0b2l$v6bhj!s2@Q@lh$N^Lkk&?I7WW;`rP*I#xisz|EJ|96{dofEGpo<!Q5i;7~b2T=j|q#x(PR"
    "FCo%fzU1K0QRZ=<KN^8_Jl;-IQt<Y=w{=}5vsdD5MV(Ff&z2)f94*bdd8#>&!yEAfmA%e#0R2Rro#*+#"
    "azX9)QUCt<{UiN6=dbi5<=;p9)8?OY{%t>hsw-`Dxn+K)`Lm}#zsBG3_x$~9o`1*B_A`xd6*%YrRDm=1"
    "3Y=?2{!Rt)%tQ0C4NS(Frx+;8&oo{SZvSwf*25o@e^5lZ&}9|e)CU&BncmmC({gauDL;}Jm3hzHdA(WX"
    "G#*;p;X_mJHX~mXVe>)$!%M;K=1nK0(u>7|KcXckfNOo1aN@b7UP7D^^=;G_rYFq5@!s%K4`fk3IX`7+"
    "74bmbw&&@n%Ll^YI>g;-H6|EYn95_=)}UfT@W-GPlm)fb|K!w}*yT!OwvNvrH0dcp4$l?|%_0h}DgP;m"
    "j{~E)6AhcWVR1{3*=i8P48O?(I%z`>9HK;|K18;7$8&8@T}&E|NL?ZLC$UR^R@;cpWf)9$)JOm=bLp9$"
    "h?dOIo;ed}DLEeE-|&IwNe+kiU~j1pMN3+6$bXeE0HUEY>OK8Ybe@VJ!Ft}M;d$b~cxhle;Wb2fv*G3k"
    "R<w}5T^dyhTB`Fn_SlLqb><<v&dIZkcTx{ZZcmRe6+n|SQga`x+-9}b@qe>Hjk<ObLe;*3*VypBWSm}S"
    "MM9{`)@eR~%4xgL9|Xuv#oS%V{p09IrK#<20Oe^bQn}N_Xhrxa+bQOv`p4h+&PApB67AA{DsAtGHGETJ"
    "VM5EDU<I^+y{0=7YA1mRrE(un->y&o?pNX>^^XSQlSnK35UfNdr0@Gj!R`S%)l9RHG4omnpc$~WY%&ri"
    "<(&*_K?donIVt)hAd41S`(c7<U?5+1ltkKm{<0bUBZJaM<j_q9-By~L6DhmfVIhOcO|D&2*>>Bm`9Z>C"
    "W^Bi5y~mo8<;O)}x&Sv(V#`IS2+55BO_;ki8l8BDZ0nOlaCYOsdG};z1N+qxKxx-k_F;TF`KxKDj7zfO"
    "U8o6PHzRi1_veQ2jRmU5KmI94h@K<Z&a@$e*LNI;wf$~+?v(KK%@*y@0x5F3ANZ&wTH=>koq0dQXEGy$"
    "d`+5mN@Z|B&Rx-+7?>e9An-6rbp-9#f^_WRURW7Q@JCIL4x8#>(O7oK0e6zV>|D`9vmAo!{f3!#rJtC~"
    "zJWZ`kt(R<&RaMO3$==3Wh~YpRnashN5@A_)XG00_$~f25FQPJfJlIq7*!j25I{9vU}dGO(4?9VBEW+{"
    "DWa%yUONc0OXl3BL9Il4Imv_t{ah=7?)s^kZk}@*_FImM;p#+~#ll5O5iuuyugx_ueSnNH*!gf#wnl^s"
    "-^I9JiAcla^lEhzJL!^DC-~K1Ly(7$-HV5QZ}|Nw-z5c`DjmPYbO;(mgVnVGzvsoIRIt}d0iGRz0+&H)"
    "O$>!=?oG3Aiv)lD@LHWXx1RE_s|AadqPYg`!>*ff9*=IP^YiZ#3mENH4$9GW+_4|sef6e(Qhlv5YSMfB"
    "o@%N~_kSUFC2v#;ao|+?a6%(XN=Jn<^Jn`{iC!tWmngY8&iltM!+LgR0JxeC!LEKHYGimmURP!kH~Lrl"
    "i>I!jhSw+_7*_NVRDX*JC$P+(ue=lcJ-#{0spMQuKn}9fR~}L)6h*x|qK9QdDbQ{|S!*+su}~4ky1?Q;"
    "z~LfQYg^|2b=QylbrLVWaAoTU*C##QeRMjolGn}Bfpv4mI6uRAfkXqx44D^Ou^TnWQvQ*G=hKru4k671"
    "k}Nk`0!52(l(~bhQ!X*Be&@M2xw*$XIaZT9*Np!WoA&(?K5yHWcasLsif};f<7-1he~~7i;o+#EtJyY>"
    ")qy{qYNV%=OedrKNGVhRxPIF15;a?KCbb6`z?9CgJY)c|H4?Fu{g3rT!syXyCi*`5lO<pL7DK_{)FQBj"
    "!0t6*ku0Bs!M}<+n0#)6*cBDgKe!*8HO-cR*3O&KR!(EtLdP9&M@zbr9p07#Q<S7*&Z7Q4ErAdni%?hp"
    "gIhN!zg^2(J>BFe<b*+g3mZ=4Mx5ua?jakO{l5tWx34OHEbO<_M4nLK2GYSq-m&AR<uFVLQwjA8xl!Uf"
    ";DDOjKbG9X>KK%cb;BGG%CD@Fg=>S|hR~RW!Z_%NVI(31_-rB@+bl_TCm~ChG3w*mv7U;j0Sok|pfEsd"
    "z#Sx!t)pO<rnftf5oJEY;RN<y?C;tRdkpmifD-tjG57YZ>%uSh@g&XmE!FTfktXlJx~iz&SC@lZXK2%b"
    "d=Yqz7Dnsyxg84Jh#~zhbrzjP(ltSi)ctL3)<G6`AQ-()s;V_C&Jx`jpu=-Xgv+^`o6_}@LUxoUWzila"
    "mKTQK)8TiA!Qz+Gf>sl?vi}P05a9iU)QKA?!K3uOY?W<Vr~R&nk-4UM=jix)&y}OGz#d(cP+V#AxMqq#"
    "A`5aOMNx}5X`54($_hmNSLKZMyakb^gS<SUs|^N3m^!sBfV8&Xo?B=^iu9E)(M^em2uki;rd)^~nz;ES"
    "z}tyXBIYM4jn7T*P=ocdQe233?%w>$ZHBo%=8ALYP@!KV+VOJD4!dl{pVrI(?ZG4lGAu|7yKlckZV|}m"
    "zU5z`*6Gf)Vn#uMX~k71ePFCNkA#mRu?H)ToM_@ClC`{PODHEW#{OI)Tci^59N$>Csveb%|FLURHW^HG"
    "E&Mmh*5yUZLO1=iHp2W*RH=&rAFCbBkADUXi*b{ruY@7CiUEWA+8Wif7Sf_;=d?lGGKw=tJYD@Tt+LMz"
    "T@JmQGIqE?+IbFnt%n^g!p2NuM7$y|U9sD8g+DrUqI7V>(Ftt%@TVLF;N(Zz)-HwEncQYaK4{5fL9g|8"
    "c;ziQ?{>LrWL9hD;b89yU6w<bwWl^F@*u>Mn8Tq$aNOO#=N929mLqriyOQ0lbx=O*)^hr^k4=cvd@P@+"
    "1C-uak29i~=^NAjxyQzgn5FgZ5Rqv4kQ&}b-=iLfvE|bcI2D-He&$4r2^HycmCOxbD!Z3-XqS6}DvxFl"
    "q*ItTRYCO#b`5ko-{_k#`4<`5w6~>e!untNpR?BA*T3rDA3sX{`}<l#$MK_I$Iid~_wSs4Uc1im_fIN6"
    "|JEPr_wV%Mhum35FTZ}2{-^%_UaK?zd#%oO0{DMv<A2J+|CsinAZ0jrrf;6U`*`LslM$xvw^-ZqKo7LT"
    "L#4r?$z^@w8#rpuFnPVnlC95iZ5nJvtt0|0G_&{ggr!SghgMC4pw30-cnTzA_h5I&B+o8Yp7PbO&AC+1"
    "9zitZ_0bKaM=eJjCUo~xr;ll%aop80(SrL_JuhZmQO~2Higs=1Lxva4hYZhY6dx+uCldn?<SY}GvJ%Zc"
    "Z9b4T8M~=c4{PWboN@ZV1KBEY5*)707$o9&x-~8n&*VbpVus|=5fnaQM_RLOY<Z;r#EH%!negdii*tUo"
    "1WB7SKw-G<PM3VhY^xDG$GtY(DQNb1r2R7W!vkY+_m=bVA`p@`=XAoY1}8x5rvjoR9Yl#zyBz!W^=Q_o"
    "*gvCdU19v!)SyMF{s;2ZCUN<e^lUc#<qxk;>5iIU(`_VDx^Lt2b7~A6QgMg|@`NuHWq*2(ls-B=qK(7i"
    "JD#cjUra$Drr8z8D3QTWSCKt-l>V>SB}Jsuw{$ZTE;S;=UTF(%`{F{XtucGDG$aB~12xAlXWp!AN&@eH"
    "mo1s>2&)awqzA^4@U%P5?fSAisX%5@d^sIonX~ii#W5Mg^nqKXL}T}M20vdZ+&}NFh5lXs{S{=;9`=){"
    "md#;+GB71nVNn!!a^7+dGDuxfkP9DV5XT?cyG#a+#p7f$DE}jab_KUWsO_3?hmmKlJz2wXei3b_Rc1yJ"
    "&3f*`yVC#l#D9@N^#iYJK?Hqw1{KJlkKC34`Yo9zCPX08^<vrBl*um288T>zF&W|jD9*wv#UQsp=r*d1"
    "D2#f4NN#5|s1!SW_>$7T9&>H5q5rJ}8AN1NjxOZYaxE=UkU`@ssQeDYUum-%=8GE5DCg}7IyV`mMhF}-"
    "PAW@wR=Set`<Kl=f=)Fb!UhG#y%>uJMdZBVeAyXwOluEJoxugwZ$V}+6NYJz#hbUm>uqJSyBK`(TBz2;"
    "UlPIlcv<xCG`v-M+py8RebUn%c3Q(~c*#VUfr7kjH~dI69Ea0{gG?gMC$7`_-ecW6Xlfy6BSlD84gz`g"
    "KRJ0PWd7HaAd^bkBg|N2uDjNV{7=<gB<p%1O{LVUF9;{|a>7LNSjC1>>iJF%MJLGxTM&h=3-U8rg)1nR"
    "d&mtdmbTl`ki4N{vSW=eBi-1BQ@ilV1}`GRjV2J%y)`pr|L^6CCnW^P&XK&nnFyXZ8al!_2fl1I+5!<*"
    "f5z}DVIMfC*68irAH}eTx>bbw4`+JG6}a-mFa_iRWivv#-#LMYV`IL*T9wi!Z5yu6$~a0(-dm;g+BNfo"
    "f&zoSsvm?!iV`BinZm0h4nogrUMqv$H0=kn;!^@|NRFL9H$gP7p@|w(H}5+qjv(*_Ig3XYVIv4{dXaRs"
    "H_P;|+v$3(RBfM%c8{^v1!Y7|oDKzE<Yp?Fyp%Np3OfnA_6*$HbV>4>yhaul2hwR@QB;pku}bH`jxA(i"
    "3;f95?=6cxoOg$P8*l6yW7a&6dw6H}#tT$!ANsB+5#>^Xa;Ov~g&E28?CwTt(Y)E2O~@}hqOiU6kI~_b"
    "g8J+!rnzm5o89wP2&EOG0AQRf8@eQbg3^!YW3NuizH(7dqP81e675bk??GE{uPU#Kl$*1cmGDza_?2mQ"
    "X$YU-t5WVXZ&8koqP80-`<Zk(j)OPJx7((B9bR>?=5(rxlI|660!*%IX6+~4;)V0R(1N~5INMg-ZoEV*"
    "eu;24eF$MXWv#9t%!K8?8c62}?HG7oYcjhq{s6776~z?ju#ttr+z(rjB;27BkqXm74on*gRooLKoiNJN"
    "-(zm@GDMp8s#l6gctVTnSpt-1?Nqc(T9Z4-8PhV^c>6H_Xe+qKmhXqX)87s%QY|c<SrFpVI{$Mo69^w}"
    "R6J`i7P!UCx7};U5aCLo6YC^j6NGxv)<vGsX%ChDfZ%%^9LFX=cO5Uh-gSxQboy6z4{XwFS^LHsI&{EA"
    "ewC41yw*VKvFZb$M+ONlI#X1xBZi?>S;@uHMW1{xrf;lv%1<v&_FGU{W$6wF`85RGUIS1?W>(d0%BOgb"
    "n(Gobn&ef0r`K4!Ep!~1HqklI%JL9Vb*qJtfDg>Xdg6~xMxSkbQ(N9T)*&2DokR%On`x86Q4Es_3}4A)"
    "E&OLlhGbC{i2*01)4<v;slr~iW|sxIEa%kcI-RQE^vSx~TuD1o)E7}yj_}}&!F#YO7=+Xp>Oe^1Z7!r9"
    "Hs}a{`LG2|+rhNnCe0CAOogwz6>F|qc-A-0RU#TsziHrdB*2ckqEpe1qc#iDbY#O&Lzql<X>VSO?6RRw"
    "I)}2$Maf`?%UK;DV@p|^QHtYK?CE@lcc4fgWfIYa;;<<P#As5EN0^<gAL}!0XEW?KRyffwZr5rvqEqzD"
    "l&x;&h4eY=*R$*rk4OrR)$!M8&~{F!#?aXuJ?!E$8-*y9$P1iF*G#0%=y~Qx>l|UFsQIwAazbI57pU28"
    "LSO1^M;PMDS|;F%g*M##(%?)Fz}gIndMjf;K3xZS^(b{0?F~0QHqYj3ZJm>j*h%{!%@3l8I75_3>xYpu"
    "<8X8-s%0Q}4y7m?Wd+Q2{bwpY4xKg{ogZ?9FTI0gIq6m2v?0!2b=>K6H78{l0^?l2*giamS{K-(q}orK"
    "ovfLG*IWx7At~RgIVdRDtGabqY0_|^YNwrN8R<HTUo+c?b8#1T?2rgP(Rbvngj5<S@@^G-c>;@6YvKDI"
    "4?q!@_6h09GzYdjxY;-{3cNKtzv$J-O0bk(o^!aa!s)pI@S)|cE~w>@ymzFA!u(TI=wV4>T>oH&SSn>A"
    "l8YLd6N%Fb-a;3(O27#Kuj#I`%Nk_D6$Htp^T=GH&gzImldHg!o}!6it~m{av&?$nN+-egatoXUOHUE$"
    "Xf98**;IAZ|CJUx{^Vb&{2bSsGJgIoKY#UKIsL6Y*S~+ypTFv_v;F>cz3ab!T(91>ouxm&evTjG$DGHt"
    "+x*DiBI00t{%eI#D<2g;b>W4i1e)+Ia}fGk(jy)W)Td)!j~uk8c&IKvfSRXU)WqR+eaJuq2nc;4glnq#"
    "Iq%Biyhi`9u=WQcisQe-OP#u&o=BPO=2w|I&;>MdJJUlVmU@}&7jj;2OK}Q#@`?1<3D7x<lP}MwpVy*d"
    "v$|-{ouN;rAO#I6AV90=;2`r<JChrcj<)a9{hQ9mxG?=)5*DvN$B8+N+z(_K(QqmRga~7T{Ol}}0@3jr"
    "IofPB$g6|u;gPA9W4^TT5#{+_<-hl*q}eMSyt-uu{8+~my@Y<rM^|<T)`i+WNr|GgRvg$W7}IsvsFWXK"
    "02v`Nl(k(>3U{mRF~*LVo=TmQ4G#~^IKwOI0S2YTyIE5DSc!F_-_&WB5Kc~AsXftPNo%Y^;d-M<RBvl~"
    "VC#5kc)$c@@U^R@5f8Q?dO8blYtf*Wr}zEmq`v{^(<*TxvaaPbKikVh2ch8P4rJM#YkLeY+|FI0#ePSC"
    "S9#Sv>aD-RY@#lbEhKJG`5|M*hc(9yHs3?y9*j9wdrHbPoYj%?p1qb0kV})3(S@goc3L?QXD^*!zjFC0"
    "IsUJQQD~2<DuG52BjfW+*l*q|wqGdo1Y>9cb*;-@qH3Vs)%5ejtt9BKLon#_?KQD)OQN{q-5ao}n7lp4"
    "X0Ygd?%^kC`yZ?H07Zsa1baDWZoPD_yNLig*RpJWZqUviUX*ORRJ9PfuX9LPsZ_^FWX<&)GAu2$v20E#"
    "Vg(WtUiI4IvBI1KWN$=#_AUQhOZB|X3>tE#d!P9XW%UW6ArIu*H359(zUM5AVFbCRJILJp+Int@Dw+Bf"
    "o%n|Hm>b`r@m3fb^*z_CXeUEnb+p1eI4-?zls!?1z8SKU%Xx(0R}8t1Jj%xP7WK7??Gj2=9wSt2$IgQ~"
    "r>Nb6KSsI|6*S&8cUnP5#>kTig=iztH08Z5UayTt%JW5>^AKlou8E#vY8p1BTEm)Gw@_)&LV{>$_R>+w"
    "2;)E+w>&L$-nJNC30QRY@YeEclP3%UD@vr&9VYWudmQG5Hewy9Q5>bMee6Y;FH%irK*^?QkPw!!*HP>E"
    "!Zy+({2r~i@shqjV|Z1PRbeDI_R}dHE6`=$n2a))Gh4F>^6;5~#(ok7>S9Wj@!|Tcg#@?IsMB)-p_yEj"
    "gSciH2;a?2SBp1DKsS%xN5NDhwvS^|ro~Bh;5%Y+w?*hE3`gO}Gmd+8>i|~GsU?iXp%B%~j(*YDHH@g_"
    "-8E^sTMOgfqE9OKi+{ex&D|Bt1?JX}t#gp3l1f&T3poZ9{Z@PA#t5_=#9JL-dranPrPcolv2fgJiG^%b"
    "NTjvr6->;2N>`dqw^EIb63*xd-i}gwCAY@L%6YCt0sNz99iaxNJ5Lx>mx)-=kxLs+r_WXTNSsNKSH!(Q"
    "wx3Rvb5eAy+ii>CQcd(3iUPd8tw-<j+D9r1G8^andPmR&Xi8cI>nJ9wS7?43)e5}t79^cpXCuiX!;$6!"
    "1|(%GmObvx&|0_8JFm#wv}<2T;HwKZDR58)7Zf5#u%bqFUFNb{pOP~biSDgF1`}I?lYX!DaTZ%N+05v9"
    "!=sBBYFns|poKGnbexvs&ezis`&biGsI4;3R<wKFE5AgDbs23D_QQ>F`Ly*&2;Zx76vwd^-_@_)KKqU$"
    "=s-D;wUm$eT%HI{D#<NMIMiz0(k1hVvCqvBC87`olH1v|1>uNj%I@*eenNYe#&#NONBS^U>8cS0UFq?1"
    "KR1=>j2$}@LyJ*V;8=0jJ?APRdRG9bbR^ljVvc)8EotjM%C3E?;O5=!5?w;+>?7uyqEXr0L{EornP84{"
    "^gBi@Z|p60zD9S5(0{Z9qOTR=_x<BSVU@4+zUeB?xA-=0QCdAkjos0vL&C#2A=y5weC`!R9_oD}O;eGF"
    "noJ9RGigJ&kR*=d3`Nt_f6$4WSy@*=9IOyl<!u>&LsC)~K)T#6cPg#*r)90?350%FEtQ8uFAI62<a@9R"
    "R>x;44rCi=K&DApfv<8YhcHd;MavL3ZUH^Y^S7#Kn_CVAQNZV}8uBw@u3KaXb~Qa9%&8=;e(z4SF|pY|"
    "Mtc@jC&Tk#-kb=O@Da4{-VqN)DDxH9vGQmNv`amrcX8E_g;qH_CbzSFe>A{|&DIxS%YsDwbRE!K{ffdC"
    "(+O+j(x-?QcX5^dO?&1wEya~Z3l=n6BhoD8iWcT?FMvqa>Z1X@&euQGp~~f|U%(^GLnC&6;@SFjUx-b*"
    "9^p!4-?EG`3Tq}zksq5#!_yLej_r~klrw>_8jHq_HQWNdicH_ceQIkJvjY#<jv$QE;E1pi4`~ppU`Kg1"
    "Lqla`%SXVml)QXTHI{qXL0dLapBT_1UoM{?b&HN7#>eJ0g%i~X>S4Vw*}5O9vlG!r;@kOcqVu)_$x2Ww"
    "M%#1?OH@xdgCDqtt9|A+r#!+nkrb3A0;2kf*J)yN5TVnMErRGBQMaIO)g>wGT+6X2u>_>d2rg{;`jB*Y"
    "ZGv_&N7sUF%k}BM&&J8Jhi)msXswMI$uOp~n!#hIH9Nk>Y0u3#%ytgHG6dUE5*XnA)~zP>Ft!|s`U1|J"
    "iid;heRA1+Xj_CE61qgfTOxT=K|~fsuW5>MadB3Zxw?7{A>J*6%)+@`6T*ha4EL4QXlxbdHIowt8Kc*z"
    "xkgr)7JqHKw%K-e@obQBZJ<GjfIOAfH&&7p@;)>Gy3tz!Kus)?SzQ^l)x&^^p5$~S`gCgnhD4N3$D;SI"
    "$bs&@@fQ)0D@*$iU8yE*IvpsfxpzY?TxB_@HOIQSp9i~D7F+)wd~JUK-SAeH15we$Q>O(3uKfW!B1K@>"
    "p?W>5X$y(eu-d%yVYEn4;0#!jseHr|k{U-_AoXzFMR5pkhFzoUprG^U;nHf&vN8wFS@Laz%7l#{D;-Qh"
    "QFCZMHaua)39I1gp;46T|H>7OYZ|`hrg@e>wVw0G&+{1VNB{df{rr8NKmPvtef+(K{p+PUulfDQpL!m@"
    "e*a0oevkS0*WW+K_c|eHp#MS^U61ZZolsjd<T%-BvQk>>wOBuZx?zh<qIC-#ad}J(!`xm7Zk6bxo0a)w"
    "MD(0l-l%~H45pvYRYI1MB%?zGt?fgT5Xqkof107`x~@-uh=l`^*P?fDKBg-7e5&+OY52Sw3pF-Ben2JK"
    "p0-RAXl@tJ<2QaoIk{A_yG!W-X|H7L)E7zsz6{*)2WL|viToYGxv6diuK&D4Cwz*8g+w_sZ_Fo<pZ3d%"
    "#v}aK@A*L4<mA>`+Lmn%(!TeQ_onfciVU&8Dbh=yD7Wr}Qzl!i)mob$dW^p8no*r7`JHyW&r6;=Ib^g7"
    "fG?4nag@(zqPne5_(24m$Q--Ys(q0~BN%w)@Q#mWzpurdB>o5|tbW8xdMN5~H(?o3>C^1gOCvw9bQCk8"
    "-jJS5&5MySot|HuBkqh`x(UPj10SoHd9qFqq^9bz(ysXMrL^r`CvKveVhYul>c^7_O-4G<-)_5DqG+;@"
    "|7spea*(*Pj^jq&VZIFD^i^;$KUkr6{$~%`IivV{{;Qb5*)&OPk5%oG{DNx{*xW&~g$x`E_+HXhX+#rq"
    "{xB`wY}NgV-g{tLjkcM$eGu3M7W+{OPe#;HWQ+ROucvDkpJ8ktz`wp=OaT!12+(VoTMUHEsOH(M4pN&2"
    "O)zcQ_-7W`FqQJvF&dOx1hK6VRc^?R|8IT><4xUlBq=Ny1G5v%&fDsv4{}J~@^rjlB#3RJR{5e`nA%6E"
    "qvyvToZmj2{{edJ+D8wR^!1QQ(oz^QaA44PjXMwIY5z#nL+FUH-r@|zCVuaX)V&qtZe;O)#ULWZTs3tk"
    "KgN!y<mka!*54z{rTh1AkED=%Z8NWHGu{kP%`{VbEi1BS1~{NIG7FUzvSqVb(X5$30UZ%N$S+*+x@oEe"
    "Q1}&@Z_DX?;v&k<{z`$(;uTus2f`=RZr_j}Q97u`UfQm_F)jg&my!Av5s(W|uVMQ~774uC0&sjQvICAP"
    "?9(-fuICy&b%joxFGezN_Lc}X1k9-JDh<u{&fc8KI&9^G52vLd5_dq%nk9kfNLZ5%afx2!MFigQOm$9Y"
    "qTKG6b$%F_6bN17O$6z3nO|B=KT&Az1{Jef4(MMl2df84&l;sGEGhOG?tzY#*C)Yyd6lf2b`if4skdej"
    "r{OxG#OHSL96GH>7k^bWM%hcVxv@x{<Kb>PisBLKQT6uysXOD|x1iJd?YH~DUhGJ7mQsbtOXRv!=d(<<"
    "3j859&<@BR&KuM0!=mct=pW27Rh14tN^Y=ftJQDtudn5}hU`|PMB6u|<m|iQMl`d7r+Z?)yP_&jB)!GN"
    "FrESBXGe9di|_clQ%*DXJ7ss^qPfv1GKPcQge#y2(95yYj$AoYt>6Ppdg0Mo8<L3opX%ap?A~cDsxq2d"
    "+p3I&`<;;#rrD>2iFDCB6_#wX?rujBKVgeV+qp**GbRtske_a*TF*2-7MV3xunD((M1mw1_%;8f`+B-b"
    "gnU<7bdd0FI?=?x5HpWp3|g3P`mqJ<yV%)HtE^w?t8yvLjlb6oFZXMwvwdzB|D!!_YxC0q6;C&SM0wS("
    "020nE(2?FbicxZi8yG)D%xr5p`L*C&Y@lYWX>~Y0>WHdAwbR*FSXjDW>W-UnOQq1WAzQ#1;$i|v+lL4j"
    "D@M=WE0hP&B&XF_kanN1{cB+^gWjBOoOf<^+nUkmO?s4QJ#Z&i<i7MZ+_$)~yV^D^O+$}<vo)^f9d%QB"
    "yqp~F90-CfVA_v|bqnoKjzU5_*!Iw`ArClBrKr_CGY^J}XpIFkR9E#X;uI>5PoubEHJBj)y<R{p0VJ_C"
    "?5r4|r0x5ZS~W`+dW5xU8eY)#5Ded}p3_0V`8&;-Gw)gnA$hWSxK?GN$(EYk;`SwL$nG~C(RcvZ-hzw$"
    "6eN_pE$>ZzJ?uoHU2<{QpYhr`3=Q*+%?(ijzkqhczD?_~+#K93e3OHzuTv>78b`}Ykok0pQMn^5&W+{O"
    "oMa^%flkANJ8>2|9jpy&*TQ^f6yJVIi6{nPkTk(89!$dFAa;vG+UzrN-@P#4W1S67tCO0YJJ)OHM9sG|"
    "q%uB-{UA}yW+~f9+V3H!6+ik60Bb>&Fzw2%;}RN!k`?_L?Hk9I6Z#ef5NicRPTA$q1QxAj3UX4?QLk6<"
    "Yu&<kMNxCkJ3OlMc1h9qF%IX~DUiw+>H8ZPtMqU>sHY7-h(|azh?xA2joLIRq^n4<Of?2q)$^GR&F5Oi"
    "K#6vi9V$nji$ZrPjERc&U44TMqj>5Q<fs3F-NM+=_eb6$B33=y7@|4O$vaGSt6{0;^G+?yb2^|;XB1HZ"
    "GSN-zkn8H8WA@{$WUviqB~YRm<ZCY#CcjC?0Ptkq>eBgYKEVnq)UigC@^^bTzxG<z6u58kfIEq1_#^T>"
    "_TF|`K;aIIQp#Oio5&l7%2x7)zN0uS+DKSEU}_+M6G%?=Q?yUX<0D_UOz&HotSW}~6!k;Pfsk&yDx$o)"
    "2C^cj9kCU(zA52|Nu!RbS+NX2pGBcvf6xE?W<<q0fT=FmFl-k=h6T-xuAMS3*9lcCltOH<$-rBw<xES>"
    "xhtBoE2>EH9uam)4@TUZW0T_2LY3*uYUiN-FFS3#5};8^3$^!>O@ata(PG-yh^(H?=2XyW*<@#`yK_?S"
    "JpZH{PAjv6*ZGb&W6>HPF4-|L<-<n72j6b3-Lcd)6g^*MxPmqZO{m0yE=I~ydWDFb=V}|jcG2pjB;lM<"
    "{M4+JD>}(u>*1y^j-d&osf*I2t-^Uuc}X5?NPwV;DgA`RU4`vwvZ`ETK!0uBljX!h!H~o`1AKgl6xYk-"
    "X7t?Fb~6CjG&!4Cby#s3PI4ZpDb+uAJ(>S2hg1IazwP|_BmbQB$M~K9_I&(2lq314w4d#IO?v({=e3A8"
    "JvrCk>%IRdfBy`Xqs{t{!!bMaUt{3%M+{tFC>%$xR`<_br_p0y-M=Y&G(f46p5e1Sp|{c^pz)V_g7>jM"
    "M9OhDvAk+tJNUQxm;gu2;!K_cS}5*HeqeEWHWO+${&4D7%}?z<_U0wx!+UeR^Fu6Hf=eL;L`t!?me78o"
    "`kMIY52fTl=gj^TK4-pKkDN)r(+zu{SCFrHefAE?)h)0+pNuy(lri`zi^b*7EDk*d8O1&<PTR91zQX75"
    "IDyZgYva9rU~vv7$}3}(FfeKG&i+&%qiQ_LSe5617WsJcsNj_y&Qc&M;<TCnGX*VMADmwvqGu1|!_Ihs"
    "b6YKom`WnThqSVac8C@ra@)ueuKBT2350;K%u#J}E>8@Oo`hm&BTo<4sXTFy#pd9X?LZegrCav$8TjWs"
    "a#(HI@LP4r`gnYC8pK{fP$lU1*pGWR*ADPNj$oB%3>Da%^U<6n4H7CeHUe=}<?%7fQjrh4o#xSl2)`EG"
    "<NxMxl55E|iVMrnAK7ZI@o*^GPM$Q#iS)tSxPm7|?Ao<#eey=ON;Go>LbcZmbw+I2JMx##tsUqHJUu%o"
    "?&)vcfV*j<^kF<EY%4rH1^781YsPzd-5!~sKC0p8tpg}UnA!Lib+<xz_g~SS^Gcr}LyD9+V&qx`q1C)w"
    "P2}Q*&&ttk(eF=oY;kk*&ZM)iW&K3s+g~l*Q`Z8s%AV5KPpDrl@rpZHVNBQ?NN~uIbB$3G%mZ@InNWXE"
    "JpGz3=)WeBbco0|AUlF$;yJmK;l``%EKv@|E!`l0-LvSv_^aTQ&M%T{C%Wptf3<(~&2>)Mb3b&h^e@(4"
    "6t1FW<CSc>o5IAFC@x{mwGM;SoAIe)57J+2mJ@Hp0Z~XEUD?J`@iD+hm4c}Gis<x3rXNOr7||Te>+(ks"
    "L}oW=McgBT{#9QZh$H}IMA2RU3~J&P+?hDLG<v?`#0YwsmeCc&&Y_CJA?Itmgia+nzxuSoXtz1wjxeK@"
    "e{Q%?p5{FkhYHa!Y~9~*+y<yc9_v)4Za{aQj<GZ7_ik$v?~5`&sHAWSg-deDZ#0pYr=JzIo^8ZP_4fo~"
    "#kz%7eSg^d%gFg{=SS(A5Q}dN8-BC|kpyZQwPx!BSc0goQN&ck{Hc%Hw?pU%;;KUa2_Gub|K`n#W9%Qc"
    "NT~U^U1b2+X<I~Z{7XsaFC#}U+Sm7|&X7Ue60cCsp)2QxUC{A6qv=}9*GbOlb>sH3m^ZPSV9>np8V6`_"
    "|Ms3!)+09&(RgQE$d#$-;UDT>ojs1Z^vjZW%N-(oII`>XUgFcXvNfb}x$dkLSR3j<BGhLsow2Iu#5XGl"
    "zKbW`HZ^CCJ9CR}@NNe7`rvi*-w5HP49)%=5k#Wj(pJw=$Y&y##^CITSVXKD$9hJ`9Ts6UBNpL1J#Sy9"
    "k?_47L?~KRVCzOAIwd>Em+VG%y#qQeEjF4`Y%<I7gGImEQpYp3rUN?wGX+a_b1P^1SaO_Z3fWR$4t{dR"
    "=5=ZJ+<2qp3d<`_R925yd2Kh4frv=2bXRnQlL)KLssp<-2MNnJjLB*+yn(G+pGMNHUm(^yWUF=quNw)e"
    "j$$E+j*|ffqCaifs+{E`B9H4|BP(y~3L=6+c<O1>9yhFeuqge*aHVeo@0ILrL{LmT&t723@=d#tMpUSx"
    "yzvHJT5QQ;(;^t41cOak>U+&}Qk6qCV`{#QUm=96?VZz6BA$%bB^&hg?MN5ed5-t#Ideu=nciuc$uRFM"
    "=Rw?l`YQAzVNcLTy4p?Pw!{(1YNnGBt0JJn=PiJS62SqKBD;hPA?n(4Rqpy)c^Gb_r|N+ubZ1{{OsTbK"
    "X5o>`?&EN7+*V)cco=DZ&of-r+E6*jQVLPGCbOI)v_o$L#p3ch3}ad2!&?;rRF1P2)F-+{&r|7Zmh&0X"
    "5Ofjtew>Erqm=ghQ_jH;Q~Cin=Qt3grg_&Xf#GTKYuY4qt|QinPzltyeU6>@vWuQG8`PLQWCp?y@>{kj"
    "&tWk^zQ3&|K7yZk6j%IL8gH3uC80i#@Qfs(V-g0gwOb12m35~>+Ug8BfTy{;N7!OME_q@5!0bk36IJy5"
    "7N6Pc*bJ(AxoKyTHe<klry3cY?gL(7t-~LKbT|<*%sBNc>M1RFvAqOt8K}_CIYI*)o^z!68yc+;dXo^^"
    "4V9~oTBy5iXT_9o4Qauw4wG|~%Fzr|NvcV{?s^a0d5RoHUs%XPlHX-S+^t<qWp5s)i7LxVoU60^6@(^F"
    "AVk^NWLxhV3DN9SiBbq*7V@F!@n7@#4!?6Ju_%GF!K^2&-vn6XRr5NW8tIfOK;c;;Q?6Gh5-n+IS&vYb"
    "I5oTT_;4?b_7y#kS|>{>`wl6zXi^|#or`XbRw2Dk%S=QI0o2&}|1owZ*pcMO5xo%eDX;^_;ZnT+5ft_f"
    "$s&-L?tW^GMl-BpW&{>@w~fJ&2V+d+ip3)UDC?wOJdj9~9pkg8<fd3tcrNiYC<B-2Ql8-nm;dAgKJvpF"
    "7iNV)?uISzB|M-nZkQ3C3BIGnrIEu17I%wZR(Vk2yVGO}D0_}$b>mOQT`m-m=#eB{1K9TFP*1+b#pBf$"
    "tXtN;iXg)GvKc-Jg{mradhI8Lj3aKj|6Bc=`*@ucm}z~mShsUT+tFe;w(rr2TGAbb6XP1&DxyRrsj32o"
    "ScD+U*^nJ%2C-n14h_i}<XNlrts3cq`fk0o!VOE=?p+;xT>zY_FT$ji6-eq?GrfPw1r;U}GouP|;JF|Z"
    "g{(vf>zSi7HyH7upzTCLqD9l7xViFQP|`M20EZ%X21w;h52`vli({wmKfY6uIuMc+%0Ma5^o8e^Jy%nd"
    "i2QVRgha@h*vm6eCJ_<0u8)rIt!Z!s?*v(sXK;U$!xBp5)&AdZ9u!z2Jw>^B=I%gM5ow_P*DL;4pr(iS"
    "?{qKC_nJPxd;a)yg+Jjt{CWSp>%`RGzwf7$zP`V|^XGT|{`&s>8lSCxxA@ijpYhp$8?(j#V9Zw13sBQm"
    "U$)8HM39(_3$}yznf(#O)}Sm(Co}?IHg?7RsH|8$cxG|Tq-Stom$md6U(mtBRjv97kQrNx1Bz5?n#uwz"
    "HgtNP<UrQB34^{5BSM|Rnr{1dh9R`ux9$Dq!^u;MHXaqArhl+0>S<^_2}BQ+saP}AUQP;y>L0Wy6-mr>"
    "$Po&I&F%Q(r=w^}M_;z8C0gKL>(=2iOzAL%x3RSz4?F`M8IRG*;g=^Lu<6Z$NXef@KUsNco1?KHoEJaa"
    "c>0irznP&x5m!BPa?69m5p)K79Ym`R>H(vP#UQ_@F&WeSgWXszj?s}J;k1F5w^TccS3r9dAL|8K#@p#J"
    "-k0BHNJe)z6BI%}4{n0VkS}>qq%K*hRS#c1_G+^lynIykX2+wqa>i&(8!CiFgfaumUq1kaKKjSZR0Apd"
    "b-*k;{-Z!NeB6t$qHxmW_4}(fN{$A3B?vg@7XBxQCc<lWtL>bdwmG83pGf#(p^FtWhk5_Cp(3vkMext4"
    "P1ty3mR=+WcB8N4KTSJo6aRY0MLy6PJmbij1JLABh|i6y)0QP+J2OizM2d|wIC(X$1+0ix2u#&R+~63y"
    "q6B|wo1L8=s6WXR9;po5a#h}BGl`c>Xa3bz_b_LQ%oo!U5fuM@zrU?*kib2z?MWG3D}W_0{TKA*2|8dS"
    "tI_|etzmZyB?&w()$wnuy-lD0__IX-fn|po+Q9PO$b*jOxcNbZI9-vPu>6<-MZf_Y#4$|+Sw?TBw7;6z"
    "P2gcn_deq@=>;vBoZS2texR9sDlnrbH0+!pn3!K{-|OKgAd#3-Gv0T(t0GS}Lfhl2PbTiSSNP#6LSm~L"
    "H_GM3<ZwD#jR`_@bUhN)^q1M5z=Sd*l#B@qn#p^5xaqL^l92!xX+!d60vDeyYnC)=9#>wW;OC}+9c}?n"
    "na%j(k3U1V9(6uJ<tQz8;e`E|aw~TOEMxURB5=e@P_tcQg!v^m)RVJ3^+UcnNGq$`06vlsX7FEzg`UJR"
    "KicINng|M1!6qttDxUJ{JX5i&tBMqV!#0|OYnLA~f3#2lKJFVUlTW?ca%2mJLY=A^|Mg@9Zk84#QboHY"
    "W)I7<pTKIf$t$1wDl8=T5ot>XB~WlQ+tBcZu1&Rrp~Wx?;uswUB8;e(a!l+Uc~CQ(M6%*udgo9&viW-c"
    "n=v`<vvSjfb30CTt)xj*4qjHOQM!oL8?~JH6afQX`N=mqGnQpwmd!4hK7W?wkezGs%u>H+Hidw_5uNgM"
    "IZJvCAE<B6N;iV#A^KDZEk}lCxcXQ7ziW8FK|G9-{2p{tZ0p)eZlj2h(e$USq7@ntODQM&HrRP;8)zZd"
    "VD}b_jV;!Y&)C?IhVbUW#+%`#=(z=R*G)HQcBYxEZ_f}wzIE7~PNQua3kYX6CL#lkt(3sZ9hM9V1(@+;"
    "KE(}chLecjmJPOMqO5L@xQ4Dce$iGon%?7+9#IP|0y|&m?K!jW^(k+<_j%iOwjK%_ZnHu)&DbgabQ_zy"
    "oOM6Q(y^8gHfz&*U8z+8!cv_hV4V*B%xs$Qs%OxW3WkubnF2vv=Pp|6mRy!Hkx$^hKF@&F(5*3F5+Y?g"
    "VPPCNEdT(l2})u1X|zIE?G$6D@^st61K5|y&<dn$8yDJlk5urT;oq$~)rfacR9!o*4mdSC^<8rteAi^6"
    "hd8rr`N;+sh>vhkZJj2j5Ytyf9r?m|ei|L0h2^gWd&)uFr<4IgjV{G%Pu4s`EAuYnq-B_XgtQse#2kw$"
    "^X`&R>l2zZ5Ff#47$Mi?8!F;Jozp}7cx+X03YX=K*y%eh<nh!>W!v#d;nn%rbq%;5e&`R9$PIlK=U}Xk"
    "ln;wjq!Bg_&VQtaA<dkcbxOur&G?D?3dc|4dek{pbK5qyKFe5!Qp6BJG1qrR@w>uG>=t>GFax>Isbb%b"
    "45#hdK@PhdB2th6NY{yO$YP|I{n4FFB#RwmIUN(w?&xpDJG{o2!XVGCs_l*wHBVc_iq8Dy7`sT*==K0)"
    "xFp5IGE8rNYMI-KZJlj;;c3!3+;21TtGz*yui#Mgc$3jptDE>L&hd6KzSyPPl8uu-{K8$dBx!_aT1tS^"
    "n}23YGL7#m^NWor$D%S#TR1(${?&h#N7*3CNV)*NUxMl%rMIc~<wnkRx1V6`%WNw*!*6_*p$;`JeW|Be"
    "@QwwgfTx5D%`q17?Zrw!xe}Q63vO{dPMrgA46(=|T5}a11b`R}i^1O8k|3b9D%jvNTHV~y^r?bWE1A9E"
    ">IYlDI1Ami`;k~pwBJh3+>AMM+{{4iu(Ca5FHe3!k_mrs)(_0`=rhzH|3)%2l51?8IsvCfeQ(DDdaS%l"
    "rLP#DDm|+jk|Ur%Oo^x8T!kM>EDvPMXM#IH;HDk0nza>kH^_Fs5U6q_LD}zCqq!lEA_Gkux2e`^(xq)X"
    "g^yHY)fc8p^gP?ZA&W&P>92glg3Y<eDW*sa8~IqTt23(2)&k2!6kaA*-&pm+HrgZ7h$2?@l1Ys6B=6N|"
    "v%9h*9}bj8PE6*eJOa1^99oGDPpZ3THV(SH^vglgVi8q}I&3fEdN2i$L%<j)H20V9PlM=kt#mA}A`E>H"
    "wnPwJ8_~(~E=i@rRs3s0g!Uepc5zgb&0ZCS#Z}E1@!nk<2Xv5M3%4K<;3(-10w@VkxOSGK9{YBcM+%q?"
    "&$O#6n%i)%%#HrmFXzQgQJDN+sp7icdusl`Yb)Y2?Osg!S)|VuPbbw=aLi-dQU$<}F~3tCsXrW?xXFby"
    "HUg@%eJ-#^AP6ldwmB26rz6}_8AQ`L5Y$PiBc$C|B$)tOXmK@#4GkK|@Y4}KEhd=4z`6<Q7es*n3gLYI"
    "=^yW{ey99ZM*JG-JEiwh{(OyiFRZJE&vGBPC47ITo>Kd`PlnI?-}IK^`^bO3enU9v-yxhDUhUHQ0^zj!"
    "92gn6*3LQvhM*cFKH0LH^~U~z`viM4i%nK8qywrEpEikvEaE8G^I2#E?bPXlW$MFMJHH=a7VB6E-9s>&"
    "j~OApWF`4fqfXl!PYzn#DcX7WZ!Gy32y?HWUa2_x6Tmt7g#mX#r<HV*e^>G;+XnTPuKxDqtfuRLPXt}D"
    "Hd3Uj#Vjx%C*%)66g(X-rYIi6928Q((n&j+VhWzxICzi+?-htret2Dk)NsNwRB|XKO?iRFG;-`m1m~J8"
    "nHJ{&B#)C_*UZEdhnR<hf~KDk9Fmc%t@WiKvGK@3WCJ4%ecm+_lv24)FjF)Ux)G}30`FkPX9`D3w4N07"
    "5;>*#iV2AuM1{=IQnFu!Hs!E{?t{wKjDYcC8sy8FMrVIPMzngB2-~Y)*g@pOxPlWoJBpH9;GmyN6p;8B"
    "Q=~bFFP{wef=vDzgt2B`mk#oB#rTf^PGCk)AVf7n6IQ%oI(SJtJ7q2_98u;!;q7GJ_JdV~DIVQ{3KQmW"
    "YqAH?It6F!Fu{o@`*`8Z`SaxGFZo|cNt!>fe);629;}Rnw_5AI<5P~6#EJ<25Qa3H1Chr|;hK>{X`6<&"
    "sUUe6gxk261{db2&FYvsUPvsLA*(RqjQn&s8ZUli`7e|apGGrdqYql`@cdtkQY<3suakE}5adXLZ8^AP"
    "9hX0*&?x>y^n@)u#%$%M@Wldz>nY=T$@u9%>q<|1Z)dv+z^IX|`@vUzf%^a)==LY*u@d0ITbu&2#*pW2"
    "X=Os1|D+$(FYZCWy-qyB15aP(_2r%9$zm7O6Af^TZITEL324xo6@I+z<Hjip8ct&}Oq%u#0*~dN=|C{h"
    "KrX=vet&pu7~xY-mqMHX>y|^~!hT9c5@<~Y_t_`F8MQz{o*)2c_sTGyiH>jLo|-PE7b~y)H1A6mW&Ie("
    "{Q@shp+G`6#6+{aOFVv(kJ1d1icc4yJ;q8!v1G~`cZ<Wd1ptAINJ>&>&pSNkl&8Q7BYMCy^);8R<7SlA"
    "ItH}-%dj7((EYh`-va~E#5VO@$0TRBzMJG4?k@hV>YInHRF|KWh^aFAF&}4sh8O6PP<tybScsTF-ZjUT"
    "bNog!@LXe_>+4=_ThftbEsZ!8LlLgV_z!-4RnCi$e{kA3zfoJwzlT3pdxkmCo_h0dlV*(+D*-;9j{ASx"
    "id;O5a}rHHVX^5RxCVR%pZSc+VJW(aj8plyoEj1d#kXdvbaX_p$Nzm}Fc#1%gaL$%J$`Z?!qWd)=8<N0"
    "kQTkeaHi4w()NmB5_lt=LRxl?kzcCb%rR3~0>%6b#GPAgtawLO>)8a)GBgd1*0n4KwEw(*4fbmZACxJl"
    "TaD24!A&g&{kJpBrd?s=;&shTt3D0z(%S|LBWgeb5#PF_NO1COh(eb;JWs=y`pl*5z*>YWY<DQD(Bi=Q"
    "*IKKAE3DS!{C9O?xKj%Qh4yVHNp|}x$x3bD;G_A2TI<a!ZWy<VecmV0WOZ^T^2VjaR@PjOF|)EX2Wr+@"
    "Y=K_wY4`_k*JHzJuQxNFcZ!1VdXLO_Wcr)!8+dKn!AHlHSw``+M^%w9^VOwQ8lptY=IoyYzb%2NwzrjW"
    "$TR^MPs%~8er5(zWO?LQrUz+a9fia6?|WK}t!#gf+Calnba|^Ww*y(062f|prxiZvy%KDa-SG3u86MUv"
    ";s1c40#l8F1Cs_}>&j(Z^d{^O2A98_?ew;s5`;t*8&GAzl&5j1R`4$S$xll<D0UTHho2fm;JD9(i*l<P"
    "hZJUDJx^tIQ;g|0t@DZ5e0Mk`Q1hXstk5KbshOrV+yI$H&B9*gWPN73DnGfgR%{$Ziq|@S*K10_f-fMv"
    "fR#=FjhcZ)TjupJArS#mv_QdB=FE6v<$8F@>T0San0Uwwyrmys?YlLc6+~-mDsUxn4y37(+OURQc6lHF"
    "#XLpII`z&Pd>73v`n6k%<>^@du$DtRx@N+Kx&soH_UB$+Lt)rB1lkHU+V_S*=I^u^MjI75Q}gV?Ya3~U"
    "8qn2r-7Q1Lw#t^8rf<L5TS-TJ-B086V=f7HbDv83+>JzyLU_*ay9(hC)Hz35_}h6GX3GiVDy<-bMzJHh"
    "2ASe>ABzvET#VH}{h<hY<0>sV9Gdcjc?XQzkaj~=Cw)4LD+^_jCIaIm#r3XvW&&nYwVj}9f{DRdI*SM2"
    "8asvvA?hz74ND<P(s;=@&Ytnt>POchv1ro|&BBZ&dK?>`f~mFkml<t$z8*Im4zA37IbM3+Pi>tiBq~`&"
    "19peS3(}_C%t2kvM0M7(VxZp58l*fE%_<gn<!w*K9JnIuuE8L`<9o>vIXPr2?Oi8SwCtcH%Tl3cjQP^X"
    "2J4I6>7*rNtJt<cWWoc8+?0i4rAh%xwDfFY@ZDo^hFvmacO80XGO8l!j8T7kC?-AV&eifZ(Qvb=OUXg0"
    "K>3KoL<*vC95yri-Pus;bXg^}HVK9j?%TYX`0ujuD0P6!64Q|_`p5|{U^N0jNNQWxZYHtQFy*^Ub=DP-"
    "p&4=dM2IhKXKc-_)MmJgfRMNL;}u(XBZjCIUhIT4tI?2ga#n<x>d1{AYq&{6%aTaD&iG@xjT0i)#h+i9"
    "e4`NLgDDacM>r+9)9WBq1MAFN)|Mvdq_V4Wt#(GUi7)kF-fKKYPYN8fi?R+6)GgG93Hz!=%4x3#!mS_^"
    "$@Hj`bWn89+?NGwWue~#fZQwIesv5p3A?bWQ!f^TF<<+Y5fHWWd74v?tK(Xuxo2ArqhzYpN;;;57$zy^"
    "jZuIFgUf)ikyxH}ZBQ{pf>X4YJBH$yxSM$~yNv)4ol$^QMVVGs2tJKLmbx~M|DJVoua5VRtABlee&?7z"
    ">&NH!2p`wickkizJzrm6Umy3?dVQ4lmcQ<+|GP<L^e24voWH+6e)*(@|KO8$Z}$I78+J2RpEQk^pM5@&"
    "T_s!xbcCmSH|2Wm04d=BRp@Aup5~z=vatBuNq<9^5314OhU9j}Zm<<IMI=9i84u=S!Dd|$B@8cI_@5l~"
    "H!a(TvsbIgLOl9~0Rs|CCxJ)F*Ac!MmIoH#eQxPP01&#3r?%RmQ8^q9(z5g5h`OYJ9^(MsD1Zl_Th47O"
    "rph>*WvMaI9Ue(3rgl4mHzPTsReDz13SFKDd4(<3Ld5vYW+NS!xC4x#K1$kqkd(_Y!zZ~&^AiC=w_|xe"
    "z(!oP0!Pwx5|(oDKJ5--6~VF*T1hhB$9V8Te8Y9r4aYl{Cxw0z-@tdovyR*{Sv#LTW0Zm~;i6ehh1J~{"
    "4<9lW$Mew$$fuMX*-}nvI5aFMii=!7i`(3E%;I^t7>OiYMwgA@03A_8r3=$xgi4Kg(1Z3zqUw^s(49M_"
    "DPk(8-5(^dZ&c{_rE7fsBGT-ip_?D~0}ZU|TY6E>JgazHo?S24jw48>Q~r-D*=BG&!)?M0L*Gq!Ni_Ft"
    "XezWf_~dD1Ql0q{!tqCpjnp3iYQvy{r4+_p!u66At}!6AenyfB5z02B?o*Uu`A_v!>qWXTP1W+mnbyyl"
    "erb_rAkcmp)1ALLs5?z}mRvVG;)i17jf6m+A2ZtKC4VN)5tz}^`8Mkdl+%Cx?~iUs?y9@?oB6${skS`l"
    "%`JxuD46lA2kvNsC0@hPG2hVx2V+_3`o;G7Q(eVZ3@>IQq$*$^1&}k78#XF*U_|1DZB!+0?rnW$dDtWl"
    "An-Tv)-6y<bJ+VblbiB@`|#;rl;y4MAH+JGKC^_94PY$zTC=1?0LGpq&3kZcKlIm+FIbK>5uCQ`shOM="
    "5B!OxaRQMDo^`b>XDDuicrPVb-m5v=qfWy<7||NQ%H9ZC$-=eNtQR}9Y|}Uuk!w>XcPbvkl#c}`^1LK1"
    "0HE43?NKLMD07NsM{5xoFjPN}cU4`Z<@JFA=#o07H}2Oh<B@oPX<o$H!Wd*TLK1I#`rt8a9H!~F>uqbM"
    "vL~o^Im4@?zRkF)vKx~1DMxy9$gE20^>9YVmu55#KV!en`nFAlJHs^d{G@Gu!)9Q)c&)=}e2Fp-i<CE?"
    "Q^RJqfU~~LM~Yyiv0)EwVqX6F>U@XRS2qsa*(!m`!GU3ElI>`gwtShV9b-X&45&4g7{8a|_`5g8v}%LR"
    "OFO&~tx1O&$q>$%-fygi?Ytcpb(kKHu~$f2fT0XF(oFC&ow`3K=y?}MB7Y7d3~Q(-lj%qZtM>hFv8Y_+"
    "w;4?qrlKiWMEkbRl~8fHU5t)J05t>NSt^YhpRp5m%tzJ}G1goaoKK8%OeR226A}v>hZo5J3h5c>N(xHf"
    "P)<y(YMFDEjK&Pll8)2!8uVZfK&K_(z$N~M-9EO&;W#fqPVnb|{NY%a?c8f^Mo)R9dtq=7;d`4MYkVKa"
    "^DkwZ=4~s%$AXCAzfAcxx%c?#+Mus_u)GM!w0W$1nSALtht%Ygx0}r$HKLoN98$)YJ~&T2?~&&C*P<ht"
    "va=Vq@fws3Cs)ph`0Si<dil6vPuCNX)Uc<(!C)Sz<QRI$y*Me>DHu4S-AC`)Jo{TKlnZNq7^k$k(#v3*"
    "PY=2j#rihZ;u;OChQSq2v{GN8#6}}*3{7~4qZ$Run-iuFXv%R8((%k8iEQ%UG4c931s}&mDASwN3WQ~D"
    "I}0y!5Vh&FCYFI}nF5%xe65}*_vij1q<~}xW&p@W87*#@gT^2}FM56Y-$|dzOlHIFiT6mH=>lO`k;7hg"
    "b=4m5OKrV}i^ly9@opjC5faQ=WC)#8u(<wSdofZRNAHvzcfN>dGm((UIA!#Gta5Dzs4!eEg2M`pF^MIs"
    "u5s$_Bm&TyWnKtJcuZwvTV1Qvm<Y}BO{MvubuFyV%vruiWmsLpG?iYB<eq3&b!ctF?e&$38mh)a7(L<<"
    "DtFN33Uh~kU$rdDWCs+H_r)yVSo`Q!s{BtS)deyt_O@$GGkV%Xn(Fj_(_@**TBv~FX)S^}90}!WRK+=q"
    ";ms`T1dOtcCjAY;AndRb-loAsWhU~rW`P*~#Y5+M+Inb(v#+yL)YdA7e8Pce9iZ><yx)UT?zMHaIOHeX"
    "8F~j8y7Gl5CnD`7gPy@Nt|9}$GJ21`m?M;l<-v@CgiA*dH{uZ3fw5$~m`J=>kGU+gamquDbzlt!8_uoC"
    "4l?zC$vlJ4x`!lA)#=Wl_&qB@umO~=6H+5F4AibN10!STYo*sKb}RR0tYjwWJ6?bWp*>Sp)*|hG%Ds9%"
    "$EgRL7@eR%RlChlE`v$~CrtqA{9_<iQMRps#=QvC?#ZV?YZ;jG(YV^cazwYyOTdle>GiYv1BtkLvIJ7;"
    "(>Y2SrWff=r^zal<Ias5XK4_x$+%ef*lImF1UPNVQw9ZoBAMWtn}^`A5g#^Ks5FeynSnP|ud>C)5*a9l"
    "n@QvA(D8uA-tw8>a=+cafd<Z}R+`S6o~>QD+O)e}c@9&JCWuL%hS}Eq_vs!DHrxwtGocj8S}<Q6Jmx~&"
    "3zRzTzHIIFiV>pv5Eh$F{SVT}M3Dtjb)t-=9xd)r{*UD8Vpj>yu5=hgqd%73Ffz&lvFkGcHd8^0503U_"
    "3)#fNS-kU7=>;)wssu4>QAerJN?*-9xVq6EIz|W1RF+w3R8F)7IrpDjze%<znGsyIs6e=Gm|2i{la5_h"
    "BlRaV7F3^9+qWR@H_c_$c$;=7N*7cV)$kqHvZ9hJUWQJ~7HaM)4_kG)V(1lRBCzg7Cn(4Im9Uq<FdFc)"
    "vuhGOk83K>r5RcoY~#8naSW5bU`16&vBl%6j#>OIm84WAp+uFGo<Pz-+^qD1O<dgLnto&;b?|$fTNt=Z"
    "A<5upnc9CgQ_CM;f5LeG_>6UYz1Oc&KT>;--+w+w{{H&>Z23KWe7=`)m&t#6zux=z_5JZxa?PJ9z5hjX"
    "4AlIancCII|Fsp)xgXGPI47d;oT&z*TNL>!03j2Vv4@WG;KKQJ=8lBZVUQxr);&r0IiiM7!@Ov`*`TZb"
    "4@8G-CT<Nwi<h%8Uq0bn*C9L+po@f~1EO<5Sbza+^>NH66b32+GYOH6N;*PL+{L;F3&$ve*aK2CoQez|"
    "BSbTaPCo}tLmkBEj8czc9Eo1DjphxJp2LM~tfg}r`)#bc%nClaU|rb!NI+t-3FFju!1aJlgM1c}W54b$"
    "s`pd+%YYKqu|1C7$8nr62!y~XJxM^}99Q({*nX;}k{Vgpv>Kyyio5~WudvRwN5>Ip%h}_XnC$HtWWgB6"
    "5qwCDb##(TjP@`e?PQ&&Q7G4IW;!XrB*nuoM*@7Gl*V)Lx0cNBkT;V^8;cH{3HW%}{-U2>d2%l_Xh-ih"
    "K-q5xJg2a9u*xOKM|$uOUjer_g)tVz2J76XSFisY&rw(<&Unq~Qes+_tN)7>2cs-Uuw|!-#}_Tm3>b-L"
    "JjZrn{TH5d{SPCxFk9@k!kI<c{qDQPGdceK;io<?z#|XS;-|j;fIY$<>7VpKKZ=~XjhG)P{5apMl8e(@"
    "Z9O6SQ~<~~_gP4;U=4;~VOpQfD4E?=?g!qA(-5om-BX7r5J`~GcO7AKjdL16wV;Gu{x%kKv1reQI`u(V"
    "m5o=&H-^RS%_^uZk6iCOU%#?^983$-dV9l@%N?CS^03$SCZI5)6sP%|Q(ycD8L__vrpF)cm7{tz?B2LR"
    "qfZDYF?x2gIUXeYqna@mY%mA&JnAk>ihmV5&ll8p9ZYyWkGF|V-dlYANK*ef&LO>7pwsF)ovZTrc$;5~"
    "&{_dGHNK#5PaCN>(_O`{&uel7nOfF=q4UantQ3V^pJM<_MJK~sLxlCqnZw@aYs}M7_gcvwwtg)?s1Bb>"
    "ETg<m@UtaSBJ43p7jn0!O<8<~=04%P&+Ij?Wj)UZXjG?<n1<Ke)>TdGyW|k4>zN1cFT17)&?DzLedi?&"
    "1AO&0G`^K*VojbJn_<4g8aa?XT8>U1NR%y5*4J4UQyctBl%q0#g`I;oB~qNJSFumxXaTZ%ou7ICXCx=~"
    "^qSM`^-g$8)AGn)L^TNpP<fLPDG5n`n{vv>M2E|&kqc9KHk~yE)mD4r?M8#dG~xq|k6oUQ5d7wA-3!)O"
    ";FN#8**dvDWiNe0t)f?DWf%yA(^reY`^kzRV!I-I)p_r`1w@!OF|M=<$qtoJDxTu+a8?9bR^KuZZqCn1"
    "bq`2!29I;@RQyCh<P|Y@Dps04RNxp6AhA2|{n@w9Y&?P4Y!iNAkBQ0Xn({6Pxtlhg9IIFn@M{3vH<^h&"
    "+A1PN2z%KMcDrl?r_4Eaq$12)R={H>8yK1t<dF?NGN@b*VP_hM?j7?)^8^LjyCiM^bFfHKK!Up+OJU3@"
    "8Eg9YL!s>W62>WiM(8g=`<C1mNrxx40`o6h&O;#SFS305DmzKIIG@3mhN}x18SE%J8pL{wv{0HEpjel0"
    "nUijh*1C^I>E?FTqK)4`q4__0R<cHpc}1BM8^Uoo&&Z!)<`Jk6sNdq4QXQuN_~#;HkTopsCx%yhhDe>p"
    "c(bB>g6f`Rz1%hvq;uq4pSEyQz_MiuDQH3zYg7!~YL^<Rmmh7N1jszUJyk$59|7_RWT<T;JPZ09SySil"
    "Pk1(RhoqOp!!RvFd{sUxins@DA@{mwP#9SxT!Pj3ec8%kQ4BNjrPKU|lCEi*URF!U%TNTPM0ISz`A`FW"
    ">9*fEex^kspe0S4lVh));yGdPfytqANi=QKQ&5gg+=x8&+5BPTD)*ZH!%S#nyC??sKLK!?hpZVsq<{Ax"
    ">!^%#QHdM<%@Ee`9AT_xo8kE-z!X_Z>c@N8GDm`giWr8ZpH^8WL)iha>tD=9PKXIz^Cr%w44<0&VHW@>"
    "y~rj$eO^oQ2vZ<LdY#hgkt(9Liak!T05w@F8CZO^r6s2tCSg_9l}2C=Jkx)dCQ|%+|LI6WIBP4R@iqt`"
    "*9n_gRh#@sZ6&CoKS)eZOLNhB<CamTsT!OJYYj2>37!d&zmrxUBoHQTs~$}0)JdvgE<sB7$+I3E0s*mc"
    "ky+HhmE($b`{6~Wy&UAA!Kg4j{qjV|9B~j3u^QGhm(T2U`x7&azzZhXgmt416nIi|nC?&qGzW<{=!CNE"
    "Mn~VQPobS(olM2x=;0Wbt8C1XCiQf3jK%Xz>CTs0aJ+2KEUzrja&)H)MXNp!mnvDAESaGdvmaQU2mtDg"
    "cZ%zx9Oko9J;I^LWOfL6^9?0q&9pmCGKua?nwdmINdSn-G0nfeIN9djr@xs_uW=0yjS9_TIf(*E8uy+9"
    "?sIg86sWd0@yzFuSN*^8WE?Ua1}BCb<BIbT#TUl%Ds0`(xMu3yFs&#%YTAf#U1?r6l5(epOQW-aITt*Q"
    "%Vo8TE<i2REq7TJp-DgO=%OZqaS<S87#f)bc=$%KdQ~`DOX!f~k7JLL%mtX)>yt1grx@9Yiadr*8&wcx"
    "_j!g0cE69tX8WN>f~C6LW&UC7H5*3f&hmqJQypdmkiX0oBkpf``t?LgnESAXd!xE*@JF^cA{{7M_xdvg"
    "U6rSrFyI@rcKy9Q!?%-4c)N!<_ya~WC&;RNmxL_CHz-M~7ib2wtbwLE3bF12v<t|mg8ry(Rs2f{KVK=5"
    "Y}MO#IWz_mS8r1k_o#WY%Lrv$gHW_T0u%J8TQc}=4H7R&%+eL)wCX_xY|Kk!JoN%i+Ncsuw$!P-#sfY;"
    "SCj6~(3?$?;tX!WIq&{t0{#20sxnRh*#zsjPUGZ6KsXUwNzTilH14bcU;}MPm!MYDFCx)~8*mns+ey9|"
    "ItN8<iy-hiIdWd=>DZ?5fMEqjpi)0+&19TwiJ(^&*MCKP-tRB;em@Nb=X{p0&(G^)<kbGWe~z!~EByKR"
    "C|@6+_4<=P?<%4GxsT=g{(V2L@B632*Y(SL&0x;InXknc^R@fX_>K5vWOJA2_k%rtP<R-9gGhiY?eN|B"
    "`f~y-gG$JUen`5vQ_cqP2jV_e*7nspn0PV4rsXjTL6MI(IUiI!W)n6~<Xx`XBIXs{nEubSdUloV2N;BG"
    "Nl%XM)q*F`(LPM<yz<mRM$6t#?sXsmcxRgLcm#*)WLc!i(i7}+$gyb>0bX{??Y`me6DJ;@V8DO<zIQ|>"
    "3P9p1o<uhn?U>k9LR86&Jb3JdYy=KKH`?p4rxX4m4^27ZCDPEDEVN@fO*OIImObQ|)`O#4_dO{44Y+`H"
    "_WK7&Q7v_>s8hM+l~MN!`8Y66hP>h89uPPb>nq%Je?-z|P(%-EnTnPB0rTmI^!rq8#l!?QzoGz%0{&jK"
    "%z+1V4%gSOPHo(cC_9U6Ff*BYL=YZ#j7`x4q>P|m;b7{PC_NKHA6G$gc{^qD5Vl&PeQ{i+s!c56Xu6jK"
    "AY(rAENW!0GX6O~hgp^Vx}Rb0`(GYyI-LxttXNCse<rT6{=r|GAMfe?7b}X?zCxn6E0N%B*Z#PKWHgMV"
    "BfWaRJ;9R`92MrLwQ48snK|Q)CW%zu#2jJG+x-g`0KZtOvdkD|l7#C<uz_1zC(=J*I>81=2#L44Xv!-b"
    "^Q_O&p5gM##M&wVrj6Ot;k2E>Q#dnbcu?BjQbF-EL+!UA?bL5f7q)v{7SBQ-3u$yZyUl$0FeYB}8Z%TT"
    "(lTv8;&kwuV8JOCW=vdZqB~_{xkEHAe&0_ccr6+p@7mo>Kfmtvg~qDA_;O7^sXtfQ_A@h7XF@<05yef4"
    ";#o*?)Oi5l9{cyJ2wJ8<D0_6P;PLSi{Zr-$AHx(zu<_L?E?A>6Q>b=;C*(SFw8@A^COyMXR)%nQB7AsC"
    "(!yq?*YG<`T5MK5q)EaE8%E$5g&A*LC&io^dnXmW<)^!#);ROV#!%;XfAB`I2mxNa@7!m>kjrj{h|f45"
    "KG}KiZMjtM-=)K3`r#R;K)=>@-$U7dCp{HuF6cQNJG_WmVD(Rk*Z3JHe8_8%o5Kuhn)?~862R%cj|^zm"
    "x%8sn!-lwe;u@O$0Ls+qVJbrvleT1yiG4Aqx5^aG>|=p2x~c^|W>tRA$blIa^sB!moGFk{lIuKJwkQ?5"
    "^|kqH<Cwm7DC}42cKd6>25I*Gd%IIpR<)HoCqx}`ZQ!>*Y#qM5+4hWgzJ7SAd7@gl*}Nu$y1E&R*n>5H"
    "$yD-ndhQapc+w9=d6K~M=1P+%<4qSvpEI_Zq_uulqvawlJ@Iqm6(nfdKW3UoeCYE;&Bogvc>}N$9!&GA"
    "&jcc#!3@q?Eh=SwCmXtmO|~YcIyS@Zj?%_+pl@A5nK>m|`*+8*kLTu2pQ$tb$=RsR^ZET$#ivLRY*ey}"
    "@@^*TGOL%a#NZ~AskiYI>Z~S735~6TUZQ2k<`3-7dznD0<a_0bg($3ZrEolJ$)~~sB@5)^682b3hL9%b"
    "-klYHV0t5|=1hBdR`?kQX#hpXtGj5!cGC2z99RhjOgvTS)GcBNb&0cT8QVjS7N&z2aw%JqbDzyTBO=XX"
    "!sLjE?Y){q`ArL3!xJVs-b9B6#%LQi$I<jSDswIfhM#_cYbKG_0ya7GVWJ?(NR=-5@_XPL{$LtDWXnVi"
    "p%PS{`|2DxVHUeVJk2i<=BPv7_J2S>TzP_4z%i-s(@$=D$AXL^qX~^k)TG>pLgb)&Y)Q+^m6_8k6TqRv"
    "$RtQRT%K@31CyU2^f*&7gH?dd-C1n9uDQ0RaLn;UIv&EB4wtQG(e2Qi$+k=^<$<}H^cB9TYPxDJjpkxZ"
    "_GPuYE(cYX+Fk%C0LDrCx7Z>sU3(_E@pal0i~IC#`?cPSCS&)vAJcblNWAl9z_^0aMZ`Ki{4m+a4#BZ`"
    "SoEV?O!^vD9*<tgXix6r8BYy?Jt@A>5!l{#3MO%cD4}W{<hqm9orcM}#eI*^4?@N{veT|-@Zx!BQYoW%"
    "y2oM?N_YJHQq)#|P^TJqoNVj^ZojNF!tN9ct`#vguQU0JVGbbEW*Y0BA-S*;LtplO>~EaER*T?n^TdY*"
    "gHj!7dK_zdh9@tMCU}<+-GX@)m#k>%6%RID^;<cE<qnRe4bq85RQMT*V7HzKlmTY!+cY;me^;XxQdhsu"
    "qZ59k=*Aqe8PGA_%S_rj8Rw3Tent%i8p7ETt*k{1E3cvZq>j5@S;xM|J`QDi<}8+ZZLWo2<P|38+QBia"
    "(cAF;kiS=O_i#g>l)OiY8(=8d90~u;*mu)iJvHfZut?KLVq!t%tz8y+lwEjfEog{td5sEj62?i2UdB<("
    "8}BbEs7`MFk>#({m9AnUtk6_OhQxb|z<udyNGFpP{_Gm`{;>WaS{^7-SJ3LfNbmlG$!0mCNUxQW*19%V"
    "@_O>+7K7zBn`T|WaGZ1<t5O4ef@1SbSjNlv2o?8T!%E{aJm1$mtZ{*w`@2ScnP7b1lj;QS`bA2$pobbS"
    "AU}jqazoqpLYhfA(y82s2}kJtsL`xtVkVaa5`MkZ(?l^QpZr2Y;ST4GTtXfS2$lmDrJ$?GSe0^i4e|ju"
    "TL?{dt*s@3Qq=OOg~`9DGDJJPpZ@n>(r{7A&!d+!T@M|hN#1}1GuAx>&6VsAffTw4r@(&n&45InLY>B6"
    "LL+_b$T|bfL`WM~@_^tKr#KblsrvS~xRrz>Tj3bq{qG5!#j;#QN^(|^sJ6Cu+`~KRQ|a*tV8bg?Q$)S_"
    "?AWcm`W0Q)*%yJvWXav<+kMnb+IJREyruZ+Z_Q%v%jK0EcvCZUY#NUi+2lU;_Gw;m(30eKW13h|;Z>XR"
    "u7W)sN6p5-l8|Wx0~3G~AC$Q+_ifFjvdq0J;iHUynw}Jr=At_!tu9%SaCVJMhc&HHz;Y&$tagL&_D25C"
    "R&2Td`S@(@<Kr&RzTV$+d;jxYdmmr#z1}C#)xyVJNq&#_tAE`)`fdxuNA35C`se%pZ^|z#w)kJH*jn7J"
    "*zUEm#OMr3ShANzH+}ZiVoj9R#-SwXcD4rbfa3%j{9qSrbsX(F1egHMsLzlCA=mK;=k$^YH?_$#SG%sA"
    "Fs63ReZ!ASQ+Jq#cb#hbo!M_x*UdP5(=jzTWkQH_X`vrS`%gp1OvgZL6Y_DqO^7uqXpiCixPvCADy1mS"
    "6)gAj5l`P2?^jXdf@)sndZv1^IFsL{T5Qb81g_gv<OI_}OT#bCfKT*dKlt%6xe(PDsuzKE<p^iUzCg)?"
    "x^S~E%@c%!hTD8bIhDqGSXB^w?%NcylmSJ{HPb=YM4%fnKTMvP;idzQ(Wh)4qn<J2l<qxy1aXLOf@*17"
    "wET8@&D09fpVosj)vw_MWDe6!>l0Q-wMhKk%U%iAopS&Uz8Kyc=?LOD@07UO&Zuv^g@dtTN*;tXMDYmH"
    "$K+eQDtD3!H0DOtZlIWH_LKXb(vUmh0s|_X?wE4*e@1b_AZfLF(#|>X;&Jv2VQFt=I<=)0M6hzli3`8~"
    "dC~8r=U7)nn{`G2mLL*f_GC${u)MlviIIcM=EumWzKV##^kUO=C~w&C^Pk{Pa+joAW~6<@A2_oTr2f>X"
    ")@_iil5L6-3<}g$=mB10T;drP({0W6`<eM4Cu-oS7B*GWGlU*Am;t;<+Se9U&%nL$xP~T%Ij)mbomRv("
    "tN#5-hu;%rBIar7Z5WuVTV!*$CAc21%BM!YeAz*gFrhaP+=9tko1rNitrYji`3LG0#gr{g;m2}p%-1Pn"
    "y8J@F)u<DX4;#A&>qXYnp|MshT#3`_+T`Nxox~|CnW_$>OfO4d{6qo?^&}tXg&0hQQl1#;LqP$3?B6ik"
    "DCg06ciHc_ZkaHd3pnv4)fv?3omgM=M+TnK6SsU(e5fk#(>N!2yf<Z8>j2i+Lw@sUS!{qef3~(wfN|T4"
    "xZT)da2K;Z(M)}PKgQju!^~z+KI05Yk^D0vM+h5-IvCJn{`fcarEGdF{do=RrEE*sci1jx0ghnpt3e0U"
    ";!svYwc!<WXpfJGhT!q3blN^ye44bUiNEMV()3R=+O<7NTFbD^^9;vnh@M~6WaGyM4H=4n$+&(#&5P_U"
    "t{EgVJ>1aZ{xXC0Isrx-`l4?5V7w@y`ix-$fAkhM2vK(&FU;f5%S2DnsT9|4H3q;`t!eX2XQHvouhyB{"
    "9V(;=TrlkNc##<;gcTGHolahTP~D(BbC&(dBLH`@q3C0ahq#_FeMmNdbS(S=AH}C{pls7D7PHskcGUPe"
    "p{_SPJEzT<W2_%g3tk<s<_}U;Ybv8MNR4CLp$Q$~q)0q%Ub<79^p|f9Afr7+ce7Tr2Y<F6dI`3c8X<Q#"
    "tB#yjOGmQHiW4H>C0s(!MIWb`627G<AYSz7Z_ZE{eDSKrsvT`E&6#Or+(@dwpE>;7*c|AwOn)jU^~?aa"
    "ZlhZ>UGU^VMFp*xbc}6V$EkmFthCNck(M10u|ntx>b4!-HI@qoBbkgZP9VkZr6hsKGe)*~eEr_-!1a<h"
    "0R<e~5>79qSm+dcqK!70qchu2bi~wwVa&YgAaeA{O&-1D&_(~Oqi*w3jnPW<{LP;s+T>82+g;mfv-*mn"
    "f-ylWZ=SB^7lO{CJWHo*in$#5LlN>@L~lu{ztWgs6G*8njnXo1$^=tQa5g5-Gu1Yr`GL0oTNT)z)_Kv&"
    "9bG8s65h7yxV`4pHSm`rOfWd=0ovM4cAIR;6~4$5ZtxDZ>Q<~i{pbtO#%L?5F|(xUdB!b;IEt-nqI1yn"
    "u#*`0gI#5lX}nF6Li@RMg2`^{`n7fEnCdR?9?4nC#DVhi)FO9{6i37#*@2MWRh+<evmsP-L$CH4^#`}5"
    "<a20?UW73&{L<WZ_#`o<q;2W&mzMMC2?lCWh|yc1sKg04g^g~J9EzmZp&L$qXy9wXe1=WPTe#$EdQR~4"
    "teH&I=F#wWw4oT7OzrI35kwA%r*DynU4WB}_UdGJXbK4dJ*|`A2!8<lEfcIokT0`%B}lh*;$OY~HRd1e"
    "7!3jL#jWiXj7D#dJW_L#Yt$(=dY{lkXVI)YEg{gFZX+t;LIBAsd2&MH3j(X@JQ#=Jtu*f+2{l$n6Q|3I"
    "Uf&d3n91MJ^u`V|tclISpg-e;i0puV#2+Cof|dFEHZ`uU8aq#Jt!AEbm-F&(YhEL$`NWWIgC!M@JNTIG"
    "(XvrULV_aCU+w(lh<oI;fOY`+M#d?iL?|_yRYQhN%J@0Ge=nTmIUbcNDRvsX-M<0>PFWtP2H<k*nS@yT"
    "(cU{!m!yWPv8|AOXdYeA>K7J!v5-pLlWagMs?oJ{yS(g;d`G*gitCh}9=Zx{EO{SR;)o=aop1BdoC<66"
    "ux6l01eP*gkpNO3l)(ZTl~#gu!#059w5~IA`H?L4wjy>a)b2I)D%I9_Qhr%Kadaw2^_%({-WG%~6pSrZ"
    "a2wRFrV|j%jG${d)bJ|67fn})j(m>SE;OhVbI6x1e?it@*w`_mY!gqEmNV8iQPG`|pqi8~pYQ7?cy3&b"
    "%&tSyDJs>9f5^+F`nUR>aIx|4^OmVLsA&2ySHCihluZ3sGWE6L)+B%AbRQ}*>`F?-PK_zGc`Vk4^u1*l"
    "X*WIfa~W$-K-~wTp{4hgkjcqK9s0pfq+bG@mhyLde-4tlKS>q>aNoN?C77$qOq<dx*SN_l#SxbCjt8uG"
    "^)!SglkH=j%$_D%!2CF%99rf0C5j*Vgx%*lq8q!fU@@12`$!l>GQen?8Mz&+2}M<@n4m%h3lenoT64CF"
    "RjqhSN`*=po0)Pw9rHRo6;9K7y;vRQC-cTBDQU(bI!Xf##3RSLaa8VG2_W25eELu!Rg{!^Yiac~wxwgi"
    "gf8mF%@@`gM#k`jl9q7|my+e_Q!ga5-fAs(RRM~Hjt;4k>VHLn?mF}S)AvdE9^b#p$M;tn?;m#&dq1D_"
    "Cw<rc*;5PY^J{#RPl>rc@_p8Pm-g|Q|D^oqmxUVu&%ar?)$9Mlh61Gp1=0mkXn&-&hQK)vBW{(P9FwZ$"
    "u}y8KL9ot(fhY@q@<1xjF%_pwkaF6Nr+ys3bL&YkL;cXmEjj$w0s!Dl2rYzH7p}L;LDZ(_fPn9#1|_jG"
    "BB#Q`$Vtli6nEnuoMB7$)ybwi34>I2swxDZ?>YT1G-kTr6+)jhl}o3;45@1wKfzFS)7<{W1l(Th+NaBN"
    "RPX7p1m}%`UcyM)Ml<`7AyfG4xUKm~U%O6H9-S8=2EkS27)&Lf-~iQ}GFaBY3{lGgRch8X;V}lzeR<aV"
    "8lIyS4E(6_0bfGLlbj-PJmHdik;xL+d(?P(*Ptu(WuqHKJ{!2{)5Xfv+#cQH(p>3eBiL-BTApgoj$dnk"
    "edsyya_HvoYCz5ZGvM_I{aFq#?IzVHTlRk?@?=B#wU|zTMe)nVk>P?lVbPZGnv<oYnkOr70ikpqw3)i~"
    "N;vxVZO&AhGwVqHnGNSnvg6zoPr{<d-m8Bax0+N9Q%mw&PxC~UtU}o7b<tceOfCxir?@Ls9D-w<gpcwR"
    "Vf;2>8xBqhPZa7^bL8px1IN7WGcbbp{Om_LBW>>nLxK8WsQw0f5z77^3e?eEU}h7p1&Z>=h;P#=FT7B$"
    "<T!|J4t6~ltK}Uzs6W|5)8omcotK=<^w%scO-Vy2zr3GTH@GR0!3AN8q{<duqOMsQHK4i_oDY&#<2a?#"
    "_!Tl#uN&HwOvPsE5~mJowYsWrMkeO#wG3thGt^@8{IZkAqZh?Gj@7S8PtcI|by*Q{>V`6DKlj^Qcwqbw"
    "=2t=@H<f+o^-XUdV|W#0ZAk-9Q(HD>G?`Ouwit51Xr58Q#jWB`wM-P`w#Igw;OZ8=bAOr|$zZNOu6PVm"
    "!*YK?7uTyHg83OsP|~Jq$Y`A61oR3aC1QG&^&LgBt=bcGO^1(#o=Dn};EakV__t)lIByD5e7mtIW-qLA"
    "r!=J^mN-o2@M8`IHf)hO<(O)-Wa$t`<2F=hI1<cpVn5^5Ef3_CM4t!<8#qha42TW1KuO+b**mRFAbAT7"
    "n0X>4J8dP;!7hy5-4-jqS?u&6IiM47Bt&HOI|#<X#2>cmBp7rx8Eqi|17bwLMASfG0~wiOl&Kps8pr6?"
    "CWT{H8964$yj)as)?^RUCN~*+#YWP|Y@EcnvFkLPSBTRF*4&t&KOGY{(?7VgG5?IgucwknEcO1925)(a"
    "uKP|_L}k4FSO7dvGNsz-e?faBMV9ESgorwWV9G?-A2T^*O{fdD@FX%LO%;}^g6$Kg3A`mw?K#Q4k~ZtD"
    "F!e1^<*`q4PCN646|lMtrZa-?=I!6_1zptGR93QBd^-LJ+7>-C>=TsdggH2JY?^OI$3(3VP;#K8-8VGT"
    "aSTv|N4)Kan4Z>bw8hVWVW%SOc5-641U_<)Pg^lH>+#i6E_LTGk#dBkQ&<fqZL<bjjzo=WTbAKLGP`b}"
    "d|0MwC}FO*VuQZice>f5{D|Ay#Db<iMjV#1N#Zhgbec$YGf>)dMXwSrWzkci7akHAl)Tw>2i4UREIM;w"
    "GP|P@T9gaIFV+YGm;|DLY3Rk;GgVl4TX_-2In1p`i=X(x5ob_Peid(!yNe`4OO~n9X2S%|gAHi&L2W>e"
    "7}&vVYeDS_GNND)OsQh!<EHt;s<Ev$l7rt3P{}eM9^*aMGn6>8NVP%}D@s(G8mG8yd~xK^?_3$kR+}DK"
    "g>{r^33kBH6zhxWm_M-}vUBzcWw+ZD|Mv-OadNWnR!<nbW)zr#bDdICGSpbqQtQCiw@`8rRfsbc%YF6h"
    "Ly(70;lR)`AS6cXh-8YmN1O$xjfrTgkEu5-+qIr{*=?PyZHL#$ArtyG4U7d)n|M|0kUehUW1a?W2pY<Y"
    "bk69o>7JIFsrNp&?^<rZw47k&0Myyh;s=GppE7k;HG}@nK*uS$4kNAx<e3d$w*{+`pb8Nc$qF-~Cb2ot"
    "wTw04m9tx>ycbMxJTmEko&K-^>o!K34yXyY-*P`u4VdRey~yoCW<*~nGKiCE(!{vGC^i^$u&Nsq-b~K*"
    "^w)Zn=!~P^gCmtosx$S4?Ya)VBESY`%y_+a43ESy<IK>+`(?7K8R2Rf8DREndcY*>VHGH|?yK2|QSjeb"
    "gNL-x()Fa*n@Yk>Ig~=@rfSX85TF9Ol=F;P(yM4`CjN%7lN&^OS8B3NI+?AjZhR)wZ8ZFXswK_TC*Vg("
    "3#ctJgW|NWAYm6+NvS?>j1E$_Kuw%wkA3p`y`{I;R^o?*IAljBzz<=^y$Grl4wc}_GISIah0mw<^a}6-"
    "foLZQnMc*b8-dV53Avdv*q$$w7JwbyMINzgY)1B2P=%gX%c?RbFS>GsBdEpBj7+9e!2J<+2aY`JVp6Ge"
    "r|F^yRvvGAEkM~NJgrW6FFhmVqwPsG#V(taj0hXK=`mwB_`%WZAeP~=+V7qhPMzLZ;!r72=mxm)h=yNZ"
    "Q&aG;sU~#vV6gvD4Pj8{wp}D9I&jngRd}4@hV+_AQ?o>(ueuh8<Y0iU>x(=ib~-aLfeWLrPJ0o1!Sv=Z"
    "A}BFgp;6fb)O2r?wIqlJ0kA>RM31+lT_u;H#m`RTOL0@AeFnm1*{SY9|G6>!oHQwpP}k+z$XCQEw==yX"
    "k#iN$b)A$|m7nIKS);cHDm2>!S9@u^3|#KFIi_qvo0%;QUQ1vfqw>5(9_jp5kOjH}-0&dLqDO*qxb!xy"
    "+fdj}quQkca4Iy}hO|h|8DlFYi8`yeBWSf}!pY<x!cBoO|4Lw10=s<Z0C|;%V*@{t9aJ%{lBbAK0&d#i"
    "UJ5`F8q??kx)@iR-k-|rf~LkfcHyfFFG|x893}yB7qYt}ztkm(hAGoJg68ECDo5F2SHAF{19;NsNB&Ij"
    "A9v$(eSW|9t9*X-@2`)K>+>^x-DhU~j^ksr9KPz;d+Gh_^Ik-sAGLqo+ot`pV*{A^H}vK%O#iQM@J(Le"
    "8$^#<2tk0L$!P~@L5oj?2N#@9gIB}=`9P%bfIclexgTT!@##(<;+&xCO^zda<Eh^~9R=*RlV~KUL=J;t"
    "=aYjM4)78NZP_H#`x1z@aC?QSu*{IA1|lhny_ni*uAd;;J610K<a*_NdN|C!u>;^#8pFJbg9{wWl4>(F"
    ")xWWwel8@(waUXv=aE!@<Ba3Lk1rUq4dc#79nmA0ZKBx4lx*%F5AJ-SCmYN3Nfyx7&euuKgE&`EYQU2N"
    "BZ8v<C8EBxQcLpoaM0-7cLAUS(^tA|1Wz#@Kt18zDpl`if^lMJ)O!dYiq&%;v0P0pP{A-l`(H2)5jWj9"
    "+gm$*X~jr}PTHJVQ<|K%gO(_p&~g=ft{6iTukw&+RKzNMaCxd-)8A-om-8z(qNqztwOA);`rrvyoRv-D"
    "fX$dSAwRrI{q|y~<_k)u0rGfS>Fr(^4OU4tomgjh3BCU#iu0UKJ@a=qCVsTZShi|m!&e@JfZTu7f%I+9"
    "r0<N%i~r*pZL(#(pmW24IKn!+khu>VpR{#~m+dnj;cgCmDq!X?t4gM3{T_apsnsWFT`(-tUvFAMT<Z*s"
    "Wp&g+`I*k(6yTCsz5p6{=3KVt!~W(nD_^{2F>LYz3C6;7K*JGr0Xl#X7f{@nm)2V0)ENF)$1kNf{;Fy)"
    "RLSPI%~_W5OXo){(+o56Fv8gv6>M|F6WT`xc88Tlns}WgOUP|)6T=K=8PGmJ($*7iPfc%Zt18CB2vtBB"
    "BL+?vDptId+Ei|=xiXD9cqm9wCDE|s20jRQEWg-m1ZPrUyqvL85Wz>@gq_%eHG@DWt9%zUD^SWU0E@~C"
    "#FSy#{4*UftKkoFSte<=kXn#M8pjcN?I_DsDB}39k42U`<lHewD{YT`$Guw#EyWmm!^2&Gj(Nhro9IOK"
    "_!#gvkutlJp(})_w}remD&&UK0EI4<t$4#mBQR5nX|uOrlqQ{)h>@r-<U13yVZmw+|Aqud0-lQv9y+da"
    "fdoCB#C0Kn^=r&p_<<lBlA{_-B$gV>Yz#^!hU&4a8SS7tgQQ)iwwZ6aphI0Kdzl0B43EhIewDUSHRS!L"
    ");G~$O9mUVhltC9-3#6%eqWjGc*a9is6R2ySZ|n@1=pc(W?D#2Jgf6rfD^L{Z#Wq!b<^5W5@>lByJ-?B"
    ")udMYlB*S^^=Mm;ZskPO*~m05*^HvI7+0dSsdmk@t7a0SF7||2uwVkcs&{m^7OOKlFthznWl0g>+zm$8"
    "ZPj6<Mh*feX0!6AD~pH>JX|#fM52vchW`piCh8G-mV5*cL~PT`iko1%ox$SJc8~JR!-M`|g5Rhs$sJeV"
    "GBZl843A==4p^;C<^(xx4W{#ppv&2Ep7t%sFsWa}T`Os__L2T;Z&L1R<b8bpQF!ik^*>)?^`!5Q&(F`="
    "^ZR{9eueR!;@2qU^P_#g-~XEKCgxIX_Mh>)H*wo>Xio08`qyBf_ZNeKvh*gJ4fc6WhGwsq_I4nnaEiF}"
    "caxetIDRP#gX20#k>Qq1J)RnXLHa|mmpoaGXQyL%lUTP(iZN-suiAH<*c`iUZy!NH`BW_<9Vup+=9%p9"
    "`Zr>G6dYrUPdicN`RIdy$_?ARiv;eg@9q|BE|Lr(yJJHhwH-J*GNpoN`WQAZ_Hg6So_LmxkZ?wT_G4B3"
    "m`?G+7<68g|7lhothSs~O{8D-!1s!fqfE7|CYY-XK9uURsSzTfBXMw7Yq)><kXkwNO6GdkYaWL#nE`B4"
    "C^3<&4pxZi5WvaQH;Tw>9)DtrnGdYKU_p@#<+$tvW+b_t7Gz;W6z8N_7JH|sNIr2e;6U6n$n~*T&(lIE"
    "&vZ@s(d(tRdiYrv7Y%B-9szCVp%=E@08=1x(>*ecJs&Kqk>eEycVi}}HsruB4P*|nJnhOZ<BW7(mt0;L"
    "J9)0JMRo7wf99C+jntb71Y#a#Iza9-FkpeitIg3JofVpk+nP;*O<NF6o6*N;KZZ%x%#QVY))Apr2~&2t"
    "y_Ki4+}vrB7;Ph3D4P%!)ikTMXb4^^r2kSj3&((JL44TeG92fY`&%m;Bdm02s{@s`<ESJw6;fqs7tsZ+"
    "*6R=C1XQ<bOs5fSGjXyqYq^iwbtI@4s0&wTjwzIuMDgj0XX4BG*+4xV^OpcSg3p2rV5x#Gt#ituq%(gE"
    "(MT=musp*VLpmYqG6*)%ue}wiS8DsY<3aqcJr@jgM}jl(GPMS(gNMTPaGqK~1vq!&+dAu>)*{<uHW;%S"
    "Z4=F+oNoXWR_JLQBzv)jGZYi^9bhHj2PP=|%FrV?x8B5XirHOhkF80#KR<&|QWx;HRF%<mzKUFZt&Z48"
    "i>P{;q*dc2CehQ-I^%tnWhBO}5q{nk>^1pNh;zvkvA0HKWe5#ty|E_=wW+WWjS%VV+BOF088xZuPEGMO"
    "$<j0E$(F;vn_%^7(y!4)YJvwTM9)?+;w^45E@UMudpTGR6Kx5aJ(_1Z%5-&6m^IZLRFA<CGzySb&JkpS"
    "d*4RN+P>SUH<y;SuJlTG{AQsZT&8^L$nS1e_Vd|sN|hUBxEcbRS`lsPex12h)=kj|4Oq|pd-|N{#lBg3"
    "P?LuXJ7XAoHi}4U_T946nvOl*4MSM*?fM`h1V2NNp9HJncXwzFdE-uwJxsG$ZNi9xWgQehI&PN)G{Bun"
    "4Pq&ka?rtC2xc#N1(=g|e-rfQzcrwiX?BJytT0TnUzS&U8aWD?S0gznyz-k>;J<OxjI>#}ZwEzvG!91<"
    "SHphQ>mN{PMz}0+`5RMGSiim4Z?TdaxuBt90W?%992XfzMU<eiHwb1L!rX=Kf5tLu__#OOy%pL=i65Wu"
    "cNdpG^T!DFy?n<%UthWZ`K;e}zxST+H+tV}f8zIh>|f=6?B8GMmlB0e;Lt9Nzum&UxBoA0-9lZu1;Ls`"
    "YY2%#$a5-lr4Q;8v?~cN!dcLu1MA)|2~6{nk};gpQzF*B*yBA6)~bd+R6OiCkca4`!T5GEc+%VqJJf1d"
    "SotM^>AzGwgttq$iEAh;qT~~DBW1V-4H7COTj-u9@H5}fQG2D%fnz&3JK@inJqXnBK^<}}r%F@pRnQFB"
    "0lcC{Ux(-Dc?BeuF{Wj39H()y6}rAYg7X@189$7+#eS5Kj6I@x{e5J;wgAI9plND}_>B2FXjcS)^7$_7"
    ">Vor3#t{~(oXz57F!IfZ+Li&B{C9bpn5U{bI(24vCQB?D1<XDiMpI76gJ=h#$mo_HF=vOhrPHIF>?GVJ"
    "G0Mzu^?w8j1un&83+_nMaviF5O`0<HoQVs+h!vFbD=6jouY@&ej4s79Zeho*bDw}3Iz<!bf-vWUi&(qJ"
    "?M|LmU1&_r=s6t&wm<-2zHp(?Lo0`$Y#skS=0%z;qE6Jvwf%FyAS+FbJBfTS$ypBD(X;KPY)!UxeLxQ?"
    "$ziXW{%iQ1SN}@8X%|x;)$675j1`r~cet+2tksUr_-Z{lX@-)>HgB(!>}SK!FjEz7sE$kMZ&_ZY%5@vJ"
    "2MCaP+H3^6WA5{~*kuHBLq{`uNwL>Oc@b;^EW4#10Eo?9=`fASZ@oBH#I;`85b6rLRD)&OlUrtr892Vh"
    "ZDYpDs27e?ka@eBIYy)I7f|VzwWtkPm^#I?Fj2><1F8#%f}%|qGNpK-Y7@i(uDX@XQmoU6UxS%zr*ve5"
    ">uvy;>@tX|&r^TPNrh30IX%fzS2sK==KJL{eM|ofmNt*K8A{#^0ELdC1zvQ%Hf1uyYd9bUuOaR2C|n5A"
    "BFIJE6G7E4H0-FM_~6i>k*oMsW9+;o8~#w!44AIiNC7C=3Zwcgifc<O4O~z$n*b&&)Bh~o3Ty(p29@h?"
    "){hNJAj!I-!=6KRJ#)HyyM(=A=o6V@bbr~|z2|5gVOdw%U{0keQj=lUoGb+ZNi^?XmB^$~(NB1^$CIGU"
    "yqhGj_Ou1ZH!0Oqb*h}3KD9>#3_{;h?H<QwsUiCAWik)rm&>*`!J6;Jz~Z-Ojq1~0Y%P;9Az(e>cp~Vq"
    "uTyCVXGt%+j*F#E^F<TX@IEkvuyz?~IOAN-Je6<7S*R2AzQ61%1GJd;egV&+1TYsdGRN+-%^ZbQwuJzA"
    "IzGo9r)7_RX#_88tEj$fsCh5w<YVAIKA;*5#ywio&xT>up(N3<nl6(FEf7T`p$F1{34nw;(O%+b(L5&B"
    "uR0E?j~Z-6ecZ7comAT%MaPG0Nn-3GwU{lq<LVTzz|N2zU*(vb;Zt5`FT`qbuj1M<6?GsTCy|JHGkXzh"
    "jNA!iYy!M;3IDxgxR1&D`Ca;Zt{<a+fA#Nc{28hc#$B+4@E+>NSO5Gh@y`|Bug}`w+t=s&{p(Y{yNSOY"
    "gS&x$?ifT>dLcixmHgxs7bo$N0XBoLUp1_Cawu)<jE`(S)IgDH&si;Aw()3lTOm-7ImgobPW{M_c(nR+"
    "@P=j|RqSM6$s`=(oR9+*-h&JJRf8S!bCBj9xOq<a`c($qPk?W8;Y57I7z*J=^-8#Ulmi)O*tTLksalwd"
    ")qZ#|1Id9SmCc4vIiA=k_INBm#9X8;@#q2Y&?&_{EXoKz3~Ngc?VNm_)fqSY!s8hhP8^q5X5c_GW`c#`"
    "p_y~jhh_XAEW91Z%yvgkj9cj<TRHkSBS(;vh?v~yu}*-2&{i|T*xSi`_0wOd>W6!Tn&fUgNs~E!K;Qlu"
    "ibkhT2uBBk3!Mr~=?nZ<wBCcgfHIlY^&n`lkcp}K=?g)#OxU4C5C4L)Lh{kN8U$3I19rh1-X!thxm-*z"
    "hi8|ClEp$Nc+3@Lc!c9nQMDZ!GpUo0dDWvC%x#KZM8JRKUdjK~EvPiGLI-NaTb$mq>(n-5S+6qRCw_WT"
    "DH$1>yS!#m;r!oS11rPZangN85Uq`~%+z7NG1}H!ocNVP&hn;V#sZBClo&MCo{?;I<%v-BZGj6&2`vk?"
    "1`@Z_9Q`|xd@R!jQ_FSsM$G3(Q&c1GyDYzG@;G5G+udmTcx5NnF!Dlo(c{MZqNW}y3#2n@I9lpnZTL8E"
    "_<}~5u`**LGEE{}wys9(%x#IYU!ExPQf&U@9AeX(>&?)D4TP5(ss?x31bJvq8i!q6sbXyg)?X~5P&L>g"
    "Gg%e`kxNfJSEns(JXm57$dX4J5(~0bWattyEU0tHq)TGHAHZQM0aWhZWlM$0?<zu&UrOV^&;hCoCL|0B"
    "I2POr?%9%BOijuFq7_8Y4J;_?>9Dt+59AqmA~_*ghmS5^3k7z82Yowi_sP{|5?--=S0%)}{aVf+*z|GE"
    "cy%}qLMcUjWRM0wt-sWAbS#mutBTW~g-PR0x7(t$Qw60d-@vz2@~lV%dgzV_U(GQHn`iRPgALs>=Kf5f"
    "rZtMoP_bM50GW!sYV$-=oy04f=jXHmZ**E(8llpj+h9YJ?6L<Jad$=C3Z$GT>vnXJR6t?Smlb-_04s|R"
    "D}yiR`vEEwS*<7LjFhxYp+x86yzvwR_hXhK-4<4)c?T3Oc<nY*ZpA58gS(pEWhp4&C=x6qu0l56D4kL4"
    "m&GwlrJ(91$?CA+tjNq=dL=GF=__FMm9h?Rirzs}@=t1Z9Yk5%vz`An?4i#LyTcVv852Ye3PYlb3X>YD"
    "m$@c{(Wd(g=t1f4G=q*DE%3^+0xG!qcCKT5KVvgbEs{&h$sOSvr!ArPK6<)o&QwE1Wo*TX67O2Uj`xNb"
    "|FuUL<>RyT&yV_beZ=qh=l%W4AMYO@pS^yLD}VjTcRO>pWhs8fkMjQU^>MZL_q)>hZskw9-hZ)>T>t-b"
    "laNP!AtCjpM~HSH$<O5TsnQ#Va1st+&*174VJ!#BxhinUtngT|B>u!r=`#+VTbhNLuX^Mm@u+{!#4>{#"
    "<Drz2jRIpek@wqhX3`<8W0-3I|8*);PkH7_AggA2XdV#rF|eMAv0Q*8hZ0lcHPGYDF)aPE6)x4pcK!af"
    "2-Dm$Ovh`sL_UmoBRs$CGzntT<al#Tlz4Qw(kO&bk}&^lhe{BkXx6hceRw$e{Lnll=QL^wbf+Ln4B1bl"
    "FN;BhNUQ%GM?^t`7afZ=&1kwd@-asvSdnLG?HDr)>$Un8&4d853*sSWyocHw+(auT0uL1(?;-pT&;u|M"
    "+P@T4RDk0INZA8G5=<&2iH_@mBb7x)Vb+wBe^MOSE1$SWU~ot-T{FVgD#vaRb=!kzvCd7KF+zR$I~%Mc"
    "W@}k2jF`#oIXun#l)V>!%@zZZ*)A2|bqe9BI(J3Y=b9|ou4-lcbAO<|Alh%#ls2wH`*3H+jV{Km)iRZ6"
    "S?5e<aA;`VwLd`e!x6*!+Jz_|posXIv|7rPT#G1U+zg>}cDC&OHa9|cb3!kUA3Ph(YE=O?yz*9yYNwWY"
    "1Z$67-KYZ-a=p`Q_3<gjKJ2OH-bKimNC2q++p8IdPBZx4I<PpRgU6t%f~9<^d98&Se4YC%4Czhfi>?+S"
    "DX?Y=!q*ldSZ-tQZdHFCn^DhSGPPST(A*toER787ND~KJDoX8xB49PzMUY07sM==W+d2S@9F7UXv>Q$Z"
    "uCQdt6jK`^%Z)J$bEsvjCM-Ma;50&E5d)!e5DN;R>gozh?o%)orFhyo-50nPw=BolO#Ok4OXH|sUFGp$"
    "b5`U9+a8dXD}fYs=x8Wa)mL2Eld9j9A1vC8*(TsOm1DP$2)g35IxSAVc13&#as*YcVUw&^Gl{fI7gDQj"
    "o<WRshu8>L?iOkgn&qQAydwz23hPXHDc;7LihC7iF>T^B`Ya|*GH-5qIxbjk5!df<e{xEEyn1GMaw-$j"
    "ATTy)a-0?d<z3#&O&IkrL!0C?bPz_ZDYm|cl)jt0vIy#4J#|bYX<cLq=h<~v;{uRKN*6FFTm&USczSU>"
    "Hh%7-)3<bk{Tu{3r$Nmy0QeauteY=c_%8rwn72{Eu8TgIEo<Wj?eLK#mv0z_a~{LGqB&aR{>{v+=$NkP"
    "6t!vdkO<H&>kz%EZcp;)$vmSBM3MbFR0$Q^JCrS*M9$gz1Ig4eZk|-}zLU>l!uR3cL>uiW<9(OR@l|nD"
    "tmS^to#_yc8~1TWA4X9^i<_4)T{oh8%9U*!3%+oAxWy4^%|%Ak*h`zP%w)6`;!%a#y8X=()S3V%TOp-5"
    "Z|l*PlKyj_@SeW!ZF+s&dm)MGeJ|j9;njY9Uw6s<p2AlT-(n(39M!Im7Q>(KdyijzT<`bc`HOu-3-B*k"
    "g5=h1>l4P(C+L-s25H-Oj<%C**NJ~blX7)S37FEMf+Qz+%8U5}<G^xx7~!Ro0z2$Dd$r?i6d((NO|)fa"
    "GHLeUF3O3f9pr9;ptnQyipWgI<-L5&O^t_QSk6FVmsPoC51G64a-`TJ-f-b;Q+)v$2TN0DmaF+zWqPHz"
    "6BMJ~SCwWJd9pk6Q0wd!+`*9(GE;Zf#5mS@euQ)qeR`yt<ChMur-IV$#LZ0(CGXVt*cB(}@3lf>hyZ!D"
    "6PUmysdG2FZn+%aaFhbn;*=ibs}V!O)4U%42A5>!pkELK4ko`62PV<#25bu76o;3sF<a>3t{|+gBBh-2"
    "DD}em<!$6?n2``UT!+^^trt>onpMF|{G=CPo@o#VlB0aaS~@hsWK2>GIrLb)QfcwnULy#ULQIEL7|7C2"
    "VhK%83i5Dt)zKH%!8u^6y=%3KT+_~GL1;K7sNTzXRQ_`DdHFT5|8v72`F_UWwAni=+LnRPl-b-bxJ^U8"
    "GRcG*pvEZ?oLFI84s@4q30k^bW>xx-d_daDm3(k4$QmXN1G!zdNrKsPuq^M=b-T$5>YjrAFzIKI<goSv"
    "Y^Vom<|t1den1oFi3r6$<w9CX8rPF&QlM*@5fCRGfSReU!E7_ELaoRJFUrp+YK9X5{x|ceAjdK+r-K;Z"
    "%EFCLPp!6(7#>u#Gf5y>WNH_w07g>AOy*iRiF7RjBcQ>k;1R6fm`Oq-3oBVDxh#Z2r*rQvsyT5@A+L6t"
    "+1z5~EWwJwF_x#}=p_3eLf8L&0wBIL){&ncMK<t9&tnaG-}0yAA%oYRvtUHCFRB4?nAW_uEIr2%C9Pn="
    "6rUh)(ri>mW7IPUyYD9h-v_l96zh=eNeP(5tR!yAobaUhJK|k;cc|uURi#4ftuNMS<eahg?yEab6A0JS"
    "QO-WJ9%;?0Wt9a{{}Zl7v_ZiD-*}pp#k%KI_3lhGhqzogBdG6(iM$?p8XN@&BQzstxz4PcfMl%m19he3"
    "$}Z``Gff2wG6Q+HFxwC`xg~=Xds!$#g{n1T01?IEFJ$&GCDg%HH@&l4Q8Xps<(3|%>3q1JBZV2KE+5IC"
    "pe$+JMJG92_-~-241nPp-Zx7IWW-KIr#?I2E{K-1q$a<!(4k5NwTaaR?-B<z!zXnea}0;CYjP@L5SJ}A"
    "vM%$oG6y_>$c~PTnq9b!RDF&?-0G7iCv<IUz3&3;#H>|v>F%9Y0y5+cpC}p>4%y(v#?FRgmEhXOi+K#r"
    "9M^7lN2D<V4yLw+x+H2mfzWGJ)lN%$HypVb!VR%Jabf2puUElcAky@*6*(!GmPbO|E{yx?g}8H#07^RZ"
    "8@2$6=B^A!MC+CycdC&MKmL0Qp}44zkB>j)y^pUeg!cZ~(`UQygZTBG)iK=7O~3n@j~M%(^5@TYy8k~}"
    "*T4Vy)50&P!R^7nC>T=O6%6+SUG&Z#`4d~klkNxVONdO;<0NwlE<L*#A?=hMJq$D!Xg-uJ9cPPZO1CK6"
    "V2mey!2NPnr4XEAK2SbNYPCu15~=dMjuXu%6$gc*bD<6(q5HK?LXyw!tJWKWW?$E_IKO`{1AGjG@HMO9"
    "OzGCr9br;~hk2*Rv}@)K9?F5SV=Zyu-bac_`#qwh)*kD};19H$DvIa$FqPv-xnGbF0#>CLnxK66HX_&v"
    "TMmqHJyWmo9Iha`o_;&WWhhR?ICAdq!?-@d{_wP@uGnxKB2TpO97h%b-i0e1;FG9olsb`WK1*vtIsF<P"
    "&cT7nY1CaSU|yB)b<_uRzWL>O)wHMTr||OVsbls<a?KfSJkXPbWtZsdh4GXI(>bOiEvt$0iMrmwjR{U^"
    "`R9qgylhD@eJXi51sRM%@>$2$Ou(xG)Y%XcCc%KyDA@McE4<@MIN{IY-NmiyxI>1ID``pFuQDBN2n1#}"
    "kv;b69zaUcQh-gQ-G;|sgXXUI4x&)kJ9Rkk&pA|FeQMIMa)jS4$E`&z+}Uk<qaBTQkMn9b8V{={uhp7?"
    "kQ64@E==c+coDND3xZvjE6h=zPnYQ-)4?}A1Ebb<-M3tKnt@PYyDW=nOhHZYQ5O<SAq%HMSbDZ2QECrH"
    "v0RvG6I4w8sREKn(29C!QPb>@K!IOUu`T~V5#sbf)a;(gKI`En-ljWG71q-OuU!Pc!4i*cCBbsLk2RnL"
    "1pWf}00iZOX+!tTGrv0c(;5=F1v;Wo%w?o)7lA_SZb)*k)z7Npf=4A-B;lz}T-aI#s;vUS*7vx=&lwee"
    "9FfC%s*0L1Jd4R#g=0t#8<g=QP0d)Y$DmlX2VtO5_$U)<hQ)M<q&3|a>Q0IyMjO72+ya6v-IEw0P+Qho"
    "$eovF7FEoAP1Ut56Ev{2%4$*OB};eE-X(4D(JYU#)<wgtbqd8Cpt>an66r855rWF;BIv8#XURs38_$4V"
    ">>+7I@rI9PVy>e|oEaY!b|Deq1y%8y)cIhuht<SK&0}&)bm4NYE1`l>lECCNhL!zj!yUf*fT?o-9W|P_"
    "C4B@}kTl5~udKKYkZMTqrP{`hzR3Ff1#aPR!PQ-3HtE5OAJ`ktVhF94Zb80<kgOOy6eBhb*J{xUJ0;y%"
    "<GqV&xF#4UdQcH~H<u01Mec>^mvY^slpS%NJbDW{oQH6Bk{$$}t#r;f5eZG{%bR@)7>wzMW3j$!p{7Pu"
    "1RPfx>>*!QnrVmwXPAt<FmJAJiur8OoYaI}l5m|M;vZTy%|P;9!T)D7qCdIUHtyo|>po;Z!e{Fr_oI6M"
    "eh=ZJ)X$HP_+3AArIh|z>sS6xpP#Li^7;9B7xcfz`!2hGO7nUg@7KPk+})?!QkpXoN1CfKXk?SV>SDEq"
    "Eu+P1!#{dZl1B5WP0yvU%?C>r)iBzxSoKXqk$xIW>rihtC220C*Br{9p<^*WQgdXji<8l#2k=mx5+(_B"
    "fZ?R><*;>YKW6x-I*#Mu94@YEXfogelJ|PG6IQ^H=?v@g=63%u>P<H4n8{-gz^ZtnWyR<VB2J?eIUJ{Q"
    "Rx%8XAnjh=Kz>h^IUz4N^Qb(xRme$tjbDsjZ@h|iQ)Ace{oI+zPbJa}F1&GIIV34koBNqNVWv3O<dVAo"
    "P@8N0WE(s%&kdKEnXk1u5lje{^%^-=#^D8(ewC*iJcoyJ!lhMA`8+$X*xUG!w#4vQo4d(lFjpXSU^g7o"
    "p*GJ1d+CgB9y;qghGU*2W;E9D&%8dht;aTERjP`O%dpNI`!FZMB$(zE-M)|E<U)b@y6#yEJ7*k)O(1?h"
    "!7=lgp#l}soX8DwEKFTb@ooplOw>CbpH!TP<S?DQFY~P?gbCHfyVU(omI&T+;;aZvteffuGQQbFG+x+1"
    "yQ00I%8(_o(9~6J10CD04(rg44v)FRWlM_n_MQ|<EmTyV7N)o?QlYmw2qLvt2p7eFe49b;P>?o0F0A8N"
    "A@E*pnvbX`@6N_T3W~J!cYQ|!w!&yIrK}i)3vU=tTy|yl1+<kKGT@_Na)&gX!mb8#iS0cQ@o7Z8ps`m$"
    "MsY7{V_l>9tjrK)Zjf|@js?1%^Yf6wt_3O_Aub#!AMoJ^Z&=D6*_vRg@Ov@2m3N{Z;RcL?)z-k@MPjzI"
    "kL9SOo_dgc$E>J5aSbdvR|lVJUYA-A6SGN6eVA%!;YYkSa}v{5(3hfk#Uwk>Aa;!ZRx%x|Juh7J)R<or"
    "5+3QH2$E37@E#vg-14x6u=BYPF31NbT+211I!5iR<c<=ylQ<#hNo#6#bamKqvYgg_Q(|*+YIIoGYCh@$"
    "cyyRyoE*+MhzxgAv%;s5S)o|xv9i&kF`bI0uCjv?%BYHWak$31w<AsDHOVi8<4{RF`*3H{Ed>2hNrWXM"
    "gi@23SiYAaUHZG70(!q<x9Q12D%D{+kQnA6y^-_#lftN~q(s|&<|zRTYmD8Du*SZp0q<P+P~mJCRf3O="
    "VyY1gfdaunIZOf^b)q7!0gaV<ZD~&W<cYinWCE@!oPHo2!*+Bd?5QMr$m}egdqIddnfF(~J8G;N02?2`"
    "6w!O3KDX3S>aN(Rs@BX`uCY|1&oCLuT)fyN4wCDWyTi>aU5XPHB}PuwiW(7ZhGYCZ{3!pmD8IhG?{+hN"
    "l=t`c(b7lDA36O=?|;5N@8^6!??2zUzJFZ#&-lL5XYND&@q2IY_b<7h$nW%m{yV+kT$JD6dgt8SuW`}u"
    "$`yPK#r)+Yp0<S7UpdK-rcgu;#9r!<H>aA%-GBVYxG+vzJv12ISnI*GabOPqKy9jCIG%il>@9scW$fW3"
    "n|7#<r06Yp@d3yuBVMNhwrK%N1XLVKeq_ezV9`KPr=HN6b~5_JT-He<Wi|u#q;aKZH#hTvR#-t<=N`bD"
    "LZ%wd7tW?BpJb#aE*G;O9jkT#FOm#U5Dg%TcCgPOK|AOY5yZ?SLY(8f$3NAp=Az&(%Egn~F`Qc7)tZe5"
    "T=|$rrYoHEpc?O1VzoR3!D`_66x9KUs~zJcq{NB1o;m<W>v*a-4^m^AhYkSS85bAa^;$irgn_7rA7M4P"
    "YVJ5#9HbScK@-T$LksR(VjFt+pY$2#{K%My2k7x=<NITHQ9SjhY&|SGQLi(juUhFnk$Z-tUPM0Cjk~#`"
    "+7<wkV)>U2Akz%#&5?cu`v{2_-SOT4kjpM+8-v|o8t;QRG{?LzyRd-BYJlIcbwMU9aSAoGHd9!y)@mn5"
    "q(ztomF&NBHUM=4amDEqs-?p!WD*H5Ng00dxc4u50cU@3`Z$@zY@sy8Y>Ed0zW?pEL@pahSNLfFGN3yA"
    "B!ki`P~sS|_9nwQEERxDGGq<u3U-@D^%BzQsgr;)d3oAw0qIJkc<S}~lgomKSrpVknF!V#>cVVO9UMCe"
    "^VFqyr{f}C;x)U7je8F;fchxIN}DzuG*`^l@}5mjLqEu2x>r?m-qawqUelt*`ZH5xf!8>$JwoEU*GPY>"
    ")2Qq>`;r=H0$&h?@8vUe%;ETN@04ZxJVtN<PPOJ*p9P~SFz=uM0&KJZ?Lkd4DQnPL2D@?nIAgA@o;m|m"
    "xVUJmZs}HY=<~7GR(C?)SVT@1O>KwbHRG&Qn5*nsLJr7>$Cy46)k;yT35$Jmis{yA=ib-xL(a`_uCST0"
    "32xoO#4=w3@~FsO`cuVBt4LnhniCwK^olULWBg_?e793WlH2B@!oI|O$<E+2?b1m#^m7eWYmiIYj+M}&"
    "(*c+ri-phBkm-b2MeF#cvo8XsB=Ajz*m{!(TPv-Zgz7DlVny#t$9SXcq!B)%6W8ttea+0klH1g<>b9pQ"
    "5GItR48&y#zU^-oZJ-q^Q;~%LgqX@Tc)i%lE776rvQl#vT}nsQ+^a4bY4P3UpqgYsguixTLQxwDWu>f3"
    "F-v(}1)Smf@EFm4h&BK$N=&iE>7IG5V`=(_Ts|GNU^RB1W<HB60C#(s))K{If;a<ZqjB$R9S;cPPVn;*"
    "k1ZQEQIj#4rlvv4_69WEZ)y0n1k<dPE}DpzVTHsHfxG4Z+5>!z5wG|Aj4$<1j_)5|_XGM0AAkOgE8Vwc"
    "zi;L=KE6I{{cQKXjpMz3-%Y^XhWtt6J>=h{nf_l$GvkFcla?L;LTMd7xQxY~X6`mG5keF)iNz7``qy%4"
    "-kvIMATsoWpACVe9&$BP^uwI39%{8gx_uB@jd$FEn<3gjZyw|dXcYD1pc{7BkN<^L8PED+^#?kNJj{cI"
    "j0f*2!9e*l(iCYNX%nPVaKgim|LM{cL|zXbw;jgv8VX@q#PKl!z;<9*pp8Wb*v%BB+B_0wrcMm_!*q4K"
    "t{&*@f<811>;wX`8qU@?MA9@^0d_-S9D6i>5&uzCg6QbjY{h;$Pv-3~|9AK&@0xMa>L%g&xw-r2^cQR8"
    "kji%7Cv{57kvnE&4P_i8tB^VE))7EZvTpYr&vKA%nHMvEJmoc2IS_o3zYphCfuf2Cbak<NCbCC4f}yeN"
    "HmA`6c%p!zFKecyXn2HKW*GlcmWy&y8O)oU)22;3K?NI2Aix??_mLfw9SA^w_+LUd()_zDHz}A9P+CwO"
    "QE$WvS`4!~4|XQO!U>w$2u97A$LN|-<#!kqi6fe6AYpeka-AYUzX;=&?r}Wjt-%aF<g54v(n#}%`?VQm"
    "D9a;H-MP6%oohwcvsT4cm&Zv)WdYfM#-52<clb({?TbjQE$8FPVfCg-h()e_w;VSisu9RStQY3TkpiMn"
    "mYdsmtr2KbbRJNY(FzA$p|p;$<6$WMrnL}zrT|cRYam`G)UqNQkZNMnCHsRg7cA)D8_|P+ryWm?)suhf"
    "2MjFKh9CJL#y$Im{GOi@zyXHk^fm>zY1s;UweQE8miP$v?Zdh#i{p>kr#KU0Q`hEtTYfUjw<uix0Wv(M"
    "k@g6sWtbeu9oe0S6E61HIO1_8+NbyH+AS1OEL4^kY!Q^%%itzF^IcL~3P)71&bCDD0g3|m$14}wuY7{H"
    "eL<l}%P5LemFK=PsYr1htFjmVVs*m1ntthx>l7*H&1eSjE!n!%oMxM$xmJU-BHqnHG;S)}2>elP{C6<V"
    "6eB{F!(nZwnMAnHMJS259ch|!iR8-UZmY~(<B`%%n1ao$X|Eic0Iz4A-s!+ec&$|QdvMDtRz$@;sF09F"
    "<dVxgkP_^8`IXko(i;)9r(`DWWx0Db`Xij0rQ>df&e72=JjO7~@(L4X%AQpKN4TELMv@*(P?IqDVfmGV"
    "-sralWz^y5>`myRTBd5c7-xh4vo9{Mtp2drO|fm^^FAy2n%Ed>;M#3{qS1U`HwaSoWK>OioGF{FpPA!v"
    "P>w}9#oR7A5pLKCh=p>Y=Vq#lth?>u<T^g^T1R48Z7H4@4h4df^$F{LCbM7lBZlwy?;bv-rA>d{?<#zZ"
    "??2bq=T}#{@ZI7o)T@4cr;q&k^{2e&KjHhX+yA_OeSQ2U%#430%(U=An8{mNUOm21!<cQ*aNv-rws{aj"
    "*$jxLlhr-0i1t^SIVj;oD#w^xr-&FDwnIoU9Sb#Wdz+th3|n76S{)PAb&in;rN_{&ih(D++;HmVF*i%K"
    "h=vc%(^{t_9z&0@ZzE+zNK}Z9B|N2JF*}F@|1&ajbm<+a72*Ss4B_&bUmn`w5xS465i+j9K~&18uEv~7"
    "eSc)Xa?d`>TNO42>kxBkn%uaW6#gv;QLE^}$xj;I(dGswUefpsYkM=J{%1+fP}%Z6pE7`S*D3!vMd+|d"
    "@DTYIG<}B!$p|bwBZ)J}<RL;ztUS(fe(^ApE%%^<>Y9?A8OLCNW$tU>G=43~t=nxFM<ctZ7(LLRRG?-u"
    "!D=aWIyvPNQR@E1B18{JnH|w$R89WRvAy~vA}&=jyo%}Qrh<VC<UM_B2E@*qTu`zvkSAAW(IZ%FmRLGe"
    "HkZi_h<r7IVw*3+a#e#_LyfnY#?6Ov^^7IaMhfs4Ob?||l+TEmAeNqt*|2Kg2WlbMCLuk&CTDpII{+)X"
    "-+#t`1YJ2EZZ@v%Xwg_1ROR_K6(E#J9KdjyMkF(MRdHAPwWR@xTVp!6m`e;uZB?Na`1@>&J}ZU=6A!aA"
    "qP#&Y;~>}`y!|)FMyo*-pUd|5VrXEk3x(g=G7Fj1;i{Sj2<$gqu)?Hfh^L<OwJLvx2D6~^1S~EnyJbrm"
    "nY+4SdQW4Q$Y;`Yh7h$iu?%jF3IfMO@Y^b8^m7<s+RsX6x2f8N)z1Y>#LilZJr(6F#2K-+h8j;Nn?dO="
    "_3CAOK$i}+bbCQ~5Pz}qAlgH&3L1Kvi``cnCdSL7g7yYgG=?qgctio#HntPfPPlvBIjORnW$NQyO9k^X"
    "FNgeqNr~RPMy<9g(|tJB{J4riCa$fOby%QV!)?!-^9U^D#HAi!2SrkDne^Deq?4|`Ku(%i+MO^Io52=~"
    "$4GnBauPyxSLQ1}gEhs#T*l5kWxEtt0%Af~;}MwXML-x#rDwcS_*<ESyDj$zCSp#QKwq7-9xIZuO8Q0u"
    "F<R<@?kE9$eo!<f>{ROgNdu8B(ps74KDq27&9K~~Ni*7vG1XmC{QzZ`>!YqVkP*C{(CDX)wxt9(k?s-}"
    "4@F*AGiaH?MCCsyD+x_)n-2f3Y{Tx{uQqLJ^i^~@VA^xvK0B8^`)fnlqe<8Gr-^y0*a<FbMhmHD3zqHs"
    "#oepXMs>7u+fqQYB(v93M-ASkx%#~?EkM)1UCs6H;!8?b><6PQN;N-3)=<E(swPKw6ZW4c=AY@~{jR~o"
    "$NT%eaZ3LD^VPnukiN_3b&1k`y{GVfZ`zNqdnf$4%l5DPb6ua|{cC);@cC<EPSyP{mHGWCURX10tgb3L"
    "DX0-kfjEYf?}SQo2!Dbp#fUlJ@K~oMHVAjC;L>C0rmfte71%2ZxGWwkHl3=$vNBP)R!!BjEMV4AC*ve2"
    "?Wmq8*y=tWoydzx>^RJLHA~j6_K3}{i9KEC#NYa6EDa+rz_EBLW;60UNdt4lR8Ljwp^#HdphvZC#rrie"
    "xmOo-4Z%vWr<@J}I)oER2}Ta;4vXc)kW43w(U8hCv~E;b454~IQeM>EOUoOP%rcZ5C;cx&iKKfgT9wq9"
    "m)Bzim6PhZfP(8lC?D6+50!jQJ5)e1P+@aQ)&k_Whw0zs*ia7rPDxgcq3}c?mW6QSLx19dd7nk{qd=WX"
    "ftKmWN_vn+pn>@`Q4FWYB^%+4%~Q2YuOuHa$0I>Vw-@GFLJd$f#`Z5vcHyeJ^#~vu4viu%J5Mdox*Q01"
    "*9jbq6`FEkd53n-nr#P7=sp6-1AAlIh7gf-SFZ9^;W3MIq5E-8II%!)(IV`-mf8pAo~66DbmgQ$Sx^z6"
    "J2$MXe-yG0f@~*`D9|G?@FU291p2aEd?aXwh<PtSscCx`;w*hI-wH1jP5?)V^~Ki*7K!pd2(r@?Eqa~Q"
    "YI;q)tbpt{cu=OrQuQozhcY9YA69t4??pO|h6RPzBdo+QonVBDhG%4?n6eR)`(z|N)^Ig!5ecn8dUA!I"
    "iMfkI4FmStyaFl+hqB%Mo9&jw4v(JIE{O&MOLrU^J6c#dz?4Zyep^{SX1dw50L(${ga#pZA>_#4v?*(<"
    "y_RLE7woM0U`Uf7sN)29AJl7Au8~fWkp(8UI7dR5&~c%*YPGPZqMjiKkTFC?r|py1kC`bwZB@CxUB^-^"
    "h@T+?nCB_S7<RQ8h}<CA28cMTrf!KaAm_u;y{*2?%ggL*6(}EZ+<H?<tU2UZq)i$~Nw!{zEl=pp3l>V<"
    "%kkx@CRgH}6>X9NZt&4ik)-uw38E6w40t$9DRj3FsFxHCw8k|xZdJLN=O(fPbTv#N#IYEA!r+{+RZw}2"
    "#Xz`BW3jlP8CHplh+h)B8O0j8nv`Ag|CF5xb~CxrY&S%nSD1n2Xx#r2Ud0WRngGjo|Htk2(E22*1|X3c"
    "af4-9dpPMfOI1#74-*YyAz+;I*U1xvIkBa2^TVUq(PpRGUx#KL4s^E%BA&7V6xqFpdAU&|!4~E{jrIeC"
    "wZW)1;8`7?*N_7A>X_@vQMF#VQ)PomS;tZ_pL_XcIpmO=2HS$O)pxxbHYa|0EwcJuopL5|<9KXQzvNJ1"
    "5s$(?dL!p4B8uCx{jqFkQ3)F|9M4vmP6kduuX;JdjHb=2Z>6YI?|iI?E2I)hqBX5BuBb8wC~oH8J4`>@"
    "$9WMy#@BECj9>lyT|U0rNBe0?psHsfKE6LbepCMb_$t3&wR}bKB|kn|`1u{L^cR=h|Gh3xxx5Kk*8Ey|"
    "D`ey(Owm{JF2L4Rn$|6KH{{w2cMZZArZ=;)HLK-tTLB7jHT5eA)rN7_cY*=TrD<}xWcDug4!eFh21d(x"
    "oAdEIEsM|biX77KqUZiDYBn=h%Fr+;20GuClAN<OU{&*HT=DHU74OKCjeGtk1$BGvcXhdDwon0#d+<2!"
    "h90SgQ`GSoJ(Y(A$1OY(;*xxYPnz)n9b&tcziT^Jc~LF?WSAK5Ob!hk!GU&SN)pE10W9fiB#Cw-jK1!G"
    "f%cz^^33Tf!JI94zU}~$NxbW9-HDk*&E&otZ?x`Wy|V6d0T6VPcbkU=*OXWU=joiEM!IJ+nk@%ZhViG="
    "b~g&9<ggvvfxyzK8i?U$+(d%sfbQwe7s(6#reV%~uM{m+bRBC@>;KS}A4YDdHU{NYFL6YfF&i5caJVIg"
    "bQRPhT`#p<b)A-3)8rSVZtWVjN**S=WgpLtG>je8tF$&%!beJ-&_u-dvD}R6)uqgw(dlo7>?UHr>ht9Q"
    "j_4%KPSjJ?iM7=Lb(pLjZ)XZin2t;77KYV9{o*gCwP(YwsTL8tX`91^=x0G~<Sn8H`~eM0>7L6m!=;R;"
    "e|>gre*qYTtUWj}Fxwob2f%&g#d1;z2|~US?d8VEoTd{UY+_s%vCy3Ioj6XSH;58=VI4JzZ%>#v@sM;W"
    "o{8*94}U_ck-AlZ9L0|@#VNW%=Zd9UVC~te%){+~Av@3URk8$HAo%7f(xT~l&InINuKKM(MTAaZ1El(D"
    "cidW!J7MxcnMAMkAQhz+KUr&jFhz;CmU#H9Q2bac5iKj<(st5Bi0KvwFqs&m9NuBgc3Y09(a)DFl4CfZ"
    "g=Nd}OO&Ch?J!0(170k`l!9byQ-nrY6$2`aL~_TL;-{}LY-|3Ui^7b3j90?^A=d@y+7LOZ_FJ(vf?#Oi"
    "XXq&nQ|fUC3XrU&jr^_fV`SF{@D?AVNAUR^lFPB4jk-k=ka~=y53|cL>-te9j{fzzB5?sF9a-y1vy{SA"
    "6rv9S!HcMrM!gR~(5N(bEfqAT-jC?~+w%&o#25R(Dt{b!eQG2W`;M+m_d4-jXbc4IIwJY2c4O8y{co=Y"
    "xei=B);_eFRu<=>tUu<ikyqhM(ICI+hfjmooFmvuNY<@A1SRf7#y(M2*`h*?!gSXkFe=NY5UyU!r6;YN"
    "{H}sLlIsUgW6>SN!ukSdHQDLcu0Gc&v`)1mZAS83FcUc!zA%8+uA`@@BCM}EMk<Z{-xlQO(fTaC1!}Lq"
    "=ZUC({f_VPahyx=Z~e|+U*{I{5x&1``b-}`zwNh-@AD1*{)(f-k8>$`QLs>J|1Skgep9fl;jmAt!)i7g"
    "A<R1U#~UGYLx?#8pArL%J07D<fb~+Drg??mznj`ak_a3fB7eN0iz{tMO(*rtH2Uc0OH*!GE~re|-HD7)"
    "bMX%C&2IFh>-uEx8kRY~7vpYEG1avI<d!}D)L2}d3CY_k-u^p&%*+%QAtX0ab43xo(XR;Z<OjQwuoY){"
    "`krbO<OYxS#nUJ6x4aw_U7AC<okN*)=R+0tHOBejLNNH`4uMF5V3c4bmOA;alrQfEb0f5w+<C<z+OC%G"
    ">u^foa{R5QqFIJmZ&^IjLKf$dxJ*L8@?P930StE=DJK~SL`^r(4v}-7A$pkJL3Z8hso>j7@Tlcb4Zkux"
    "ym>FfXQ2@PTH~^h#hclUeAS6Hu@+{kl4u<9ZsdSB8U9vPH(G*6`d9xIz^JaWO#O1r*rGSbj1>)6-O6y)"
    "9Thn)>h|n;x5}zIL*ZU3z#67)4a=2&I|=JG?lvJkt$0MW7c(l;bU@j7!dKyTqvm)c4)7wJ1(|w=q}-4%"
    "q*-PIQn6}DigDfa*f6ccWXBd26TFSOv;wW*MOVez#}Eg?XvEox`XH@YC)E*B+IF$EidYl#)peUN;k67G"
    "GUqIMGHL4A@S>CR6qc||8eE50f1Y^Rc_Pg!H^he*>h+IFz(mGrZ*dCRRJp`xv5uSeWv#@cB|gEi&2<Xl"
    "Wg5brlhRIk0ogt~&Yh#s1NR<jPv=Exiz?aCo_e_3wEN3=sS0WkH?v>|c;jWiV;5#rAQrPwO&YLOJD}Ir"
    "cyP3Lb1Ikh(@zj}kxVv;a<|5~y>yntPR|36lhh#vF!`EK6K3cV$`(L~lOaTI4sC<&4?tj2Uklf4BmqvF"
    "6KXIbFV}2wqILn3Dk^~lRW*|UHkLV1(@A6J<G}@;_BfxehuYkkQX2^Ba;Y?&mGMG)N0j8M)+Jb7+ng{r"
    "h~MzT@FWHYgR3Xopcluo12<&sHUPk=kHy7R_I`*F?I6-<JrqsNbkG-8gSZKN>vRsrs#rz<9mV<#k(o`O"
    "3$SOJ#-*>cJ_0GyBq_mJkSwXN6(WtSykJ|!OYbCJr-@GU46n7-DAlQZ>#xFyNe`mphXh}5gcAAmuqDMr"
    "j{xM!!}enSvCcTmE{F9R>#`|eQ6vw^?CR=3BK5q_rKG@!ENQ)9MRSa%C^r}@CiOX>+re3B3~%V0Oc3f6"
    "k#A=E2&Pq-Q!oHr=|1jVgjD_>m^xb?Ak&@A75ZvM=Sl+X$+q=Ud<Tt)NAa+fjbaOs(_FY^tAv}qz1?`9"
    "3dN>M1aLkA|GE%APq*VY|Mc(QqgPq};t_;N|B3bI^QZRy{hg(s75!G$rEo~5@_FuZKOcg4y$V+H{}imG"
    "65bl)eJjLy4Aj~}!J|fFy{nvw_%ekgTi1EV0zu2A*}N~W8x`fwpr}TjX1pq`sGrN7J&n9Gh%EBQNVb1V"
    "qGRDR5lXI7wFg?hZBXN(qJZE@*)s;OwsS>k7w6kq;<#^%>o_43o}vQKc8=S&I5Q%3+KbFLEGjqs^CUl?"
    "%??CRcy+l^)X1Qx@hz1m68n0mR2XztLH}wf+izs^^gi%W^e`K^;f|P&r$oLB+jJt*5OaawgGE_m4XW@Q"
    "f_XsyFJ-trPc>f<mvF0~CjKH<LSC#9z=L<wWR|#U@IBEeyLWx#8^{L=0c(^Q&#DoZQXKbXIMBFy#ZQtc"
    "ev=N6rsW)=Ib<&#TjE_*k!rZa;#aGY20EMGX`Z4aeDxSkeTw*cfqwtDGTixw5*NZ{;yqk-t0MRjxWzk7"
    "^Di!6lCItA{ExF%dBlzN^!Jxm-v_A|+tQA-TJ4L0rZyscTLjbQmvB7ReB&`5E16i|Kl1;TN8Er?`b7Fy"
    "hE>%zoExd*iaI)9z4J?i3||UT<RRxr7p(A+iLzXjOo7j%>OiW|2S<kOD}b1&E?58ayw;Zgtld8^H+l`^"
    "pL`e%tY2(7WIiS_Pd`i@>piARH7p<CESS%Ktz`#)>2Nad3t)+LmsO*jgAJ%1g&^s%)46CVdblQmUxd6V"
    "k3&|Cj=oW~la(HJ_YLHKZw0fz7|+o4!J1;jR&_mH6kWOVcJY^V?P-IqL7HG8;K#|)Qhf(EJ*$2YntMZV"
    ">?|i?XnCXj75w=J&ww`d4F{svX7ChS-8FyFzI`+nr9`9LoJ<@`ftPF1nK`VQXI9H9_qA>xo=Vt|w7@Od"
    "&P3Bf%wOHVZgu3vvg`186KtjrA|46?=oR7WpQhknqN;s?*AsNO?sW0}O!EoY`}Alc0W9hXEf2dY_(Q7("
    "y!x8viGE^gkO<j$Y*2EC-TXaRTw3h0e5%#Nb{@tQ04DQe)vL7oV4?U^HIl^_{HqFM_{eMfz3};L>3r~8"
    "<MgDPwSj50)9EH8E+OE~4Bhh8G_Du^yfC5?sq3PzKR3ADO3BLjm<MeNT3(y&RK@N?FF<h>&E_8H4QWkp"
    "W=Ypfpt=vn(kGevCMfj-OXH;b;nd!yUc}B?a_4f=o|%&h^b$?Ij*CQ7FAPTBaFKd(o*i4)495}V%mZ(X"
    ")USBjhq1sbRnMeg|IMPWctvy*6tOv{?3NFzA03G2NN=QNizFLxDZLS*7c?hvtFM466Lozxy0DM&T1DO~"
    "JxmPomM??crnOcfS#p{^kk;f)y7++opXV0L#8)(`ReG7og9wl6Wh=C)+(dbmmUmh{3PX{6)vYZh=Z4~8"
    "NjuVa;GJWbqxP8a49~XB68$*fSk`0^4x)aWZLNplEbq=0FW~oAJ9^yN1<&l2LOE~oVw&{=)^^d|DnTjE"
    "HGk+GPjzl7+bm};^03A#D3=E(I^E9ocDHH3))_|Y0Cwu^aM=~#JiTNNh4G`KKEoh5&IyIf>@h&S1rbU5"
    "Uj*O9_203-hsCch3LFWH%VS-PtX8Bj;e4xgse5fI+rE+7H2FDzB>0J%QD|koRcV5n95%u$$FXF3Ocbm3"
    "HW7E(V)JG|0Y!(e&PQ?C495diB+e7UOeA5%hPcyxr<F0x{EUb8eLueKZ4H3Vr<NWvBaM72H_mO>zJFw9"
    "DLPGP!PRrC`x}?BP|?(oq-`!pbq7IB#+8lk;fNHTkk1G@nF(~DJZoMJ^@@gZXTs%Ejurzr?yw!l?vjL7"
    "4#~k6*{PY2HOu!2$3QeO;RH3HO3nqZ%(m->P1E|o(m#xW_EU@=78ZS9;dmzEJ>vzh7$gs6jtA#mTkAF6"
    "t=i{SoUPb?gmoVv(=*QAR0LS<I7`{ZUQa<2aX6guf!mI8z?0W+8G{v22v9$sbYx_5f@La(N#3JQ3Gvm="
    "O^TI<epn^t&s%*U&?o}tEh68L0yHZKRw5;pJ5iv08h+hAk=~*~RD5OXG^=!6#Nbn#sjTkfj<-##!UHVE"
    "du#LYp=_-@%#{N#Ze0_g@D4rI@UyavNdxBLWZ5h@kYS3rx|Apqwuua;Sq*H|os~!)sv73h2BoC$(j^@5"
    "PLX>cT@d=ocJM@tc&l<P)3bp^O-MW8R1}{N$=D#BtU1ZT66IZkiPB+7(EYN9y|QaF+l!{7GIKg;++rW*"
    "{BUgYbxV{uW}m-@2BGS43Ju>DD<<YUG9|8fWoInf7|Q>RG$yQyciJq0NrAJ;6?6?l6g3{pMPGKlpvJyn"
    "C+dZ#aAgPR1+u+&Q)WDILJbo<P;HsbM@^12?|c!`(zFZJV!dL|)pT+nEH1cJG*??X$>L!e%VY+tA7uJl"
    "KuN?LUnPR}LnmWUhch;j++>eLjH21HeI46OGJ>N@o{T?WPb4Hv>jPrLK0TrFh}S&<lO{T14qK!#s5Od0"
    "2Ajry=LbpzBHhv=!Aiw@zw%eDd&<Cbs1C^1Y>q?Sgk+>U7t4+POcYG804>5?!M0FUy)EQ(K4tbg7p?^L"
    "24$y031V1=uaOri8aIlyo|H)xUko_3W5%%V|8o8(y>=;>;6Mq0hVWdkeI7Uqip^AD!?}@_6#u~u#98*`"
    "W#*uUAGmq#oma{nZpIMdI?IQ!Jnz<4<?2BTx>#v&RfRLgK71M1qhxp2AUgMhtW7WB(H7t6Rb{^|VbbH+"
    "!Xp@LOpi1+H;bT&!g^Xd5k&;qq-mA#Z<xlK^Q5AhNi%YfjK*;|&{)dYb-BWqSeZs8j47$l*Dy?xuvC}n"
    "cz@lq0iEIzWV2r}%{iW7?R6CYa}#Rqw9u~(Uf5Fh1+dYW8y26ERnS5j8ChCk>}wj)l(=*^it%Yv<)j^1"
    "%?-^;GUmQ48bH>s@h@j3;dkWp5x?TsZ}>e|$y~ob%g+bsop5}Y?~ik5F6UeKQ$D}@80U-oQ-6=rzrV+E"
    "e7s_Jn1kHRO3v%`qFQQis->|FOOBcE<<bw++0ASNZUcRT;eGmX+t9{kD!Cwc!7}d~b+@)6iFwJ2j=@9W"
    "_qMNgYi%z`F&hS?dMlB6cx2j0u#^-z-FX+(Dzr9IodYj1H}sq8OfH0-)X3#Oj7qfkG+aL5dj11QG&w?B"
    "#Cw5QkWbzCb(4&5;ssYIYb*>mdK_eVBG3^ECaFNXMZW8pr`lM80M(M=jtEq)<R~BLj4!x%9aH4j%k}4J"
    "akz;n$c~b?8_YrGy2t-Xvc!^BtyHK!-gCmbo0Vv1&gPA?N9)u;$#kQg(>Bl<k+2!@2;GdQP=Kl9+RYqL"
    "S76+_9L@uBoET8%YeA=vej}|)d9-V@E*5#HnUrrPiz-MGGSJ!}7zOe*?tB}n@`{T-oh{`V2(A5h`lW6r"
    "y-<!5kL1qwc1>O8YHFhO_`yQB%qlXe7~w$&dds*7%qfCfy1ek)2cY#^X$PqCAJ&+qWm2N<ifZfmX=oO&"
    "9kpv-6X#rGjqR9!C4N}*F>wp0oQ>Y|(W2OVkhs1zsZpk?)=-B}J3-%vI+~d@q=!10Fdd1@p)Yb+4E#Y="
    "UJr*)ZG#iMbc`uHNl1<kT1<b8ejsqEJ*2bDv4Z6_d7vHbiGiLlTH>!;@SLBhb=|p&XQ8|gljxYJr&j21"
    "XLrn(?i&pHnI@q4cnIhVNnho>c5GroH0{xMS}u%Md0K9V=O#4r$JT8R^Khf@p_}QX(y>m34qDsjYha<!"
    "z?Mh1tP?)2kKC=~By@$0E@NWdM?IGPdVa8Tzjd&UbuWNC)wI)nf2=d&^KwA@X<%Tj5u#<cEDoa6B)?lv"
    "9n4T@jkmc3Z7cT!#~f2chF0<2(7|((n7agzSHOX8<eW~sKN6AaaR}!RjoKHN<%3f(HWjIHxoma2%|cVC"
    "x%S|F<p{HNQJ&aFNz9@(FMzdMlh3kEV6wlC$gW`&l&ZF9(#R%J^N{3vkvW*p+0FvV@gODg2Fib;SFqH5"
    "IVhCI>dJ6WLF<8%ShEry!3R8dTh#-W_HlXR-G4_FIL}@DtzFIHkT+~=_0Vn1yRZ9QxZUS=zRkHg#^jkT"
    "L;F6_d*3dOq=}y6Iupq4xa4hZ@jV4+^E_xD&uLp_kiIrB`I&8Ac6O)A-Qzg14mni;DBzjo%46R7Xh60*"
    "aLWpt=G;jE1ZwI_&w0#5<8?K5BlfsvleCP4x+q|P!+0CH==7@?F^_J_bwt>ZtE3R9@x*?54ecm{wqfw>"
    "6}f0ceyCN;{k|>PTxFosEm$dojfjtJIN**Vix%Hp#dNxSrygd+EzmG#KT4ffk|u^>^FDL7ZE`1RKz8pm"
    "UYYLae|LX(Db-kg#0v~<E+kgxYwZqes0A|@a@8Aie8p7J)@*&(wdOFh=*^o(GFxY)C3%e-dIQpkEJ+x*"
    "I4smDU+nAch{S^Y<=tzCmGTY;((!ilJd`8$r4W_vaXD>$<9K&cg-3wxVb4Hu`;PDw=4a2P3jh;MlGGfX"
    "k(>?q)3`&MQ(lR7^Q~9QqtZ&XaJ-iN4(g3jfA5&c6*W!NNb->P*b-LswlOczZg>pned@Au5UFqPQZy~7"
    "ncfYuL^K*%wemV+757UTcNDQX;-DV0!DDgxqPvwUo_~&-Dj&d=nIxEtvIk#CNU3h?$h4N>Ge!@TV%nK0"
    "=Y!MEM?+%U<lE3t0YCO2jX2e*(^cH)GLjZnA1iN(J0LZk`i&UBWM*gNYM}L2!v+iLwAram#Nqe+pLmfM"
    "z~+QR@R<2AopDGA0phw6X9q=|AD*#cbxdPL+Z{3Lu2XMac)i?tBIl!{V`1!{n`?L@uXsN-BBRb!G_2u|"
    "MF_^>uhQk$o6DkIJVIN#k%rIF9`K8dy;U0u>h!e}XNOw#MFlu;;JvgkO(usP``ciP&K|%vZ4><(au6+>"
    ")?u6!uArsLG{{SB*)F5wLWW0iz;UhEWr1UYH;v1)^a;d*=Vb;EL1tDX4#h{ly_5%vZaz4+V<tiAF<nY4"
    "D7tGT*XVh$t;lHSnet3kSz88#IZ+;F$#S()<K3IMvA72p$U%!#>X;y79derK`dJ3`^>SB~>2dO4o_K%g"
    "v{xT*hslqt2VJX8N4<>y#bC<>7jUVZSTWT&Nq)I?H+e_-w$j6_0wOuHhAE30QlQ<{^H?21qwRWKuagn_"
    "&4ai}JF+XrJ*?HV?)l^Bj@x0Kmi6A*yk%!4vnLy4Fx$*5*9Q-nKw)baorhJnyTPCfE<MS<vXWO~r}h~x"
    "nLi-4^plFsVsbv4vA5EI2ZN`%nW|{zxMq(f55}_2^I%0aeI6NIt|>WPp`V_;y!y4+N<(sEz$5@Y1WYdq"
    "NAei9IF00(E-V#^UO`Kf1&VTaHM{9|m3gho{aTG)v|F34yV9b1Y)$M?qR)xR`z6?f#!aI~nco60qB*Ug"
    "snEM;pDH{!jBm+Hh=I;CjHYLLNi+*ndpue97uQ|rirB<WYs<3eSulxVC9LA&Fv&rT$`hy}HQ0%U8Z*a!"
    ">)c2J5#|i95|P1USq;b2kypr{woR)ekrNy~h^lMerAe<noU*qpu$%ySG>i3XybJY06GQoIWA!#^eZ|BD"
    "vZ06L5*5d4lCG}zI=)DqxoQIbl5NKxjJk%e=DBBWb5`=+MmVnIHh}&NSYnGFV%6=rlFS{(3S5CFNmhEr"
    "0|nIi1N$-^Gh{?>O#XAW4_eroJ=u!69#y)T49R$o^Xh~v++5`~Pe3p0CRT0Fz6u}BH=@;HPZ(`=)#)Z%"
    "Y4YXxV6fL+Uv%e@J=Q<s!dD4MN%D{sCJH(@+zyL<4x5R*_-vUl6b6~~iR{kEC1AjupK@KIAhjJcwHCOG"
    "dJ7ovsUa3EwcH7yCp6<u41YyCdv=gC?C0xNs0s^xfe<Z?q%)QE7yK(bKA|o4LY?QL1W20ogbMEhAZ{#Z"
    "i+RzH(Esfe=B(_`H!^;g_E~>Flcwn-e#VdQ-xTvlto=KG)E<6I{Tk<L`1yVQm+umPLObfYzJ9(sR@%K|"
    "<#h^kK5@Hc<*d7xDGYIp6TF43?`F6nct>`628r7uhu<M~)C~)6UPMEZ(@o;Ad}u1p1`?g<l;E3$U^>U@"
    "n7~FjK>xiPpL?{gluA5^+js-w$2&6&W~*%D@n$L!>^ot5LH1Bu_z&|JY3rZ{#+htzH-53CCr2ySLi^A2"
    "mu9er-eCuwgqtx^qQ4NE#VOh+d%T-%P&_DQy}%ixd-Ohl@#&KDvCXyZW`-08_F4uDQDhb`;5W=y`Z@{9"
    "3Aw!#U8(oml(cCVbK1=ud#e$18#iqBug5-=t$-fd-4&OfB5C|yIYkpP*>6lgQD;WSy5g_V1{lljXMK)%"
    "TxR5KQDOiE^FDn6!HM*1P@8bnyJ2B*wUfP)o$H%0^M%`-gQPHb4{FX;h!lcb_s`O7@*@mDir#|adL%OG"
    "Yh%dEr>wSM<4d?QtK`(J?ij5{UiB^2h($v{d!sqe*5NgAZJ0-QNQgwSQj{JmyBk@s3h~`^?~Y60)(}F_"
    "h<I?;?6Y5|v)2<X@-3v|LJAR?N}5|BR?Jr4utx9#8qP#v81g(UFT~EKj>VczVwE=IRJG6`fNSKB#y4~-"
    "{IZc<4upMtxk^yriUiE+tiEoRb*9#_Bb(gLP|CDjm}-6EVwcW2Jp_H&FtZ1wFgol)Ab<UJXHD@!-g+t="
    "!Xz1M#XO*IZAaryJ64NW^LZF}D<n~wdBY}yE!N>lqE@dIK2)nn9{35%3PYOm#qh+47G+mU24ctspcS@m"
    "_H2~CvkM>HlpyI#o095rWgToyiE0?_F-@7(Ldx0tasOrEghqX>v|L~}6$8@I(l(!R+Zu>A95V=`6^uJh"
    "8z;8%tQsD;R*^!d6dww;VRodbz-h9DD}W5%@|lN6K8fUHbqLxte6oZrXG28)W5yI0$SP!Y@@cF9TqgvH"
    "hJq7!5`eOU+KZJsT#=0>)$Np`SEnUI(ubu(61!%J=1{<$HRbwhkhzKQALRrc0W(IQ**2=Bk*U@Z%W6#S"
    "hlC5$7HJws;4QBQ6g3?yf1}xUOvWqNVOG$%PBfj!m9^?ra>!!OvzJ#7N_L$HpM7IKSCdZoZSs}Q0@<w0"
    "i{HbVZ<FQ;%g)5Ew_=Lw0T?J>YlVUZ10a%v-B6CCF)jXG8w1bUvBj~NZwl25>N|a18n5a-H9QPw>G^g#"
    "wZ{|lxYW|go)~IEeA;QtSh1!>iHL#W0C;vOT&4(qqi)EKGN~n?g!SU+QR#WI0LR<3phyZhsz)^kTWgrL"
    "Mf7zT2yp&&_Som|_t#I!>8qxnp3?W{IA8Y9uMo;d_!__8v3<0&=KsiF=dtyx{EU2leXgT_*YNXOUqw*u"
    "f0LW~v1_2thxfJmma<^CVP3Ou+$HByUhn=HWBUBaH-9obZ0HKNm8*L=PPYPQo5C%v(~+p0r1PKPvfm*<"
    "AI$u;uP4^Cn_`o9oHmVeQdAP8RPUfS4Lv~erml@Ug}d}8&AupElmHcyA!YB^36NUw7>h1Mx-l3ls*+*C"
    "bJ)#9b$R>g&PTY}CBQD%ja<D65{qUv6}qlG*RjPL5s>C;6#ngM;q@ExzT9lkv)c@2E#;17)hYE3#serB"
    "ZllZ8^He4(ubejIJ0>r%z9&S%XLK~BJH|J7+|vAZGUE?Ki5?mV#am))@|wvx`Y^s;eXZN4CQ4_Y;mVj_"
    "Lcy8uPz351CH*4;!_Tz^{L0PE3C&+LX2(QK2(4GQaIo${qHXVb6*Rc7cd>Ppsti|!#e9ko5Zevr%wf)S"
    "Y+G~*BR$<6ehcVh0d3WEf>VtUbNC;qC^QcZ1&_~FmT+ti@UwW3R3T5x(8^Fb_Z9wCS6A*o9`(QcaWnwC"
    "E4u3=G}QYK9~je{?u!QaqmlMAtSMR^DWqR0b<+CT;-5jiu=1=wJ$tCH#=nepnqrHxx*n*^<W#6)!fC1="
    "-=fLqFGML)Hf%2aieFrn;QV}H6;CkPG{834i0Y0l-n3Obrbfx*GQApyf&^#LmrgV3u$w!Te+=OL&3^4a"
    "{*3=v%Fl!FCM@#l#e*Y*POY|R%=}+2C9=Eeb=6nlCAqnl>Cdix8LT(m$^7@Uu1iBl2KCm6O=W6cBo0c#"
    "8~Hb0N7@!m&9>k%AMNERrRmK>k2mVA{#Z7*A@xw=@p@*L=Q|>6T+aAG2nKhO&c;gdwR9s}2~=#IFVjW)"
    "`mh*?fCU!?zZsYQ+v^}|SaXN2sm)u+?<bn+E^|76v4TQ_5&$;rYIW(;$)24>=nxu|tLqG7CPi~|ihaGf"
    "e4#HaL%50)9Nn6ppk~qJc;kzO>FhpOWQ=_V_VBD5fFp6xYsRpn-8z2<C5x>wEZG-^zU@@q4g5vRBu{_3"
    "`*R<18Ziw;-ngf<G^?QcWKtvl9W#7<8^A!m)CWxdy!1t%m)G<4nF-U@N;Le_7D&7kWw9*jH<ZfS?siX5"
    "(w<!cX^mTYxPz0&Y@!s8Tekb>!HQcZewmw{f$KR9zSzURjmEF?3@)p#ySx5E(iVA3G`v6W>c+y;_tEb%"
    "ZSGEzJs#_d)KDcdk}xZdMNGzr6+xYFDQ5sI`gBkp_r$kmzy<@=U{!6hg_U6QxcQyBel&MsiV&zD5LIos"
    "x8$fATu_})<7e}jGunl>{1{FQLQ7S=?2_=g8c?iiW|b&q`b<+bUSrdRq1Mu9N=-$-xsIZWPMqIOr99sL"
    "Zs&p4HYtJ{7b0Tz8Wx-++pqa7s{nBAWxH?8sqx?F&|Gc#i&%hmt19k`V40gfkh=UXkKSA|c0pm@o`eC_"
    "Gs7IR?RT?8En2)~ZUwhQpIhDLbv5!5liIZ9tBXUUk5MLb(Cw8PzNydj*IOh%@WGur(ymx4Ca3q=5=7Fe"
    "k=Tm<|64PsZ(B8F)hfx_w={E+Q^NJu;A2>=^rX5~;_9wr9dW|JhQA1ddEu?z-+wd_h$zD4f^*u+-X)bE"
    "LIBNn6(>1OVR139aY^j8v;jw#?6cJ~0Ejnn^Qy|KR*-d}0RuzprL?YUQ8bv!s`7jV>lB9G$Y_yov7E}B"
    ";Uz^G2PkRzoiJL~ZXH%Qk*2sE9(;D;>4+vdE9Uj{1|D(EU-Naz7*$rnCzl|1t88U`<v5B#+Co--&Z=q*"
    "&IWY`k!-EJLDkV;%bKHi^IV^*WhQ0fi;fvB6vujjb<~x_N7Wai)TzKmZMxQDret&u&YWZGY^!n9Svo6H"
    "7&4;MxQVD-tklZtY+Ko74uZ3*%6#gKTqk?&iag%R6m*>l0b!s`?js~oXS!3duiCgYzaWC+qU|@>qb2MZ"
    "edUrmWM%S;JtU}U;!IXTu;%Cd27NZTke9gTP$Rp-dt5vB17uwm-zrVG6q6CTRM&K3a%;3esmW+U0}#9F"
    ";Hp(&pRCU5GxE#0<U+g=TNZ+~*RrC`3=2L<0q&`<tj-|fx!DRZ{F~TYaWj&$JNLB1&*CCZYFJ>;OVUvR"
    "N+lMiM0X1`0Ai|J%FBIN{YG=B&qRfhR%f$X_d4Mi<tv-HpgkZSh@`0NYuOabrsAlW$DnsS15l}$ca|lZ"
    "`ykjWwb*%skyO!kk(#NkXsSvjg7JM=cU<Z5#=nrAupIwEny30FtP?&KJyQ>keA`4MY6?APOpb9D&z|Q5"
    "TpjBbVNV=3ZR_JPr7&28HMx>0tF#@(&Il}6M3IJD=g29wNU!YZ4w$B0A%T=XQ5_CsK!Yjy5qGwamhJ50"
    "*GQN3BTv@NIyaM>yO4Krp~yt)36m(l#P0CX)EllgxMkj`XPZ9pz7aMusxa(+MrSf?Gm+;?2k4th{n>4-"
    "95dL&9&a)3dqG>3HtZ3|66{rB&gZf6S7*bo$)84#o4>3;HHSqQRg0oJ)zxGW5<o|_C0SXc5etD{&}a;j"
    "^t7(Uv~5co18dc5IGi#FuDE=Atpvk!H9*+*j3aY$qRE;L@`Qd(G@XT;Ovw_fvT`QUF_T2whD32OTrOg@"
    "5@M196$nW7!7i6wStzA}+VO~99g@awsah6^*jP7rl<wy<so`l#AhlJO;UDpFui4<RjDb)&X)V+My!c*7"
    "EfpH86KLVJK#J6rNvm_vXDNDjG;%O(Ae%n7;SyxUY|dO(soAMTyn*<4O8d$9ut~$QL7uP`<0wO4#c)Yw"
    "YgOuJ8b)s-21R$Kug?L^<+1HyF5>l!X1uD%j$$MwMuRP|9ch&9*{T!M?L1WdO<_*g+r5b1v!*jrc4{Hk"
    "X}qR>C5I|5Y=p7ZMtbv9WTZ@!i@XwYXOM}J$;A+AIrRrL&Cx;%62mBx02{Fsw{ra3S<Ywq&fmv(`}s}j"
    "C#KKz`TKGHy@l`ZaaI@~U*~5oA0NMc{QkuJoktn*x0R3Z@$vbQN_mk|F{k;P<+OV#RZVYFs<=w2g3k<`"
    "H?K(8+lXTA3}trw%m}};NT+Ef(80;hotuvGbEZ()@j@f~KGusGl_Uv^D}oOf@3R`1er3u@gHSRz^xrbu"
    "J-X#2PTUB+CUuC?BhIg9-MN`vVDW1PS=7#2dD9UOhzr!ELdf8H@$S;mJX7aE7LMW+-nXw}CTyFK>ODvg"
    "J-7QX?LI*`nqA#0)}|2Qyy21-MUFxa0(ciyaT1eM;czC_b^`l*Op*mevs7`%;|5JEAD#|ChtD(l?q0-z"
    "HFnH;quCevJ|KzUTSBnU%Wi<_)qjsRKdzV%Rr;W4Q|@=8l;EQ&Vu*OSVOD88++D{;7I{fmd~viW;x3p)"
    "<NQR%Mc~|$Nl3f7JLH%$lz&>Pmf+&wDi5E10%)TBQ0zM6CIHZr98y<vbI)J$yn2&A81+aK`Jx#pc%rl5"
    "zS9lr0Fwt_h^SRQikQZKkLu&ZPu&1`(v-G!c0vjs%YV6OcKc7J$p|(JyKq?1!EyP^r^q*$DqIx$cxjrX"
    "<Jvt3_6*_CeeMVlcK<<zzIna|C9Cs3t$#5JN^h_rme;~8$q3D3^WAGSlnnA^t6t|oc$+;znlOX74$?GD"
    "=zNP{*+trC8eHmXKYe)2qhwkq`NqJ`=Bp7yE3Me|_;s=3?3^&?UvGb>58SzXjLr5=0z(?LIue*fJga=i"
    "HKWkzLp<|dQxNIr4H9eZ0T|+X-L9n#IuQ*QKskh+aW<bq-G7UZ>F2f$@*Bo%gxRKNY^}+<uY;Cmwl<%$"
    "dTg_K5tFaIXDst)2e-!FU;w@bb26gonEO$+?B5Wpr>{FL^p5R+oqq+3I4<sHwE6jUADS~+KgiHCM%{Gr"
    ")5KBy8%F!;wSsN+uAX*ZBj&JW_cn4V%f%Syj$ZJJ6*E2Wdw-Z=Ue<@3>@@W?QMoZ`&V>1_Op1mfD5Zy!"
    "5CL&4f@Tgn$-_F&P~saM`<gO#50ClJFvp$o&1Q{D=>cewbo*m#ADsVV08{8*pWK;Vkpu<M@A1z}PA^S!"
    "lWw&R{(U+Je)^L+N@Qzq=&@1-29K8K#*?09L`1Tm0rO+(X`=Ja9%Ta}xRbBGu)u&b<zQRP$DAbk1r2lQ"
    "-)3UiM`Xax7n^*(obipC&>YQ*OM_<}3h*X9M4ZMw@SCgh>#?pdc=G0WInNel^aah^I7~}an_sEkqzS=$"
    "8;-bVN81@@h`a5H)UUm@GHFTCv@j?C@C}w^Dy{Svb#FTJMAg=przUJKgB!05?M!oK`repifuGw9KH7#n"
    "C6Ywq_?t}Gz_@gZA7D06xzT?Qe*V`a#W6d7ZT_dTr+mlrp3#`3N(97^NPW?D>xQ>)Z~@v(lM?rYlUvGs"
    "LCf~V=m+ZM+0TZ<QtoeRJ|B5TzM9I_=UBauskZm48YZ1ETzL5qIh${cT%$h@a!P;^S9HV^rMQ0BkuRpj"
    "1Wn-F3K!OKC9Ke17GI_RBOMXiN)OsLW-2n=(c6={Q}am$YL&+x$?4=xfiI>Z&w{P6m6v|MVYSSLh>@ga"
    "UWK>{^YtR?Iua2V=h-uuz^LZ<`V`n=;vG#HTb2!_H<3!WDI8<~j{nSY0AgWUyLXS`^F;ML!&YS5(N-kD"
    "l(Wm2`EXm=P!%W|Wutt6XDB8&>y4U80Q5jsatQ4#Y_AuQnT4BIv21RidU&RV2prI8zD%r>bTM{zN<*z%"
    "eO_$x!|Nr6<FS(jXE0p3Y~&>4I^4lihsScOnefSSATfJ#a8)%%+DFK^MjaxhCqaD9Gyw%<evM@}$!2`!"
    "hrKf-LS$nIjGEl02ekh^;!bo5^d9$BUi0)wd6>iZ1n5wmNpir_+d2~gfD<zXC)lVdMJi8R)>_-o0>`4{"
    "roRA~4X0w}rGD4Ko1f2g7rsoNfqYMOlG^H&NRF||29*dC;yEqq?Ny88PA$VF=+Gj0U_cRYV>t#B2A%D@"
    "cE`QVF+k|H|Bro*NKA&*ALt-3JCj+~u3WeDFFiXdj>}}$J6#HVfDO#cj2WSiTD$N~CEc`5cuth{P_HH="
    "bOxg_lUM4VC<7Qr1Ah5)3EwJqlA0l`(1cVM!vJLR8he{aj8}{1c^?p)%5z5_{c!7=&PQHW2E&VWv1|QP"
    "dzuTVMz;}tOT$7wkVw;=NM<yc1V~U{XuOu<wpB;AC=KBn&q0`A7d0eTqgWVpF!lcE(0;Dz>Q2QOm!Pyo"
    "Jjm-KN%+Erp~?75g*0t(#?EWfw3g$1+r#+^u$SxQpNYC_-EY?s_Jp^5Wo8FeiCNQjfjx>xMrApKMA@P{"
    "Hk;mrgN}CP7aSV>J;nqzMFVHzSolo;Q6az}nO6Y`c#g<SlYxC?oK9xdxr&K|2*G~yfK(?sm?~s^SeZy-"
    "d^B9XCD@O9tRDi#N<C>2W)XtJl6oDgu<Gb(Hn1RF7HT`SC0aQ)a1ZsM6v_GEltv3NAq)T>?r@N;@XP(u"
    "t`w6=w4^kR4+@+aki@SiB5s13UTp@JYKx*7uN6TLe_p-XxjN)sQzE?v(a3yhurjZ0#uK`>N5E7BVP4|k"
    "K|SoluedXw>SS#QrQWZc;bhYmpaJ4S1zavGV)vMd8LTR*ChLr0hTTDPbek7Mfi`nA9p-wuqc&R`I-0tB"
    "F|Cpn%<1P|uSSKPHo)1**kG;EA{aNa;1hys!f>EF&}Y)3O*b7n$!cwPtbl}7PJrPD(4o`8wVcoASTyIg"
    "Itn=%*6)m4Bd@1ET`JeMVY>-LcPE7nAFI9xJ4tJORGE|e*e7eWkEl+i|4wM-XPKf>emz(PNN5oae1UZY"
    "D>@v1jDHSzOEEM69lD2$d=V&6k-y9|HMyWxWlRI7LHcAe$U#zybTH-TMIuqOwSS%C`13hFd-yuiZ%V)7"
    "CCKsAKfaI8Bh>MA-sSKce-+;NQS$gMC4GJWetvwF_Fczkc(LU$rTHJDoO3&W^W~&vl*1V#YRp?7q|@Kv"
    "dJ&!0Y3>Wuf@$1%1B``s-V@=?Hy#RMogrA&f5c(+c8J4+J(;3??lke;rB01ZaRcx#k3Hh#Zv|5qKF;7M"
    "bNl06qq`a!mO0Rd<T=5Ofk!C^6U?QtMY<a?LD>zmtTq*+L^RjiC`!$%C9ersRL9-d41nb>OC{puz!Lhc"
    "Z=Y#)_DgSo+x;MCFvqSM9u0e`W4oEqL`|Qy@dAFS)@<JVzEYHsQxLBvOA2>$2g1g&ZZfjfSiHo$`5`jO"
    "gWd~nZ7&JoZt6f!mBS!QmE)xI@%{|f1L_m1q(t?r-#y>n<=`X%AZF)r#||7+Oykb2)o{_)IqPDU)b7I3"
    "4;j8HT`#KuMDkeE2L1w6gM(v<Nji%Q=-Ida{Z8GLZNfsoo9yF#hXMcwbuJExLcrJVW;q)0*ca6(5Tic!"
    "&4e*~yD<zv%_yP6!l?g!lp_o{ecq@v5pB1VUb}e43+Ti!MTesH^<(x)7BDH=>;Mbt={fu16Rvt$oAR^F"
    "No}0bSY?6<ADg*dg@N8|6&}%vWX|pio<zRBB8WQtyvBzGfn+M2-$E$%V`J<xxGhd~Y1Zzc8>C+dMs2k^"
    "&=s0~P&7X+np&lkmX_Ncxkwf^A;h+3yAw$9Js=y*RdtJC^6J7lJ~d+^1pzs4LtmZ{h1n3lYmc%=w?2hs"
    "^!{QR?MTdMUZBQA2d6hGF^5U$1axe9Y|(7cG|2^tLM8YQE2=fs6&1^~XA3naR1VGAv(-8gi|0GBC^Cbc"
    "AtqC04Xbg3x>!~QmJNi9CP0b8(*C7O4He|Qcba&F&$AV48v9G&%Pqk5py##4X-ui>C?F1S-q=j}5jG_n"
    "gm-~to-1-A`O_RkvoaJs*XqWeB7CK_cgt!J-Hwf#6=-A|3~L>9SOkbUm-1Z$eQtVE{OI|CrXe60kq(wT"
    "Fa6h!I=J%&(pVd2<UfJeJj41t={R;cm*;$MK&ntl^OUMZi_|mZu@-{eIctbOMY_-`WmuOir&Rl)?2Rj0"
    "9@y7V<(N}A{FxiM=u4fAdP}xc@L_6o9s#PAOk7N%H<OdGdNh$adF!`wXmKQiXRw5{WgRclEM!!?iEIKi"
    "W_eT-#Pz4>sMmdnmlAoxDq__S;^5laRG;_tSr?{XCpdL81cg0lRAq-s^tCZF^oVvMUz&4+)DWcGL%X#("
    "g>$)B=LSViSJvDj<e8IPu9)T`R!2N5w)Iy~IexD1(iliJNksafFQ~TB+Ez|VY!5Wf5@Z!A8wOrfMiQ1#"
    "th_-*X;p|l2_{I<<5>M_9keN<DJ%;XP@h*u{{+*us31+<uHJ*&$q94pfmXqdUfoPR#Z1%06-XP_s~AJu"
    "SuUJ$rwp41-IP$qI-&7#7KRy72YLZXa0}+Y9S~8Mxiu`g%1bROPDWZ7l&XUBNh?xl>0h5*j?d4}UO(bT"
    "KhHxSU%&OUod@-gvp75dTS@29yN}=2di(8P=_l5Yug~)HoyvLQ`S>j1RfLxAMQG>e{paLz{x<)wZAX{9"
    "99{fk2=x<)#)&tiB#ES*yjdqA_0E5-)rAAjXvU)6)!!;orQEVw)(6%2AI$TI-5#2EU8Li5XNw2rLi>sQ"
    "%rV87Hv%a}PI1=D!FGh3^Hp}4Btx<uD=i5%-075PF@$tnv&qPldUGyOh=U#nEs|)TpZzW%CcqGpAI*@R"
    "c2^}1wWaIT0gtJAese40Q-dYh7<A!wZ*xd6zdtqQkUig{qxSwS^>mzNllm~2_}rDcDdM$OM1uPK9$NEz"
    "C-gc9ac~Ewfjhmua~blKhTK>XXiUWVesv;4+I*N&mJGBtclPZB1MxK_`|VivRHEhEdiz}A5dR{Pr}SVg"
    "4r@T--xRRx`ylM>lU9`D9XI1350O!50Y-~CIN!X2SkI-IW>eEMmr}dE=i|5vL3|t`6G?glk|U>vI7JC`"
    "$5c3$oBMed!E@(SqT9jHG?oAKj^%=ETzw-UpJh4z?-&Ad0n*H(kQ|c8`aR;CO2DA|gd0EXuz)Z#>9N{x"
    "@~brel>w+cH`Z#x5zMNkO^sMg2EKbI;(-=zhI_xgAkQ?D)^A?hdi_-{A)0jgdoFFhfb&)f6-|AYbKDeW"
    "Ozn#%u9_>YQYwkHAb)SLnDF-(VfDkgE?d%EnxP=fx`SK1h+j6g0%ldr-J1KRO9{06JoVuDt3Lj;cgvs+"
    "-B-D;8@Txm5YeobakOKc=S*J0mBP?1bpQe|eO{^TIt4o`rxUYG!Qnqzm&K1fr9+p9W5#C?!MQ=6v6J}A"
    "wTW7A(fnf;RGoz*=htDk5A)QrDZt89Q%(Ci2hBP~5GzUyKU<y&E#U>OfV}lB<~G|(tJyolb4gFPTiPFv"
    "eNoMiG>Qwc5HqTCQv4w=5JAmv!S)uaP56Sv7z#4lS!>A7pl%3&U&+GW?k(vzg^=DOT=B<9*2aD{xV+VK"
    ")lPI$w}E&W!X}b$rUD|kS+eUvvCuQ5Db_GJbH;IAX+!+_ffCAV8ZM<Msv9T8kMD>xDLeUb*Bh|>9*%>>"
    "1PKJ7t81_M%1+KFXgpXzH3N$&TbA-z$0YrtlCTA1$e(}?!ei|!oR6E4!yeTKBDw6=dz0iuUzID_x7+)s"
    "pZu;Lty8CH00#mhA4pzHY~WuHM{vM6Zd1{wOS&@7hQnnL>C$0{Br5f~e^s6D&7`Z9IX+Wf)^_$&Y)$4d"
    "RP$a^HT6{U9@<^OX1H@a)%MKtETdk8ysig}{lJW*o#0d79Lp-_`X!Ml(=b2`T2D7L_UK`FbmN%Tot}B5"
    ">B}VDal}NV5bD8sO&&V`tW{j+ux|S^a+{oq&5APTaOjo_DQ!I5X<G~}wbAQLta}AQt0UqX1fW|j!M?42"
    "4Ye9sJAClGDxj=zG$7c8DZCel#_s|+LoS#SAm-DZ^wI7u0p6}MhH%55F%Vh)Ov^K;_oPo01ST7>8i^4!"
    "nxWSPQrDXT)vyw&ix?{s>AV4{0S1L;qy*{Tb^12W!`4Qq(0)<P;_(!C8r~KQVldcj_Ufdb3C_fheWF)i"
    "x8^!Y2Z4G=+8lKo1OpE7*i!8xu9D2*kTck9i*j|hD{F=fI|E84HG0|Rwy2Qw&`1=moUVaNZyx7G62h+}"
    "ueL6{hWBY^zUTz7x_;azuC%nnG!w{GDDyUlfVLGn!`djqXN%YIMw%XP;_Jp8O-WZH1{|K7zUO-c%yQY3"
    "iES$L0?DDw|L(9d;G(|1q>^Afm;;q7EK<80`NQY2^M*^&J!f=Wif5^9ijBjD%#pK4>!d?`$W;ua8tevX"
    "dYWoOXGf+dby(G#wfw#99I8GCXljb7nNn>U)r4VBfVVSuh7OsVzy`0zi<aWeH7-7OyPo3&A%Z<vi}srI"
    "=jFqB0<^1T0m3bgK4ty3IJz1E!bT88nzh4W?L8cO{Pknfjjlda_Pa|Lb=7pMgDju8qp?t39>%f2Tu5vD"
    "o}Sw}c?|krR52F8FzH#j4+r*58|!5JW-3?eRM>=lgUD7{mZ`&_FPBkSRv)k9R;3wtXrH@QvO0Cf-crMU"
    "tbq<S6?3&CdN3E_**6f9etUqcz#9lvJ=}`aaX8csu@Q*gAoKds$dzv-L95%=RxXM&sswTqvUKJ=sdjKo"
    "$09ojW{Bx9#S5%fh>!^oSUMLgzZuYjrZB|<NXH&n#*7}Z@8}g{f`FQ!O##BmqPQ$#y%fs<pW;s{;=$b*"
    "8N(&#Sy_+lOWeoGTFg^J1R!tq$d7F$CoxN{J7jjcNWHlR@}O%wQmIELra~w9+HpnzHXzHdhDRO~l&j)j"
    "Gd|I8;KA=>b%TfGiU`TP>n-Vfot|y<<(_xLbf}?5L)MIzE&7e4Dm-=<5Y=@z{bI0T43oS91DZ7z1R@J4"
    "Bg4ZP+F4|awS>sBxVk-<rrEl#=S<vq(v2lzuO^0{*LtkD&8K?CiMaDrj%mo|$8!UYt>DbjJF`TD8s5SS"
    "DqgqZiY{S6mLRTT?i?7eW2^2R@k}hM5w$(&UK;Nl9P7*q(lmRG3>Hy`^Q{)HHq4hSMkuhJgu+p~yt(BH"
    "m70b#Y8+;wujJ1*{a~HKwF-CIDemXPjnrRwI2~JAH#f>w)JziXULr*LaK2l|1p9P~`f+R;HqD0(`07~8"
    "wL@?{lXDWzt$qhtWQSFW)UA%4pdFnu7xd6thwv^U)I|+#$s9}Jq2gpCn;RT;AW+BM&@Va>BR*Z-wEP*S"
    "a?*|kVSbXdE>EkOEo)&_-_0(;fqSURW1S2gy{?*jGLPDkWXQe9VNtOZjj^Apedb{<X&w=Y8$&J`MTu=O"
    "6-8H;P}=ogcTJ{(>TX~HqDNPVH^T^pnD(N^nLGOQgPaCT{bB|Zec9G@5l2Ai^{Jq<w32G|;QFegv28>n"
    "`)*{WrexPKp43d!zK&s5(`$P`hX6L_Y)46O{ETx~lPk>Bj(^RN{`~kkkAW?Jopne%*T_&m+UI$0`uvsx"
    "?z5)x`|(lQdFlE``uZAQ>D(pLPbxnx=HKHr!o|~^{|O!#Z{UHljC}01P%vg@<BvD#=rZWAQOW?v@h9GN"
    "dqJ%r?djKv`@MCod#dhtZu5{Q$?ttmir$REKoKS~boq3H6Ucw;uEr7v=sezuiOPj<ig6lAv_<us?>Ics"
    "ZmdtVzs8+FsB%<gX26c7;-lVb(VET|Isj5v>0mu>heM)yNcOF&P&$!XZnH`%s-YPM5GP?N-%owiB1iHW"
    "{vtKf-PMu48*hkIFwO(3`KJA^MMcAz4DWQF@!vb#<uJxLas16Yp8cPpPxYC^$7xBu>fJOf4pKacu|lG1"
    "uv~cmfF>QeLOw7&)IJgM?^7T5kXTX;`&U+8J??IHAMp}Lgpus!BcJXD<1K$h@?i0>{88$na4TGspG40v"
    "hzey$NxT(ro^$m^G?1ydx<m*{<u=6U+!j&aI*_|K(QFI#xEz;0Qeo5@(F4<%@3g3@b^^G9hM`Hv$$N#S"
    ">_5o5n-&zOhxFF|yKv1G?CJNXowRXtA0C**%TE7Bcb3!)$Z&g`_e76_o`3^1P1?xI7p&kJ{sR-=j`Z;M"
    "U9)k(KnGUXGyg~Cr)dU-$$s<BK21r;PLEpu>@(YvJ0}eri8?a+nZHnb5L3B2`t!U({^sHRaw7sl*wGDq"
    "l_;ws)>)PueIdb~gYzTRaO7z<d9ZtnUOK4FXv;z2FDuRYmLhXkN!qr^Y;7*B{Dqk_d_nLI&_G<sBaRIs"
    "8+aMIo2vdnRL2>k@oH6~2Sg`fhLaO)!TvLuOiKY@%*Jz1nd}`oMeOHyOKy=k{}X77%&Iw^$Y?{yBT1;W"
    "9lD~~SYS$@@gI~UCH)#-4`yGDN$juo5TZiH86zoX=xdIt%%RR-mwUtD2Zeb#=AA%>zW#t>uxYd|s&I<W"
    "_>bxNsCqt*T?t8>Fs2#aScynE@JML;dM-;iA+HX&wAB(bxIMXHrpc^Y*%(dh_6n9*OuOTQ&Z{<1I<%cM"
    "=v2Kz2aF?+Z@y=I;*9R}I<Nv_bnB*_#igDj{ko(P^<~%<AqP_z2sVe!NSlCL<k2jqMYb*daks8jxco!L"
    "%%j>_YpNo1p>^9JN0xmR;*6?>0zrhi8Bf!(Q=c7~?q)rL)aZk4j^>XnTSUNlr)o*92W`^uhE(^8BNy`0"
    "Ms0EW#WJ~t4K!Ubbt*WOBOgmISLdfrmk|j=FVT9wq9=@EJGPCPp#woh8tGf22gTPZud&aK^A;T+Qp2RL"
    "luzXtewETX18i3ARA}0&T4jsq_88l5Z@}9!VW`PL!P$D<;Smp`iDCRG8G753Wbea)lU9qRxTEyNpx<q9"
    "J)Je<VN>t<B<sw~0Ys;xZVX`F!pZ}rMX59N4k4bFLk^ur?)n8+b7_UeiJhn>;}7M*ml!JryTJ5cQ{5Rn"
    "NQ_&W_$|hSI`&oI7|qd}uWu>ZJ^8hA#soz$ld5bDJqZF?HBe{e+VMau#at&$uWL~!%0iYTD5#Azf4)i;"
    "k6_V~pH(?ijN!CO#-$$r+Ax%U!^h|6c?CYsOBcRsZC^dtkKdoKTz+Ew{pg=De0|sNc>Ml;m#>&VK7V`r"
    "=%t*`et6CC;dFH;yNj=eq4H)Js>=~9I)m<^Z7-rqz2Rl$nR?!isZuX@{Iy`Y7L9#uD)BCCuwqN~3hFev"
    "aBCQ9WtQ#F`NokdU+;)+L_#FuMlP{cywMJ&;ncF{JYSd@a+6YY%{DtFwienOirD!XQ8wv<Y1`7`AMdzi"
    "C{pS4+Bm27_i@WPqes?kp(b1W&g2t#dt+mcktagB$NOujkcVodsE$L=8_3zCGbBnjd+BV*VD(1bcp&E@"
    "s~e<9bDH%{R*m+KB)PcL34`5Dcd0tIRm98ca|mI1=R`^jxJRs)?k+oy=O!^#f$V6d$&4G$9~^h*FOz6o"
    "4Dknqw`{%K9=54n=)X2p0nF0w(oV76+38kz6typgobQ_g+L#~^1-npHMdX{iuKqZ=jbtb4qvzwe&;7Iu"
    "AkEPWI`y06P4!Fi6<==;tV+E29@L}yN1b=qn3C)e*Las_L~<1BBqHF{Du6-v-%eiv@{`R#fSZD-SYcDF"
    "U9zY1t$g%N)%M3Yd-^Q(47=dv^`Aqk+Q!<61Ow@8nGjE6S$L0N8B-HgCn4*2!@Io_#5V9-emOqIJp(8p"
    "KhumVOsJTEh-(halk3Cm)sna5f$=Uqtd<tW`J3<B!#w}~+yJs+(y1hB)ThaLe&)r(r*Aq?+XaWx>_WSQ"
    "sxLa}=(#Do%KTR}<?p#Co#?~sLnH@YGxI+-@z;68^o0o5N%Yd2ZQTtkz^u>kf6tRwc9ZmD0Nwn3({5a1"
    "=3gHZVit^PSqqYC`OR~t?)X-20y6zc<Ap>&*p!14IwhzLGR3?-rurSnY$WhLxVe?LM?L!^INT+hZ?q|_"
    ";3-Duc6h|Xn0bfyy}Wl$^$}gM?E<jF+2_GZ67p;G@-L;=xH74bLQX~FG7{+0hShmH#-FTpJup7Qgv~wM"
    "g$_jSzELJ3O&2|6Oa-dD%<F=ZOt16UhmYMKJLAGKQFHHjpEN>Pme7a845G!j8l|1}$U6zlxgb1-Q_89J"
    "{8%AV&Z`14MzV}ww!Q<+l3{E5hk0HqKzK{vEFoh&H=aUHZYCHj><8)j{^)ZTr%L>ZOE+{*9}`+XiP9xs"
    "Xse~KgP${WSBzu^X)j#Prq$s^<zgMqXd<E&x5il3X;?}og`yF#rJJ!d92)UD)D993a09Z3rmL4d%;>9l"
    "OsN%@Ij`)w;&3_8;Scl9)URHN6DU_`k;g}!5wPhk`g?x!`fw%^%tK8p`x`5(*hoJGo_e|0)BMmv>g*iU"
    "T*>Uouwgq*nW~me8`n{%CUipzS)o(OFB;WOWE3%L7?<IKT5EN}x<FgYD<TOl*D7Sf=ejk>ZHsPeQ*)iB"
    "T0Nq9T_1}B<eVcr8?sP?&N-F8YT$T;x>bY*5W%M!W7i1MGYRZwq?`nDpVFqcCw;p=u8gkALRH$n96CoH"
    "8*rR@TmpYM4Ygg3-mS!#!c{Uq#<9|~+5}>hsiQL3(IK9jEXDbHR<cQD!VpI=yzxF^Iy4d-Rt}y|iX`#b"
    "9kwmVS^vl@n<|kpgLOujP`CUhXOwFk;c)S<-JD>3z6E<PJ@XH_JdLQLftqItF$X)#<d#Ecn?c*>=UnMI"
    "@#rr&I6tPG-ooJ`f2>Qk&wjy!z{ygjiNsldyZ6tj@kAZgEQ2<Ma3%OdZmsh<vy{;JVai0`VRkv7a-^3l"
    "F_8q9(Qvla&UZ}#CHw$U1?5YAc(;M$&csh3?>hUr)NVY}i{kUCo-e1Gctr&Hlq&(#V_7Q#z9`fZ_z~SS"
    "QyVp|J*hZ#o>>AlE0_$P(J6ix0th@Xe1{ySkY+9z57qjf=+7s@TM+U^6A-;NFPCZwTeA8+c$mLaWE(<A"
    "oSZt>NG!m`1<STYZsJaV=rKVU#%*Ie-&<xLU#6+u_RLPMmQ}oX#Y0KJMDv5xh65`vxj~!e5<Jl`&oKMw"
    "Ngw>kL~BUfdZ(%jKCMmI3MJlzTt3&~uXb&E7f;|?v>Q>fN9**hzg|9(G(1EA9nkLRuleZuz{It*eIp&w"
    "XP9VDjkaVHFqK&f<~?pJ%vOc?zOtPUc&y{0QNk*558d{7%3E?m5P3^{%aJvZ2$`1Zi79F%4NulkaS$fF"
    "K>bV<b!B;506sNZLLMtQeI}O)Z@>~9-y$si2lZw}A|M-ydszL_>W#e8fzR(WNzgz(QG)pQ*&<9RiA9%C"
    "PwLs&5tXdsE(J`mrSvpU#lb4tIZB&zG2+-GK0-D9*Xku;d_`@gI!0@w{@~$Q`z;qn4`iGyOzwJhe0sF7"
    "^Kt+#%?}i_=KQKQkX<m1c+A_@9QCz@=;>OOslO4h0X_&@oq^Ymvah=YFFR-lM3ta2l3i+>K(@0K{E;H3"
    "+ByK^ObTZ;$Y(Z^E<st3?6h|2;1tzxQMw_f`yQ+*H)>02RxdC(1TfGA;gf?h(>Mu1QYUe0U5W~!6?%*$"
    "#M2Uo5TF|xW>VhkIuG7JKSkGwVF=SQGEbaTw<ZE<cZr7nlnw#QYGoOG*ffm}*$isUfDSol2@UE*Ez!%f"
    "?<%*Q)80e9V%B&-oSr^MNHgeYc}cK_9)zWy?;kSHXulGd*QAfS)OPJSFC?-w9JZ~_?I7E9ua`cJO&e`$"
    "8?b|DYAZWK5-OB&+kxzBt*4`Ekp|pOVLFf>tSqf|k}Qku6x#C!k}Nk80ldLNj5V=D*B+{a!$sqv%}*s+"
    "qAaLfv$DvIntwDc=PK*ia9I&F+Y@+1ujZD~<l!d8-GN1qk+ViDQp#V_vK8q{N4pAweO?oue#u!aKXq=;"
    "a<XC$FFkk6CM2L1CSPTE{5&l1UXF<hSpzAUH22GJB{C(p1uL3F3YYS4rz-LH>+|C`mG)DA>*vqcN3P%P"
    "TpL@=;iLSV>-gtq9bdJ7)X&dU>iOAf{s_OnAES=?@$(8ZDE~WA=iI2@rYdbs)M+Hh9QJF>lHply@=eGa"
    "0uxw$iftZBzjuIP`S1waP~HF2_yXVGxr#v25E8N7c3{o*lrmcW2k9tp^ljvnkPdT9cWJzhd<h6N2MGoe"
    "3A<Ff0bm&thoa9$Ky9hFP_d`jevOPCoeWt^Za5A|^<tsIil#ZH8=4nxdYvRL&nBw<aTDVb(35&LD)vG`"
    "o_IIBFf^3%!b~A~w{Kkd^v@+@n8S-~6Y7o33S&Ji(c*9E-KpMX*l-@oKqCtTbxl=UzZ+EL=#e&R4rnY?"
    "hxzXQM2;+UN*WV)9TY<DcLP5;iV6c^fGWaD-HZ<tc?N>Fk~XgGBbO0xXBXx>ANFj90`>K{V=MF-qnS&b"
    "mN?XLZ$BGiU-Ia}OkPen<!0)qHI?NIg}d^o!tviH7o8TbIbu2zj#&yreqYJm<a?;?8<A${P<2daf&>wD"
    "iCgLns>h64#cP<{@MW6SO<{OtC{NgCC#A7W<xX{#uMOy2T(+%2q1ExS=P)JfPQ594T5>j0Pw2Eb$y9S-"
    "9oSiM7|zuko9;p?KZ}JrsYgV;d*I6UIJcxl8-nGGvz@k+z%?qx(62lr+Us^GiWux2&uZKD;2R-151S>?"
    "0d?b2{d#!nSS7x<1YIjE@vL2RgWH(GlgReQuN5`ORn})%ZOPrk$3Cgv*#<fyXi-^7_kGr^^-cPK;Wa>v"
    "feEL~^MNepSysE0zC~z`|8l>~$$b{QS)N5v6pmFy#6rm*l;SI)L+{yU?1DeWtlih^OXVFLVV;>eX3%sx"
    "Z&YWH?CrjULr0#&>R7b1HdjV!!Wi@1Xx<o+(j_{gzjiPLLDL)^h_Q4S$a&)wBFj=D$zw!Y2W*LKrY<iR"
    "c+9-lM0-zgOemVF6oV)8XN|hG-JJAeBm=f9m@B}J4|_0EUZWo6iq%#$I?truYZY4B#3b!0aaF&0?rCj#"
    "?DIr!UrB7dU`3HsVLiBBCuiMElv(gGT@nxa7y=xO&6bBtPR5P`txrj{v-{PYVO%%eizc@o!VzF<^}2(|"
    "c$UI3wuT1lJj`?U54`~nWmc7GepRjutUS4+NSZ@y^MsbV2Lj;JR8H;+MrQv_`6eA~Vdv(azmB|@Taf0^"
    "7>Fe>4Z!&`a1H0r(+f;pwwS2HR2nR)=o2z%fBFaz5A~DkGTMuoP8!+N&F3~VyLo&sV^P^`zt8B19!LlV"
    "0;)$`(zJSRGb@_2^f!y^_<E(%MjxFe8C%Ma3PMm?KdsT)ftwRN)OJbuTUXc2P|4P44LfUQ;Py12Kk7JS"
    "DD1zcjP>8I->>g-d>?1A9e+Q+e(T5iTYvwApP%1xKH2fNfBc@G?D#$MN2*_`|D3h?c}h(`;rlDU7UuP}"
    "Ft2}w`FO3%+gn}Ux4N8Ai|*fu{EB*?VwoM`9xt}k<Xpv@k`4FP9}dC(oEsRElSPB-a?JvyIy>&_$}}^x"
    "bk8!hk9t>@H@EDc?efCL9PaEI-Sh2w7*dajy52+rhGgT3nJL3z6!{)UtmgoUuU55AYkk}ZVZ2<j)KK?{"
    "zw}<AVSNY=i^g1VpaH(Q(on_(7Ay{aQ1(;5t<3F^z|-tu;CVUIomB$rr3_!eqU?k1@CKb5RHc=U9Xn6;"
    "F*x_P-x`)-G$am3y4smZmE28X?kr%23mi}e6owlT9RDXd5_-f~_A{X%cPbopoiIC9G_>gLM!&IEX_O>E"
    "BgZv0sB;VVg}DhPjnqJ`KjTK47K6<(WL`zAi{4z{t8(0|T92Dfd4Z^$H11BlLU0wlcshJ)!M?Xct=WWz"
    "y%b{AN?B7FFOm{Xp*W|OYFVuJ5fx3wS+UgSWG7z#(ouc=;R=+Vvs~>p53Ja$rQ;G-;Nq|@C~OXlGW{ku"
    "r^&y6nx@d{26G%9)>oV_igvK(i?D)E9%1TtMEwtNh3YEVU>L%cVU8EeI&T5%f?}nC>4`QMY}>U<bR%2b"
    "6%3Ddv8?*~*qUi3Xo|r?8hf`bF0oyymTksHzFAlDmFI~-WaGjhdtsTWMraz6wF+c9AzYC>y~Bc>rDHAW"
    "1>q&~4$#BP42_qs80dZG2kJPNHjD=0J9?oErYM98hPYi99j|<=^PD}_IbsW&1M(SOQU*1`Q5ZsAKNUzW"
    "U0(^Um|^Y*LmhlAYpAADImc~zdh}%UhXG*$Dx383uWy-<Fr+*NAY)owTiwIEp>m;%ng5ycU*2WdwNHW2"
    "#^&@(wM1lcG0Zuy&2ID$YECr9wYm9^tu0suyz{{3si%0DWVN99QlI=W{4PdZ<^7akEfJOE6lPJuWhdNi"
    "I5M4HN^+JT)>ek<W79%Jv&SUfnUuNnN369SdVxV`!8oQG;JL+0s$3+&k(`;rL_AG|(d*Whz%Dh>g#wxz"
    "Y0Q?@qJ=-X8Jx{Y^|+!Jmz6`I2eNc2@J_vEp2O#!R_|c|q;`+e1^#)$yk6REF-_D9yc>BONNySu1ua8u"
    "Akhxz(aDo}O10&_=S@V}!b|dCwO&THt1XCLtuJ-Tv3)2Xxmd<CBM_IjuUaIM{xUO~9Y!d3x7<`~o{GU~"
    "#AsKCUadpcJhL|Ag&bt^GrVhs&6hS`#sclDJG?`KwH5aX1<?U$PbocY=pR#(v8+3}UVyPON0w@gVGTO="
    "K~5sP57d?R8vKsfQ1-JMknsqP%mrVYnBHI}&9VVQ5dc4}aM8=%omS0-W`4xbMC00`8`YRy9JBC>5wKpi"
    "A5&)3A7;d~cbyj`xZ+LfSuRbNr|rf&F1IR7v60*WN5^#-;|wgw%kvkU8P`l0WwFyECOMY9RBPB7QAJFd"
    "4O!~GYWnzPi`Rn9li{eODJ?4F+BV*U0qSKO8dvYk3cj%=R`}F1eaw%1y{>9Yro6#X<seKzj*{_*oDGJr"
    "P~SR5Kwin;F|9}od7PcQv@B6x)CX`*va6yK+yiQt99Q{3*J{_MID#PzeLS+c!Wvs!5{`$-?9yFp=AbBl"
    "W-T1bOfL%N>vZZ6y|v3~MN!E}4g@rB4IJQhZ4YH}eCkXeryt4VY!biYTKFV{^x0A{1*VmH1rMn0uCC1b"
    "o|Ty*jaaiyWoIWbb!!_3R8o4HbnfTpOT@~nyzVzF1Q=}?F+~o@R(9kS`NcOzJ)mz>;|wG`=rR)(^A?#p"
    "*8_eGCo%Ng6*c|FmQg7y{S!-`PC1y$x)GUuUGA7TsOeQF`>tOoZ|3JKc1b-hIc2!jk{9XOLH&e=q>fF|"
    "VjXq3@Jn^7S|yy1k4<J)y$q0plwqupvXMRTe@(S|6uT(Y1nAD&_0&q?smplBAj>#qxsbmYKj;icYp@-="
    "xIWnH??6&2ulZm+*Mat2O2sGbfbF$lksk&(Y%RFd3b(5kIn86X@mUDc?6fcH*uufxsYdD`$m-ztUsc$y"
    "DMLSIKR~d36tGa{>{9mctr^8JX2t?DMpS614Yla4%ZgKYxXbW*Rrx14Bv-2ER%Bx%WOqQ*i#;vS7$B)^"
    "#QZ*?NG80wOV2Q-O?G1%JDmPWUrv$;@+Q%3RRc{V)I3~OED>!w?emh+Pt?j$Ol+QA;uTOtbCnT`6DW19"
    "hWSAU+<i3`_YyZUz=~eYIjn@@Z{_TbxFHqU{j{-0LMn88x)SRGQJ1TOkk$v=MB;p+Rdt{>VAIJn)arF3"
    "FSZaeONs$#i6&Z9RAC0$ZYMt#(-{N1zOU963J30H+fztv!Bq!btz1|VB1oDHyBzf#Yym@56|@R0=Yr>%"
    "`2xWIHT{#<4hpi)M}e3|+Ekh+RgdrAWVHlRnk$H?BJz;4$s{|Y-!wv!hCnKck$FtFwLKPp<P}lG0xHZu"
    "Q<`KvL2z7Xain`&yTyqyQ|yzr<A*!Wb{;dlxi+nfy-p%_63)d0AtBy*h+$jsIdg6`(Ni!2jKY@2sDpE%"
    "?;vSfBC!rL?>$V2%{UZ|yb@6+X0fi6HoMp>ah~Twoak4?>d7lT_Ow%@CuIfi5qXg4Y*?(i@)sW)mx@rR"
    "3ZT2%?=N~W&zob+mS3Zw&r%ATG;_49B$wdks+7?%JJ$s{oH8nXmK{J=alm)Au_MtC+SaHbMF($c2BVhP"
    "M70`Y<f~4-U4^bvcsdZL%~~ho4+l1+=O%bexH9&V15Go>ZZ&C}9x(7|@}t|&9p5yFnl}O1it{<m5_APe"
    "pW+w~weG;r?(;ZWLQYYmvVlbsZB{{&=bPMTU%qG=BP}S4oy*vS!L1{5%pN1En{Y0S<#5e`891$Hg!2K3"
    "Q}TWwVSrJjJyLs9v*@>ve>++!M<I6d_#EZP_3QU&HGbvso72ZnjGv!9<<V2s3{k3^kKc3e|2XT=pYv<Z"
    "KlnOYY4@X*1?JVt8_a9$vz0c(Q9@;I4E_41<<E;|E?`eHbn|&@<<$t3ZGk()iL~4(Y_gHm=kgm85y!dT"
    "8@401sG(O+0^d8qQ^$e<E!+XO;8yQaW-Q|Y7J>=}nbggcAs~u{q+oHR@KJHxYo5d=ZIoLQ6AdT++<2Us"
    "8M;z&C|tO+Y!i}%csI;L>fIbb6C7zp&L@-}3!;T|o1Yl_bfEeDI!OAvakD4YrJ><kCQyadvxd9znIy>&"
    "W5+DWLb)Mp6|}$+VN2rS(EudfAk;KhVJ+!azV|$}0pZqJts$wuG@=-XF&0C-9T({ZR#zAyNCUZc6H^54"
    "R9VW^LQc80$8j4j<lMX<1qQOSL(Q{0#S@qp3@gPsF=kx6>)af*YaWoQJY3y(S3ZHhqzfkBM&b{K|BlLv"
    "G_}p7dT!vTD{|zbV-e!;dic=4)uie^KrF7gZcA^r*-eL-H@k*MZgnO$qe5n#A$I6k`y1j+i^&?VGXaWq"
    ")GmRj`6Z9N&xJ|_L-e-BV_4=Ser2+;W1pY6%{Rv5MsHupILeOa&B#@-;^~DPbfghX(#BvUn|C*WlrRZV"
    "`1!LA3y?Ws^%&>zW|g8n&4{AQfTYC?R;hZi_biPi=G4UzA#6?(j1r<SP#&m~+gb{FhBtwMBD`Hrw?;Fs"
    "Y_wP)rOke6l=WKuVzHKn^86U9UW|QMEd%kQQe;9tYmi_K;@U-{(~@-5i$2`*d!W#QxD$~|x803vZm%)$"
    "b+V0+kOJ%xO=he?orfpLF;05w`F|8Ui!4^bfUqewg7gFZL6BxDW^Cy(vibsI>1u$$&ZaVm9#?WME)o=1"
    "fM)J)2?wg!6lf&1;ApVBXl2pyO3StpW_USG$?W7}+y?5@1Yi}Vj<=}Zr}k3ktjRo}H7N7HQnqkri}JI?"
    "j<$rV8)+OW6NAAlwAci*)zEGV(YS9Mwk#**-CYXwsPBwe$(g3Y!bkP@b<-sj?rWbvR*_LGA(C<cp&|ox"
    ">y)+QtrE`xBR87<6_8eGD<Eq?a!jC8arbW^1CUx@NAx~ZI&Hrt{k1LchMpC$Wl_g<982@GW@D~c%4<9a"
    "kPtyHV`Etd>FjPTLt9RBTOTCQkde->T4;(1)fz}FAT#4+vzodkpbT_Q%4(^TU_ub^W7Q!`aTH*R>X~lV"
    "zlPag9~XgoWyv>fo{@WUuGnMBiwj%7dJ=NvfQ4N2j#%h~z3<q6dxG&uG_~f>Hau?QCH40$xKyoz8#3GE"
    "az3C9QV+H2>!69w2KbbSJ=c>beiuis^c6rAef%XWK&Ua;b5_&ov{MQzc36KI=rGj)TAfB(nsVDD{AFvF"
    "Y=!c#slNTErJwTCzdpY6S37I#uK31rzNcT|_cMKruita2`}`R7=QpK~@2{%==l8eQpLCuWUWihZ_&4W("
    "*C5AI%l}L3IY9HE&HNBOwa}y@Ur^rLx;;#Au95DTXO41LluIpHZ9#h)>7Q;g9ow|$v`kW>)PQ%~S2a^2"
    "OUU6M$dGT!c0QfX@3}d@<W6hTjkjkEq3068&z-yqj_|n<(hR5T(anUqI|YbjsH34u@oFje4L-=D4axMW"
    "cTqLh8y;@9pkBQLk|SVC#XI(}G_40lH99oiff~1Z8&(t_<c=BQUhgvBQwFxKPM2Cks21bh&7&XLEI-R0"
    "3fFs8naQ36<LP6nH;kP3{X-U?0}LOwmm&|FwDvF8)*ldW245eF!Q&3qMb?9=8}d==L7w(qtl>2;((<7A"
    "izGo^xIYF=grboo=(t&^-o9t#e2T5PA2U`e-o?TvVh?E>HTu&Q6W@I$DIo4NGp*JJv8K=7rM;U)!QS_{"
    "Jl=JO-$rJOR`jHaU5V?>Pk+FsS47h*tEF9kAM>xi&5yLxkZ3^>WH^aNTFcwQ|7l}MnsI9jZxRKQL?#j8"
    "*E)xtVTI#TmxZ3+pfh}H?g`Tqh$?lbq>yVj9v7GBig)b0LXA;uo${FJFo|(TuJ|Z0|J^Pijzq-u4fvbU"
    "I~Wbp|B=AuEjDvzTn6h-@-gvBdH+h1yz)$6^f2w2rx2#bZA5RB&kIY)a2>f8_Gu5JrZ(v}Y{Alza6Eo_"
    "Tj3-jr0ZAEpyWC24FENNb|m9*Vz%DYbQTq57|ze_#?~opKoSE`#o6-clwQA=j3<3&Pquk29Ot-A$zil0"
    "C4ssrT*xZ@5OL*k@us8a-<vr>H7B{QDm*|LNJ&#SURa*@okKN)NlT0J8vk`ZV|jjXH^13p*HIY?9e%<;"
    "7_zX-JCr-@jG$x=%`_^mWEuaMJeehSEZJPpwn^wgQ{=#p$JwS$&BAi*m_&~G(uDp8j(Tp%<oaL&$fKPC"
    "WFk3sXP&sKS*kS$le(NAvr)gCxjP@Qnr%bm_{`P}>o|<ZCZ!9)fSLz&Y_?=5?EQG0C56kugor>ZmA_?="
    "l;UY5OqzZV0yXUID`%)S=TYS{g+$%N854rmVJ?lBGzCmXjp+!Gck3H}xU%;15UYW^Qa71w@vcu96vJli"
    "zd8h@Eu>)5P&lV>;%a6_YX-{=Ucx^kf_HgVtMlN<c4d8elR`u|MLK>X3^M>JKUTP=rYS8zGncwEOv)*O"
    "@8vD8dE(-x3`PkJ!$QMt5if*ZvMimiQ|~jRZR-tj6kyvNMkjdEUo41QEO_eO26um3^pN`S!n>%kBtOaX"
    "&OSXksSl#bd?H+4eLM9NI^{IQl1_Boj_KSSTB(M-cC;?gd#V#qUYmK!^QzN4E`O@mfkZy&dX@S_#4v9J"
    "fh2%75pmljFwA$+KRg)()6L3J8@Id#lOpo62#Ux4ylOrBC#~x(-an<BVQE7cAz6-{Mr&T6o;X#~$qcA4"
    "-HplWud!zVqHN8c9eOUO+D+DB$24tx4&76g=_2BcMg(Xy#b-@Rr;h4%%B)o1Cx`iD&k)OUpy_rtsJJn8"
    "T!&3mzUv5tH;BQqgE6{Es_KIR$8Q_{yPFKB<y$)al=+@++$~Qer@O)+_wZqFC|bT++7dTh1H&^zZXJVp"
    "u9WD3I>ylDj8^C9SQ8r!+=lFVh5oP<Hyh_u)rFO`6;u#{1gE&Y4v(kXDp?(p?bwE~k-c%efwvMJbcYa|"
    "c;N<YvJiNAj5U<+7u$+C6uO$^p^G8{HX$N}K0m?1_?0-LWw%#^yad(3eX0c&>P1mHHVWKRqAAo~mFGOn"
    "z4|Ok9O1YXa5hLjtiW-bc;bbso6FnF2dpm6EibYfDNs+(M|=zHAn}dqnBy!R75o%MCT<>9sTZnm3f^ex"
    "ElGJm5!BumYQ;L2dE^aYa)r8`=r!JaXv=$T>VIT!a&^y6v|3iuMatQ6o&67E%3e=a2*(uAz`W+7w1wF%"
    "TU9XFTvQW}nGq+MpKHyi6><03vOYz`&H&S+HLq0UOLv_m1Tl!?CIP!D&X(c&SW$`5R$x>H*)h$g@-=5l"
    "#Fcu=THGzpA~+F$uKw__cW1lCR6G#2(ZRYbh?Z6nO1)*URUA>e&7!>!b?UHXwY_6n<y^=Mjyxw75<Ap6"
    "JlQ9j{A3&ChpP=eAPLt3-Q}&@UZV3j`_ytG&{JNsqN}!q=3<T;51EAF#gG@YH03eY_9m&XR<f`f>AUOk"
    "=3R)vt(v+`3&4XX!(XBU065m!oV%Y)88<<gv`yO41W2@1L5+9#4~e1fbTFzq9EYpAwb_B*^6F0079sGT"
    "%sT+gh{8HcSkP2#z+p8V==V03#&H=aPqh~3G|QIrv0jIOdg-UizgwY!0+s@G7@M@loU4-(Y5nWatrARq"
    "S!3c^c$NjDhpGEalQR}AW%hTPP`zb3ls$fj&lruJ%441lGbe+%`)gFp19~e{#q4+pG;Z(8I8hg@<339l"
    "L7boyVqKQpArX?g(4lIutAE(@oGg7o%Zi4I2V@=AiB_ch1|_3Alzjk#=Gtv`E>5qibo4|ZwAZ*E8VIrO"
    "ucHptWyn$iL;&|X=4x{I#)Z21`&AW?!0Bm61&&2mM-NBgMvPImNOYY-R5dgV_z!qY9;;+)q_<*LLXd9v"
    "4z140$t06($x`-enj-E&r-O4*DDDZWoFj|Ykb7oni^!7W9z3#2fUyIJBnUm<3kHMC4;HIB;0GQ7Ja^|>"
    "qwk=WaWX)1#O*kHn3=%^V#X$bzF19}lg?_CAaXYQ$(cDpxNfy?4N8!0iHv@jisR9SVt^$|tz;Mh@?HD5"
    "l{X<puDd?K;3vrpgqN6oaz9sCAxSn8H6P0kQN0vJP}i3kpv`aR!6Pzsi%P=@LWgNCzCRl6Fyll@<6|cC"
    "6r0<5KUIF#MO57mlq&>I8S~yiITea%l)R+gg?~GsY2PD$_pag0_gP1__}$Xaclqt<C;!CX<1>DKf7kEu"
    "^ZD7z_j$Sc=kfcSKF$U5x8~m$IF)BF|4XRV!!FcPy|E5x=7uya%swX78z@deX~C}2eH;($j&HqtBoSBx"
    "cwCN25qpC*VYg^L$!h1knQKVCqhh`VLjbk9#N!TC#2LAOErSLc>Tx%rvA%&v6Oi3BA-v19e4=BE?|D+;"
    "h@`q5(WpbEwxdE@S*dQ!;LkFhG8)kg*Q3umZYE*Y%r_!%>Xm2m-l-RZZ~&Zy&rYAK-eQX2$u$zv;?zIY"
    "<1SePv|9nUGYTm}f`Ozvy--15XE?<?J(jzuK#m?L#R&ctV=o=$Zk|y6ZG66AXP}-9H)EIPP+Ggv=wE48"
    "F^(HD6)?p?G&mV095Bkw<Rh|-=_HO;wlt#7k9I$z;c9z@R$DTo&bf&zjL9ZF?>wyB>QKcSJe7XFC4>!="
    "o7R?mBTH1JnwZX434gU+#Z>|HKA}1Oi528;TSA~4u?`XxwfXfH&TxikgZetLG78)Yg5%00SQqtVbFL~`"
    "@kP(iK4#h;p{h$29%i-}+RS;_i5?gt$}7v%)tN52&sHyhNJ-z(<P##ZO8Jfc3iPZHn&dE9TC6Xf0mz<c"
    "pvjR6kXrr*)8swFWsPX+*9u<a+JH_p@dB|dWShZ4UY<}=(M^3&k*xNv9=b#fTz7KjCMGhVs~U$CBLVg2"
    "Rh9pR{z9wU!7v^8odCUB{Gnj;U=H|L`T(4>*{ZD<(KTTk&XbE0*1_g;s;&#?e_FI!RW!qIC^I#T1%b3U"
    "DLL7yMv;o+{H`{pFv^l!ZpUGXV(yj^7a)Zh%A8CCm)~X^^uUzUwe)&B*w4&4=bFlzvqn(2X*ghZs~^DX"
    "qoXfQ++xnp>y<h(evsiM?IG2CAgU~o6x_EqzI3rbJ&?0n&`VxHHR7i&=Wa}F(XU7a4`*`NF=eT)i$>gL"
    "GU{dcU@uO;UA<LH#rOl~=CB&y(JI82lBu}Pn4EI?=(uqqg7(Zs<Q&Ml^;MdroHd;^mXfchV?9yWgKRFO"
    "zNZe<I&Vj_w9HLh+793tv%FA}Kc9zS-J)&~t&yNIO2(~IA&vGh?m6n=z-|U*H_&wMZ@{?mFrly4iJ*{W"
    "HN?xRx?Eq7O4NTbUb<{mvS;Na_IamjUbG<g3(N0>+`}gjvZWH{R<zKmESjhsu>;C2r-C!GVkP*GS$xk3"
    "yKH~SgB-!)E@<j=eghCLQs7IGy?!i?SP_(*Uk80{#JHe(#Bj*6t~vydLlb)%tQ#e1uJmvX<jcf%m1TA4"
    "nB0<hZ^LVxnnrYGXfsq6$QX9_=W+fqzGnl4PcqRX+Z0nb0$ji&+absM1_rl)kv9%N4QV|Bps8><5>-#S"
    "U$4Ru4`~L?+!p6e)`2d-Z6A#Uwd5$T{_sIp2ZwW=JN^%d+ID>Y{-j#IO8NfzJeQ-dpYx-Z`kg*Mj_;qd"
    "l==M3<L4uX^!@u=kIxc+YpK8S`0g*K02lcGOQzLsWLj}O1&DaWRG*3HwliNh6t$%Wro+Lk^@dt1nOixW"
    "sv2hC**m}Jm<DU4qs;9_ywmOz1~0*@ggz=x%iTc&p$uhpdI%7WBk>(knyx;MX$Rmj^IfJMzh?r<T&IKU"
    "KSaS1>8-L8Rw~;_DK|wZ!NTW?Ss#`MKX0^X`bS}|>oo6FcceQpntrC$;5eub6H)F8Ro(*tqD&Kp5&JiF"
    "KNq7O*89}%qx%hcN(W`mLRu+UE5l8Re7-WE?d{KSx~Ya(_3j#)*O(c_dY&i&__(2_fxQyiv?1ITWg?Y3"
    "Eu2;wfsUhXE-KE`apQ@Jqua@^(*fEQH74>g?!(NRa|Vg#q0fnN_U0tPkrqu1X}EgwV!bQ*@r@&2s{@;n"
    "@Lb^rrzOdC;`u1UPv$T=>wg#hVg7s3V&y;e#UnrBmg{x}*FD1<bIQgJ(sqKQ&vYx+eYMVfsfWsV8c=OY"
    "Zp(3FEGG=&C}z2YgdJByYSYb^Qy<iLV}9IIn*`io90WOZD_+CLv}7ald<_!42@TK3;RNALc9h*rvgFBu"
    "5NY}|S}-bi*;0G()~j!vFOiD8YKFh0HOE}!1qwVkM1r7*J{Um<I<9e*t_LQj9iX*(uzCvA<kZ@UQCIZ0"
    "4f!=Nh8AM5W?oM<-8C?ZSi~E|uZK}CFSvz|ZI(cxY}y|u23K4-hv(iRWvEzVzE7iljWde}VIMM799(vW"
    "H?;ej85!HDYtVO}kyQaj%OJ$pNp=m!z#7cbY*;5EBR~aoHYY4UYWp>yAy!jNG)>d(e)0mk`Jt+x5y!D?"
    "5J@-`jedt!z+PuKWsr$Gwp^J?Vu~74s^EeY4f=R`y6FY2Eb(GcDk6Ilqb$^Q(_U`{41*B1XudjI{{=5>"
    "G60gOEcz%U$*qw~b2>Qe;-BN4TxW@{!w5u$qwh)UeKrb{<rI<Ox)wK8bt$c9ZOyX%t`1960R*_M;Tgsg"
    "M&Rq^MV_YCp-%Ow%NmJ!Dc1=D3vH28CsZn$Yw(gpGP4Ji4gFutFk;`{je_kL_zFRzG9Az`h|QGeMYMYu"
    "K@c@v#P=foZqzS>!XU4$ekN-{2B?gr!?E2Qy^?m7$e|>arKOfR6zDSq%{8LSQ*ji|yD&6lMS!_mezdyk"
    "46oB3Y7SNNtR#<Gwj?YfKS&^`4D7LxfqN2_(EngFbcpMj!VFptGmfSv$A2Ml=U}|fJ6or8P|Gl&Odywo"
    "Y+j4qsw~<$>_9i24B>Tgp9e@C@v?bpR!#@M_fzFqvWy=3-H?POpZ5b#+&X>%CE;xLN(YKy5=~1PvibRG"
    "%fTXNw9i^{hF*-8*u%s)Z!`5t>-O>Q8~^?5xBiy?@%=O8#rW?1=jZqdKj*zYcZ2eK)*$B!_xTyV(ntIH"
    "_$Z_P#P<8~@%i)nJ6;^xuIB$&$={Fnl0U5_KSL~K1nNq}nfv#qg!dvTb1N;(^Ox_pGI$;QQCT))<wCFJ"
    "E>0oL))g&Q57O_7ElqTo!Ku5dR(-q4%TV>yI3En`hd0Pu2RKQlAUBaj+c$CLK+|cBy9iUAmvg!8^=sd2"
    "D(|!lHA9zfGB7GDU!9{SXb>gdc`QsjsFvO6<Wz1dT15eA`elI}>WCO`-7FnU5Ws%dicq(2EZG_GT4x0t"
    "pwz-mE_TqkzgVX&BY=Zv+D#-$BJXE-CZ--Ek#ggH7~wXmrGp6f;_z_z245>Jr-JU-9c7lgE2N(^{Ce#3"
    "7+=xJmb>#Qy`3PtS1Y&$By1b)KR7WsGqw>ukXPV#xI@#X0}&>EBrSWA7mzgce&W#ZyH2r{0gBp6-lIAm"
    ">Ut-JPsN`ZHA0R5r<y-(rfVZ-0ogv||DonD_9_GrXOfVo9Won1B&ya`i<4*tV9;+kAi&a2&O)h$ped-A"
    "K*?X0_k`b^U6h9=N2kcE7{bEPH^E@Arig)4k5fy*`>jR9{p_6HwO$32bH6l6(OAyIt-w_h_~dz%#XIVl"
    "F5yD)GUjteT80kd(Gj-7iZ{@aYwrS@@9_9lBx;<}KzOf_yM%e_&uQsJF?pUF@=cFl<OE3>iQaiIxztWL"
    "7JWx9mV2Hh4PF$r_^mBc(<k+t7Qdx)vDhQ*n0jrN9L7>Xp|R$pMo>+Spx!_+T|M%N5KQHj-gf`^n8=?p"
    "sW=4K;QeAYQWnp^Z1Gcr^8j%$pDlhu(xet#N6zPwJkQf*Dy03i_V;^b##7JrQYAg0I_Hx^lgzaXGlXuA"
    "!q;kFB}1k~K@6Z0i&X7LG0&T4&u=|`mJI!wqZ?=fZI=?W-4JlpdZD%zY$)|+Sf(ua*-aFx{Y_O(k5Yr?"
    "DCYsW61n(~GEAYzf4uehXO^1Z)`mZtB~!hkwCuH<u0rc|^02VetH)MM^R!*5uGDXol6s4JN06lbBB8K9"
    "rv9G+?`t3#J!VL~gzEATxMd8~0h!N+sL-K<jb=<%3E>M+NSu?i`st2|y@=Y5C8-XwzQbP7Nvf~O!X08H"
    "y0}a}MssdTLnEXrhc8HZd3<y7(fa>4cCJfu+g1>Mp<Rc#gHPj{YdJq0yW&)yKkTnD%7Oz+`eE5ttu*8i"
    "1kUNx7lB8u*)ZVv87Dr=29sr9_mi+(8r5CW0W-oIgMj98|BUf>vVP52*j^YvqdX~_SXpHT#u>?zV<<yM"
    "=)Xb^vDhHW<XBcnnx~wo9xTV!+_(E%)&bFm2bmcEQog0Plz6o+*e!pvC=g9)f7Scb;&Py<j2=Dk&&`gI"
    "J4kf>m;+)zG1N*RFG*)f*~}j%)Qpa$gIrArMGn+MSU~`1q-+LTN5n5a7A<!C>3aWql*!Ng<5F*r%k`Pk"
    "b=NTNDE_b8Q7hcG$K@Fx@&3%=(pyd`-Q~q}tCx^2x8A<g`;_uOsP~W8?wocZ5NfLTRguYXjJUtur^8#h"
    "Z@4Si=?>7Y)s^3orbzhiL|d<iRaIt_PtAck9;E%0yZWuzKekFiO%e9I#wx2$M0{Jd4r&eBs@C_Ak$1Qy"
    "tAIjV#$c$YWgT*G7|@N&3Qz!~=DI;p1>OfaugX+PIlbqW?}s&oDo2h`F%H3Cy8Q1K6e=mNsEG%7#i_7}"
    "^bl!A?>gfY@H@E+)fKa6gMNoceIAA>$D+;)P4R|bx&T16U)V{t1z9MW6ujASLg15J)^lC*j}T5!z<vfN"
    "NbQ1cLtI>HQ0NIMPMF1rWeY;ExGC*foE&*~nXLa`1mtCBYZUzH+{O}m^*7ue>$eC37uA*r5f(+iW=^0H"
    "B{_nNY5T$%fQ-X{QEwfNeOl>lVdtgsM&d$?Gp7Xdr?!1xfE~uK@g3<;{*7QY^;=TFtKbjs{lX{y!{t@?"
    "H>+dk($jHk)es<A!>J4=PnpIT#4b^vXoLrEfU)&aEFIeeyX{;zLt4<@Z4&i9#3o?}-;)Ms&WwYDi$NdP"
    "yA6j{Mw+487wQaX4r&j&YlL7-#D`n%$%am4e?U?cH=tHxaRv?9>${|rVdIDEQ)*HQ7gE5%D$2P3iJWMt"
    "KHJ4Qie{>t6p|=E5Pd`Yn?*}y5ZB$!s&}Z_J_n}}S{xB{#>R08#-=LzS*dJ2HzJNNth|Ws0x~5KP6{y4"
    "LOIEqaSqqcA%ePy;nnb4`f%#*smkm_%!TU7y~a+pXow>aN<1lqq%V}Lt0y~sZo|1Mpn2m64`HtA%qY~r"
    "(iFt818F9!4MUyy6!oC_3knz88-)+Wz6JKz;MDRuuOzZ_^rS*TRZdE9qgxZ6{5ktjC;QQF!}K_8NX%@b"
    "jg+-GPkUxDYR!={${I=#sDoH2spfB<q<Lne@l6s3r9eQ^Tcs=FMj&P%TVOn=n(x*O!G$rIM?BALxb)*h"
    "Itg|&;~d=?<WcYOKpQ6Ed8SQ4u~SqVQv;n{xw}M$_Nbk9g49XeD<A|Jr%b&?*4#%}8QBA(`GJVe!Tsq^"
    "d-SemtayTk@Ag+tzoJog-2AFtw1P%_QTUArcrDKoZc5!KktereP3h4iKnmCX0FyqY>AX&aAZ1j$eKTcU"
    "=3apOBC0@SJnm#amHl$4JF0|cT{Cvhl>_la;T=xP*jZV{B<WEh{bXk>sf9nA_KJ%f?ZC>`7u91G=e9eu"
    "GQ7ODzoxlt&gv~6c1hCSiHllmsO!Xy3;E3BLtbAk%wtnVREOOGirZ-@X-2U|sHvGJmTZ6K)<F{2c>stY"
    "I3;I}OIW+p00@ML49s&uZWv~wS;lgoxQ;5YiOyxKm?%J0Qn8flPiNd+9*=yx#9P0`%dy1oq2C|d)}Kci"
    "nM-}{M+s2FZ4Zy|xX5~SFOO%t#GLn|QMlad7bDiatc_SFn15fu{ADitRjJGIIpB?LUG*EgAiq#@SZgu{"
    "s%3@piy?`Z1;$qFJIkR#vyT;a563~7m&LW1nFI|)$id~KE$BFCq;!~S1B)a)zZd@5A}*L)^n)y*_sgdW"
    "7%lDYeObfNZCUvXx53u&xM3^_^U~7D#}2UjHcSdu5PlA9yG?c;9R8Xmtw=6_F5M1mOmO#?)Ah>Qv<?#`"
    "jbAzra_<CqMalsIXfkirR}U-J3aJ>b&h=PI+6V3Q?MM4~KRuGiTT64xB?Zap)xnvj!CNK1DXZEa-OgrT"
    "rZQ+v)P3)_C8z|LpRK;&Uf36AvDuM&%y(+AL%ksXx(v4qo+ox@kjGX9A27$I{32OEQWDjy5;0O)NDv}*"
    "tIY?UJg&shw7k|vd4q4!sEZWH(#rRZSh12Mp{&baqJB81*r#nc<@n%{u6d^2vUS-|lLu5j!6IZ5Kz!X_"
    "uxEyffJQ4wnKkh-Nue~hoL>pciF|hgAh0=WXFpV(I4Fs^SZ5V~63}YH$W!!m#qV27M0vryOc}#+eBOK>"
    "f4vFyA)FYxWGwlWM<xirJNtE-dv`koJL@<(E>`mcVY&>ak5}y!q@ir?5|E=>UzGaCU{f5gc%DrqJrS|9"
    "po(z|`J3-O<WtKLoyM_kAYEEGD8?1&<|$r#L+m4o5)JNpW3G{%Rx}KdVm(JXXmZg8(mon`@yMN?q!~d="
    "XQp|ElOJ{)N74?sJO)3?#28G2s)&e=NkQV;2Pq4#Xs~TlG5_f6u#Ab4=BMKN*^f8a`a3zE{alFWAtn~w"
    "2ZN>(wxWWdIel}g5+%`ZcFXfXz>8HZ4HO@zJdPMpLEtX~URrHPuk9qho{v`JL^N`ZsBTF}u}Gp><432s"
    "^NJmBd47XPv84bMvj=Xr&Ld7E0h%;i`NlAzvvRGQr5|E!I;$5LfMh`s!d|lk(GlkNh(@5YpFf8xy{Lu)"
    "x;UP^ezB2PVeIDE()bqY#0bG!bb?68LLzo2&(d1GKRX_)`VTa#e2AbL5tOF!u#g!>f!3NA=XTlYG)0Kt"
    "V2>%xFfZy3)aDURXy<1bAZIu-BOv!wghTEnF`0xW9F};46TSDuwIL}pJ9EQQ5VaTy1FPX<JVP)Aqf^|4"
    "EUHl8QmL*IfZqB3=3tfHxPJkmnTOUCHBKTOx?aH~`5b#<Yzru*K-)Jl%aJBJmE$zoA5>_W;3nU0M|4KW"
    "RK|XHrl4YjX6QwR`ME~B;iw455>7=Gq3mCa@Hj^Inwr<+%T1o?sR*}!S}}v}r(IC5$2FAN!X-VQbw3{R"
    "@$THW%WcoM)?<5!Ta|C=xyfAlR-d=tOWSY#k@K_N;uq|F{~PT6OVD)N!$0!52Cs`6JSl^F*x&T`qu)zU"
    "{y~MU`dHJYuWE1!C|h&Rz^8lv1<?SvbJ-Z#XFM(G>)4BU%FKjIlijfT$bh|<QcN__T$N*;{T=YQIl?Zi"
    "2qp9upN7FLF=G6<t&@gDc7RW+fo~~}K3Rg>&iEOjvb32Cp+Me-&4@rnGb%uNR+lN;14ROwHHQa8Y;hSR"
    "AqNLaiQSG>X(1@~AC^aP#fUwPclW)rCVB_o;Z2*Nlg)Bp)$4pH)lv!ww{%*xbrD`278M7R$FnUaJ@1#g"
    "5qcm3Cm_JFbcbim;%m~x0QndStVlG_dv1WHaQ(%k=}zX9_2FLnx(K)J5|jy6oNA*511xFu>9@fMF4$dJ"
    "w78Kyj_R&D1)`}Y?29mjOg^&1S#2XHhpw9P_ls~gRCalpD=KORKO5Z4=c>95%LJ7japcX2JD@(z1LJ&7"
    "=2H*j&LpRiJsCRuRt#q+tGx|XJN$xgsH&~O7;+Lwn9d0~Fp`<}Sf*~Jsj5@3^EtLk2kk2@11ku42bd4#"
    "Q6{6E|7w}j?0W>$R>+-3_mV~KH1G2{{W<zeJp(~hxF0I!PycStem&X2gn$W@_NHEjwPG<N;VA#7L04!m"
    "J!?l6z76s_)*d@C8K;4iIYqMC<7|>KJ4#g4a4Er?Nizqg_mNyLR!LK|Gk)dhEh(!{^L<%0f_g*2_PI}C"
    "%{QibNk7RBAU_F~-E6Br9Ls6xtcTVMJ{i_U>;J{)wa4!;8-k}nI|!;7=fXWf_ke%^EB4qKjr(Ccb`pnH"
    "th7lVWu9Lgd?H~e6o)ne8D!7KWFJ}y@15dgA$LF&0g-5`!BJgn{V9<EYm`p{OOh|kI=-1!njF(B7+GJN"
    "R!N45jMLhPoN478==Cu+LCp{_DA(lH3V}4|Ld3z~v0~GMm2MBtVHh;ed6Vty?b}EqOtc-0h!<XC;f!KQ"
    "1gYs6uUU5FOEjD%Ly2K(T~9%<xJc}t^H4I1OWN)Eb#}cMRws2i=?Xh3IpV3Q*hejU@-l_;8TE4Igk2&l"
    "iZ2tIJ*v=i2|faf>@Kd--ZD{R6~xN(1KZiIPZyvZ4aU=fnagK)+TF+O9HLiVr?7D+kP6_e><&0NL2-_&"
    "NLUXV9tk!nA}F*DL_iD;QyHdUJ@?z`!;~4BLV&-+<t2`^Y;SsYd4>0J0$9PMR-|Lt!+Jg$kstjz^QbuN"
    "HmjRp%c0U#uMq@cC|oj&oc$~`Omv;48;WyeB>q-Lr*^0ncD&r7yBaIhkTchxEx(VabGbfmw{$()t#;Yd"
    "{TeUraoLoib3clf5^wjSw2gK-R&RJ54YI`R*U}&Te!u*`{B~*m{qno)3vp{ZG2M$<h@2j~V{YFH6i)_~"
    "Y-)Ejj6fG)s)ruvI6yzr;xB6$D(<7&B?Wm2GBe*UxI@U+QgrsVDn_$ES*>O#{(8ZHZpCOGG8ibUVZmv6"
    "S?vwxDJ)q)y|vGYXo70-q|VK*)R!#@vNhT?X6e<Qa_^97cazW|@O%;i008-Zm2EVcbc=>0B%ujQLb?2q"
    "lc`}sG-6m*^zyuVdG-YdcBDn^pKOm&94V}aqlV#gU*Od-8r3d#$%vqlp)C~+0guXH^JkLFqMC7h`W6?v"
    ">u<-B0dTBy35z}tFU{!BwHm?L&tip>a~W(5!Mrso=PK>XbT_9?X)C3M+`P$#yrR@gvFsuoG>i0M4!C#0"
    "#=e=cBdLR-M4<QuQ9cRyhIC^7geXfXw;x23;j#Gvb3jhrYJd|?4K@_`x>be|mZz()qaDml$-5DV*#)tV"
    "toTymP_AmvreqVwdIDjK<AQCK(f1KJ9I0=N_Lh@W5SLap3dcbOmMnHwL}EO7042C>E+^r+7yM3aEsDX~"
    "M9)csGg%zFOB`~?SUS1On~*_=6=C2NT$4rk(W)7T_L>}*x%RHkx7$6zlh#y)A#%N`Ybbd*`Uc^Q!Ny6E"
    "58JU9pzD~7?V)O?5u=-wo|IMorP0Dd*PV3?_;fTky2KhtOA2mP%ZJ$wXV<x!U&2PVI6DB^PMTgOO>j-n"
    "OCRmK*b=p5hyb(FwepFx+_H=mxoWpwcTCu=nzS6`37YqL0XYUqzZO^#f{wb4=TV%V!_0`7)wfDuiYhC3"
    "+Q(7Q!PibqNdUucl9tSD>{3O_O?86#Jcxj^V1+7DTb!>1@4Y$*hb_-Hp4EDqFdwYNPvTQpv`o7Z-%@nh"
    "r05BCSl|}FX-=%oN08zi{3ZswX>u~_p#xP#V&bWjpu<U<AeS6O&)Q8@sDlP1eSffq_cZGuHC5ter~=9Y"
    "HbgGlw4p>?_uI*}sJhKlTM8q>D8{f@6x2DZc${5hAAo4)Sz(4(zr}P#GpW7;D)ODFY~$eYS@><i91^oh"
    "_K6t6$(@RqEI9Kj<1~deuT}U;Kuc$m7N%9QC{<y^q)jvca-CF4*F0MW>r*}Ph<Z76Hi0)g^ZOh|cRXs)"
    "meOrnu90gbCC>s_Y`@aHtF>ft9mxSq7WNT{009MfM{UK)`4)vwWIH+j(OziUfN+TTPAHL3Fi45P7yF4#"
    "r|L%$f&_T&vzWa1(M5>FFAY?&OLigJtZx`QOe5#&ni~%usq7G=Mu~7@w%aN0UfWOG%Ixuajra7t9!qF{"
    "TtmOdYrVGTe!V?f+b-d8>ERj5{dQ@$`}6ULx9wO0+avemj-J=AxOe#>?tNT@DCftu{dN28@%!cYt;fIb"
    "fBbcH7vYybk4t*|`uOvY+i$;)i~RlauYW!tfBol|{~mwpf5iStO8"
)


class CertificateError(RuntimeError):
    """Raised when an exact identity, factor, chamber, or scope gate fails."""


def ftext(value: F | int) -> str:
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def _canonical_json_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def _canonical_hash(value: object) -> str:
    return hashlib.sha256(_canonical_json_bytes(value)).hexdigest()


def _assert_equal(actual: object, expected: object, message: str) -> None:
    if actual != expected:
        raise CertificateError(message)


@lru_cache(maxsize=1)
def _factor_manifest() -> dict[str, object]:
    if not FACTOR_MANIFEST_B85 or not FACTOR_MANIFEST_RAW_SHA256:
        raise CertificateError("gap-free exact factor manifest is not installed")
    try:
        compressed = base64.b85decode(FACTOR_MANIFEST_B85.encode("ascii"))
        raw = zlib.decompress(compressed)
        decoded = json.loads(raw.decode("utf-8"))
    except (ValueError, UnicodeError, zlib.error, json.JSONDecodeError) as error:
        raise CertificateError("factor manifest decoding failed") from error
    if hashlib.sha256(raw).hexdigest() != FACTOR_MANIFEST_RAW_SHA256:
        raise CertificateError("factor manifest raw hash mismatch")
    if raw != _canonical_json_bytes(decoded):
        raise CertificateError("factor manifest bytes are not canonical")
    if not isinstance(decoded, dict):
        raise CertificateError("factor manifest root is not an object")
    return decoded


@lru_cache(maxsize=1)
def phase_lines() -> tuple[tuple[int, int], ...]:
    lines = tuple(
        sorted(
            {
                (origin, shift * multiplier)
                for _, multiplier, origin in CHANNELS
                for shift in (0, 1, 2)
            }
        )
    )
    _assert_equal(len(lines), 78, "phase event-line census changed")
    return lines


@lru_cache(maxsize=1)
def phase_breakpoints() -> tuple[F, ...]:
    values = {PHASE_LEFT, PHASE_RIGHT}
    lines = phase_lines()
    for index, (left_origin, left_slope) in enumerate(lines):
        for right_origin, right_slope in lines[index + 1 :]:
            if left_slope == right_slope:
                continue
            crossing = F(
                right_origin - left_origin,
                left_slope - right_slope,
            )
            if PHASE_LEFT < crossing < PHASE_RIGHT:
                values.add(crossing)
    result = tuple(sorted(values))
    if len(result) != 109 or result[0] != 100 or result[-1] != 200:
        raise CertificateError("109-point phase breakpoint census changed")
    return result


def _haar_sign(x: F, t: F, origin: int, multiplier: int) -> int:
    displacement = x - origin
    width = multiplier * t
    if 0 <= displacement < width:
        return 1
    if width <= displacement < 2 * width:
        return -1
    return 0


def _state(x: F, t: F) -> tuple[int, ...]:
    return tuple(
        (8 // multiplier) * _haar_sign(x, t, origin, multiplier)
        for _, multiplier, origin in CHANNELS
    )


@lru_cache(maxsize=None)
def _generic_cells(
    left: F,
    right: F,
) -> tuple[tuple[tuple[int, int], tuple[int, int], tuple[int, ...]], ...]:
    sample_t = (left + right) / 2
    ordered = tuple(
        sorted(
            phase_lines(),
            key=lambda line: F(line[0]) + line[1] * sample_t,
        )
    )
    if any(
        F(ordered[index][0]) + ordered[index][1] * sample_t
        >= F(ordered[index + 1][0]) + ordered[index + 1][1] * sample_t
        for index in range(len(ordered) - 1)
    ):
        raise CertificateError("generic chamber contains an event collision")
    cells = []
    for left_line, right_line in zip(ordered, ordered[1:]):
        left_x = F(left_line[0]) + left_line[1] * sample_t
        right_x = F(right_line[0]) + right_line[1] * sample_t
        cells.append(
            (
                left_line,
                right_line,
                _state((left_x + right_x) / 2, sample_t),
            )
        )
    _assert_equal(len(cells), 77, "generic phase-cell census changed")
    return tuple(cells)


@lru_cache(maxsize=None)
def _exact_cells(t: F) -> tuple[tuple[F, F, tuple[int, ...]], ...]:
    events = tuple(sorted({F(origin) + slope * t for origin, slope in phase_lines()}))
    cells = tuple(
        (left, right, _state((left + right) / 2, t))
        for left, right in zip(events, events[1:])
    )
    if not (69 <= len(cells) <= 77):
        raise CertificateError("exact phase-cell census changed")
    return cells


def _epoch_indices(n: int) -> tuple[int, ...]:
    if n == 4:
        return tuple(
            index
            for index, (rank, _, _) in enumerate(CHANNELS)
            if rank <= 7
        )
    if n == 8:
        return tuple(
            index
            for index, (rank, _, _) in enumerate(CHANNELS)
            if rank >= 8
        )
    raise ValueError("only fixture epochs n=4 and n=8 are defined")


def _owner_full_indices(owner: tuple[int, int]) -> tuple[int, ...]:
    n, multiplier = owner
    ranks = range(3, 8) if n == 4 else range(7, 16)
    return tuple(
        CHANNELS.index((rank, multiplier, POINTS[rank])) for rank in ranks
    )


def _owner_group_indices(owner: tuple[int, int]) -> tuple[int, ...]:
    n, multiplier = owner
    ranks = range(3, 8) if n == 4 else range(8, 16)
    return tuple(
        CHANNELS.index((rank, multiplier, POINTS[rank])) for rank in ranks
    )


MATRICES = {n: membership.point_m_matrix(n) for n in (4, 8)}


def _owner_c0(owner: tuple[int, int], state: tuple[int, ...]) -> F:
    n, multiplier = owner
    indices = _owner_full_indices(owner)
    local = tuple(state[index] for index in indices)
    return F(multiplier, 128) * membership.quadratic(MATRICES[n], local)


def _validate_integer(value: object, label: str) -> int:
    if type(value) is not int:
        raise CertificateError(f"{label} must be an integer, not a boolean")
    return value


def _validate_factor(record: Mapping[str, object], chamber: int) -> dict[str, object]:
    expected_keys = {
        "chamber",
        "left",
        "right",
        "denominator",
        "rank4",
        "rank8",
        "columns",
        "factor_hash",
    }
    if set(record) != expected_keys:
        raise CertificateError("factor record keys changed")
    if _validate_integer(record["chamber"], "factor chamber") != chamber:
        raise CertificateError("factor chamber index changed")
    breakpoints = phase_breakpoints()
    if F(record["left"]) != breakpoints[chamber]:
        raise CertificateError("factor left endpoint changed")
    if F(record["right"]) != breakpoints[chamber + 1]:
        raise CertificateError("factor right endpoint changed")
    denominator = _validate_integer(record["denominator"], "factor denominator")
    rank4 = _validate_integer(record["rank4"], "factor rank4")
    rank8 = _validate_integer(record["rank8"], "factor rank8")
    if denominator <= 0 or rank4 <= 0 or rank8 <= 0:
        raise CertificateError("factor denominator or epoch rank is nonpositive")
    columns_raw = record["columns"]
    if not isinstance(columns_raw, list) or len(columns_raw) != rank4 + rank8:
        raise CertificateError("factor column count changed")
    past = set(_epoch_indices(4))
    current = set(_epoch_indices(8))
    columns: list[tuple[int, ...]] = []
    counted4 = 0
    counted8 = 0
    for column_index, raw_column in enumerate(columns_raw):
        if not isinstance(raw_column, list) or len(raw_column) != 52:
            raise CertificateError("factor column coordinate count changed")
        column = tuple(
            _validate_integer(value, f"factor column {column_index} entry")
            for value in raw_column
        )
        if sum(column) != 0 or not any(column):
            raise CertificateError("factor column is zero or lost zero sum")
        support = {index for index, value in enumerate(column) if value}
        if support <= past:
            counted4 += 1
        elif support <= current:
            counted8 += 1
        else:
            raise CertificateError("factor column crosses epoch blocks")
        columns.append(column)
    if (counted4, counted8) != (rank4, rank8):
        raise CertificateError("factor epoch rank census changed")
    factor_payload = {
        "denominator": denominator,
        "rank4": rank4,
        "rank8": rank8,
        "columns": [list(column) for column in columns],
    }
    if record["factor_hash"] != _canonical_hash(factor_payload):
        raise CertificateError("factor semantic hash mismatch")
    return {
        **factor_payload,
        "columns_tuple": tuple(columns),
        "factor_hash": record["factor_hash"],
    }


def _make_state_evaluator(
    factor: Mapping[str, object],
) -> Callable[
    [tuple[int, ...]],
    tuple[dict[int, F], tuple[F, ...], tuple[F, ...]],
]:
    denominator = factor["denominator"]
    columns = factor["columns_tuple"]
    assert isinstance(denominator, int) and isinstance(columns, tuple)
    squared_denominator = denominator * denominator
    past = set(_epoch_indices(4))
    column_epochs = tuple(
        4 if any(column[index] for index in past) else 8 for column in columns
    )

    @lru_cache(maxsize=None)
    def evaluate(
        state: tuple[int, ...],
    ) -> tuple[dict[int, F], tuple[F, ...], tuple[F, ...]]:
        total_dots = tuple(
            sum(state[index] * column[index] for index in range(52))
            for column in columns
        )
        physical = {
            n: F(
                sum(
                    total_dots[index] * total_dots[index]
                    for index, epoch in enumerate(column_epochs)
                    if epoch == n
                ),
                squared_denominator,
            )
            for n in (4, 8)
        }
        owned: list[F] = []
        demands: list[F] = []
        for owner in OWNER_ORDER:
            group = _owner_group_indices(owner)
            group_dots = tuple(
                sum(state[index] * column[index] for index in group)
                for column in columns
            )
            owned.append(
                F(
                    sum(
                        left * right
                        for left, right in zip(group_dots, total_dots)
                    ),
                    squared_denominator,
                )
            )
            demands.append(_owner_c0(owner, state))
        if sum(owned, F(0)) != physical[4] + physical[8]:
            raise CertificateError("owner shares do not recover physical energy")
        return physical, tuple(owned), tuple(demands)

    return evaluate


def _poly_add(left: tuple[F, F, F], right: tuple[F, F, F]) -> tuple[F, F, F]:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def _poly_scale(value: F, poly: tuple[F, F, F]) -> tuple[F, F, F]:
    return tuple(value * coefficient for coefficient in poly)  # type: ignore[return-value]


def _poly_eval(poly: tuple[F, F, F], t: F) -> F:
    return poly[0] * t * t + poly[1] * t + poly[2]


def _poly_minimum(
    poly: tuple[F, F, F],
    left: F,
    right: F,
) -> tuple[F, F, str]:
    candidates = [(left, "left_endpoint"), (right, "right_endpoint")]
    if poly[0] > 0:
        vertex = -poly[1] / (2 * poly[0])
        if left < vertex < right:
            candidates.append((vertex, "interior_vertex"))
    point, kind = min(candidates, key=lambda item: _poly_eval(poly, item[0]))
    return _poly_eval(poly, point), point, kind


def _epoch_polynomials(
    left: F,
    right: F,
    evaluate: Callable[
        [tuple[int, ...]],
        tuple[dict[int, F], tuple[F, ...], tuple[F, ...]],
    ],
) -> dict[int, tuple[F, F, F]]:
    coefficients = {
        n: {"Ap": F(0), "Bp": F(0), "Ad": F(0), "Bd": F(0)}
        for n in (4, 8)
    }
    for left_line, right_line, state in _generic_cells(left, right):
        delta_origin = F(right_line[0] - left_line[0])
        delta_slope = F(right_line[1] - left_line[1])
        physical, _, demands = evaluate(state)
        for n in (4, 8):
            demand = sum(
                (
                    value
                    for owner, value in zip(OWNER_ORDER, demands)
                    if owner[0] == n
                ),
                F(0),
            )
            coefficients[n]["Ap"] += delta_origin * physical[n]
            coefficients[n]["Bp"] += delta_slope * physical[n]
            coefficients[n]["Ad"] += delta_origin * demand
            coefficients[n]["Bd"] += delta_slope * demand
    return {
        n: (
            -coefficients[n]["Bp"],
            2 * coefficients[n]["Bd"] - coefficients[n]["Ap"],
            2 * coefficients[n]["Ad"],
        )
        for n in (4, 8)
    }


def _actual_endpoint_t_phi(
    t: F,
    ratio: F,
    evaluate: Callable[
        [tuple[int, ...]],
        tuple[dict[int, F], tuple[F, ...], tuple[F, ...]],
    ],
) -> tuple[F, int]:
    price = {4: F(0), 8: F(0)}
    demand = {4: F(0), 8: F(0)}
    row_count = 0
    for left, right, state in _exact_cells(t):
        physical, owned, demands = evaluate(state)
        length = right - left
        for owner, owner_value, c0 in zip(OWNER_ORDER, owned, demands):
            if t * owner_value - c0 < 0:
                raise CertificateError("factor violates an exact endpoint owner row")
            demand[owner[0]] += length * c0 / t
            row_count += 1
        for n in (4, 8):
            price[n] += length * physical[n]
    phi4 = 2 * demand[4] - price[4]
    phi8 = 2 * demand[8] - price[8]
    return t * (phi4 + ratio * phi8), row_count


def _chamber_audit(
    chamber: int,
    record: Mapping[str, object],
) -> tuple[dict[str, object], tuple[F, F]]:
    breakpoints = phase_breakpoints()
    left = breakpoints[chamber]
    right = breakpoints[chamber + 1]
    factor = _validate_factor(record, chamber)
    evaluate = _make_state_evaluator(factor)

    generic_owner_checks = 0
    for _, _, state in _generic_cells(left, right):
        _, owned, demands = evaluate(state)
        for owner_value, c0 in zip(owned, demands):
            if left * owner_value - c0 < 0:
                raise CertificateError("factor violates a left limiting owner row")
            if right * owner_value - c0 < 0:
                raise CertificateError("factor violates a right limiting owner row")
            generic_owner_checks += 2

    epoch_polys = _epoch_polynomials(left, right, evaluate)
    weighted_polys = {
        FEJER_RATIO_MIN: _poly_add(
            epoch_polys[4],
            _poly_scale(FEJER_RATIO_MIN, epoch_polys[8]),
        ),
        FEJER_RATIO_MAX: _poly_add(epoch_polys[4], epoch_polys[8]),
    }
    minima: dict[F, tuple[F, F, str]] = {}
    endpoint_owner_checks = 0
    for ratio, poly in weighted_polys.items():
        minimum = _poly_minimum(poly, left, right)
        if minimum[0] <= 0:
            raise CertificateError("weighted chamber t*Phi is not strictly positive")
        minima[ratio] = minimum
        for endpoint in (left, right):
            actual, rows = _actual_endpoint_t_phi(endpoint, ratio, evaluate)
            if actual != _poly_eval(poly, endpoint):
                raise CertificateError("collapsed endpoint t*Phi mismatch")
            endpoint_owner_checks += rows

    row = {
        "chamber_index": chamber,
        "closed_t_interval": [ftext(left), ftext(right)],
        "factor_denominator": factor["denominator"],
        "factor_ranks": {"n4": factor["rank4"], "n8": factor["rank8"]},
        "factor_hash": factor["factor_hash"],
        "generic_open_cell_count": len(_generic_cells(left, right)),
        "generic_owner_endpoint_checks": generic_owner_checks,
        "collapsed_endpoint_owner_checks_with_ratio_replay": endpoint_owner_checks,
        "epoch_t_times_Phi_polynomials": {
            f"n{n}": [ftext(value) for value in epoch_polys[n]] for n in (4, 8)
        },
        "weighted_endpoint_ratio_audits": {
            "9/16": {
                "polynomial": [
                    ftext(value) for value in weighted_polys[FEJER_RATIO_MIN]
                ],
                "minimum": ftext(minima[FEJER_RATIO_MIN][0]),
                "minimizer_t": ftext(minima[FEJER_RATIO_MIN][1]),
                "minimizer_type": minima[FEJER_RATIO_MIN][2],
            },
            "1/1": {
                "polynomial": [
                    ftext(value) for value in weighted_polys[FEJER_RATIO_MAX]
                ],
                "minimum": ftext(minima[FEJER_RATIO_MAX][0]),
                "minimizer_t": ftext(minima[FEJER_RATIO_MAX][1]),
                "minimizer_type": minima[FEJER_RATIO_MAX][2],
            },
        },
        "all_owner_rows_hold_on_closed_chamber": True,
        "both_endpoint_ratios_strictly_positive": True,
        "all_ratios_9_over_16_through_1_positive_by_affinity": True,
    }
    return row, (minima[FEJER_RATIO_MIN][0], minima[FEJER_RATIO_MAX][0])


def _overlap(width: F, distance: int) -> F:
    if distance >= width:
        return F(0)
    return (width - distance) / (width * width)


def _psi(n: int, i: int, j: int, width: F) -> F:
    middle = POINTS[j - 1] - POINTS[i]
    left = POINTS[i] - POINTS[i - 1]
    right = POINTS[j] - POINTS[j - 1]
    return (
        _overlap(width, middle)
        + _overlap(width, middle + left + right)
        - _overlap(width, middle + left)
        - _overlap(width, middle + right)
    )


def _alpha(n: int, i: int, j: int) -> F:
    return F((j - i) ** 2, 4 * n * n)


def _sources(n: int) -> tuple[tuple[int, int], ...]:
    return tuple(
        (i, j)
        for j in range(n + 2, 2 * n)
        for i in range(n, j - 1)
    )


def _primitive_direct_capacity(n: int, i: int, j: int, t: F) -> F:
    return sum(
        (
            2
            * (2**scale * t)
            * _alpha(n, i, j)
            * (
                _psi(n, i, j, 2**scale * t)
                - _psi(n, i, j, 2 ** (scale + 1) * t)
            )
            for scale in range(4)
        ),
        F(0),
    )


def _integrated_direct_demand(t: F) -> F:
    total = F(0)
    for left, right, state in _exact_cells(t):
        c0 = sum((_owner_c0(owner, state) for owner in OWNER_ORDER), F(0))
        total += (right - left) * c0 / t
    return total


def _phase_stencil_boundary_audit() -> dict[str, object]:
    prerequisite = whole.build_certificate()
    if prerequisite["integrity"]["payload_sha256"] != EXPECTED_WHOLE_STENCIL_PAYLOAD:
        raise CertificateError("whole-stencil prerequisite payload changed")
    ledger = prerequisite["whole_stencil_Abel_Gothic_ledger"]
    if ledger["lambda_equals_2M_rows_checked"] != 46:
        raise CertificateError("whole-stencil lambda=2M prerequisite changed")
    expected_census = {
        "primitive_count": 24,
        "four_corner_occurrence_count": 96,
        "distinct_nonzero_Gothic_row_count": 42,
        "mixed_sign_reused_row_count": 28,
    }
    for key, expected in expected_census.items():
        if ledger[key] != expected:
            raise CertificateError(f"whole-stencil {key} prerequisite changed")

    sample_points = set(phase_breakpoints())
    sample_points.update(
        (left + right) / 2
        for left, right in zip(phase_breakpoints(), phase_breakpoints()[1:])
    )
    identity_checks = 0
    demand_checks = 0
    nonzero_lower_boundary_samples = 0
    for t in sorted(sample_points):
        source_total = F(0)
        lower_total = F(0)
        for n in (4, 8):
            for i, j in _sources(n):
                alpha = _alpha(n, i, j)
                terminal = _psi(n, i, j, 16 * t)
                if terminal != 0:
                    raise CertificateError("16t primitive terminal is nonzero")
                direct = _primitive_direct_capacity(n, i, j, t)
                abel = 2 * t * alpha * _psi(n, i, j, t)
                abel += sum(
                    (
                        2**scale
                        * t
                        * alpha
                        * _psi(n, i, j, 2**scale * t)
                        for scale in range(1, 4)
                    ),
                    F(0),
                )
                if direct != abel:
                    raise CertificateError("phase primitive Abel identity failed")
                source_total += direct
                lower_total += 2 * t * alpha * _psi(n, i, j, t)
                identity_checks += 1
        if source_total != _integrated_direct_demand(t):
            raise CertificateError("phase primitive/direct-M demand identity failed")
        if lower_total > 0:
            nonzero_lower_boundary_samples += 1
        demand_checks += 1
    return {
        "whole_stencil_prerequisite_payload_sha256": EXPECTED_WHOLE_STENCIL_PAYLOAD,
        **expected_census,
        "lambda_equals_2M_rows_in_prerequisite": 46,
        "phase_sample_count_endpoints_plus_chamber_midpoints": len(sample_points),
        "primitive_Abel_identities_checked": identity_checks,
        "primitive_sum_equals_integrated_direct_demand_checks": demand_checks,
        "upper_16t_terminal_zero_for_every_checked_primitive": True,
        "lower_t_boundary_retained_not_dropped": True,
        "samples_with_nonzero_lower_boundary": nonzero_lower_boundary_samples,
        "aggregate_Gothic_ledger_replaced_one_for_one": True,
        "primitive_owned_cover_claimed": False,
    }


def _full_phase_audit() -> dict[str, object]:
    manifest = _factor_manifest()
    if manifest.get("schema") != "erdos1191.phase_epoch_factor_manifest.v1":
        raise CertificateError("factor manifest schema changed")
    records = manifest.get("chambers")
    if not isinstance(records, list) or len(records) != 108:
        raise CertificateError("factor manifest is not gap-free over 108 chambers")
    rows: list[dict[str, object]] = []
    minima_by_ratio = {FEJER_RATIO_MIN: [], FEJER_RATIO_MAX: []}
    for chamber, record in enumerate(records):
        if not isinstance(record, Mapping):
            raise CertificateError("factor chamber record is not an object")
        row, chamber_minima = _chamber_audit(chamber, record)
        rows.append(row)
        minima_by_ratio[FEJER_RATIO_MIN].append(chamber_minima[0])
        minima_by_ratio[FEJER_RATIO_MAX].append(chamber_minima[1])
    mu_at_min_ratio = min(minima_by_ratio[FEJER_RATIO_MIN])
    mu_at_max_ratio = min(minima_by_ratio[FEJER_RATIO_MAX])
    mu = min(mu_at_min_ratio, mu_at_max_ratio)
    if mu <= 0:
        raise CertificateError("global phase t*Phi minimum is not positive")
    normalized = mu / 200
    total_factor_columns = sum(
        len(record["columns"])
        for record in records
        if isinstance(record, Mapping) and isinstance(record.get("columns"), list)
    )
    maximum_factor_entry = max(
        abs(entry)
        for record in records
        if isinstance(record, Mapping)
        for column in record["columns"]
        for entry in column
    )
    return {
        "phase_parameterization": "t=100*2^theta, 0<=theta<=1",
        "closed_phase_interval": ["100/1", "200/1"],
        "event_line_count": len(phase_lines()),
        "phase_endpoint_count": len(phase_breakpoints()),
        "phase_endpoints": [ftext(value) for value in phase_breakpoints()],
        "event_chamber_count": len(rows),
        "covered_chamber_count": len(rows),
        "uncovered_chamber_count": 0,
        "factor_manifest": manifest,
        "factor_manifest_raw_sha256": FACTOR_MANIFEST_RAW_SHA256,
        "factor_properties": {
            "total_rational_Gram_columns": total_factor_columns,
            "maximum_absolute_integer_entry": maximum_factor_entry,
            "PSD_by_exact_rational_Gram_factor": True,
            "every_factor_column_zero_sum": True,
            "every_factor_column_supported_in_exactly_one_epoch": True,
            "every_cross_epoch_Gram_block_zero": True,
        },
        "chamber_audits": rows,
        "total_open_chamber_owner_rows": sum(
            row["generic_owner_endpoint_checks"] for row in rows
        )
        // 2,
        "total_collapsed_endpoint_owner_rows_with_shared_endpoints_repeated": sum(
            row["collapsed_endpoint_owner_checks_with_ratio_replay"]
            for row in rows
        )
        // 2,
        "endpoint_ratio_range": ["9/16", "1/1"],
        "r_9_over_16_audited_every_chamber": True,
        "r_1_audited_every_chamber": True,
        "every_r_in_closed_range_follows_by_affinity": True,
        "every_endpoint_and_quadratic_vertex_positive": True,
        "global_mu_at_r_9_over_16": ftext(mu_at_min_ratio),
        "global_mu_at_r_1": ftext(mu_at_max_ratio),
        "global_mu_min_t_times_Phi": ftext(mu),
        "normalized_log_phase_lower_bound_mu_over_200": ftext(normalized),
        "normalized_log_phase_identity": (
            "integral_0^1 Phi(100*2^theta)dtheta "
            "=integral_100^200 Phi(t)dt/(t*log(2)) "
            ">=mu/(200*log(2)) > mu/200"
        ),
    }


def _build_uncached() -> dict[str, object]:
    phase = _full_phase_audit()
    stencil = _phase_stencil_boundary_audit()
    certificate: dict[str, object] = {
        "schema": SCHEMA,
        "status": STATUS,
        "scope": {
            "fixed_a_k_equals_k_times_k_plus_100_history_only": True,
            "fixed_two_epoch_n4_n8_aggregate_model_only": True,
            "all_108_phase_chambers_and_109_endpoints_exact": True,
            "independent_zero_row_sum_PSD_epoch_blocks_only": True,
            "cross_width_coupling_inside_epochs_allowed": True,
            "all_canonical_owner_rows_checked": True,
            "Fejer_ratios_9_over_16_through_1_positive": True,
            "aggregate_whole_Gothic_replacement_only": True,
            "primitive_owned_cover_constructed": False,
            "directed_epoch_flow_constructed": False,
            "m_3_m_2_m_1_terminal_closed": False,
            "global_birth_final_terminal_ledger_constructed": False,
            "arbitrary_horizon_or_history_proved": False,
            "C058_Q1_Q2_proved": False,
            "publication_novelty_or_prize_claimed": False,
        },
        "fixture": {
            "tower": "a_k=k(k+100), 0<=k<=15",
            "epochs": [4, 8],
            "widths": ["t", "2t", "4t", "8t"],
            "upper_terminal_width": "16t",
            "t_interval": ["100/1", "200/1"],
            "physical_coordinate_count": len(CHANNELS),
            "generic_event_count": len(phase_lines()),
            "generic_positive_length_cell_count": len(phase_lines()) - 1,
            "owner_count": len(OWNER_ORDER),
            "generic_owner_cell_row_count": len(OWNER_ORDER) * 77,
            "shared_a7_endpoint_owned_once_by_past_epoch": True,
        },
        "phase_scaled_whole_stencil_ledger": stencil,
        "full_phase_chamber_cover": phase,
        "theorem_boundary": {
            "proved": (
                "on the fixed two-epoch aggregate history, exact epoch-block "
                "cross-width Gram factors cover every t in [100,200] and every "
                "Fejer ratio r in [9/16,1] with a positive normalized phase bound"
            ),
            "not_proved": (
                "primitive ownership, directed flow, the final m=3,2,1 epochs, "
                "global birth/final/terminal accounting, arbitrary histories or "
                "horizons, C058, Q1/Q2, novelty, publication, or prize eligibility"
            ),
        },
    }
    certificate["integrity"] = {
        "canonical_json": True,
        "payload_sha256": payload_hash(certificate),
    }
    return certificate


@lru_cache(maxsize=1)
def _cached_certificate_json() -> str:
    return json.dumps(
        _build_uncached(),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )


def build_certificate() -> dict[str, object]:
    return json.loads(_cached_certificate_json())


def payload_hash(certificate: Mapping[str, object]) -> str:
    payload = {key: value for key, value in certificate.items() if key != "integrity"}
    return hashlib.sha256(_canonical_json_bytes(payload)).hexdigest()


def rendered_bytes(certificate: Mapping[str, object]) -> bytes:
    return _canonical_json_bytes(certificate) + b"\n"


def _check_scalar_types(actual: object, expected: object, path: str = "root") -> None:
    if isinstance(expected, bool):
        if type(actual) is not bool:
            raise CertificateError(f"{path} must be a literal boolean")
        return
    if type(expected) is int:
        if type(actual) is not int:
            raise CertificateError(f"{path} must be an integer, not a boolean")
        return
    if isinstance(expected, Mapping):
        if not isinstance(actual, Mapping):
            raise CertificateError(f"{path} must be an object")
        for key, value in expected.items():
            if key in actual:
                _check_scalar_types(actual[key], value, f"{path}.{key}")
    elif isinstance(expected, list) and isinstance(actual, list):
        for index, (left, right) in enumerate(zip(actual, expected)):
            _check_scalar_types(left, right, f"{path}[{index}]")


def verify_certificate(certificate: Mapping[str, object]) -> None:
    if not isinstance(certificate, Mapping):
        raise CertificateError("JSON root must be an object")
    integrity = certificate.get("integrity")
    if not isinstance(integrity, Mapping):
        raise CertificateError("missing integrity row")
    if integrity.get("canonical_json") is not True:
        raise CertificateError("canonical_json must be the boolean true")
    if integrity.get("payload_sha256") != payload_hash(certificate):
        raise CertificateError("payload hash mismatch")
    expected = build_certificate()
    _check_scalar_types(certificate, expected)
    if certificate != expected:
        raise CertificateError("certificate differs from exact semantic replay")


def _rehash(certificate: dict[str, object]) -> None:
    integrity = certificate["integrity"]
    assert isinstance(integrity, dict)
    integrity["payload_sha256"] = payload_hash(certificate)


def self_check(certificate: Mapping[str, object]) -> dict[str, int]:
    verify_certificate(certificate)
    mutation_specs = (
        (("schema",), "wrong.schema"),
        (("status",), "C058_SOLVED"),
        (("scope", "C058_Q1_Q2_proved"), True),
        (("scope", "m_3_m_2_m_1_terminal_closed"), True),
        (("scope", "primitive_owned_cover_constructed"), True),
        (("fixture", "physical_coordinate_count"), 51),
        (("full_phase_chamber_cover", "event_chamber_count"), 107),
        (("full_phase_chamber_cover", "uncovered_chamber_count"), 1),
        (("full_phase_chamber_cover", "global_mu_min_t_times_Phi"), "0/1"),
        (
            (
                "full_phase_chamber_cover",
                "normalized_log_phase_lower_bound_mu_over_200",
            ),
            "0/1",
        ),
        (
            (
                "full_phase_chamber_cover",
                "chamber_audits",
                0,
                "both_endpoint_ratios_strictly_positive",
            ),
            False,
        ),
        (
            (
                "full_phase_chamber_cover",
                "factor_manifest",
                "chambers",
                0,
                "denominator",
            ),
            1,
        ),
        (
            (
                "full_phase_chamber_cover",
                "factor_manifest",
                "chambers",
                0,
                "columns",
                0,
                0,
            ),
            True,
        ),
        (
            (
                "phase_scaled_whole_stencil_ledger",
                "primitive_Abel_identities_checked",
            ),
            0,
        ),
        (
            (
                "phase_scaled_whole_stencil_ledger",
                "primitive_owned_cover_claimed",
            ),
            True,
        ),
        (("integrity", "canonical_json"), 1),
    )
    rejected = 0
    for path, value in mutation_specs:
        changed = copy.deepcopy(certificate)
        target: object = changed
        for key in path[:-1]:
            target = target[key]  # type: ignore[index]
        target[path[-1]] = value  # type: ignore[index]
        _rehash(changed)
        try:
            verify_certificate(changed)
        except CertificateError:
            rejected += 1
    if rejected != len(mutation_specs):
        raise CertificateError("a rehashed semantic mutation was accepted")
    return {
        "mutations_attempted": len(mutation_specs),
        "mutations_rejected": rejected,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--verify", type=Path)
    parser.add_argument("--self-check", action="store_true")
    arguments = parser.parse_args()
    try:
        if arguments.verify is not None:
            raw = arguments.verify.read_bytes()
            parsed = json.loads(raw.decode("utf-8"))
            if not isinstance(parsed, dict):
                raise CertificateError("JSON root must be an object")
            certificate = parsed
            if raw != rendered_bytes(certificate):
                raise CertificateError("certificate bytes are not canonical JSON")
            verify_certificate(certificate)
        else:
            certificate = build_certificate()
        if arguments.output is not None:
            arguments.output.write_bytes(rendered_bytes(certificate))
        elif arguments.verify is None:
            sys.stdout.buffer.write(rendered_bytes(certificate))
        machine_stdout = arguments.output is None and arguments.verify is None
        if not machine_stdout:
            print(f"verified payload_sha256={certificate['integrity']['payload_sha256']}")
        if arguments.self_check:
            result = self_check(certificate)
            message = (
                f"self_check mutations_attempted={result['mutations_attempted']} "
                f"mutations_rejected={result['mutations_rejected']}"
            )
            print(message, file=sys.stderr if machine_stdout else sys.stdout)
    except (CertificateError, OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
