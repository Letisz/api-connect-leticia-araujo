# API Connect

## Sobre o projeto

A API Connect é uma API REST desenvolvida como um Produto Mínimo Viável (MVP) para gerenciamento de usuários.

O projeto permite realizar operações de cadastro, consulta, atualização e exclusão de usuários, utilizando requisições HTTP e respostas estruturadas em JSON.

A aplicação foi desenvolvida seguindo o princípio de Separação de Responsabilidades, mantendo rotas, controladores e dados organizados em diferentes arquivos.

## Tecnologias utilizadas

- Python
- Flask
- API REST
- HTTP
- JSON
- Git
- GitHub

## Estrutura do projeto

```text
api-connect/
│
├── venv/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── routes/
│   └── connect_routes.py
│
├── controllers/
│   └── connect_controller.py
│
└── data/
    └── connect_data.py
