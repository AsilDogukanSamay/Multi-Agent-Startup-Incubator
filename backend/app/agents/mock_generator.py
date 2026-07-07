import re
from typing import Dict, Any

class MockGenerator:
    @staticmethod
    def clean_text(text: str) -> str:
        # Remove non-alphanumeric characters for clean titles
        return re.sub(r'[^a-zA-ZğüşıöçĞÜŞİÖÇ\s]', '', text).strip()

    @staticmethod
    def get_keywords(idea: str) -> list:
        # Simple Turkish stop words removal to extract keywords
        stop_words = {"bir", "ve", "veya", "ile", "için", "uygulaması", "projesi", "platformu", "sistemi", "yapan", "eden", "olan"}
        words = idea.lower().split()
        keywords = [re.sub(r'[^a-zA-ZğüşıöçĞÜŞİÖÇ]', '', w) for w in words]
        return [w for w in keywords if w and w not in stop_words]

    @classmethod
    def generate_market(cls, idea: str) -> Dict[str, Any]:
        kws = cls.get_keywords(idea)
        kw_title = cls.clean_text(idea.split()[0]) if idea.split() else "Girişim"
        if len(kw_title) > 15:
            kw_title = kw_title[:12] + "..."
            
        main_kw = kws[0] if kws else "hizmet"
        second_kw = kws[1] if len(kws) > 1 else "kullanıcı"
        
        # Categorize
        idea_lower = idea.lower()
        if any(w in idea_lower for w in ["tarım", "sulama", "bitki", "bahçe", "tarl"]):
            category = "Agriculture"
            audience = ["Modern çiftçiler ve tarım işletmeleri", "Akıllı tarım teknolojilerine ilgi duyanlar", "Tarım kooperatifleri"]
            competitors = [
                {"name": "Geleneksel Tarım Sensörleri", "advantage": "Fiziksel dayanıklılık", "disadvantage": "AI analizi ve mobil entegrasyon eksikliği"},
                {"name": "Büyük Endüstriyel Tarım Firmaları", "advantage": "Geniş bütçe", "disadvantage": "Küçük ve orta ölçekli çiftçilere yüksek maliyet"}
            ]
            trends = ["Yapay zeka destekli sulama optimizasyonu", "Hassas tarım teknolojilerinin yaygınlaşması", "Su tasarrufu odaklı çevre dostu tarım"]
            swot = {
                "strengths": ["Anlık sensör verisi işleme", "Kolay mobil arayüz", "Su ve gübre maliyetlerinde yüksek tasarruf"],
                "weaknesses": ["Donanım üretim maliyetleri", "İnternet bağlantısı zayıf kırsal bölgeler"],
                "opportunities": ["Devlet tarım teşvikleri", "Küresel kuraklık nedeniyle su tasarrufu ihtiyacı"],
                "threats": ["Çip krizi nedeniyle donanım tedarik sorunları", "Rakiplerin benzer sensörler üretmesi"]
            }
        elif any(w in idea_lower for w in ["pet", "hayvan", "köpek", "kedi", "veteriner"]):
            category = "PetCare"
            audience = ["Çalışan kedi/köpek sahipleri", "Evcil hayvan otelleri ve bakıcıları", "Veteriner klinikleri"]
            competitors = [
                {"name": "Geleneksel Evcil Hayvan Bakıcıları", "advantage": "Kişisel temas", "disadvantage": "Otonom takip ve 7/24 durum raporlaması eksikliği"},
                {"name": "Basit Evcil Hayvan Takip Cihazları", "advantage": "Uygun fiyat", "disadvantage": "Yapay zeka analitiği ve davranış yorumlama olmaması"}
            ]
            trends = ["Evcil hayvanların insanlaştırılması (Pet Humanization)", "Akıllı evcil hayvan donanımları pazarı", "Yapay zeka destekli pet sağlık takibi"]
            swot = {
                "strengths": ["Dostlarımızın davranışlarını yapay zeka ile öğrenme", "Kullanıcı dostu mobil uygulama", "Veterinerler ile anlık veri paylaşımı"],
                "weaknesses": ["Evcil hayvanların cihazı çiğneme riski", "İlk aşamada marka bilinirliği eksikliği"],
                "opportunities": ["Hızla büyüyen pet-tech pazarı", "Sigorta şirketleriyle pet sağlık ortaklığı"],
                "threats": ["Çip tedarik zinciri aksamaları", "Büyük pet markalarının sektöre girmesi"]
            }
        elif any(w in idea_lower for w in ["eğitim", "okul", "öğrenci", "ders", "kurs", "akademi"]):
            category = "EdTech"
            audience = ["Bireysel öğrenmek isteyenler", "Özel ders veren öğretmenler", "Eğitim kurumları ve kolejler"]
            competitors = [
                {"name": "Udemy / Coursera", "advantage": "Geniş içerik kütüphanesi", "disadvantage": "Pasif izleme modeli, ki̇şelleşti̇ri̇lmi̇ş AI mentör eksikliği"},
                {"name": "Geleneksel Özel Ders", "advantage": "Birebir etkileşim", "disadvantage": "Saatlik yüksek ücret ve erişilebilirlik sınırı"}
            ]
            trends = ["Mikro-öğrenme ve mobil odaklı eğitim", "Yapay zeka destekli kişiselleştirilmiş öğrenme yolları", "Oyunlaştırma (Gamification) ile ders takibi"]
            swot = {
                "strengths": ["7/24 erişilebilir kişisel yapay zeka mentör", "Hata analizlerine göre özel soru üretimi", "Uygun fiyatlı abonelik modeli"],
                "weaknesses": ["Öğrencilerin ekran başında motivasyon kaybetmesi", "Müfredat güncellemelerinin takibi"],
                "opportunities": ["Uzaktan eğitimin kalıcı bir trend haline gelmesi", "Kurumsal şirketlerin çalışan eğitim bütçeleri"],
                "threats": ["Ücretsiz yapay zeka araçlarının (ChatGPT vb.) doğrudan ders çalıştırmak için kullanılması"]
            }
        elif any(w in idea_lower for w in ["otel", "rezervasyon", "tatil", "seyahat", "bilet"]):
            category = "Booking"
            audience = ["Sık seyahat eden iş insanları", "Butik otel işletmecileri", "Genç gezginler ve sırt çantalılar"]
            competitors = [
                {"name": "Booking.com / Airbnb", "advantage": "Devasa pazar payı ve kullanıcı tabanı", "disadvantage": "Yüksek komisyon oranları ve yapay zeka ile dinamik rota planlama eksikliği"},
                {"name": "Geleneksel Turizm Acenteleri", "advantage": "Tam paket hizmet", "disadvantage": "Yavaş işlem süreleri ve esnek olmayan fiyatlandırma"}
            ]
            trends = ["Yapay zeka destekli seyahat asistanlığı", "Yerel ve butik konaklama taleplerinde artış", "Temassız ve mobil check-in çözümleri"]
            swot = {
                "strengths": ["Yapay zeka ile kişiselleştirilmiş rota ve otel önerileri", "Çok düşük komisyon oranları", "Hızlı rezervasyon onay sistemi"],
                "weaknesses": ["Başlangıçta otel ağının sınırlı olması", "Yüksek müşteri kazanım maliyeti"],
                "opportunities": ["Seyahat trendlerindeki esnek çalışma kaynaklı artış", "Bölgesel turizm ofisleri ile ortaklık"],
                "threats": ["Seyahat kısıtlamaları veya küresel krizler", "Sektör devlerinin bütçe avantajı"]
            }
        elif any(w in idea_lower for w in ["sağlık", "diyet", "spor", "fit", "hastane", "doktor", "ilaç"]):
            category = "Health"
            audience = ["Sağlıklı yaşamı hedefleyen bireyler", "Diyetisyenler ve kişisel antrenörler", "Kronik hastalık takibi yapan hastalar"]
            competitors = [
                {"name": "Geleneksel Diyet ve Spor Salonları", "advantage": "Sosyal motivasyon", "disadvantage": "Sınırlı takip ve yüksek üyelik ücretleri"},
                {"name": "Kalori Takip Uygulamaları", "advantage": "Büyük gıda veritabanı", "disadvantage": "Yapay zeka asistanı ve bütünsel sağlık tavsiyelerinin olmaması"}
            ]
            trends = ["Uzaktan sağlık takibi (Tele-health)", "Preventif (önleyici) sağlık çözümleri", "Giyilebilir teknolojilerle entegre sağlık verisi analizi"]
            swot = {
                "strengths": ["Giyilebilir cihazlarla doğrudan entegrasyon", "AI destekli kişiye özel beslenme ve spor planı", "Hekim/Diyetisyen paneli bağlantısı"],
                "weaknesses": ["Kullanıcıların veri güvenliği endişeleri", "Medikal doğruluk sorumlulukları"],
                "opportunities": ["Büyüyen wellness ve sağlıklı yaşam bilinci", "Sağlık sigortaları ile entegrasyon fırsatı"],
                "threats": ["Sıkılaşan kişisel sağlık verisi mevzuatları (KVKK/GDPR)", "Benzer fitness uygulamalarının çokluğu"]
            }
        elif any(w in idea_lower for w in ["yemek", "restoran", "kurye", "sipariş", "mutfak"]):
            category = "FoodDelivery"
            audience = ["Çalışan beyaz yakalılar", "Yerel restoran sahipleri", "Öğrenciler ve bekar yaşayanlar"]
            competitors = [
                {"name": "Yemeksepeti / Trendyol Yemek", "advantage": "Dehşet pazar bilinirliği ve dev kurye ağı", "disadvantage": "Restoranlardan alınan yüksek komisyonlar ve kişiselleştirilmiş rota eksikliği"},
                {"name": "Restoranların Kendi Kuryeleri", "advantage": "Maliyet kontrolü", "disadvantage": "Sınırlı dağıtım kapasitesi ve sipariş takip yazılımı olmaması"}
            ]
            trends = ["Yapay zeka ile kurye rotalama optimizasyonu", "Abonelik modeli ile ücretsiz teslimat paketleri", "Bulut mutfak (Cloud Kitchen) modellerinin artışı"]
            swot = {
                "strengths": ["AI kurye rotalama ile en hızlı teslimat garantisi", "Restoran dostu çok düşük komisyon modeli", "Kullanıcıya özel yapay zeka yemek önerileri"],
                "weaknesses": ["Yüksek başlangıç kurye ve lojistik maliyeti", "Sert rekabet koşulları"],
                "opportunities": ["Bulut mutfaklarla iş birliği yaparak özel menüler çıkarma", "Abonelik tabanlı yemek paketleri"],
                "threats": ["Akaryakıt maliyetlerinin artışı", "Rakip devlerin fiyat kırma politikaları"]
            }
        elif any(w in idea_lower for w in ["ticaret", "market", "satış", "dükkan", "e-ticaret"]):
            category = "Ecommerce"
            audience = ["KOBİ'ler ve yerel üreticiler", "Sosyal medya üzerinden satış yapanlar", "Kendi e-ticaret markasını kurmak isteyenler"]
            competitors = [
                {"name": "Shopify / WooCommerce", "advantage": "Geniş eklenti mağazası", "disadvantage": "Yüksek eklenti ücretleri, teknik bilgi gereksinimi ve yerel entegrasyon zorlukları"},
                {"name": "Trendyol / Hepsiburada Pazaryerleri", "advantage": "Hazır müşteri trafiği", "disadvantage": "Çok yüksek komisyonlar ve kendi müşteri portföyünü oluşturamama"}
            ]
            trends = ["Çok kanallı (Omnichannel) satış entegrasyonu", "Yapay zeka ile otomatik ürün açıklaması ve tasarımı", "Sosyal ticaretin (Social Commerce) patlaması"]
            swot = {
                "strengths": ["Tek tıkla tüm pazaryerleri entegrasyonu", "AI ile otomatik ürün açıklaması ve görsel optimizasyonu", "Çok uygun sabit fiyat modeli"],
                "weaknesses": ["Büyük e-ticaret devlerine karşı arama motoru görünürlüğü", "Kargo firmaları ile anlaşma hacmi eksikliği"],
                "opportunities": ["KOBİ'lerin dijitalleşme sürecindeki hızlı artış", "Yurtdışına kolay e-ihracat modülü sunma"],
                "threats": ["Kargo ve lojistik maliyetlerinin hızla dalgalanması", "Global rakiplerin pazara agresif girmesi"]
            }
        else:
            category = "SaaS"
            audience = [f"Yapay zeka tabanlı {main_kw} çözümlerine ihtiyaç duyan KOBİ'ler", f"{second_kw} süreçlerini dijitalleştirmek isteyen profesyoneller", "Teknoloji odaklı girişimler"]
            competitors = [
                {
                    "name": f"Geleneksel {main_kw.capitalize()} Araçları",
                    "advantage": "Sektörde uzun süredir var olma",
                    "disadvantage": "Yapay zeka otomasyonlarının ve otonom ajan desteğinin bulunmaması"
                },
                {
                    "name": "Benzer AI Çözümleri",
                    "advantage": "Temel yapay zeka entegrasyonu",
                    "disadvantage": "Esnek olmayan mimari ve yüksek abonelik ücretleri"
                }
            ]
            trends = [f"İş süreçlerinde {main_kw} otomasyonu", "Kullanıcı dostu yapay zeka panelleri", "Veri odaklı karar destek sistemleri"]
            swot = {
                "strengths": ["Yapay zeka destekli akıllı karar motoru", "Modüler ve ölçeklenebilir altyapı", "Hızlı kurulum ve entegrasyon"],
                "weaknesses": ["Yeni başlayan marka bilinirliği", "Başlangıçta kısıtlı sektörel veri seti"],
                "opportunities": ["Dijital dönüşüm trendlerinin ivmelenmesi", "Gelişmekte olan pazarlarda ilk oyuncu olma fırsatı"],
                "threats": ["Teknolojik gelişmelerin çok hızlı değişmesi", "Büyük teknoloji şirketlerinin benzer özellikleri sunması"]
            }
            
        return {
            "target_audience": audience,
            "competitors": competitors,
            "market_trends": trends,
            "swot": swot
        }

    @classmethod
    def generate_finance(cls, idea: str, market_data: Dict[str, Any]) -> Dict[str, Any]:
        kws = cls.get_keywords(idea)
        main_kw = kws[0] if kws else "hizmet"
        
        idea_lower = idea.lower()
        if any(w in idea_lower for w in ["tarım", "sulama", "bitki", "bahçe", "tarl"]):
            monetization = ["Donanım Satışı (Akıllı Sensörler)", "SaaS Yazılım Aboneliği (Aylık/Yıllık)", "Veri Analizi Raporlama Ücretleri"]
            pricing = [
                {"tier_name": "Başlangıç (Basic)", "price": "$19 / Ay", "features": ["1 Tarla Desteği", "Saatlik Nem Ölçümü", "Temel Mobil Bildirimler"]},
                {"tier_name": "Profesyonel (Pro)", "price": "$49 / Ay", "features": ["5 Tarla Desteği", "Sensör Dahil", "Anlık Nem Ölçümü", "Yapay Zeka Sulama Önerileri", "Öncelikli Destek"]},
                {"tier_name": "Kurumsal (Enterprise)", "price": "Teklif Alın", "features": ["Sınırsız Tarla", "Özel Entegrasyon", "Ziraat Mühendisi Desteği", "API Erişimi"]}
            ]
            costs = [
                {"item": "IoT Sensör Donanım Üretim ve Parça Giderleri", "amount": "$2500 / Ay", "frequency": "Aylık"},
                {"item": "Bulut Altyapı ve Veri İletişim Maliyetleri", "amount": "$350 / Ay", "frequency": "Aylık"},
                {"item": "Ziraat Mühendisi ve Teknik Destek Kadrosu", "amount": "$4000 / Ay", "frequency": "Aylık"}
            ]
            tips = [
                "Başlangıçta donanım marjını düşük tutup, asıl geliri SaaS aboneliğinden elde etmeye odaklanın.",
                "Su tasarrufu teşvikleri veren yerel yönetimler ile ortaklıklar kurun."
            ]
        elif any(w in idea_lower for w in ["pet", "hayvan", "köpek", "kedi", "veteriner"]):
            monetization = ["Premium Mobil Uygulama Aboneliği", "Uygulama İçi Pet Market Satışları", "Veteriner Randevu Komisyonu"]
            pricing = [
                {"tier_name": "Ücretsiz (Free)", "price": "$0", "features": ["Temel Profil Oluşturma", "Aşı Takvimi", "Sınırlı Günlük Log"]},
                {"tier_name": "Premium Pet", "price": "$12 / Ay", "features": ["Yapay Zeka Davranış Analizi", "Sınırsız Log Takibi", "Veterinerle Canlı Sohbet", "Pet Market İndirimleri"]},
                {"tier_name": "Çoklu Evcil (Family)", "price": "$24 / Ay", "features": ["3 Evcil Hayvan Desteği", "Tüm Premium Özellikler", "Özel Destek"]}
            ]
            costs = [
                {"item": "Veteriner Destek ve Danışmanlık Ücretleri", "amount": "$1500 / Ay", "frequency": "Aylık"},
                {"item": "Mobil Uygulama Sunucu ve Veri Trafik Giderleri", "amount": "$200 / Ay", "frequency": "Aylık"},
                {"item": "Sosyal Medya Reklamları ve Topluluk Yönetimi", "amount": "$1000 / Ay", "frequency": "Aylık"}
            ]
            tips = [
                "Mama ve aksesuar markalarıyla sponsorluk anlaşmaları yaparak ek gelir yaratın.",
                "Kullanıcıların aşı takvimi gibi vazgeçilmez özellikleri ücretsiz sunarak bağlılığı artırın."
            ]
        elif any(w in idea_lower for w in ["eğitim", "okul", "öğrenci", "ders", "kurs", "akademi"]):
            monetization = ["Aylık Öğrenci Aboneliği", "Eğitim Kurumu Kurumsal Lisansları", "Sertifika ve Sınav Ücretleri"]
            pricing = [
                {"tier_name": "Öğrenci (Student)", "price": "$9 / Ay", "features": ["Aylık 20 AI Mentör Sorusu", "Ders Raporları", "Temel Alıştırmalar"]},
                {"tier_name": "Sınav Hazırlık (Pro)", "price": "$25 / Ay", "features": ["Sınırsız AI Mentör Sorusu", "Hata Analiz Grafikleri", "Kişiselleştirilmiş Çalışma Planı", "Başarı Sertifikası"]},
                {"tier_name": "Okul (Enterprise)", "price": "Teklif Alın", "features": ["Öğretmen Yönetim Paneli", "Öğrenci İlerleme Raporları", "API Entegrasyonu"]}
            ]
            costs = [
                {"item": "Gemini API ve Büyük Dil Modelleri Maliyetleri", "amount": "$600 / Ay", "frequency": "Aylık"},
                {"item": "Eğitim İçeriği ve Soru Bankası Üretim Giderleri", "amount": "$2000", "frequency": "Tek seferlik"},
                {"item": "Sunucu Altyapısı ve Ölçekleme Giderleri", "amount": "$300 / Ay", "frequency": "Aylık"}
            ]
            tips = [
                "Gemini API maliyetlerini kontrol altında tutmak için sık sorulan soruları yerel veritabanında cache'leyin.",
                "Eğitim kurumlarına demo sürüm vererek toplu satış yapmaya odaklanın."
            ]
        elif any(w in idea_lower for w in ["otel", "rezervasyon", "tatil", "seyahat", "bilet"]):
            monetization = ["Rezervasyon Başına Komisyon (%5 - %8)", "Otel/İşletme Premium Listeleme Ücretleri", "AI Rota Planlama Premium Servisi"]
            pricing = [
                {"tier_name": "Standart Üyelik", "price": "Ücretsiz", "features": ["Rezervasyon Yapma", "Standart Listeleme", "E-posta Bildirimleri"]},
                {"tier_name": "Gezgin Pro (Traveler)", "price": "$8 / Ay", "features": ["Rezervasyonlarda İndirim", "Yapay Zeka Akıllı Rota Planlayıcı", "Reklamsız Deneyim", "7/24 Öncelikli Destek"]},
                {"tier_name": "İşletme Premium", "price": "$39 / Ay", "features": ["Listelemelerde En Üst Sıra", "İşletme İstatistikleri Paneli", "Doğrudan Mesajlaşma"]}
            ]
            costs = [
                {"item": "Müşteri İlişkileri ve Destek Operasyonları", "amount": "$2000 / Ay", "frequency": "Aylık"},
                {"item": "Harita ve Lokasyon API Lisans Bedelleri (Google Maps vb.)", "amount": "$400 / Ay", "frequency": "Aylık"},
                {"item": "Arama Motoru Reklamcılığı (SEO/Google Ads)", "amount": "$1500 / Ay", "frequency": "Aylık"}
            ]
            tips = [
                "Başlangıçta komisyon oranlarını düşük tutarak otelleri platforma çekin.",
                "AI rota planlayıcı özelliğini pazarlamada öne çıkararak diğer platformlardan sıyrılın."
            ]
        elif any(w in idea_lower for w in ["sağlık", "diyet", "spor", "fit", "hastane", "doktor", "ilaç"]):
            monetization = ["Bireysel Premium Sağlık Aboneliği", "Diyetisyen/Antrenör Yönetim Yazılımı Lisansı", "Uygulama İçi Gıda/Takviye Satış Komisyonu"]
            pricing = [
                {"tier_name": "Temel Sağlık", "price": "Ücretsiz", "features": ["Günlük Su ve Kalori Kaydı", "Basit Adım Takibi"]},
                {"tier_name": "Premium Fit", "price": "$15 / Ay", "features": ["AI Destekli Diyet ve Egzersiz Planı", "Detaylı Makro Analizleri", "Giyilebilir Cihaz Entegrasyonu", "Uzman Danışma"]},
                {"tier_name": "Klinik Panel (B2B)", "price": "$59 / Ay", "features": ["Sınırsız Danışan Yönetimi", "Danışan Sağlık Verisi Takibi", "API Erişimi"]}
            ]
            costs = [
                {"item": "Medikal Hukuk ve KVKK Veri Güvenliği Danışmanlığı", "amount": "$3000", "frequency": "Tek seferlik"},
                {"item": "Güvenli Sağlık Verisi Bulut Depolama Maliyetleri", "amount": "$500 / Ay", "frequency": "Aylık"},
                {"item": "Diyetisyen ve Spor Eğitmeni İş Birlikleri", "amount": "$2500 / Ay", "frequency": "Aylık"}
            ]
            tips = [
                "Kullanıcı verilerinin güvenliğini (KVKK) en üst düzeyde koruduğunuzu pazarlamada vurgulayın.",
                "Akıllı saat markalarıyla (Apple, Garmin vb.) entegrasyonları ilk günden hazır edin."
            ]
        elif any(w in idea_lower for w in ["yemek", "restoran", "kurye", "sipariş", "mutfak"]):
            monetization = ["Sipariş Başına Komisyon (%10)", "Kurye Teslimat Ücreti", "Restoran Öne Çıkarma Sponsorlukları"]
            pricing = [
                {"tier_name": "Klasik Üyelik", "price": "Ücretsiz", "features": ["Restoranlardan Sipariş", "Standart Teslimat"]},
                {"tier_name": "Gurme Plus (SaaS)", "price": "$10 / Ay", "features": ["Tüm Siparişlerde Ücretsiz Teslimat", "Öncelikli Kurye Ataması", "Özel Gurme İndirimleri"]},
                {"tier_name": "Restoran Premium", "price": "$45 / Ay", "features": ["Komisyonda İndirim", "Haftalık Analiz Raporu", "Sponsorlu Öne Çıkarma"]}
            ]
            costs = [
                {"item": "Kurye Havuzu ve Dağıtım Operasyon Maliyetleri", "amount": "$5000 / Ay", "frequency": "Aylık"},
                {"item": "Harita API ve Rota Optimizasyon Sunucu Giderleri", "amount": "$600 / Ay", "frequency": "Aylık"},
                {"item": "Restoran Kazanım Saha Personel Giderleri", "amount": "$3000 / Ay", "frequency": "Aylık"}
            ]
            tips = [
                "Bölgesel olarak küçük alanlarda başlayıp kurye lojistiğini optimize ettikten sonra büyüyün.",
                "Abonelik modeli olan Plus paketini satarak düzenli nakit akışı sağlayın."
            ]
        elif any(w in idea_lower for w in ["ticaret", "market", "satış", "dükkan", "e-ticaret"]):
            monetization = ["Aylık Dükkan Yazılım Aboneliği", "Ödeme Altyapısı İşlem Komisyonu (%1.5)", "Kargo Entegrasyon Kar Payı"]
            pricing = [
                {"tier_name": "Yeni Başlayan", "price": "$15 / Ay", "features": ["50 Ürün Ekleme", "Hazır Ödeme Entegrasyonu", "Temel Tema"]},
                {"tier_name": "Büyüyen KOBİ (Pro)", "price": "$39 / Ay", "features": ["Sınırsız Ürün Ekleme", "AI Ürün Açıklaması Yazıcı", "Pazaryeri Entegrasyonları", "Gelişmiş Raporlama"]},
                {"tier_name": "Kurumsal (Enterprise)", "price": "Teklif Alın", "features": ["Özel Tema Tasarımı", "Dedicated Sunucu Altyapısı", "Birebir Destek"]}
            ]
            costs = [
                {"item": "E-Ticaret Sunucu ve CDN Altyapı Maliyetleri", "amount": "$800 / Ay", "frequency": "Aylık"},
                {"item": "Teknik Destek ve Canlı Yardım Ekibi", "amount": "$2000 / Ay", "frequency": "Aylık"},
                {"item": "Ödeme Geçidi Lisansları ve Güvenlik Altyapısı", "amount": "$1500", "frequency": "Tek seferlik"}
            ]
            tips = [
                "Kullanıcıların sitelerinin çok hızlı açılmasını sağlayacak CDN ve veritabanı optimizasyonlarına önem verin.",
                "AI ile ürün görseli arka planı silme gibi özellikleri KOBİ'lere pazarlama kozu olarak sunun."
            ]
        else:
            monetization = ["SaaS Yazılım Aboneliği", "Kullanım Başına API veya Kredi Satışı", "B2B Özel Kurulum ve Entegrasyon Bedelleri"]
            pricing = [
                {"tier_name": "Başlangıç (Basic)", "price": "$19 / Ay", "features": ["Temel AI Özellikleri", "Aylık 1000 Kredi", "E-posta Desteği"]},
                {"tier_name": "Profesyonel (Pro)", "price": "$49 / Ay", "features": ["Gelişmiş AI Modülleri", "Sınırsız Kredi", "7/24 Canlı Sohbet Desteği", "API Entegrasyon Erişimi"]},
                {"tier_name": "Kurumsal (Enterprise)", "price": "Teklif Alın", "features": ["Özel Sunucu Kurulumu", "Dedicated AI Kaynakları", "SLA Desteği"]}
            ]
            costs = [
                {"item": "AI API Sorgu ve Model Barındırma Ücretleri", "amount": "$500 / Ay", "frequency": "Aylık"},
                {"item": "Sunucu Altyapı ve Veri Depolama Giderleri", "amount": "$250 / Ay", "frequency": "Aylık"},
                {"item": "Yazılım Geliştirme ve Bakım Hizmet Bedelleri", "amount": "$3000 / Ay", "frequency": "Aylık"}
            ]
            tips = [
                "Kullanıcı başı API maliyetini düşürmek için verimli LLM prompt yapılandırmaları yapın.",
                "Yıllık alımlarda %20 indirim sunarak kullanıcı bağlılığını ve nakit akışını artırın."
            ]
            
        return {
            "monetization_models": monetization,
            "pricing_tiers": pricing,
            "estimated_costs": costs,
            "financial_tips": tips
        }

    @classmethod
    def generate_tech(cls, idea: str, market_data: Dict[str, Any], finance_data: Dict[str, Any]) -> Dict[str, Any]:
        kws = cls.get_keywords(idea)
        main_kw = kws[0] if kws else "girişim"
        
        idea_lower = idea.lower()
        if any(w in idea_lower for w in ["tarım", "sulama", "bitki", "bahçe", "tarl"]):
            stack = {
                "frontend": ["React Native (Android/iOS Mobil)", "HTML5/CSS3", "Chart.js (Grafikler)"],
                "backend": ["Python", "FastAPI (Asenkron API)", "Uvicorn", "C++ (IoT Sensör Yazılımı)"],
                "database": ["InfluxDB (Zaman serisi veri tabanı - sensör verisi)", "PostgreSQL (Kullanıcı ve Tarla Verisi)"],
                "cloud_hosting": ["AWS IoT Core", "Render", "Vercel"],
                "ai_models": ["Gemini 2.5 Flash", "TensorFlow Lite (Kenar yapay zeka - Edge AI)"]
            }
            schema = [
                {"table_name": "users", "columns": ["id (UUID) - Primary Key", "email (VARCHAR) - Kullanıcı e-postası", "created_at (TIMESTAMP) - Kayıt tarihi"]},
                {"table_name": "fields", "columns": ["id (UUID) - Primary Key", "user_id (UUID) - Foreign Key -> users.id", "name (VARCHAR) - Tarla adı", "soil_type (VARCHAR) - Toprak türü"]},
                {"table_name": "sensor_logs", "columns": ["id (BIGINT) - Primary Key", "field_id (UUID) - Foreign Key -> fields.id", "moisture (FLOAT) - Toprak nemi %", "temperature (FLOAT) - Sıcaklık C", "timestamp (TIMESTAMP) - Kayıt zamanı"]}
            ]
            endpoints = [
                {"method": "GET", "path": "/api/v1/fields", "description": "Kullanıcının tarlalarını listeler."},
                {"method": "POST", "path": "/api/v1/sensors/log", "description": "Sensörden gelen nem ve sıcaklık verisini kaydeder."},
                {"method": "POST", "path": "/api/v1/irrigation/trigger", "description": "Yapay zeka analizine göre sulama valfini tetikler."}
            ]
            summary = "IoT tarla sensörleri nem verilerini InfluxDB zaman serisi veritabanına gönderir. FastAPI backend servisi bu verileri analiz eder ve nem seviyesi kritik sınırın altına düştüğünde mobil uygulamaya bildirim atarak sulama valfini tetikler."
        elif any(w in idea_lower for w in ["pet", "hayvan", "köpek", "kedi", "veteriner"]):
            stack = {
                "frontend": ["Flutter (Cross-platform Mobil Uygulama)", "Tailwind CSS"],
                "backend": ["Python", "FastAPI", "Uvicorn"],
                "database": ["PostgreSQL (Kullanıcı ve Pet Verisi)", "Redis (Hızlı önbellek)"],
                "cloud_hosting": ["Supabase", "Render", "AWS S3 (Pet fotoğrafları)"],
                "ai_models": ["Gemini 2.5 Flash (Pet davranış analiz motoru)"]
            }
            schema = [
                {"table_name": "users", "columns": ["id (UUID) - Primary Key", "email (VARCHAR) - Kullanıcı e-postası", "password_hash (VARCHAR) - Şifre"]},
                {"table_name": "pets", "columns": ["id (UUID) - Primary Key", "user_id (UUID) - Foreign Key -> users.id", "name (VARCHAR) - Pet ismi", "type (VARCHAR) - Tür (Kedi/Köpek)"]},
                {"table_name": "activity_logs", "columns": ["id (BIGINT) - Primary Key", "pet_id (UUID) - Foreign Key -> pets.id", "activity_type (VARCHAR) - Aktivite (Yemek/Yürüyüş)", "duration (INT) - Süre (dakika)"]}
            ]
            endpoints = [
                {"method": "GET", "path": "/api/v1/pets", "description": "Kullanıcının evcil hayvanlarını listeler."},
                {"method": "POST", "path": "/api/v1/pets/activity", "description": "Evcil hayvan için yeni bir aktivite kaydeder."},
                {"method": "POST", "path": "/api/v1/ai/behavior-analyze", "description": "Haftalık pet loglarını analiz ederek davranış raporu sunar."}
            ]
            summary = "Evcil hayvan sahipleri petlerinin günlük aktivitelerini Flutter mobil uygulaması üzerinden kaydeder. FastAPI sunucusu bu verileri PostgreSQL veritabanında saklar ve Gemini API entegrasyonu ile haftalık pet sağlık/davranış analizleri çıkartır."
        elif any(w in idea_lower for w in ["eğitim", "okul", "öğrenci", "ders", "kurs", "akademi"]):
            stack = {
                "frontend": ["React.js (Web Panel)", "Tailwind CSS", "Monaco Editor (Kod alıştırmaları için)"],
                "backend": ["Python", "FastAPI", "Uvicorn", "Docker (Güvenli kod çalıştırma ortamı)"],
                "database": ["PostgreSQL (Öğrenci ve Ders ilerlemeleri)", "MongoDB (Soru bankası ve esnek soru içerikleri)"],
                "cloud_hosting": ["Vercel", "DigitalOcean Droplets", "AWS S3"],
                "ai_models": ["Gemini 2.5 Flash (Eğitim mentörü)", "Gemini 2.5 Pro (Kod analizörü)"]
            }
            schema = [
                {"table_name": "students", "columns": ["id (UUID) - Primary Key", "name (VARCHAR) - Öğrenci adı", "email (VARCHAR) - E-posta"]},
                {"table_name": "courses", "columns": ["id (UUID) - Primary Key", "title (VARCHAR) - Ders başlığı", "description (TEXT) - Ders içeriği"]},
                {"table_name": "submissions", "columns": ["id (UUID) - Primary Key", "student_id (UUID) - Foreign Key", "course_id (UUID) - Foreign Key", "code_content (TEXT) - Öğrenci kodu", "is_correct (BOOLEAN) - Doğruluk durumu"]}
            ]
            endpoints = [
                {"method": "GET", "path": "/api/v1/courses", "description": "Aktif eğitim derslerini listeler."},
                {"method": "POST", "path": "/api/v1/student/submit", "description": "Öğrencinin kod alıştırmasını Docker sandbox içinde test eder ve kaydeder."},
                {"method": "POST", "path": "/api/v1/ai/mentor-advice", "description": "Öğrencinin hatalarına göre Gemini tabanlı mentorluk tavsiyesi üretir."}
            ]
            summary = "Öğrenci React.js web platformunda kod alıştırmalarını çözer. FastAPI backend servisi kodu alır ve güvenli Docker sandbox konteynerlerinde çalıştırarak test eder. Hata durumlarında Gemini API tetiklenerek öğrenciye özel rehberlik sunulur."
        elif any(w in idea_lower for w in ["otel", "rezervasyon", "tatil", "seyahat", "bilet"]):
            stack = {
                "frontend": ["Next.js (React Web Uygulaması)", "Tailwind CSS", "Mapbox GL (İnteraktif seyahat haritası)"],
                "backend": ["Python", "FastAPI", "Uvicorn", "Celery (Arka plan görevleri - e-posta bildirimleri)"],
                "database": ["PostgreSQL (Kullanıcı, Otel ve Rezervasyonlar)", "Redis (Oda doluluk lock mekanizması ve kuyruk)"],
                "cloud_hosting": ["Vercel (Frontend)", "AWS ECS (Fargate Backend)", "Supabase Auth"],
                "ai_models": ["Gemini 2.5 Flash (Kişiselleştirilmiş rota ve otel öneri algoritması)"]
            }
            schema = [
                {"table_name": "hotels", "columns": ["id (UUID) - Primary Key", "name (VARCHAR) - Otel adı", "city (VARCHAR) - Şehir", "price_per_night (DECIMAL) - Gecelik ücret"]},
                {"table_name": "reservations", "columns": ["id (UUID) - Primary Key", "hotel_id (UUID) - Foreign Key", "check_in (DATE) - Giriş tarihi", "check_out (DATE) - Çıkış tarihi", "status (VARCHAR) - Rezervasyon durumu"]}
            ]
            endpoints = [
                {"method": "GET", "path": "/api/v1/hotels/search", "description": "Şehir ve tarihe göre uygun otelleri listeler."},
                {"method": "POST", "path": "/api/v1/reservations/create", "description": "Redis kilitlemesi kullanarak mükerrer rezervasyonu önleyerek oda ayırtır."},
                {"method": "POST", "path": "/api/v1/ai/route-plan", "description": "Gezginin bütçe ve tercihlerine göre yapay zekalı seyahat rotası çizer."}
            ]
            summary = "Rezervasyon sistemi Next.js arayüzünden Mapbox harita entegrasyonu ile otelleri gösterir. Çakışmaları önlemek için Redis tabanlı lock kullanılır. FastAPI backend, rezervasyon tamamlandığında Celery ile e-posta gönderir."
        elif any(w in idea_lower for w in ["sağlık", "diyet", "spor", "fit", "hastane", "doktor", "ilaç"]):
            stack = {
                "frontend": ["React Native (iOS/Android)", "HealthKit / Google Fit API", "Tailwind CSS"],
                "backend": ["Python", "FastAPI", "Uvicorn"],
                "database": ["PostgreSQL (Şifrelenmiş kullanıcı verisi)", "Redis (Hızlı veri depolama)"],
                "cloud_hosting": ["AWS (HiPAA uyumlu bulut barındırma)", "Render"],
                "ai_models": ["Gemini 2.5 Flash (Önleyici sağlık ve diyet tavsiye motoru)"]
            }
            schema = [
                {"table_name": "users", "columns": ["id (UUID) - Primary Key", "email (VARCHAR) - E-posta (AES şifreli)", "created_at (TIMESTAMP) - Oluşturma tarihi"]},
                {"table_name": "health_metrics", "columns": ["id (BIGINT) - Primary Key", "user_id (UUID) - Foreign Key", "heart_rate (INT) - Nabız", "steps (INT) - Adım sayısı", "timestamp (TIMESTAMP) - Kayıt zamanı"]}
            ]
            endpoints = [
                {"method": "POST", "path": "/api/v1/health/sync", "description": "Akıllı saatten gelen nabız ve adım verilerini senkronize eder."},
                {"method": "GET", "path": "/api/v1/health/weekly", "description": "Kullanıcının haftalık sağlık raporunu döner."},
                {"method": "POST", "path": "/api/v1/ai/diet-plan", "description": "Kullanıcının günlük sağlık verilerine göre yapay zekalı beslenme planı üretir."}
            ]
            summary = "Mobil uygulama, akıllı saatlerdeki HealthKit/Google Fit verilerini alıp şifreli bağlantıyla FastAPI sunucusuna gönderir. PostgreSQL veritabanında saklanan hassas sağlık verileri, Gemini API ile işlenerek kişiye özel önleyici sağlık tavsiyelerine dönüştürülür."
        elif any(w in idea_lower for w in ["yemek", "restoran", "kurye", "sipariş", "mutfak"]):
            stack = {
                "frontend": ["Next.js (Restoran Paneli & Web)", "Flutter (Kurye Mobil Uygulaması)", "Tailwind CSS"],
                "backend": ["Python", "FastAPI", "Uvicorn", "Websockets (Canlı sipariş takibi)"],
                "database": ["PostgreSQL (Sipariş ve Restoran verisi)", "Redis (Kurye anlık lokasyon depolama)"],
                "cloud_hosting": ["AWS ECS", "AWS ElastiCache", "Vercel"],
                "ai_models": ["Gemini 2.5 Flash (Kurye rotalama optimizasyonu)"]
            }
            schema = [
                {"table_name": "orders", "columns": ["id (UUID) - Primary Key", "restaurant_id (UUID) - Foreign Key", "customer_address (TEXT) - Adres", "status (VARCHAR) - Sipariş durumu (Hazırlanıyor/Yolda)"]},
                {"table_name": "couriers", "columns": ["id (UUID) - Primary Key", "name (VARCHAR) - Kurye adı", "is_active (BOOLEAN) - Aktiflik durumu"]}
            ]
            endpoints = [
                {"method": "POST", "path": "/api/v1/orders/create", "description": "Yeni bir yemek siparişi oluşturur ve restoran paneline anlık iletir."},
                {"method": "GET", "path": "/api/v1/courier/route", "description": "Kurye için yapay zekayla optimize edilmiş en hızlı rota çizgisini döner."},
                {"method": "GET", "path": "/api/v1/order/track", "description": "Websocket üzerinden kuryenin konumunu canlı olarak istemciye aktarır."}
            ]
            summary = "Müşteri sipariş verdiğinde FastAPI, Websocket bağlantısı ile restoran paneline siparişi anlık düşürür. Kuryenin anlık konum verisi Redis'te tutulur ve yapay zeka tabanlı rota çizim motoru ile en hızlı teslimat planı çıkarılır."
        elif any(w in idea_lower for w in ["ticaret", "market", "satış", "dükkan", "e-ticaret"]):
            stack = {
                "frontend": ["Next.js (Mağaza Vitrini & Admin Paneli)", "Tailwind CSS", "Framer Motion"],
                "backend": ["Python", "FastAPI", "Uvicorn", "Stripe / iyzico (Ödeme API entegrasyonu)"],
                "database": ["PostgreSQL (Ürünler, Siparişler ve Stoklar)", "Elasticsearch (Hızlı ürün arama motoru)"],
                "cloud_hosting": ["Vercel (Frontend)", "AWS Fargate (Backend)", "AWS CloudFront (Hızlı CDN)"],
                "ai_models": ["Gemini 2.5 Flash (Otomatik ürün açıklaması ve pazarlama görseli yazarı)"]
            }
            schema = [
                {"table_name": "products", "columns": ["id (UUID) - Primary Key", "title (VARCHAR) - Ürün adı", "description (TEXT) - Ürün açıklaması", "stock (INT) - Stok miktarı", "price (DECIMAL) - Satış fiyatı"]},
                {"table_name": "orders", "columns": ["id (UUID) - Primary Key", "total_price (DECIMAL) - Toplam ciro", "created_at (TIMESTAMP) - Sipariş tarihi"]}
            ]
            endpoints = [
                {"method": "GET", "path": "/api/v1/products/search", "description": "Elasticsearch kullanarak milisaniyeler içinde arama sonuçlarını listeler."},
                {"method": "POST", "path": "/api/v1/admin/ai-generate-desc", "description": "Ürün başlığına göre Gemini API ile SEO uyumlu açıklama metni hazırlar."},
                {"method": "POST", "path": "/api/v1/checkout", "description": "Ödeme entegrasyonunu (Stripe/iyzico) tetikleyerek siparişi tamamlar."}
            ]
            summary = "E-Ticaret sistemi Next.js admin paneli üzerinden yönetilir. Admin yeni ürün eklediğinde Gemini API ile otomatik ürün açıklamaları üretilir. Hızlı arama sorguları Elasticsearch ile karşılanır ve ödeme işlemi güvenli API'lerle tamamlanır."
        else:
            stack = {
                "frontend": ["Next.js (Web Panel)", "Tailwind CSS", "Framer Motion"],
                "backend": ["Python", "FastAPI", "Uvicorn"],
                "database": ["PostgreSQL (Kullanıcı verileri ve ana modeller)", "Redis (Önbellek ve kuyruk yönetimi)"],
                "cloud_hosting": ["Render", "Vercel", "AWS S3"],
                "ai_models": ["Gemini 2.5 Flash (Ana analiz ve otomasyon motoru)"]
            }
            schema = [
                {"table_name": "users", "columns": ["id (UUID) - Primary Key", "email (VARCHAR) - Kullanıcı e-postası", "created_at (TIMESTAMP) - Kayıt tarihi"]},
                {"table_name": "analyses", "columns": ["id (UUID) - Primary Key", "user_id (UUID) - Foreign Key -> users.id", "input_data (TEXT) - Kullanıcı girdisi", "output_data (JSON) - Çözüm sonuçları"]}
            ]
            endpoints = [
                {"method": "POST", "path": f"/api/v1/{main_kw}/analyze", "description": f"Kullanıcı girdisini alır ve Gemini modelini tetikleyerek analiz raporu üretir."},
                {"method": "GET", "path": f"/api/v1/{main_kw}/history", "description": "Geçmiş analiz kayıtlarını listeler."},
                {"method": "DELETE", "path": f"/api/v1/analysis/delete", "description": "Analiz kaydını sistemden siler."}
            ]
            summary = f"Girişim platformu Next.js web uygulaması üzerinden {main_kw} otomasyon süreçlerini yönetir. Girdiler FastAPI backend servisine aktarılır ve PostgreSQL veritabanında saklanır. Gemini API ile veriler analiz edilip kullanıcıya canlı loglar eşliğinde gösterilir."
            
        return {
            "tech_stack": stack,
            "database_schema": schema,
            "api_endpoints": endpoints,
            "architecture_summary": summary
        }

    @classmethod
    def generate_prototype(cls, idea: str) -> Dict[str, Any]:
        idea_lower = idea.lower()
        kws = cls.get_keywords(idea)
        kw_title = cls.clean_text(idea.split()[0]) if idea.split() else "Girişim"
        if len(kw_title) > 15:
            kw_title = kw_title[:12] + "..."
            
        main_kw = kws[0] if kws else "hizmet"
        
        # Categorize
        if any(w in idea_lower for w in ["tarım", "sulama", "bitki", "bahçe", "tarl"]):
            app_name = "AgriPulse"
            primary_color = "#06b6d4"
            screens = {
                "main": {
                    "navigation_title": "Genel Durum",
                    "layout": [
                        { "type": "text", "text": "🌱 Akıllı Tarla Takibi", "size": "large" },
                        { "type": "chart", "chart_type": "ring", "value": 42, "label": "Nem Oranı" },
                        { "type": "card", "title": "Toprak Durumu", "desc": "Nem kritik seviyede (%42). Sulama önerilir." },
                        { "type": "button", "label": "Vana Kontrollerine Git", "action": "navigate", "target": "controls" }
                    ]
                },
                "controls": {
                    "navigation_title": "Vana Yönetimi",
                    "layout": [
                        { "type": "text", "text": "💦 Sulama Kontrolü", "size": "medium" },
                        { "type": "input", "placeholder": "Sulama Süresi (Dk)", "input_type": "number" },
                        { "type": "card", "title": "Vana Seçimi", "desc": "Ana Vana #1 (Kapalı)" },
                        { "type": "button", "label": "Sulamayı Başlat", "action": "navigate", "target": "success" }
                    ]
                },
                "success": {
                    "navigation_title": "İşlem Tamam",
                    "layout": [
                        { "type": "text", "text": "✅ Sulama Başlatıldı", "size": "large" },
                        { "type": "card", "title": "Su Akışı Aktif", "desc": "Belirtilen süre boyunca vana açık tutulacak." },
                        { "type": "button", "label": "Ana Sayfaya Dön", "action": "navigate", "target": "main" }
                    ]
                }
            }
        elif any(w in idea_lower for w in ["pet", "hayvan", "köpek", "kedi", "veteriner"]):
            app_name = "PetCare"
            primary_color = "#8b5cf6"
            screens = {
                "main": {
                    "navigation_title": "Dostum",
                    "layout": [
                        { "type": "text", "text": "🐶 Evcil Hayvan Durumu", "size": "large" },
                        { "type": "chart", "chart_type": "ring", "value": 75, "label": "Günlük Aktivite" },
                        { "type": "card", "title": "Sağlık & Beslenme", "desc": "Bugünkü kalori hedefine ulaşıldı. Kuru mama azaldı." },
                        { "type": "button", "label": "Mama Gönderimine Git", "action": "navigate", "target": "feed" }
                    ]
                },
                "feed": {
                    "navigation_title": "Mama Gönder",
                    "layout": [
                        { "type": "text", "text": "🍖 Otomatik Mama Kabı", "size": "medium" },
                        { "type": "input", "placeholder": "Mama Gramajı (gr)", "input_type": "number" },
                        { "type": "card", "title": "Mama Kabı Durumu", "desc": "Hazne Doluluk Oranı: %30" },
                        { "type": "button", "label": "Porsiyon Gönder", "action": "navigate", "target": "success" }
                    ]
                },
                "success": {
                    "navigation_title": "Gönderildi",
                    "layout": [
                        { "type": "text", "text": "🎉 Mama Döküldü!", "size": "large" },
                        { "type": "card", "title": "Afiyet Olsun", "desc": "Mama kabına başarıyla porsiyon gönderildi." },
                        { "type": "button", "label": "Ana Sayfaya Dön", "action": "navigate", "target": "main" }
                    ]
                }
            }
        elif any(w in idea_lower for w in ["eğitim", "okul", "öğrenci", "ders", "kurs", "akademi"]):
            app_name = "EduAI"
            primary_color = "#3b82f6"
            screens = {
                "main": {
                    "navigation_title": "Eğitim Paneli",
                    "layout": [
                        { "type": "text", "text": "📚 AI Kişisel Mentör", "size": "large" },
                        { "type": "chart", "chart_type": "ring", "value": 94, "label": "Haftalık Başarı" },
                        { "type": "card", "title": "Sıradaki Ders", "desc": "Python Nesne Yönelimli Programlama (OOP)" },
                        { "type": "button", "label": "Ders Çalışmaya Başla", "action": "navigate", "target": "lesson" }
                    ]
                },
                "lesson": {
                    "navigation_title": "Python OOP",
                    "layout": [
                        { "type": "text", "text": "📝 Python Sınıf Egzersizi", "size": "medium" },
                        { "type": "input", "placeholder": "Kodunu buraya yaz...", "input_type": "text" },
                        { "type": "card", "title": "Egzersiz Sorusu", "desc": "Bir 'Car' sınıfı oluşturup 'speed' niteliği ekleyin." },
                        { "type": "button", "label": "Kodu Test Et", "action": "navigate", "target": "success" }
                    ]
                },
                "success": {
                    "navigation_title": "Harika!",
                    "layout": [
                        { "type": "text", "text": "🔥 Tebrikler, Doğru!", "size": "large" },
                        { "type": "card", "title": "AI Mentor Raporu", "desc": "Sınıf yapısını kusursuz tasarladın. +20 Puan kazandın." },
                        { "type": "button", "label": "Ana Sayfaya Dön", "action": "navigate", "target": "main" }
                    ]
                }
            }
        elif any(w in idea_lower for w in ["otel", "rezervasyon", "tatil", "seyahat", "bilet"]):
            app_name = "Bookify"
            primary_color = "#f59e0b"
            screens = {
                "main": {
                    "navigation_title": "Gezgin",
                    "layout": [
                        { "type": "text", "text": "✈️ Seyahat Asistanı", "size": "large" },
                        { "type": "card", "title": "Yaklaşan Seyahat", "desc": "Antalya Tatili (3 Gün Sonra)" },
                        { "type": "list", "items": ["Hotel Sun Queen - Standart Oda", "Uçak Bileti - TK408", "Müze Kart Giriş Hakkı"] },
                        { "type": "button", "label": "Yeni Rezervasyon Yap", "action": "navigate", "target": "book" }
                    ]
                },
                "book": {
                    "navigation_title": "Arama Yap",
                    "layout": [
                        { "type": "text", "text": "🔍 Otel veya Bilet Bul", "size": "medium" },
                        { "type": "input", "placeholder": "Gideceğiniz Şehir", "input_type": "text" },
                        { "type": "input", "placeholder": "Kişi Sayısı", "input_type": "number" },
                        { "type": "button", "label": "Fiyatları Listele", "action": "navigate", "target": "success" }
                    ]
                },
                "success": {
                    "navigation_title": "Rezervasyon Alındı",
                    "layout": [
                        { "type": "text", "text": "🎟️ Biletiniz Hazır!", "size": "large" },
                        { "type": "card", "title": "İşlem Başarılı", "desc": "Antalya seyahat paketiniz onaylandı. QR kodunuz üretildi." },
                        { "type": "button", "label": "Ana Sayfaya Dön", "action": "navigate", "target": "main" }
                    ]
                }
            }
        elif any(w in idea_lower for w in ["sağlık", "diyet", "spor", "fit", "hastane", "doktor", "ilaç"]):
            app_name = "LifeFit"
            primary_color = "#10b981"
            screens = {
                "main": {
                    "navigation_title": "Sağlığım",
                    "layout": [
                        { "type": "text", "text": "❤️ Kalp ve Egzersiz", "size": "large" },
                        { "type": "chart", "chart_type": "ring", "value": 68, "label": "Günlük Adım Oranı" },
                        { "type": "card", "title": "Bugünkü İlerleme", "desc": "8.420 Adım Atıldı. 400 Kalori Yakıldı." },
                        { "type": "button", "label": "Egzersiz Kaydet", "action": "navigate", "target": "log" }
                    ]
                },
                "log": {
                    "navigation_title": "Egzersiz Ekle",
                    "layout": [
                        { "type": "text", "text": "🏋️ Egzersiz Detayları", "size": "medium" },
                        { "type": "input", "placeholder": "Egzersiz Adı (Örn: Koşu)", "input_type": "text" },
                        { "type": "input", "placeholder": "Süre (Dakika)", "input_type": "number" },
                        { "type": "button", "label": "Kaydet ve Analiz Et", "action": "navigate", "target": "success" }
                    ]
                },
                "success": {
                    "navigation_title": "Kaydedildi",
                    "layout": [
                        { "type": "text", "text": "🔥 Egzersiz Tamam!", "size": "large" },
                        { "type": "card", "title": "AI Analiz Sonucu", "desc": "Metabolizmanız %12 hızlandı. Günlük adım hedefi güncellendi." },
                        { "type": "button", "label": "Ana Sayfaya Dön", "action": "navigate", "target": "main" }
                    ]
                }
            }
        elif any(w in idea_lower for w in ["yemek", "restoran", "kurye", "sipariş", "mutfak"]):
            app_name = "QuickBite"
            primary_color = "#ef4444"
            screens = {
                "main": {
                    "navigation_title": "Yemek Siparişi",
                    "layout": [
                        { "type": "text", "text": "🍔 Hızlı AI Mutfağı", "size": "large" },
                        { "type": "card", "title": "Aktif Sipariş", "desc": "Gurme Burger Menüsü hazırlanıyor." },
                        { "type": "list", "items": ["1x Gurme Burger", "1x Patates Cipsi", "1x Coca Cola Zero"] },
                        { "type": "button", "label": "Kurye Konumunu Takip Et", "action": "navigate", "target": "track" }
                    ]
                },
                "track": {
                    "navigation_title": "Kurye Takibi",
                    "layout": [
                        { "type": "text", "text": "🚴 Kurye Yolda", "size": "medium" },
                        { "type": "card", "title": "Teslimat Durumu", "desc": "Kurye Ahmet yola çıktı. Tahmini varış: 2 dk." },
                        { "type": "button", "label": "Temassız Teslimat Onayı", "action": "navigate", "target": "success" }
                    ]
                },
                "success": {
                    "navigation_title": "Teslim Edildi",
                    "layout": [
                        { "type": "text", "text": "🎉 Afiyet Olsun!", "size": "large" },
                        { "type": "card", "title": "Sipariş Tamamlandı", "desc": "Yemek teslim edildi. Lütfen restoranı puanlayın." },
                        { "type": "button", "label": "Ana Sayfaya Dön", "action": "navigate", "target": "main" }
                    ]
                }
            }
        elif any(w in idea_lower for w in ["ticaret", "market", "satış", "dükkan", "e-ticaret"]):
            app_name = "B2BStore"
            primary_color = "#6366f1"
            screens = {
                "main": {
                    "navigation_title": "Yönetim Paneli",
                    "layout": [
                        { "type": "text", "text": "🛒 Akıllı Mağaza Durumu", "size": "large" },
                        { "type": "card", "title": "Bugünkü Satış", "desc": "12 sipariş alındı. Toplam ciro: $240.00" },
                        { "type": "button", "label": "Hızlı Ürün Ekle", "action": "navigate", "target": "add_product" }
                    ]
                },
                "add_product": {
                    "navigation_title": "Ürün Ekle",
                    "layout": [
                        { "type": "text", "text": "➕ Yeni Ürün Bilgisi", "size": "medium" },
                        { "type": "input", "placeholder": "Ürün Adı", "input_type": "text" },
                        { "type": "input", "placeholder": "Fiyat ($)", "input_type": "number" },
                        { "type": "button", "label": "AI ile Açıklama Yaz ve Kaydet", "action": "navigate", "target": "success" }
                    ]
                },
                "success": {
                    "navigation_title": "Ürün Kaydedildi",
                    "layout": [
                        { "type": "text", "text": "🚀 Ürün Mağazada!", "size": "large" },
                        { "type": "card", "title": "AI Açıklaması Hazır", "desc": "Yapay zeka SEO uyumlu ürün açıklamasını otomatik oluşturdu." },
                        { "type": "button", "label": "Ana Sayfaya Dön", "action": "navigate", "target": "main" }
                    ]
                }
            }
        else:
            app_name = f"{kw_title}AI"
            primary_color = "#ec4899"
            screens = {
                "main": {
                    "navigation_title": "Dashboard",
                    "layout": [
                        { "type": "text", "text": f"🤖 {kw_title} AI Platformu", "size": "large" },
                        { "type": "chart", "chart_type": "ring", "value": 92, "label": "Ajan Hazırlık Skoru" },
                        { "type": "card", "title": "Sistem Sağlığı", "desc": f"Tüm otonom {main_kw} akışları optimize edildi." },
                        { "type": "button", "label": "Ajan Görevini Tetikle", "action": "navigate", "target": "trigger" }
                    ]
                },
                "trigger": {
                    "navigation_title": "Ajan Tetikle",
                    "layout": [
                        { "type": "text", "text": "⚡ Ajan Parametreleri", "size": "medium" },
                        { "type": "input", "placeholder": "Görev Hedefi", "input_type": "text" },
                        { "type": "button", "label": "Orkestrasyonu Başlat", "action": "navigate", "target": "success" }
                    ]
                },
                "success": {
                    "navigation_title": "Başarı",
                    "layout": [
                        { "type": "text", "text": "🚀 Ajanlar Başlatıldı!", "size": "large" },
                        { "type": "card", "title": "Görev Dağıtıldı", "desc": "Otonom iş akışları arka planda yürütülüyor." },
                        { "type": "button", "label": "Ana Sayfaya Dön", "action": "navigate", "target": "main" }
                    ]
                }
            }
        return {
            "app_name": app_name,
            "branding": {
                "primary_color": primary_color,
                "dark_mode": True
            },
            "initial_screen": "main",
            "screens": screens
        }

