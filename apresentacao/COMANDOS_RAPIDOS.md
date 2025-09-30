# ⚡ COMANDOS RÁPIDOS - APRESENTAÇÃO

## 🖥️ **PC 1 - SERVIDOR**

### **Preparação:**
```bash
# Descobrir IP
ipconfig

# Liberar firewall (PowerShell Admin)
New-NetFirewallRule -DisplayName "gRPC Services" -Direction Inbound -LocalPort 8081-8085 -Protocol TCP -Action Allow
```

### **Durante Apresentação:**
```bash
# Iniciar TODOS os servidores
python grpc_main_windows.py

# Verificar portas abertas
netstat -ano | findstr "808"

# Iniciar serviços INDIVIDUAIS (Terminal separado para cada):
python grpc_services/chatbot_server.py      # Terminal 1
python grpc_services/cursos_server.py       # Terminal 2
python grpc_services/cpar_server.py         # Terminal 3
python grpc_services/insights_server.py     # Terminal 4

# Ver processos Python
tasklist | findstr python

# Parar servidores
Ctrl + C
```

---

## 💻 **PC 2 - CLIENTE**

### **Preparação:**
```bash
# Editar arquivo com IP do servidor
notepad cliente\teste_remoto.py
# Alterar: IP_SERVIDOR = "192.168.1.100"  # IP do PC 1

# Testar conexão
ping 192.168.1.100

# Verificar dependências
pip install -r requirements.txt
```

### **Durante Apresentação:**
```bash
# Teste remoto completo
python cliente/teste_remoto.py

# Teste individual - Chatbot
python cliente/teste_chatbot.py

# Teste individual - Cursos
python cliente/teste_cursos.py

# Teste individual - CPAR
python cliente/teste_cpar.py

# Teste individual - Insights
python cliente/teste_insights.py

# Teste de comunicação entre serviços
python cliente/teste_comunicacao.py

# Ver IP local
ipconfig
```

---

## 🔧 **TROUBLESHOOTING RÁPIDO**

```bash
# Verificar se portas estão abertas
netstat -ano | findstr "8082"

# Testar conectividade de porta (PowerShell)
Test-NetConnection -ComputerName 192.168.1.100 -Port 8082

# Matar processo por porta
netstat -ano | findstr :8082
taskkill /PID [numero] /F

# Reinstalar dependências
pip install -r requirements.txt
```

---

## 📋 **ORDEM DE EXECUÇÃO**

1. **PC 1:** `ipconfig` (anotar IP)
2. **PC 1:** Liberar firewall
3. **PC 2:** Editar `teste_remoto.py` com IP
4. **PC 2:** `ping [IP_do_PC1]`
5. **PC 1:** `python grpc_main_windows.py`
6. **PC 1:** `netstat -ano | findstr "808"`
7. **PC 2:** `python cliente/teste_remoto.py`
8. **PC 2:** `python cliente/teste_chatbot.py`
9. **PC 1:** Parar e reiniciar serviços individuais
10. **PC 2:** Testar novamente

---

**Cole este arquivo no desktop para acesso rápido durante apresentação! 📌**
