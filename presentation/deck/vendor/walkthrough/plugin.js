/* Spoken walk-through for reveal.js 5.2.1.
   Plays the current horizontal slide's clip from window.DECK_AUDIO (preferred;
   file:// cannot fetch a sibling JSON) or, failing that, audio/manifest.json.
   Manifest shape is deck/audio/manifest.json: { "<anchor>": { "file", "duration", "text_hash" } }.
   "file" is relative to the deck HTML. When a clip ends, advance to the next
   horizontal slide at vertical index 0 (never down into a stack) and continue.
   Slides with no clip are skipped while playing. Stops on the last slide. */
(function () {
  "use strict";

  function manifestEntry(manifest, id) {
    if (!manifest || !id || !Object.prototype.hasOwnProperty.call(manifest, id)) return null;
    var entry = manifest[id];
    if (typeof entry === "string") return { file: entry };
    if (!entry || !entry.file) return null;
    return entry;
  }

  function topAnchor(deck) {
    var slides = deck.getHorizontalSlides();
    var outer = slides[deck.getIndices().h] || null;
    if (!outer) return "";
    if (outer.id) return outer.id;
    var first = outer.querySelector("section");
    return (first && first.id) || "";
  }

  window.RevealWalkthrough = {
    id: "walkthrough",
    init: function (deck) {
      var manifest = {};
      var audio = document.createElement("audio");
      audio.className = "walkthrough-audio";
      audio.preload = "auto";
      audio.setAttribute("playsinline", "");
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "walkthrough-btn";
      btn.textContent = "Play";
      btn.setAttribute("aria-label", "Play the spoken walk-through");
      btn.setAttribute("aria-pressed", "false");
      document.body.appendChild(audio);
      document.body.appendChild(btn);

      var state = "stopped"; // stopped | playing | paused
      var loaded = "";
      var suppress = false;

      function paint(next) {
        state = next;
        var on = next === "playing";
        btn.textContent = on ? "Pause" : "Play";
        btn.setAttribute("aria-pressed", on ? "true" : "false");
        btn.classList.toggle("is-playing", on);
      }

      function hasAny() {
        return Object.keys(manifest).some(function (id) { return manifestEntry(manifest, id); });
      }

      function applyManifest(data) {
        manifest = data && typeof data === "object" ? data : {};
        btn.disabled = !hasAny();
        btn.title = btn.disabled ? "No walk-through audio" : "Spoken walk-through";
      }

      /* Move to the next top-level slide. Returns false at the end of the deck. */
      function nextTop() {
        if (deck.isOverview && deck.isOverview()) return false;
        var h = deck.getIndices().h;
        if (h + 1 >= deck.getHorizontalSlides().length) return false;
        suppress = true;
        deck.slide(h + 1, 0);
        suppress = false;
        return true;
      }

      function playAnchor(id) {
        var entry = manifestEntry(manifest, id);
        if (!entry) return false;
        if (loaded === id && state === "paused" && audio.currentTime > 0 && !audio.ended) {
          audio.play().catch(function () { paint("stopped"); });
          paint("playing");
          return true;
        }
        loaded = id;
        audio.src = entry.file;
        audio.play().catch(function () { paint("stopped"); });
        paint("playing");
        return true;
      }

      /* Play this top slide, or skip forward through tops that have no clip. */
      function startHere() {
        var guard = 0;
        while (guard++ < 500) {
          if (playAnchor(topAnchor(deck))) return;
          if (!nextTop()) {
            paint("stopped");
            return;
          }
        }
        paint("stopped");
      }

      audio.addEventListener("ended", function () {
        if (state !== "playing") return;
        if (!nextTop()) {
          paint("stopped");
          return;
        }
        startHere();
      });

      audio.addEventListener("error", function () {
        if (!audio.src) return;
        btn.title = "Could not play this clip";
        paint("stopped");
      });

      deck.on("slidechanged", function () {
        if (suppress || state !== "playing") return;
        var id = topAnchor(deck);
        if (id === loaded && !audio.paused && !audio.ended) return;
        startHere();
      });

      btn.addEventListener("click", function () {
        if (btn.disabled) return;
        if (state === "playing") {
          audio.pause();
          paint("paused");
          return;
        }
        startHere();
      });

      if (window.DECK_AUDIO && typeof window.DECK_AUDIO === "object") {
        applyManifest(window.DECK_AUDIO);
        return Promise.resolve();
      }
      var opts = {};
      if (typeof AbortSignal !== "undefined" && AbortSignal.timeout) opts.signal = AbortSignal.timeout(3000);
      return fetch("audio/manifest.json", opts).then(function (res) {
        if (!res.ok) throw new Error(String(res.status));
        return res.json();
      }).then(applyManifest).catch(function () {
        applyManifest(null);
      });
    }
  };
})();
