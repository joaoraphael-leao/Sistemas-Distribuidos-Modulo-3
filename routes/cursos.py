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
    return jsonify(message)


if __name__ == '__main__':
    app.run(debug=True, port = port)