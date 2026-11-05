#!/usr/bin/env python3
"""Validate spoken scripts and detail descriptions."""
import re
import sys

MARK = re.compile(r"\[(T \d|D |Gemini|P\]|inferred|related)")


def split(block):
    """-> (script_or_desc, more, sources, marker_ok)"""
    ok = all(re.search(r"(^|\n\n)" + re.escape(m) + r"\n", block + "\n") for m in ("**More:**", "Source" + "s:") if m in block)
    head, _, src = block.partition("\nSource" + "s:")
    first, _, more = head.partition("\n**More:**")
    return first.strip(), more.strip(), src.strip(), ok


def sentences(t):
    return len(re.findall(r"[.!?](\s|$)", t))


text = open(sys.argv[1]).read()
fence, slides, cur = False, [], None
for line in text.splitlines():
    if line.startswith("```"):
        fence = not fence
    if not fence and re.match(r"^#{1,2} ", line):
        cur = [line, []]
        slides.append(cur)
    elif cur is not None:
        cur[1].append(line)
bad = words = tops = 0
for head, body in slides:
    top = head.startswith("# ")
    m = re.findall(r"::: notes\n(.*?)\n:::", "\n".join(body), re.S)
    why = ""
    if len(m) != 1:
        why = f"{len(m)} notes blocks (want 1)"
    else:
        first, more, src, ok = split(m[0])
        if not ok:
            why = "markers must stand on their own line after a blank line"
        elif top:
            tops += 1
            words += len(first.split())
            why = ("no SCRIPT" if not first else "provenance/brackets in SCRIPT" if MARK.search(first) or "[" in first else "")
        else:
            why = ("**More:** on a vertical slide" if more else "empty description" if not first else
                   "provenance in description" if MARK.search(first) else
                   f"{sentences(first)} sentences (want 2-4)" if not 2 <= sentences(first) <= 4 else "")
    if why:
        bad += 1
        print(f"notes: {head[:70]} :: {why}")
print(f"notes: {len(slides) - bad}/{len(slides)} slides OK (title exempt) · script: {tops} top slides, {words} words, "
      f"~{words / 150:.1f} min at 150 wpm")
sys.exit(1 if bad else 0)
