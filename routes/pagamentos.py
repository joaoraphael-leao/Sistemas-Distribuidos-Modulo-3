from config import create_app, request, jsonify, requests

app = create_app()
port = 5007

@app.route('/pagamentos', methods=['GET'])
def pagamentos():
    message = "Servico de Pagamentos Conectado -> Endpoint GET /cursos"
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True, port=port)