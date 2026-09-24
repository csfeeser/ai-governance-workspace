#!/bin/bash
# Run a browser tool with the locally unpacked Chromium from tools/setup-browser.sh.
B=${BROWSER_DIR:-$(pwd)/.browser}
export LD_LIBRARY_PATH=$(find "$B/libroot" -name "*.so*" -printf "%h\n" | sort -u | paste -sd:)
export FONTCONFIG_FILE="$B/fonts.conf" PLAYWRIGHT_BROWSERS_PATH="$B/browsers"
"$B/venv/bin/python" "$@" 2>&1 | grep -v "NOTREACHED\|\]\[err\]"
