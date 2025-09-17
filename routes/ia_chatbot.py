import sys
import os
from dotenv import load_dotenv
import google.generativeai as gemini
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env'))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import create_app, request, jsonify, requests


GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
gemini.configure(api_key = GEMINI_API_KEY)
model = gemini.GenerativeModel("gemini-2.0-flash")

app = create_app()
port = 5003

@app.route('/chatbot', methods=['GET'])
def chatbot():
    message = "Servico de Chatbot Conectado -> Endpoint GET /cursos"
    return jsonify(GEMINI_API_KEY)


@app.route('/chatbot/duvida', methods=['POST'])
def tirar_duvida():
    try:
        payload = request.json
        
        # Validação do payload
        if not payload:
            return jsonify({"erro": "Payload JSON é obrigatório"}), 400
            
        aula_contexto = payload.get('aula_contexto')
        duvida = payload.get('duvida')
        
        # Validação dos campos obrigatórios
        if not duvida:
            return jsonify({"erro": "Campo 'duvida' é obrigatório"}), 400
            
        if not aula_contexto:
            return jsonify({"erro": "Campo 'aula_contexto' é obrigatório"}), 400
        
        resposta = call_gemini_api(duvida, aula_contexto)
        print(resposta)
        return jsonify({"resposta": resposta})
        
    except Exception as e:
        print(f"Erro no endpoint /chatbot/duvida: {str(e)}")
        return jsonify({"erro": "Erro interno do servidor"}), 500


def call_gemini_api(duvida, aula_contexto):
    try:
        message = f"Aula Contexto: {aula_contexto}\nDuvida: {duvida}\n\nGemini, por favor solucione essa dúvida, responda apenas com texto"
        response = model.generate_content(message)
        return response.text  # Corrigido: era response.toString()
    except Exception as e:
        print(f"Erro na API do Gemini: {str(e)}")
        return f"Erro ao processar a dúvida: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, port=port)