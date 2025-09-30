#!/usr/bin/env python3
"""
TESTE MANUAL - Chatbot Service (Porta 8082)
Cliente para testar o serviço de Chatbot com IA Gemini
"""

import sys
import os
import grpc

# Adicionar o diretório raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grpc_services import services_pb2, services_pb2_grpc

def teste_chatbot():
    """Testa o serviço de Chatbot"""
    
    print("=" * 60)
    print("TESTE MANUAL - CHATBOT SERVICE (Porta 8082)")
    print("=" * 60)
    
    # Conectar com o serviço
    print("\n🔌 Conectando com o servidor...")
    channel = grpc.insecure_channel('localhost:8082')
    stub = services_pb2_grpc.ChatbotServiceStub(channel)
    
    try:
        # 1. Verificar status
        print("\n1️⃣ VERIFICANDO STATUS DO CHATBOT...")
        print("-" * 40)
        resposta = stub.GetChatbotStatus(services_pb2.Empty(), timeout=5)
        print(f"   ✅ Status: {resposta.message}")
        
        # 2. Fazer primeira pergunta
        print("\n2️⃣ FAZENDO PERGUNTA 1 AO CHATBOT...")
        print("-" * 40)
        request = services_pb2.ChatbotDuvidaRequest(
            aula_contexto="Sistemas Distribuidos com gRPC",
            duvida="Qual a diferenca entre gRPC e REST?"
        )
        print(f"   📤 Enviando pergunta: '{request.duvida}'")
        print(f"   📚 Contexto: '{request.aula_contexto}'")
        print("   ⏳ Aguardando resposta da IA...")
        
        resposta = stub.ResolveDuvida(request, timeout=15)
        
        print(f"\n   📥 RESPOSTA RECEBIDA ({len(resposta.resposta)} caracteres):")
        print("   " + "-" * 56)
        print(f"{resposta.resposta}")
        print("   " + "-" * 56)
        
        # 3. Fazer segunda pergunta
        print("\n3️⃣ FAZENDO PERGUNTA 2 AO CHATBOT...")
        print("-" * 40)
        request = services_pb2.ChatbotDuvidaRequest(
            aula_contexto="Arquitetura de Microservicos",
            duvida="O que e um microservico?"
        )
        print(f"   📤 Enviando pergunta: '{request.duvida}'")
        print(f"   📚 Contexto: '{request.aula_contexto}'")
        print("   ⏳ Aguardando resposta...")
        
        resposta = stub.ResolveDuvida(request, timeout=15)
        
        print(f"\n   📥 RESPOSTA RECEBIDA ({len(resposta.resposta)} caracteres):")
        print("   " + "-" * 56)
        # Mostrar apenas os primeiros 300 caracteres
        preview = resposta.resposta[:300]
        print(f"{preview}...")
        print("   " + "-" * 56)
        
        # 4. Fazer terceira pergunta (exemplo prático)
        print("\n4️⃣ FAZENDO PERGUNTA 3 AO CHATBOT...")
        print("-" * 40)
        request = services_pb2.ChatbotDuvidaRequest(
            aula_contexto="Protocol Buffers",
            duvida="Como funcionam os Protocol Buffers?"
        )
        print(f"   📤 Enviando pergunta: '{request.duvida}'")
        print(f"   📚 Contexto: '{request.aula_contexto}'")
        print("   ⏳ Aguardando resposta...")
        
        resposta = stub.ResolveDuvida(request, timeout=15)
        
        print(f"\n   📥 RESPOSTA RECEBIDA ({len(resposta.resposta)} caracteres):")
        print("   " + "-" * 56)
        preview = resposta.resposta[:300]
        print(f"{preview}...")
        print("   " + "-" * 56)
        
        # Resumo
        print("\n" + "=" * 60)
        print("✅ CHATBOT TESTADO COM SUCESSO!")
        print("=" * 60)
        print("\n📊 RESUMO DO TESTE:")
        print("   ✅ Status verificado")
        print("   ✅ 3 perguntas respondidas pela IA")
        print("   ✅ Comunicação gRPC funcionando")
        print("   ✅ Servidor respondendo corretamente")
        print("\n🎯 Serviço de Chatbot 100% operacional!\n")
        
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
    teste_chatbot()
