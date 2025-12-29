#!/usr/bin/env bash
set -euo pipefail

module="${1:-}"
if [[ -z "${module}" ]]; then
  echo "Usage: scripts/test-module.sh <module>"
  echo "Example: scripts/test-module.sh springboot-web-mvc"
  exit 2
fi

mvn -q -pl "${module}" test

