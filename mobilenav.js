/* ============================================================
   Cadbim — Mobil Navigasyon + Site İçi Arama
   Tek kaynak. Her sayfaya <script src="mobilenav.js" defer> ile eklenir.
   Kendi stilini enjekte eder; sayfa CSS değişkenlerine bağlı değildir.
   ============================================================ */
(function () {
  "use strict";

  /* Sayfa derinligine gore ic link on eki (kok sayfalar icin "", post/ altindaki
     blog yazilari icin "../") — ayni dosya hem kokten hem post/'tan yuklendigi
     icin on ek calisma zamaninda hesaplanir. */
  var BASE = /\/post\//.test(window.location.pathname) ? "../" : "";
  function withBase(p) {
    if (!p) return BASE || "./";
    if (/^https?:\/\//.test(p) || p.indexOf("mailto:") === 0 || p.indexOf("tel:") === 0) return p;
    if (p === "/") return BASE + "index.html";
    return BASE + p.replace(/^\//, "");
  }

  /* ---- IA: menü grupları ---- */
  var GROUPS = [
    {
      label: "Ürünler", href: "/urunler",
      items: [
        ["Autodesk", "/autodesk"],
        ["Adobe", "/adobe"],
        ["HP DesignJet", "/designjet"],
        ["HP Workstations", "/hp-z-workstation"],
        ["HP Build Workspace", "/hp-build-workspace"],
        ["Chaos", "/chaos"],
        ["UltiMaker", "/ultimaker"],
        ["SketchUp", "/sketchup"],
        ["Lumion", "/lumion"],
        ["Microsoft", "/microsoft"]
      ]
    },
    {
      label: "Çözümler", href: "/cozumler",
      items: [
        ["Dijital Dönüşüm", "/dijital-donusum"],
        ["BIM", "/bim"],
        ["BIM İçerik & Obje Üretimi", "/bim-icerik-uretimi"],
        ["İnşaat Proje Yönetimi", "/insaat-yonetimi"],
        ["Gerçeklik Yakalama", "/gerceklik-yakalama"],
        ["Dijital İkiz", "/dijital-ikiz"],
        ["Simülasyon & Analiz", "/simulasyon"],
        ["Tolerans Analizi", "/tolerans-analizi"],
        ["Tasarım Otomasyonu", "/tasarim-otomasyonu"],
        ["CAM & İmalat", "/cam"],
        ["Eklemeli İmalat & 3D Baskı", "/eklemeli-imalat"],
        ["Nesting", "/nesting"],
        ["Fabrika Tasarımı", "/fabrika-tasarimi"],
        ["PLM", "/plm"],
        ["PDM", "/pdm"],
        ["Görselleştirme & Render", "/gorsellestirme"],
        ["AI Destekli Görselleştirme", "/ai-gorsellestirme"],
        ["Yaratıcı İçerik & Tasarım", "/yaratici-icerik"]
      ]
    },
    {
      label: "Endüstriler", href: "/sektor-mimari",
      items: [
        ["Mimarlık", "/sektor-mimari"],
        ["Makine & Üretim", "/sektor-makine"],
        ["Medya & Eğlence", "/sektor-medya"],
        ["İç Mimarlık", "/sektor-icmimarlik"],
        ["İnşaat & Altyapı", "/sektor-insaat"],
        ["Mekanik Tesisat", "/sektor-tesisat"],
        ["Otomotiv", "/sektor-otomotiv"],
        ["Eğitim", "/sektor-egitim"],
        ["Savunma ve Havacılık", "/sektor-havacilik"]
      ]
    },
    {
      label: "Hizmetler", href: "/danismanlik",
      items: [
        ['<span class="sanatsal-gradient">Sanatsal Baskı Atölyesi</span>', "/sanatsal-baski"],
        ["Danışmanlık", "/danismanlik"],
        ["HP Plotter Teknik Servis", "/designjet-teknik-servis"],
        ["Yazılım Geliştirme", "/yazilim-gelistirme"]
      ]
    },
    { label: "Eğitimler", href: "/egitimler", flat: true }
  ];

  /* Grup dışı ana linkler */
  var TOP_LINKS = [
    ["Hakkımızda", "/hakkimizda"],
    ["İletişim", "/iletisim"],
    ["KVKK", "/kvkk"],
    ["Blog", "/blog"]
  ];

  /* ---- Arama indeksi: tüm sayfalar + anahtar kelimeler ---- */
  var INDEX = [
    ["Ana Sayfa", "/", "cadbim autodesk adobe gold partner", "Sayfa"],
    ["Tüm Ürünler", "/urunler", "urunler katalog marka autodesk adobe hp chaos", "Sayfa"],
    ["HP DesignJet Ailesi", "/designjet", "hp designjet plotter tum modeller katalog", "Ürün"],
    ["DesignJet T200 Serisi", "/designjet-t200", "hp t230 t250 24 inc plotter giris 3c753a 3ed58a 3ed67a 3ed68a 3ed69a 3ed70a 3ed71a 3ed77a 3ed78a 3ed79a 5hb07a 8aj60a 9gf94a", "Ürün"],
    ["DesignJet T600 Serisi", "/designjet-t600", "hp t630 t650 kucuk ofis plotter 3ed58a 3ed67a 3ed68a 3ed69a 3ed70a 3ed71a 3ed77a 3ed78a 3ed79a 5hb11a", "Ürün"],
    ["DesignJet T830 MFP", "/designjet-t830", "hp t830 tarama kopyalama santiye 3wx25a", "Ürün"],
    ["DesignJet T850", "/designjet-t850", "hp t850 36 inc plotter mfp 2y9h0a 2y9h2h", "Ürün"],
    ["DesignJet T950", "/designjet-t950", "hp t950 36 inc istifleyici plotter 2y9h1a 2y9h3a", "Ürün"],
    ["DesignJet Smart Tank", "/designjet-smart-tank", "hp t858 t908 murekkep tank dusuk maliyet 2y9h4a 2y9h6a", "Ürün"],
    ["DesignJet T1600", "/designjet-t1600", "hp t1600 departman cift rulo plotter 3ek10a 3ek11a 3ek12a 3ek13a", "Ürün"],
    ["DesignJet T1700", "/designjet-t1700", "hp t1700 44 inc gis harita plotter 1vd87a 1vd88a", "Ürün"],
    ["DesignJet T2600 MFP", "/designjet-t2600", "hp t2600 tarama kopyalama departman 3ek15a 3xb78a", "Ürün"],
    ["DesignJet T1600 Plus Edition", "/designjet-t1600-plus", "hp t1600 plus build connected workspace bulut plotter yeni 3ek10d", "Ürün"],
    ["DesignJet T2600 MFP Plus Edition", "/designjet-t2600-plus", "hp t2600 plus build connected vektorizasyon qr tarama yeni 3jn69a", "Ürün"],
    ["DesignJet XL 3600", "/designjet-xl3600", "hp xl 3600 dayanikli uretim mfp 3jj54a 6cc86a 6kd23a 6kd25a 6se87a 6se88a", "Ürün"],
    ["DesignJet XL 3800", "/designjet-xl3800", "hp xl 3800 en hizli 6 a1 dakika 7qr88a", "Ürün"],
    ["DesignJet Z6810", "/designjet-z6810", "hp z6810 42 inc uretim fotograf 2qu12a", "Ürün"],
    ["DesignJet Z6 Pro", "/designjet-z6pro", "hp z6 pro 64 inc grafik uretim 1a4t0a 1xb17a 1xb18a 1xb19a 1xb20a 1xb21a 1xb22a 2qu25a 3ed19a 3ee09a 5ek00a 7hc73a 7hc74a 7hc76a 8sw00a 8sw01a 8sw11a", "Ürün"],
    ["DesignJet Z9+ Pro", "/designjet-z9pro", "hp z9 pro 64 inc fine art 12 murekkep 1a4t0a 1xb03a 1xb04a 1xb05a 1xb06a 1xb07a 1xb08a 1xb09a 1xb10a 1xb11a 1xb12a 2rm82a 3ed19a 3ee09a 5ek00a 7hc73a 7hc74a 7hc75a 7hc76a 8sw00a 8sw01a 8sw11a", "Ürün"],
    ["DesignJet Z6 PostScript", "/designjet-z6ps", "hp z6 ps grafik harita pixel control 1qf38a", "Ürün"],
    ["DesignJet Z9+ PostScript", "/designjet-z9ps", "hp z9 ps fotograf fine art studyo 1qf38a 2qx55a", "Ürün"],
    ["DesignJet HD Pro 2 Tarayıcı", "/designjet-hd-pro", "hp hd pro 2 42 inc buyuk format tarayici 1487ena", "Ürün"],
    ["DesignJet SD Pro 2 Tarayıcı", "/designjet-sd-pro", "hp sd pro 2 44 inc buyuk format tarayici 5ek01a", "Ürün"],
    ["HP DesignJet Sarf Malzemeleri", "/designjet-sarf-malzeme", "hp murekkep baski kafasi medya kagit rulo sarf", "Ürün"],
    ["HP DesignJet Teknik Servis", "/designjet-teknik-servis", "hp plotter ariza onarim bakim servis talebi", "Hizmet"],
    ["HP Series 7 Pro Monitör", "/hp-monitor", "hp monitor z serisi ekran", "Ürün"],
    ["AEC Collection", "/aec-collection", "autodesk koleksiyon revit civil3d paket", "Ürün"],
    ["PD&M Collection", "/pdm-collection", "autodesk koleksiyon inventor vault imalat paket", "Ürün"],
    ["M&E Collection", "/me-collection", "autodesk koleksiyon maya 3dsmax arnold paket", "Ürün"],
    ["Autodesk Forma", "/autodesk-forma", "autodesk forma construction cloud build takeoff docs insaat saha", "Ürün"],
    ["Forma Design Collaboration", "/bim-collaborate-pro", "autodesk bim collaborate pro revit bulut worksharing ortak calisma", "Ürün"],
    ["Forma Data Management", "/autodesk-docs", "autodesk docs cde dokuman yonetimi iso 19650", "Ürün"],
    ["Vehicle Tracking", "/vehicle-tracking", "autodesk arac donus izi swept path otopark", "Ürün"],
    ["Photoshop", "/photoshop", "adobe goruntu duzenleme retus firefly", "Ürün"],
    ["Illustrator", "/illustrator", "adobe vektor logo grafik", "Ürün"],
    ["InDesign", "/indesign", "adobe sayfa tasarimi dizgi katalog yayin", "Ürün"],
    ["Premiere Pro", "/premiere-pro", "adobe video kurgu montaj", "Ürün"],
    ["After Effects", "/after-effects", "adobe motion graphics vfx efekt", "Ürün"],
    ["Lightroom", "/lightroom", "adobe fotograf raw duzenleme arsiv", "Ürün"],
    ["Substance 3D", "/substance3d", "adobe 3d doku malzeme painter designer", "Ürün"],
    ["Firefly", "/firefly", "adobe uretken yapay zeka ai gorsel", "Ürün"],
    ["Adobe Express", "/adobe-express", "adobe sablon sosyal medya hizli icerik", "Ürün"],
    ["Adobe Stock", "/adobe-stock", "adobe stok gorsel video lisans", "Ürün"],
    ["Adobe Acrobat Pro", "/acrobat-pro", "adobe pdf e-imza acrobat sign form dokuman", "Ürün"],
    ["Adobe Creative Cloud", "/creative-cloud", "adobe photoshop illustrator premiere after effects indesign firefly paket", "Ürün"],
    ["Chaos Corona", "/corona", "chaos render mimari fotogercekci", "Ürün"],
    ["Chaos Vantage", "/vantage", "chaos gercek zamanli ray tracing", "Ürün"],
    ["Chaos Phoenix", "/phoenix", "chaos ates duman sivi simulasyon vfx", "Ürün"],
    ["Chaos Anima", "/anima", "chaos kalabalik insan animasyon", "Ürün"],
    ["Chaos Cosmos", "/cosmos", "chaos varlik kutuphane model hdri", "Ürün"],
    ["Chaos Enscape", "/enscape", "chaos enscape gercek zamanli render vr revit sketchup archicad rhino", "Ürün"],
    ["Chaos V-Ray", "/vray", "chaos vray fotogercekci render 3dsmax maya sketchup revit", "Ürün"],
    ["Chaos Veras AI", "/veras", "chaos veras yapay zeka konsept gorsellestirme ai render", "Ürün"],
    ["Lumion View", "/lumion-view", "lumion cad icinde render sketchup revit", "Ürün"],
    ["Lumion Studio", "/lumion-studio", "lumion ekip paket floating", "Ürün"],
    ["Lumion Cloud", "/lumion-cloud", "lumion paylasim yorum onay bulut", "Ürün"],
    ["SketchUp Pro", "/sketchup-pro", "sketchup masaustu layout ekstansiyon warehouse", "Ürün"],
    ["SketchUp Pro Scan", "/sketchup-pro-scan", "sketchup scan essentials nokta bulutu rolove", "Ürün"],
    ["SketchUp Pro Civil Contractor", "/sketchup-pro-civil-contractor", "sketchup trimble siteworks saha hafriyat aplikasyon", "Ürün"],
    ["SketchUp Advanced Workflows", "/sketchup-advanced-workflows", "sketchup revit importer scan essentials nokta bulutu", "Ürün"],
    ["SketchUp Go", "/sketchup-go", "sketchup web ipad mobil modelleme", "Ürün"],
    ["SketchUp Studio", "/sketchup-studio", "sketchup vray scan essentials revit importer", "Ürün"],
    ["Trimble Connect", "/trimble-connect", "trimble bulut model isbirligi ifc", "Ürün"],
    ["UltiMaker Factor 4", "/factor4", "ultimaker endustriyel 3d yazici pps-cf", "Ürün"],
    ["Method XL", "/method-xl", "ultimaker abs muhendislik 3d yazici", "Ürün"],
    ["Sketch Sprint", "/sketch-sprint", "makerbot egitim sinif 3d yazici", "Ürün"],
    ["UltiMaker Cura", "/cura", "ultimaker dilimleme slicer yazilim", "Ürün"],
    ["Digital Factory", "/digital-factory", "ultimaker filo yonetim bulut baski", "Ürün"],
    ["UltiMaker S3", "/ultimaker-s3", "ultimaker s3 kompakt masaustu 3d yazici cift ekstruder", "Ürün"],
    ["UltiMaker S5", "/ultimaker-s5", "ultimaker s5 buyuk baski hacmi 3d yazici", "Ürün"],
    ["UltiMaker S7", "/ultimaker-s7", "ultimaker s7 air manager pei tabla 3d yazici", "Ürün"],
    ["UltiMaker S8", "/ultimaker-s8", "ultimaker s8 endustriyel hizli 3d yazici cheetah", "Ürün"],
    ["UltiMaker Malzeme Kütüphanesi", "/ultimaker-malzeme", "ultimaker pla abs petg nylon pc tpu malzeme filament", "Ürün"],
    ["HP Z Workstation", "/hp-z-workstation", "hp is istasyonu z2 z4 z6 z8 fury masaustu", "Ürün"],
    ["HP Z1 G1i", "/hp-z1-g1i", "hp z1 g1i masaustu is istasyonu giris seviye cad b34jses a2kl5es", "Ürün"],
    ["HP Z2 G1i", "/hp-z2-g1i", "hp z2 g1i masaustu is istasyonu cad a2kx6es b34k0es a2kr1es b34jzes a2kr0es b34jfes b34jges cu0j1es", "Ürün"],
    ["HP Z2m G1i", "/hp-z2m-g1i", "hp z2m g1i mini masaustu is istasyonu cad a2kh2es a2kj1es", "Ürün"],
    ["HP Z4 G5", "/hp-z4-g5", "hp z4 g5 masaustu is istasyonu tek islemci cad 5e8g1ea 5e8g3ea 5e1s3es b34shes b34sjes b34skes", "Ürün"],
    ["HP Z6 G5", "/hp-z6-g5", "hp z6 g5 masaustu is istasyonu cift islemci cad 5e8g6ea 5e8k4ea 5e1s4es 5e1s5es", "Ürün"],
    ["HP Z6 G5 A", "/hp-z6-g5-a", "hp z6 g5 a masaustu is istasyonu cad b34tbes", "Ürün"],
    ["HP Z8 G5", "/hp-z8-g5", "hp z8 g5 masaustu is istasyonu simulasyon render 5e1s6es", "Ürün"],
    ["HP Z8 G5 Fury", "/hp-z8-g5-fury", "hp z8 g5 fury masaustu is istasyonu simulasyon render b34tces", "Ürün"],
    ["HP ZBook", "/hp-zbook", "hp mobil is istasyonu laptop firefly power studio fury", "Ürün"],
    ["HP ZBook 8 G1i 14", "/hp-zbook-8-g1i-14", "hp zbook 8 g1i 14 mobil is istasyonu giris seviye a3zw7et a3zw6et", "Ürün"],
    ["HP ZBook 8 G1i 16", "/hp-zbook-8-g1i-16", "hp zbook 8 g1i 16 mobil is istasyonu giris seviye b30hges a3zw3et", "Ürün"],
    ["HP ZBook 8 G2i 14", "/hp-zbook-8-g2i-14", "hp zbook 8 g2i 14 mobil is istasyonu giris seviye dn5y7ea dn5y6ea dn9t6es dn6a5ea", "Ürün"],
    ["HP ZBook 8 G2i 16", "/hp-zbook-8-g2i-16", "hp zbook 8 g2i 16 mobil is istasyonu giris seviye dn5z2ea dn5y5ea", "Ürün"],
    ["HP ZBook Fury 16/18 G1i", "/hp-zbook-fury-16-18-g1i", "hp zbook fury 16 18 g1i mobil is istasyonu cad 5f9t8es c65g3es c65g7es c65g8es c65g2es c65h8es", "Ürün"],
    ["HP ZBook Power zX 16 G1i", "/hp-zbook-power-zx-16-g1i", "hp zbook power zx 16 g1i mobil is istasyonu cad b30hles b30hmes b30hnes cu0j2es", "Ürün"],
    ["HP ZBook Power zX 16 G2i", "/hp-zbook-power-zx-16-g2i", "hp zbook power zx 16 g2i mobil is istasyonu cad dn5z9ea dn9t2es dn9t3es dn6b3ea", "Ürün"],
    ["HP ZBook Ultra 14 G1a", "/hp-zbook-ultra-14-g1a", "hp zbook ultra 14 g1a mobil is istasyonu cad b30hdes", "Ürün"],
    ["Autodesk", "/autodesk", "autocad revit inventor fusion civil3d gold partner", "Ürün"],
    ["Adobe", "/adobe", "creative cloud photoshop illustrator", "Ürün"],
    ["HP", "/hp", "workstation 3d baski z", "Ürün"],
    ["HP Build & Workspace", "/hp-build-workspace", "hp build workspace", "Ürün"],
    ["Chaos", "/chaos", "vray corona render", "Ürün"],
    ["UltiMaker", "/ultimaker", "3d yazici printer", "Ürün"],
    ["SketchUp", "/sketchup", "3d modelleme mimari", "Ürün"],
    ["Lumion", "/lumion", "render gorsellestirme mimari", "Ürün"],
    ["Microsoft", "/microsoft", "surface office 365", "Ürün"],
    ["AutoCAD", "/autocad", "autodesk 2d 3d cizim", "Ürün"],
    ["Revit", "/revit", "bim autodesk mimari", "Ürün"],
    ["Inventor", "/inventor", "autodesk mekanik makine", "Ürün"],
    ["Fusion", "/fusion", "autodesk cad cam", "Ürün"],
    ["Fusion Manage", "/fusion-manage", "plm autodesk", "Ürün"],
    ["Civil 3D", "/civil3d", "altyapi insaat autodesk", "Ürün"],
    ["Alias", "/alias", "otomotiv tasarim yuzey", "Ürün"],
    ["Vault PDM", "/vault-pdm", "veri yonetimi autodesk", "Ürün"],
    ["Çözümler", "/cozumler", "genel bakis", "Çözüm"],
    ["BIM", "/bim", "revit yapi bilgi modelleme", "Çözüm"],
    ["PLM", "/plm", "urun yasam dongusu", "Çözüm"],
    ["PDM", "/pdm", "urun veri yonetimi vault", "Çözüm"],
    ["Simülasyon & Analiz", "/simulasyon", "cfd fea analiz", "Çözüm"],
    ["CAM & İmalat", "/cam", "imalat cnc uretim", "Çözüm"],
    ["Tolerans Analizi", "/tolerans-analizi", "gd&t tolerans", "Çözüm"],
    ["Nesting", "/nesting", "yerlesim kesim optimizasyon", "Çözüm"],
    ["Fabrika Tasarımı", "/fabrika-tasarimi", "factory layout yerlesim", "Çözüm"],
    ["Tasarım Otomasyonu", "/tasarim-otomasyonu", "ilogic otomasyon", "Çözüm"],
    ["Görselleştirme & Render", "/gorsellestirme", "render gorselleştirme vray corona lumion enscape", "Çözüm"],
    ["Eklemeli İmalat & 3D Baskı", "/eklemeli-imalat", "3d baski eklemeli imalat ultimaker", "Çözüm"],
    ["İnşaat Proje Yönetimi", "/insaat-yonetimi", "construction cloud saha cde santiye", "Çözüm"],
    ["Yaratıcı İçerik & Tasarım", "/yaratici-icerik", "adobe grafik video icerik", "Çözüm"],
    ["Gerçeklik Yakalama", "/gerceklik-yakalama", "tarama nokta bulutu recap scan-to-bim rolove", "Çözüm"],
    ["Simülasyon", "/simulasyon", "analiz", "Çözüm"],
    ["Sanatsal Baskı", "/sanatsal-baski", "fine art print baski", "Çözüm"],
    ["Yazılım Geliştirme", "/yazilim-gelistirme", "api ozel yazilim", "Hizmet"],
    ["Danışmanlık", "/danismanlik", "consulting proje", "Hizmet"],
    ["Eğitimler", "/egitimler", "atc sertifika kurs", "Hizmet"],
    ["Webinar Takvimi", "/webinar", "webinar online etkinlik ucretsiz", "Hizmet"],
    ["Teklif İste", "/teklif-iste", "teklif form yazilim donanim danismanlik", "Sayfa"],
    ["Başarı Öyküleri", "/basari-oykuleri", "musteri referans fusion inventor nastran maya revit vault", "Kurumsal"],
    ["Endüstriler", "/endustriler", "sektor mimari insaat otomotiv medya egitim havacilik uzman", "Sayfa"],
    ["Sürdürülebilirlik", "/surdurulebilirlik", "cevre yesil", "Kurumsal"],
    ["Mimarlık", "/sektor-mimari", "sektor mimari", "Sektör"],
    ["İç Mimarlık & Tasarım", "/sektor-icmimarlik", "sektor ic mimarlik dekorasyon mobilya interior", "Sektör"],
    ["İnşaat & Altyapı", "/sektor-insaat", "sektor insaat altyapi", "Sektör"],
    ["Mekanik Tesisat", "/sektor-tesisat", "sektor mekanik tesisat mep hvac havalandirma kanal boru", "Sektör"],
    ["Makine & Üretim", "/sektor-makine", "sektor makine uretim imalat", "Sektör"],
    ["Otomotiv", "/sektor-otomotiv", "sektor otomotiv", "Sektör"],
    ["Medya & Eğlence", "/sektor-medya", "sektor medya eglence render", "Sektör"],
    ["Eğitim", "/sektor-egitim", "sektor egitim universite okul akademik lab", "Sektör"],
    ["Savunma ve Havacılık", "/sektor-havacilik", "sektor havacilik savunma defense aerospace", "Sektör"],
    ["Hakkımızda", "/hakkimizda", "kurumsal 1993 firma", "Kurumsal"],
    ["İletişim", "/iletisim", "adres telefon teklif form izmir ankara", "Kurumsal"],
    ["KVKK", "/kvkk", "kisisel veri gizlilik", "Yasal"],
    ["KVKK Politikası", "/kvkk-politikasi", "politika", "Yasal"],
    ["Gizlilik Politikası", "/kvkk-gizlilik-politikasi", "privacy", "Yasal"],
    ["Çerez Politikası", "/kvkk-cerez-politikasi", "cookie", "Yasal"],
    ["KVKK Başvuru Formu", "/kvkk-basvuru-formu", "basvuru", "Yasal"],
    ["Autodesk 3ds Max", "/3dsmax", "autodesk 3d modelleme animasyon render mimari vfx", "Ürün"],
    ["Autodesk Maya", "/maya", "autodesk animasyon vfx karakter modelleme", "Ürün"],
    ["Maya Creative", "/maya-creative", "autodesk maya uygun animasyon", "Ürün"],
    ["Autodesk Arnold", "/arnold", "autodesk render motoru vfx isik", "Ürün"],
    ["MotionBuilder", "/motionbuilder", "autodesk motion capture animasyon oyun", "Ürün"],
    ["Mudbox", "/mudbox", "autodesk dijital heykel doku boyama", "Ürün"],
    ["Autodesk Flame", "/flame", "autodesk vfx renk finishing compositing", "Ürün"],
    ["Golaem", "/golaem", "autodesk kalabalik crowd maya simulasyon", "Ürün"],
    ["Autodesk Flow Studio", "/flow-studio", "autodesk wonder studio ai sahne motion capture", "Ürün"],
    ["Flow Production Tracking", "/flow-production-tracking", "autodesk shotgrid produksiyon takip pipeline", "Ürün"],
    ["Navisworks", "/navisworks", "autodesk koordinasyon cakisma clash 4d 5d", "Ürün"],
    ["InfraWorks", "/infraworks", "autodesk altyapi konsept kentsel gis", "Ürün"],
    ["Advance Steel", "/advance-steel", "autodesk celik detaylandirma yapisal", "Ürün"],
    ["Robot Structural Analysis", "/robot-structural", "autodesk yapisal analiz statik betonarme", "Ürün"],
    ["Autodesk Fabrication CADmep", "/fabrication-cadmep", "autodesk mep mekanik elektrik tesisat bim detaylandirma", "Ürün"],
    ["Autodesk Fabrication CAMduct", "/fabrication-camduct", "autodesk kanal mep cnc imalat parametrik uretim", "Ürün"],
    ["Autodesk Fabrication ESTmep", "/fabrication-estmep", "autodesk mep taahhut maliyet tahmini", "Ürün"],
    ["Autodesk CFD", "/cfd", "autodesk hesaplamali akiskanlar dinamigi isil analiz simulasyon", "Ürün"],
    ["Autodesk VRED", "/vred", "autodesk otomotiv vr gercek zamanli gorsellestirme dijital prototip", "Ürün"],
    ["Autodesk Forma", "/forma", "autodesk erken tasarim site analiz spacemaker bulut", "Ürün"],
    ["Autodesk Tandem", "/tandem", "autodesk dijital ikiz operasyon varlik iot digital twin", "Ürün"],
    ["ReCap Pro", "/recap-pro", "autodesk nokta bulutu gerceklik yakalama tarama", "Ürün"],
    ["Autodesk Drive", "/autodesk-drive", "autodesk bulut depolama dosya paylasim", "Ürün"],
    ["Desktop Connector", "/desktop-connector", "autodesk bulut dosya senkron acc", "Ürün"],
    ["Design Review", "/design-review", "autodesk dwf isaretleme redline", "Ürün"],
    ["DWG TrueView", "/dwg-trueview", "autodesk dwg goruntuleyici ucretsiz", "Ürün"],
    ["AutoCAD LT", "/autocad-lt", "autodesk 2d cizim uygun", "Ürün"],
    ["AutoCAD Web", "/autocad-web", "autodesk tarayici bulut cizim", "Ürün"],
    ["Revit LT", "/revit-lt", "autodesk bim uygun mimari", "Ürün"],
    ["Factory Design Utilities", "/factory-design", "autodesk fabrika yerlesim layout", "Ürün"],
    ["FeatureCAM", "/featurecam", "autodesk cam otomasyon cnc", "Ürün"],
    ["PowerMill", "/powermill", "autodesk cam cok eksen cnc frezeleme", "Ürün"],
    ["PowerShape", "/powershape", "autodesk cam modelleme kalip", "Ürün"],
    ["Moldflow", "/moldflow", "autodesk enjeksiyon kalip simulasyon plastik", "Ürün"],
    ["Netfabb", "/netfabb", "autodesk eklemeli imalat 3d baski hazirlik", "Ürün"],
    ["Meshmixer", "/meshmixer", "autodesk mesh 3d baski hazirlik ucretsiz", "Ürün"],
    ["Tinkercad", "/tinkercad", "autodesk egitim 3d tasarim ucretsiz baslangic", "Ürün"],
    ["Dijital İkiz & Varlık Operasyonu", "/dijital-ikiz", "tandem operasyonel dijital ikiz varlik bim iot fm digital twin", "Çözüm"],
    ["KVKK Çalışan Adayı Aydınlatma", "/kvkk-calisan-adayi-aydinlatma", "aydinlatma calisan adayi", "Yasal"],
    ["KVKK İnternet Sitesi Aydınlatma", "/kvkk-internet-sitesi-aydinlatma", "aydinlatma internet sitesi ziyaretci", "Yasal"],
    ["KVKK Müşteri Aydınlatma", "/kvkk-musteri-aydinlatma", "aydinlatma musteri", "Yasal"],
    ["KVKK Potansiyel Müşteri Aydınlatma", "/kvkk-potansiyel-musteri-aydinlatma", "aydinlatma potansiyel musteri", "Yasal"],
    ["KVKK Tedarikçi Aydınlatma", "/kvkk-tedarikci-aydinlatma", "aydinlatma tedarikci", "Yasal"],
    ["KVKK Tedarikçi Çalışanı Aydınlatma", "/kvkk-tedarikci-calisani-aydinlatma", "aydinlatma tedarikci calisani", "Yasal"],
    ["KVKK Privacy Policy", "/kvkk-privacy-policy", "privacy policy english kvkk", "Yasal"],

    /* ---- Blog: kategori/ürün filtreli sonuçlar (blog.html ?topic= parametresini destekliyor) ---- */
    ["BIM (Blog)", "/blog?topic=BIM", "bim yazilari blog", "Blog"],
    ["CAD (Blog)", "/blog?topic=CAD", "cad yazilari blog", "Blog"],
    ["Simülasyon (Blog)", "/blog?topic=Sim%C3%BClasyon", "simulasyon yazilari blog", "Blog"],
    ["Görselleştirme (Blog)", "/blog?topic=G%C3%B6rselle%C5%9Ftirme", "gorsellestirme render yazilari blog", "Blog"],
    ["İnşaat (Blog)", "/blog?topic=%C4%B0n%C5%9Faat", "insaat yazilari blog", "Blog"],
    ["Medya (Blog)", "/blog?topic=Medya", "medya eglence yazilari blog", "Blog"],
    ["Otomotiv (Blog)", "/blog?topic=Otomotiv", "otomotiv yazilari blog", "Blog"],
    ["3D Baskı (Blog)", "/blog?topic=3D%20Bask%C4%B1", "3d baski eklemeli imalat yazilari blog", "Blog"],
    ["Fusion (Blog)", "/blog?topic=Fusion", "autodesk fusion yazilari blog", "Blog"],
    ["Revit (Blog)", "/blog?topic=Revit", "autodesk revit yazilari blog", "Blog"],
    ["Inventor (Blog)", "/blog?topic=Inventor", "autodesk inventor yazilari blog", "Blog"],
    ["AutoCAD (Blog)", "/blog?topic=AutoCAD", "autodesk autocad yazilari blog", "Blog"],
    ["AutoCAD LT (Blog)", "/blog?topic=AutoCAD%20LT", "autodesk autocad lt yazilari blog", "Blog"],
    ["Alias (Blog)", "/blog?topic=Alias", "autodesk alias yazilari blog", "Blog"],
    ["Vault (Blog)", "/blog?topic=Vault", "autodesk vault pdm yazilari blog", "Blog"],
    ["PLM (Blog)", "/blog?topic=PLM", "plm yazilari blog", "Blog"],
    ["PDM (Blog)", "/blog?topic=PDM", "pdm yazilari blog", "Blog"],
    ["Nastran (Blog)", "/blog?topic=Nastran", "autodesk nastran yazilari blog", "Blog"],
    ["BIM 360 (Blog)", "/blog?topic=BIM%20360", "bim 360 yazilari blog", "Blog"],
    ["InfraWorks (Blog)", "/blog?topic=InfraWorks", "autodesk infraworks yazilari blog", "Blog"],
    ["Forma (Blog)", "/blog?topic=Forma", "autodesk forma yazilari blog", "Blog"],
    ["Navisworks (Blog)", "/blog?topic=Navisworks", "autodesk navisworks yazilari blog", "Blog"],
    ["Civil 3D (Blog)", "/blog?topic=Civil%203D", "autodesk civil 3d yazilari blog", "Blog"],
    ["Advance Steel (Blog)", "/blog?topic=Advance%20Steel", "autodesk advance steel yazilari blog", "Blog"],
    ["Robot Structural (Blog)", "/blog?topic=Robot%20Structural", "autodesk robot structural analysis yazilari blog", "Blog"],
    ["CFD (Blog)", "/blog?topic=CFD", "autodesk cfd yazilari blog", "Blog"],
    ["Generative Design (Blog)", "/blog?topic=Generative%20Design", "uretken tasarim yazilari blog", "Blog"],
    ["Factory Design (Blog)", "/blog?topic=Factory%20Design", "fabrika tasarim yazilari blog", "Blog"],
    ["Fabrication (Blog)", "/blog?topic=Fabrication", "autodesk fabrication mep yazilari blog", "Blog"],
    ["Dynamo (Blog)", "/blog?topic=Dynamo", "autodesk dynamo yazilari blog", "Blog"],
    ["Maya (Blog)", "/blog?topic=Maya", "autodesk maya yazilari blog", "Blog"],
    ["3ds Max (Blog)", "/blog?topic=3ds%20Max", "autodesk 3ds max yazilari blog", "Blog"],
    ["Recap Pro (Blog)", "/blog?topic=Recap%20Pro", "autodesk recap pro yazilari blog", "Blog"],
    ["Illustrator (Blog)", "/blog?topic=Illustrator", "adobe illustrator yazilari blog", "Blog"],
    ["Photoshop (Blog)", "/blog?topic=Photoshop", "adobe photoshop yazilari blog", "Blog"],
    ["Acrobat (Blog)", "/blog?topic=Acrobat", "adobe acrobat yazilari blog", "Blog"],
    ["HP Build Workspace (Blog)", "/blog?topic=HP%20Build%20Workspace", "hp build workspace yazilari blog", "Blog"]
  ];

  /* ---- Türkçe karakter normalizasyonu (arama için) ---- */
  function norm(s) {
    return (s || "").toLowerCase()
      .replace(/ı/g, "i").replace(/İ/g, "i")
      .replace(/ş/g, "s").replace(/ğ/g, "g")
      .replace(/ü/g, "u").replace(/ö/g, "o").replace(/ç/g, "c")
      .replace(/\s+/g, " ").trim();
  }

  var ICON = {
    "Ürün": "ti-box", "Çözüm": "ti-topology-star-3", "Sektör": "ti-building-factory-2",
    "Kurumsal": "ti-building", "Hizmet": "ti-tools", "Yasal": "ti-gavel",
    "Sayfa": "ti-home", "Blog": "ti-news"
  };

  /* ---- Stil enjeksiyonu ---- */
  var css = `
  .cbm-btn{display:none;align-items:center;justify-content:center;width:44px;height:44px;border:none;background:transparent;color:#fff;cursor:pointer;position:relative;z-index:2001;margin-left:auto;-webkit-tap-highlight-color:transparent;}
  .cbm-btn span{position:absolute;left:11px;right:11px;height:2px;background:currentColor;border-radius:2px;transition:transform .28s cubic-bezier(.4,0,.2,1),opacity .2s;}
  .cbm-btn span:nth-child(1){top:15px;} .cbm-btn span:nth-child(2){top:21px;} .cbm-btn span:nth-child(3){top:27px;}
  body.cbm-open .cbm-btn span:nth-child(1){transform:translateY(6px) rotate(45deg);}
  body.cbm-open .cbm-btn span:nth-child(2){opacity:0;}
  body.cbm-open .cbm-btn span:nth-child(3){transform:translateY(-6px) rotate(-45deg);}
  @media(max-width:1024px){ .cbm-btn{display:flex;} .nav-links{display:none!important;} }

  .cbm-panel{position:fixed;inset:0;z-index:2000;background:#060c1a;color:#fff;
    display:flex;flex-direction:column;transform:translateX(100%);transition:transform .34s cubic-bezier(.4,0,.2,1);
    visibility:hidden;overscroll-behavior:contain;-webkit-overflow-scrolling:touch;}
  body.cbm-open .cbm-panel{transform:translateX(0);visibility:visible;}
  .cbm-panel *{box-sizing:border-box;}

  .cbm-top{position:sticky;top:0;z-index:3;background:#060c1a;padding:14px 18px 12px;border-bottom:.5px solid rgba(255,255,255,.08);}
  .cbm-search{display:flex;align-items:center;gap:10px;background:rgba(255,255,255,.06);border:1px solid rgba(0,200,240,.22);border-radius:12px;padding:0 14px;height:50px;}
  .cbm-search i{font-size:19px;color:#00c8f0;flex-shrink:0;}
  .cbm-search input{flex:1;background:none;border:none;outline:none;color:#fff;font-size:16px;font-family:inherit;min-width:0;}
  .cbm-search input::placeholder{color:rgba(255,255,255,.4);}
  .cbm-clear{border:none;background:none;color:rgba(255,255,255,.45);font-size:19px;cursor:pointer;display:none;padding:4px;}

  .cbm-body{flex:1;overflow-y:auto;padding:8px 12px 40px;}

  /* Arama sonuçları */
  .cbm-results{display:none;padding-top:6px;}
  .cbm-results.on{display:block;}
  .cbm-menu.off{display:none;}
  .cbm-res{display:flex;align-items:center;gap:14px;padding:14px 12px;border-radius:12px;text-decoration:none;color:#fff;min-height:56px;}
  .cbm-res:active{background:rgba(0,200,240,.1);}
  .cbm-res i{font-size:20px;color:#00c8f0;width:24px;text-align:center;flex-shrink:0;}
  .cbm-res .t{font-size:15.5px;font-weight:600;}
  .cbm-res .k{font-size:11px;color:rgba(255,255,255,.4);letter-spacing:.5px;text-transform:uppercase;margin-top:1px;}
  .cbm-res mark{background:rgba(0,200,240,.28);color:#7fe8ff;border-radius:3px;padding:0 1px;}
  .cbm-empty{text-align:center;color:rgba(255,255,255,.4);font-size:14px;padding:40px 20px;}

  /* Akordeon menü */
  .cbm-group{border-bottom:.5px solid rgba(255,255,255,.07);}
  .cbm-ghead{display:flex;align-items:center;justify-content:space-between;width:100%;background:none;border:none;color:#fff;
    font-family:inherit;font-size:16px;font-weight:700;padding:17px 12px;cursor:pointer;text-align:left;min-height:56px;}
  .cbm-ghead i{font-size:20px;color:rgba(255,255,255,.5);transition:transform .25s;}
  .cbm-group.open .cbm-ghead i{transform:rotate(180deg);color:#00c8f0;}
  .cbm-sub{max-height:0;overflow:hidden;transition:max-height .3s ease;}
  .cbm-group.open .cbm-sub{max-height:640px;}
  .cbm-sub a{display:flex;align-items:center;gap:10px;padding:13px 12px 13px 20px;color:rgba(255,255,255,.72);text-decoration:none;font-size:15px;min-height:50px;border-radius:10px;}
  .cbm-sub a:active{background:rgba(0,200,240,.1);color:#00c8f0;}
  .cbm-sub a::before{content:"";width:5px;height:5px;border-radius:50%;background:rgba(0,200,240,.5);flex-shrink:0;}

  .cbm-link{display:flex;align-items:center;justify-content:space-between;padding:17px 12px;color:#fff;text-decoration:none;font-size:16px;font-weight:600;border-bottom:.5px solid rgba(255,255,255,.07);min-height:56px;}
  .cbm-link i{color:rgba(255,255,255,.3);font-size:18px;}
  .cbm-link:active{color:#00c8f0;}

  .cbm-cta{display:flex;align-items:center;justify-content:center;gap:8px;margin:22px 4px 8px;background:#00c8f0;color:#060c1a;
    font-weight:800;font-size:16px;padding:16px;border-radius:12px;text-decoration:none;min-height:56px;}
  .cbm-actions{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:12px 4px 0;}
  .cbm-act{display:flex;align-items:center;justify-content:center;gap:8px;padding:14px;border-radius:12px;border:1px solid rgba(255,255,255,.14);
    color:#fff;text-decoration:none;font-size:14px;font-weight:600;min-height:52px;}
  .cbm-act i{color:#00c8f0;font-size:18px;}
  .cbm-act:active{border-color:#00c8f0;}

  /* ===== Site geneli responsive iyileştirme katmanı ===== */
  html,body{overflow-x:hidden;}
  img,svg,iframe,video{max-width:100%;}
  @media(max-width:1024px){
    /* nav'ı hamburger için toparla */
    .nav{padding-left:1.25rem!important;padding-right:1rem!important;gap:10px;}
    /* sabit kolonlu gridler daralt */
    .format-grid{grid-template-columns:repeat(2,1fr)!important;}
  }
  @media(max-width:640px){
    /* taşmaya yol açan geniş inline gridleri tek kolona indir */
    [style*="minmax(320px"],[style*="minmax(300px"],[style*="minmax(280px"]{grid-template-columns:1fr!important;}
    .format-grid,.stats{grid-template-columns:1fr 1fr!important;}
    /* yatay padding'i telefonda dengele */
    .section,.hero,.others,.partners{padding-left:1.25rem!important;padding-right:1.25rem!important;}
    /* ana başlığı taşırmadan sığdır */
    .hero h1{font-size:clamp(1.9rem,7vw,2.6rem)!important;word-break:normal;}
    /* uzun URL/kod bloklarının satır kaydırması */
    p,li,td,span,a{overflow-wrap:break-word;}
  }
  @media(max-width:440px){
    .stats,.format-grid{grid-template-columns:1fr!important;}
    .nav{padding-left:1rem!important;padding-right:.75rem!important;}
  }

  /* ===== Masaüstü arama (⌘K komut paleti) ===== */
  .cbk-trigger{display:none;align-items:center;gap:6px;height:34px;padding:0 10px;border-radius:9px;border:.5px solid rgba(255,255,255,.14);
    background:rgba(255,255,255,.05);color:rgba(255,255,255,.55);font-family:inherit;font-size:13px;cursor:pointer;transition:border-color .2s,color .2s;}
  .cbk-trigger:hover{border-color:rgba(0,200,240,.4);color:#fff;}
  .cbk-trigger i{font-size:16px;color:#00c8f0;}
  .cbk-trigger .kbd{margin-left:2px;font-size:13px;color:rgba(255,255,255,.55);letter-spacing:.2px;}
  @media(min-width:1025px){ .cbk-trigger{display:inline-flex;} }

  .cbk-overlay{position:fixed;inset:0;z-index:2500;background:rgba(4,8,18,.6);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);
    display:flex;align-items:flex-start;justify-content:center;padding-top:12vh;opacity:0;visibility:hidden;transition:opacity .18s;}
  .cbk-overlay.on{opacity:1;visibility:visible;}
  .cbk-modal{width:min(600px,92vw);background:#0a1225;border:1px solid rgba(255,255,255,.1);border-radius:16px;overflow:hidden;
    box-shadow:0 24px 70px rgba(0,0,0,.6);transform:translateY(-10px) scale(.98);transition:transform .2s;}
  .cbk-overlay.on .cbk-modal{transform:translateY(0) scale(1);}
  .cbk-head{display:flex;align-items:center;gap:12px;padding:0 18px;height:60px;border-bottom:.5px solid rgba(255,255,255,.08);}
  .cbk-head i{font-size:20px;color:#00c8f0;}
  .cbk-head input{flex:1;background:none;border:none;outline:none;color:#fff;font-size:17px;font-family:inherit;}
  .cbk-head input::placeholder{color:rgba(255,255,255,.38);}
  .cbk-head .kbd{font-size:11px;padding:3px 7px;border-radius:5px;background:rgba(255,255,255,.06);border:.5px solid rgba(255,255,255,.12);color:rgba(255,255,255,.4);}
  .cbk-list{max-height:56vh;overflow-y:auto;padding:8px;}
  .cbk-item{display:flex;align-items:center;gap:14px;padding:12px 14px;border-radius:10px;text-decoration:none;color:#fff;cursor:pointer;}
  .cbk-item i{font-size:19px;color:#00c8f0;width:22px;text-align:center;flex-shrink:0;}
  .cbk-item .t{font-size:15px;font-weight:600;}
  .cbk-item .k{font-size:11px;color:rgba(255,255,255,.4);text-transform:uppercase;letter-spacing:.5px;margin-top:1px;}
  .cbk-item .go{margin-left:auto;font-size:12px;color:rgba(255,255,255,.25);opacity:0;}
  .cbk-item.active{background:rgba(0,200,240,.12);}
  .cbk-item.active .go{opacity:1;color:#00c8f0;}
  .cbk-item mark{background:rgba(0,200,240,.28);color:#7fe8ff;border-radius:3px;padding:0 1px;}
  .cbk-empty{text-align:center;color:rgba(255,255,255,.4);font-size:14px;padding:36px 20px;}
  .cbk-foot{display:flex;align-items:center;gap:16px;padding:10px 18px;border-top:.5px solid rgba(255,255,255,.08);font-size:11.5px;color:rgba(255,255,255,.35);}
  .cbk-foot b{font-weight:600;color:rgba(255,255,255,.5);}
  `;

  function inject() {
    if (document.getElementById("cbm-style")) return;
    var st = document.createElement("style");
    st.id = "cbm-style";
    st.textContent = css;
    document.head.appendChild(st);
  }

  function buildPanel() {
    var groupsHtml = GROUPS.map(function (g) {
      if (g.flat) {
        return '<a class="cbm-link" href="' + withBase(g.href) + '">' + g.label + '<i class="ti ti-chevron-right"></i></a>';
      }
      var subs = g.items.map(function (it) {
        return '<a href="' + withBase(it[1]) + '">' + it[0] + "</a>";
      }).join("");
      return '<div class="cbm-group"><button class="cbm-ghead" type="button">' + g.label +
        '<i class="ti ti-chevron-down"></i></button><div class="cbm-sub">' + subs + "</div></div>";
    }).join("");

    var links = TOP_LINKS.map(function (l) {
      return '<a class="cbm-link" href="' + withBase(l[1]) + '">' + l[0] + '<i class="ti ti-chevron-right"></i></a>';
    }).join("");

    var panel = document.createElement("div");
    panel.className = "cbm-panel";
    panel.setAttribute("role", "dialog");
    panel.setAttribute("aria-label", "Menü");
    panel.innerHTML =
      '<div class="cbm-top" style="display:flex;align-items:center;gap:10px;">' +
        '<div class="cbm-search" style="flex:1;min-width:0;">' +
          '<i class="ti ti-search"></i>' +
          '<input type="search" inputmode="search" autocomplete="off" placeholder="Ara: ürün, çözüm, sektör…" aria-label="Site içi arama">' +
          '<button class="cbm-clear" type="button" aria-label="Temizle"><i class="ti ti-x"></i></button>' +
        "</div>" +
        '<button class="cbm-close" type="button" aria-label="Kapat" style="flex-shrink:0;width:42px;height:42px;border:none;background:rgba(255,255,255,.07);border-radius:11px;color:#fff;display:flex;align-items:center;justify-content:center;cursor:pointer;-webkit-tap-highlight-color:transparent;"><i class="ti ti-x" style="font-size:22px;"></i></button>' +
      "</div>" +
      '<div class="cbm-body">' +
        '<div class="cbm-results" role="listbox"></div>' +
        '<div class="cbm-menu">' +
          groupsHtml + links +
          '<a class="cbm-cta" href="' + withBase("/teklif-iste#form") + '"><i class="ti ti-send"></i>Teklif Al</a>' +
          '<div class="cbm-actions">' +
            '<a class="cbm-act" href="tel:+902324643490"><i class="ti ti-phone"></i>Ara</a>' +
            '<a class="cbm-act" href="mailto:cadbim@cadbim.com.tr"><i class="ti ti-mail"></i>E-posta</a>' +
          "</div>" +
        "</div>" +
      "</div>";
    return panel;
  }

  function highlight(text, q) {
    if (!q) return text;
    var nt = norm(text), nq = norm(q), i = nt.indexOf(nq);
    if (i < 0) return text;
    return text.slice(0, i) + "<mark>" + text.slice(i, i + q.length) + "</mark>" + text.slice(i + q.length);
  }

  function init() {
    var nav = document.querySelector("nav.nav") || document.querySelector("nav");
    if (!nav) return;
    inject();

    /* Hamburger butonu */
    var btn = document.createElement("button");
    btn.className = "cbm-btn";
    btn.type = "button";
    btn.setAttribute("aria-label", "Menü");
    btn.innerHTML = "<span></span><span></span><span></span>";
    nav.appendChild(btn);

    var panel = buildPanel();
    document.body.appendChild(panel);

    var input = panel.querySelector(".cbm-search input");
    var clearBtn = panel.querySelector(".cbm-clear");
    var results = panel.querySelector(".cbm-results");
    var menu = panel.querySelector(".cbm-menu");
    var scrollY = 0;

    function open() {
      scrollY = window.scrollY;
      document.body.classList.add("cbm-open");
      document.body.style.position = "fixed";
      document.body.style.top = -scrollY + "px";
      document.body.style.width = "100%";
      btn.setAttribute("aria-expanded", "true");
    }
    function close() {
      document.body.classList.remove("cbm-open");
      document.body.style.position = "";
      document.body.style.top = "";
      document.body.style.width = "";
      window.scrollTo(0, scrollY);
      btn.setAttribute("aria-expanded", "false");
    }
    btn.addEventListener("click", function () {
      document.body.classList.contains("cbm-open") ? close() : open();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && document.body.classList.contains("cbm-open")) close();
    });
    var closeBtn = panel.querySelector(".cbm-close");
    if (closeBtn) closeBtn.addEventListener("click", close);

    /* Akordeon */
    panel.querySelectorAll(".cbm-ghead").forEach(function (h) {
      h.addEventListener("click", function () {
        h.parentNode.classList.toggle("open");
      });
    });

    /* Arama */
    function render(q) {
      var nq = norm(q);
      if (!nq) {
        results.classList.remove("on");
        menu.classList.remove("off");
        clearBtn.style.display = "none";
        results.innerHTML = "";
        return;
      }
      clearBtn.style.display = "block";
      var hits = INDEX.filter(function (r) {
        return norm(r[0]).indexOf(nq) >= 0 || norm(r[2]).indexOf(nq) >= 0 || norm(r[3]).indexOf(nq) >= 0;
      }).sort(function (a, b) {
        var as = norm(a[0]).indexOf(nq), bs = norm(b[0]).indexOf(nq);
        as = as < 0 ? 99 : as; bs = bs < 0 ? 99 : bs;
        return as - bs;
      });
      menu.classList.add("off");
      results.classList.add("on");
      if (!hits.length) {
        results.innerHTML = '<div class="cbm-empty">"' + q + '" için sonuç yok.<br>Farklı bir terim deneyin.</div>';
        return;
      }
      results.innerHTML = hits.slice(0, 12).map(function (r) {
        var ic = ICON[r[3]] || "ti-file";
        return '<a class="cbm-res" href="' + withBase(r[1]) + '"><i class="ti ' + ic + '"></i>' +
          '<div><div class="t">' + highlight(r[0], q) + '</div><div class="k">' + r[3] + "</div></div></a>";
      }).join("");
    }
    input.addEventListener("input", function () { render(input.value); });
    clearBtn.addEventListener("click", function () {
      input.value = ""; render(""); input.focus();
    });

    buildDesktopSearch(nav);
  }

  /* ===== Masaüstü ⌘K komut paleti ===== */
  function buildDesktopSearch(nav) {
    var isMac = /Mac|iPhone|iPad/.test(navigator.platform || navigator.userAgent);
    var trigger = document.createElement("button");
    trigger.className = "cbk-trigger";
    trigger.type = "button";
    trigger.setAttribute("aria-label", "Site içi arama");
    trigger.innerHTML = '<i class="ti ti-search"></i><span class="kbd">Ara</span>';
    trigger.title = "Ara";
    var navLinks = nav.querySelector(".nav-links");
    if (navLinks) {
      var li = document.createElement("li");
      li.style.listStyle = "none";
      li.appendChild(trigger);
      var ctaEl = navLinks.querySelector(".nav-cta");
      var ctaLi = ctaEl ? ctaEl.closest("li") : null;
      if (ctaLi) navLinks.insertBefore(li, ctaLi);
      else navLinks.appendChild(li);
    } else {
      nav.appendChild(trigger);
    }

    var ov = document.createElement("div");
    ov.className = "cbk-overlay";
    ov.innerHTML =
      '<div class="cbk-modal" role="dialog" aria-label="Arama">' +
        '<div class="cbk-head"><i class="ti ti-search"></i>' +
          '<input type="search" autocomplete="off" placeholder="Ürün, çözüm, sektör veya sayfa ara…">' +
          '<span class="kbd">ESC</span></div>' +
        '<div class="cbk-list"></div>' +
        '<div class="cbk-foot"><span><b>↑↓</b> gezin</span><span><b>↵</b> aç</span><span><b>esc</b> kapat</span></div>' +
      "</div>";
    document.body.appendChild(ov);

    var inp = ov.querySelector("input");
    var list = ov.querySelector(".cbk-list");
    var active = 0, current = [];

    function draw(q) {
      var nq = norm(q);
      current = !nq ? INDEX.slice() : INDEX.filter(function (r) {
        return norm(r[0]).indexOf(nq) >= 0 || norm(r[2]).indexOf(nq) >= 0 || norm(r[3]).indexOf(nq) >= 0;
      }).sort(function (a, b) {
        var as = norm(a[0]).indexOf(nq), bs = norm(b[0]).indexOf(nq);
        as = as < 0 ? 99 : as; bs = bs < 0 ? 99 : bs; return as - bs;
      });
      active = 0;
      if (!current.length) { list.innerHTML = '<div class="cbk-empty">"' + q + '" için sonuç yok.</div>'; return; }
      list.innerHTML = current.slice(0, 14).map(function (r, i) {
        var ic = ICON[r[3]] || "ti-file";
        return '<a class="cbk-item' + (i === 0 ? " active" : "") + '" href="' + withBase(r[1]) + '" data-i="' + i + '">' +
          '<i class="ti ' + ic + '"></i><div><div class="t">' + highlight(r[0], q) + '</div>' +
          '<div class="k">' + r[3] + '</div></div><span class="go">Enter ↵</span></a>';
      }).join("");
      [].forEach.call(list.querySelectorAll(".cbk-item"), function (el) {
        el.addEventListener("mousemove", function () { setActive(+el.dataset.i); });
      });
    }
    function setActive(i) {
      var items = list.querySelectorAll(".cbk-item");
      if (!items.length) return;
      active = (i + items.length) % items.length;
      [].forEach.call(items, function (el, j) { el.classList.toggle("active", j === active); });
      items[active].scrollIntoViewIfNeeded ? items[active].scrollIntoViewIfNeeded() : null;
    }
    function openK() {
      ov.classList.add("on"); inp.value = ""; draw("");
      setTimeout(function () { inp.focus(); }, 40);
    }
    function closeK() { ov.classList.remove("on"); }

    trigger.addEventListener("click", openK);
    inp.addEventListener("input", function () { draw(inp.value); });
    ov.addEventListener("click", function (e) { if (e.target === ov) closeK(); });
    inp.addEventListener("keydown", function (e) {
      if (e.key === "ArrowDown") { e.preventDefault(); setActive(active + 1); }
      else if (e.key === "ArrowUp") { e.preventDefault(); setActive(active - 1); }
      else if (e.key === "Enter") {
        var items = list.querySelectorAll(".cbk-item");
        if (items[active]) window.location.href = items[active].getAttribute("href");
      } else if (e.key === "Escape") { closeK(); }
    });
    document.addEventListener("keydown", function (e) {
      if ((e.metaKey || e.ctrlKey) && (e.key === "k" || e.key === "K")) {
        e.preventDefault();
        ov.classList.contains("on") ? closeK() : openK();
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();


/* ==== scroll-reveal motoru (iç sayfalar; index kendi .reveal'ını kullanır) ==== */
(function(){
  if(window.matchMedia("(prefers-reduced-motion: reduce)").matches)return;
  var els=[].slice.call(document.querySelectorAll(
    "section .sh, section .card, .pgrid .pcard, section .feat, .xp, .cross, .cta-strip, .office-card"
  )).filter(function(e){return !e.closest(".reveal,.reveal-stagger")&&!e.hasAttribute("data-rv");});
  if(!els.length)return;
  var sayac=new Map();
  els.forEach(function(e){
    var p=e.parentElement,i=sayac.get(p)||0;sayac.set(p,i+1);
    e.setAttribute("data-rv","");
    e.style.setProperty("--rvd",Math.min(i*60,360)+"ms");
  });
  var bekleyen=els.slice(),son=0,zam=null;
  function tara(){
    var vh=window.innerHeight;
    for(var i=bekleyen.length-1;i>=0;i--){
      var r=bekleyen[i].getBoundingClientRect();
      if(r.top<vh*0.92&&r.bottom>0){bekleyen[i].classList.add("rv-in");bekleyen.splice(i,1);}
    }
    if(!bekleyen.length){
      window.removeEventListener("scroll",planla);
      window.removeEventListener("resize",planla);
    }
  }
  function planla(){
    var s=Date.now();
    if(s-son>80){son=s;tara();}
    else{clearTimeout(zam);zam=setTimeout(tara,90);}
  }
  window.addEventListener("scroll",planla,{passive:true});
  window.addEventListener("resize",planla,{passive:true});
  /* Ürün filtreleri (pfilter/psearch) display:none'ı JS ile değiştiriyor —
     bu scroll/resize tetiklemediği için filtre sonucu görünür hale gelen
     kartlar tara()'ya hiç uğramadan opacity:0'da kalabiliyordu. */
  if("MutationObserver" in window){
    var mo=new MutationObserver(function(){planla();});
    els.forEach(function(e){mo.observe(e,{attributes:true,attributeFilter:["style","class"]});});
  }
  window.__rv={tara:tara,bekleyen:bekleyen};
  tara();
})();

/* ==== grid satır dengeleme (.cpills, .grid.g2/g3/g4, "İyi Uygulamalar" tipi
   inline grid'ler) ====
   auto-fill/auto-fit yalnızca container genişliğine göre kaç sütun sığdığını
   belirler; kalan öğeler son satıra düzensiz dağılabiliyordu (ör. 8 öğe ->
   5+3, 6 öğe -> 4+2). Her grid'in doğal (CSS'ten gelen) sütun sayısını
   ölçüp satır sayısına bölerek sütunları yeniden hesaplıyoruz (tek sayıda
   öğe varsa ilk satır bir fazla alır). Doğal grid-template-columns değeri
   (class'tan mı geliyor, inline style'tan mı) ilk ölçümde WeakMap'e
   önbelleğe alınır; resize'da tekrar o değere dönülüp yeniden ölçülür. */
(function(){
  var dogal=new WeakMap();
  function grupla(){
    var gridler=[].slice.call(document.querySelectorAll(".cpills, .grid.g2, .grid.g3, .grid.g4, .hero-features"));
    [].slice.call(document.querySelectorAll('[style*="minmax(280px,1fr)"]')).forEach(function(e){
      if(gridler.indexOf(e)===-1)gridler.push(e);
    });
    return gridler;
  }
  function dengele(){
    grupla().forEach(function(grid){
      var items=[].slice.call(grid.children).filter(function(c){return c.nodeType===1;});
      var n=items.length;
      if(n<2)return;
      if(!dogal.has(grid))dogal.set(grid,grid.style.gridTemplateColumns);
      grid.style.gridTemplateColumns=dogal.get(grid);
      var maxCols=getComputedStyle(grid).gridTemplateColumns.split(" ").length;
      if(!maxCols||maxCols<1)maxCols=1;
      var rows=Math.ceil(n/maxCols);
      var cols=Math.ceil(n/rows);
      grid.style.gridTemplateColumns="repeat("+cols+",1fr)";
    });
  }
  if(document.readyState==="loading"){document.addEventListener("DOMContentLoaded",dengele);}
  else{dengele();}
  window.addEventListener("load",dengele);
  var zt=null;
  window.addEventListener("resize",function(){clearTimeout(zt);zt=setTimeout(dengele,120);},{passive:true});
})();
