(function () {
  var STORAGE_KEY = "cadbim_cookie_consent";
  var GA_ID = "G-CADBIM2026";

  function getConsent() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : null;
    } catch (e) {
      return null;
    }
  }

  function setConsent(analytics) {
    try {
      localStorage.setItem(
        STORAGE_KEY,
        JSON.stringify({ analytics: analytics, ts: Date.now() })
      );
    } catch (e) {}
  }

  function loadGA() {
    if (window.__gaLoaded) return;
    window.__gaLoaded = true;
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA_ID;
    document.head.appendChild(s);
    window.gtag("js", new Date());
    window.gtag("config", GA_ID);
  }

  function removeBanner() {
    var el = document.getElementById("cc-banner");
    if (el) el.remove();
    var pref = document.getElementById("cc-prefs");
    if (pref) pref.remove();
  }

  function buildBanner() {
    var wrap = document.createElement("div");
    wrap.id = "cc-banner";
    wrap.setAttribute(
      "style",
      "position:fixed;left:0;right:0;bottom:0;z-index:9999;background:#0a1225;" +
      "border-top:1px solid rgba(255,255,255,0.1);padding:18px 24px;" +
      "display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px;" +
      "font-family:'Manrope',sans-serif;box-shadow:0 -8px 30px rgba(0,0,0,0.35);"
    );
    wrap.innerHTML =
      '<div style="flex:1;min-width:240px;font-size:13px;line-height:1.6;color:rgba(255,255,255,0.7);">' +
      "Bu sitede deneyiminizi iyileştirmek ve site kullanımını analiz etmek için çerezler kullanıyoruz. " +
      '<a href="cadbim_kvkk_cerez_politikasi.html" style="color:#00c8f0;text-decoration:none;">Çerez Politikası</a>' +
      '</div><div style="display:flex;gap:10px;flex-wrap:wrap;">' +
      '<button id="cc-manage" style="background:transparent;color:rgba(255,255,255,0.7);border:.5px solid rgba(255,255,255,0.25);padding:10px 18px;border-radius:8px;font-size:13px;cursor:pointer;font-family:inherit;">Tercihleri Yönet</button>' +
      '<button id="cc-reject" style="background:transparent;color:rgba(255,255,255,0.7);border:.5px solid rgba(255,255,255,0.25);padding:10px 18px;border-radius:8px;font-size:13px;cursor:pointer;font-family:inherit;">Reddet</button>' +
      '<button id="cc-accept" style="background:#00c8f0;color:#060c1a;border:none;padding:10px 20px;border-radius:8px;font-size:13px;font-weight:700;cursor:pointer;font-family:inherit;">Kabul Et</button>' +
      "</div>";
    document.body.appendChild(wrap);

    document.getElementById("cc-accept").onclick = function () {
      setConsent(true);
      removeBanner();
      loadGA();
    };
    document.getElementById("cc-reject").onclick = function () {
      setConsent(false);
      removeBanner();
    };
    document.getElementById("cc-manage").onclick = function () {
      removeBanner();
      buildPrefsPanel();
    };
  }

  function buildPrefsPanel() {
    var overlay = document.createElement("div");
    overlay.id = "cc-prefs";
    overlay.setAttribute(
      "style",
      "position:fixed;inset:0;z-index:9999;background:rgba(6,12,26,0.75);" +
      "display:flex;align-items:center;justify-content:center;padding:20px;font-family:'Manrope',sans-serif;"
    );
    overlay.innerHTML =
      '<div style="background:#0a1225;border:1px solid rgba(255,255,255,0.1);border-radius:16px;max-width:460px;width:100%;padding:28px;">' +
      '<h3 style="color:#fff;font-size:17px;font-weight:700;margin:0 0 10px;">Çerez Tercihleri</h3>' +
      '<p style="color:rgba(255,255,255,0.6);font-size:13px;line-height:1.6;margin:0 0 20px;">Zorunlu çerezler sitenin çalışması için gereklidir ve kapatılamaz. Diğer kategorileri kendiniz seçebilirsiniz.</p>' +
      '<div style="display:flex;justify-content:space-between;align-items:center;padding:12px 0;border-top:.5px solid rgba(255,255,255,0.08);">' +
      '<span style="font-size:13px;color:#fff;">Zorunlu Çerezler</span>' +
      '<span style="font-size:12px;color:rgba(255,255,255,0.4);">Her zaman aktif</span></div>' +
      '<div style="display:flex;justify-content:space-between;align-items:center;padding:12px 0;border-top:.5px solid rgba(255,255,255,0.08);border-bottom:.5px solid rgba(255,255,255,0.08);">' +
      '<span style="font-size:13px;color:#fff;">Analitik Çerezler (Google Analytics)</span>' +
      '<label style="position:relative;display:inline-block;width:40px;height:22px;">' +
      '<input id="cc-analytics-toggle" type="checkbox" checked style="opacity:0;width:0;height:0;">' +
      '<span id="cc-toggle-track" style="position:absolute;inset:0;background:rgba(255,255,255,0.2);border-radius:22px;transition:.2s;cursor:pointer;"></span>' +
      '<span id="cc-toggle-knob" style="position:absolute;left:3px;top:3px;width:16px;height:16px;background:#fff;border-radius:50%;transition:.2s;pointer-events:none;"></span>' +
      "</label></div>" +
      '<div style="display:flex;gap:10px;margin-top:22px;justify-content:flex-end;">' +
      '<button id="cc-prefs-cancel" style="background:transparent;color:rgba(255,255,255,0.6);border:.5px solid rgba(255,255,255,0.25);padding:10px 18px;border-radius:8px;font-size:13px;cursor:pointer;font-family:inherit;">Vazgeç</button>' +
      '<button id="cc-prefs-save" style="background:#00c8f0;color:#060c1a;border:none;padding:10px 20px;border-radius:8px;font-size:13px;font-weight:700;cursor:pointer;font-family:inherit;">Kaydet</button>' +
      "</div></div>";
    document.body.appendChild(overlay);

    var toggle = document.getElementById("cc-analytics-toggle");
    var track = document.getElementById("cc-toggle-track");
    var knob = document.getElementById("cc-toggle-knob");
    var existing = getConsent();
    if (existing) toggle.checked = !!existing.analytics;
    function syncToggleUI() {
      if (toggle.checked) {
        track.style.background = "#00c8f0";
        knob.style.left = "21px";
      } else {
        track.style.background = "rgba(255,255,255,0.2)";
        knob.style.left = "3px";
      }
    }
    track.onclick = function () {
      toggle.checked = !toggle.checked;
      syncToggleUI();
    };
    syncToggleUI();

    document.getElementById("cc-prefs-cancel").onclick = function () {
      overlay.remove();
      buildBanner();
    };
    document.getElementById("cc-prefs-save").onclick = function () {
      var analytics = toggle.checked;
      setConsent(analytics);
      overlay.remove();
      if (analytics) loadGA();
    };
  }

  window.openCookiePrefs = function () {
    removeBanner();
    buildPrefsPanel();
  };

  var consent = getConsent();
  if (consent && consent.analytics) {
    loadGA();
  } else if (!consent) {
    if (document.body) {
      buildBanner();
    } else {
      window.addEventListener("DOMContentLoaded", buildBanner);
    }
  }
})();
