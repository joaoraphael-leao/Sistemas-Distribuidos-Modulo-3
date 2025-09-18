import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import create_app, request, jsonify, requests

app = create_app()
port = 5004

@app.route('/identidade', methods=['GET'])
def identidade():
    message = "Servico de Identiadade Conectado -> Endpoint GET /cursos"
    return jsonify(message)

@app.route('/identidade/usuario_logado', methods=['GET'])
def usuario_logado():
    response = {
        "message": "Servico de Identidade Conectado -> Endpoint GET /identidade/usuario_logado",
        "id_usuario": 1
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=port)