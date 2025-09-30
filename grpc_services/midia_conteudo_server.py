import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import grpc
from concurrent import futures
import time

# Importar os arquivos gRPC gerados
from grpc_services import services_pb2
from grpc_services import services_pb2_grpc

class MidiaConteudoServiceServicer(services_pb2_grpc.MidiaConteudoServiceServicer):
    def GetStatus(self, request, context):
        return services_pb2.StatusResponse(
            message="Servico de Midia e Conteudo conectado via gRPC -> Endpoint GetStatus"
        )
    
    def GetMedia(self, request, context):
        try:
            return services_pb2.GetCourseMediaResponse(
                midia_curso=f"Midia do curso {request.id_curso} via gRPC"
            )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Erro ao buscar mídia: {str(e)}')
            return services_pb2.GetCourseMediaResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_MidiaConteudoServiceServicer_to_server(MidiaConteudoServiceServicer(), server)
    
    listen_addr = '0.0.0.0:50056'
    server.add_insecure_port(listen_addr)
    
    print(f"Servidor gRPC de Midia e Conteudo iniciando na porta 50056...")
    server.start()
    
    try:
        while True:
            time.sleep(86400)  # 1 dia
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()