#!/usr/bin/env bash
set -euo pipefail

python3 scripts/check-md-relative-links.py
python3 scripts/check-md-relative-links.py README.md
python3 scripts/check-chapter-cards.py
python3 scripts/check-teaching-coverage.py --min-labs 2

# Optional gate: booklike-v2 checks (empty blocks / redirect minimal / duplicate lab entry).
# Enable via env:
#   BOOKLIKE_V2_CHECK=1          (warn-only, exit code always 0)
#   BOOKLIKE_V2_CHECK=1 BOOKLIKE_V2_STRICT=1   (strict, non-zero exit on issues)
if [[ "${BOOKLIKE_V2_CHECK:-0}" == "1" ]]; then
  if [[ "${BOOKLIKE_V2_STRICT:-0}" == "1" ]]; then
    python3 scripts/check-booklike-v2.py --strict
  else
    python3 scripts/check-booklike-v2.py
  fi
fi
