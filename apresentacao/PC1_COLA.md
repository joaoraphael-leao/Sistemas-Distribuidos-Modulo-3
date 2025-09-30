# 🖥️ PC 1 - SERVIDOR - COLA

## ⚙️ **PREPARAÇÃO**
```bash
ipconfig                    # Anotar IPv4: _______________

# PowerShell Admin:
New-NetFirewallRule -DisplayName "gRPC Services" -Direction Inbound -LocalPort 8081-8085 -Protocol TCP -Action Allow
```

---

## 🎬 **APRESENTAÇÃO**

### **1. Iniciar Todos os Servidores**
```bash
python grpc_main_windows.py
```

### **2. Mostrar Portas**
```bash
netstat -ano | findstr "808"
```

### **3. Parar Tudo**
```
Ctrl + C
```

### **4. Iniciar Individuais**

**Terminal 1:**
```bash
python grpc_services/chatbot_server.py
```

**Terminal 2:**
```bash
python grpc_services/cpar_server.py
```

**Terminal 3:**
```bash
python grpc_services/insights_server.py
```

**Terminal 4 (depois):**
```bash
python grpc_services/cursos_server.py
```

### **5. Mostrar Processos**
```bash
tasklist | findstr python
```

### **6. Mostrar IP**
```bash
ipconfig
```

---

## 🆘 **PROBLEMAS**

**Porta ocupada:**
```bash
netstat -ano | findstr :8082
taskkill /PID [numero] /F
```

---

**IMPRIMIR E COLOCAR AO LADO DO PC 1! 📌**
