#!/bin/bash

# ===========================================
# SCRIPT DE INÍCIO LOCAL - WORKADVENTURE AR ONLINE
# ===========================================

echo "🏢 Iniciando WorkAdventure Local para AR Online..."

# Verificar se Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "❌ Docker não encontrado!"
    echo "📥 Instale o Docker Desktop: https://www.docker.com/products/docker-desktop"
    exit 1
fi

# Verificar se Docker Compose está instalado
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose não encontrado!"
    echo "📥 Instale o Docker Compose: https://docs.docker.com/compose/install/"
    exit 1
fi

# Criar diretórios necessários
echo "📁 Criando diretórios..."
mkdir -p uploads logs

# Parar containers existentes
echo "🛑 Parando containers existentes..."
docker-compose -f docker-compose.local.yml down

# Iniciar serviços
echo "🚀 Iniciando serviços locais..."
docker-compose -f docker-compose.local.yml up -d

# Aguardar serviços iniciarem
echo "⏳ Aguardando serviços iniciarem..."
sleep 15

# Verificar status
echo "🔍 Verificando status dos serviços..."
docker-compose -f docker-compose.local.yml ps

echo ""
echo "✅ WorkAdventure Local iniciado!"
echo "🌐 Acesse: http://localhost:8080"
echo "🔧 Admin: http://localhost:8080/admin"
echo ""
echo "📊 Comandos úteis:"
echo "   Ver logs: docker-compose -f docker-compose.local.yml logs -f"
echo "   Parar: docker-compose -f docker-compose.local.yml down"
echo "   Reiniciar: docker-compose -f docker-compose.local.yml restart"
echo ""
echo "🎯 Integrações disponíveis:"
echo "   ✅ Excalidraw (desenho colaborativo)"
echo "   ✅ Eraser (ferramenta de desenho)"
echo "   ✅ Cards (sistema Kanban)"
echo "   ❌ Google Docs/Drive (requer OAuth2)"
echo ""
echo "💡 Para testar o mapa AR Online:"
echo "   1. Acesse http://localhost:8080"
echo "   2. Faça login (modo desenvolvimento)"
echo "   3. Navegue para o mapa AR Online"
echo "   4. Teste as integrações disponíveis"
