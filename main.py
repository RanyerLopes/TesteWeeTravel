from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

class Proposta(BaseModel):
    proposta: str
    cliente: str
    destino: str
    periodo: str
    consultor: str

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
    return response.json()
