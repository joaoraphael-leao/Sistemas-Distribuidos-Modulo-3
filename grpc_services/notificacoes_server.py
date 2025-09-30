import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import grpc
from concurrent import futures
import time

# Importar os arquivos gRPC gerados
from grpc_services import services_pb2
from grpc_services import services_pb2_grpc

class NotificacoesServiceServicer(services_pb2_grpc.NotificacoesServiceServicer):
    def GetNotificacoesStatus(self, request, context):
        return services_pb2.StatusResponse(
            message="Servico de Notificacoes conectado via gRPC -> Endpoint GetNotificacoesStatus"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_NotificacoesServiceServicer_to_server(NotificacoesServiceServicer(), server)
    
    listen_addr = '0.0.0.0:50054'
    server.add_insecure_port(listen_addr)
    
    print(f"Servidor gRPC de Notificacoes iniciando na porta 50054...")
    server.start()
    
    try:
        while True:
            time.sleep(86400)  # 1 dia
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()