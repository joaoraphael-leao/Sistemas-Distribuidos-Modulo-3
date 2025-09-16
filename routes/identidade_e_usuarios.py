from config import create_app, request, jsonify, requests

app = create_app()
port = 5004

@app.route('/identidade', methods=['GET'])
def identidade():
    message = "Servico de Identiadade Conectado -> Endpoint GET /cursos"
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True, port=port)