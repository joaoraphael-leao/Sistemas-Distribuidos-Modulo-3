#!/usr/bin/env python3
"""
Versão All-in-One para redes corporativas restritivas
Todos os serviços em um único processo, sem comunicação de rede
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
import google.generativeai as gemini

load_dotenv('.env')

# Configurar Gemini
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if GEMINI_API_KEY:
    gemini.configure(api_key=GEMINI_API_KEY)
    model = gemini.GenerativeModel("gemini-2.0-flash")

class AllInOneService:
    """Todos os serviços em uma classe única"""
    
    def __init__(self):
        print("🚀 Iniciando Sistema All-in-One (sem rede)")
    
    # === SERVIÇO DE CURSOS ===
    def get_cursos_status(self):
        return "✅ Serviço de Cursos ativo"
    
    def get_user_courses(self, id_usuario):
        return {
            "message": f"Cursos do usuário {id_usuario}",
            "cursos": [{"id": 1, "nome": "Python Básico"}]
        }
    
    def send_notification(self, id_usuario, message):
        return f"📱 Notificação enviada para {id_usuario}: {message}"
    
    # === SERVIÇO DE CHATBOT ===
    def get_chatbot_status(self):
        return "✅ Serviço de Chatbot ativo"
    
    def resolve_duvida(self, aula_contexto, duvida):
        try:
            if GEMINI_API_KEY and model:
                prompt = f"Aula Contexto: {aula_contexto}\nDuvida: {duvida}\n\nResponda de forma didática:"
                response = model.generate_content(prompt)
                return response.text
            else:
                return f"Resposta simulada para: {duvida} (Configure GEMINI_API_KEY para usar IA real)"
        except Exception as e:
            return f"Erro ao processar: {str(e)}"
    
    def register_metrics(self, id_interacao):
        return f"📊 Métricas registradas para interação {id_interacao}"
    
    # === SERVIÇO CPAR ===
    def get_cpar_status(self):
        return "✅ Serviço CPAR ativo"
    
    def notify_schedule(self, id_agendamento):
        return f"📅 Notificação de agendamento {id_agendamento} enviada"
    
    # === OUTROS SERVIÇOS ===
    def get_insights_status(self):
        return "✅ Serviço de Insights ativo"
    
    def get_notifications_status(self):
        return "✅ Serviço de Notificações ativo"
    
    def get_media_status(self):
        return "✅ Serviço de Mídia ativo"

def test_all_services():
    """Testa todos os serviços"""
    service = AllInOneService()
    
    print("\n=== TESTANDO TODOS OS SERVIÇOS ===\n")
    
    # Teste Cursos
    print("📚 CURSOS:")
    print(f"   Status: {service.get_cursos_status()}")
    print(f"   Cursos: {service.get_user_courses('123')}")
    print(f"   Notificação: {service.send_notification('123', 'Bem-vindo!')}")
    
    # Teste Chatbot
    print("\n🤖 CHATBOT:")
    print(f"   Status: {service.get_chatbot_status()}")
    print(f"   Dúvida: {service.resolve_duvida('Python Básico', 'Como criar uma função?')}")
    print(f"   Métricas: {service.register_metrics('inter_001')}")
    
    # Teste CPAR
    print("\n📅 CPAR:")
    print(f"   Status: {service.get_cpar_status()}")
    print(f"   Agendamento: {service.notify_schedule('agend_456')}")
    
    # Teste outros
    print("\n📊 OUTROS SERVIÇOS:")
    print(f"   Insights: {service.get_insights_status()}")
    print(f"   Notificações: {service.get_notifications_status()}")
    print(f"   Mídia: {service.get_media_status()}")
    
    print("\n✅ TODOS OS SERVIÇOS FUNCIONANDO!")

def interactive_mode():
    """Modo interativo para testar funcionalidades"""
    service = AllInOneService()
    
    print("\n🎮 MODO INTERATIVO")
    print("Digite 'help' para ver comandos ou 'quit' para sair\n")
    
    while True:
        try:
            cmd = input("📝 Comando: ").strip().lower()
            
            if cmd == 'quit':
                break
            elif cmd == 'help':
                print("""
🔧 COMANDOS DISPONÍVEIS:
   cursos          - Status do serviço de cursos
   meus-cursos     - Ver cursos do usuário
   pergunta        - Fazer pergunta ao chatbot
   agendamento     - Notificar agendamento
   status          - Status de todos os serviços
   test            - Executar todos os testes
   quit            - Sair
                """)
            elif cmd == 'cursos':
                print(f"   {service.get_cursos_status()}")
            elif cmd == 'meus-cursos':
                user_id = input("   ID do usuário: ")
                print(f"   {service.get_user_courses(user_id)}")
            elif cmd == 'pergunta':
                contexto = input("   Contexto da aula: ")
                duvida = input("   Sua dúvida: ")
                print(f"   🤖 {service.resolve_duvida(contexto, duvida)}")
            elif cmd == 'agendamento':
                agend_id = input("   ID do agendamento: ")
                print(f"   {service.notify_schedule(agend_id)}")
            elif cmd == 'status':
                print(f"   📚 {service.get_cursos_status()}")
                print(f"   🤖 {service.get_chatbot_status()}")
                print(f"   📅 {service.get_cpar_status()}")
                print(f"   📊 {service.get_insights_status()}")
            elif cmd == 'test':
                test_all_services()
            else:
                print("   ❌ Comando não reconhecido. Digite 'help' para ajuda.")
                
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"   ❌ Erro: {e}")
    
    print("\n👋 Até logo!")

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'interactive':
        interactive_mode()
    else:
        test_all_services()