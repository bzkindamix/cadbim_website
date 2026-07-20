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
