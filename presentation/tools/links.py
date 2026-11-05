#!/usr/bin/env python3
"""Report internal links (#/id) in a built deck that point at no slide. Usage: links.py DECK.html"""
import re
import sys

h = open(sys.argv[1]).read()
ids = set(re.findall(r'id="([^"]+)"', h))
broken = sorted(set(re.findall(r'href="#/([^"]+)"', h)) - ids)
print("links: " + ("OK" if not broken else "BROKEN " + " ".join(broken)))
sys.exit(1 if broken else 0)
