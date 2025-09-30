#!/usr/bin/env python3
"""
Servidor de Notificações - Implementação gRPC Otimizada
"""

import sys
import os
import grpc
from concurrent import futures
import logging

# Configuração de path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Imports gRPC
from grpc_services import services_pb2, services_pb2_grpc

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationsServiceServicer(services_pb2_grpc.NotificationsServiceServicer):
    """Servicer para o serviço de notificações"""
    
    def __init__(self):
        self.notifications_sent = 0
        logging.info("Serviço de Notificações inicializado")
    
    def GetNotificacoesStatus(self, request, context):
        """Retorna status do serviço"""
        return services_pb2.StatusResponse(
            message=f"Notificações ativas - {self.notifications_sent} notificações enviadas"
        )
    
    def SendNotification(self, request, context):
        """Envia notificação para usuário"""
        try:
            self.notifications_sent += 1
            
            # Simula envio de notificação
            notification_id = f"notif_{self.notifications_sent:06d}"
            
            logging.info(f"📤 Notificação enviada para usuário {request.id_usuario}: {request.message[:50]}...")
            
            return services_pb2.SendNotificationResponse(
                message=f"Notificação enviada com sucesso [ID: {notification_id}]"
            )
            
        except Exception as e:
            logging.error(f"❌ Erro ao enviar notificação: {e}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Erro interno: {str(e)}")
            return services_pb2.SendNotificationResponse(
                message=f"Erro ao enviar notificação: {str(e)}"
            )

def serve():
    """Inicia o servidor de notificações"""
    port = 8084
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Adiciona o servicer
    services_pb2_grpc.add_NotificationsServiceServicer_to_server(
        NotificationsServiceServicer(), server
    )
    
    # Configura porta
    listen_addr = f'localhost:{port}'
    server.add_insecure_port(listen_addr)
    
    try:
        server.start()
        logging.info(f"Servidor de Notificações rodando em {listen_addr}")
        server.wait_for_termination()
    except KeyboardInterrupt:
        logging.info("Parando servidor de notificações...")
        server.stop(0)
    except Exception as e:
        logging.error(f"❌ Erro no servidor: {e}")

if __name__ == '__main__':
    serve()