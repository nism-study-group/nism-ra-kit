# Study boards for tldraw. Three parts:
#  1. A small vocabulary of board blocks (header, card, note, flow, grid, table, ...). board.js draws them.
#  2. learn_to_spec(): turns a chapter's LEARN html into a board spec, so boards carry exactly the
#     content of the web page and nothing new. A chapter can instead supply its own spec (ch02_board.py).
#  3. render(): opens tldraw.com in a headless browser, lets board.js lay the board out (tldraw itself
#     measures every text box), checks that no two shapes overlap, and saves a .tldr file.
# Markup inside board text: **bold**, ==highlight== (numbers and dates), _italic_, "- " bullets, \n new line.
import json, os, re, sys
from html.parser import HTMLParser

LIB = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- 1. vocabulary
def header(no, title, sub): return {"t": "header", "no": no, "title": title, "sub": sub}
def H(s): return {"t": "h", "text": s}
def P(s, **k): return {"t": "p", "text": s, **k}
def card(s, color="blue", **k): return {"t": "card", "text": s, "color": color, **k}
def note(kind, s, **k): return {"t": "note", "kind": kind, "text": s, **k}
def row(*items, widths=None, equal=True): return {"t": "row", "items": list(items), "widths": widths, "equal": equal}
def stack(*items): return {"t": "stack", "items": list(items)}
def grid(cols, *items, color="blue"): return {"t": "grid", "cols": cols, "items": list(items), "color": color}
def flow(*items, labels=None, back=None): return {"t": "flow", "items": list(items), "labels": labels, "back": back}
def table(cols, *rows): return {"t": "table", "cols": cols, "rows": list(rows)}
def bars(*rows, labelWidth=280): return {"t": "bars", "rows": list(rows), "labelWidth": labelWidth}
def seg(f, s, color, fill="solid"): return {"f": f, "text": s, "color": color, "fill": fill}
def box(s, color="blue", **k): return {"text": s, "color": color, **k}
# main content on the left, a column of sticky notes on the right
def side(main, *notes): return row(stack(*main) if isinstance(main, list) else main, stack(*notes), widths=[1, 260], equal=False)

STYLE = {"bodyFont": "sans", "bodySize": "m", "headFont": "draw", "noteFont": "draw", "dash": "draw", "noteWidth": 260}
LEGEND = [["trap", "A point the exam likes to twist"], ["analogy", "An everyday picture of the idea"],
          ["why", "WHY IT MATTERS\nThe reason behind a rule"], ["remember", "A number or date to learn. ==Highlighted== text means the same."]]
HINT = "Frames read top to bottom, then left to right. Zoom into one frame at a time."

def make_spec(slug, page_name, title, sub, oneline, frames, columns=5):
    return {"slug": slug, "pageName": page_name, "frameWidth": 1400, "columns": columns, "style": STYLE,
            "banner": {"title": title, "sub": sub, "oneline": oneline, "legend": LEGEND, "hint": HINT}, "frames": frames}

# ---------------------------------------------------------------- 2. LEARN html to board spec
VOID = {"br", "img", "input", "meta", "link", "hr", "wbr", "source", "col", "area", "base", "embed", "param", "track"}

class Node:
    def __init__(self, tag, attrs):
        self.tag, self.attrs, self.kids = tag, dict(attrs), []
    @property
    def cls(self): return set((self.attrs.get("class") or "").split())
    def els(self): return [k for k in self.kids if isinstance(k, Node)]

class Tree(HTMLParser):
    # Lenient tree builder: an end tag closes everything up to its matching open tag, so the
    # page's loose nesting (sections opened inside a .col div) still keeps document order.
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root", []); self.stack = [self.root]
    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs); self.stack[-1].kids.append(n)
        if tag not in VOID: self.stack.append(n)
    def handle_startendtag(self, tag, attrs): self.stack[-1].kids.append(Node(tag, attrs))
    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]; return
    def handle_data(self, d): self.stack[-1].kids.append(d)

def parse(html):
    t = Tree(); t.feed(html); return t.root

# Board-only wording, where the page refers to colour that the board does not use.
TEXT_SWAPS = {
    "Red text: the two commodities move opposite ways.": "Highlighted cells: the two commodities move opposite ways.",
    " Tap a chapter to open it.": "",
    "open the **Quiz** tab at the top of this page.": "open the **Quiz** tab on this session's web page.",
    "Try the calculator:": "Try the calculator on the web page:",
    "Below, green candles closed higher and red candles closed lower. The highlighted candles form the pattern.": "The drawn pattern diagrams are on this chapter's web page.",
    " Dashed lines are the trendlines drawn along the highs and lows.": " The drawn diagrams are on this chapter's web page.",
    "The lower line is support; the upper line is resistance. A break above resistance on volume is a breakout.": "A break above resistance on volume is a breakout.",
}

def _segs(n, mark=None):
    if isinstance(n, str): return [(n, mark)]
    if n.tag in ("style", "script", "svg", "input", "button", "select", "output"): return []
    if n.tag == "br": return [("\n", None)]
    m = mark
    if n.tag in ("b", "strong") or "k" in n.cls: m = mark or "b"
    if "num" in n.cls: m = "h"
    if n.tag in ("i", "em") and not mark: m = "i"
    out = []
    if n.tag == "sup": out.append(("^", mark))
    for k in n.kids: out += _segs(k, m)
    return out

def inline(n, plain=False):
    segs = _segs(n) if isinstance(n, Node) else [(n, None)]
    merged = []
    for t, m in segs:
        t = re.sub(r"[ \t\r\n]+", " ", t) if t != "\n" else t
        if merged and merged[-1][1] == m and t != "\n" and merged[-1][0] != "\n": merged[-1] = (merged[-1][0] + t, m)
        else: merged.append((t, m))
    out = ""
    for t, m in merged:
        if t == "\n": out += "\n"; continue
        if not m or plain or not t.strip(): out += t; continue
        lead, core, trail = re.match(r"^(\s*)(.*?)(\s*)$", t, re.S).groups()
        d = {"b": "**", "h": "==", "i": "_"}[m]
        out += f"{lead}{d}{core}{d}{trail}"
    out = "\n".join(re.sub(r" +", " ", l).strip() for l in out.split("\n"))
    out = re.sub(r"\*\*\s*\*\*", "", out)
    for k, v in TEXT_SWAPS.items(): out = out.replace(k, v)
    return out.strip()

def text_of(n): return inline(n, plain=True)

COLOR = {"gd": "green", "bd": "red", "hl": "violet"}
def color_of(n, default="blue"):
    for c, col in COLOR.items():
        if c in n.cls: return col
    return default

def lines_of(n):
    # Text of a box-like element, one line per child block: tag (italic), h4 (bold), p, lists.
    lines, buf = [], []
    def flush():
        if buf:
            s = inline_join(buf)
            if s: lines.append(s)
            buf.clear()
    for k in n.kids:
        if isinstance(k, str) or (k.tag in ("b", "strong", "i", "em", "a", "small", "sup", "sub") or (k.tag == "span" and not ({"tag", "big", "tl-t", "tl-d"} & k.cls))):
            buf.append(k); continue
        flush()
        if k.tag == "span" and "tag" in k.cls: lines.append("_" + text_of(k) + "_")
        elif k.tag == "span" and ({"big", "tl-t"} & k.cls): lines.append("**" + text_of(k) + "**")
        elif k.tag == "span" and "tl-d" in k.cls: pass
        elif k.tag in ("h3", "h4"): lines.append("**" + text_of(k) + "**")
        elif k.tag in ("ul", "ol"): lines += list_lines(k)
        elif k.tag in ("p", "div"):
            if "bigm" in k.cls: lines.append("**" + text_of(k) + "**")
            else:
                s = inline(k)
                if s: lines.append(s)
        else:
            s = inline(k)
            if s: lines.append(s)
    flush()
    return "\n".join(lines)

def inline_join(nodes):
    holder = Node("span", []); holder.kids = list(nodes); return inline(holder)

def list_lines(n):
    items = [k for k in n.els() if k.tag == "li"]
    if n.tag == "ol": return [f"{i}. {inline(li)}" for i, li in enumerate(items, 1)]
    return ["- " + inline(li) for li in items]

def table_block(t):
    rows = []
    for tr in [x for x in walk(t) if isinstance(x, Node) and x.tag == "tr"]:
        cells = [c for c in tr.els() if c.tag in ("th", "td")]
        r = []
        for c in cells:
            s = inline(c).replace("\n", " ")
            if "dn" in c.cls and s: s = "==" + s.replace("**", "").replace("==", "") + "=="
            r.append(s)
            span = int(c.attrs.get("colspan") or 1)
            r += [""] * (span - 1)
        rows.append(r)
    n = max(len(r) for r in rows)
    rows = [r + [""] * (n - len(r)) for r in rows]
    # header row and first column are drawn bold by board.js, so drop marks there
    rows = [[re.sub(r"\*\*|==", "", c) if (i == 0 or j == 0) else c for j, c in enumerate(r)] for i, r in enumerate(rows)]
    w = []
    for j in range(n):
        avg = sum(len(r[j]) for r in rows) / len(rows)
        w.append(round(min(3.0, max(0.8, avg / 22)), 2))
    return table(w, *rows)

def walk(n):
    yield n
    if isinstance(n, Node):
        for k in n.kids: yield from walk(k)

def box_items(container):
    return [b for b in container.els() if "box" in b.cls or "tl-i" in b.cls]

def block(n, ctx):
    """Board blocks for one element. ctx carries chapter info and the widget figure ids."""
    c = n.cls
    if n.tag in ("style", "script", "footer", "svg") or c & {"map", "meta", "btns", "calc", "kicker"}: return []
    if n.tag == "p":
        s = inline(n)
        if not s: return []
        return [P(s, color="grey")] if "ptr" in c else [P(s)]
    if n.tag == "h3": return [H(text_of(n))]
    if n.tag == "ol" and "traplist" in c: return [{"t": "notes", "kind": "trap", "cols": 4, "numbered": True, "items": [inline(li) for li in n.els() if li.tag == "li"]}]
    if n.tag == "ol" and "talk" in c: return [{"t": "notes", "kind": "discuss", "cols": 4, "numbered": True, "items": [inline(li) for li in n.els() if li.tag == "li"]}]
    if n.tag in ("ul", "ol"): return [P("\n".join(list_lines(n)))]
    if n.tag == "dl":
        dts = n.els(); lines = []
        for i, k in enumerate(dts):
            if k.tag == "dt":
                dd = dts[i + 1] if i + 1 < len(dts) and dts[i + 1].tag == "dd" else None
                lines.append(f"- **{text_of(k)}**: {inline(dd) if dd else ''}")
        return [card("\n".join(lines), "grey")]
    if n.tag == "details":
        summ = next((k for k in n.els() if k.tag == "summary"), None)
        rest = Node("div", []); rest.kids = [k for k in n.kids if k is not summ]
        head = "**" + text_of(summ) + "**" if summ else ""
        return [card((head + "\n" + lines_of(rest)).strip(), "blue", acc=True)]
    if n.tag == "table": return [table_block(n)]
    if n.tag == "figure":
        fid = n.attrs.get("id", "")
        if fid == "fig-map": return []
        cap = next((k for k in n.els() if k.tag == "figcaption"), None)
        title = sub = ""
        if cap:
            sp = next((k for k in cap.els() if k.tag == "span"), None)
            title = inline_join([k for k in cap.kids if k is not sp]).replace("**", "")
            sub = inline(sp) if sp else ""
        if fid in ctx["widgets"]:
            return [card(f"**Interactive tool on the web page: {title}**\n{sub}\nOpen this chapter's study page to try it.", "grey")]
        out = [H(title)] if title else []
        if sub: out.append(P(sub, color="grey"))
        inner = []
        rows = [x for x in walk(n) if isinstance(x, Node) and ({"wrow", "drow"} & x.cls)]
        pcts = [x for x in walk(n) if isinstance(x, Node) and "pct" in x.cls]
        if rows:  # orientation charts: chapter rows with a value
            dr = "drow" in rows[0].cls
            body = [["Ch", "Chapter", "Marks per 10 pages" if dr else "Marks"]]
            for r in rows:
                sp = r.els()
                small = next((x for x in sp[1].els() if x.tag == "small"), None)
                name = text_of(sp[1]) if not small else inline_join([k for k in sp[1].kids if k is not small]) + " (" + text_of(small) + ")"
                body.append([text_of(sp[0]), name, text_of(sp[-1])])
            inner.append(table([0.4, 3, 1], *body))
            inner += [b for k in n.els() if not ({"wrow", "drow"} & k.cls) and k.tag != "figcaption" for b in block(k, ctx)]
        elif pcts:
            body = [["Sector", "Share of demand"]] + [[text_of(p.els()[0]), text_of(p.els()[-1])] for p in pcts]
            inner.append(table([2, 1], *body))
            inner += [b for k in n.els() if "pct" not in k.cls and k.tag != "figcaption" for b in block(k, ctx)]
        else:
            for k in n.els():
                if k.tag != "figcaption": inner += block(k, ctx)
        return out + inner
    if n.tag == "div":
        if "why" in c or "analogy" in c or "trap" in c:
            kind = "why" if "why" in c else "analogy" if "analogy" in c else "trap"
            kids = list(n.kids)
            first = next((k for k in kids if isinstance(k, Node) or (isinstance(k, str) and k.strip())), None)
            if kind == "why" and isinstance(first, Node) and first.tag == "b":
                rest = inline_join(kids[kids.index(first) + 1:])
                return [note(kind, f"**{text_of(first)}**\n{rest}")]
            return [note(kind, inline(n))]
        if "formula" in c: return [card(inline(n), "violet")]
        if "flow" in c:
            steps = [s for s in n.els() if "step" in s.cls]
            items = [box(lines_of(s), color_of(s)) for s in steps]
            return [flow(*items)] if len(items) <= 5 else [grid(3, *[{"text": i["text"], "color": i["color"]} for i in items])]
        if "stack" in c:
            segs = []
            for d in n.els():
                st = d.attrs.get("style", "")
                m = re.search(r"flex:\s*([\d.]+)", st) or re.search(r"width:\s*([\d.]+)%", st)
                f = float(m.group(1)) if m else 1.0
                col = "violet" if ("indigo" in st or "s1" in d.cls) else "green" if ("teal" in st or "s2" in d.cls) else "grey"
                segs.append(seg(f, text_of(d), col))
            return [bars({"segs": segs})]
        boxes = box_items(n)
        if boxes:
            cols = 4 if "g4" in c else 3 if ("g3" in c or "porter" in c or "tl" in c) else 2
            items = [{"text": lines_of(b), "color": color_of(b)} for b in boxes]
            extra = [P(text_of(a), color="grey") for a in n.els() if "ax" in a.cls]
            return [grid(min(cols, len(items)), *items)] + extra
        if "box" in c: return [card(lines_of(n), color_of(n))]
        out = []
        for k in n.kids:
            if isinstance(k, Node): out += block(k, ctx)
            elif k.strip(): out.append(P(k.strip()))
        return out
    if n.tag in ("section", "header", "span", "h1", "h2"):
        return []
    out = []
    for k in n.els(): out += block(k, ctx)
    return out

def _pair_notes(blocks):
    # Sticky notes sit beside the block they follow, the way the hand-built boards do it.
    out = []
    for b in blocks:
        if b["t"] == "note" and out and out[-1]["t"] not in ("header", "h", "note"):
            prev = out.pop()
            if prev.get("_side"):
                prev["items"][1]["items"].append(b); out.append(prev)
            else:
                r = side(prev, b); r["_side"] = True; out.append(r)
        else:
            out.append(b)
    # notes left on their own (straight after a heading) go in a row
    res = []
    for b in out:
        if b["t"] == "note" and res and res[-1].get("_noterow"):
            res[-1]["items"].append(b)
        elif b["t"] == "note":
            r = row(b, equal=False); r["_noterow"] = True; res.append(r)
        else: res.append(b)
    # accordion cards (syllabus topics) side by side
    final = []
    for b in res:
        if b.get("acc") and final and final[-1].get("_accgrid"):
            final[-1]["items"].append({"text": b["text"], "color": b["color"]})
        elif b.get("acc"):
            g = grid(3, {"text": b["text"], "color": b["color"]}); g["_accgrid"] = True; final.append(g)
        else: final.append(b)
    def clean(o):
        if isinstance(o, dict): return {k: clean(v) for k, v in o.items() if not k.startswith("_") and k != "acc"}
        if isinstance(o, list): return [clean(v) for v in o]
        return o
    return [clean(b) for b in final]

def _chars(o):
    if isinstance(o, str): return len(o)
    if isinstance(o, dict): return sum(_chars(v) for k, v in o.items() if k in ("text", "items", "rows", "segs"))
    if isinstance(o, list): return sum(_chars(v) for v in o)
    return 0

def _split(f, limit=4000):
    # A long section becomes "part 1 of 2" frames, cut at subheadings into roughly equal shares,
    # like the hand-built boards. Size is measured in characters of text.
    head, body = f["blocks"][0], f["blocks"][1:]
    total = _chars(body)
    n = -(-total // limit)
    cuts = [i for i, b in enumerate(body) if b["t"] == "h" and i > 0]
    if total <= limit * 1.15 or n < 2 or not cuts: return [f]
    sizes = [_chars(b) for b in body]
    chosen, start = [], 0
    for k in range(1, n):
        goal = total * k / n
        best = min(cuts, key=lambda i: abs(sum(sizes[:i]) - goal))
        if best > start and best not in chosen: chosen.append(best); start = best
    bounds = [0] + sorted(chosen) + [len(body)]
    parts = [body[bounds[i]:bounds[i + 1]] for i in range(len(bounds) - 1)]
    if len(parts) == 1: return [f]
    out = []
    for i, part in enumerate(parts, 1):
        h = dict(head); h["sub"] = f"{head['sub']}  ·  Part {i} of {len(parts)}"
        out.append({"name": f"{f['name']} ({i} of {len(parts)})", "blocks": [h] + part})
    return out

def learn_to_spec(c, widgets):
    root = parse(c["learn"])
    ctx = {"widgets": widgets}
    hero = next(x for x in walk(root) if isinstance(x, Node) and x.tag == "header" and "hero" in x.cls)
    kicker = text_of(next(x for x in walk(hero) if isinstance(x, Node) and "kicker" in x.cls))
    h1 = text_of(next(x for x in walk(hero) if isinstance(x, Node) and x.tag == "h1"))
    pills = [text_of(x) for x in walk(hero) if isinstance(x, Node) and "pill" in x.cls]
    one = next((x for x in walk(hero) if isinstance(x, Node) and "oneline" in x.cls), None)
    n = c["n"]
    title = f"Chapter {n}: {h1}" if n else f"Session 0: {h1}"
    sub = "  ·  ".join(["NISM Series XV Research Analyst"] + pills + ["Notes from the February 2026 workbook. Study aid only."])
    oneline = text_of(one) if one else ""

    frames, cur = [], None
    def start(badge, name, heading, sub_):
        nonlocal cur
        cur = {"name": name, "blocks": [header(badge, heading, sub_)]}
        frames.append(cur)
    def visit(node):
        nonlocal cur
        for k in node.kids:
            if not isinstance(k, Node): continue
            if k is hero: continue
            if k.tag == "section" and "sec" in k.cls:
                secno = next((x for x in k.els() if "secno" in x.cls), None)
                h2 = next((x for x in k.els() if x.tag == "h2"), None)
                name = text_of(h2) if h2 else ""
                sid = k.attrs.get("id", "")
                if sid == "traps": start("!", name, name, "Read these the night before. Each one is a question waiting to happen")
                elif sid == "talk": start("?", name, name, "Pick one each. Argue it out")
                else:
                    no = text_of(secno) if secno else ""
                    start(no.split(" ")[0] or "*", f"{no} {name}".strip(), name, kicker)
                visit(k); continue
            if k.tag in ("div",) and ({"wrap", "col"} & k.cls): visit(k); continue
            bl = block(k, ctx)
            if bl:
                if cur is None: start("*", "Overview", "Overview", kicker)
                cur["blocks"] += bl
    visit(root)
    frames = [part for f in frames for part in _split(f)]
    for f in frames:
        f["blocks"] = [f["blocks"][0]] + _pair_notes(f["blocks"][1:])
    page_name = title
    return make_spec(c["data"]["id"], page_name, title, sub, oneline, frames)

# ---------------------------------------------------------------- 3. render
CHECK_JS = r"""(frameIds) => {
  const editor = window.editor, out = []
  for (const fid of frameIds) {
    const fb = editor.getShapePageBounds(fid)
    const kids = editor.getSortedChildIdsForParent(fid).map(id => editor.getShape(id)).filter(s => s.type !== 'arrow' && s.type !== 'line')
    const bs = kids.map(s => ({id: s.id, b: editor.getShapePageBounds(s.id)}))
    for (const k of bs) {
      if (k.b.minX < fb.minX - 1 || k.b.maxX > fb.maxX + 1 || k.b.minY < fb.minY - 1 || k.b.maxY > fb.maxY + 1) out.push(['outside', fid, k.id])
    }
    for (let i = 0; i < bs.length; i++) for (let j = i + 1; j < bs.length; j++) {
      const a = bs[i].b, b = bs[j].b
      const ox = Math.min(a.maxX, b.maxX) - Math.max(a.minX, b.minX), oy = Math.min(a.maxY, b.maxY) - Math.max(a.minY, b.minY)
      if (ox > 2 && oy > 2) out.push(['overlap', fid, bs[i].id, bs[j].id])
    }
  }
  return out
}"""

def check_dashes(o):
    s = json.dumps(o, ensure_ascii=False)
    bad = [ch for ch in ("–", "—") if ch in s]
    if bad: sys.exit("dash found in board text: " + " ".join(bad))

def render(specs_and_outs, shots_dir=None):
    """specs_and_outs: list of (spec, out_path). Renders all in one browser session. Returns problems found."""
    from playwright.sync_api import sync_playwright
    js = open(os.path.join(LIB, "board.js")).read()
    problems = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1600, "height": 1000})
        pg.goto("https://www.tldraw.com/", wait_until="networkidle", timeout=90000)
        pg.wait_for_function("() => !!window.editor", timeout=60000)
        for spec, out in specs_and_outs:
            check_dashes(spec)
            res = pg.evaluate(js, spec)
            issues = pg.evaluate(CHECK_JS, [f["id"] for f in res["frames"]])
            json.dump(res["tldr"], open(out, "w"), ensure_ascii=False)
            tall = max(f["h"] for f in res["frames"])
            print(f"{os.path.basename(out)}: {len(res['frames'])} frames in {res['columns']} columns, tallest {tall}px, layout issues: {len(issues)}")
            for i in issues[:10]: print("   ", i)
            problems += [(os.path.basename(out), i) for i in issues]
            if shots_dir:
                os.makedirs(shots_dir, exist_ok=True)
                for k, f in enumerate(res["frames"]):
                    pg.evaluate("(id) => { window.editor.zoomToBounds(window.editor.getShapePageBounds(id), {inset: 20}) }", f["id"])
                    pg.wait_for_timeout(300)
                    pg.screenshot(path=os.path.join(shots_dir, f"{spec['slug']}-{k:02d}.png"))
        b.close()
    return problems
