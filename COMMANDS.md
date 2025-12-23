# ⚡ HIZLI BAŞLANGIÇ KOMUTLARI

## 🚀 Projeyi İlk Defa Başlatmak

```bash
# 1. Projeyi indir (Git ile)
git clone <repo-url>
cd ai-chat-assistant

# 2. .env dosyası oluştur
cp .env.example .env
# Sonra .env dosyasını düzenle ve API key'ini ekle

# 3. VS Code'da aç
code .

# 4. Docker ile başlat
docker-compose up --build
```

## 🔄 Normal Başlatma (2. ve sonraki seferler)

```bash
# Proje klasörüne git
cd ai-chat-assistant

# Docker'ı başlat (build'e gerek yok)
docker-compose up
```

## 🛑 Durdurmak

```bash
# Terminal'de Ctrl + C
# veya
docker-compose down
```

## 🔍 Durum Kontrolü

```bash
# Çalışan container'ları gör
docker ps

# Logları takip et
docker-compose logs -f

# Backend sağlık kontrolü
curl http://localhost:8000/health

# Frontend aç (tarayıcıda)
# http://localhost:8501
```

## 🔨 Geliştirme Komutları

```bash
# Backend'i yeniden başlat
docker-compose restart backend

# Frontend'i yeniden başlat
docker-compose restart frontend

# Her şeyi yeniden oluştur
docker-compose down
docker-compose up --build

# Container'ların içine gir
docker exec -it ai-chat-backend bash
docker exec -it ai-chat-frontend bash
```

## 🗑️ Temizlik

```bash
# Container'ları sil
docker-compose down

# Volume'leri de sil
docker-compose down -v

# Image'leri de sil
docker-compose down --rmi all

# Tüm Docker cache'ini temizle
docker system prune -a
```

## 📦 Git Komutları

```bash
# İlk kurulum
git init
git add .
git commit -m "Initial commit"
git remote add origin <github-url>
git push -u origin main

# Değişiklikleri kaydet
git status
git add .
git commit -m "feat: Açıklama"
git push

# En son değişiklikleri al
git pull
```

## 🔧 Python (Docker olmadan test)

```bash
# Virtual environment oluştur
python -m venv venv

# Aktif et
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Backend çalıştır
cd backend
pip install -r requirements.txt
uvicorn app:app --reload

# Frontend çalıştır (yeni terminal)
cd frontend
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## 🌐 URL'ler

```bash
Frontend:    http://localhost:8501
Backend:     http://localhost:8000
API Docs:    http://localhost:8000/docs
Health:      http://localhost:8000/health
```

## 📝 Dosya Yolları

```bash
.
├── backend/
│   └── app.py              # Backend kodu
├── frontend/
│   └── streamlit_app.py    # Frontend kodu
├── .env                    # API key'ler (sakla!)
├── docker-compose.yml      # Docker config
└── README.md               # Dokümantasyon
```

## 💡 Hızlı Test

```bash
# Backend test
curl http://localhost:8000/health

# API'ye mesaj gönder
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Merhaba!"}'

# Logları göster
docker-compose logs backend
docker-compose logs frontend
```

## 🚨 Acil Durum Komutları

```bash
# Her şeyi durdur
docker stop $(docker ps -aq)

# Her şeyi sil ve baştan başla
docker-compose down -v
rm -rf __pycache__
docker-compose up --build

# Port takılı kaldıysa
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Mac/Linux:
lsof -ti:8000 | xargs kill -9
```

## 🎯 Yararlı Kısayollar

```bash
# .bashrc veya .zshrc dosyana ekle:

alias dc='docker-compose'
alias dcu='docker-compose up'
alias dcb='docker-compose up --build'
alias dcd='docker-compose down'
alias dcl='docker-compose logs -f'
alias dps='docker ps'

# Sonra kullan:
dcb  # docker-compose up --build yerine
dcd  # docker-compose down yerine
```

---

**Not:** Komutları kopyala-yapıştır yapabilirsin! 📋
