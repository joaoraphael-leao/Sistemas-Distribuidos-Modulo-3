from config import create_app, request, jsonify, requests

app = create_app()
port = 5006

@app.route('/notificacoes', methods=['GET'])
def notificacoes():
    message = "Servico de Notificacoes Conectado -> Endpoint GET /cursos"
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True, port=port)