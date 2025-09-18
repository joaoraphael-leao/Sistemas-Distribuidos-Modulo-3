import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import create_app, request, jsonify, requests

app = create_app()
port = 5007

@app.route('/pagamentos', methods=['GET'])
def pagamentos():
    message = "Servico de Pagamentos Conectado -> Endpoint GET /cursos"
    return jsonify(message)

@app.route('/pagamentos/ver_inscricoes', methods=['GET'])
def ver_inscricoes_do_usuario():

    requisicao_servico_identidade = requests.get("http://localhost:5004/identidade/usuario_logado").json()
    id_usuario = requisicao_servico_identidade["id_usuario"]

    requisicao_servico_cursos = requests.get("http://localhost:5001/cursos/ver_inscricoes_do_usuario/" + str(id_usuario)).json()
    cursos_inscritos = requisicao_servico_cursos["cursos_inscritos"]
    
    return jsonify(cursos_inscritos)
    
if __name__ == '__main__':
    app.run(debug=True, port=port)