#projetado em 23/06
#atualizado dia 30/06
from flask import Flask, request, render_template, redirect, make_response, url_for

app = Flask(__name__)

users = {"raphael" : "0297",
         "rodrigo": "1546",
         "rogério": "1540"}

counter = 0

@app.route('/')
def view_form():
    return render_template('loginForm.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    mensagem = "Faça login para aproveitar nossos serviços"
    if request.method == 'POST':
        nome = request.form['nome'].lower()
        senha = request.form['senha'].lower()
        if nome in users and users[nome] == senha:
            resposta = make_response(redirect(url_for('home')))
            resposta.set_cookie('username', nome, max_age=60*30)
            resposta.set_cookie('counter', "0", max_age=60*30)
            return resposta
        else:
            mensagem = "Usuário ou senha inválidos. Tente novamente."

    return render_template('loginForm.html', mensagem=mensagem)


@app.route('/set_theme', methods=['POST'])
def set_theme():
    new_theme = request.form.get("theme")

    if new_theme != 'light' and new_theme != 'dark':
        new_theme = 'light'

    response = make_response(redirect(url_for('home')))
    response.set_cookie('theme', new_theme, max_age=60*30)
    return response

@app.route('/set_category', methods=['POST'])
def set_category():
    initial_category = request.form.get("initial_category")
    if not initial_category in ['esporte', 'politica', 'musica', 'lazer']:
        initial_category = 'esporte'

    response = make_response(redirect(url_for('home')))
    response.set_cookie('initial_category', initial_category, max_age=60*30)
    return response


@app.route('/home_page')
def home():
    global counter
    counter += 1
    theme = request.cookies.get('theme')
    if theme != 'light' and theme != 'dark':
        theme = 'light'
    category = request.cookies.get("initial_category")
    if not category in ['esporte', 'politica', 'musica', 'lazer']:
        category = "esporte"
    username = request.cookies.get('username')
    if username:
        return render_template('home.html', usuario=username, counter=counter, initial_theme=theme, initial_category=category)
    return render_template('loginForm.html')

@app.route('/logout', methods=['POST'])   
def logout():
    global counter
    counter = 0
    resposta = make_response(redirect(url_for('view_form')))
    if request.method == 'POST':
        resposta = make_response(redirect(url_for('login')))
        resposta.set_cookie('username', '', expires=0)
        resposta.set_cookie('counter', '', expires=0)
    return resposta

if __name__ == '__main__':
    app.run(debug=True)