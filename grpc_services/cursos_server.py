#!/usr/bin/env python3
"""
Cursos Service - gRPC Server
Gestão de cursos, inscrições e notificações
"""

import sys
import os
import grpc
from concurrent import futures
import time

# Configuração de ambiente
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Imports gRPC
from grpc_services import services_pb2, services_pb2_grpc

class CursosServiceServicer(services_pb2_grpc.CursosServiceServicer):
    """Implementação otimizada do serviço de Cursos"""
    
    def GetCursosStatus(self, request, context):
        """Status do serviço"""
        return services_pb2.StatusResponse(
            message="📚 Cursos Service ativo - Gestão de cursos e inscrições"
        )
    
    def GetUserCourses(self, request, context):
        """Lista cursos do usuário"""
        try:
            # Simulação otimizada de cursos
            courses = [
                services_pb2.Course(id=1, nome="Python Fundamentals"),
                services_pb2.Course(id=2, nome="Data Science Básico"),
                services_pb2.Course(id=3, nome="Machine Learning Intro")
            ]
            
            return services_pb2.GetUserCoursesResponse(
                message=f"📚 Cursos encontrados para usuário {request.id_usuario}",
                cursos_inscritos=courses
            )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Erro ao buscar cursos: {str(e)}')
            return services_pb2.GetUserCoursesResponse()
    
    def GetCourseMedia(self, request, context):
        """Busca mídia de um curso"""
        try:
            # Simulação de integração com serviço de mídia
            media_content = f"📺 Conteúdo multimídia do curso {request.id_curso}: vídeos, slides, exercícios práticos"
            
            return services_pb2.GetCourseMediaResponse(
                midia_curso=media_content
            )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Erro ao buscar mídia: {str(e)}')
            return services_pb2.GetCourseMediaResponse()
    
    def AskQuestion(self, request, context):
        """Integração com chatbot para dúvidas"""
        try:
            # Em um sistema real, faria chamada gRPC para o chatbot
            # Aqui simularemos a resposta
            resposta_simulada = f"""🤖 Processando dúvida sobre o curso {request.id_curso}:

Contexto: {request.aula_contexto}
Pergunta: {request.duvida}

💡 Esta funcionalidade integra com o Chatbot Service para respostas inteligentes.
Em produção, seria feita uma chamada gRPC para o serviço de Chatbot."""

            return services_pb2.AskQuestionResponse(
                resposta=resposta_simulada
            )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Erro ao processar dúvida: {str(e)}')
            return services_pb2.AskQuestionResponse()
    
    def SendNotification(self, request, context):
        """Envio de notificações"""
        try:
            # Simulação de integração com serviço de notificações
            notificacao_response = services_pb2.StatusResponse(
                message="📱 Notificação enviada com sucesso"
            )
            
            return services_pb2.SendNotificationResponse(
                message=f"📚 Notificação de curso enviada para usuário {request.id_usuario}",
                notificacao_servico=notificacao_response
            )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Erro ao enviar notificação: {str(e)}')
            return services_pb2.SendNotificationResponse()

def serve():
    """Inicia o servidor gRPC otimizado"""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_CursosServiceServicer_to_server(CursosServiceServicer(), server)
    
    listen_addr = 'localhost:8081'
    server.add_insecure_port(listen_addr)
    
    print("Cursos Service iniciando na porta 8081...")
    print("Integrado com: Chatbot, Notificações, Mídia")
    
    server.start()
    
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        print("\nParando Cursos Service...")
        server.stop(0)

if __name__ == '__main__':
    serve()