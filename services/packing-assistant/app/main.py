from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schema import PacklistRequest, PacklistResponse
from app.ai_generator import generate_ai_packlist
import os
import google.generativeai as genai

# FastAPI-Instanz
app = FastAPI(
    title="Smart Packing Assistant",
    description="Erstellt Packlisten basierend auf Wetter, Dauer und Zielort (Dummy-Wetterdaten).",
    version="1.0.0"
)

# CORS-Middleware erlauben (für Frontend-Kommunikation)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Gemini API-Schlüssel initialisieren
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Health-Check-Endpunkt
@app.get("/healthz")
def health_check():
    return {
        "ok": True,
        "service": "packing-assistant",
        "model": "gemini-1.5-flash"
    }

# Packliste generieren
@app.post("/v1/packlist", response_model=PacklistResponse)
async def generate_packlist(request: PacklistRequest):
    try:
        return generate_ai_packlist(
            destination=request.destination,
            days=request.duration_days,
            activities=request.activities
        )
    except Exception as e:
        return {
            "destination": request.destination,
            "summary": f"Fehler bei Generierung: {str(e)}",
            "items": []
        }
