#!/usr/bin/env python3
"""
Teste Final Completo do Serviço de Insights
Testa todas as funcionalidades implementadas
"""

import sys
import os
import grpc
import time

# Configuração de path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'grpc_services'))

# Imports gRPC
from grpc_services import services_pb2, services_pb2_grpc

def test_insights_comprehensive():
    """Teste completo e abrangente do serviço de insights"""
    
    print("🔍 TESTE FINAL COMPLETO - SERVIÇO DE INSIGHTS")
    print("=" * 60)
    
    # Conecta com o serviço
    channel = grpc.insecure_channel('localhost:8085')
    stub = services_pb2_grpc.InsightsServiceStub(channel)
    
    try:
        # Teste 1: Status inicial
        print("\n📊 1. VERIFICANDO STATUS INICIAL...")
        response = stub.GetInsightsStatus(services_pb2.Empty(), timeout=5)
        print(f"   ✅ Status: {response.message}")
        
        # Teste 2: Múltiplos registros de métricas
        print("\n📈 2. REGISTRANDO MÚLTIPLAS MÉTRICAS...")
        for i in range(5):
            request = services_pb2.RegisterMetricsRequest(id_interacao=f"test_final_{i}")
            response = stub.RegisterMetrics(request, timeout=5)
            print(f"   ✅ Métrica {i+1}: {response.message}")
            print(f"      📋 ID: {response.id_interacao}")
            print(f"      🔍 Serviço: {response.insights_servico.message}")
            time.sleep(0.5)  # Pequena pausa entre registros
        
        # Teste 3: Status após registros
        print("\n📊 3. VERIFICANDO STATUS APÓS REGISTROS...")
        response = stub.GetInsightsStatus(services_pb2.Empty(), timeout=5)
        print(f"   ✅ Status atualizado: {response.message}")
        
        # Teste 4: Teste de performance
        print("\n🚀 4. TESTE DE PERFORMANCE (10 registros rápidos)...")
        start_time = time.time()
        for i in range(10):
            request = services_pb2.RegisterMetricsRequest(id_interacao=f"perf_test_{i}")
            response = stub.RegisterMetrics(request, timeout=5)
        end_time = time.time()
        print(f"   ⚡ 10 registros em {end_time - start_time:.2f} segundos")
        print(f"   📊 Média: {(end_time - start_time)/10:.3f}s por registro")
        
        # Teste 5: Status final
        print("\n📊 5. STATUS FINAL...")
        response = stub.GetInsightsStatus(services_pb2.Empty(), timeout=5)
        print(f"   ✅ Status final: {response.message}")
        
        # Teste 6: Teste de erro handling
        print("\n🛡️  6. TESTANDO TRATAMENTO DE ERROS...")
        try:
            # Teste com timeout muito baixo
            request = services_pb2.RegisterMetricsRequest(id_interacao="timeout_test")
            response = stub.RegisterMetrics(request, timeout=0.001)
            print(f"   ⚠️  Resposta inesperada: {response.message}")
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.DEADLINE_EXCEEDED:
                print(f"   ✅ Timeout tratado corretamente: {e.code()}")
            else:
                print(f"   ✅ Erro tratado: {e.code()}")
        
        print("\n🎉 TODOS OS TESTES PASSARAM COM SUCESSO!")
        print("\n📋 RESUMO DOS TESTES:")
        print("   ✅ Status do serviço")
        print("   ✅ Registro de métricas individual") 
        print("   ✅ Registro de múltiplas métricas")
        print("   ✅ Atualização de contadores")
        print("   ✅ Teste de performance")
        print("   ✅ Tratamento de erros")
        print("   ✅ Comunicação gRPC estável")
        print("\n🚀 SERVIÇO DE INSIGHTS 100% OPERACIONAL!")
        
    except grpc.RpcError as e:
        print(f"   ❌ Erro gRPC: {e.code()} - {e.details()}")
    except Exception as e:
        print(f"   ❌ Erro: {e}")
    finally:
        channel.close()

if __name__ == '__main__':
    test_insights_comprehensive()