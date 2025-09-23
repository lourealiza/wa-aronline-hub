# 🏗️ Guia de Configuração Backend WorkAdventure - AR Online

## 📋 **Pré-requisitos**

### **Servidor/Cloud**
- **Mínimo**: 2GB RAM, 1 CPU, 20GB SSD
- **Recomendado**: 4GB RAM, 2 CPU, 50GB SSD
- **OS**: Ubuntu 20.04+ ou similar
- **Domínio**: workadventure.ar-online.com.br (ou subdomínio)

### **Ferramentas Necessárias**
- Docker e Docker Compose
- Git
- Editor de texto (nano, vim, etc.)

---

## 🚀 **Passo 1: Preparar Servidor**

### **1.1 Atualizar Sistema**
```bash
sudo apt update && sudo apt upgrade -y
```

### **1.2 Instalar Docker**
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
# Reiniciar terminal ou fazer logout/login
```

### **1.3 Instalar Docker Compose**
```bash
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

---

## 🔧 **Passo 2: Configurar Google OAuth2**

### **2.1 Acessar Google Cloud Console**
1. Vá para: https://console.cloud.google.com/
2. Crie um projeto ou selecione existente
3. Nome do projeto: "AR Online WorkAdventure"

### **2.2 Ativar APIs**
1. Vá para "APIs e Serviços" > "Biblioteca"
2. Ative as seguintes APIs:
   - **Google Docs API**
   - **Google Drive API**
   - **Google Slides API**
   - **Google Sheets API**

### **2.3 Configurar OAuth2**
1. Vá para "APIs e Serviços" > "Credenciais"
2. Clique em "Criar Credenciais" > "ID do cliente OAuth 2.0"
3. Tipo: "Aplicação Web"
4. Nome: "AR Online WorkAdventure"
5. URIs autorizados: `https://workadventure.ar-online.com.br`
6. URIs de redirecionamento: `https://workadventure.ar-online.com.br/auth/google/callback`
7. Salve e copie o Client ID e Client Secret

---

## 🗄️ **Passo 3: Configurar Banco de Dados**

### **3.1 Instalar PostgreSQL (Opcional - Docker já inclui)**
```bash
sudo apt install postgresql postgresql-contrib
```

### **3.2 Configurar Banco (se não usar Docker)**
```bash
sudo -u postgres createdb workadventure_aronline
sudo -u postgres createuser aronline_user
sudo -u postgres psql -c "ALTER USER aronline_user PASSWORD 'sua_senha_super_segura';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE workadventure_aronline TO aronline_user;"
```

---

## ⚙️ **Passo 4: Configurar Variáveis de Ambiente**

### **4.1 Copiar Arquivo de Configuração**
```bash
cp env.ar-online.example .env
```

### **4.2 Editar Configurações**
```bash
nano .env
```

### **4.3 Configurações Essenciais**
```env
# Banco de Dados
POSTGRES_PASSWORD=sua_senha_super_segura_aqui
DATABASE_URL=postgresql://aronline_user:sua_senha_super_segura_aqui@postgres:5432/workadventure_aronline

# Google OAuth2
GOOGLE_CLIENT_ID=seu_client_id_google_aqui
GOOGLE_CLIENT_SECRET=seu_client_secret_google_aqui

# JWT e Segurança
JWT_SECRET=sua_chave_jwt_super_secreta_aqui
SECRET_KEY=sua_chave_secreta_geral_aqui

# Domínio AR Online
DOMAIN=workadventure.ar-online.com.br
```

---

## 🐳 **Passo 5: Deploy com Docker**

### **5.1 Executar Script de Instalação**
```bash
chmod +x install-workadventure.sh
./install-workadventure.sh
```

### **5.2 Ou Executar Manualmente**
```bash
# Criar diretórios
mkdir -p maps uploads ssl logs

# Iniciar serviços
docker-compose -f docker-compose.ar-online.yml up -d

# Verificar status
docker-compose -f docker-compose.ar-online.yml ps
```

---

## 🌐 **Passo 6: Configurar DNS e SSL**

### **6.1 Configurar DNS**
- Aponte `workadventure.ar-online.com.br` para o IP do servidor
- Ou use subdomínio: `wa.ar-online.com.br`

### **6.2 Configurar SSL (Let's Encrypt)**
```bash
# Instalar Certbot
sudo apt install certbot

# Gerar certificado
sudo certbot certonly --standalone -d workadventure.ar-online.com.br

# Copiar certificados
sudo cp /etc/letsencrypt/live/workadventure.ar-online.com.br/fullchain.pem ssl/
sudo cp /etc/letsencrypt/live/workadventure.ar-online.com.br/privkey.pem ssl/
```

---

## 🔍 **Passo 7: Verificar Instalação**

### **7.1 Verificar Serviços**
```bash
docker-compose -f docker-compose.ar-online.yml ps
```

### **7.2 Verificar Logs**
```bash
docker-compose -f docker-compose.ar-online.yml logs -f
```

### **7.3 Testar Acesso**
- Acesse: `https://workadventure.ar-online.com.br`
- Teste login com Google
- Verifique integrações no menu

---

## 🎯 **Passo 8: Configurar Mapa AR Online**

### **8.1 Upload do Mapa**
```bash
# Copiar mapa para diretório maps
cp public/wa_map-interativo.tmj maps/
cp public/mapScript.js maps/
cp -r public/tilesets maps/
```

### **8.2 Configurar Admin**
1. Acesse: `https://workadventure.ar-online.com.br/admin`
2. Faça login com Google
3. Configure permissões
4. Upload do mapa

---

## 🚨 **Solução de Problemas**

### **Problema: Serviços não iniciam**
```bash
# Verificar logs
docker-compose -f docker-compose.ar-online.yml logs

# Reiniciar serviços
docker-compose -f docker-compose.ar-online.yml restart
```

### **Problema: Banco de dados não conecta**
```bash
# Verificar conexão
docker exec -it ar-online-postgres psql -U aronline_user -d workadventure_aronline

# Recriar banco
docker-compose -f docker-compose.ar-online.yml down
docker volume rm wa-aronline-hub_postgres_data
docker-compose -f docker-compose.ar-online.yml up -d
```

### **Problema: Google OAuth não funciona**
- Verificar Client ID e Secret
- Verificar URIs autorizados
- Verificar domínio configurado

---

## 📊 **Comandos Úteis**

### **Gerenciar Serviços**
```bash
# Iniciar
docker-compose -f docker-compose.ar-online.yml up -d

# Parar
docker-compose -f docker-compose.ar-online.yml down

# Reiniciar
docker-compose -f docker-compose.ar-online.yml restart

# Ver logs
docker-compose -f docker-compose.ar-online.yml logs -f

# Atualizar
docker-compose -f docker-compose.ar-online.yml pull
docker-compose -f docker-compose.ar-online.yml up -d
```

### **Backup**
```bash
# Backup do banco
docker exec ar-online-postgres pg_dump -U aronline_user workadventure_aronline > backup.sql

# Restaurar backup
docker exec -i ar-online-postgres psql -U aronline_user workadventure_aronline < backup.sql
```

---

## 🎉 **Resultado Final**

Após a configuração, você terá:

- ✅ **WorkAdventure funcionando** com todas as integrações
- ✅ **Google Docs/Drive/Slides** habilitados
- ✅ **Excalidraw** para desenho colaborativo
- ✅ **Sistema de Cards** para Kanban
- ✅ **Mapa AR Online** carregado
- ✅ **SSL** configurado
- ✅ **Backup** automatizado

**Acesse**: `https://workadventure.ar-online.com.br`

---

## 💰 **Custos Estimados**

### **Servidor Cloud**
- **DigitalOcean**: $20-40/mês
- **AWS EC2**: $25-50/mês
- **Google Cloud**: $20-45/mês

### **Domínio**
- **Registro**: $10-15/ano
- **SSL**: Gratuito (Let's Encrypt)

### **Total**: ~$25-50/mês

---

## 🆘 **Suporte**

Se precisar de ajuda:
1. Verifique os logs: `docker-compose logs -f`
2. Consulte a documentação oficial: https://docs.workadventu.re/
3. Verifique este guia novamente
4. Entre em contato com a equipe de desenvolvimento
