#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_grpc_connection():
    """Teste simples de conexão gRPC"""
    
    try:
        import grpc
        from grpc_services import services_pb2, services_pb2_grpc
        
        print("🔍 Testando conexão gRPC...")
        
        # Testar Chatbot (porta 8082)
        try:
            print("   🤖 Testando Chatbot (localhost:8082)...")
            channel = grpc.insecure_channel('localhost:8082')
            stub = services_pb2_grpc.ChatbotServiceStub(channel)
            response = stub.GetStatus(services_pb2.Empty(), timeout=5)
            print(f"   ✅ Chatbot: {response.message}")
            channel.close()
        except grpc.RpcError as e:
            print(f"   ❌ Chatbot erro: {e.code()} - {e.details()}")
        except Exception as e:
            print(f"   ❌ Chatbot erro geral: {e}")
        
        # Testar Cursos (porta 8081)
        try:
            print("   📚 Testando Cursos (localhost:8081)...")
            channel = grpc.insecure_channel('localhost:8081')
            stub = services_pb2_grpc.CursosServiceStub(channel)
            response = stub.GetStatus(services_pb2.Empty(), timeout=5)
            print(f"   ✅ Cursos: {response.message}")
            channel.close()
        except grpc.RpcError as e:
            print(f"   ❌ Cursos erro: {e.code()} - {e.details()}")
        except Exception as e:
            print(f"   ❌ Cursos erro geral: {e}")
        
        # Testar CPAR (porta 8083)
        try:
            print("   📅 Testando CPAR (localhost:8083)...")
            channel = grpc.insecure_channel('localhost:8083')
            stub = services_pb2_grpc.CPARServiceStub(channel)
            response = stub.GetStatus(services_pb2.Empty(), timeout=5)
            print(f"   ✅ CPAR: {response.message}")
            channel.close()
        except grpc.RpcError as e:
            print(f"   ❌ CPAR erro: {e.code()} - {e.details()}")
        except Exception as e:
            print(f"   ❌ CPAR erro geral: {e}")
            
    except ImportError as e:
        print(f"❌ Erro de import: {e}")
        print("   Verifique se os arquivos gRPC foram gerados corretamente")
    except Exception as e:
        print(f"❌ Erro geral: {e}")

def test_chatbot_functionality():
    """Teste específico do chatbot"""
    
    try:
        import grpc
        from grpc_services import services_pb2, services_pb2_grpc
        
        print("\n🤖 Testando funcionalidade do Chatbot...")
        
        channel = grpc.insecure_channel('localhost:8082')
        stub = services_pb2_grpc.ChatbotServiceStub(channel)
        
        # Teste ResolveDuvida
        request = services_pb2.ChatbotDuvidaRequest(
            aula_contexto="Python Básico",
            duvida="Como criar uma função em Python?"
        )
        
        response = stub.ResolveDuvida(request, timeout=30)
        print(f"   📝 Resposta: {response.resposta}")
        
        channel.close()
        
    except Exception as e:
        print(f"   ❌ Erro: {e}")

if __name__ == '__main__':
    print("🧪 TESTE DE CONECTIVIDADE gRPC")
    print("=" * 40)
    
    test_grpc_connection()
    
    # Perguntar se quer testar chatbot
    resposta = input("\n🤔 Testar funcionalidade do Chatbot? (s/n): ").lower()
    if resposta in ['s', 'sim', 'y', 'yes']:
        test_chatbot_functionality()
    
    print("\n🎯 PARA USAR:")
    print("   1. Mantenha os servidores rodando")
    print("   2. Use: python all_in_one.py (funciona sempre)")
    print("   3. Ou implemente sua própria interface gRPC")