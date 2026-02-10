#!/usr/bin/env bash
# Generate an A4 PDF from an SVG using Chrome headless with zero margins.
# Usage: bash generate-pdf.sh <input.svg> [output.pdf]
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <input.svg> [output.pdf]"
  exit 1
fi

SVG_PATH="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
PDF_PATH="${2:-${SVG_PATH%.svg}.pdf}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# --- Pre-check: verify A4 bounds ---
echo "==> Running A4 bounds verification..."
if ! python3 "$SCRIPT_DIR/verify-a4.py" "$SVG_PATH"; then
  echo "ERROR: SVG failed A4 bounds check. Fix issues before generating PDF."
  exit 1
fi
echo ""

# --- Detect Chrome ---
if [ -x "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" ]; then
  CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
elif command -v google-chrome &>/dev/null; then
  CHROME="google-chrome"
elif command -v chromium-browser &>/dev/null; then
  CHROME="chromium-browser"
elif command -v chromium &>/dev/null; then
  CHROME="chromium"
else
  echo "ERROR: Chrome/Chromium not found."
  exit 1
fi

# --- Create temporary HTML wrapper ---
TMPHTML="$(mktemp /tmp/svg2pdf-XXXXXX.html)"
trap 'rm -f "$TMPHTML"' EXIT

SVG_CONTENT="$(cat "$SVG_PATH")"

cat > "$TMPHTML" <<HTMLEOF
<!DOCTYPE html>
<html>
<head>
<style>
  @page { size: 210mm 297mm; margin: 0; }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body {
    width: 210mm; height: 297mm;
    overflow: hidden;
    -webkit-print-color-adjust: exact;
  }
  body {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  svg {
    display: block;
    width: 210mm;
    height: 297mm;
  }
</style>
</head>
<body>
${SVG_CONTENT}
</body>
</html>
HTMLEOF

# --- Generate PDF ---
echo "==> Generating PDF: $PDF_PATH"
"$CHROME" \
  --headless \
  --disable-gpu \
  --no-sandbox \
  --print-to-pdf="$PDF_PATH" \
  --print-to-pdf-no-header \
  --no-pdf-header-footer \
  "file://$TMPHTML" \
  2>/dev/null

echo "==> Done: $PDF_PATH"
