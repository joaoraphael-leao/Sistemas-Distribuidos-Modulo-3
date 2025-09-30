#!/usr/bin/env python3
"""
Chatbot Service - gRPC Server com Integração Gemini AI
Implementação otimizada e limpa
"""

import sys
import os
import grpc
from concurrent import futures
import time

# Configuração do caminho para imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Imports gRPC
from grpc_services import services_pb2, services_pb2_grpc

# Tentativa de carregar dotenv e Gemini AI
model = None
try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env'))
    
    try:
        import google.generativeai as gemini
        GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
        if GEMINI_API_KEY:
            gemini.configure(api_key=GEMINI_API_KEY)
            model = gemini.GenerativeModel("gemini-2.0-flash")
            print("[OK] Gemini AI configurada com sucesso")
        else:
            print("[AVISO] GEMINI_API_KEY nao configurada - usando respostas simuladas")
    except ImportError as e:
        print("[AVISO] google-generativeai nao instalado - usando respostas simuladas")
        print("        Para instalar: pip install google-generativeai")
except ImportError:
    print("[AVISO] python-dotenv nao instalado - continuando sem arquivo .env")
except Exception as e:
    print(f"[AVISO] Erro ao configurar ambiente: {e}")
    print("        Continuando em modo simulacao...")

class ChatbotServiceServicer(services_pb2_grpc.ChatbotServiceServicer):
    """Implementação otimizada do serviço de Chatbot"""
    
    def GetChatbotStatus(self, request, context):
        """Status do serviço"""
        ai_status = "com IA Gemini" if model else "modo simulação"
        return services_pb2.StatusResponse(
            message=f"Chatbot Service ativo {ai_status}"
        )
    
    def ResolveDuvida(self, request, context):
        """Resolve dúvidas usando Gemini AI"""
        try:
            # Validação otimizada
            if not request.duvida or not request.aula_contexto:
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details("Campos 'duvida' e 'aula_contexto' são obrigatórios")
                return services_pb2.ChatbotDuvidaResponse()
            
            # Processamento da dúvida
            resposta = self._process_question(request.duvida, request.aula_contexto)
            
            return services_pb2.ChatbotDuvidaResponse(resposta=resposta)
            
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Erro interno: {str(e)}")
            return services_pb2.ChatbotDuvidaResponse()
    
    def RegisterMetrics(self, request, context):
        """Registra métricas de interação"""
        try:
            insights_response = services_pb2.StatusResponse(
                message="[OK] Metricas registradas com sucesso"
            )
            
            return services_pb2.RegisterMetricsResponse(
                message=f"Metricas da interacao {request.id_interacao} processadas",
                id_interacao=request.id_interacao,
                insights_servico=insights_response
            )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Erro ao registrar metricas: {str(e)}')
            return services_pb2.RegisterMetricsResponse()
    
    def _process_question(self, duvida, aula_contexto):
        """Processa a pergunta com IA ou simulação"""
        if model:
            try:
                prompt = f"Contexto da aula: {aula_contexto}\n\nDúvida do estudante: {duvida}\n\nResponda de forma didática e clara:"
                response = model.generate_content(prompt)
                return response.text
            except Exception as e:
                return f"[ERRO] Erro na IA: {str(e)}\n\nResposta alternativa: Para '{duvida}' no contexto de '{aula_contexto}', recomendo consultar a documentacao oficial e praticar com exemplos."
        else:
            # Modo simulação otimizado
            return f"""[SIMULACAO] Resposta simulada para sua duvida sobre '{duvida}':

No contexto de '{aula_contexto}', esta e uma excelente pergunta! 

Sugestoes:
1. Consulte a documentacao oficial
2. Pratique com exemplos simples
3. Use ambientes de desenvolvimento interativos

NOTA: Para respostas reais da IA Gemini, configure GEMINI_API_KEY no arquivo .env"""

def serve():
    """Inicia o servidor gRPC otimizado"""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_ChatbotServiceServicer_to_server(ChatbotServiceServicer(), server)
    
    listen_addr = 'localhost:8082'
    server.add_insecure_port(listen_addr)
    
    print("=" * 50)
    print("Chatbot Service iniciando na porta 8082...")
    ai_info = "com Gemini AI" if model else "em modo simulacao"
    print(f"IA Status: {ai_info}")
    print("=" * 50)
    
    server.start()
    
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        print("\nParando Chatbot Service...")
        server.stop(0)

if __name__ == '__main__':
    serve()