# ===========================================
# SCRIPT DE SINCRONIZAÇÃO TILED → GITHUB
# ===========================================

Write-Host "🔄 Sincronizando mudanças do Tiled Map Editor..." -ForegroundColor Green

# Verificar se há mudanças nos arquivos TMJ
$tmjFiles = Get-ChildItem -Path "public" -Filter "*.tmj" | Where-Object { $_.LastWriteTime -gt (Get-Date).AddMinutes(-5) }

if ($tmjFiles.Count -eq 0) {
    Write-Host "ℹ️ Nenhuma mudança recente encontrada nos arquivos TMJ" -ForegroundColor Yellow
    exit 0
}

Write-Host "📁 Arquivos modificados:" -ForegroundColor Blue
foreach ($file in $tmjFiles) {
    Write-Host "  - $($file.Name)" -ForegroundColor White
}

# Fazer build do projeto
Write-Host "🔨 Fazendo build do projeto..." -ForegroundColor Blue
npm run build

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Erro no build do projeto!" -ForegroundColor Red
    exit 1
}

# Adicionar mudanças ao Git
Write-Host "📝 Adicionando mudanças ao Git..." -ForegroundColor Blue
git add public/*.tmj
git add dist/*.tmj

# Fazer commit
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
git commit -m "feat: atualizar mapa via Tiled Map Editor - $timestamp"

if ($LASTEXITCODE -ne 0) {
    Write-Host "ℹ️ Nenhuma mudança para commitar" -ForegroundColor Yellow
    exit 0
}

# Fazer push
Write-Host "🚀 Enviando mudanças para GitHub..." -ForegroundColor Blue
git push origin master

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Sincronização concluída com sucesso!" -ForegroundColor Green
    Write-Host "🌐 O mapa será atualizado em alguns minutos no GitHub Pages" -ForegroundColor Cyan
} else {
    Write-Host "❌ Erro ao enviar para GitHub!" -ForegroundColor Red
    exit 1
}
