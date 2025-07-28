from flask import Blueprint, jsonify, request
import json
import os

bp = Blueprint('routes', __name__)

# Caminho absoluto para o JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, '..', 'produtos.json')


# Função para carregar os produtos
def carregar_produtos():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)



# Função para salvar os produtos
def salvar_produtos(produtos):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)


# Rota: GET /produtos — listar todos os produtos
@bp.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = carregar_produtos()
    return jsonify(produtos)


# Rota: GET /produtos/<id> — obter um produto por id
@bp.route('/produtos/<int:id>', methods=['GET'])
def obter_produto(id):
    produtos = carregar_produtos()
    for produto in produtos:
        if produto['id'] == id:
            return jsonify(produto)
    return jsonify({'erro': 'Produto não encontrado'}), 404


# Rota: POST /produtos — adicionar um novo produto
@bp.route('/produtos', methods=['POST'])
def adicionar_produto():
    novo_produto = request.get_json()
    produtos = carregar_produtos()
    novo_produto['id'] = max([p['id'] for p in produtos], default=0) + 1
    produtos.append(novo_produto)
    salvar_produtos(produtos)
    return jsonify(novo_produto), 201


# Rota: PUT /produtos/<id> — atualizar um produto
@bp.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    dados = request.get_json()
    produtos = carregar_produtos()
    for produto in produtos:
        if produto['id'] == id:
            produto.update(dados)
            salvar_produtos(produtos)
            return jsonify(produto)
    return jsonify({'erro': 'Produto não encontrado'}), 404


# Rota: DELETE /produtos/<id> — remover um produto
@bp.route('/produtos/<int:id>', methods=['DELETE'])
def remover_produto(id):
    produtos = carregar_produtos()
    novos_produtos = [p for p in produtos if p['id'] != id]
    if len(novos_produtos) == len(produtos):
        return jsonify({'erro': 'Produto não encontrado'}), 404
    salvar_produtos(novos_produtos)
    return jsonify({'mensagem': 'Produto removido com sucesso'})

@bp.route('/', methods=['GET'])
def home():
    return jsonify({"mensagem": "API de produtos está no ar!"})
