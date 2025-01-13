# Insider Web Test Automation Project

Bu proje, Insider'ın web sitesindeki kariyer sayfası ve QA pozisyonları için test otomasyonu içerir. Python ve Selenium WebDriver kullanılarak geliştirilmiştir.

## 🎯 Test Senaryoları

### 1. Kariyer Sayfası Testi
- Ana sayfaya git ve "Company" menüsünden "Careers" sayfasına eriş
- Careers sayfasındaki tüm bölümlerin görünür olduğunu kontrol et

### 2. QA İş İlanları Testi (Istanbul)
- QA Careers sayfasına git
- "See all QA jobs" butonuna tıkla
- Lokasyon olarak "Istanbul, Turkey" ve departman olarak "Quality Assurance" seç
- İş ilanlarının listelendiğini kontrol et

### 3. QA İş İlanı Detay Kontrolü
- QA Careers sayfasına git ve filtreleri uygula
- Listelenen iş ilanlarının:
  - Position: "Quality Assurance" içerdiğini
  - Department: "Quality Assurance" içerdiğini
  - Location: "Istanbul, Turkey" içerdiğini kontrol et

### 4. İş Başvuru Sayfası Yönlendirme Testi
- QA Careers sayfasına git ve filtreleri uygula
- Bir iş ilanının üzerine gel (hover)
- Çıkan "View Role" butonuna tıkla
- Lever Application formuna yönlendirildiğini doğrula

## 🛠️ Kullanılan Teknolojiler

- Python 3.13.0
- Selenium WebDriver
- Pytest
- Chrome WebDriver

## 📦 Gereksinimler

```txt
selenium==4.17.2
pytest==7.4.3
pytest-html==4.1.1
webdriver_manager==4.0.1
```

## 🚀 Kurulum

1. Projeyi klonlayın:
```bash
git clone [repository-url]
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

## 🎮 Testleri Çalıştırma

Tüm testleri çalıştırmak için:
```bash
pytest tests/test_home_page.py -v
```

Belirli bir testi çalıştırmak için:
```bash
pytest tests/test_home_page.py::test_careers_page_sections -v
pytest tests/test_home_page.py::test_qa_jobs_istanbul -v
pytest tests/test_home_page.py::test_qa_jobs_details -v
pytest tests/test_home_page.py::test_qa_job_application_redirect -v
```

## 📁 Proje Yapısı

```
MEHMET_ASLANTAS.QA/
├── pages/
│   ├── base_page.py       # Temel sayfa fonksiyonları
│   ├── home_page.py       # Ana sayfa işlemleri
│   ├── careers_page.py    # Kariyer sayfası işlemleri
│   └── qa_jobs_page.py    # QA iş ilanları sayfası işlemleri
├── tests/
│   ├── conftest.py        # Pytest konfigürasyonu
│   └── test_home_page.py  # Test senaryoları
├── requirements.txt       # Gerekli paketler
└── README.md             # Proje dokümantasyonu
```

## ✨ Özellikler

- Page Object Model (POM) tasarım deseni kullanıldı
- Explicit wait ile güvenilir element beklemeleri
- Detaylı hata ayıklama ve screenshot alma
- Temiz ve okunabilir kod yapısı
- Her senaryo için ayrı test fonksiyonları

## 👤 Yazar

Mehmet ASLANTAŞ
QA Engineer
