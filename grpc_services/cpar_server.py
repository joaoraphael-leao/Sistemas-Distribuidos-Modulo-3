#!/usr/bin/env python3
"""
CPAR Service - gRPC Server
Gestão de agendamentos e notificações
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

class CPARServiceServicer(services_pb2_grpc.CPARServiceServicer):
    """Implementação otimizada do serviço CPAR"""
    
    def GetStatus(self, request, context):
        """Status do serviço"""
        return services_pb2.StatusResponse(
            message="📅 CPAR Service ativo - Gestão de agendamentos"
        )
    
    def NotifySchedule(self, request, context):
        """Notifica sobre agendamentos"""
        try:
            # Processamento do agendamento
            agendamento_info = f"📅 Agendamento {request.id_agendamento} processado"
            
            # Simulação de integração com notificações
            notificacao_response = services_pb2.StatusResponse(
                message="📱 Notificação de agendamento enviada"
            )
            
            return services_pb2.NotifyScheduleResponse(
                message=agendamento_info,
                id_agendamento=request.id_agendamento,
                notificacao_servico=notificacao_response
            )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Erro ao notificar agendamento: {str(e)}')
            return services_pb2.NotifyScheduleResponse()

def serve():
    """Inicia o servidor gRPC otimizado"""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_CPARServiceServicer_to_server(CPARServiceServicer(), server)
    
    listen_addr = 'localhost:8083'
    server.add_insecure_port(listen_addr)
    
    print("CPAR Service iniciando na porta 8083...")
    print("Integrado com: Notificações")
    
    server.start()
    
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        print("\nParando CPAR Service...")
        server.stop(0)

if __name__ == '__main__':
    serve()