import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import grpc
from concurrent import futures
import time

# Importar os arquivos gRPC gerados
from grpc_services import services_pb2
from grpc_services import services_pb2_grpc

# Importar módulos existentes para reutilizar lógica
import requests
from config import create_app

class CursosServiceServicer(services_pb2_grpc.CursosServiceServicer):
    def GetCursosStatus(self, request, context):
        return services_pb2.StatusResponse(
            message="Servico de Cursos conectado via gRPC -> Endpoint GetCursosStatus"
        )
    
    def GetUserCourses(self, request, context):
        try:
            message = f"Servico de Cursos conectado via gRPC - Vendo cursos do usuario de id: {request.id_usuario}"
            
            # Simular cursos do usuário
            course1 = services_pb2.Course(id=1, nome="Curso 1")
            
            return services_pb2.GetUserCoursesResponse(
                message=message,
                cursos_inscritos=[course1]
            )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Erro interno: {str(e)}')
            return services_pb2.GetUserCoursesResponse()
    
    def GetCourseMedia(self, request, context):
        try:
            # Fazer chamada para o serviço de mídia via gRPC
            # Por agora, simular a resposta
            return services_pb2.GetCourseMediaResponse(
                midia_curso=f"Midia do curso {request.id_curso}"
            )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Erro ao buscar mídia: {str(e)}')
            return services_pb2.GetCourseMediaResponse()
    
    def AskQuestion(self, request, context):
        try:
            # Simular chamada para o chatbot via gRPC
            # Por agora, retornar resposta simulada
            return services_pb2.AskQuestionResponse(
                resposta=f"Resposta simulada para a dúvida: {request.duvida}"
            )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Erro ao processar dúvida: {str(e)}')
            return services_pb2.AskQuestionResponse()
    
    def SendNotification(self, request, context):
        try:
            message = f"Servico de Cursos enviando notificacao via gRPC para usuario {request.id_usuario}"
            
            # Simular resposta do serviço de notificações
            notificacao_response = services_pb2.StatusResponse(
                message="Servico de Notificacoes via gRPC"
            )
            
            return services_pb2.SendNotificationResponse(
                message=message,
                notificacao_servico=notificacao_response
            )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Erro ao enviar notificação: {str(e)}')
            return services_pb2.SendNotificationResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_CursosServiceServicer_to_server(CursosServiceServicer(), server)
    
    # Usar porta comum para rede corporativa
    listen_addr = 'localhost:8081'
    server.add_insecure_port(listen_addr)
    
    print(f"Servidor gRPC de Cursos iniciando na porta 8081...")
    server.start()
    
    try:
        while True:
            time.sleep(86400)  # 1 dia
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()