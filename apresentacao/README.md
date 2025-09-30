# 📁 DOCUMENTAÇÃO DE APRESENTAÇÃO
## Sistema Distribuído com gRPC

Esta pasta contém TODA a documentação necessária para apresentar o projeto com 2 computadores.

---

## 📋 **ARQUIVOS PRINCIPAIS**

### **1. 📖 ROTEIRO_APRESENTACAO_2PCS.md** ⭐ PRINCIPAL
**Use este para a apresentação!**
- Roteiro COMPLETO passo a passo
- O que fazer em CADA PC (PC 1 e PC 2)
- O que falar em cada momento
- Timing detalhado (15 minutos)
- Provas de sistema distribuído

### **2. 📋 GUIA_APRESENTACAO.md**
**Guia detalhado geral:**
- Preparação completa
- Estrutura da apresentação
- Perguntas frequentes
- Troubleshooting

### **3. 📊 DIAGRAMA_APRESENTACAO.md**
**Diagramas visuais:**
- Arquitetura do sistema
- Fluxo de comunicação
- Comparação REST vs gRPC
- Provas visuais

---

## 🖨️ **COLAS PARA IMPRESSÃO** (Imprimir!)

### **🖥️ PC1_COLA.md**
**Imprimir e colocar ao lado do PC 1 (Servidor)**
- Comandos para o servidor
- Preparação
- Ordem de execução
- Troubleshooting rápido

### **💻 PC2_COLA.md**
**Imprimir e colocar ao lado do PC 2 (Cliente)**
- Comandos para o cliente
- Testes a executar
- Configuração do IP
- Troubleshooting

### **✅ CHECKLIST_DIA_APRESENTACAO.md**
**Imprimir e usar no dia**
- Checklist completo
- 1 dia antes
- 2 horas antes
- 30 minutos antes
- Durante apresentação
- Plano B

### **⚡ COMANDOS_RAPIDOS.md**
**Referência rápida**
- Comandos PC 1
- Comandos PC 2
- Ordem de execução
- Troubleshooting

---

## 🎯 **COMO USAR ESTA DOCUMENTAÇÃO**

### **📅 1 Dia Antes da Apresentação:**
1. Ler **ROTEIRO_APRESENTACAO_2PCS.md** completo
2. Ler **CHECKLIST_DIA_APRESENTACAO.md**
3. Imprimir **PC1_COLA.md**, **PC2_COLA.md** e **CHECKLIST**
4. Preparar ambos PCs (seguir checklist)
5. Testar uma vez completo

### **🎬 No Dia da Apresentação:**
1. Ter **ROTEIRO_APRESENTACAO_2PCS.md** aberto no notebook
2. **PC1_COLA.md** impresso ao lado do PC 1
3. **PC2_COLA.md** impresso ao lado do PC 2
4. **CHECKLIST_DIA_APRESENTACAO.md** para conferir
5. Seguir roteiro passo a passo

### **📖 Durante a Apresentação:**
- **Consultar:** PC1_COLA.md e PC2_COLA.md (comandos rápidos)
- **Explicar:** Usar DIAGRAMA_APRESENTACAO.md (mostrar arquitetura)
- **Responder perguntas:** Usar GUIA_APRESENTACAO.md (FAQ)

---

## 📦 **ESTRUTURA DO PROJETO**

```
Sistemas-Distribuidos-Modulo-3/
│
├── apresentacao/              ← VOCÊ ESTÁ AQUI
│   ├── README.md             ← Este arquivo
│   ├── ROTEIRO_APRESENTACAO_2PCS.md    ⭐ PRINCIPAL
│   ├── GUIA_APRESENTACAO.md
│   ├── DIAGRAMA_APRESENTACAO.md
│   ├── PC1_COLA.md           🖨️ IMPRIMIR
│   ├── PC2_COLA.md           🖨️ IMPRIMIR
│   ├── CHECKLIST_DIA_APRESENTACAO.md   🖨️ IMPRIMIR
│   └── COMANDOS_RAPIDOS.md
│
├── cliente/                   ← Testes para executar no PC 2
│   ├── teste_chatbot.py
│   ├── teste_cursos.py
│   ├── teste_cpar.py
│   ├── teste_insights.py
│   ├── teste_comunicacao.py
│   └── teste_remoto.py       ⭐ Configure o IP aqui
│
├── grpc_services/             ← Servidores para rodar no PC 1
│   ├── chatbot_server.py
│   ├── cursos_server.py
│   ├── cpar_server.py
│   └── insights_server.py
│
└── grpc_main_windows.py       ← Inicia TODOS os servidores
```

---

## ⚡ **INÍCIO RÁPIDO**

### **Setup em 5 passos:**

1. **PC 1 - Descobrir IP:**
   ```bash
   ipconfig
   # Anotar IPv4: _______________
   ```

2. **PC 1 - Liberar Firewall:**
   ```powershell
   New-NetFirewallRule -DisplayName "gRPC Services" -Direction Inbound -LocalPort 8081-8085 -Protocol TCP -Action Allow
   ```

3. **PC 2 - Configurar IP:**
   ```bash
   notepad ..\cliente\teste_remoto.py
   # Linha 22: IP_SERVIDOR = "IP_do_PC1"
   ```

4. **PC 1 - Iniciar Servidores:**
   ```bash
   cd ..
   python grpc_main_windows.py
   ```

5. **PC 2 - Testar:**
   ```bash
   cd ..
   python cliente/teste_remoto.py
   ```

---

## 📊 **ORDEM DE APRESENTAÇÃO**

| Tempo | PC 1 (Servidor) | PC 2 (Cliente) | O que mostrar |
|-------|----------------|----------------|---------------|
| 0-2min | - | - | Introdução, explicar setup |
| 2-3min | Iniciar servidores | - | Serviços iniciando |
| 3-5min | - | teste_remoto.py | Conexão remota |
| 5-7min | - | teste_chatbot.py | Chatbot funcionando |
| 7-10min | Parar/Reiniciar | teste_remoto.py | Independência |
| 10-12min | - | teste_comunicacao.py | Comunicação |
| 12-14min | Mostrar processos/IP | Mostrar IP | Provas |
| 14-15min | - | - | Conclusão |

---

## 🎯 **PROVAS A DEMONSTRAR**

1. ✅ **IPs Diferentes** - Mostrar `ipconfig` em ambos PCs
2. ✅ **Processos Independentes** - Parar um serviço, outros continuam
3. ✅ **Portas Diferentes** - `netstat -ano | findstr "808"`
4. ✅ **Comunicação via Rede** - Cliente no PC 2 acessa servidor no PC 1
5. ✅ **Middleware gRPC** - HTTP/2 + Protocol Buffers

---

## 💡 **DICAS FINAIS**

✅ **IMPORTANTE:**
- Testar TUDO 1 dia antes
- Imprimir as 3 colas
- Ter água disponível
- Aumentar fonte dos terminais
- Desativar notificações

✅ **DURANTE:**
- Respirar fundo
- Seguir o roteiro
- Consultar as colas
- Se algo falhar, manter calma

✅ **LEMBRE-SE:**
- Você conhece o sistema
- Está tudo documentado
- Tem plano B
- Vai dar certo! 🚀

---

## 📞 **SUPORTE**

- 📖 Dúvida no roteiro? → Abrir **ROTEIRO_APRESENTACAO_2PCS.md**
- 🔧 Problema técnico? → Ver **COMANDOS_RAPIDOS.md** ou **CHECKLIST**
- ❓ Pergunta da plateia? → Consultar **GUIA_APRESENTACAO.md** (FAQ)
- 📊 Explicar arquitetura? → Mostrar **DIAGRAMA_APRESENTACAO.md**

---

**BOA APRESENTAÇÃO! 🎉**

*Sistema distribuído real, provando o poder do middleware gRPC!*
