#!/usr/bin/env python3
"""
Cliente de Teste gRPC - Versão Final Otimizada
Testa todos os serviços gRPC do sistema
"""

import sys
import os
import grpc

# Configuração de ambiente
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Imports gRPC
from grpc_services import services_pb2, services_pb2_grpc

class FinalGRPCClient:
    """Cliente gRPC final para todos os testes"""
    
    def __init__(self):
        self.services = {
            'chatbot': {'port': 8082, 'stub_class': services_pb2_grpc.ChatbotServiceStub},
            'cursos': {'port': 8081, 'stub_class': services_pb2_grpc.CursosServiceStub},
            'cpar': {'port': 8083, 'stub_class': services_pb2_grpc.CPARServiceStub},
            'insights': {'port': 8085, 'stub_class': services_pb2_grpc.InsightsServiceStub}
        }
        self.channels = {}
        self.stubs = {}
        self._connect_services()
    
    def _connect_services(self):
        """Conecta com todos os serviços disponíveis"""
        for service_name, config in self.services.items():
            try:
                channel = grpc.insecure_channel(f'localhost:{config["port"]}')
                stub = config['stub_class'](channel)
                
                self.channels[service_name] = channel
                self.stubs[service_name] = stub
                
            except Exception as e:
                print(f"⚠️  Erro ao conectar com {service_name}: {e}")
    
    def test_complete_system(self):
        """Executa teste completo do sistema"""
        print("TESTE COMPLETO DO SISTEMA gRPC")
        print("=" * 50)
        
        # Testa status de todos os serviços
        active_services = self._test_all_status()
        
        if active_services > 0:
            print(f"\nTESTES FUNCIONAIS")
            print("-" * 30)
            
            # Testes específicos por serviço
            if 'chatbot' in self.stubs:
                self._test_chatbot()
            
            if 'cursos' in self.stubs:
                self._test_cursos()
            
            if 'cpar' in self.stubs:
                self._test_cpar()
            
            if 'insights' in self.stubs:
                self._test_insights()
        
        # Resumo final
        self._print_final_summary(active_services)
    
    def _test_all_status(self):
        """Testa status de todos os serviços"""
        print("STATUS DOS SERVIÇOS:")
        active_count = 0
        
        # Testa cada serviço com seu método específico
        for service_name, stub in self.stubs.items():
            try:
                if service_name == 'chatbot':
                    response = stub.GetChatbotStatus(services_pb2.Empty(), timeout=5)
                elif service_name == 'cursos':
                    response = stub.GetCursosStatus(services_pb2.Empty(), timeout=5)
                elif service_name == 'cpar':
                    response = stub.GetCPARStatus(services_pb2.Empty(), timeout=5)
                elif service_name == 'insights':
                    response = stub.GetInsightsStatus(services_pb2.Empty(), timeout=5)
                else:
                    continue
                    
                print(f"   OK - {service_name.capitalize()}: {response.message}")
                active_count += 1
            except grpc.RpcError as e:
                print(f"   ERRO - {service_name.capitalize()}: {e.code()} - {e.details()}")
            except Exception as e:
                print(f"   ERRO - {service_name.capitalize()}: {e}")
        
        return active_count
    
    def _test_chatbot(self):
        """Testa funcionalidades do chatbot"""
        print(f"\nCHATBOT:")
        try:
            request = services_pb2.ChatbotDuvidaRequest(
                aula_contexto="Teste gRPC",
                duvida="Como funciona o gRPC?"
            )
            response = self.stubs['chatbot'].ResolveDuvida(request, timeout=15)
            print(f"   OK - Resposta recebida: {len(response.resposta)} caracteres")
        except Exception as e:
            print(f"   ERRO: {e}")
    
    def _test_cursos(self):
        """Testa funcionalidades de cursos"""
        print(f"\nCURSOS:")
        try:
            request = services_pb2.GetUserCoursesRequest(id_usuario="test_123")
            response = self.stubs['cursos'].GetUserCourses(request, timeout=5)
            print(f"   OK - Cursos encontrados: {len(response.cursos_inscritos)}")
        except Exception as e:
            print(f"   ERRO: {e}")
    
    def _test_cpar(self):
        """Testa funcionalidades do CPAR"""
        print(f"\nCPAR:")
        try:
            request = services_pb2.NotifyScheduleRequest(id_agendamento="test_456")
            response = self.stubs['cpar'].NotifySchedule(request, timeout=5)
            print(f"   OK - Notificação: {response.message}")
        except Exception as e:
            print(f"   ERRO: {e}")
    
    def _test_insights(self):
        """Testa funcionalidades do insights"""
        print(f"\nINSIGHTS:")
        try:
            # Testa registro de métricas
            request = services_pb2.RegisterMetricsRequest(id_interacao="test_insights_123")
            response = self.stubs['insights'].RegisterMetrics(request, timeout=5)
            print(f"   OK - Métrica registrada: {response.message}")
        except Exception as e:
            print(f"   ERRO: {e}")
    
    def _test_notifications(self):
        """Testa funcionalidades de notificações"""
        print(f"\nNOTIFICAÇÕES:")
        try:
            request = services_pb2.SendNotificationRequest(
                id_usuario="test_123",
                message="Teste do sistema gRPC"
            )
            response = self.stubs['notifications'].SendNotification(request, timeout=5)
            print(f"   OK - Enviada: {response.message}")
        except Exception as e:
            print(f"   ERRO: {e}")
    
    def _print_final_summary(self, active_services):
        """Imprime resumo final dos testes"""
        print(f"\nRESUMO FINAL")
        print("=" * 30)
        
        total_services = len(self.services)
        print(f"Total de serviços: {total_services}")
        print(f"Serviços ativos: {active_services}")
        print(f"Serviços inativos: {total_services - active_services}")
        
        if active_services == total_services:
            print(f"\nSISTEMA 100% FUNCIONAL!")
        elif active_services > 0:
            print(f"\nSistema parcialmente ativo")
        else:
            print(f"\nSistema inativo - Execute: python grpc_main_windows.py")
    
    def close_connections(self):
        """Fecha todas as conexões"""
        for channel in self.channels.values():
            try:
                channel.close()
            except:
                pass

def main():
    """Função principal"""
    client = FinalGRPCClient()
    
    try:
        client.test_complete_system()
    finally:
        client.close_connections()

if __name__ == '__main__':
    main()