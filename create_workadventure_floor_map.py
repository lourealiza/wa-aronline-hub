#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criar mapa usando floorLayer do WorkAdventure para divisões visuais
"""

import json
import os

def create_workadventure_floor_map():
    # Configurações do mapa
    width_tiles = 12
    height_tiles = 8
    tile_size = 32
    
    # Criar camada de piso base (tile 1 = chão padrão)
    floor_data = [1] * (width_tiles * height_tiles)
    
    # Criar floorLayer com tiles diferentes para cada sala
    floor_layer_data = [0] * (width_tiles * height_tiles)
    
    # Sala 1 - Lobby (tile 2) - canto superior esquerdo
    for y in range(0, 4):
        for x in range(0, 6):
            index = y * width_tiles + x
            floor_layer_data[index] = 2
    
    # Sala 2 - CEO (tile 3) - canto superior direito
    for y in range(0, 4):
        for x in range(6, 12):
            index = y * width_tiles + x
            floor_layer_data[index] = 3
    
    # Sala 3 - Marketing (tile 4) - canto inferior esquerdo
    for y in range(4, 8):
        for x in range(0, 6):
            index = y * width_tiles + x
            floor_layer_data[index] = 4
    
    # Sala 4 - Desenvolvimento (tile 5) - canto inferior direito
    for y in range(4, 8):
        for x in range(6, 12):
            index = y * width_tiles + x
            floor_layer_data[index] = 5
    
    # Criar spawn point no centro do lobby
    spawn_point = {
        "id": 1,
        "name": "spawn",
        "type": "spawn",
        "x": 80,  # Centro do lobby (2.5 * 32)
        "y": 48,  # Centro do lobby (1.5 * 32)
        "width": 32,
        "height": 32,
        "visible": True
    }
    
    # Criar zonas para interação
    zones = [
        {
            "id": 2,
            "name": "Lobby",
            "type": "common",
            "x": 0,    # 0 * 32
            "y": 0,    # 0 * 32
            "width": 192,  # 6 * 32
            "height": 128, # 4 * 32
            "visible": True,
            "properties": [
                {"name": "description", "type": "string", "value": "Lobby Central"}
            ]
        },
        {
            "id": 3,
            "name": "CEO",
            "type": "department",
            "x": 192,  # 6 * 32
            "y": 0,    # 0 * 32
            "width": 192,  # 6 * 32
            "height": 128, # 4 * 32
            "visible": True,
            "properties": [
                {"name": "description", "type": "string", "value": "Gabinete Executivo"}
            ]
        },
        {
            "id": 4,
            "name": "Marketing",
            "type": "department",
            "x": 0,    # 0 * 32
            "y": 128,  # 4 * 32
            "width": 192,  # 6 * 32
            "height": 128, # 4 * 32
            "visible": True,
            "properties": [
                {"name": "description", "type": "string", "value": "Marketing"}
            ]
        },
        {
            "id": 5,
            "name": "Desenvolvimento",
            "type": "department",
            "x": 192,  # 6 * 32
            "y": 128,  # 4 * 32
            "width": 192,  # 6 * 32
            "height": 128, # 4 * 32
            "visible": True,
            "properties": [
                {"name": "description", "type": "string", "value": "Desenvolvimento"}
            ]
        }
    ]
    
    # Estrutura do mapa usando convenções do WorkAdventure
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
        "nextobjectid": 10,
        "properties": [
            {
                "name": "mapName",
                "type": "string",
                "value": "AR Online - Mapa com FloorLayer"
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
                "name": "floorLayer",
                "type": "tilelayer",
                "width": width_tiles,
                "height": height_tiles,
                "opacity": 1,
                "visible": True,
                "data": floor_layer_data
            },
            {
                "id": 3,
                "name": "start",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": [spawn_point]
            },
            {
                "id": 4,
                "name": "zones",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": zones
            }
        ]
    }
    
    # Salvar como .tmj
    output_path = "wa_map-floor-layer.tmj"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    # Copiar para public também
    with open(f"public/{output_path}", 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Mapa com floorLayer criado:")
    print(f"   📄 TMJ: {output_path} (raiz e public)")
    print(f"📊 Tamanho: {width_tiles}x{height_tiles} tiles")
    print(f"🏠 Salas: 4 salas em grid 2x2")
    print(f"🎯 Spawn: Centro do lobby")
    print(f"🎨 FloorLayer: Tiles 2, 3, 4, 5 para cada sala")
    print(f"📐 Layout: Quadrantes bem definidos")
    
    return output_path

if __name__ == "__main__":
    create_workadventure_floor_map()
