# Screenshots every <figure class="fig"> on each chapter page to ChNN-.../visuals/NN-name.png (for the group chat).
# Run after build.py. Needs playwright.
import os, sys
from playwright.sync_api import sync_playwright
HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.dirname(HERE) + "/"
sys.path.insert(0, HERE)
from chapters import CH, WIDGET_FIGS

with sync_playwright() as p:
    b = p.chromium.launch()
    for c in sorted(CH.values(), key=lambda c: c["n"]):
        d, f = c["dir"], c["file"]
        pg = b.new_page(viewport={"width": 960, "height": 900}, device_scale_factor=2, color_scheme="light")
        pg.goto("file://" + R + d + "/" + f); pg.wait_for_timeout(300)
        ids = [x for x in pg.eval_on_selector_all("figure.fig", "els=>els.map(e=>e.id)") if x not in WIDGET_FIGS]
        for i, fid in enumerate(ids, 1):
            name = f"{i:02d}-{fid.replace('fig-', '')}.png"
            pg.locator("#" + fid).screenshot(path=f"{R}{d}/visuals/{name}")
        print(d, len(ids), "visuals")
    b.close()
