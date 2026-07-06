# 🚀 Multi-Agent Startup Incubator

Multi-Agent Startup Incubator (Çoklu Ajanlı Girişim Kuluçka Merkezi), kullanıcılardan gelen ham girişim fikirlerini alan; Pazar Araştırması, Finans Planlaması ve Teknik Mimari alanlarında uzmanlaşmış bağımsız yapay zeka ajanlarını orkestre eden ve ortak hafıza (shared memory) kullanarak kapsamlı bir girişim raporu ve yol haritası üreten modern bir web uygulamasıdır.

Bu proje, **Yapay Zeka ve Teknoloji Akademisi 2026 Bootcamp** kapsamında geliştirilmiştir.

---

## 👥 Ekip ve Roller
* **Asil Doğukan Samay** - Product Owner (PO)
* *(Diğer ekip üyeleri buraya eklenecektir)* - Scrum Master & Developers

---

## ✨ Özellikler
* **🧠 Çoklu Ajan Orkestrasyonu (Multi-Agent):** Bağımsız 3 ajan (Pazar Analisti, Finans Mentörü ve Yazılım Mimarı) sıralı bir iş akışı halinde çalışır.
* **💾 Ortak Hafıza (Shared Memory):** Her ajan kendisinden önceki ajanın kararlarını okur ve analizini buna göre şekillendirir.
* **💻 Canlı Ajan Konsolu (Terminal):** Arayüzde ajanların arka planda birbirleriyle nasıl haberleştiğini ve hangi ortak hafızayı kullandığını gösteren simüle edilmiş canlı terminal ekranı.
* **📊 SWOT & Pazar Analizi:** Hedef kitle, trendler, rakipler ve SWOT analizinin grafiksel sunumu.
* **💰 Gelir & Maliyet Modellemesi:** Gelir modelleri, fiyatlandırma paketleri ve operasyonel gider tabloları.
* **🏗️ Yazılım Mimarisi Tasarımı:** En uygun teknoloji yığını (tech stack), ilişkisel veritabanı şeması ve kritik API uç noktaları.
* **🎨 Premium Tasarım:** Yarı saydam cam efekti (glassmorphism), neon gradyan geçişleri ve koyu tema (dark mode) kullanan modern kullanıcı arayüzü.

---

## 🛠️ Teknoloji Yığını (Tech Stack)
* **Frontend:** HTML5, CSS3 (Vanilla Glassmorphic Design), JavaScript (ES6+), Marked.js (Markdown parser)
* **Backend:** Python 3.10+, FastAPI (Asenkron API Framework), Uvicorn
* **Yapay Zeka:** Gemini 1.5 Flash (google-generativeai SDK)
* **Test:** Python Unittest (Test Kapsamı: %100 Ajan ve Hafıza mantığı)

---

## 🚀 Kurulum ve Çalıştırma

Uygulamayı yerel bilgisayarınızda çalıştırmak için iki yöntem bulunmaktadır:

### Yöntem A: Tek Tıkla Kolay Başlatma (Tavsiye Edilen)
Proje dizininde yer alan **`run_app.bat`** dosyasına çift tıklamanız yeterlidir. Bu işlem:
1. Sisteminizde Python olup olmadığını kontrol eder.
2. Sanal ortamı (`venv`) otomatik olarak oluşturur.
3. Gerekli paketleri (`requirements.txt`) otomatik kurar.
4. Tarayıcınızda uygulamayı (`http://127.0.0.1:8000`) açar ve sunucuyu başlatır.

---

### Yöntem B: Manuel Kurulum
Manuel olarak çalıştırmak isterseniz aşağıdaki komutları sırayla çalıştırın:

```bash
# 1. Sanal Ortam Oluşturma ve Aktifleştirme
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows PowerShell için

# 2. Bağımlılıkların Yüklenmesi
pip install -r backend/requirements.txt

# 3. API Anahtarı Tanımlama
# Ana dizindeki .env dosyasını açıp kendi anahtarınızı ekleyin
# (Eğer anahtar yoksa, uygulama otomatik olarak simülasyon modunda çalışır)
GEMINI_API_KEY=your_gemini_api_key

# 4. Sunucuyu Başlatma
uvicorn backend.app.main:app --reload
```
Ardından tarayıcınızdan **`http://localhost:8000`** adresine gidin.

---

## 🧪 Birim Testlerinin Çalıştırılması
Yazılan ajan mantığı ve hafıza yönetim testlerini çalıştırmak için sanal ortam aktifken şu komutu kullanın:
```bash
python -m unittest backend.tests.test_agents
```
