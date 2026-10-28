/* Click-to-copy for inline code: /navi and @commands automatically, anything else via `text`{ .copy }. */
(function () {
  var AUTO = /^(\/navi\s|@\w)/;
  var tip = null;
  var hideTimer = null;

  function decorate(root) {
    var nodes = root.querySelectorAll(".md-typeset code:not(.copyable)");
    for (var i = 0; i < nodes.length; i++) {
      var el = nodes[i];
      if (el.closest("pre, a, .highlight")) continue;
      if (!el.classList.contains("copy") && !AUTO.test(el.textContent.trim())) continue;
      el.classList.add("copyable");
      el.setAttribute("tabindex", "0");
      el.setAttribute("role", "button");
      el.setAttribute("title", "Click to copy");
      el.setAttribute("aria-label", "Copy " + el.textContent.trim());
    }
  }

  function legacyCopy(text) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.select();
    var ok = false;
    try { ok = document.execCommand("copy"); } catch (e) {}
    document.body.removeChild(ta);
    return ok ? Promise.resolve() : Promise.reject();
  }

  function write(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text).catch(function () { return legacyCopy(text); });
    }
    return legacyCopy(text);
  }

  function show(el, message) {
    if (!tip) {
      tip = document.createElement("div");
      tip.className = "copy-tip";
      tip.setAttribute("role", "status");
      document.body.appendChild(tip);
    }
    tip.textContent = message;
    var r = el.getBoundingClientRect();
    tip.style.left = r.left + r.width / 2 + window.scrollX + "px";
    tip.style.top = r.top + window.scrollY + "px";
    tip.classList.add("copy-tip--visible");
    clearTimeout(hideTimer);
    hideTimer = setTimeout(function () { tip.classList.remove("copy-tip--visible"); }, 1500);
  }

  function copy(el) {
    write(el.textContent.trim()).then(
      function () { show(el, "Copied"); },
      function () { show(el, "Copy failed"); }
    );
  }

  document.addEventListener("click", function (e) {
    var el = e.target.closest && e.target.closest("code.copyable");
    if (el) copy(el);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key !== "Enter" && e.key !== " ") return;
    var el = e.target.closest && e.target.closest("code.copyable");
    if (!el) return;
    e.preventDefault();
    copy(el);
  });

  if (window.document$) {
    window.document$.subscribe(function () { decorate(document); });
  } else {
    document.addEventListener("DOMContentLoaded", function () { decorate(document); });
  }
})();
