import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import create_app, request, jsonify, requests

app = create_app()
port = 5002

@app.route('/cpar', methods=['GET'])
def cpar():
    message = "Servico de CPAR Conectado -> Endpoint GET /cpar"
    return jsonify(message)

@app.route('/cpar/notificar_agendamento/<id_agendamento>', methods=['GET'])
def notificar_agendamento(id_agendamento):
    message = "Servico de CPAR enviando notificacao de agendamento " + id_agendamento
    
    response = requests.get("http://localhost:5006/notificacoes")
    notificacao_response = response.json()
    
    return jsonify({
        "message": message,
        "id_agendamento": id_agendamento,
        "notificacao_servico": notificacao_response
    })

if __name__ == '__main__':
    app.run(debug=True, port=port)