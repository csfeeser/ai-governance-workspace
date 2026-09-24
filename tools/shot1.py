"""usage: shot1.py URL_FRAGMENT OUT.png  (no reset; uses whatever answers are saved)"""
import sys
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(channel="chromium"); pg = b.new_page(viewport={"width": 1440, "height": 900})
    pg.goto("http://127.0.0.1:2299/#/" + sys.argv[1]); pg.wait_for_selector("#panel > *"); pg.wait_for_timeout(400)
    pg.screenshot(path=sys.argv[2]); b.close()
