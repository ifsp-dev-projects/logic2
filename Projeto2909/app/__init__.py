from flask import Flask, request
import logging

logging.basicConfig(level=logging.INFO)

app=Flask(__name__)
app.config['SECRET_KEY']='  uma-chave-secreta-muito-forte'

@app.before_request
def log_request_info():
    app.logger.info('Requisição Recebida %s %s', request.method, request.path)

from app import routes