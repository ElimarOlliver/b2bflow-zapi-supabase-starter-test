import os
import requests
from dotenv import load_dotenv

load_dotenv()

ZAPI_INSTANCE = os.getenv("ZAPI_INSTANCE")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")

if not ZAPI_INSTANCE or not ZAPI_TOKEN or not ZAPI_CLIENT_TOKEN:
    raise ValueError("Variáveis da Z-API não configuradas no .env")

def enviar_mensagem(numero, mensagem):
    """Envia mensagem via Z-API"""
    try:
        url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE}/token/{ZAPI_TOKEN}/send-text"
        payload = {
            "phone": numero,
            "message": mensagem
        }
        headers = {
            "client-token": ZAPI_CLIENT_TOKEN,
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            print(f"[OK] Mensagem enviada para {numero}")
        else:
            print(f"[ERRO] Falha ao enviar para {numero} - Status {response.status_code} - {response.text}")
    except Exception as e:
        print(f"[ERRO] Exceção ao enviar mensagem para {numero}: {e}")