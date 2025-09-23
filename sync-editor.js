// ===========================================
// SCRIPT DE SINCRONIZAÇÃO - EDITOR ONLINE
// ===========================================

class MapEditorSync {
    constructor() {
        this.apiUrl = 'https://api.github.com/repos/lourealiza/wa-aronline-hub';
        this.mapData = null;
        this.isOnline = navigator.onLine;
        
        this.init();
    }

    init() {
        this.checkOnlineStatus();
        this.loadMapData();
    }

    // Verificar status online
    checkOnlineStatus() {
        window.addEventListener('online', () => {
            this.isOnline = true;
            this.updateStatus('Conectado', 'success');
        });

        window.addEventListener('offline', () => {
            this.isOnline = false;
            this.updateStatus('Desconectado', 'error');
        });
    }

    // Carregar dados do mapa
    async loadMapData() {
        try {
            const response = await fetch('wa_map-interativo.tmj');
            this.mapData = await response.json();
            this.updateStatus('Mapa carregado', 'success');
        } catch (error) {
            this.updateStatus('Erro ao carregar mapa', 'error');
            console.error('Erro ao carregar mapa:', error);
        }
    }

    // Salvar mudanças no mapa
    async saveMapChanges(roomData) {
        if (!this.isOnline) {
            this.updateStatus('Sem conexão. Mudanças salvas localmente.', 'warning');
            this.saveLocalChanges(roomData);
            return;
        }

        try {
            this.updateStatus('Salvando mudanças...', 'info');
            
            // Atualizar dados do mapa
            this.updateMapData(roomData);
            
            // Simular salvamento (em produção, usar API real)
            await this.simulateSave();
            
            this.updateStatus('Mudanças salvas com sucesso!', 'success');
            
            // Notificar WorkAdventure para atualizar
            this.notifyWorkAdventure();
            
        } catch (error) {
            this.updateStatus('Erro ao salvar mudanças', 'error');
            console.error('Erro ao salvar:', error);
        }
    }

    // Atualizar dados do mapa
    updateMapData(roomData) {
        if (!this.mapData) return;

        // Encontrar e atualizar a sala no mapa
        const roomLayer = this.mapData.layers.find(layer => 
            layer.name === 'PrivateZones' || layer.name === 'zones'
        );

        if (roomLayer) {
            const roomObject = roomLayer.objects.find(obj => 
                obj.name === roomData.name
            );

            if (roomObject) {
                // Atualizar propriedades da sala
                roomObject.x = roomData.coords.split(',')[0] * 32;
                roomObject.y = roomData.coords.split(',')[1] * 32;
                roomObject.width = roomData.coords.split(',')[2] * 32;
                roomObject.height = roomData.coords.split(',')[3] * 32;
                roomObject.type = roomData.type;
            }
        }
    }

    // Simular salvamento
    async simulateSave() {
        return new Promise(resolve => {
            setTimeout(() => {
                resolve();
            }, 2000);
        });
    }

    // Salvar mudanças localmente
    saveLocalChanges(roomData) {
        const localChanges = JSON.parse(localStorage.getItem('mapChanges') || '[]');
        localChanges.push({
            ...roomData,
            timestamp: new Date().toISOString()
        });
        localStorage.setItem('mapChanges', JSON.stringify(localChanges));
    }

    // Notificar WorkAdventure
    notifyWorkAdventure() {
        // Enviar mensagem para o iframe do WorkAdventure
        const iframe = document.getElementById('mapPreview');
        if (iframe && iframe.contentWindow) {
            iframe.contentWindow.postMessage({
                type: 'MAP_UPDATED',
                message: 'O mapa foi atualizado! Recarregue para ver as mudanças.'
            }, '*');
        }
    }

    // Atualizar status
    updateStatus(message, type) {
        const statusElement = document.getElementById('status');
        if (statusElement) {
            statusElement.textContent = message;
            statusElement.className = `status ${type}`;
        }
    }

    // Sincronizar mudanças locais quando voltar online
    async syncLocalChanges() {
        if (!this.isOnline) return;

        const localChanges = JSON.parse(localStorage.getItem('mapChanges') || '[]');
        if (localChanges.length === 0) return;

        this.updateStatus('Sincronizando mudanças locais...', 'info');

        for (const change of localChanges) {
            await this.saveMapChanges(change);
        }

        localStorage.removeItem('mapChanges');
        this.updateStatus('Mudanças locais sincronizadas', 'success');
    }

    // Exportar configuração do mapa
    exportMapConfig() {
        const config = {
            rooms: this.mapData ? this.getRoomsFromMap() : [],
            timestamp: new Date().toISOString(),
            version: '2.0'
        };

        const blob = new Blob([JSON.stringify(config, null, 2)], {
            type: 'application/json'
        });

        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `ar-online-map-config-${Date.now()}.json`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }

    // Importar configuração do mapa
    importMapConfig(file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            try {
                const config = JSON.parse(e.target.result);
                this.loadMapConfig(config);
                this.updateStatus('Configuração importada com sucesso', 'success');
            } catch (error) {
                this.updateStatus('Erro ao importar configuração', 'error');
            }
        };
        reader.readAsText(file);
    }

    // Carregar configuração do mapa
    loadMapConfig(config) {
        // Implementar carregamento da configuração
        console.log('Carregando configuração:', config);
    }

    // Obter salas do mapa
    getRoomsFromMap() {
        if (!this.mapData) return [];

        const rooms = [];
        const roomLayers = this.mapData.layers.filter(layer => 
            layer.name === 'PrivateZones' || layer.name === 'zones'
        );

        roomLayers.forEach(layer => {
            layer.objects.forEach(obj => {
                rooms.push({
                    name: obj.name,
                    type: obj.type,
                    coords: `${obj.x/32},${obj.y/32},${obj.width/32},${obj.height/32}`,
                    x: obj.x,
                    y: obj.y,
                    width: obj.width,
                    height: obj.height
                });
            });
        });

        return rooms;
    }
}

// Inicializar sincronização quando a página carregar
document.addEventListener('DOMContentLoaded', () => {
    window.mapSync = new MapEditorSync();
});
