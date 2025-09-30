#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste específico para o serviço de insights
"""

import sys
import os
import grpc

# Configuração de path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'grpc_services'))

# Imports gRPC
from grpc_services import services_pb2, services_pb2_grpc

def test_insights_service():
    """Testa apenas o serviço de insights"""
    
    # Conecta com o serviço
    channel = grpc.insecure_channel('localhost:8085')
    stub = services_pb2_grpc.InsightsServiceStub(channel)
    
    print("=== TESTE DO SERVICO DE INSIGHTS ===")
    
    try:
        # Teste 1: Status
        print("\n1. Testando GetInsightsStatus...")
        response = stub.GetInsightsStatus(services_pb2.Empty(), timeout=5)
        print(f"   [OK] Status: {response.message}")
        
        # Teste 2: Register Metrics
        print("\n2. Testando RegisterMetrics...")
        request = services_pb2.RegisterMetricsRequest(id_interacao="test_123")
        response = stub.RegisterMetrics(request, timeout=5)
        print(f"   [OK] Metrica registrada: {response.message}")
        print(f"   [INFO] ID: {response.id_interacao}")
        print(f"   [INFO] Status do servico: {response.insights_servico.message}")
        
        # Teste 3: Outro status após registro
        print("\n3. Testando status apos registro...")
        response = stub.GetInsightsStatus(services_pb2.Empty(), timeout=5)
        print(f"   [OK] Novo status: {response.message}")
        
        print("\n*** TODOS OS TESTES PASSARAM! ***")
        
    except grpc.RpcError as e:
        print(f"   [ERRO] Erro gRPC: {e.code()} - {e.details()}")
    except Exception as e:
        print(f"   [ERRO] Erro: {e}")
    finally:
        channel.close()

if __name__ == '__main__':
    test_insights_service()