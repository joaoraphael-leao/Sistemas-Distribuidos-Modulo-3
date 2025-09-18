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

if __name__ == '__main__':
    app.run(debug=True, port=port)
