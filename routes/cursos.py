from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/cursos', methods=['GET'])
def cursos():
    message = "Cursos funcionando -> Endpoint GET /cursos"
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True, port=5001)