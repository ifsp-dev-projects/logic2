from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'chaveSuperSecreta'

users = {'ana': '123', 'helo': '456'}

app.permanent_session_lifetime = timedelta(days=7) 

@app.route('/')
def carregarIndex():
    if 'user' in session:  
        return render_template('index.html', user=session['user'])
    return redirect(url_for('paginaLogin'))  

@app.route('/mudarNoticias', methods=['GET'])
def paginaNoticias():
    if 'user' in session:
        return render_template('noticias.html')
    return redirect(url_for('paginaLogin'))  

@app.route('/mudarEventos', methods=['GET'])
def paginaEventos():
    if 'user' in session:
        return render_template('eventos.html')
    return redirect(url_for('paginaLogin'))

@app.route('/mudarPremiacoes', methods=['GET'])
def paginaPremicoes():
    if 'user' in session:
        return render_template('premiações.html')
    return redirect(url_for('paginaLogin'))

@app.route('/mudarLogin', methods=['GET'])
def paginaLogin():
    return render_template('login.html')

@app.route('/mudarCadastro', methods=['GET'])
def paginaCadastro():
    return render_template('cadastro.html')

@app.route('/logar', methods=['POST'])
def logar():
    username = request.form['username']
    password = request.form['password']
    remember = 'remember' in request.form  
    
    if username in users and users[username] == password:
        session['user'] = username  
        session.permanent = remember  
        
        if remember:
            app.permanent_session_lifetime = timedelta(days=7)  
        return redirect(url_for('carregarIndex'))  
    
    return render_template('login.html', mensagem='Usuário ou senha incorretos.')  

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    name = request.form['name']
    email = request.form['email']
    user = request.form['username']
    password = request.form['password']
    password2 = request.form['confirm_password']

    if not name or not email or not user or not password or not password2:
        return render_template('cadastro.html', mensagem = 'Preencha todos os campos')

    if password == password2:  
        if user not in users: 
            users[user] = password  
            return redirect(url_for('paginaLogin'))  
        else:
            return render_template('cadastro.html', mensagem='Este nome de usuário já está em uso.')  
    else:
        return render_template('cadastro.html', mensagem='As senhas não coincidem.')  

if __name__ == '__main__':
    app.run(debug=True)
