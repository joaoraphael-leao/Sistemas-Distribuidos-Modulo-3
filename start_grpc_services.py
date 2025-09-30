#!/usr/bin/env python3

import subprocess
import sys
import os
import time
import signal

# Lista de serviços gRPC para iniciar
SERVICES = [
    ("Cursos", "grpc_services/cursos_server.py"),
    ("Chatbot", "grpc_services/chatbot_server.py"),
    ("CPAR", "grpc_services/cpar_server.py"),
    ("Notificações", "grpc_services/notificacoes_server.py"),
    ("Insights", "grpc_services/insights_server.py"),
    ("Mídia e Conteúdo", "grpc_services/midia_conteudo_server.py"),
]

processes = []

def signal_handler(signum, frame):
    """Handler para Ctrl+C"""
    print("\n🛑 Parando todos os serviços...")
    for service_name, process in processes:
        try:
            process.terminate()
            process.wait(timeout=5)
            print(f"✅ {service_name} parado.")
        except subprocess.TimeoutExpired:
            process.kill()
            print(f"🔪 {service_name} forçado a parar.")
        except Exception as e:
            print(f"❌ Erro ao parar {service_name}: {e}")
    sys.exit(0)

def start_all_services():
    """Inicia todos os serviços gRPC"""
    global processes
    
    # Registrar handler para Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    # Caminho para o python do ambiente virtual
    python_path = "C:/Users/marce/Projetos/IC/Sistemas-Distribuidos-Modulo-3/.venv/Scripts/python.exe"
    
    print("🚀 Iniciando todos os serviços gRPC...")
    
    for service_name, script_path in SERVICES:
        try:
            print(f"Iniciando {service_name}...")
            process = subprocess.Popen(
                [python_path, script_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            processes.append((service_name, process))
            time.sleep(2)  # Aguardar mais tempo entre os starts
            
            # Verificar se o processo ainda está rodando
            if process.poll() is None:
                print(f"✅ {service_name} iniciado com sucesso!")
            else:
                stdout, stderr = process.communicate()
                print(f"❌ {service_name} falhou ao iniciar:")
                if stderr:
                    print(f"   Erro: {stderr.strip()}")
                    
        except Exception as e:
            print(f"❌ Erro ao iniciar {service_name}: {e}")
    
    running_services = [name for name, proc in processes if proc.poll() is None]
    print(f"\n✅ {len(running_services)} serviços rodando: {', '.join(running_services)}")
    print("Pressione Ctrl+C para parar todos os serviços.")
    
    try:
        # Aguardar indefinidamente
        while True:
            time.sleep(1)
            # Verificar se algum processo morreu
            dead_processes = [(name, proc) for name, proc in processes if proc.poll() is not None]
            if dead_processes:
                for name, proc in dead_processes:
                    stdout, stderr = proc.communicate()
                    print(f"⚠️  {name} parou inesperadamente")
                    if stderr:
                        print(f"   Erro: {stderr.strip()}")
                processes = [(name, proc) for name, proc in processes if proc.poll() is None]
                
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)

def start_single_service(service_name):
    """Inicia um serviço específico"""
    python_path = "C:/Users/marce/Projetos/IC/Sistemas-Distribuidos-Modulo-3/.venv/Scripts/python.exe"
    
    service_map = {service[0].lower(): service[1] for service in SERVICES}
    
    if service_name.lower() in service_map:
        script_path = service_map[service_name.lower()]
        print(f"Iniciando {service_name}...")
        subprocess.run([python_path, script_path])
    else:
        print(f"Serviço '{service_name}' não encontrado.")
        print("Serviços disponíveis:", [service[0] for service in SERVICES])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        start_single_service(sys.argv[1])
    else:
        start_all_services()