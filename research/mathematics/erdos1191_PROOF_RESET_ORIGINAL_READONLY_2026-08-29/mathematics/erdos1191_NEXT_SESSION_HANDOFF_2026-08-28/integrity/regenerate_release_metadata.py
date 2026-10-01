#!/usr/bin/env python3
"""Regenerate the sorted inventory and self-excluding SHA-256 manifest."""
from __future__ import annotations

import hashlib
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
MANIFEST = PACKAGE_ROOT / "integrity" / "PACKAGE_SHA256SUMS.txt"
INVENTORY = PACKAGE_ROOT / "FILE_INVENTORY.txt"
CACHE_PARTS = {"__pycache__", ".pytest_cache", ".ruff_cache", ".scholar_cache"}


def included_files() -> list[Path]:
    return sorted(
        (
            path
            for path in PACKAGE_ROOT.rglob("*")
            if path.is_file()
            and not (set(path.parts) & CACHE_PARTS)
            and path.suffix != ".lock"
        ),
        key=lambda path: path.relative_to(PACKAGE_ROOT).as_posix(),
    )


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def main() -> None:
    paths = included_files()
    relative_paths = [path.relative_to(PACKAGE_ROOT).as_posix() for path in paths]
    inventory_text = (
        "# File Inventory — Erdős Problem #1191 current continuation\n\n"
        f"Total release files: {len(relative_paths)}\n\n"
        + "\n".join(relative_paths)
        + "\n"
    )
    INVENTORY.write_text(inventory_text, encoding="utf-8")

    paths = included_files()
    lines = [
        f"{digest(path)}  {path.relative_to(PACKAGE_ROOT).as_posix()}"
        for path in paths
        if path != MANIFEST
    ]
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"WROTE INVENTORY: {len(paths)} files")
    print(f"WROTE MANIFEST: {len(lines)} self-excluding entries")


if __name__ == "__main__":
    main()
