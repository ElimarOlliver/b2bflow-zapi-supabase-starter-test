# b2bflow – Supabase → Z-API (Python)

Projeto do desafio: ler contatos no Supabase e enviar, via Z-API, a mensagem:

> `Olá {{nome_contato}}, tudo bem com você?`

Onde `{{nome_contato}}` é substituído pelo campo salvo no banco.

---

## 1) Banco (Supabase)

### Tabela
Crie a tabela `public.contacts`:
```sql
create table if not exists public.contacts (
  id uuid primary key default gen_random_uuid(),
  nome_contato text not null,
  telefone text not null
);
