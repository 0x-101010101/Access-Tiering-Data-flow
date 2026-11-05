.DEFAULT_GOAL := all
PYTHON ?= python3
VOICE_PYTHON := .cache/venv/bin/python
SOURCES := $(wildcard src/*.md) src/ORDER tools/assemble.py
PANDOC := pandoc -f markdown -t revealjs --slide-level=2 -s \
 --lua-filter=tools/marks.lua --css=deck.css \
 -V revealjs-url=vendor/reveal.js -V theme=white -V width=1280 -V height=720 \
 -V margin=0 -V hash=true -V history=true -V slideNumber="'h.v'" \
 -V showSlideNumber=all -V controlsTutorial=false -V transition=none \
 -V backgroundTransition=none -V center=false

CHROMIUM ?= $(shell command -v chromium chromium-browser google-chrome 2>/dev/null | head -1)

all: deck/standalone.html transcript

build/slides.md: $(SOURCES)
	$(PYTHON) tools/assemble.py

deck/standalone.html: build/slides.md deck/deck.css tools/inline-audio.py tools/marks.lua $(wildcard deck/audio/manifest.json)
	$(PANDOC) -o $@ build/slides.md
	$(PYTHON) -c "p='deck/standalone.html'; t=open(p).read(); t=t.replace('vendor/reveal.js/dist/plugin/notes.js','vendor/reveal.js/plugin/notes/notes.js').replace('vendor/reveal.js/dist/plugin/search.js','vendor/reveal.js/plugin/search/search.js').replace('vendor/reveal.js/dist/plugin/zoom.js','vendor/reveal.js/plugin/zoom/zoom.js').replace('<section id=\"title-slide\">','<section id=\"title-slide\" data-background-color=\"#000000\">',1); needle='      });\n    </script>'; t=t.replace(needle, needle+'\n    <script src=\"keys.js\"></script>', 1); open(p,'w').write(t)"
	@if [ -f deck/audio/manifest.json ]; then $(PYTHON) tools/inline-audio.py $@ deck/audio/manifest.json; fi

setup:
	$(PYTHON) tools/audio.py --setup

audio: build/slides.md
	$(VOICE_PYTHON) tools/audio.py build/slides.md --strict --output deck/audio
	$(MAKE) deck/standalone.html

transcript:
	$(PYTHON) tools/transcript.py

pdf: deck/standalone.pdf

deck/standalone.pdf: deck/standalone.html
	test -n "$(CHROMIUM)" || { echo "no chromium found"; exit 1; }
	$(CHROMIUM) --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
	  --virtual-time-budget=10000 --print-to-pdf=$(CURDIR)/$@ "file://$(CURDIR)/$<"

check: deck/standalone.html
	$(PYTHON) tools/transcript.py --check
	$(PYTHON) tools/share-check.py --self-test
	$(PYTHON) tools/share-check.py --tracked .
	$(PYTHON) tools/links.py deck/standalone.html
	$(PYTHON) tools/notes.py build/slides.md

clean:
	rm -rf build deck/standalone.html

.PHONY: all setup audio transcript pdf check clean
