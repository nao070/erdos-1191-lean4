from pathlib import Path
import importlib.util
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_pack.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_pack", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def test_real_pack_is_valid():
    mod = load_validator()
    errors = mod.validate_pack(ROOT)
    assert errors == []


def test_bad_skill_description_is_rejected():
    mod = load_validator()
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "skills" / "bad").mkdir(parents=True)
        (root / "AGENTS.md").write_text("# AGENTS\n", encoding="utf-8")
        (root / "TOOL_ROUTER_POLICY.md").write_text("# tools\n", encoding="utf-8")
        (root / "evals").mkdir()
        (root / "evals" / "PRESSURE_TESTS.yaml").write_text("version: 1\n", encoding="utf-8")
        (root / "skills" / "bad" / "SKILL.md").write_text(
            "---\nname: bad\ndescription: This workflow does many things\n---\n# Bad\n",
            encoding="utf-8",
        )
        errors = mod.validate_pack(root)
        assert any("description must start with 'Use when'" in e for e in errors)


def test_duplicate_skill_names_are_rejected():
    mod = load_validator()
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "skills" / "a").mkdir(parents=True)
        (root / "skills" / "b").mkdir(parents=True)
        (root / "AGENTS.md").write_text("# AGENTS\n", encoding="utf-8")
        (root / "TOOL_ROUTER_POLICY.md").write_text("# tools\n", encoding="utf-8")
        (root / "evals").mkdir()
        (root / "evals" / "PRESSURE_TESTS.yaml").write_text("version: 1\n", encoding="utf-8")
        body = "---\nname: same\ndescription: Use when testing duplicate names\n---\n# X\n"
        (root / "skills" / "a" / "SKILL.md").write_text(body, encoding="utf-8")
        (root / "skills" / "b" / "SKILL.md").write_text(body, encoding="utf-8")
        errors = mod.validate_pack(root)
        assert any("duplicate skill name" in e for e in errors)


def test_harness_evolution_is_explicit_only():
    mod = load_validator()
    meta = ROOT / "skills" / "harness-evolution" / "agents" / "openai.yaml"
    assert meta.is_file(), "harness-evolution must ship explicit-invocation metadata"
    text = meta.read_text(encoding="utf-8")
    assert "allow_implicit_invocation: false" in text
    errors = mod.validate_pack(ROOT)
    assert errors == []
