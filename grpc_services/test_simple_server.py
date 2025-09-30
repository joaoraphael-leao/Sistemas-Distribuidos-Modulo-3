#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import grpc
from concurrent import futures
import time

# Importar os arquivos gRPC gerados
from grpc_services import services_pb2
from grpc_services import services_pb2_grpc

class SimpleServiceServicer(services_pb2_grpc.CursosServiceServicer):
    def GetCursosStatus(self, request, context):
        return services_pb2.StatusResponse(
            message="✅ Serviço gRPC funcionando! Rede corporativa OK!"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_CursosServiceServicer_to_server(SimpleServiceServicer(), server)
    
    # Tentar diferentes endereços para rede corporativa
    addresses_to_try = [
        'localhost:8080',
        'localhost:9090', 
        '127.0.0.1:8080',
        '127.0.0.1:9090'
    ]
    
    for addr in addresses_to_try:
        try:
            server.add_insecure_port(addr)
            print(f"🚀 Servidor gRPC teste iniciando em {addr}...")
            server.start()
            print(f"✅ Sucesso! Servidor rodando em {addr}")
            break
        except Exception as e:
            print(f"❌ Falha em {addr}: {e}")
            continue
    else:
        print("❌ Não foi possível iniciar em nenhuma porta!")
        return
    
    print("\n🎯 Como testar:")
    print("   1. Abra outro terminal")
    print("   2. Execute: python grpc_services/test_simple.py")
    print("\n⏹️  Pressione Ctrl+C para parar")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Parando servidor...")
        server.stop(0)

if __name__ == '__main__':
    serve()