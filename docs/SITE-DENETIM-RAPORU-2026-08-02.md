# CADBİM Web Sitesi — Kapsamlı Denetim Raporu ve "20.000 USD Sınıfı" Yol Haritası

**Tarih:** 2 Ağustos 2026 · **Hazırlayan:** Claude (PDM asistanı) + Onur Bozok
**Kapsam:** 1.318 HTML sayfa (192 kök + 1.126 blog), 5 JS dosyası, 664 varlık dosyası (2,60 GiB), sitemap/robots/htaccess taslağı. 16.050 iç link ve tüm varlık referansları tarandı. **Bu denetimde hiçbir dosya değiştirilmedi** — rapor salt tespit ve öneridir.

---

## 1. Yönetici Özeti

Sitenin **tasarım sistemi ve şablon disiplini beklenenin üzerinde**: tek tutarlı navy/cyan kimlik, %100 alt metin kapsamı, her sayfada tek H1, eksiksiz canonical/OG kapsamı, kaliteli mobil menü + site içi arama, blog filtreleme. "Görünüm" tarafında temel sağlam.

Ancak site bugün üç katmanda **kırık** sayılır:

1. **Dağıtım katmanı:** Temiz URL'ler sunucuda tanımlı değil (.htaccess hâlâ taslakta). Menüdeki 16.050 iç linkin tamamı fiilen HTTP 404 dönüp JavaScript hilesiyle yönleniyor; 1.126 blog URL'sinin ise **hiçbir yönlendirme haritasında karşılığı yok**. Google açısından sitemap'teki 1.312 URL'nin büyük kısmı indekslenemez durumda.
2. **Dönüşüm katmanı:** Eğitim sayfasındaki form **hiçbir yere veri göndermiyor** (sahte onay mesajı gösterip sıfırlanıyor). Tek gerçek form, koyu temalı sitenin içine gömülü açık temalı bir Microsoft Forms iframe'i — ölçülemiyor, markasız, mobilde sorunlu.
3. **Ölçüm/uyum katmanı:** Çerez onayı ve GA4, **ana sayfa dahil 23 sayfada yok**. En yüksek trafikli giriş noktalarında analitik kör, KVKK çerez bandı çıkmıyor; footer'daki "Çerez Ayarları" linki bu sayfalarda sessizce çalışmıyor.

| Boyut | Not (10 üzerinden) | Özet gerekçe |
|---|---|---|
| Görsel tasarım & tutarlılık | 7,5 | Tek tasarım sistemi, disiplinli şablonlar; küçük token sürüklenmeleri |
| Teknik SEO | **3** | Temiz URL'ler sunucuda çözümsüz, 99 mükerrer post, 8.409 eski-format link |
| Performans | 4 | İlk yükün %73'ü tek ikon fontu; gzip/cache yok; 11 MB'lık ürün sayfaları |
| Dönüşüm & lead toplama | **2,5** | Sahte form, iframe form, ürün sayfalarında lead noktası yok, ölçüm yok |
| Erişilebilirlik | 5 | Alt %100 ve tek H1 güçlü; odak göstergesi/skip link/ARIA yok |
| İçerik & güven | 5 | 19 başarı öyküsü var ama logosuz/metriksiz; blog içeriği tek cümlelik |
| Altyapı & sürdürülebilirlik | 4 | CSS %95,6 tekrar; 1.318 sayfada elle bakım; build/CI yok |

**Sonuç:** 20.000 USD sınıfı bir site farkı üç şeyde gösterir — *kusursuz teslimat* (her URL çalışır, hızlı açılır), *ölçülebilir dönüşüm* (her lead CRM'e düşer, her adım izlenir) ve *güven veren içerik* (kanıtlı başarı öyküleri, derin içerik). Mevcut görsel kimlik korunarak, aşağıdaki 4 fazlık planla bu seviyeye ulaşılabilir.

---

## 2. KRİTİK Bulgular

### K1 — Temiz URL şeması sunucuda yok; site JS-404 hilesiyle ayakta
`.htaccess` sunucuya hiç kurulmamış (repoda yalnız `docs/htaccess-taslak.txt`, 783 satır, kendi başlığında "TASLAK" yazıyor). `/autocad` isteği sunucudan **HTTP 404** döner; `404.html` içindeki 186 kayıtlı JS haritası tarayıcıda `cadbim_autocad.html`'e sıçratır. Kullanıcı beyaz ekran flaşı görür; Googlebot 404 statüsü görür ve canonical hedefi (`/autocad`) indekslenmez.
**Düzeltme:** Taslak, UTF-8 (BOM'suz) olarak `.htaccess` adıyla köke kurulup staging'de doğrulanmalı.

### K2 — 1.126 blog URL'si hiçbir yönlendirme haritasında yok
`sitemap.xml`'deki 1.126 `/post/...` temiz URL'si için ne `404.html` JS haritasında ne de `.htaccess` taslağında tek bir kural var. Bu URL'ler bugün de, taslak kurulsa da **404 döner**.
**Düzeltme:** Taslağa tek genel kural: `RewriteRule ^post/(.+?)/?$ /post/$1.html [L]`

### K3 — Eğitim formu sahte: veri hiçbir yere gitmiyor
`cadbim_egitimler.html:1008` — `handleSubmit` yalnızca butona "Talebiniz alındı!" yazıp 3 saniye sonra formu sıfırlıyor. `action` yok, `fetch` yok. **Eğitim talebi bırakan her müşteri kayboluyor ve kullanıcı gönderildiğini sanıyor.**
**Düzeltme:** Form gerçek bir uca (Dynamics 365 / e-posta API / en azından mevcut MS Forms) bağlanana kadar buton doğrudan iletişim kanallarına yönlendirilmeli.

### K4 — Çerez onayı + GA4 ana sayfa dahil 23 sayfada yok
`cookie-consent.js` (GA4 `G-DTTE7C82NB`'yi onay sonrası yükleyen script) şu sayfalarda eksik: **index.html**, 5 `sektor_*` sayfası, `cozumler`, `egitimler`, `endustriler`, `404.html`, `construction_cloud` ve **13 KVKK sayfasının tamamı** (çerez politikası sayfası dahil). Etkileri: ana sayfada analitik yok, KVKK çerez bandı giriş sayfasında çıkmıyor, bu sayfalardaki "Çerez Ayarları" footer linki (`window.openCookiePrefs`) sessizce çalışmıyor.
**Düzeltme:** 23 sayfaya `<script src="cookie-consent.js?v=2" defer></script>` eklenmeli.

### K5 — Footer 189 sayfada içeriksiz
Tam footer (e-posta, telefon, WhatsApp, 16 linklik site haritası) yalnızca 3 sayfada var: `index`, `iletisim`, `sanatsal_baski`. Kalan 189 kök sayfa + 1.126 post'ta footer sadece "© 2026 Cadbim · KVKK · Çerez Ayarları" + 3 sosyal ikon. `mailto:`/`tel:`/`wa.me` yalnız 3 dosyada geçiyor. **Adres hiçbir footer'da yok; Ankara temsilciliği sitede hiç görünmüyor.**
**Düzeltme:** `index.html`'deki `footer-grid` bloğu ortak parça yapılıp tüm sayfalara yayılmalı (İzmir adresi + Ankara temsilciliği ile).

### K6 — 99 Türkçe karakterli mükerrer blog çifti — ikisi de indekste
`post/` içinde 99 çift birebir kopya (`...genel-bakış.html` ↔ `...genel-bakis.html`). Her ikisi de kendine canonical veriyor, ikisi de sitemap'te, ikisi de `blog-posts.json` üzerinden linkleniyor. Google gözünde 99 mükerrer içerik kümesi.
**Düzeltme:** Türkçe karakterli kopyaların canonical'ı ASCII ikizine çevrilmeli, sitemap ve JSON'dan çıkarılıp 301 ile birleştirilmeli.

### K7 — İlk yükün %73,5'i tek bir ikon fontu; gzip/cache hiç yok
- `tabler-icons.woff2` **462 KB** — 5.900+ ikonluk set, sitede yalnız 300 ikon için indiriliyor. `index.html` ilk ziyaret ~614–730 KB; bunun ~79 KB'ı kendi içeriğimiz.
- `.htaccess` taslağında **tek bir cache/sıkıştırma yönergesi yok** (`mod_deflate`/`mod_expires` 0 satır). `index.html` 87 KB yerine 21 KB inebilirdi (%75 kayıp, tüm sitede geçerli). `?v=` cache-busting parametreleri `Expires` başlığı olmadığı için işlevsiz.
**Düzeltme:** Kullanılan 300 ikon yerel SVG sprite/subset'e çevrilmeli (~40 KB); taslağa deflate+expires blokları eklenmeli. Bu iki adım tek başına ilk yükü ~190 KB'a indirir.

### K8 — DesignJet sayfaları 10–14 MB görsel taşıyor
Karşılaştırma bölümündeki 13 dev PNG (824 KB–1.209 KB, 1200 px) her DesignJet sayfasında tekrarlanıyor ve **220 px'lik kutuda** gösteriliyor. En az 18 sayfa tam kaydırmada 10 MB+ indiriyor (`cadbim_designjet.html` 13,7 MB). 4 Chaos sayfasında da `preload`süz autoplay hero videoları toplam 37,5 MB otomatik iniyor (`cadbim_vray.html` tek başına 17,7 MB).
**Düzeltme:** 220/440 px WebP türevleri + `srcset`; hero videolara `preload="none"` veya ~2-3 MB'a yeniden kodlama.

### K9 — 2,46 GiB referanssız ham varlık site kökünde duruyor
`assets/products/designjet/` (188 dosya; basın fotoğrafları, MP4'ler, 19 adet Thumbs.db) hiçbir sayfadan referans almıyor. `.gitignore`'da olduğu için repoya girmiyor (doğru), ama klasör site kökünde durduğu için **FTP/rsync ile toplu yüklemede sunucuya 2,46 GiB ölü ağırlık çıkar**.
**Düzeltme:** Klasör site kökü dışına taşınmalı (ör. `D:\cadbim-ham-asset\`), yayın betiğine exclude eklenmeli.

---

## 3. YÜKSEK Öncelikli Bulgular

| # | Bulgu | Kanıt | Düzeltme |
|---|---|---|---|
| Y1 | `vray`, `enscape`, `veras` rewrite kuralı yok — sitemap'te ama sunucu kuralı tanımsız | .htaccess taslağı bölüm 3'te 0 eşleşme; 13 iç link etkileniyor | Taslağa 3 satır kural |
| Y2 | 4 yeni SketchUp sayfası sitemap + 404 haritasında yok | `sketchup-pro`, `-scan`, `-civil-contractor`, `advanced-workflows` (commit 2bb572b ile eklendi, haritalar güncellenmedi) | sitemap.xml + 404.html MAP'e ekle |
| Y3 | Post'larda 8.409 iç link `.html` uzantılı eski formatta | `../cadbim_iletisim.html` (1.161), `../index.html` (3.378)… hepsi canlıda 301 zinciri üretir | Toplu değişimle kök-göreli temiz URL'e çevir |
| Y4 | Kök sayfalarda 568 × `href="index.html"` — canonical `/` ile çelişen karışık şema | Diğer tüm linkler temiz URL | `href="/"` yap |
| Y5 | 11 noindex KVKK sayfası sitemap'te; `robots.txt` var olmayan `/tesekkurler`'i disallow ediyor | grep doğrulandı | Sitemap'ten çıkar; teşekkür sayfasını oluştur (bkz. Faz 2) |
| Y6 | Klavye odak göstergesi tüm sitede yok; skip link 0; masaüstü dropdown'larda ARIA 0 (yalnız `:hover` — dokunmatikte de sorunlu) | `:focus-visible` 0 dosya, `outline:none` 91 dosya | Global `:focus-visible` kuralı + skip link + `aria-expanded`/klavye desteği |
| Y7 | Footer yasal linkleri WCAG kontrast FAIL (2,61:1) — 1.314 sayfada | `rgba(255,255,255,.3)`; KVKK linklerinin okunması zor | `0.58`'e çıkar (index'te düzeltilmiş, 191 sayfaya yayılmamış — token sürüklenmesi) |
| Y8 | Satır içi CSS'in %95,6'sı sayfalar arası tekrar: 6,08 MB sevk ediliyor, 121 KB yeterli | 40 kural 1000+ sayfada aynı; `design-system.css` bağlı ama 7,6 KB'lık iskelet | Ortak kuralları `design-system.css`'e taşı |
| Y9 | Blog listesi tamamen JS ile üretiliyor; statik link 0, RSS yok, sayfalama meta'sı yok, post→post link %4,5 | `blog-posts.json` (414 KB) fetch'i olmadan boş sayfa | Statik liste + "İlgili Yazılar" + `/feed.xml` |
| Y10 | `cadbim_construction_cloud.html` markasız beyaz stub (494 bayt) | Nav/footer/CSS yok | Sil, `.htaccess`'te 301'e çevir |
| Y11 | `width`/`height` hiçbir `<img>`'de yok (2.672 etiket, CLS riski); `srcset` 0; lazy kapsamı %45,8 | Ölçüldü | Toplu şablon düzeltmesi |
| Y12 | Post nav'ı 9 düz link — kök sayfalardaki 40 linklik mega menüden kopuk | 1.126 post'ta aynı | Post şablonu nav'ını kökle eşitle |

---

## 4. ORTA / DÜŞÜK Bulgular (özet)

- **O1:** 664 post title 60+ karakter (SERP'te kırpılır); 86 kök description 160+; post'ta 79 mükerrer title grubu, 223 çok kısa description ("VAULT PROFESSIONAL" gibi).
- **O2:** JSON-LD: `Article`'da `author`/`image`/`dateModified` yok; `BlogPosting` 0; `FAQPage` 0; `LocalBusiness` yalnız 2 sayfada; `Organization.logo` 1200×630 OG görseline işaret ediyor (kare olmalı).
- **O3:** 229 metin blog yazısında `og:image` yok.
- **O4:** Tek dönüşüm formu MS Forms iframe'i: açık tema (marka kopukluğu), 600 px sabit yükseklik (mobil kaydırma kapanı), `title` yok, gönderim GA'da ölçülemiyor. Altında ~60 satır yorumda bırakılmış eski form ölü kodu.
- **O5:** Ürün sayfalarında (189 sayfa) satır içi lead formu yok — dönüşüm hep `iletisim`'e sıçramak zorunda.
- **O6:** Başarı öyküleri (19 müşteri) video+filtreli iyi bir yapıda ama **müşteri logosu 0, sayısal sonuç metriği 0, alıntı 0**; ana nav'dan link yok.
- **O7:** 404 sayfası gerçek bir hata deneyimi değil (nav/footer/arama yok); yönlendirme aracı olarak yazılmış.
- **O8:** Başlık hiyerarşisi atlamaları (h1→h3): `egitimler`, `kvkk`, `iletisim`, `basari_oykuleri`.
- **O9:** 1.009 YouTube iframe'inin hiçbirinde facade yok; 993'ü çerezli `youtube.com` domain'inde (16'sı nocookie) — KVKK açısından da gözden geçirilmeli. Thumbnail altyapısı (`hqdefault.jpg`, 1.793 kullanım) zaten mevcut.
- **O10:** `mobilenav.js` sürüm karmaşası: 740 post `?v=11`, 386 post `?v=9` (çifte cache girdisi).
- **O11:** `index.html`'de 36 KB satır içi 3D sahne betiği — harici `defer` dosyaya çıkarılmalı (önbelleklenir, HTML 87→51 KB).
- **O12:** Nav logosu 39 KB'lık 640×153 PNG, 26 px'de `filter:invert(1)` ile bembeyaz gösteriliyor — ~2 KB'lık SVG işi; 1.316 sayfada eager yükleniyor.
- **D1:** `apple-touch-icon` tüm sitede SVG'ye işaret ediyor (iOS desteklemez, ikon çıkmaz); 180×180 PNG yok; `site.webmanifest` yok; favicon yolu göreli/mutlak karışık.
- **D2:** `prefers-reduced-motion` yalnız 3/192 sayfada.
- **D3:** Sosyal ikon tutarsızlığı: tam footer 4, stub footer 3 (Facebook eksik); `social-widget.js` ile aynı sayfada çifte sosyal blok.
- **D4:** Marka yazımı: metinlerde "Cadbim", logoda ve kurumsal kimlikte "CADBİM" — tek yazım kararlaştırılıp title/copy genelinde uygulanmalı.
- **D5:** Site içi arama indeksi yalnız ~190 kök sayfayı kapsıyor; 1.126 blog yazısı aranamıyor (blog sayfasının kendi filtresi var — kabul edilebilir, birleşik arama ideali).
- **D6:** sitemap'te 198 URL ham Türkçe karakterli (percent-encoding yok — Google tolere eder, diğer botlar etmeyebilir).
- **D7:** 21 referanssız varlık (partner rozetleri ~1 MB) + kökte artık `og-image.png`.
- **D8:** Sayaç animasyonu (`data-n`) tetiklenmeden istatistikler "0+" görünüyor — SSR/noscript fallback değerleri yazılmalı.

---

## 5. Güçlü Yönler (korunmalı)

1. **Tek tasarım sistemi:** 1.318 sayfada aynı token seti, tipografi (Manrope/Space Grotesk), navy/cyan palet — eski sürüm kalıntısı yok.
2. **Şablon disiplini:** Post'larda breadcrumb/tarih/CTA/canonical/OG/JSON-LD %100; kök sayfalarda nav byte-düzeyinde özdeş; mükerrer kök title/description 0.
3. **Erişilebilirlik temelleri:** alt kapsamı %100 (dekoratif boş alt'lar doğru kullanılmış), her sayfada tek H1, `lang="tr"` tam.
4. **`mobilenav.js` kalitesi:** ARIA'lı hamburger, Escape/ok tuşu desteği, ⌘K arama modali, `BASE` hesabıyla post/ uyumu — savunmacı ve tek kaynaklı.
5. **KVKK yaklaşımı (kapsam hariç):** GA4'ün onay sonrası yüklenmesi (Consent Mode mantığı) doğru kurgulanmış.
6. **OG altyapısı:** 153 özel OG görseli, hepsi diskte mevcut, yetim dosya yok; sitemap biçimi temiz (mutlak URL, .html'siz, mükerrersiz).
7. **WhatsApp entegrasyonu:** ön tanımlı mesaj, `aria-label`, çerez bandı ile çakışma çözümü.

---

## 6. "20.000 USD Sınıfı" Yol Haritası

> Hedef tanımı: her URL ilk istekte 200 döner, ana sayfa ilk yükü < 300 KB, LCP < 2,5 s, her lead CRM'e düşer ve ölçülür, içerik güven verir, tek şablondan yönetilir.

### Faz 0 — Yangın söndürme (1–3 gün, sıfır tasarım değişikliği)
| İş | Etki |
|---|---|
| `.htaccess`'i canlıya al (K1) + `post/` genel rewrite kuralı (K2) + vray/enscape/veras + 4 SketchUp kuralı (Y1, Y2) | 16.050 link ve 1.312 sitemap URL'si gerçek 200 döner — **tek başına en yüksek etkili iş** |
| Taslağa `mod_deflate` + `mod_expires` blokları (K7) | Tüm sitede ~%70 bant genişliği tasarrufu |
| `cookie-consent.js`'i 23 sayfaya ekle (K4) | Ana sayfada analitik + KVKK bandı çalışır |
| Eğitim formunu gerçek bir uca bağla ya da geçici olarak iletişim kanalına yönlendir (K3) | Lead kaybı durur |
| Tam footer'ı 189 sayfaya + post şablonuna yay (K5) | Her sayfadan telefon/e-posta/adres erişimi |
| 2,46 GiB ham klasörü site kökünden çıkar (K9) + Thumbs.db temizliği | Deploy güvenliği |
| Sitemap düzeltmeleri: 11 noindex çıkar, 4 SketchUp ekle (Y5, Y2) | Search Console temizliği |
| Footer kontrast token'ını 191 sayfaya yay (Y7) | WCAG AA + KVKK linkleri okunur |

### Faz 1 — Performans + SEO paketi (1–2 hafta)
| İş | Etki |
|---|---|
| Tabler ikon subset/SVG sprite (K7) | İlk yük 614 KB → ~190 KB |
| 13 DesignJet PNG + 8 UltiMaker WebP yeniden kodlama, 220/440 px türevler + `srcset` (K8) | 18 sayfada 10 MB+ → ~1 MB |
| 4 hero videoya `preload="none"` veya yeniden kodlama (K8) | 37,5 MB otomatik indirme biter |
| Tüm `<img>`'lere `width/height` + eksik 1.410 etikete `loading="lazy"` (Y11) | CLS/LCP skorları |
| Ortak CSS'i `design-system.css`'e taşı (Y8) + 3D betiği harici dosyaya (O11) + nav logosu SVG (O12) | Sayfalar arası önbellek; bakım tek noktadan |
| 99 mükerrer post birleştirme + 301 (K6); post'lardaki 8.409 `.html` linki temiz URL'e (Y3); 568 `index.html` → `/` (Y4) | Mükerrer içerik ve 301 zincirleri biter |
| Meta uzunlukları (664 post title, 86 kök desc); `Article`'a author/image/dateModified; ürün sayfalarına FAQPage; 229 post'a og:image (O1–O3) | SERP görünümü ve zengin sonuçlar |
| RSS feed + post şablonuna "İlgili Yazılar" + paylaşım butonları (Y9) | İç linkleme + içerik dağıtımı |
| `:focus-visible` + skip link + dropdown ARIA/klavye (Y6); apple-touch-icon PNG + manifest (D1) | Erişilebilirlik ve PWA temeli |

### Faz 2 — Dönüşüm & güven (2–4 hafta) — "20k hissi" burada oluşur
| İş | Etki |
|---|---|
| **Markalı native form + Dynamics 365 entegrasyonu** — MS Forms iframe'i yerine sitenin kendi koyu temalı formu; gönderim doğrudan CRM'e lead olarak düşer (şirket zaten Dynamics 365 kullanıyor); KVKK onay kutusu + `/tesekkurler` sayfası | Lead'ler otomatik CRM'de; dönüşüm ölçülebilir; marka bütünlüğü |
| GA4 dönüşüm ölçümü: form gönderimi, WhatsApp/tel tıklaması, teklif CTA'ları event olarak | "Site ne getiriyor?" sorusu veriyle yanıtlanır |
| Ürün sayfalarına kompakt satır içi teklif formu veya "30 saniyede teklif" modalı (O5) | Dönüşüm sürtünmesi azalır |
| Başarı öykülerine müşteri logosu + tek satır ölçülebilir sonuç + alıntı; ana nav'a "Başarı Öyküleri" girişi (O6) | Güven sinyali — B2B'de en güçlü satış aracı |
| Nav IA düzeltmesi: KVKK ana menüden footer'a; "Teklif Al"/"Teklif İste" tek etikete indirgenir | Menü müşteri odaklı sadeleşir |
| 404'ü gerçek tasarımlı sayfaya çevir (arama + popüler sayfalar) (O7); `construction_cloud` stub'ını 301'e çevir (Y10) | Kusursuz kenar durumlar |
| Blog içerik derinleştirme programı: en çok trafik alan 50 yazıya 300+ kelimelik özgün gövde + yazar bloğu (E-E-A-T) | 1.126 sayfalık ince içerik riskten değere döner |
| YouTube facade (mevcut thumbnail altyapısıyla) + `youtube-nocookie.com` birleştirmesi (O9) | Blog sayfaları hafifler; KVKK uyumu |

### Faz 3 — Altyapı & sürdürülebilirlik (sürekli)
| İş | Etki |
|---|---|
| Statik site üretecine geçiş (Eleventy/Astro): nav, footer, head, post şablonu **tek kaynaktan** derlenir; içerik Markdown/JSON'da | "1.318 sayfada elle düzeltme" dönemi kapanır — bu denetimdeki bulguların çoğunun kök nedeni budur |
| CI/CD: GitHub Actions ile otomatik derleme + link denetimi + Lighthouse CI eşikleri + otomatik sitemap | Her push'ta kalite güvencesi |
| Görsel pipeline: yeni görseller otomatik WebP/AVIF + boyut türevleri | Performans kalıcı olur |
| Staging ortamı + uptime/404 izleme (Search Console entegrasyonu) | Canlıya güvenli çıkış |

### Hedef metrikler (kabul kriterleri)
- Ana sayfa ilk yük **< 300 KB**, LCP **< 2,5 s**, CLS **< 0,1**, PageSpeed **90+** (mobil)
- Search Console: temiz URL'lerde 404 = **0**; mükerrer içerik uyarısı = 0
- Analitik kapsamı: **1.318/1.318 sayfa**; form→CRM lead akışı uçtan uca test edilmiş
- WCAG 2.1 AA: kontrast, odak, klavye navigasyonu geçer
- Tüm bakım tek şablon + tek CSS kaynağından

---

## 7. Denetim Yöntemi

Üç paralel inceleme koluyla yürütüldü: (1) teknik SEO (sitemap/robots/canonical/JSON-LD/iç link şeması), (2) performans ve varlıklar (664 dosyanın referans analizi, format/boyut envanteri, ilk yük ölçümleri — CDN varlıkları canlı `Content-Length` ile ölçüldü), (3) UX tutarlılık/dönüşüm/erişilebilirlik (10 sayfalık derin örneklem + 1.126 post tam tarama + hesaplanmış WCAG kontrast oranları). Yerel önizleme `http://localhost:8420` üzerinde doğrulandı (mobil 375px viewport dahil).
