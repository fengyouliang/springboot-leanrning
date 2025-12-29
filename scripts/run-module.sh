#!/usr/bin/env bash
set -euo pipefail

module="${1:-}"
if [[ -z "${module}" ]]; then
  echo "Usage: scripts/run-module.sh <module>"
  echo "Example: scripts/run-module.sh springboot-basics"
  exit 2
fi

mvn -pl "${module}" spring-boot:run

