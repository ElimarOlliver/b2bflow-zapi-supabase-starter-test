"""
zapi_client.py
Responsável por enviar mensagens via Z-API.

Endpoint utilizado:
POST https://api.z-api.io/instances/{INSTANCE_ID}/token/{TOKEN}/send-text

Body:
{
  "phone": "5511999999999",
  "message": "Olá Fulano, tudo bem com você?"
}

Se você ativar 'Account security token' na Z-API, inclua o header 'Client-Token'.
"""

import os
from typing import Optional, Dict, Any
import requests
from dotenv import load_dotenv

load_dotenv()

ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN", "")  # opcional

if not ZAPI_INSTANCE_ID or not ZAPI_TOKEN:
    raise RuntimeError(
        "ZAPI_INSTANCE_ID e/ou ZAPI_TOKEN não configurados no .env."
    )

BASE_URL = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}"

def send_text(phone: str, message: str) -> Dict[str, Any]:
    """
    Envia mensagem de texto para um número.
    Retorna o JSON de resposta da Z-API ou lança exceção se HTTP != 2xx, exibindo o corpo da resposta.
    """
    url = f"{BASE_URL}/send-text"
    headers = {"Content-Type": "application/json"}
    if ZAPI_CLIENT_TOKEN:
        headers["Client-Token"] = ZAPI_CLIENT_TOKEN

    payload = {"phone": phone, "message": message}

    resp = requests.post(url, json=payload, headers=headers, timeout=30)
    if not resp.ok:
        # mostra status + corpo (ajuda a diagnosticar 404/401/403/422 etc.)
        raise RuntimeError(f"Z-API error {resp.status_code}: {resp.text}")
    return resp.json()
