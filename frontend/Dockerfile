# Python 3.11 slim imajını kullan
FROM python:3.11-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gereksinimleri kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Port 8501'i aç (Streamlit default portu)
EXPOSE 8501

# Streamlit'i başlat
CMD ["streamlit", "run", "streamlit_app.py", "--server.address=0.0.0.0"]
