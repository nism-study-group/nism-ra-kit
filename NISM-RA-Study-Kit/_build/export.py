import os
from playwright.sync_api import sync_playwright
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/"
chs=[("Ch00-Orientation","Ch00-study-page.html"),("Ch01-Research-Analyst-Profession","Ch01-study-page.html"),("Ch02-Securities-Market","Ch02-study-page.html"),("Ch03-Equity-Debt-Terms","Ch03-study-page.html"),("Ch04-Fundamentals-of-Research","Ch04-study-page.html"),("Ch05-Economic-Analysis","Ch05-study-page.html"),("Ch06-Industry-Analysis","Ch06-study-page.html"),("Ch07-Company-Business-Governance","Ch07-study-page.html"),("Ch08-Company-Financial-Analysis","Ch08-study-page.html")]
with sync_playwright() as p:
    b=p.chromium.launch()
    for d,f in chs:
        pg=b.new_page(viewport={"width":960,"height":900},device_scale_factor=2,color_scheme="light")
        pg.goto("file://"+R+d+"/"+f); pg.wait_for_timeout(300)
        ids=[x for x in pg.eval_on_selector_all("figure.fig","els=>els.map(e=>e.id)") if x not in ("fig-map","fig-bondtool","fig-calc","fig-bondcalc","fig-carry","fig-dupont")]
        for i,fid in enumerate(ids,1):
            name=f"{i:02d}-{fid.replace('fig-','')}.png"
            pg.locator("#"+fid).screenshot(path=f"{R}{d}/visuals/{name}")
        print(d,len(ids),"visuals")
    b.close()
