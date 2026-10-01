#!/usr/bin/env python3
"""Instrument this new module's targeted build and explicit declaration axiom audit only."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence"
SOURCE = ROOT / "Q1/SidonCollisionDetermination.lean"
DRIVER = OUT / "sidon_collision_determination_axioms.lean"
RUNNER = Path(__file__).resolve()
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
FROZEN_RECORD = ROOT / "evidence/sidon_collision_determination_prior_files.json"
FROZEN_FILES = json.loads(FROZEN_RECORD.read_text())["files"]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot():
    paths = [ROOT / p for p in ("lean-toolchain", "lakefile.toml", "lake-manifest.json", "Q1.lean")]
    paths += sorted((ROOT / "Q1").glob("*.lean"))
    paths += [DRIVER, RUNNER, FROZEN_RECORD]
    return {str(p.relative_to(ROOT)): sha(p) for p in paths}


def frozen_snapshot():
    return {name: sha(ROOT.parent / name) for name in FROZEN_FILES}


def save(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def run(label, argv):
    stem = OUT / ("sidon_collision_determination_" + label)
    for suffix in (".stdout.txt", ".stderr.txt", ".run.json"):
        if Path(str(stem) + suffix).exists():
            raise RuntimeError("Refusing to overwrite prior evidence: " + str(stem))
    before = snapshot()
    frozen_before = frozen_snapshot()
    if frozen_before != FROZEN_FILES:
        raise RuntimeError("A prior frozen file differs before execution")
    started = datetime.now(timezone.utc).isoformat()
    timer = time.perf_counter()
    proc = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    elapsed = time.perf_counter() - timer
    finished = datetime.now(timezone.utc).isoformat()
    after = snapshot()
    frozen_after = frozen_snapshot()
    stdout_path = Path(str(stem) + ".stdout.txt")
    stderr_path = Path(str(stem) + ".stderr.txt")
    stdout_path.write_bytes(proc.stdout)
    stderr_path.write_bytes(proc.stderr)
    record = {
        "argv": argv, "cwd": str(ROOT), "started_utc": started, "finished_utc": finished,
        "wall_time_seconds": elapsed, "observed_returncode": proc.returncode,
        "source_sha256_before": before, "source_sha256_after": after,
        "source_unchanged_gate_performed": True, "source_unchanged_gate_passed": before == after,
        "prior_frozen_record": str(FROZEN_RECORD), "prior_frozen_record_sha256": sha(FROZEN_RECORD),
        "prior_frozen_file_count": len(FROZEN_FILES),
        "prior_frozen_sha256_before": frozen_before, "prior_frozen_sha256_after": frozen_after,
        "prior_frozen_unchanged_gate_passed": frozen_before == frozen_after == FROZEN_FILES,
        "stdout_path": str(stdout_path), "stdout_sha256": sha(stdout_path),
        "complete_stdout": proc.stdout.decode(),
        "stderr_path": str(stderr_path), "stderr_sha256": sha(stderr_path),
        "complete_stderr": proc.stderr.decode(), "runner_sha256": sha(RUNNER),
    }
    save(Path(str(stem) + ".run.json"), record)
    print(label + ": exit=" + str(proc.returncode) + ", unchanged=" + str(before == after), flush=True)
    if proc.stdout:
        print(proc.stdout.decode(), end="", flush=True)
    if proc.stderr:
        print(proc.stderr.decode(), end="", file=sys.stderr, flush=True)
    if proc.returncode or before != after or frozen_before != frozen_after:
        raise RuntimeError("Evidence gate failed: " + label)
    return record


def main():
    lake = shutil.which("lake")
    elan = shutil.which("elan")
    if not lake or not elan:
        raise RuntimeError("Pinned Lean/Lake launchers unavailable")
    runtime = {
        "python_executable": str(Path(sys.executable).resolve()),
        "python_version": sys.version,
        "python_executable_sha256": sha(Path(sys.executable).resolve()),
        "lake_launcher": lake,
        "lake_launcher_sha256": sha(Path(lake).resolve()),
        "versions_and_resolved_executables": {},
    }
    for label, argv in [
        ("lake_version", [lake, "--version"]),
        ("lean_version", [lake, "env", "lean", "--version"]),
        ("resolved_lean", [elan, "which", "lean"]),
        ("resolved_lake", [elan, "which", "lake"]),
    ]:
        record = run(label, argv)
        runtime["versions_and_resolved_executables"][label] = record
        if label.startswith("resolved_"):
            executable = Path(record["complete_stdout"].strip()).resolve()
            runtime[label + "_sha256"] = sha(executable)
    save(OUT / "sidon_collision_determination_runtime.json", runtime)
    run("build", [lake, "build", "Q1.SidonCollisionDetermination"])
    audited = run("axioms", [lake, "env", "lean", str(DRIVER.relative_to(ROOT))])
    text = SOURCE.read_text()
    declarations = ["Erdos1191Q1.SidonCollisionDetermination." + name for name in re.findall(
        r"^(?:noncomputable def|def|theorem)\s+(\w+)", text, re.MULTILINE)]
    driver_names = re.findall(r"^#print axioms (\S+)$", DRIVER.read_text(), re.MULTILINE)
    if declarations != driver_names:
        raise RuntimeError("Explicit driver differs from module declaration inventory")
    axiom_map = {}
    for name, values in re.findall(r"'([^']+)' depends on axioms: \[([^]]*)\]",
                                   audited["complete_stdout"]):
        if name in axiom_map:
            raise RuntimeError("Duplicate axiom output")
        axiom_map[name] = [s.strip() for s in values.split(",") if s.strip()]
    for name in re.findall(r"'([^']+)' does not depend on any axioms", audited["complete_stdout"]):
        if name in axiom_map:
            raise RuntimeError("Duplicate axiom output")
        axiom_map[name] = []
    if set(axiom_map) != set(declarations):
        raise RuntimeError("Axiom output does not cover every new declaration exactly once")
    if any(not set(values) <= ALLOWED for values in axiom_map.values()):
        raise RuntimeError("Disallowed axiom")
    banned = re.findall(r"\b(?:sorry|admit|axiom|native_decide|unsafe)\b", text)
    if banned:
        raise RuntimeError("Banned source token: " + repr(banned))
    artifacts = sorted((ROOT / ".lake/build/lib/lean/Q1").glob("SidonCollisionDetermination.*"))
    result = {
        "status": "PASS", "declarations": declarations, "declaration_count": len(declarations),
        "axioms_by_declaration": axiom_map, "allowed_axioms": sorted(ALLOWED),
        "explicit_driver_exact_coverage": True, "source_scan_banned_tokens": banned,
        "final_source_snapshot": snapshot(),
        "prior_frozen_file_count": len(FROZEN_FILES),
        "prior_frozen_files_unchanged": frozen_snapshot() == FROZEN_FILES,
        "compiled_artifact_sha256": {str(p.relative_to(ROOT)): sha(p) for p in artifacts},
        "scope": "Actual finite Sidon endpoint-record determination, near projection injectivity and cardinality at most the near-set cube. Full "
                 "matching-orbit partition, convolution energy, shared-envelope closure and Q1 remain unformalized. "
                 "The existing unrelated declaration audit was not rerun.",
    }
    save(OUT / "sidon_collision_determination_result.json", result)
    print("PASS: " + str(len(declarations)) + " explicit new declarations, allowed axioms only", flush=True)


if __name__ == "__main__":
    main()
