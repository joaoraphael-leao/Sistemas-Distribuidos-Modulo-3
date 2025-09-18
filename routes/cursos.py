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

@app.route("/cursos/tirar_duvida/<id_curso>", methods=['GET'])
def tirar_duvida(id_curso):

    # id_curso já está disponível como parâmetro da função

    aula_contexto = "Aula de Python Condicionais"
    duvida = "Como fazer um if else em Python?"

    body = {
        'aula_contexto': aula_contexto,
        'duvida': duvida
    }
    
    response = requests.post("http://localhost:5003/chatbot/duvida", json=body)

    resposta_duvida = response.json()
    print(resposta_duvida)
    return jsonify(resposta_duvida)


if __name__ == '__main__':
    app.run(debug=True, port = port)