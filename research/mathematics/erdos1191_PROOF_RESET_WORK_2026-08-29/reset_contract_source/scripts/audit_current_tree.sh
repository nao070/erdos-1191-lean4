#!/usr/bin/env bash
set -uo pipefail

ROOT="${1:-}"
if [[ -z "$ROOT" || ! -d "$ROOT" ]]; then
  echo "Usage: $0 /path/to/erdos1191_NEXT_SESSION_HANDOFF_2026-08-28" >&2
  exit 2
fi

ROOT="$(cd "$ROOT" && pwd)"
OUT="${2:-$PWD/erdos1191_reset_audit_$(date +%Y%m%d_%H%M%S)}"
mkdir -p "$OUT"

exec > >(tee "$OUT/audit.log") 2>&1

echo "AUDIT_ROOT=$ROOT"
echo "AUDIT_OUTPUT=$OUT"
echo "DATE=$(date -Iseconds)"
echo

echo "== file count =="
find "$ROOT" -type f | wc -l

echo

echo "== top-level current-direction markers =="
for f in 00_START_HERE_PROMPT.txt HANDOFF_MANIFEST.md README_START_HERE_JA.md NEW_SESSION_LAUNCH_MESSAGE.txt; do
  if [[ -f "$ROOT/$f" ]]; then
    echo "--- $f"
    grep -nE 'Wave 1[2345]|P17|P18|Question 1|equivalent|next direction|primary next' "$ROOT/$f" | head -n 80 || true
  fi
done

echo

echo "== canonical later markers =="
for f in core_workspace/1191_MASTER_STATUS.md core_workspace/proof_obligations.md; do
  if [[ -f "$ROOT/$f" ]]; then
    echo "--- $f"
    grep -nE 'Wave 1[345]|P17|P18|Question 1|equivalent' "$ROOT/$f" | tail -n 100 || true
  fi
done

echo

echo "== package manifest verification =="
manifest_status=127
if [[ -f "$ROOT/integrity/verify_package.py" ]]; then
  (cd "$ROOT" && PYTHONDONTWRITEBYTECODE=1 python3 integrity/verify_package.py) \
    | tee "$OUT/verify_package.log"
  manifest_status=${PIPESTATUS[0]}
else
  echo "verify_package.py missing"
fi
echo "MANIFEST_EXIT=$manifest_status"

echo

echo "== Wave 13-15 artifacts =="
find "$ROOT/core_workspace/endpoint_variance" -maxdepth 1 -type f \
  \( -iname '*wave13*' -o -iname '*wave14*' -o -iname '*wave15*' \) \
  -printf '%f\n' | sort | tee "$OUT/wave13_15_files.txt"

echo

echo "== Wave 15 evidence gate =="
wave15_missing=0
for pattern in '*wave15*.py' 'test_wave15*.py' '*wave15*.json'; do
  if ! find "$ROOT/core_workspace/endpoint_variance" -maxdepth 1 -type f -iname "$pattern" | grep -q .; then
    echo "MISSING: $pattern"
    wave15_missing=1
  fi
done

echo

echo "== pytest collection =="
cd "$ROOT/core_workspace/endpoint_variance"
PYTHONDONTWRITEBYTECODE=1 pytest --collect-only -q -p no:cacheprovider \
  | tee "$OUT/pytest_collect.log"
collect_status=${PIPESTATUS[0]}
echo "COLLECT_EXIT=$collect_status"

echo

echo "== focused Wave 13/14 tests =="
PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider \
  test_wave13_p18_harmonic_obstruction_probe.py \
  test_wave13_new_birth_barrier_probe.py \
  test_wave14_future_rank_promotion.py \
  test_wave14_future_rank_promotion_certificate.py \
  | tee "$OUT/focused_tests.log"
focused_status=${PIPESTATUS[0]}
echo "FOCUSED_EXIT=$focused_status"

full_status=0
if [[ "${FULL:-0}" == "1" ]]; then
  echo
  echo "== optional full pytest =="
  PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider \
    | tee "$OUT/full_pytest.log"
  full_status=${PIPESTATUS[0]}
  echo "FULL_EXIT=$full_status"
fi

cat > "$OUT/summary.txt" <<EOF
ROOT=$ROOT
MANIFEST_EXIT=$manifest_status
WAVE15_MISSING_EVIDENCE=$wave15_missing
COLLECT_EXIT=$collect_status
FOCUSED_EXIT=$focused_status
FULL_REQUESTED=${FULL:-0}
FULL_EXIT=$full_status
EOF

if [[ $manifest_status -ne 0 || $wave15_missing -ne 0 || $collect_status -ne 0 || $focused_status -ne 0 || $full_status -ne 0 ]]; then
  echo
  echo "AUDIT_STATUS=UNSEALED_OR_INCOMPLETE"
  exit 1
fi

echo

echo "AUDIT_STATUS=PASS_FOR_REQUESTED_GATES"
