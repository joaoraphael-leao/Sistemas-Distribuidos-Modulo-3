#!/usr/bin/env python3
"""
TESTE MANUAL - Conexão Remota (Máquinas Diferentes)
Cliente para testar sistema distribuído em rede
"""

import sys
import os
import grpc

# Adicionar o diretório raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grpc_services import services_pb2, services_pb2_grpc

# ============================================
# CONFIGURAÇÃO: IP DO SERVIDOR
# ============================================
# IMPORTANTE: Altere para o IP da máquina onde os servidores estão rodando
# Para descobrir o IP:
#   Windows: ipconfig
#   Linux/Mac: ifconfig ou hostname -I

IP_SERVIDOR = "localhost"  # ⬅️ TROCAR AQUI pelo IP real (ex: "192.168.1.100")

# ============================================

def teste_remoto():
    """Testa conexão com servidores em máquina remota"""
    
    print("=" * 60)
    print("TESTE MANUAL - SISTEMA DISTRIBUIDO EM REDE")
    print("=" * 60)
    print(f"\n🌐 Servidor Remoto: {IP_SERVIDOR}")
    
    if IP_SERVIDOR == "localhost":
        print("\n⚠️  AVISO: IP_SERVIDOR configurado como 'localhost'")
        print("   Para testar sistema distribuído em rede, edite este arquivo")
        print("   e altere a variável IP_SERVIDOR para o IP real do servidor.")
        print("\n   Como descobrir o IP do servidor:")
        print("   - Windows: ipconfig")
        print("   - Linux/Mac: ifconfig ou hostname -I")
        print("\n   Continuando com teste local...\n")
    
    print("\n" + "=" * 60)
    print("TESTANDO SERVICOS REMOTOS")
    print("=" * 60)
    
    # Configuração dos serviços
    servicos = {
        'Chatbot': {
            'porta': 8082,
            'stub_class': services_pb2_grpc.ChatbotServiceStub,
            'metodo_status': 'GetChatbotStatus'
        },
        'Cursos': {
            'porta': 8081,
            'stub_class': services_pb2_grpc.CursosServiceStub,
            'metodo_status': 'GetCursosStatus'
        },
        'CPAR': {
            'porta': 8083,
            'stub_class': services_pb2_grpc.CPARServiceStub,
            'metodo_status': 'GetCPARStatus'
        },
        'Insights': {
            'porta': 8085,
            'stub_class': services_pb2_grpc.InsightsServiceStub,
            'metodo_status': 'GetInsightsStatus'
        },
    }
    
    servicos_ativos = 0
    
    # Testar cada serviço
    for nome, config in servicos.items():
        print(f"\n🔍 TESTANDO {nome.upper()}...")
        print("-" * 40)
        print(f"   📡 Conectando com {IP_SERVIDOR}:{config['porta']}...")
        
        try:
            # Conectar com serviço remoto
            endereco = f"{IP_SERVIDOR}:{config['porta']}"
            channel = grpc.insecure_channel(endereco)
            stub = config['stub_class'](channel)
            
            # Chamar método de status
            metodo = getattr(stub, config['metodo_status'])
            resposta = metodo(services_pb2.Empty(), timeout=5)
            
            print(f"   ✅ {nome}: {resposta.message}")
            print(f"   📍 Localização: {IP_SERVIDOR}")
            print(f"   🔌 Porta: {config['porta']}")
            print(f"   ✅ Comunicação gRPC estabelecida!")
            
            servicos_ativos += 1
            channel.close()
            
        except grpc.RpcError as e:
            print(f"   ❌ Erro gRPC: {e.code()}")
            print(f"   📝 Detalhes: {e.details()}")
            print(f"\n   💡 POSSÍVEIS CAUSAS:")
            print(f"      • Servidor não está rodando")
            print(f"      • Firewall bloqueando a porta {config['porta']}")
            print(f"      • IP incorreto")
            
        except Exception as e:
            print(f"   ❌ Erro: {e}")
    
    # Teste funcional detalhado
    if servicos_ativos > 0:
        print("\n" + "=" * 60)
        print("TESTE FUNCIONAL REMOTO")
        print("=" * 60)
        
        # Teste 1: Chatbot
        print("\n💬 TESTANDO CHATBOT REMOTO...")
        print("-" * 40)
        try:
            channel = grpc.insecure_channel(f"{IP_SERVIDOR}:8082")
            stub = services_pb2_grpc.ChatbotServiceStub(channel)
            
            request = services_pb2.ChatbotDuvidaRequest(
                aula_contexto="Teste de Sistema Distribuido",
                duvida="Este sistema esta realmente distribuido em rede?"
            )
            
            print(f"   📤 Enviando pergunta para {IP_SERVIDOR}...")
            resposta = stub.ResolveDuvida(request, timeout=15)
            
            print(f"   ✅ Resposta recebida de servidor remoto!")
            print(f"   📏 Tamanho: {len(resposta.resposta)} caracteres")
            print(f"\n   📄 RESPOSTA:")
            print("   " + "-" * 56)
            print(f"{resposta.resposta[:400]}...")
            print("   " + "-" * 56)
            
            channel.close()
            
        except Exception as e:
            print(f"   ❌ Erro: {e}")
        
        # Teste 2: Insights
        print("\n📊 TESTANDO INSIGHTS REMOTO...")
        print("-" * 40)
        try:
            channel = grpc.insecure_channel(f"{IP_SERVIDOR}:8085")
            stub = services_pb2_grpc.InsightsServiceStub(channel)
            
            request = services_pb2.RegisterMetricsRequest(
                id_interacao="teste_remoto_001"
            )
            
            print(f"   📤 Registrando métrica em {IP_SERVIDOR}...")
            resposta = stub.RegisterMetrics(request, timeout=5)
            
            print(f"   ✅ Métrica registrada remotamente!")
            print(f"   📝 {resposta.message}")
            
            channel.close()
            
        except Exception as e:
            print(f"   ❌ Erro: {e}")
    
    # Resumo final
    print("\n" + "=" * 60)
    print("RESUMO DO TESTE REMOTO")
    print("=" * 60)
    
    print(f"\n📊 ESTATÍSTICAS:")
    print(f"   • Serviços testados: {len(servicos)}")
    print(f"   • Serviços ativos: {servicos_ativos}")
    print(f"   • Serviços inativos: {len(servicos) - servicos_ativos}")
    
    if servicos_ativos == len(servicos):
        print("\n✅ TODOS OS SERVICOS REMOTOS ESTAO FUNCIONANDO!")
    elif servicos_ativos > 0:
        print(f"\n⚠️  Sistema parcialmente ativo ({servicos_ativos}/{len(servicos)})")
    else:
        print("\n❌ NENHUM SERVICO ATIVO")
        print("\n💡 CHECKLIST DE TROUBLESHOOTING:")
        print("   1. Servidor está rodando?")
        print("      python grpc_main_windows.py")
        print(f"\n   2. IP está correto? (atual: {IP_SERVIDOR})")
        print("      Windows: ipconfig")
        print("      Linux/Mac: ifconfig")
        print("\n   3. Firewall liberado?")
        print("      PowerShell (Admin):")
        print("      New-NetFirewallRule -DisplayName 'gRPC' -Direction Inbound \\")
        print("        -LocalPort 8081-8085 -Protocol TCP -Action Allow")
        print("\n   4. Máquinas na mesma rede?")
        print("      ping", IP_SERVIDOR)
    
    if servicos_ativos > 0:
        print("\n🎯 PROVA DE SISTEMA DISTRIBUÍDO:")
        print(f"   ✅ Cliente rodando nesta máquina")
        print(f"   ✅ Servidores rodando em {IP_SERVIDOR}")
        print(f"   ✅ Comunicação via gRPC/HTTP2")
        print(f"   ✅ Múltiplas portas (8081-8085)")
        print(f"   ✅ Arquitetura de microserviços distribuída")
    
    print("\n" + "=" * 60 + "\n")

if __name__ == '__main__':
    teste_remoto()
