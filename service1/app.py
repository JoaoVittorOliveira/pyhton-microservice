from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lógica de autenticação aqui
        return jsonify({'message': 'Usuário autenticado com sucesso!'})
    else:
        # Se for uma solicitação GET, retorne uma mensagem explicando 
        #que a rota só aceita solicitações POST
        return jsonify(
             {'message': 'Essa rota so aceita solicitacoes POST'}), 405

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)