(function () {
  function equalize() {
    document.querySelectorAll("#specs .grid").forEach(function (grid) {
      var cards = grid.querySelectorAll(":scope > .card");
      if (!cards.length) return;
      var rowGroups = [];
      cards.forEach(function (card) {
        var rows = card.querySelectorAll(".spec-row");
        rows.forEach(function (row, i) {
          row.style.minHeight = "0px";
          if (!rowGroups[i]) rowGroups[i] = [];
          rowGroups[i].push(row);
        });
      });
      rowGroups.forEach(function (rows) {
        var max = 0;
        rows.forEach(function (r) {
          max = Math.max(max, r.getBoundingClientRect().height);
        });
        rows.forEach(function (r) {
          r.style.minHeight = max + "px";
        });
      });
    });
  }

  var t;
  function debouncedEqualize() {
    clearTimeout(t);
    t = setTimeout(equalize, 120);
  }

  window.addEventListener("load", equalize);
  window.addEventListener("resize", debouncedEqualize);
  if (document.readyState === "complete") equalize();
})();
