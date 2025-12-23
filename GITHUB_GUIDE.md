# 📤 GITHUB'A YÜKLEME REHBERİ

Projenizi GitHub'a yüklemek için bu adımları takip edin!

## 🎯 ÖN HAZIRLIK

### GitHub Hesabı Oluştur

1. https://github.com adresine git
2. Sign Up'a tıkla
3. Email, şifre belirle
4. Hesabını onayla

### Git Kurulumu Kontrol

Terminal'de çalıştır:

```bash
git --version
```

Eğer hata alıyorsan, Git'i indir: https://git-scm.com/downloads

### Git Yapılandırması

İlk kez kullanıyorsan:

```bash
git config --global user.name "Senin Adın"
git config --global user.email "senin@email.com"
```

## 📦 ADIM ADIM YÜKLEME

### 1️⃣ GitHub'da Yeni Repo Oluştur

1. GitHub'da giriş yap
2. Sağ üstte `+` > `New repository`
3. Repository adı: `ai-chat-assistant`
4. Açıklama: `AI Chat Assistant built with FastAPI, Streamlit & Gemini`
5. Public veya Private seç
6. **❌ Initialize with README seçme** (zaten var)
7. `Create repository` butonuna tıkla

### 2️⃣ Projeyi Git'e Hazırla

VS Code'da terminal aç ve şu komutları çalıştır:

```bash
# Git repository'sini başlat
git init

# Tüm dosyaları staging'e ekle
git add .

# İlk commit'i oluştur
git commit -m "Initial commit: AI Chat Assistant with FastAPI, Streamlit and Gemini"
```

### 3️⃣ GitHub'a Bağlan

GitHub'dan kopyaladığın URL'i kullan (repo oluşturduktan sonra gösterilir):

```bash
# Origin ekle (URL'i kendi repona göre değiştir)
git remote add origin https://github.com/KULLANICI_ADIN/ai-chat-assistant.git

# Ana branch'i main olarak ayarla
git branch -M main

# GitHub'a push et
git push -u origin main
```

### 4️⃣ Kontrol Et

1. GitHub sayfanı yenile
2. Tüm dosyaları görmelisin
3. README.md otomatik görünecek

## ✅ İŞLEM TAMAMLANDI!

Artık projen GitHub'da! 🎉

Repo URL'in:
```
https://github.com/KULLANICI_ADIN/ai-chat-assistant
```

## 🔄 DEĞİŞİKLİKLERİ GÜNCELLEMEK

Kod değiştirdiğinde:

```bash
# Değişiklikleri kontrol et
git status

# Tüm değişiklikleri ekle
git add .

# Commit oluştur
git commit -m "feat: Yaptığın değişikliği açıkla"

# GitHub'a gönder
git push
```

## 📝 İYİ COMMIT MESAJLARI

Commit mesajları için bu formatı kullan:

```bash
git commit -m "feat: Yeni özellik eklendi"
git commit -m "fix: Hata düzeltildi"
git commit -m "docs: Dokümantasyon güncellendi"
git commit -m "style: Görsel değişiklikler"
git commit -m "refactor: Kod iyileştirmesi"
```

## 🎨 README'yi Güzelleştir

GitHub'da projen güzel görünsün! Şunları ekle:

### Badges Ekle

README.md'nin başına:

```markdown
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31-red.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)
```

### Ekran Görüntüsü Ekle

1. Uygulamanın ekran görüntüsünü al
2. `screenshots` klasörü oluştur
3. Resmi oraya koy
4. README'ye ekle:

```markdown
## 📸 Ekran Görüntüleri

![App Screenshot](screenshots/app.png)
```

### Demo Video Ekle

```markdown
## 🎥 Demo

[![Watch Demo](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)
```

## 🔒 GÜVENLİK ÖNEMLİ!

### ⚠️ .env Dosyası

**ASLA** `.env` dosyasını GitHub'a yükleme!

Kontrol et:
```bash
# .gitignore'da .env olmalı
cat .gitignore | grep .env
```

### API Key Sızdı mı?

Eğer yanlışlıkla API key'i yüklediysen:

1. **HEMEN** Google AI Studio'ya git
2. O API key'i SİL
3. Yeni bir API key oluştur
4. GitHub'da:
   ```bash
   git filter-branch --force --index-filter \
   "git rm --cached --ignore-unmatch .env" \
   --prune-empty --tag-name-filter cat -- --all
   
   git push origin --force --all
   ```

## 📊 GitHub Actions (Opsiyonel)

Otomatik test için `.github/workflows/test.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build with Docker Compose
        run: docker-compose build
```

## 🌟 REPO'YU GÜZELLEŞTİR

### Topics Ekle

GitHub repo sayfanda:
1. Sağ üstte ⚙️ (Settings) değil, Topics kısmını bul
2. Şunları ekle:
   - `fastapi`
   - `streamlit`
   - `docker`
   - `gemini-ai`
   - `ai-chatbot`
   - `python`

### About Kısmını Doldur

1. Repo ana sayfasında sağ üstte ⚙️
2. Description: Kısa açıklama yaz
3. Website: Eğer deploy ettiysen URL ekle
4. Topics: Yukarıdaki listeden ekle

### LICENSE Ekle

1. Repo ana sayfasında `Add file` > `Create new file`
2. Dosya adı: `LICENSE`
3. Sağda "Choose a license template"
4. MIT License'ı seç (en yaygın)
5. Commit et

## 🚀 DEPLOY (İleri Seviye)

Projeyi yayına almak için:

### Render.com (Ücretsiz)

1. https://render.com'a git
2. GitHub ile giriş yap
3. New > Web Service
4. Repo'nu seç
5. Environment variables ekle (GEMINI_API_KEY)
6. Deploy!

### Railway.app (Ücretsiz)

1. https://railway.app'a git
2. Deploy from GitHub
3. Repo'nu seç
4. Environment variables ekle
5. Deploy!

## 💡 PRO İPUÇLARI

1. **Branch Kullan:**
   ```bash
   git checkout -b feature/yeni-ozellik
   # Değişiklikleri yap
   git push origin feature/yeni-ozellik
   # GitHub'da Pull Request oluştur
   ```

2. **Sık Commit At:**
   - Her mantıklı değişiklikten sonra commit
   - Küçük commitler daha iyi

3. **README Güncel Tut:**
   - Yeni özellik ekledikçe güncelle
   - Ekran görüntüleri ekle

4. **Issues Kullan:**
   - Yapılacakları issue olarak aç
   - Commit'te `#issue_number` ile referans ver

## 🎓 GİT KOMUTLARI CHEAT SHEET

```bash
# Durum kontrol
git status

# Değişiklikleri gör
git diff

# Commit geçmişi
git log --oneline

# Geri al (dikkatli!)
git reset --hard HEAD

# Branch'ler arası geçiş
git checkout branch-name

# En son değişiklikleri çek
git pull

# Uzak repo'yu gör
git remote -v
```

## 🆘 YARDIM

### Git Hatası Aldıysan

```bash
# Önce pull et, sonra push
git pull origin main
git push origin main

# Conflict varsa
# Dosyaları düzenle, sonra:
git add .
git commit -m "fix: Merge conflict resolved"
git push
```

### GitHub Token (2FA)

GitHub şifre yerine token kullanıyorsa:

1. GitHub > Settings > Developer settings > Personal access tokens
2. Generate new token
3. Repo access ver
4. Token'ı kopyala
5. Git push'ta şifre yerine token'ı kullan

---

**Tebrikler!** 🎉 Artık projen GitHub'da ve herkese açık!

Projeyi paylaşırken şunu söyle:
"FastAPI, Streamlit ve Docker ile AI sohbet uygulaması yaptım! 🚀"

URL: `https://github.com/KULLANICI_ADIN/ai-chat-assistant`
