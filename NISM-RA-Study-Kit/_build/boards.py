# Builds a tldraw study board (ChNN-board.tldr) for every chapter, next to its study page.
# Needs network: the layout runs inside tldraw.com so tldraw measures every text box.
# Run:  ../../.venv/bin/python boards.py            (all chapters)
#       ../../.venv/bin/python boards.py ch07 ch08  (just these)
# Open: drag the .tldr file onto tldraw.com and choose "Open file".
import os, sys, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "lib"))
sys.path.insert(0, HERE)
import boardkit
from chapters import CH, WIDGET_FIGS

def spec_for(key, c):
    # A chapter may supply a hand-built board as chapters/<key>_board.py with a SPEC; otherwise convert its LEARN page.
    try:
        return importlib.import_module(f"chapters.{key}_board").SPEC
    except ModuleNotFoundError:
        return boardkit.learn_to_spec(c, WIDGET_FIGS)

if __name__ == "__main__":
    want = [a for a in sys.argv[1:] if not a.startswith("-")]
    shots = os.path.join(HERE, "publish", "board-shots") if "--shots" in sys.argv else None
    jobs = []
    for key, c in sorted(CH.items(), key=lambda kv: kv[1]["n"]):
        if want and key not in want: continue
        out = os.path.join(ROOT, c["dir"], c["dir"][:4] + "-board.tldr")
        jobs.append((spec_for(key, c), out))
    problems = boardkit.render(jobs, shots)
    print("boards built" if not problems else f"boards built, with {len(problems)} layout issues listed above")
