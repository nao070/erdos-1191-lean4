"""Run and bind the MomentDemand verification gates to their exact project sources.

This runner does not prove Q1. leanchecker uses its default from-imports mode.
Existing logs are preserved; choose a new suffix before deliberately repeating a run.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sources():
    paths = [ROOT / p for p in ("lean-toolchain", "lakefile.toml", "lake-manifest.json")]
    paths += [ROOT / "Q1.lean", *sorted((ROOT / "Q1").glob("*.lean"))]
    return {str(p.relative_to(ROOT)): sha(p) for p in paths}


def utc():
    return datetime.now(timezone.utc).isoformat()


def run(stem, command):
    log = EVIDENCE / (stem + ".log")
    metadata = EVIDENCE / (stem + ".run.json")
    assert not log.exists() and not metadata.exists(), "Refusing to replace prior evidence"
    record = {"command": command, "cwd": str(ROOT), "utc_started": utc(),
              "source_sha256_before": sources(), "runner_sha256": sha(Path(__file__))}
    with log.open("wb") as out:
        result = subprocess.run(command, cwd=ROOT, stdout=out, stderr=subprocess.STDOUT)
    record.update(exit_code=result.returncode, utc_completed=utc(),
                  source_sha256_after=sources(), log_sha256=sha(log))
    record["source_unchanged"] = record["source_sha256_before"] == record["source_sha256_after"]
    metadata.write_text(json.dumps(record, indent=2) + "\n")
    print(stem, "exit", result.returncode, "source_unchanged", record["source_unchanged"], flush=True)
    if result.returncode or not record["source_unchanged"]:
        sys.exit(result.returncode or 1)
    return record


def main():
    run("build-with-moment-demand", ["lake", "build"])
    run("axiom-audit-with-moment-demand", ["lake", "env", "lean", "Q1/AxiomAudit.lean"])
    audit = (EVIDENCE / "axiom-audit-with-moment-demand.log").read_text()
    allowed = {"propext", "Classical.choice", "Quot.sound"}
    checked = {}
    for match in re.finditer(r"'([^']+)' depends on axioms:\s*\[([^\]]*)\]", audit):
        checked[match[1]] = sorted(x.strip() for x in match[2].split(",") if x.strip())
    for match in re.finditer(r"'([^']+)' does not depend on any axioms", audit):
        checked[match[1]] = []
    expected = re.findall(r"^#print axioms (\S+)", (ROOT / "Q1/AxiomAudit.lean").read_text(), re.M)
    new = re.findall(r"^(?:noncomputable )?(?:def|theorem) (\w+)",
                     (ROOT / "Q1/MomentDemand.lean").read_text(), re.M)
    assert set(expected) == set(checked), (set(expected) - set(checked), set(checked) - set(expected))
    assert all(set(xs) <= allowed for xs in checked.values()), checked
    assert all("Erdos1191Q1." + name in checked for name in new)
    report = {"allowed": sorted(allowed), "checked": checked, "result": "PASS",
              "new_module_all_named_declarations": new,
              "log": "evidence/axiom-audit-with-moment-demand.log",
              "source_metadata": "evidence/axiom-audit-with-moment-demand.run.json"}
    (EVIDENCE / "axiom-allowlist-with-moment-demand.json").write_text(json.dumps(report, indent=2) + "\n")
    print("axiom allowlist PASS:", len(checked), "total;", len(new), "new named declarations", flush=True)
    run("leanchecker-moment-demand", ["lake", "env", "leanchecker", "Q1.MomentDemand"])
    lean_paths = [ROOT / "Q1.lean", *sorted((ROOT / "Q1").glob("*.lean"))]
    forbidden = r"\b(sorry|admit|sorryAx|native_decide|axiom)\b|Lean\.ofReduceBool|debug\.skipKernelTC"
    findings = {}
    for path in lean_paths:
        # Source-token hygiene complements, and does not replace, kernel axiom auditing.
        text = re.sub(r"/-.*?-/|--[^\n]*", "", path.read_text(), flags=re.S)
        hits = [m.group(0) for m in re.finditer(forbidden, text)]
        if hits:
            findings[str(path.relative_to(ROOT))] = hits
    assert not findings, findings
    scan = {"result": "PASS", "scope": [str(p.relative_to(ROOT)) for p in lean_paths],
            "source_sha256": sources(), "pattern": forbidden, "findings": findings}
    (EVIDENCE / "source-scan-with-moment-demand.json").write_text(json.dumps(scan, indent=2) + "\n")
    print("source trust-boundary scan PASS", flush=True)


if __name__ == "__main__":
    main()
