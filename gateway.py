from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/gateway', methods=['GET'])
def home():
    return "Gateway funcionando"

@app.route('/gateway/cursos', methods=['GET'])
def cursos():
    response = requests.get('http://127.0.0.1:5001/cursos')
    print("RESPOSTA ", response.json())
    return response.json()

if __name__ == '__main__':
    app.run(debug=True, port=5000)