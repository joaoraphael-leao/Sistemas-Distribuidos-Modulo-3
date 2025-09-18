import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import create_app, request, jsonify, requests

app = create_app()
port = 5001

@app.route('/cursos', methods=['GET'])
def cursos():
    message = "Servico de Cursos conectado -> Endpoint GET /cursos"
    return jsonify(message)
        
@app.route('/cursos/ver_inscricoes_do_usuario/<id_usuario>', methods=['GET'])
def ver_inscricoes_do_usuario(id_usuario):
    message = "Servico de Cursos conectado Vendo cursos do usuario de id: " + id_usuario + "-> Endpoint GET /cursos/ver_inscricoes_do_usuario/" + id_usuario
    
    response = {
        "message": message,
        "cursos_inscritos": [
            {
                "id": 1,
                "nome": "Curso 1"
            }   
        ]
    }
    return jsonify(response)

@app.route("/cursos/consumir_midia_curso/<id_curso>")
def consumir_midia_curso(id_curso):
    requisicao_servico_midia_conteudo = requests.get("http://localhost:5008/midia_conteudo/" + id_curso).json()
    midia_curso = requisicao_servico_midia_conteudo["midia_curso"]
    return jsonify(midia_curso)

@app.route("/cursos/tirar_duvida/<id_curso>", methods=['POST'])
def tirar_duvida(id_curso):
    try:
        payload = request.json
        
        # Validação do payload
        if not payload:
            return jsonify({"erro": "Payload JSON é obrigatório"}), 400
            
        aula_contexto = payload.get('aula_contexto')
        duvida = payload.get('duvida')
        
        # Validação dos campos obrigatórios
        if not duvida:
            return jsonify({"erro": "Campo 'duvida' é obrigatório"}), 400
            
        if not aula_contexto:
            return jsonify({"erro": "Campo 'aula_contexto' é obrigatório"}), 400

        body = {
            'aula_contexto': aula_contexto,
            'duvida': duvida
        }
        
        response = requests.post("http://localhost:5003/chatbot/duvida", json=body)

        resposta_duvida = response.json()
        print(resposta_duvida)
        return jsonify(resposta_duvida)
        
    except Exception as e:
        print(f"Erro no endpoint /cursos/tirar_duvida: {str(e)}")
        return jsonify({"erro": "Erro interno do servidor"}), 500

@app.route("/cursos/enviar_notificacao/<id_usuario>", methods=['GET'])
def enviar_notificacao(id_usuario):
    message = "Servico de Cursos enviando notificacao para usuario " + id_usuario
    
    response = requests.get("http://localhost:5006/notificacoes")
    notificacao_response = response.json()
    
    return jsonify({
        "message": message,
        "notificacao_servico": notificacao_response
    })

@app.route("/cursos/notificar_agendamento/<id_agendamento>", methods=['GET'])
def notificar_agendamento(id_agendamento):
    message = "Servico de Cursos notificando agendamento " + id_agendamento
    
    response = requests.get("http://localhost:5006/notificacoes")
    notificacao_response = response.json()
    
    return jsonify({
        "message": message,
        "id_agendamento": id_agendamento,
        "notificacao_servico": notificacao_response
    })


if __name__ == '__main__':
    app.run(debug=True, port = port)