# Docker Project 🚀

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100-green?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-24-blue?logo=docker)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?logo=sqlalchemy)

Um **projeto de teste de Docker** com Python, FastAPI e PostgreSQL, totalmente containerizado, ideal para estudo e prática.

---

## Tecnologias
- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)

---

## Estrutura do projeto
```
Docker_Project/
│
├─ src/                  # Código fonte da aplicação
├─ Dockerfile            # Configuração do container da aplicação
├─ docker-compose.yml    # Orquestração de containers
├─ .env.example          # Exemplo de variáveis de ambiente
├─ requirements.txt      # Dependências Python
├─ install.sh            # Script de instalação rápida
└─ run.py                # Arquivo principal
```

---

## Rodando o projeto

1. Clone o repositório:
```bash
git clone https://github.com/iamDFSB/Docker_Project.git
cd Docker_Project
```

2. Configure as variáveis de ambiente:
```bash
cp .env.example .env
```

3. Inicie os containers:
```bash
docker-compose up --build
```

4. Acesse a aplicação:
```
http://localhost:8000
```

---

## Funcionalidades
- API básica com FastAPI.
- Conexão com PostgreSQL via SQLAlchemy.
- Totalmente containerizado para fácil deploy e testes.

---

## Boas práticas
- `.env` ignorado pelo Git (listado no `.gitignore`).
- Uso de Dockerfile e docker-compose para **containerização completa**.
- Estrutura organizada para estudo e manutenção.

