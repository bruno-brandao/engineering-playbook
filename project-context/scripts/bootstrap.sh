#!/usr/bin/env bash
# Dev Context Platform — bootstrap (macOS / Linux)

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REQUIREMENTS="$SCRIPT_DIR/requirements.txt"
ROSYN_PROJECT="$SCRIPT_DIR/indexers/roslyn/RoslynIndexer/RoslynIndexer.csproj"
VENV_DIR="$SCRIPT_DIR/.venv"

find_python() {
  for cmd in python3 python py; do
    if command -v "$cmd" >/dev/null 2>&1; then
      if "$cmd" -c "import sys; exit(0 if sys.version_info >= (3, 10) else 1)" 2>/dev/null; then
        command -v "$cmd"
        return 0
      fi
    fi
  done
  return 1
}

install_python_hint() {
  echo "Python 3.10+ não encontrado."
  echo "  macOS:  brew install python@3.12"
  echo "  Ubuntu: sudo apt install python3 python3-venv python3-pip"
  exit 1
}

echo "=== DCP Bootstrap ==="

PYTHON="$(find_python)" || install_python_hint
echo "Python: $PYTHON"

if [[ ! -d "$VENV_DIR" ]]; then
  echo "Criando venv..."
  "$PYTHON" -m venv "$VENV_DIR"
fi

VENV_PYTHON="$VENV_DIR/bin/python"
"$VENV_PYTHON" -m pip install --upgrade pip -q
"$VENV_PYTHON" -m pip install -r "$REQUIREMENTS" -q

if command -v dotnet >/dev/null 2>&1 && [[ -f "$ROSYN_PROJECT" ]]; then
  echo "Compilando Roslyn indexer..."
  dotnet build "$ROSYN_PROJECT" -v q --nologo || echo "WARN: Roslyn build failed"
fi

"$VENV_PYTHON" "$SCRIPT_DIR/scan.py" --help >/dev/null
echo "$VENV_PYTHON" > "$SCRIPT_DIR/.python-path"
echo ""
echo "Bootstrap concluído."
echo "Use: ./project-context/scripts/dcp.sh status --project AtivosCompraMobilizacao"
