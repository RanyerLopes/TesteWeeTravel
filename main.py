from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os

# Instância do FastAPI
app = FastAPI()

# Habilitar CORS (libera o acesso ao backend para o frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, use ["http://localhost:3000"] ou domínio do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuração do Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://npeqhqhmnnjczkfcxeoj.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5wZXFocWhtbm5qY3prZmN4ZW9qIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTM3ODc1OTQsImV4cCI6MjA2OTM2MzU5NH0.tdwXp57XJ7io34IWQ1R350uhfhOXswKc2lAoIr9f02A")

# Modelo de dados
class Proposta(BaseModel):
    proposta: str
    cliente: str
    destino: str
    periodo: str
    consultor: str

# Rota para registrar proposta
@app.post("/registrar-proposta")
def registrar_proposta(data: Proposta):
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/propostas",
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=representation"
        },
        json=data.dict()
    )

    if response.status_code == 201:
        return {"message": "Proposta registrada com sucesso!", "data": response.json()}
    else:
        return {
            "error": response.text,
            "status_code": response.status_code,
            "message": "Erro ao registrar proposta"
        }
