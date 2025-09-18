import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import create_app, request, jsonify, requests

app = create_app()
port = 5008

@app.route('/midia_conteudo', methods=['GET'])
def midia_conteudo():
    message = "Servico de Midia e Conteudo Conectado -> Endpoint GET /midia_conteudo"
    return jsonify(message)

@app.route('/midia_conteudo/<id_curso>', methods=['GET'])
def midia_conteudo_curso(id_curso):
    response = {
        "message": "Servico de Midia e Conteudo Conectado -> Endpoint GET /midia_conteudo/" + id_curso,
        "midia_curso": {
            "id": id_curso,
            "dados_midia": {
                "nome": "Midia 1",
                "descricao": "Descricao da Midia 1",
            },
        }
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=port)
