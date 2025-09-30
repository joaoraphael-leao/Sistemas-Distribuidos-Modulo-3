#!/usr/bin/env python3
"""
Sistema gRPC Distribuído - Versão Compatível Windows
Execução completa de todos os serviços
"""

import subprocess
import sys
import os
import time
import signal

# Configuração dos serviços gRPC
GRPC_SERVICES = {
    'chatbot': {
        'script': 'grpc_services/chatbot_server.py',
        'port': 8082,
        'description': 'Chatbot com IA Gemini'
    },
    'cursos': {
        'script': 'grpc_services/cursos_server.py', 
        'port': 8081,
        'description': 'Gestão de Cursos'
    },
    'cpar': {
        'script': 'grpc_services/cpar_server.py',
        'port': 8083,
        'description': 'Agendamentos CPAR'
    }
}

class GRPCSystemManager:
    def __init__(self):
        self.processes = {}
        self.running = True
    
    def signal_handler(self, sig, frame):
        """Handler para Ctrl+C"""
        print("\nParando sistema gRPC...")
        self.stop_all_services()
        sys.exit(0)
    
    def start_service(self, service_name, service_config):
        """Inicia um serviço gRPC específico"""
        try:
            print(f"Iniciando {service_config['description']}...")
            
            # Inicia o processo do serviço
            process = subprocess.Popen(
                [sys.executable, service_config['script']],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1
            )
            
            # Aguarda um pouco para verificar se iniciou
            time.sleep(1)
            
            if process.poll() is None:
                # Processo ainda rodando = sucesso
                self.processes[service_name] = {
                    'process': process,
                    'name': service_name,
                    'port': service_config['port']
                }
                print(f"OK - {service_name.capitalize()} ativo na porta {service_config['port']}")
                return True
            else:
                # Processo terminou = erro
                stdout, stderr = process.communicate()
                print(f"ERRO - Falha ao iniciar {service_name}: {stderr}")
                return False
                
        except Exception as e:
            print(f"ERRO - Erro em {service_name}: {e}")
            return False
    
    def start_all_services(self):
        """Inicia todos os serviços configurados"""
        print("Iniciando Sistema Distribuído gRPC")
        print("=" * 45)
        
        success_count = 0
        
        for service_name, service_config in GRPC_SERVICES.items():
            if self.start_service(service_name, service_config):
                success_count += 1
            time.sleep(0.5)  # Pausa entre serviços
        
        print(f"\n{success_count}/{len(GRPC_SERVICES)} serviços ativos")
        
        if success_count > 0:
            print("\nPara testar:")
            print("   python grpc_services/test_client_final.py")
            print("\nPressione Ctrl+C para parar")
            
            # Monitora os serviços
            self.monitor_services()
        else:
            print("Nenhum serviço foi iniciado com sucesso")
            return False
        
        return True
    
    def monitor_services(self):
        """Monitora os serviços rodando"""
        try:
            while self.running:
                time.sleep(2)
                
                # Verifica se algum processo parou
                for service_name, p in list(self.processes.items()):
                    if p['process'].poll() is not None:
                        print(f"AVISO - Serviço {p['name']} parou inesperadamente")
                        del self.processes[service_name]
                        
        except KeyboardInterrupt:
            pass
    
    def stop_service(self, service_name):
        """Para um serviço específico"""
        if service_name in self.processes:
            service_info = self.processes[service_name]
            try:
                service_info['process'].terminate()
                service_info['process'].wait(timeout=5)
                print(f"OK - {service_info['name']} parado")
                del self.processes[service_name]
            except subprocess.TimeoutExpired:
                service_info['process'].kill()
                print(f"FORCA - {service_info['name']} finalizado")
                del self.processes[service_name]
            except Exception as e:
                print(f"ERRO - Erro ao parar {service_info['name']}: {e}")
        else:
            print(f"ERRO - Serviço '{service_name}' não encontrado")
    
    def stop_all_services(self):
        """Para todos os serviços"""
        for service_name in list(self.processes.keys()):
            self.stop_service(service_name)

def start_single_service(service_name):
    """Inicia um único serviço (para desenvolvimento)"""
    if service_name in GRPC_SERVICES:
        service_config = GRPC_SERVICES[service_name]
        print(f"Iniciando {service_config['description']}...")
        
        try:
            subprocess.run([sys.executable, service_config['script']])
        except KeyboardInterrupt:
            print(f"\n{service_name} parado")
    else:
        print(f"Serviço '{service_name}' não encontrado")
        print(f"Serviços disponíveis: {', '.join(GRPC_SERVICES.keys())}")

def main():
    """Função principal"""
    if len(sys.argv) > 1:
        # Modo serviço único
        service_name = sys.argv[1]
        start_single_service(service_name)
    else:
        # Modo sistema completo
        manager = GRPCSystemManager()
        
        # Configura handler para Ctrl+C
        signal.signal(signal.SIGINT, manager.signal_handler)
        
        manager.start_all_services()

if __name__ == '__main__':
    main()