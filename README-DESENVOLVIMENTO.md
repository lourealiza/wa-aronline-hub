# 🚀 WorkAdventure AR Online - Desenvolvimento Local

## ⚡ **Início Rápido**

### **Windows (PowerShell)**
```powershell
# Executar script de início
.\start-local.ps1
```

### **Linux/Mac (Bash)**
```bash
# Executar script de início
chmod +x start-local.sh
./start-local.sh
```

### **Manual (Docker Compose)**
```bash
# Iniciar serviços
docker-compose -f docker-compose.local.yml up -d

# Verificar status
docker-compose -f docker-compose.local.yml ps
```

---

## 🌐 **Acesso**

- **WorkAdventure**: http://localhost:8080
- **Admin**: http://localhost:8080/admin
- **Banco PostgreSQL**: localhost:5432
- **Redis**: localhost:6379

---

## 🎯 **Integrações Disponíveis**

### **✅ Funcionando**
- **Excalidraw** - Desenho colaborativo
- **Eraser** - Ferramenta de desenho
- **Cards** - Sistema Kanban

### **❌ Requer Configuração**
- **Google Docs** - Requer OAuth2
- **Google Drive** - Requer OAuth2

---

## 🗺️ **Mapa AR Online**

### **Arquivos**
- **Mapa**: `public/wa_map-interativo.tmj`
- **Script**: `public/mapScript.js`
- **Tilesets**: `public/tilesets/`

### **Comandos de Teste**
- `/menu` - Menu principal
- `/integrations` - Status das integrações
- `/info` - Informações da empresa

---

## 🛠️ **Comandos Úteis**

### **Gerenciar Serviços**
```bash
# Iniciar
docker-compose -f docker-compose.local.yml up -d

# Parar
docker-compose -f docker-compose.local.yml down

# Reiniciar
docker-compose -f docker-compose.local.yml restart

# Ver logs
docker-compose -f docker-compose.local.yml logs -f

# Ver status
docker-compose -f docker-compose.local.yml ps
```

### **Banco de Dados**
```bash
# Conectar ao PostgreSQL
docker exec -it wa-local-postgres psql -U wa_user -d workadventure_local

# Backup
docker exec wa-local-postgres pg_dump -U wa_user workadventure_local > backup.sql

# Restaurar
docker exec -i wa-local-postgres psql -U wa_user workadventure_local < backup.sql
```

---

## 🔍 **Solução de Problemas**

### **Problema: Serviços não iniciam**
```bash
# Verificar logs
docker-compose -f docker-compose.local.yml logs

# Verificar espaço em disco
df -h

# Reiniciar Docker
sudo systemctl restart docker  # Linux
# Ou reiniciar Docker Desktop no Windows
```

### **Problema: Porta 8080 ocupada**
```bash
# Verificar processos na porta
netstat -ano | findstr :8080  # Windows
lsof -i :8080                 # Linux/Mac

# Matar processo
taskkill /PID <PID> /F         # Windows
kill -9 <PID>                  # Linux/Mac
```

### **Problema: Banco de dados não conecta**
```bash
# Verificar status do PostgreSQL
docker exec -it wa-local-postgres psql -U wa_user -d workadventure_local

# Recriar banco
docker-compose -f docker-compose.local.yml down
docker volume rm wa-aronline-hub_postgres_data
docker-compose -f docker-compose.local.yml up -d
```

---

## 📊 **Monitoramento**

### **Verificar Recursos**
```bash
# Uso de CPU e RAM
docker stats

# Espaço em disco
docker system df

# Logs em tempo real
docker-compose -f docker-compose.local.yml logs -f
```

---

## 🎉 **Próximos Passos**

### **Para Produção**
1. Configurar Google OAuth2
2. Usar servidor cloud
3. Configurar SSL
4. Configurar backup automatizado

### **Para Desenvolvimento**
1. Testar todas as integrações
2. Personalizar mapa AR Online
3. Adicionar novas funcionalidades
4. Testar com múltiplos usuários

---

## 💡 **Dicas**

- **Desenvolvimento**: Use `NODE_ENV=development` para logs detalhados
- **Testes**: Teste com múltiplos navegadores
- **Performance**: Monitore uso de recursos
- **Backup**: Faça backup regular do banco de dados

---

## 🆘 **Suporte**

Se precisar de ajuda:
1. Verifique os logs: `docker-compose logs -f`
2. Consulte este guia
3. Verifique a documentação oficial: https://docs.workadventu.re/
4. Entre em contato com a equipe de desenvolvimento
