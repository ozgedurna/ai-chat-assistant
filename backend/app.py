"""
AI Chat Assistant Backend
FastAPI application with Google Gemini integration
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
import os
from typing import List, Optional
from datetime import datetime

app = FastAPI(
    title="AI Chat Assistant API",
    description="Google Gemini destekli AI sohbet asistanı",
    version="1.0.0"
)

# CORS ayarları - Frontend'in backend'e erişmesi için
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Gemini API anahtarını ortam değişkeninden al
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Pydantic modelleri (veri yapıları)
class Message(BaseModel):
    role: str
    content: str
    timestamp: Optional[str] = None

class ChatRequest(BaseModel):
    message: str
    chat_history: Optional[List[Message]] = []
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 1000

class ChatResponse(BaseModel):
    response: str
    timestamp: str
    model: str

class HealthResponse(BaseModel):
    status: str
    message: str
    timestamp: str

# API Endpoint'leri

@app.get("/", response_model=HealthResponse)
async def root():
    """Ana sayfa - sağlık kontrolü"""
    return HealthResponse(
        status="healthy",
        message="🚀 AI Chat Assistant API çalışıyor!",
        timestamp=datetime.now().isoformat()
    )

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Detaylı sağlık kontrolü"""
    api_configured = bool(GEMINI_API_KEY)
    return HealthResponse(
        status="healthy" if api_configured else "warning",
        message="✅ API Key yapılandırıldı" if api_configured else "⚠️ API Key bulunamadı",
        timestamp=datetime.now().isoformat()
    )

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Ana sohbet endpoint'i
    Mesaj gönder, AI cevap al
    """
    if not GEMINI_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="Gemini API key yapılandırılmamış. .env dosyasını kontrol edin."
        )
    
    try:
        # Gemini modelini başlat
        model = genai.GenerativeModel('gemini-pro')
        
        # Sohbet geçmişini hazırla
        history = []
        for msg in request.chat_history:
            history.append({
                "role": "user" if msg.role == "user" else "model",
                "parts": [msg.content]
            })
        
        # Sohbet oturumu başlat
        chat = model.start_chat(history=history)
        
        # AI'dan cevap al
        response = chat.send_message(
            request.message,
            generation_config=genai.types.GenerationConfig(
                temperature=request.temperature,
                max_output_tokens=request.max_tokens,
            )
        )
        
        return ChatResponse(
            response=response.text,
            timestamp=datetime.now().isoformat(),
            model="gemini-pro"
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"AI isteği başarısız: {str(e)}"
        )

@app.get("/models")
async def list_models():
    """Kullanılabilir modelleri listele"""
    if not GEMINI_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="API key yapılandırılmamış"
        )
    
    try:
        models = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                models.append({
                    "name": m.name,
                    "display_name": m.display_name,
                    "description": m.description
                })
        return {"models": models}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Modeller listelenemedi: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
