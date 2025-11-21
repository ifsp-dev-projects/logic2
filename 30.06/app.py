from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "segredo123"   

USUARIOS = {
    "ana": {"senha": "111", "perfil": "aluna"},
    "dudu": {"senha": "222", "perfil": "professor"},
    "admin": {"senha": "123", "perfil": "administrador"}
}

@app.route('/', methods=['GET', 'POST'])
def login():
    mensagem = ""

    if request.method == "POST":
        usuario = request.form['username']
        senha = request.form['password']

        if usuario in USUARIOS and senha == USUARIOS[usuario]["senha"]:
            session["usuario"] = usuario     
            return redirect(url_for('bemvindo'))
        else:
            mensagem = "Usuário ou senha inválidos."

    return render_template('login.html', error=mensagem)

@app.route('/bemvindo')
def bemvindo():
    if "usuario" not in session:
        return redirect(url_for('login'))

    usuario = session["usuario"]
    perfil = USUARIOS[usuario]["perfil"]

    return render_template("bemvindo.html", user=usuario, perfil=perfil)

@app.route('/logout')
def logout():
    session.clear()  
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
