#!/usr/bin/env python3
"""
Teste Rápido de Conexão gRPC
"""

import sys
import os
import grpc

# Configuração de ambiente
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Imports gRPC
from grpc_services import services_pb2, services_pb2_grpc

def test_cursos_connection():
    """Testa conexão com serviço de cursos"""
    try:
        # Conecta com o serviço
        channel = grpc.insecure_channel('localhost:8081')
        stub = services_pb2_grpc.CursosServiceStub(channel)
        
        # Testa status
        response = stub.GetCursosStatus(services_pb2.Empty(), timeout=5)
        print(f"✅ CURSOS: {response.message}")
        
        # Testa funcionalidade
        request = services_pb2.GetUserCoursesRequest(id_usuario="test_123")
        response = stub.GetUserCourses(request, timeout=5)
        print(f"✅ FUNCIONALIDADE: Encontrados {len(response.cursos_inscritos)} cursos")
        
        channel.close()
        return True
        
    except Exception as e:
        print(f"❌ ERRO: {e}")
        return False

if __name__ == '__main__':
    print("🧪 TESTE RÁPIDO DE CONEXÃO gRPC")
    print("=" * 40)
    
    if test_cursos_connection():
        print("\n🎉 SERVIÇO DE CURSOS FUNCIONANDO!")
    else:
        print("\n❌ Falha na conexão")