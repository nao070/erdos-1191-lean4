#!/usr/bin/env python3
"""Exact fixed-fixture signed coordinate-owner graph/PSD master certificate.

The exact arithmetic in this file is deliberately finite.  It proves two
no-go statements for the fixed 16-mark, four-width fixture and records one
rational cross-epoch PSD witness.  It does not construct a directed source
ledger and does not resolve C058 or the underlying Erdős problem.
"""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
from functools import lru_cache
import hashlib
from itertools import combinations
import json
from pathlib import Path
import sys
from typing import Mapping, Sequence

import direct_b_membership_sddm_lp_certificate as membership


SCHEMA = "erdos1191.route_c_signed_coordinate_owner_master_lp.v1"
STATUS = "EXACT_FIXED_ZERO_ROW_SUM_PSD_AND_GRAPH_ROOT_PHI_NO_GO_C058_OPEN"
HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_SIGNED_COORDINATE_OWNER_MASTER_LP_certificate.json"

POINTS = tuple(k * (k + 100) for k in range(16))
WIDTHS = (100, 200, 400, 800)
CHANNELS = tuple((k, width, POINTS[k]) for width in WIDTHS for k in range(3, 16))
OWNER_ORDER = tuple((n, width) for width in WIDTHS for n in (4, 8))


class CertificateError(RuntimeError):
    """Raised when an exact witness, scope gate, or byte replay fails."""


GRAPH_PRIMAL = {
    ((5, 200), (10, 400)): F(148825, 4388),
    ((5, 200), (11, 400)): F(70575, 4388),
    ((8, 200), (5, 400)): F(1225, 1097),
    ((8, 200), (10, 400)): F(2450, 1097),
    ((8, 200), (11, 400)): F(15175, 2194),
    ((9, 200), (5, 400)): F(1225, 1097),
    ((13, 200), (15, 200)): F(12775, 4388),
    ((14, 200), (12, 400)): F(1875, 1097),
    ((3, 400), (4, 400)): F(48875, 1097),
    ((6, 400), (7, 400)): F(48875, 1097),
    ((7, 400), (8, 400)): F(8575, 1097),
    ((8, 400), (9, 400)): F(500, 1097),
    ((8, 400), (10, 400)): F(16675, 2194),
    ((11, 400), (15, 400)): F(15175, 2194),
    ((13, 400), (15, 400)): F(2000, 1097),
    ((14, 400), (15, 400)): F(176975, 17552),
    ((7, 800), (8, 800)): F(1045, 4),
    ((8, 800), (9, 800)): F(90),
    ((13, 800), (15, 800)): F(755, 16),
    ((14, 800), (15, 800)): F(685, 16),
}

NO_CROSS_DUAL = {
    ((4, 200), (525, 616)): F(1160397, 10000),
    ((4, 200), (636, 709)): F(951597, 10000),
    ((4, 200), (749, 816)): F(1136403, 10000),
    ((4, 200), (836, 849)): F(927603, 10000),
    ((8, 200), (981, 1036)): F(529407, 2500),
    ((8, 200), (1725, 1744)): F(1129941, 10000),
    ((8, 200), (1796, 1825)): F(1318059, 10000),
    ((4, 400), (525, 616)): F(1327797, 10000),
    ((4, 400), (709, 725)): F(615447, 10000),
    ((4, 400), (725, 736)): F(518553, 10000),
    ((4, 400), (1109, 1149)): F(621, 5),
    ((8, 400), (1221, 1264)): F(2799081, 10000),
    ((8, 400), (1344, 1381)): F(1494927, 10000),
    ((8, 400), (1469, 1500)): F(1321371, 10000),
    ((8, 400), (1744, 1781)): F(338301, 10000),
    ((8, 400), (1869, 1900)): F(257247, 2500),
    ((8, 400), (1900, 1909)): F(355167, 10000),
    ((8, 400), (1996, 2016)): F(3483, 20),
    ((8, 800), (1100, 1109)): F(188019, 10000),
    ((8, 800), (1181, 1200)): F(6345981, 10000),
    ((8, 800), (1221, 1264)): F(515943, 10000),
    ((8, 800), (1300, 1321)): F(188019, 5000),
    ((8, 800), (1421, 1436)): F(828981, 10000),
    ((8, 800), (1549, 1569)): F(101007, 625),
    ((8, 800), (1596, 1621)): F(10773, 20),
    ((8, 800), (1664, 1669)): F(3159, 20),
    ((8, 800), (1869, 1900)): F(120591, 5000),
    ((8, 800), (2349, 2396)): F(163809, 1250),
}

FULL_GRAPH_DUAL = {
    ((4, 200), (525, 616)): F(31779, 200),
    ((4, 200), (636, 709)): F(50342391, 500000),
    ((4, 200), (836, 849)): F(16677837, 200000),
    ((4, 200), (864, 925)): F(17305893, 500000),
    ((8, 200), (981, 1036)): F(149927679, 500000),
    ((8, 200), (1100, 1109)): F(46206963, 1000000),
    ((8, 200), (1725, 1744)): F(38472093, 250000),
    ((8, 200), (1796, 1825)): F(28847907, 250000),
    ((4, 400), (709, 725)): F(36037287, 500000),
    ((4, 400), (725, 736)): F(26332713, 500000),
    ((4, 400), (1109, 1149)): F(6831, 50),
    ((4, 400), (1264, 1300)): F(13213827, 1000000),
    ((8, 400), (1149, 1181)): F(166827573, 1000000),
    ((8, 400), (1216, 1221)): F(3318183, 125000),
    ((8, 400), (1221, 1264)): F(148176963, 1000000),
    ((8, 400), (1344, 1381)): F(145987281, 1000000),
    ((8, 400), (1469, 1500)): F(36645939, 250000),
    ((8, 400), (1744, 1781)): F(4441239, 40000),
    ((8, 400), (1869, 1900)): F(120524877, 1000000),
    ((8, 400), (1900, 1909)): F(3928023, 125000),
    ((8, 400), (1996, 2016)): F(20243619, 125000),
    ((8, 400), (2021, 2125)): F(1851003, 62500),
    ((4, 800), (1264, 1300)): F(41097573, 1000000),
    ((4, 800), (1421, 1436)): F(73792719, 1000000),
    ((4, 800), (1696, 1725)): F(21880683, 1000000),
    ((4, 800), (1825, 1869)): F(45018963, 500000),
    ((8, 800), (1596, 1621)): F(98901, 400),
    ((8, 800), (1664, 1669)): F(60291, 400),
    ((8, 800), (2349, 2396)): F(37719, 200),
    ((8, 800), (2464, 2525)): F(9207, 100),
}

# Columns of a rational Gram factor B.  The coordinate matrix in the PSD
# witness is X=B B^T; every integer below is divided by 5,200,000.
PSD_FACTOR_DENOMINATOR = 5_200_000
PSD_FACTOR_COLUMNS = (
    (-155,-363,-1299,-1039,-1507,1197,1613,1353,833,-259,-987,-103,573,-1403,625,365,-415,2237,-623,-1039,-1299,-675,-311,105,-1663,1,2029,-51,-1455,-2131,469,1509,-363,-103,209,1613,1301,-1663,-1351,-883,469,1665,417,989,573,729,-883,-51,1145,729,261,-935),
    (677,1093,573,261,-987,-883,105,833,1,-103,-467,-727,1405,1,469,1457,-259,1145,-4367,-4159,-831,-519,1613,53,1041,-519,-675,-675,-207,1405,2341,-363,521,1041,1665,-1039,5201,105,-1403,6813,-363,-3587,-623,-1975,-1767,-2703,-2755,1977,677,313,-1455,625),
    (571,-521,-1301,155,-2393,259,1923,2391,1091,207,1091,-1197,-1821,-157,1559,-625,-3069,2599,-989,-1665,-157,-833,-1925,103,2547,2079,-573,-521,1143,-2497,467,-7229,883,5459,-521,1351,-5305,5147,2443,-1249,4003,883,1923,-1457,-1821,-1197,-3381,51,2339,1663,-2601,675),
    (-1198,-1458,-626,362,1038,2234,2494,2078,2286,-2,-470,-522,1714,778,-366,-1250,-1718,-3330,-2,570,-106,2338,-2810,1454,-1510,-938,-2550,-2654,6030,-1666,-3902,4418,-7698,6134,1246,258,-262,154,-3486,1038,1194,-5306,1610,2026,1870,-1562,1974,-106,-418,2910,-1510,-782),
    (882,570,-574,-522,154,-1198,-938,-1614,-1978,-470,-210,-2758,1142,-782,518,362,-262,1974,310,-418,518,466,570,4938,3742,-4786,934,2234,-1354,-3070,726,7850,-3850,-522,1610,-4526,-2758,8994,-1770,-1718,414,4990,-1354,-2,-4474,-3538,-2030,5874,-2342,-1198,2910,-1666),
    (-1301,-781,623,467,-677,2027,1715,363,-677,-365,-1561,-1301,-2289,519,-365,-1353,467,-625,-2965,2391,-1873,-2393,-157,1611,-625,-5045,1611,2287,-2029,4835,3847,-2705,7175,10607,-1613,-6969,6135,4627,-7437,-6865,-6605,3587,-885,51,2963,-3693,7591,-4993,-573,5459,-2289,51),
    (1248,1560,1612,1092,364,-1456,0,884,3380,2340,-52,1144,-156,1716,988,2652,1456,-1976,1456,-416,-676,-156,6032,-1092,-2288,-4108,2184,-8892,884,3692,520,-5876,-7800,-1560,1092,-5928,10140,-3172,3172,-10140,12428,2652,4264,-4888,-11856,4316,1144,468,-6448,6500,884,-3328),
    (-5094,-6550,-830,3590,2914,158,106,262,-570,-2546,-206,990,470,4890,-6394,-6758,-2026,2914,2446,-206,210,4162,3486,-882,418,158,5306,-5874,-2598,-2702,7594,8530,3122,12066,5410,9882,106,-882,4838,-4314,-518,-5198,-12270,-14090,-8630,5150,5202,-986,3486,-8682,990,-50),
    (1769,-1455,1197,-571,-935,1301,365,-207,417,-571,-1403,-103,261,4525,-1611,3329,4629,2393,3641,2081,-3431,1145,-519,-467,-3067,209,-14871,6553,-3171,6553,-16743,7489,12377,-2703,1613,3277,5929,6553,-11179,-8683,11753,-5355,989,-2235,-7539,885,-8111,-4055,13105,-4003,-2131,781),
    (-418,2702,1142,-1302,-678,-574,466,-314,206,-2810,-834,-1302,-314,-3174,7486,10918,7798,-1042,-1978,-1926,-3746,934,1142,2026,-158,726,2962,-12118,2754,6186,1870,11334,-626,-1978,50,8734,-4526,-1770,8006,-11858,-14042,986,22878,-7646,-4110,-16538,570,-2966,2598,-7230,-11754,13258),
    (1612,-624,260,3536,104,-624,832,624,-572,104,-1716,988,624,6396,-780,-5460,-6188,-156,-2756,208,-1092,780,-936,-676,-1040,1092,-10192,8788,7540,-3692,-5668,2548,780,4680,780,4992,12636,-13936,18252,-6032,1456,17784,-21476,22048,-11232,-18616,-2964,2860,-6292,-104,-14508,15028),
    (-523,1141,-2187,413,-2915,309,-575,1349,309,-783,-1823,-991,-1511,-1615,9149,-3,-4839,-3591,3221,2441,2701,-419,-263,621,-575,-3,-10455,-1511,13361,-2915,-7387,-4059,1557,4001,3117,4625,2805,-523,-2187,15389,-27355,17261,7953,2805,-31567,14817,3533,-9415,9305,1089,9669,-12951),
    (2652,2964,-1612,-728,364,-780,-676,52,-468,-728,-2080,-936,-416,1664,5616,-884,-6916,312,-936,-2236,-4108,-1248,2444,-1144,-312,-832,-17212,6760,15340,-4368,-14404,6864,-2132,728,-1144,-3640,7644,-6812,6292,3276,-2236,30316,-3692,-49036,29744,7228,-3432,8580,-1924,6552,-7436,-884),
)

# The zero-row-sum PSD dual uses row weights numerator / 1,000,000.  Row
# order is OWNER_ORDER-major, then the 76 common cells from left to right.
PSD_DUAL_DENOMINATOR = 1_000_000
PSD_DUAL_NUMERATORS = (
    (0,10165716),(7,3326994),(12,70264755),(16,40405068),(17,44635140),
    (92,44927586),(93,15475482),(101,607167),(103,13075623),(105,4117608),
    (108,13664475),(113,8040582),(118,19365093),(120,13031766),
    (126,29024721),(127,36375471),(128,9449253),(131,30427155),
    (132,34628517),(152,40091733),(154,23045319),(156,1941390),
    (157,78629067),(160,55345653),(161,13590621),(163,1290465),
    (164,71650161),(165,983961),(167,6503607),(168,73029825),
    (169,13153140),(170,765072),(171,7820802),(172,19903752),
    (173,20001960),(174,15291045),(175,2326203),(177,55286451),
    (244,47451789),(245,6238287),(247,13544784),(248,76331376),
    (249,27531702),(252,14554782),(253,49738788),(254,9326988),
    (256,4561326),(258,20487357),(259,16000578),(261,6725268),
    (262,8409357),(263,12237489),(264,24925230),(265,3093453),
    (266,8677449),(267,19187289),(268,13010481),(269,6931386),
    (271,4667355),(272,39817602),(274,14662692),(276,23192136),
    (277,14138586),(278,25261929),(279,43212510),(281,13071564),
    (282,61547607),(283,43380315),(284,728937),(286,59470686),
    (287,20736936),(289,114027606),(306,16534089),(307,22888998),
    (309,61007661),(310,16057206),(312,33199848),(314,20738718),
    (315,25396074),(316,49088556),(318,9959697),(320,70686198),
    (322,4842981),(323,4162257),(324,42492582),(329,49858380),
    (331,34194699),(333,7616367),(334,2047023),(335,44956494),
    (338,7185420),(339,7979004),(340,45957186),(341,2799522),
    (342,3765366),(343,23977998),(344,8859312),(345,185922),
    (396,28726929),(397,29523879),(398,22287672),(401,26910576),
    (402,33091245),(403,14903658),(404,7043652),(405,23766138),
    (406,35828892),(407,33691185),(408,2151270),(410,59068449),
    (411,3989205),(412,26260641),(413,9023454),(414,18340146),
    (415,40183902),(416,18638136),(417,17505180),(418,4726557),
    (419,14156109),(420,36459720),(421,31919085),(422,13739616),
    (424,19323117),(425,8009397),(427,11796048),(428,17296389),
    (429,22001859),(430,20165607),(431,23768316),(432,33231132),
    (433,21859200),(434,47937780),(435,17960679),(436,16129080),
    (437,22450626),(438,66372768),(439,16048692),(440,51381),
    (441,103532913),(443,33776523),(445,40074705),(446,69075468),
    (447,61324857),(448,75815487),(456,7823079),(457,11183535),
    (459,16432119),(461,19514583),(462,26685252),(464,56148048),
    (468,63998748),(469,1014651),(470,1013265),(472,78557391),
    (476,33699006),(478,41505156),(479,9124434),(480,22993740),
    (481,15963651),(482,27967797),(483,33318648),(484,4224726),
    (486,28862163),(487,21316878),(488,17396973),(490,10618245),
    (491,22857813),(492,17896824),(493,8435592),(495,17041662),
    (496,23337270),(497,1074150),(503,2908323),(504,15163830),
    (505,18845145),(506,39593664),(507,31393494),(508,4406193),
    (509,23938695),(510,48625236),(511,33159258),(512,733491),
    (513,16559334),(514,50218146),(515,14429844),(517,99821007),
    (518,3970098),(519,9839016),(521,118880784),(548,33014718),
    (549,19105614),(550,18659520),(552,2630925),(553,25637931),
    (554,34201629),(557,51314571),(558,14054436),(559,23860782),
    (562,40621482),(563,18679518),(564,18340839),(567,39967290),
    (568,24203718),(570,3651615),(571,6928515),(572,33602085),
    (573,14788026),(574,21825045),(576,26325585),(577,71075466),
    (578,77996655),(580,29359737),(581,38376261),(583,43451892),
    (584,16144128),(585,17954937),(586,33007887),(587,36983331),
    (589,24246486),(590,58018752),(592,19934937),(593,80578476),
    (594,40020354),(596,27219159),(598,123109965),(599,28610505),
    (600,81397602),
)


def ftext(value: F | int) -> str:
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def _haar_sign(x: int, origin: int, width: int) -> int:
    displacement = x - origin
    if 0 <= displacement < width:
        return 1
    if width <= displacement < 2 * width:
        return -1
    return 0


@lru_cache(maxsize=1)
def _geometry() -> tuple[
    tuple[int, ...], tuple[tuple[int, int], ...], tuple[tuple[int, ...], ...]
]:
    events = tuple(
        sorted(
            {
                origin + shift
                for _, width, origin in CHANNELS
                for shift in (0, width, 2 * width)
            }
        )
    )
    cells = tuple(zip(events, events[1:]))
    q_states = tuple(
        tuple((800 // width) * _haar_sign(left, origin, width) for _, width, origin in CHANNELS)
        for left, _ in cells
    )
    if (len(CHANNELS), len(events), len(cells)) != (52, 77, 76):
        raise CertificateError("52/77/76 fixture census changed")
    return events, cells, q_states


def _owner_full_indices(owner: tuple[int, int]) -> tuple[int, ...]:
    n, width = owner
    ranks = range(3, 8) if n == 4 else range(7, 16)
    return tuple(CHANNELS.index((rank, width, POINTS[rank])) for rank in ranks)


def _owner_group_indices(owner: tuple[int, int]) -> tuple[int, ...]:
    n, width = owner
    # The shared a_7 coordinate is assigned once, to the earlier n=4 owner.
    ranks = range(3, 8) if n == 4 else range(8, 16)
    return tuple(CHANNELS.index((rank, width, POINTS[rank])) for rank in ranks)


@lru_cache(maxsize=1)
def _demand_rows() -> tuple[F, ...]:
    _, _, q_states = _geometry()
    rows: list[F] = []
    for owner in OWNER_ORDER:
        n, width = owner
        matrix = membership.point_m_matrix(n)
        indices = _owner_full_indices(owner)
        for q in q_states:
            h = tuple(F(q[index], 1600) for index in indices)
            rows.append(F(2 * width) * membership.quadratic(matrix, h))
    if len(rows) != 608:
        raise CertificateError("owner-row census changed")
    return tuple(rows)


def _row_key(row_index: int) -> tuple[tuple[int, int], tuple[int, int]]:
    _, cells, _ = _geometry()
    return OWNER_ORDER[row_index // len(cells)], cells[row_index % len(cells)]


def _row_index(key: tuple[tuple[int, int], tuple[int, int]]) -> int:
    _, cells, _ = _geometry()
    owner, cell = key
    return OWNER_ORDER.index(owner) * len(cells) + cells.index(cell)


def _root_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(combinations(range(len(CHANNELS)), 2))


def _root_price(pair: tuple[int, int]) -> F:
    _, cells, q_states = _geometry()
    i, j = pair
    return sum(
        (F(right - left, 1600 * 1600) * (q[i] - q[j]) ** 2 for q, (left, right) in zip(q_states, cells)),
        F(0),
    )


def _owner_root_share(row_index: int, pair: tuple[int, int], *, q_scale: bool = False) -> F:
    _, cells, q_states = _geometry()
    owner = OWNER_ORDER[row_index // len(cells)]
    q = q_states[row_index % len(cells)]
    group = set(_owner_group_indices(owner))
    i, j = pair
    delta = q[i] - q[j]
    value = F(0)
    if i in group:
        value += q[i] * delta
    if j in group:
        value += q[j] * (-delta)
    return value if q_scale else value / (1600 * 1600)


def _semantic_pair_indices(
    pair: tuple[tuple[int, int], tuple[int, int]]
) -> tuple[int, int]:
    indices = tuple(
        CHANNELS.index((rank, width, POINTS[rank])) for rank, width in pair
    )
    return tuple(sorted(indices))  # type: ignore[return-value]


def _pair_label(pair: tuple[int, int]) -> str:
    i, j = pair
    left = CHANNELS[i]
    right = CHANNELS[j]
    return f"T{left[1]}:a{left[0]}|T{right[1]}:a{right[0]}"


def _is_cross_epoch(pair: tuple[int, int]) -> bool:
    left_rank = CHANNELS[pair[0]][0]
    right_rank = CHANNELS[pair[1]][0]
    return (left_rank <= 7 < right_rank) or (right_rank <= 7 < left_rank)


def _alpha_global(n: int, left_gap: int, right_gap: int) -> F:
    if n <= left_gap <= right_gap - 2 and n + 2 <= right_gap <= 2 * n - 1:
        return F((right_gap - left_gap) ** 2, 4 * n * n)
    return F(0)


def _gothic_lambda(n: int, point_left: int, point_right: int) -> F:
    return (
        _alpha_global(n, point_left, point_right)
        + _alpha_global(n, point_left - 1, point_right + 1)
        - _alpha_global(n, point_left, point_right + 1)
        - _alpha_global(n, point_left - 1, point_right)
    )


def _dual_audit(
    witness: Mapping[tuple[tuple[int, int], tuple[int, int]], F],
    *,
    allow_cross_epoch: bool,
) -> tuple[F, F]:
    demands = _demand_rows()
    indexed = {_row_index(key): F(value) for key, value in witness.items()}
    if any(value < 0 for value in indexed.values()):
        raise CertificateError("negative graph dual weight")
    objective = sum((demands[row] * value for row, value in indexed.items()), F(0))
    margins: list[F] = []
    for pair in _root_pairs():
        if not allow_cross_epoch and _is_cross_epoch(pair):
            continue
        load = sum(
            (_owner_root_share(row, pair) * value for row, value in indexed.items()),
            F(0),
        )
        margin = _root_price(pair) - load
        if margin < 0:
            raise CertificateError(f"graph dual violation at {_pair_label(pair)}")
        margins.append(margin)
    return objective, min(margins)


def _graph_root_audit() -> dict[str, object]:
    _, cells, q_states = _geometry()
    pairs = _root_pairs()
    primal = {_semantic_pair_indices(pair): weight for pair, weight in GRAPH_PRIMAL.items()}
    demands = _demand_rows()
    slacks = []
    for row, demand in enumerate(demands):
        correction = sum(
            (weight * _owner_root_share(row, pair) for pair, weight in primal.items()),
            F(0),
        )
        slack = correction - demand
        if slack < 0:
            raise CertificateError(f"graph primal violation at {_row_key(row)}")
        slacks.append(slack)
    objective = sum((weight * _root_price(pair) for pair, weight in primal.items()), F(0))
    if objective != F(99062067, 179732480):
        raise CertificateError("graph feasible price changed")

    no_cross_bound, no_cross_margin = _dual_audit(
        NO_CROSS_DUAL, allow_cross_epoch=False
    )
    full_bound, full_margin = _dual_audit(FULL_GRAPH_DUAL, allow_cross_epoch=True)
    if no_cross_bound != F(611554977, 1024000000):
        raise CertificateError("no-cross dual objective changed")
    if full_bound != F(55874798199, 102400000000):
        raise CertificateError("full graph dual objective changed")
    if full_margin != F(69, 25600000):
        raise CertificateError("full graph minimum dual margin changed")

    identity_checks = 0
    groups = tuple(set(_owner_group_indices(owner)) for owner in OWNER_ORDER)
    flattened = sorted(index for group in groups for index in group)
    if flattened != list(range(52)):
        raise CertificateError("coordinate-owner groups do not partition the channels")
    for pair in pairs:
        i, j = pair
        for cell_index, q in enumerate(q_states):
            total = sum(
                _owner_root_share(owner_index * len(cells) + cell_index, pair, q_scale=True)
                for owner_index in range(len(OWNER_ORDER))
            )
            if total != (q[i] - q[j]) ** 2:
                raise CertificateError("owner shares do not recover the physical root")
            identity_checks += 1

    direct_rows = 0
    for n in (4, 8):
        matrix = membership.point_m_matrix(n)
        for p in range(n, 2 * n):
            for q in range(p, 2 * n):
                if 2 * matrix[p - n][q - n + 1] != _gothic_lambda(n, p, q):
                    raise CertificateError("direct-M/Gothic 2M=lambda identity failed")
                direct_rows += 1
    if direct_rows != 46:
        raise CertificateError("direct-M/Gothic row census changed")
    twice_demand = F(2069, 5120)
    conditional_margin = full_bound - twice_demand
    cross_gap = no_cross_bound - objective
    if cross_gap != F(51737891019, 1123328000000):
        raise CertificateError("cross-epoch essentiality gap changed")
    return {
        "variable_cone": "nonnegative physical graph roots with canonical signed coordinate-row shares",
        "feasible_primal": {
            "positive_root_count": len(primal),
            "physical_price": ftext(objective),
            "minimum_owner_row_slack": ftext(min(slacks)),
            "cross_epoch_positive_root_count": sum(_is_cross_epoch(pair) for pair in primal),
            "root_weights": {_pair_label(pair): ftext(weight) for pair, weight in sorted(primal.items())},
        },
        "no_cross_epoch_dual": {
            "support_count": len(NO_CROSS_DUAL),
            "lower_bound": ftext(no_cross_bound),
            "minimum_allowed_root_margin": ftext(no_cross_margin),
        },
        "cross_epoch_essentiality_gap": ftext(cross_gap),
        "full_dual": {
            "support_count": len(FULL_GRAPH_DUAL),
            "lower_bound": ftext(full_bound),
            "minimum_root_margin": ftext(full_margin),
        },
        "twice_integrated_demand": ftext(twice_demand),
        "conditional_Phi_strict_negative_margin": ftext(conditional_margin),
        "conditional_identity": "if Goff_owned+terminal_owned=D and terminal_owned>=0, then Phi=2*Goff_owned-P<=2D-P",
        "pointwise_owner_root_identities_checked": identity_checks,
        "direct_M_Gothic_lambda_equals_2M_rows_checked": direct_rows,
    }


def _physical_gram_q() -> list[list[F]]:
    _, cells, q_states = _geometry()
    return [
        [
            sum(
                (F(right - left) * q[i] * q[j] for q, (left, right) in zip(q_states, cells)),
                F(0),
            )
            for j in range(52)
        ]
        for i in range(52)
    ]


def _psd_row_matrix_entry(row: int, i: int, j: int) -> F:
    _, cells, q_states = _geometry()
    owner = OWNER_ORDER[row // len(cells)]
    q = q_states[row % len(cells)]
    group = set(_owner_group_indices(owner))
    return F(q[i] * q[j] * (int(i in group) + int(j in group)), 2)


def _strict_ldl_pivots(matrix: Sequence[Sequence[F]]) -> tuple[F, ...]:
    """Return exact positive unpivoted LDL pivots, or reject the matrix."""
    size = len(matrix)
    lower = [[F(0) for _ in range(size)] for _ in range(size)]
    diagonal: list[F] = []
    for i in range(size):
        for j in range(i):
            residual = F(matrix[i][j]) - sum(
                (lower[i][k] * diagonal[k] * lower[j][k] for k in range(j)),
                F(0),
            )
            if diagonal[j] == 0:
                if residual != 0:
                    raise CertificateError("zero LDL pivot has a nonzero residual")
                lower[i][j] = F(0)
            else:
                lower[i][j] = residual / diagonal[j]
        pivot = F(matrix[i][i]) - sum(
            (lower[i][k] * lower[i][k] * diagonal[k] for k in range(i)),
            F(0),
        )
        if pivot <= 0:
            raise CertificateError(f"projected PSD-dual slack is not positive definite at pivot {i}")
        diagonal.append(pivot)
        lower[i][i] = F(1)
    return tuple(diagonal)


def _zero_row_sum_psd_dual_audit(maximum_goff: F) -> dict[str, object]:
    demands = _demand_rows()
    dual = {row: F(numerator, PSD_DUAL_DENOMINATOR) for row, numerator in PSD_DUAL_NUMERATORS}
    if len(dual) != 227 or any(value <= 0 for value in dual.values()):
        raise CertificateError("PSD dual support changed")
    objective = sum((demands[row] * value for row, value in dual.items()), F(0))
    if objective != F(64678786029, 204800000000):
        raise CertificateError("PSD dual objective changed")

    slack = _physical_gram_q()
    _, cells, q_states = _geometry()
    groups = {owner: set(_owner_group_indices(owner)) for owner in OWNER_ORDER}
    for row, weight in dual.items():
        owner = OWNER_ORDER[row // len(cells)]
        group = groups[owner]
        q = q_states[row % len(cells)]
        active = tuple(index for index, value in enumerate(q) if value)
        for i in active:
            for j in active:
                coefficient = F(
                    q[i] * q[j] * (int(i in group) + int(j in group)), 2
                )
                slack[i][j] -= weight * coefficient

    # E=[e_0-e_51,...,e_50-e_51] spans 1^perp.  Positivity of
    # E^T S E is exactly the dual condition relevant to X 1=0.
    last = 51
    projected = [
        [
            slack[i][j] - slack[i][last] - slack[last][j] + slack[last][last]
            for j in range(last)
        ]
        for i in range(last)
    ]
    pivots = _strict_ldl_pivots(projected)
    twice_maximum_goff = 2 * maximum_goff
    gap = objective - twice_maximum_goff
    if gap != F(89607170277983, 1807769600000000) or gap <= 0:
        raise CertificateError("PSD Phi no-go gap changed")
    return {
        "dual_convention": "y>=0 and E^T(G-sum_r y_r B_r)E positive definite, E=[e_i-e_51]",
        "support_count": len(dual),
        "weight_common_denominator": PSD_DUAL_DENOMINATOR,
        "dual_row_numerators": {str(row): numerator for row, numerator in PSD_DUAL_NUMERATORS},
        "lower_bound": ftext(objective),
        "projected_dimension": len(projected),
        "strictly_positive_LDL_pivot_count": len(pivots),
        "projected_slack_positive_definite_exactly": True,
        "twice_maximum_Goff": ftext(twice_maximum_goff),
        "gap_above_twice_maximum_Goff": ftext(gap),
        "fixed_cone_Phi_upper_bound": ftext(-gap),
    }


def _psd_witness_audit() -> dict[str, object]:
    if len(PSD_FACTOR_COLUMNS) != 13 or any(len(column) != 52 for column in PSD_FACTOR_COLUMNS):
        raise CertificateError("PSD factor shape changed")
    if any(sum(column) != 0 for column in PSD_FACTOR_COLUMNS):
        raise CertificateError("PSD factor lost exact zero column sums")
    factor = tuple(
        tuple(F(value, PSD_FACTOR_DENOMINATOR) for value in column)
        for column in PSD_FACTOR_COLUMNS
    )
    _, cells, q_states = _geometry()
    demands = _demand_rows()
    groups = {owner: _owner_group_indices(owner) for owner in OWNER_ORDER}

    slacks: list[F] = []
    owner_values: list[F] = []
    for row, demand in enumerate(demands):
        owner = OWNER_ORDER[row // len(cells)]
        q = q_states[row % len(cells)]
        value = sum(
            (
                sum((q[index] * column[index] for index in groups[owner]), F(0))
                * sum((q[index] * column[index] for index in range(52)), F(0))
                for column in factor
            ),
            F(0),
        )
        slack = value - demand
        if slack < 0:
            raise CertificateError(f"rational PSD witness violates owner row {_row_key(row)}")
        owner_values.append(value)
        slacks.append(slack)

    for cell_index, q in enumerate(q_states):
        total_owned = sum(
            owner_values[owner_index * len(cells) + cell_index]
            for owner_index in range(len(OWNER_ORDER))
        )
        physical = sum(
            (sum((q[index] * column[index] for index in range(52)), F(0)) ** 2 for column in factor),
            F(0),
        )
        if total_owned != physical:
            raise CertificateError("PSD coordinate-owner shares do not sum to physical energy")

    price = sum(
        (
            F(right - left)
            * sum(
                (sum((q[index] * column[index] for index in range(52)), F(0)) ** 2 for column in factor),
                F(0),
            )
            for q, (left, right) in zip(q_states, cells)
        ),
        F(0),
    )
    if price != F(19511959, 50000000):
        raise CertificateError("rational PSD witness price changed")
    twice_demand = F(2069, 5120)
    margin = twice_demand - price
    if margin != F(5544953, 400000000):
        raise CertificateError("PSD witness margin below twice demand changed")

    past = tuple(index for index, (rank, _, _) in enumerate(CHANNELS) if rank <= 7)
    current = tuple(index for index, (rank, _, _) in enumerate(CHANNELS) if rank >= 8)
    cross_entries = {
        (i, j): sum((column[i] * column[j] for column in factor), F(0))
        for i in past
        for j in current
    }
    nonzero_cross = {pair: value for pair, value in cross_entries.items() if value}
    if not nonzero_cross:
        raise CertificateError("PSD witness unexpectedly has zero cross-epoch block")
    example_pair, example_value = next(iter(nonzero_cross.items()))
    return {
        "coordinate_scaling": "q=1600*h=(800/T)*g and X=B*B^T",
        "factor_shape": [52, 13],
        "factor_common_denominator": PSD_FACTOR_DENOMINATOR,
        "factor_integer_columns": [list(column) for column in PSD_FACTOR_COLUMNS],
        "zero_row_sum_exact": True,
        "PSD_by_rational_Gram_factor": True,
        "owner_rows_checked": len(demands),
        "all_owner_rows_feasible_exactly": True,
        "tight_owner_row_count": sum(slack == 0 for slack in slacks),
        "minimum_owner_row_slack": ftext(min(slacks)),
        "physical_price": ftext(price),
        "below_twice_demand_margin": ftext(margin),
        "cross_epoch_block_nonzero": True,
        "nonzero_cross_epoch_matrix_entry_count": len(nonzero_cross),
        "cross_epoch_example": {
            "left": _pair_label(tuple(sorted(example_pair))).split("|")[0],
            "right": _pair_label(tuple(sorted(example_pair))).split("|")[1],
            "entry": ftext(example_value),
        },
        "cross_epoch_essential_in_PSD_cone_proved": False,
    }


def _overlap(width: int, distance: int) -> F:
    return F(width - distance, width * width) if distance < width else F(0)


def _beta(n: int, p: int, q: int) -> F:
    separation = q - p
    if separation == 0:
        return F(1, n * n)
    if separation == 1:
        return F(1, 4 * n * n)
    return F(1, 2 * n * n)


def _positive_pair_owners(n: int) -> tuple[tuple[int, int, int, F], ...]:
    return tuple(
        (p, q, POINTS[q] - POINTS[p - 1], _beta(n, p, q))
        for p in range(n + 1, 2 * n - 1)
        for q in range(p, 2 * n - 1)
    )


def _tent(n: int, i: int, j: int, width: int) -> F:
    middle = POINTS[j - 1] - POINTS[i]
    left_gap = POINTS[i] - POINTS[i - 1]
    right_gap = POINTS[j] - POINTS[j - 1]
    return (
        _overlap(width, middle)
        + _overlap(width, middle + left_gap + right_gap)
        - _overlap(width, middle + left_gap)
        - _overlap(width, middle + right_gap)
    )


def _wave_density(n: int, width: int) -> F:
    return sum(
        (
            F((j - i) ** 2, 4 * n * n) * _tent(n, i, j, width)
            for j in range(n + 2, 2 * n)
            for i in range(n, j - 1)
        ),
        F(0),
    )


def _positive_density(n: int, width: int) -> F:
    return sum(
        (coefficient * _overlap(width, distance) for _, _, distance, coefficient in _positive_pair_owners(n)),
        F(0),
    )


def _minimum_terminal_piece(n: int, width: int) -> F:
    """Exact one-row bounded fractional-knapsack optimum and dual replay."""
    demand = F(width) * _wave_density(n, width)
    if demand == 0:
        return F(0)
    choices = []
    for p, q, distance, coefficient in _positive_pair_owners(n):
        value = 2 * _overlap(width, distance)
        terminal_value = 2 * _overlap(1600, distance)
        capacity = F(width) * coefficient / 2
        if value:
            choices.append((terminal_value / value, p, q, value, terminal_value, capacity))
    remaining = demand
    cost = F(0)
    allocations: list[tuple[F, F, F, F]] = []
    marginal_ratio: F | None = None
    for ratio, _, _, value, terminal_value, capacity in sorted(choices):
        amount = min(capacity, remaining / value)
        if amount:
            allocations.append((ratio, value, terminal_value, amount))
            remaining -= amount * value
            cost += amount * terminal_value
            marginal_ratio = ratio
        if remaining == 0:
            break
    if remaining != 0 or marginal_ratio is None:
        raise CertificateError("pair-allocation row is infeasible")
    theta = marginal_ratio
    dual_lower = theta * demand + sum(
        (
            (terminal_value - theta * value) * capacity
            for ratio, _, _, value, terminal_value, capacity in choices
            if ratio < theta
        ),
        F(0),
    )
    if dual_lower != cost:
        raise CertificateError("fractional-knapsack terminal primal/dual gap")
    return cost


def _pair_owner_ledger_audit(psd_price: F) -> tuple[dict[str, object], F]:
    _, cells, _ = _geometry()
    demands = _demand_rows()
    integrated_by_owner: dict[tuple[int, int], F] = {}
    for owner_index, owner in enumerate(OWNER_ORDER):
        offset = owner_index * len(cells)
        integrated_by_owner[owner] = sum(
            (
                F(right - left) * demands[offset + cell_index]
                for cell_index, (left, right) in enumerate(cells)
            ),
            F(0),
        )
    integrated_demand = sum(integrated_by_owner.values(), F(0))
    if integrated_demand != F(2069, 10240):
        raise CertificateError("integrated signed demand changed")

    proportional_rows: dict[tuple[int, int], dict[str, F]] = {}
    total_goff = F(0)
    total_terminal = F(0)
    for n in (4, 8):
        owners = _positive_pair_owners(n)
        cumulative = {owner: F(0) for owner in owners}
        for width in WIDTHS:
            q_value = _wave_density(n, width)
            p_value = _positive_density(n, width)
            ratio = q_value / p_value if p_value else F(0)
            for owner in owners:
                _, _, distance, coefficient = owner
                value = 2 * _overlap(width, distance)
                allocation = F(width) * coefficient * ratio / 2 if value else F(0)
                cumulative[owner] += allocation
            goff = sum(
                (
                    cumulative[owner]
                    * (2 * _overlap(width, owner[2]) - 2 * _overlap(2 * width, owner[2]))
                    for owner in owners
                ),
                F(0),
            )
            proportional_rows[(n, width)] = {
                "direct_M_integrated_demand": integrated_by_owner[(n, width)],
                "Goff": goff,
                "terminal": F(0),
            }
            total_goff += goff
        terminal = sum(
            (cumulative[owner] * 2 * _overlap(1600, owner[2]) for owner in owners),
            F(0),
        )
        proportional_rows[(n, 800)]["terminal"] = terminal
        total_terminal += terminal
    if total_goff != F(1553495291871, 12502746112000):
        raise CertificateError("proportional Goff changed")
    if total_terminal != F(972694327829, 12502746112000):
        raise CertificateError("proportional terminal changed")
    if total_goff + total_terminal != integrated_demand:
        raise CertificateError("proportional Goff/terminal identity failed")
    proportional_phi = 2 * total_goff - psd_price
    if proportional_phi != -F(2768860635551669, 19535540800000000):
        raise CertificateError("proportional PSD Phi changed")

    minimum_terminal = sum(
        (_minimum_terminal_piece(n, width) for n in (4, 8) for width in WIDTHS),
        F(0),
    )
    maximum_goff = integrated_demand - minimum_terminal
    if minimum_terminal != F(124605023, 1807769600):
        raise CertificateError("minimum finite pair terminal changed")
    if maximum_goff != F(240656237, 1807769600):
        raise CertificateError("maximum finite Goff changed")
    maximum_phi_at_witness = 2 * maximum_goff - psd_price
    if maximum_phi_at_witness != -F(1751172283851, 14123200000000):
        raise CertificateError("optimized pair-allocation Phi changed")
    return (
        {
            "one_for_one_coefficient_rule": "lambda_(p,q)=2*M_(p-n,q-n+1); existing Gothic rows are rewritten, never duplicated",
            "birth_and_prebirth_rule": "each strict positive pair has its unique birth epoch and its prebirth state is zero",
            "finite_scale_rule": "sum_r a_(gamma,r)v_(gamma,r)=sum_r s_(gamma,r)(v_(gamma,r)-v_(gamma,r+1))+s_(gamma,U)v_(gamma,U+1)",
            "integrated_owner_rows": {
                f"n{n}_T{width}": {
                    key: ftext(value) for key, value in proportional_rows[(n, width)].items()
                }
                for width in WIDTHS
                for n in (4, 8)
            },
            "proportional": {
                "Goff": ftext(total_goff),
                "terminal": ftext(total_terminal),
                "Goff_plus_terminal": ftext(total_goff + total_terminal),
                "Phi_at_PSD_witness_price": ftext(proportional_phi),
            },
            "optimal_finite_pair_allocation": {
                "optimization": "minimize the upper T=1600 terminal independently in each (n,T) row under 0<=a<=T*beta/2 and sum_gamma a*v=T*Q",
                "exact_fractional_knapsack_primal_dual_rows": 8,
                "minimum_terminal": ftext(minimum_terminal),
                "maximum_Goff": ftext(maximum_goff),
                "maximum_Phi_at_PSD_witness_price": ftext(maximum_phi_at_witness),
            },
        },
        maximum_goff,
    )


def _build_uncached() -> dict[str, object]:
    graph = _graph_root_audit()
    psd_witness = _psd_witness_audit()
    psd_price = F(psd_witness["physical_price"])
    pair_ledger, maximum_goff = _pair_owner_ledger_audit(psd_price)
    psd_dual = _zero_row_sum_psd_dual_audit(maximum_goff)
    _, cells, _ = _geometry()
    integrated_by_owner = {
        key: value["direct_M_integrated_demand"]
        for key, value in pair_ledger["integrated_owner_rows"].items()  # type: ignore[union-attr]
    }
    certificate: dict[str, object] = {
        "schema": SCHEMA,
        "status": STATUS,
        "scope": {
            "fixed_fixture_graph_root_theorem": True,
            "one_exact_rational_PSD_feasible_witness": True,
            "all_zero_row_sum_PSD_corrections_in_fixed_coordinate_owner_model_closed": True,
            "zero_row_sum_PSD_coordinate_owner_cone_no_go": True,
            "C067_finite_pair_allocation_convention_frozen": True,
            "exact_graph_root_optimum_known": False,
            "exact_PSD_optimum_known": False,
            "directed_current_to_past_source_map_constructed": False,
            "cross_epoch_essential_in_PSD_cone_proved": False,
            "arbitrary_PSD_under_other_ownership_or_channel_models": False,
            "indefinite_blocks": False,
            "indefinite_or_other_owner_split_theorem": False,
            "other_pair_allocation_or_terminal_conventions": False,
            "birth_final_terminal_global_ledger_constructed": False,
            "C058_Q1_Q2_proved": False,
            "publication_novelty_or_prize_claimed": False,
        },
        "fixture": {
            "tower": "a_k=k(k+100), 0<=k<=15",
            "epochs": [4, 8],
            "widths": list(WIDTHS),
            "upper_terminal_width": 1600,
            "coordinate_order": [f"T{width}:a{rank}" for rank, width, _ in CHANNELS],
            "physical_coordinate_count": len(CHANNELS),
            "finite_event_count": len(cells) + 1,
            "positive_length_cell_count": len(cells),
            "owner_order": [f"n{n}_T{width}" for n, width in OWNER_ORDER],
            "owner_count": len(OWNER_ORDER),
            "owner_cell_row_count": len(OWNER_ORDER) * len(cells),
            "physical_root_count": len(_root_pairs()),
            "coordinate_groups_partition_all_coordinates": True,
            "shared_a7_endpoint_owned_once_by_past_epoch": True,
            "owner_integrated_signed_demands": integrated_by_owner,
            "integrated_signed_demand": "2069/10240",
            "pointwise_owner_root_identities_checked": graph["pointwise_owner_root_identities_checked"],
            "direct_M_Gothic_lambda_equals_2M_rows_checked": graph["direct_M_Gothic_lambda_equals_2M_rows_checked"],
        },
        "graph_root_master": graph,
        "psd_reopening_witness": psd_witness,
        "pair_owner_Abel_ledger": pair_ledger,
        "zero_row_sum_PSD_dual": psd_dual,
        "theorem_boundary": {
            "fixed_PSD_cone_conclusion": "for every X>=0 with X*1=0 satisfying all 608 canonical owner rows, P>=L_PSD>2*Goff_max, hence Phi=2*Goff-P<0 for every allowed finite C067 pair allocation",
            "directed_map_not_needed_for_no_go": "a legitimate directed source-to-root master would be a subset of this priced feasible cone, so the scalar upper bound closes positive Phi without constructing that map",
            "symmetric_cross_root_warning": "a nonzero symmetric cross block is not an oriented current-to-past payment or an injective primitive-row source map",
            "missing_for_C058": "other ownership rules, other channel models, indefinite cross blocks, and the global birth/final/terminal ledger remain outside the theorem",
        },
    }
    certificate["integrity"] = {
        "canonical_json": True,
        "payload_sha256": payload_hash(certificate),
    }
    return certificate


@lru_cache(maxsize=1)
def _cached_certificate_json() -> str:
    # Cache immutable text, never a mutable certificate object.
    return json.dumps(
        _build_uncached(), sort_keys=True, separators=(",", ":"), ensure_ascii=False
    )


def build_certificate() -> dict[str, object]:
    return json.loads(_cached_certificate_json())


def payload_hash(certificate: Mapping[str, object]) -> str:
    payload = {key: value for key, value in certificate.items() if key != "integrity"}
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def rendered_bytes(certificate: Mapping[str, object]) -> bytes:
    return (
        json.dumps(
            certificate, sort_keys=True, separators=(",", ":"), ensure_ascii=False
        )
        + "\n"
    ).encode("utf-8")


def _check_boolean_types(actual: object, expected: object, path: str = "root") -> None:
    if isinstance(expected, bool):
        if type(actual) is not bool:
            raise CertificateError(f"{path} must be a literal boolean")
        return
    if isinstance(expected, Mapping):
        if not isinstance(actual, Mapping):
            raise CertificateError(f"{path} must be an object")
        for key, value in expected.items():
            if key in actual:
                _check_boolean_types(actual[key], value, f"{path}.{key}")
    elif isinstance(expected, list) and isinstance(actual, list):
        for index, (left, right) in enumerate(zip(actual, expected)):
            _check_boolean_types(left, right, f"{path}[{index}]")


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
    _check_boolean_types(certificate, expected)
    if certificate != expected:
        raise CertificateError("certificate differs from exact semantic replay")


def _rehash(certificate: dict[str, object]) -> None:
    certificate["integrity"]["payload_sha256"] = payload_hash(certificate)  # type: ignore[index]


def self_check(certificate: Mapping[str, object]) -> dict[str, int]:
    verify_certificate(certificate)
    mutations: list[dict[str, object]] = []
    mutation_specs = (
        (("schema",), "wrong.schema"),
        (("status",), "C058_SOLVED"),
        (("scope", "C058_Q1_Q2_proved"), True),
        (("scope", "indefinite_blocks"), True),
        (("scope", "directed_current_to_past_source_map_constructed"), True),
        (("fixture", "physical_coordinate_count"), 51),
        (("fixture", "integrated_signed_demand"), "0/1"),
        (("graph_root_master", "feasible_primal", "physical_price"), "0/1"),
        (("graph_root_master", "full_dual", "lower_bound"), "0/1"),
        (("psd_reopening_witness", "physical_price"), "0/1"),
        (("pair_owner_Abel_ledger", "optimal_finite_pair_allocation", "maximum_Goff"), "0/1"),
        (("zero_row_sum_PSD_dual", "lower_bound"), "0/1"),
    )
    for path, value in mutation_specs:
        changed = copy.deepcopy(certificate)
        target: object = changed
        for key in path[:-1]:
            target = target[key]  # type: ignore[index]
        target[path[-1]] = value  # type: ignore[index]
        _rehash(changed)
        mutations.append(changed)
    rejected = 0
    for changed in mutations:
        try:
            verify_certificate(changed)
        except CertificateError:
            rejected += 1
    if rejected != len(mutations):
        raise CertificateError("a rehashed semantic mutation was accepted")
    return {"mutations_attempted": len(mutations), "mutations_rejected": rejected}


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
            print(
                f"self_check mutations_attempted={result['mutations_attempted']} mutations_rejected={result['mutations_rejected']}",
                file=sys.stderr if machine_stdout else sys.stdout,
            )
    except (CertificateError, OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
