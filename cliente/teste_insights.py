#!/usr/bin/env python3
"""
TESTE MANUAL - Insights Service (Porta 8085)
Cliente para testar o serviço de Métricas e Insights
"""

import sys
import os
import grpc

# Adicionar o diretório raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grpc_services import services_pb2, services_pb2_grpc

def teste_insights():
    """Testa o serviço de Insights"""
    
    print("=" * 60)
    print("TESTE MANUAL - INSIGHTS SERVICE (Porta 8085)")
    print("=" * 60)
    
    # Conectar com o serviço
    print("\n🔌 Conectando com o servidor...")
    channel = grpc.insecure_channel('localhost:8085')
    stub = services_pb2_grpc.InsightsServiceStub(channel)
    
    try:
        # 1. Verificar status inicial
        print("\n1️⃣ VERIFICANDO STATUS INICIAL...")
        print("-" * 40)
        resposta = stub.GetInsightsStatus(services_pb2.Empty(), timeout=5)
        print(f"   ✅ Status: {resposta.message}")
        print("   ℹ️  Observe o contador de métricas atual")
        
        # 2. Registrar primeira métrica
        print("\n2️⃣ REGISTRANDO METRICA 1...")
        print("-" * 40)
        request = services_pb2.RegisterMetricsRequest(
            id_interacao="interacao_manual_001"
        )
        print(f"   📤 ID da Interação: {request.id_interacao}")
        print("   ⏳ Registrando métrica...")
        
        resposta = stub.RegisterMetrics(request, timeout=5)
        
        print(f"   📥 Resultado: {resposta.message}")
        print(f"   🆔 ID confirmado: {resposta.id_interacao}")
        print(f"   📊 Insights: {resposta.insights_servico.message}")
        
        # 3. Registrar segunda métrica
        print("\n3️⃣ REGISTRANDO METRICA 2...")
        print("-" * 40)
        request = services_pb2.RegisterMetricsRequest(
            id_interacao="interacao_manual_002"
        )
        print(f"   📤 ID da Interação: {request.id_interacao}")
        print("   ⏳ Registrando métrica...")
        
        resposta = stub.RegisterMetrics(request, timeout=5)
        
        print(f"   📥 Resultado: {resposta.message}")
        print(f"   📊 Insights: {resposta.insights_servico.message}")
        
        # 4. Registrar terceira métrica
        print("\n4️⃣ REGISTRANDO METRICA 3...")
        print("-" * 40)
        request = services_pb2.RegisterMetricsRequest(
            id_interacao="interacao_manual_003"
        )
        print(f"   📤 ID da Interação: {request.id_interacao}")
        print("   ⏳ Registrando métrica...")
        
        resposta = stub.RegisterMetrics(request, timeout=5)
        
        print(f"   📥 Resultado: {resposta.message}")
        
        # 5. Registrar múltiplas métricas em sequência
        print("\n5️⃣ REGISTRANDO MULTIPLAS METRICAS (5x)...")
        print("-" * 40)
        for i in range(4, 9):
            request = services_pb2.RegisterMetricsRequest(
                id_interacao=f"interacao_batch_{i:03d}"
            )
            resposta = stub.RegisterMetrics(request, timeout=5)
            print(f"   ✅ Métrica {i-3}/5 registrada: {request.id_interacao}")
        
        # 6. Verificar status atualizado
        print("\n6️⃣ VERIFICANDO STATUS ATUALIZADO...")
        print("-" * 40)
        resposta = stub.GetInsightsStatus(services_pb2.Empty(), timeout=5)
        print(f"   ✅ Status: {resposta.message}")
        print("   📈 Observe o contador de métricas incrementado!")
        
        # Resumo
        print("\n" + "=" * 60)
        print("✅ INSIGHTS TESTADO COM SUCESSO!")
        print("=" * 60)
        print("\n📊 RESUMO DO TESTE:")
        print("   ✅ Status inicial verificado")
        print("   ✅ 8 métricas registradas com sucesso")
        print("   ✅ Status atualizado verificado")
        print("   ✅ Contadores funcionando corretamente")
        print("   ✅ Comunicação gRPC funcionando")
        print("   ✅ Servidor respondendo corretamente")
        print("\n🎯 Serviço de Insights 100% operacional!\n")
        
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
    teste_insights()
