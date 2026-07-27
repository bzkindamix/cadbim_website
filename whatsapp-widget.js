(function () {
  var PHONE = "905532426737";
  var MESSAGE = "Merhaba, bilgi almak istiyorum.";

  var btn = document.createElement("a");
  btn.href = "https://wa.me/" + PHONE + "?text=" + encodeURIComponent(MESSAGE);
  btn.target = "_blank";
  btn.rel = "noopener";
  btn.id = "wa-float-btn";
  btn.setAttribute("aria-label", "WhatsApp ile iletişime geçin");
  btn.style.cssText =
    "position:fixed;right:24px;bottom:24px;width:58px;height:58px;border-radius:50%;" +
    "background:#25D366;display:flex;align-items:center;justify-content:center;" +
    "box-shadow:0 6px 20px rgba(0,0,0,0.35);z-index:9998;transition:bottom .2s ease;";
  btn.innerHTML =
    '<svg viewBox="0 0 32 32" width="30" height="30" fill="#fff" aria-hidden="true">' +
    '<path d="M16.001 3C9.383 3 4 8.373 4 14.994c0 2.61.83 5.033 2.24 7.012L4.999 29l7.202-1.883a12.9 12.9 0 0 0 3.8.573h.001c6.618 0 12-5.373 12-11.995C28 8.373 22.619 3 16.001 3zm0 21.807a9.74 9.74 0 0 1-4.976-1.363l-.357-.213-4.274 1.119 1.142-4.168-.233-.372a9.75 9.75 0 0 1-1.5-5.196c0-5.395 4.397-9.789 9.804-9.789 5.406 0 9.803 4.394 9.803 9.79 0 5.396-4.397 9.192-9.409 9.192zm5.376-7.33c-.295-.148-1.744-.86-2.014-.958-.27-.099-.467-.148-.664.148-.197.295-.762.958-.934 1.155-.172.197-.344.222-.639.074-.295-.148-1.245-.459-2.372-1.464-.877-.782-1.469-1.748-1.641-2.043-.172-.295-.018-.454.13-.601.134-.133.295-.345.443-.517.148-.172.197-.295.295-.492.099-.197.05-.369-.025-.517-.074-.148-.664-1.6-.911-2.192-.24-.575-.484-.497-.664-.507-.172-.008-.369-.01-.566-.01a1.09 1.09 0 0 0-.787.369c-.27.295-1.032 1.009-1.032 2.462 0 1.453 1.057 2.858 1.205 3.055.148.197 2.081 3.18 5.045 4.457.705.304 1.255.486 1.684.622.708.225 1.352.193 1.86.117.567-.085 1.744-.713 1.99-1.401.246-.689.246-1.28.172-1.401-.074-.123-.27-.197-.566-.345z"/>' +
    "</svg>";

  function mount() {
    document.body.appendChild(btn);
    adjust();
    var obs = new MutationObserver(adjust);
    obs.observe(document.body, { childList: true });
    window.addEventListener("resize", adjust);
  }

  function adjust() {
    var banner = document.getElementById("cc-banner");
    if (banner) {
      var h = banner.getBoundingClientRect().height;
      btn.style.bottom = h + 16 + "px";
    } else {
      btn.style.bottom = "24px";
    }
  }

  if (document.body) {
    mount();
  } else {
    window.addEventListener("DOMContentLoaded", mount);
  }
})();
