#!/bin/bash
# One-time setup of a headless Chromium for tools/labcheck.py and tools/shot1.py, without root.
# Everything goes under $BROWSER_DIR (default: ./.browser, which is git-ignored).
set -e
B=${BROWSER_DIR:-$(pwd)/.browser}
mkdir -p "$B/debs" "$B/libroot"
python3 -m venv "$B/venv"
"$B/venv/bin/pip" install -q playwright
PLAYWRIGHT_BROWSERS_PATH="$B/browsers" "$B/venv/bin/playwright" install --no-shell chromium
# Libraries and fonts Chromium needs that this VM does not have, unpacked locally (no apt install).
cd "$B/debs"
for p in libatk1.0-0t64 libatk-bridge2.0-0t64 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libasound2t64 \
         libatspi2.0-0t64 libxrender1 libxi6 libxres1 libwayland-server0 libxkbcommon0 libxshmfence1 libdrm2 libcups2t64 \
         libcairo2 libpango-1.0-0 libavahi-client3 libavahi-common3 libpixman-1-0 libxcb-render0 libxcb-shm0 libthai0 \
         libdatrie1 libfribidi0 libharfbuzz0b libgraphite2-3 libxft2 libfontconfig1 fontconfig-config \
         fonts-dejavu-core fonts-liberation fonts-noto-color-emoji; do
  apt-get download "$p" >/dev/null 2>&1 || echo "could not download $p"
done
for d in *.deb; do dpkg-deb -x "$d" "$B/libroot"; done
cat > "$B/fonts.conf" <<CONF
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
  <dir>$B/libroot/usr/share/fonts</dir>
  <cachedir>$B/fontcache</cachedir>
  <alias><family>sans-serif</family><prefer><family>DejaVu Sans</family></prefer></alias>
  <alias><family>system-ui</family><prefer><family>DejaVu Sans</family></prefer></alias>
</fontconfig>
CONF
echo "Done. Run tools with: tools/run.sh tools/labcheck.py lab-2.1"
