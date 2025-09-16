from config import create_app, request, jsonify, requests

port = 5002

@app.route('/cpar', methods=['GET'])
def cpar():
    message = "Servico de CPAR Conectado -> Endpoint GET /cursos"
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True, port=port)