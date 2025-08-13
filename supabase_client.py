"""
supabase_client.py
Responsável por ler os contatos no Supabase.

- Usa a ANON KEY (somente leitura).
- Lê até 3 contatos (ou menos, se não houver 3).
"""

from typing import List, Dict
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()  # carrega variáveis de ambiente do .env

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError(
        "SUPABASE_URL e/ou SUPABASE_KEY não configurados. "
        "Crie o arquivo .env com as variáveis ou exporte no ambiente."
    )

# cria o cliente do Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_contacts(limit: int = 3) -> List[Dict]:
    """
    Busca contatos na tabela 'contacts', retornando no máximo `limit` linhas.
    Campos esperados: nome_contato (text), phone (text).
    """
    try:
        resp = supabase.table("contacts").select("nome_contato, telefone").limit(limit).execute()
        data = resp.data or []
        # filtro simples para garantir que há nome e phone
        data = [c for c in data if c.get("nome_contato") and c.get("telefone")]
        return data
    except Exception as e:
        # Em um projeto real, logue com mais contexto
        raise RuntimeError(f"Erro ao consultar contatos no Supabase: {e}") from e
