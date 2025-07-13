from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

USUARIO_CADASTRADO = ["ana", "dudu", "little agosto"]
SENHA_CADASTRADA = "231"

@app.route('/', methods=['GET', 'POST'])
def login():
    mensagem = ""

    if request.method == "POST":
        usuario = request.form['username']
        senha = request.form['password']

        if usuario in USUARIO_CADASTRADO and senha == SENHA_CADASTRADA:
            destino = request.cookies.get('redirect_depois_login')
            if not destino:
                destino = url_for('noticias')

            resposta = make_response(redirect(destino))
            resposta.set_cookie('username', usuario, max_age=60*10)
            resposta.set_cookie('visitas', '1', max_age=60*30)
            resposta.set_cookie('tema', 'light', max_age=60*30)
            resposta.set_cookie('redirect_depois_login', '', expires=0)
            return resposta
        else:
            mensagem = "Usuário ou senha inválidos. Tente novamente."

    return render_template('login.html', error=mensagem)

@app.route('/noticias')
def noticias():
    username = request.cookies.get('username')

    if not username:
        resposta = make_response(redirect(url_for('login')))
        resposta.set_cookie('redirect_depois_login', request.path, max_age=60)
        return resposta

    visitas_cookie = request.cookies.get('visitas')
    if visitas_cookie:
        visitas = int(visitas_cookie) + 1
    else:
        visitas = 1

    tema = request.cookies.get('tema')
    if not tema:
        tema = 'light'

    categoria_selecionada = request.cookies.get('ultima_categoria')

    resposta = make_response(render_template(
        'noticias.html',
        user=username,
        visitas=visitas,
        tema=tema,
        categoria=categoria_selecionada
    ))
    resposta.set_cookie('visitas', str(visitas), max_age=60*30)
    return resposta

@app.route('/esportes')
def esportes():
    username = request.cookies.get('username')
    if not username:
        resposta = make_response(redirect(url_for('login')))
        resposta.set_cookie('redirect_depois_login', request.path, max_age=60)
        return resposta

    tema = request.cookies.get('tema') or 'light'

    resposta = make_response(render_template('esportes.html', user=username, tema=tema))
    resposta.set_cookie('ultima_categoria', 'esportes', max_age=60*30)
    return resposta

@app.route('/entretenimento')
def entretenimento():
    username = request.cookies.get('username')
    if not username:
        resposta = make_response(redirect(url_for('login')))
        resposta.set_cookie('redirect_depois_login', request.path, max_age=60)
        return resposta

    tema = request.cookies.get('tema') or 'light'

    resposta = make_response(render_template('entretenimento.html', user=username, tema=tema))
    resposta.set_cookie('ultima_categoria', 'entretenimento', max_age=60*30)
    return resposta

@app.route('/lazer')
def lazer():
    username = request.cookies.get('username')
    if not username:
        resposta = make_response(redirect(url_for('login')))
        resposta.set_cookie('redirect_depois_login', request.path, max_age=60)
        return resposta

    tema = request.cookies.get('tema') or 'light'

    resposta = make_response(render_template('lazer.html', user=username, tema=tema))
    resposta.set_cookie('ultima_categoria', 'lazer', max_age=60*30)
    return resposta

@app.route('/limpar_categoria')
def limpar_categoria():
    username = request.cookies.get('username')
    if not username:
        resposta = make_response(redirect(url_for('login')))
        resposta.set_cookie('redirect_depois_login', request.path, max_age=60)
        return resposta

    resposta = make_response(redirect(url_for('noticias')))
    resposta.set_cookie('ultima_categoria', '', expires=0)
    return resposta

@app.route('/logout')
def logout():
    ultima_pagina = request.referrer

    if not ultima_pagina:
        ultima_pagina = url_for('noticias')

    resposta = make_response(redirect(url_for('login')))
    resposta.set_cookie('username', '', expires=0)
    resposta.set_cookie('redirect_depois_login', ultima_pagina, max_age=60)
    return resposta

@app.route('/mudartema', methods=['POST'])
def mudar_tema():
    username = request.cookies.get('username')

    if not username:
        return redirect(url_for('login'))

    tema_atual = request.cookies.get('tema') or 'light'

    novoTema = 'dark' if tema_atual == 'light' else 'light'

    voltar_para = request.referrer or url_for('noticias')

    resposta = make_response(redirect(voltar_para))
    resposta.set_cookie('tema', novoTema, max_age=60*30)
    resposta.set_cookie('username', username, max_age=60*30)

    visitas_cookie = request.cookies.get('visitas')
    if visitas_cookie:
        resposta.set_cookie('visitas', visitas_cookie, max_age=60*30)

    return resposta

if __name__ == '__main__':
    app.run(debug=True)
