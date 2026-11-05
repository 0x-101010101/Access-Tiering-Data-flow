# Maintainer notes

## Layout

`deck/standalone.html` is the built page. `deck/deck.css` is its stylesheet. `deck/audio/` holds the narration clips and `deck/audio/manifest.json`. `deck/vendor/` holds reveal.js, the fonts, and the walk-through plugin. `deck/standalone.pdf` is the page-per-slide PDF. `src/` holds the slides, `src/title.md`, and `src/ORDER` (a `## label` line names an overview group). `tools/` holds the build and check scripts.

`make` writes `build/` and refreshes `NARRATION-TRANSCRIPT.generated.md`. It does not rebuild the PDF. `make pdf` does, and it needs Chromium, which is optional for maintainers. `make setup` writes `.cache/`. `make audio` also writes `deck/audio/text/` and `deck/audio/.cache.json`. Those paths are gitignored.

## Dependencies

Tested with pandoc 3.1.3, Python 3.12.3, and ffmpeg 6.1.1 (the build uses both `ffmpeg` and `ffprobe`). Graphviz is optional. The diagrams in `src/` are already drawn, and `make` does not call it. Graphviz 2.43.0 was present during this test and was not used.

`make setup` creates `.cache/venv` (virtualenv if that program is on `PATH`, otherwise the standard-library virtual environment with pip) and installs `kokoro-onnx==0.6.1` from PyPI. It then downloads two files from `https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.1/` unless `KOKORO_MODEL` and `KOKORO_VOICES` already point at them:

| file | bytes |
| --- | ---: |
| `kokoro-v1.0.onnx` | 325532387 |
| `voices-v1.0.bin` | 28214398 |

The voice is Kokoro-82M, `af_heart`. Generation uses that ONNX package, loudness `I=-16:TP=-1.5:LRA=11`, and Opus at 48 kbit/s. The weights are not committed. See [NOTICE](NOTICE).

## Workflow

Edit `src/`, then:

```sh
make
make audio
make check
```

Commit the result, including `NARRATION-TRANSCRIPT.generated.md` and, when narration changed, the clips and `deck/audio/manifest.json`. Keep commits small. Keep history linear.

`make` rebuilds `deck/standalone.html` and rewrites the transcript. With pandoc 3.1.3, the page rebuild matches the committed `deck/standalone.html`. `make check` fails if the committed transcript does not match the sources and the manifest. It also checks publication text, links, and speaker notes.

`make audio` is incremental. A clip is regenerated when its spoken text or the voice settings change.

## Speaker notes

Each slide has one `::: notes` block. On a top-level slide the spoken paragraphs come first. A line that is exactly `**More:**` starts the detail, which is not narrated. Do not add a Sources section. A vertical slide has a short description and no More marker.

`make transcript` reads only the spoken part. Timestamps are cumulative from `deck/audio/manifest.json`. A missing or stale clip is timed at 150 words per minute and marked `(est.)`.

## Content rules

The audience is the people named on the title slide. Do not add names of other people, private conversation content, or internal ids or host names. `make check` runs the structural publication check.

## Licences

Third-party notices are in [NOTICE](NOTICE).

## Cloud speech

The committed audio was generated locally. No cloud account is needed.

A maintainer may add another speech engine. That needs their own account and an API token in the environment. Never commit the token. At the rates seen on 2026-10-19, regenerating the whole walk-through cost about $1 with MiniMax or ElevenLabs and about $0.25 with Chatterbox.

The voices compared during authoring (MiniMax, ElevenLabs, Chatterbox) and a speech-to-text check of the clips (Whisper) ran on [Replicate](https://replicate.com). To use Replicate: create an account, create an API token at <https://replicate.com/account/api-tokens>, and export it as `REPLICATE_API_TOKEN` in your shell (for example from a private, mode-0600 env file you source). Never commit it or pass it on a command line. The tools in this repo do not call Replicate; such an engine would be an addition.
