#!/usr/bin/env python3
"""
Servidor de Insights - Implementação gRPC
Sistema distribuído para coleta e análise de métricas de desempenho
"""

import sys
import os
import grpc
import logging
import random
import time
from concurrent import futures
from datetime import datetime

# Configuração de path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Imports gRPC
from grpc_services import services_pb2, services_pb2_grpc

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class InsightsServiceServicer(services_pb2_grpc.InsightsServiceServicer):
    """
    Servicer para o serviço de insights
    Responsável por coletar, processar e armazenar métricas do sistema
    """

    def __init__(self):
        """Inicializa o serviço de insights"""
        self.metrics_collected = 0
        self.metrics_data = []
        self.start_time = datetime.now()
        logger.info("📊 Serviço de Insights inicializado")

    def GetStatus(self, request, context):
        """
        Retorna o status atual do serviço de insights
        
        Args:
            request: Requisição de status
            context: Contexto gRPC
            
        Returns:
            StatusResponse: Status do serviço
        """
        uptime = datetime.now() - self.start_time
        uptime_str = str(uptime).split('.')[0]  # Remove microsegundos
        
        return services_pb2.StatusResponse(
            message=f"[OK] Insights ativos - {self.metrics_collected} metricas coletadas | Uptime: {uptime_str}"
        )

    def GetInsightsStatus(self, request, context):
        """
        Retorna o status atual do serviço de insights (método específico do protobuf)
        
        Args:
            request: Requisição de status
            context: Contexto gRPC
            
        Returns:
            StatusResponse: Status do serviço
        """
        uptime = datetime.now() - self.start_time
        uptime_str = str(uptime).split('.')[0]  # Remove microsegundos
        
        return services_pb2.StatusResponse(
            message=f"[OK] Insights ativos - {self.metrics_collected} metricas coletadas | Uptime: {uptime_str}"
        )

    def RegisterMetrics(self, request, context):
        """
        Registra métricas do sistema
        
        Args:
            request: Dados da métrica a ser registrada
            context: Contexto gRPC
            
        Returns:
            RegisterMetricsResponse: Resultado do registro
        """
        try:
            # Incrementa contador de métricas
            self.metrics_collected += 1
            
            # Simula coleta de métricas realísticas
            metrics_data = {
                'id': self.metrics_collected,
                'interaction_id': request.id_interacao,
                'timestamp': datetime.now().isoformat(),
                'response_time': round(random.uniform(0.1, 2.5), 3),
                'user_satisfaction': round(random.uniform(3.5, 5.0), 2),
                'memory_usage': round(random.uniform(45.0, 85.0), 1),
                'cpu_usage': round(random.uniform(10.0, 70.0), 1)
            }
            
            # Armazena métricas (em produção seria um banco de dados)
            self.metrics_data.append(metrics_data)
            
            # Mantém apenas as últimas 1000 métricas para evitar uso excessivo de memória
            if len(self.metrics_data) > 1000:
                self.metrics_data = self.metrics_data[-1000:]
            
            logger.info(f"[INFO] Metrica registrada - ID: {request.id_interacao} | Total: {self.metrics_collected}")
            
            return services_pb2.RegisterMetricsResponse(
                message=f"[OK] Metrica registrada com sucesso [ID: {request.id_interacao}]",
                id_interacao=request.id_interacao,
                insights_servico=services_pb2.StatusResponse(
                    message="Insights Service OK"
                )
            )
            
        except Exception as e:
            error_msg = f"Erro ao registrar métrica: {str(e)}"
            logger.error(f"❌ {error_msg}")
            
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Erro interno: {str(e)}")
            
            return services_pb2.RegisterMetricsResponse(
                message=f"❌ {error_msg}",
                id_interacao=request.id_interacao,
                insights_servico=services_pb2.StatusResponse(
                    message="Insights Service ERROR"
                )
            )

    def get_metrics_summary(self):
        """
        Retorna um resumo das métricas coletadas
        
        Returns:
            dict: Resumo das métricas
        """
        if not self.metrics_data:
            return {"total": 0, "summary": "Nenhuma métrica coletada"}
        
        response_times = [m['response_time'] for m in self.metrics_data]
        satisfaction_scores = [m['user_satisfaction'] for m in self.metrics_data]
        
        return {
            "total": len(self.metrics_data),
            "avg_response_time": round(sum(response_times) / len(response_times), 3),
            "avg_satisfaction": round(sum(satisfaction_scores) / len(satisfaction_scores), 2),
            "latest_metric": self.metrics_data[-1] if self.metrics_data else None
        }


def serve(port=8085):
    """
    Inicia o servidor de insights
    
    Args:
        port (int): Porta para o servidor (padrão: 8085)
    """
    # Configuração do servidor
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Instancia e adiciona o servicer
    insights_servicer = InsightsServiceServicer()
    services_pb2_grpc.add_InsightsServiceServicer_to_server(insights_servicer, server)
    
    # Configura endereço e porta
    listen_addr = f'localhost:{port}'
    server.add_insecure_port(listen_addr)
    
    try:
        # Inicia o servidor
        server.start()
        logger.info(f"� Servidor de Insights rodando em {listen_addr}")
        logger.info("💡 Pressione Ctrl+C para parar o servidor")
        
        # Aguarda sinal de interrupção
        server.wait_for_termination()
        
    except KeyboardInterrupt:
        logger.info("🛑 Recebido sinal de interrupção")
        
        # Exibe resumo das métricas antes de parar
        summary = insights_servicer.get_metrics_summary()
        logger.info(f"📊 Resumo final: {summary}")
        
        # Para o servidor graciosamente
        logger.info("🔄 Parando servidor de insights...")
        server.stop(grace=5)
        logger.info("✅ Servidor de insights parado com sucesso")
        
    except Exception as e:
        logger.error(f"❌ Erro crítico no servidor: {e}")
        raise


def main():
    """Função principal para executar o servidor"""
    try:
        serve()
    except Exception as e:
        logger.error(f"❌ Falha ao iniciar servidor: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()