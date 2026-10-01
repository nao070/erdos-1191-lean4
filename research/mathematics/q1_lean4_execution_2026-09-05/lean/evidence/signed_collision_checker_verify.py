#!/usr/bin/env python3
"""One targeted Lean-kernel replay in the existing imported environment."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence"
RUNNER = Path(__file__).resolve()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    record_path = OUT / "signed_collision_checker.run.json"
    stdout_path = OUT / "signed_collision_checker.stdout.txt"
    stderr_path = OUT / "signed_collision_checker.stderr.txt"
    if any(p.exists() for p in (record_path, stdout_path, stderr_path)):
        raise RuntimeError("Refusing to overwrite prior checker evidence")
    result = json.loads((OUT / "signed_collision_result.json").read_text())
    runtime = json.loads((OUT / "signed_collision_runtime.json").read_text())
    lean_path = Path(runtime["versions_and_resolved_executables"]["resolved_lean"]["complete_stdout"].strip())
    checker_path = lean_path.with_name("leanchecker").resolve()
    paths = [ROOT / name for name in result["final_source_snapshot"]]
    paths += [ROOT / name for name in result["compiled_artifact_sha256"]]
    paths += [RUNNER, OUT / "signed_collision_result.json", OUT / "signed_collision_runtime.json"]
    before = {str(p.relative_to(ROOT)): sha(p) for p in paths}
    for name, expected in result["final_source_snapshot"].items():
        assert before[name] == expected
    for name, expected in result["compiled_artifact_sha256"].items():
        assert before[name] == expected
    checker_before = sha(checker_path)
    argv = [shutil.which("lake"), "env", "leanchecker", "Q1.SignedCollision"]
    started = datetime.now(timezone.utc).isoformat()
    timer = time.perf_counter()
    proc = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    elapsed = time.perf_counter() - timer
    finished = datetime.now(timezone.utc).isoformat()
    after = {str(p.relative_to(ROOT)): sha(p) for p in paths}
    checker_after = sha(checker_path)
    stdout_path.write_bytes(proc.stdout)
    stderr_path.write_bytes(proc.stderr)
    record = {
        "argv": argv, "cwd": str(ROOT), "mode": "from_imports",
        "started_utc": started, "finished_utc": finished, "wall_time_seconds": elapsed,
        "observed_returncode": proc.returncode,
        "source_and_artifact_sha256_before": before, "source_and_artifact_sha256_after": after,
        "source_and_artifact_unchanged_gate_performed": True,
        "source_and_artifact_unchanged_gate_passed": before == after,
        "checker_executable": str(checker_path),
        "checker_executable_sha256_before": checker_before,
        "checker_executable_sha256_after": checker_after,
        "runner_sha256": sha(RUNNER),
        "stdout_path": str(stdout_path), "stdout_sha256": sha(stdout_path),
        "complete_stdout": proc.stdout.decode(),
        "stderr_path": str(stderr_path), "stderr_sha256": sha(stderr_path),
        "complete_stderr": proc.stderr.decode(),
        "scope": "One new process replays Q1.SignedCollision declarations in their imported "
                 "environment using Lean's own kernel. This is not fresh replay of all imported "
                 "dependencies, an independent external checker, a Sidon partition proof or Q1.",
    }
    record_path.write_text(json.dumps(record, indent=2) + "\n")
    print(proc.stdout.decode(), end="")
    print(proc.stderr.decode(), end="", file=sys.stderr)
    print("checker_exit=" + str(proc.returncode) + "; unchanged=" + str(before == after))
    assert proc.returncode == 0 and before == after and checker_before == checker_after


if __name__ == "__main__":
    main()
