import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import grpc
from grpc_services import services_pb2
from grpc_services import services_pb2_grpc

class GRPCClient:
    def __init__(self):
        # Conexões com os serviços (portas atualizadas para rede corporativa)
        self.cursos_channel = grpc.insecure_channel('localhost:8081')
        self.cursos_stub = services_pb2_grpc.CursosServiceStub(self.cursos_channel)
        
        self.chatbot_channel = grpc.insecure_channel('localhost:8082')
        self.chatbot_stub = services_pb2_grpc.ChatbotServiceStub(self.chatbot_channel)
        
        self.cpar_channel = grpc.insecure_channel('localhost:8083')
        self.cpar_stub = services_pb2_grpc.CPARServiceStub(self.cpar_channel)
    
    def test_cursos_service(self):
        print("\n=== Testando Serviço de Cursos ===")
        
        # Teste 1: Status
        try:
            response = self.cursos_stub.GetCursosStatus(services_pb2.Empty())
            print(f"Status: {response.message}")
        except grpc.RpcError as e:
            print(f"Erro no status: {e}")
        
        # Teste 2: Buscar cursos do usuário
        try:
            request = services_pb2.GetUserCoursesRequest(id_usuario="123")
            response = self.cursos_stub.GetUserCourses(request)
            print(f"Cursos do usuário: {response.message}")
            for curso in response.cursos_inscritos:
                print(f"  - Curso {curso.id}: {curso.nome}")
        except grpc.RpcError as e:
            print(f"Erro ao buscar cursos: {e}")
        
        # Teste 3: Enviar notificação
        try:
            request = services_pb2.SendNotificationRequest(
                id_usuario="123",
                message="Teste de notificação"
            )
            response = self.cursos_stub.SendNotification(request)
            print(f"Notificação: {response.message}")
        except grpc.RpcError as e:
            print(f"Erro ao enviar notificação: {e}")
    
    def test_chatbot_service(self):
        print("\n=== Testando Serviço de Chatbot ===")
        
        # Teste 1: Status
        try:
            response = self.chatbot_stub.GetChatbotStatus(services_pb2.Empty())
            print(f"Status: {response.message}")
        except grpc.RpcError as e:
            print(f"Erro no status: {e}")
        
        # Teste 2: Resolver dúvida
        try:
            request = services_pb2.ChatbotDuvidaRequest(
                aula_contexto="Aula de Python Condicionais",
                duvida="Como fazer um if else em Python?"
            )
            response = self.chatbot_stub.ResolveDuvida(request)
            print(f"Resposta da dúvida: {response.resposta}")
        except grpc.RpcError as e:
            print(f"Erro ao resolver dúvida: {e}")
        
        # Teste 3: Registrar métricas
        try:
            request = services_pb2.RegisterMetricsRequest(id_interacao="interacao_123")
            response = self.chatbot_stub.RegisterMetrics(request)
            print(f"Métricas: {response.message}")
        except grpc.RpcError as e:
            print(f"Erro ao registrar métricas: {e}")
    
    def test_cpar_service(self):
        print("\n=== Testando Serviço CPAR ===")
        
        # Teste 1: Status
        try:
            response = self.cpar_stub.GetCPARStatus(services_pb2.Empty())
            print(f"Status: {response.message}")
        except grpc.RpcError as e:
            print(f"Erro no status: {e}")
        
        # Teste 2: Notificar agendamento
        try:
            request = services_pb2.NotifyScheduleRequest(id_agendamento="agend_456")
            response = self.cpar_stub.NotifySchedule(request)
            print(f"Notificação de agendamento: {response.message}")
        except grpc.RpcError as e:
            print(f"Erro ao notificar agendamento: {e}")
    
    def close_connections(self):
        self.cursos_channel.close()
        self.chatbot_channel.close()
        self.cpar_channel.close()

def main():
    client = GRPCClient()
    
    try:
        client.test_cursos_service()
        client.test_chatbot_service()
        client.test_cpar_service()
    finally:
        client.close_connections()

if __name__ == '__main__':
    main()