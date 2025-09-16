from config import create_app, request, jsonify, requests

app = create_app()
port = 5003

@app.route('/chatbot', methods=['GET'])
def chatbot():
    message = "Servico de Chatbot Conectado -> Endpoint GET /cursos"
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True, port=port)