# 🎯 ADIM ADIM KURULUM REHBERİ

Bu rehber, projeyi sıfırdan başlatman için hazırlandı. Her adımı takip et! 🚀

## ✅ ÖN HAZIRLIK KONTROL LİSTESİ

Başlamadan önce bunların kurulu olduğundan emin ol:

- [ ] Docker Desktop yüklü ve **çalışıyor** (🐳 simgesi görev çubuğunda yeşil olmalı)
- [ ] VS Code yüklü
- [ ] Git yüklü
- [ ] Gemini API Key aldın (Google AI Studio'dan)

## 📥 ADIM 1: PROJEYİ İNDİR

### Yöntem A: Git ile (Önerilen)

```bash
# Terminal'i aç (Windows: cmd veya PowerShell, Mac: Terminal)
cd Desktop
git clone <repo-url>
cd ai-chat-assistant
```

### Yöntem B: ZIP İndirme

1. GitHub'dan projeyi ZIP olarak indir
2. ZIP'i masaüstüne çıkar
3. Klasör adı `ai-chat-assistant` olmalı

## 💻 ADIM 2: VS CODE'DA AÇ

```bash
# Proje klasörünün içinde şu komutu çalıştır:
code .
```

**veya** VS Code'u aç ve:
1. File > Open Folder
2. `ai-chat-assistant` klasörünü seç
3. Open'a tıkla

## 🔑 ADIM 3: API KEY'İNİ AYARLA

### 3.1 `.env` dosyası oluştur

VS Code'da:
1. Sol panelde `.env.example` dosyasını bul
2. Sağ tık > Copy
3. Aynı yere Paste
4. Dosya adını `.env` yap (uzantısız)

### 3.2 API Key'i ekle

`.env` dosyasını aç ve düzenle:

```bash
GEMINI_API_KEY=AIzaSyC_senin_asıl_api_keyin_buraya
```

**ÖNEMLİ:** 
- `your_api_key_here` kısmını SİL
- Google AI Studio'dan aldığın gerçek API key'i YAPIŞTIR
- `AIzaSy` ile başlayan uzun bir kod olmalı

### 3.3 Kaydet

- Windows: `Ctrl + S`
- Mac: `Cmd + S`

## 🐳 ADIM 4: DOCKER DESKTOP'I KONTROL ET

1. Docker Desktop'ı aç
2. Sol altta 🐳 simgesi **yeşil** olmalı
3. "Docker Desktop is running" yazısını görmeli

**Eğer çalışmıyorsa:**
- Windows: Başlat menüsünden Docker Desktop'ı çalıştır
- Mac: Applications'dan Docker'ı çalıştır

## 🚀 ADIM 5: PROJEYI BAŞLAT

VS Code'da terminal aç:
- Üst menüden: `Terminal > New Terminal`
- veya kısayol: `Ctrl + ` (backtick)

Terminal'de şu komutu çalıştır:

```bash
docker-compose up --build
```

### Ne Olacak?

1. 📦 Docker, gerekli tüm paketleri indirecek (ilk seferde biraz sürer)
2. 🏗️ Backend ve Frontend container'ları oluşturulacak
3. ✅ Her iki servis de başlayacak
4. 📝 Loglar akacak (bu normal!)

### Bekle...

Şu mesajları görene kadar bekle:

```
backend  | INFO:     Uvicorn running on http://0.0.0.0:8000
frontend | You can now view your Streamlit app in your browser.
```

## 🌐 ADIM 6: TARAYICIDA AÇ

Tarayıcını aç ve bu adreslere git:

1. **Frontend (Ana Uygulama):**
   ```
   http://localhost:8501
   ```
   👆 Burada AI ile sohbet edeceksin!

2. **Backend API Docs:**
   ```
   http://localhost:8000/docs
   ```
   👆 API'nin interaktif dokümantasyonu

3. **Health Check:**
   ```
   http://localhost:8000/health
   ```
   👆 API'nin çalışıp çalışmadığını kontrol et

## ✨ ADIM 7: TEST ET

1. Frontend'te (localhost:8501) mesaj yaz
2. "Merhaba, nasılsın?" gibi basit bir şey dene
3. Gönder'e bas
4. AI'ın cevap vermesini bekle

**Başarılı!** 🎉 AI'ın cevap verdiğini görüyorsan her şey çalışıyor!

## 🛠️ ADIM 8: KODLARI DÜZENLEMEYİ ÖĞREN

### Backend'i Düzenle

1. VS Code'da `backend/app.py` dosyasını aç
2. Bir değişiklik yap (örn: mesaj metni değiştir)
3. Kaydet (`Ctrl + S`)
4. Docker otomatik yeniden yükler (hot reload)
5. Tarayıcıyı yenile ve test et

### Frontend'i Düzenle

1. VS Code'da `frontend/streamlit_app.py` dosyasını aç
2. Bir değişiklik yap (örn: başlık değiştir)
3. Kaydet (`Ctrl + S`)
4. Streamlit otomatik yeniden yükler
5. Tarayıcıda değişikliği göreceksin

## 🛑 ADIM 9: DURDURMAK İSTERSEN

Terminal'de:
- `Ctrl + C` tuşlarına bas

veya Docker Desktop'tan durdur.

Tekrar başlatmak için:

```bash
docker-compose up
```

(artık `--build` bayrağına gerek yok, zaten oluşturuldu)

## 🐛 SORUN ÇÖZME

### "Port already in use" Hatası

Port zaten kullanılıyorsa:

```bash
# Docker'ı durdur ve yeniden başlat
docker-compose down
docker-compose up
```

### "API Key not configured" Hatası

1. `.env` dosyasının var olduğunu kontrol et
2. İçinde doğru API key olduğunu kontrol et
3. Docker'ı yeniden başlat: `docker-compose restart`

### Docker çalışmıyor

1. Docker Desktop'ın açık olduğundan emin ol
2. Bilgisayarı yeniden başlat
3. Docker Desktop'ı yeniden yükle

### Frontend Backend'e bağlanamıyor

1. Backend'in çalıştığını kontrol et: http://localhost:8000/health
2. Her iki container'ın da çalıştığını kontrol et:
   ```bash
   docker ps
   ```

## 📚 SONRAKİ ADIMLAR

Artık projen çalışıyor! Şimdi ne yapabilirsin:

1. ✏️ Kodları incele ve öğren
2. 🎨 UI'ı özelleştir (renkler, metinler)
3. 🤖 Yeni AI özellikleri ekle
4. 📊 Yeni sayfalar ekle
5. 🚀 GitHub'a yükle

## 🎓 ÖĞRENME KAYNAKLARI

- **FastAPI:** https://fastapi.tiangolo.com/tutorial/
- **Streamlit:** https://docs.streamlit.io/get-started
- **Docker:** https://docs.docker.com/get-started/
- **Gemini API:** https://ai.google.dev/tutorials/python_quickstart

## 💡 İPUÇLARI

1. **VS Code Terminal Kullan:** Her şeyi VS Code içinden yap
2. **Docker Logs:** `docker-compose logs -f` ile canlı logları izle
3. **Hot Reload:** Kod değişiklikleri otomatik yüklenir
4. **Git Kullan:** Her önemli değişiklikten sonra commit at

## 🆘 YARDIM

Takıldığın bir yer olursa:

1. README.md'yi oku
2. Docker loglarını kontrol et
3. GitHub'da issue aç
4. Webinar topluluğuna sor

---

**Başarılar!** 🎉 Artık kendi AI uygulamanı geliştirmeye hazırsın!
