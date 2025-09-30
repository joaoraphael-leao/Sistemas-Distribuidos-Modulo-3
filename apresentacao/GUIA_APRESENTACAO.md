# 🎤 GUIA COMPLETO DE APRESENTAÇÃO
## Sistema Distribuído com gRPC - Passo a Passo

---

## 📋 **ÍNDICE**

1. [Preparação Antes da Apresentação](#preparação)
2. [Estrutura da Apresentação](#estrutura)
3. [Demonstração Prática](#demonstração)
4. [Provas de Sistema Distribuído](#provas)
5. [Roteiro Detalhado](#roteiro)
6. [Perguntas Frequentes](#perguntas)
7. [Troubleshooting Rápido](#troubleshooting)

---

## 🔧 **PREPARAÇÃO ANTES DA APRESENTAÇÃO** {#preparação}

### **1. Verificar Dependências (1 dia antes)**

```bash
# Instalar todas as dependências
pip install -r requirements.txt

# Verificar instalação
pip list | grep grpc
pip list | grep protobuf
```

### **2. Testar Sistema Localmente (1 dia antes)**

```bash
# Terminal 1: Iniciar servidores
python grpc_main_windows.py

# Terminal 2: Testar cada serviço
python cliente/teste_chatbot.py
python cliente/teste_cursos.py
python cliente/teste_cpar.py
python cliente/teste_insights.py
python cliente/teste_comunicacao.py
```

✅ **Todos os testes devem passar!**

### **3. Preparar Teste Remoto (Se aplicável)**

Se você vai demonstrar com máquinas diferentes:

**Na máquina do servidor (amigo):**
```bash
# Descobrir IP
ipconfig

# Anotar o "Endereço IPv4" (ex: 192.168.1.100)
```

**Liberar firewall (PowerShell como Admin):**
```powershell
New-NetFirewallRule -DisplayName "gRPC Services" -Direction Inbound -LocalPort 8081-8085 -Protocol TCP -Allow
```

**Na sua máquina (cliente):**
```bash
# Editar arquivo
notepad cliente\teste_remoto.py

# Alterar a linha:
IP_SERVIDOR = "192.168.1.100"  # Colocar IP real
```

### **4. Checklist Final**

- [ ] Todos os arquivos estão no lugar
- [ ] Dependências instaladas
- [ ] Testes locais passando
- [ ] (Opcional) Teste remoto configurado
- [ ] Terminais preparados
- [ ] README.md aberto para consulta

---

## 📊 **ESTRUTURA DA APRESENTAÇÃO** {#estrutura}

### **Tempo Total: 10-15 minutos**

| Etapa | Tempo | Conteúdo |
|-------|-------|----------|
| 1. Introdução | 2 min | O que é o projeto, tecnologias |
| 2. Arquitetura | 2 min | Mostrar estrutura de microserviços |
| 3. Demonstração | 6-8 min | Executar testes ao vivo |
| 4. Provas | 2 min | Demonstrar que está distribuído |
| 5. Conclusão | 1 min | Resumo e benefícios |

---

*[Conteúdo completo está em GUIA_APRESENTACAO.md na raiz do projeto]*

---

**Este é um guia completo. Para a apresentação, use ROTEIRO_APRESENTACAO_2PCS.md**
