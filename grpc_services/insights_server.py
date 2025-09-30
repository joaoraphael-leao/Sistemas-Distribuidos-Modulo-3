#!/usr/bin/env python3
"""
Servidor de Insights - Implementação gRPC Otimizada
"""

import sys
import os
import grpc
from concurrent import futures
import logging
import random

# Configuração de path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Imports gRPC
from grpc_services import services_pb2, services_pb2_grpc

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InsightsServiceServicer(services_pb2_grpc.InsightsServiceServicer):
    """Servicer para o serviço de insights"""
    
    def __init__(self):
        self.metrics_collected = 0
        logging.info("📊 Serviço de Insights inicializado")
    
    def GetInsightsStatus(self, request, context):
        """Retorna status do serviço"""
        return services_pb2.StatusResponse(
            message=f"Insights ativos - {self.metrics_collected} métricas coletadas"
        )
    
    def RegisterMetrics(self, request, context):
        """Registra métricas do sistema"""
        try:
            self.metrics_collected += 1
            
            # Simula coleta de métricas
            metrics_data = {
                'interaction_id': request.id_interacao,
                'timestamp': self.metrics_collected,
                'response_time': random.uniform(0.1, 2.0),
                'user_satisfaction': random.uniform(3.5, 5.0)
            }
            
            logging.info(f"📈 Métricas registradas: ID {request.id_interacao}")
            
            return services_pb2.RegisterMetricsResponse(
                message=f"Métricas registradas com sucesso [ID: {request.id_interacao}]",
                id_interacao=request.id_interacao,
                insights_servico=services_pb2.StatusResponse(
                    message="Insights processados com sucesso"
                )
            )
            
        except Exception as e:
            logging.error(f"❌ Erro ao registrar métricas: {e}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Erro interno: {str(e)}")
            return services_pb2.RegisterMetricsResponse(
                message=f"Erro ao registrar métricas: {str(e)}",
                id_interacao=request.id_interacao,
                insights_servico=services_pb2.StatusResponse(
                    message="Erro no processamento de insights"
                )
            )

def serve():
    """Inicia o servidor de insights"""
    port = 8085
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Adiciona o servicer
    services_pb2_grpc.add_InsightsServiceServicer_to_server(
        InsightsServiceServicer(), server
    )
    
    # Configura porta
    listen_addr = f'localhost:{port}'
    server.add_insecure_port(listen_addr)
    
    try:
        server.start()
        logging.info(f"📊 Servidor de Insights rodando em {listen_addr}")
        server.wait_for_termination()
    except KeyboardInterrupt:
        logging.info("🛑 Parando servidor de insights...")
        server.stop(0)
    except Exception as e:
        logging.error(f"❌ Erro no servidor: {e}")

if __name__ == '__main__':
    serve()