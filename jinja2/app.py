from flask import Flask, render_template
app = Flask(__name__)
@app.route('/user/<username>')
def profile(username):
    return render_template("profile.html",user=username)

@app.route('/')
def home():
    produtos = ["Maçã", "Banana", "Laranja"]
    logado=True
    return render_template("home.html", produtos=produtos, logado=logado)
if __name__ == "__main__":
    app.run(debug=True)