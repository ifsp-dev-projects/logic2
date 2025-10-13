from flask import Blueprint, render_template, request, abort, jsonify
import math
from models.produto import PRODUTOS, buscar_produto_por_id, buscar_produtos_por_nome

produto_bp = Blueprint('produto_bp', __name__)

@produto_bp.route('/')
@produto_bp.route('/produtos')
def listar_produtos():
    return render_template('produtos.html', produtos=PRODUTOS)

@produto_bp.route('/produtos-paginados')
def listar_produtos_paginados():
    page = request.args.get('page', 1, type=int)
    per_page = 5

    start = (page-1)*per_page
    end = start + per_page
    total_pages = math.ceil(len(PRODUTOS)/per_page)

    produtos_da_pagina = PRODUTOS[start:end]

    return render_template(
        'produtos_paginados.html',
        produtos=produtos_da_pagina,
        page=page,
        total_pages=total_pages
    )

@produto_bp.route('/produto/<int:produto_id>')
def detalhe_produto(produto_id):
    produto = buscar_produto_por_id(produto_id)
    if produto is None:
        abort(404)
    return render_template('detalhe_produto.html', produto=produto)

@produto_bp.route('/api/buscar-produto', methods=['POST'])
def api_buscar_produto():
    dados = request.get_json()
    nome_produto = dados.get('nome', '')
    resultado = buscar_produtos_por_nome(nome_produto)
    # Transformar em dicionário para JSON
    resultado_dict = [{'id': p.id, 'nome': p.nome, 'preco': p.preco} for p in resultado]
    return jsonify({'produtos_encontrados': resultado_dict})
