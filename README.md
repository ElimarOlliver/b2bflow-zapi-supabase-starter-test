# 📦 B2BFlow – Integração Supabase + Z-API

Projeto de integração entre [Supabase](https://supabase.com) e [Z-API](https://z-api.io) para envio automatizado de mensagens WhatsApp a partir de dados em banco de dados.

---

## 🎯 Objetivo

Automatizar o envio de mensagens personalizadas pelo WhatsApp, buscando contatos e mensagens de uma tabela no Supabase e enviando via API da Z-API.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.10+**
- **Supabase** (PostgreSQL e RLS)
- **Z-API**
- **Requests** (requisições HTTP)
- **python-dotenv** (carregar variáveis de ambiente)

---

## 🎬 Demonstração rápida

<p align="center">
  <img src="assets/terminal%20em%20execução.gif" alt="Execução do projeto no terminal" width="48%" />
  <img src="assets/mensagem_popup.gif" alt="Mensagem recebida no WhatsApp" width="48%" />
</p>

<p align="center">
  <em>À esquerda: execução do script enviando as mensagens. À direita: mensagem personalizada chegando no WhatsApp.</em>
</p>

---

## 📂 Estrutura do Projeto

```
.
├── assets/                      # GIFs e imagens do README
├── main.py                      # Script principal
├── supabase_client.py           # Conexão e operações com Supabase
├── zapi_client.py                # Cliente HTTP para integração com Z-API
├── requirements.txt              # Dependências do projeto
├── .env.example                  # Exemplo de variáveis de ambiente
├── README.md                     # Documentação
└── venv/                         # Ambiente virtual (ignorado no Git)
```

---

## 🔑 Configuração do `.env`

Copie o arquivo `.env.example` e configure suas credenciais reais:

```bash
cp .env.example .env
```

Edite com suas informações:

```env
SUPABASE_URL=https://xxxxxxxx.supabase.co
SUPABASE_KEY=chave_api_aqui
ZAPI_INSTANCE_ID=xxxxxxxx
ZAPI_TOKEN=xxxxxxxx
```

---

## 🚀 Como executar

1. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   # Linux/Mac
   source venv/bin/activate
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o script:
   ```bash
   python main.py
   ```

---

## 🛠️ Troubleshooting

- **Erro de política de execução no PowerShell**  
  Execute:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
  ```

- **Variáveis de ambiente não carregadas**  
  Verifique se o arquivo `.env` está na raiz do projeto e não possui espaços extras.

---

## 📜 Licença

Este projeto é distribuído sob a licença MIT.
