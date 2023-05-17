# API Para consultar ,Criar,Editar e Excluir Livros .

# Endpoints

""" localhost/livros (GET)
localhost/livros/id (GET)
localhost/livros/id (PUT)
localhost/livros/id (DELETE) """

from flask import Flask,jsonify,request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Mundo de Sofia',
        'autor': 'Jostein Gaarder'
    },
    {
        'id': 2,
        'titulo': 'As Violetas de Marco',
        'autor': 'Sarah Jio'
    },
    {
        'id': 3,
        'titulo': 'A Expressão do Carater de Cristo',
        'autor': 'Marcelo Almeida'
    },
    {
        'id': 4,
        'titulo': 'As cinco linguagens do amor',
        'autor': 'Gary Chapman '
    },
    {
        'id': 5,
        'titulo': 'O vendedor de senhos',
        'autor': 'Augusto Cury'
    }
]

# Consultando 
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)
# Consultando ID
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
# Editar Livro
@app.route('/livros/<int:id>',methods=['PUT'])
def editando_livro_por_id(id):
   livro_alterado = request.get_json()
   for indice,livro in enumerate(livros):
       if livro.get('id') == id:
           livros[indice].update(livro_alterado)
           return jsonify(livros[indice])
# Criando Novo Livro
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
   novo_livro = request.get_json()
   livros.append(novo_livro)
   return jsonify(livros)

# Excluindo Livros
@app.route('/livros<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify(livros) 
app.run(port=5000,host='localhost',debug=True)


