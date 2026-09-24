"""Visit every tab of a lab on the test server (http://127.0.0.1:2299), print JS errors, and optionally
screenshot each tab into a folder. Resets that lab's answers on the test server first.
usage: tools/run.sh tools/labcheck.py LAB [SHOT_DIR]"""
import sys, json, urllib.request
from playwright.sync_api import sync_playwright
lab = sys.argv[1]; shots = sys.argv[2] if len(sys.argv) > 2 else None
base = "http://127.0.0.1:2299"
urllib.request.urlopen(urllib.request.Request(f"{base}/api/labs/{lab}/answers", method="DELETE"))
tabs = json.load(urllib.request.urlopen(f"{base}/api/labs/{lab}"))["tabs"]
errors = []
with sync_playwright() as p:
    b = p.chromium.launch(channel="chromium")
    pg = b.new_page(viewport={"width": 1440, "height": 900})
    pg.on("console", lambda m: m.type == "error" and errors.append(m.text))
    pg.on("pageerror", lambda e: errors.append(str(e)))
    for i, t in enumerate(tabs):
        pg.goto(f"{base}/#/{lab}/{t['id']}"); pg.wait_for_selector("#panel > *"); pg.wait_for_timeout(300)
        steps = pg.locator(".step").count()
        print(f"tab {t['id']}: {t['type']} steps={steps}")
        if shots:
            name = f"{i+1}-" + "".join(c if c.isalnum() else "-" for c in t["title"].lower()).strip("-")
            while "--" in name: name = name.replace("--", "-")
            pg.screenshot(path=f"{shots}/{name}.png")
    b.close()
print("errors:", errors)
