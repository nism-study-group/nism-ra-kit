# Chapter registry: one entry per chapter page. build.py, export.py and boards.py all read it.
# Keep the order: build.py derives each chapter's answer-shuffle seed from its position,
# so new chapters go at the END.
from . import ch00, ch01, ch02_learn, ch02_qs, ch03_learn, ch03_qs, ch04, ch05, ch06_learn, ch06_qs, ch07, ch08_learn, ch08_qs, ch09, ch10_learn, ch10_qs, ch11, ch12_learn, ch12_qs

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
 "ch07": {"dir":"Ch07-Company-Business-Governance","file":"Ch07-study-page.html","data":ch07.DATA,"learn":ch07.LEARN,"widgets":"","title":"Company analysis: business and governance","n":7},
 "ch08": {"dir":"Ch08-Company-Financial-Analysis","file":"Ch08-study-page.html","data":ch08_qs.DATA,"learn":ch08_learn.LEARN,"widgets":ch08_learn.WIDGETS,"title":"Company analysis: financial analysis","n":8,"extra":"Includes both book case studies, a ratio formula sheet and a DuPont calculator."},
 "ch09": {"dir":"Ch09-Corporate-Actions","file":"Ch09-study-page.html","data":ch09.DATA,"learn":ch09.LEARN,"widgets":ch09.WIDGETS,"title":"Corporate actions","n":9,"extra":"Bonus, split and consolidation calculator."},
 "ch10": {"dir":"Ch10-Valuation-Principles","file":"Ch10-study-page.html","data":ch10_qs.DATA,"learn":ch10_learn.LEARN,"widgets":ch10_learn.WIDGETS,"title":"Valuation principles","n":10,"extra":"Includes the book's case study and a CAPM, WACC and Gordon calculator."},
 "ch11": {"dir":"Ch11-Commodities","file":"Ch11-study-page.html","data":ch11.DATA,"learn":ch11.LEARN,"widgets":ch11.WIDGETS,"title":"Fundamental analysis of commodities","n":11,"extra":"Hedge ratio calculator."},
 "ch12": {"dir":"Ch12-Risk-and-Return","file":"Ch12-study-page.html","data":ch12_qs.DATA,"learn":ch12_learn.LEARN,"widgets":ch12_learn.WIDGETS,"title":"Fundamentals of risk and return","n":12,"extra":"Return calculator and Sharpe, Treynor and Jensen calculator."},
}

# Figures that are interactive tools: skipped by the PNG export and drawn as a pointer on the boards.
WIDGET_FIGS = ("fig-map", "fig-bondtool", "fig-calc", "fig-bondcalc", "fig-carry", "fig-dupont", "fig-cacalc", "fig-wacc", "fig-hedgecalc", "fig-retcalc", "fig-rcalc")
