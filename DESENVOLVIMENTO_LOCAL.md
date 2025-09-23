# 🚀 Desenvolvimento Local - WorkAdventure AR Online

## ⚡ **Início Rápido**

### **Pré-requisitos**

- Docker Desktop instalado
- Docker Compose instalado
- 4GB RAM disponível

### **Passos**

1. **Executar script de início**

```bash
chmod +x start-local.sh
./start-local.sh
```

2. **Acessar aplicação**

- **WorkAdventure**: <http://localhost:8080>
- **Admin**: <http://localhost:8080/admin>

3. **Testar integrações**

- Excalidraw (desenho colaborativo)
- Eraser (ferramenta de desenho)
- Cards (sistema Kanban)

---

## 🔧 **Configuração Atual**

### **Serviços Iniciados**

- **PostgreSQL**: Porta 5432
- **Redis**: Porta 6379
- **WorkAdventure**: Porta 8080

### **Integrações Disponíveis**

- ✅ **Excalidraw** - Desenho colaborativo
- ✅ **Eraser** - Ferramenta de desenho
- ✅ **Cards** - Sistema Kanban
- ❌ **Google Docs/Drive** - Requer OAuth2

### **Mapa AR Online**

- Localizado em: `./public/wa_map-interativo.tmj`
- Script: `./public/mapScript.js`
- Tilesets: `./public/tilesets/`

---

## 🎯 **Testando o Mapa AR Online**

### **1. Acessar WorkAdventure**

1. Vá para: <http://localhost:8080>
2. Faça login (modo desenvolvimento)
3. Navegue para o mapa AR Online

### **2. Testar Comandos**

- `/menu` - Menu principal
- `/integrations` - Status das integrações
- `/info` - Informações da empresa

### **3. Testar Integrações**

- **Excalidraw**: Menu → Integrações → Excalidraw
- **Cards**: Menu → Integrações → Cards
- **Eraser**: Menu → Integrações → Eraser

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
sudo systemctl restart docker
```

### **Problema: Porta 8080 ocupada**

```bash
# Verificar processos na porta
lsof -i :8080

# Matar processo
sudo kill -9 PID

# Ou mudar porta no docker-compose.local.yml
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

### **Métricas dos Serviços**

- **PostgreSQL**: `docker exec -it wa-local-postgres psql -U wa_user -d workadventure_local -c "SELECT * FROM pg_stat_activity;"`
- **Redis**: `docker exec -it wa-local-redis redis-cli info`
- **WorkAdventure**: Logs em `docker-compose logs workadventure`

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
3. Verifique a documentação oficial: <https://docs.workadventu.re/>
4. Entre em contato com a equipe de desenvolvimento
