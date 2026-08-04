/* Yaklasan webinar cekmecesi — ekranin SAG kenarinda, sosyal medya rayinin aynasi.
 *
 * Veri KOPYALANMAZ: kartlar cadbim_webinar.html'den okunur (tek dogru kaynak).
 * Boylece webinar takvimi guncellendiginde widget kendiliginden guncel kalir.
 * Istek, sayfa yuklendikten sonra bosta yapilir; sayfa acilisini yavaslatmaz.
 *
 * Davranis: kapaliyken sag kenara gomulu bir sekme (en yakin webinarin tarihi)
 * durur; acildiginda kart disari kayar. Ileri/geri oklariyla siradaki
 * webinarlar gezilir. Veri gelmezse veya yaklasan webinar yoksa hic gorunmez.
 */
(function () {
  "use strict";

  /* Webinar sayfasinin kendisinde gereksiz — sayfa zaten tum listeyi gosteriyor. */
  if (document.querySelector(".wcard")) return;

  var AY = { oca:0, "şub":1, sub:1, mar:2, nis:3, may:4, haz:5, tem:6,
             "ağu":7, agu:7, eyl:8, eki:9, kas:10, ara:11 };
  var AY_UZUN = ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran",
                 "Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"];

  /* Webinar sayfasinin adresi bu script'in kendi src'sine gore cozulur;
     alt klasorlerdeki (post/) sayfalarda da dogru hedefi verir. */
  var self = document.currentScript && document.currentScript.src;
  if (!self) {
    var tags = document.getElementsByTagName("script");
    for (var i = tags.length - 1; i >= 0; i--) {
      if (tags[i].src && tags[i].src.indexOf("webinar-widget.js") > -1) { self = tags[i].src; break; }
    }
  }
  if (!self) return;
  var LISTE = new URL("webinar", self).href;
  /* Iki barindirma bicimi var, ikisi de denenir:
       - canli site (.htaccess): /webinar calisir, /cadbim_webinar.html 400 verir
       - GitHub Pages / yerel:   /cadbim_webinar.html calisir, temiz URL 404'e duser
     Sirayla denenip icinde gercekten webinar karti olan yanit kullanilir. */
  var KAYNAKLAR = [LISTE, new URL("cadbim_webinar.html", self).href];

  /* Gun+ay veriliyor, yil verilmiyor: tarihi bugune EN YAKIN yila oturt.
     Sonuc gecmiste de olabilir; eleme sonraki adimda yapilir.
     Onceki surum tarihi "ileriye donuk bir pencereye" oturtmaya calisiyordu;
     bu yuzden sayfada 30 gunden uzun sure duran gecmis bir kart, gelecek
     yilin tarihiymis gibi yeniden "yaklasan" listesine giriyordu. */
  function tariheCevir(gun, ayKisa) {
    var ay = AY[String(ayKisa).toLowerCase().trim()];
    if (ay === undefined) return null;
    var bugun = new Date(); bugun.setHours(0, 0, 0, 0);
    var en = null;
    for (var y = bugun.getFullYear() - 1; y <= bugun.getFullYear() + 1; y++) {
      var d = new Date(y, ay, gun);
      if (!en || Math.abs(d - bugun) < Math.abs(en - bugun)) en = d;
    }
    return en;
  }

  function metin(kok, sec) { var e = kok.querySelector(sec); return e ? e.textContent.trim() : ""; }

  function kartlariOku(html, kaynak) {
    var doc = new DOMParser().parseFromString(html, "text/html");
    var bugun = new Date(); bugun.setHours(0, 0, 0, 0);
    var liste = [];
    Array.prototype.forEach.call(doc.querySelectorAll(".wcard"), function (k) {
      var gun = metin(k, ".wdate-day"), ayk = metin(k, ".wdate-mon");
      var t = tariheCevir(parseInt(gun, 10), ayk);
      if (!t || t < bugun) return;                       /* gecmis webinarlar elenir */
      var img = k.querySelector(".wimg img");
      var btn = k.querySelector("a.wbtn");
      liste.push({
        tarih: t,
        gun: gun,
        ay: ayk,
        /* webinar sayfasindaki sektor filtresiyle ayni anahtar: aec | dm */
        kategori: k.getAttribute("data-cat") || "",
        ayUzun: AY_UZUN[t.getMonth()],
        etiket: metin(k, ".wtag"),
        saat: metin(k, ".wtime"),
        baslik: metin(k, "h3"),
        gorsel: img ? new URL(img.getAttribute("src"), kaynak).href : "",
        gorselAlt: img ? (img.getAttribute("alt") || "") : "",
        kayit: btn ? new URL(btn.getAttribute("href"), kaynak).href : LISTE
      });
    });
    liste.sort(function (a, b) { return a.tarih - b.tarih; });
    return liste;
  }

  var CSS =
    "#wb-rail{position:fixed;right:0;top:50%;transform:translateY(-50%);z-index:9989;" +
      "font-family:inherit;display:none;}" +
    "#wb-rail.wb-hazir{display:block;}" +

    /* --- kapali sekme: koyu cam yuzey + ustte cyan "takvim sirti" --- */
    "#wb-tab{position:absolute;right:0;top:50%;transform:translate(13px,-50%);" +
      "display:flex;flex-direction:column;align-items:center;width:56px;" +
      "padding:13px 7px 11px;overflow:hidden;cursor:pointer;color:#fff;" +
      "border:.5px solid rgba(0,200,240,.34);border-right:0;border-radius:13px 0 0 13px;" +
      "background:linear-gradient(180deg,#13294a 0%,#0d1830 62%);" +
      "box-shadow:-6px 0 20px rgba(0,0,0,.42),inset 0 1px 0 rgba(255,255,255,.06);" +
      "transition:transform .28s cubic-bezier(.2,.7,.3,1.25),box-shadow .25s,border-color .25s;}" +
    /* ustteki cyan serit — takvim yapragi hissi */
    "#wb-tab::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;" +
      "background:linear-gradient(90deg,#00c8f0,#4de3ff);}" +
    /* ic parlama; hover'da guclenir */
    "#wb-tab::after{content:'';position:absolute;inset:0;pointer-events:none;opacity:0;" +
      "background:radial-gradient(ellipse 90% 55% at 50% 0%,rgba(0,200,240,.28),transparent 70%);" +
      "transition:opacity .25s;}" +
    "#wb-rail:hover #wb-tab,#wb-tab:focus-visible{transform:translate(0,-50%);" +
      "border-color:rgba(0,200,240,.72);" +
      "box-shadow:-8px 0 28px rgba(0,0,0,.5),0 0 0 1px rgba(0,200,240,.22)," +
        "inset 0 1px 0 rgba(255,255,255,.09);}" +
    "#wb-rail:hover #wb-tab::after,#wb-tab:focus-visible::after{opacity:1;}" +
    "#wb-tab .wb-t-gun{position:relative;font-size:21px;font-weight:800;line-height:1;" +
      "letter-spacing:-.6px;font-family:'Manrope',inherit;}" +
    "#wb-tab .wb-t-ay{position:relative;margin-top:3px;font-size:10px;font-weight:800;line-height:1;" +
      "text-transform:uppercase;letter-spacing:.8px;color:#00c8f0;}" +
    "#wb-tab .wb-t-cizgi{position:relative;width:20px;height:1px;margin:8px 0 7px;" +
      "background:rgba(255,255,255,.16);}" +
    "#wb-tab .wb-t-et{position:relative;font-size:8px;font-weight:700;letter-spacing:1.1px;" +
      "color:rgba(255,255,255,.5);}" +
    "#wb-rail.wb-acik #wb-tab{transform:translate(66px,-50%);opacity:0;pointer-events:none;}" +

    /* --- acilan kart --- */
    "#wb-panel{position:absolute;right:0;top:50%;transform:translate(calc(100% + 14px),-50%);" +
      "width:302px;max-width:calc(100vw - 26px);max-height:calc(100vh - 170px);overflow:auto;" +
      "background:#0d1830;border:.5px solid rgba(255,255,255,.13);border-right:0;" +
      "border-radius:14px 0 0 14px;box-shadow:-10px 0 34px rgba(0,0,0,.5);" +
      "opacity:0;pointer-events:none;transition:transform .3s cubic-bezier(.2,.7,.3,1),opacity .22s;}" +
    "#wb-rail.wb-acik #wb-panel{transform:translate(0,-50%);opacity:1;pointer-events:auto;}" +

    "#wb-bas{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:11px 12px 9px 14px;" +
      "border-bottom:.5px solid rgba(255,255,255,.09);}" +
    "#wb-bas span{font-size:10px;font-weight:700;letter-spacing:1.7px;text-transform:uppercase;color:#00c8f0;}" +
    "#wb-kapat{width:26px;height:26px;flex-shrink:0;border:0;border-radius:7px;cursor:pointer;" +
      "background:rgba(255,255,255,.07);color:rgba(255,255,255,.66);font-size:15px;line-height:1;" +
      "display:flex;align-items:center;justify-content:center;transition:background .2s,color .2s;}" +
    "#wb-kapat:hover{background:rgba(255,255,255,.14);color:#fff;}" +

    /* --- sektor suzgeci (webinar sayfasindaki AEC / D&M ayrimiyla ayni) --- */
    "#wb-filtre{display:flex;gap:6px;padding:10px 14px 11px;}" +
    ".wb-fc{flex:1;padding:6px 4px;border-radius:8px;cursor:pointer;font-family:inherit;" +
      "font-size:11px;font-weight:700;letter-spacing:.2px;" +
      "border:.5px solid rgba(255,255,255,.13);background:rgba(255,255,255,.04);" +
      "color:rgba(255,255,255,.56);transition:border-color .2s,background .2s,color .2s;}" +
    ".wb-fc:hover{border-color:rgba(255,255,255,.28);color:rgba(255,255,255,.86);}" +
    ".wb-fc[aria-pressed='true']{background:rgba(0,200,240,.14);" +
      "border-color:rgba(0,200,240,.46);color:#00c8f0;}" +
    /* etkin cipe yeniden basmak suzgeci temizler — sitedeki .fchip davranisi */
    ".wb-fc[aria-pressed='true']::after{content:'\\00d7';margin-left:6px;font-size:13px;" +
      "line-height:1;font-weight:700;opacity:.62;}" +

    "#wb-gorsel{display:block;width:100%;aspect-ratio:1200/627;object-fit:cover;background:#0a1225;}" +
    "#wb-govde{padding:12px 14px 14px;}" +
    "#wb-ust{display:flex;align-items:center;gap:10px;margin-bottom:9px;}" +
    "#wb-tarih{flex-shrink:0;width:44px;padding:5px 0 6px;border-radius:9px;text-align:center;" +
      "background:rgba(0,200,240,.13);border:.5px solid rgba(0,200,240,.32);}" +
    "#wb-tarih b{display:block;font-size:17px;font-weight:800;color:#fff;line-height:1.1;}" +
    "#wb-tarih i{display:block;font-style:normal;font-size:9.5px;font-weight:700;letter-spacing:.5px;" +
      "text-transform:uppercase;color:#00c8f0;}" +
    "#wb-etiket{font-size:10px;font-weight:700;letter-spacing:.7px;text-transform:uppercase;" +
      "color:rgba(255,255,255,.5);display:block;margin-bottom:2px;}" +
    "#wb-saat{font-size:11.5px;color:rgba(255,255,255,.62);}" +
    "#wb-baslik{font-size:13.5px;font-weight:700;line-height:1.45;color:#fff;margin:0 0 12px;}" +

    "#wb-kayit{display:flex;align-items:center;justify-content:center;gap:7px;width:100%;" +
      "padding:10px 14px;border-radius:10px;background:#00c8f0;color:#04101e;" +
      "font-size:13px;font-weight:800;text-decoration:none;transition:background .2s,transform .15s;}" +
    "#wb-kayit:hover{background:#3ad8ff;transform:translateY(-1px);}" +

    "#wb-alt{display:flex;align-items:center;justify-content:space-between;gap:8px;" +
      "margin-top:12px;padding-top:11px;border-top:.5px solid rgba(255,255,255,.09);}" +
    "#wb-oklar{display:flex;gap:6px;}" +
    ".wb-ok{width:30px;height:30px;border:.5px solid rgba(255,255,255,.14);border-radius:8px;cursor:pointer;" +
      "background:rgba(255,255,255,.05);color:rgba(255,255,255,.78);font-size:15px;line-height:1;" +
      "display:flex;align-items:center;justify-content:center;transition:border-color .2s,background .2s,color .2s;}" +
    ".wb-ok:hover:not(:disabled){border-color:rgba(0,200,240,.5);background:rgba(0,200,240,.12);color:#fff;}" +
    ".wb-ok:disabled{opacity:.32;cursor:default;}" +
    "#wb-sayac{font-size:11px;color:rgba(255,255,255,.42);font-variant-numeric:tabular-nums;}" +
    "#wb-tumu{font-size:11.5px;color:#00c8f0;text-decoration:none;font-weight:600;}" +
    "#wb-tumu:hover{text-decoration:underline;}" +

    /* Dokunmatikte hover yok: sekme kalici olarak gomulu kalmasin diye
       disari tasma payi kucultulur, boylece dokunma hedefi buyur. */
    "@media (hover:none){#wb-tab{transform:translate(5px,-50%);}}" +
    "@media (max-width:600px){" +
      "#wb-tab{width:46px;padding:9px 5px 8px;}" +
      "#wb-tab .wb-t-gun{font-size:15px;}#wb-tab .wb-t-et{display:none;}" +
      /* Sekme dikey ortadayken tam genislikteki kartlarin ~13px uzerine
         biniyordu. Mobilde yuzen dugmelerin bulundugu sag-alt koseye,
         WhatsApp dugmesinin (bottom:24px, 58px) hemen ustune alinir;
         panel de asagi tasmamak icin yukari dogru acilir. */
      "#wb-rail{top:auto;bottom:130px;}" +
      "#wb-panel{top:auto;bottom:0;transform:translate(calc(100% + 14px),0);}" +
      "#wb-rail.wb-acik #wb-panel{transform:translate(0,0);}" +
      "#wb-panel{width:min(292px,calc(100vw - 22px));max-height:calc(100vh - 150px);}}" +
    "@media (prefers-reduced-motion:reduce){" +
      "#wb-tab,#wb-panel,#wb-kayit,.wb-ok{transition:none;}}";

  function ekle() {
    var st = document.createElement("style");
    st.textContent = CSS;
    document.head.appendChild(st);

    var rail = document.createElement("aside");
    rail.id = "wb-rail";
    rail.innerHTML =
      '<button id="wb-tab" type="button" aria-expanded="false" aria-controls="wb-panel">' +
        '<span class="wb-t-gun"></span><span class="wb-t-ay"></span>' +
        '<span class="wb-t-cizgi" aria-hidden="true"></span>' +
        '<span class="wb-t-et">WEBİNAR</span></button>' +
      '<div id="wb-panel" role="region" aria-label="Yaklaşan webinarlar">' +
        '<div id="wb-bas"><span>Yaklaşan Webinar</span>' +
          '<button id="wb-kapat" type="button" aria-label="Kapat">' +
            '<i class="ti ti-x" aria-hidden="true"></i></button></div>' +
        '<div id="wb-filtre" role="group" aria-label="Sektöre göre süz">' +
          '<button class="wb-fc" type="button" data-f="aec" aria-pressed="false">İnşaat</button>' +
          '<button class="wb-fc" type="button" data-f="dm" aria-pressed="false">Üretim</button>' +
        '</div>' +
        '<img id="wb-gorsel" alt="" loading="lazy" decoding="async">' +
        '<div id="wb-govde" aria-live="polite">' +
          '<div id="wb-ust"><div id="wb-tarih"><b></b><i></i></div>' +
            '<div><span id="wb-etiket"></span><span id="wb-saat"></span></div></div>' +
          '<p id="wb-baslik"></p>' +
          '<a id="wb-kayit" href="#"><span>Kayıt Ol</span>' +
            '<i class="ti ti-arrow-right" aria-hidden="true"></i></a>' +
          '<div id="wb-alt"><div id="wb-oklar">' +
            '<button class="wb-ok" id="wb-onceki" type="button" aria-label="Önceki webinar">' +
              '<i class="ti ti-chevron-left" aria-hidden="true"></i></button>' +
            '<button class="wb-ok" id="wb-sonraki" type="button" aria-label="Sonraki webinar">' +
              '<i class="ti ti-chevron-right" aria-hidden="true"></i></button>' +
            '</div><span id="wb-sayac"></span>' +
            '<a id="wb-tumu" href="' + LISTE + '">Tümü</a></div>' +
        '</div></div>';
    document.body.appendChild(rail);
    return rail;
  }

  function baslat(tumListe) {
    if (!tumListe.length) return;
    var rail = ekle();
    var q = function (s) { return rail.querySelector(s); };
    var tab = q("#wb-tab"), panel = q("#wb-panel");
    var ix = 0;
    var filtre = null;                 /* null = tumu, yoksa "aec" | "dm" */

    /* Suzgecten gecen liste. Bir sektorde hic webinar kalmadiysa suzgec
       yok sayilir; kullanici bos bir panelle karsilasmaz. */
    function liste() {
      if (!filtre) return tumListe;
      var s = tumListe.filter(function (w) { return w.kategori === filtre; });
      return s.length ? s : tumListe;
    }

    function ciz() {
      var l = liste();
      if (ix > l.length - 1) ix = l.length - 1;
      if (ix < 0) ix = 0;
      var w = l[ix];
      q("#wb-gorsel").src = w.gorsel;
      q("#wb-gorsel").alt = w.gorselAlt;
      q("#wb-tarih b").textContent = w.gun;
      q("#wb-tarih i").textContent = w.ay;
      q("#wb-etiket").textContent = w.etiket;
      q("#wb-saat").textContent = w.saat;
      q("#wb-baslik").textContent = w.baslik;
      var kayit = q("#wb-kayit");
      kayit.href = w.kayit;
      kayit.setAttribute("aria-label", w.baslik + " webinarına kayıt ol");
      /* Kayit linki Teams gibi dis bir siteye gidiyorsa yeni sekmede acilir
         ve ikon dis-baglanti isaretine doner. */
      var disari = false;
      try { disari = new URL(w.kayit, location.href).origin !== location.origin; } catch (e) {}
      if (disari) {
        kayit.target = "_blank";
        kayit.rel = "noopener";
      } else {
        kayit.removeAttribute("target");
        kayit.removeAttribute("rel");
      }
      kayit.querySelector("i").className =
        "ti " + (disari ? "ti-external-link" : "ti-arrow-right");
      q("#wb-sayac").textContent = (ix + 1) + " / " + l.length;
      q("#wb-onceki").disabled = ix === 0;
      q("#wb-sonraki").disabled = ix === l.length - 1;
      /* Sekmede daima (suzgecten bagimsiz) en yakin webinarin tarihi durur. */
      tab.querySelector(".wb-t-gun").textContent = tumListe[0].gun;
      tab.querySelector(".wb-t-ay").textContent = tumListe[0].ay;
      tab.setAttribute("aria-label",
        "Yaklaşan webinar: " + tumListe[0].gun + " " + tumListe[0].ayUzun + " — " + tumListe[0].baslik);
    }

    function ac(durum) {
      /* Panel her acilista daima siradaki (en yakin) webinarla baslar;
         onceki gezinme yerinde kalmaz. Sektor secimi kullanicinin bilincli
         tercihi oldugu icin korunur, yalnizca sira basa alinir. */
      if (durum) { ix = 0; ciz(); }
      rail.classList.toggle("wb-acik", durum);
      tab.setAttribute("aria-expanded", String(durum));
      if (durum) q("#wb-kapat").focus();
      else tab.focus();
    }

    tab.addEventListener("click", function () { ac(true); });
    q("#wb-kapat").addEventListener("click", function () { ac(false); });
    q("#wb-onceki").addEventListener("click", function () { if (ix > 0) { ix--; ciz(); } });
    q("#wb-sonraki").addEventListener("click", function () { if (ix < liste().length - 1) { ix++; ciz(); } });

    /* Sektor cipleri: etkin cipe yeniden basmak suzgeci temizler. */
    Array.prototype.forEach.call(rail.querySelectorAll(".wb-fc"), function (c) {
      c.addEventListener("click", function () {
        var f = c.getAttribute("data-f");
        filtre = (filtre === f) ? null : f;
        Array.prototype.forEach.call(rail.querySelectorAll(".wb-fc"), function (x) {
          x.setAttribute("aria-pressed", String(x.getAttribute("data-f") === filtre));
        });
        ix = 0;
        ciz();
      });
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && rail.classList.contains("wb-acik")) ac(false);
    });
    /* Panel disina tiklayinca kapanir. */
    document.addEventListener("click", function (e) {
      if (rail.classList.contains("wb-acik") && !rail.contains(e.target)) ac(false);
    });

    ciz();
    rail.classList.add("wb-hazir");
  }

  function getir(i) {
    i = i || 0;
    if (i >= KAYNAKLAR.length) return;      /* veri yoksa widget hic gorunmez */
    var kaynak = KAYNAKLAR[i];
    fetch(kaynak, { credentials: "same-origin" })
      .then(function (r) { return r.ok ? r.text() : Promise.reject(r.status); })
      .then(function (html) {
        var liste = kartlariOku(html, kaynak);
        /* Yanit geldi ama webinar karti yoksa (orn. 404 sayfasi) sonrakini dene. */
        if (!liste.length) return Promise.reject("kart yok");
        return liste;
      })
      /* Hata isleyicisi bilincli olarak yalnizca VERI adimini kapsar:
         baslat() icindeki bir hata yutulup sessizce sonraki kaynaga
         gecilmesin, konsolda gorunsun. */
      .then(baslat, function () { getir(i + 1); });
  }

  /* Sayfa acilisini yavaslatmamak icin bosta calistir. */
  function planla() {
    /* requestIdleCallback geri cagirima IdleDeadline gecirir; getir()'in
       kaynak indeksi parametresiyle karismasin diye sarmalanir. */
    var basla = function () { getir(0); };
    if (window.requestIdleCallback) requestIdleCallback(basla, { timeout: 3000 });
    else setTimeout(basla, 1200);
  }
  if (document.readyState === "complete") planla();
  else window.addEventListener("load", planla);
})();
