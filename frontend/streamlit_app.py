"""
AI Chat Assistant Frontend
Streamlit UI for chatting with Gemini AI
"""

import streamlit as st
import requests
from datetime import datetime
import time

# Sayfa yapılandırması
st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Backend API URL'i
BACKEND_URL = "http://backend:8000"

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #e3f2fd;
        margin-left: 2rem;
    }
    .assistant-message {
        background-color: #f5f5f5;
        margin-right: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Session state'i başlat
if "messages" not in st.session_state:
    st.session_state.messages = []

if "backend_status" not in st.session_state:
    st.session_state.backend_status = "checking"

# Backend sağlık kontrolü
def check_backend_health():
    try:
        response = requests.get(f"{BACKEND_URL}/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get("status"), data.get("message")
        return "error", "Backend'e ulaşılamıyor"
    except Exception as e:
        return "error", f"Bağlantı hatası: {str(e)}"

# Mesaj gönder
def send_message(message, temperature, max_tokens):
    try:
        # Sohbet geçmişini hazırla
        chat_history = [
            {"role": msg["role"], "content": msg["content"]} 
            for msg in st.session_state.messages
        ]
        
        # API'ye istek gönder
        response = requests.post(
            f"{BACKEND_URL}/chat",
            json={
                "message": message,
                "chat_history": chat_history,
                "temperature": temperature,
                "max_tokens": max_tokens
            },
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            return data.get("response"), None
        else:
            return None, f"API Hatası: {response.status_code}"
    
    except Exception as e:
        return None, f"İstek hatası: {str(e)}"

# Ana başlık
st.markdown('<h1 class="main-header">🤖 AI Chat Assistant</h1>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar - Ayarlar
with st.sidebar:
    st.header("⚙️ Ayarlar")
    
    # Backend durumu
    status, message = check_backend_health()
    if status == "healthy":
        st.success(f"✅ {message}")
    else:
        st.error(f"❌ {message}")
    
    st.markdown("---")
    
    # AI Parametreleri
    st.subheader("🎛️ AI Parametreleri")
    
    temperature = st.slider(
        "Temperature (Yaratıcılık)",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1,
        help="Düşük değer: Daha tutarlı, Yüksek değer: Daha yaratıcı"
    )
    
    max_tokens = st.slider(
        "Maksimum Token (Cevap Uzunluğu)",
        min_value=100,
        max_value=2000,
        value=1000,
        step=100,
        help="AI'ın üretebileceği maksimum kelime sayısı"
    )
    
    st.markdown("---")
    
    # Sohbet geçmişini temizle
    if st.button("🗑️ Sohbeti Temizle"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    
    # Bilgi
    with st.expander("ℹ️ Hakkında"):
        st.write("""
        **AI Chat Assistant**
        
        Bu uygulama Görkem Sayer'in webinar'ında 
        öğrenilen teknolojilerle yapılmıştır:
        
        - 🚀 FastAPI
        - 🎨 Streamlit
        - 🐳 Docker
        - 🤖 Google Gemini AI
        
        **Kullanım:**
        1. Sağ tarafta mesaj yazın
        2. Gönder'e basın
        3. AI'ın cevabını görün
        
        **İpucu:** Temperature değerini 
        ayarlayarak AI'ın cevap stilini 
        değiştirebilirsiniz!
        """)

# Ana alan - Chat
st.subheader("💬 Sohbet")

# Mesaj geçmişini göster
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong>👤 Sen:</strong><br>
                {message["content"]}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message assistant-message">
                <strong>🤖 AI Assistant:</strong><br>
                {message["content"]}
            </div>
            """, unsafe_allow_html=True)

# Mesaj input alanı
st.markdown("---")
col1, col2 = st.columns([6, 1])

with col1:
    user_input = st.text_input(
        "Mesajınızı yazın:",
        key="user_input",
        placeholder="AI'a bir şey sorun...",
        label_visibility="collapsed"
    )

with col2:
    send_button = st.button("📤 Gönder", use_container_width=True)

# Mesaj gönderme işlemi
if send_button and user_input:
    # Kullanıcı mesajını ekle
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "timestamp": datetime.now().isoformat()
    })
    
    # Loading göster
    with st.spinner("🤔 AI düşünüyor..."):
        response, error = send_message(user_input, temperature, max_tokens)
    
    if error:
        st.error(f"❌ Hata: {error}")
    else:
        # AI cevabını ekle
        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "timestamp": datetime.now().isoformat()
        })
    
    # Sayfayı yenile
    st.rerun()

# Sayfa altı
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 0.8rem;'>
    Made with ❤️ using FastAPI, Streamlit & Docker | 
    Powered by Google Gemini AI
</div>
""", unsafe_allow_html=True)
