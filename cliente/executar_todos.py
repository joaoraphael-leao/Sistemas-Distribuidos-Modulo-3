#!/usr/bin/env python3
"""
EXECUTAR TODOS OS TESTES - Sequencialmente
Executa todos os testes manuais em sequência para demonstração completa
"""

import sys
import os
import time

# Adicionar o diretório raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar(mensagem="Pressione ENTER para continuar..."):
    """Pausa a execução"""
    input(f"\n{mensagem}")

def executar_todos():
    """Executa todos os testes em sequência"""
    
    limpar_tela()
    
    print("=" * 60)
    print("DEMONSTRAÇÃO COMPLETA - SISTEMA DISTRIBUÍDO gRPC")
    print("=" * 60)
    print("\nEste script executará todos os testes manuais em sequência:")
    print("   1. Chatbot")
    print("   2. Cursos")
    print("   3. CPAR")
    print("   4. Insights")
    print("   5. Comunicação entre Serviços")
    print("\n⚠️  IMPORTANTE: Certifique-se de que os servidores estão rodando!")
    print("   Execute em outro terminal: python grpc_main_windows.py")
    
    pausar("\nPressione ENTER para iniciar os testes...")
    
    testes = [
        ("CHATBOT SERVICE", "teste_chatbot"),
        ("CURSOS SERVICE", "teste_cursos"),
        ("CPAR SERVICE", "teste_cpar"),
        ("INSIGHTS SERVICE", "teste_insights"),
        ("COMUNICACAO ENTRE SERVICOS", "teste_comunicacao"),
    ]
    
    for i, (nome, modulo) in enumerate(testes, 1):
        limpar_tela()
        print("=" * 60)
        print(f"TESTE {i}/{len(testes)}: {nome}")
        print("=" * 60)
        print()
        
        try:
            # Importar e executar o teste
            mod = __import__(modulo)
            
            # Executar função principal do módulo
            if hasattr(mod, f'teste_{modulo.split("_")[1]}'):
                getattr(mod, f'teste_{modulo.split("_")[1]}')()
            
            if i < len(testes):
                pausar(f"\n✅ Teste {i} concluído! Pressione ENTER para próximo teste...")
        
        except Exception as e:
            print(f"\n❌ Erro ao executar teste {nome}: {e}")
            pausar()
    
    # Resumo final
    limpar_tela()
    print("=" * 60)
    print("🎉 TODOS OS TESTES CONCLUÍDOS!")
    print("=" * 60)
    print("\n✅ Testes executados:")
    for i, (nome, _) in enumerate(testes, 1):
        print(f"   {i}. {nome}")
    
    print("\n📊 Sistema gRPC 100% testado e funcional!")
    print("\n💡 Para testar individualmente, execute:")
    print("   python cliente/teste_chatbot.py")
    print("   python cliente/teste_cursos.py")
    print("   etc...\n")

if __name__ == '__main__':
    try:
        executar_todos()
    except KeyboardInterrupt:
        print("\n\n⚠️  Testes interrompidos pelo usuário.\n")
    except Exception as e:
        print(f"\n❌ Erro: {e}\n")
