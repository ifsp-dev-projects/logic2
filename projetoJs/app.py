from flask import Flask, render_template, request, flash, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = 'edudela'

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
            flash('Todos os campos são obrigatórios', 'danger')
        else:
            flash(f'Usuário {username} cadastrado com sucesso!', 'success')
            return redirect(url_for('registrarUsuario'))

        # flash(): Armazena uma mensagem que será exibida na próxima requisição. Isso
        # é útil para fornecer mensagens ao usuário.
    return render_template('formulario.html')

def armazenarUsuario():
     #Armazenamento: Os dados dos usuários cadastrados (username, password e senha) deverão ser armazenados em uma lista. Utilize session ou cookies para gerenciar a gravação.
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        resposta = make_response(redirect(url_for('formulario')))
        resposta.set_cookie('username', username, max_age=60*10)
                           
if __name__ == '__main__':
    app.run(debug=True)