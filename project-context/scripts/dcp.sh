#!/usr/bin/env bash
# Wrapper DCP — bootstrap (se necessário) + scan.py

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_PATH_FILE="$SCRIPT_DIR/.python-path"
VENV_PYTHON="$SCRIPT_DIR/.venv/bin/python"

get_python() {
  if [[ -f "$PYTHON_PATH_FILE" ]]; then
    local p
    p="$(cat "$PYTHON_PATH_FILE")"
    [[ -x "$p" ]] && echo "$p" && return 0
  fi
  [[ -x "$VENV_PYTHON" ]] && echo "$VENV_PYTHON" && return 0
  command -v python3 2>/dev/null || command -v python 2>/dev/null || return 1
}

PYTHON="$(get_python)" || true
if [[ -z "${PYTHON:-}" ]]; then
  echo "Bootstrap necessário..."
  bash "$SCRIPT_DIR/bootstrap.sh"
  PYTHON="$(cat "$PYTHON_PATH_FILE")"
fi

if [[ $# -eq 0 ]]; then
  exec "$PYTHON" "$SCRIPT_DIR/scan.py" --help
fi

exec "$PYTHON" "$SCRIPT_DIR/scan.py" "$@"
