#!/usr/bin/env python3
"""Assemble editable slides while retaining their explicit identifiers."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
src = root / "src"
files = []
groups = {}
for line in (src / "ORDER").read_text().splitlines():
    line = line.strip()
    if not line or (line.startswith("#") and not line.startswith("## ")):
        continue
    if line.startswith("## "):
        groups[len(files)] = line[3:].strip()
        continue
    path = (src / line).resolve()
    if not path.is_relative_to(src.resolve()) or not path.is_file():
        raise SystemExit("Invalid slide entry")
    files.append(path)
parts = [p.read_text() for p in files]
head = re.compile(r"^# (.*?) \{([^}]+)\}$", re.M)
overview = next((s for s in parts if re.search(r"^# .*\{#overview(?: |\})", s, re.M)), None)
if overview is None:
    raise SystemExit("Missing overview")
rows = []
for n, part in enumerate(parts):
    match = head.search(part)
    if not match:
        raise SystemExit("Top slide needs an explicit identifier")
    title, attrs = match.groups()
    title = re.sub(r"<[^>]+>", "", title)
    anchor = re.search(r"(?:^|\s)#(\S+)", attrs)[1]
    if anchor == "overview":
        continue
    if n in groups:
        rows.append(f"- [{groups[n]}]{{.ovgroup}}")
    kind = next((v[1:] for v in attrs.split() if v in (".concept", ".case", ".closing", ".vision")), "slide")
    rows.append(f"- [{n + 2}]{{.ovnum}} [{kind}]{{.ovkind .{kind}}} [{title}](#{anchor})")
# The navigation list is regenerated; the overview heading and notes remain editable.
overview2, nsub = re.subn(r"::: \{\.overview-list\}\n.*?\n:::",
                          lambda _: "::: {.overview-list}\n" + "\n".join(rows) + "\n:::", overview, count=1, flags=re.S)
if nsub != 1:
    raise SystemExit("Missing overview navigation list")
parts[parts.index(overview)] = overview2

def protect_diagrams(text):
    """Keep pre-rendered diagrams byte-for-byte. Pandoc otherwise re-parses the SVG and reflows it."""
    def repl(match):
        body = match.group(0)
        if not body.endswith("\n"):
            body += "\n"
        return "```{=html}\n" + body + "```\n"
    return re.sub(r'<div class="diagram\b.*?</div>', repl, text, flags=re.S)

parts = [protect_diagrams(p) for p in parts]
out = root / "build" / "slides.md"
out.parent.mkdir(exist_ok=True)
out.write_text((src / "title.md").read_text().rstrip() + "\n\n" + "\n\n".join(s.rstrip() for s in parts) + "\n")
