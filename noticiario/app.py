from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

USUARIO_CADASTRADO = "ana"
SENHA_CADASTRADA = "231"

@app.route('/', methods=['GET', 'POST'])
def login():
    mensagem = ""

    if request.method == "POST":
        usuario = request.form['username']
        senha = request.form['password']

        if usuario == USUARIO_CADASTRADO and senha == SENHA_CADASTRADA:
            resposta = make_response(redirect(url_for('noticias')))
            resposta.set_cookie('username', usuario, max_age=60*10)
            resposta.set_cookie('visitas', '1', max_age=60*30)
            resposta.set_cookie('tema', 'light', max_age=60*30)
            return resposta
        else:
            mensagem = "Usuário ou senha inválidos. Tente novamente."

    return render_template('login.html', error=mensagem)

@app.route('/bemvindo')
def bemvindo():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
    
    visitas = int(request.cookies.get('visitas', 0)) + 1
    resposta = make_response(render_template(
        'bemvindo.html',
        user=username,  # Aqui está como 'user'
        visitas=visitas,
        tema=request.cookies.get('tema', 'light')
    ))
    resposta.set_cookie('visitas', str(visitas), max_age=60*30)
    
    return resposta

@app.route('/esportes')
def esportes():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
    
    tema = request.cookies.get('tema', 'light') 


    resposta = make_response(render_template(
        'esportes.html',
        user=username, 
        tema=tema
    ))

    return resposta

@app.route('/entretenimento')
def entretenimento():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))

    tema = request.cookies.get('tema', 'light') 


    resposta = make_response(render_template(
        'entretenimento.html',
        user=username, 
        tema=tema
    ))


    return resposta
@app.route('/lazer')
def lazer():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))

    tema = request.cookies.get('tema', 'light') 


    resposta = make_response(render_template(
        'lazer.html',
        user=username, 
        tema=tema
    ))

    return resposta

@app.route('/noticias')
def noticias():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
    

    visitas = int(request.cookies.get('visitas', 0)) + 1

    tema = request.cookies.get('tema', 'light') 


    resposta = make_response(render_template(
        'noticias.html',
        user=username, 
        visitas=visitas,
        tema=tema
    ))

    resposta.set_cookie('visitas', str(visitas), max_age=60*30)

    return resposta


@app.route('/logout')
def logout():
    resposta = make_response(redirect(url_for('login')))
    resposta.set_cookie('username', '', expires=0)
    return resposta

@app.route('/mudartema', methods=['POST'])
def mudar_tema():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
    
    tema_atual = request.cookies.get('tema', 'light')
    novoTema = 'dark' if tema_atual == 'light' else 'light'
    resposta = make_response(redirect(request.referrer or url_for('noticias')))
    resposta.set_cookie('tema', novoTema, max_age=60*30)

    resposta.set_cookie('username', username, max_age=60*30)
    if 'visitas' in request.cookies:
        resposta.set_cookie('visitas', request.cookies['visitas'], max_age=60*30)
    return resposta

if __name__ == '__main__':
    app.run(debug=True)