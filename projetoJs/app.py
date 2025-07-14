from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'ana_lindona'

@app.route('/')
def index():
    return redirect(url_for('registrarUsuario'))

@app.route('/registrarUsuario', methods=['GET', 'POST'])
def registrarUsuario():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']


        # Validação simples do lado do servidor
        if not username or not email or not password:
            flash('Todos os campos são obrigatórios!', 'danger')
        else:
            flash(f'Usuário {username} cadastrado com sucesso!', 'success')
            return redirect(url_for('register'))

        # flash(): Armazena uma mensagem que será exibida na próxima requisição. Isso
        # é útil para fornecer mensagens ao usuário.

    return render_template('formulario.html')
                           
if __name__ == '__main__':
    app.run(debug=True)