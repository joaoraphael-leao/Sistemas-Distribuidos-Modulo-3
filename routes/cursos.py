from config import create_app, request, jsonify, requests

app = create_app()
port = 5001

@app.route('/cursos', methods=['GET'])
def cursos():
    message = "Servico de Cursos conectado -> Endpoint GET /cursos"
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True, port = port)