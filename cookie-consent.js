(function () {
  var CBM_BASE = /\/post\//.test(window.location.pathname) ? "../" : "";
  var STORAGE_KEY = "cadbim_cookie_consent";
  var GA_ID = "G-DTTE7C82NB";
  var META_PIXEL_ID = "648741288903445";
  var LINKEDIN_PARTNER_ID = "516209";

  function getConsent() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : null;
    } catch (e) {
      return null;
    }
  }

  function setConsent(analytics, marketing) {
    try {
      localStorage.setItem(
        STORAGE_KEY,
        JSON.stringify({ analytics: analytics, marketing: marketing, ts: Date.now() })
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

  function loadMeta() {
    if (window.__metaLoaded) return;
    window.__metaLoaded = true;
    (function (f, b, e, v, n, t, s) {
      if (f.fbq) return;
      n = f.fbq = function () {
        n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments);
      };
      if (!f._fbq) f._fbq = n;
      n.push = n;
      n.loaded = true;
      n.version = "2.0";
      n.queue = [];
      t = b.createElement(e);
      t.async = true;
      t.src = v;
      s = b.getElementsByTagName(e)[0];
      s.parentNode.insertBefore(t, s);
    })(window, document, "script", "https://connect.facebook.net/en_US/fbevents.js");
    window.fbq("init", META_PIXEL_ID);
    window.fbq("track", "PageView");
  }

  function loadLinkedIn() {
    if (window.__linkedinLoaded) return;
    window.__linkedinLoaded = true;
    window._linkedin_partner_id = LINKEDIN_PARTNER_ID;
    window._linkedin_data_partner_ids = window._linkedin_data_partner_ids || [];
    window._linkedin_data_partner_ids.push(LINKEDIN_PARTNER_ID);
    if (!window.lintrk) {
      window.lintrk = function (a, b) {
        window.lintrk.q.push([a, b]);
      };
      window.lintrk.q = [];
    }
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://snap.licdn.com/li.lms-analytics/insight.min.js";
    document.getElementsByTagName("script")[0].parentNode.insertBefore(
      s,
      document.getElementsByTagName("script")[0]
    );
  }

  function removeBanner() {
    var el = document.getElementById("cc-banner");
    if (el) el.remove();
    var pref = document.getElementById("cc-prefs");
    if (pref) pref.remove();
  }

  function applyConsent(analytics, marketing) {
    setConsent(analytics, marketing);
    removeBanner();
    if (analytics) loadGA();
    if (marketing) {
      loadMeta();
      loadLinkedIn();
    }
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
      "Bu sitede deneyiminizi iyileştirmek, site kullanımını analiz etmek ve ilgi alanınıza uygun reklamlar sunmak için çerezler kullanıyoruz. " +
      '<a href="' + CBM_BASE + 'kvkk-cerez-politikasi" style="color:#00c8f0;text-decoration:none;">Çerez Politikası</a>' +
      '</div><div style="display:flex;gap:10px;flex-wrap:wrap;">' +
      '<button id="cc-manage" style="background:transparent;color:rgba(255,255,255,0.7);border:.5px solid rgba(255,255,255,0.25);padding:10px 18px;border-radius:8px;font-size:13px;cursor:pointer;font-family:inherit;">Tercihleri Yönet</button>' +
      '<button id="cc-reject" style="background:transparent;color:rgba(255,255,255,0.7);border:.5px solid rgba(255,255,255,0.25);padding:10px 18px;border-radius:8px;font-size:13px;cursor:pointer;font-family:inherit;">Reddet</button>' +
      '<button id="cc-accept" style="background:#00c8f0;color:#060c1a;border:none;padding:10px 20px;border-radius:8px;font-size:13px;font-weight:700;cursor:pointer;font-family:inherit;">Kabul Et</button>' +
      "</div>";
    document.body.appendChild(wrap);

    document.getElementById("cc-accept").onclick = function () {
      applyConsent(true, true);
    };
    document.getElementById("cc-reject").onclick = function () {
      applyConsent(false, false);
    };
    document.getElementById("cc-manage").onclick = function () {
      removeBanner();
      buildPrefsPanel();
    };
  }

  function toggleRow(id, label) {
    return (
      '<div style="display:flex;justify-content:space-between;align-items:center;padding:12px 0;border-top:.5px solid rgba(255,255,255,0.08);">' +
      '<span style="font-size:13px;color:#fff;">' + label + "</span>" +
      '<label style="position:relative;display:inline-block;width:40px;height:22px;">' +
      '<input id="' + id + '" type="checkbox" checked style="opacity:0;width:0;height:0;">' +
      '<span id="' + id + '-track" style="position:absolute;inset:0;background:rgba(255,255,255,0.2);border-radius:22px;transition:.2s;cursor:pointer;"></span>' +
      '<span id="' + id + '-knob" style="position:absolute;left:3px;top:3px;width:16px;height:16px;background:#fff;border-radius:50%;transition:.2s;pointer-events:none;"></span>' +
      "</label></div>"
    );
  }

  function wireToggle(id, existingValue) {
    var toggle = document.getElementById(id);
    var track = document.getElementById(id + "-track");
    var knob = document.getElementById(id + "-knob");
    if (existingValue !== undefined && existingValue !== null) {
      toggle.checked = !!existingValue;
    }
    function sync() {
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
      sync();
    };
    sync();
    return toggle;
  }

  function buildPrefsPanel() {
    var existing = getConsent();
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
      toggleRow("cc-analytics-toggle", "Analitik Çerezler (Google Analytics)") +
      toggleRow("cc-marketing-toggle", "Pazarlama Çerezleri (Meta Pixel, Google Ads, LinkedIn)") +
      '<div style="display:flex;gap:10px;margin-top:22px;justify-content:flex-end;">' +
      '<button id="cc-prefs-cancel" style="background:transparent;color:rgba(255,255,255,0.6);border:.5px solid rgba(255,255,255,0.25);padding:10px 18px;border-radius:8px;font-size:13px;cursor:pointer;font-family:inherit;">Vazgeç</button>' +
      '<button id="cc-prefs-save" style="background:#00c8f0;color:#060c1a;border:none;padding:10px 20px;border-radius:8px;font-size:13px;font-weight:700;cursor:pointer;font-family:inherit;">Kaydet</button>' +
      "</div></div>";
    document.body.appendChild(overlay);

    var analyticsToggle = wireToggle(
      "cc-analytics-toggle",
      existing ? existing.analytics : undefined
    );
    var marketingToggle = wireToggle(
      "cc-marketing-toggle",
      existing ? existing.marketing : undefined
    );

    document.getElementById("cc-prefs-cancel").onclick = function () {
      overlay.remove();
      buildBanner();
    };
    document.getElementById("cc-prefs-save").onclick = function () {
      overlay.remove();
      applyConsent(analyticsToggle.checked, marketingToggle.checked);
    };
  }

  window.openCookiePrefs = function () {
    removeBanner();
    buildPrefsPanel();
  };

  var consent = getConsent();
  if (consent) {
    if (consent.analytics) loadGA();
    if (consent.marketing) {
      loadMeta();
      loadLinkedIn();
    }
  } else {
    if (document.body) {
      buildBanner();
    } else {
      window.addEventListener("DOMContentLoaded", buildBanner);
    }
  }
})();
