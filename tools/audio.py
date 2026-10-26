#!/usr/bin/env python3
"""Generate incremental offline narration using the bundled voice settings."""
import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import time
import urllib.request
import venv
import wave


def setup():
    cache = Path('.cache')
    cache.mkdir(exist_ok=True)
    if not (cache / 'venv/bin/python').exists():
        alternative = shutil.which('virtualenv')
        if alternative:
            subprocess.run([alternative, '--app-data', str(cache / 'environment-data'), str(cache / 'venv')], check=True)
        else:
            venv.EnvBuilder(with_pip=True).create(cache / 'venv')
    subprocess.run([str(cache / 'venv/bin/python'), '-m', 'pip', 'install', 'kokoro-onnx==0.6.1'], check=True)
    base = 'https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.1/'
    for variable, filename in [('KOKORO_MODEL', 'kokoro-v1.0.onnx'), ('KOKORO_VOICES', 'voices-v1.0.bin')]:
        dest = cache / filename
        supplied = os.environ.get(variable)
        if supplied:
            if Path(supplied).resolve() != dest.resolve():
                shutil.copyfile(supplied, dest)
        elif not dest.exists():
            # A failed download must not become a usable cache entry.
            temp = dest.with_suffix(dest.suffix + '.part')
            try:
                urllib.request.urlretrieve(base + filename, temp)
                temp.replace(dest)
            finally:
                temp.unlink(missing_ok=True)
    print('setup: voice environment ready')


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def write_changed(path, text):
    if not path.exists() or path.read_text() != text:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)


def narration(text):
    text = re.split(r'(?m)^[ \t]*\*\*More:\*\*[ \t]*$', text)[0]
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    text = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', text)
    text = re.sub(r'\[([^\]]+)\]\{[^}]*\}', r'\1', text)
    text = re.sub(r'[`*_]', '', text)
    return ' '.join(text.split())


def extract(markdown):
    slides, current, fence, notes, depth = {}, None, None, None, 0
    for line in markdown.splitlines():
        if notes is not None:
            if re.match(r'^\s*:::\s*$', line):
                if depth:
                    depth -= 1
                else:
                    if current is not None:
                        slides[current] = narration('\n'.join(notes))
                    notes = None
            else:
                if re.match(r'^\s*:::', line):
                    depth += 1
                notes.append(line)
            continue
        m = re.match(r'^\s*(`{3,}|~{3,})', line)
        if m:
            if fence and m[1][0] == fence[0] and len(m[1]) >= len(fence):
                fence = None
            elif not fence:
                fence = m[1]
            continue
        if fence:
            continue
        m = re.match(r'^(#{1,2})\s+.*?\{[^}]*#([^\s}]+)[^}]*\}\s*$', line)
        if re.match(r'^#{1,2}\s', line):
            current = None
            if m and m[1] == '#':
                current = m[2]
                if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*', current) or current in slides:
                    raise ValueError('Invalid or duplicate anchor')
                slides[current] = ''
        if re.match(r'^\s*:::\s*(?:notes|\{\.notes\})\s*$', line):
            notes, depth = [], 0
    if notes is not None:
        raise ValueError('Unclosed notes block')
    return slides


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('input', type=Path, nargs='?')
    p.add_argument('--setup', action='store_true')
    p.add_argument('--output', type=Path, default=Path('deck/audio'))
    p.add_argument('--model', default='.cache/kokoro-v1.0.onnx')
    p.add_argument('--voices', default='.cache/voices-v1.0.bin')
    p.add_argument('--strict', action='store_true')
    a = p.parse_args()
    if a.setup:
        setup()
        return
    if a.input is None:
        p.error('input required')
    start = time.monotonic()
    slides = extract(a.input.read_text())
    missing = [anchor for anchor, text in slides.items() if not text]
    if missing and a.strict:
        raise SystemExit('audio: missing narration: ' + ', '.join(missing))
    identity = {'engine': 'kokoro', 'model': hashlib.sha256(Path(a.model).read_bytes()).hexdigest(),
                'voices': hashlib.sha256(Path(a.voices).read_bytes()).hexdigest(),
                'voice': 'af_heart', 'version': importlib.metadata.version('kokoro-onnx'),
                'pipeline': 1, 'codec': 'libopus', 'loudness': 'I=-16:TP=-1.5:LRA=11'}
    a.output.mkdir(parents=True, exist_ok=True)
    cache_path = a.output / '.cache.json'
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}
    new_cache, manifest, generated, kokoro = {}, {}, 0, None
    pronunciation_data = None
    for anchor, text in slides.items():
        if not text:
            continue
        text += '\n'
        write_changed(a.output / 'text' / (anchor + '.txt'), text)
        text_hash = digest(text)
        key = digest(json.dumps([text_hash, identity], sort_keys=True))
        target = a.output / (anchor + '.ogg')
        if cache.get(anchor, {}).get('key') != key or not target.exists() or cache[anchor].get('audio_hash') != hashlib.sha256(target.read_bytes()).hexdigest():
            import numpy as np
            from kokoro_onnx import Kokoro
            from kokoro_onnx.config import EspeakConfig
            import espeakng_loader
            import onnxruntime as ort
            if kokoro is None:
                options = ort.SessionOptions()
                options.intra_op_num_threads = 4
                session = ort.InferenceSession(a.model, sess_options=options, providers=['CPUExecutionProvider'])
                # The pronunciation library has a fixed-size data-path buffer.
                # A short private copy also supports deeply nested checkouts.
                pronunciation_data = tempfile.TemporaryDirectory(prefix='voice-data-')
                short_data = Path(pronunciation_data.name) / 'data'
                shutil.copytree(espeakng_loader.get_data_path(), short_data)
                kokoro = Kokoro.from_session(session, a.voices,
                    espeak_config=EspeakConfig(data_path=str(short_data)))
            with tempfile.TemporaryDirectory(prefix='.tts-', dir=a.output) as tmp:
                wav, encoded = Path(tmp) / 'raw.wav', Path(tmp) / 'audio.ogg'
                samples, rate = kokoro.create(text.strip(), voice='af_heart', speed=1.0, lang='en-us')
                with wave.open(str(wav), 'wb') as dest:
                    dest.setnchannels(1)
                    dest.setsampwidth(2)
                    dest.setframerate(rate)
                    dest.writeframes((np.clip(samples, -1, 1) * 32767).astype('<i2').tobytes())
                subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', str(wav), '-af',
                                'loudnorm=I=-16:TP=-1.5:LRA=11', '-c:a', 'libopus', '-b:a', '48k', str(encoded)],
                               check=True, stdout=subprocess.DEVNULL)
                encoded.replace(target)
            generated += 1
            print('audio: generated ' + anchor, flush=True)
        duration = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                         '-of', 'default=noprint_wrappers=1:nokey=1', str(target)], text=True))
        manifest[anchor] = {'file': 'audio/' + target.name, 'duration': duration, 'text_hash': text_hash}
        new_cache[anchor] = {'key': key, 'audio_hash': hashlib.sha256(target.read_bytes()).hexdigest()}
    write_changed(a.output / 'manifest.json', json.dumps(manifest, indent=2) + '\n')
    write_changed(cache_path, json.dumps(new_cache, indent=2) + '\n')
    if pronunciation_data is not None:
        pronunciation_data.cleanup()
    print(f'audio: {generated} generated, {len(manifest) - generated} cached, {len(missing)} missing; {time.monotonic() - start:.2f}s')


if __name__ == '__main__':
    main()
