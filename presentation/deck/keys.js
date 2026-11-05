(function () {
  var dirs = {
    ArrowLeft: "left",
    ArrowRight: "right",
    ArrowUp: "up",
    ArrowDown: "down",
  };

  document.addEventListener(
    "keydown",
    function (event) {
      if (event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
      if (!Reveal.isReady || !Reveal.isReady()) return;
      var typing = document.activeElement && /^(input|textarea)$/i.test(document.activeElement.tagName);
      if (typing) return;

      if (event.key === " " || event.code === "Space") {
        var slide = Reveal.getCurrentSlide();
        if (slide && slide.querySelector(".fragment")) {
          event.preventDefault();
          event.stopImmediatePropagation();
          Reveal.nextFragment();
        }
        return;
      }

      var name = dirs[event.key];
      if (!name) return;
      event.preventDefault();
      event.stopImmediatePropagation();
      Reveal[name]({ skipFragments: true });
    },
    true
  );
})();
