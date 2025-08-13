# b2bflow – Supabase → Z‑API (Python)

Projeto de estágio: lê contatos no Supabase e envia mensagem personalizada via Z‑API.

## Tabela no Supabase
Crie a tabela `contacts` com as colunas:
- id (serial ou uuid, PK)
- nome_contato (text, NOT NULL)
- telefone (text, NOT NULL) – formato E.164 (ex.: 5511999999999)

Exemplo SQL:
```sql
CREATE TABLE IF NOT EXISTS contacts (
  id serial PRIMARY KEY,
  nome_contato text NOT NULL,
  telefone text NOT NULL,
  created_at timestamptz DEFAULT now()
);
```

## Variáveis de ambiente (.env)
Veja `.env.example` e crie um `.env` com seus valores reais.

## Instalação
```bash
python -m venv .venv
# PowerShell:
.\.venv\Scripts\Activate.ps1
# CMD:
# .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Execução
```bash
python main.py
```