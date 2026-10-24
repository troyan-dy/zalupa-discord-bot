#!/bin/bash
# Installs project dependencies for Claude Code cloud sessions.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"

PYTHON_VERSION="$(cat .python-version)"

if ! command -v poetry >/dev/null 2>&1; then
  pip install --quiet --user poetry
  export PATH="$HOME/.local/bin:$PATH"
fi

# Use the interpreter pinned in .python-version, installing it with uv when the image lacks it.
if command -v "python${PYTHON_VERSION}" >/dev/null 2>&1; then
  PYTHON_BIN="$(command -v "python${PYTHON_VERSION}")"
else
  uv python install --quiet "$PYTHON_VERSION"
  PYTHON_BIN="$(uv python find "$PYTHON_VERSION")"
fi

poetry env use --quiet "$PYTHON_BIN"
poetry sync --no-interaction --quiet
