import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import grpc
from concurrent import futures
import time

# Importar os arquivos gRPC gerados
from grpc_services import services_pb2
from grpc_services import services_pb2_grpc

class GatewayService:
    def __init__(self):
        # Conexões com os serviços
        self.cursos_channel = grpc.insecure_channel('localhost:50051')
        self.cursos_stub = services_pb2_grpc.CursosServiceStub(self.cursos_channel)
        
        self.chatbot_channel = grpc.insecure_channel('localhost:50052')
        self.chatbot_stub = services_pb2_grpc.ChatbotServiceStub(self.chatbot_channel)
        
        self.cpar_channel = grpc.insecure_channel('localhost:50053')
        self.cpar_stub = services_pb2_grpc.CPARServiceStub(self.cpar_channel)
        
        self.notificacoes_channel = grpc.insecure_channel('localhost:50054')
        self.notificacoes_stub = services_pb2_grpc.NotificacoesServiceStub(self.notificacoes_channel)
        
        self.insights_channel = grpc.insecure_channel('localhost:50055')
        self.insights_stub = services_pb2_grpc.InsightsServiceStub(self.insights_channel)
        
        self.midia_channel = grpc.insecure_channel('localhost:50056')
        self.midia_stub = services_pb2_grpc.MidiaConteudoServiceStub(self.midia_channel)
    
    def call_cursos_status(self):
        try:
            response = self.cursos_stub.GetCursosStatus(services_pb2.Empty())
            return response.message
        except grpc.RpcError as e:
            return f"Erro ao conectar com Cursos: {e.details()}"
    
    def call_chatbot_status(self):
        try:
            response = self.chatbot_stub.GetChatbotStatus(services_pb2.Empty())
            return response.message
        except grpc.RpcError as e:
            return f"Erro ao conectar com Chatbot: {e.details()}"
    
    def call_cpar_status(self):
        try:
            response = self.cpar_stub.GetCPARStatus(services_pb2.Empty())
            return response.message
        except grpc.RpcError as e:
            return f"Erro ao conectar com CPAR: {e.details()}"
    
    def call_notificacoes_status(self):
        try:
            response = self.notificacoes_stub.GetNotificacoesStatus(services_pb2.Empty())
            return response.message
        except grpc.RpcError as e:
            return f"Erro ao conectar com Notificações: {e.details()}"
    
    def call_insights_status(self):
        try:
            response = self.insights_stub.GetInsightsStatus(services_pb2.Empty())
            return response.message
        except grpc.RpcError as e:
            return f"Erro ao conectar com Insights: {e.details()}"
    
    def call_midia_status(self):
        try:
            response = self.midia_stub.GetMidiaStatus(services_pb2.Empty())
            return response.message
        except grpc.RpcError as e:
            return f"Erro ao conectar com Mídia: {e.details()}"
    
    def close_connections(self):
        self.cursos_channel.close()
        self.chatbot_channel.close()
        self.cpar_channel.close()
        self.notificacoes_channel.close()
        self.insights_channel.close()
        self.midia_channel.close()

def test_gateway():
    """Função para testar as conexões com todos os serviços"""
    gateway = GatewayService()
    
    print("=== Testando Gateway gRPC ===")
    print(f"Cursos: {gateway.call_cursos_status()}")
    print(f"Chatbot: {gateway.call_chatbot_status()}")
    print(f"CPAR: {gateway.call_cpar_status()}")
    print(f"Notificações: {gateway.call_notificacoes_status()}")
    print(f"Insights: {gateway.call_insights_status()}")
    print(f"Mídia: {gateway.call_midia_status()}")
    print("=== Teste concluído ===")
    
    gateway.close_connections()

if __name__ == '__main__':
    test_gateway()