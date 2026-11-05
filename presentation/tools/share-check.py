#!/usr/bin/env python3
"""Check publication files for structural leftovers. Seeds are synthetic."""
import re
import sys
import tempfile
from pathlib import Path

RULES = [  # (name, regex, flags, seed)
    ("provenance mark", r"\[(T \d|P\]|Gemini|inferred)", 0, "[" + "T 0]"),
    ("Sources section", r"\bSources:", 0, "Source" + "s:"),
    ("email address", r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", 0, "person@" + "example.com"),
    ("at handle", r"@(?!(?:media|import|page|font-face|keyframes|supports|charset|namespace|layer|container|if)\b)[A-Za-z][A-Za-z0-9_-]{1,30}\b", 0, "@" + "example"),
    ("document-shaped id", r"\b1(?=[A-Za-z0-9_-]*[A-Z_])[A-Za-z0-9_-]{39,}\b", 0, "1" + "Ab" + "c" * 38),
    # Hyphenated names are words, not one opaque id. The published clone URL is such a name.
    ("mixed-case token", r"\b(?=[A-Za-z0-9_]*[A-Z])(?=[A-Za-z0-9_]*[a-z])(?=[A-Za-z0-9_]*\d)[A-Za-z0-9_]{12,}\b", 0, "Zz9" + "exampleToken"),
]


def scan(root, tracked=False):
    hits = []
    root = Path(root)
    if tracked:
        import subprocess
        paths = [root / p for p in subprocess.check_output(["git", "-C", str(root), "ls-files", "-z"], text=True).split("\0") if p]
    else:
        paths = root.rglob("*")
    for f in sorted(paths):
        if not f.is_file():
            continue
        rel = f.relative_to(root)
        if ".git" in rel.parts or "vendor" in rel.parts:
            continue
        data = f.read_bytes()
        if b"\0" in data[:8192]:
            continue
        t = data.decode("utf-8", errors="replace")
        for name, rx, fl, _ in RULES:
            for m in re.finditer(rx, t, fl):
                hits.append(f"{rel}: {name}: …{t[max(0, m.start() - 30):m.end() + 30]!r}…")
    return hits


if sys.argv[1:] == ["--self-test"]:
    with tempfile.TemporaryDirectory() as d:
        fired = []
        for name, rx, fl, seed in RULES:
            (Path(d) / "index.html").write_text(f"<p>clean text {seed} clean text</p>")
            fired.append((name, any(f": {name}:" in hit for hit in scan(d))))
        missed = [n for n, ok in fired if not ok]
        print(f"share-check self-test: {sum(ok for _, ok in fired)}/{len(fired)} rules fire on their seed"
              + (f"; MISSED: {missed}" if missed else ""))
        (Path(d) / "index.html").write_text("<p>clean text only</p>")
        clean = not scan(d)
        print(f"share-check self-test: clean sample passes: {clean}")
        (Path(d) / "NOTICE").write_text(RULES[0][3])
        suffixless = bool(scan(d))
        print(f"share-check self-test: suffixless seeded file detected: {suffixless}")
        sys.exit(0 if not missed and clean and suffixless else 1)
tracked = "--tracked" in sys.argv
root = [a for a in sys.argv[1:] if a != "--tracked"][0]
hits = scan(root, tracked=tracked)
for h in hits[:60]:
    print("share-check: FAIL", h)
print(f"share-check: {len(hits)} hit(s) in {root}" + (" — OK" if not hits else ""))
sys.exit(1 if hits else 0)
