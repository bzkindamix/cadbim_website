# CADBİM Web Sitesi — Değişiklik Kayıtları (PDM / Revizyon Günlüğü)

> Bu dosya, projeye yapılan her değişikliğin izlenebilir kaydını tutar (PDM/ECO mantığı).
> Kayıt biçimi: **DK-YYYY-MM-DD-NN** · Tarih · Yapan · Kapsam · Etkilenen dosyalar · Doğrulama · Durum · Referans (commit).
> Kaynak kod sürüm kontrolü Git/GitHub'dadır; bu dosya insan-okunur değişiklik özetidir.

---

## 2026-07-20

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
