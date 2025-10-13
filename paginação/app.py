from flask import Flask, render_template
from controllers.produto_controller import produto_bp

app = Flask(__name__)
app.register_blueprint(produto_bp)

@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template('404.html'), 404

@app.errorhandler(403)
def pagina_proibida(error):
    return render_template('403.html'), 403

@app.errorhandler(401)
def pagina_nao_autorizada(error):
    return render_template('401.html'), 401

if __name__ == '__main__':
    app.run(debug=True)
