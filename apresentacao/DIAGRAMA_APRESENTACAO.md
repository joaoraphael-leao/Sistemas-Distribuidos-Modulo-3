# 📊 DIAGRAMA DA APRESENTAÇÃO

## 🎯 **ARQUITETURA DO SISTEMA**

```
┌─────────────────────────────────────────────────────────┐
│                      PC 2 (CLIENTE)                      │
│                   IP: 192.168.1.50                       │
│                                                          │
│  ┌────────────────────────────────────────────────┐    │
│  │         TESTES DO CLIENTE                       │    │
│  │  • teste_chatbot.py                             │    │
│  │  • teste_cursos.py                              │    │
│  │  • teste_cpar.py                                │    │
│  │  • teste_insights.py                            │    │
│  │  • teste_comunicacao.py                         │    │
│  │  • teste_remoto.py                              │    │
│  └────────────────────────────────────────────────┘    │
│                         │                                │
└─────────────────────────┼────────────────────────────────┘
                          │
                          │ gRPC / HTTP/2
                          │ Protocol Buffers
                          │ REDE (LAN/WiFi)
                          ▼
┌─────────────────────────────────────────────────────────┐
│                   PC 1 (SERVIDOR)                        │
│                 IP: 192.168.1.100                        │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │          MICROSERVIÇOS gRPC                      │  │
│  ├──────────────────────────────────────────────────┤  │
│  │  ┌─────────────┐  ┌─────────────┐               │  │
│  │  │  CHATBOT    │  │   CURSOS    │               │  │
│  │  │  Porta 8082 │  │  Porta 8081 │               │  │
│  │  │  IA Gemini  │  │  Gestão de  │               │  │
│  │  │             │  │  Matrículas │               │  │
│  │  └─────────────┘  └─────────────┘               │  │
│  │                                                  │  │
│  │  ┌─────────────┐  ┌─────────────┐               │  │
│  │  │    CPAR     │  │  INSIGHTS   │               │  │
│  │  │ Porta 8083  │  │ Porta 8085  │               │  │
│  │  │Agendamentos │  │  Métricas   │               │  │
│  │  │             │  │  Análises   │               │  │
│  │  └─────────────┘  └─────────────┘               │  │
│  └──────────────────────────────────────────────────┘  │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

## 🔄 **FLUXO DE COMUNICAÇÃO**

### **1. Cliente faz requisição:**
```
PC 2 → [Request gRPC] → Porta 8082 (PC 1)
```

### **2. Servidor processa:**
```
PC 1 → [Chatbot processa] → Gera resposta
```

### **3. Servidor retorna:**
```
PC 1 → [Response gRPC] → PC 2
```

### **4. Tudo via HTTP/2:**
```
• Conexão persistente
• Multiplexing
• Compressão binária (Protocol Buffers)
• Header compression
```

---

## 📦 **PROTOCOL BUFFERS vs JSON**

### **Exemplo de Requisição:**

**JSON (REST - ~150 bytes):**
```json
{
  "aula_contexto": "Sistemas Distribuidos",
  "duvida": "O que e gRPC?"
}
```

**Protocol Buffers (gRPC - ~50 bytes):**
```
[Binário compacto não legível]
0x0a 0x15 0x53 0x69 0x73 0x74...
```

**Resultado: 70% menor! 🚀**

---

## ⚡ **COMPARAÇÃO: REST vs gRPC**

```
┌──────────────┬───────────────┬───────────────┐
│   Aspecto    │     REST      │     gRPC      │
├──────────────┼───────────────┼───────────────┤
│  Protocolo   │   HTTP/1.1    │    HTTP/2     │
│              │               │               │
│  Formato     │     JSON      │   Protobuf    │
│              │   (texto)     │   (binário)   │
│              │               │               │
│  Velocidade  │   Baseline    │  10x mais     │
│              │               │   rápido      │
│              │               │               │
│  Payload     │   Grande      │  30% menor    │
│              │               │               │
│  Tipagem     │   Fraca       │   Forte       │
│              │ (runtime)     │  (compile)    │
│              │               │               │
│  Streaming   │   Limitado    │   Nativo      │
│              │               │  Bidirecional │
└──────────────┴───────────────┴───────────────┘
```

---

## 🎯 **PROVAS DE SISTEMA DISTRIBUÍDO**

### **1. IPs Diferentes:**
```
PC 1: 192.168.1.100  ≠  PC 2: 192.168.1.50
      ↓                        ↓
   SERVIDOR                 CLIENTE
```

### **2. Processos Independentes:**
```
PC 1 - Task Manager:
┌─────────┬──────────┐
│   PID   │ Serviço  │
├─────────┼──────────┤
│  12345  │ Chatbot  │
│  12346  │ Cursos   │
│  12347  │ CPAR     │
│  12348  │ Insights │
└─────────┴──────────┘
```

### **3. Portas Diferentes:**
```
Chatbot  → 8082
Cursos   → 8081
CPAR     → 8083
Insights → 8085
```

### **4. Comunicação via Rede:**
```
PC 2 [ping 192.168.1.100] → ✅ Resposta
PC 2 [telnet 192.168.1.100 8082] → ✅ Conectado
```

---

## 🎬 **SEQUÊNCIA DA DEMONSTRAÇÃO**

```
1. [PC 1] Iniciar servidores
         ↓
2. [PC 1] Mostrar portas abertas
         ↓
3. [PC 2] Teste remoto completo
         ↓
4. [PC 2] Teste chatbot individual
         ↓
5. [PC 1] Parar serviço de Cursos
         ↓
6. [PC 2] Testar novamente (Cursos falha)
         ↓
7. [PC 1] Reiniciar Cursos
         ↓
8. [PC 2] Testar novamente (Tudo OK)
         ↓
9. [PC 1 + PC 2] Mostrar IPs diferentes
         ↓
10. Conclusão: Sistema distribuído provado! ✅
```

---

## 💡 **BENEFÍCIOS DEMONSTRADOS**

✅ **Distribuição Real:**
- Servidores em PC 1
- Cliente em PC 2
- Comunicação via rede

✅ **Independência:**
- Cada serviço é um processo
- Pode parar/iniciar separadamente
- Não afeta outros serviços

✅ **Performance:**
- gRPC 10x mais rápido que REST
- Payloads 30% menores
- HTTP/2 multiplexing

✅ **Escalabilidade:**
- Adicionar novos serviços facilmente
- Escalar serviços individualmente
- Load balancing nativo

✅ **Produção-Ready:**
- Usado por Google, Netflix, Uber
- Tipagem forte (menos erros)
- Multi-linguagem

---

**Use este diagrama para explicar a arquitetura! 📊**
