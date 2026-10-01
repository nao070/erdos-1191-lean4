from __future__ import annotations
from pathlib import Path
import re
from typing import Dict, List, Tuple

REQUIRED_ROOT = [
    "AGENTS.md",
    "TOOL_ROUTER_POLICY.md",
    "tool-router-policy.yaml",
    "SOURCE_MAP.md",
    "DEPLOYMENT.md",
    "evals/PRESSURE_TESTS.yaml",
]
NAME_RE = re.compile(r"^[A-Za-z0-9-]+$")


def parse_frontmatter(path: Path) -> Tuple[Dict[str, str], str, List[str]]:
    errors: List[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) < 4 or lines[0].strip() != "---":
        return {}, text, [f"{path}: missing opening YAML frontmatter delimiter"]
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        return {}, text, [f"{path}: missing closing YAML frontmatter delimiter"]
    meta: Dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"{path}: malformed frontmatter line: {line}")
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"').strip("'")
    body = "\n".join(lines[end + 1 :])
    return meta, body, errors


def validate_pack(root: Path) -> List[str]:
    root = Path(root)
    errors: List[str] = []

    for rel in REQUIRED_ROOT:
        if not (root / rel).is_file():
            errors.append(f"missing required file: {rel}")

    skills_root = root / "skills"
    skill_files = sorted(skills_root.glob("*/SKILL.md")) if skills_root.exists() else []
    if len(skill_files) != 5:
        errors.append(f"expected exactly 5 SKILL.md files (4 research + 1 harness evolution), found {len(skill_files)}")

    seen = set()
    for skill in skill_files:
        meta, body, fm_errors = parse_frontmatter(skill)
        errors.extend(fm_errors)
        name = meta.get("name", "")
        desc = meta.get("description", "")
        if not name:
            errors.append(f"{skill}: missing name")
        elif not NAME_RE.match(name):
            errors.append(f"{skill}: invalid skill name {name!r}")
        elif name != skill.parent.name:
            errors.append(f"{skill}: skill name {name!r} does not match directory {skill.parent.name!r}")
        if name in seen:
            errors.append(f"duplicate skill name: {name}")
        seen.add(name)
        if not desc.startswith("Use when"):
            errors.append(f"{skill}: description must start with 'Use when'")
        if len(desc) > 500:
            errors.append(f"{skill}: description exceeds 500 characters")
        if len(body.split()) > 500:
            errors.append(f"{skill}: skill body exceeds 500 words ({len(body.split())})")
        if "/Users/" in body or "/root/" in body:
            errors.append(f"{skill}: contains machine-specific absolute path")

    if "harness-evolution" in seen:
        he = root / "skills/harness-evolution/SKILL.md"
        he_text = he.read_text(encoding="utf-8")
        for phrase in ["Immutable", "Weakness mining", "Minimal proposals", "Validation", "PROPOSE_ONLY"]:
            if phrase not in he_text:
                errors.append(f"harness-evolution missing required contract phrase: {phrase}")
        he_meta = root / "skills/harness-evolution/agents/openai.yaml"
        if not he_meta.is_file():
            errors.append("harness-evolution must include agents/openai.yaml")
        elif "allow_implicit_invocation: false" not in he_meta.read_text(encoding="utf-8"):
            errors.append("harness-evolution must disable implicit invocation")

    agents = root / "AGENTS.md"
    if agents.is_file():
        text = agents.read_text(encoding="utf-8")
        for phrase in ["Immutable truth surface", "Completion gate", "research/NEXT_THEOREM_CONTRACT.md", "TOOL_ROUTER_POLICY.md"]:
            if phrase not in text:
                errors.append(f"AGENTS.md missing required phrase: {phrase}")

    router = root / "tool-router-policy.yaml"
    if router.is_file():
        text = router.read_text(encoding="utf-8")
        m = re.search(r"reported_total_tools:\s*(\d+)", text)
        if not m or int(m.group(1)) != 85:
            errors.append("tool-router-policy.yaml must record the user-reported total of 85 tools")
        if "additionalQueries_supported: false" not in text:
            errors.append("tool-router-policy.yaml must not invent Exa additionalQueries support")

    pressure = root / "evals/PRESSURE_TESTS.yaml"
    if pressure.is_file():
        text = pressure.read_text(encoding="utf-8")
        ids = re.findall(r"^\s*- id:\s*(\S+)", text, flags=re.MULTILINE)
        if len(ids) < 20:
            errors.append(f"PRESSURE_TESTS.yaml has too few cases: {len(ids)}")
        if len(ids) != len(set(ids)):
            errors.append("PRESSURE_TESTS.yaml contains duplicate case IDs")
        if "SPECIFIED_NOT_YET_RUN_IN_USER_CODEX" not in text:
            errors.append("PRESSURE_TESTS.yaml must state that behavioral tests were not yet run in the user Codex runtime")

    return errors


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=str(Path(__file__).resolve().parents[1]))
    args = parser.parse_args()
    errors = validate_pack(Path(args.root))
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1
    print("STATIC PACK VALIDATION: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
