 Integração de Soluções NoSQL com Streamlit para Visualização de Dados

Este projeto é uma aplicação CRUD completa usando MongoDB e Streamlit, com dados fictícios gerados pelo Faker. O objetivo é simular o gerenciamento de clientes de uma empresa de e-commerce chamada **E-Shop Brasil**, aplicando práticas modernas como o uso de containers, bancos de dados NoSQL e interfaces web interativas.

---

#  Tecnologias Utilizadas

- Python 3.10+
- Streamlit
- MongoDB (via Docker)
- Docker Compose
- Faker

---

# Estrutura do Projeto

.
├── app/
│ └── main.py
├── data/
│ └── gerar_dados.py
├── docker-compose.yml
├── requirements.txt
└── README.md

yaml
Copiar
Editar

---

# Como Rodar o Projeto

1. Instale o [Docker](https://www.docker.com/) e o Python 3.10+.

2. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Crie e ative o ambiente virtual:


python -m venv venv
# Linux/Mac:
source venv/bin/activate
# Windows:
.\venv\Scripts\activate
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Suba o MongoDB com Docker:


docker-compose up -d
Gere os dados fictícios (mais de 1 milhão de registros):

python data/gerar_dados.py
Rode a aplicação:

streamlit run app/main.py
 Funcionalidades
 Cadastro de clientes

Visualização da lista de clientes

Atualização de informações existentes

Exclusão de registros

Sobre o Projeto

A empresa E-Shop Brasil está em processo de modernização e precisa gerenciar dados de forma eficiente e escalável. A proposta é criar uma aplicação CRUD conectada a um banco NoSQL (MongoDB), com interface desenvolvida em Streamlit, possibilitando:

Portabilidade via Docker

Visualização e manipulação de grandes volumes de dados

Facilidade de uso para usuários finais





