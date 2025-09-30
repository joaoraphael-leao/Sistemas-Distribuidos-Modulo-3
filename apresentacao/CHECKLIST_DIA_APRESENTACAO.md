# ✅ CHECKLIST - DIA DA APRESENTAÇÃO

## 📅 **1 DIA ANTES**

### **Preparação Geral:**
- [ ] Código atualizado em ambos os PCs
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Teste local funcionando em cada PC
- [ ] Imprimir `PC1_COLA.md` e `PC2_COLA.md`
- [ ] Imprimir `DIAGRAMA_APRESENTACAO.md`

### **PC 1 - Servidor:**
- [ ] Descobrir IP: `ipconfig` → Anote: __________________
- [ ] Liberar firewall (PowerShell Admin):
  ```
  New-NetFirewallRule -DisplayName "gRPC Services" -Direction Inbound -LocalPort 8081-8085 -Protocol TCP -Action Allow
  ```
- [ ] Testar inicialização: `python grpc_main_windows.py`
- [ ] Verificar portas: `netstat -ano | findstr "808"`

### **PC 2 - Cliente:**
- [ ] Editar `cliente/teste_remoto.py`
- [ ] Colocar IP do PC 1 na linha 22
- [ ] Salvar arquivo
- [ ] Testar ping: `ping [IP_do_PC1]`
- [ ] Rodar teste completo: `python cliente/teste_remoto.py`

### **Teste Final (Ambos PCs):**
- [ ] PC 1 rodando servidores
- [ ] PC 2 conecta com sucesso
- [ ] Todos os 4 serviços respondem
- [ ] Sem erros

---

## 🎯 **2 HORAS ANTES**

- [ ] Ambos PCs ligados e conectados na mesma rede
- [ ] Testar ping entre PCs novamente
- [ ] Fechar programas desnecessários
- [ ] Desativar notificações (modo apresentação)
- [ ] Abrir terminais necessários:
  - **PC 1:** 5 terminais (1 para todos, ou 4 individuais + 1 para comandos)
  - **PC 2:** 2 terminais (1 para testes, 1 para comandos)
- [ ] Aumentar fonte dos terminais (legibilidade)
- [ ] `PC1_COLA.md` ao lado do PC 1
- [ ] `PC2_COLA.md` ao lado do PC 2

---

## 🚀 **30 MINUTOS ANTES**

### **Teste Final Completo:**

**PC 1:**
```bash
python grpc_main_windows.py
```
✅ Deve mostrar: 3/3 serviços ativos

**PC 2:**
```bash
python cliente/teste_remoto.py
```
✅ Deve conectar com todos os serviços

**Parar tudo:**
- PC 1: `Ctrl+C`

---

## 🎬 **DURANTE A APRESENTAÇÃO**

### **Materiais prontos:**
- [ ] PCs posicionados lado a lado (visíveis para plateia)
- [ ] Projetor/tela mostrando um dos PCs
- [ ] `ROTEIRO_APRESENTACAO_2PCS.md` aberto para consulta
- [ ] Água disponível 💧

### **Ordem de execução:**

#### **1. Introdução (2 min)**
- [ ] Explicar setup (2 PCs)
- [ ] Mostrar `DIAGRAMA_APRESENTACAO.md`

#### **2. Iniciar Servidores (1 min)**
- [ ] **PC 1:** `python grpc_main_windows.py`
- [ ] **PC 1:** `netstat -ano | findstr "808"`

#### **3. Teste Remoto (2 min)**
- [ ] **PC 2:** `python cliente/teste_remoto.py`

#### **4. Teste Chatbot (2 min)**
- [ ] **PC 2:** `python cliente/teste_chatbot.py`

#### **5. Independência (3 min)**
- [ ] **PC 1:** `Ctrl+C` (parar tudo)
- [ ] **PC 1:** Iniciar 3 serviços (sem Cursos)
- [ ] **PC 2:** `python cliente/teste_remoto.py` (Cursos falha)
- [ ] **PC 1:** Iniciar Cursos
- [ ] **PC 2:** `python cliente/teste_remoto.py` (tudo OK)

#### **6. Comunicação (2 min)**
- [ ] **PC 2:** `python cliente/teste_comunicacao.py`

#### **7. Provas Visuais (2 min)**
- [ ] **PC 1:** `tasklist | findstr python`
- [ ] **PC 1:** `ipconfig`
- [ ] **PC 2:** `ipconfig`

#### **8. Conclusão (1 min)**
- [ ] Resumir benefícios
- [ ] Perguntas

---

## 🆘 **PLANO B (Se algo falhar)**

### **Se PC 2 não conectar:**
1. Verificar ping
2. Verificar IP no `teste_remoto.py`
3. Verificar firewall do PC 1
4. **Último recurso:** Rodar cliente no próprio PC 1 (localhost)

### **Se um serviço crashar:**
1. Reiniciar apenas aquele serviço
2. Explicar que "isso prova independência"
3. Continuar apresentação

### **Se tudo falhar:**
1. Manter calma
2. Mostrar código-fonte
3. Explicar arquitetura
4. Mostrar `DIAGRAMA_APRESENTACAO.md`
5. Explicar benefícios do gRPC

---

## 📊 **PONTOS-CHAVE PARA MENCIONAR**

- [ ] "Sistema distribuído REAL em 2 máquinas"
- [ ] "Middleware gRPC usado por Google, Netflix, Uber"
- [ ] "10x mais rápido que REST"
- [ ] "IPs diferentes = máquinas diferentes"
- [ ] "Processos independentes = microserviços"
- [ ] "HTTP/2 + Protocol Buffers = eficiência"
- [ ] "Pode escalar cada serviço separadamente"
- [ ] "Pronto para produção"

---

## ⏰ **TIMING**

| Tempo | Atividade |
|-------|-----------|
| 00:00 - 02:00 | Introdução |
| 02:00 - 03:00 | Iniciar servidores |
| 03:00 - 05:00 | Teste remoto |
| 05:00 - 07:00 | Teste chatbot |
| 07:00 - 10:00 | Independência |
| 10:00 - 12:00 | Comunicação |
| 12:00 - 14:00 | Provas visuais |
| 14:00 - 15:00 | Conclusão |
| **Total:** | **15 min** |

---

## 📞 **CONTATOS EMERGÊNCIA**

- Suporte técnico: __________________
- Professor: __________________
- Colega com código: __________________

---

## ✅ **CHECKLIST FINAL (5 MIN ANTES)**

- [ ] Ambos PCs funcionando
- [ ] Ping entre PCs OK
- [ ] Teste rápido passou
- [ ] Terminais prontos
- [ ] Fonte legível
- [ ] Colas impressas
- [ ] Água disponível
- [ ] Respirar fundo 😊

---

## 🎯 **APÓS APRESENTAÇÃO**

- [ ] Agradecer à plateia
- [ ] Responder perguntas
- [ ] Compartilhar repositório (se solicitado)
- [ ] Parar servidores:
  - **PC 1:** `Ctrl+C`
- [ ] Comemorar! 🎉

---

**VOCÊ ESTÁ PRONTO! BOA APRESENTAÇÃO! 🚀**

*Lembre-se: Se algo der errado, mantenha a calma e explique a arquitetura. O importante é demonstrar conhecimento do sistema.*
