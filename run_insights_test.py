#!/usr/bin/env python3
"""
Script para iniciar servidor e testar automaticamente
Resolve o problema de coordenação entre servidor e cliente
"""

import subprocess
import time
import sys
import os
import signal

def run_server_and_test():
    """Inicia servidor e executa testes"""
    
    print("🚀 INICIANDO SERVIDOR E TESTE AUTOMÁTICO")
    print("=" * 50)
    
    # Inicia o servidor em processo separado
    print("📊 1. Iniciando servidor de insights...")
    server_process = subprocess.Popen([
        sys.executable, "grpc_services/insights_server.py"
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    try:
        # Aguarda o servidor inicializar
        print("⏳ 2. Aguardando servidor inicializar (3 segundos)...")
        time.sleep(3)
        
        # Verifica se o servidor ainda está rodando
        if server_process.poll() is not None:
            stdout, stderr = server_process.communicate()
            print(f"❌ Servidor falhou ao iniciar:")
            print(f"STDOUT: {stdout}")
            print(f"STDERR: {stderr}")
            return False
        
        print("✅ 3. Servidor iniciado! Executando testes...")
        
        # Executa o teste
        test_result = subprocess.run([
            sys.executable, "test_insights_only.py"
        ], capture_output=True, text=True)
        
        print("📋 4. Resultado do teste:")
        print(test_result.stdout)
        
        if test_result.stderr:
            print("⚠️ Erros/Avisos:")
            print(test_result.stderr)
        
        # Verifica resultado
        if "*** TODOS OS TESTES PASSARAM! ***" in test_result.stdout:
            print("🎯 TESTE BEM-SUCEDIDO!")
            return True
        else:
            print("❌ TESTE FALHOU!")
            return False
            
    finally:
        # Para o servidor
        print("\n🛑 5. Parando servidor...")
        try:
            if os.name == 'nt':  # Windows
                server_process.terminate()
            else:  # Unix/Linux
                server_process.send_signal(signal.SIGINT)
            
            # Aguarda o servidor parar graciosamente
            try:
                server_process.wait(timeout=5)
                print("✅ Servidor parado graciosamente")
            except subprocess.TimeoutExpired:
                server_process.kill()
                print("🔪 Servidor forçado a parar")
                
        except Exception as e:
            print(f"⚠️ Erro ao parar servidor: {e}")

if __name__ == "__main__":
    success = run_server_and_test()
    sys.exit(0 if success else 1)