#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criar mapa profissional da AR Online baseado no design fornecido
"""

import json
import os

def create_ar_online_professional_map():
    # Configurações do mapa baseado no design
    width_tiles = 24
    height_tiles = 20
    tile_size = 32
    
    # Criar camada de piso base (tile 1 = chão cinza)
    floor_data = [1] * (width_tiles * height_tiles)
    
    # Criar camada de paredes (tile 0 = vazio, tile 2 = parede)
    walls_data = [0] * (width_tiles * height_tiles)
    
    # Criar camada de salas com cores diferentes
    rooms_data = [0] * (width_tiles * height_tiles)
    
    # Definir áreas baseadas no design:
    # - Área Superior: Convivência & Eventos (tile 3)
    # - Ala Esquerda: Gestão & Liderança (tile 4) 
    # - Ala Direita: Operações (tile 5)
    # - Centro: Lobby AR ONLINE (tile 6)
    
    # Área Superior - Convivência & Eventos (tiles 0-23, 0-6)
    for y in range(0, 7):
        for x in range(0, 24):
            index = y * width_tiles + x
            rooms_data[index] = 3
    
    # Ala Esquerda - Gestão & Liderança (tiles 0-11, 7-19)
    for y in range(7, 20):
        for x in range(0, 12):
            index = y * width_tiles + x
            rooms_data[index] = 4
    
    # Ala Direita - Operações (tiles 12-23, 7-19)
    for y in range(7, 20):
        for x in range(12, 24):
            index = y * width_tiles + x
            rooms_data[index] = 5
    
    # Centro - Lobby AR ONLINE (tiles 8-15, 7-12)
    for y in range(7, 13):
        for x in range(8, 16):
            index = y * width_tiles + x
            rooms_data[index] = 6
    
    # Criar paredes internas
    # Paredes horizontais
    for x in range(0, 24):
        # Parede entre convivência e gestão/operações
        walls_data[6 * width_tiles + x] = 2
        # Paredes internas do lobby
        if x >= 8 and x <= 15:
            walls_data[12 * width_tiles + x] = 2
    
    # Paredes verticais
    for y in range(0, 20):
        # Parede entre gestão e operações
        walls_data[y * width_tiles + 11] = 2
        walls_data[y * width_tiles + 12] = 2
        # Paredes do lobby
        if y >= 7 and y <= 12:
            walls_data[y * width_tiles + 7] = 2
            walls_data[y * width_tiles + 16] = 2
    
    # Criar spawn point no centro do lobby
    spawn_point = {
        "id": 1,
        "name": "spawn",
        "type": "spawn",
        "x": 192,  # Centro do lobby (6 * 32)
        "y": 160,  # Centro do lobby (5 * 32)
        "width": 32,
        "height": 32,
        "visible": True
    }
    
    # Criar objetos de zona para cada área
    zones = [
        {
            "id": 2,
            "name": "Lobby AR ONLINE",
            "type": "common",
            "x": 256,  # 8 * 32
            "y": 224,  # 7 * 32
            "width": 256,  # 8 * 32
            "height": 192, # 6 * 32
            "visible": True,
            "properties": [
                {"name": "tile", "type": "int", "value": 6},
                {"name": "description", "type": "string", "value": "Área central da AR Online"},
                {"name": "color", "type": "string", "value": "azul"}
            ]
        },
        {
            "id": 3,
            "name": "Convivência & Eventos",
            "type": "common",
            "x": 0,    # 0 * 32
            "y": 0,    # 0 * 32
            "width": 768,  # 24 * 32
            "height": 224, # 7 * 32
            "visible": True,
            "properties": [
                {"name": "tile", "type": "int", "value": 3},
                {"name": "description", "type": "string", "value": "Área de convivência e eventos"},
                {"name": "color", "type": "string", "value": "verde"}
            ]
        },
        {
            "id": 4,
            "name": "Gestão & Liderança",
            "type": "department",
            "x": 0,    # 0 * 32
            "y": 224,  # 7 * 32
            "width": 384,  # 12 * 32
            "height": 416, # 13 * 32
            "visible": True,
            "properties": [
                {"name": "tile", "type": "int", "value": 4},
                {"name": "description", "type": "string", "value": "Gestão e liderança"},
                {"name": "color", "type": "string", "value": "cinza"}
            ]
        },
        {
            "id": 5,
            "name": "Operações",
            "type": "department",
            "x": 384,  # 12 * 32
            "y": 224,  # 7 * 32
            "width": 384,  # 12 * 32
            "height": 416, # 13 * 32
            "visible": True,
            "properties": [
                {"name": "tile", "type": "int", "value": 5},
                {"name": "description", "type": "string", "value": "Operações e desenvolvimento"},
                {"name": "color", "type": "string", "value": "azul"}
            ]
        }
    ]
    
    # Estrutura do mapa
    map_data = {
        "type": "map",
        "version": "1.10",
        "tiledversion": "1.10.2",
        "orientation": "orthogonal",
        "renderorder": "right-down",
        "infinite": False,
        "width": width_tiles,
        "height": height_tiles,
        "tilewidth": tile_size,
        "tileheight": tile_size,
        "compressionlevel": -1,
        "nextlayerid": 6,
        "nextobjectid": 15,
        "properties": [
            {
                "name": "mapName",
                "type": "string",
                "value": "AR Online - Escritório Profissional"
            },
            {
                "name": "script",
                "type": "string",
                "value": "mapScript.js"
            }
        ],
        "tilesets": [
            {
                "firstgid": 1,
                "name": "WA_Room_Builder",
                "tilewidth": 32,
                "tileheight": 32,
                "tilecount": 1000,
                "columns": 25,
                "image": "tilesets/WA_Room_Builder.png",
                "imagewidth": 800,
                "imageheight": 1280
            },
            {
                "firstgid": 1001,
                "name": "tileset_colors_walls",
                "tilewidth": 32,
                "tileheight": 32,
                "tilecount": 10,
                "columns": 4,
                "image": "tilesets/tileset_colors_walls.png",
                "imagewidth": 128,
                "imageheight": 256
            }
        ],
        "layers": [
            {
                "id": 1,
                "name": "floor",
                "type": "tilelayer",
                "width": width_tiles,
                "height": height_tiles,
                "opacity": 1,
                "visible": True,
                "data": floor_data
            },
            {
                "id": 2,
                "name": "walls",
                "type": "tilelayer",
                "width": width_tiles,
                "height": height_tiles,
                "opacity": 1,
                "visible": True,
                "data": walls_data
            },
            {
                "id": 3,
                "name": "rooms",
                "type": "tilelayer",
                "width": width_tiles,
                "height": height_tiles,
                "opacity": 0.7,
                "visible": True,
                "data": rooms_data
            },
            {
                "id": 4,
                "name": "start",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": [spawn_point]
            },
            {
                "id": 5,
                "name": "zones",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": zones
            }
        ]
    }
    
    # Salvar como .tmj
    output_path = "wa_map-ar-online-professional.tmj"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    # Copiar para public também
    with open(f"public/{output_path}", 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Mapa profissional AR Online criado:")
    print(f"   📄 TMJ: {output_path} (raiz e public)")
    print(f"📊 Tamanho: {width_tiles}x{height_tiles} tiles")
    print(f"🏢 Layout: 4 áreas principais")
    print(f"   - Convivência & Eventos (superior)")
    print(f"   - Gestão & Liderança (esquerda)")
    print(f"   - Operações (direita)")
    print(f"   - Lobby AR ONLINE (centro)")
    print(f"🎯 Spawn: Centro do lobby")
    print(f"🎨 Tiles: 3=Convivência, 4=Gestão, 5=Operações, 6=Lobby")
    print(f"📐 Design: Baseado no layout profissional fornecido")
    
    return output_path

if __name__ == "__main__":
    create_ar_online_professional_map()
