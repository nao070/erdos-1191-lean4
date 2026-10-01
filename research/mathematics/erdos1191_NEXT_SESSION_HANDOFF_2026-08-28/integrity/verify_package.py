#!/usr/bin/env python3
"""Verify the self-excluding SHA-256 manifest for this handoff package."""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    manifest = root / "integrity" / "PACKAGE_SHA256SUMS.txt"
    if not manifest.is_file():
        print(f"ERROR: missing manifest: {manifest}", file=sys.stderr)
        return 2

    expected: dict[str, str] = {}
    errors: list[str] = []
    for line_no, raw in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        try:
            digest, rel = line.split("  ", 1)
        except ValueError:
            errors.append(f"malformed manifest line {line_no}: {raw!r}")
            continue
        if len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
            errors.append(f"invalid digest on line {line_no}: {digest!r}")
            continue
        if rel in expected:
            errors.append(f"duplicate manifest path on line {line_no}: {rel}")
            continue
        expected[rel] = digest

    excluded = {"integrity/PACKAGE_SHA256SUMS.txt"}
    all_files = [p for p in root.rglob("*") if p.is_file()]
    forbidden_cache_files = sorted(
        p.relative_to(root).as_posix()
        for p in all_files
        if "__pycache__" in p.parts
        or ".pytest_cache" in p.parts
        or ".ruff_cache" in p.parts
        or ".scholar_cache" in p.parts
    )
    if forbidden_cache_files:
        errors.append("forbidden cache files present: " + ", ".join(forbidden_cache_files))
    forbidden_lock_files = sorted(
        p.relative_to(root).as_posix() for p in all_files if p.suffix == ".lock"
    )
    if forbidden_lock_files:
        errors.append("forbidden lock files present: " + ", ".join(forbidden_lock_files))

    actual_files = {
        p.relative_to(root).as_posix()
        for p in all_files
        if p.relative_to(root).as_posix() not in excluded
        and "__pycache__" not in p.parts
        and ".pytest_cache" not in p.parts
        and ".ruff_cache" not in p.parts
        and ".scholar_cache" not in p.parts
        and p.suffix != ".lock"
    }

    listed = set(expected)
    missing_from_manifest = sorted(actual_files - listed)
    missing_from_disk = sorted(listed - actual_files)
    if missing_from_manifest:
        errors.append("unlisted files: " + ", ".join(missing_from_manifest))
    if missing_from_disk:
        errors.append("listed but missing files: " + ", ".join(missing_from_disk))

    checked = 0
    for rel in sorted(listed & actual_files):
        got = sha256(root / rel)
        checked += 1
        if got != expected[rel]:
            errors.append(f"checksum mismatch: {rel}\n  expected {expected[rel]}\n  got      {got}")

    if errors:
        print("PACKAGE VERIFICATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PACKAGE VERIFICATION PASSED: {checked} files")
    print("Manifest intentionally excludes integrity/PACKAGE_SHA256SUMS.txt itself.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
