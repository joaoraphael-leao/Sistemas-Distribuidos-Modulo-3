#!/usr/bin/env python3
"""
Sistema Distribuído com gRPC - Execução Principal
Implementação otimizada sem redundâncias
"""

import sys
import os
import subprocess
import time
import signal
from concurrent.futures import ThreadPoolExecutor

# Configuração dos serviços gRPC
GRPC_SERVICES = {
    'chatbot': {
        'script': 'grpc_services/chatbot_server.py',
        'port': 8082,
        'description': '🤖 Chatbot com IA Gemini'
    },
    'cursos': {
        'script': 'grpc_services/cursos_server.py', 
        'port': 8081,
        'description': '📚 Gestão de Cursos'
    },
    'cpar': {
        'script': 'grpc_services/cpar_server.py',
        'port': 8083, 
        'description': '📅 Agendamentos CPAR'
    }
}

class GRPCSystemManager:
    """Gerenciador otimizado do sistema gRPC"""
    
    def __init__(self):
        self.processes = []
        signal.signal(signal.SIGINT, self._signal_handler)
    
    def _signal_handler(self, signum, frame):
        """Handler otimizado para parada dos serviços"""
        print("\n🛑 Parando sistema gRPC...")
        self.stop_all_services()
        sys.exit(0)
    
    def start_service(self, service_name, service_config):
        """Inicia um serviço específico"""
        try:
            print(f"🚀 Iniciando {service_config['description']}...")
            
            process = subprocess.Popen([
                sys.executable, service_config['script']
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            self.processes.append({
                'name': service_name,
                'process': process,
                'port': service_config['port']
            })
            
            # Verificação rápida de inicialização
            time.sleep(1)
            if process.poll() is None:
                print(f"✅ {service_name.capitalize()} ativo na porta {service_config['port']}")
                return True
            else:
                stdout, stderr = process.communicate()
                print(f"❌ Falha ao iniciar {service_name}: {stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Erro em {service_name}: {e}")
            return False
    
    def start_all_services(self):
        """Inicia todos os serviços de forma otimizada"""
        print("🏗️  Iniciando Sistema Distribuído gRPC")
        print("=" * 45)
        
        success_count = 0
        for service_name, service_config in GRPC_SERVICES.items():
            if self.start_service(service_name, service_config):
                success_count += 1
            time.sleep(0.5)  # Pausa mínima entre inicializações
        
        print(f"\n✨ {success_count}/{len(GRPC_SERVICES)} serviços ativos")
        
        if success_count > 0:
            print("\n🧪 Para testar:")
            print("   python grpc_services/test_client.py")
            print("\n⏹️  Pressione Ctrl+C para parar")
            
            # Loop principal otimizado
            try:
                while True:
                    time.sleep(2)
                    # Verificação rápida de saúde dos processos
                    dead_processes = [p for p in self.processes if p['process'].poll() is not None]
                    if dead_processes:
                        for p in dead_processes:
                            print(f"⚠️  Serviço {p['name']} parou inesperadamente")
                        # Remove processos mortos da lista
                        self.processes = [p for p in self.processes if p['process'].poll() is None]
            except KeyboardInterrupt:
                self._signal_handler(signal.SIGINT, None)
        else:
            print("❌ Nenhum serviço foi iniciado com sucesso")
    
    def stop_all_services(self):
        """Para todos os serviços de forma otimizada"""
        for service_info in self.processes:
            try:
                service_info['process'].terminate()
                service_info['process'].wait(timeout=3)
                print(f"✅ {service_info['name']} parado")
            except subprocess.TimeoutExpired:
                service_info['process'].kill()
                print(f"🔪 {service_info['name']} forçado a parar")
            except Exception as e:
                print(f"⚠️  Erro ao parar {service_info['name']}: {e}")
    
    def run_single_service(self, service_name):
        """Executa um serviço específico"""
        if service_name not in GRPC_SERVICES:
            print(f"❌ Serviço '{service_name}' não encontrado")
            print(f"Disponíveis: {', '.join(GRPC_SERVICES.keys())}")
            return
        
        service_config = GRPC_SERVICES[service_name]
        print(f"🚀 Iniciando {service_config['description']}...")
        
        try:
            # Execução direta para um serviço
            subprocess.run([sys.executable, service_config['script']])
        except KeyboardInterrupt:
            print(f"\n🛑 {service_name} parado")

def main():
    """Função principal otimizada"""
    manager = GRPCSystemManager()
    
    if len(sys.argv) > 1:
        # Execução de serviço específico
        service_name = sys.argv[1].lower()
        manager.run_single_service(service_name)
    else:
        # Execução de todos os serviços
        manager.start_all_services()

if __name__ == '__main__':
    main()