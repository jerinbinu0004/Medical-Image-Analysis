#!/usr/bin/env bash
# Simple helper to run the Flask app in background and show the local URL
set -e

# Move to project root (script assumes it's run from workspace root)
cd "$(dirname "$0")"

# Activate venv if present
if [ -d "venv" ] && [ -f "venv/bin/activate" ]; then
  # shellcheck disable=SC1091
  source venv/bin/activate
fi

echo "Starting Medical Image Processing server..."

# Start app in background with nohup so it keeps running after terminal closes
nohup python3 app.py > server.log 2>&1 &
PID=$!

echo "Server started (PID: $PID)."
echo "Open the app at: http://localhost:5000"
echo "Server logs: run_server.sh && tail -f server.log"

exit 0
