# app-retta-flask

Este projeto é uma aplicação backend desenvolvida em **Flask**, com foco em integração via **API RESTful**, automações com **n8n** e exposição local com **ngrok**. Foi elaborado como parte do desafio técnico proposto pela empresa **Retta**, que atua com soluções low-code/no-code e inteligência artificial aplicada a negócios.

## 🧠 Objetivo

Demonstrar domínio técnico e iniciativa na criação de uma aplicação backend simples e funcional, conectável a fluxos de automação n8n e acessível remotamente via ngrok. O projeto também visa refletir práticas modernas de desenvolvimento, integração e documentação, alinhando-se aos princípios e demandas de um **Platform Specialist** em ambientes de **Edge AI**.

## ⚙️ Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [n8n](https://n8n.io/) – ferramenta de automação de fluxos low-code
- [ngrok](https://ngrok.com/) – túnel HTTP para exposição local
- [Git](https://git-scm.com/)
- [VS Code](https://code.visualstudio.com/)
- [Docker (em breve)](https://www.docker.com/) – para facilitar deploy

##  Estrutura do Projeto

app-retta-flask/
├── app/
│ ├── init.py # Inicialização do app Flask
│ ├── routes.py # Rotas da API
│ └── controllers/ # Lógica separada por domínio (futuramente)
├── produtos.json # Base de dados simulada (mock)
├── requirements.txt # Dependências do projeto
├── run.py # Arquivo principal para executar a aplicação
├── README.md # Documentação do projeto
└── .env # (opcional) variáveis de ambiente


## 📡 Endpoints Disponíveis

| Rota             | Método | Descrição                          |
|------------------|--------|------------------------------------|
| `/produtos`      | GET    | Lista todos os produtos            |
| `/produtos`      | POST   | Adiciona um novo produto           |
| `/produtos/<codigo>` | GET  | Retorna detalhes de um produto     |
| `/produtos/<codigo>` | PUT  | Atualiza os dados de um produto    |
| `/produtos/<codigo>` | DELETE| Remove um produto da base         |

## 🛠️ Como Executar Localmente

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/app-retta-flask.git
cd app-retta-flask

python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt

Rodar a API Flask

python run.py

Iniciar ngrok (instalado previamente)
# O ngrok deve ser instalado em outro terminal e com a Api rodando. 
