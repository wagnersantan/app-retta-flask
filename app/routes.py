from flask import Blueprint, jsonify, request, send_file
import json
import os
import requests
import uuid
from reportlab.pdfgen import canvas
from app.services.pdf_service import gerar_pdf

routes = Blueprint("routes", __name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), "../produtos.json")


# ======== ENVIAR PARA N8N ========
@routes.route("/enviar_sugestao", methods=["POST"])
def enviar_sugestao():
    dados = request.json

    n8n_webhook = "https://SEU_N8N_DOMAIN/webhook/ID_DO_FLUXO"

    try:
        r = requests.post(n8n_webhook, json=dados)
        r.raise_for_status()

        return jsonify({
            "status": "enviado",
            "n8n_status": r.status_code
        })

    except Exception as e:
        return jsonify({
            "status": "erro",
            "mensagem": str(e)
        }), 500


# ======== LISTAR PRODUTOS ========
@routes.route("/produtos", methods=["GET"])
def listar_produtos():
    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    return jsonify(data)


# ======== ADICIONAR PRODUTO ========
@routes.route("/produtos", methods=["POST"])
def adicionar_produto():
    novo_produto = request.json

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    data.append(novo_produto)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return jsonify(novo_produto), 201


# ======== ATUALIZAR PRODUTO ========
@routes.route("/produtos/<int:produto_id>", methods=["PUT"])
def atualizar_produto(produto_id):
    atualizado = request.json

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    for produto in data:
        if produto.get("id") == produto_id:
            produto.update(atualizado)

            with open(DATA_FILE, "w") as f:
                json.dump(data, f, indent=4)

            return jsonify(produto), 200

    return jsonify({"erro": "Produto não encontrado"}), 404


# ======== DELETAR PRODUTO ========
@routes.route("/produtos/<int:produto_id>", methods=["DELETE"])
def deletar_produto(produto_id):

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    for i, produto in enumerate(data):

        if produto.get("id") == produto_id:

            deletado = data.pop(i)

            with open(DATA_FILE, "w") as f:
                json.dump(data, f, indent=4)

            return jsonify(deletado), 200

    return jsonify({"erro": "Produto não encontrado"}), 404
# ======== RECEBER DADOS DO TYPEBOT ========
# ======== RECEBER DADOS DO TYPEBOT ========
@routes.route("/typebot", methods=["POST"])
def receber_typebot():

    dados = request.json

    nome = dados.get("nome")
    produto_busca = dados.get("produto")

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    encontrados = []

    for produto in data:
        if produto_busca.lower() in produto.get("descricao", "").lower():
            encontrados.append(produto)

    return jsonify({
        "usuario": nome,
        "produtos_encontrados": encontrados
    })
 # ======== BUSCAR PRODUTO POR NOME ========
@routes.route("/buscar", methods=["GET"])
def buscar_produto():

    nome = request.args.get("nome")

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    resultados = []

    for produto in data:
        descricao = produto.get("descricao", "").lower()

        if nome.lower() in descricao:
            resultados.append(produto)

    return jsonify(resultados)


    # ======== GERAR PDF ========
@routes.route("/gerar-pdf", methods=["POST"])
def gerar_pdf():

    dados = request.json

    nome = dados.get("nome")
    produto_busca = dados.get("produto")

    with open(DATA_FILE, "r") as f:
        produtos = json.load(f)

    produto_encontrado = None

    for produto in produtos:
        if produto_busca.lower() in produto.get("descricao","").lower():
            produto_encontrado = produto
            break

    if not produto_encontrado:
        return jsonify({"erro": "Produto não encontrado"}), 404

    arquivo = f"pdfs/{uuid.uuid4()}.pdf"

    c = canvas.Canvas(arquivo)

    c.drawString(100, 750, "Solicitação de Produto")
    c.drawString(100, 720, f"Cliente: {nome}")
    c.drawString(100, 700, f"Produto: {produto_encontrado['descricao']}")

    c.save()

    return send_file(arquivo, as_attachment=True)