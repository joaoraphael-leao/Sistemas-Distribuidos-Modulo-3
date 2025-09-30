import sys
import os
from dotenv import load_dotenv
import google.generativeai as gemini

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env'))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import grpc
from concurrent import futures
import time

# Importar os arquivos gRPC gerados
from grpc_services import services_pb2
from grpc_services import services_pb2_grpc

# Configurar Gemini
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
gemini.configure(api_key=GEMINI_API_KEY)
model = gemini.GenerativeModel("gemini-2.0-flash")

class ChatbotServiceServicer(services_pb2_grpc.ChatbotServiceServicer):
    def GetChatbotStatus(self, request, context):
        return services_pb2.StatusResponse(
            message="Servico de Chatbot conectado via gRPC -> Endpoint GetChatbotStatus"
        )
    
    def ResolveDuvida(self, request, context):
        try:
            # Validação dos campos obrigatórios
            if not request.duvida:
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details("Campo 'duvida' é obrigatório")
                return services_pb2.ChatbotDuvidaResponse()
                
            if not request.aula_contexto:
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details("Campo 'aula_contexto' é obrigatório")
                return services_pb2.ChatbotDuvidaResponse()
            
            resposta = self.call_gemini_api(request.duvida, request.aula_contexto)
            print(f"gRPC - Resposta Gemini: {resposta}")
            
            return services_pb2.ChatbotDuvidaResponse(resposta=resposta)
            
        except Exception as e:
            print(f"Erro no gRPC ResolveDuvida: {str(e)}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Erro interno do servidor: {str(e)}")
            return services_pb2.ChatbotDuvidaResponse()
    
    def RegisterMetrics(self, request, context):
        try:
            message = f"Servico de Chatbot registrando metricas via gRPC da interacao {request.id_interacao}"
            
            # Simular resposta do serviço de insights
            insights_response = services_pb2.StatusResponse(
                message="Servico de Insights via gRPC"
            )
            
            return services_pb2.RegisterMetricsResponse(
                message=message,
                id_interacao=request.id_interacao,
                insights_servico=insights_response
            )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Erro ao registrar métricas: {str(e)}')
            return services_pb2.RegisterMetricsResponse()
    
    def call_gemini_api(self, duvida, aula_contexto):
        try:
            message = f"Aula Contexto: {aula_contexto}\nDuvida: {duvida}\n\nGemini, por favor solucione essa dúvida, responda apenas com texto"
            response = model.generate_content(message)
            return response.text
        except Exception as e:
            print(f"Erro na API do Gemini: {str(e)}")
            return f"Erro ao processar a dúvida: {str(e)}"

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_ChatbotServiceServicer_to_server(ChatbotServiceServicer(), server)
    
    # Usar porta comum para rede corporativa
    listen_addr = 'localhost:8082'
    server.add_insecure_port(listen_addr)
    
    print(f"Servidor gRPC de Chatbot iniciando na porta 8082...")
    server.start()
    
    try:
        while True:
            time.sleep(86400)  # 1 dia
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()