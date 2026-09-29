# Session 0: orientation class. Exam format, marking, syllabus, how the group works.
# Facts come from the workbook front matter (pages 2 to 13), the NISM exam page text,
# Annexure I (syllabus and weights) and the NISM test centre list for October 2026.

# (chapter, short name, marks, first book page). Chapter 15 ends on page 327.
SYL = [
 (1,"Introduction to Research Analyst Profession",1,15),
 (2,"Introduction to Securities Market",2,22),
 (3,"Terminology in Equity and Debt Markets",2,55),
 (4,"Fundamentals of Research",5,78),
 (5,"Economic Analysis",5,90),
 (6,"Industry Analysis",8,105),
 (7,"Company Analysis: Business and Governance",6,130),
 (8,"Company Analysis: Financial Analysis",12,145),
 (9,"Corporate Actions",5,187),
 (10,"Valuation Principles",12,198),
 (11,"Fundamental Analysis of Commodities",5,218),
 (12,"Fundamentals of Risk and Return",7,228),
 (13,"Qualities of a Good Research Report",5,247),
 (14,"Legal and Regulatory Environment",10,255),
 (15,"Technical Analysis",15,295),
]
LAST_PAGE = 327

# Plain-language summary of the official curriculum topics for each chapter.
TOPICS = {
 1:["What a research analyst does","Their main duties","Rules for dealing with companies and clients","Qualities of a good analyst"],
 2:["What securities are","Market words: shares, bonds, warrants, indices, mutual funds, ETFs, commodities","Primary market (IPO, FPO, rights, bonus, QIP, OFS and more) and secondary market","Who takes part: exchanges, depositories, brokers, funds, FPIs and others","Cash, forward, futures, options and swaps. Hedging and arbitrage","Demat and remat"],
 3:["Equity words: face value, book value, market cap, EPS, P/E, P/B, DVRs","Bond words: coupon, maturity, current yield, YTM, duration","Types of bonds: zero coupon, floating rate, convertible, perpetual and more","Commodity words: spot price, basis, contango, backwardation, cost of carry"],
 4:["Active and passive investing","Why research matters. Insider information versus mosaic analysis","Four approaches: technical, fundamental (top down and bottom up), quantitative, behavioural","Research on commodities, and how commodities affect shares"],
 5:["Basics of micro and macro economics","National income, savings, inflation, interest rates, jobs","Foreign money flows (FDI and FPI), fiscal and monetary policy, trade and exchange rates","Long-term, cyclical and seasonal trends. Where to find economic data"],
 6:["Defining an industry and its cycles","Market size and trends. Business life cycle","Porter's five forces, PESTLE, BCG matrix, SCP","Industry drivers and KPIs. Regulation. Taxes. Sources of data"],
 7:["Business models and pricing power","Competitive advantage and SWOT","Management quality, independent directors, governance, promoter holding","Business risks, credit rating history, ESG"],
 8:["Balance sheet, profit and loss, cash flow, notes to accounts","Standalone versus consolidated results. Equity dilution","Reading the audit report","Ratios: profitability, return, leverage, liquidity, efficiency. DuPont","Peer comparison and company history"],
 9:["Why companies take corporate actions","Dividend, rights, bonus, split, consolidation","Mergers, demergers, schemes of arrangement, loan restructuring","Buyback, delisting and relisting, share swap"],
 10:["Price versus value","DCF valuation","Earnings multiples: P/E, PEG, EV/EBITDA, EV/Sales, dividend yield","Asset multiples: P/B, EV/capital employed, NAV","Sum of the parts, new-age business metrics, CAPM"],
 11:["Supply and demand. Big producers and consumers","Currency and the dollar index. Global versus Indian prices","Crop, weather, stock and production data","Government policy, geopolitics, and hedging (hedge ratio)"],
 12:["Simple, annualised and compounded returns","Types of risk. Measuring risk. Beta","Sensitivity analysis and margin of safety","Sharpe, Treynor and Jensen's alpha","Behavioural biases and measuring liquidity"],
 13:["Qualities of a good research report","Rating conventions (buy, sell and so on)","Using a checklist, with a sample"],
 14:["Regulators: MoF, MCA, RBI, SEBI, IRDA, PFRDA, IBBI, WDRA","Key laws: SCRA 1956, SEBI Act 1992, insider trading, unfair trade practices, RA Regulations 2014, IBC","Code of conduct for analysts","Conflicts of interest and disclosures","Exchange surveillance: ASM and GSM"],
 15:["What technical analysis is. Types of charts","Dow Theory and market trends","Reversal and consolidation patterns","Support, resistance, trendlines and channels","Technical indicators"],
}

BLOCKS = [
 ("Foundations",[1,2,3],"Who an analyst is, how markets work, basic terms"),
 ("How research works",[4,5,6],"Approaches, the economy, industries"),
 ("The company",[7,8,9],"Business quality, financial statements, corporate actions"),
 ("Numbers and value",[10,11,12],"Valuation, commodities, risk and return"),
 ("Report, rules, charts",[13,14,15],"Writing reports, regulation, technical analysis"),
]

def _mk(m): return f"{m} mark" + ("" if m == 1 else "s")

def _pages(n):
    s = SYL[n-1][3]
    e = SYL[n][3]-1 if n < 15 else LAST_PAGE
    return e - s + 1

def _weights():
    out = ""
    for n,name,m,_ in SYL:
        out += f'<div class="wrow"><span class="wn">{n}</span><span class="wname">{name}</span><span class="wbar"><i style="width:{m/15*100:.1f}%"></i></span><span class="wm">{m}</span></div>'
    return out

def _blocks():
    out = ""
    for title,chs,desc in BLOCKS:
        m = sum(SYL[c-1][2] for c in chs)
        out += f'<div class="box"><span class="tag">Chapters {chs[0]} to {chs[-1]}</span><h4>{title}</h4><p class="bigm">{m} <small>marks</small></p><p>{desc}</p></div>'
    return out

def _density():
    rows = []
    for n,name,m,_ in SYL:
        p = _pages(n); rows.append((m/p*10, n, name, m, p))
    top = max(r[0] for r in rows)
    out = ""
    for d,n,name,m,p in rows:
        out += f'<div class="drow"><span class="wn">{n}</span><span class="dname">{name}<small>{p} pages, {_mk(m)}</small></span><span class="wbar"><i style="width:{d/top*100:.1f}%"></i></span><span class="wm">{d:.1f}</span></div>'
    return out

def _topics():
    out = ""
    for n,name,m,s in SYL:
        lis = "".join(f"<li>{t}</li>" for t in TOPICS[n])
        out += f'<details class="acc"><summary><b>{n}</b> {name} <span class="accm">{_mk(m)}</span></summary><ul>{lis}</ul><p class="ptr">Book pages {s} to {SYL[n][3]-1 if n < 15 else LAST_PAGE}.</p></details>'
    return out

EXTRA_CSS = """
<style>
.wrow,.drow{display:grid;grid-template-columns:2rem minmax(0,1.3fr) minmax(0,1fr) 2.4rem;gap:10px;align-items:center;padding:.4rem 0;border-bottom:1px solid var(--line)}
.wn{font-family:var(--head);font-weight:800;color:var(--muted)}
.wname,.dname{font-size:.93rem;line-height:1.3}
.dname small{display:block;color:var(--muted);font-size:.8rem}
.wbar{height:14px;background:var(--line);border-radius:99px;overflow:hidden}
.wbar i{display:block;height:100%;background:var(--indigo);border-radius:99px}
.drow .wbar i{background:var(--teal)}
.wm{font-family:var(--head);font-weight:800;text-align:right}
@media (max-width:560px){.wrow,.drow{grid-template-columns:1.6rem 1fr 2.4rem}.wbar{display:none}}
.big{font-family:var(--head);font-weight:800;font-size:2.4rem;line-height:1;display:block}
.bigm{font-family:var(--head);font-weight:800;font-size:1.9rem;line-height:1;margin:.3rem 0}
.bigm small{font-size:.9rem;color:var(--muted);font-weight:500}
.acc{background:var(--card);border:1px solid var(--line);border-radius:12px;margin:.45rem 0;padding:.1rem .9rem}
.acc summary{cursor:pointer;padding:.55rem 0;font-weight:700;list-style-position:outside}
.acc summary b{font-family:var(--head);color:var(--indigo);margin-right:.3rem}
.accm{font-weight:400;color:var(--muted);font-size:.88rem;white-space:nowrap}
.acc ul{margin-top:0}
.calc{display:grid;gap:14px}
.calc label{display:block;font-weight:700}
.calc output{font-family:var(--head);font-weight:800}
.calc input[type=range]{width:100%}
.calcres{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
@media (max-width:520px){.calcres{grid-template-columns:repeat(2,1fr)}}
.calcres div{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:.6rem;text-align:center}
.calcres b{display:block;font-family:var(--head);font-size:1.6rem}
.calcres small{color:var(--muted)}
.calcv{font-family:var(--head);font-weight:800;font-size:1.2rem;margin:.2rem 0 0}
.calcv.pass{color:var(--teal)}.calcv.fail{color:var(--brick)}
.stack .s1{background:var(--indigo)}.stack .s2{background:var(--teal)}
</style>
"""

LEARN = EXTRA_CSS + r"""
<div class="wrap">
<header class="hero">
<div class="kicker">Session 0: orientation</div>
<h1>The exam, the book and the plan</h1>
<div class="meta"><span class="pill">Covers the <b>whole exam</b></span><span class="pill">Workbook pages 1 to 13</span><span class="pill">About 45 minutes in class</span></div>
<p class="oneline"><span class="k">100 questions</span> in <span class="k">2 hours</span>. Pass at <span class="k">60</span>. Every wrong answer costs a quarter mark.</p>
</header>

<figure class="fig" id="fig-map"><figcaption>Today's map<span>Seven questions. Tap one to jump there.</span></figcaption>
<div class="map">
<a href="#s1"><b>1</b><span>Why take this exam?</span><small>Who needs it, what you get</small></a>
<a href="#s2"><b>2</b><span>What does the paper look like?</span><small>80 MCQs plus 5 case studies</small></a>
<a href="#s3"><b>3</b><span>How is it marked?</span><small>Negative marking, when to guess</small></a>
<a href="#s4"><b>4</b><span>What is on the syllabus?</span><small>15 chapters, very uneven weights</small></a>
<a href="#s5"><b>5</b><span>What about numericals?</span><small>Excel or LibreOffice at the centre</small></a>
<a href="#s6"><b>6</b><span>How do I book the exam?</span><small>Registration, centres, time slots</small></a>
<a href="#s7"><b>7</b><span>How does this group work?</span><small>One chapter per meeting</small></a>
</div></figure>

<div class="col">
<section class="sec" id="s1"><span class="secno">1</span><h2>Why take this exam?</h2>
<p>The exam is run by <span class="k">NISM</span>, the National Institute of Securities Markets. Under a SEBI regulation of 2007 on certifying market professionals, NISM sets a minimum knowledge level for people who work in the securities markets.</p>
<p>This exam is <b>Series XV: Research Analyst</b>. It is required for people who prepare or publish research reports:</p>
<ul><li>Research analysts registered with SEBI and their associated persons</li><li>People employed as research analysts</li><li>Partners of a research analyst firm</li></ul>
<div class="why"><b>The legal hook</b>Regulation <span class="num">7(2)</span> of the <b>SEBI (Research Analysts) Regulations, 2014</b> says associated persons must pass this exam. That is why it exists. You will study these regulations in Chapter 14.</div>
<div class="analogy">A driving licence test. It does not make you a great driver. It proves you know the rules and the basics, so others can trust you on the road.</div>
<h3>What passing gives you</h3>
<ul><li>A certificate, valid for <span class="num">3 years</span>.</li>
<li>The certificate is issued only if your <b>PAN</b> is in your NISM registration details. Add it when you register.</li>
<li>Passing does <b>not</b> by itself register you with SEBI as a research analyst. Registration is a separate process.</li></ul>
</section>

<section class="sec" id="s2"><span class="secno">2</span><h2>What does the paper look like?</h2>
<p>It is a computer-based test. There are two kinds of questions.</p>
</div>

<figure class="fig" id="fig-paper"><figcaption>The paper at a glance<span>100 questions, 1 mark each</span></figcaption>
<div class="grid g4">
<div class="box"><span class="big">100</span><p>marks, 100 questions</p></div>
<div class="box"><span class="big">120</span><p>minutes</p></div>
<div class="box"><span class="big">60</span><p>marks to pass (60%)</p></div>
<div class="box"><span class="big">&minus;0.25</span><p>for each wrong answer</p></div>
</div>
<div class="stack" style="margin-top:16px"><div class="s1" style="width:80%">80 standalone MCQs</div><div class="s2" style="width:20%">5 cases</div></div>
<p class="ptr" style="margin-top:8px">A case study is a short story about a person or company, followed by 4 questions. 5 cases &times; 4 questions = 20 marks.</p>
</figure>

<div class="col">
<p>This pattern started on <span class="num">20 January 2026</span>, when the syllabus was revised. Technical analysis and commodities were added. Our workbook is the <b>February 2026</b> version. It applies to exams taken on or after <span class="num">30 March 2026</span>.</p>
<h3>Time</h3>
<p>120 minutes for 100 questions is about <span class="num">72 seconds</span> a question. Case questions take longer, because you must read the story first.</p>
<div class="why"><b>A suggested time plan</b>This is our suggestion, not an NISM rule. Do the 80 MCQs first, in about 70 minutes. Then the 5 cases, about 7 minutes each. Keep the last 15 minutes to return to questions you marked for review.</div>
<div class="analogy">A cricket innings of 100 balls. Take the easy singles first. Do not spend five overs on one difficult bowler.</div>
</section>

<section class="sec" id="s3"><span class="secno">3</span><h2>How is it marked?</h2>
<div class="grid g3">
<div class="box gd"><h4>Right</h4><p class="bigm">+1</p></div>
<div class="box bd"><h4>Wrong</h4><p class="bigm">&minus;0.25</p></div>
<div class="box"><h4>Skipped</h4><p class="bigm">0</p></div>
</div>
<p>So <b>4 wrong answers wipe out 1 right answer</b>. Your net score is: right answers minus a quarter of wrong answers.</p>
</div>

<figure class="fig" id="fig-calc"><figcaption>Score calculator<span>Move the sliders. Skipped questions fill the rest of the 100.</span></figcaption>
<div class="calc">
<div><label for="c-right">Right answers: <output id="o-right">65</output></label><input type="range" id="c-right" min="0" max="100" value="65"></div>
<div><label for="c-wrong">Wrong answers: <output id="o-wrong">20</output></label><input type="range" id="c-wrong" min="0" max="100" value="20"></div>
<div class="calcres">
<div><b id="r-skip">15</b><small>skipped</small></div>
<div><b id="r-lost">5</b><small>marks lost to penalty</small></div>
<div><b id="r-net">60</b><small>net score</small></div>
<div><b id="r-need">0</b><small>short of 60</small></div>
</div>
<p class="calcv" id="r-verdict"></p>
</div></figure>

<div class="col">
<div class="trap">Getting 60 questions right is not enough if you also got some wrong. 65 right and 20 wrong gives exactly 60. 62 right and 38 wrong gives only 52.5.</div>
<h3>Should you guess?</h3>
<p>Each question has 4 options. The table shows what a guess earns you on average.</p>
</div>

<figure class="fig" id="fig-guess"><figcaption>What a guess is worth<span>Average marks gained per question</span></figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th>You can rule out</th><th>Chance of being right</th><th>Working</th><th>Average gain</th></tr></thead>
<tbody>
<tr><th>Nothing</th><td>1 in 4</td><td>0.25 &times; 1 minus 0.75 &times; 0.25</td><td><b>+0.06</b></td></tr>
<tr><th>1 option</th><td>1 in 3</td><td>0.33 &times; 1 minus 0.67 &times; 0.25</td><td><b>+0.17</b></td></tr>
<tr><th>2 options</th><td>1 in 2</td><td>0.5 &times; 1 minus 0.5 &times; 0.25</td><td><b>+0.38</b></td></tr>
</tbody></table></div></figure>

<div class="col">
<div class="why"><b>The rule we will use</b>A blind guess is barely better than a skip. If you can cross out even one option, answer. Skip only when you have no idea at all.</div>
</section>

<section class="sec" id="s4"><span class="secno">4</span><h2>What is on the syllabus?</h2>
<p>The book has <span class="k">15 chapters</span>. They are not worth the same. The marks below are the official weights from the workbook.</p>
</div>

<figure class="fig" id="fig-weights"><figcaption>Marks per chapter<span>Out of 100. Longest bar is 15 marks.</span></figcaption>
""" + _weights() + r"""
</figure>

<div class="col">
<p>Four chapters, <b>8, 10, 14 and 15</b>, carry <span class="num">49 marks</span> together. Chapters 1 to 3 carry only <span class="num">5</span>. We still read in order, because the early chapters teach the words the later ones use.</p>
</div>

<figure class="fig" id="fig-blocks"><figcaption>Five blocks of three<span>The marks grow as the book goes on</span></figcaption>
<div class="grid g3">""" + _blocks() + r"""</div></figure>

<div class="col">
<h3>Pages are not marks</h3>
<p>Some chapters are long but carry few marks. Others are short and carry many. The chart shows <b>marks per 10 pages</b> of the book. A longer bar means each page you read is worth more in the exam.</p>
</div>

<figure class="fig" id="fig-density"><figcaption>Marks per 10 pages<span>Page counts from the workbook contents page, so they are approximate</span></figcaption>
""" + _density() + r"""
</figure>

<div class="col">
<div class="analogy">Chapter 2 is a long road with few toll booths. Chapter 13 is a short road with many. Do not judge a chapter's importance by its thickness.</div>
<h3>What each chapter covers</h3>
<p>From the official curriculum. Tap a chapter to open it.</p>
""" + _topics() + r"""
<div class="trap">The workbook itself warns: the exam is <b>largely</b> based on the book, but NISM does not promise every question will come from it. The sample questions in the book are for reference only; the real exam may be harder.</div>
</section>

<section class="sec" id="s5"><span class="secno">5</span><h2>What about numericals?</h2>
<p>The test centre computers have either <span class="k">Microsoft Excel</span> or <span class="k">LibreOffice Calc</span>. You will not know which one in advance. The workbook advises being comfortable with both.</p>
<p>Numericals will come mostly from:</p>
<ul><li><b>Chapter 8</b>: financial ratios and DuPont analysis</li><li><b>Chapter 10</b>: DCF, P/E, EV/EBITDA and other valuation measures</li><li><b>Chapter 12</b>: returns, risk, beta, Sharpe and Treynor ratios</li><li><b>Chapter 3</b>: bond yields, in a small way</li></ul>
<div class="why"><b>Practise on a spreadsheet</b>When we reach these chapters, do the practice questions in a spreadsheet, not on a calculator. Typing formulas quickly is part of the skill the exam tests.</div>
</section>

<section class="sec" id="s6"><span class="secno">6</span><h2>How do I book the exam?</h2>
<ul><li>Register and book on NISM's certification portal: <b>cert.nism.ac.in</b> (linked from <b>www.nism.ac.in</b>).</li>
<li>Add your <b>PAN</b> to your profile, or the certificate will not be issued.</li>
<li>NISM publishes a list of test centres and dates <b>every month</b>. The October 2026 list has about <span class="num">230</span> centres across India.</li>
<li>Most centres offer two afternoon slots: <b>13:30 to 15:30</b> and <b>15:30 to 17:30</b>. A few offer other times. Each centre runs on certain dates only, so check your city in the latest month's list.</li>
<li>Helpdesk, as printed on the centre list: certification@nism.ac.in, phone +91 8080806476.</li></ul>
<div class="why"><b>When to book</b>Book once you have finished a first pass of the book and taken a full mock test. Each centre runs only on some dates, so look at the list early.</div>
</section>

<section class="sec" id="s7"><span class="secno">7</span><h2>How does this group work?</h2>
<p>We read the workbook <b>one chapter per meeting, in order</b>. That is 15 meetings after today. For each chapter there is one web page with three tabs.</p>
</div>

<figure class="fig" id="fig-meeting"><figcaption>One chapter, one week<span>What to do before and during each meeting</span></figcaption>
<div class="flow">
<div class="step"><h4>Learn</h4><p>Read the notes before the meeting. Yellow marks are key terms. Red boxes are exam traps.</p></div><div class="arrow"></div>
<div class="step"><h4>Flashcards</h4><p>Mark each card "Got it" or "Again". Come back to the "Again" pile.</p></div><div class="arrow"></div>
<div class="step"><h4>Quiz</h4><p>Take it in exam mode. Press "Copy result for the group" and paste it in the group chat.</p></div><div class="arrow"></div>
<div class="step gd"><h4>Meet</h4><p>We spend the meeting on the questions most people missed.</p></div>
</div></figure>

<div class="col">
<ul><li>The notes are shorter and simpler than the book, but they follow the <b>book</b>, not the news. Where current rules differ from the book, the exam marks against the book, so we do too.</li>
<li>Your flashcard and quiz progress is saved <b>only in your own browser</b>, on your own device. Nothing is collected or shared unless you paste your result yourself.</li>
<li>Every diagram is also saved as a picture, for sharing in the group chat.</li>
<li>Once more chapters are done, we will add a full mock test: 80 MCQs and 5 case sets, timed at 2 hours.</li></ul>
<p>Try it now: open the <b>Quiz</b> tab at the top of this page. It has questions on everything we covered today.</p>
</section>

<section class="sec" id="traps"><h2>Things people get wrong about this exam</h2>
<ol class="traplist">
<li>Thinking 60 right answers means a pass. Wrong answers pull the score down: 60 right and 8 wrong is only 58.</li>
<li>Skipping every doubtful question. If you can rule out one option, guessing pays on average.</li>
<li>Guessing wildly on questions you know nothing about. It barely helps and adds risk.</li>
<li>Giving every chapter equal time. Chapters 8, 10, 14 and 15 are nearly half the paper.</li>
<li>Judging a chapter by its length. Chapter 2 is 33 pages for 2 marks; Chapter 13 is 8 pages for 5 marks.</li>
<li>Ignoring the 20 case questions. They are one fifth of the paper and take longer to read.</li>
<li>Practising numericals only on a calculator. The centre gives you Excel or LibreOffice Calc.</li>
<li>Studying from an older workbook. Use the February 2026 version; the pattern and syllabus changed in 2026.</li>
<li>Forgetting to add your PAN. No PAN, no certificate.</li>
</ol>
</section>

<section class="sec" id="talk"><h2>For the group discussion</h2>
<ol class="talk">
<li>When does each of us plan to take the exam? Does 15 meetings fit that date?</li>
<li>Which chapters look hardest from the topic list? Which do we already know from work or study?</li>
<li>Who is comfortable with Excel formulas? Should we add a short spreadsheet session before Chapter 8?</li>
<li>What meeting day, time and length works for everyone?</li>
<li>How will we keep each other on track between meetings?</li>
</ol>
</section>
</div>

<footer>Built from the NISM Series XV workbook (February 2026 version), the official syllabus and the NISM test centre list for October 2026. Study aid only. Always check nism.ac.in for the latest rules.</footer>
</div>
"""

WIDGETS = r"""
window.__WIDGETS__ = function(){
  const r=document.getElementById('c-right'), w=document.getElementById('c-wrong');
  if(!r) return;
  function upd(e){
    let a=+r.value, b=+w.value;
    if(a+b>100){ if(e&&e.target===r){ b=100-a; w.value=b; } else { a=100-b; r.value=a; } }
    const s=100-a-b, lost=b*0.25, net=a-lost, need=Math.max(0,60-net);
    const f=x=>Number.isInteger(x)?String(x):x.toFixed(2).replace(/0$/,'');
    document.getElementById('o-right').textContent=a;
    document.getElementById('o-wrong').textContent=b;
    document.getElementById('r-skip').textContent=s;
    document.getElementById('r-lost').textContent=f(lost);
    document.getElementById('r-net').textContent=f(net);
    document.getElementById('r-need').textContent=f(need);
    const v=document.getElementById('r-verdict');
    v.textContent = net>=60 ? 'Pass' : 'Fail: '+f(need)+' marks short';
    v.className='calcv '+(net>=60?'pass':'fail');
  }
  r.addEventListener('input',upd); w.addEventListener('input',upd); upd();
};
"""

CARDS = [
 {"f":"How many questions, and how long?","b":"<b>100 questions</b> (100 marks) in <b>2 hours</b>."},
 {"f":"How is the paper split?","b":"<b>80 standalone MCQs</b> of 1 mark each, plus <b>5 case studies with 4 questions each</b> (20 marks)."},
 {"f":"Pass mark?","b":"<b>60 marks</b>, that is 60%."},
 {"f":"Negative marking?","b":"<b>Minus 0.25</b> for each wrong answer (25% of the question's mark). 0 for a skipped question."},
 {"f":"How many wrong answers cancel one right answer?","b":"<b>Four.</b> 4 &times; 0.25 = 1."},
 {"f":"Average gain from a blind guess on a 4-option question?","b":"About <b>+0.06</b>. Rule out one option: <b>+0.17</b>. Rule out two: <b>+0.38</b>."},
 {"f":"When did the current exam pattern start?","b":"<b>20 January 2026</b>, with the revised syllabus. Technical analysis and commodities were added."},
 {"f":"Which workbook version, and from when?","b":"<b>February 2026</b> version, for exams on or after <b>30 March 2026</b>."},
 {"f":"Which regulation makes this exam compulsory?","b":"Regulation <b>7(2)</b> of the <b>SEBI (Research Analysts) Regulations, 2014</b>."},
 {"f":"Which chapter carries the most marks?","b":"<b>Chapter 15, Technical Analysis: 15 marks.</b>"},
 {"f":"Which four chapters carry 49 marks together?","b":"<b>8</b> Financial Analysis (12), <b>10</b> Valuation (12), <b>14</b> Legal and Regulatory (10), <b>15</b> Technical Analysis (15)."},
 {"f":"How many marks do Chapters 1 to 3 carry together?","b":"<b>5 marks</b> (1 + 2 + 2)."},
 {"f":"What software is on the test centre computers?","b":"<b>Microsoft Excel or LibreOffice Calc.</b> Practise on both."},
 {"f":"What must you add to get the certificate?","b":"Your <b>PAN</b> (Income Tax Permanent Account Number) in your registration details."},
 {"f":"How long is the certificate valid?","b":"<b>3 years.</b>"},
 {"f":"Does passing register you with SEBI?","b":"<b>No.</b> Registration as a research analyst is a separate process."},
]

MCQS = [
 {"id":"0.1","q":"The NISM Series XV exam has ______ questions to be answered in ______.","o":["100; 2 hours","100; 3 hours","80; 2 hours","120; 2 hours"],"a":0,"w":"100 questions of 1 mark each, in 2 hours (120 minutes)."},
 {"id":"0.2","q":"Which of the following best describes the structure of the paper?","o":["80 MCQs of 1 mark and 5 case studies with 4 questions of 1 mark each","100 MCQs of 1 mark each","70 MCQs of 1 mark and 10 case studies with 3 questions each","80 MCQs of 1 mark and 10 case studies with 2 questions each"],"a":0,"w":"80 standalone MCQs (80 marks) plus 5 cases &times; 4 questions (20 marks)."},
 {"id":"0.3","q":"What is the passing score?","o":["60 marks","50 marks","65 marks","75 marks"],"a":0,"w":"The pass mark is 60 out of 100, that is 60%."},
 {"id":"0.4","q":"For a 1-mark question answered wrongly, the candidate loses:","o":["0.25 marks","0.33 marks","0.5 marks","Nothing; there is no negative marking"],"a":0,"w":"Negative marking is 25% of the marks for the question, so 0.25 for a 1-mark question."},
 {"id":"0.5","q":"A candidate gets 64 right, 24 wrong and skips 12. What is the net score?","o":["58","64","60","52"],"a":0,"w":"64 minus 24 &times; 0.25 = 64 minus 6 = 58. That is a fail, even though 64 answers were right."},
 {"id":"0.6","q":"Which chapter carries the highest weight in the exam?","o":["Technical Analysis","Company Analysis: Financial Analysis","Valuation Principles","Legal and Regulatory Environment"],"a":0,"w":"Technical Analysis carries 15 marks. Financial Analysis and Valuation carry 12 each; Legal and Regulatory carries 10."},
 {"id":"0.7","q":"Chapters 1, 2 and 3 together carry ______ marks.","o":["5","10","3","8"],"a":0,"w":"1 + 2 + 2 = 5 marks."},
 {"id":"0.8","q":"Which software will be available on the test centre computers for numericals?","o":["Microsoft Excel or LibreOffice Calc","A basic on-screen calculator only","Google Sheets","No software; numericals must be done by hand"],"a":0,"w":"The workbook says the workstations have either Microsoft Excel or LibreOffice Calc, and advises being comfortable with both."},
 {"id":"0.9","q":"The passing certificate is issued only to candidates who have:","o":["Furnished or updated their PAN in their registration details","Registered with SEBI as a research analyst","Scored at least 75 marks","Completed a work experience of one year"],"a":0,"w":"NISM issues the certificate only if the PAN is in the registration details."},
 {"id":"0.10","q":"Passing this exam is a requirement under which provision?","o":["Regulation 7(2) of the SEBI (Research Analysts) Regulations, 2014","Section 12 of the SEBI Act, 1992","The SEBI (Investment Advisers) Regulations, 2013","The Securities Contracts (Regulation) Act, 1956"],"a":0,"w":"The workbook states that associated persons must pass the exam to meet Regulation 7(2) of the SEBI (Research Analysts) Regulations, 2014."},
 {"id":"0.11","q":"The February 2026 workbook applies to exams taken on or after:","o":["30 March 2026","20 January 2026","1 February 2026","1 April 2026"],"a":0,"w":"30 March 2026. The tempting wrong answer is 20 January 2026, which is when the revised exam pattern launched."},
 {"id":"0.12","q":"On a 4-option question, you can rule out two options. On average, answering gains you about:","o":["+0.38 marks","+0.06 marks","+0.17 marks","Nothing; it is better to skip"],"a":0,"w":"A 1 in 2 chance: 0.5 &times; 1 minus 0.5 &times; 0.25 = 0.375. +0.06 is a blind guess; +0.17 is after ruling out one."},
 {"id":"0.13","q":"Which statement about passing the exam is correct?","o":["It does not by itself register the person with SEBI as a research analyst","It registers the person with SEBI automatically","It is valid for life","It is needed only by independent analysts, not employees"],"a":0,"w":"Passing gives a certificate valid for 3 years. SEBI registration is a separate process, and the exam applies to employees and partners too."},
 {"id":"0.14","q":"Chapters 8, 10, 14 and 15 together carry:","o":["49 marks","39 marks","54 marks","25 marks"],"a":0,"w":"12 + 12 + 10 + 15 = 49 marks, nearly half the paper."},
]

CASES = [
 {"id":"C0","title":"Meera's first mock test","text":"Meera takes a full 100-question mock test under exam rules. She answers 70 questions and skips 30. Of the 70 she answered, 58 are right and 12 are wrong.",
  "qs":[
   {"q":"What is Meera's net score?","o":["55","58","61","46"],"a":0,"w":"58 minus 12 &times; 0.25 = 58 minus 3 = 55."},
   {"q":"Did Meera pass?","o":["No, she is 5 marks short","Yes, she passed with 58","Yes, because she answered 70 questions","No, she is 2 marks short"],"a":0,"w":"The pass mark is 60 and her net score is 55, so she is 5 marks short. 58 is her count of right answers, not her score."},
   {"q":"Keeping her 12 wrong answers the same, how many of the 30 skipped questions must she answer correctly to pass?","o":["5","2","3","12"],"a":0,"w":"Each extra right answer adds 1 mark. 55 + 5 = 60."},
   {"q":"In 20 of the skipped questions, Meera could have ruled out two options each. If she had guessed on all 20, how much would she have gained on average?","o":["About 7.5 marks","About 1.2 marks","About 3.4 marks","Nothing"],"a":0,"w":"Each such guess is worth 0.5 &times; 1 minus 0.5 &times; 0.25 = 0.375 on average. 20 &times; 0.375 = 7.5, enough to pass on average."},
  ]},
]

DATA = {"id":"ch00","short":"Orientation","title":"Session 0: The exam, the book and the plan","cards":CARDS,"mcqs":MCQS,"cases":CASES}
