from config import create_app, request, jsonify, requests

app = Flask(__name__)

@app.route('/gateway', methods=['GET'])
def home():
    return "Gateway funcionando"


@app.route('/gateway/cpar', methods=['GET'])
def cpar():
    response = requests.get('http://127.0.0.1:5001/cpar')
    return response.json()

@app.route('/gateway/cursos', methods=['GET'])
def cursos():
    response = requests.get('http://127.0.0.1:5002/cursos')
     return response.json()

@app.route('/gateway/chatbot', methods=['GET'])
def chatbot():
    response = requests.get('http://127.0.0.1:5003/chatbot')
    return response.json()

@app.route('/gateway/identidade', methods=['GET'])
def identidade():
    response = requests.get('http://127.0.0.1:5004/identidade')
    return response.json()

@app.route('/gateway/insights', methods=['GET'])
def insights():
    response = requests.get('http://127.0.0.1:5005/insights')
    return response.json()

@app.route('/gateway/notificacoes', methods=['GET'])
def notificacoes():
    response = requests.get('http://127.0.0.1:5006/notificacoes')
    return response.json()

@app.route('/gateway/pagamentos', methods=['GET'])
def pagamentos():
    response = requests.get('http://127.0.0.1:5007/pagamentos')
    return response.json()

if __name__ == '__main__':
    app.run(debug=True, port=5000)