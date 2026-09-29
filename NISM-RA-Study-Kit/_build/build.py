import os, random, json, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from template import page, CSS, FONTS
import ch00, ch01, ch02_learn, ch02_qs, ch03_learn, ch03_qs, ch04, ch05, ch06_learn, ch06_qs

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CH = {
 "ch01": {"dir":"Ch01-Research-Analyst-Profession","file":"Ch01-study-page.html","data":ch01.DATA,"learn":ch01.LEARN,"widgets":"","title":"The research analyst profession","n":1},
 "ch02": {"dir":"Ch02-Securities-Market","file":"Ch02-study-page.html",
          "data":{"id":"ch02","short":"Ch2","title":"Chapter 2: The securities market","cards":ch02_qs.CARDS,"mcqs":ch02_qs.MCQS,"cases":ch02_qs.CASES},
          "learn":ch02_learn.LEARN,"widgets":ch02_learn.WIDGETS,"title":"The securities market","n":2,"extra":"Two interactive tools."},
 # Orientation class. Listed last so the shuffle seeds of the chapters above stay unchanged.
 "ch00": {"dir":"Ch00-Orientation","file":"Ch00-study-page.html","data":ch00.DATA,"learn":ch00.LEARN,"widgets":ch00.WIDGETS,"title":"Orientation: the exam, the book and the plan","n":0},
 "ch03": {"dir":"Ch03-Equity-Debt-Terms","file":"Ch03-study-page.html","data":ch03_qs.DATA,"learn":ch03_learn.LEARN,"widgets":ch03_learn.WIDGETS,"title":"Terms in equity and debt markets","n":3,"extra":"Two calculators: bond price and duration, commodity futures."},
 "ch04": {"dir":"Ch04-Fundamentals-of-Research","file":"Ch04-study-page.html","data":ch04.DATA,"learn":ch04.LEARN,"widgets":"","title":"Fundamentals of research","n":4},
 "ch05": {"dir":"Ch05-Economic-Analysis","file":"Ch05-study-page.html","data":ch05.DATA,"learn":ch05.LEARN,"widgets":"","title":"Economic analysis","n":5},
 "ch06": {"dir":"Ch06-Industry-Analysis","file":"Ch06-study-page.html","data":ch06_qs.DATA,"learn":ch06_learn.LEARN,"widgets":"","title":"Industry analysis","n":6},
}

def shuffle_q(q, rng, target):
    n=len(q["o"]); idx=list(range(n))
    fixed=[i for i in idx if "above" in q["o"][i].lower()]
    free=[i for i in idx if i not in fixed]
    if q["a"] in fixed:
        rng.shuffle(free); order=free+fixed
    else:
        others=[i for i in free if i!=q["a"]]; rng.shuffle(others)
        slots=len(free); t=target % slots
        order=others[:t]+[q["a"]]+others[t:]+fixed
    q["o"]=[q["o"][i] for i in order]; q["a"]=order.index(q["a"])

def prep(data, seed):
    rng=random.Random(seed)
    # Balance MCQs and case questions separately, so each group is even on its own.
    for group in (list(data["mcqs"]), [q for c in data.get("cases",[]) for q in c["qs"]]):
        targets=[i%4 for i in range(len(group))]; rng.shuffle(targets)
        for q,t in zip(group,targets): shuffle_q(q,rng,t)

def strip(h): return re.sub(r"<[^>]+>", "", h).replace("&amp;","&")

def bank_md(key, c):
    d = c["data"]; L = "abcd"
    out = [f"# Chapter {c['n']}: {c['title']}" if c['n'] else f"# Session 0: {c['title']}", "", "Question bank for the NISM Series XV study group. Answers and explanations are at the end of each section so you can test yourself first.", "", "Scoring in the exam: +1 right, minus 0.25 wrong, 0 skipped.", "", "## Multiple-choice questions", ""]
    for i,q in enumerate(d["mcqs"],1):
        out.append(f"**Q{q['id']}.** {strip(q['q'])}  ")
        for k,o in enumerate(q["o"]): out.append(f"{L[k]}) {strip(o)}  ")
        out.append("")
    out += ["### Answers", ""]
    for q in d["mcqs"]:
        out.append(f"- **Q{q['id']}: {L[q['a']]}**. {strip(q['w'])}")
    for cs in d.get("cases", []):
        out += ["", f"## Case {cs['id']}: {cs['title']}", "", strip(cs["text"]), ""]
        for k,q in enumerate(cs["qs"],1):
            out.append(f"**{cs['id']}-{k}.** {strip(q['q'])}  ")
            for j,o in enumerate(q["o"]): out.append(f"{L[j]}) {strip(o)}  ")
            out.append("")
        out += ["### Answers", ""]
        for k,q in enumerate(cs["qs"],1):
            out.append(f"- **{cs['id']}-{k}: {L[q['a']]}**. {strip(q['w'])}")
    return "\n".join(out) + "\n"

WEIGHTS = [(1,"Introduction to Research Analyst Profession",1),(2,"Introduction to Securities Market",2),(3,"Terminology in Equity and Debt Markets",2),(4,"Fundamentals of Research",5),(5,"Economic Analysis",5),(6,"Industry Analysis",8),(7,"Company Analysis: Business and Governance",6),(8,"Company Analysis: Financial Analysis",12),(9,"Corporate Actions",5),(10,"Valuation Principles",12),(11,"Fundamental Analysis of Commodities",5),(12,"Fundamentals of Risk and Return",7),(13,"Qualities of a Good Research Report",5),(14,"Legal and Regulatory Environment",10),(15,"Technical Analysis",15)]

def home():
    links = {c['n']:f"{c['dir']}/{c['file']}" for c in CH.values() if c['n']}
    cards = ""
    for n in sorted(links):
        c = next(c for c in CH.values() if c['n']==n); d = c['data']; w = WEIGHTS[n-1][2]
        cards += f'<a class="chcard" href="{links[n]}"><b>Chapter {n}</b><h3>{c["title"]}</h3><p class="ptr">{w} mark{"" if w==1 else "s"}. {len(d["cards"])} flashcards, {len(d["mcqs"])} MCQs, {sum(len(x["qs"]) for x in d["cases"])} case questions. {c.get("extra","")}</p></a>\n'
    intro = f"{CH['ch00']['dir']}/{CH['ch00']['file']}"
    rows = ""
    for n,name,w in WEIGHTS:
        ready = n in links
        nm = f'<a href="{links[n]}">{name}</a>' if ready else name
        tag = '<span class="rdy">Ready</span>' if ready else ''
        rows += f'<div class="wrow{" on" if ready else ""}"><span class="wn">{n}</span><span class="wname">{nm} {tag}</span><span class="wbar"><i style="width:{w/15*100:.1f}%"></i></span><span class="wm">{w}</span></div>'
    extra = """
.wrow{display:grid;grid-template-columns:2rem minmax(0,1.3fr) minmax(0,1fr) 2rem;gap:10px;align-items:center;padding:.45rem 0;border-bottom:1px solid var(--line)}
.wn{font-family:var(--head);font-weight:800;color:var(--muted)}
.wname{font-size:.95rem;line-height:1.3}
.wrow.on .wname a{font-weight:700}
.wbar{height:14px;background:var(--line);border-radius:99px;overflow:hidden}
.wbar i{display:block;height:100%;background:var(--indigo);border-radius:99px}
.wrow.on .wbar i{background:var(--teal)}
.wm{font-family:var(--head);font-weight:800;text-align:right}
.rdy{font-size:.72rem;font-weight:700;background:var(--teal);color:var(--card);border-radius:6px;padding:0 .35rem;vertical-align:2px}
@media (max-width:560px){.wrow{grid-template-columns:1.6rem 1fr 2rem}.wbar{display:none}}
.big{font-family:var(--head);font-weight:800;font-size:2.4rem;line-height:1}
.chcards{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}
.chcard{display:block;text-decoration:none;color:var(--ink);background:var(--card);border:1px solid var(--line);border-radius:18px;padding:18px}
.chcard:hover{border-color:var(--indigo)}
.chcard b{font-family:var(--head);color:var(--indigo)}
.chcard h3{margin:.3rem 0 .4rem}
"""
    html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>NISM Series XV study kit</title>{FONTS}<style>{CSS}{extra}</style></head><body>
<div class="bar"><div class="wrap"><span class="brand" style="display:block">NISM RA study kit</span><button class="themebtn" id="themebtn" style="margin-left:auto" aria-label="Switch light or dark">&#9790;</button></div></div>
<div class="wrap">
<header class="hero"><div class="kicker">NISM Series XV: Research Analyst</div><h1>Study kit</h1>
<p class="oneline">One page per chapter. Each page has <span class="k">notes</span>, <span class="k">flashcards</span> and an <span class="k">exam-style quiz</span>.</p></header>

<h2 style="margin-top:10px">Chapters ready</h2>
<div class="chcards">
<a class="chcard" href="{intro}"><b>Start here</b><h3>Orientation: the exam, the book and the plan</h3><p class="ptr">Exam format, marking, syllabus, booking, and how the group works. A score calculator and a short quiz on the exam rules.</p></a>
{cards}</div>

<section class="sec"><h2>The exam</h2>
<div class="grid g4">
<div class="box"><span class="big">100</span><p>marks, 100 questions</p></div>
<div class="box"><span class="big">120</span><p>minutes</p></div>
<div class="box"><span class="big">60</span><p>marks to pass</p></div>
<div class="box"><span class="big">&minus;0.25</span><p>for each wrong answer</p></div>
</div>
<p>The paper has <b>80 standalone MCQs</b> of one mark each, plus <b>5 case studies with 4 questions each</b>. This pattern started on 20 January 2026. The test computer has Excel or LibreOffice Calc for numericals, so practise on both.</p>
<div class="why"><b>Should you guess?</b>With 4 options, a blind guess earns on average 0.25 &times; 1 minus 0.75 &times; 0.25 = <b>+0.06</b> marks. Slightly positive, but a coin toss. If you can rule out <b>one</b> option, the average rises to <b>+0.17</b>. Rule out two and it is <b>+0.38</b>. So: skip only when you have no idea at all. If you can cross out even one option, answer.</div>
</section>

<section class="sec"><h2>Where the marks are</h2>
<p>Official weights from the February 2026 workbook. Chapters 8, 10, 14 and 15 together carry <b>49 marks</b>. Chapters 1 to 3 carry 5.</p>
<div style="margin-top:12px">{rows}</div>
</section>

<section class="sec"><h2>How to use each chapter page</h2>
<div class="flow">
<div class="step"><h4>Learn</h4><p>Read the notes before the meeting. Yellow marks are key terms. Red boxes are exam traps.</p></div><div class="arrow"></div>
<div class="step"><h4>Flashcards</h4><p>Mark each card "Got it" or "Again". The page remembers, on your own device.</p></div><div class="arrow"></div>
<div class="step"><h4>Quiz</h4><p>Take it in exam mode. Press "Copy result for the group" and paste it in the group chat.</p></div><div class="arrow"></div>
<div class="step gd"><h4>Meet</h4><p>Spend the meeting on the questions most people missed.</p></div>
</div></section>

<footer>Built from the NISM Series XV workbook (February 2026 version). Study aid only. Always check the official workbook and nism.ac.in.</footer>
</div>
<script>(function(){{const tb=document.getElementById('themebtn');function a(t){{if(t)document.documentElement.setAttribute('data-theme',t);else document.documentElement.removeAttribute('data-theme');}}let t=null;try{{t=localStorage.getItem('nismra:theme')}}catch(e){{}}a(t);tb.addEventListener('click',()=>{{const d=document.documentElement.getAttribute('data-theme')==='dark'||(!document.documentElement.getAttribute('data-theme')&&matchMedia('(prefers-color-scheme: dark)').matches);const n=d?'light':'dark';a(n);try{{localStorage.setItem('nismra:theme',n)}}catch(e){{}}}})}})();</script>
</body></html>"""
    return html

README = """# NISM Series XV Research Analyst: study kit

Open `index.html` in any browser. Everything works offline except the fonts, which fall back to system fonts.

## Folder layout

```
NISM-RA-Study-Kit/
  index.html                        Home: exam pattern, chapter weights, links
  README.md
  Ch00-Orientation/
    Ch00-study-page.html            Intro class: exam format, marking, syllabus, plan
  Ch01-Research-Analyst-Profession/
    Ch01-study-page.html            Notes + flashcards + quiz (one page)
    Ch01-question-bank.md           Printable questions, answers at the end
    visuals/                        Every diagram as a PNG, for the group chat
  Ch02-Securities-Market/
    (same three items)
```

New chapters get their own `ChNN-...` folder with the same three items.

## Notes

- Progress (flashcards known, questions missed) is saved in each person's own browser. Nothing is shared or uploaded.
- Quiz scoring matches the exam: +1, minus 0.25, 0 for a skip.
- Answer positions are shuffled, so there is no letter pattern to learn.
"""

if __name__ == "__main__":
    os.makedirs(ROOT, exist_ok=True)
    for i,(key,c) in enumerate(CH.items()):
        prep(c["data"], 1000+i)
        d = os.path.join(ROOT, c["dir"]); os.makedirs(os.path.join(d,"visuals"), exist_ok=True)
        with open(os.path.join(d, c["file"]),"w") as f: f.write(page(c["data"], c["learn"], c["widgets"]))
        with open(os.path.join(d, c["file"].replace("study-page.html","question-bank.md")),"w") as f: f.write(bank_md(key,c))
        dist = [q["a"] for q in c["data"]["mcqs"]]
        print(key, "answer spread a-d:", [dist.count(k) for k in range(4)], "cases:", [q["a"] for cs in c["data"]["cases"] for q in cs["qs"]])
    with open(os.path.join(ROOT,"index.html"),"w") as f: f.write(home())
    pub=os.path.join(HERE,"publish"); os.makedirs(pub,exist_ok=True)
    for key,c in CH.items():
        with open(os.path.join(pub,c["file"]),"w") as f: f.write(page(c["data"], c["learn"], c["widgets"], home=False))
    with open(os.path.join(ROOT,"README.md"),"w") as f: f.write(README)
    print("built")
