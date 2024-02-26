from flask import Flask, request, jsonify

app = Flask(__name__)

pets = []

# Rota para adicionar um novo animal de estimação
@app.route('/adicionar_pet', methods=['POST'])
def adicionar_pet():
    dados = request.get_json()
    pets.append(dados)
    return jsonify({"mensagem": "Animal de estimação adicionado com sucesso!"})

# Rota para listar todos os animais de estimação
@app.route('/listar_pets', methods=['GET'])
def listar_pets():
    return jsonify(pets)

# Rota para atualizar informações de um animal de estimação
@app.route('/atualizar_pet/<int:id>', methods=['PUT'])
def atualizar_pet(id):
    dados = request.get_json()
    if id < len(pets):
        pets[id] = dados
        return jsonify({"mensagem": "Informações do animal de estimação atualizadas com sucesso!"})
    else:
        return jsonify({"erro": "ID do animal de estimação não encontrado."})

# Rota para excluir um animal de estimação
@app.route('/excluir_pet/<int:id>', methods=['DELETE'])
def excluir_pet(id):
    if id < len(pets):
        del pets[id]
        return jsonify({"mensagem": "Animal de estimação excluído com sucesso!"})
    else:
        return jsonify({"erro": "ID do animal de estimação não encontrado."})

if __name__ == '__main__':
    app.run(debug=True)
