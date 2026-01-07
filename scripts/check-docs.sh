#!/usr/bin/env bash
set -euo pipefail

python3 scripts/check-md-relative-links.py
python3 scripts/check-md-relative-links.py README.md
python3 scripts/check-teaching-coverage.py --min-labs 2
python3 scripts/check-chapter-contract.py --require-labtest
