#!/usr/bin/env bash
set -euo pipefail

python3 scripts/docs-site-sync.py

python3 -m mkdocs build -f docs-site/mkdocs.yml
