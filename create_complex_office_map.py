#!/usr/bin/env python3
"""
Criar mapa complexo do AR Online Virtual Office baseado na estrutura da imagem
"""

import json
import math

def create_complex_office_map():
    """Cria um mapa complexo com hub central octogonal e salas interconectadas"""
    
    # Dimensões do mapa (40x30 tiles)
    map_width = 40
    map_height = 30
    tile_size = 32
    
    # Estrutura do mapa
    map_data = {
        "compressionlevel": -1,
        "height": map_height,
        "infinite": False,
        "layers": [],
        "nextlayerid": 1,
        "nextobjectid": 1,
        "orientation": "orthogonal",
        "renderorder": "right-down",
        "tiledversion": "1.10.2",
        "tileheight": tile_size,
        "tilesets": [
            {
                "firstgid": 1,
                "name": "WA_Room_Builder",
                "tilewidth": 32,
                "tileheight": 32,
                "tilecount": 1000,
                "columns": 25,
                "image": "https://lourealiza.github.io/wa-aronline-hub/WA_Room_Builder.png",
                "imagewidth": 800,
                "imageheight": 1280
            }
        ],
        "tilewidth": tile_size,
        "type": "map",
        "version": "1.10",
        "width": map_width,
        "properties": [
            {
                "name": "mapName",
                "type": "string",
                "value": "AR Online Virtual Office - Complexo"
            },
            {
                "name": "script",
                "type": "string",
                "value": "mapScript.js"
            }
        ]
    }
    
    # Layer de piso (floor)
    floor_layer = {
        "id": 1,
        "name": "floor",
        "type": "tilelayer",
        "opacity": 1,
        "visible": True,
        "width": map_width,
        "height": map_height,
        "x": 0,
        "y": 0,
        "data": []
    }
    
    # Layer de paredes (walls)
    walls_layer = {
        "id": 2,
        "name": "walls",
        "type": "tilelayer",
        "opacity": 1,
        "visible": True,
        "width": map_width,
        "height": map_height,
        "x": 0,
        "y": 0,
        "data": []
    }
    
    # Layer de decorações (decorations)
    decorations_layer = {
        "id": 3,
        "name": "decorations",
        "type": "tilelayer",
        "opacity": 1,
        "visible": True,
        "width": map_width,
        "height": map_height,
        "x": 0,
        "y": 0,
        "data": []
    }
    
    # Layer de zonas (zones)
    zones_layer = {
        "id": 4,
        "name": "zones",
        "type": "objectgroup",
        "opacity": 1,
        "visible": True,
        "objects": []
    }
    
    # Layer floorLayer (obrigatório)
    floor_layer_obj = {
        "id": 5,
        "name": "floorLayer",
        "type": "objectgroup",
        "opacity": 1,
        "visible": True,
        "objects": []
    }
    
    # Inicializar dados dos layers
    floor_data = [0] * (map_width * map_height)
    walls_data = [0] * (map_width * map_height)
    decorations_data = [0] * (map_width * map_height)
    
    # Função para definir tile em posição
    def set_tile(data, x, y, tile_id):
        if 0 <= x < map_width and 0 <= y < map_height:
            data[y * map_width + x] = tile_id
    
    # Função para criar retângulo
    def create_rectangle(data, x1, y1, x2, y2, tile_id):
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                set_tile(data, x, y, tile_id)
    
    # Função para criar octógono
    def create_octagon(data, center_x, center_y, radius, tile_id):
        for y in range(max(0, center_y - radius), min(map_height, center_y + radius + 1)):
            for x in range(max(0, center_x - radius), min(map_width, center_x + radius + 1)):
                # Verificar se está dentro do octógono
                dx = abs(x - center_x)
                dy = abs(y - center_y)
                if dx + dy <= radius and (dx <= radius * 0.7 or dy <= radius * 0.7):
                    set_tile(data, x, y, tile_id)
    
    # 1. HUB CENTRAL OCTOGONAL (SELCIOTEE)
    hub_center_x = map_width // 2
    hub_center_y = map_height // 2
    hub_radius = 6
    
    # Piso do hub
    create_octagon(floor_data, hub_center_x, hub_center_y, hub_radius, 1)
    
    # Paredes do hub (octógono externo)
    create_octagon(walls_data, hub_center_x, hub_center_y, hub_radius, 2)
    
    # 2. SEÇÃO SUPERIOR
    # Sala superior esquerda (Пешо парня)
    create_rectangle(floor_data, 2, 2, 12, 8, 1)
    create_rectangle(walls_data, 2, 2, 12, 8, 2)
    
    # Corredor superior (Sulinioncerbaterer)
    create_rectangle(floor_data, 14, 4, 26, 6, 1)
    create_rectangle(walls_data, 14, 4, 26, 6, 2)
    
    # Sala superior direita (Honize lacnoanesteti)
    create_rectangle(floor_data, 28, 2, 38, 10, 1)
    create_rectangle(walls_data, 28, 2, 38, 10, 2)
    
    # 3. SEÇÃO ESQUERDA
    # Cherm winn (superior esquerda)
    create_rectangle(floor_data, 2, 10, 8, 14, 1)
    create_rectangle(walls_data, 2, 10, 8, 14, 2)
    
    # SelaCantar (meio esquerda)
    create_rectangle(floor_data, 2, 16, 8, 20, 1)
    create_rectangle(walls_data, 2, 16, 8, 20, 2)
    
    # Ecotic GOD houry (inferior esquerda)
    create_rectangle(floor_data, 2, 22, 8, 26, 1)
    create_rectangle(walls_data, 2, 22, 8, 26, 2)
    
    # Rel Entosa (inferior esquerda)
    create_rectangle(floor_data, 2, 28, 8, 29, 1)
    create_rectangle(walls_data, 2, 28, 8, 29, 2)
    
    # 4. SEÇÃO DIREITA
    # Сютится ол дот (superior direita)
    create_rectangle(floor_data, 30, 12, 38, 18, 1)
    create_rectangle(walls_data, 30, 12, 38, 18, 2)
    
    # Pok Receping (meio direita)
    create_rectangle(floor_data, 30, 20, 34, 24, 1)
    create_rectangle(walls_data, 30, 20, 34, 24, 2)
    
    # Gonoming (meio direita)
    create_rectangle(floor_data, 35, 20, 38, 22, 1)
    create_rectangle(walls_data, 35, 20, 38, 22, 2)
    
    # Memerinta (meio direita)
    create_rectangle(floor_data, 35, 23, 38, 25, 1)
    create_rectangle(walls_data, 35, 23, 38, 25, 2)
    
    # coinong IT Dig (meio direita)
    create_rectangle(floor_data, 30, 25, 33, 27, 1)
    create_rectangle(walls_data, 30, 25, 33, 27, 2)
    
    # Narsporo (meio direita)
    create_rectangle(floor_data, 34, 25, 38, 27, 1)
    create_rectangle(walls_data, 34, 25, 38, 27, 2)
    
    # 5. SEÇÃO INFERIOR
    # Gonaanara (inferior esquerda)
    create_rectangle(floor_data, 10, 25, 18, 29, 1)
    create_rectangle(walls_data, 10, 25, 18, 29, 2)
    
    # Monprorm ming (centro inferior)
    create_rectangle(floor_data, 20, 25, 28, 29, 1)
    create_rectangle(walls_data, 20, 25, 28, 29, 2)
    
    # Mormeenton (inferior direita)
    create_rectangle(floor_data, 30, 28, 38, 29, 1)
    create_rectangle(walls_data, 30, 28, 38, 29, 2)
    
    # 6. CORREDORES DE CONEXÃO
    # Corredor do hub para cima
    create_rectangle(floor_data, hub_center_x - 1, hub_center_y - hub_radius - 1, hub_center_x + 1, hub_center_y - 1, 1)
    
    # Corredor do hub para esquerda
    create_rectangle(floor_data, hub_center_x - hub_radius - 1, hub_center_y - 1, hub_center_x - 1, hub_center_y + 1, 1)
    
    # Corredor do hub para direita
    create_rectangle(floor_data, hub_center_x + 1, hub_center_y - 1, hub_center_x + hub_radius + 1, hub_center_y + 1, 1)
    
    # Corredor do hub para baixo
    create_rectangle(floor_data, hub_center_x - 1, hub_center_y + 1, hub_center_x + 1, hub_center_y + hub_radius + 1, 1)
    
    # 7. DECORAÇÕES E MÓVEIS
    # Mesas no hub central
    create_rectangle(decorations_data, hub_center_x - 2, hub_center_y - 2, hub_center_x + 2, hub_center_y + 2, 3)
    
    # Mesas nas salas de trabalho
    create_rectangle(decorations_data, 4, 4, 6, 6, 3)  # Sala superior esquerda
    create_rectangle(decorations_data, 30, 4, 32, 6, 3)  # Sala superior direita
    create_rectangle(decorations_data, 32, 14, 34, 16, 3)  # Sala direita superior
    
    # 8. ZONAS E OBJETOS
    zones = [
        {
            "id": 1,
            "name": "Hub Central - SELCIOTEE",
            "type": "",
            "x": (hub_center_x - hub_radius) * tile_size,
            "y": (hub_center_y - hub_radius) * tile_size,
            "width": (hub_radius * 2) * tile_size,
            "height": (hub_radius * 2) * tile_size,
            "visible": True,
            "properties": [
                {"name": "message", "type": "string", "value": "Bem-vindo ao Hub Central do AR Online Virtual Office!"},
                {"name": "type", "type": "string", "value": "zone"}
            ]
        },
        {
            "id": 2,
            "name": "Sala de Desenvolvimento",
            "type": "",
            "x": 2 * tile_size,
            "y": 2 * tile_size,
            "width": 11 * tile_size,
            "height": 7 * tile_size,
            "visible": True,
            "properties": [
                {"name": "message", "type": "string", "value": "Sala de Desenvolvimento - Equipe de TI"},
                {"name": "type", "type": "string", "value": "zone"}
            ]
        },
        {
            "id": 3,
            "name": "Sala de Reuniões",
            "type": "",
            "x": 28 * tile_size,
            "y": 2 * tile_size,
            "width": 11 * tile_size,
            "height": 9 * tile_size,
            "visible": True,
            "properties": [
                {"name": "message", "type": "string", "value": "Sala de Reuniões - Espaço para colaboração"},
                {"name": "type", "type": "string", "value": "zone"}
            ]
        },
        {
            "id": 4,
            "name": "RH & Financeiro",
            "type": "",
            "x": 2 * tile_size,
            "y": 10 * tile_size,
            "width": 7 * tile_size,
            "height": 5 * tile_size,
            "visible": True,
            "properties": [
                {"name": "message", "type": "string", "value": "RH & Financeiro - Gestão de pessoas e recursos"},
                {"name": "type", "type": "string", "value": "zone"}
            ]
        },
        {
            "id": 5,
            "name": "Marketing & Design",
            "type": "",
            "x": 2 * tile_size,
            "y": 16 * tile_size,
            "width": 7 * tile_size,
            "height": 5 * tile_size,
            "visible": True,
            "properties": [
                {"name": "message", "type": "string", "value": "Marketing & Design - Criatividade e comunicação"},
                {"name": "type", "type": "string", "value": "zone"}
            ]
        },
        {
            "id": 6,
            "name": "Vendas & Suporte",
            "type": "",
            "x": 30 * tile_size,
            "y": 12 * tile_size,
            "width": 9 * tile_size,
            "height": 7 * tile_size,
            "visible": True,
            "properties": [
                {"name": "message", "type": "string", "value": "Vendas & Suporte - Atendimento ao cliente"},
                {"name": "type", "type": "string", "value": "zone"}
            ]
        },
        {
            "id": 7,
            "name": "Auditório",
            "type": "",
            "x": 10 * tile_size,
            "y": 25 * tile_size,
            "width": 9 * tile_size,
            "height": 5 * tile_size,
            "visible": True,
            "properties": [
                {"name": "message", "type": "string", "value": "Auditório - Apresentações e treinamentos"},
                {"name": "type", "type": "string", "value": "zone"}
            ]
        }
    ]
    
    # Adicionar zonas ao layer
    zones_layer["objects"] = zones
    
    # Adicionar objetos ao floorLayer
    floor_layer_obj["objects"] = [
        {
            "id": 1,
            "name": "Spawn Point 1",
            "type": "",
            "x": hub_center_x * tile_size,
            "y": hub_center_y * tile_size,
            "width": tile_size,
            "height": tile_size,
            "visible": True,
            "properties": [
                {"name": "type", "type": "string", "value": "spawn"}
            ]
        }
    ]
    
    # Atualizar dados dos layers
    floor_layer["data"] = floor_data
    walls_layer["data"] = walls_data
    decorations_layer["data"] = decorations_data
    
    # Adicionar layers ao mapa
    map_data["layers"] = [floor_layer, walls_layer, decorations_layer, zones_layer, floor_layer_obj]
    
    return map_data

def main():
    """Função principal"""
    print("Criando mapa complexo do AR Online Virtual Office...")
    
    # Criar mapa
    map_data = create_complex_office_map()
    
    # Salvar arquivo
    filename = "wa_map-complexo.tmj"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    print(f"Mapa complexo criado: {filename}")
    print("Estrutura do mapa:")
    print("   - Hub Central Octogonal (SELCIOTEE)")
    print("   - Sala de Desenvolvimento")
    print("   - Sala de Reunioes")
    print("   - RH & Financeiro")
    print("   - Marketing & Design")
    print("   - Vendas & Suporte")
    print("   - Auditorio")
    print("   - Corredores interconectados")
    print("   - Zonas com mensagens interativas")

if __name__ == "__main__":
    main()
