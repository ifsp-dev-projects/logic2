from flask import (render_template,request,redirect, url_for, flash, abort, jsonify, session)
from app import app

TAREFAS_DB = {
    1:{'texto': 'Aprender os conceitos do Flask', 'concluida': True},
    2:{'texto': 'Ver os exemplos de código', 'concluida': False},
    3:{'texto': 'Construir minha própria aplicação', 'concluida': False},
}

next_id=4


@app.route("/")
def index():
    return render_template('index.html', tarefas= TAREFAS_DB)

@app.route('/tarefa/<int:tarefa_id>')
def detalhe_tarefa(tarefa_id):
    tarefa = TAREFAS_DB.get(tarefa_id)
    if not tarefa:
        abort(404)
    return render_template('detalhe.html', tarefa=tarefa, tarefa_id=tarefa_id)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    global next_id
    texto_tarefa = request.form.get('texto_da_tarefa')

    if not texto_tarefa or len(texto_tarefa) < 3:
        flash('A tarefaprecisa conter pelo menos 3 caracteres!', 'erro')
    else:
        TAREFAS_DB[next_id] = {'texto': texto_tarefa, 'concluida': False}
        next_id+=1

        flash('Tarefa adicionada com sucesso!' 'sucesso')

        session['contador'] = session.get('contador', 0) + 1
        flash(f"Você ja adicionou {session['contador']} tarefas!", "info")

    return redirect(url_for("index"))

@app.route('/tarefa/concluir/<int:tarefa_id>', methods=['POST'])
def concluir_tarefas(tarefa_id):
    tarefa= TAREFAS_DB.get(tarefa_id)
    if tarefa:
        tarefa['concluida'] = not tarefa ['concluida']
        return jsonify({'status': 'sucesso', 'concluida': tarefa['concluida']})
    return jsonify({'status':'erro'}), 404


@app.route('/admin')
def admin_panel():
    if session.get('username') != 'admin':
        abort(403)
    return '<h1> Painel do administrador<h1>'

@app.errorhandler(404)
def not_found_error(error):
    return render_template('erros/404.html'), 404

@app.errorhandler(403)
def forbidden_error(error):
    return render_template('erros/403.html'), 403

@app.errorhandler(401)
def unauthorized_error(error):
    return render_template('erros/401.html'), 401

