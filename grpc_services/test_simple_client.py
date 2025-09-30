#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import grpc
from grpc_services import services_pb2
from grpc_services import services_pb2_grpc

def test_connection():
    # Tentar diferentes endereços
    addresses_to_try = [
        'localhost:8080',
        'localhost:9090', 
        '127.0.0.1:8080',
        '127.0.0.1:9090'
    ]
    
    for addr in addresses_to_try:
        try:
            print(f"🔍 Testando conexão com {addr}...")
            
            channel = grpc.insecure_channel(addr)
            stub = services_pb2_grpc.CursosServiceStub(channel)
            
            # Testar com timeout de 5 segundos
            response = stub.GetCursosStatus(
                services_pb2.Empty(), 
                timeout=5
            )
            
            print(f"✅ SUCESSO em {addr}!")
            print(f"📨 Resposta: {response.message}")
            channel.close()
            return True
            
        except grpc.RpcError as e:
            print(f"❌ Erro gRPC em {addr}: {e.code()} - {e.details()}")
        except Exception as e:
            print(f"❌ Erro geral em {addr}: {e}")
    
    print("\n❌ Não foi possível conectar em nenhum endereço!")
    print("\n🛠️  Possíveis soluções:")
    print("   1. Verifique se o servidor está rodando")
    print("   2. Tente usar uma VPN se estiver em rede corporativa")
    print("   3. Contate o administrador da rede sobre portas bloqueadas")
    return False

if __name__ == '__main__':
    test_connection()