/* ============================================================
   Cadbim — Mobil Navigasyon + Site İçi Arama
   Tek kaynak. Her sayfaya <script src="mobilenav.js" defer> ile eklenir.
   Kendi stilini enjekte eder; sayfa CSS değişkenlerine bağlı değildir.
   ============================================================ */
(function () {
  "use strict";

  /* ---- IA: menü grupları ---- */
  var GROUPS = [
    {
      label: "Ürünler", href: "cadbim_urunler.html",
      items: [
        ["Autodesk", "cadbim_autodesk.html"],
        ["Adobe", "cadbim_adobe.html"],
        ["HP DesignJet", "cadbim_designjet.html"],
        ["HP Workstations", "cadbim_hp_z_workstation.html"],
        ["HP Build Workspace", "cadbim_hp_build_workspace.html"],
        ["Chaos", "cadbim_chaos.html"],
        ["UltiMaker", "cadbim_ultimaker.html"],
        ["SketchUp", "cadbim_sketchup.html"],
        ["Lumion", "cadbim_lumion.html"],
        ["Microsoft", "cadbim_microsoft.html"]
      ]
    },
    {
      label: "Çözümler", href: "cadbim_cozumler.html",
      items: [
        ["BIM", "cadbim_bim.html"],
        ["PLM", "cadbim_plm.html"],
        ["PDM", "cadbim_pdm.html"],
        ["Simülasyon & Analiz", "cadbim_simulasyon.html"],
        ["CAM & İmalat", "cadbim_cam.html"],
        ["Tolerans Analizi", "cadbim_tolerans_analizi.html"],
        ["Nesting", "cadbim_nesting.html"],
        ["Fabrika Tasarımı", "cadbim_fabrika_tasarimi.html"],
        ["Tasarım Otomasyonu", "cadbim_tasarim_otomasyonu.html"],
        ["Görselleştirme & Render", "cadbim_gorsellestirme.html"],
        ["Eklemeli İmalat & 3D Baskı", "cadbim_eklemeli_imalat.html"],
        ["İnşaat Proje Yönetimi", "cadbim_insaat_yonetimi.html"],
        ["Yaratıcı İçerik & Tasarım", "cadbim_yaratici_icerik.html"],
        ["Gerçeklik Yakalama", "cadbim_gerceklik_yakalama.html"]
      ]
    },
    {
      label: "Endüstriler", href: "sektor_mimari.html",
      items: [
        ["Mimarlık", "sektor_mimari.html"],
        ["İnşaat & Altyapı", "sektor_insaat.html"],
        ["Makine & Üretim", "sektor_makine.html"],
        ["Otomotiv", "sektor_otomotiv.html"],
        ["Medya & Eğlence", "sektor_medya.html"],
        ["Eğitim", "sektor_egitim.html"],
        ["Havacılık & Savunma", "sektor_havacilik.html"]
      ]
    }
  ];

  /* Grup dışı ana linkler */
  var TOP_LINKS = [
    ["Eğitimler", "cadbim_egitimler.html"],
    ["Hakkımızda", "cadbim_hakkimizda.html"],
    ["İletişim", "cadbim_iletisim.html"],
    ["KVKK", "cadbim_kvkk.html"]
  ];

  /* ---- Arama indeksi: tüm sayfalar + anahtar kelimeler ---- */
  var INDEX = [
    ["Ana Sayfa", "index.html", "cadbim autodesk adobe gold partner", "Sayfa"],
    ["Tüm Ürünler", "cadbim_urunler.html", "urunler katalog marka autodesk adobe hp chaos", "Sayfa"],
    ["HP DesignJet Ailesi", "cadbim_designjet.html", "hp designjet plotter tum modeller katalog", "Ürün"],
    ["DesignJet T200 Serisi", "cadbim_designjet_t200.html", "hp t230 t250 24 inc plotter giris", "Ürün"],
    ["DesignJet T600 Serisi", "cadbim_designjet_t600.html", "hp t630 t650 kucuk ofis plotter", "Ürün"],
    ["DesignJet T830 MFP", "cadbim_designjet_t830.html", "hp t830 tarama kopyalama santiye", "Ürün"],
    ["DesignJet T850", "cadbim_designjet_t850.html", "hp t850 36 inc plotter mfp", "Ürün"],
    ["DesignJet T870", "cadbim_designjet_t870.html", "hp t870 24 inc hizli plotter", "Ürün"],
    ["DesignJet T950", "cadbim_designjet_t950.html", "hp t950 36 inc istifleyici plotter", "Ürün"],
    ["DesignJet Smart Tank", "cadbim_designjet_smart_tank.html", "hp t858 t908 murekkep tank dusuk maliyet", "Ürün"],
    ["DesignJet T1600", "cadbim_designjet_t1600.html", "hp t1600 departman cift rulo plotter", "Ürün"],
    ["DesignJet T1700", "cadbim_designjet_t1700.html", "hp t1700 44 inc gis harita plotter", "Ürün"],
    ["DesignJet T2600 MFP", "cadbim_designjet_t2600.html", "hp t2600 tarama kopyalama departman", "Ürün"],
    ["DesignJet XL 3600", "cadbim_designjet_xl3600.html", "hp xl 3600 dayanikli uretim mfp", "Ürün"],
    ["DesignJet XL 3800", "cadbim_designjet_xl3800.html", "hp xl 3800 en hizli 6 a1 dakika", "Ürün"],
    ["DesignJet Z6810", "cadbim_designjet_z6810.html", "hp z6810 42 inc uretim fotograf", "Ürün"],
    ["DesignJet Z6 Pro", "cadbim_designjet_z6pro.html", "hp z6 pro 64 inc grafik uretim", "Ürün"],
    ["DesignJet Z9+ Pro", "cadbim_designjet_z9pro.html", "hp z9 pro 64 inc fine art 12 murekkep", "Ürün"],
    ["DesignJet Z6 PostScript", "cadbim_designjet_z6ps.html", "hp z6 ps grafik harita pixel control", "Ürün"],
    ["DesignJet Z9+ PostScript", "cadbim_designjet_z9ps.html", "hp z9 ps fotograf fine art studyo", "Ürün"],
    ["DesignJet Tarayıcılar", "cadbim_designjet_tarayicilar.html", "hp hd pro 2 sd pro 2 buyuk format tarayici", "Ürün"],
    ["AEC Collection", "cadbim_aec_collection.html", "autodesk koleksiyon revit civil3d paket", "Ürün"],
    ["PD&M Collection", "cadbim_pdm_collection.html", "autodesk koleksiyon inventor vault imalat paket", "Ürün"],
    ["M&E Collection", "cadbim_me_collection.html", "autodesk koleksiyon maya 3dsmax arnold paket", "Ürün"],
    ["Construction Cloud", "cadbim_construction_cloud.html", "autodesk build takeoff docs insaat saha", "Ürün"],
    ["BIM Collaborate Pro", "cadbim_bim_collaborate_pro.html", "autodesk revit bulut worksharing ortak calisma", "Ürün"],
    ["Autodesk Docs", "cadbim_autodesk_docs.html", "autodesk cde dokuman yonetimi iso 19650", "Ürün"],
    ["Vehicle Tracking", "cadbim_vehicle_tracking.html", "autodesk arac donus izi swept path otopark", "Ürün"],
    ["Photoshop", "cadbim_photoshop.html", "adobe goruntu duzenleme retus firefly", "Ürün"],
    ["Illustrator", "cadbim_illustrator.html", "adobe vektor logo grafik", "Ürün"],
    ["InDesign", "cadbim_indesign.html", "adobe sayfa tasarimi dizgi katalog yayin", "Ürün"],
    ["Premiere Pro", "cadbim_premiere_pro.html", "adobe video kurgu montaj", "Ürün"],
    ["After Effects", "cadbim_after_effects.html", "adobe motion graphics vfx efekt", "Ürün"],
    ["Lightroom", "cadbim_lightroom.html", "adobe fotograf raw duzenleme arsiv", "Ürün"],
    ["Substance 3D", "cadbim_substance3d.html", "adobe 3d doku malzeme painter designer", "Ürün"],
    ["Firefly", "cadbim_firefly.html", "adobe uretken yapay zeka ai gorsel", "Ürün"],
    ["Adobe Express", "cadbim_adobe_express.html", "adobe sablon sosyal medya hizli icerik", "Ürün"],
    ["Adobe Stock", "cadbim_adobe_stock.html", "adobe stok gorsel video lisans", "Ürün"],
    ["Chaos Corona", "cadbim_corona.html", "chaos render mimari fotogercekci", "Ürün"],
    ["Chaos Vantage", "cadbim_vantage.html", "chaos gercek zamanli ray tracing", "Ürün"],
    ["Chaos Phoenix", "cadbim_phoenix.html", "chaos ates duman sivi simulasyon vfx", "Ürün"],
    ["Chaos Anima", "cadbim_anima.html", "chaos kalabalik insan animasyon", "Ürün"],
    ["Chaos Cosmos", "cadbim_cosmos.html", "chaos varlik kutuphane model hdri", "Ürün"],
    ["Lumion View", "cadbim_lumion_view.html", "lumion cad icinde render sketchup revit", "Ürün"],
    ["Lumion Studio", "cadbim_lumion_studio.html", "lumion ekip paket floating", "Ürün"],
    ["Lumion Cloud", "cadbim_lumion_cloud.html", "lumion paylasim yorum onay bulut", "Ürün"],
    ["SketchUp Go", "cadbim_sketchup_go.html", "sketchup web ipad mobil modelleme", "Ürün"],
    ["SketchUp Studio", "cadbim_sketchup_studio.html", "sketchup vray scan essentials revit importer", "Ürün"],
    ["Trimble Connect", "cadbim_trimble_connect.html", "trimble bulut model isbirligi ifc", "Ürün"],
    ["UltiMaker Factor 4", "cadbim_factor4.html", "ultimaker endustriyel 3d yazici pps-cf", "Ürün"],
    ["Method XL", "cadbim_method_xl.html", "ultimaker abs muhendislik 3d yazici", "Ürün"],
    ["Sketch Sprint", "cadbim_sketch_sprint.html", "makerbot egitim sinif 3d yazici", "Ürün"],
    ["UltiMaker Cura", "cadbim_cura.html", "ultimaker dilimleme slicer yazilim", "Ürün"],
    ["Digital Factory", "cadbim_digital_factory.html", "ultimaker filo yonetim bulut baski", "Ürün"],
    ["HP DesignJet T Serisi", "cadbim_hp_designjet_t.html", "hp plotter teknik cizim pafta t200 t600 t1600", "Ürün"],
    ["HP DesignJet XL Serisi", "cadbim_hp_designjet_xl.html", "hp plotter mfp xl 3600 3800 tarayici", "Ürün"],
    ["HP DesignJet Z Serisi", "cadbim_hp_designjet_z.html", "hp fotograf fine art baski z6 z9", "Ürün"],
    ["HP Z Workstation", "cadbim_hp_z_workstation.html", "hp is istasyonu z2 z4 z6 z8 fury masaustu", "Ürün"],
    ["HP ZBook", "cadbim_hp_zbook.html", "hp mobil is istasyonu laptop firefly power studio fury", "Ürün"],
    ["Autodesk", "cadbim_autodesk.html", "autocad revit inventor fusion civil3d gold partner", "Ürün"],
    ["Adobe", "cadbim_adobe.html", "creative cloud photoshop illustrator", "Ürün"],
    ["HP", "cadbim_hp.html", "workstation 3d baski z", "Ürün"],
    ["HP Build & Workspace", "cadbim_hp_build_workspace.html", "hp build workspace", "Ürün"],
    ["Chaos", "cadbim_chaos.html", "vray corona render", "Ürün"],
    ["UltiMaker", "cadbim_ultimaker.html", "3d yazici printer", "Ürün"],
    ["SketchUp", "cadbim_sketchup.html", "3d modelleme mimari", "Ürün"],
    ["Lumion", "cadbim_lumion.html", "render gorsellestirme mimari", "Ürün"],
    ["Microsoft", "cadbim_microsoft.html", "surface office 365", "Ürün"],
    ["AutoCAD", "cadbim_autocad.html", "autodesk 2d 3d cizim", "Ürün"],
    ["Revit", "cadbim_revit.html", "bim autodesk mimari", "Ürün"],
    ["Inventor", "cadbim_inventor.html", "autodesk mekanik makine", "Ürün"],
    ["Fusion", "cadbim_fusion.html", "autodesk cad cam", "Ürün"],
    ["Fusion Manage", "cadbim_fusion_manage.html", "plm autodesk", "Ürün"],
    ["Civil 3D", "cadbim_civil3d.html", "altyapi insaat autodesk", "Ürün"],
    ["Alias", "cadbim_alias.html", "otomotiv tasarim yuzey", "Ürün"],
    ["Vault PDM", "cadbim_vault_pdm.html", "veri yonetimi autodesk", "Ürün"],
    ["Çözümler", "cadbim_cozumler.html", "genel bakis", "Çözüm"],
    ["BIM", "cadbim_bim.html", "revit yapi bilgi modelleme", "Çözüm"],
    ["PLM", "cadbim_plm.html", "urun yasam dongusu", "Çözüm"],
    ["PDM", "cadbim_pdm.html", "urun veri yonetimi vault", "Çözüm"],
    ["Simülasyon & Analiz", "cadbim_simulasyon.html", "cfd fea analiz", "Çözüm"],
    ["CAM & İmalat", "cadbim_cam.html", "imalat cnc uretim", "Çözüm"],
    ["Tolerans Analizi", "cadbim_tolerans_analizi.html", "gd&t tolerans", "Çözüm"],
    ["Nesting", "cadbim_nesting.html", "yerlesim kesim optimizasyon", "Çözüm"],
    ["Fabrika Tasarımı", "cadbim_fabrika_tasarimi.html", "factory layout yerlesim", "Çözüm"],
    ["Tasarım Otomasyonu", "cadbim_tasarim_otomasyonu.html", "ilogic otomasyon", "Çözüm"],
    ["Görselleştirme & Render", "cadbim_gorsellestirme.html", "render gorselleştirme vray corona lumion enscape", "Çözüm"],
    ["Eklemeli İmalat & 3D Baskı", "cadbim_eklemeli_imalat.html", "3d baski eklemeli imalat ultimaker", "Çözüm"],
    ["İnşaat Proje Yönetimi", "cadbim_insaat_yonetimi.html", "construction cloud saha cde santiye", "Çözüm"],
    ["Yaratıcı İçerik & Tasarım", "cadbim_yaratici_icerik.html", "adobe grafik video icerik", "Çözüm"],
    ["Gerçeklik Yakalama", "cadbim_gerceklik_yakalama.html", "tarama nokta bulutu recap scan-to-bim rolove", "Çözüm"],
    ["Simülasyon", "cadbim_simulasyon.html", "analiz", "Çözüm"],
    ["Sanatsal Baskı", "cadbim_sanatsal_baski.html", "fine art print baski", "Çözüm"],
    ["Yazılım Geliştirme", "cadbim_yazilim_gelistirme.html", "api ozel yazilim", "Hizmet"],
    ["Danışmanlık", "cadbim_danismanlik.html", "consulting proje", "Hizmet"],
    ["Eğitimler", "cadbim_egitimler.html", "atc sertifika kurs", "Hizmet"],
    ["Sürdürülebilirlik", "cadbim_surdurulebilirlik.html", "cevre yesil", "Kurumsal"],
    ["Mimarlık", "sektor_mimari.html", "sektor mimari", "Sektör"],
    ["İnşaat & Altyapı", "sektor_insaat.html", "sektor insaat altyapi", "Sektör"],
    ["Makine & Üretim", "sektor_makine.html", "sektor makine uretim imalat", "Sektör"],
    ["Otomotiv", "sektor_otomotiv.html", "sektor otomotiv", "Sektör"],
    ["Medya & Eğlence", "sektor_medya.html", "sektor medya eglence render", "Sektör"],
    ["Eğitim", "sektor_egitim.html", "sektor egitim universite okul akademik lab", "Sektör"],
    ["Havacılık & Savunma", "sektor_havacilik.html", "sektor havacilik savunma defense aerospace", "Sektör"],
    ["Hakkımızda", "cadbim_hakkimizda.html", "kurumsal 1993 firma", "Kurumsal"],
    ["İletişim", "cadbim_iletisim.html", "adres telefon teklif form izmir ankara", "Kurumsal"],
    ["KVKK", "cadbim_kvkk.html", "kisisel veri gizlilik", "Yasal"],
    ["KVKK Politikası", "cadbim_kvkk_politikasi.html", "politika", "Yasal"],
    ["Gizlilik Politikası", "cadbim_kvkk_gizlilik_politikasi.html", "privacy", "Yasal"],
    ["Çerez Politikası", "cadbim_kvkk_cerez_politikasi.html", "cookie", "Yasal"],
    ["KVKK Başvuru Formu", "cadbim_kvkk_basvuru_formu.html", "basvuru", "Yasal"],
    ["Autodesk 3ds Max", "cadbim_3dsmax.html", "autodesk 3d modelleme animasyon render mimari vfx", "Ürün"],
    ["Autodesk Maya", "cadbim_maya.html", "autodesk animasyon vfx karakter modelleme", "Ürün"],
    ["Maya Creative", "cadbim_maya_creative.html", "autodesk maya uygun animasyon", "Ürün"],
    ["Autodesk Arnold", "cadbim_arnold.html", "autodesk render motoru vfx isik", "Ürün"],
    ["MotionBuilder", "cadbim_motionbuilder.html", "autodesk motion capture animasyon oyun", "Ürün"],
    ["Mudbox", "cadbim_mudbox.html", "autodesk dijital heykel doku boyama", "Ürün"],
    ["Autodesk Flame", "cadbim_flame.html", "autodesk vfx renk finishing compositing", "Ürün"],
    ["Golaem", "cadbim_golaem.html", "autodesk kalabalik crowd maya simulasyon", "Ürün"],
    ["Autodesk Flow Studio", "cadbim_flow_studio.html", "autodesk wonder studio ai sahne motion capture", "Ürün"],
    ["Flow Production Tracking", "cadbim_flow_production_tracking.html", "autodesk shotgrid produksiyon takip pipeline", "Ürün"],
    ["Navisworks", "cadbim_navisworks.html", "autodesk koordinasyon cakisma clash 4d 5d", "Ürün"],
    ["InfraWorks", "cadbim_infraworks.html", "autodesk altyapi konsept kentsel gis", "Ürün"],
    ["Advance Steel", "cadbim_advance_steel.html", "autodesk celik detaylandirma yapisal", "Ürün"],
    ["Robot Structural Analysis", "cadbim_robot_structural.html", "autodesk yapisal analiz statik betonarme", "Ürün"],
    ["Autodesk Forma", "cadbim_forma.html", "autodesk erken tasarim site analiz spacemaker bulut", "Ürün"],
    ["Autodesk Tandem", "cadbim_tandem.html", "autodesk dijital ikiz operasyon varlik iot digital twin", "Ürün"],
    ["ReCap Pro", "cadbim_recap_pro.html", "autodesk nokta bulutu gerceklik yakalama tarama", "Ürün"],
    ["Autodesk Drive", "cadbim_autodesk_drive.html", "autodesk bulut depolama dosya paylasim", "Ürün"],
    ["Desktop Connector", "cadbim_desktop_connector.html", "autodesk bulut dosya senkron acc", "Ürün"],
    ["Design Review", "cadbim_design_review.html", "autodesk dwf isaretleme redline", "Ürün"],
    ["DWG TrueView", "cadbim_dwg_trueview.html", "autodesk dwg goruntuleyici ucretsiz", "Ürün"],
    ["AutoCAD LT", "cadbim_autocad_lt.html", "autodesk 2d cizim uygun", "Ürün"],
    ["AutoCAD Web", "cadbim_autocad_web.html", "autodesk tarayici bulut cizim", "Ürün"],
    ["Revit LT", "cadbim_revit_lt.html", "autodesk bim uygun mimari", "Ürün"],
    ["Factory Design Utilities", "cadbim_factory_design.html", "autodesk fabrika yerlesim layout", "Ürün"],
    ["FeatureCAM", "cadbim_featurecam.html", "autodesk cam otomasyon cnc", "Ürün"],
    ["PowerMill", "cadbim_powermill.html", "autodesk cam cok eksen cnc frezeleme", "Ürün"],
    ["PowerShape", "cadbim_powershape.html", "autodesk cam modelleme kalip", "Ürün"],
    ["Moldflow", "cadbim_moldflow.html", "autodesk enjeksiyon kalip simulasyon plastik", "Ürün"],
    ["Netfabb", "cadbim_netfabb.html", "autodesk eklemeli imalat 3d baski hazirlik", "Ürün"],
    ["Meshmixer", "cadbim_meshmixer.html", "autodesk mesh 3d baski hazirlik ucretsiz", "Ürün"],
    ["Tinkercad", "cadbim_tinkercad.html", "autodesk egitim 3d tasarim ucretsiz baslangic", "Ürün"],
    ["Dijital İkiz & Varlık Operasyonu", "cadbim_dijital_ikiz.html", "tandem operasyonel dijital ikiz varlik bim iot fm digital twin", "Çözüm"],
    ["KVKK Çalışan Adayı Aydınlatma", "cadbim_kvkk_calisan_adayi_aydinlatma.html", "aydinlatma calisan adayi", "Yasal"],
    ["KVKK İnternet Sitesi Aydınlatma", "cadbim_kvkk_internet_sitesi_aydinlatma.html", "aydinlatma internet sitesi ziyaretci", "Yasal"],
    ["KVKK Müşteri Aydınlatma", "cadbim_kvkk_musteri_aydinlatma.html", "aydinlatma musteri", "Yasal"],
    ["KVKK Potansiyel Müşteri Aydınlatma", "cadbim_kvkk_potansiyel_musteri_aydinlatma.html", "aydinlatma potansiyel musteri", "Yasal"],
    ["KVKK Tedarikçi Aydınlatma", "cadbim_kvkk_tedarikci_aydinlatma.html", "aydinlatma tedarikci", "Yasal"],
    ["KVKK Tedarikçi Çalışanı Aydınlatma", "cadbim_kvkk_tedarikci_calisani_aydinlatma.html", "aydinlatma tedarikci calisani", "Yasal"],
    ["KVKK Privacy Policy", "cadbim_kvkk_privacy_policy.html", "privacy policy english kvkk", "Yasal"]
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
    "Kurumsal": "ti-building", "Hizmet": "ti-tools", "Yasal": "ti-file-shield",
    "Sayfa": "ti-home"
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
      var subs = g.items.map(function (it) {
        return '<a href="' + it[1] + '">' + it[0] + "</a>";
      }).join("");
      return '<div class="cbm-group"><button class="cbm-ghead" type="button">' + g.label +
        '<i class="ti ti-chevron-down"></i></button><div class="cbm-sub">' + subs + "</div></div>";
    }).join("");

    var links = TOP_LINKS.map(function (l) {
      return '<a class="cbm-link" href="' + l[1] + '">' + l[0] + '<i class="ti ti-chevron-right"></i></a>';
    }).join("");

    var panel = document.createElement("div");
    panel.className = "cbm-panel";
    panel.setAttribute("role", "dialog");
    panel.setAttribute("aria-label", "Menü");
    panel.innerHTML =
      '<div class="cbm-top">' +
        '<div class="cbm-search">' +
          '<i class="ti ti-search"></i>' +
          '<input type="search" inputmode="search" autocomplete="off" placeholder="Ara: ürün, çözüm, sektör…" aria-label="Site içi arama">' +
          '<button class="cbm-clear" type="button" aria-label="Temizle"><i class="ti ti-x"></i></button>' +
        "</div>" +
      "</div>" +
      '<div class="cbm-body">' +
        '<div class="cbm-results" role="listbox"></div>' +
        '<div class="cbm-menu">' +
          groupsHtml + links +
          '<a class="cbm-cta" href="cadbim_iletisim.html#form"><i class="ti ti-send"></i>Teklif Al</a>' +
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
        return '<a class="cbm-res" href="' + r[1] + '"><i class="ti ' + ic + '"></i>' +
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
        return '<a class="cbk-item' + (i === 0 ? " active" : "") + '" href="' + r[1] + '" data-i="' + i + '">' +
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
