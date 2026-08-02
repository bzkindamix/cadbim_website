# Canlıya Geçiş — URL Haritası ve İçerik Eşleme (cadbim.com.tr)

> Üretim: 2026-07-21 · Kaynak: canlı Wix sitemap'leri (665 URL) + yeni site canonical seti (153 slug)
> Makine-okunur tam liste: `docs/redirects-taslak.csv` (665 satır)

## 1. Özet

| Grup | Adet |
|---|---|
| Ana sayfalar | 120 |
| Blog yazıları (/post/*) | 242 |
| Blog taksonomi (/blog/*) | 97 |
| Dinamik koleksiyon öğeleri | 206 |
| **Toplam canlı URL** | **665** |

| Eşleme durumu | Adet | Anlamı |
|---|---|---|
| BIREBIR | 277 | Aynı slug yeni sitede var — 301 gerekmez (host aynı davranırsa). 739 blog yazısının tamamı (242 orijinal + 497 YouTube video) dahil |
| KURAL | 388 | Kesin hedef belirlendi — 301 listesine girer. 97 blog taksonomi sayfası (/blog/categories/*) client-side filtreli /blog hub'ına yönlendiriliyor |
| GOZDEN | 0 | — |
| GOZDEN-BLOG | 0 | Blog migrasyonu tamamlandı (2026-07-28) — tüm gerçek Wix yazıları taşındı, taksonomi sayfaları /blog'a yönlendirildi (bkz. §5) |

## 2. Strateji

1. **301 zorunlu:** Wix'ten çıkışta eşleşmeyen her URL 404 olur; sıralama ve backlink değeri kaybolur. Aşağıdaki harita birebir 301 olarak uygulanmalı.
2. **Host seçimi kritik:** GitHub Pages sunucu-taraflı 301 YAPAMAZ (yalnızca meta-refresh). Canlıya geçişte Cloudflare Pages (`_redirects`), Netlify veya benzeri, toplu 301 destekleyen bir host seçilmeli. `redirects-taslak.csv` bu formata kolayca dönüştürülür.
3. **Alan adı ve protokol:** `https://www.cadbim.com.tr` biçimi korunmalı (www'suz → www 301).
4. **Search Console:** Geçiş günü yeni sitemap gönderilir; 'Adres değişikliği' aracı KULLANILMAZ (alan adı aynı). 404 raporu ilk 4 hafta haftalık izlenir, kaçak URL'ler haritaya eklenir.
5. **Türkçe karakterli URL'ler:** `/insaat-proje-yönetimi`, `/yapisal-mühendislik-icin-bim` — 301 kuralları hem ham hem yüzde-kodlanmış biçimi kapsamalı.

## 3. Ana Sayfalar — Birebir Eşleşenler (33)

`/`, `/adobe`, `/advance-steel`, `/aec-collection`, `/alias`, `/autocad`, `/autocad-lt`, `/autodesk`, `/bim`, `/chaos`, `/cozumler`, `/danismanlik`, `/egitimler`, `/fusion`, `/iletisim`, `/infraworks`, `/inventor`, `/kvkk`, `/maya`, `/navisworks`, `/pdm`, `/plm`, `/recap-pro`, `/revit`, `/revit-lt`, `/sketchup`, `/surdurulebilirlik`, `/tasarim-otomasyonu`, `/tolerans-analizi`, `/ultimaker`, `/urunler`, `/vault-pdm`, `/yazilim-gelistirme`

## 4. Ana Sayfalar — 301 Haritası (87)

| Eski URL | Yeni URL | Durum | Not |
|---|---|---|---|
| `/3d-animasyon` | `/me-collection` | KURAL | kategori sayfası → M&E Collection |
| `/3ds-max` | `/3dsmax` | KURAL | slug farkı |
| `/abc-pro` | `/urunler` | KURAL | eski ürün tanımlanamadı, genel ürünler sayfası (onaylandı) |
| `/acrobat-sign` | `/adobe` | KURAL | Acrobat Sign ayrı sayfa yok → Adobe hub |
| `/adobe-acrobat` | `/adobe` | KURAL | Acrobat karta indirgendi → Adobe hub |
| `/adobe-creative-cloud` | `/adobe` | KURAL |  |
| `/adobe-yaraticilik` | `/yaratici-icerik` | KURAL | kategori → Yaratıcı İçerik çözümü |
| `/alt-yapi` | `/sektor-insaat` | KURAL |  |
| `/alt-yapi-icin-bim` | `/bim` | KURAL |  |
| `/altyapi-yazilimlari` | `/sektor-insaat` | KURAL |  |
| `/autocad-architecture` | `/autocad` | KURAL | toolset artık AutoCAD'e dahil |
| `/autocad-electrical` | `/autocad` | KURAL | toolset |
| `/autocad-map` | `/autocad` | KURAL | toolset (Map 3D) |
| `/autocad-mechanical` | `/autocad` | KURAL | toolset |
| `/autocad-mep` | `/autocad` | KURAL | toolset |
| `/autodesk-cfd` | `/cfd` | KURAL | CFD hâlâ satılıyor, yeni ürün sayfası oluşturuldu |
| `/basari` | `/basari-oykuleri` | KURAL | gerçek başarı öyküleri sayfası kuruldu (13 vaka) |
| `/basari-oykuleri` | `/basari-oykuleri` | BIREBIR | gerçek başarı öyküleri sayfası kuruldu (13 vaka) |
| `/blog` | `/blog` | BIREBIR | blog mimarisi kuruldu, kategori+ürün filtreli yeni sayfa |
| `/bosalan` | `/` | KURAL | Wix boş sayfa |
| `/cam-ve-imalat-teknolojileri` | `/cam` | KURAL |  |
| `/cam-ve-imalat-yazilimlari` | `/cam` | KURAL |  |
| `/designjet-fotograf` | `/hp-designjet-z` | KURAL |  |
| `/designjet-grafik` | `/hp-designjet-z` | KURAL |  |
| `/designjet-ofis` | `/hp-designjet-t` | KURAL |  |
| `/designjet-sarf` | `/designjet` | KURAL | geçici — DesignJet sarf malzeme sayfası planlandı |
| `/designjet-tarayici` | `/designjet-hd-pro` | KURAL | alt modeller ayrı eşleşti (hd-pro/sd-pro) |
| `/designjet-uretim` | `/hp-designjet-xl` | KURAL |  |
| `/endustri` | `/endustriler` | KURAL | gerçek Endüstriler indeks sayfası bulundu, düzeltildi |
| `/etkinlikler` | `/` | GOZDEN | etkinlik sayfası yeni sitede yok |
| `/fabrication` | `/fabrication-cadmep` | KURAL | CADmep/ESTmep/CAMduct için ayrı sayfalar oluşturuldu |
| `/fabrika-tasarimi-ve-dijital-ikiz` | `/fabrika-tasarimi` | KURAL |  |
| `/factory-design-utilities` | `/factory-design` | KURAL | slug farkı |
| `/farkli-cad-sistemleri` | `/urunler` | KURAL |  |
| `/film-vfx-yazilimlari` | `/sektor-medya` | KURAL |  |
| `/fotografcilik-ve-videografi` | `/adobe` | KURAL |  |
| `/fusion360-manage` | `/fusion-manage` | KURAL | Fusion 360 Manage → Fusion Manage (yeni ad) |
| `/gorsel-efekt` | `/sektor-medya` | KURAL |  |
| `/hata` | `/` | KURAL | Wix hata sayfası |
| `/hp-is-istasyonlari` | `/hp` | KURAL |  |
| `/hp-masaustu-workstation` | `/hp-z-workstation` | KURAL |  |
| `/hp-mobil-isistasyonu` | `/hp-zbook` | KURAL |  |
| `/hp-performans-monitor` | `/hp-monitor` | KURAL | HP Z Monitör sayfası mevcut, canonical düzeltilip yönlendirildi |
| `/hp-plotter` | `/designjet` | KURAL |  |
| `/hp-plotter-servis` | `/hp` | KURAL | HP hub sayfası zaten Yetkili Servis içeriyor (onaylandı) |
| `/hsm-works` | `/fusion` | KURAL | HSMWorks → Fusion CAM'e evrildi (onaylandı) |
| `/insaat-icin-bim` | `/bim` | KURAL |  |
| `/insaat-proje-yönetimi` | `/insaat-yonetimi` | KURAL | URL'de Türkçe karakter vardı |
| `/insaat-yazilimlari` | `/sektor-insaat` | KURAL |  |
| `/inventor-cam` | `/cam` | KURAL | Inventor CAM → CAM çözüm sayfası |
| `/inventor-nesting` | `/nesting` | KURAL |  |
| `/kampanyalar` | `/` | GOZDEN | kampanya sayfası yok — karar |
| `/makine-ve-ekipman-uretimi` | `/sektor-makine` | KURAL |  |
| `/mecollection` | `/me-collection` | KURAL | slug farkı |
| `/mekanik-tesisat` | `/bim` | KURAL | MEP içerik BIM sayfasında (onaylandı) |
| `/mekanik-tesisat-yazilimlari` | `/bim` | KURAL | MEP içerik BIM sayfasında (onaylandı) |
| `/mep-icin-bim` | `/bim` | KURAL |  |
| `/mimari` | `/sektor-mimari` | KURAL |  |
| `/mimarlik-icin-bim` | `/bim` | KURAL |  |
| `/mimarlik-yazilimlari` | `/sektor-mimari` | KURAL |  |
| `/nastran` | `/inventor` | KURAL | Nastran → Inventor Nastran; Inventor sayfasına bölüm eklendi |
| `/otomotiv` | `/sektor-otomotiv` | KURAL |  |
| `/otomotiv-agirlik-azaltma` | `/sektor-otomotiv` | KURAL |  |
| `/oyun-vr-yazilimlari` | `/sektor-medya` | KURAL |  |
| `/pdmc` | `/pdm-collection` | KURAL | slug farkı |
| `/plant-3d` | `/autocad` | KURAL | toolset (Plant 3D) |
| `/plm-ve-pdm-yazilimlari` | `/plm` | KURAL |  |
| `/point-layout` | `/revit` | KURAL | Point Layout EOL → Revit'e yönlendirildi |
| `/raster-design` | `/autocad` | KURAL | toolset |
| `/robot-structure-analysis` | `/robot-structural` | KURAL | slug farkı |
| `/sanatsalbaski` | `/sanatsal-baski` | KURAL | slug farkı |
| `/simulasyon-ve-analiz` | `/simulasyon` | KURAL |  |
| `/simulasyon-ve-analiz-yazilimlari` | `/simulasyon` | KURAL |  |
| `/statik` | `/revit` | KURAL | statik kategori → Revit'e yönlendirildi (onaylandı) |
| `/statik-yazilimlari` | `/revit` | KURAL | statik kategori → Revit'e yönlendirildi (onaylandı) |
| `/teklif-iste` | `/teklif-iste` | BIREBIR | 2026-08-02: artık `/iletisim`'e yönlenmiyor — kendi teklif isteme formuna sahip özel sayfa (`cadbim_teklif_iste.html`); nav'daki "Teklif Al" butonu buraya bağlandı |
| `/tesis-tasarimi-icin-bim` | `/bim` | KURAL |  |
| `/ultimaker-3d-yazicilar` | `/ultimaker` | KURAL |  |
| `/ultimaker-aksesuar` | `/ultimaker` | KURAL | geçici — UltiMaker aksesuar sayfası planlandı |
| `/urun-tasarimi-uretim-yazilimlari` | `/pdm-collection` | KURAL |  |
| `/vault-plm` | `/vault-pdm` | KURAL | Vault PLM bölümü vault-pdm sayfasında |
| `/video-oyun-tasarimi` | `/sektor-medya` | KURAL |  |
| `/vred` | `/vred` | BIREBIR | yeni VRED ürün sayfası oluşturuldu (2026-07-28) |
| `/webinar` | `/webinar` | BIREBIR | gerçek webinar takvimi kuruldu, 9 aktif webinar |
| `/yapi-urunleri-ureticileri-icin-bim` | `/bim` | KURAL |  |
| `/yapi-urunleri-uretim-ve-imalati` | `/bim` | KURAL |  |
| `/yapisal-mühendislik-icin-bim` | `/bim` | KURAL | URL'de Türkçe karakter vardı |

## 5. Blog (242 yazı + 97 taksonomi) — TAMAMLANDI (2026-07-28)

Seçenek A uygulandı: Blog mimarisi kuruldu (kategori+ürün filtreli hub + `post/<slug>.html` şeması, aynı slug korunarak) — 301 gerekmedi, içerik SEO değeri korundu.

- **242 orijinal Wix yazısı:** Tamamı gerçek içerikle taşındı (WebFetch ile canlı siteden çekildi, uydurma metin kullanılmadı). 2 yazı gerçek içeriği olmadığı için (thin/duplicate) `/` anasayfaya yönlendirildi.
- **497 YouTube videosu:** Kanaldaki teknik destek videoları da blog'a video-postu olarak eklendi (başlık/açıklama YouTube'dan aynen alındı). Kanal artık günlük otomatik taranıyor (`.github/workflows/youtube-blog-sync.yml`), yeni video geldikçe blog otomatik güncelleniyor.
- **97 taksonomi sayfası** (`/blog/categories/*`): Ayrı statik sayfa olarak yeniden kurulmadı; client-side kategori/ürün filtre sistemi olan `/blog` hub'ına 301'lendi (aynı işlevi tek sayfada sağlıyor).
- **Toplam blog yazısı:** 739 — hepsi `assets/data/blog-posts.json` içinde tek kaynak olarak tutuluyor.

## 6. Dinamik Koleksiyonlar — Kural Özetleri

| Koleksiyon | Öğe | Kural |
|---|---|---|
| `/adobe-yaraticilik/*` | 30 | Uygulama bazlı (Photoshop...) |
| `/basari-oykuleri/*` | 4 | Wix placeholder içerikti; gerçek DECONS vakası #decons'a, diğerleri hub sayfaya yönlendirildi |
| `/chaos/*` | 15 | Ürün bazlı (Corona, Vantage, Phoenix, Anima, Cosmos) |
| `/danismanlik/*` | 9 | → /danismanlik |
| `/designjet-fotograf/*` | 2 | Model bazlı (Z) |
| `/designjet-grafik/*` | 3 | Model bazlı (Z) |
| `/designjet-ofis/*` | 11 | Model bazlı eşleme (T230/T250→t200...) |
| `/designjet-sarf/*` | 11 | → /designjet (sarf sayfası yok) |
| `/designjet-tarayici/*` | 2 | HD/SD Pro |
| `/designjet-uretim/*` | 4 | Model bazlı (XL) |
| `/egitimler/*` | 39 | → /egitimler |
| `/etkinlikler/*` | 1 | → / (karar) |
| `/hp-masaustu-workstation/*` | 24 | → /hp-z-workstation |
| `/hp-mobil-isistasyonu/*` | 5 | → /hp-zbook |
| `/hp-performans-monitor/*` | 9 | → /hp (monitör sayfası yok — karar) |
| `/kampanyalar/*` | 4 | → / (karar) |
| `/kvkk/*` | 11 | → /kvkk |
| `/sketchup/*` | 12 | Plan bazlı (Go/Studio/Pro) |
| `/ultimaker-3d-yazicilar/*` | 5 | Model bazlı (Method XL, Factor 4, Sketch...) |
| `/ultimaker-aksesuar/*` | 5 | → /ultimaker |

Öğe bazlı tam liste CSV'dedir; `GOZDEN` işaretli satırlar yayına almadan önce tek tek onaylanmalı.

## 7. İçerik / Ürün Adı Değişiklikleri (eski site → güncel)

Yeni site içeriği güncel adlandırmayla yazıldı. Eski site ziyaretçisi/aramaları için karşılıklar:

| Eski adlandırma | Güncel karşılık | Yeni sayfa |
|---|---|---|
| Autodesk Construction Cloud / BIM 360 | Autodesk Forma (AEC endüstri bulutu) | `/autodesk-forma` |
| BIM 360 Docs / Autodesk Docs | Forma Data Management (CDE) | `/autodesk-docs` |
| BIM Collaborate Pro | Forma Design Collaboration | `/bim-collaborate-pro` |
| Fusion 360 | Autodesk Fusion | `/fusion` |
| Fusion 360 Manage | Fusion Manage | `/fusion-manage` |
| ShotGrid (Shotgun) | Flow Production Tracking | `/flow-production-tracking` |
| HSMWorks | Fusion (CAM iş akışları) | `/fusion` |
| Inventor CAM | CAM & İmalat çözümü içinde | `/cam` |
| Inventor Nesting | Nesting çözümü içinde | `/nesting` |
| AutoCAD Architecture/MEP/Electrical/Mechanical/Map 3D/Plant 3D/Raster Design | AutoCAD 'specialized toolsets' — tek üründe | `/autocad` |
| Robot Structure Analysis (eski yazım) | Robot Structural Analysis | `/robot-structural` |
| Nastran, Autodesk CFD | Satıştan kalktı → Simülasyon & Analiz çözümü | `/simulasyon` |
| Point Layout | Satıştan kalktı → BIM çözümü | `/bim` |
| VRED | Yeni sitede sayfası yok — KARAR (görselleştirme) | `/gorsellestirme` |
| MakerBot Sketch | Sketch Sprint (UltiMaker çatısı) | `/sketch-sprint` |
| Method XL (MakerBot) | UltiMaker Method XL | `/method-xl` |
| V-Ray/Enscape/Veras ayrı sayfalar | Chaos hub'ında birleşik | `/chaos` |
| HP performans monitörleri | Yeni sitede yok — KARAR | `/hp` |
| DesignJet sarf malzemeleri | Yeni sitede yok — KARAR | `/designjet` |

## 8. Geçiş Günü Kontrol Listesi

- [ ] Host 301 motoru hazır (CSV → `_redirects` dönüşümü)
- [ ] GOZDEN satırları Onur onayından geçti
- [ ] Blog kararı verildi (A/B)
- [ ] `sitemap.xml` yeni host'ta doğrulandı, Search Console'a gönderildi
- [ ] robots.txt yayında, sitemap satırı var
- [ ] www yönlendirmesi + HTTPS zorlaması aktif
- [ ] İlk 48 saat: canlı 404 logları → eksik 301 yaması
- [ ] 4 hafta: Search Console kapsama/404 haftalık takip
