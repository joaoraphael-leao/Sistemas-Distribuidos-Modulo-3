from config import create_app, request, jsonify, requests

app = create_app()
port = 5005

@app.route('/insights', methods=['GET'])
def insights():
    message = "Servico de Insights Conectado -> Endpoint GET /cursos"
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True, port=port)