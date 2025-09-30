import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import grpc
from concurrent import futures
import time

# Importar os arquivos gRPC gerados
from grpc_services import services_pb2
from grpc_services import services_pb2_grpc

class CPARServiceServicer(services_pb2_grpc.CPARServiceServicer):
    def GetStatus(self, request, context):
        return services_pb2.StatusResponse(
            message="Servico de CPAR conectado via gRPC -> Endpoint GetStatus"
        )
    
    def NotifySchedule(self, request, context):
        try:
            message = f"Servico de CPAR enviando notificacao via gRPC de agendamento {request.id_agendamento}"
            
            # Simular resposta do serviço de notificações
            notificacao_response = services_pb2.StatusResponse(
                message="Servico de Notificacoes via gRPC"
            )
            
            return services_pb2.NotifyScheduleResponse(
                message=message,
                id_agendamento=request.id_agendamento,
                notificacao_servico=notificacao_response
            )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Erro ao notificar agendamento: {str(e)}')
            return services_pb2.NotifyScheduleResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_CPARServiceServicer_to_server(CPARServiceServicer(), server)
    
    # Usar porta comum para rede corporativa
    listen_addr = 'localhost:8083'
    server.add_insecure_port(listen_addr)
    
    print(f"Servidor gRPC de CPAR iniciando na porta 8083...")
    server.start()
    
    try:
        while True:
            time.sleep(86400)  # 1 dia
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()