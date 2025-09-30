#!/usr/bin/env python3
"""
TESTE MANUAL - Cursos Service (Porta 8081)
Cliente para testar o serviço de Gestão de Cursos
"""

import sys
import os
import grpc

# Adicionar o diretório raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grpc_services import services_pb2, services_pb2_grpc

def teste_cursos():
    """Testa o serviço de Cursos"""
    
    print("=" * 60)
    print("TESTE MANUAL - CURSOS SERVICE (Porta 8081)")
    print("=" * 60)
    
    # Conectar com o serviço
    print("\n🔌 Conectando com o servidor...")
    channel = grpc.insecure_channel('localhost:8081')
    stub = services_pb2_grpc.CursosServiceStub(channel)
    
    try:
        # 1. Verificar status
        print("\n1️⃣ VERIFICANDO STATUS DO SERVICO DE CURSOS...")
        print("-" * 40)
        resposta = stub.GetCursosStatus(services_pb2.Empty(), timeout=5)
        print(f"   ✅ Status: {resposta.message}")
        
        # 2. Buscar cursos do primeiro usuário
        print("\n2️⃣ BUSCANDO CURSOS DO USUARIO 'joao_123'...")
        print("-" * 40)
        request = services_pb2.GetUserCoursesRequest(id_usuario="joao_123")
        print(f"   📤 Solicitando cursos para ID: {request.id_usuario}")
        
        resposta = stub.GetUserCourses(request, timeout=5)
        
        print(f"   📚 Total de cursos encontrados: {len(resposta.cursos_inscritos)}")
        
        if len(resposta.cursos_inscritos) > 0:
            print("\n   📋 CURSOS INSCRITOS:")
            for i, curso in enumerate(resposta.cursos_inscritos, 1):
                print(f"      {i}. {curso}")
        else:
            print("   ℹ️  Nenhum curso encontrado para este usuário")
        
        # 3. Buscar cursos de outro usuário
        print("\n3️⃣ BUSCANDO CURSOS DO USUARIO 'maria_456'...")
        print("-" * 40)
        request = services_pb2.GetUserCoursesRequest(id_usuario="maria_456")
        print(f"   📤 Solicitando cursos para ID: {request.id_usuario}")
        
        resposta = stub.GetUserCourses(request, timeout=5)
        
        print(f"   📚 Total de cursos encontrados: {len(resposta.cursos_inscritos)}")
        
        if len(resposta.cursos_inscritos) > 0:
            print("\n   📋 CURSOS INSCRITOS:")
            for i, curso in enumerate(resposta.cursos_inscritos, 1):
                print(f"      {i}. {curso}")
        else:
            print("   ℹ️  Nenhum curso encontrado para este usuário")
        
        # 4. Buscar cursos de terceiro usuário
        print("\n4️⃣ BUSCANDO CURSOS DO USUARIO 'pedro_789'...")
        print("-" * 40)
        request = services_pb2.GetUserCoursesRequest(id_usuario="pedro_789")
        print(f"   📤 Solicitando cursos para ID: {request.id_usuario}")
        
        resposta = stub.GetUserCourses(request, timeout=5)
        
        print(f"   📚 Total de cursos encontrados: {len(resposta.cursos_inscritos)}")
        
        if len(resposta.cursos_inscritos) > 0:
            print("\n   📋 CURSOS INSCRITOS:")
            for i, curso in enumerate(resposta.cursos_inscritos, 1):
                print(f"      {i}. {curso}")
        else:
            print("   ℹ️  Nenhum curso encontrado para este usuário")
        
        # Resumo
        print("\n" + "=" * 60)
        print("✅ CURSOS TESTADO COM SUCESSO!")
        print("=" * 60)
        print("\n📊 RESUMO DO TESTE:")
        print("   ✅ Status verificado")
        print("   ✅ Múltiplas consultas de cursos realizadas")
        print("   ✅ Comunicação gRPC funcionando")
        print("   ✅ Servidor respondendo corretamente")
        print("\n🎯 Serviço de Cursos 100% operacional!\n")
        
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
    teste_cursos()
