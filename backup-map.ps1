# ===========================================
# SCRIPT DE BACKUP DO MAPA - AR ONLINE
# ===========================================

Write-Host "💾 Criando backup do mapa AR Online..." -ForegroundColor Green

# Criar diretório de backup com timestamp
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$backupDir = "backups/mapa_$timestamp"

if (!(Test-Path "backups")) {
    New-Item -ItemType Directory -Name "backups"
}

New-Item -ItemType Directory -Path $backupDir

# Copiar arquivos do mapa
Write-Host "📁 Copiando arquivos do mapa..." -ForegroundColor Blue
Copy-Item "public/wa_map-interativo.tmj" "$backupDir/"
Copy-Item "public/wa_map-teste.tmj" "$backupDir/"
Copy-Item "public/mapScript.js" "$backupDir/"

# Copiar tilesets
if (Test-Path "public/tilesets") {
    Copy-Item "public/tilesets" "$backupDir/" -Recurse
}

# Criar arquivo de informações
$info = @"
Backup do Mapa AR Online
Data: $(Get-Date)
Versão: 2.0
Arquivos:
- wa_map-interativo.tmj (Mapa principal)
- wa_map-teste.tmj (Mapa de teste)
- mapScript.js (Script de interações)
- tilesets/ (Tilesets do mapa)

Para restaurar:
1. Copie os arquivos de volta para public/
2. Execute: npm run build
3. Execute: git add . && git commit -m "restore: restaurar backup" && git push
"@

$info | Out-File -FilePath "$backupDir/README.txt" -Encoding UTF8

Write-Host "✅ Backup criado em: $backupDir" -ForegroundColor Green
Write-Host "📊 Arquivos incluídos:" -ForegroundColor Yellow
Write-Host "  - wa_map-interativo.tmj" -ForegroundColor White
Write-Host "  - wa_map-teste.tmj" -ForegroundColor White
Write-Host "  - mapScript.js" -ForegroundColor White
Write-Host "  - tilesets/" -ForegroundColor White
Write-Host "  - README.txt" -ForegroundColor White
