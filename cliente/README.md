# 📁 TESTES MANUAIS DO CLIENTE gRPC

Esta pasta contém todos os testes manuais para interagir com os serviços gRPC do sistema.

## 🚀 COMO USAR

### **PASSO 1: Iniciar os Servidores**

Em um terminal separado, execute:
```bash
python grpc_main_windows.py
```

Deixe este terminal aberto! Os serviços ficarão rodando nas portas:
- Chatbot: 8082
- Cursos: 8081
- CPAR: 8083
- Insights: 8085

### **PASSO 2: Executar os Testes**

Em outro terminal, execute os testes individuais:

```bash
# Testar Chatbot
python cliente/teste_chatbot.py

# Testar Cursos
python cliente/teste_cursos.py

# Testar CPAR
python cliente/teste_cpar.py

# Testar Insights
python cliente/teste_insights.py

# Testar Comunicação entre Serviços
python cliente/teste_comunicacao.py

# Testar Conexão Remota (máquinas diferentes)
python cliente/teste_remoto.py
```

## 📋 DESCRIÇÃO DOS TESTES

| Arquivo | Descrição | O que testa |
|---------|-----------|-------------|
| `teste_chatbot.py` | Testa o serviço de Chatbot | Status, perguntas à IA |
| `teste_cursos.py` | Testa o serviço de Cursos | Status, busca de cursos |
| `teste_cpar.py` | Testa o serviço CPAR | Status, notificações |
| `teste_insights.py` | Testa o serviço de Insights | Status, registro de métricas |
| `teste_comunicacao.py` | Testa múltiplos serviços | Fluxo completo entre serviços |
| `teste_remoto.py` | Testa conexão remota | Sistema distribuído em rede |

## 🌐 TESTE REMOTO (Máquinas Diferentes)

Para testar com o servidor em outra máquina:

1. **Na máquina do servidor:**
   ```bash
   python grpc_main_windows.py
   ```

2. **Descobrir o IP do servidor:**
   ```bash
   ipconfig
   ```
   Anote o "Endereço IPv4" (ex: 192.168.1.100)

3. **Liberar firewall (PowerShell como Admin):**
   ```powershell
   New-NetFirewallRule -DisplayName "gRPC Services" -Direction Inbound -LocalPort 8081-8085 -Protocol TCP -Action Allow
   ```

4. **Na sua máquina (cliente):**
   - Edite o arquivo `cliente/teste_remoto.py`
   - Altere a linha `IP_SERVIDOR = "localhost"` para o IP do servidor
   - Execute: `python cliente/teste_remoto.py`

## ✅ ORDEM RECOMENDADA PARA APRESENTAÇÃO

1. `teste_chatbot.py` - Mostra IA funcionando
2. `teste_cursos.py` - Mostra gestão de dados
3. `teste_cpar.py` - Mostra notificações
4. `teste_insights.py` - Mostra métricas
5. `teste_comunicacao.py` - Mostra integração
6. `teste_remoto.py` - Prova distribuição em rede

## 🎯 DICAS

- Todos os testes são **independentes** - podem ser executados em qualquer ordem
- Cada teste se conecta aos serviços e fecha a conexão automaticamente
- Os servidores devem estar rodando ANTES de executar qualquer teste
- Se um teste falhar, verifique se os servidores estão ativos

## 🔧 TROUBLESHOOTING

**Erro "Connection refused":**
```bash
# Verifique se os servidores estão rodando
netstat -ano | findstr "808"
```

**Erro "Module not found":**
```bash
# Execute os testes a partir da raiz do projeto
cd ..
python cliente/teste_chatbot.py
```

---

**Sistema Distribuído com gRPC - Testes Manuais Organizados** 🚀
