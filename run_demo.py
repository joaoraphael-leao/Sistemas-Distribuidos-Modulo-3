#!/usr/bin/env python3

import sys
import os
import subprocess
import time
import signal

# Passo 1: Teste rápido de execução individual
def test_single_service():
    print("🧪 TESTE 1: Executando serviço individual...")
    
    try:
        print("   Iniciando servidor de Chatbot...")
        process = subprocess.Popen([
            sys.executable, 
            "grpc_services/chatbot_server.py"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Aguardar 3 segundos
        time.sleep(3)
        
        if process.poll() is None:
            print("   ✅ Servidor iniciado com sucesso!")
            
            # Testar conexão
            print("   🔗 Testando conexão...")
            test_process = subprocess.run([
                sys.executable, 
                "grpc_services/test_simple_client.py"
            ], capture_output=True, text=True, timeout=10)
            
            if test_process.returncode == 0:
                print("   ✅ Conexão funcionando!")
                result = True
            else:
                print("   ❌ Conexão falhou")
                print(f"      Erro: {test_process.stderr}")
                result = False
            
            # Parar servidor
            process.terminate()
            process.wait()
            return result
            
        else:
            stdout, stderr = process.communicate()
            print("   ❌ Servidor falhou ao iniciar")
            print(f"      STDOUT: {stdout}")
            print(f"      STDERR: {stderr}")
            return False
            
    except Exception as e:
        print(f"   ❌ Erro durante teste: {e}")
        return False

# Passo 2: Execução com feedback
def run_chatbot_with_feedback():
    print("\n🚀 EXECUTANDO CHATBOT gRPC...")
    print("   Pressione Ctrl+C para parar\n")
    
    try:
        # Executar e mostrar output em tempo real
        process = subprocess.Popen([
            sys.executable, 
            "grpc_services/chatbot_server.py"
        ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, 
           text=True, bufsize=1, universal_newlines=True)
        
        # Função para parar processo
        def signal_handler(signum, frame):
            print("\n🛑 Parando servidor...")
            process.terminate()
            process.wait()
            sys.exit(0)
        
        signal.signal(signal.SIGINT, signal_handler)
        
        # Ler output em tempo real
        for line in process.stdout:
            print(f"   {line.strip()}")
            
            # Se vir a mensagem de sucesso, mostrar como testar
            if "iniciando na porta" in line.lower():
                print("\n   🎯 COMO TESTAR (em outro terminal):")
                print("      python grpc_services/test_simple_client.py")
                print("      python all_in_one.py")
                print()
        
        process.wait()
        
    except KeyboardInterrupt:
        print("\n🛑 Parando servidor...")
        if process:
            process.terminate()
            process.wait()
    except Exception as e:
        print(f"❌ Erro: {e}")

# Passo 3: Executar tudo
def main():
    print("🎮 EXECUTADOR gRPC para Rede Corporativa")
    print("=" * 50)
    
    # Teste simples primeiro
    if test_single_service():
        print("\n✅ Teste inicial passou! O gRPC funciona na sua rede.")
        
        # Perguntar se quer continuar
        resposta = input("\n🤔 Executar servidor do Chatbot? (s/n): ").lower()
        if resposta in ['s', 'sim', 'y', 'yes']:
            run_chatbot_with_feedback()
        else:
            print("👋 Ok! Use 'python all_in_one.py' para versão sem rede.")
    else:
        print("\n❌ gRPC não funcionou. Usando versão All-in-One...")
        print("   Executando: python all_in_one.py")
        subprocess.run([sys.executable, "all_in_one.py"])

if __name__ == '__main__':
    main()