# App Retta Flask

Este projeto é uma aplicação backend desenvolvida em **Flask**, com foco em integração via **API RESTful**, automações com **n8n** e integração com interfaces conversacionais utilizando **Typebot**.

Foi elaborado como parte de um **desafio técnico proposto pela empresa Retta**, que atua com soluções **low-code/no-code** e **inteligência artificial aplicada a negócios**.

A aplicação demonstra a construção de uma API simples, integrada a fluxos de automação e capaz de gerar **documentos em PDF** a partir de dados estruturados.

---

# 🧠 Objetivo

Demonstrar domínio técnico na criação de uma aplicação backend conectável a plataformas de automação e interfaces conversacionais.

O projeto evidencia:

* criação de **APIs RESTful com Flask**
* integração com **fluxos n8n**
* utilização de **dados estruturados em JSON**
* geração automática de **PDFs**
* integração com **chatbots (Typebot)**

Esses elementos refletem competências relevantes para atuação como **Platform Specialist em ambientes de automação e Edge AI**.

---

# ⚙️ Tecnologias Utilizadas

* Python 3.10+
* Flask
* n8n (Automação de fluxos)
* Typebot (Interface conversacional)
* ngrok (exposição local da API)
* JSON (mock de base de dados)
* Git
* VS Code

Possíveis evoluções:

* Docker para deploy
* Banco de dados persistente
* Frontend Web

---

# 📁 Estrutura do Projeto

```
app-retta-flask/
│
├── app/
│   ├── __init__.py          # Inicialização da aplicação Flask
│   ├── routes.py            # Definição das rotas da API
│   └── services/            # Lógica de negócio (ex: geração de PDF)
│
├── n8n/
│   └── fluxo_sugestao_artigos_n8n.json   # Workflow de automação
│
├── typebot/
│   └── fluxo_typebot.md     # Estrutura/documentação do fluxo do chatbot
│
├── pdfs/
│   └── *.pdf                # PDFs gerados dinamicamente
│
├── produtos.json            # Base de dados simulada (mock)
├── pedido.pdf               # Exemplo de pedido gerado
│
├── requirements.txt         # Dependências do projeto
├── run.py                   # Arquivo principal para execução da aplicação
│
├── README.md                # Documentação do projeto
└── venv/                    # Ambiente virtual Python
```

---

# 📡 Endpoints Disponíveis

| Rota                 | Método | Descrição                      |
| -------------------- | ------ | ------------------------------ |
| `/produtos`          | GET    | Lista todos os produtos        |
| `/produtos`          | POST   | Adiciona um novo produto       |
| `/produtos/<codigo>` | GET    | Retorna detalhes de um produto |
| `/produtos/<codigo>` | PUT    | Atualiza um produto            |
| `/produtos/<codigo>` | DELETE | Remove um produto              |

Esses endpoints simulam uma **API de catálogo de produtos** consumida por automações externas.

---

# 📄 Geração de PDF

A aplicação também possui lógica para **geração de pedidos em PDF**, armazenados na pasta:

```
/pdfs
```

Essa funcionalidade demonstra a capacidade do backend de **processar dados recebidos via API e gerar documentos automaticamente**.

---

# 🛠️ Como Executar Localmente

## 1. Clonar o Repositório

```
git clone https://github.com/seu-usuario/app-retta-flask.git
cd app-retta-flask
```

---

## 2. Criar Ambiente Virtual

```
python3 -m venv venv
```

---

## 3. Ativar o Ambiente

Linux / Mac

```
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

---

## 4. Instalar Dependências

```
pip install -r requirements.txt
```

---

## 5. Executar a Aplicação

```
python run.py
```

A API estará disponível em:

```
http://127.0.0.1:5000
```

---

# 🌐 Exposição da API com ngrok

Para permitir que ferramentas externas consumam a API local:

```
ngrok http 5000
```

O ngrok gerará uma URL pública que pode ser usada por **n8n, Typebot ou outros serviços**.

---

# 🔁 Integração com n8n

Workflow disponível em:

```
n8n/fluxo_sugestao_artigos_n8n.json
```

Fluxo de automação:

1. Trigger manual ou webhook
2. Requisição HTTP para a API Flask
3. Processamento dos dados
4. Integração com serviços externos (ex: planilhas ou automações)

Esse fluxo demonstra a **interoperabilidade entre APIs REST e plataformas low-code**.

---

# 🤖 Integração com Typebot

O projeto também inclui um fluxo de chatbot documentado em:

```
typebot/fluxo_typebot.md
```

O Typebot pode ser utilizado para:

* coletar pedidos do usuário
* enviar dados para a API
* iniciar automações via n8n
* gerar pedidos em PDF

---

# 📈 Possíveis Evoluções

* Persistência com banco de dados (PostgreSQL ou MongoDB)
* Containerização com Docker
* Deploy em cloud (AWS, GCP ou Railway)
* Interface frontend
* Integração com WhatsApp
* API de pagamentos

---

# 👨‍💻 Autor

Projeto desenvolvido como parte de um **desafio técnico voltado à integração entre APIs, automação e plataformas low-code**.
