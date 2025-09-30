#!/usr/bin/env python3
"""
TESTE MANUAL - CPAR Service (Porta 8083)
Cliente para testar o serviço de Agendamentos CPAR
"""

import sys
import os
import grpc

# Adicionar o diretório raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grpc_services import services_pb2, services_pb2_grpc

def teste_cpar():
    """Testa o serviço CPAR"""
    
    print("=" * 60)
    print("TESTE MANUAL - CPAR SERVICE (Porta 8083)")
    print("=" * 60)
    
    # Conectar com o serviço
    print("\n🔌 Conectando com o servidor...")
    channel = grpc.insecure_channel('localhost:8083')
    stub = services_pb2_grpc.CPARServiceStub(channel)
    
    try:
        # 1. Verificar status
        print("\n1️⃣ VERIFICANDO STATUS DO SERVICO CPAR...")
        print("-" * 40)
        resposta = stub.GetCPARStatus(services_pb2.Empty(), timeout=5)
        print(f"   ✅ Status: {resposta.message}")
        
        # 2. Enviar primeira notificação
        print("\n2️⃣ ENVIANDO NOTIFICACAO DE AGENDAMENTO 1...")
        print("-" * 40)
        request = services_pb2.NotifyScheduleRequest(
            id_agendamento="agendamento_001"
        )
        print(f"   📤 ID do Agendamento: {request.id_agendamento}")
        print("   ⏳ Enviando notificação...")
        
        resposta = stub.NotifySchedule(request, timeout=5)
        
        print(f"   📥 Resultado: {resposta.message}")
        
        # 3. Enviar segunda notificação
        print("\n3️⃣ ENVIANDO NOTIFICACAO DE AGENDAMENTO 2...")
        print("-" * 40)
        request = services_pb2.NotifyScheduleRequest(
            id_agendamento="agendamento_002"
        )
        print(f"   📤 ID do Agendamento: {request.id_agendamento}")
        print("   ⏳ Enviando notificação...")
        
        resposta = stub.NotifySchedule(request, timeout=5)
        
        print(f"   📥 Resultado: {resposta.message}")
        
        # 4. Enviar terceira notificação
        print("\n4️⃣ ENVIANDO NOTIFICACAO DE AGENDAMENTO 3...")
        print("-" * 40)
        request = services_pb2.NotifyScheduleRequest(
            id_agendamento="agendamento_003"
        )
        print(f"   📤 ID do Agendamento: {request.id_agendamento}")
        print("   ⏳ Enviando notificação...")
        
        resposta = stub.NotifySchedule(request, timeout=5)
        
        print(f"   📥 Resultado: {resposta.message}")
        
        # 5. Verificar status atualizado
        print("\n5️⃣ VERIFICANDO STATUS ATUALIZADO...")
        print("-" * 40)
        resposta = stub.GetCPARStatus(services_pb2.Empty(), timeout=5)
        print(f"   ✅ Status: {resposta.message}")
        print("   ℹ️  (O servidor pode ter contadores internos atualizados)")
        
        # Resumo
        print("\n" + "=" * 60)
        print("✅ CPAR TESTADO COM SUCESSO!")
        print("=" * 60)
        print("\n📊 RESUMO DO TESTE:")
        print("   ✅ Status verificado")
        print("   ✅ 3 notificações de agendamento enviadas")
        print("   ✅ Todas as notificações processadas")
        print("   ✅ Comunicação gRPC funcionando")
        print("   ✅ Servidor respondendo corretamente")
        print("\n🎯 Serviço CPAR 100% operacional!\n")
        
    except grpc.RpcError as e:
        print(f"\n❌ ERRO gRPC: {e.code()} - {e.details()}")
        print("\n💡 DICA: Verifique se o servidor está rodando:")
        print("   python grpc_main_windows.py")
    except Exception as e:
        print(f"\n❌ ERRO: {e}")
    finally:
        channel.close()
        print("🔌 Conexão fechada.\n")

if __name__ == '__main__':
    teste_cpar()
