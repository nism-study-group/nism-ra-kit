# Handover: NISM Series XV Research Analyst study kit

Read this whole file before doing anything. It covers the goal, the user's rules, what exists, how it is built, and what to do next.

---

## 1. The project in one paragraph

The organiser runs a study group preparing for the **NISM Series XV: Research Analyst** certification exam (SEBI). The group reads the official NISM workbook **one chapter at a time, in order**, and meets to discuss. For each chapter we produce: tighter, simpler, more visual notes than the book, plus assessment material (exam-style MCQs, case-based question sets, flashcards, quizzes). An orientation page (Session 0) and Chapters 1 to 6 are done and live. **Chapter 7 is next.**

---

## 2. The user's rules (apply to everything: code comments excepted, all user-facing text and replies)

- **No em dashes. No en dashes either.** Use a full stop, colon, comma or the word "to" (for ranges: "pages 15 to 21"). Run the dash check in section 9 before delivering.
- No jargon. If a technical term is unavoidable, explain it in plain words the first time.
- No mannered prose. Intuitive, simple language. Short, simple sentences.
- Use analogies wherever they help.
- No sycophancy. No side deviations: do what was asked, stay on task.
- Replies to the user: plain prose, minimal formatting, no flattery.

---

## 3. Source material

- **The workbook:** "NISM-Series-XV: Research Analyst Certification Examination Workbook", **February 2026 version**. It applies to exams on or after 30 March 2026.
- It lives at `source/17 NISM-Series-XV-Research Analyst Examination Workbook February 2026.pdf`, next to the kit folder. It is a real 342-page PDF. Extract with `pdftotext "<file>" book.txt` (no `-layout`). `source/` is gitignored: the workbook is copyrighted and must never be committed. Do not quote long passages from it in outputs.
- `source/` also holds `curriculum.txt`, `test-objectives.txt`, `revised-guidelines.txt` and `Annexure-I-Syllabus-Weightage.pdf` (official syllabus and weights). A monthly NISM test centre list (for example `October-2026-2.pdf`) may sit in the top folder; it is also gitignored.
- To locate a chapter: `grep -n "^CHAPTER" book.txt`. Each chapter heading appears twice: once in the contents, once at the chapter start.

### Chapter list and official weights (marks out of 100, from the workbook)

| Ch | Title | Marks | Book pages | Status |
|---|---|---|---|---|
| 1 | Introduction to Research Analyst Profession | 1 | 15 | Done |
| 2 | Introduction to Securities Market | 2 | 22 | Done |
| 3 | Terminology in Equity and Debt Markets | 2 | 55 | Done |
| 4 | Fundamentals of Research | 5 | 78 | Done |
| 5 | Economic Analysis | 5 | 90 | Done |
| 6 | Industry Analysis | 8 | 105 | Done |
| 7 | Company Analysis: Business and Governance | 6 | 130 | **Next** |
| 8 | Company Analysis: Financial Analysis | 12 | 145 | |
| 9 | Corporate Actions | 5 | 187 | |
| 10 | Valuation Principles | 12 | 198 | |
| 11 | Fundamental Analysis of Commodities | 5 | 218 | |
| 12 | Fundamentals of Risk and Return | 7 | 228 | |
| 13 | Qualities of a Good Research Report | 5 | 247 | |
| 14 | Legal and Regulatory Environment | 10 | 255 | |
| 15 | Technical Analysis | 15 | 295 | |

Annexures 1 to 3 start at page 328 (Annexure 1 is the RA Investor Charter; relevant to Chapter 14).

Chapters 8, 10, 14 and 15 carry 49 marks together. These deserve the most depth, the most numericals and the most case sets. Chapters 8, 10 and 12 need worked numerical problems (ratios, DuPont, DCF, P/E, EV/EBITDA, WACC, CAPM, risk measures). Chapter 15 needs chart-pattern visuals.

---

## 4. Exam facts (verified online in September 2026)

- 100 questions, 100 marks, 120 minutes. Pass mark 60.
- **80 standalone MCQs** (1 mark each) plus **5 case studies with 4 questions each** (1 mark each).
- **Negative marking: minus 0.25 per wrong answer.** 0 for a skipped question.
- This pattern launched **20 January 2026** (revised syllabus). Technical Analysis and commodities were added.
- Test centre computers have **Excel or LibreOffice Calc** for numericals.
- Certificate valid 3 years. Passing does not by itself register you with SEBI.
- Guessing math (shown on the home page): blind guess expected value +0.06; rule out one option +0.17; rule out two +0.375. So answer whenever at least one option can be eliminated.

---

## 5. What exists now

```
NISM-RA-Study-Kit/
  HANDOVER.md                       This file
  README.md                         Short user-facing readme
  index.html                        Home: exam pattern, guessing rule, weight chart, chapter links
  Ch01-Research-Analyst-Profession/
    Ch01-study-page.html            Single self-contained page: Learn + Flashcards + Quiz
    Ch01-question-bank.md           Same questions as the quiz, printable, answers at the end
    visuals/*.png                   8 diagrams exported as PNG (for WhatsApp)
  Ch02-Securities-Market/
    Ch02-study-page.html
    Ch02-question-bank.md
    visuals/*.png                   30 diagrams
  Ch00-Orientation/                 Session 0 intro class: exam format, marking, syllabus, booking, group plan
  Ch03-Equity-Debt-Terms/
  Ch04-Fundamentals-of-Research/
  Ch05-Economic-Analysis/
  Ch06-Industry-Analysis/           (each with study page, question bank, visuals/)
  _build/
    template.py                     Shared CSS, JS and HTML shell for every chapter page
    ch01.py                         Chapter 1 content: LEARN html, CARDS, MCQS, CASES, DATA
    ch02_learn.py                   Chapter 2 LEARN html and WIDGETS js (interactive tools)
    ch02_qs.py                      Chapter 2 CARDS, MCQS, CASES
    ch00.py                         Orientation page (Session 0), with a score calculator widget
    ch03_learn.py, ch03_qs.py       Chapter 3 (widgets: bond calculator, futures fair value calculator)
    ch04.py                         Chapter 4
    ch05.py                         Chapter 5
    ch06_learn.py, ch06_qs.py       Chapter 6
    build.py                        Builds every page, the home page, question banks, README
    export.py                       Screenshots each <figure class="fig"> to visuals/*.png
    publish/                        Copies of chapter pages with the home link removed (for hosting)
```

Content counts:
- Chapter 1: 18 flashcards, 14 MCQs, 1 case set (4 questions).
- Chapter 2: 52 flashcards, 42 MCQs, 2 case sets (8 questions). Two interactive tools: a bond name finder (domestic, foreign, euro, masala) and an options payoff slider (the book's Arvind and Salim example).
- Orientation (Session 0): 16 flashcards, 14 MCQs, 1 case set (C0). Score calculator.
- Chapter 3: 52 flashcards, 48 MCQs, 2 case sets (C4, C5). Bond calculator and futures fair value calculator.
- Chapter 4: 41 flashcards, 34 MCQs, 2 case sets (C6, C7).
- Chapter 5: 43 flashcards, 39 MCQs, 2 case sets (C8, C9). Includes one two-option true/false question from the book.
- Chapter 6: 60 flashcards, 49 MCQs, 2 case sets (C10, C11). Porter five forces and BCG matrix diagrams.

**The question bank .md files are not extra questions.** They are the same questions as each page's quiz, in a printable text form, for anyone who prefers paper or wants to discuss specific question numbers.

### Live site (GitHub Pages)

- Home: https://nism-study-group.github.io/nism-ra-kit/
- Orientation: https://nism-study-group.github.io/nism-ra-kit/Ch00-Orientation/Ch00-study-page.html
- Chapter 1: https://nism-study-group.github.io/nism-ra-kit/Ch01-Research-Analyst-Profession/Ch01-study-page.html
- Chapter 2: https://nism-study-group.github.io/nism-ra-kit/Ch02-Securities-Market/Ch02-study-page.html
- Chapter 3: https://nism-study-group.github.io/nism-ra-kit/Ch03-Equity-Debt-Terms/Ch03-study-page.html
- Chapter 4: https://nism-study-group.github.io/nism-ra-kit/Ch04-Fundamentals-of-Research/Ch04-study-page.html
- Chapter 5: https://nism-study-group.github.io/nism-ra-kit/Ch05-Economic-Analysis/Ch05-study-page.html
- Chapter 6: https://nism-study-group.github.io/nism-ra-kit/Ch06-Industry-Analysis/Ch06-study-page.html
- Add `#cards` or `#quiz` to any chapter link to open that tab directly.

Repo: https://github.com/nism-study-group/nism-ra-kit (public, owned by the free organization `nism-study-group`). The repo root is the folder that contains `NISM-RA-Study-Kit/`. A GitHub Actions workflow (`.github/workflows/pages.yml`) publishes `NISM-RA-Study-Kit/` on every push to `main`, leaving out `_build/` and `HANDOVER.md`. Commits use the author `nism-study-group <nism-study-group@users.noreply.github.com>` (set in the repo's local git config) so no personal email appears. The `.gitignore` excludes `source/`, `*.pdf`, `workbook*`, `_build/publish/`, `__pycache__/`, `*.zip`, `archive/`, `.venv/` and `.DS_Store`.

### How to publish a new chapter

1. Build: `cd NISM-RA-Study-Kit/_build && ../../.venv/bin/python build.py` (Playwright lives in a local `.venv` in the repo root, because Homebrew Python blocks global installs).
2. Export: `../../.venv/bin/python export.py`.
3. Run the checks in section 6 and the dash check in section 9.
4. From the repo root: `git status` (confirm no PDF or `source/` file is listed), then `git add -A && git commit -m "Add Chapter N" && git push`.
5. Wait about a minute for the workflow (`gh run watch -R nism-study-group/nism-ra-kit`), then open the new chapter link on the live site. Chapter links follow the pattern `.../ChNN-Folder/ChNN-study-page.html` and never change.

### Legacy links (claude.ai artifacts, private until shared, no longer updated)

- Chapter 1: https://claude.ai/artifact/FNDndyPJmsvp7vAA5yk5hb
- Chapter 2: https://claude.ai/artifact/AU4XTLZLJr6VFd7TrqqkwM

---

## 6. How the build works

Requirements: Python 3. For PNG export, Playwright in a local venv (one time, from the repo root): `python3 -m venv .venv && .venv/bin/pip install playwright && .venv/bin/python -m playwright install chromium`.

```
cd NISM-RA-Study-Kit/_build
../../.venv/bin/python build.py     # writes all pages, index.html, question banks, README, publish/ copies
../../.venv/bin/python export.py    # writes visuals/*.png for each chapter (needs playwright)
```

Paths are relative: `build.py` writes into the parent folder of `_build`.

### Content data format (per chapter)

```python
CARDS = [{"f": "front html", "b": "back html"}, ...]
MCQS  = [{"id": "3.1", "q": "question", "o": ["a","b","c","d"], "a": 0, "w": "why the answer is right"}, ...]
CASES = [{"id": "C4", "title": "...", "text": "scenario", "qs": [ {q, o, a, w}, ... 4 items ]}, ...]
DATA  = {"id": "ch03", "short": "Ch3", "title": "Chapter 3: ...", "cards": CARDS, "mcqs": MCQS, "cases": CASES}
```

- `a` is the index of the correct option **as written**. `build.py` then shuffles options with **balanced answer placement** (each letter correct about equally often; MCQs and case questions are balanced separately). Any option containing "above" ("All of the above", "None of the above") stays last. Write questions in any order; do not hand-balance.
- `w` should say why the right answer is right and, where useful, why a tempting wrong option is wrong.
- Case set IDs run across the whole kit: C0 (orientation), C1 (Ch1), C2 and C3 (Ch2), C4 and C5 (Ch3), C6 and C7 (Ch4), C8 and C9 (Ch5), C10 and C11 (Ch6). Chapter 7 should start at C12.
- New chapters go at the **end** of the `CH` dict: each chapter's shuffle seed comes from its position.

### The page engine (template.py)

- `page(data, learn_html, widgets_js="", home=True)` returns one self-contained HTML file.
- Three tabs: Learn, Flashcards, Quiz. URL hash `#learn`, `#cards`, `#quiz` opens a tab directly.
- **Flashcards:** flip on tap, "Got it" or "Again", progress bar, shuffle, "only cards I missed", clear progress. Keyboard: space flips, arrows mark.
- **Quiz:** sets (Quick 10 random, all MCQs, case sets only, everything, only previously missed). Modes: practice (answer after each) or exam (all at the end). Skip allowed. Result shows correct, wrong, skipped, net score (correct minus 0.25 x wrong), pass or fail against 60%, penalty lost, and review of every missed question.
- **"Copy result for the group"** button copies a one-line summary with missed question IDs, for pasting into WhatsApp. This replaced a live shared scoreboard, which would need every member to have a Claude account.
- Progress is saved in `localStorage` under keys `nismra:<chapterId>:...`, wrapped in try/catch. Theme choice under `nismra:theme`.
- Light and dark themes (follows the system, with a toggle). Responsive down to phone width.
- Interactive widgets: put JS in a string that defines `window.__WIDGETS__ = function(){...}`; the engine calls it after load.

### Adding a chapter (the recipe)

1. Read the chapter fully from the workbook, including its sample questions at the end.
2. Create `_build/chNN.py` (or split into `chNN_learn.py` and `chNN_qs.py` if long) with `LEARN`, `CARDS`, `MCQS`, `CASES`, and optionally `WIDGETS`.
3. In `build.py`: import it and add a `"chNN"` entry at the end of the `CH` dict (`dir`, `file`, `data`, `learn`, `widgets`, `title`, `n`, optional `extra` text for the home card). The home page card and weight-chart link are generated from `CH`. In `export.py`, add the folder to `chs`, and add any widget figure ids to the skip list.
4. Run `build.py`, then `export.py`.
5. Check: no JS errors, no horizontal scroll at 390 px width, dark mode readable, quiz runs end to end, answer spread is balanced (printed by build.py), and the dash check passes.
6. Publish (section 5).

---

## 7. Content conventions for the LEARN html

Structure every chapter page the same way:

1. **Hero:** "Chapter N of 15", title, pills (marks, book pages, reading time), then a one-line summary of the whole chapter in large type with 2 or 3 key terms highlighted.
2. **Chapter map** (`figure#fig-map` with `.map` links to each section).
3. **One `<section class="sec" id="sN">` per book section**, following the book's numbering (2.1, 2.2 ...). Do not reorder the book; the group reads linearly.
4. **Exam traps** section (`ol.traplist`), a consolidated list of everything testable and easy to confuse.
5. **For the group discussion** section: 4 or 5 prompts.
6. Footer: "Notes built from the NISM Series XV workbook (February 2026 version). Study aid only."

CSS building blocks (all in template.py):

| Class | Use |
|---|---|
| `.col` | Narrow reading column (about 720 px) for prose |
| `span.k` | Key term, drawn as a yellow highlighter mark |
| `.why` | Blue callout: the logic behind a rule, "why this exists" |
| `.analogy` | Dashed box, auto-labelled "Think of it like this". Do not start the text with "Think of..." |
| `.trap` | Red box, auto-labelled "Exam trap" |
| `.num` | Red bold for numbers worth memorising (dates, percentages) |
| `figure.fig` + `figcaption` (with optional `<span>` subtitle) | Every visual. Give each a unique `id="fig-..."`; export.py uses it for the PNG name |
| `.flow > .step + .arrow` | Process flowchart; turns vertical on phones. `.step.hl/.gd/.bd` = highlight, good, bad |
| `.grid.g2/.g3/.g4 > .box` | Card grids; `.box .tag` for a small label |
| `table.cmp` inside `.scroll` | Comparison tables (scroll sideways on phones) |
| `.stack` | Horizontal proportion bar (for example IPO allocation) |
| `.tl > .tl-i` | Three-point timeline |
| `dl.terms` | Definition list, if needed |

Rules learned the hard way:
- Prefer HTML and CSS diagrams over hand-drawn SVG. An SVG timeline with text labels overlapped badly and had to be replaced. SVG is fine for charts drawn by code (like the option payoff).
- Use CSS variables for every colour so dark mode works. Text on coloured bars uses `var(--card)`, not white.
- Only state what the book says. An earlier draft added a "how each analyst is paid" row the book never mentions; it was removed. Analogies and "why" lines are allowed as teaching aids, but facts must come from the book.
- **Follow the book even where current law differs**, since the exam marks against the book. Example: the book says private placement is capped at 50 investors, so the notes say "as per the book". Where the book looks outdated or ambiguous, add at most a short neutral note and do not build quiz questions on the ambiguous point (the anchor investor pricing sentence in 2.3 was left out of the quiz for this reason).
- Flag look-alike terms. Example: "FPO" means both Follow-on Public Offer and Farmer Producer Organisation in Chapter 2.

## 8. Question-writing conventions

- Match NISM style: "Which of the following...", "Which is NOT...", fill-in-the-blank with "______", "All of the above" options, and short scenario-based questions.
- Include the book's own sample questions from the end of each chapter.
- Distractors should be plausible and preferably drawn from the same chapter (other dates, other sections, other regulators).
- Case sets: a short realistic scenario (a named person or company), 4 questions, each testing a different point.
- Aim for roughly: flashcards covering every key term and number; MCQs covering every exam trap; 1 case set per chapter for light chapters, 2 or more for heavy ones. Heavy chapters (8, 10, 12, 14, 15) need numerical questions solvable with a spreadsheet.

## 9. Visual design tokens

- Fonts: Bricolage Grotesque (headings), Atkinson Hyperlegible (body), loaded from Google Fonts with system fallbacks.
- Light palette: paper `#F5F6F8`, card `#FFFFFF`, ink `#1B2340`, muted `#586178`, line `#D8DDE7`, indigo `#2E3F8F`, highlighter `#FFE27A`, teal (right) `#12705F`, brick (trap or wrong) `#A83C29`, sun `#F2B233`.
- Dark palette is defined in the same `:root` blocks in template.py.
- The one memorable element is the highlighter-pen key term. Keep everything else quiet.

### Dash check (run before every delivery)

```
grep -rl $'\xe2\x80\x94\|\xe2\x80\x93' NISM-RA-Study-Kit/ ; echo done
```

No file names should print.

---

## 10. Decisions already made (do not reopen unless the organiser asks)

- One web page per chapter holding notes, flashcards and quiz together.
- Folder per chapter, nested under one root folder, named `ChNN-Short-Title`.
- PNG exports of every diagram for sharing in the group chat.
- No live shared scoreboard; the copy-result button instead.
- Printable question bank per chapter, same questions as the quiz.

## 11. Suggested next steps

1. Chapter 7 (Company Analysis: Business and Governance, 6 marks).
2. Keep the linear pace, one chapter per meeting.
3. Later, once several chapters exist: a mixed mock test page drawing from all built chapters, weighted by the official marks, 80 MCQs plus 5 case sets, timed at 120 minutes.
4. Consider a small "formula sheet" page when reaching Chapters 8, 10 and 12.
