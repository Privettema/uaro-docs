#!/usr/bin/env bash
# Serve the docs on a port unique to this checkout, so several worktrees can run mkdocs at once.
# The port starts from a hash of the checkout path (8100-8999) and moves up until a free one is found.
# Usage: scripts/serve.sh [extra mkdocs serve args]
set -euo pipefail

root="$(git rev-parse --show-toplevel)"
port=$((8100 + $(printf '%s' "$root" | cksum | cut -d' ' -f1) % 900))

while lsof -iTCP:"$port" -sTCP:LISTEN >/dev/null 2>&1; do
  port=$((port + 1))
  [ "$port" -gt 8999 ] && port=8100
done

echo "Serving $root at http://127.0.0.1:$port/"
cd "$root"
exec mkdocs serve -a "127.0.0.1:$port" "$@"
