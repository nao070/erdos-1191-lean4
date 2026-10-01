#!/usr/bin/env python3
"""Exploratory exact epsilon analysis for the finalized Hou--Zhao direction.

Offline mode verifies the PD/correlation interval and fixed-published-q
rational function.  ``--upstream`` pins the external raw certificate.
``--reoptimize`` additionally requires python-flint and proves an exact KKT
certificate at epsilon=1/462.  Nothing here concerns Erdős #1191 itself.
"""
from __future__ import annotations

import argparse
import contextlib
from decimal import Decimal, localcontext
from fractions import Fraction as F
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import sys

import hou_zhao_cross_perturbation_certificate as pinned

# det of the affected 6x6 block is a positive constant times D(e).
D = (
  2051707767720157160228913515968431069103,
  0,
  -1090358633197796493303909355562500000000000,
  0,
  79621528955194140625000000000000000000000000,
)
# Phi(e)=PHI(e)/(6250000000000000000000000000*D(e)).
PHI = (
  1579648126496907969900052799755219449397509946587270973641199934573351,
  -16789611189433600673984109322772927353173257596017494980362500000000,
  -835158523606263507429326707130833427855542304336000927907062500000000000,
  2347565758310277319420342902130626721008135422656250000000000000000000,
  60801381770307109026673820026552631865142255468750000000000000000000000000,
)
# Fixed-q product f(e)=P(e)/(PRODUCT_SCALE*D(e)).
P = (
  71343190180148696287089829461802436807482861104366060617359641343345688676330605810393731498863269,
  -688949678047903405650962466178185715108687937886243340791972944795558575230871706437109950000000,
  -35762575836734584139208303240930178216885950629887047926268055686168783718215914518659187500000000000,
  -2672666687645206198383455219767403860617056810163696987999052146289418952360509375000000000000000000,
  2519749277552345625177614029184155183837358441240592067743117767884821799218750000000000000000000000000,
  270563572640245351359418698609056893954326073841327403975727479960937500000000000000000000000000000000,
)
PRODUCT_SCALE = 39062500000000000000000000000000000000000000000000000000000
# Primitive numerator of f'(e); the omitted factor and denominator are positive.
Q = (
 -28270468120383697182468674731568953976091079926676284051590329258876000308844960990542205867471784796224030136229972118241177497,
 176612347795513752243525261721952165380836166016200287394633850264249411494408764178894084578898326951668672326470847614950000000000,
 -344035904800081830898819184678323933978085022799662911029606372976551706776553675361125032774243112285248129027323392375000000000000,
 -40853177377858395736220534257117855083821004190235861415983629925158012301864492568182491737997960192673705933593750000000000000000000,
 117086355899854789512223593125242156786195652472067423257901629009585772164661586969470622443337051684859402343750000000000000000000000,
 4001623568951131183892185385246123925139698133080858245498393263591610557735433915967324210726042114257812500000000000000000000000000000,
 -13444643474269326893158915281229156471110763056475851221082653027444695118644663558626097545092773437500000000000000000000000000000000000,
 0,
 430853706663921368453254293118714077060227737438431391134354382318728852859692077636718750000000000000000000000000000000000000000000000000,
)

CORR_LO = F(-99328875215622458703517433743,266215653825678622228000000000)  # d=29
CORR_HI = F(1512327642358025296022757086677,2129928656379216904877200000000) # d=15
ROOT_LO = F(237277724271,5000000000000)
ROOT_HI = F(474555448543,10000000000000)
FIXED_OPT_LO = F(80060813,500000000000)
FIXED_OPT_HI = F(160121627,1000000000000)
REOPT_EPSILON = F(1,462)
CLEAN_BOUND = F(94348767,100000000)
ACTIVE = tuple(i for i in range(128) if i not in (1,15))

EXPECTED_HASHES = {
 "Phi":"48833af26e3e355ec066ba167489021f098dc843d9073a9cca43186b22d94a72",
 "a":"790050d486b890c8654a2edfab1c7e22dfc1bc23537c810541081e5a3fbba9a5",
 "b":"8b9a03f83c06c7e3ca3f38b20ccf77bb161290341c8bce7b8221dbd1cf52c7d5",
 "product":"fed1b5a8d060f704ddf29a17bd69a0cb37189de3ce8d5ab188f6857536be0b55",
 "q":"67c241f79156ef8d74fed591f1756e833ddfba712a93a6c11454bec551912287",
 "y":"b8ad1a0e84b0fd111ba498bd8fdbbe78aa266d990faefea2240d32d621d65099",
 "slack":"1e1f3f5a53b6d3c14c5a2e3203d526c2c1a7ca0391ba3aab69fd96bc56ef5ba8",
}
REGRESSION_500 = {"epsilon":"1/500","payload_sha256":"f5c4a7743ad638d55c319fa23b75178fc769d7985d6080d342c62299b4872a9e",
 "product":"799578224634670764272481866540709796873919168302331459392314110216176712567272031751257288243108517066619419219187380517807268084333846060372628498931680400301285212479484790748980648505590978199909530716902435494441467886063345485819742629197034872853438214181256025040528933338436773746755674625502593445997237625288264866795244887885124282955935605742501546973041695073880294005189184851915241976693710784165510273981347229409790814154522041327293362979339701953614452933384629834373393808482420058751893179656511740709374862692057615230315534169039039538851966720726247407690194055119482190394599106796619090615038881716048358814643997714136609962526083651036991753548055453534208609637413007628744785910137148634828312751860569867216305211675828160750177391582180399747856479972959972648125186723143304691906792992563517190600597654888030224777727861128667790394450768797674951463284641774295573832487845880608690742323906810231724465972434048634034283423179139888022514106312325707855653013314765832027327910518892681476416597063697586064295633823685316863469879956201105708035508491004778452593591864471193696014553969097847895590568297643276315882967323484528568787569339620874041910527516268169902101167521351135356697300601497822369788707632829568328956976987279476831884422834755231949920171254492667881588554229020163618757704750701037950512235914145164497057942765021297840731326973010965166098586006524760066047216411193472710538453772738975512523945482040817570477895341812484373956118285002597788769467777643811552714366799427654630345006931838914382427343057395777318747840897273047973700119030876788706715378900904710033780711251346259073446022146323859767490395025215063725503843817373022534472346946941308043698632425025660190508775136821672131121149640660604994328395413843426485388183185439819291491424241338242613783488915273271480078939647800494995068235702455915290211345086097135911051301740273362099033554899622074428355209119991309846654414745573829532211817190840551165209658465576998913690613182235925859198559181044614681262559228198787141875957818891066553417216837834876467115615845294213834941853481361961169465339197054729496252688004136478363976182737692390913286644535942777680653863696266683265456446079311178105496202855814651522728065771289494546347367373564023077590532024009060524572973245525893898268253671019554964177715375683230217599047449816556512414258802207724663683530562057487904072092040876394205246828048219070413134819016605489309080869297088406095559861836246675360075611257303073982550336441341441834627349980885023364568961933630713737866120975732108474561383875715944254887015304029690959055492178434806197417120366132045202609167183480097624347736300241668314270794221413363892098369667783519268064674349923631905366105433657113883140899360109943472790402473397811890320510731171961102763053395975988585969465141896326268200384467553286163601678020876810005216421095539690080113525683444312241948714500628768214874173632725879562302103985343976369908038722710231538155464502205135151754087675237401809313372906243848383941406594944418733247677231022602284227797810570406577484829888570819940337960844728526609363922941345923158533578640672394064752104116690722695087348752223283077949821155565782227182445381184087620267612622221303285790524718307002511378218515891552685590715720607608213705317578713241426020507993496707484171696190924823816944554420501863246180167294270337236873344442154106877404116267574260236900810836522477923282186839396116902702145409732410204772542917526174443055484870923153726437791093722245129101754289890790596583803988011380807653611327621549120342755757417192322515993957042582638748156120261695004550440224687096488452827202235225136460751837/898231907347568382201728444382738517443881485994999299221454628930043044075726796870657605883317472460819096676367045611010388123901254255203652260551895074334994536073406190910608394263026419972999447631209785969767621823865859425258856305479616275064195247633879276605892022826171728657699506930089460619134853597371522315910445099993786768587505921064321613343257714816408008016691545783974781130705512664536604772056241954114555955236069843884708206799864266460469798617059734195711614758951581201715083755890393099313573771552942675190365884061656099452734248481480927900586024481213763702344131300106127971227677670466276661242419182296170297031969020941376495794233354402786592214094258666132831820843361166948842452672595790015533212924322219283782722345306067136441403101999637001054127286399172972947938317292016376509115395427727699691052686580145118597354188288410984123412417879506002556208360507837261713667426218528074325750088368581349565786325204328705239775884450563120752367577032338141175735992474898983834092647577932768520502075699594075701483832893060992869909643691071131065637945967048586684609642695505049308412387658867724659123308531776229680228866229586779390199442122744813977975798078810747968226198759101404736167201351128135067552414425171479406599601927409026333231229574685845573884163992700828198093549051563879264622474364735620356524866790146156201574045461938718743328172778592987832559891155902904232791771989131513313689229866922611691662428004330686814152243623156121291088820642063530872566111734096485445921106154073167766667913183850348856357535024209776664524388336743779075399924410022590600651008258838614924434171552992482705618142526939059603275999596203773664410048472990062966394455932017769969664483515573555501532841559665162692700501503936786982166003568201975469016242539638781141240281142802424779300546080525173286879356902356445904676828155207166973955836356192533539802890925548265170975298064155943550671057203479725966020831487282965765219445509827196460821976314629700010455352182341320548170007633278386728359487991617294746697620877085965389869447411715306270886629297179410802144301065553340661425460401205940338010272869132017982871176716178753179327680909886519306982943410572443870111092768093159574230763083839927730803085482609726803461631151201384894059976762775735789387517331686999334326257607840241303676888392166857907489235773373415833968456751351151436370981327992482429300438786843778903063187851770865704316398745767495998796169671249722540847744716777797980328767268598258704755201664029170261774803188354474031719933739569718598405361863870930957330220393940942148967775078404873993578902754866307139443518509042990562380127391785938245998119425480454110001883325529206975257903548388108733417738807274536574123994544259013874153940209482160830840346014720872700062749011357114364031526678612481537289335207663798625336121783240041920298723869189443088216648029916048498124195732034531170241378928915395510684857430220170056829184754549390263412477281348248694588392716949683352871238847708360169902809420821492654139320701122506059290901556307427500330088081097798662052319562302889444262380175597510428087636068306574952623365611535952431539208546230421381429316493176078549735918309246955437351892776420560409624622409180602526597306360148081467622734891854532552508962552974552954848191146595110416048823442080815461491050257011834466854070156091940631027974840639783485162034453123056382639361366441965470803423965597155645165478252576478007045474719110347457293479541998692979384591039834914292154473759911602210856026894973964382626019030026271400101931002487110203894559095349289850512168807231462394676521875000000000000000000000000000000000000",
 "product_sha256":"f2a43e5968bf0c657cc2793fcaabff90f68543c137edd05ffb7f3a05140080e9",
 "coefficient_decimal":"0.9434876940574035151880525370100940845949071128092548852",
 "clean_bound":"9434877/10000000","primary_1_over_462_strictly_below":True}
DEFAULT_CERTIFICATE=Path(__file__).resolve().with_name("hou_zhao_reoptimized_boundary_certificate.json")

STATUS = "exact finite F(N) coefficient certificate; no global/novelty/prize/#1191 claim"
EXPECTED_KKT = {
 "dual_positive_on_active":True,"cover_slack_nonnegative":True,
 "omitted_slack_strictly_positive":True,"stationarity_zero":True,
 "complementarity_zero":True,"primal_equals_dual":True,
 "primal_q_strictly_positive":True,
}
EXPECTED_CLAIMS = {
 "global_optimum":False,"novelty":False,"prize_claim":False,
 "erdos_1191_resolution":False,"q1_resolved":False,"q2_resolved":False,
 "compatible_history":False,"current_best":False,
 "allowed":"finite F(N) coefficient bound via the project-internal generalized master lemma",
}

def ev(poly, x:F) -> F:
    return sum(F(c)*x**i for i,c in enumerate(poly))

def trim(p:list[F]) -> list[F]:
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def derivative(p:list[F]) -> list[F]:
    return trim([F(i)*p[i] for i in range(1,len(p))] or [F(0)])

def remainder(a:list[F], b:list[F]) -> list[F]:
    a=trim(a[:]); b=trim(b[:])
    while len(a)>=len(b) and any(a):
        shift=len(a)-len(b); scale=a[-1]/b[-1]
        for i,x in enumerate(b): a[i+shift]-=scale*x
        trim(a)
    return a

def sturm(poly:tuple[int,...]) -> list[list[F]]:
    seq=[[F(x) for x in poly]]; seq.append(derivative(seq[0]))
    while any(seq[-1]):
        rem=[-x for x in remainder(seq[-2],seq[-1])]
        if not any(rem): break
        seq.append(rem)
    return seq

def variations(seq:list[list[F]], x:F) -> int:
    signs=[]
    for p in seq:
        value=ev(p,x)
        if value: signs.append(1 if value>0 else -1)
    return sum(a!=b for a,b in zip(signs,signs[1:]))

def fixed_product(x:F) -> F:
    return ev(P,x)/(PRODUCT_SCALE*ev(D,x))

def fixed_phi(x:F) -> F:
    return ev(PHI,x)/(6250000000000000000000000000*ev(D,x))

def decimal_sqrt(x:F) -> str:
    with localcontext() as ctx:
        ctx.prec=55
        return str((Decimal(x.numerator)/Decimal(x.denominator)).sqrt())

def offline_summary() -> dict[str,object]:
    disc=D[2]**2-4*D[4]*D[0]
    assert disc>0
    assert ev(D,ROOT_LO)>0>ev(D,ROOT_HI)
    assert CORR_LO < -F(1,20) < F(1,20) < CORR_HI
    seq=sturm(Q)
    assert variations(seq,-F(1,20))-variations(seq,F(1,20))==1
    assert ev(Q,FIXED_OPT_LO)<0<ev(Q,FIXED_OPT_HI)
    grid=FIXED_OPT_HI; product=fixed_product(grid)
    assert product < fixed_product(F(1,6250))
    assert product < F(94349223,100000000)**2
    return {
      "status":"exploratory finite F(N) analysis only; no novelty/global/#1191 claim",
      "correlation_interval":{"lower":str(CORR_LO),"upper":str(CORR_HI),"limiting_shifts":[29,15]},
      "pd_polynomial_low_to_high":[str(x) for x in D],
      "pd_endpoint":"rho=sqrt((-D2-sqrt(D2^2-4*D4*D0))/(2*D4))",
      "rho_bracket":[str(ROOT_LO),str(ROOT_HI)],
      "combined_feasible_rational_epsilons":"epsilon in Q and -rho < epsilon < rho",
      "fixed_q":{"Phi_formula":"PHI(e)/(6250000000000000000000000000*D(e))",
        "product_formula":"P(e)/(39062500000000000000000000000000000000000000000000000000000*D(e))",
        "P_low_to_high":[str(x) for x in P],"Phi_numerator_low_to_high":[str(x) for x in PHI],
        "derivative_numerator_low_to_high":[str(x) for x in Q],"unique_stationary_bracket":[str(FIXED_OPT_LO),str(FIXED_OPT_HI)],
        "rational_grid_epsilon":str(grid),"rational_grid_product":str(product),
        "rational_grid_coefficient_decimal":decimal_sqrt(product)},
    }

def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))

def matvec(a,x): return [dot(row,x) for row in a]

def transpose(a): return list(map(list,zip(*a)))

def inverse(a):
    n=len(a); aug=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for c in range(n):
        p=next(r for r in range(c,n) if aug[r][c]); aug[c],aug[p]=aug[p],aug[c]
        v=aug[c][c]; aug[c]=[x/v for x in aug[c]]
        for r in range(n):
            if r!=c and aug[r][c]:
                v=aug[r][c]; aug[r]=[x-v*y for x,y in zip(aug[r],aug[c])]
    return [row[n:] for row in aug]

def determinant(a):
    work=[list(row) for row in a]; out=F(1)
    for c in range(len(work)):
        p=next((r for r in range(c,len(work)) if work[r][c]),None)
        if p is None: return F(0)
        if p!=c: work[c],work[p]=work[p],work[c]; out=-out
        pivot=work[c][c]; out*=pivot
        for r in range(c+1,len(work)):
            scale=work[r][c]/pivot
            for k in range(c,len(work)): work[r][k]-=scale*work[c][k]
    return out

def block_apply(block,vector,count):
    width=len(block); out=[]
    for k in range(count): out.extend(matvec(block,vector[k*width:(k+1)*width]))
    return out

def load_upstream(path:Path):
    pinned.verify_upstream(path)
    spec=importlib.util.spec_from_file_location("hz_epsilon_external",path)
    module=importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(module)
    verify_raw_fixed_functions(module)
    return module

def raw_correlation(kernels,matrix,shift):
    return sum(matrix[r][s]*sum(kernels[r][i]*kernels[s][i+shift] for i in range(32-shift))
               for r in range(8) for s in range(8))

def verify_raw_fixed_functions(module):
    kernels=tuple(tuple(x) for x in module.kernels); gamma=tuple(module.lambdas)
    d,j,_=pinned.matrices(F(0)); base=[raw_correlation(kernels,d,k) for k in range(32)]
    slope=[raw_correlation(kernels,j,k) for k in range(32)]
    lows=[(-base[k]/slope[k],k) for k in range(32) if slope[k]>0]
    highs=[(-base[k]/slope[k],k) for k in range(32) if slope[k]<0]
    assert max(lows)==(CORR_LO,29) and min(highs)==(CORR_HI,15)
    qpub=[[gamma[r]*module.weights[r][col] for r in range(8)] for col in range(128)]
    active=(0,1,3,4,6,7)
    for e in (F(-1,100),F(-1,1000),F(0),F(1,1000),F(1,100)):
        _,_,h=pinned.matrices(e); hi=inverse(h)
        phi=sum(dot(col,matvec(hi,col)) for col in qpub)
        a=32*raw_correlation(kernels,h,0); product=a*(1+(phi-128)/16)
        assert phi==fixed_phi(e) and product==fixed_product(e)
        block=[[h[r][s] for s in active] for r in active]
        assert determinant(block)==ev(D,e)/F(390625000000000000000000000000000000000000000)

def reoptimize(module) -> dict[str,object]:
    try: import flint
    except ImportError as exc: raise RuntimeError("--reoptimize requires python-flint") from exc
    kernels=tuple(tuple(x) for x in module.kernels); gamma=tuple(module.lambdas)
    _,j,h=pinned.matrices(REOPT_EPSILON)
    hi=inverse(h); n=128; width=8
    cover=[[F(0) for _ in range(n*width)] for _ in range(n)]; rhs=[]
    for row in range(n):
        tail=F(0)
        for r,kernel in enumerate(kernels):
            for i,weight in enumerate(kernel):
                target=row+i
                if target<n: cover[row][target*width+r]+=weight
                else: tail+=gamma[r]*weight
        rhs.append(1-tail)
    selected=[cover[i] for i in ACTIVE]
    transformed=[block_apply(h,row,n) for row in selected]
    gram=[[dot(row,other) for other in transformed] for row in selected]
    fq=lambda x: flint.fmpq(x.numerator,x.denominator)
    ff=lambda x: F(int(x.numerator),int(x.denominator))
    solution=flint.fmpq_mat([[fq(x) for x in row] for row in gram]).solve(
             flint.fmpq_mat([[fq(2*rhs[i])] for i in ACTIVE]))
    y=[F(0)]*n
    for k,row in enumerate(ACTIVE): y[row]=ff(solution[k,0])
    aty=matvec(transpose(cover),y); q=[x/2 for x in block_apply(h,aty,n)]
    slack=[x-c for x,c in zip(matvec(cover,q),rhs)]
    stationarity=[2*x-z for x,z in zip(block_apply(hi,q,n),aty)]
    complementarity=[x*z for x,z in zip(y,slack)]
    phi=dot(q,block_apply(hi,q,n)); dual=dot(rhs,y)-dot(y,matvec(cover,block_apply(h,aty,n)))/4
    assert all(x>0 for x in (y[i] for i in ACTIVE)) and y[1]==y[15]==0
    assert all(x>=0 for x in slack) and slack[1]>0 and slack[15]>0
    assert not any(stationarity) and not any(complementarity) and phi==dual
    assert all(x>0 for x in q)
    a=32*sum(h[r][s]*sum(kernels[r][i]*kernels[s][i] for i in range(32)) for r in range(8) for s in range(8))
    b=1+(phi-128)/16; product=a*b
    assert product < CLEAN_BOUND**2
    qpub=[[gamma[r]*module.weights[r][col] for r in range(8)] for col in range(n)]
    phipub=sum(dot(col,matvec(hi,col)) for col in qpub); fixed=a*(1+(phipub-128)/16)
    assert product<fixed
    values={"Phi":phi,"a":a,"b":b,"product":product}
    vectors={"q":q,"y":y,"slack":slack}
    for name,value in values.items(): assert hashlib.sha256(str(value).encode()).hexdigest()==EXPECTED_HASHES[name]
    for name,value in vectors.items():
        digest=hashlib.sha256("\n".join(str(x) for x in value).encode()).hexdigest()
        assert digest==EXPECTED_HASHES[name]
    correlations=[raw_correlation(kernels,h,k) for k in range(32)]; minimum=min((x,k) for k,x in enumerate(correlations))
    margins=[h[r][r]-sum(abs(h[r][s]) for s in range(8) if s!=r) for r in range(8)]
    assert all(x>0 for x in correlations) and minimum==(F(140676565613953482417771177563,481250000000000000000000000000000),31)
    assert all(x>0 for x in margins)
    return {"epsilon":str(REOPT_EPSILON),"H":"diag(lambda)+epsilon*J","s":"1","beta":"1",
      "active_count":126,"active_constraints":list(ACTIVE),"omitted_constraints":[1,15],
      "exact_kkt":EXPECTED_KKT,
      "Phi":str(phi),"a":str(a),"b":str(b),"product":str(product),
      "coefficient_decimal":decimal_sqrt(product),"clean_bound":str(CLEAN_BOUND),
      "clean_bound_squared_minus_product":str(CLEAN_BOUND**2-product),
      "pd":{"proof":"strict symmetric diagonal dominance","gershgorin_margins":[str(x) for x in margins]},
      "correlations":{"count":32,"all_strictly_positive":True,"minimum_shift":minimum[1],"minimum_value":str(minimum[0]),
        "block_lift":"C(d)=((h-t)D_q+tD_(q+1))/h^2 with D_32=0"},
      "product_sha256":EXPECTED_HASHES["product"],"Phi_sha256":EXPECTED_HASHES["Phi"],
      "q_sha256":EXPECTED_HASHES["q"],"y_sha256":EXPECTED_HASHES["y"],"slack_sha256":EXPECTED_HASHES["slack"],
      "fixed_published_q_product":str(fixed),"fixed_product_minus_reoptimized_product":str(fixed-product),
      "strictly_below_fixed_published_q_at_same_epsilon":True}

def canonical_bytes(value) -> bytes:
    return json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()

def render(value) -> bytes:
    return (json.dumps(value,sort_keys=True,indent=2,ensure_ascii=False)+"\n").encode()

def build_certificate(module) -> dict[str,object]:
    payload={"schema":"erdos1191.hou_zhao_reoptimized_boundary.v1",
      "status":STATUS,
      "source":{"repository":pinned.UPSTREAM_REPOSITORY,"commit":pinned.UPSTREAM_COMMIT,"tree":pinned.UPSTREAM_TREE,
        "path":pinned.UPSTREAM_PATH,"sha256":pinned.UPSTREAM_SHA256,"raw_source_bundled":False},
      "direction":{"J_edges_one_based":[list(x) for x in pinned.J_EDGES],"row_sum_zero":True},
      "epsilon_feasibility":offline_summary(),"reoptimized_boundary":reoptimize(module),
      "regression_epsilon_1_over_500":REGRESSION_500,
      "claim_boundary":EXPECTED_CLAIMS}
    payload["payload_sha256"]=hashlib.sha256(canonical_bytes(payload)).hexdigest()
    return payload

def validate_certificate(payload:dict[str,object]) -> None:
    assert isinstance(payload,dict)
    body=dict(payload); supplied=body.pop("payload_sha256",None)
    if supplied!=hashlib.sha256(canonical_bytes(body)).hexdigest(): raise ValueError("payload hash mismatch")
    expected_top={"schema","status","source","direction","epsilon_feasibility","reoptimized_boundary",
      "regression_epsilon_1_over_500","claim_boundary","payload_sha256"}
    if set(payload)!=expected_top: raise ValueError("top-level key set mismatch")
    if payload.get("schema")!="erdos1191.hou_zhao_reoptimized_boundary.v1": raise ValueError("schema mismatch")
    if payload.get("status")!=STATUS: raise ValueError("status mismatch")
    expected_source={"repository":pinned.UPSTREAM_REPOSITORY,"commit":pinned.UPSTREAM_COMMIT,
      "tree":pinned.UPSTREAM_TREE,"path":pinned.UPSTREAM_PATH,"sha256":pinned.UPSTREAM_SHA256,
      "raw_source_bundled":False}
    if payload.get("source")!=expected_source: raise ValueError("source provenance mismatch")
    expected_direction={"J_edges_one_based":[list(x) for x in pinned.J_EDGES],"row_sum_zero":True}
    if payload.get("direction")!=expected_direction: raise ValueError("direction mismatch")
    if payload.get("epsilon_feasibility")!=offline_summary(): raise ValueError("epsilon analysis mismatch")
    r=payload["reoptimized_boundary"]
    expected_r_keys={"epsilon","H","s","beta","active_count","active_constraints","omitted_constraints",
      "exact_kkt","Phi","a","b","product","coefficient_decimal","clean_bound",
      "clean_bound_squared_minus_product","pd","correlations","product_sha256","Phi_sha256",
      "q_sha256","y_sha256","slack_sha256","fixed_published_q_product",
      "fixed_product_minus_reoptimized_product","strictly_below_fixed_published_q_at_same_epsilon"}
    if set(r)!=expected_r_keys: raise ValueError("reoptimized boundary key set mismatch")
    if r.get("H")!="diag(lambda)+epsilon*J": raise ValueError("matrix definition mismatch")
    if r.get("epsilon")!=str(REOPT_EPSILON) or r.get("s")!="1" or r.get("beta")!="1": raise ValueError("epsilon/normalization mismatch")
    if r.get("active_count")!=126 or r.get("active_constraints")!=list(ACTIVE) or r.get("omitted_constraints")!=[1,15]: raise ValueError("active set mismatch")
    if r.get("exact_kkt")!=EXPECTED_KKT: raise ValueError("KKT failure")
    phi,a,b,product=map(F,(r["Phi"],r["a"],r["b"],r["product"]))
    if b!=1+(phi-128)/16 or product!=a*b: raise ValueError("objective identity mismatch")
    for name,value in (("Phi",phi),("a",a),("b",b),("product",product)):
        if hashlib.sha256(str(value).encode()).hexdigest()!=EXPECTED_HASHES[name]: raise ValueError("exact objective hash mismatch")
        if name in ("Phi","product") and r.get(f"{name}_sha256")!=EXPECTED_HASHES[name]: raise ValueError("recorded objective hash mismatch")
    if r["coefficient_decimal"]!=decimal_sqrt(product): raise ValueError("decimal projection mismatch")
    if r["clean_bound"]!=str(CLEAN_BOUND) or product>=F(r["clean_bound"])**2 or F(r["clean_bound_squared_minus_product"])!=F(r["clean_bound"])**2-product: raise ValueError("clean coefficient bound mismatch")
    expected_margins=[str(x) for x in (F(4461195947,11550000000),F(118272167,1443750000),F(67671,50000000),F(139131983,1155000000),F(2312155411,11550000000),F(2832639,100000000),F(1014579901,11550000000),F(1363539539,23100000000))]
    expected_pd={"proof":"strict symmetric diagonal dominance","gershgorin_margins":expected_margins}
    if r.get("pd")!=expected_pd: raise ValueError("PD margin failure")
    corr=r["correlations"]
    expected_corr={"count":32,"all_strictly_positive":True,"minimum_shift":31,
      "minimum_value":"140676565613953482417771177563/481250000000000000000000000000000",
      "block_lift":"C(d)=((h-t)D_q+tD_(q+1))/h^2 with D_32=0"}
    if corr!=expected_corr: raise ValueError("correlation failure")
    for name in ("q","y","slack"):
        if r.get(f"{name}_sha256")!=EXPECTED_HASHES[name]: raise ValueError("KKT vector hash mismatch")
    fixed=F(r["fixed_published_q_product"]); gap=F(r["fixed_product_minus_reoptimized_product"])
    if fixed!=fixed_product(REOPT_EPSILON): raise ValueError("fixed published q product mismatch")
    if r.get("strictly_below_fixed_published_q_at_same_epsilon") is not True or gap!=fixed-product or gap<=0: raise ValueError("fixed-q comparison failure")
    regression=payload.get("regression_epsilon_1_over_500")
    if regression!=REGRESSION_500: raise ValueError("e=1/500 regression mismatch")
    regression_product=F(regression["product"])
    if hashlib.sha256(str(regression_product).encode()).hexdigest()!=regression["product_sha256"]: raise ValueError("e=1/500 product hash mismatch")
    if regression["coefficient_decimal"]!=decimal_sqrt(regression_product): raise ValueError("e=1/500 decimal mismatch")
    if regression_product>=F(regression["clean_bound"])**2: raise ValueError("e=1/500 clean bound mismatch")
    if not (product<regression_product and regression["primary_1_over_462_strictly_below"] is True): raise ValueError("primary/regression comparison failure")
    if payload.get("claim_boundary")!=EXPECTED_CLAIMS: raise ValueError("claim boundary mismatch")

def self_check(payload:dict[str,object]) -> int:
    validate_certificate(payload)
    mutations=(
      (("source","sha256"),"0"*64),(("direction","J_edges_one_based",0,2),1),
      (("source","repository"),"https://example.invalid"),(("source","path"),"wrong.py"),
      (("status",),"Q1 solved"),
      (("reoptimized_boundary","epsilon"),"1"),(("reoptimized_boundary","s"),"2"),
      (("reoptimized_boundary","beta"),"2"),(("reoptimized_boundary","active_count"),125),
      (("reoptimized_boundary","omitted_constraints",0),2),
      (("reoptimized_boundary","exact_kkt","stationarity_zero"),False),
      (("reoptimized_boundary","exact_kkt","primal_q_strictly_positive"),False),
      (("reoptimized_boundary","Phi"),"1"),(("reoptimized_boundary","product"),"1"),
      (("reoptimized_boundary","pd","gershgorin_margins",0),"-1"),
      (("reoptimized_boundary","pd","proof"),"eigenvalues looked positive"),
      (("reoptimized_boundary","correlations","minimum_value"),"-1"),
      (("reoptimized_boundary","correlations","block_lift"),"unchecked"),
      (("reoptimized_boundary","q_sha256"),"0"*64),
      (("reoptimized_boundary","fixed_published_q_product"),"1"),
      (("reoptimized_boundary","fixed_product_minus_reoptimized_product"),"-1"),
      (("reoptimized_boundary","clean_bound_squared_minus_product"),"-1"),
      (("reoptimized_boundary","coefficient_decimal"),"0"),
      (("regression_epsilon_1_over_500","payload_sha256"),"0"*64),
      (("regression_epsilon_1_over_500","product"),"1"),
      (("claim_boundary","global_optimum"),True),(("claim_boundary","novelty"),True),
      (("claim_boundary","prize_claim"),True),(("claim_boundary","erdos_1191_resolution"),True),
      (("claim_boundary","q1_resolved"),True),(("claim_boundary","q2_resolved"),True),
      (("claim_boundary","compatible_history"),True),(("claim_boundary","current_best"),True),
    )
    for path,replacement in mutations:
        value=json.loads(json.dumps(payload)); cursor=value
        for key in path[:-1]: cursor=cursor[key]
        cursor[path[-1]]=replacement; value.pop("payload_sha256",None)
        value["payload_sha256"]=hashlib.sha256(canonical_bytes(value)).hexdigest()
        try: validate_certificate(value)
        except ValueError: pass
        else: raise ValueError(f"mutation accepted: {path}")
    deletions=(("reoptimized_boundary","exact_kkt","stationarity_zero"),
      ("source","repository"),("reoptimized_boundary","pd","proof"),
      ("reoptimized_boundary","correlations","block_lift"))
    for path in deletions:
        value=json.loads(json.dumps(payload)); cursor=value
        for key in path[:-1]: cursor=cursor[key]
        del cursor[path[-1]]; value.pop("payload_sha256",None)
        value["payload_sha256"]=hashlib.sha256(canonical_bytes(value)).hexdigest()
        try: validate_certificate(value)
        except ValueError: pass
        else: raise ValueError(f"deletion accepted: {path}")
    additions=(("q1_resolved",True),("reoptimized_boundary",{"current_best":True}))
    for key,replacement in additions:
        value=json.loads(json.dumps(payload))
        if key=="reoptimized_boundary": value[key].update(replacement)
        else: value[key]=replacement
        value.pop("payload_sha256",None)
        value["payload_sha256"]=hashlib.sha256(canonical_bytes(value)).hexdigest()
        try: validate_certificate(value)
        except ValueError: pass
        else: raise ValueError(f"addition accepted: {key}")
    bad=dict(payload); bad["payload_sha256"]="f"*64
    try: validate_certificate(bad)
    except ValueError: pass
    else: raise ValueError("hash mutation accepted")
    return len(mutations)+len(deletions)+len(additions)+1

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--upstream",type=Path)
    parser.add_argument("--reoptimize",action="store_true")
    parser.add_argument("--output",type=Path)
    parser.add_argument("--verify",type=Path)
    parser.add_argument("--self-check",action="store_true")
    args=parser.parse_args(argv)
    summary=offline_summary(); payload=None
    if args.reoptimize and not args.upstream: parser.error("--reoptimize requires --upstream")
    if args.upstream:
        module=load_upstream(args.upstream); summary["upstream_replay"]="passed"
        if args.reoptimize: payload=build_certificate(module)
    if args.output:
        if payload is None: parser.error("--output requires --upstream and --reoptimize")
        args.output.write_bytes(render(payload)); print(f"wrote {args.output}")
        print(f"payload_sha256={payload['payload_sha256']}")
    if args.verify:
        value=json.loads(args.verify.read_text(encoding="utf-8")); validate_certificate(value)
        if args.verify.read_bytes()!=render(value): raise ValueError("certificate is not byte-canonical")
        print(f"certificate verify: PASS {value['payload_sha256']}")
        if args.self_check: print(f"self-check: PASS ({self_check(value)} mutations rejected)")
    elif args.self_check:
        if payload is None: parser.error("--self-check requires --verify or --upstream --reoptimize")
        print(f"self-check: PASS ({self_check(payload)} mutations rejected)")
    if not args.output and not args.verify: print(json.dumps(payload or summary,sort_keys=True,indent=2))
    return 0

if __name__=="__main__": raise SystemExit(main())
