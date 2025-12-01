from flask import Flask, request, jsonify
import redis
import os

app = Flask(__name__)

# Conexão com o Banco NoSQL Redis
# O host 'redis_db' é o nome do serviço no docker-compose
r = redis.Redis(host='redis_db', port=6379, decode_responses=True)

@app.route('/')
def home():
    return '''
    <h1>Trabalho SO - Python + Redis</h1>
    <p>Para adicionar: /add?nome=SeuNome</p>
    <p>Para listar: /users</p>
    '''

@app.route('/add')
def add():
    nome = request.args.get('nome')
    if nome:
        r.rpush('usuarios', nome)
        return f"Usuario {nome} salvo no Redis!"
    return "Faltou o nome na URL."

@app.route('/users')
def users():
    lista = r.lrange('usuarios', 0, -1)
    return jsonify(lista)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
