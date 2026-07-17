# CADBİM Web Sitesi — Devir Notu (Handoff)

> Son güncelleme: 2026-07-17 · Bu dosya, projeye yeni başlayan bir session'ın/geliştiricinin
> sıfır bağlamla devam edebilmesi için yazıldı. Süreç kronolojisi, mimari kararlar,
> bekleyen işler ve çalışma kuralları aşağıdadır.

## 1. Proje nedir?

CADBİM (1993'ten beri İzmir merkezli Autodesk Gold Partner; Adobe, HP, Microsoft,
UltiMaker, Chaos iş ortağı) kurumsal web sitesi. **152 statik HTML sayfası** —
framework yok, build adımı yok. Her sayfa kendi `<style>` bloğunu taşır; site
geneli düzeltmeler `assets/css/design-system.css` overlay dosyasıyla dağıtılır
(her sayfada satır içi stillerden SONRA yüklenir, bu yüzden onları ezebilir).

- Yerel çalıştırma: `python -m http.server 8420` (`.claude/launch.json` tanımlı, ad: `cadbim-static`)
- Deploy hedefi: www.cadbim.com.tr (statik hosting; zip'i köke açmak yeterli, tüm yollar göreli)

## 2. Bugüne kadar yapılanlar (kronolojik)

### Faz 0 — Analiz ve yön seçimi
- Eski site "AI yapılmış / amatör" bulunuyordu: gerçek görsel yok, tek kart kalıbının
  tekrarı, klişe aurora/scan efektleri (blur 60px + 10 sonsuz animasyon), tek font.
- Üç tasarım yönü mockup'landı (artifact: https://claude.ai/code/artifact/02693383-2b70-4013-b25b-0e52165bf278 ).
- **Seçilen yön: "Engineering Precision"** — koyu navy/cyan marka kimliği korunur;
  klişe efektler yerine markaya özgü teknik çizim dili (izometrik wireframe, ölçü
  çizgileri, koordinat etiketleri).

### Faz 1-4 — İlk modernizasyon turu
- **Tipografi:** Başlıklar Space Grotesk, gövde Manrope (Google Fonts linki 152 sayfada).
  Overlay `--fd`/`--font-d` değişkenlerini ve `h1,h2` kurallarını ezerek dağıtır.
- **Ana sayfa** yeniden inşa edildi (izometrik SVG hero, sayan metrikler, bento düzen).
- **Performans:** Site 22MB → ~6MB. Base64 gömülü CADBİM logosu 122 sayfadan çıkarılıp
  `assets/logos/cadbim-logo.png` yapıldı; 108 gömülü base64 görsel tekilleştirilip
  `assets/img/emb-<hash>.<ext>` (40 dosya) olarak çıkarıldı; Tabler Icons CDN `@3`e
  sabitlendi; çöp dosyalar silindi.
- Müşteri sayısı site genelinde **10.000+** yapıldı (hero, metrikler, hakkımızda, dijital dönüşüm).

### Ana sayfa R2 — Test bulguları sonrası (Onur'un revizyon listesi)
- **Kalıcı 3D katman:** İlk sürümdeki scroll-pin (240vh sticky hero) "boş sayfa" hissi
  verdiği için kaldırıldı. Sahne artık `#heroDraw` `position:fixed` katmanda; TÜM sayfa
  scroll'u orbit'i sürer (theta 0.15→1.7 rad), hero'dan çıkarken merkeze kayıp büyür ve
  0.13 opaklıkta arka planda dönmeye devam eder. Bölüm zeminleri yarı saydam (`--srf`);
  açık zeminli "cred" bölümü sahneyi doğal örter. Test kancaları:
  `window.CADBIM_hero.set(p)` ve `.setLayer(q)`. Mobil (<900px) ve reduced-motion'da statik.
- **3D sektör seçici:** Ürün arama kaldırıldı. `#sectorSvg` viewport'unda 7 prosedürel
  wireframe obje (bina/vinç/dişli/araç/kamera/kep/uçak) — listede hover → obje çizilir
  ve otomatik döner; tıklama → sektor_*.html.
- **Çözümler:** 7 endüstri sekmesi, tüm çözüm sayfalarına tıklanabilir kartlar.
- Logo duvarı eş boyut + tıklanabilir; "İzmir & Ankara" kaldırıldı (Ankara yalnızca
  iletişim sayfasında); "Sektörün Lider Markaları" bölümü kaldırıldı;
  4. metrik "8 Marka yetkili iş ortaklığı".
- **Mega-menü:** Çözümler dropdown'ı 152 sayfada 4 kolonlu yatay mega-menü
  (`.nav-mega`, stiller design-system.css'te). Her sayfanın kendi `active` işareti korundu.

### İç sayfa şablonları turu
- **Marka sayfaları:** autodesk (rozet duvarı: Gold/ATC/Service Provider + 4 associate;
  tekrarlar teke; cross şeridi sona; eş boyut ürün kartları), adobe & hp (rozet duvarları),
  chaos/ultimaker/microsoft (ürün kutularında `.plogo-ph` placeholder),
  sketchup/lumion (çapraz satış kutularına marka logoları).
- **Çözüm sayfaları (15):** "kullanılan ürünler" + "hangi endüstrilerde" şeritleri CTA
  öncesine taşındı; içerik/iş akışı üste çıktı. `cadbim_dijital_donusum.html` farklı
  şablonda — dokunulmadı.
- **Endüstri sayfaları (7):** CTA'lar footer öncesine taşındı; sektor_mimari'de 3ds Max
  kartındaki yanlış Chaos logosu Autodesk yapıldı.
- Kompakt şerit kuralı (global): `.section > * { max-width:1180px; margin:auto }`.

### GitHub'a aktarım (bu oturum)
- Depo `git init` ile oluşturuldu, `.gitignore` `.claude/` klasörünü dışlar.
- `gh` CLI winget ile kuruldu; kimlik doğrulama GitHub device-flow ile yapıldı
  (kod kullanıcı tarafından github.com/login/device adresinde girildi).
- Uzak depo: bkz. `git remote -v` (özel/private oluşturuldu; görünürlük GitHub'dan değiştirilebilir).

## 3. Kritik çalışma kuralları (BOZMA!)

1. **CSS cache-busting:** `design-system.css?v=N` — overlay her değiştiğinde N artırılmalı
   ve 152 sayfada güncellenmeli (basit PowerShell replace). Şu an **v=5**.
2. **mobilenav.js** şu seçicilere bağımlı: `nav.nav`, `.nav-links`, `.nav-cta`.
   Nav DOM yapısını değiştirme; mega-menü iç yapısı serbest (mobil panel `a` etiketlerini toplar).
3. Sayfalar **UTF-8 (BOM'suz)**; PowerShell ile okurken `-Encoding UTF8` /
   `[IO.File]::ReadAllText(..., [Text.Encoding]::UTF8)` kullan, yazarken
   `New-Object Text.UTF8Encoding($false)`.
4. Satır sonları CRLF olabilir — string replace yerine `(?s)` regex + `\s*` kullan.
5. Kurumsal ton: resmi Türkçe, **emojisiz**; ürün adları İngilizce kalır
   (organizasyon talimatı). Görsellerde en-boy oranı bozulmaz.
6. İletişim formu **Microsoft Forms iframe**'idir (bilinçli tercih; eski HTML form
   yorum satırında durur). `#form` çapası site genelinde CTA hedefidir.

## 4. Bekleyen işler (bir sonraki session buradan devam etsin)

1. **Eksik ürün logoları** — sayfalarda kesikli çerçeveli `LOGO` placeholder'ları
   (`.plogo-ph`) ile işaretli. Onur logo dosyalarını verecek; placeholder'lar
   `<img>` ile değiştirilecek. Liste:
   - autodesk: AutoCAD, Revit, Inventor, Fusion, Forma, Tandem
   - chaos: V-Ray, Enscape, Veras AI, Phoenix FD, Vantage, Corona
   - ultimaker: S7, S5, S3, Method XL, Cura
   - microsoft: Microsoft 365, Azure, 365 Güvenlik
2. **Müşteri referans logoları + 2-3 vaka çalışması** — "10K site" hissinin son eksiği;
   Onur izinli referans listesi verecek, ana sayfaya referans şeridi eklenecek.
3. Gerçek proje/eğitim fotoğrafları (hakkımızda ve eğitim sayfaları için).
4. Deploy: zip'i sunucuya aç → yayın sonrası ana sayfada sert yenileme ile kontrol.
5. (İsteğe bağlı) `cadbim_dijital_donusum.html` farklı şablonda kaldı; yeni dile
   uyarlanması değerlendirilebilir.

## 5. Dosya haritası (önemli olanlar)

| Yol | Ne |
|---|---|
| `index.html` | Ana sayfa — kalıcı 3D sahne + sektör seçici + sekmeli çözümler; tüm scriptler sayfa sonunda inline |
| `assets/css/design-system.css` | Site geneli overlay (v5): tipografi, mega-menü, kart/buton dili, kompaktlık, erişilebilirlik |
| `assets/logos/` | Marka logoları ve rozetler (cadbim-logo.png dahil) |
| `assets/img/emb-*.{png,jpg,webp}` | Eski base64 gömülülerden çıkarılan 40 tekil görsel |
| `mobilenav.js` | Mobil menü + komut paleti (dokunma!) |
| `cadbim_*.html` | Marka/ürün/çözüm/KVKK sayfaları |
| `sektor_*.html` | 7 endüstri sayfası |
| `sitemap.xml` | lastmod 2026-07-17 |

## 6. Hızlı doğrulama komutları

- Sunucu: `python -m http.server 8420` → http://localhost:8420
- 3D test (konsol): `CADBIM_hero.set(0.5)` — sahne dönmeli; `CADBIM_hero.setLayer(1)` — katman küçülüp saydamlaşmalı.
- Kırık varlık taraması: tüm `src/href` yerel referanslarını diske karşı kontrol eden
  PowerShell script'i geçmiş oturumda kullanıldı (regex: `(?:src|href)="(?!https?:|//|data:|mailto:|tel:|#)..."`).
