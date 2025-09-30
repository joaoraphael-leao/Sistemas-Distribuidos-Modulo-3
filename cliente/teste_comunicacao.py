#!/usr/bin/env python3
"""
TESTE MANUAL - Comunicação entre Múltiplos Serviços
Cliente que demonstra a arquitetura distribuída com comunicação entre serviços
"""

import sys
import os
import grpc

# Adicionar o diretório raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grpc_services import services_pb2, services_pb2_grpc

def teste_comunicacao():
    """Testa a comunicação entre múltiplos serviços"""
    
    print("=" * 60)
    print("TESTE MANUAL - COMUNICACAO ENTRE SERVICOS")
    print("Fluxo Completo: Cliente -> Múltiplos Serviços")
    print("=" * 60)
    
    # Conectar com múltiplos serviços
    print("\n🔌 CONECTANDO COM MULTIPLOS SERVICOS...")
    print("-" * 40)
    
    try:
        # Conexões
        channel_chatbot = grpc.insecure_channel('localhost:8082')
        stub_chatbot = services_pb2_grpc.ChatbotServiceStub(channel_chatbot)
        print("   ✅ Conectado com Chatbot (porta 8082)")
        
        channel_cursos = grpc.insecure_channel('localhost:8081')
        stub_cursos = services_pb2_grpc.CursosServiceStub(channel_cursos)
        print("   ✅ Conectado com Cursos (porta 8081)")
        
        channel_cpar = grpc.insecure_channel('localhost:8083')
        stub_cpar = services_pb2_grpc.CPARServiceStub(channel_cpar)
        print("   ✅ Conectado com CPAR (porta 8083)")
        
        channel_insights = grpc.insecure_channel('localhost:8085')
        stub_insights = services_pb2_grpc.InsightsServiceStub(channel_insights)
        print("   ✅ Conectado com Insights (porta 8085)")
        
        # Verificar status de todos
        print("\n📊 VERIFICANDO STATUS DE TODOS OS SERVICOS...")
        print("-" * 40)
        
        status_chatbot = stub_chatbot.GetChatbotStatus(services_pb2.Empty(), timeout=5)
        print(f"   ✅ Chatbot: {status_chatbot.message}")
        
        status_cursos = stub_cursos.GetCursosStatus(services_pb2.Empty(), timeout=5)
        print(f"   ✅ Cursos: {status_cursos.message}")
        
        status_cpar = stub_cpar.GetCPARStatus(services_pb2.Empty(), timeout=5)
        print(f"   ✅ CPAR: {status_cpar.message}")
        
        status_insights = stub_insights.GetInsightsStatus(services_pb2.Empty(), timeout=5)
        print(f"   ✅ Insights: {status_insights.message}")
        
        # Fluxo de uso completo
        print("\n" + "=" * 60)
        print("🎬 SIMULANDO FLUXO COMPLETO DE USUARIO")
        print("=" * 60)
        
        # Passo 1: Usuário consulta seus cursos
        print("\n📚 PASSO 1: Usuario consulta seus cursos...")
        print("-" * 40)
        request = services_pb2.GetUserCoursesRequest(id_usuario="aluno_teste_123")
        cursos = stub_cursos.GetUserCourses(request, timeout=5)
        print(f"   ✅ {len(cursos.cursos_inscritos)} cursos encontrados")
        if len(cursos.cursos_inscritos) > 0:
            for i, curso in enumerate(cursos.cursos_inscritos[:3], 1):
                print(f"      {i}. {curso}")
        
        # Passo 2: Usuário faz pergunta ao chatbot
        print("\n💬 PASSO 2: Usuario faz pergunta ao chatbot...")
        print("-" * 40)
        request = services_pb2.ChatbotDuvidaRequest(
            aula_contexto="Banco de Dados Relacional",
            duvida="Como funciona uma transacao SQL?"
        )
        print(f"   📤 Pergunta: '{request.duvida}'")
        resposta = stub_chatbot.ResolveDuvida(request, timeout=15)
        print(f"   ✅ Resposta recebida: {len(resposta.resposta)} caracteres")
        print(f"   📄 Preview: {resposta.resposta[:150]}...")
        
        # Passo 3: Sistema registra métrica da interação
        print("\n📊 PASSO 3: Sistema registra metrica da interacao...")
        print("-" * 40)
        request = services_pb2.RegisterMetricsRequest(
            id_interacao="fluxo_completo_teste_001"
        )
        metricas = stub_insights.RegisterMetrics(request, timeout=5)
        print(f"   ✅ {metricas.message}")
        print(f"   📈 {metricas.insights_servico.message}")
        
        # Passo 4: Usuário agenda atendimento CPAR
        print("\n📅 PASSO 4: Usuario agenda atendimento CPAR...")
        print("-" * 40)
        request = services_pb2.NotifyScheduleRequest(
            id_agendamento="agendamento_teste_001"
        )
        notificacao = stub_cpar.NotifySchedule(request, timeout=5)
        print(f"   ✅ {notificacao.message}")
        
        # Passo 5: Registra métrica do agendamento
        print("\n📊 PASSO 5: Sistema registra metrica do agendamento...")
        print("-" * 40)
        request = services_pb2.RegisterMetricsRequest(
            id_interacao="agendamento_cpar_001"
        )
        metricas = stub_insights.RegisterMetrics(request, timeout=5)
        print(f"   ✅ {metricas.message}")
        
        # Passo 6: Verificar insights atualizados
        print("\n📈 PASSO 6: Verificando insights atualizados...")
        print("-" * 40)
        status = stub_insights.GetInsightsStatus(services_pb2.Empty(), timeout=5)
        print(f"   ✅ {status.message}")
        
        # Resumo final
        print("\n" + "=" * 60)
        print("✅ COMUNICACAO ENTRE SERVICOS TESTADA COM SUCESSO!")
        print("=" * 60)
        print("\n📋 RESUMO DO FLUXO COMPLETO:")
        print("   1. ✅ Cliente conectou com 4 serviços diferentes")
        print("   2. ✅ Consultou cursos no serviço de Cursos")
        print("   3. ✅ Fez pergunta ao Chatbot com IA")
        print("   4. ✅ Registrou métrica no Insights")
        print("   5. ✅ Criou agendamento no CPAR")
        print("   6. ✅ Registrou outra métrica no Insights")
        print("   7. ✅ Verificou insights atualizados")
        print("\n🎯 DEMONSTRAÇÃO DE ARQUITETURA DISTRIBUÍDA:")
        print("   • Múltiplos serviços independentes")
        print("   • Comunicação via gRPC")
        print("   • Cada serviço em porta diferente")
        print("   • Cliente orquestra múltiplos serviços")
        print("   • Sistema modular e escalável\n")
        
        # Fechar todas as conexões
        channel_chatbot.close()
        channel_cursos.close()
        channel_cpar.close()
        channel_insights.close()
        print("🔌 Todas as conexões fechadas.\n")
        
    except grpc.RpcError as e:
        print(f"\n❌ ERRO gRPC: {e.code()} - {e.details()}")
        print("\n💡 DICA: Verifique se todos os servidores estão rodando:")
        print("   python grpc_main_windows.py")
    except Exception as e:
        print(f"\n❌ ERRO: {e}")

if __name__ == '__main__':
    teste_comunicacao()
