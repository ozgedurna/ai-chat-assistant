# 🤖 AI Chat Assistant

Webinar'da öğrendiklerinle yapılmış, FastAPI + Streamlit + Docker + Gemini AI kullanarak tam özellikli bir AI sohbet uygulaması.

## 📋 Gereksinimler

- ✅ Docker Desktop (yüklü ve çalışıyor olmalı)
- ✅ VS Code
- ✅ Git
- ✅ Gemini API Key (Google AI Studio'dan aldığın)

## 🚀 Kurulum Adımları

### 1️⃣ Projeyi VS Code'da Aç

```bash
# Terminal'i aç ve şu komutları çalıştır:
cd Desktop  # veya istediğin bir klasör
git clone <bu-repo-url>
cd ai-chat-assistant
code .  # VS Code'u açar
```

### 2️⃣ API Key'ini Ayarla

Proje klasöründe `.env` dosyası oluştur ve içine şunu yaz:

```
GEMINI_API_KEY=your_api_key_here
```

**ÖNEMLİ:** `your_api_key_here` yazan yere Google AI Studio'dan aldığın API key'i yapıştır!

### 3️⃣ Docker ile Çalıştır

VS Code'da yeni bir terminal aç (Terminal > New Terminal) ve şu komutu çalıştır:

```bash
docker-compose up --build
```

Bu komut:
- ✅ Backend API'yi başlatır (FastAPI) → http://localhost:8000
- ✅ Frontend'i başlatır (Streamlit) → http://localhost:8501

### 4️⃣ Uygulamayı Kullan

Tarayıcında şu adresleri aç:

- **Frontend (Streamlit):** http://localhost:8501
- **Backend API Docs:** http://localhost:8000/docs
- **Health Check:** http://localhost:8000/health

## 🛠️ VS Code'da Geliştirme

### Kodları Düzenle

1. **Backend'i düzenlemek için:** `backend/app.py` dosyasını aç
2. **Frontend'i düzenlemek için:** `frontend/streamlit_app.py` dosyasını aç
3. Değişiklikleri kaydet
4. Docker otomatik olarak yeniden yükler (hot reload)

### Docker'ı Durdur

Terminal'de `Ctrl + C` tuşlarına bas veya:

```bash
docker-compose down
```

### Logları Görüntüle

```bash
docker-compose logs -f
```

## 📁 Proje Yapısı

```
ai-chat-assistant/
├── backend/
│   ├── app.py              # FastAPI uygulaması
│   ├── requirements.txt    # Python bağımlılıkları
│   └── Dockerfile         # Backend Docker yapılandırması
├── frontend/
│   ├── streamlit_app.py   # Streamlit UI
│   ├── requirements.txt   # Python bağımlılıkları
│   └── Dockerfile        # Frontend Docker yapılandırması
├── docker-compose.yml     # Docker orchestration
├── .env                   # API anahtarların (GIT'E EKLEME!)
├── .gitignore            # Git ignore kuralları
└── README.md             # Bu dosya
```

## 🎯 Özellikler

- ✅ Google Gemini AI entegrasyonu
- ✅ Modern ve responsive UI (Streamlit)
- ✅ RESTful API (FastAPI)
- ✅ Docker ile kolay deployment
- ✅ Sohbet geçmişi
- ✅ Ayarlanabilir AI parametreleri (temperature, max tokens)
- ✅ API dokümantasyonu (Swagger/OpenAPI)

## 🐛 Sorun Giderme

### Docker çalışmıyor
```bash
# Docker Desktop'ın çalıştığından emin ol
# Ardından:
docker-compose down
docker-compose up --build
```

### Port zaten kullanımda
```bash
# Portları değiştir: docker-compose.yml dosyasında
# 8000 → 8001 ve 8501 → 8502
```

### API Key hatası
- `.env` dosyasının doğru yerde olduğundan emin ol
- API key'inin doğru olduğunu kontrol et
- Docker'ı yeniden başlat: `docker-compose restart`

## 📚 Kaynaklar

- [FastAPI Dokümantasyonu](https://fastapi.tiangolo.com/)
- [Streamlit Dokümantasyonu](https://docs.streamlit.io/)
- [Gemini API Dokümantasyonu](https://ai.google.dev/docs)
- [Docker Dokümantasyonu](https://docs.docker.com/)

## 🤝 Katkıda Bulun

1. Fork'la
2. Feature branch oluştur (`git checkout -b feature/amazing-feature`)
3. Commit'le (`git commit -m 'feat: Add amazing feature'`)
4. Push'la (`git push origin feature/amazing-feature`)
5. Pull Request aç

## 📝 Lisans

MIT License - istediğin gibi kullanabilirsin!

---

**Yapımcı:** Görkem Sayer Webinar'ından ilhamla ❤️
**Tarih:** 2024
