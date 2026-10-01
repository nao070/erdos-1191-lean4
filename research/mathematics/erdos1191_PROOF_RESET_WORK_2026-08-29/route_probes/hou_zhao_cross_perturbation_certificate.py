#!/usr/bin/env python3
"""Exact two-cycle cross perturbation of Hou--Zhao's eight-kernel input.

Default operation is deterministic and offline.  Only exact aggregate values
are embedded.  ``--upstream PATH`` pins and runs the external official script,
then rebuilds the covers, correlations, Phi, a, and b from its raw arrays.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
from fractions import Fraction as F

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE / "hou_zhao_cross_perturbation_certificate.json"
UPSTREAM_REPOSITORY = "https://github.com/HbZhao1/sidon-vector-smoothing"
UPSTREAM_COMMIT = "ef044564300e546f8832b31f5fba133fd192cc3a"
UPSTREAM_TREE = "600e317e727e6a8940cc5f13c072aa1c6b766784"
UPSTREAM_PATH = "sidon_certificate_8kernel.py"
UPSTREAM_SHA256 = "957a5afadd849ac4f97c2b71252abb5c796c2db3c91a608ab35097e3c49292a8"

M, L, N = 32, 4, 128
EPSILON = F(1, 6250)
J_EDGES = ((1, 2, -1), (1, 4, 2), (1, 7, -1), (2, 8, 1),
           (4, 5, -1), (4, 8, -1), (5, 7, 1))
LAMBDAS = (
    F(19745437, 50000000), F(539057, 6250000), F(67671, 50000000),
    F(645593, 5000000), F(10225781, 50000000), F(2832639, 100000000),
    F(4608571, 50000000), F(6335669, 100000000),
)
OFFICIAL_A = F(497329054138522113993707809619, 390625000000000000000000000000)
OFFICIAL_B = F(69918675237166718360455326217, 100000000000000000000000000000)
OFFICIAL_PRODUCT = F(34772588622318632383981521978715331189177469643597175481323,
                     39062500000000000000000000000000000000000000000000000000000)
LEAST_SLACK = F(4735171805469436153, 6250000000000000000000000000000)
OLD_SINGLE_CYCLE_PRODUCT = F(
    2048931240613272557952824967850053635684604249584937576474589383402375105273559739421917,
    2301708946605776562881869357031250000000000000000000000000000000000000000000000000000000)

CORRELATIONS = (
 F(497337598850312567313325417619,12500000000000000000000000000000),
 F(3817346178837648246387910251603,100000000000000000000000000000000),
 F(453675975694853025661453959667,12500000000000000000000000000000),
 F(861534090104320932435764829233,25000000000000000000000000000000),
 F(817232696185429644390060648637,25000000000000000000000000000000),
 F(38739611726898448559008462543,1250000000000000000000000000000),
 F(73131593749804943953806263579,2500000000000000000000000000000),
 F(2751850301214136667750964688799,100000000000000000000000000000000),
 F(644676302211714924868143485861,25000000000000000000000000000000),
 F(2414405530024057195966578320159,100000000000000000000000000000000),
 F(225124529414981396794568486293,10000000000000000000000000000000),
 F(1045467015255224570927419063373,50000000000000000000000000000000),
 F(964872444182111642571223944323,50000000000000000000000000000000),
 F(888244042330476016750263897801,50000000000000000000000000000000),
 F(406960782096663533359254887549,25000000000000000000000000000000),
 F(1511986853773004621317976734677,100000000000000000000000000000000),
 F(672244942816088885939795971099,50000000000000000000000000000000),
 F(599834316957503668554753455831,50000000000000000000000000000000),
 F(21564113113362299565729672263,2000000000000000000000000000000),
 F(957573852185398727325788034771,100000000000000000000000000000000),
 F(83795139838751427500028619713,10000000000000000000000000000000),
 F(181172304933655800164448310929,25000000000000000000000000000000),
 F(77443768250174396505529842179,12500000000000000000000000000000),
 F(16391313392531276583409146001,3125000000000000000000000000000),
 F(43443572321756909803090686357,10000000000000000000000000000000),
 F(87478041162758012882171994173,25000000000000000000000000000000),
 F(34197589901491257651194136399,12500000000000000000000000000000),
 F(103413997099146588488389214161,50000000000000000000000000000000),
 F(37092753302555411114826253521,25000000000000000000000000000000),
 F(99371469720234567283073913743,100000000000000000000000000000000),
 F(15731050807383775708620452627,25000000000000000000000000000000),
 F(1819897465312660450421661319,6250000000000000000000000000000),
)
EXPECTED_PHI = F(
 1579624060150375763081182134406091935613108916851453560453448655773351,
 12822999091195800386592256049305804181893750000000000000000000000000)
EXPECTED_A = F(497337598850312567313325417619,390625000000000000000000000000)
EXPECTED_B = F(
 143448161936446119782849456883841867241008916851453560453448655773351,
 205167985459132806185476096788892866910300000000000000000000000000000)
EXPECTED_PRODUCT = F(
 71342164416962916721779776697373603740587064431196223748760854144493362660496722080976377486071269,
 80143744319973752416201600308161276136835937500000000000000000000000000000000000000000000000000000)

def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)

def fs(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"

def canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()

def decimal_sqrt(x: F, digits: int = 52) -> str:
    from decimal import Decimal, localcontext
    with localcontext() as ctx:
        ctx.prec = digits
        return str((Decimal(x.numerator) / Decimal(x.denominator)).sqrt())

def matrices(epsilon: F = EPSILON) -> tuple[list[list[F]], list[list[F]], list[list[F]]]:
    d = [[LAMBDAS[r] if r == s else F(0) for s in range(8)] for r in range(8)]
    j = [[F(0) for _ in range(8)] for _ in range(8)]
    for r, s, value in J_EDGES:
        j[r-1][s-1] = j[s-1][r-1] = F(value)
    h = [[d[r][s] + epsilon*j[r][s] for s in range(8)] for r in range(8)]
    return d, j, h

def inverse(matrix: list[list[F]]) -> list[list[F]]:
    n = len(matrix)
    aug = [row[:] + [F(i == j) for j in range(n)] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col]), None)
        require(pivot is not None, "singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x/scale for x in aug[col]]
        for row in range(n):
            if row != col and aug[row][col]:
                scale = aug[row][col]
                aug[row] = [x-scale*y for x, y in zip(aug[row], aug[col])]
    return [row[n:] for row in aug]

def core_values(epsilon: F = EPSILON, correlations: tuple[F, ...] = CORRELATIONS) -> dict[str, object]:
    d, j, h = matrices(epsilon)
    row_sums = [sum(row) for row in j]
    abs_rows = [sum(abs(x) for c, x in enumerate(row) if c != r) for r, row in enumerate(j)]
    margins = [LAMBDAS[r]-epsilon*abs_rows[r] for r in range(8)]
    minimum = min((x, shift) for shift, x in enumerate(correlations))
    a = M*correlations[0]
    b = 1+(EXPECTED_PHI-N)/16
    hi = inverse(h)
    s_value = sum(sum(row) for row in h)
    beta = sum(LAMBDAS[r]*hi[r][t]*LAMBDAS[t] for r in range(8) for t in range(8))
    return {"D": d, "J": j, "H": h, "row_sums": row_sums, "abs_rows": abs_rows,
            "margins": margins, "minimum": minimum, "a": a, "b": b, "product": a*b,
            "s": s_value, "beta": beta}

def build_payload() -> dict[str, object]:
    v = core_values()
    require(sum(LAMBDAS) == 1 and all(x > 0 for x in LAMBDAS), "invalid lambdas")
    require(v["row_sums"] == [0]*8, "J does not annihilate the all-ones vector")
    require(v["s"] == 1 and v["beta"] == 1, "normalization s/beta mismatch")
    require(all(x > 0 for x in v["margins"]), "H is not positive definite by strict diagonal dominance")
    require(min(v["margins"]) == F(67671,50000000), "wrong overall Gershgorin bound")
    require(min(v["margins"][r] for r in (0,1,3,4,6,7)) == F(6303669,100000000),
            "wrong affected-row margin")
    require(len(CORRELATIONS) == 32 and all(x > 0 for x in CORRELATIONS), "negative correlation")
    require(v["minimum"] == (F(1819897465312660450421661319,6250000000000000000000000000000),31),
            "wrong minimum correlation")
    require(v["a"] == EXPECTED_A and v["b"] == EXPECTED_B and v["product"] == EXPECTED_PRODUCT,
            "objective mismatch")
    official_gain = OFFICIAL_PRODUCT-EXPECTED_PRODUCT
    old_gain = OLD_SINGLE_CYCLE_PRODUCT-EXPECTED_PRODUCT
    require(official_gain > 0 and old_gain > 0, "strict improvement missing")
    require(EXPECTED_PRODUCT < F(9435,10000)**2, "source coefficient comparison failed")
    clean_bound = F(94349223,100000000)
    require(EXPECTED_PRODUCT < clean_bound**2, "clean rational decimal bound failed")
    payload: dict[str, object] = {
      "schema": "erdos1191.hou_zhao_cross_perturbation.v2",
      "status": "exact finite-certificate refinement; not a global, novelty, prize, or Erdős #1191 resolution claim",
      "source": {"repository": UPSTREAM_REPOSITORY, "commit": UPSTREAM_COMMIT, "tree": UPSTREAM_TREE,
        "path": UPSTREAM_PATH, "sha256": UPSTREAM_SHA256,
        "scope": "Hou--Zhao arXiv v2 Section 5 only suggests controlled cross terms; raw source is external and not bundled"},
      "fixed_input": {"m": M, "L": L, "n": N, "lambda": [fs(x) for x in LAMBDAS],
        "q_definition": "q[r,j]=lambda[r]*w[r,j], w[r,j]=W_INTS[r,j]/10^9+17/250000000000",
        "cover": {"unchanged_reason": "lambda, p, w, and q are unchanged", "minimum_shift": 128,
          "minimum_slack": "0", "least_positive_shift": 127, "least_positive_slack": fs(LEAST_SLACK)},
        "official_a": fs(OFFICIAL_A), "official_b": fs(OFFICIAL_B), "official_product": fs(OFFICIAL_PRODUCT),
        "official_coefficient_decimal": decimal_sqrt(OFFICIAL_PRODUCT)},
      "perturbation": {"epsilon": fs(EPSILON), "H": "diag(lambda)+epsilon*J",
        "J_edges_one_based": [list(x) for x in J_EDGES],
        "J_edges_zero_based": [[r-1,s-1,x] for r,s,x in J_EDGES],
        "cycle_decomposition": "(-12,+14,+28,-48)+(+14,-17,-45,+57), one-based",
        "row_sums": [fs(x) for x in v["row_sums"]], "s": fs(v["s"]), "beta": fs(v["beta"]),
        "pd": {"proof": "symmetric strict diagonal dominance with positive diagonal",
          "absolute_offdiag_row_sums": [fs(x) for x in v["abs_rows"]],
          "gershgorin_margins": [fs(x) for x in v["margins"]],
          "smallest_affected_margin": "6303669/100000000", "smallest_overall_margin": "67671/50000000"}},
      "correlations": {"definition": "D_d=sum_rs H_rs sum_i p_r[i]p_s[i+d], 0<=d<=31",
        "at_epsilon": [fs(x) for x in CORRELATIONS], "minimum_shift": v["minimum"][1],
        "minimum_value": fs(v["minimum"][0]),
        "block_lift": "d=q*h+t, 0<=t<h: C_H(d)=((h-t)D_q+tD_(q+1))/h^2, D_32=0"},
      "boundary_objective": {"aggregate": "Phi=sum_j q_j^T H^-1 q_j, exact value replayed from upstream",
        "Phi": fs(EXPECTED_PHI), "a": fs(EXPECTED_A), "b_formula": "b=1+(Phi-128)/16 since s=beta=1",
        "b": fs(EXPECTED_B), "product_a_times_b": fs(EXPECTED_PRODUCT),
        "coefficient_sqrt_product_decimal": decimal_sqrt(EXPECTED_PRODUCT),
        "clean_rational_coefficient_upper_bound": fs(clean_bound),
        "clean_bound_squared_minus_product": fs(clean_bound**2-EXPECTED_PRODUCT),
        "official_product_minus_product": fs(official_gain), "old_single_cycle_product_minus_product": fs(old_gain),
        "target_0.9435_squared_minus_product": fs(F(9435,10000)**2-EXPECTED_PRODUCT)},
      "search_scope": {"statement": "best bounded two-cycle combination in the stated finite search; not a global optimization claim",
        "enumeration": "all 210 alternating four-cycles, both orientations; sums/differences among the best 80 downhill cycles; gcd reduction",
        "primary": "clean two-cycle candidate", "secondary_regression": "earlier optimized single-cycle product retained only for exact comparison"},
      "claim_boundary": {"global_optimum": False, "novelty": False, "erdos_1191_resolution": False,
        "prize_claim": False, "allowed": "one exact finite F(N) coefficient refinement of the pinned eight-kernel input"}}
    payload["payload_sha256"] = hashlib.sha256(canonical_bytes(payload)).hexdigest()
    return payload

def validate_payload(payload: dict[str, object]) -> None:
    require(isinstance(payload, dict), "certificate is not an object")
    body = dict(payload); supplied = body.pop("payload_sha256", None)
    require(supplied == hashlib.sha256(canonical_bytes(body)).hexdigest(), "payload hash mismatch")
    require(payload == build_payload(), "certificate semantic mismatch")
    claims = payload["claim_boundary"]
    require(not any(claims[k] for k in ("global_optimum","novelty","erdos_1191_resolution","prize_claim")),
            "forbidden overclaim")

def self_check() -> int:
    """Run deterministic semantic mutations without importing the test suite."""
    payload = build_payload(); validate_payload(payload)
    mutations = (
      (("source","sha256"),"0"*64),
      (("perturbation","row_sums",0),"1"),
      (("perturbation","J_edges_one_based",0,2),1),
      (("perturbation","epsilon"),"1"),
      (("correlations","at_epsilon",31),"-1"),
      (("fixed_input","cover","minimum_slack"),"1"),
      (("perturbation","beta"),"2"),
      (("perturbation","s"),"2"),
      (("boundary_objective","product_a_times_b"),"0"),
      (("boundary_objective","official_product_minus_product"),"-1"),
      (("claim_boundary","global_optimum"),True),
      (("claim_boundary","novelty"),True),
      (("claim_boundary","erdos_1191_resolution"),True),
      (("claim_boundary","prize_claim"),True),
    )
    for path, replacement in mutations:
        value=json.loads(json.dumps(payload)); cursor=value
        for key in path[:-1]: cursor=cursor[key]
        cursor[path[-1]]=replacement
        value.pop("payload_sha256",None)
        value["payload_sha256"]=hashlib.sha256(canonical_bytes(value)).hexdigest()
        try: validate_payload(value)
        except ValueError: pass
        else: raise ValueError(f"mutation was not rejected: {path}")
    bad_hash=dict(payload); bad_hash["payload_sha256"]="f"*64
    try: validate_payload(bad_hash)
    except ValueError: pass
    else: raise ValueError("hash mutation was not rejected")
    return len(mutations)+1

def render_payload(payload: dict[str, object]) -> bytes:
    return (json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False)+"\n").encode()

def verify_upstream(path: Path) -> dict[str, str]:
    path = path.resolve(); require(path.is_file(), f"upstream file not found: {path}")
    require(path.name == UPSTREAM_PATH, "wrong upstream filename")
    require(sha256_file(path) == UPSTREAM_SHA256, "wrong upstream source hash")
    repo = path.parent
    commit = subprocess.run(["git","-C",str(repo),"rev-parse","HEAD"],check=True,capture_output=True,text=True).stdout.strip()
    tree = subprocess.run(["git","-C",str(repo),"rev-parse","HEAD^{tree}"],check=True,capture_output=True,text=True).stdout.strip()
    require(commit == UPSTREAM_COMMIT and tree == UPSTREAM_TREE, "wrong upstream provenance")
    tracked = subprocess.run(["git","-C",str(repo),"ls-files","--error-unmatch",UPSTREAM_PATH],
                             check=True,capture_output=True,text=True).stdout.strip()
    require(tracked == UPSTREAM_PATH, "upstream file is not pinned tracked path")
    env = dict(os.environ); env["PYTHONDONTWRITEBYTECODE"] = "1"
    run = subprocess.run([sys.executable,str(path)],cwd=repo,env=env,capture_output=True,text=True,check=True)
    require("Certified C < 0.9435" in run.stdout and f"SHA-256 = {UPSTREAM_SHA256}" in run.stdout,
            "official verifier did not pass")
    spec = importlib.util.spec_from_file_location("pinned_hz",path)
    require(spec is not None and spec.loader is not None, "cannot load upstream")
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(module)
    lambdas=tuple(module.lambdas); kernels=tuple(tuple(x) for x in module.kernels); weights=tuple(tuple(x) for x in module.weights)
    require(lambdas == LAMBDAS, "raw lambdas mismatch")
    require(len(kernels)==8 and all(len(x)==M for x in kernels), "kernel shape mismatch")
    require(len(weights)==8 and all(len(x)==N for x in weights), "boundary shape mismatch")
    slacks=[]
    for shift in range(N+1):
        total=sum(lam*p[i]*(w[shift+i] if shift+i<N else F(1))
                  for lam,p,w in zip(lambdas,kernels,weights) for i in range(M))
        slacks.append(total-1)
    require(all(x>=0 for x in slacks) and slacks[128]==0, "raw cover failure")
    least,least_shift=min((x,i) for i,x in enumerate(slacks) if x>0)
    require((least_shift,least)==(127,LEAST_SLACK), "raw cover slack mismatch")
    _,_,h=matrices()
    raw_corr=tuple(sum(h[r][s]*sum(kernels[r][i]*kernels[s][i+d] for i in range(M-d))
                       for r in range(8) for s in range(8)) for d in range(M))
    require(raw_corr == CORRELATIONS, "raw correlations mismatch")
    q=[[lambdas[r]*weights[r][col] for r in range(8)] for col in range(N)]
    hi=inverse(h)
    phi=sum(qj[r]*hi[r][s]*qj[s] for qj in q for r in range(8) for s in range(8))
    a=M*raw_corr[0]; b=1+(phi-N)/16
    require((phi,a,b,a*b)==(EXPECTED_PHI,EXPECTED_A,EXPECTED_B,EXPECTED_PRODUCT), "raw objective mismatch")
    return {"commit":commit,"tree":tree,"sha256":UPSTREAM_SHA256,"official_run":"passed"}

def main(argv: list[str] | None = None) -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=DEFAULT_OUTPUT)
    parser.add_argument("--verify",type=Path)
    parser.add_argument("--upstream",type=Path)
    parser.add_argument("--self-check",action="store_true",help="run built-in semantic mutation checks")
    args=parser.parse_args(argv)
    if args.self_check:
        count=self_check()
        print(f"self-check: PASS ({count} mutations rejected); finite F(N) certificate only; global/novelty/#1191/prize claims unresolved")
    if args.upstream:
        print("upstream replay: PASS",json.dumps(verify_upstream(args.upstream),sort_keys=True))
    if args.verify:
        payload=json.loads(args.verify.read_text(encoding="utf-8")); validate_payload(payload)
        require(args.verify.read_bytes()==render_payload(payload), "certificate is not byte-canonical")
        print(f"certificate verify: PASS {payload['payload_sha256']}"); return 0
    if args.self_check and not args.upstream:
        return 0
    payload=build_payload(); validate_payload(payload); args.output.write_bytes(render_payload(payload))
    print(f"wrote {args.output}"); print(f"payload_sha256={payload['payload_sha256']}"); return 0

if __name__ == "__main__":
    raise SystemExit(main())
