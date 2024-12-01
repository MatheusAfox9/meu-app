from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configurar a URL de conexão com o banco de dados PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:senha@db:5432/meubanco'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instanciar o SQLAlchemy
db = SQLAlchemy(app)

# Definir um modelo para a tabela "Produto" no banco de dados
class Produto(db.Model):
    produto_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(500), nullable=False)
    preco = db.Column(db.Float, nullable=False)

# Rota para acessar dados de um produto
@app.route('/api/data')
def get_data():
    produto = Produto.query.first()  # Busca o primeiro produto
    if produto:
        return jsonify({
            'produto_id': produto.produto_id,
            'nome': produto.nome,
            'descricao': produto.descricao,
            'preco': produto.preco
        })
    return jsonify({'message': 'Produto não encontrado'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
