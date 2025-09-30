# 🚀 GUIA COMPLETO - COMO EXECUTAR O SERVIDOR DE INSIGHTS

## 📋 Pré-requisitos

1. **Python 3.7+** instalado
2. **Dependências instaladas**:
   ```bash
   pip install grpcio grpcio-tools
   ```

## 🏃‍♂️ FORMAS DE EXECUTAR

### **Opção 1: Execução Simples (Recomendada)**

```bash
# No diretório raiz do projeto
python grpc_services/insights_server.py
```

**Saída esperada:**
```
2025-09-30 00:59:05,888 - __main__ - INFO - 📊 Serviço de Insights inicializado
2025-09-30 00:59:05,907 - __main__ - INFO - 🚀 Servidor de Insights rodando em localhost:8085
2025-09-30 00:59:05,907 - __main__ - INFO - 💡 Pressione Ctrl+C para parar o servidor
```

### **Opção 2: Execução em Background**

```bash
# Para rodar em background
python grpc_services/insights_server.py &

# Para parar depois
kill %1
```

### **Opção 3: Execução com Porta Customizada**

Edite o arquivo `insights_server.py` e altere a linha:
```python
def serve(port=8085):  # Mude para porta desejada
```

### **Opção 4: Execução via Script Principal**

```bash
# Se houver um script principal
python grpc_main_windows.py
```

## 🧪 COMO TESTAR

### **Teste Básico:**
```bash
python test_insights_only.py
```

### **Teste Completo:**
```bash
python test_final_completo.py
```

### **Teste de Integração:**
```bash
python grpc_services/test_client_final.py
```

## 🔧 CONFIGURAÇÕES

### **Arquivo de Configuração:**
- **Porta padrão:** 8085
- **Endereço:** localhost
- **Workers:** 10 threads
- **Timeout:** 5 segundos

### **Logs:**
Os logs são exibidos no terminal com informações detalhadas:
- 📊 Inicialização do serviço
- 📈 Métricas registradas
- 🛑 Parada graceful
- ✅ Resumo final

## 🚨 TROUBLESHOOTING

### **Erro: "Connection refused"**
1. Verifique se o servidor está rodando
2. Confirme a porta (8085)
3. Verifique se não há firewall bloqueando

### **Erro: "Port already in use"**
```bash
# Encontre processo usando a porta
netstat -ano | grep :8085

# Termine o processo
taskkill //PID [número_do_pid] //F
```

### **Erro: "Module not found"**
```bash
# Regenere os arquivos gRPC
python generate_grpc.py
```

## 📊 MONITORAMENTO

### **Métricas Disponíveis:**
- Número de métricas coletadas
- Tempo de atividade (uptime)
- Response time simulado
- User satisfaction scores
- Memory/CPU usage simulado

### **Endpoints gRPC:**
- `GetInsightsStatus()` - Status do serviço
- `RegisterMetrics(id_interacao)` - Registro de métricas

## 🎯 EXEMPLO PRÁTICO

1. **Abra um terminal** e execute:
   ```bash
   python grpc_services/insights_server.py
   ```

2. **Em outro terminal**, teste:
   ```bash
   python test_insights_only.py
   ```

3. **Para parar**, pressione `Ctrl+C` no servidor

## ✅ SUCESSO!

Se tudo estiver funcionando, você verá:
```
🎉 TODOS OS TESTES PASSARAM!
🚀 SERVIÇO DE INSIGHTS 100% OPERACIONAL!
```