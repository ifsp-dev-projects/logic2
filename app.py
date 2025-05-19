from flask import Flask, render_template

app=Flask(__name__)
@app.route('/bemvindo/<nome>')
def bemvindo(nome):
    return render_template('bemvindo.html', usuario=nome)
