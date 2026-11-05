#!/usr/bin/env python3
"""Inline deck/audio/manifest.json into a built reveal.js HTML file and attach the walkthrough plugin.

Chromium treats each file:// document as its own origin, so fetch('audio/manifest.json')
fails when the deck is opened by double-click. The plugin reads window.DECK_AUDIO instead.
Clip paths inside the manifest stay relative to the HTML file (deck/standalone.html).

Usage: inline-audio.py <deck.html> <manifest.json>
Rewrites the HTML in place. Safe to run again after a rebuild once the plugin tags are present;
the manifest script is replaced, the tags are not duplicated.
"""
import json
import re
import sys
from pathlib import Path

MARK = "deck-audio-manifest"
CSS = "vendor/walkthrough/plugin.css"
JS = "vendor/walkthrough/plugin.js"


def inline(html, manifest):
    blob = json.dumps(manifest, indent=2, sort_keys=False)
    script = f'<script id="{MARK}">window.DECK_AUDIO = {blob};</script>'
    html2, n = re.subn(
        rf'<script id="{MARK}">.*?</script>',
        lambda _: script,
        html,
        count=1,
        flags=re.S,
    )
    if n == 0:
        anchor = '<script src="vendor/reveal.js/dist/reveal.js"></script>'
        if anchor not in html2:
            raise SystemExit("inline-audio: reveal.js script tag not found")
        html2 = html2.replace(anchor, script + "\n" + anchor, 1)
    if f'href="{CSS}"' not in html2:
        link = f'<link rel="stylesheet" href="{CSS}" />'
        html2 = html2.replace("</head>", link + "\n</head>", 1)
    if f'src="{JS}"' not in html2:
        tag = f'<script src="{JS}"></script>'
        html2 = html2.replace(script, script + "\n" + tag, 1)
    if "RevealWalkthrough" not in html2:
        html2, n = re.subn(
            r"plugins\s*:\s*\[([^\]]*)\]",
            lambda m: "plugins: [" + m.group(1).rstrip().rstrip(",") + ", RevealWalkthrough]",
            html2,
            count=1,
        )
        if n != 1 or "RevealWalkthrough" not in html2:
            raise SystemExit("inline-audio: plugins array not found")
    return html2


def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: inline-audio.py <deck.html> <manifest.json>")
    html_path, manifest_path = Path(sys.argv[1]), Path(sys.argv[2])
    manifest = json.loads(manifest_path.read_text())
    if not isinstance(manifest, dict):
        raise SystemExit("inline-audio: manifest must be a JSON object")
    html_path.write_text(inline(html_path.read_text(), manifest))
    print(f"inline-audio: {len(manifest)} clips -> {html_path}")


if __name__ == "__main__":
    main()
