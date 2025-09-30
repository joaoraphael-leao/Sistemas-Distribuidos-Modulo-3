# Sistema Distribuído com gRPC

Este projeto foi adaptado de uma API REST Flask para gRPC, mantendo a mesma funcionalidade mas usando comunicação mais eficiente.

## Arquitetura gRPC

### Serviços Disponíveis

1. **Cursos Service** (porta 50051)
   - GetStatus: Status do serviço
   - GetUserCourses: Buscar cursos de um usuário
   - GetCourseMedia: Obter mídia de um curso
   - AskQuestion: Fazer pergunta sobre um curso
   - SendNotification: Enviar notificação

2. **Chatbot Service** (porta 50052)
   - GetStatus: Status do serviço
   - ResolveDuvida: Resolver dúvidas usando Gemini AI
   - RegisterMetrics: Registrar métricas de interação

3. **CPAR Service** (porta 50053)
   - GetStatus: Status do serviço
   - NotifySchedule: Notificar sobre agendamentos

4. **Notificações Service** (porta 50054)
   - GetStatus: Status do serviço

5. **Insights Service** (porta 50055)
   - GetStatus: Status do serviço

6. **Mídia e Conteúdo Service** (porta 50056)
   - GetStatus: Status do serviço
   - GetMedia: Obter mídia de um curso

## Instalação e Configuração

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Gerar Arquivos gRPC (se necessário)

```bash
python generate_grpc.py
```

### 3. Configurar Ambiente

Certifique-se de ter o arquivo `.env` com a chave do Gemini:
```
GEMINI_API_KEY=sua_chave_aqui
```

## Executando os Serviços

### Opção 1: Iniciar Todos os Serviços

```bash
python start_grpc_services.py
```

### Opção 2: Iniciar Serviços Individuais

```bash
# Serviço de Cursos
python start_grpc_services.py cursos

# Serviço de Chatbot  
python start_grpc_services.py chatbot

# Serviço CPAR
python start_grpc_services.py cpar

# Etc...
```

### Opção 3: Iniciar Manualmente

```bash
# Em terminais separados:
python grpc_services/cursos_server.py
python grpc_services/chatbot_server.py
python grpc_services/cpar_server.py
python grpc_services/notificacoes_server.py
python grpc_services/insights_server.py
python grpc_services/midia_conteudo_server.py
```

## Testando o Sistema

### Teste Básico com Gateway

```bash
python grpc_services/gateway_grpc.py
```

### Teste Completo

```bash
python grpc_services/test_client.py
```

## Principais Diferenças do REST

### Vantagens do gRPC:

1. **Performance**: Mais rápido que REST (Protocol Buffers vs JSON)
2. **Type Safety**: Definições strongly-typed nos arquivos .proto
3. **Streaming**: Suporte nativo a streaming bidirecional
4. **Interoperabilidade**: Funciona entre diferentes linguagens
5. **Menor Latência**: Protocolo binário mais eficiente

### Estrutura dos Arquivos:

```
grpc_services/
├── protos/
│   └── services.proto          # Definições dos serviços
├── services_pb2.py             # Código gerado (mensagens)
├── services_pb2_grpc.py        # Código gerado (serviços)
├── cursos_server.py            # Servidor do serviço de cursos
├── chatbot_server.py           # Servidor do chatbot
├── cpar_server.py              # Servidor CPAR
├── notificacoes_server.py      # Servidor de notificações
├── insights_server.py          # Servidor de insights
├── midia_conteudo_server.py    # Servidor de mídia
├── gateway_grpc.py             # Gateway gRPC
└── test_client.py              # Cliente de teste
```

## Integração entre Serviços

### Cursos → Notificações
```python
# O serviço de cursos chama notificações via gRPC
notification_request = services_pb2.NotificationRequest(...)
response = notification_stub.SendNotification(notification_request)
```

### Chatbot → Insights
```python
# O chatbot registra métricas no insights
metrics_request = services_pb2.RegisterMetricsRequest(...)
response = insights_stub.RegisterMetrics(metrics_request)
```

### CPAR → Notificações
```python
# CPAR notifica sobre agendamentos
schedule_request = services_pb2.NotifyScheduleRequest(...)
response = notification_stub.NotifySchedule(schedule_request)
```

## Comparação de Endpoints

### REST vs gRPC

| Funcionalidade | REST | gRPC |
|----------------|------|------|
| Status do serviço | `GET /cursos` | `GetStatus()` |
| Cursos do usuário | `GET /cursos/ver_inscricoes_do_usuario/123` | `GetUserCourses(id_usuario="123")` |
| Resolver dúvida | `POST /chatbot/duvida` | `ResolveDuvida(aula_contexto, duvida)` |
| Notificar agendamento | `GET /cpar/notificar_agendamento/123` | `NotifySchedule(id_agendamento="123")` |

## Monitoramento

Os serviços gRPC incluem logs básicos e tratamento de erros. Para monitoramento avançado, considere adicionar:

- Métricas Prometheus
- Tracing distribuído (Jaeger/Zipkin)  
- Health checks automáticos
- Circuit breakers

## Troubleshooting

### Erro "Module not found"
```bash
pip install grpcio grpcio-tools protobuf
```

### Erro de conexão
Verifique se todos os serviços estão rodando nas portas corretas (50051-50056).

### Regenerar arquivos .proto
```bash
python generate_grpc.py
```