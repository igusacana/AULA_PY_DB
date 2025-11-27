# 🎬 Sistema de Cinema

Sistema de gerenciamento de cinema desenvolvido em Python + PostgreSQL para fins acadêmicos.

## 🚀 Funcionalidades

### Administrador
- Cadastrar e listar filmes
- Cadastrar e listar salas
- Criar e listar sessões

### Cliente
- Cadastro e login
- Ver filmes em cartaz
- Comprar ingressos
- Histórico de compras

## 🛠️ Tecnologias

- **Python 3.8+**
- **PostgreSQL 13+**
- **psycopg2** (conector Python-PostgreSQL)

## 📁 Estrutura do Projeto
```
├── config/          # Conexão com banco de dados
├── services/        # Lógica CRUD
├── view/
│   ├── menus/       # Menus do sistema
│   └── actions/     # Ações dos menus
├── funcoes.py       # Funções utilitárias
└── main.py          # Entrada do programa
```

## 🗃️ Banco de Dados

5 tabelas relacionadas:
- `usuarios` - Clientes do cinema
- `filmes` - Catálogo de filmes
- `salas` - Salas físicas
- `sessoes` - Horários dos filmes
- `ingressos` - Compras realizadas

## ▶️ Como usar
```bash
python main.py
```

### Credenciais Admin
**Senha:** `admin123`

## 📚 Conceitos Aplicados

- Integração Python + PostgreSQL
- Arquitetura em camadas (MVC adaptado)
- CRUD completo
- Relacionamentos entre tabelas (Foreign Keys)
- JOINs em queries SQL

## 👨‍💻 Autor

Projeto acadêmico desenvolvido para demonstrar integração entre Python e banco de dados.

---

⭐ **Sistema de Cinema - Python + PostgreSQL**