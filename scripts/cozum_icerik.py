# -*- coding: utf-8 -*-
"""Cozum sayfalarinin icerik kaynagi (tek dogru kaynak).

Metinler; Autodesk, Adobe, Chaos, UltiMaker ve Lumion'un resmi urun/cozum
sayfalarindaki guncel yetenek ve terminolojiden derlenip Cadbim kurumsal
diline yeniden yazilmistir. Fiyat bilgisi bilincli olarak yer almaz
(bkz. "CADBIM fiyat gosterilmez" kurali) — her yerde "Teklif Iste" CTA'si.

Marka sirasi kurali: Autodesk her zaman ilk.
Urun sirasi kurali: Koleksiyonlar (AEC / PD&M / M&E) her zaman ilk.
"""

# --------------------------------------------------------------------------
# marka kunyeleri
# --------------------------------------------------------------------------
BRANDS = {
    "autodesk": ("Autodesk", "autodesk", "assets/logos/autodesk-primary-white.svg",
                 "Gold Partner"),
    "adobe": ("Adobe", "adobe", "assets/logos/adobe-logo.svg",
              "Gold Reseller Partner"),
    "hp": ("HP", "hp", "assets/logos/hp-logo.png", "Yetkili is ortagi"),
    "chaos": ("Chaos", "chaos", "assets/logos/chaos-logo-red.svg",
              "Yetkili is ortagi"),
    "ultimaker": ("UltiMaker", "ultimaker", "assets/logos/ultimaker.svg",
                  "Yetkili is ortagi"),
    "sketchup": ("SketchUp", "sketchup", "assets/logos/sketchup.svg",
                 "Yetkili satici"),
    "lumion": ("Lumion", "lumion", "assets/logos/lumion.png", "Yetkili satici"),
    "trimble": ("Trimble", "trimble-connect", "assets/logos/products/trimble-icon.png",
                "Yetkili satici"),
    "microsoft": ("Microsoft", "microsoft", "assets/logos/microsoft-logo.png",
                  "Yetkili is ortagi"),
}

# --------------------------------------------------------------------------
# cozum icerikleri
# --------------------------------------------------------------------------
COZUM = {}

COZUM["dijital_donusum"] = dict(
    slug="dijital-donusum", visual="dijital-donusum", accent="#00c8f0",
    lead=u"Dijital dönüşüm bir yazılım alımı değil, verinin çizimden üretime ve "
         u"işletmeye kadar hiç kopmadan aktığı bir çalışma düzenidir. Cadbim, 1993'ten "
         u"bu yana Türkiye'deki mühendislik ekipleriyle bu düzeni kurar: mevcut "
         u"olgunluğunuzu ölçer, hedefi tanımlar ve adım adım hayata geçirir.",
    stats=[(u"1993", u"bu yana sektörde"), (u"5", u"olgunluk basamağı"),
           (u"Tek", u"muhatap: satın alma, kurulum, eğitim, destek")],
    intro_title=u"Dijital dönüşüm nedir, nereden başlanır?",
    intro=[
        u"Autodesk'in tanımıyla dijital dönüşümün çekirdeği <strong>veri sürekliliğidir</strong>: "
        u"tasarım aşamasında üretilen bilginin, sonraki her fazda yeniden çizilmeden, "
        u"yeniden girilmeden kullanılabilmesi. Çoğu kurumda kopma noktası yazılımın "
        u"kendisi değil, iki yazılım arasındaki elle yapılan aktarımdır.",
        u"Bu yüzden dönüşümü tek bir sıçrama olarak değil, beş basamaklı bir olgunluk "
        u"eğrisi olarak ele alıyoruz: <strong>çizim → model → veri → otomasyon → dijital ikiz</strong>. "
        u"Her basamak bir öncekinin ürettiği veriyi tüketir; basamak atlandığında "
        u"yatırım geri dönmez, çünkü üst basamağın besleneceği veri yoktur.",
        u"Cadbim'in rolü bu haritayı sizin süreçlerinize göre çıkarmak ve her basamakta "
        u"doğru Autodesk, Adobe, HP, Chaos ve UltiMaker bileşenini konumlandırmaktır. "
        u"Lisans satışı işin başlangıcıdır; kurulum, göç planı, rol bazlı eğitim ve "
        u"yenileme dönemine kadar tüm yaşam döngüsü tek muhatapta kalır.",
    ],
    bullets=[
        (u"Olgunluk analizi", u"Mevcut yazılım, süreç ve yetkinlik envanteriniz çıkarılır; "
                             u"kopma noktaları somut olarak işaretlenir."),
        (u"Öncelikli kazanç", u"En kısa sürede geri dönen adım ilk sıraya alınır; "
                              u"bütçe tek seferde değil, kazanç ürettikçe genişler."),
        (u"Standart ve şablon", u"Şablon, adlandırma, klasör ve yetki yapısı en baştan "
                                u"kurulur; dönüşüm kişiye değil kuruma bağlanır."),
        (u"Ölçülebilir hedef", u"Her fazda takip edilecek gösterge (çevrim süresi, hata "
                               u"oranı, fire, teslim gecikmesi) önceden tanımlanır."),
    ],
    brands=["autodesk", "adobe", "hp", "chaos", "ultimaker", "sketchup", "lumion", "microsoft"],
    faq=[
        (u"Dijital dönüşüme hangi yazılımla başlamalıyım?",
         u"Yazılımla değil, ölçümle başlanır. Hangi verinin nerede elle yeniden "
         u"üretildiğini tespit etmeden alınan lisans, çoğunlukla eski süreci daha "
         u"pahalı biçimde tekrarlar. Cadbim ücretsiz olgunluk analiziyle bu haritayı çıkarır."),
        (u"Mevcut çizim arşivimiz ne olacak?",
         u"Arşiv atılmaz. DWG tabanlı geçmiş veri, yeni model ortamına referans olarak "
         u"bağlanır; hangi projelerin modele taşınacağı, hangilerinin arşivde kalacağı "
         u"göç planında karara bağlanır."),
        (u"Dönüşüm ne kadar sürer?",
         u"Tek bir cevabı yoktur; ekip büyüklüğüne ve hedef basamağa bağlıdır. Buna "
         u"karşılık her faz, sonuç üreten bağımsız bir paket olarak planlanır — "
         u"aylarca sürecek bir projenin sonunu beklemeden kazanç görülür."),
        (u"Eğitim dahil mi?",
         u"Cadbim Autodesk Yetkili Eğitim Merkezi'dir (ATC). Rol bazlı eğitim planı "
         u"dönüşüm projesinin ayrılmaz parçasıdır; İzmir merkez ofisimizdeki sınıf "
         u"eğitimleri ve çevrim içi oturumlar birlikte kurgulanır."),
    ],
)

COZUM["bim"] = dict(
    slug="bim", visual="bim", accent="#818cf8",
    lead=u"BIM, bir yapıya ait bilginin tüm yaşam döngüsü boyunca üretilmesi ve "
         u"yönetilmesidir. Mimari, statik ve MEP disiplinlerini tek federe modelde "
         u"birleştirir; çakışmayı şantiyede değil ekranda bulur. Cadbim, Autodesk Gold "
         u"Partner olarak BIM altyapısını standardıyla birlikte kurar.",
    stats=[(u"ISO 19650", u"uyumlu ortak veri ortamı"),
           (u"3", u"disiplin tek federe modelde"),
           (u"ATC", u"Autodesk Yetkili Eğitim Merkezi")],
    intro_title=u"BIM tam olarak neyi değiştirir?",
    intro=[
        u"Autodesk'in tanımıyla BIM; akıllı bir modele dayanan ve bulut platformuyla "
        u"desteklenen, <strong>yapılandırılmış ve çok disiplinli veriyi</strong> planlamadan "
        u"tasarıma, inşaattan işletmeye kadar bütünleştiren bir süreçtir. Yani BIM bir "
        u"dosya biçimi değil, bilginin yönetim biçimidir.",
        u"Pratikte fark şurada görülür: CAD'de bir duvarı taşıdığınızda yalnızca çizgiler "
        u"yer değiştirir. BIM'de duvarı taşıdığınızda plan, kesit, görünüş, metraj ve "
        u"çakışma raporu birlikte güncellenir. Metraj tablosu modelin türevidir; ayrıca "
        u"hazırlanan ve modelle senkron kalmayan bir Excel değildir.",
        u"Ölçülebilir kazanç ise koordinasyondadır. Mimari, statik ve MEP modelleri "
        u"Navisworks'te üst üste bindirilip haftalık çakışma rutinine bağlandığında, "
        u"sahada rölöve ile bulunacak çarpışmalar tasarım masasında kapanır — imalata "
        u"girmemiş bir hatanın maliyeti, imalattan sonra bulunanın çok altındadır.",
    ],
    bullets=[
        (u"Federe model", u"Revit mimari, statik ve MEP modelleri tek koordinat "
                          u"sisteminde birleştirilir; her disiplin kendi dosyasında çalışmayı sürdürür."),
        (u"Çakışma tespiti", u"Navisworks ile kural tabanlı çakışma testleri kurulur; "
                             u"bulgular konu (issue) olarak sorumluya atanır ve kapanışı izlenir."),
        (u"Ortak veri ortamı", u"Autodesk Docs üzerinde ISO 19650'ye uygun klasör, "
                               u"adlandırma ve durum kodu yapısı kurulur; teslimlerde sürüm karmaşası yaşanmaz."),
        (u"Model tabanlı metraj", u"Metraj ve maliyet, modelin içinden alınır; "
                                  u"tasarım değiştiğinde miktarlar da değişir."),
    ],
    brands=["autodesk", "chaos", "trimble", "hp"],
    faq=[
        (u"Revit ile BIM aynı şey mi?",
         u"Hayır. Revit bir yazılımdır; BIM ise bilginin nasıl üretilip yönetileceğini "
         u"tanımlayan süreçtir. Revit satın almak tek başına BIM'e geçmek anlamına "
         u"gelmez — şablon, LOD tanımları, ortak veri ortamı ve koordinasyon rutini kurulmadan "
         u"yalnızca üç boyutlu çizim yapılmış olur."),
        (u"CAD'den BIM'e geçiş ekibimi ne kadar yavaşlatır?",
         u"İlk projede bir yavaşlama beklenmelidir; bunun büyüklüğü hazırlığa bağlıdır. "
         u"Ofis şablonu, aile kütüphanesi ve rol bazlı eğitim önceden kurulduğunda geçiş "
         u"dönemi belirgin biçimde kısalır. Cadbim geçişi pilot proje üzerinden yürütür."),
        (u"BIM yalnızca büyük projeler için mi?",
         u"Hayır. Çakışma ve revizyon maliyeti küçük projelerde de vardır; üstelik küçük "
         u"ekiplerde tek bir hatanın etkisi oransal olarak daha büyüktür. Ölçek, "
         u"seçilecek LOD seviyesini ve araç setini değiştirir, yaklaşımı değil."),
        (u"AEC Collection almak zorunda mıyım?",
         u"Zorunlu değil, ancak BIM iş akışı tek bir üründen ibaret değildir: Revit'in "
         u"yanında AutoCAD, Navisworks, Civil 3D, ReCap Pro ve Forma araçları da devreye "
         u"girer. Bu nedenle koleksiyon çoğu ekipte tek tek lisanslamaya göre daha uygun bir "
         u"başlangıçtır. Karşılaştırmalı teklifi birlikte çıkarabiliriz."),
    ],
)

COZUM["simulasyon"] = dict(
    slug="simulasyon", visual="simulasyon", accent="#f87171",
    lead=u"Simülasyon, üretmeden önce bilmektir. Yapısal, termal ve akış davranışını "
         u"dijital ortamda test ederek fiziksel prototip sayısını düşürür, geç aşamada "
         u"ortaya çıkan tasarım hatalarını tasarım masasında yakalar.",
    stats=[(u"FEA · CFD", u"yapısal, termal ve akış analizi"),
           (u"CAD içinde", u"Inventor ve Fusion'a gömülü çalışır"),
           (u"PD&M", u"Collection kapsamında")],
    intro_title=u"Simülasyon hangi soruyu cevaplar?",
    intro=[
        u"Autodesk'in tanımıyla simülasyon; bir tasarımın gerçek dünyadaki kuvvet ve "
        u"etkilere <strong>üretilmeden önce</strong> nasıl tepki vereceğini gösterir. "
        u"Girdi, parça geometrisi ile ona etki edecek yükler ve sınır koşullarıdır; "
        u"çıktı ise tasarımın hangi noktada, hangi yükte yetersiz kaldığının raporudur.",
        u"Sonlu elemanlar analizi (FEA) parçayı mikro ölçekte ağa böler ve her elemanda "
        u"gerilme, yer değiştirme ve emniyet katsayısını hesaplar. Hesaplamalı akışkanlar "
        u"dinamiği (CFD) ise gaz ve sıvı davranışını çözer: soğutma performansı, basınç "
        u"kaybı, hava direnci. Plastik enjeksiyon için Moldflow, kalıp ve malzeme "
        u"kararlarını dolum öncesinde değerlendirir.",
        u"Kazancın büyüklüğü zamanlamayla ilgilidir. Tasarımın erken evresinde yapılan "
        u"analiz, malzeme kalınlığını gereksiz yere artırmayı önler; geç evrede yapılan "
        u"analiz ise yalnızca hatayı doğrular. Cadbim, analizi ayrı bir uzmanlık adası "
        u"olarak değil, tasarım akışının içinde bir kontrol noktası olarak kurar.",
    ],
    bullets=[
        (u"Yapısal analiz (FEA)", u"Inventor Nastran ile statik, modal, burkulma ve "
                                  u"yorulma çalışmaları; gerilme yığılmalarının erken tespiti."),
        (u"Akış ve termal (CFD)", u"Autodesk CFD ile soğutma, havalandırma, basınç kaybı "
                                  u"ve katı cisim hareketi analizleri."),
        (u"Plastik enjeksiyon", u"Moldflow ile dolum, çarpılma ve soğuma davranışı; "
                                u"kalıp ve yolluk kararlarının doğrulanması."),
        (u"Jeneratif tasarım", u"Fusion içinde yük ve kısıtlar tanımlanır; hafifletilmiş "
                               u"ve üretilebilir alternatifler otomatik türetilir."),
    ],
    brands=["autodesk", "hp"],
    faq=[
        (u"Simülasyon için ayrı bir uzman istihdam etmek gerekir mi?",
         u"Tüm senaryolar için gerekmez. Inventor Nastran ve Fusion Simulation, tasarımcının "
         u"kendi ortamında çalıştırabileceği doğrulama analizleri için tasarlanmıştır. "
         u"Sertifikasyona esas, doğrusal olmayan veya çok fizikli analizlerde uzman "
         u"desteği önerilir; bu noktada Cadbim danışmanlık verir."),
        (u"Analiz sonucuna ne kadar güvenebilirim?",
         u"Sonuç, girdilerin kalitesi kadar iyidir: malzeme kartı, sınır koşulları ve ağ "
         u"yoğunluğu doğru kurulmadıysa çıktı yanıltıcı olur. Bu nedenle ilk kurulumda "
         u"bilinen bir vaka üzerinde doğrulama (korelasyon) çalışması yapılmasını öneriyoruz."),
        (u"Analiz için nasıl bir donanım gerekir?",
         u"Çözüm süresi büyük ölçüde çekirdek sayısı ve bellek kapasitesine bağlıdır. "
         u"CFD ve büyük montaj analizlerinde HP Z serisi iş istasyonları belirgin fark "
         u"yaratır; ihtiyaç profilinize göre donanım yapılandırmasını da biz çıkarıyoruz."),
        (u"Simülasyon fiziksel prototipi tamamen ortadan kaldırır mı?",
         u"Hayır, sayısını azaltır. Amaç, prototibe giden tasarımın çoktan elenmiş "
         u"alternatiflerden değil, en güçlü adaydan seçilmesidir."),
    ],
)

COZUM["tolerans_analizi"] = dict(
    slug="tolerans-analizi", visual="tolerans-analizi", accent="#c084fc",
    lead=u"Her parça toleransı içinde üretilir; ama montajda toleranslar toplanır. "
         u"Tolerans analizi, bu birikimin istatistiksel sonucunu üretim öncesinde "
         u"hesaplar — sahada montaj tutmadığında değil.",
    stats=[(u"GD&T", u"model üzerinden tolerans zinciri"),
           (u"Cpk · DPMO", u"istatistiksel yeterlilik ölçütleri"),
           (u"PD&M", u"Collection kapsamında")],
    intro_title=u"Tolerans yığılması neden sorun olur?",
    intro=[
        u"Autodesk Inventor Tolerance Analysis, 3B model üzerindeki geometrik ölçü ve "
        u"tolerans (GD&T) tanımlarının <strong>yığılma döngüsündeki kümülatif etkisini</strong> "
        u"hesaplar. Tek tek bakıldığında hepsi kabul sınırları içinde olan parçalar, "
        u"zincir hâlinde birleştiğinde montajı tutmayabilir.",
        u"Yazılım hem en kötü durum (worst-case) hem de RSS ve istatistiksel sonuçları "
        u"üretir; Cpk, Sigma, DPMO ve verim yüzdesi gibi ölçütlerle raporlar. Böylece "
        u"karar, sezgiye değil sayıya dayanır: hangi ölçüye dar tolerans gerçekten gerekli, "
        u"hangisi yalnızca alışkanlıktan dar tutuluyor?",
        u"Bunun doğrudan bir maliyet karşılığı vardır. Gereksiz dar tolerans; daha hassas "
        u"tezgâh, daha yavaş işleme, daha sık ölçüm ve daha yüksek ıskarta demektir. "
        u"Analiz, toleransı gerektiği yerde sıkar, gerekmediği yerde gevşetir — "
        u"parça değiştirilebilirliğinden ödün vermeden işleme maliyetini düşürür.",
    ],
    bullets=[
        (u"Yığılma zinciri", u"Montaj içindeki ölçü zinciri model üzerinden kurulur; "
                             u"kritik boşluk ve girişimler tanımlanır."),
        (u"Worst-case ve RSS", u"En kötü durum ile istatistiksel sonuç birlikte "
                               u"değerlendirilir; hangi senaryonun bağlayıcı olduğu görülür."),
        (u"Yeterlilik ölçütleri", u"Cpk, Sigma, DPMO ve verim yüzdesi raporlanır; kalite "
                                  u"hedefi sayısal olarak izlenir."),
        (u"Maliyet iletişimi", u"Analiz çıktısı tasarım ve üretim ekipleri arasında ortak "
                               u"dil olur; tolerans tartışması kişisel görüşten çıkar."),
    ],
    brands=["autodesk"],
    faq=[
        (u"Tolerans analizi için ayrı bir yazılım almam gerekir mi?",
         u"Inventor Tolerance Analysis yalnızca Product Design & Manufacturing Collection "
         u"kapsamında sunulur; tek başına lisanslanmaz. Zaten Inventor kullanan ekipler "
         u"için koleksiyona geçiş genellikle en pratik yoldur."),
        (u"Elle yapılan tolerans hesabından farkı ne?",
         u"Elle hesap tek boyutlu ve tek yönlüdür; geometrik toleransların (konum, "
         u"diklik, profil) etkisini gerçekçi biçimde yansıtmaz. Yazılım zinciri model "
         u"geometrisi üzerinden kurar ve istatistiksel dağılımı hesaba katar."),
        (u"Hangi sektörlerde kritik?",
         u"Seri üretimin ve montaj hattının olduğu her yerde: otomotiv, beyaz eşya, "
         u"makine imalatı, havacılık. Değiştirilebilir parça üreten her tedarikçi için "
         u"doğrudan kalite ve maliyet konusudur."),
        (u"Eğitim veriyor musunuz?",
         u"Evet. GD&T temelleri ve Inventor Tolerance Analysis uygulaması, İzmir merkez "
         u"ofisimizdeki eğitim programımızda yer alır; kuruma özel içerikle de planlanabilir."),
    ],
)

COZUM["tasarim_otomasyonu"] = dict(
    slug="tasarim-otomasyonu", visual="tasarim-otomasyonu", accent="#fbbf24",
    lead=u"Mühendislik zamanının önemli bir bölümü yeni bir şey tasarlamaya değil, "
         u"bilinen bir şeyi yeniden çizmeye gider. Tasarım otomasyonu bu tekrarı kural "
         u"hâline getirir; mühendis yalnızca kararı verir, modeli sistem üretir.",
    stats=[(u"iLogic", u"kod yazmadan kural tabanlı tasarım"),
           (u"Konfigüratör", u"müşteri özelinde otomatik varyant"),
           (u"Çizim + CAM", u"otomasyon imalata kadar uzanır")],
    intro_title=u"Neyi otomatikleştiriyoruz?",
    intro=[
        u"Autodesk'in tanımıyla tasarım otomasyonu, <strong>mühendislik bilgisinin ve "
        u"tasarım niyetinin yakalanıp yeniden kullanılmasıdır</strong>. Sac parçalar, "
        u"kaynaklı çerçeveler ve standart bağlantılar gibi basit ama yorucu modelleme "
        u"işleri, bir kez kurala bağlandığında her seferinde elle yapılmaz.",
        u"Inventor içindeki iLogic teknolojisi bunu karmaşık kodlama gerektirmeden "
        u"sağlar: parametreler tanımlanır, aralarındaki ilişkiler kural olarak yazılır ve "
        u"model bu kurallara göre kendini yeniden kurar. Olgunlaştıkça aynı yapı, satış "
        u"ekibinin kullanabileceği bir ürün konfigüratörüne dönüşür.",
        u"Otomasyonun sınırı model değildir. Kurallar; teknik resim üretimini, parça "
        u"listesini, malzeme kartlarını ve CAM takım yollarını da kapsayacak biçimde "
        u"genişletilebilir. Cadbim bu noktada hem uygulama hem de kurum içi yazılım "
        u"geliştirme tarafında destek verir.",
    ],
    bullets=[
        (u"Kural tabanlı model", u"Parametreler ve iLogic kuralları ile geometri, "
                                 u"özellik ve malzeme otomatik belirlenir."),
        (u"Ürün konfigüratörü", u"Müşteri seçimlerine göre modelin, teknik resmin ve "
                                u"parça listesinin otomatik türetilmesi."),
        (u"Doküman otomasyonu", u"Teknik resim, BOM ve teklif ekleri tek adımda ve "
                                u"standardına uygun üretilir."),
        (u"Kurumsal entegrasyon", u"Vault, ERP ve web arayüzleriyle bağlantı; Cadbim "
                                  u"yazılım geliştirme ekibi tarafından yazılan özel eklentiler."),
    ],
    brands=["autodesk"],
    faq=[
        (u"Otomasyon için yazılım geliştirici olmak gerekir mi?",
         u"Temel iLogic kuralları için gerekmez; parametre ve basit koşul mantığını "
         u"bilen bir mühendis kısa sürede üretken hâle gelir. Konfigüratör, ERP "
         u"entegrasyonu veya web arayüzü gibi ileri senaryolarda Cadbim yazılım "
         u"geliştirme ekibi devreye girer."),
        (u"Hangi ürünler otomasyona uygundur?",
         u"Aynı mantığın farklı ölçülerde tekrar ettiği her ürün: çelik konstrüksiyon, "
         u"konveyör, asansör, kalıp, pano, tank, makine kabini. Tekrar oranı ne kadar "
         u"yüksekse geri dönüş o kadar hızlıdır."),
        (u"Mevcut modellerim kullanılabilir mi?",
         u"Genellikle evet, ancak önce sadeleştirme gerekir. Elle biriktirilmiş "
         u"modellerde çoğu kez gereksiz özellik ve kırılgan bağımlılık bulunur; "
         u"otomasyona hazır bir ana model (master) kurmak daha sağlıklı sonuç verir."),
        (u"Geri dönüşü nasıl ölçeriz?",
         u"Otomasyon öncesi ve sonrası, aynı işin çevrim süresi ölçülerek. Projeye "
         u"başlarken bu ölçümü birlikte tanımlıyoruz ki kazanç tahmin değil, veri olsun."),
    ],
)

COZUM["dijital_ikiz"] = dict(
    slug="dijital-ikiz", visual="dijital-ikiz", accent="#5eead4",
    lead=u"Dijital ikiz, tamamlanan yapının teslimle birlikte rafa kalkmayan hâlidir. "
         u"As-built BIM verisi Autodesk Tandem ile işletme verisine bağlanır; bina, "
         u"tesis ve altyapı model üzerinden işletilir.",
    stats=[(u"Tandem", u"Autodesk dijital ikiz platformu"),
           (u"Revit · IFC", u"mevcut modelden ikiz oluşturma"),
           (u"%25", u"Metro İstanbul'un bildirdiği enerji ve bakım maliyeti düşüşü")],
    intro_title=u"Dijital ikiz, üç boyutlu modelden nasıl ayrılır?",
    intro=[
        u"Autodesk'in tanımıyla dijital ikiz; fiziksel bir nesnenin, sistemin veya "
        u"ortamın <strong>sürekli güncellenen sanal karşılığıdır</strong>. Sensörlerden, "
        u"yapı bilgi modelinden ve nesnelerin interneti cihazlarından gelen veriyle "
        u"birlikte yaşar. Statik bir model geçmişi anlatır; dijital ikiz o anki durumu gösterir.",
        u"Autodesk Tandem, Revit ve IFC modellerini alıp bunları varlık kayıtlarıyla "
        u"zenginleştirir: her ekipmanın markası, garanti süresi, bakım geçmişi ve "
        u"dokümanları model üzerindeki nesneye bağlanır. Böylece devir-teslim bir kutu "
        u"dolusu klasör değil, sorgulanabilir bir veri kümesi hâline gelir.",
        u"Getirisi işletme tarafında ortaya çıkar. Autodesk'in yayımladığı Metro İstanbul "
        u"örneğinde, pilot uygulamanın ardından enerji tüketimi ve bakım maliyetlerinde "
        u"yaklaşık %25 azalma bildirilmiştir. Stanford CIFE'nin tahminlerine göre ise "
        u"dijital ikiz kullanımı, bütçe dışı değişiklik taleplerinde belirgin bir düşüşle "
        u"ilişkilendirilmektedir.",
    ],
    bullets=[
        (u"İkiz kurulumu", u"Revit veya IFC modeli Tandem'e aktarılır; sınıflandırma ve "
                           u"varlık şablonları tanımlanır."),
        (u"Varlık verisi", u"Ekipman kimliği, garanti, bakım planı ve dokümanlar model "
                           u"nesnesine bağlanır; arama modelin üzerinden yapılır."),
        (u"Operasyon içgörüsü", u"Sensör ve otomasyon verisi bağlanarak enerji, konfor ve "
                                u"kullanım göstergeleri izlenir."),
        (u"Devir-teslim kalitesi", u"İşveren, projeyi fiziksel yapıyla birlikte "
                                   u"kullanılabilir bir dijital varlık olarak teslim alır."),
    ],
    brands=["autodesk"],
    faq=[
        (u"Dijital ikiz için binanın Revit modeli şart mı?",
         u"Şart değil ama en kısa yol odur. Modeli olmayan mevcut yapılarda önce "
         u"gerçeklik yakalama (lazer tarama) ile as-built model üretilir; Cadbim bu iki "
         u"adımı tek proje olarak yürütebilir."),
        (u"Sensör altyapım yoksa dijital ikiz kurulur mu?",
         u"Evet. İkizin ilk değeri varlık verisinin düzenlenmesinden gelir; sensör "
         u"bağlantısı sonraki olgunluk adımıdır. Tandem'in ücretsiz sürümüyle test "
         u"senaryosu kurup örnek sensör bağlamak mümkündür."),
        (u"Bunu kim kullanır?",
         u"Öncelikle tesis yönetimi ve bakım ekipleri. Yapıyı teslim eden müteahhit ve "
         u"tasarım ofisi için ise farklılaşan bir teslim kalemi hâline gelir."),
        (u"Veri nerede tutuluyor?",
         u"Tandem, Autodesk bulut altyapısında çalışır. Kurumsal veri yönetimi ve erişim "
         u"yetkileri konusunda KVKK uyumlu bir yapı kurulması için Cadbim danışmanlık verir."),
    ],
)

COZUM["fabrika_tasarimi"] = dict(
    slug="fabrika-tasarimi", visual="fabrika-tasarimi", accent="#38bdf8",
    lead=u"Fabrika yerleşimi bir kez yanlış kurulduğunda her gün maliyet üretir. "
         u"Autodesk Factory Design Utilities, bina ve ekipman verisini tek dijital "
         u"temsilde birleştirerek yerleşimi kurulmadan önce test etmenizi sağlar.",
    stats=[(u"2B + 3B", u"aynı yerleşimin iki gösterimi eşzamanlı"),
           (u"Ekipman kütüphanesi", u"özelleştirilebilir varlık kataloğu"),
           (u"PD&M", u"Collection kapsamında")],
    intro_title=u"Yerleşimi neden sanal ortamda kurmalı?",
    intro=[
        u"Autodesk Factory Design Utilities, bina ve ekipman verisini birleştirerek "
        u"üretim tesisi yerleşimleri oluşturur: yerleşim 2B ve 3B olarak planlanır, "
        u"uygulanmadan önce görselleştirilip doğrulanır, ekipman kurulum ve devreye alma "
        u"takvimi çıkarılır ve <strong>sanal fabrika simüle edilerek</strong> verim ile "
        u"çıktı miktarı iyileştirilir.",
        u"Bu yaklaşımın değeri, kararların geri döndürülemez hâle gelmeden alınmasıdır. "
        u"Malzeme akışı, forklift güzergâhı, bakım erişim mesafesi, vinç açıklığı ve "
        u"altyapı bağlantıları ekranda çakıştığında düzeltmenin maliyeti bir çizim "
        u"revizyonudur; aynı çakışma montaj sırasında bulunduğunda maliyeti duran bir hattır.",
        u"Yerleşim modeli aynı zamanda fabrikanın dijital ikizinin temelidir. Autodesk "
        u"Tandem'e taşındığında, üretim tesisinin işletme dönemindeki varlık ve bakım "
        u"verisi de aynı model üzerinden yönetilebilir hâle gelir.",
    ],
    bullets=[
        (u"Konsept ve detay yerleşim", u"DWG'den 3B model üretimi; merkezî varlık "
                                       u"kütüphanesi ve nesnelere iliştirilmiş meta veri."),
        (u"Malzeme akışı analizi", u"Akış güzergâhları ve taşıma mesafeleri "
                                   u"değerlendirilir; makine kullanımı ve taşıma maliyeti iyileştirilir."),
        (u"Çakışma ve takvim", u"Bina ile ekipman tek temsilde birleştirilir; detay "
                               u"tasarım incelemesinde çakışmalar bulunur, kurulum sıralaması planlanır."),
        (u"Görsel karar desteği", u"Yatırım kararı, plan üzerinden değil üç boyutlu "
                                  u"gerçek ölçekli görsel üzerinden alınır."),
    ],
    brands=["autodesk", "hp"],
    faq=[
        (u"Factory Design Utilities'i tek başına alabilir miyim?",
         u"Hayır; Autodesk bu ürünü yalnızca Product Design & Manufacturing Collection "
         u"kapsamında sunmaktadır. Koleksiyon aynı zamanda Inventor, AutoCAD ve Fusion'ı "
         u"da içerdiği için fabrika projelerinde bütünlüklü bir set sağlar."),
        (u"Mevcut fabrikamın çizimi yok, ne yapmalıyım?",
         u"Lazer tarama ile mevcut durum yakalanır ve nokta bulutu ReCap Pro üzerinden "
         u"tasarım ortamına alınır. Yeni ekipman bu gerçek veriye göre yerleştirildiğinde "
         u"kurulum sürprizleri belirgin biçimde azalır."),
        (u"Ekipman kütüphanesinde bizim makinelerimiz yok.",
         u"Kütüphane özelleştirilebilir. Kendi makine modelleriniz varlık olarak "
         u"tanımlanıp meta verisiyle birlikte kütüphaneye eklenir; sonraki projelerde "
         u"hazır kullanılır."),
        (u"Yerleşim simülasyonu da yapılabiliyor mu?",
         u"Evet. Factory Design Utilities varlıkları Autodesk FlexSim içinde kullanılarak "
         u"senaryo bazlı üretim simülasyonu çalıştırılabilir; farklı yerleşimlerin çıktı "
         u"miktarına etkisi karşılaştırılır."),
    ],
)

COZUM["cam"] = dict(
    slug="cam", visual="cam", accent="#f87171",
    lead=u"CAM, CAD modelini tezgâhın anlayacağı dile çevirir. Autodesk Fusion ile "
         u"tasarım ve imalat aynı ortamda kaldığında, tasarım revizyonu takım yoluna "
         u"otomatik yansır — yeniden programlama gerekmez.",
    stats=[(u"2B → 5 eksen", u"frezeleme, tornalama, torna-freze"),
           (u"Tek ortam", u"CAD ve CAM aynı dosyada"),
           (u"Sanal doğrulama", u"tezgâha göndermeden önce çarpışma kontrolü")],
    intro_title=u"CAD ile CAM arasındaki kopuş nerede maliyet üretir?",
    intro=[
        u"Autodesk'in tanımıyla CAM yazılımı, CAD tasarımlarını CNC tezgâhların "
        u"çalıştırabileceği <strong>makine talimatlarına dönüştürür</strong>; takım yolu "
        u"üretimi, tezgâh kurulumu ve süreç iyileştirmesi bu yazılımın kapsamındadır.",
        u"Ayrık CAD ve CAM kullanan atölyelerde asıl kayıp, revizyon anında ortaya çıkar: "
        u"model değiştiğinde dosya yeniden dışa aktarılır, CAM'e yeniden alınır ve takım "
        u"yolları yeniden kurulur. Fusion'da tasarım ile imalat aynı veri üzerinde "
        u"durduğu için revizyon takım yollarına yansır ve yalnızca etkilenen işlemler "
        u"yeniden hesaplanır.",
        u"İkinci kazanç doğrulamadadır. Takım yolu, malzeme ve tezgâh kinematiği ekranda "
        u"simüle edilerek çarpışma ve aşırı kesme riskleri talaş kaldırılmadan görülür. "
        u"Tezgâhta yapılan bir deneme kesiminin maliyeti yalnızca malzeme değil, "
        u"duran tezgâh zamanıdır.",
    ],
    bullets=[
        (u"Takım yolu stratejileri", u"2B, 2,5B, 3, 4 ve 5 eksen frezeleme; adaptif "
                                     u"kaba talaş ve yüksek hızlı işleme stratejileri."),
        (u"Tornalama ve torna-freze", u"Çok görevli tezgâhlar için birleşik torna ve "
                                      u"freze işlemleri, uygun NC kodu üretimi."),
        (u"Post işlemci", u"Tezgâhınıza özel post işlemci yapılandırması; kodun "
                          u"tezgâhın özel yapılandırmalarından yararlanması."),
        (u"Ölçüm ve prob", u"Tezgâh içi prob ile kurulum otomasyonu ve süreç içi kontrol; "
                           u"hurda oranının düşürülmesi."),
    ],
    brands=["autodesk", "hp"],
    faq=[
        (u"Mevcut tezgâhıma uygun post işlemci var mı?",
         u"Fusion geniş bir post işlemci kütüphanesiyle gelir; kütüphanede bulunmayan "
         u"veya özel yapılandırılmış tezgâhlar için post işlemci düzenlemesi yapılır. "
         u"Tezgâh markası ve kontrol ünitesi bilgisini paylaşmanız yeterlidir."),
        (u"SolidWorks veya Catia modelleriyle çalışabilir miyim?",
         u"Evet. Fusion yaygın CAD biçimlerini içe aktarır; Inventor tarafında ise "
         u"HSMWorks ile SolidWorks içinde doğrudan çalışma seçeneği bulunur."),
        (u"Operatör eğitimi veriyor musunuz?",
         u"Evet. Cadbim Autodesk Yetkili Eğitim Merkezi olarak Fusion CAM eğitimlerini "
         u"İzmir merkez ofisinde ve kuruma özel programlarla yürütür; eğitim, kendi "
         u"parçalarınız üzerinden kurgulanabilir."),
        (u"Eklemeli imalat da CAM kapsamında mı?",
         u"Evet. Fusion, talaşlı imalatın yanında eklemeli imalat için de iş hazırlığı "
         u"sunar; parça yönlendirme, destek yapıları ve malzeme bazlı parametreler aynı "
         u"ortamda yönetilir."),
    ],
)

COZUM["eklemeli_imalat"] = dict(
    slug="eklemeli-imalat", visual="eklemeli-imalat", accent="#10b981",
    lead=u"3B baskı, prototipi günlere değil saatlere indirir; aparat ve yedek parçayı "
         u"tedarik zincirinden çıkarıp masanıza taşır. Cadbim; UltiMaker donanımı, "
         u"malzeme danışmanlığı ve baskı yazılımını birlikte kurar.",
    stats=[(u"300+", u"UltiMaker ekosisteminde uyumlu malzeme"),
           (u"400+", u"Cura'da ayarlanabilir dilimleme parametresi"),
           (u"Kurulum + eğitim", u"donanım tek başına teslim edilmez")],
    intro_title=u"Eklemeli imalat kurumda neyi değiştirir?",
    intro=[
        u"Eklemeli imalat, parçayı bir bloktan eksilterek değil, malzemeyi katman katman "
        u"ekleyerek üretir. Bunun ilk sonucu <strong>hızlı prototipleme</strong>dir: "
        u"tasarımcı, mühendis ve üretici tasarımı hızla iyileştirebilir; kalıp ve takım "
        u"maliyeti ortadan kalktığı için deneme yapmanın bedeli düşer.",
        u"İkinci sonuç geleneksel yöntemlerle üretilmesi zor ya da imkânsız geometrilerin "
        u"mümkün hâle gelmesidir; iç kanallar, kafes yapılar ve tek parçaya indirgenmiş "
        u"montajlar gibi. Üçüncüsü ise talep anında üretimdir: aparat, mastar ve yedek "
        u"parça stokta tutulmak yerine gerektiğinde basılır.",
        u"UltiMaker tarafında S serisi, 2,85 mm filamentle çalışan açık malzeme "
        u"ekosistemi sunar; Marketplace üzerinden üretici onaylı baskı profilleri "
        u"indirilerek üçüncü taraf malzemeler elle ayar yapmadan kullanılabilir. "
        u"Yeni nesil S serisinde Cheetah hareket planlayıcı, hız ile kalite arasındaki "
        u"ödünleşmeyi belirgin biçimde azaltmaktadır.",
    ],
    bullets=[
        (u"Doğru cihaz seçimi", u"Parça boyutu, malzeme ve tolerans beklentinize göre "
                                u"S serisi, Factor 4 veya Method ailesinden uygun model belirlenir."),
        (u"Malzeme danışmanlığı", u"PLA, PETG, ABS, TPU, naylon ve karbon takviyeli "
                                  u"kompozitler arasında uygulamaya uygun seçim ve profil kurulumu."),
        (u"Yazılım zinciri", u"UltiMaker Cura ile dilimleme, kurumsal dağıtım için Cura "
                             u"Enterprise, filo yönetimi için Digital Factory."),
        (u"Tasarım tarafı", u"Autodesk Fusion ve Netfabb ile baskıya hazırlık, parça "
                            u"yönlendirme, destek ve kafes yapı optimizasyonu."),
    ],
    brands=["autodesk", "ultimaker", "hp"],
    faq=[
        (u"3B yazıcı satın alırken nelere dikkat etmeliyim?",
         u"Baskı hacmi, malzeme uyumluluğu, tekrarlanabilirlik ve yerel servis "
         u"desteğine. Cihazın kendisi kadar arkasındaki malzeme profili ekosistemi ve "
         u"eğitim de sonucu belirler; Cadbim cihazı kurulum ve kullanıcı eğitimiyle birlikte teslim eder."),
        (u"Hangi malzemeyi kullanmalıyım?",
         u"Uygulamaya bağlıdır: kavramsal model için PLA, dayanıklı aparat için PETG veya "
         u"ABS, esnek parça için TPU, yüksek mukavemet gereken fikstürler için karbon "
         u"takviyeli naylon. İhtiyaç profilinizi birlikte çıkarıp öneri sunuyoruz."),
        (u"Cura ücretli mi?",
         u"UltiMaker Cura ücretsiz ve açık kaynaklıdır. Kurumsal ortamlarda merkezî "
         u"dağıtım, uzun destek süresi ve güvenlik taraması gerektiren ekipler için "
         u"Cura Enterprise sürümü tercih edilir."),
        (u"Eğitim ve servis desteğiniz var mı?",
         u"Evet. Kurulum, ilk baskı eğitimi, bakım ve sarf tedariki Cadbim tarafından "
         u"yürütülür; eğitim kurumları için sınıf ortamına uygun yapılandırma da sunulur."),
    ],
)

COZUM["nesting"] = dict(
    slug="nesting", visual="nesting", accent="#34d399",
    lead=u"Sac ve levha kesiminde en büyük gizli maliyet firedir. Gerçek-şekil yuvalama, "
         u"parçaları levha üzerine en verimli düzende yerleştirerek aynı işi daha az "
         u"malzemeyle çıkarır.",
    stats=[(u"Gerçek-şekil", u"dikdörtgen değil, parçanın gerçek konturu"),
           (u"Çoklu senaryo", u"farklı levha ve malzeme seçenekleri karşılaştırılır"),
           (u"DXF · CAM", u"kesim yoluna doğrudan aktarım")],
    intro_title=u"Yuvalama neden gözle yapılmamalı?",
    intro=[
        u"Autodesk Inventor Nesting, düz ham malzemeden elde edilen verimi artırırken "
        u"maliyeti düşürmeye odaklanır: farklı malzeme ve paketleme seçenekleriyle "
        u"<strong>birden çok levha yerleşimi üretilir</strong>, bu çalışmaların verimi ve "
        u"maliyeti karşılaştırılarak en kârlı senaryo seçilir.",
        u"Elle yapılan yerleşimde operatör genellikle parçaları dikdörtgen kabul eder ve "
        u"güvenli bir boşluk bırakır. Gerçek-şekil yuvalama ise parçanın konturunu esas "
        u"alır; iç boşlukları değerlendirir, döndürme ve iç içe geçirme olanaklarını "
        u"arar. Aradaki fark tek levhada küçük görünür, yıllık malzeme bütçesinde büyür.",
        u"Yazılım ayrıca tane yönü kısıtını da yönetir: estetik gereklilikler veya "
        u"çatlak riskini azaltmak için parçaların yalnızca izin verilen yönlerde "
        u"yerleştirilmesi tanımlanabilir. Sonuç yerleşimin 3B modeli oluşturulur ve kesim "
        u"yolları Inventor CAM ile üretilir ya da DXF olarak dışa aktarılır.",
    ],
    bullets=[
        (u"Otomatik gerçek-şekil yuvalama", u"Parça konturuna göre yerleşim; fire alanı "
                                            u"en aza indirilir."),
        (u"Senaryo karşılaştırma", u"Farklı levha ölçüleri ve malzemeler için verim ve "
                                   u"maliyet yan yana değerlendirilir."),
        (u"Tane yönü kontrolü", u"İzin verilen yerleştirme yönleri tanımlanarak görünüm "
                                u"tutarlılığı ve çatlak riski yönetilir."),
        (u"Kesime aktarım", u"Inventor CAM ile kesim yolu üretimi veya DXF çıktısı ile "
                            u"mevcut kesim yazılımınıza aktarım."),
    ],
    brands=["autodesk"],
    faq=[
        (u"Inventor Nesting'i ayrı satın alabilir miyim?",
         u"Hayır; Autodesk bu ürünü yalnızca Product Design & Manufacturing Collection "
         u"kapsamında sunmaktadır."),
        (u"Kesim makinemin yazılımı zaten yuvalama yapıyor.",
         u"Çoğu makine yazılımı yuvalamayı iş emri anında yapar. Inventor Nesting ise "
         u"tasarım aşamasında çalışır; parça daha çizilirken malzeme verimini gözeterek "
         u"tasarım kararı almanızı sağlar ve teklif aşamasında gerçekçi malzeme maliyeti verir."),
        (u"Ne kadar tasarruf sağlar?",
         u"Parça geometrisine ve mevcut yerleşim alışkanlığınıza bağlıdır; genelleme "
         u"yapmak doğru olmaz. Kendi parçalarınızdan oluşan bir örnek set üzerinde "
         u"karşılaştırmalı bir çalışma yaparak somut rakamı birlikte görebiliriz."),
        (u"Hangi malzemeler için uygundur?",
         u"Düz ham malzemeden kesilen her şey: sac, levha, ahşap panel, cam, kompozit "
         u"ve tekstil. Tane yönü kısıtı özellikle ahşap ve desenli malzemelerde önem kazanır."),
    ],
)

COZUM["plm"] = dict(
    slug="plm", visual="plm", accent="#38bdf8",
    lead=u"PLM, ürün verisini mühendisliğin dışına taşır. Satın alma, kalite, üretim ve "
         u"tedarikçi aynı canlı kayda bakar; değişiklik e-posta zincirinde değil, "
         u"izlenebilir bir iş akışında yürür.",
    stats=[(u"Bulut PLM", u"kurulum yükü olmadan devreye alma"),
           (u"Hazır süreç kütüphanesi", u"yapılandırılmış şablonlarla hızlı başlangıç"),
           (u"Açık API", u"ERP ve CRM entegrasyonu")],
    intro_title=u"PLM ile PDM aynı şey değildir",
    intro=[
        u"PDM mühendislik verisini yönetir: CAD dosyaları, sürümler, revizyonlar. PLM ise "
        u"<strong>ürünün kendisini</strong> yönetir; fikir aşamasından pazardan çekilmeye "
        u"kadar tüm yaşam döngüsünü ve buna dokunan tüm departmanları kapsar. Autodesk "
        u"Fusion Manage, bunu yapılandırılabilir bulut süreçleriyle sağlar.",
        u"Fusion Manage'in kapsamı; ürün ağacı (BOM) yönetimi, değişiklik ve serbest "
        u"bırakma süreçleri, görev yönetimi, tedarikçi iş birliği, kalite yönetimi "
        u"(uygunsuzluk, iade, düzeltici-önleyici faaliyet, FMEA), yeni ürün geliştirme, "
        u"portföy ve gereksinim yönetimi ile gösterge panolarını içerir.",
        u"Uygulamada en görünür kazanç, tek bir doğru BOM'un ortaya çıkmasıdır. "
        u"Mühendislik, üretim ve satın alma listeleri ayrı Excel dosyalarında yaşamayı "
        u"bıraktığında, yanlış parça sipariş etmek ya da eski revizyondan üretmek gibi "
        u"pahalı hatalar yapısal olarak ortadan kalkar.",
    ],
    bullets=[
        (u"BOM yönetimi", u"Çok kullanıcılı, gerçek zamanlı ürün ağacı; satın alma, "
                          u"montaj ve üretim planlama için gereken bilgi tek kayıtta."),
        (u"Değişiklik yönetimi", u"Değişiklik talebi, emri, görevleri ve onayları "
                                 u"otomatik akar; kök neden ve denetim için tam izlenebilirlik kalır."),
        (u"Tedarikçi iş birliği", u"Teklif, tedarik ve geliştirme süreçlerinde dış "
                                  u"paydaşlara güvenli ve yetkilendirilmiş erişim."),
        (u"Kalite yönetimi", u"Uygunsuzluk (NCR), iade (RMA), düzeltici-önleyici faaliyet "
                             u"(CAPA), FMEA ve tedarikçi kalite raporları tek sistemde."),
    ],
    brands=["autodesk"],
    faq=[
        (u"PLM yalnızca büyük şirketler için mi?",
         u"Hayır. Fusion Manage bulut tabanlı olduğu için sunucu kurulumu ve ağır "
         u"yapılandırma gerektirmez; hazır süreç şablonlarıyla ihtiyaç duyulan modülden "
         u"başlanıp zamanla genişletilebilir. Belirleyici olan şirket büyüklüğü değil, "
         u"departmanlar arası veri kopukluğunun maliyetidir."),
        (u"ERP'miz var, PLM'e neden ihtiyacımız olsun?",
         u"ERP ürünü üretmeye ve satmaya odaklanır; ürünün nasıl olgunlaştığını, hangi "
         u"revizyondan geçtiğini ve neden değiştiğini taşımaz. PLM bu boşluğu doldurur ve "
         u"açık API üzerinden ERP ile entegre çalışır — iki sistem rakip değil, tamamlayıcıdır."),
        (u"Vault kullanıyoruz, PLM'e geçmeli miyiz?",
         u"Vault'u bırakmanız gerekmez. Autodesk, Vault Professional (PDM) ile Fusion "
         u"Manage'i (PLM) birlikte sunan Vault PLM paketini sağlar; mühendislik verisi "
         u"Vault'ta kalırken süreçler PLM'e taşınır."),
        (u"Devreye alma ne kadar sürer?",
         u"Kapsama bağlıdır. Hazır süreç şablonlarıyla tek bir modülden (örneğin "
         u"değişiklik yönetimi) başlamak, tüm süreçleri aynı anda devreye almaya göre "
         u"çok daha hızlı sonuç verir. Cadbim fazlı bir devreye alma planı çıkarır."),
    ],
)

COZUM["pdm"] = dict(
    slug="pdm", visual="pdm", accent="#34d399",
    lead=u"\"Son_hali_2_revize_SON.ipt\" bir dosya adı değil, bir risktir. PDM; sürüm, "
         u"revizyon ve yetkiyi tek merkezde toplayarak hangi dosyanın geçerli olduğu "
         u"sorusunu ortadan kaldırır.",
    stats=[(u"Tek kaynak", u"sürüm ve revizyon merkezî yönetilir"),
           (u"Check-in / out", u"eşzamanlı çalışmada üzerine yazma riski yok"),
           (u"Mobil ve tarayıcı", u"ofis dışından güvenli erişim")],
    intro_title=u"Dosya sunucusu neden yetmiyor?",
    intro=[
        u"Autodesk Vault, Autodesk araçlarıyla ve diğer CAD sistemleriyle derin biçimde "
        u"bütünleşen bir <strong>ürün veri yönetimi</strong> yazılımıdır. Paylaşılan bir "
        u"klasörden farkı, dosyaları saklamakla kalmayıp aralarındaki bağımlılıkları da "
        u"bilmesidir: bir parçayı değiştirdiğinizde hangi montajların ve teknik resimlerin "
        u"etkilendiğini gösterir.",
        u"İkinci fark süreçtir. Veri oluşturma, revizyon, inceleme ve serbest bırakma "
        u"adımları tanımlı hâle geldiğinde, onaylanmamış bir revizyondan üretim yapılması "
        u"engellenir. Check-in / check-out mekanizması ise aynı dosya üzerinde çalışan iki "
        u"kişinin birbirinin işini silmesini yapısal olarak imkânsız kılar.",
        u"Vault ayrıca uzaktan çalışma senaryolarını kapsar: mobil uygulama, tarayıcı "
        u"tabanlı ince istemci ve Vault Gateway ile veriye ofis dışından da erişilir. "
        u"Mühendislik verisi büyüdükçe Vault Professional'a, oradan da Vault PLM paketiyle "
        u"süreç yönetimine ölçeklenir.",
    ],
    bullets=[
        (u"Doğrudan CAD entegrasyonu", u"Inventor, AutoCAD ve diğer CAD ortamlarından "
                                       u"çıkmadan veri yönetimi."),
        (u"Sürüm ve revizyon", u"Her kaydın geçmişi tutulur; hangi revizyonun ne zaman ve "
                               u"kim tarafından serbest bırakıldığı izlenebilir."),
        (u"Eşzamanlı tasarım", u"Büyük montajlarda birden çok kullanıcının çakışmadan "
                               u"çalışması; kilit ve yetki yönetimi."),
        (u"Veri yeniden kullanımı", u"Var olan parçanın aranıp bulunması; aynı parçanın "
                                    u"yeniden çizilmesinin ve stok kalabalığının önlenmesi."),
    ],
    brands=["autodesk"],
    faq=[
        (u"Küçük bir ekibiz, PDM'e gerçekten ihtiyacımız var mı?",
         u"Ekip iki kişiye çıktığı anda \"hangi dosya güncel\" sorusu doğar. Vault Basic "
         u"küçük ekipler için giriş seviyesidir; ihtiyaç büyüdükçe Workgroup ve "
         u"Professional sürümlerine geçilir."),
        (u"Mevcut klasör yapımız Vault'a nasıl taşınır?",
         u"Doğrudan kopyalayarak değil, planlı bir göçle. Önce yinelenen ve ölü dosyalar "
         u"ayıklanır, adlandırma ve özellik standardı tanımlanır, ardından toplu aktarım "
         u"yapılır. Cadbim bu göçü proje olarak yürütür."),
        (u"Vault ile Vault PLM arasındaki fark nedir?",
         u"Vault, mühendislik verisini yönetir. Vault PLM ise Vault Professional ile "
         u"Autodesk Fusion Manage bulut PLM'ini tek pakette birleştirir; veri yönetimine "
         u"departmanlar arası süreç yönetimi eklenir."),
        (u"Sunucu gerekiyor mu?",
         u"Vault şirket içi sunucuda çalışır; uzaktan erişim için Vault Gateway ve ince "
         u"istemci seçenekleri vardır. Sunucu boyutlandırmasını kullanıcı sayısı ve veri "
         u"hacmine göre birlikte belirliyoruz."),
    ],
)

COZUM["insaat_yonetimi"] = dict(
    slug="insaat-yonetimi", visual="insaat-yonetimi", accent="#22c55e",
    lead=u"İnşaat projelerinde bilgi kaybı, malzeme kaybından pahalıdır. Autodesk Forma "
         u"ürün ailesi; ortak veri ortamı, metraj, saha yönetimi ve model koordinasyonunu "
         u"tek platformda birleştirir.",
    stats=[(u"ISO 19650", u"standardına uygun ortak veri ortamı"),
           (u"Ofis ↔ saha", u"aynı veri, mobil erişimle"),
           (u"AEC", u"Collection ile bütünleşik")],
    intro_title=u"Ortak veri ortamı neyi çözer?",
    intro=[
        u"Bir inşaat projesinde tasarım ofisi, müteahhit, alt yükleniciler ve işveren "
        u"aynı anda veri üretir. Bu veri farklı e-posta kutularında ve yerel klasörlerde "
        u"dağıldığında, sahada <strong>hangi revizyonun geçerli olduğu</strong> her zaman "
        u"belirsizdir. Yanlış paftadan yapılan bir imalatın bedeli, sökülüp yeniden yapılmasıdır.",
        u"Autodesk Forma Data Management, ISO 19650 standardına göre yapılandırılmış bir "
        u"ortak veri ortamı sunar: klasör hiyerarşisi, adlandırma kuralları, durum kodları "
        u"ve onay akışları en baştan tanımlanır. Model, çizim ve saha raporu aynı "
        u"kaynaktan beslenir; sürüm geçmişi kaybolmaz.",
        u"Bunun üzerine Forma Build ile saha yönetimi (konu takibi, kalite ve iş güvenliği "
        u"kontrol listeleri, teslim listesi), Forma Takeoff ile model tabanlı metraj ve "
        u"Model Management ile disiplinler arası koordinasyon eklenir. Cadbim, bu yapıyı "
        u"projenizin sözleşme gerekliliklerine göre kurar.",
    ],
    bullets=[
        (u"Ortak veri ortamı (CDE)", u"ISO 19650 uyumlu klasör, adlandırma, durum kodu ve "
                                     u"onay akışı; tek doğru kaynak."),
        (u"Saha yönetimi", u"Konu (issue) takibi, kalite ve iş güvenliği kontrol "
                           u"listeleri, fotoğraflı saha raporları, teslim listesi."),
        (u"Model tabanlı metraj", u"Miktarlar modelden alınır; tasarım değiştiğinde "
                                  u"metraj da güncellenir."),
        (u"Koordinasyon", u"Disiplin modelleri birleştirilir, çakışmalar konuya "
                          u"dönüştürülüp sorumluya atanır ve kapanışı izlenir."),
    ],
    brands=["autodesk", "trimble", "chaos", "hp"],
    faq=[
        (u"Alt yüklenicilerimizin Autodesk lisansı yok, sisteme girebilirler mi?",
         u"Ortak veri ortamına davet edilen dış paydaşlar, tanımlanan yetki düzeyinde "
         u"tarayıcı ve mobil uygulama üzerinden erişebilir. Erişim modelini proje "
         u"sözleşmenize göre birlikte kuruyoruz."),
        (u"Sahada internet zayıf, mobil kullanım mümkün mü?",
         u"Saha uygulamaları çevrim dışı çalışmayı destekler; bağlantı sağlandığında veri "
         u"eşitlenir. Şantiye koşullarına uygun cihaz ve kullanım senaryosunu "
         u"planlamaya dahil ediyoruz."),
        (u"Bu ürünler AEC Collection'da var mı?",
         u"AEC Collection; Revit, AutoCAD, Civil 3D, Navisworks, ReCap Pro ve Forma "
         u"araçlarını bir arada sunar. Saha yönetimi ve metraj modülleri projenin "
         u"kapsamına göre ayrıca değerlendirilir; doğru kombinasyonu birlikte belirleriz."),
        (u"Mevcut projemizin ortasında geçiş yapabilir miyiz?",
         u"Yapılabilir, ancak veri göçünün planlanması gerekir. Genellikle yeni fazın "
         u"başlangıcında geçiş yapmak, proje ortasında yapmaktan daha az sürtünme yaratır."),
    ],
)

COZUM["gorsellestirme"] = dict(
    slug="gorsellestirme", visual="gorsellestirme", accent="#f59e0b",
    lead=u"Görselleştirme bir süsleme değil, karar aracıdır. Konsept eskizinden final "
         u"animasyona kadar uzanan hattı; V-Ray, Corona, Lumion, Enscape ve Vantage ile "
         u"projenizin temposuna göre kuruyoruz.",
    stats=[(u"Gerçek zamanlı → final", u"aynı sahne, iki farklı hız"),
           (u"CAD ve BIM uyumlu", u"Revit, 3ds Max, SketchUp, Rhino"),
           (u"HP Z", u"render için doğru donanım yapılandırması")],
    intro_title=u"Hangi render aracı, hangi işe?",
    intro=[
        u"Görselleştirmede tek bir doğru araç yoktur; belirleyici olan projenin hangi "
        u"aşamasında olduğunuzdur. Tasarım devam ederken hızlı geri bildirim gerekir; "
        u"sunum aşamasında ise <strong>fotogerçekçilik ve kontrol</strong> öne çıkar.",
        u"Chaos V-Ray, ödüllü ışın izleme motoruyla yüksek uçlu görselleştirme ve "
        u"prodüksiyon işlerinin karşılığıdır; milyarlarca poligon ve binlerce ışık içeren "
        u"sahneleri kaldırır, CPU ve GPU'yu birlikte kullanır. Chaos Corona mimari "
        u"görselleştirmede sadeliğiyle, Chaos Vantage ise %100 ışın izlemeli gerçek zamanlı "
        u"gezinti ve doğrulama ile devreye girer.",
        u"Lumion tarafında öncelik hızdır: SketchUp, Revit ve Archicad eklentileriyle "
        u"modelleme aracının içinden gerçek zamanlı geri bildirim alınır, geniş varlık "
        u"kütüphanesiyle bağlam hızla kurulur. Cadbim, bu araçları birbirinin alternatifi "
        u"olarak değil, tek bir hattın farklı hızlardaki durakları olarak konumlandırır.",
    ],
    bullets=[
        (u"Tasarım aşaması", u"Enscape ve Lumion View ile modelleme ortamının içinden "
                             u"anlık görsel geri bildirim; tasarım akışı bölünmez."),
        (u"Sunum ve pazarlama", u"V-Ray ve Corona ile fotogerçekçi still görseller, "
                                u"malzeme ve ışık üzerinde tam kontrol."),
        (u"Gerçek zamanlı sunum", u"Chaos Vantage ile ışın izlemeli gezinti; müşteriyle "
                                  u"canlı oturumda değişiklik gösterme."),
        (u"Renk ve son işlem", u"ACEScg gibi açık standartlarla renk yönetimi; Adobe "
                               u"Creative Cloud ile son işlem ve sunum paketleme."),
    ],
    brands=["autodesk", "chaos", "lumion", "adobe", "hp"],
    faq=[
        (u"Lumion mu, V-Ray mi almalıyım?",
         u"Beklentiye bağlı. Hız, kolay öğrenme ve geniş hazır varlık kütüphanesi "
         u"önceliğinizse Lumion; malzeme, ışık ve kompozisyon üzerinde tam kontrol ile "
         u"prodüksiyon kalitesi arıyorsanız V-Ray. Birçok ofis ikisini birlikte kullanır — "
         u"iş akışınıza göre karşılaştırmalı öneri sunabiliriz."),
        (u"Render için nasıl bir bilgisayar gerekir?",
         u"Motoru neyin belirlediğine bağlıdır: CPU tabanlı render çok çekirdekten, GPU "
         u"tabanlı render ise ekran kartı belleğinden fayda sağlar. HP Z serisi iş "
         u"istasyonu ve ZBook yapılandırmalarını kullandığınız motora göre boyutlandırıyoruz."),
        (u"Revit modelimi doğrudan kullanabilir miyim?",
         u"Evet. V-Ray for Revit, Enscape ve Lumion, Revit ile doğrudan çalışır. "
         u"Verimli sonuç için modelin malzeme ve kesit temizliği önem taşır; bu hazırlığı "
         u"eğitim kapsamında aktarıyoruz."),
        (u"Eğitim veriyor musunuz?",
         u"Evet. 3ds Max, V-Ray, Corona ve Lumion eğitimleri İzmir merkez ofisimizdeki "
         u"programda yer alır; kuruma özel, kendi projeleriniz üzerinden ilerleyen "
         u"içerikler de hazırlanabilir."),
    ],
)

COZUM["yaratici_icerik"] = dict(
    slug="yaratici-icerik", visual="yaratici-icerik", accent="#e25922",
    lead=u"Kurumsal içerik üretimi, tek tek uygulama lisanslarından ibaret değildir. "
         u"Adobe Gold Reseller Partner olarak lisans yönetimi, marka tutarlılığı ve ekip "
         u"yetkinliğini birlikte kuruyoruz.",
    stats=[(u"20+", u"Creative Cloud uygulaması tek planda"),
           (u"Gold Reseller", u"Adobe yetkili iş ortağı"),
           (u"Merkezî yönetim", u"koltuk ataması ve kurumsal depolama")],
    intro_title=u"Creative Cloud'u kurumsal ölçekte yönetmek",
    intro=[
        u"Adobe Creative Cloud for teams; Photoshop, Illustrator, InDesign, Premiere ve "
        u"Acrobat Pro dahil <strong>20'yi aşkın uygulamayı</strong> üretken yapay zekâ "
        u"özellikleri, iş birliği araçları ve kurumsal yönetim yetenekleriyle birlikte sunar.",
        u"Kurumsal ölçekte belirleyici olan uygulamaların kendisi değil, çevresindeki "
        u"düzendir: koltukların merkezî atanması ve geri alınması, çalışan ayrıldığında "
        u"varlıkların kaybolmaması, marka kitaplığının tek yerden dağıtılması ve lisans "
        u"envanterinin denetime hazır tutulması. Cadbim bu düzeni kurar ve yenileme "
        u"dönemine kadar takip eder.",
        u"İçerik hattının teknik ucu da bizim kapsamımızdadır. Mimari ve mühendislik "
        u"görsellerinin son işlemi, Substance 3D ile malzeme üretimi, Adobe Stock ile "
        u"lisanslı içerik tedariki ve sanatsal baskı atölyemizle fiziksel çıktı — "
        u"tasarımdan baskıya kadar tek muhatap.",
    ],
    bullets=[
        (u"Lisans ve koltuk yönetimi", u"Admin Console üzerinden merkezî atama, ekip "
                                       u"bazlı raporlama ve yenileme planlaması."),
        (u"Marka tutarlılığı", u"Kurumsal renk, tipografi ve şablon kitaplıklarının "
                               u"paylaşımı; her tasarımcının aynı kaynaktan çalışması."),
        (u"Üretken yapay zekâ", u"Adobe Firefly ile ticari kullanıma uygun görsel üretimi "
                                u"ve mevcut varlıkların hızla türetilmesi."),
        (u"Eğitim", u"Photoshop, Illustrator, InDesign, Premiere Pro ve After Effects "
                    u"eğitimleri; kuruma özel program seçeneğiyle."),
    ],
    brands=["autodesk", "adobe", "hp"],
    faq=[
        (u"Bireysel aboneliklerden kurumsal plana geçmeli miyiz?",
         u"Ekipte birden fazla kullanıcı varsa genellikle evet. Kurumsal planlarda "
         u"koltuklar merkezî yönetilir, çalışan değişiminde lisans ve varlıklar kurumda "
         u"kalır; ayrıca yönetici konsolu ve kurumsal depolama devreye girer."),
        (u"Adobe lisanslarını doğrudan Adobe'den de alabiliriz, farkı ne?",
         u"Yetkili iş ortağı üzerinden alımda lisans yönetimi, kurulum, Türkçe destek ve "
         u"yenileme takibi tek muhatapta toplanır. Ayrıca kurum içi kullanım profiline "
         u"göre doğru plan bileşimini birlikte belirleriz."),
        (u"Firefly ile üretilen görseller ticari olarak kullanılabilir mi?",
         u"Adobe, Firefly'ın ticari kullanıma uygun olacak şekilde eğitildiğini "
         u"belirtmektedir. Kullanım koşulları plan türüne göre değişebildiğinden, "
         u"yayına almadan önce güncel Adobe şartlarını birlikte teyit etmenizi öneririz."),
        (u"Eğitim ve baskı desteği de veriyor musunuz?",
         u"Evet. Adobe uygulamalarına yönelik eğitimlerin yanında, HP DesignJet altyapımızla "
         u"sanatsal ve teknik baskı hizmeti sunuyoruz."),
    ],
)

COZUM["gerceklik_yakalama"] = dict(
    slug="gerceklik-yakalama", visual="gerceklik-yakalama", accent="#fbbf24",
    lead=u"Mevcut yapıyı metreyle ölçmek hem yavaştır hem eksik. Lazer tarama ve "
         u"fotogrametri verisi ReCap Pro ile işlenerek tasarımın üzerine oturacağı "
         u"gerçek zemin hâline gelir.",
    stats=[(u"Nokta bulutu → mesh", u"tarama verisinden model üretimi"),
           (u"Revit eklentisi", u"büyük mesh verisinin proje içine alınması"),
           (u"AEC", u"Collection kapsamında")],
    intro_title=u"Gerçeklik yakalama iş akışı",
    intro=[
        u"Autodesk ReCap Pro, gerçek dünyadaki varlıkların yüksek kaliteli ve detaylı "
        u"modellerinin yakalanmasını sağlar: fotoğraflardan veya lazer taramalardan "
        u"<strong>3B model üretmek</strong>, mevcut durumu ve as-built varlıkları nokta "
        u"bulutu ya da mesh olarak teslim etmek ve bulut tabanlı iş akışlarıyla dosyaları "
        u"güncelleyip yönetmek.",
        u"Tipik akış şöyledir: sahada birden çok duruş noktasından tarama yapılır, "
        u"taramalar tek koordinat sisteminde kaydedilir (registration), gürültü temizlenir "
        u"ve veri seyreltilir. Ardından nokta bulutu Revit, AutoCAD veya Civil 3D içine "
        u"referans olarak alınır ve modelleme bu gerçek veri üzerinde yapılır.",
        u"Kazanç iki yerde ortaya çıkar. Birincisi ölçüm doğruluğu: mevcut yapının "
        u"gerçek geometrisi üzerinde çalışıldığı için yenileme ve ekipman yerleştirme "
        u"projelerinde saha sürprizleri azalır. İkincisi zaman: haftalar süren rölöve "
        u"çalışması, günlere iner.",
    ],
    bullets=[
        (u"Tarama ve kayıt", u"Çoklu duruş taramalarının tek koordinat sisteminde "
                             u"birleştirilmesi; kayıt hassasiyetinin raporlanması."),
        (u"Nokta bulutundan mesh'e", u"Scan to Mesh ile bölümlenmiş mesh modeller; "
                                     u"Mesh Editor üzerinden detaylı dışa aktarım."),
        (u"Scan-to-BIM", u"Nokta bulutunun Revit ve Civil 3D içine referanslanması; "
                         u"as-built modelin gerçek veri üzerine kurulması."),
        (u"Paylaşım", u"Tarama verisinin bulut üzerinden ekiplerle paylaşılması, işaretleme "
                      u"ve gözden geçirme."),
    ],
    brands=["autodesk", "trimble", "sketchup", "hp"],
    faq=[
        (u"Tarama hizmetini siz mi yapıyorsunuz?",
         u"Cadbim'in kapsamı yazılım tarafı, iş akışı kurulumu ve eğitimdir; saha tarama "
         u"hizmeti için çalıştığımız iş ortaklarıyla birlikte çözüm üretiyoruz. "
         u"Projenizin kapsamını paylaşırsanız uygun modeli birlikte belirleriz."),
        (u"Telefonla çekilen fotoğraflar yeterli olur mu?",
         u"Küçük nesneler ve kaba hacim çalışmaları için fotogrametri iş görebilir; "
         u"ancak bina ve tesis ölçeğinde, milimetre mertebesinde doğruluk gerektiren "
         u"işlerde lazer tarama gerekir."),
        (u"Nokta bulutu dosyaları çok büyük, bilgisayarımız kaldırır mı?",
         u"ReCap indeksleme ve seyreltme ile büyük veriyi yönetilebilir kılar; yine de "
         u"bellek ve disk hızı belirleyicidir. HP Z serisi yapılandırmalarını veri "
         u"hacminize göre boyutlandırıyoruz."),
        (u"ReCap Pro'yu tek başına alabilir miyim?",
         u"Alınabilir; ancak taramadan modele giden akışta Revit, Civil 3D ve Navisworks "
         u"de devreye girdiğinden AEC Collection çoğu ekipte daha bütünlüklü bir "
         u"başlangıç olur. Karşılaştırmalı teklifi birlikte çıkarabiliriz."),
    ],
)
