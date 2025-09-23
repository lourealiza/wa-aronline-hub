#!/bin/bash

# ===========================================
# SCRIPT DE INSTALAÇÃO WORKADVENTURE - AR ONLINE
# ===========================================

echo "🏢 Instalando WorkAdventure para AR Online..."

# Verificar se Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "❌ Docker não encontrado. Instalando..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker $USER
    echo "✅ Docker instalado. Reinicie o terminal e execute novamente."
    exit 1
fi

# Verificar se Docker Compose está instalado
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose não encontrado. Instalando..."
    sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
fi

# Criar diretórios necessários
echo "📁 Criando diretórios..."
mkdir -p maps uploads ssl logs

# Copiar arquivo de configuração
if [ ! -f .env ]; then
    echo "📋 Copiando arquivo de configuração..."
    cp env.ar-online.example .env
    echo "⚠️  Configure o arquivo .env com suas credenciais antes de continuar!"
    echo "   - Edite GOOGLE_CLIENT_ID e GOOGLE_CLIENT_SECRET"
    echo "   - Configure senhas seguras"
    echo "   - Ajuste o domínio se necessário"
    exit 1
fi

# Baixar e iniciar serviços
echo "🚀 Iniciando serviços..."
docker-compose -f docker-compose.ar-online.yml up -d

# Aguardar serviços iniciarem
echo "⏳ Aguardando serviços iniciarem..."
sleep 30

# Verificar status
echo "🔍 Verificando status dos serviços..."
docker-compose -f docker-compose.ar-online.yml ps

echo "✅ Instalação concluída!"
echo "🌐 Acesse: http://localhost (ou seu domínio configurado)"
echo "🔧 Para parar: docker-compose -f docker-compose.ar-online.yml down"
echo "📊 Para logs: docker-compose -f docker-compose.ar-online.yml logs -f"
