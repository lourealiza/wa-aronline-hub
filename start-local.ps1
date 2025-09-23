# ===========================================
# SCRIPT DE INÍCIO LOCAL - WORKADVENTURE AR ONLINE (PowerShell)
# ===========================================

Write-Host "🏢 Iniciando WorkAdventure Local para AR Online..." -ForegroundColor Green

# Verificar se Docker está instalado
try {
    docker --version | Out-Null
    Write-Host "✅ Docker encontrado" -ForegroundColor Green
} catch {
    Write-Host "❌ Docker não encontrado!" -ForegroundColor Red
    Write-Host "📥 Instale o Docker Desktop: https://www.docker.com/products/docker-desktop" -ForegroundColor Yellow
    exit 1
}

# Verificar se Docker Compose está instalado
try {
    docker-compose --version | Out-Null
    Write-Host "✅ Docker Compose encontrado" -ForegroundColor Green
} catch {
    Write-Host "❌ Docker Compose não encontrado!" -ForegroundColor Red
    Write-Host "📥 Instale o Docker Compose: https://docs.docker.com/compose/install/" -ForegroundColor Yellow
    exit 1
}

# Criar diretórios necessários
Write-Host "📁 Criando diretórios..." -ForegroundColor Blue
if (!(Test-Path "uploads")) { New-Item -ItemType Directory -Name "uploads" }
if (!(Test-Path "logs")) { New-Item -ItemType Directory -Name "logs" }

# Parar containers existentes
Write-Host "🛑 Parando containers existentes..." -ForegroundColor Yellow
docker-compose -f docker-compose.local.yml down

# Iniciar serviços
Write-Host "🚀 Iniciando serviços locais..." -ForegroundColor Blue
docker-compose -f docker-compose.local.yml up -d

# Aguardar serviços iniciarem
Write-Host "⏳ Aguardando serviços iniciarem..." -ForegroundColor Yellow
Start-Sleep -Seconds 15

# Verificar status
Write-Host "🔍 Verificando status dos serviços..." -ForegroundColor Blue
docker-compose -f docker-compose.local.yml ps

Write-Host ""
Write-Host "✅ WorkAdventure Local iniciado!" -ForegroundColor Green
Write-Host "🌐 Acesse: http://localhost:8080" -ForegroundColor Cyan
Write-Host "🔧 Admin: http://localhost:8080/admin" -ForegroundColor Cyan
Write-Host ""
Write-Host "📊 Comandos úteis:" -ForegroundColor Yellow
Write-Host "   Ver logs: docker-compose -f docker-compose.local.yml logs -f" -ForegroundColor White
Write-Host "   Parar: docker-compose -f docker-compose.local.yml down" -ForegroundColor White
Write-Host "   Reiniciar: docker-compose -f docker-compose.local.yml restart" -ForegroundColor White
Write-Host ""
Write-Host "🎯 Integrações disponíveis:" -ForegroundColor Yellow
Write-Host "   ✅ Excalidraw (desenho colaborativo)" -ForegroundColor Green
Write-Host "   ✅ Eraser (ferramenta de desenho)" -ForegroundColor Green
Write-Host "   ✅ Cards (sistema Kanban)" -ForegroundColor Green
Write-Host "   ❌ Google Docs/Drive (requer OAuth2)" -ForegroundColor Red
Write-Host ""
Write-Host "💡 Para testar o mapa AR Online:" -ForegroundColor Yellow
Write-Host "   1. Acesse http://localhost:8080" -ForegroundColor White
Write-Host "   2. Faça login (modo desenvolvimento)" -ForegroundColor White
Write-Host "   3. Navegue para o mapa AR Online" -ForegroundColor White
Write-Host "   4. Teste as integrações disponíveis" -ForegroundColor White
