"""
main.py
Orquestra o fluxo: lê contatos do Supabase e envia mensagem personalizada via Z-API.

Mensagem EXACTA exigida:
"Olá {{nome_contato}}, tudo bem com você?"

No código, substituímos {{nome_contato}} pelo valor do banco.
"""

from supabase_client import get_contacts
from zapi_client import send_text

def build_message(nome_contato: str) -> str:
    # mensagem exatamente como pedida, só substituindo o placeholder
    return f"Olá {nome_contato}, tudo bem com você?"

def main() -> None:
    contatos = get_contacts(limit=3)

    if not contatos:
        print("Nenhum contato encontrado.")
        return

    # Evita enviar duplicado caso existam números repetidos
    enviados = set()

    for contato in contatos:
        nome = str(contato["nome_contato"]).strip()
        phone = str(contato["phone"]).strip()

        if not phone or phone in enviados:
            continue

        msg = build_message(nome)
        try:
            resp = send_text(phone, msg)
            print(f"[OK] Enviado para {nome} ({phone}). Resposta: {resp}")
            enviados.add(phone)
        except Exception as e:
            print(f"[ERRO] Falha ao enviar para {nome} ({phone}): {e}")

if __name__ == "__main__":
    main()
