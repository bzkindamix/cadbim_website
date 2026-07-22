# CADBİM Web Sitesi — Değişiklik Kayıtları (PDM / Revizyon Günlüğü)

> Bu dosya, projeye yapılan her değişikliğin izlenebilir kaydını tutar (PDM/ECO mantığı).
> Kayıt biçimi: **DK-YYYY-MM-DD-NN** · Tarih · Yapan · Kapsam · Etkilenen dosyalar · Doğrulama · Durum · Referans (commit).
> Kaynak kod sürüm kontrolü Git/GitHub'dadır; bu dosya insan-okunur değişiklik özetidir.

---

## 2026-07-22

### DK-2026-07-22-07 — Atölye şeridi v2: tam genişlik + palet uyumu

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Onur'un iki maddesi:**
  1. **Tam genişlik, çerçevesiz:** Yuvarlatılmış degrade çerçeveli kart kaldırıldı; şerit artık section sarmalayıcısız, kenardan kenara tam bleed bir bant (üst/alt ince w10 çizgiler, section-alt dilinde navy2 zemin + cyan ışımalar, hover'da navy3).
  2. **Palet denetimi:** Ana sayfanın gerçek paleti ölçüldü — yalnız lacivert ailesi + cyan ailesi (#00c8f0/#0ea5e9/#38bdf8) + nötr açık (#e6ebf2). Şeritteki 5 yabancı renk (viyole #8b7cf7, magenta #f26bd8, mavi #3d78ff...) doğrulandı: palette YOK → tamamı temizlendi. Degrade çerçeve/em/tag/marquee vurguları cyan'a; **halka panelleri** palet-içi "baskı" görsellerine yeniden boyandı (cyan güneş, sis, s/b çizgiler, cyan konik, mimari çizgiler, nötr kağıt) — sıcak/viyole tonlar tamamen çıktı.
- **Doğrulama:** Tam bleed (sol 0, genişlik = içerik genişliği 1265), border-radius 0, em/tag cyan (rgb 0,200,240), 6 panel, dosyada yabancı renk kalıntısı 0, taşma 0, div/section dengesi 0.
- **Durum:** ✅ Tamamlandı ve yayınlandı. **Referans:** commit (main) — aşağıda.

### DK-2026-07-22-06 — Ana sayfaya Sanatsal Baskı Atölyesi şeridi

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** index.html'de Çözümler ile Fark (Neden Cadbim) bölümleri arasına, atölye sayfasına yönlendiren tıklanabilir tanıtım şeridi. Ana sayfanın lacivert/cyan diline oturan ama atölye kimliğini taşıyan tasarım:
  - **İridesan degrade çerçeve** (cyan→viyole→magenta, padding-box/border-box tekniği) + köşe ışımaları; hover'da yükselme + viyole gölge.
  - **Mini 3D halka:** atölye sayfasındaki galeri halkasının 6 panelli kompakt versiyonu (saf CSS, 22s dönüş, -10° eğim; mobilde gizli).
  - **Akan kelime şeridi:** alt kenarda GICLÉE · KANVAS · FOTOBLOK · ÇERÇEVE · SERGİ BASKISI · REPRODÜKSİYON (26s döngü).
  - Metin: "Fotoğrafınız, duvarda bir *esere* dönüşür." (degrade em) + rötuş/finisaj özeti + "Atölyeyi keşfedin" oku.
  - Ana sayfanın mevcut `.reveal` animasyon sistemine bağlandı; tüm hareket `prefers-reduced-motion` korumalı.
- **Doğrulama:** localhost 1280/375 — konum doğru (Çözümler→şerit→Fark), hedef link doğru, 6 panel + `aringDon` animasyonu, 12 marquee span, 1169×312 yerleşim, mobilde halka gizli/335px genişlik, yatay taşma 0, div dengesi 0.
- **Durum:** ✅ Tamamlandı ve yayınlandı. **Referans:** commit (main) — aşağıda.

### DK-2026-07-22-05 — Sanatsal Baskı R2: tek-ekran hero, ray okları, 3+3 finisaj, 3D galeri halkası

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Onur'un 4 maddesi:**
  1. **Hero her cihazda tek ekran:** Display tipografisi genişlik+yükseklik duyarlı ölçeğe alındı — `clamp(2.5rem, min(11.5vw, 15vh), 10.5rem)`; tüm dikey boşluklar (hero padding, h1/h-bottom/h-meta marjları, buton yükseklikleri) vh-clamp'e çevrildi. Doğrulama: 1366×700 → 668/700, 1600×860 → 797/860, 375×812 → 761/812 — hepsi sığıyor.
  2. **Yüzey rayına ok düğmeleri:** başlık satırına ←/→ dairesel butonlar; kart genişliği+16px adımla smooth kaydırma + smooth'un çalışmadığı ortamlar için 320ms zamanlayıcı güvencesi (doğrudan scrollLeft). İki yön de test edildi.
  3. **Finisaj 3+3:** auto-fit yerine sabit `repeat(3,1fr)` (≤900px: 2 sütun, ≤540px: 1). Doğrulama: 2 satır × 3 kutu.
  4. **Girişe 3D animasyon:** Saf CSS **3D galeri halkası** — 8 "baskı paneli" (gradient eserler) `preserve-3d` + `rotateY(n·45°) translateZ()` ile halka dizilimi, 34s sonsuz dönüş, -8° eğim, imleçle ±8° paralaks (pointer:fine + hareket açıkken). Kütüphanesiz, `prefers-reduced-motion`'da statik yelpaze, ≤1180px'te gizli.
- **Ek düzeltme:** 3D panellerin projeksiyonu scrollable alanı genişletiyordu → `html{overflow-x:clip}`. Başlık metni ile halka çakışması gerçek metin genişliğiyle ölçüldü: 1366'da 500px+ boşluk, çakışma yok.
- **Durum:** ✅ Tamamlandı ve yayınlandı. **Referans:** commit (main) — aşağıda.

### DK-2026-07-22-04 — Sanatsal Baskı: Ankara kaldırıldı, WhatsApp hattı eklendi

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** Onur'un talebi — bu sayfada Ankara'dan bahsedilmeyecek. "ANKARA HATTI" iletişim kartı (0553 353 99 20) kaldırıldı; yerine **WHATSAPP HATTI — 0554 740 37 57** kartı geldi. Kart `https://wa.me/905547403757` linkiyle, "Merhaba, sanatsal baskı talebim var." ön-dolu mesajıyla WhatsApp'ı açıyor (`target="_blank" rel="noopener"`). Süreç bölümündeki "E-posta ya da WhatsApp" ifadesiyle artık tutarlı.
- **Doğrulama:** Sayfada Ankara/0553 referansı 0; wa.me/905547403757 ve görünür numara doğru.
- **Durum:** ✅ Tamamlandı ve yayınlandı. **Referans:** commit (main) — aşağıda.

### DK-2026-07-22-03 — Sanatsal Baskı: özel e-posta + metin tonu keskinleştirme

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **E-posta:** Sayfadaki görünür tüm iletişim noktaları **sanatsalbaski@cadbim.com.tr** oldu (CTA butonu + e-posta kartı; 2 mailto + 1 görünür metin). JSON-LD Organization kaydındaki cadbim@ bilinçli korundu — kurum kimliği site genelinde tektir. *Not: yeni adresin posta sunucusunda tanımlanması gerekir.*
- **Metin tonu (38 metin bloğu):** Açıklayıcı ton, kısa-özgüvenli galeri diline çevrildi. Örnekler: hero → "Duvara astığınız şey artık bir çıktı değil — bir eser."; hizmetler başlığı → "Kadrajdan koleksiyona."; rötuş → "Ham dosya girer. Eser çıkar."; yüzeyler → "Doğru kağıt, işin yarısı."; süreç → "Renk doğruluğu pazarlık konusu değil."; finisaj → "Baskı yarısı; sunum diğer yarısı." CTA kartları ve kapanış notu sadeleştirildi; tüm iddialar içerik kaynaklı kaldı (yeni sayı/iddia eklenmedi).
- **Doğrulama:** localhost — 5 yeni ton işaretçisi + sanatsalbaski@ görünür (2 mailto), eski adres görünür metinde 0, sürgü çalışıyor, taşma yok.
- **Durum:** ✅ Tamamlandı ve yayınlandı. **Referans:** commit (main) — aşağıda.

### DK-2026-07-22-02 — Sanatsal Baskı one-pager'ı Noomo stiline geçirildi

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Tetikleyici:** Onur'un referansı — noomoagency.com (Awwwards). Canlı siteden tasarım imzaları çıkarıldı: menekşe-siyah zemin (#181520), buz-lavanta metin, elektrik mavisi (#007aff), NeueMachina display tipografisi, iridesan 3D küre.
- **Uyarlama (DK-01'deki galeri/fildişi sürüm yerine):**
  - **Palet:** #131019 menekşe-siyah + buz-lavanta (#e9ecf7) + elektrik mavisi/iridesan degrade (cyan→viyole→magenta). **Tipografi:** Space Grotesk (NeueMachina'nın Google Fonts karşılığı) + Inter.
  - **Hero:** 11.5vw'lik 3 satır display — SANATSAL (dolu) / BASKI (iridesan degrade) / ATÖLYESİ (kontur) — satır-maskeli yükleme reveal'ları; arkada 2 iridesan CSS orb (WebGL küre öykünmesi, blur+drift).
  - **Noomo imzaları:** özel imleç (nokta + gecikmeli halka, data-hover'da büyür; ilk mousemove'a kadar gizli), manyetik butonlar, marquee şerit, dev satır-listesi hizmetler (hover'da degrade dolgu + ok rotasyonu), yatay sürükle-kaydır yüzey rayı, degrade dev sayaçlar, kontur CTA tipografisi (BASKIYA HAZIR MISINIZ?).
  - **Korunanlar:** interaktif rötuş sürgüsü (koyu restil), 4 adım süreç, 6 finisaj kartı, iletişim kartları; içerik birebir.
- **Erişilebilirlik/dayanıklılık:** Tüm hareket `prefers-reduced-motion`'da kapalı; imleç/manyetik yalnız `hover:hover + pointer:fine`; sayaçlarda rAF + zamanlayıcı güvencesi; reveal zaman-eşikli scroll motoru. SEO bloğu (canonical, Service JSON-LD) değişmedi.
- **Doğrulama:** localhost 1280/375 — yapı tam (5 iş + 6 yüzey + 4 adım + 4 sayaç + 6 finisaj + 4 iletişim + 2 orb), Space Grotesk aktif, sürgü %30→%75, marquee 18 span, reveal kademeli (16/36 kısmi), sayaçlar 12/2400/152/100, başlık mobilde sığıyor, ray kaydırılabilir, taşma 0, konsol hatası 0.
- **Durum:** ✅ Tamamlandı ve yayınlandı. **Referans:** commit (main) — aşağıda.

### DK-2026-07-22-01 — Sanatsal Baskı Atölyesi: özel tasarım one-pager

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** `cadbim_sanatsal_baski.html` sıfırdan, site genel temasından bilinçli ayrılan **galeri/editoryal estetikte** tek sayfalık tasarımla yeniden yazıldı (Onur'un talebi: "tamamen muhteşem, gerekirse tema dışı"). İçerik canlı cadbim.com.tr/sanatsalbaski + mevcut sayfadan derlendi.
- **Tasarım dili:** Fildişi kağıt zemini + mürekkep siyahı + vermilyon vurgu; Fraunces (optik boyutlu serif) + Inter tipografisi; CSS gren/kağıt dokusu; navy/cyan temadan tam kopuş.
- **Bölümler:** Minimal sabit üst bar → Hero (saf CSS "galeri duvarı": 3 çerçeveli eser + künye plaketi, kademeli yükleme animasyonu) → akan şerit (GICLÉE/KANVAS/FOTOBLOK...) → 5 hizmet satırı (editoryal liste) → 6 yüzey kartı (hover parlaklık süpürmeli doku çipleri) → **interaktif rötuş kıyas sürgüsü** (HAM DOSYA / ATÖLYE ÇIKIŞI) → 4 adımlı süreç (kontur rakamlar) → koyu ekipman bölümü (Z9+ Pro: 12 renk / 2400 dpi / 152 cm / 100+ yıl **animasyonlu sayaçlar**) → sergi alıntısı → 6 finisaj kartı (el çizimi SVG ikonlar) → iletişim (İzmir/Ankara/e-posta/form kartları).
- **Etkileşim/erişilebilirlik:** Sayfaya özel zaman-eşikli scroll-reveal + hero paralaksı + sayaçlar; tümü `prefers-reduced-motion`'da devre dışı (içerik anında görünür). Uppercase metinler literal yazıldı — İ/I sorunu tasarımdan elendi (GICLÉE, FINE ART).
- **SEO:** canonical `/sanatsal-baski` korundu; title/description yenilendi; JSON-LD **Service** şeması eklendi (Organization + WebPage + Breadcrumb ile).
- **Doğrulama:** localhost 1280/375 — yapı sayımları tam (5+6+4+4+6+4 kart/bölüm, 3 çerçeve), logo/Fraunces yüklü, sürgü %25→%80 tepkili, şerit çoğaltıldı (18 span), reveal kademeli (17/41 kısmi kaydırmada), sayaçlar hedefe ulaştı (12/2400/152/100), yatay taşma yok, konsol hatası 0.
- **Durum:** ✅ Tamamlandı ve yayınlandı.
- **Referans:** commit (main) — aşağıda.

## 2026-07-21

### DK-2026-07-21-31 — Canlıya geçiş hazırlığı: eski site URL envanteri + 301 haritası

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** Canlı cadbim.com.tr (Wix) sitemap index'inden **665 URL** toplandı (24 alt sitemap): 120 ana sayfa, 242 blog yazısı, 97 blog taksonomi, ~206 dinamik koleksiyon öğesi. Yeni site canonical setiyle (153) tam eşleme üretildi:
  - **33 BIREBIR** (aynı slug — 301 gerekmez), **210 KURAL** (kesin 301 hedefi), **83 GOZDEN** (Onur onayı gerekli), **339 GOZDEN-BLOG** (blog kararına bağlı).
  - DesignJet/UltiMaker/Chaos/Adobe koleksiyon öğeleri **model/ürün bazında** eşlendi (ör. /designjet-ofis/hp-designjet-t230 → /designjet-t200).
  - **İçerik adı değişiklikleri tablosu:** Construction Cloud→Autodesk Forma, Fusion 360→Fusion, ShotGrid→Flow Production Tracking, HSMWorks→Fusion, AutoCAD dikey ürünleri→toolset, Nastran/CFD/Point Layout EOL, MakerBot→UltiMaker vb.
  - Strateji notları: GitHub Pages sunucu-taraflı 301 yapamaz → canlıda Cloudflare Pages/Netlify benzeri host şart; Türkçe karakterli eski URL'ler; Search Console süreci; geçiş günü kontrol listesi.
- **Çıktılar:** `docs/CANLIYA-GECIS-URL-HARITASI.md` (rapor) + `docs/redirects-taslak.csv` (665 satır, makine-okunur).
- **Durum:** ✅ Doküman hazır; GOZDEN kalemleri Onur onayı bekliyor.

### DK-2026-07-21-30 — İç sayfalara scroll-reveal animasyon motoru

- **Kapsam:** Ana sayfadaki reveal deneyimi tüm iç sayfalara taşındı. `design-system.css`'e `[data-rv]` stilleri (yalnız `prefers-reduced-motion: no-preference` altında), `mobilenav.js`'e motor eklendi: `.sh/.card/.pgrid .pcard/.feat/.xp/.cross/.cta-strip/.office-card` hedefleri, ebeveyn içi 60ms kademeli gecikme (maks 360ms), ana sayfanın kendi `.reveal`'ı hariç tutulur.
- **Teknik karar:** IntersectionObserver yerine **zaman-eşikli scroll dinleyicisi** (80ms) — tarayıcı panelinde IO/rAF'ın hiç ateşlemediği tespit edildi; scroll+getBoundingClientRect her ortamda deterministik. `window.__rv` teşhis kancası bırakıldı.
- **Cache-bust:** design-system.css v7, mobilenav.js v5 (153 sayfa).
- **Doğrulama:** localhost — revit/autodesk/urunler: ilk görünüm anında, kaydırdıkça kademeli reveal (urunler 89 eleman, 1500px kaydırmada 39 reveal); stagger 0/60/120/180ms ölçüldü.

### DK-2026-07-21-29 — Site geneli kod + SEO denetimi ve düzeltmeleri

- **Denetim (154 dosya):** kırık iç link **0**, kırık asset **0**, duplicate id **0**, div dengesizliği **0**, alt'sız görsel **0**, title/desc mükerrerliği **0** — yapı zaten sağlamdı. Bulunan ve düzeltilenler:
  - **Attribute kıran tırnaklar:** designjet hd_pro/sd_pro description'larında kaçışsız `42"`/`44"` → `&quot;` (3'er meta).
  - **Kısa title'lar:** cozumler, kvkk, tesekkurler zenginleştirildi; **index description** 182→146 karakter.
  - **tesekkurler.html** form-sonrası sayfa → `noindex, follow`.
  - **Sitemap ↔ canonical uyumu:** 6 slug hizalandı (z6pro→z6-pro, factor4→factor-4, substance3d→substance-3d...).
  - **Performans:** 107 sayfada **647 img'e `loading="lazy"`**, 878 img'e `decoding="async"` — nav + hero görselleri bilinçli hariç (LCP koruması).
  - Yönlendirme stub'ına h1.
- **Durum:** ✅ Tamamlandı ve yayınlandı. **Referans:** commit (main) — DK-29/30/31 tek commit.

### DK-2026-07-21-28 — construction_cloud → autodesk_forma yeniden adlandırma + sayfa denetimi

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** Sayfa içeriği DK-öncesi turlarda "Autodesk Forma"ya çevrilmişti ama **dosya adı/URL** eski kalmıştı. Yapılanlar:
  - `cadbim_construction_cloud.html` → **`cadbim_autodesk_forma.html`** (git mv); canonical/og/JSON-LD 7 URL `/construction-cloud` → `/autodesk-forma`.
  - **Logolar güncellendi:** hero'daki jenerik vinç ikonu → resmi `forma.svg` (56px); "Build & Takeoff" modül kartındaki kask ikonu → `forma.svg`. (Diğer modül kartları zaten resmi SVG'liydi.)
  - **12 referans** güncellendi (8 sayfa + urunler 2 + tandem 4 dahil); `mobilenav.js` arama dizini kaydı "Autodesk Forma" oldu (eski ad arama anahtarı olarak korundu); `sitemap.xml` girdisi `/autodesk-forma` (lastmod 2026-07-21).
  - Eski adrese **yönlendirme stub'ı** bırakıldı (meta refresh + JS replace + canonical + noindex) — eski linkler kırılmaz.
  - Sayfada görünür "Construction Cloud" metni taraması: yalnızca bilinçli "(Eski adı Autodesk Construction Cloud.)" notu var, korunudu.
- **Doğrulama:** localhost — eski URL yeni sayfaya yönlendiriyor; başlık doğru; 3 forma.svg yüklü; taşma yok; site genelinde `construction_cloud` referansı 0.
- **Durum:** ✅ Tamamlandı ve yayınlandı.

### DK-2026-07-21-27 — Site geneli İngilizce sözcüklerde büyük-İ (İ→I) denetimi

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Sorun:** Sayfalar `lang="tr"` olduğundan `text-transform:uppercase` İngilizce sözcüklerde de noktalı İ üretiyor (Architecture→ARCHİTECTURE, Trimble→TRİMBLE); ayrıca kaynakta yazılı 1 hata (COOKİE).
- **Denetim:** 152 sayfada (a) kaynakta İ içeren tüm sözcükler, (b) uppercase-transform'lu sınıf ve satır-içi stillerin tam metinleri tarandı. `lang="en"` verilmiş öğeler (sektör hero-badge'leri) zaten doğruydu — dokunulmadı. Türkçe sözcükler (LİSANSLAMA, SERİ, VİDEOSU, CADBİM...) bilinçli olarak İ ile bırakıldı.
- **Düzeltmeler (19 dosya, 27 değişiklik; İngilizce sözcükler kaynakta ön-uppercase edildi):** COOKİE→COOKIE (çerez politikası ×2); urunler grup başlıkları (ARCHITECTURE/ENGINEERING/CONSTRUCTION, PRODUCT DESIGN & MANUFACTURING, MEDIA & ENTERTAINMENT) + AMPLIFY rozeti; autodesk hero-pill SERVICE PROVIDER; hp hero-pill AMPLIFY; slabel'ler: ALIAS ×2, CIVIL, FUSION, AMPLIFY Impact ×2; satır-içi etiketler: CREDENTIALS, SPECIALIZATION (hakkimizda), HP CONSTRUCTION (build_workspace), LUMION B.V., MICROSOFT, TRIMBLE (sketchup), ULTIMAKER, HP DESIGNJET (sanatsal_baski), NESTING, FINE ART (designjet); pbrand: TRIMBLE (mimari), ULTIMAKER (makine).
- **Durum:** ✅ Tamamlandı ve yayınlandı.
- **Referans:** commit (main) — aşağıda (DK-27 ve DK-28 tek commit).

### DK-2026-07-21-26 — Filtreli katalog deseni 7 endüstri sayfasına yayıldı

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** Marka sayfalarındaki filtreli katalog mantığı (Tümü+kategori chipleri, isim arama, pcard grid, boş durum) endüstri sayfalarına taşındı:
  - **Sekmeli gezgin dönüşümü (5 sayfa):** mimari (14), insaat (9), makine (15), medya (15), otomotiv (10) — eski `.solutions` sekme yapısı (tek kategori görünür, switchCat JS) kaldırıldı; tüm ürünler tek filtrelenebilir grid'de. Mevcut kategori adları chip oldu; kart içeriği (marka üst-etiketi + isim + rol + ikon) birebir korundu. Ölü switchCat script blokları silindi.
  - **Pill şeridi yükseltmesi (2 sayfa):** egitim (7: Yazılım 4 / 3D Baskı 2 / Donanım 1), havacilik (8: Tasarım & Müh. 3 / Üretim & Sim. 3 / Veri 1 / Donanım 1) — "Bu sektörde kullanılan ürünler" 13px pill şeridi katalog kartlarına dönüştü; açıklamalar hedef ürün sayfalarının meta description'ından otomatik alındı. Kutunun içinde filtre çubuğu sticky değil (statik).
- **Etkilenen dosyalar (7):** sektor_mimari, sektor_insaat, sektor_makine, sektor_medya, sektor_otomotiv, sektor_egitim, sektor_havacilik (+ scratchpad `sektor_catalogs.py`).
- **Doğrulama:** localhost 1280/375 — 7 sayfada toplam 78 kart; tüm chip sayıları kategori toplamlarıyla tutarlı; arama çalışıyor (mimari "revit"→2); 0 gerçek kırık ikon (ilk ölçümdeki 10 "kırık" lazy-load'du, eager doğrulamayla çürütüldü); mobilde tek sütun, chip taşması ve yatay taşma yok; div dengeleri 0; switchCat kalıntısı 0.
- **Durum:** ✅ Tamamlandı ve yayınlandı.
- **Referans:** commit (main) — aşağıda.

### DK-2026-07-21-25 — Filtreli ürün kataloğu 5 marka sayfasına daha yayıldı

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** Autodesk'te kurulan filtreli katalog deseni (DK-23: fchip kategori filtreleri + isim arama + pgrid/pcard + boş durum) uygun tüm markalara uygulandı:
  - **Adobe (13):** "Creative Cloud Uygulamaları" bölümü katalogla değişti — Paket & Doküman 2 / Grafik & Fotoğraf 4 / Video & Ses 3 / 3D & AI 2 / İçerik & Stok 2.
  - **HP (22):** Designjet Serisi bölümünden sonra YENİ katalog bölümü — tüm model sayfaları tek listede: DesignJet T 9 / XL 2 / Z 5 / Tarayıcı & Tank 3 / İş İstasyonları 2 / Yazılım 1. Model adları ve açıklamaları her modelin kendi sayfasının title/meta'sından otomatik çekildi.
  - **Chaos (8):** "Chaos Ekosistemi" bölümü katalogla değişti — Render 2 / Gerçek Zamanlı 2 / Simülasyon & Animasyon 2 / AI & Varlıklar 2 (Anima ve Cosmos eklendi).
  - **UltiMaker (9):** "Yazıcı Modelleri" bölümü katalogla değişti — 3D Yazıcılar 7 (S8-S3, Factor 4, Method XL, Sketch Sprint) / Yazılım 2 (Cura, Digital Factory).
  - **SketchUp (7):** "SketchUp Pro Ürünleri" bölümü katalogla değişti — Pro Ailesi 4 / Platform & Paketler 3.
- **Kural:** Kendi sayfası olmayan ya da bulunulan sayfaya işaret eden ürünler ok'suz, tıklanmaz kart olarak listelendi (ör. V-Ray/Enscape/Veras, S-serisi modeller, Pro varyantları). **Lumion (4) ve Microsoft (3)** bilinçli kapsam dışı: tüm ürünleri zaten tek bakışta görünüyor, filtre değer katmıyor.
- **Bonus:** cadbim_urunler.html'de Digital Factory kartındaki yanlış ikon (Autodesk logosu) → ultimaker-icon düzeltildi.
- **Doğrulama:** localhost 1280/375 — 5 sayfada kart sayıları ve tüm chip filtreleri doğru (59 kart toplam), 0 kırık ikon, arama çalışıyor (hp "t850"→1), mobilde tek sütun/statik filtre/taşma yok, div dengeleri 0.
- **Durum:** ✅ Tamamlandı ve yayınlandı.
- **Referans:** commit (main) — aşağıda.

### DK-2026-07-21-24 — Site geneli logo-metin dikey hizalama denetimi ve düzeltmesi

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Tetikleyici:** cadbim_alias.html sürüm kartlarında ürün ikonu ile sürüm rozeti (CONCEPT / SURFACE / AUTOSTUDIO) baseline hizasında kayık duruyordu.
- **Denetim (152 sayfa, statik tarama + tarayıcıda piksel ölçümü):**
  - `img + <span class="cmp-badge">` satır-içi deseni: **4 bulgu** (alias 3, vault_pdm 1) → ikisi birlikte `display:flex;align-items:center;gap:10px` sarmalayıcıya alındı, rozetin `margin-bottom:10px`'i satır içinde sıfırlandı.
  - Öne çıkan kart başlıklarında `align-items:flex-start`: **3 bulgu** (chaos) → `center` yapıldı.
  - `.cp`/`.cross-pill` içi 13px mini logolar (53 dosya, ~130 kullanım): sınıf zaten `display:flex;align-items:center` — tarayıcı ölçümüyle 0.0px merkez farkı doğrulandı, **değişiklik gerekmedi**.
  - Flex dışı `vertical-align` img kullanımı: **0 bulgu**.
- **Doğrulama (localhost, DOM merkez ölçümü):** alias 3/3 rozet 0.0px; vault_pdm PLM BUNDLE 0.0px; chaos 3/3 başlık 0.0px; sketchup .cp örneklemi 5/5 0.0px; div dengeleri değişmedi.
- **Etkilenen dosyalar (3):** cadbim_alias.html, cadbim_vault_pdm.html, cadbim_chaos.html.
- **Durum:** ✅ Tamamlandı ve yayınlandı.
- **Referans:** commit (main) — aşağıda.

### DK-2026-07-21-23 — Autodesk sayfası: filtreli tam ürün kataloğu (46 ürün)

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** `cadbim_autodesk.html` "Öne Çıkan Ürünler" bölümü (13 kart) yalnızca portföyün bir kısmını gösteriyordu. Ürünler sayfasındaki desenle (fchip + pgrid/pcard) **46 ürünlük tam katalog** ile değiştirildi: kategori filtreleri (Tümü / Koleksiyonlar 3 / Mimarlık & İnşaat 11 / Forma Platformu 4 / Ürün Tasarımı & İmalat 11 / Medya & Eğlence 10 / Genel Araçlar 7) + isimle arama kutusu + "eşleşen ürün yok" boş durumu. Filtre çubuğu masaüstünde yapışkan (sticky), mobilde statik. Kart verisi cadbim_urunler.html Autodesk bölümünden birebir alındı (AutoCAD Web mükerrer kaydı tekilleştirildi).
- **Etkilenen dosyalar:** cadbim_autodesk.html (+ scratchpad `autodesk_catalog.py`).
- **Doğrulama:** localhost 1280/375 — 46 kart, 0 kırık ikon; filtreler doğru sayıyor (AEC 11, M&E 10), arama "maya"→4, boş arama mesajı çalışıyor, sıfırlama 46; mobilde tek sütun, chip taşması yok, yatay taşma yok; div dengesi 0.
- **Durum:** ✅ Tamamlandı ve yayınlandı.
- **Referans:** commit (main) — aşağıda.

### DK-2026-07-21-22 — Marka sayfaları R3 kalite iyileştirmesi (6 sayfa)

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam (Onur'un 5 maddesi, tüm marka ana sayfalarına uygulandı):**
  1. **Gold Partner rozeti küçültüldü** — autodesk hero rozeti clamp(200-290px)→clamp(150-200px) (masaüstü 282×429→192×292).
  2. **Hero hızlı-linkleri** — dağınık hap (pill) stili yerine eşit genişlikte gerilen, ikonlu, hover'lı düzenli kutular (`.hf` yeniden; mobil ≤600px varyantı ile). Autodesk/adobe/chaos/ultimaker.
  3. **Koleksiyonlar yan yana** — autodesk'te AEC/PD&M/M&E kartları kayıp grid sarmalayıcısı (`.colgrid`) ile 3 sütuna alındı (sayfadaki kadim -1 div dengesizliği de burada kapandı); resmi collection SVG ikonları + "Koleksiyonu incele →" linki eklendi.
  4. **LOGO placeholder temizliği** — 27 adet kesikli "LOGO" kutusu gerçek ürün logolarıyla değişti: autodesk 13 (resmi Autodesk SVG'leri; bağlantısız Navisworks/InfraWorks/Maya/Forma-platform kartları linklendi; mükerrer "Autodesk Forma" başlığı → "Forma Site Design"), chaos 6 (chaos.webp), ultimaker 5 (ultimaker-icon), microsoft 3 (microsoft.svg).
  5. **"Birlikte sıkça tercih edilenler"** — küçük/okunmaz logolu hap şeritleri yerine `.xgrid` kart modülü (42px logo kutusu + başlık + açıklama + ok); hedef linkler doğru ürün sayfalarına ayrıştırıldı (Z Workstation→hp_z_workstation, Designjet→designjet vb.). Autodesk/adobe/hp/chaos/ultimaker.
- **Partner rozet duvarları:** adobe (3 beyaz kutu → tek şeffaf Adobe Gold Reseller logosu), hp (3 beyaz kutu → tek resmi HP Amplify Synergy insignia, kendi kart tasarımıyla, çerçevesiz).
- **Etkilenen dosyalar (6):** cadbim_autodesk, cadbim_adobe, cadbim_hp, cadbim_chaos, cadbim_ultimaker, cadbim_microsoft (+ scratchpad script `brand_quality_r3.py`). sketchup/lumion/designjet/hp_z_workstation/hp_build_workspace'te bu desenler yok — değişiklik gerekmedi.
- **Doğrulama:** localhost 1280 ve 375 — 6 sayfada 0 kalan placeholder, 0 kırık logo, div dengeleri 0, yatay taşma yok; hf satırları eşit genişlik; koleksiyonlar masaüstünde tek satır/mobilde tek sütun; hp rozeti mobil 190×187 ortalı.
- **Durum:** ✅ Tamamlandı ve yayınlandı.
- **Referans:** commit (main) — aşağıda.

### DK-2026-07-21-21 — Autodesk hero: resmi tam-liste Gold Partner logosu (kullanıcı dosyası)

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** DK-20'deki sade "AUTODESK Gold Partner" logosu, Onur'un ilettiği **resmi tam-liste** Gold Partner lockup'ı ile değiştirildi (Specialization: Product Design & Mfg., Building Architecture, Media & Entertainment, PLM, Design & Manufacturing Cloud + Value Added Services: Authorized Training Center, Authorized Developer, System Integrator). Şeffaf zeminli beyaz versiyon; çerçeve/kutu yok.
- **Kaynak dosya:** `5070268038-20230407083646.avif` (RGBA, 318×484, şeffaf) → PIL ile 2× LANCZOS → `assets/logos/autodesk-gold-partner-full-white.png` (636×968).
- **Etkilenen dosyalar:** cadbim_autodesk.html (img src + `.hero-badge img` genişlik clamp(200–290px) dikey logoya göre ayarlandı).
- **Doğrulama:** localhost — logo yüklendi (natural 636×968; masaüstü 282×429, hero metniyle 456px hizalı; mobil 200×304 ortalı); yatay taşma yok (1280 ve 375).
- **Durum:** ✅ Tamamlandı ve yayınlandı.
- **Referans:** commit (main) — aşağıda.

### DK-2026-07-21-20 — Autodesk hero: partner logo karmaşasını tek Gold Partner logosuna indirme

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** `cadbim_autodesk.html` hero'sundaki sağ rozet duvarı (7 kutu: Gold Partner, ATC, Service Provider, D&M Cloud, PD&M, M&E, PLM — beyaz kartlar) kaldırıldı. Yerine tek **Autodesk Gold Partner** logosu, çerçevesiz/beyaz-zeminsiz, koyu hero üzerinde beyaz (ters) versiyon (`autodesk-gold-partner-white.png`).
- **Etkilenen dosyalar:** cadbim_autodesk.html (markup: `.badgewall`→`.hero-badge`; CSS: `.bw-tile`/`.bw-wide` kuralları kaldırıldı, `.hero-badge` eklendi).
- **Doğrulama:** localhost — eski kutu sayısı 0, logo yüklendi (natural 845×215, masaüstü 358×91 / mobil 260×66), sağ sütunda, yatay taşma yok (1280 ve 375).
- **Durum:** ✅ Tamamlandı ve yayınlandı.
- **Referans:** commit (main) — aşağıda.

### DK-2026-07-20-01 — SEO: prefix'li canonical/og:url/JSON-LD düzeltmesi

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** 29 sayfada canonical, `og:url` ve yapısal veri (JSON-LD `@id`/`url`/breadcrumb) alanlarındaki `/cadbim-<slug>` biçimi hosting'de 404 veriyordu. Sitemap ve canlıda çalışan öneksiz `/<slug>` biçimine hizalandı.
- **Etkilenen dosyalar (29):** cadbim_advance_steel, cadbim_arnold, cadbim_autocad_lt, cadbim_autocad_web, cadbim_autodesk_drive, cadbim_design_review, cadbim_desktop_connector, cadbim_dwg_trueview, cadbim_factory_design, cadbim_featurecam, cadbim_flame, cadbim_flow_production_tracking, cadbim_flow_studio, cadbim_golaem, cadbim_infraworks, cadbim_maya, cadbim_maya_creative, cadbim_meshmixer, cadbim_moldflow, cadbim_motionbuilder, cadbim_mudbox, cadbim_navisworks, cadbim_netfabb, cadbim_powermill, cadbim_powershape, cadbim_recap_pro, cadbim_revit_lt, cadbim_robot_structural, cadbim_tinkercad (her birinde 7 örnek; toplam 203 değişiklik).
- **Yöntem:** Byte düzeyinde `cadbim.com.tr/cadbim-` → `cadbim.com.tr/` değişimi (UTF-8/BOM ve satır sonları korundu).
- **Doğrulama:** Canlı GitHub Pages'te `cadbim_maya.html` → canonical ve og:url `https://www.cadbim.com.tr/maya`; JSON-LD'de prefix kalmadı; 0 kırık görsel. Kalan prefix'li URL taraması: 0.
- **Durum:** ✅ Tamamlandı ve yayınlandı.
- **Referans:** commit `1eabbf9` (main); yayın: GitHub Pages build `built` (2026-07-20).

### DK-2026-07-20-02 — SEO teknik denetimi (dokümantasyon)

- **Kapsam:** 152 sayfa genelinde teknik SEO sağlık taraması yapıldı.
- **Sonuç (güçlü):** title, description, canonical, OG/Twitter, viewport, `lang="tr"`, görsel `alt` (%100), JSON-LD (151/152; `tesekkurler` bilinçli hariç), sitemap (151 URL) + robots — hepsi mevcut ve tutarlı.
- **Tespit edilen hosting davranışı (cadbim.com.tr, canlı test):** Öneksiz temiz URL çalışır (`/autocad`, `/advance-steel`); prefix'li biçim 404; `.html` uzantılı biçim HTTP 400.
- **Durum:** Denetim tamamlandı; DK-...-01 uygulandı.

- **AÇIK KARAR (bekliyor):** İç linkler hâlâ `.html` biçiminde (`href="cadbim_autocad.html"`). Eski site Wix ile yapılmış; temiz URL'ler Wix'ten geliyordu. Wix bırakılınca yeni deploy'un URL davranışı seçilecek host'a bağlı. İç link + canonical + sitemap şeması host netleşince kesinleşecek. Onur onayı bekliyor.

### DK-2026-07-20-03 — Claude Design "son sürüm" paketinin uygulanması

- **Yapan:** Onur Bozok (Claude Design export) + Claude (PDM asistanı)
- **Kaynak:** `C:\Users\o.bozok\Downloads\cadbim web site.zip` (Claude Design bundle, 2026-07-20 10:45; `site/` kökü + README + hash'li/hash'siz asset ikizleri).
- **Kapsam:** Onur'un Claude Design'da tamamladığı güncel sürüm repoya uygulandı. En büyük değişiklik `index.html` (64.7KB → 80.4KB, yenilenmiş ana sayfa); `cadbim_iletisim.html` küçük güncelleme; toplam 81 sayfada içerik değişikliği + `mobilenav.js` güncellendi + `README.md` eklendi.
- **Yöntem:** Zip staging'e açıldı; hash'li ikiz asset'ler (70 dosya) ayıklandı (HTML yalnızca hash'siz adları referans ediyor); `site/*.html`, `mobilenav.js`, hash'siz `assets/*` repoya kopyalandı. Kök SEO dosyaları (`sitemap.xml`, `robots.txt`, `favicon.svg`, `og-image.png`) pakette olmadığından repodakiler korundu. Asset içerikleri repodakiyle birebir aynı çıktı (fiili asset değişikliği yok).
- **Not — canonical:** Paket, DK-...-01'deki canonical düzeltmesini geri alıyordu (`/cadbim-maya` gibi 404 biçimi). Uygulama sonrası düzeltme tekrar geçildi (29 sayfa, öneksiz `/slug`). Kalan prefix'li URL: 0.
- **Doğrulama:** Yerel sunucu (localhost:8420) — ana sayfa ve görsel-yoğun autodesk sayfası; konsol hatası yok, varlıklar 200, gerçek kırık görsel yok (rozetler `loading=lazy`, fetch 200). `index.html` = 80363 byte.
- **Durum:** ✅ Uygulandı ve doğrulandı; commit + push aşağıda.

### DK-2026-07-20-04 — Ana sayfa başlık/açıklama iyileştirmesi + yerel vurgu kaldırma

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam (index.html):**
  - Başlık/og/twitter: "Autodesk & Adobe Gold Partner | İzmir" → **"Autodesk Gold Partner & Tasarım Teknolojileri"** (şehir/ülke ibaresiz). İzmir yerel algısı yaratıyordu; "Türkiye" de gereksiz karakter olduğu için tamamen kaldırıldı.
  - Meta/og/twitter açıklamaları: portföy + hizmet + sektör birleştirildi. **Marka doğruluğu:** yalnızca Autodesk "Gold Partner"; Adobe/HP/Microsoft/Chaos/UltiMaker "yetkili iş ortağı" (önceki metin Adobe'yi de Gold gösteriyordu — düzeltildi).
  - Hero dekoratif koordinatından "— İZMİR" kaldırıldı (statik satır + dinamik JS güncellemesi).
- **Korundu:** JSON-LD adres şeması (faktüel İzmir merkez; yerel SEO/Haritalar) ve görünür "İzmir Merkez Ofis" etiketi (Onur tercihi).
- **Doğrulama:** localhost:8420 — sekme başlığı ve hero koordinatı güncel; İzmir ibaresi hero'da yok.
- **Durum:** ✅ Uygulandı ve doğrulandı.

### DK-2026-07-20-05 — Site geneli marka/yerel tarama + Adobe statü düzeltmesi

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Tarama sonucu:** "Autodesk & Adobe" dar çerçevesi site geneli DEĞİL — yalnızca `index.html` (footer), `cadbim_hakkimizda.html`, `cadbim_adobe.html`. İzmir 57 sayfada (125 kez) ama çoğu meşru (iletişim adresi, KVKK yasal, footer/schema).
- **Adobe statüsü:** Onur teyit etti → **Adobe Gold Reseller Partner** (sitenin adobe sayfası da öyle diyor). DK-...-04'te ana sayfada Adobe'yi hatalı biçimde "yetkili iş ortağı"na indirmiştim; düzeltildi.
- **Değişiklikler:**
  - `index.html` meta/og/twitter açıklamaları: Adobe → "Autodesk Gold Partner ve Adobe Gold Reseller Partner"; HP/Microsoft/(Chaos)/UltiMaker "yetkili iş ortağı".
  - `cadbim_hakkimizda.html` meta: "İzmir ve Ankara" ibaresi kaldırıldı; Adobe statüsü doğru yazıldı.
- **Dokunulmadı (zaten doğru):** adobe sayfası "Gold Reseller Partner" rozeti, hakkımızda gövde metni, footer "İzmir Merkez Ofis" (Onur tercihi), JSON-LD adres şeması.
- **Doğrulama:** localhost:8420 — ana sayfa meta/og "Adobe Gold Reseller Partner" içeriyor.
- **Durum:** ✅ Uygulandı ve doğrulandı.

### DK-2026-07-20-06 — Metin rötuşları: hakkımızda sosyal açıklama + ana sayfa footer

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:**
  - `cadbim_hakkimizda.html` og/twitter açıklaması: "Autodesk & Adobe Gold Partner" → "Autodesk Gold Partner, Adobe Gold Reseller Partner" (tam ve doğru statü).
  - `index.html` footer: "Autodesk ve Adobe Gold İş Ortağı." → tam portföy: "Autodesk Gold Partner ve Adobe Gold Reseller Partner; HP, Microsoft, Chaos ve UltiMaker yetkili iş ortağı."
- **Doğrulama:** localhost:8420 — footer metni tam portföyü gösteriyor.
- **Durum:** ✅ Uygulandı ve doğrulandı.

### DK-2026-07-20-07 — DesignJet sayfalarına ürün görseli + broşür (BATCH — devam ediyor)

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Amaç:** Sitedeki DesignJet sayfalarında ürün görseli yoktu; ekleniyor.
- **Kaynak kararları (Onur):** Ürün görselleri **HP resmi DAM CDN**'inden (temiz, şeffaf-zemin PNG); broşür PDF'leri **cadbim.com.tr**'den; video HP'den (varsa YouTube gömme). "En iyi çaba batch" — kalite sonra birlikte ayıklanacak.
- **Şablon:** hero altına yeni bölüm — beyaz kartta ürün görseli (`width:100%`/`height:auto`, oran korunur) + "Broşür İndir (PDF)" butonu (`btn-p`); Product JSON-LD `image` alanı ürün görseline güncellenir. Görseller `assets/products/`, PDF'ler `assets/brochures/`.
- **Kapsam (13 birebir eşleşen):** t1600, t2600, t830, t850, t950, t1700, xl3600, xl3800, z6pro, z9pro, z6ps, z9ps, tarayıcılar.
- **Hariç (rapor):** t200/t600 (canlıda ad farkı: T230/T630), t870/z6810/smart_tank (kaynak yok).
- **Kesinleşen kaynak kararları:** Görsel = HP (Onur'un indirdiği HP asset kitleri, `assets/products/designjet/` — gitignore'da); PDF = cadbim.com.tr broşürleri; **Video = CADBİM YouTube kanalı** (iframe embed, repoya video konmaz — mp4'ler 2.5GB, bazıları >100MB); Tarayıcı = `tarayıcılar` sayfası **sd_pro + hd_pro** iki ayrı sayfaya bölünecek (hub yok).
- **Görsel hazırlığı:** 13 model görseli seçildi, 1400px'e küçültüldü, şeffaf PNG'ler beyaz zemine düzleştirilip JPG yapıldı (47–236KB). `assets/products/hp-designjet-*.jpg` + `hp-scanner-{sd,hd}-pro.jpg`.
- **Tamamlanan (11 ürün sayfası, görsel+broşür, yayında):** t1600, t2600, xl3600, z6pro, z9pro, t1700, t830, t200(T230 görseli), t600(T630 görseli), z6ps, z9ps. Commit'ler: f8b9c14, 3d481cb, 07847d3, ac871b8.
- **Tarayıcı bölme ✅:** `cadbim_designjet_tarayicilar.html` silindi; yerine `cadbim_designjet_sd_pro.html` (SD Pro 2, 44" CIS) ve `cadbim_designjet_hd_pro.html` (HD Pro 2, 42" CCD) oluşturuldu. Her biri kendi görseli + cadbim broşürü + scanner'a özgü title/meta/canonical/JSON-LD/hero. sitemap 2 yeni URL (designjet-sd-pro, designjet-hd-pro); designjet.html kategori kartı 2'ye bölündü. Dangling referans yok, eski slug 404.
- **Şeffaf görsel ✅ (Onur "beyaz fonu sevmedim, kesip PNG yap"):** 13 DesignJet sayfasının tamamı beyaz kart yerine **şeffaf ürün PNG + hafif cyan glow**. 9'u şeffaf kaynaktan (folder PNG / HP DAM c-png), 4'ü (xl3600, z6pro, sd-pro, hd-pro) `rembg` (yerel u2netp) ile kesildi. z6pro "SALE" posteri temiz görselle değişti. Görseller 1200px, ~200KB-1MB.
- **Kategori thumbnail ✅:** `cadbim_designjet.html` kataloğunda görseli olan 13 modelin kartındaki jenerik ikon, küçük şeffaf ürün PNG'siyle değiştirildi. HP seri sayfalarında (t/xl/z) ürün galerisi yok (yalnızca çapraz-link), dokunulmadı.
- **HP YouTube videoları ✅:** 9 modele HP resmi tanıtım videosu responsive iframe ile gömüldü (hero altı): t1600, t2600, z6pro, z9pro, t200(T250), t600(T630), xl3600, t830, t1700. z6ps/z9ps ve tarayıcılar için net resmi ürün videosu yok (tutorial/3. taraf) → atlandı.
- **Durum:** ✅ DesignJet medya işi tamam — 13 sayfa şeffaf ürün görseli + broşür, kategori thumbnail'leri, 9 video. Kalan opsiyonel: assetsiz modeller (t850/t950/t870/z6810/xl3800/smart_tank) ve scanner/z-ps videoları.

### DK-2026-07-20-09 — Sürüm yedeği (bulut + local)

- **Bulut:** git tag **`v2026.07.20`** (commit `3f2da76`) oluşturulup GitHub'a push edildi. `main` güncel.
- **Local:** `C:\Users\o.bozok\Downloads\cadbim_site_yedek_2026-07-20.zip` (`git archive HEAD`, ~25MB, 265 dosya) — deploy edilebilir site; .git/.claude/ham-asset (`assets/products/designjet/`) hariç.
- **Kapsananlar:** DesignJet medya (şeffaf görsel+broşür+kategori thumbnail), IA yeniden sıralama+carousel, tarayıcı 2 sayfa, üst menü beyaz. **Videolar kaldırıldı** (yalnızca @HPGraphicArts linkleri beklendiği için — YouTube bana kapalı, Onur linkleri verecek).

### DK-2026-07-20-08 — DesignJet bilgi mimarisi (bölüm sırası) düzeltmesi

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur hedef sırayı onayladı.
- **Sorun:** Ürün sayfalarında özellikler, video+çözümler bloklarının ALTINDA kalıyordu ("karmaşa"); kategoride katalog, teklif/çözüm linklerinin altındaydı.
- **Ürün sayfaları (13):** yeni sıra = hero → ürün görseli → **Öne Çıkan Özellikler → Modeller/Varyantlar** → Tanıtım videosu → İlgili çözümler → **Diğer DesignJet Modelleri (kaydırmalı carousel, thumbnail'li)** → Cadbim Farkı → **CTA (Teklif İste + Broşür İndir)**. Python regex ile blok yeniden sıralama; section dengesi doğrulandı.
- **Kategori (`cadbim_designjet.html`):** katalog (ürünler) hero'nun hemen altına; ilgili çözümler/marka linkleri aşağı. Ekran görüntüsüyle doğrulandı.
- **AÇIK — site geneli:** Onur "tüm siteyi bu mantıkla denetle" dedi. Marka (autodesk/adobe/hp/chaos/ultimaker/microsoft/sketchup/lumion), çözüm ve endüstri sayfalarında da "içerik/ürünler önce, ilgili/CTA sonra" denetimi + düzeltmesi yapılacak (çözüm/endüstri sayfaları önceki turda kısmen düzeltilmişti).
- **Durum:** 🔄 DesignJet bitti; site geneli audit kaldı.
- **Not:** z6pro görselinde çıktı "SALE" posteri — ileride değiştirilebilir. Atlananlar: t730 (EOL), t850, t950, t870, z6810, xl3800, smart_tank (kaynak yok).
- **Durum:** 🔄 Tüm sayfalar (13 ürün + 2 scanner) görsel+broşürlü; yalnızca video kaldı.

### DK-2026-07-20-10 — DesignJet: T870 + XL3600 tanıtım videosu gömüldü

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur video linklerini verdi.
- **Kaynak:** Onur iki YouTube linki iletti (HP resmi videolar):
  - `cuvHfdbQaNE` → "HP DesignJet XL 3600 MFP Series. Extreme reliability, compact size." → `cadbim_designjet_xl3600.html`
  - `CNG6QSRUDSQ` → "HP DesignJet T870 A1 Plotter — Versatile large-format 24-inch Printer" → `cadbim_designjet_t870.html`
- **Uygulama:** Her iki sayfada "Modeller & Varyantlar" bölümünden sonra responsive 16:9 iframe (padding-bottom:56.25%, loading=lazy). Gizlilik/KVKK için **`youtube-nocookie.com`** kullanıldı (önceki blokların `youtube.com/embed` yerine).
- **Doğrulama:** Her iki embed URL'i tarayıcıda açıldı — oynatıcı yükleniyor, "video kullanılamıyor" hatası yok, embed'e izin veriliyor. Dosyalarda tek iframe/tek video bölümü (grep ile teyit).
- **Not:** T870 ve XL3600 daha önce "kaynak yok" diye atlanmıştı (DK-08); bu linklerle kapatıldı. Kalan videosuz: t850, t950, z6810, xl3800, smart_tank, z6ps, z9ps, sd_pro, hd_pro.
- **Durum:** ✅ Uygulandı ve doğrulandı.

### DK-2026-07-20-11 — HP video kaynak politikası + T850 videosu (hp.com yöntemi)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "hp.com yöntemini standart yap, T850'den başla" dedi.
- **Politika kararı:** Video kaynağı standardı belirlendi → `docs/HP-VIDEO-KAYNAK-POLITIKASI.md`. Birincil yöntem: ürünün **resmi hp.com sayfasını tarayıcıda açıp** video ID'sini oradan almak (hp.com ne koyduysa resmi + doğru üründür). Yedek: onaylı HP resmi kanalları whitelist'i. Bayi/3. şahıs (HP Plotter=Resolution GB, ACP techWERK, vb.) ve HPE reddedilir.
- **T850 ✅:** hp.com T850/T870/T950 seri sayfasından resmi video ID `hRa2oRinXyc` ("HP DesignJet T850, T870 and T950... Compact Size. Cutting-Edge Results", kanal: HP) alındı. `cadbim_designjet_t850.html`e "Modeller & Varyantlar" sonrası nocookie iframe ile gömüldü. Embed tarayıcıda test edildi (oynatıcı yüklendi, hata yok).
- **Ek bulgu:** Aynı seri videosu (`hRa2oRinXyc`) T870 + T950'yi de kapsıyor → o sayfalar için de resmi seçenek. T870 şu an Onur'un verdiği `CNG6QSRUDSQ` ile; değiştirilmedi (Onur onayı olmadan dokunulmaz).
- **Doğrulama tuzakları netleşti:** "HP Construction" adında resmi kanal YOK; AEC içeriği ana/bölgesel kanal + hp.com blogda. İsimde "HP" geçen bayi kanalları resmi değil.
- **Durum:** ✅ Politika + T850 tamam. Kalan: t950, z6810, xl3800, smart_tank, z6ps, z9ps, sd_pro, hd_pro (hp.com yöntemiyle sırayla).

### DK-2026-07-20-12 — T950 videosu (seri videosu, T850 ile ortak)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "aynı videoyu 2 ürün içinde kullanabilirsin" dedi.
- **T950 ✅:** hp.com seri videosu `hRa2oRinXyc` (T850/T870/T950'yi birlikte anlatan resmi HP videosu) `cadbim_designjet_t950.html`e gömüldü — T850 ile aynı. Şablon aynı (Modeller sonrası, nocookie, lazy). Video daha önce doğrulanmıştı (oynatıcı yükleniyor).
- **T870 dokunulmadı:** Onur'un verdiği `CNG6QSRUDSQ` ile kalıyor (kendi onayı olmadan değiştirilmez).
- **Durum:** ✅ T950 tamam. Kalan: xl3800, z6ps, z9ps, z6810, smart_tank, sd_pro, hd_pro.

### DK-2026-07-20-13 — DesignJet video batch: hp.com yöntemiyle 7 sayfa daha

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "hepsini yap" dedi.
- **Kapsam:** 15 videosuz DesignJet sayfası hp.com yöntemiyle tarandı (her ürünün resmi hp.com sayfası tarayıcıda açılıp video ID'si oradan alındı).
- **Gömülen (7, nocookie iframe, Modeller sonrası):**
  - t200 → hzxO73kldmc · t600 → 6WzCOBtWuGQ (ikisi de "Simple. Compact. Responsible.", HP)
  - t1600 + t2600 → ZEnzBgbS2yk (hp.com "Build Connected" seri videosu, ortak — Onur "aynı video 2 ürün" onayı)
  - xl3800 → MbASXZgN3tI · z6pro → EgbZf_9Ewjg (ikisi hp.com sayfasından, HP)
  - z9pro → zj8HtwqYn7w (resmi HP "Introducing Z6/Z9 Pro"; hp.com Z9 sayfası self-host, fallback). Embed test edildi.
- **Videosuz bırakılan (7, resmi yok):** t830, t1700, z6810, z6ps, z9ps, sd_pro, hd_pro. Gerekçeler politika dosyasında.
- **Reddedilen bayi videoları (doğrulama tuttu):** "HP DesignJet T830 Product Video" = GDS/Graphic Design Supplies Ltd (bayi); "T1600 & T2600 Product Video" = GOM Australia (bayi). İsim/başlık HP içerse de resmi değil → alınmadı.
- **Not:** t830/t1600/t2600 için hp.com'da temiz tekil ürün videosu yoktu; t1600/t2600'de "Build Connected" seri videosu kullanıldı. z6pro/z9pro daha önce (eski turda) kaldırılan sayfalardı; artık doğru resmi videolarla geri kondu.
- **smart_tank ✅:** hp.com Smart Tank sayfasında YouTube yoktu; resmi **HP Asia** kanalından (whitelist'te onaylı bölgesel resmi kanal) `zsYVMY0h3uU` ("Smart Tank T858 plotter and T908 MFP: HP's First Large Format Ink Tank Printer") alındı, embed test edildi, gömüldü.
- **Durum:** ✅ Batch tamam. Toplam **videolu: 12 sayfa** (t200,t600,t850,t870,t950,t1600,t2600,xl3600,xl3800,z6pro,z9pro,smart_tank). **Videosuz: 7** (t830,t1700,z6810,z6ps,z9ps,sd_pro,hd_pro — resmi video yok).

### DK-2026-07-20-14 — VideoObject schema (SEO) 11 sayfaya eklendi

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "VideoObject ekle" onayı.
- **Amaç:** Gömülü videoların Google'da video zengin sonucu (thumbnail+süre) üretebilmesi için schema.org VideoObject yapısal verisi.
- **Yöntem:** Her videonun GERÇEK metadata'sı YouTube watch sayfasından çekildi (uydurma yok): name (resmi başlık), uploadDate, duration (lengthSeconds→ISO8601), thumbnailUrl (i.ytimg.com/hqdefault). embedUrl (nocookie) + contentUrl + publisher=HP.
- **Eklenen (11):** t200, t600, t850, t950, t1600, t2600, xl3600, xl3800, z6pro, z9pro, smart_tank. Video bölümünden sonra ayrı ld+json bloğu. 11'i de JSON parse + zorunlu alan kontrolünden geçti.
- **Kanal doğrulaması (metadata sırasında):** hp.com kaynaklı videoların kanalları teyit edildi — HP, HP Construction Technology (T200/T600/T850-serisi/T1600-T2600), HP WW Studio (XL3600), HP Asia (Smart Tank). Hepsi resmi HP.
- **⚠️ T870 hariç bırakıldı:** T870 videosu (CNG6QSRUDSQ, Onur'un verdiği) kanalı **"Plot it"** = bayi, resmi HP değil. Politikaya aykırı olduğu için VideoObject eklenmedi; Onur'a swap önerisi (hRa2oRinXyc seri videosu T870'i de kapsıyor) sunulacak.
- **Yan bulgu (kapsam dışı):** sd_pro + hd_pro sayfalarının MEVCUT head JSON-LD'sinde önceden var olan JSON syntax hatası (muhtemelen kaçışsız " — 44"/42" ölçüleri). Bu iki sayfanın tüm yapısal verisi bozuk; ayrı düzeltilmeli.
- **Durum:** ✅ 11 VideoObject yayında. Açık: T870 kararı + scanner JSON fix.

### DK-2026-07-20-15 — T870 videosu resmi seriyle değiştirildi + scanner JSON-LD fix

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur her iki kararı onayladı.
- **T870 ✅:** Bayi kanalı videosu (CNG6QSRUDSQ "Plot it") → resmi HP seri videosu `hRa2oRinXyc` ("T850, T870 and T950", HP Construction Technology) ile değiştirildi. Ayrıca VideoObject eklendi. Artık T870 da politikaya uygun ve SEO schema'lı.
- **Scanner JSON fix ✅:** `sd_pro` ve `hd_pro` sayfalarının head JSON-LD `name` alanındaki kaçışsız `"` (44"/42") → `\"` yapıldı. Önceden bu iki sayfanın TÜM structured data'sı Google için geçersizdi; artık geçerli.
- **Doğrulama:** Tüm DesignJet sayfaları JSON parse edildi → 12 geçerli VideoObject, scanner head JSON'ları da parse oluyor, 0 hata.
- **Durum:** ✅ Tamam. Videolu 12 sayfanın tamamı resmi HP + VideoObject'li. Videosuz 7: t830, t1700, z6810, z6ps, z9ps + scanner'lar (sd/hd_pro resmi ürün videosu yok).

## 2026-07-21

### DK-2026-07-21-01 — Autodesk ürün sayfalarına resmi ürün logoları eklendi

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur resmi Autodesk ürün ikon paketini verdi (`Downloads/Autodesk Products/Original Format`, 125 `*-product-icons.zip`).
- **Sorun:** Autodesk ürün sayfalarının çoğunda hero'da gerçek ürün logosu yerine jenerik Tabler ikon kutusu vardı (yalnızca 8 sayfada logo vardı: autocad, revit, civil3d, fusion, fusion_manage, inventor, alias, vault_pdm).
- **Yapılan:** İlgili zip'lerden resmi **SVG** ürün ikonları çıkarıldı → `assets/logos/products/*.svg` (35 ikon). Her sayfanın hero rozeti (jenerik `<i class="ti">` kutusu / metin rozeti) resmi ürün SVG'siyle değiştirildi: `<img ... width:56px;height:56px;object-fit:contain>` (şeffaf 3B ikon olduğu için gölge/radius yok, oran korunur).
- **Kapsam (35 sayfa):** 3dsmax, advance_steel, arnold, autocad_lt, autocad_web, autodesk_drive, autodesk_docs, design_review, desktop_connector, factory_design, featurecam, flame, flow_production_tracking, flow_studio, golaem, infraworks, maya, maya_creative, moldflow, motionbuilder, mudbox, navisworks, nesting, netfabb, powermill, powershape, recap_pro, revit_lt, robot_structural, tandem, vehicle_tracking, aec_collection, bim_collaborate_pro, me_collection, pdm_collection.
- **Ayıklama (dokunulmadı):** Adobe (photoshop, illustrator vb.), Chaos (corona, phoenix, vantage, cosmos), UltiMaker/3D baskı (cura, method_xl, factor4, sketch_sprint), Trimble, ANIMA ve çözüm/konsept sayfaları (bim, plm, simulasyon...) — hero'daki "AUTODESK" etiketiyle filtrelendi.
- **İkon bulunamayan (atlandı, sayfa logosuz kaldı):** forma, tinkercad, meshmixer, dwg_trueview — verilen ikon setinde karşılığı yok.
- **Doğrulama:** Yerel sunucuda (localhost:8777) advance_steel, 3dsmax (eski metin rozeti), aec_collection (farklı en-boy) DOM ile kontrol edildi — SVG'ler yükleniyor, 56×56, object-fit:contain, kırık görsel yok. Otomatik tarama: 35 referans = 35 benzersiz ikon, 0 kırık, 0 kullanılmayan.
- **Durum:** ✅ Uygulandı ve doğrulandı.

### DK-2026-07-21-02 — Ürün logoları çözüm/collection/endüstri/eğitim sayfalarındaki pill'lere yayıldı

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "bu ürün logolarını çözüm/collection/endüstri/eğitim sayfalarında kullan" dedi.
- **Sorun:** Bu sayfalardaki ürün-link pill'leri (`class="cp"`) Autodesk ürünleri için jenerik `autodesk-white.svg` veya Tabler `ti` ikonu kullanıyordu (marka logosu mantığı vardı: Chaos→chaos.webp, UltiMaker→ultimaker.svg, ama Autodesk ürünleri için tekil logo yoktu).
- **Yapılan:** Autodesk ürününe giden her `cp` pill'inin ikonu, ürünün kendi SVG logosuyla değiştirildi (`assets/logos/products/*.svg`, height:14px). Pill'lerde geçen ama daha önce çıkarılmamış 7 ürün (autocad, revit, civil3d, fusion, fusion_manage, inventor, vault_pdm) SVG'si de eklendi → products klasörü 42 ikon.
- **Kapsam:** 92 pill / 22 sayfa. Collection (aec/me/pdm: 14+11+11), çözüm sayfaları (bim, plm, pdm, simulasyon, cam, dijital_ikiz, nesting, insaat_yonetimi, gerceklik_yakalama, vb.), endüstri (sektor_havacilik/makine/insaat/mimari/otomotiv).
- **Korundu (doğru davranış):** Adobe/Chaos/UltiMaker/SketchUp/Lumion/HP/Microsoft marka logoları; çözüm-konsept (bim, construction_cloud) ve endüstri linkleri; SVG'si olmayan Autodesk ürünleri (forma, tinkercad). Yalnızca `products/<slug>.svg` mevcutsa değiştirildi.
- **Doğrulama:** localhost — aec_collection (18 pill'in 14'ü logo, hepsi yüklü) ve bim (Autodesk ürünleri logo aldı; chaos.webp/ultimaker.svg korundu; sektor_* linkleri ti ikonda kaldı). 0 kırık görsel.
- **Durum:** ✅ Uygulandı ve doğrulandı.

### DK-2026-07-21-03 — Forma ürün ikonu autodesk.com'dan eklendi (beyaz)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "Forma'yı beyaza çevirip kullan; Tinkercad/Meshmixer/DWG TrueView aynı kalsın" dedi.
- **Kaynak:** autodesk.com Forma sayfasından resmi `forma-product-icon.svg` (images.ctfassets.net). Orijinal siyah monokrom glif → koyu temada görünsün diye `fill="#ffffff"` yapıldı → `assets/logos/products/forma.svg`.
- **Uygulama:** cadbim_forma.html hero rozeti (jenerik gradient+ti ikonu) → beyaz Forma SVG'si (diğer 35 ürünle aynı bare-icon deseni, 56px). 4 kategorideki forma cp-pill'leri de logoyu aldı (aec_collection ×2, dijital_ikiz ×1).
- **Atlanan (Onur kararı):** Tinkercad (yalnızca yatay wordmark), Meshmixer (kaldırılmış ürün, kalıcı asset yok), DWG TrueView (viewer, ürün ikonu yok) → mevcut Tabler ikonlarında bırakıldı.
- **Not:** Autodesk güncel ürün ikonları sade monokrom glif (ctfassets); zip'teki renkli 3B kutulardan stil farkı var. Forma tek monokrom beyaz ikon olarak duruyor (Onur onayladı).
- **Doğrulama:** localhost — forma hero beyaz glif yüklü (56px, koyu zeminde kontrastlı). products klasörü 43 SVG.
- **Durum:** ✅ Uygulandı ve doğrulandı.

### DK-2026-07-21-04 — Tinkercad + Meshmixer logoları eklendi (Onur'un verdiği)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur logoları İndirilenler klasörüne koydu.
- **Tinkercad:** `tinkercad-lockup-white.svg` (beyaz yatay wordmark) → `assets/logos/products/tinkercad.svg`. cadbim_tinkercad.html hero rozeti (jenerik ti-cube) → wordmark (height:34px). Wordmark olduğu için pill'lere uygulanmadı (metin etiketiyle tekrar olurdu).
- **Meshmixer:** `meshmixer.png` (renkli low-poly kare ikon, 120×120) → `assets/logos/products/meshmixer.png`. cadbim_meshmixer.html hero rozeti → ikon (56px, object-fit:contain, diğer ürünlerle aynı desen).
- **DWG TrueView:** autodesk.com/products/dwg-trueview/overview sayfası tarandı — üründe **logo/ikon yok** (yalnızca arayüz ekran görüntüsü). Alınamadı; sayfa mevcut Tabler ikonuyla kaldı.
- **Doğrulama:** localhost — meshmixer (120×120 PNG, 56px yüklü) ve tinkercad (wordmark 129×34 yüklü). products klasörü 45 asset (43 svg + tinkercad.svg + meshmixer.png; forma dahil).
- **Not:** Tinkercad hero'da wordmark + "Tinkercad" metin etiketi bir miktar tekrar oluşturuyor; istenirse metin etiketi sadeleştirilebilir.
- **Durum:** ✅ Tinkercad + Meshmixer uygulandı. DWG TrueView'da logo yok.

### DK-2026-07-21-05 — DWG TrueView logosu bulundu ve eklendi

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur ekran görüntüsüyle logonun hero'da olduğunu gösterdi.
- **Düzeltme:** DK-04'te "DWG TrueView'da logo yok" demiştim — yanlıştı. Logo, autodesk.com sayfasında **inline SVG** olarak gömülüydü (img/CDN taraması kaçırmıştı). DOM'da hero eyebrow'un kardeş öğesinde bulundu.
- **Kaynak/uygulama:** Inline SVG (viewBox 965×880, kırmızı "D": #78082A/#E51050/#E85984 + beyaz harf) çıkarıldı → `assets/logos/products/dwg-trueview.svg`. **Zip ikonlarıyla birebir aynı detaylı 3B-kutu stili** — mükemmel uyum. cadbim_dwg_trueview.html hero (jenerik ti-file-search) → ikon (56px). sektor_egitim.html'deki dwg pill'i de logoyu aldı.
- **Doğrulama:** localhost — hero SVG yüklü (164×150 doğal, 56px, object-fit:contain), kırmızı D render oluyor.
- **Durum:** ✅ Eklendi. Böylece 4 eksik ikon da tamamlandı: Forma, Tinkercad, Meshmixer, DWG TrueView.

### DK-2026-07-21-06 — Ürünler sayfası (cadbim_urunler.html) Autodesk ürün logoları

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "ürün logoları eski tip, elindekilerle güncelle" dedi.
- **Sorun:** Ürünler sayfasındaki kartlarda (`.pcard`) jenerik Tabler ikonları (`ti ti-*`) vardı.
- **Yapılan:** Her kartın `.pico` kutusundaki jenerik ikon, ürünün resmi logosuyla değiştirildi (kutu korundu, içine 28px `object-fit:contain` logo). Alias ikonu da zip'ten çıkarıldı (`alias.svg`).
- **Kapsam:** 45 Autodesk ürün kartı (koleksiyonlar dahil). Toplam 88 karttan.
- **Bilerek yapılmadı:** Adobe/Chaos/UltiMaker/Microsoft ürün kartları — bu markaların logoları **koyu zeminde görünmez** (ultimaker.svg çoğunlukla `fill=black`, microsoft %100 siyah). Mevcut renkli Tabler ikonları görünür olduğu için korundu (siyah logo koymaktan iyi). Tinkercad (yatay wordmark, 42px kare kutuya uymaz) ve logosuz olanlar (construction_cloud, anima, digital_factory, trimble_connect, hp_*) da olduğu gibi kaldı.
- **Doğrulama:** localhost — 45 ürün logosu yüklü, 0 kırık, kutu içinde 28×28.
- **Durum:** ✅ Autodesk ürün kartları güncellendi.

### DK-2026-07-21-07 — "Forma" adlandırma karışıklığı düzeltmesi (ürünler sayfası)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur ürünler sayfasında "hem Autodesk Forma hem Forma var" karışıklığını sordu.
- **Kök neden (araştırıldı):** Autodesk 2025 rebrand — Construction Cloud → **Autodesk Forma** (endüstri bulutu), Autodesk Docs → **Forma Data Management**. Eskiden tek başına "Autodesk Forma" olan tasarım ürünü → artık **"Forma Site Design"**. Site zaten yeni markalamayı kullanıyordu; tek eksik, tasarım ürününün "Forma" olarak kalmasıydı (şemsiye markayla çakışıyordu).
- **Düzeltme:** cadbim_urunler.html'de `forma.html` kartı **"Forma" → "Forma Site Design"**. Böylece endüstri bulutu ("Autodesk Forma" → construction_cloud) ile tasarım uygulaması ("Forma Site Design" → forma) net ayrışıyor.
- **Doğrulama:** 4 Forma kartı artık ayrı adlarda (Forma Site Design / Autodesk Forma / …Design Collaboration / …Data Management).
- **Açık (opsiyonel):** forma.html sayfasının kendi başlığı/hero'su hâlâ "Forma Building Design"; tam tutarlılık için "Forma Site Design"a çekilebilir (Onur onayı bekliyor).
- **Not:** Önceki turda bu kartları hatalı biçimde "yanlış etiketlenmiş" demiştim — düzeltme: site aslında güncel Autodesk markalamasını kullanıyor.
- **Durum:** ✅ Ürünler sayfası karışıklığı giderildi.

### DK-2026-07-21-08 — Forma tam tutarlılık + ürünler sayfasında gruplama

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "tam tutarlı olsun, Forma grubu yan yana dursun" dedi.
- **forma.html:** "Forma Building Design" → **"Forma Site Design"** (title, meta, og, twitter, JSON-LD — 12 yer). Hero adı "Building Design" → "Site Design" (eyebrow "AUTODESK FORMA" korundu → "Autodesk Forma / Site Design" okunur). Kalan "Building Design" → "Site Design" (2 yer). Artık sayfa baştan sona resmi "Forma Site Design" adını kullanıyor.
- **cadbim_urunler.html:** "Forma Site Design" kartı, diğer 3 Forma kartının (Autodesk Forma / …Design Collaboration / …Data Management) yanına taşındı → **4 Forma ürünü artık yan yana**.
- **Doğrulama:** pcard sayısı 88 (değişmedi), section dengesi 4/4, forma.html'de "Building Design" kalmadı, sıra: InfraWorks → [Forma Site Design, Autodesk Forma, …Design Collaboration, …Data Management] → Vehicle Tracking.
- **Durum:** ✅ Forma adlandırması tutarlı + gruplandı.

### DK-2026-07-21-09 — Autodesk Forma platform yapısı (hub + gruplama)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "Forma grubunu iyi anlatan bir yapı, gerekirse üst sayfada platformu yansıtan" istedi. Onaylar: construction_cloud'u dönüştür + ürünler sayfasında alt-başlık+modüller.
- **Hub (cadbim_construction_cloud.html → Autodesk Forma platformu):**
  - Hero platform seviyesine genişletildi: eyebrow alt satırı "Site Design · Data Management · Design Collaboration · Build · Takeoff"; H1 "AEC Endüstri Bulutu — Tasarımdan Sahaya"; giriş paragrafı Site Design dahil tüm modülleri anlatıyor (+"Eski adı Autodesk Construction Cloud").
  - **Yeni "Platform Modülleri" bölümü:** 4 linkli kart — Forma Site Design → forma, Forma Data Management → autodesk_docs, Forma Design Collaboration → bim_collaborate_pro, Build & Takeoff → insaat_yonetimi. Her kart ürün logolu + "İncele →".
  - Başlık/meta: "İnşaat Yönetim Platformu" → "AEC Endüstri Bulutu" (4 yer: title/og/twitter).
- **Ürünler sayfası (cadbim_urunler.html):** 4 Forma kartı AEC grid'inden çıkarılıp **"Autodesk Forma Platformu"** etiketli ayrı grid'e alındı (Forma logosu + açıklama + "Platforma genel bakış →" construction_cloud'a link). Grup artık net ayrışıyor.
- **Doğrulama:** localhost — hub 4 modül kartı doğru sayfalara linkli, logolar yüklü; ürünler alt-grubu etiketli, 4 kart ayrı grid; 0 kırık. section 6/6, div 147/147, 88 kart korundu.
- **Durum:** ✅ Forma platform yapısı kuruldu.

### DK-2026-07-21-10 — Ürünler sayfası logo tamamlama: Adobe + marka logoları

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "her ürünün logosu olsun, gerekirse vendor resmi sitesinden al" dedi.
- **Adobe (Onur'un 'adobe logolar' klasöründen):** 9 ürün app ikonu SVG çıkarıldı (photoshop, illustrator, indesign, premiere-pro, after-effects, lightroom, firefly, adobe-express, adobe-stock) + acrobat.svg + adobe.png (Creative Cloud). Ürünler sayfası 9 Adobe kartına uygulandı; adobe.html'de eksik olan **Acrobat kartı** gerçek app ikonuyla güncellendi (diğer 7 zaten inline SVG ikonluydu).
- **Marka logoları (koyu zeminde görünür olanlar):** HP ürünleri (6) → hp-blue.png; Chaos (chaos/corona/vantage/phoenix/cosmos) → chaos.webp; Lumion (lumion/view/cloud) → lumion.png. construction_cloud ("Autodesk Forma") → forma.svg; adobe markası → adobe.png (Creative Cloud).
- **Kalan (vendor fetch gerek — koyu/wordmark/dosya yok):** substance3d, cura, method_xl, sketch_sprint, sketchup, sketchup_go, microsoft, trimble_connect, anima, digital_factory, tinkercad. Sıradaki adımda vendor resmi sitelerinden alınacak.
- **Durum:** 🔄 Ürünler sayfası logo tamamlama — Adobe + görünür markalar bitti; vendor-spesifik olanlar kaldı.

### DK-2026-07-21-11 — Ürünler sayfası: kalan tüm ürün logoları tamamlandı (88/88)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "her ürünün logosu olsun, gerekirse vendor resmi sitesinden al".
- **Vendor resmi sitelerinden çekilenler (curl):** UltiMaker favicon → ultimaker-icon.webp (cura, method_xl, sketch_sprint, factor4, ultimaker); SketchUp favicon.svg (#0063a3) → sketchup-icon.svg (sketchup, sketchup_go, sketchup_studio); Trimble apple-touch → trimble-icon.png (trimble_connect); AXYZ anima apple-touch → anima-icon.png; Tinkercad app_icon_512 → tinkercad-icon.png.
- **Elle oluşturulan:** microsoft.svg (resmi 4 renkli kare mark — koyu zeminde görünür).
- **Fallback:** substance3d → adobe.png (Creative Cloud). Adobe Substance sitesi SPA olduğu için curl ikon vermedi; geçerli Adobe-markalı ikon konuldu, Substance'a özel ikon bulununca değişecek. digital_factory → autodesk beyaz logo; construction_cloud → forma.svg.
- **Sonuç:** **88/88 ürün kartı logolu, 0 jenerik ikon, 0 kırık referans.** products klasörü 66 asset.
- **Not:** Bazı vendor ikonları favicon kaynaklı (kare, resmi ama app-icon değil). Tarayıcı bu turda kararsızdı; doğrulama dosya-bazlı (tüm img referansları mevcut dosyalara çözümleniyor).
- **Durum:** ✅ Ürünler sayfası logo tamamlama bitti.

### DK-2026-07-21-12 — Ana sayfa hero ekrana sığma düzeltmesi

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur ekran görüntüsüyle ana sayfanın ekrana sığmadığını gösterdi (istatistikler 30+/10.000+/7 alttan kesiliyordu).
- **Teşhis (tarayıcı ölçümü):** Yatay overflow YOK. Sorun dikey: hero içeriği yalnızca 514px ama `min-height:calc(100vh - 132px)` (940px ekranda 808px) + dikey ortalama → 294px boş alan; bu da hero'yu şişirip istatistik bölümünü ekran dışına itiyordu.
- **Düzeltme (index.html):** `.hero` min-height `calc(100vh - 132px)` → `calc(100vh - 260px)`; padding-top 80px → 72px. Boş alan 294→166px azaldı; içerik hâlâ dikey ortada, taşma yok.
- **Doğrulama (localhost, cache-buster):** 940px viewport'ta hero 808→680px, istatistikler tam görünür. 860px viewport'ta hero 606px, içerik sığıyor, istatistik tam görünür, 0 yatay overflow. Mobil/tablet breakpoint'leri (min-height:auto) etkilenmedi.
- **Durum:** ✅ Hero ekrana sığıyor.

### DK-2026-07-21-13 — Ana sayfa hero: küçük viewport/ölçekleme için ek sıkıştırma

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur hard-refresh sonrası hâlâ stats'ın kesildiğini bildirdi.
- **Teşhis:** DK-12 fix'i canlıda mevcuttu (curl+tarayıcı teyit), ama Onur'un ekranında Windows ölçekleme (%125/%150) efektif viewport'u küçültüyor → içerik (514px) + stats hâlâ sığmıyordu. 722px viewport'ta 11px, daha küçükte daha çok kesiliyordu.
- **Düzeltme (index.html hero):** min-height calc(100vh-260px)→calc(100vh-300px); padding-top 72→68; boşluklar sıkıştırıldı (eyebrow mb 22→14, h1 mb 20→14, sub mb 34→22, btns mb 34→8, btns gap 14→12); h1 clamp max 4rem→3.5rem. İçerik 514→~430px.
- **Doğrulama (localhost):** 722px viewport stats alt 647 (tam görünür); 648px viewport stats alt 644 (tam görünür, 4px pay); yatay overflow yok. ~%150 ölçeklemeye kadar sığıyor.
- **Not:** Onur'un gördüğü yarım-kesik büyük olasılıkla eski sürüm cache'iydi (düzeltilmiş sürüm en fazla birkaç px kesiyordu). Kesin çözüm için cache-buster URL (?v=) önerildi.
- **Durum:** ✅ Hero küçük viewport/ölçeklemede de sığıyor.

### DK-2026-07-21-14 — Ana sayfa hero: her ekranda tutarlı (içerik-boyutlu)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "her ekranda aynı olacak şekilde ayarla" dedi.
- **Değişiklik:** `.hero`'dan `min-height:calc(100vh - ...)` (viewport-bağımlı) kaldırıldı → hero artık **içerik-boyutlu, sabit** (padding 88/52). Böylece ekran yüksekliğinden bağımsız her ekranda AYNI hero yüksekliği (~572px), stats hep tutarlı konumda.
- **Doğrulama (localhost, çoklu boyut):** 1040px, 750px → hero 572px, stats tam görünür. 648px (uç %150 ölçekleme) → hero 569px (tutarlı) ama stats 48px altta. Yatay overflow yok. Hero yüksekliği tüm boyutlarda ~sabit (569-572).
- **Not:** Önceki vh-bağımlı yaklaşım küçük ekranda hero'yu küçültüyordu (sığdırıyordu ama ekrandan ekrana değişiyordu). Yeni yaklaşım tutarlılık önceliğinde; gerçek masaüstü viewport'larında (≥750px) stats tam görünür.
- **Durum:** ✅ Hero her ekranda tutarlı.

### DK-2026-07-21-15 — Substance 3D: Adobe sayfasından resmi ikonlar + içerik

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "substance ürününü adobe.com/tr/products/substance3d sayfasındaki gibi (içerik + görseller) istiyorum" dedi.
- **Görseller (adobe.com CDN, curl):** Resmi Substance 3D ikonları çıkarıldı → `assets/logos/products/`: substance3d.svg (ana koleksiyon), substance-painter/sampler/designer/stager/modeler/assets.svg (6 uygulama).
- **cadbim_substance3d.html:** Hero ikonu jenerik ti-texture → gerçek Substance 3D ikonu. Yeni **"Substance 3D Uygulamaları" bölümü** eklendi (cross sonrası): 6 uygulama kartı, her biri resmi app ikonu + Türkçe açıklama (Painter=doku boyama, Sampler=fotoğraftan malzeme, Designer=prosedürel, Stager=sahneleme/render, Modeler=heykel/VR, Assets=kütüphane). İçerik Adobe'nin ürün yapısına göre, CADBİM Türkçesiyle adapte (verbatim kopya değil).
- **cadbim_urunler.html:** substance3d kartı fallback adobe.png → gerçek substance3d.svg.
- **Doğrulama (localhost):** Substance sayfası hero ikonu + 6 app ikonu yüklü, 0 kırık.
- **Durum:** ✅ Substance 3D Adobe sayfasına göre güncellendi (gerçek ikonlar + uygulama bölümü).

### DK-2026-07-21-16 — Tüm ürün sayfalarında bilgi mimarisi: içerik önce, CTA sonda

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "ürün sayfalarında önce ürünü tanıt; ilgili ürünler/kullanıldığı çözümler ve CTA sonda olsun; şu an hero'da ilk 'Teklif İste' geliyor, tüm ürünler için değiştir" dedi.
- **Yapılan (2 işlem, tüm ürün/marka/sektör sayfaları):**
  1. **Hero CTA kaldırıldı** — hero'daki "Teklif İste / Marka Sayfası / Eğitim" butonları çıkarıldı. 3 farklı hero yapısı ele alındı: Tip A (`display:flex;gap:12px`), Tip B tek-satır ve **çok-satırlı** `hero-btns`, ve microsoft'taki çıplak `btn-p`. Toplam 79 sayfada hero artık yalnızca ürünü tanıtıyor.
  2. **"İlgili ürünler & çözümler" (cross) bölümü sona taşındı** — hero'nun hemen altındaki cross, sayfanın sonuna (cta-strip'ten hemen önce) alındı. 94 sayfada.
- **Yöntem:** Python dönüşümü + her sayfada section/div **denge kontrolü** (delta=0 zorunlu, bozulanlar atlanır). 0 sayfa bozuldu. (autodesk.html'deki -1 div farkı önceden vardı, benim değişikliğim değil.)
- **Doğrulama (localhost):** autocad (emb-logo tipi) ve substance3d (Tip A) — hero'da CTA yok, tek "Teklif İste" yalnızca sondaki cta-strip'te, cross CTA'dan hemen önce, 0 kırık görsel. Yeni sıra: hero(tanıtım) → özellikler/uygulamalar → kullanım → ilgili ürünler(cross) → CTA.
- **Not:** Autodesk sayfalarında 2 cross uç uca gelebiliyor (ilgili ürünler + Cadbim lisans); yapısal sorun değil, istenirse birleştirilir.
- **Durum:** ✅ Tüm ürün sayfaları: içerik önce, CTA sonda.

### DK-2026-07-21-17 — Ürün sayfası sonu: "Bu Ürünle İlgili" modülü (çözüm/endüstri/eğitim)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur karışık cross'u beğenmedi; "kullanıldığı çözümler ve endüstriler şeritleri + ilgili sayfalara link; eğitimi olan ürünlerde eğitim yönlendirmesi (sadece Autodesk, önce eğitim var mı kontrol et)" istedi. Tasarımı substance3d prototipinde onayladı.
- **Yeni modül (sayfa sonu, cross yerine):** "Keşfet / Bu Ürünle İlgili" başlığı + etiketli 3 grup: **Kullanıldığı Çözümler** (çözüm sayfalarına linkli pill'ler), **Endüstriler** (sektör sayfalarına linkli), **Birlikte Çalıştığı Ürünler** (cross'tan çıkarılan, ürün logolu). + **Eğitim CTA banner'ı**.
- **Eşleştirme:** Ürün→kategori (AEC/M&E/PD&M/PLATFORM/Adobe/Chaos) → kategori-bazlı çözüm+endüstri. Birlikte-ürünler mevcut cross'tan alındı.
- **Eğitim banner'ı:** Yalnızca eğitimi olan Autodesk ürünlerinde (egitimler'deki data-cat'lere göre: autocad, revit, inventor, fusion, civil, media=3ds/maya, aec). 16 sayfada. Banner `cadbim_egitimler.html?cat=<kategori>#katalog`'a gidiyor; egitimler'e URL-param filtre desteği eklendi (o kategoriyi otomatik filtreleyip katalog'a kaydırır). Adobe/HP/vb.'de eğitim banner'ı yok.
- **Kapsam:** 63 sayfa (62 script + substance manuel). cross varsa değiştirildi, yoksa cta-strip öncesi eklendi.
- **Doğrulama:** Denge kontrolü 0 bozulma (autodesk'in -1'i önceden vardı). autocad (çözüm/endüstri linkleri, eğitim→?cat=autocad, modül CTA öncesi, 0 kırık); egitimler?cat=autocad → AutoCAD sekmesi aktif, 4 kurs filtreli. 
- **Durum:** ✅ Tüm ürün sayfalarında yeni ilgili-modülü + koşullu eğitim yönlendirmesi.

### DK-2026-07-21-18 — Mobil arama kapatma + egitimler logo temizliği + HP logosu

- **Yapan:** Onur Bozok + Claude (PDM asistanı).
- **1) Mobil menü/arama kapatılamıyordu:** Kök neden — hamburger `.nav` (z-index:1000) stacking context'i içinde; arama paneli `z-index:2000` hamburger'ı örtüyordu. Çözüm: panelin `.cbm-top` bar'ına görünür **kapat (X) butonu** eklendi (`.cbm-close`), `close()`e bağlandı. Artık ESC + hamburger + kapat butonu ile kapanıyor. (mobilenav.js)
- **2) cadbim_egitimler.html:** Rozet satırından **Adobe Gold Reseller ve HP Amplify** logoları kaldırıldı (Cadbim yalnızca Autodesk ATC eğitimi veriyor). Kalan: Autodesk ATC + Academic Partner.
- **3) Ana sayfa markalar (HP kutusu):** Karmaşık `hp-amplify-insignia.png` → sade resmi **mavi HP logosu** (`HP_Blue_RGB_150_MD.png` → assets/logos/hp-logo.png, 300×300). index.html cred-row.
- **Doğrulama (localhost, mobil+masaüstü):** Mobilde menü açılıp kapat butonuyla kapanıyor; egitimler'de adobe/hp logosu yok; ana sayfa HP kutusu mavi HP logosu yüklü.
- **Durum:** ✅ Üç düzenleme tamam.

### DK-2026-07-21-19 — Nav logosu yatay CADBİM + marka logo boyut dengeleme

- **Yapan:** Onur Bozok + Claude (PDM asistanı).
- **Nav logosu (153 sayfa):** Sol üstteki ikon + "CADBİM" + "Est. 1993" metni kaldırıldı; yerine Onur'un verdiği **yatay CADBİM logosu** (`cadbim logo yatay png.png` → assets/logos/cadbim-yatay.png). Ek metin eklenmedi (Onur talebi). Mevcut `.nav-logo img` CSS'i (height:26px, filter beyaz) korundu → logo beyaz, ~109×26. Hover'da mevcut "draw/reveal" animasyonu (clip-path) uygulanıyor. Görsel 24862px'ten 640px'e küçültüldü (decompression-bomb boyutundaydı).
- **Marka logo boyutları (index.html cred-row):** Kare/baskın logolar (hp/chaos/adobe/microsoft) küçültüldü, sketchup düşürüldü (Onur "çok büyük"), geniş olanlar (ultimaker/lumion) genişletildi. base max-height 66→48 + per-logo `[src*=]` ayarları. Yükseklik aralığı 22-66 → 22-56 (çoğu 44-56).
- **Doğrulama:** localhost 1280px — nav logo 109×26 görünür; marka logoları dengeli. (Not: browser pane bir ara 0×0 viewport'a düştü, ölçümler yanıltıcıydı; düzgün boyutta doğrulandı.)
- **Durum:** ✅ Logo + boyut dengeleme tamam. Animasyon seçeneği Onur'a soruluyor. SketchUp Pro ürünleri + derin mobil cila sıradaki iş.
