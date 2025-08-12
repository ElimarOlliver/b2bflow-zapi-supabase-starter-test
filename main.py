from supabase_client import buscar_contatos
from zapi_client import enviar_mensagem

def main():
    contatos = buscar_contatos(limit=3)

    if not contatos:
        print("[INFO] Nenhum contato encontrado no Supabase.")
        return

    for contato in contatos:
        nome = contato.get("nome_contato"),
        telefone = contato.get("telefone")

        if not telefone:
            print(f"[ALERTA] Contato {nome} não possui telefone.")
            continue

        mensagem = f"Olá {nome}, tudo bem com você?"
        enviar_mensagem(telefone, mensagem)

if __name__ == "__main__":
    main()
