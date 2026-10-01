"""Read saved evidence and resolve the checker after its completed replay.

This script does not build Lean, rerun the axiom audit, or rerun leanchecker.
"""
import datetime
import hashlib
import json
import pathlib
import subprocess
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]
PREFIX = ROOT / "evidence/sidon_ranked_collision_"


def sha(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def read(suffix):
    return json.loads(pathlib.Path(str(PREFIX) + suffix).read_text())


def write_new(suffix, data):
    path = pathlib.Path(str(PREFIX) + suffix)
    with path.open("x") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")


def check_map(mapping, root=ROOT):
    assert all(sha(root / path) == expected for path, expected in mapping.items())


def check_run(record, checker=False):
    assert record["observed_returncode"] == 0
    key = "source_and_artifact_sha256" if checker else "source_sha256"
    assert record[key + "_before"] == record[key + "_after"]
    check_map(record[key + "_after"])
    assert record["prior_frozen_sha256_before"] == record["prior_frozen_sha256_after"]
    assert record["prior_frozen_sha256_after"] == frozen["files"]
    check_map(record["prior_frozen_sha256_after"], ROOT.parent)
    assert sha(record["prior_frozen_record"]) == record["prior_frozen_record_sha256"]
    for channel in ("stdout", "stderr"):
        path = pathlib.Path(record[channel + "_path"])
        assert sha(path) == record[channel + "_sha256"]
        assert path.read_bytes() == record["complete_" + channel].encode()
    runner = "checker_verify.py" if checker else "verify.py"
    assert record["runner_sha256"] == sha(str(PREFIX) + runner)


frozen = json.loads((ROOT / "evidence/sidon_ranked_collision_prior_files.json").read_text())
assert len(frozen["files"]) == 219
check_map(frozen["files"], ROOT.parent)
result, runtime = read("result.json"), read("runtime.json")
assert result["status"] == "PASS" and result["declaration_count"] == 4
assert len(set(result["declarations"])) == 4
assert set(result["axioms_by_declaration"]) == set(result["declarations"])
assert result["explicit_driver_exact_coverage"]
assert result["source_scan_banned_tokens"] == []
assert all(set(v) <= {"propext", "Classical.choice", "Quot.sound"}
           for v in result["axioms_by_declaration"].values())
check_map(result["final_source_snapshot"])
check_map(result["compiled_artifact_sha256"])
for name in ("build", "axioms"):
    check_run(read(name + ".run.json"))
for record in runtime["versions_and_resolved_executables"].values():
    check_run(record)
assert sha(runtime["python_executable"]) == runtime["python_executable_sha256"]
assert sha(runtime["lake_launcher"]) == runtime["lake_launcher_sha256"]
for name in ("lean", "lake"):
    path = runtime["versions_and_resolved_executables"]["resolved_" + name]["complete_stdout"].strip()
    assert sha(path) == runtime["resolved_" + name + "_sha256"]
checker = read("checker.run.json")
check_run(checker, checker=True)
assert checker["checker_executable_sha256_before"] == checker["checker_executable_sha256_after"]
assert sha(checker["checker_executable"]) == checker["checker_executable_sha256_after"]

argv = [runtime["lake_launcher"], "env", "which", "leanchecker"]
checker_before = sha(checker["checker_executable"])
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
tick = time.monotonic()
completed = subprocess.run(argv, cwd=ROOT, capture_output=True, check=False)
elapsed = time.monotonic() - tick
finished = datetime.datetime.now(datetime.timezone.utc).isoformat()
resolved = completed.stdout.decode().strip()
resolution = {
    "scope": "Post-replay executable resolution only; not another checker replay.",
    "argv": argv,
    "cwd": str(ROOT),
    "started_utc": started,
    "finished_utc": finished,
    "wall_time_seconds": elapsed,
    "observed_returncode": completed.returncode,
    "complete_stdout": completed.stdout.decode(),
    "complete_stderr": completed.stderr.decode(),
    "stdout_sha256": hashlib.sha256(completed.stdout).hexdigest(),
    "stderr_sha256": hashlib.sha256(completed.stderr).hexdigest(),
    "checker_executable_sha256_before": checker_before,
    "checker_executable_sha256_after": sha(checker["checker_executable"]),
    "matches_recorded_checker_path": resolved == checker["checker_executable"],
    "runner_sha256": sha(__file__),
}
write_new("checker_resolution.run.json", resolution)
assert completed.returncode == 0 and resolution["matches_recorded_checker_path"]
assert resolution["checker_executable_sha256_after"] == checker_before
check_map(result["final_source_snapshot"])
check_map(frozen["files"], ROOT.parent)
paths = sorted((ROOT / "evidence").glob("sidon_ranked_collision_*"))
binding = {
    "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "status": "PASS",
    "scope": "Current byte readback of the saved targeted build, explicit audit and imported-environment checker; no substantive rerun.",
    "declaration_count": 4,
    "source_snapshot_count": len(result["final_source_snapshot"]),
    "checker_snapshot_count": len(checker["source_and_artifact_sha256_after"]),
    "source_sha256": sha(ROOT / "Q1/SidonRankedCollision.lean"),
    "evidence_sha256": {str(p.relative_to(ROOT)): sha(p) for p in paths if p.is_file()},
    "all_saved_output_bytes_match": True,
    "all_saved_source_and_artifact_bytes_match": True,
    "all_runtime_executable_bytes_match": True,
    "prior_frozen_files_count": 219,
    "prior_frozen_files_current_match": True,
    "runner_sha256": sha(__file__),
}
write_new("readback.json", binding)
print(json.dumps({k: v for k, v in binding.items() if k != "evidence_sha256"}, indent=2))
